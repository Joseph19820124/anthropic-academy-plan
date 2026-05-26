---
layout: default
title: Anthropic Academy Plan
---

# Joseph's Anthropic Academy Plan

A **strict 4-week, ~30-hour** study plan covering [Anthropic Academy](https://anthropic.skilljar.com/)'s 18 courses, tailored for a senior cloud / backend engineer who already builds with the Claude API daily.

> **The deal I made with myself:** finish a course block, tick a checkbox in this repo, push the commit. No checkbox, no progress.

---

## TL;DR — at a glance

| Week | Focus | Hours | Outcome |
|------|-------|-------|---------|
| **1** | Foundations: Claude Code + Cowork + capabilities | ~7h | Daily-workflow mastery; conceptual scaffolding |
| **2** | API depth: Building with Claude API + AI Fluency | ~7h | Refactor `codex-oauth-client` to add a Claude provider as practical exercise |
| **3** | Protocols: MCP intro + advanced + Bedrock | ~9h | Ship a real custom MCP server (committed to GitHub) |
| **4** | Agentic: skills + subagents + capstone | ~7h | Custom skill + custom subagent integrated into daily Claude Code use |

**Total: 30 hours over 28 days.** Weekday slots 60 min, weekend slots 90 min.

---

## How this plan was personalized

Anthropic Academy has 18 courses spanning beginner→advanced and business→technical. To avoid wasting your time, I split them by your existing background:

### 🏃 Speed-run (review-level, single 30-60 min session each)

You already know this material — you're confirming you didn't miss anything subtle:

- **Claude 101** — basic Claude.ai usage
- **Claude with Amazon Bedrock** — you're an AWS Pro architect
- **AI Capabilities and Limitations** — conceptual primer
- **AI Fluency: Framework & Foundations** — collaboration concepts

### 🔬 Deep-dive (multiple sessions, hands-on)

These directly map to what you build today (SDKs, agents, MCP integrations):

- **Claude Code 101 + In Action** — formal coverage of features you currently use ad-hoc
- **Building with the Claude API** — comprehensive, will inform your TypeScript SDK work
- **Introduction to MCP + Advanced Topics** — directly relevant to OpenAB / ggcoder / opencode work
- **Introduction to agent skills** — Claude Code's skill system
- **Introduction to subagents** — context-management patterns
- **Introduction to Claude Cowork** — newer feature, worth structured intro

### ⏭ Skip entirely

Not your target audience — these aren't worth your time:

- AI Fluency for educators / students / nonprofits / Small Businesses / Teaching AI Fluency
- Claude with Google Cloud's Vertex AI (you don't deploy on GCP)

---

## The 4-week schedule

→ See **[the full daily plan](PLAN.md)** for the complete day-by-day breakdown.

### Quick week index
- [Week 1: Foundations](PLAN.md#week-1--foundations) — May 25–31, 2026
- [Week 2: API depth](PLAN.md#week-2--api-depth) — Jun 1–7, 2026
- 🎁 [Bonus: Brain/Hands/Loop agent build](BONUS_AGENT_BUILD.md) — opt-in, Week 2→3 bridge
- [Week 3: Protocols (MCP + Bedrock)](PLAN.md#week-3--protocols-mcp--bedrock) — Jun 8–14, 2026
- [Week 4: Agentic + capstone](PLAN.md#week-4--agentic--capstone) — Jun 15–21, 2026

### 📚 External references
- [Ken Kai's autoblogger build demo (2026-05-25)](references/kenkai-blog-build-2026-05-25.md) — Skool community live demo by the ggcoder maintainer; transferable prompt-template + 5 prompting principles + "simulate at scale" mindset

---

## How to use this repo

1. **Open [PLAN.md](PLAN.md)** every morning, find today's row.
2. **Block the slot** in your calendar (60 min weekdays, 90 min weekends).
3. **Complete the lesson + exercise.**
4. **Tick the checkbox** in PLAN.md, commit, push:
   ```bash
   git -c user.email="<you>" commit -am "day N done: <course>"
   git push
   ```
5. The commit graph **is** your progress dashboard.

---

## Hard rules

| Rule | Why |
|------|-----|
| No checkbox until the lesson is actually completed (no skim-and-check) | Self-honesty is the only thing this plan enforces |
| Weekend can compensate for one missed weekday max | Buffer prevents collapse from a single bad day |
| If you skip more than 2 days, re-baseline (shift the whole plan) | Don't let guilt accumulate |
| Capstone (week 4 last 3 days) is non-negotiable | Synthesis is where the actual learning lands |
| All hands-on exercises commit to a public repo | Forces real artifacts, not just "I watched the video" |

---

## Tracking deliverables

Each week produces **one shippable artifact**:

| Week | Deliverable | Where |
|------|-------------|-------|
| 1 | A `daily-workflow.md` documenting your Claude Code setup | this repo, `artifacts/week1/` |
| 2 | `claude-provider` branch on [codex-oauth-client](https://github.com/Joseph19820124/codex-oauth-client) | external |
| 3 | A custom MCP server in its own public repo | new repo `mcp-<topic>` |
| 4 | A custom skill + subagent committed to your day-to-day repo | external |

---

## Resources

- [Anthropic Academy (Skilljar)](https://anthropic.skilljar.com/) — the courses
- [Claude Code docs](https://code.claude.com/docs) — reference
- [MCP spec](https://modelcontextprotocol.io) — for week 3
- [Claude API docs](https://docs.claude.com/en/api) — for week 2

---

*This plan was generated 2026-05-24 and personalized based on existing skill profile. Adjust as needed — the schedule is calendar dates, not contract dates.*
