---
layout: default
title: Daily Plan
---

# 📅 The 28-day daily plan

[← Back to overview](index.md)

**Start date:** Monday, 2026-05-25 · **End date:** Sunday, 2026-06-21

> **Self-tracking:** as you finish a day, change `- [ ]` to `- [x]` in this file, commit, push.

---

## Week 1 — Foundations
*May 25–31, 2026 · ~7 hours · Goal: master your daily Claude Code workflow & build conceptual scaffolding*

### Day 1 · Mon · 2026-05-25 · 60 min
- [ ] **Claude 101** (speed-run, 30 min) — confirm there's nothing subtle you missed
- [ ] **Claude Code 101** — part 1 (30 min): installation, auth, first session

**Exercise:** open `~/.claude/CLAUDE.md` and inventory what you have there.

### Day 2 · Tue · 2026-05-26 · 60 min
- [ ] **Claude Code 101** — part 2 (60 min): hooks, slash commands, settings.json

**Exercise:** add **one** slash command to `~/.claude/commands/` that you'll actually use this week.

### Day 3 · Wed · 2026-05-27 · 60 min
- [ ] **Claude Code in Action** — part 1 (60 min): real workflow integration

**Exercise:** identify **one** repetitive task you did this week and write 1-sentence prompt template for it.

### Day 4 · Thu · 2026-05-28 · 60 min
- [ ] **Claude Code in Action** — part 2 (60 min): advanced patterns

**Exercise:** configure `.claude/settings.local.json` for one repo you actively work on (Nike or one of your OSS projects).

### Day 5 · Fri · 2026-05-29 · 60 min
- [ ] **Introduction to Claude Cowork** (60 min)

**Exercise:** try Cowork on **one** real file from your `joseph-chen-resume` repo and note what felt different from Claude Code.

### Day 6 · Sat · 2026-05-30 · 90 min
- [ ] **AI Capabilities and Limitations** (60 min)
- [ ] **Week 1 deliverable** (30 min): write `artifacts/week1/daily-workflow.md` documenting your current Claude Code setup

### Day 7 · Sun · 2026-05-31 · 60 min
- [ ] Buffer: review the week's exercises, polish `daily-workflow.md`, commit to this repo

**🎯 Week 1 checkpoint:** `daily-workflow.md` is in `artifacts/week1/` of this repo with at least: your slash commands, hooks, key settings, and 3 prompt templates.

---

## Week 2 — API Depth
*Jun 1–7, 2026 · ~7 hours · Goal: deep understanding of the Claude API, applied to your existing SDK work*

### Day 8 · Mon · 2026-06-01 · 60 min
- [ ] **Building with the Claude API** — Part 1 (60 min): basics, messages, system prompts

