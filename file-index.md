# File Index

A manifest of every file in this project, what it is for, and where to read it.

Project: Veer's PM-internship execution system targeting a Summer-2027 PM internship (Google APM or equivalent). This is the planning and coaching system. The dashboard product lives in a separate repo (`veer-sanyal/india-msme-digital-trade-exposure`).

> Three-tier reading convention (2026-06-10): `context/` holds compressed working copies — the system READS THESE, not the originals. `docs/` holds uncompressed originals, reference only (open when a compressed copy lacks detail). `files/` holds the full deep-research originals for deep dives. Compressed copies preserve every fact, number, date, name, and citation at roughly half the tokens. When a doc is added or substantively edited, refresh its `context/` copy in the same session.

---

## 1. Setup and system state (root — read live, no compressed copies)

| File | Purpose |
|------|---------|
| `SYSTEM-PROMPT.md` | The text to paste into the cowork project's custom-instructions field. Not read as a doc; it is the project's standing prompt. |
| `README.md` | What this project is and how to set it up (GitHub repo, cowork project, Calendar connector). |
| `memory.md` | CURRENT STATE only: what's shipped, active focus, next moves, durable operating principles, tools. Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`. |
| `PROGRESS.md` | The everything-log. Running day-by-day narrative across all four pillars, external conversations (Dr. G, alumni), and system signals. PRIVATE (real names + strategy): keep this repo private. |
| `alumni-tracker.md` | Pillar 3 outreach spine: the 10-name verified alumni shortlist (+ bench), per-contact message/reply/call tracking, LinkedIn Alumni Tool recipes and Boolean queries, targeting criteria, the 5-part message blueprint, and the running ledger. Started 2026-06-09. PRIVATE (real names). |
| `file-index.md` | This file. |

---

## 2. Operating docs — read the `context/` copy; `docs/` original is reference

| Doc | Read (`context/`) | Original (`docs/`) | Purpose |
|-----|-------------------|--------------------|---------|
| About me | `about-me.md` | same name | Operational profile + comms guidelines: the planner's default decision lens. Identity, capabilities and gaps, the "insight without action" pattern, daily non-negotiables. |
| Direction | `direction.md` | same name | Canonical strategy: the goal + four pillars + phase plan + decision rules. |
| Scheduling blueprint | `scheduling-blueprint.md` | same name | Evidence-based rules for daily and weekly structure (consistency over surges, cued behavior, visible progress, recovery as execution, the Sunday session). |
| Daily briefing spec | `daily-email-instructions.md` | same name | How the daily plan is composed and delivered. Delivery is Google Calendar, not email (the Gmail connector cannot send). Filename kept for reference continuity. |
| Key dates | `key-dates.md` | same name | Recruiting timeline worked back from deadlines (Google APM closes ~early-mid Oct 2026) + program open/close table. |
| Dashboard roadmap | `infisum-dashboard-roadmap.md` | same name | Build plan for Pillar 1 (the India MSME digital-trade-exposure dashboard): vision, phased plan, stack, success criteria. |
| Full profile | `veer-full-profile.md` | same name | Deep psychological/coaching profile for personalization. Reference, not day-to-day lens. |

---

## 3. Research library

| Topic | Read | Full original |
|-------|------|---------------|
| Interview reality | `docs/PM_Internship_Interview_Reality_Check.md` (not yet compressed) | `files/` same name |
| Recruiting market | `context/Product_Management_Internship_Recruiting_for_Summer_2027.md` | `files/` same name |
| Networking | `context/Genuine_Networking_for_Competitive_PM_Internships.md` | `files/` same name |
| Sustained execution | `context/Sustained_Execution_on_Long-Horizon_Goals.md` | `files/` same name |
| College-as-leverage | `context/The_College-as_Leverage_Thesis_Examined_Honestly.md` | `files/` same name |
| LinkedIn presence (posting/content) | `context/research-linkedin-presence.md` | `files/` same name |
| Metrics fluency curriculum | `context/research-metrics-fluency-curriculum.md` | `docs/` same name |
| Adjacent roles to PM | `docs/research-adjacent-roles-to-pm.md` (not yet compressed) | — |
| Purdue network recruiting | `docs/research-purdue-network-recruiting.md` (not yet compressed) | — |
| Dashboard user problem | `context/research-infisum-dashboard-user-problem.md` | `docs/` same name |

