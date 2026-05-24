---
layout: default
title: Bonus — Brain/Hands/Loop Agent Build
---

# 🎁 Bonus exercise — Brain/Hands/Loop agent

[← Back to PLAN](PLAN.md) · [← Back to overview](index.md)

> **Slot:** end of Week 2 weekend (Day 14) or any rest-day buffer · **Time:** 90 min focused, optional extensions · **Status:** opt-in, not mandatory

---

## What this is

A hands-on build of the **Brain · Hands · Loop** architecture popularized by the [AI Accelerator's *Agent Architecture Build Guide*](https://www.skool.com/systems-to-scale-9517) — adapted for someone who already has the SDK-level chops you're building in Week 2.

The original Skool guide is excellent for first-timers. **You're not a first-timer.** So this exercise:

1. Uses the same mental model (Brain / Hands / Loop)
2. Uses the same loop library (Vercel AI SDK)
3. **Swaps the brain access layer**: skip OpenRouter, use your own `codex-oauth-client` + `gemini-codeassist-client` to pay through subscriptions instead of API keys
4. **Compares hand layers**: build the same agent twice — once with Zapier SDK (5 min), once with a small custom MCP server (1 hour) — to feel the trade-off you'll deep-dive in Week 3

End state: a working inbox triage agent in `~/inbox-agent/`, and a note documenting which hand-layer felt right for which job.

---

## Mental model recap

```text
┌──────────┐       ┌──────────┐       ┌──────────┐
│  BRAIN   │ ◄────►│   LOOP   │ ◄────►│  HANDS   │
│ the model│       │ your code│       │ the tools│
└──────────┘       └──────────┘       └──────────┘
```

| Piece | Standard Skool stack | Joseph-adapted stack |
|-------|---------------------|---------------------|
| Brain | OpenRouter (one key, ~5% markup, +100-300ms latency) | **Your own provider clients** (Claude via Anthropic API or `codex-oauth-client`/`gemini-codeassist-client` for subscription billing) |
| Hands | Zapier SDK (9000 apps, OAuth automated) | **Compare both**: Zapier SDK *and* a custom MCP server, decide which fits which use case |
| Loop | Vercel AI SDK (`ai@^6`) | Same — already the de-facto standard in `ggcoder` / `opencode` |

---

## Why bother if you already understand this

Two reasons:

1. **Synthesis.** You've read `ggcoder` source, you've read `opencode` source, you've built `codex-oauth-client` and `gemini-codeassist-client`. You know all the parts. But you haven't yet **assembled** them into one working agent end-to-end. This exercise is the assembly step.

2. **The Zapier-vs-MCP comparison is a real engineering decision.** When you ship something to a non-technical user, do you give them "connect via Zapier" or "install an MCP server"? You don't have a felt answer yet. After today you will.

---

## Pre-flight (5 min)

You'll need:
- Node 20+ (`node --version`)
- A working Gmail account (you have one)
- A Slack workspace where you can post (or substitute Discord webhook, see Variant B)
- Either: an Anthropic API key, *or* `~/.config/codex-oauth-client/credentials.json` from your own client

If Slack is friction, **just write to a local file or post via Discord webhook** — the architecture lesson is the same.

---

## Step 1 — Project scaffold (10 min)

```bash
mkdir ~/inbox-agent && cd ~/inbox-agent
npm init -y
npm pkg set type=module
npm install ai @ai-sdk/anthropic zod dotenv
npm install -D typescript tsx @types/node
echo ".env" >> .gitignore
echo "node_modules/" >> .gitignore
```

**Deliberate choice:** install `@ai-sdk/anthropic` directly, not `@openrouter/ai-sdk-provider`. This keeps you on direct Anthropic billing (or your own subscription path) — no middleman markup, no extra latency.

If you want to swap models later, you'll add `@ai-sdk/openai`, `@ai-sdk/google`, etc. alongside it — one line per provider, like the Skool guide promises, but without OpenRouter.

---

## Step 2 — Hands variant A: Zapier SDK (30 min)

Follow the Skool guide pages 7-8 verbatim for connecting Gmail + Slack in Zapier and installing `@zapier/zapier-sdk`. Time-box yourself: **30 minutes max.** If OAuth balks, switch to Variant B.

The point of this variant: feel how fast you go from zero to "production-grade OAuth handled for me".

---

## Step 3 — Loop (30 min)

Use **Claude Code itself** to write `agent.ts`. Paste the prompt from page 9 of the Skool guide, but with these substitutions:

```text
- Provider: anthropic (not openrouter)
- Default model: anthropic("claude-opus-4-7")    // or claude-sonnet-4-7 for cost
- Drop the OpenRouter import; use the direct Anthropic provider
- TASK: read my last 20 unread emails, decide what needs
  attention vs noise, post a 3-line takeaway to local file
  inbox-digest.md (or Slack if Zapier is connected)
```

Run:

```bash
npx tsx agent.ts
```

You should see tool calls fire and a digest land. Total time from `mkdir` to digest: **< 1 hour** if Zapier OAuth cooperates.

---

## Step 4 — Hands variant B: custom MCP server (60 min, optional)

Now do it again with your own MCP server replacing Zapier.

Scaffold a tiny MCP server that exposes the same two tools:

```bash
mkdir ~/inbox-agent/mcp-mail && cd ~/inbox-agent/mcp-mail
npm init -y && npm pkg set type=module
npm install @modelcontextprotocol/sdk googleapis
```

Implement two MCP tools:
- `read_recent_emails(query)` — uses Gmail API via `googleapis` and your OAuth creds
- `send_digest(text)` — writes to local file or POSTs Discord/Slack webhook

Point your `agent.ts` at this MCP server instead of Zapier:
- Use Vercel AI SDK's MCP client (`experimental_createMCPClient` or equivalent)
- All other code stays identical — that's the architectural point

This is the lighter, code-owned alternative to Zapier. It's what you'd actually ship to other devs.

---

## Step 5 — Decision log (15 min)

In `~/inbox-agent/REFLECTION.md`, answer four questions:

```markdown
# Inbox agent reflection — YYYY-MM-DD

## 1. Which hand layer felt better for personal use?
(Zapier SDK or custom MCP — why?)

## 2. Which would you ship to a non-technical friend?
(Same answer? Different? Why?)

## 3. Where did the "one-line brain swap" claim hold up?
(Did it actually work cleanly when you swapped Claude → GPT/Gemini? Any surprises?)

## 4. What's worth pulling into codex-oauth-client / gemini-codeassist-client?
(Now that you've used Vercel AI SDK in real anger — what patterns would you back-port?)
```

This decision log is the **actual deliverable** of this bonus day. Push it to the plan repo:

```bash
mkdir -p artifacts/bonus
cp ~/inbox-agent/REFLECTION.md artifacts/bonus/inbox-agent-reflection.md
git add artifacts/bonus/inbox-agent-reflection.md
git commit -m "bonus: inbox agent build + reflection"
git push
```

---

## Why this slots between Week 2 and Week 3

| | Week 2 (API depth) | **Bonus** | Week 3 (MCP) |
|---|---|---|---|
| Focus | Direct API mastery (one provider) | **Compose: brain + hands + loop into one agent** | Build a real MCP server you publish |
| Hands layer | (not yet) | **Zapier SDK + tiny MCP comparison** | Full MCP intro/advanced curriculum |
| Outcome | `claude-provider` branch | **Working agent + decision log** | Published `mcp-<topic>` repo |

The bonus is the "Aha, that's why MCP matters" moment **before** Week 3's curriculum lands. It primes Week 3.

---

## Things I want you to notice (Senior-engineer eyes only)

1. **Vercel AI SDK's `stepCountIs(15)` stop condition is a leaky abstraction** — when does it stop? After 15 model calls? 15 tool calls? Both? Read the source.

2. **Tool call format is not actually universal.** Try sending the same `tools` array to Claude vs GPT-5 vs Gemini and watch the wire serialization differ. The SDK abstracts it, but **reasoning vs. content vs. parallel-tool-call semantics** still leak through in real apps.

3. **OpenRouter's 5% markup is real** but the bigger cost is latency. Time a Claude-direct call vs. Claude-via-OpenRouter on the same prompt — note the gap.

4. **The 50-line claim** is true if you accept the libraries' defaults. Add cancel + retry + observability + cost tracking and you're at 200+. The Skool guide doesn't lie, it just defines "agent" generously.

---

## Hard stop rules

- **90 min focused time max** for variant A (Zapier path). Variant B is optional extension.
- **Don't rewrite `codex-oauth-client` or `gemini-codeassist-client`** for this exercise. They're production code. This is a playground.
- **Don't commit your OpenRouter / Anthropic / Slack tokens.** Use `.env`, double-check `git status` before push.

---

[← Back to PLAN](PLAN.md) · [← Back to overview](index.md)
