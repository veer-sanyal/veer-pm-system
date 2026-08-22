---
name: user-project-stick
description: "STICK — Veer's CURRENT independent product build (Pillar 1). Deployed AI study app: turns course material into a daily exam-aware spaced-retrieval plan via bounded LLM steps. Use as headline project for AI/ML, product, and technical-PM roles. Replaced StudyFlowForge as the active build."
metadata:
  node_type: memory
  type: user
---

> **CURRENCY NOTE.** STICK is the live Pillar-1 product and its build state moves constantly. The authoritative source is `~/Desktop/stick-dev/STATE.md` (never mirrored into this repo). The numbers below are a point-in-time honest snapshot (last refreshed **2026-08-21**) — re-verify against STATE.md before putting a fresh metric on a resume. STICK is a **from-scratch rebuild, not a rename of StudyFlowForge** (no code reused; see [[user-project-studyflowforge]], now a superseded past project).

**STICK** — Independent product build (Pillar 1) — 2026 – Present
*Subtitles that fit: "AI-Powered Study Platform", "AI Study App (deployed)", "Independent Product Build"*

**What it is:** A web app that turns admin-curated course material into a single daily, exam-aware spaced-retrieval practice plan for university students. Uses **bounded AI** (extract, grade, hint, generate) — not an open chatbot. Piloting as a deep single-course build at Purdue.

**Stack (real, in use):** React 18 + TypeScript + Vite, TailwindCSS v4; Supabase (Postgres + Auth + Storage + Deno Edge Functions); `ts-fsrs` (FSRS spaced-repetition scheduling); `pdfjs-dist` (exam PDF rendering); an LLM extraction pipeline. Deployed on Vercel. Tools: Git/GitHub, Claude Code (AI-assisted development).

**Role:** Sole builder — problem definition, data model, LLM pipeline, and app end-to-end.

**Honest stage (do not overstate):** Deployed dev build, **single-admin dogfooding** (Veer as admin is currently the only user). Purdue student pilot is pre-launch — **zero students yet, no retention/mastery/outcome data**. As of 2026-08-21 the student write path has fired exactly once, from testing. 11 of 14 planned practice-flow slices are unbuilt; STATE.md's own words are "nothing on the path is a spec-grade build."

**Headline proof bullets (defensible, quizzable):**
- Building STICK end-to-end as sole developer: a deployed web app (React/TypeScript + Supabase) that converts course material into a daily, exam-aware spaced-retrieval study plan using bounded LLM steps rather than an open chatbot.
- Designed and shipped an LLM extraction pipeline (Deno edge functions) that ingested a real 14-page, 12-question college exam end-to-end with 100% extraction confidence and zero questions falling into the unclassified/manual-review path; all 12 auto-proposed answer keys matched the instructor's published key on first pass.
- Built the full student-facing practice loop end-to-end — auth + role-gated routing, a daily plan generated from FSRS spaced-repetition scheduling, a question player with server-graded, per-choice-rationale feedback, and automatic re-scheduling on each attempt — verified working via an automated end-to-end test against a seeded account.
- Designed the Postgres data model and data-access security: 46 migrations and 33+ row-level-security policies, checked by a dedicated automated RLS probe script.
- Defined the product strategy — bounded, admin-curated AI over an open chatbot — and scoped a single-course Purdue pilot as the first real-user test.
- Ran a human-in-the-loop review queue over the LLM's output rather than shipping model output directly: 53 questions verified and 2 rejected with zero left unreviewed, across 30 live topics (verified by direct database query, 2026-08-19/20).
- Root-caused a generation-quality failure and raised question yield from 1/5 and 0/8 on consecutive runs to 8/8 on the runs after the fix (2026-08-21).
- Automated the content-publishing path end-to-end so verified material promotes itself without a human touch; the pipeline ran live unattended twice (2026-08-20/21).
- Added mechanical release gates (pre-commit and commit-message hooks since 2026-08-11; a visual-regression pass with an automated accessibility check) after tracking 24+ defects that manual review had let through, making review escapes a measured quality metric instead of an impression.
- Orchestrated the build itself as a multi-agent workflow: a coordinator agent makes decisions serially and dispatches parallel agent lanes (code, design, research) into isolated git worktrees, governed by a 400+-entry decision ledger. (Source: stick-dev CONCURRENCY-DESIGN D279; ledger count verified 2026-08-21 at D42x, 26 logged work sessions. For AI-agent roles.)

**Skills demonstrated:** product strategy/scoping, LLM pipeline design + prompt/step design, data modeling (Postgres), row-level-security / data-access design, React/TypeScript (built-with), Supabase/Deno edge functions (built-with), FSRS/spaced-repetition, AI-assisted development (Claude Code).

**Would be INFLATION (never claim at current stage):** "in production" or "live with students"; feature-completeness against the spec (11 of 14 practice-flow slices unbuilt); "exam-aware scheduling works" (exam_topics = 0, parked by decision); "multi-provider LLM support" (only Gemini is live, the OpenRouter port is parked); full automated test coverage (before 2026-08-15 zero defects were caught by automated checks); "piloted with students" / "users" (zero students — pipeline verified against a seeded test account, not a real one); any retention/mastery/engagement outcome numbers; "18 screens" or "operational dashboards" (that was StudyFlowForge, not STICK); extraction accuracy as a *measured rate across exams* (this is one real exam, n=1 — say "one exam," never "the accuracy"); the 12/12 answer-key match as a "certification" (it's agreement between two independently-built sources, not a validated ground truth); calling it "production" (it is a dev deployment).

**Tailoring notes:**
- AI/ML/technical-PM: lead with the LLM extraction pipeline + bounded-AI product decision + data model.
- Product/PM: lead with product strategy (bounded vs. chatbot) + single-course pilot framing + end-to-end ownership.
- SWE/full-stack: lead with the edge-function pipeline + Postgres/RLS + FSRS integration.
- Always re-check STATE.md for current numbers before use.