Note: the former `docs/` "working summary" copies of the five two-tier reports (Recruiting market, Networking, Sustained execution, College-as-leverage, LinkedIn presence) were removed 2026-06-10 — the `context/` compressed copies replace them. Their full originals remain in `files/`.

---

## 4. Assets (`files/linkedin/`)

| File | Purpose |
|------|---------|
| `chart_A_consulting.png` | Feed-ready chart for the first LinkedIn post: India's consulting exports 13x since 2005 vs flat rest of "other business services" (WTO TiSMoS, rebuilt from `site/data.js` in the site palette). |
| `chart_B_ip_licensing.png` | Alternate post chart: the ~10x placeholder vs the computed 29.4x IP-licensing growth, 2005-2025 (WTO DDS). Illustrates the no-hardcoded-numbers build rule. |
| `post-01-v2.md` | Fresh first-post draft (2026-06-10), written from scratch off the research structure with the accurate Entry 009 error-catch story. Includes posting notes (chart B, links-in-body rationale, golden-hour guidance). Supersedes post-01-draft.md. |
| `post-01-v3.md` | Alternate first-post draft (2026-06-10), no Entry 009 story per Veer: leads with the consulting 13x finding and the exposure index (chart A). Superseded by v4. |
| `post-01-v4.md` | Current first-post draft (2026-06-10), built from the full research original + the product repo's DECISIONS.md: consulting hook (Entry 011), named user/policy anchor (Entry 012), $90B vs 92k firms (Entry 010), v0-honesty (Entry 008). Chart A. Includes traceability + posting notes. |

---

## 5. Specs (`specs/`)

| File | Purpose |
|------|---------|
| `2026-06-04-strategic-docs-research-realignment-design.md` | The approved realignment that set metrics-first over SQL, adjacent roles as a parallel track, the sector-level dashboard reframe, the 10/30 mock bar, and 3/week outreach. Historical reference. |

---

## 6. Application documents (resume / cover letter system)

On-demand capability folded in 2026-06-13. Workflow: `context/applications/application-docs-workflow.md`.

| Path | Tier | Purpose |
|------|------|---------|
| `context/applications/application-docs-workflow.md` | instructions | How to produce tailored resumes/cover letters end-to-end. |
| `context/applications/resume-template.tex` | template | Canonical ATS-safe single-column LaTeX template; start every resume here. |
| `context/applications/profile/` | source-of-truth (read these) | Veer's contact, education, experiences (Firmly, SMIF), project (StudyFlowForge), design portfolio (Etsy), leadership (EPICS), skills, role-positioning, reusable bullets, + MEMORY index. |
| `context/applications/research/` | compressed research (read these) | Compressed ResumeDeepResearch + CoverLetterDeepResearch. |
| `files/applications/` | deep research (full) | Full ResumeDeepResearch, CoverLetterDeepResearch, Summer2026_Internship_Research (last read directly, uncompressed). |
| `applications/` | output | Per-company tailored resumes/cover letters (.tex + .pdf), `_master/` master resume, `README.md` inventory. |

Application timing lives in `context/key-dates.md` (Application Pipeline table), not in the applications/ README. Spec: `specs/2026-06-13-application-docs-integration-design.md`; plan: `specs/2026-06-13-application-docs-integration-plan.md`.

---

## Delivery note

The daily plan is delivered through Google Calendar (Pacific). A recurring spine holds the times; each Sunday session retitles that week's blocks and writes six 9:00 Morning Briefing events. The Gmail connector can only draft, not send, so email was retired as the delivery channel.
