> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-03 ~00:25 PT** (Gmail + Calendar + Chrome reachable; product repo pulled, HEAD `84ec4ca`).

---

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — static "Guided Walkthrough" on GitHub Pages (migrated off Streamlit 2026-06-01, DECISIONS Entry 009). Four data Acts: I Overview (WTO DDS), II Service Categories (TiSMoS), III MSME Base (Udyam), IV Exposure Index (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 live**: two min-max-normalised components (MSME scale + Mode 1 trade), summed; "Other business services" disaggregated into sub-sectors. Read as direction, not calibrated magnitude; the EBOPS→NIC crosswalk caveat is surfaced in the UI at Act IV. Components 3 (digital adoption; awaits a verified ASUSE 2023-24 substitute) and 4 (policy sensitivity; awaits OECD Digital STRI) stay deferred.
- **Telemetry DONE**: GoatCounter + 5 custom events confirmed firing (Jun 16); readout shipped as DECISIONS Entry 014 (Jun 25). First-week data: 101 visits, 66% from LinkedIn, funnel holds (~half scroll into the Acts). Product `DECISIONS.md` current through Entry 014; product HEAD `84ec4ca`.
- **US-version dashboard is a committed Pillar-1 track** (told Dr. G, Jun 20): no US equivalent exists (prior-art check done); scoped as a tight v0 reusing the India architecture — do not rebuild. Update Dr. G at significant progress.
- **Purdue Daniels Summer Externship, Jul 6 – Aug 1**: ASSIGNED (Jul 1 email) — team Veer + Prisha Goswami + Jiada Li + Isabel Yura; mentor **Shawn Heggland** (shawn.heggland@gmail.com); client **Scouting America (Sagamore Council BSA)**; scope in "Business one pager.docx" (not yet read). Week 1: 5 Accenture video modules, internal team meeting, first client meeting, mentor initial meeting; W2 Jul 13 midpoint, W3 Jul 20 review, W4 finals. Weekly hours TBD — size at the Jul 5 Sunday session; Secondary block yields first, protect the deep block + metrics/stats minimum. Log Heggland + client as Pillar-3 contacts from Week 1.
- Application-docs capability lives in this repo (`/apply`); pipeline rows in `context/key-dates.md`. Latest: TikTok Category Mgmt Intern SUBMITTED via referral 2026-06-29 (off-strategy, logged + flagged); Claude Corps REJECTED 2026-06-23 (no revisit needed; four-pillar plan stays primary).

---

**Live tripwires (as of Jul 3)**

1. **Anicito confirm reply UNSENT ~2 days**: he said yes to Wed Jul 8 at 5:00/5:30pm ET (LinkedIn, Jul 1) but gave no email. Smallest action: open LinkedIn, one line confirming 5:30 + re-ask the email, send the invite. Calendar hold exists (Jul 8, 2:30pm PT). Prep: `networking/Anicito-Fidelity-call-prep.md`.
2. **Externship teammate kickoff email UNSENT**, required before Jul 6 (do NOT contact mentor/client before Jul 6).
3. Jul 1–2 were zero-trace days (no initialize, no study, no commits); due-Jul-2 cold re-tests (numerator-denominator 0.40, significance/CIs 0.30) now overdue; metric-drop diagnosis still 0 attempts.

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-06-28 + the Jun 30 rep: 3 tutor sessions logged; 5 of 10 P2 topics touched. Active: metric trees 0.62 (yellow, Apply), NSM/guardrail 0.54 (3 attempts), numerator-denominator 0.40, significance/CIs 0.30. Untouched: leading-vs-lagging, funnel, retention/cohort, A/B reading, metric-drop diagnosis, MECE causes.
- Calibration: mean overconfidence −0.15 over 6 judgments (tell is UNDER-confidence on correct reads). Confidence-number-first is a hard gate; state.json writes after every item.
- P4: all 13 topics new — interview prep ramps Phase 2 (Aug+).
- **Gating variable is sleep, not the study cue**: misses trace to the 11–1 wake, not avoidance of the block.

---

**Next moves**

- **Sleep-fix workstream is the keystone** (started Jun 26; `context/sleep-protocol.md` owns config): hard fixed 9:00 wake, behavioral-first. Week 1 read: initialize came ~2pm on Jun 29 and Jun 30; Jul 1–2 unknown. Verdict + escalation check (morning light, then 0.5mg melatonin) at the Jul 5 Sunday session / ~Jul 9.
- **Pillar 3 — convert the live funnel over raw new sends**: LaCroix call LOCKED Tue Jul 7 5:00pm ET / 2:00pm PT (invite accepted; prep `networking/LaCroix-Elanco-call-prep.md`; he flagged "no strategy, right place right time" — mine the situation). Anicito Wed Jul 8 (tripwire 1). New touches via comment-then-message (Akash Ravi) — free connect-note quota near its monthly cap (~3-5/month, 200-char limit). Funnel to date: 2 cold sends → 2 replies → 2 calls agreed.
- **Dr. G (Infisum)**: relationship in active-routing mode — he's sharing the dashboard with India policy contacts and checking for usable data; await intros. Thank-you sent Jun 20; loop closed.
- **PM Club @ Purdue**: email-list form submitted + BoilerLink membership pending (Jun 28); still to do: follow @pmclubpurdue on Instagram. Run it Minimal through the Aug–Oct APM crunch (target-company speaker events = warm Pillar-3 contacts); pitch a project/teaching slot only after the APM app ships (~mid-Oct).
- **Google APM prep**: window expected to close early-to-mid Oct 2026 — the hard anchor pulling everything forward (timeline in `context/key-dates.md`).
- **FLAG (Jun 28): Veer restarted StudyFlowForge** — P3 pattern (second anchor, rebuild-before-launch), contradicts the Jun 9 one-anchor decision. Not folded into the plan; resolve genuine-pull-vs-avoidance before it earns calendar time (US-version + externship + fragile metrics habit all live). No SFF pushes as of Jul 3.
- July 4th: Cole Miller's dad — show up in person (no formal apology text); the relationship is the asset. Confirm attendance by text.

---

**Operating principles** (durable)

- The **deployed GitHub Pages site is ground truth** for what's shipped — not the README, not memory.
- Check live artifacts and prior context BEFORE planning, not after — this file has drifted before; sanity-check against the live site and latest commits.
- When Veer proposes system improvements, distinguish genuine improvement from avoidance (pattern P6) and name the real problem being solved.
- Communication: direct and short; flag flaws before building, with concrete alternatives and honest trade-offs.

---

**Tools & resources**

- Product repo: `veer-sanyal/india-msme-digital-trade-exposure` (public) · live site above · stack: static HTML/CSS + client-side Plotly; Python (pandas) builds the processed CSVs and `site/data.js`.
- Data sources: WTO DDS, WTO TiSMoS, MoMSME Udyam Bulletin VII + Annual Report 2024-25, EBOPS-ISIC crosswalk.
- This planning repo: `veer-sanyal/veer-pm-system` (PRIVATE). `gh` CLI is authenticated as veer-sanyal; git works natively (no clone workaround needed since the Claude Code migration, 2026-07-03).
