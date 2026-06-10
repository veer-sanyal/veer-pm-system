# File Index

A manifest of every file in this project, what it is for, and what is inside it.

Project: Veer's PM-internship execution system targeting a Summer-2027 PM internship (Google APM or equivalent). This is the planning and coaching system. The dashboard product lives in a separate repo (`veer-sanyal/india-msme-digital-trade-exposure`).

> Research two-tier convention: each research report lives in BOTH `docs/` and `files/`. The `docs/` copy is the trimmed working summary (carries a `> Working summary of files/...` provenance header) and is what the system reads day to day. The `files/` copy is the full original. Go to the original when the summary is not enough.

---

## 1. Setup and system state (root)

| File | Purpose |
|------|---------|
| `SYSTEM-PROMPT.md` | The text to paste into the cowork project's custom-instructions field. Not read as a doc; it is the project's standing prompt. |
| `README.md` | What this project is and how to set it up (GitHub repo, cowork project, Calendar connector). |
| `memory.md` | CURRENT STATE only: what's shipped, active focus, next moves, durable operating principles, tools. Strategy lives in `direction.md`; the day-by-day narrative lives in `PROGRESS.md`. |
| `PROGRESS.md` | The everything-log. Running day-by-day narrative across all four pillars, external conversations (Dr. G, alumni), and system signals. PRIVATE (real names + strategy): keep this repo private. |
| `alumni-tracker.md` | Pillar 3 outreach spine: the 10-name verified alumni shortlist (+ bench), per-contact message/reply/call tracking, LinkedIn Alumni Tool recipes and Boolean queries, targeting criteria, the 5-part message blueprint, and the running ledger. Started 2026-06-09. PRIVATE (real names). |
| `file-index.md` | This file. |

---

## 2. Operating docs (`docs/`) — how the system runs

| File | Purpose |
|------|---------|
| `about-me.md` | Operational profile + comms guidelines: the planner's default decision lens. Identity, capabilities and gaps, the "insight without action" pattern, daily non-negotiables. |
| `direction.md` | Canonical strategy: the goal + four pillars + phase plan + decision rules. |
| `scheduling-blueprint.md` | Evidence-based rules for daily and weekly structure (consistency over surges, cued behavior, visible progress, recovery as execution, the Sunday session). |
| `daily-email-instructions.md` | How the daily plan is composed and delivered. Delivery is Google Calendar, not email (the Gmail connector cannot send). Filename kept for reference continuity. |
| `key-dates.md` | Recruiting timeline worked back from deadlines (Google APM closes ~early-mid Oct 2026) + program open/close table. |
| `infisum-dashboard-roadmap.md` | Build plan for Pillar 1 (the India MSME digital-trade-exposure dashboard): vision, phased plan, stack, success criteria. |
| `veer-full-profile.md` | Deep psychological/coaching profile for personalization. Reference, not day-to-day lens. |

---

## 3. Research library (`docs/` summary + `files/` original)

| Topic | `docs/` summary | `files/` original |
|-------|-----------------|-------------------|
| Interview reality | `PM_Internship_Interview_Reality_Check.md` | same name |
| Recruiting market | `Product_Management_Internship_Recruiting_for_Summer_2027.md` | same name |
| Networking | `Genuine_Networking_for_Competitive_PM_Internships.md` | same name |
| Sustained execution | `Sustained_Execution_on_Long-Horizon_Goals.md` | same name |
| College-as-leverage | `The_College-as_Leverage_Thesis_Examined_Honestly.md` | same name |
| LinkedIn presence (posting/content) | `research-linkedin-presence.md` | same name |

Four additional research docs live only in `docs/` (no separate full original): `research-metrics-fluency-curriculum.md`, `research-adjacent-roles-to-pm.md`, `research-purdue-network-recruiting.md`, `research-infisum-dashboard-user-problem.md`.

---

## 4. Assets (`files/linkedin/`)

| File | Purpose |
|------|---------|
| `chart_A_consulting.png` | Feed-ready chart for the first LinkedIn post: India's consulting exports 13x since 2005 vs flat rest of "other business services" (WTO TiSMoS, rebuilt from `site/data.js` in the site palette). |
| `chart_B_ip_licensing.png` | Alternate post chart: the ~10x placeholder vs the computed 29.4x IP-licensing growth, 2005-2025 (WTO DDS). Illustrates the no-hardcoded-numbers build rule. |
| `post-01-v2.md` | Fresh first-post draft (2026-06-10), written from scratch off the research structure with the accurate Entry 009 error-catch story. Includes posting notes (chart B, links-in-body rationale, golden-hour guidance). Supersedes post-01-draft.md. |

---

## 5. Specs (`specs/`)

| File | Purpose |
|------|---------|
| `2026-06-04-strategic-docs-research-realignment-design.md` | The approved realignment that set metrics-first over SQL, adjacent roles as a parallel track, the sector-level dashboard reframe, the 10/30 mock bar, and 3/week outreach. Historical reference. |

---

## Delivery note

The daily plan is delivered through Google Calendar (Pacific). A recurring spine holds the times; each Sunday session retitles that week's blocks and writes six 9:00 Morning Briefing events. The Gmail connector can only draft, not send, so email was retired as the delivery channel.