**Exercise:** in [codex-oauth-client](https://github.com/Joseph19820124/codex-oauth-client), check if your error handling matches Anthropic's recommendations.

### Day 9 · Tue · 2026-06-02 · 60 min
- [ ] **Building with the Claude API** — Part 2 (60 min): tool use, streaming

**Exercise:** sketch how a `claude-oauth-client` (sibling to `codex-oauth-client`) would handle tool calling differently from OpenAI's API.

### Day 10 · Wed · 2026-06-03 · 60 min
- [ ] **Building with the Claude API** — Part 3 (60 min): prompt caching, batch API, files

**Exercise:** in [gemini-codeassist-client](https://github.com/Joseph19820124/gemini-codeassist-client), add a comment noting which features Anthropic has equivalents for.

### Day 11 · Thu · 2026-06-04 · 60 min
- [ ] **AI Fluency: Framework & Foundations** (60 min) — speed-run; you mostly know this but the framework vocabulary is useful

**Exercise:** write down the 4 AI Fluency principles in your own words.

### Day 12 · Fri · 2026-06-05 · 60 min
- [ ] **Hands-on capstone for Week 2** (60 min): start a `claude-provider` branch on `codex-oauth-client`

**Exercise:** scaffold the file structure (`src/claude/`, types, OAuth provider stub).

### Day 13 · Sat · 2026-06-06 · 90 min
- [ ] **Continue `claude-provider`** (90 min): implement the API client + streaming

**Deliverable:** a working `claude-provider` branch that can stream a Claude response.

### Day 14 · Sun · 2026-06-07 · 60 min
- [ ] Buffer: tests for `claude-provider` branch, open a PR draft
- [ ] **(Optional, 90 min)** **Bonus build:** Brain/Hands/Loop inbox agent — see [BONUS_AGENT_BUILD.md](BONUS_AGENT_BUILD.md)

**🎯 Week 2 checkpoint:** `claude-provider` branch on `codex-oauth-client` exists with streaming + tests + draft PR linking back to this plan.

> 💡 **The bonus is opt-in but recommended** — it's the Week 2→Week 3 bridge that gives you the "why MCP matters" intuition before Week 3's curriculum lands. Skip only if Week 2 deliverable ran over.

---

## Week 3 — Protocols (MCP + Bedrock)
*Jun 8–14, 2026 · ~9 hours · Goal: ship a real, original MCP server*

### Day 15 · Mon · 2026-06-08 · 60 min
- [ ] **Introduction to Model Context Protocol** — Part 1 (60 min): architecture, three primitives

**Exercise:** sketch which MCP primitives your daily work would benefit from (tools? resources? prompts?).

### Day 16 · Tue · 2026-06-09 · 60 min
- [ ] **Introduction to MCP** — Part 2 (60 min): Python implementation

**Exercise:** clone the official MCP Python quickstart and run it locally.

### Day 17 · Wed · 2026-06-10 · 60 min
- [ ] **Introduction to MCP** — Part 3 (60 min): build a tiny tool/resource

**Exercise:** scaffold `mcp-<your-topic>` repo (suggestion: an MCP server that exposes your `joseph-chen-resume` or `medical-records` repo as resources for Claude).

### Day 18 · Thu · 2026-06-11 · 60 min
- [ ] **MCP: Advanced Topics** — Part 1 (60 min): sampling + notifications

**Exercise:** add one advanced feature to your MCP server (e.g. a notification when a new entry is added).

### Day 19 · Fri · 2026-06-12 · 60 min
- [ ] **MCP: Advanced Topics** — Part 2 (60 min): file system access, transport mechanisms

**Exercise:** add file system primitives to your MCP server.

### Day 20 · Sat · 2026-06-13 · 90 min
- [ ] **Claude with Amazon Bedrock** (90 min, speed-run since you're AWS Pro)

**Exercise:** in your AWS account (aws-7 or aws-8), do `aws bedrock list-foundation-models` and identify which Claude models are available in your region.

### Day 21 · Sun · 2026-06-14 · 90 min
- [ ] Final polish of MCP server: README, install instructions, integration with Claude Code

**🎯 Week 3 checkpoint:** `mcp-<topic>` repo is public, installable via `claude mcp add`, with README and at least 2 tools + 1 resource. Push to GitHub.

---

## Week 4 — Agentic + Capstone
*Jun 15–21, 2026 · ~7 hours · Goal: weave skills + subagents + MCP into a real project*

### Day 22 · Mon · 2026-06-15 · 60 min
- [ ] **Introduction to agent skills** (60 min)

**Exercise:** identify **one** repeatable task in your current work that should become a Claude Code skill.

### Day 23 · Tue · 2026-06-16 · 60 min
- [ ] **Build a custom skill** (60 min) — apply yesterday's lesson

**Deliverable:** a `~/.claude/skills/<your-skill>/SKILL.md` that you actually use.

### Day 24 · Wed · 2026-06-17 · 60 min
- [ ] **Introduction to subagents** (60 min)

**Exercise:** sketch a subagent specialized for one role you regularly delegate (e.g. "git-history-archaeologist" or "aws-cost-auditor").

### Day 25 · Thu · 2026-06-18 · 60 min
- [ ] **Build a custom subagent** (60 min) — apply yesterday's design

**Deliverable:** a `~/.claude/agents/<your-subagent>.md` that you can `@invoke`.

### Day 26 · Fri · 2026-06-19 · 90 min
- [ ] **Capstone Day 1** (90 min): combine all three (MCP server + skill + subagent) into ONE real workflow

Goal: e.g. "When I ask my AWS-Cost-Auditor subagent a question, it uses my Bedrock MCP server's tools, applies my AWS-architecture skill, and produces a Markdown report."

### Day 27 · Sat · 2026-06-20 · 90 min
- [ ] **Capstone Day 2** (90 min): polish + write up

**Deliverable:** a blog-style write-up `artifacts/week4/capstone.md` describing what you built, what surprised you, and what you'd improve.

### Day 28 · Sun · 2026-06-21 · 60 min
- [ ] **Final review** (60 min): re-read PLAN.md, count checkboxes, post your capstone link on LinkedIn / Discord communities

**🎯 Final checkpoint:** capstone write-up is public, all 28 checkboxes ticked, and you have **4 new public artifacts** (week1 doc, claude-provider branch, MCP server repo, capstone writeup).

---

## Buffer rules

- **One missed weekday** = compensate by adding 30 min to weekend
- **More than 2 missed days** = re-baseline; shift remaining days by N days, push the new dates here
- **Capstone (Day 26-27) is sacred** — protect those slots aggressively

---

[← Back to overview](index.md)
