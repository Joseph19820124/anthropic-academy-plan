---
layout: default
title: Reference — Ken Kai blog-build demo (2026-05-25)
---

# Ken Kai — autoblogger build demo (2026-05-25)

[← Back to overview](../index.md) · [← Back to PLAN](../PLAN.md)

> **Source:** [Fathom recording](https://fathom.video/share/-EfFkeVsh9RS5cwBnotSyjB65Q47msaG) · 126 min · hosted in The AI Accelerator Skool community.
>
> **Host:** Ken Kai (`buzzbeamaustralia@gmail.com`) — maintainer of [`KenKaiii/gg-framework`](https://github.com/KenKaiii/gg-framework) (ggcoder / gg-boss / gg-voice).
>
> **Why it matters here:** the host walked through, end-to-end, how he uses an agentic coding workflow to bootstrap a new project from nothing. This is the same author whose source code is referenced across Week 2 and Week 3 of the plan, and the demo overlaps directly with the daily techniques the plan teaches. This doc captures the **transferable patterns** so future me doesn't have to re-watch 126 minutes.

---

## TL;DR

Five patterns are worth lifting from this session, in order of leverage:

1. **The research-prompt template** (force date, force "free", force broad relevance)
2. **The init → CLAUDE.md → commit cycle** for every new project
3. **Five prompting principles** that contradict popular advice
4. **The `.gitignore` patterns** for agent artifacts
5. **The "simulate at scale" story** — the single biggest mindset shift in the call

Each is below with the verbatim language and how it maps to the academy plan.

---

## 1. The research-prompt template

Drop into a fresh project, before writing any code:

```
Research. This will be a <one-line app description>.

Based off of this, we will need things such as <one or two
obvious requirements> and anything relevant to an app like this.

It is now 2026 in May.

Try to find anything relevant which is free.
Packages, dependencies, whatever relevant.
```

### Why each line exists (his explanation, paraphrased)

| Line | Reason |
|------|--------|
| *"It is now 2026 in May"* | Models drift back to 2024/2025 training data even when system-injected date is correct. Saying it explicitly in the prompt overrides that drift. |
| *"find anything relevant which is free"* | LLMs default to recommending paid SaaS (vendor bias from training data). Without this, you get Vercel Pro, Contentful, etc. |
| *"anything relevant to an app like this"* — not just "find a CMS" | Forces broader search. The agent will surface dependencies (code-quality tools, fonts, analytics) you'd have forgotten to ask for. |
| *No PRD, no detailed spec* | "I know some people stuck for a day just optimizing a PRD file. We could have just jumped in." |

**Maps to:** Week 2, Day 8–10 of the plan ("Building with the Claude API"). When working through tool-call exercises, use this template instead of hand-written prompts.

---

## 2. The init → CLAUDE.md → commit cycle

Every new project follows the same skeleton:

```bash
mkdir <project-name> && cd <project-name>
# 1. Run the agent's `init` (Claude Code: /init; ggcoder: similar) to generate
#    CLAUDE.md from a brief description of the project.
# 2. Give the agent a paragraph of context: "This is an automatic blogging
#    web app using <stack>. Utilize coding agents to create blogs, etc."
# 3. Let the agent spawn subagents to populate CLAUDE.md and produce the
#    initial scaffold.
# 4. .gitignore the agent's own artifacts (see § 4).
# 5. Commit + push immediately, before writing any feature code.
```

**Key insight (his words):** *"CLAUDE.md is something you should be updating as well. When the agent loves to use the iPhone simulator and we want it to use the device, add to CLAUDE.md: 'when starting the dev server, start it on the device, device ID is X.' Now on next session it's launching it on your phone, not the simulator."*

**Maps to:** Week 1, Day 4 — currently the exercise is "configure `.claude/settings.local.json`". Upgrade to: configure **+** populate a project CLAUDE.md from this template.

---

## 3. Five prompting principles (contradict popular advice)

| # | Principle | Quote |
|---|-----------|-------|
| 1 | **Imperfect English is fine** | *"You don't have to talk like a caveman, but it doesn't have to be perfect English. LLMs are very capable of understanding what we mean."* |
| 2 | **Don't over-optimize PRDs** | *"Some people are stuck on the first thing for the next day, just optimizing a PRD file, just to build something as simple as this. We could have jumped into it right now."* |
| 3 | **Don't justify yourself to the LLM** | *(Mario Funez in the call:)* *"I try to be as concise as possible — some people justify themselves to the LLM and it's just noise. It doesn't need your explanation. You only need to command it."* |
| 4 | **Update CLAUDE.md continuously** | *"As we're building, the agent loves to use the iPhone simulator. We add 'use the device, device ID is X' to CLAUDE.md. Now on a new session it knows."* |
| 5 | **Reasoning tokens aren't for you** | *"If you look at the thinking deltas from GPT models, they remove filler words because that's not for you to read. It's reasoning with itself. People complain 'it doesn't make sense' — because it's not supposed to."* |

**Maps to:** general; especially Week 1 (Claude Code daily workflow) and Week 2 (API depth). Pin these to the top of any prompt-writing reflexes.

---

## 4. Agent-artifact `.gitignore` pattern

Add to `.gitignore` of any project where you use ggcoder or Claude Code:

```gitignore
# Agent artifacts (keep local, never commit)
.gg
.gg/commands
agents.md
# Plus the usual:
.env
node_modules/
```

**Reason (paraphrased):** files like `agents.md`, `.gg/`, slash-command definitions can leak API keys, internal prompts, or sensitive workflows when pushed to a public repo. Default to hiding them.

**Note for Claude Code specifically:** you may want to **commit** `CLAUDE.md` (it's project knowledge meant to be shared) and **ignore** `.claude/settings.local.json` (it's personal). Adjust the .gitignore accordingly.

---

## 5. The "simulate at scale" story (most senior-relevant content)

Verbatim summary of the closing 5 minutes:

> *"I got this client. Took over a developer team — 5 guys, working with him for 10 months. They were optimizing agents — building agents, doing this, doing that. For 6 months in full optimization, just optimizing prompts to get the right output they want."*
>
> *"It's crucial because it's a sensitive business niche — if it went out of those guardrails, it could result in bans, destruction of his business."*
>
> *"What do I do? Simulate it. Thousands upon thousands upon thousands of iterations. Yes, it cost money — I'm not saying $5 grand, I'm talking like $50. In an hour, right? Thousands upon thousands. And these other idiots are sending prompts manually — 'oh, what's the response back, oh I've got to change the system instructions' — but six months, you know?"*
>
> *"Which one do I trust more? Five guys talking. Or the new guy who's running 500 prompts today back and forth, all based on a rubric scoring system. Improving guardrails, system refinements, across the board, based on personas — marital status, kids, angry, depressed, all these different personas. Simulated. Boom."*
>
> *"Client over the moon, man. 'My God, what have I been doing for the last 10 months?'"*

### The single takeaway

> **"Programmatic > manual. But to make it programmatic, you have to know how to do it manually first."**

### Why this matters for the academy plan

Week 2 (API depth) and Week 4 (capstone) both push the user toward shippable artifacts, not just "I watched the video." This story is the philosophical justification: don't iterate prompts by hand — write a rubric, write a simulator, run thousands of iterations cheaply. The tests in `codex-oauth-client` are a baby version of this; the academy capstone should pull the pattern further into agent-level evaluation.

---

## Tech-stack picks discovered in the demo

For a blog-style web app (might be useful for the eventual capstone):

| Pick | Status in demo |
|------|---------------|
| **Tailwind Next.js Starter Blog** | "for most of you, this is already pretty decent" |
| **Codebox (Next.js variant)** | Final pick ✅ |
| Astrowind | Astro-based, backup |
| Lottie | "not the biggest fan" |
| Ollama | Model recommended it, **but wrong choice** — Ken uses ggcoder / Codex / Claude Code, not local Ollama |

---

## Cross-references

- This author's package: [`gg-voice`](https://github.com/KenKaiii/gg-framework/tree/main/packages/gg-voice) — referenced at end of call ("voice agent phone app… everyone should have this on the phone")
- This author's main framework: [`KenKaiii/gg-framework`](https://github.com/KenKaiii/gg-framework) — ggcoder, gg-boss, gg-voice, gg-editor
- Related notes in this repo:
  - [ACP_METHODS.md (sibling repo)](https://github.com/Joseph19820124/openab-http-agent-rfc/blob/main/ACP_METHODS.md) — protocol-level view of what these agents do over the wire
  - [BONUS_AGENT_BUILD.md](../BONUS_AGENT_BUILD.md) — the Day 14 build that applies many of these patterns

---

[← Back to overview](../index.md) · [← Back to PLAN](../PLAN.md)
