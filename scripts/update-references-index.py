#!/usr/bin/env python3
"""
Regenerate the 'External references' section of index.md by scanning
references/*.md.

For each reference file, extracts:
- Title (from YAML front-matter `title:` field, or first `# ` heading)
- One-line description (from front-matter `description:` if set, else
  the first `> **...** ...` blockquote, else the first non-empty paragraph)

The output replaces everything between these markers in index.md:

    <!-- references:start -->
    ...
    <!-- references:end -->

Idempotent: re-running with no reference changes produces no diff.
"""

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES_DIR = REPO_ROOT / "references"
INDEX_FILE = REPO_ROOT / "index.md"

START_MARKER = "<!-- references:start -->"
END_MARKER = "<!-- references:end -->"


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    """Extract YAML front-matter dict and return (fm, body)."""
    fm: dict[str, str] = {}
    body = text
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            raw_fm = text[4:end]
            body = text[end + 5 :]
            for line in raw_fm.splitlines():
                if ":" in line:
                    k, _, v = line.partition(":")
                    fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def extract_title(fm: dict[str, str], body: str, fallback: str) -> str:
    if fm.get("title"):
        return fm["title"]
    m = re.search(r"^# (.+)$", body, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return fallback


def extract_description(fm: dict[str, str], body: str) -> str:
    """Try a sequence of strategies. Return a single-line plain string."""
    if fm.get("description"):
        return fm["description"]

    # Skip the H1 line and any back-links / blank lines, then take the
    # first blockquote line (often a 'Source:' or 'TL;DR' line) OR the
    # first non-empty paragraph.
    lines = body.splitlines()
    i = 0
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith("# ") or ln.startswith("[← ") or ln == "":
            i += 1
            continue
        # First blockquote — strip the leading '> ' and any **bold** markup
        if ln.startswith(">"):
            text = ln.lstrip("> ").strip()
            text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)  # drop bold
            text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)  # drop links
            return text[:240]
        # Otherwise first non-empty paragraph line
        text = re.sub(r"\*\*([^*]+)\*\*", r"\1", ln)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        return text[:240]
    return ""


def build_section() -> str:
    """Return the markdown content between the markers (exclusive)."""
    if not REFERENCES_DIR.exists():
        return "\n*(No references yet.)*\n"

    entries: list[str] = []
    for md_file in sorted(REFERENCES_DIR.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm, body = parse_front_matter(text)
        title = extract_title(fm, body, md_file.stem)
        desc = extract_description(fm, body)
        rel_path = f"references/{md_file.name}"
        line = f"- [{title}]({rel_path})"
        if desc:
            line += f" — {desc}"
        entries.append(line)

    if not entries:
        return "\n*(No references yet.)*\n"
    return "\n" + "\n".join(entries) + "\n"


def main() -> int:
    if not INDEX_FILE.exists():
        print(f"ERROR: {INDEX_FILE} not found", file=sys.stderr)
        return 2

    original = INDEX_FILE.read_text(encoding="utf-8")
    if START_MARKER not in original or END_MARKER not in original:
        print(
            f"ERROR: markers not found in index.md. "
            f"Add '{START_MARKER}' and '{END_MARKER}' around the references list.",
            file=sys.stderr,
        )
        return 3

    new_section = build_section()
    pattern = re.compile(
        re.escape(START_MARKER) + r"[\s\S]*?" + re.escape(END_MARKER),
        re.MULTILINE,
    )
    updated = pattern.sub(
        START_MARKER + new_section + END_MARKER,
        original,
    )

    if updated == original:
        print("index.md unchanged — no diff to write.")
        return 0

    INDEX_FILE.write_text(updated, encoding="utf-8")
    print("index.md updated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
