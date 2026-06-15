# File Index

A manifest of every file in this project, what it is for, and where to read it.

Project: Veer's PM-internship execution system targeting a Summer-2027 PM internship (Google APM or equivalent). This is the planning and coaching system. The dashboard product lives in a separate repo (`veer-sanyal/india-msme-digital-trade-exposure`).

> Two-tier reading convention (simplified 2026-06-15): `context/` holds the working copies the system READS for all day-to-day work (one canonical copy per doc). `files/` holds the full deep-research originals for deep dives only (open when a `context/` copy lacks detail). The `context/` copies preserve every fact, number, date, name, and citation at roughly half the tokens. When a doc is added or substantively edited, update its `context/` copy in the same session and index it here. (The former `docs/` uncompressed-mirror tier was removed 2026-06-15; it duplicated `context/` and drifted.)

---

## 1. Setup and system state (root — read live, no compressed copies)

| File | Purpose |
|------|---------|
| `SYSTEM-PROMPT.md` | The text to paste into the cowork project's custom-instructions field. Not read as a doc; it is the project's standing prompt. Holds the auto-reconcile protocol, closed-loop accountability, the two-tier convention, and the single-source-of-truth ownership map. |
| `README.md` | What this project is and how to set it up (GitHub repo, cowork project, Calendar connector). |
| `memory.md` | OWNS current state: what's shipped, active focus, next moves, durable operating principles, tools. Mirrors a regenerated summary of `context/study/state.json` (never hand-edit that summary). Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`. |
| `PROGRESS.md` | OWNS the running narrative: day-by-day log across all four pillars, the standing pillar ledgers, external conversations (Dr. G, alumni), and system signals. Read the tail (~3-4 weeks) by default; older months roll into `PROGRESS-archive.md`. PRIVATE (real names + strategy): keep this repo private. |
| `PROGRESS-archive.md` | Closed-month entries rolled out of `PROGRESS.md` to keep the per-session tail read small. The complete historical log; created when the first month is archived. PRIVATE. |
| `alumni-tracker.md` | Pillar 3 outreach spine: the 10-name verified alumni shortlist (+ bench), per-contact message/reply/call tracking, LinkedIn Alumni Tool recipes and Boolean queries, targeting criteria, the 5-part message blueprint, and the running ledger. Started 2026-06-09. PRIVATE (real names). |
| `file-index.md` | This file. |

---

## 2. Operating docs (`context/` — the read tier)

| Doc | File (`context/`) | Owns / purpose |
|-----|-------------------|----------------|
| About me | `about-me.md` | Operational profile + comms guidelines: the planner's default decision lens. Identity, capabilities and gaps, the "insight without action" pattern, daily non-negotiables. (Goal/targets/success criteria are owned by `direction.md`; live status is owned by `memory.md`.) |
| Direction | `direction.md` | OWNS strategy: the goal + four pillars + success criteria + phase plan + decision rules. |
| Scheduling blueprint | `scheduling-blueprint.md` | OWNS the weekly/daily structure rules (consistency over surges, cued behavior, visible progress, recovery as execution, the Sunday session, weekly volume targets). |
| Daily briefing spec | `daily-email-instructions.md` | OWNS how the daily plan + Morning Briefings + Sunday session are composed and written to the calendar. Delivery is Google Calendar, not email (the Gmail connector cannot send). Filename kept for reference continuity. |
| Key dates | `key-dates.md` | OWNS the recruiting timeline, all deadlines, and the Application Pipeline. Worked back from Google APM (~early-mid Oct 2026). |
| Dashboard roadmap | `infisum-dashboard-roadmap.md` | Build plan for Pillar 1 (the India MSME digital-trade-exposure dashboard): vision, phased plan, stack, success criteria. |
| Full profile | `veer-full-profile.md` | Deep psychological/coaching profile for personalization. Reference, not day-to-day lens. Full original in `files/veer-full-profile.md`. |

---

## 3. Research library

All read copies are in `context/`. A `files/` entry means the full uncompressed deep-research original is also kept for deep dives.

| Topic | Read (`context/`) | Full original (`files/`) |
|-------|-------------------|--------------------------|
| Interview reality | `PM_Internship_Interview_Reality_Check.md` | `files/` same name |
| Recruiting market | `Product_Management_Internship_Recruiting_for_Summer_2027.md` | `files/` same name |
| Networking | `Genuine_Networking_for_Competitive_PM_Internships.md` | `files/` same name |
| Sustained execution | `Sustained_Execution_on_Long-Horizon_Goals.md` | `files/` same name |
| College-as-leverage | `The_College-as_Leverage_Thesis_Examined_Honestly.md` | `files/` same name |
| LinkedIn presence (posting/content) | `research-linkedin-presence.md` | `files/` same name |
| Metrics fluency curriculum | `research-metrics-fluency-curriculum.md` | — (context-only) |
| Adjacent roles to PM | `research-adjacent-roles-to-pm.md` | — (context-only) |
| Purdue network recruiting | `research-purdue-network-recruiting.md` | — (context-only) |
| Dashboard user problem | `research-infisum-dashboard-user-problem.md` | — (context-only) |

---

## 4. Assets (`files/linkedin/`)

