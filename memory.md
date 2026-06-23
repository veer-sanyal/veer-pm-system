> This file holds CURRENT STATE only — what's shipped, the active focus, and next moves.
> Strategy (goal, four pillars, targets, decision rules) lives in `direction.md`.
> The full day-by-day narrative lives in `PROGRESS.md` (project root).
> Last refreshed 2026-06-21 (Sunday session). Sanity-check against the live site and latest GitHub commits before trusting — this file has drifted before.

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — a single-scroll **static "Guided Walkthrough"** on GitHub Pages. As of 2026-06-01 the project **migrated off Streamlit** (DECISIONS Entry 009); there is no server runtime.
- Structure is four data "Acts":
  - **Act I — Overview** (WTO Digitally Delivered Services): is the digital-services trade real and growing?
  - **Act II — Service Categories** (WTO TiSMoS): where it concentrates; Mode 1 vs all-modes.
  - **Act III — MSME Base** (MoMSME Udyam Bulletin VII + Annual Report 2024-25): how many small firms per industry.
  - **Act IV — Exposure Index**: which sectors are most exposed (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 is built and live.** Formula = two min-max-normalised components (MSME scale in the mapped ISIC section(s) + Mode 1 trade in USD bn), summed. v0 scores: Other business services 2.00, Transport 1.37. "Other business services" is further **disaggregated** into sub-sector exposure (consulting/accounting/legal/architecture/advertising supply most firms). Read as direction, not calibrated magnitude.
- **Dr. G (Infisum): nudge sent 2026-06-13; he replied 2026-06-14 — "Thanks a lot Veer, let's catch up soon."** He did NOT answer the EBOPS→NIC crosswalk question (do not read the reply as methodology validation), but he opened a call. **Reply SENT 2026-06-16 (~12:02am PT) and the call is BOOKED: 30-min Google Meet, Thu Jun 18 2026 — RESCHEDULED to 3:45–4:15pm PT** (Dr. G's scheduler moved it the evening of Jun 17 from the original 1:00–1:30pm slot; meet.google.com/vnx-fvoc-mgi). The stuck-draft tripwire is cleared. The new 3:45pm slot no longer collides with the workout (which had been shifted to 1:30–3:00 for the old 1pm slot); no workout conflict now. Prep the EBOPS→NIC crosswalk / composite-index question for the call since he never answered it in writing. The nudge carried the telemetry + Act IV caveat update + the crosswalk-as-screening-heuristic question; the 2026-06-02 send had the live site link + de-identified repo + the exposure-score methodology question (Entry 008).
- **Dashboard is now instrumented with GoatCounter + custom events (2026-06-13).** One hosted async script in `<head>` plus five named custom events in `walkthrough.js` (each Act scrolling into view, the Act I exports/imports toggle, the Act IV score-table interaction, methodology `<details>` opens, outbound source-link clicks), all routed through a guarded `track()` helper. Live site code wired (`veersanyal.goatcounter.com`). Events CONFIRMED firing on the live site (2026-06-16) — satisfies the "at least one telemetry data point" criterion. Readout still pending more accrued data.
- **The EBOPS→NIC/ISIC crosswalk caveat is now surfaced in the UI at Act IV** — the join from a sector to its digitally delivered trade is flagged as a modeled assumption, not a measured join, so the ranking reads as direction, not calibrated magnitude.
- `DECISIONS.md` is current through **Entry 013** (telemetry instrumentation; revises Entry 012's Amplitude note, GoatCounter for v0). The exposure-score methodology is logged (Entry 008) — not an open item.
- **Accepted into the Purdue Daniels Summer Externship (email Jun 8):** 4-week virtual, team-based consulting for a local-business client, **Jul 6 – Aug 1, 2026**, with an assigned alumni mentor; ends in a final proposal presentation. Adds a Pillar-3 warm-contact surface (mentor + business owner + teammates, near-zero initiation cost), Pillar-4 client/teamwork stories, and a Daniels-branded resume line. **Supplements, does not replace, the dashboard** — that stays the only end-to-end-owned artifact and the differentiator. Weekly hours TBD.
- **Application-docs capability folded in (2026-06-13):** resume/cover-letter generation now lives in this repo. Profile source-of-truth in `context/applications/profile/`, workflow in `context/applications/application-docs-workflow.md`, outputs in `applications/` (12 legacy companies migrated, copy-only). Deadlines tracked in `context/key-dates.md` (Application Pipeline).


---

**Pillar 2 & 4 learning state**

Regenerated from `context/study/state.json` each Sunday. Doubles as the tutor's session-start dashboard.

Fields tracked:
- Topics tracked: all topics in the metrics/stats + interview-prep curriculum
- Weak (red/yellow) topics: topics where accuracy is below threshold or confidence exceeds accuracy (over-confidence flag)
- Calibration: overall over/under-confidence signal across last N attempts
- Last-practiced: timestamp per topic; flags any topic going cold (no practice in >10 days)
- Next focus: top 1-2 topics by urgency (due/weak topics + days-to-next-milestone)

State as of 2026-06-21 (Sunday session):
- All 23 topics (10 P2 + 13 P4): still **new**, 0 attempts, last_practiced null. **Zero study sessions in the 7 days since the tutor was installed (Jun 14).**
- Calibration: n/a (no data)
- This is a **pillar at zero** — flagged this session. P2 metrics study is the week-of-Jun-22 priority; establishing the first reps (metric trees, NSM/guardrail, numerator-denominator, significance/CIs, metric-drop) is the job. P4 stays dormant until Phase 2 (Aug+).

---

**Next moves**

- **Claude Corps Fellow application — REJECTED 2026-06-23.** Submitted 2026-06-18; Greenhouse decision email Jun 23: not moving forward for this cohort (limited seats, strong pool), with an invitation to apply to future cohorts and a CodePath-courses link. No interview stage reached (no take-home). **This closes the fork rather than opening one: the four-pillar Summer-2027 PM-internship plan stays the single primary track, and the Purdue leave-of-absence question is moot — no revisit needed.** No action owed beyond logging; future-cohort reapply is a possible-but-not-scheduled option. (For history: the app was filled via Claude driving Chrome from the answer key — resume PDF + combined Skilljar certs + both 350-word essays + eligibility/skill checkboxes; both gating courses done first, Claude 101 Jun 15 + AI Fluency Jun 18.)
- **Resolve the deferred exposure-score components:** the 3rd (digital adoption) is deferred pending a verified ASUSE 2023-24 substitute after ICRIER 2025 was ruled out (Entry 007/008); the 4th (policy sensitivity) waits on OECD Digital STRI (~Week 4).
- **Pillars 2 and 3 are now on** (week of Jun 8): metrics + statistics fluency leads Pillar 2 (Khan Academy + Amplitude Academy), not SQL (demoted per the 2026-06-04 realignment). Pillar 3 state as of 2026-06-09: LinkedIn profile finished (headline/About/Projects/Featured all carry the live dashboard), `alumni-tracker.md` (planning repo root) holds a 10-name verified shortlist + bench, warmest leads Daniel Anicito and Steven LaCroix (2nd-degree with mutuals). **First LinkedIn post (v7) is now LIVE (posted 2026-06-14).** Gate cleared: 3 alumni messages/week start now.
- **Externship integration:** confirm the weekly hours commitment, then fit it into the back third of summer at the Sunday session — protect dashboard minimum iteration + metrics/stats study through Jul 6 – Aug 1. Track the assigned alumni mentor + business owner as Pillar-3 contacts once assigned (Week 1).
- Google APM application prep over the coming months (close estimated **early-to-mid October 2026**).
- **Dr. G call DONE (Thu Jun 18, went well).** Two concrete outcomes: (1) he will **share the dashboard with policy contacts in India and check whether they have data Veer could use** (potential source for the modeled crosswalk join and/or the deferred digital-adoption component); (2) he raised that **he could use something similar for the US** — Veer should **check whether a US version already exists before building**. The relationship is now in active-routing mode. **Status (as of Jun 21 reconcile):** thank-you **SENT 2026-06-20, send confirmed** (final in-thread message; two leftover same-thread drafts are superseded, to be trashed). The overdue tripwire is fully closed. **US prior-art check DONE:** no US equivalent of the SME-sector exposure screen exists; only general trade data/dashboards (USITC Recent Trends in U.S. Services Trade, BEA Digital Economy) + country-level policy indices (OECD Digital STRI), none ranking SME sectors by exposure to a specific rule, and US sector data is richer so the modeled crosswalk caveat shrinks. **A US version is now a committed Pillar-1 track** — Veer told Dr. G he'd build it and send an update at significant progress. Scoped tightly in the Jun 22 week (reuse India architecture, v0 only, do not rebuild); the India dashboard stays the differentiator. Still await his India intros/data.
- **Start Pillar 3 outreach: 3 alumni messages/week**, now the first LinkedIn post is live (the gate that was holding it). **Status: week of Jun 15 finished at 1 of 3 — Daniel Anicito (Fidelity Labs incoming APM), LinkedIn connect note, Jun 20.** Week of Jun 22 target is 3, **front-loaded Mon–Wed**: LaCroix (Mon, drafted/ready), Akash Ravi (Tue, after a Mon comment on his post), Allan Tan (Wed, draft in Tue secondary). Front-loading is the fix for last week, when all 3 slipped to the end and only 1 sent. Note: LinkedIn free connect-notes cap at 200 chars and ~3-5 personalized invites/month — a real volume constraint to plan around (connect-without-note / comment-then-message, or time a free Premium trial to the fall crunch).
- **Finish telemetry setup:** events are CONFIRMED firing on the live site (checked 2026-06-16: all five custom events present in GoatCounter — hero/thesis/concepts/act1/act3/act4/learned/notclaim/next all logging). Only remaining step is the telemetry readout. It was scheduled Jun 19–20 and **slipped** (the day went to the US prior-art check + outreach); now scheduled as the Wed Jun 24 deep block (write to PROGRESS + DECISIONS). First-week data (past 7 days, captured Jun 16): 101 visits, 66% from LinkedIn (67 visits), 100% US, 57% phone / 43% desktop; section-view funnel ~13 at hero down to ~6 at the later acts.

---

**Operating principles** (durable — how to work with Veer and this project)

- The **deployed GitHub Pages site is ground truth** for what's shipped — not the README, and no longer Streamlit.
- **`PROGRESS.md` (project root) is the everything-log**; `DECISIONS.md` (repo) is curated product decisions only; `memory.md` is the current-state snapshot. Keep all three current — see the self-updating protocol in the project prompt.
- **Check live artifacts and prior context BEFORE planning, not after** — Veer caught Claude generating plans on stale roadmap assumptions; this file itself drifted (still said "Streamlit") until reconciled against commits on 2026-06-04.
- When Veer proposes system improvements, distinguish genuine improvements from avoidance patterns and name the real problem being solved.
- Communication: **direct and short**; accepts pushback when grounded, but expects flaws flagged before building, with concrete alternatives and honest trade-offs.

---

**Tools & resources**

- **GitHub repo**: `veer-sanyal/india-msme-digital-trade-exposure` (public)
- **Live site**: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/ (GitHub Pages, published from `site/`)
- **Progress log**: `PROGRESS.md` at the project root (private; not in the public repo)
- **Stack**: static HTML + CSS + client-side Plotly on a small design system (IBM Plex; warm paper / cool ink; indigo + clay). Python (pandas) only builds the processed CSVs and `site/data.js` — `scripts/build_processed.py`, `build_msme_nic.py`, `build_site_data.py`.
- **Data sources**: WTO DDS, WTO TiSMoS, MoMSME Udyam Bulletin VII + Annual Report 2024-25, EBOPS-ISIC crosswalk. Raw files processed in Python for reproducibility.
- **Web-fetch limitations**: GitHub repo pages not always reliably fetchable — pasting file contents directly is more reliable than URL fetches.
