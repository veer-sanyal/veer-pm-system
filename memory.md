> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-05 ~09:40 PT** (Gmail + Calendar reachable; Chrome not used this scan; product repo HEAD `84ec4ca`, no drift).

---

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — static "Guided Walkthrough" on GitHub Pages (migrated off Streamlit 2026-06-01, DECISIONS Entry 009). Four data Acts: I Overview (WTO DDS), II Service Categories (TiSMoS), III MSME Base (Udyam), IV Exposure Index (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 live**: two min-max-normalised components (MSME scale + Mode 1 trade), summed; "Other business services" disaggregated into sub-sectors. Read as direction, not calibrated magnitude; the EBOPS→NIC crosswalk caveat is surfaced in the UI at Act IV. Components 3 (digital adoption; awaits a verified ASUSE 2023-24 substitute) and 4 (policy sensitivity; awaits OECD Digital STRI) stay deferred.
- **Telemetry DONE**: GoatCounter + 5 custom events confirmed firing (Jun 16); readout shipped as DECISIONS Entry 014 (Jun 25). First-week data: 101 visits, 66% from LinkedIn, funnel holds (~half scroll into the Acts). Product `DECISIONS.md` current through Entry 014; product HEAD `84ec4ca`.
- **US-version dashboard is a committed Pillar-1 track** (told Dr. G, Jun 20): no US equivalent exists (prior-art check done); scoped as a tight v0 reusing the India architecture — do not rebuild. Update Dr. G at significant progress.
- **Purdue Daniels Summer Externship, Jul 6 – Aug 1**: ASSIGNED (Jul 1 email) — team Veer + Prisha Goswami + Jiada Li + Isabel Yura; mentor **Shawn Heggland**; client **Scouting America (Sagamore Council)**, contact **Bryon Haverstick (COO)**. **Scope READ (Jul 3): build a communications + marketing plan** — posting schedule/frequency/channels for 4 content buckets across 5 audiences, plus website/social adjustment recommendations. All static facts + contacts now in `context/externship-scouting-america.md` (one-pager original in Veer's Drive). Week 1: 5 Accenture video modules (Jul 2 "NEW LINK" email), internal team meeting BEFORE any mentor/client email, first client meeting, mentor initial meeting; W2 Jul 13 midpoint, W3 Jul 20 review, W4 finals. Weekly hours TBD — size at the Jul 5 Sunday session; Secondary block yields first, protect the deep block + metrics/stats minimum. At kickoff: ask for the Timeline & Project Manager role. Log Heggland + Haverstick as Pillar-3 contacts from Week 1.
- Application-docs capability lives in this repo (`/apply`); pipeline rows in `context/key-dates.md`. Latest: **Trice CONVERTED (Jul 3): Sudip Uncle says "from next week u can start" + asked for IST-mapped time windows** — reply pending (tripwire 4); role/hours/remote still unknown, sizing is a Sunday-session call. TikTok Category Mgmt Intern SUBMITTED via referral 2026-06-29 (off-strategy, logged + flagged); Claude Corps REJECTED 2026-06-23 (no revisit needed; four-pillar plan stays primary).

---

**Live tripwires (as of Jul 5 reconcile)**

1. **Kickoff email SENT Jul 5 10:18am PT** (verified in:sent; went from the gmail address, not Purdue — if any teammate hasn't replied by Monday morning, consider a resend from vsanyal@purdue.edu in case of filtering). New live edge: **watch for teammate replies; as soon as 2+ reply with Monday windows, send the calendar invite + Meet link same day.** Internal meeting gates mentor/client contact (allowed from Jul 6, internal-first rule). At the meeting: volunteer for Timeline & Project Manager, evidence in hand.
2. Jul 1–2 AND Jul 4 were zero-trace days (state.json untouched since the Jul 3 session, last practice Jun 30; no commits; no initialize). Due-Jul-2 cold re-tests (numerator-denominator 0.40, significance/CIs 0.30) overdue; metric-drop diagnosis still 0 attempts. Sleep verdict lands at TODAY's Sunday session (4pm PT, on the calendar).
3. **Anicito invite pending his email**: confirm SENT Jul 3 (5:30pm ET Jul 8 locked, email re-asked). No LinkedIn digest hits through Jul 5 am — no reply yet. When his email lands, send the Calendar invite + Meet link same day (hold exists: Jul 8, 2:30pm PT). If no email by the call, run it over LinkedIn.
4. **Trice reply SENT (Jul 5, 9:59am PT)** — gave 9:30–11pm IST weekday windows, offered to connect with the team. Now awaiting Sudip/Trice scheduling. The externship-hours flag was dropped from the sent version, so it MUST be raised on the team call, along with role family / weekly hours / remote-vs-Hyderabad. No hour commitments before the Sunday session sizes Trice against externship Week 1.

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-06-28 + the Jun 30 rep: 3 tutor sessions logged; 5 of 10 P2 topics touched. Active: metric trees 0.62 (yellow, Apply), NSM/guardrail 0.54 (3 attempts), numerator-denominator 0.40, significance/CIs 0.30. Untouched: leading-vs-lagging, funnel, retention/cohort, A/B reading, metric-drop diagnosis, MECE causes.
- Calibration: mean overconfidence −0.15 over 6 judgments (tell is UNDER-confidence on correct reads). Confidence-number-first is a hard gate; state.json writes after every item.
- P4: all 13 topics new — interview prep ramps Phase 2 (Aug+).
- **Gating variable is sleep, not the study cue**: misses trace to the 11–1 wake, not avoidance of the block.

---

**Next moves**

- **Sleep-fix workstream is the keystone** (started Jun 26; `context/sleep-protocol.md` owns config): hard fixed 9:00 wake, behavioral-first. Week 1 read: initialize came ~2pm on Jun 29 and Jun 30; Jul 1–2 unknown. Verdict + escalation check (morning light, then 0.5mg melatonin) at the Jul 5 Sunday session / ~Jul 9.
- **Pillar 3 — convert the live funnel over raw new sends**: LaCroix call LOCKED Tue Jul 7 5:00pm ET / 2:00pm PT (invite accepted; prep `networking/LaCroix-Elanco-call-prep.md`; he flagged "no strategy, right place right time" — mine the situation). Anicito Wed Jul 8 (tripwire 1). New touches via comment-then-message (Akash Ravi) — free connect-note quota near its monthly cap (~3-5/month, 200-char limit). Funnel to date: 2 cold sends → 2 replies → 2 calls agreed. Anicito: Jul 8 5:30pm ET locked (tripwire 3, invite awaits his email).
- **Dr. G (Infisum)**: relationship in active-routing mode — he's sharing the dashboard with India policy contacts and checking for usable data; await intros. Thank-you sent Jun 20; loop closed.
- **PM Club @ Purdue**: email-list form submitted + BoilerLink membership pending (Jun 28); still to do: follow @pmclubpurdue on Instagram. Run it Minimal through the Aug–Oct APM crunch (target-company speaker events = warm Pillar-3 contacts); pitch a project/teaching slot only after the APM app ships (~mid-Oct).
- **Google APM prep**: window expected to close early-to-mid Oct 2026 — the hard anchor pulling everything forward (timeline in `context/key-dates.md`).
- **FLAG (Jun 28): Veer restarted StudyFlowForge** — P3 pattern (second anchor, rebuild-before-launch), contradicts the Jun 9 one-anchor decision. Not folded into the plan; resolve genuine-pull-vs-avoidance before it earns calendar time (US-version + externship + fragile metrics habit all live). No SFF pushes as of Jul 3.
- July 4th (Cole Miller's dad) has passed — outcome unknown; ask at the Sunday session whether he went and log it.

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
