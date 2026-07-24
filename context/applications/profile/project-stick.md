---
name: user-project-stick
description: "STICK — Veer's CURRENT independent product build (Pillar 1). Deployed AI study app: turns course material into a daily exam-aware spaced-retrieval plan via bounded LLM steps. Use as headline project for AI/ML, product, and technical-PM roles. Replaced StudyFlowForge as the active build."
metadata:
  node_type: memory
  type: user
---

> **CURRENCY NOTE.** STICK is the live Pillar-1 product and its build state moves constantly. The authoritative source is `~/Desktop/stick-dev/STATE.md` (never mirrored into this repo). The numbers below are a point-in-time honest snapshot (last refreshed 2026-07-23) — re-verify against STATE.md before putting a fresh metric on a resume. STICK is a **from-scratch rebuild, not a rename of StudyFlowForge** (no code reused; see [[user-project-studyflowforge]], now a superseded past project).

**STICK** — Independent product build (Pillar 1) — 2026 – Present
*Subtitles that fit: "AI-Powered Study Platform", "AI Study App (deployed)", "Independent Product Build"*

**What it is:** A web app that turns admin-curated course material into a single daily, exam-aware spaced-retrieval practice plan for university students. Uses **bounded AI** (extract, grade, hint, generate) — not an open chatbot. Piloting as a deep single-course build at Purdue.

**Stack (real, in use):** React 18 + TypeScript + Vite, TailwindCSS v4; Supabase (Postgres + Auth + Storage + Deno Edge Functions); `ts-fsrs` (FSRS spaced-repetition scheduling); `pdfjs-dist` (exam PDF rendering); an LLM extraction pipeline. Deployed on Vercel. Tools: Git/GitHub, Claude Code (AI-assisted development).

**Role:** Sole builder — problem definition, data model, LLM pipeline, and app end-to-end.

**Honest stage (do not overstate):** Deployed dev build, **single-admin dogfooding** (Veer as admin is currently the only user). Purdue student pilot is pre-launch — **zero students yet, no retention/mastery/outcome data**.

**Headline proof bullets (defensible, quizzable):**
- Building STICK end-to-end as sole developer: a deployed web app (React/TypeScript + Supabase) that converts course material into a daily, exam-aware spaced-retrieval study plan using bounded LLM steps rather than an open chatbot.
- Designed and shipped an LLM extraction pipeline (Deno edge functions) that ingested a real 14-page exam into structured questions and auto-proposed 11 of 12 answer keys at ~35¢ end-to-end (n=1 dogfooding run).
- Designed the Postgres data model and data-access security: 11 migrations and 27 row-level-security policies, verified by a 62/62 RLS probe suite.
- Wired an FSRS spaced-repetition scheduler (`ts-fsrs`) to per-question correctness to generate each day's practice queue; built a 6-page app (auth, enroll, plan, player, admin).
- Defined the product strategy — bounded, admin-curated AI over an open chatbot — and scoped a single-course Purdue pilot as the first real-user test.

**Skills demonstrated:** product strategy/scoping, LLM pipeline design + prompt/step design, data modeling (Postgres), row-level-security / data-access design, React/TypeScript (built-with), Supabase/Deno edge functions (built-with), FSRS/spaced-repetition, AI-assisted development (Claude Code).

**Would be INFLATION (never claim at current stage):** "piloted with students" / "users" (zero students); any retention/mastery/engagement outcome numbers; "18 screens" or "operational dashboards" (that was StudyFlowForge, not STICK); extraction accuracy as a *measured rate* (single exam, n=1); calling it "production" (it is a dev deployment).

**Tailoring notes:**
- AI/ML/technical-PM: lead with the LLM extraction pipeline + bounded-AI product decision + data model.
- Product/PM: lead with product strategy (bounded vs. chatbot) + single-course pilot framing + end-to-end ownership.
- SWE/full-stack: lead with the edge-function pipeline + Postgres/RLS + FSRS integration.
- Always re-check STATE.md for current numbers before use.