| File | Purpose |
|------|---------|
| `chart_A_consulting.png` | Feed-ready chart for the first LinkedIn post: India's consulting exports 13x since 2005 vs flat rest of "other business services" (WTO TiSMoS, rebuilt from `site/data.js` in the site palette). |
| `chart_B_ip_licensing.png` | Original post chart (2026-06-10): the ~10x placeholder vs the computed 29.4x IP-licensing growth, 2005-2025 (WTO DDS). Error-catch framing. Superseded by v2 for post v5. |
| `chart_B_ip_licensing_v2.png` | **Current chart for post v5.** Same IP-licensing series rebuilt from the real `ipImp` values in the product repo's `site/data.js` (0.67B->19.8B = 29.4x), retitled to the build-discipline framing rather than the error-catch. |
| `make_chart_B.py` | Reproducible generator for `chart_B_ip_licensing_v2.png`. Holds the `ipImp` series copied from `site/data.js`; re-run after a data refresh. Matplotlib, house palette. |
| `post-01-v2.md` | Fresh first-post draft (2026-06-10), error-catch story. Superseded. |
| `post-01-v3.md` | Alternate first-post draft (2026-06-10), consulting 13x lead. Superseded by v4. |
| `post-01-v4.md` | First-post draft (2026-06-10): consulting hook + named user/policy anchor + $90B vs 92k firms + v0-honesty. Superseded by v5. |
| `post-01-v5.md` | **Current first-post draft (2026-06-13).** Spined on build discipline; 29.4x IP-licensing as the concrete example; one body link. Pairs with retitled Chart B. Supersedes v2-v4. |

---

## 5. Specs (`specs/`)

| File | Purpose |
|------|---------|
| `2026-06-04-strategic-docs-research-realignment-design.md` | The approved realignment that set metrics-first over SQL, adjacent roles as a parallel track, the sector-level dashboard reframe, the 10/30 mock bar, and 3/week outreach. Historical reference. |
| `2026-06-13-application-docs-integration-design.md` | Design spec for the application-docs capability (resume/cover letter workflow). |
| `2026-06-13-application-docs-integration-plan.md` | Implementation plan for the application-docs capability. |
| `2026-06-14-pm-skills-tutor-integration-design.md` | Design spec for the PM Skills Tutor subsystem (Pillars 2 + 4). |
| `2026-06-14-pm-skills-tutor-integration-plan.md` | Implementation plan for the PM Skills Tutor subsystem. |
| `2026-06-15-dynamic-tracking-system-upgrade.md` | Design + plan for the auto-reconcile / closed-loop-accountability / two-tier-reorg / single-source-of-truth upgrade. |

---

## 6. Application documents (resume / cover letter system)

On-demand capability folded in 2026-06-13. Workflow: `context/applications/application-docs-workflow.md`.

| Path | Tier | Purpose |
|------|------|---------|
| `context/applications/application-docs-workflow.md` | instructions | How to produce tailored resumes/cover letters end-to-end. |
| `context/applications/resume-template.tex` | template | Canonical ATS-safe single-column LaTeX template; start every resume here. |
| `context/applications/profile/` | source-of-truth (read these) | Veer's contact, education, experiences (Firmly, SMIF), project (StudyFlowForge), design portfolio (Etsy), leadership (EPICS), skills, role-positioning, reusable bullets, + MEMORY index. |
| `context/applications/research/` | compressed research (read these) | Compressed ResumeDeepResearch + CoverLetterDeepResearch. |
| `files/applications/` | deep research (full) | Full ResumeDeepResearch, CoverLetterDeepResearch, Summer2026_Internship_Research. |
| `applications/` | output | Per-company tailored resumes/cover letters (.tex + .pdf), `_master/` master resume, `README.md` inventory. |

Application timing lives in `context/key-dates.md` (Application Pipeline table), not in the applications/ README. Spec: `specs/2026-06-13-application-docs-integration-design.md`; plan: `specs/2026-06-13-application-docs-integration-plan.md`.

---

## 7. PM Skills Tutor (`context/study/`)

Added 2026-06-14. Manages Pillar 2 (metrics fluency) and Pillar 4 (core PM interview skills) via a standalone study loop.

### Context copies (read these)

| File | Purpose |
|------|---------|
| `context/study/study-tutor.md` | Entry point: activation triggers, session loop (incl. ambiguous-answer probe and fatigue-vs-weakness split), hard rules, close-out protocol. |
| `context/study/pedagogy.md` | Mastery-band pedagogy modes (Novice/Developing/Competent/Mastery), Bloom levels, session shapes (Build/Consolidate/Mock-prep), rubric grading. |
| `context/study/state-spec.md` | `state.json` schema, spacing bands, EWMA thresholds, Bloom promotion/demotion window, error-note retention, write protocol. |
| `context/study/curriculum.md` | P2/P4 topic tree with `topic_id` values, company exam-format map, seed real-prompt bank, and the Question-Generation Rubric. |
| `context/study/state.json` | OWNS learning state: mastery, flags, calibration, sessions. Committed every session. |
| `context/study/research-pm-interview-reality.md` | Compressed research: PM interview reality check (verified company formats, rubrics, sources). |
| `context/study/research-spacing-science.md` | Compressed research: spacing and retrieval science (Cepeda, Karpicke, Kang, Rohrer). |

### Full originals (`files/study/`; open when the compressed copy lacks detail)

| File | Purpose |
|------|---------|
| `files/study/research-pm-interview-reality.md` | Full PM interview reality research (uncompressed). |
| `files/study/research-spacing-science.md` | Full spacing science research (uncompressed). |

---

## Delivery note

The daily plan is delivered through Google Calendar (Pacific). A recurring spine holds the times; each Sunday session retitles that week's blocks and writes six 9:00 Morning Briefing events (each leading with the done-check on yesterday's block). The Gmail connector can only draft, not send, so email was retired as the delivery channel.
