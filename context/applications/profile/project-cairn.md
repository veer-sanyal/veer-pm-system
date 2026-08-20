---
name: user-project-cairn
description: "Cairn — Veer's open-source Claude Code plugin that scaffolds long-lived agentic systems around PM fundamentals (North Star metric, metric tree, guardrails). Public repo with one verified unprompted external adopter. Use as second project for AI-agent / agent-infrastructure / technical-PM roles."
metadata:
  node_type: memory
  type: user
---

> **CURRENCY NOTE.** Facts verified 2026-08-20 against the public repo (`veer-sanyal/cairn`,
> 140 commits, last commit 2026-08-07) and `ledgers.md` (Neal adoption verified 2026-07-29).
> Re-verify commit count / adopter status before reuse.

**Cairn — Open-Source Scaffolder for Agentic AI Systems** — 2026
*Public: github.com/veer-sanyal/cairn · Claude Code plugin, sole author*

**What it is:** A plugin that interviews the user and scaffolds a personalized, long-lived
agentic system for any goal. Before building, it decomposes the goal PM-style: North Star
metric, input-lever metric tree, maximize/minimize framing, guardrail metrics with hard
limits. Then it designs within known agentic-engineering constraints (context rot, tiered
externalized memory, when to fan out subagents, deterministic enforcement over prose).

**Real components (all in the public repo):**
- A 25-principle, evidence-graded "level-zero doctrine" of agentic-system failure modes
  (context rot, objective corruption under optimization, knowledge expiry, human boundary).
- A vendored deep-research engine that manufactures domain knowledge at build time, with
  adversarial claim verification (3-vote).
- An environment census (tools/connectors/models available on the machine).
- Commands: build (interview-driven scaffold), audit (diagnose an existing agentic setup
  against the doctrine), review (validator + memory consolidation + telemetry-cited
  proposals), research, list, upgrade. Python test suite included.

**Traction (n=1, phrase carefully):** ONE unprompted external adopter — used it without
being asked, gave product feedback (README jargon), praised the onboarding interview, then
forked it into his own public repo and extended it well past the original (job scraper on a
cron, resume-rating HQ). Verified by direct GitHub read 2026-07-29. Say "adopted unprompted
by an external builder who forked and extended it" — never "users", never a count.

**Headline proof bullets (defensible, quizzable):**
- Built and open-sourced a plugin that designs long-lived agentic systems around product
  fundamentals — it interviews the user to define a North Star metric, metric tree, and
  guardrails, then scaffolds a personalized multi-agent system with tiered memory, local
  telemetry, and human-gated self-improvement.
- Encoded 25 evidence-graded principles on agentic-system failure modes (context rot,
  objective corruption, knowledge expiry) with a bundled research engine using adversarial
  claim verification; adopted unprompted by an external builder who forked and extended it.

**Would be INFLATION (never claim):** "users" plural or any adoption count beyond the one
verified fork; GitHub stars/downloads (unverified); "production"; that Veer's own private
planning system is a Cairn instance (it is not, and the private repo is never referenced
in application materials).

**Tailoring notes:** Lead with it (or pair tightly with [[user-project-stick]]) for AI-agent
PM, agent-infrastructure, and agent-tooling roles — it is the single most on-topic artifact
for "hands-on agent building + PM thinking". First used: TikTok AI Agent PM Intern resume,
2026-08-20.
