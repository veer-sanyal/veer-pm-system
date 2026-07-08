> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-07 ~14:40 PT** (Gmail + Calendar reachable; Chrome/WhatsApp/iMessage not visible this scan; product repo HEAD `84ec4ca`, no drift). **Sunday session RUN Jul 5 ~10:30am** — week of Jul 6 planned, calendar written; do not re-plan this week mid-stream.

---

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — static "Guided Walkthrough" on GitHub Pages (migrated off Streamlit 2026-06-01, DECISIONS Entry 009). Four data Acts: I Overview (WTO DDS), II Service Categories (TiSMoS), III MSME Base (Udyam), IV Exposure Index (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 live**: two min-max-normalised components (MSME scale + Mode 1 trade), summed; "Other business services" disaggregated into sub-sectors. Read as direction, not calibrated magnitude; the EBOPS→NIC crosswalk caveat is surfaced in the UI at Act IV. Components 3 (digital adoption; awaits a verified ASUSE 2023-24 substitute) and 4 (policy sensitivity; awaits OECD Digital STRI) stay deferred.
- **Telemetry DONE**: GoatCounter + 5 custom events confirmed firing (Jun 16); readout shipped as DECISIONS Entry 014 (Jun 25). First-week data: 101 visits, 66% from LinkedIn, funnel holds (~half scroll into the Acts). Product `DECISIONS.md` current through Entry 014; product HEAD `84ec4ca`.
- **US-version dashboard is a committed Pillar-1 track** (told Dr. G, Jun 20): no US equivalent exists (prior-art check done); scoped as a tight v0 reusing the India architecture — do not rebuild. Update Dr. G at significant progress.
- **Purdue Daniels Summer Externship, Jul 6 – Aug 1**: ASSIGNED (Jul 1 email) — team Veer + Prisha Goswami + Jiada Li + Isabel Yura; mentor **Shawn Heggland**; client **Scouting America (Sagamore Council)**, contact **Bryon Haverstick (COO)**. **Scope READ (Jul 3): build a communications + marketing plan** — posting schedule/frequency/channels for 4 content buckets across 5 audiences, plus website/social adjustment recommendations. All static facts + contacts now in `context/externship-scouting-america.md` (one-pager original in Veer's Drive). Week 1: 5 Accenture video modules (Jul 2 "NEW LINK" email), internal team meeting BEFORE any mentor/client email, first client meeting, mentor initial meeting; W2 Jul 13 midpoint, W3 Jul 20 review, W4 finals. **Kickoff email SENT Jul 5 10:18am (tripwire 1: replies → invite).** W1 planned into the calendar; real weekly hours read lands next Sunday (Jul 12) and sizes W2 + Trice. Secondary block yields first; protect the deep block + metrics/stats minimum. At kickoff: ask for the Timeline & Project Manager role. Contact rows ready in `alumni-tracker.md`.
- Application-docs capability lives in this repo (`/apply`); pipeline rows in `context/key-dates.md`. Latest: **Trice CONVERTED (Jul 3): Sudip Uncle says "from next week u can start" + asked for IST-mapped time windows** — reply pending (tripwire 4); role/hours/remote still unknown, sizing is a Sunday-session call. TikTok Category Mgmt Intern SUBMITTED via referral 2026-06-29 (off-strategy, logged + flagged); Claude Corps REJECTED 2026-06-23 (no revisit needed; four-pillar plan stays primary).

---

**Live tripwires (as of Jul 7 reconcile — week of Jul 6 planned, calendar written)**

1. **Externship W1, Veer = Timeline & Project Manager** (kickoff RAN Jul 6 3:00pm PT, 3-of-4; Izzy = Client Comm, Prisha = Alumni Comm, Jiada = D&Q Lead by default, pending confirm; iMessage group is the channel, standing slot 3pm PT). **Recap email SENT Jul 6 3:58pm PT** (roles + Jiada confirm-and-chat-add ask) — no teammate replies yet as of Tue 2:36pm. Open: **(a) Heggland intro via Prisha — no email trace yet; target talked-to-by-WEDNESDAY (tomorrow); verify at today's 3pm sync (iMessage not visible to this system); (b)** Haverstick scope meeting via Izzy AFTER the mentor intro — guard stands: if Shawn can't meet by Wed, the Bryon email goes anyway with the meeting Thu/Fri; **(c)** file-sharing home (Drive) unset. **Jiada ladder: zero engagement since his decline; the 48h clock from the recap expires Wed ~4pm PT → one direct personal note**; zero engagement through W1 → raise with Heggland at the intro, not Storie.
2. **Anicito: call RAN Wed Jul 8 2:30pm PT, went well** — second completed informational interview; gave concrete interview + networking pointers (full list in `ledgers.md` relationships log; Pillar-4 technique for mock prep). **Same-day thank-you DRAFTED, who-else ask folded in — awaiting Veer's send (slug `anicito-thankyou-jul8`).** Keep-updated agreed; if he names people → warm-intro shortlist rows. Loop closes when the thank-you is sent.
3. **Trice team call:** awaiting Sudip's scheduling (windows offered Jul 5: 9:30–11pm IST weekdays = 9:00–10:30am PT); no reply as of Jul 7. Call agenda: role family, weekly hours, remote-vs-Hyderabad, + the Purdue-externship disclosure (not in the WhatsApp reply — must be said on the call). NO hour commitments before next Sunday sizes it against real externship-W1 hours.
4. **Melatonin decision Thu Jul 9** (in that day's briefing): wake landed 9:00–10:00 on 3 of the last 4 days → hold; otherwise start 0.5mg ~8:30pm. Morning light is ACTIVE from Mon Jul 6. **No in-system wake log for Mon/Tue (no /initialize runs this week)** — the Thu decision rides on Veer's self-report.

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-07-05: 4 tutor sessions logged (Jun 23, 25, 30, Jul 3). Active: metric trees 0.62 (due **Jul 9**), NSM/guardrail 0.54 (due Jul 14), numerator-denominator 0.45 (due **Jul 10**), significance/CIs **0.15 — cold-dropped from 0.30 on the Jul 3 re-test, weakest topic** (due Jul 10; Tue rebuild in teach mode). Untouched: leading-vs-lagging, funnel, retention/cohort, A/B reading, **metric-drop diagnosis (0 attempts, 4 weeks — Wed first contact, 25 min counts)**, MECE causes.
- Calibration: mean overconfidence −0.15 over 6 judgments (tell is UNDER-confidence on correct reads). Confidence-number-first is a hard gate; state.json writes after every item.
- P4: all topics new — interview prep ramps Phase 2 (Aug+). Monthly STAR audit Mon Jul 6 5pm (standing, cheap).
- **Gating variable is sleep, not the study cue**: misses trace to the late wake, not avoidance of the block. Week 1 of the 9:00 wake: mixed, trending earlier → morning light active from Jul 6, melatonin check Jul 9.

---

**Next moves (week of Jul 6–12 — calendar written at the Jul 5 Sunday session, 18 blocks + 6 briefings)**

- **Keystone (sleep):** 9:00 wake + **morning light from Mon Jul 6** (outside within ~5 min of the alarm, 10+ min); melatonin decision Thu (tripwire 4). Wind-down cue closes EVERYTHING, including StudyFlow spec files.
- **Externship W1 is the week's fixed structure** (Secondary yields first): Mon team meeting + videos start, 5 videos done by Tue, mentor intro + first client meeting out of Monday's meeting, role ask = Timeline & Project Manager. Contacts logged Wed (rows ready in `alumni-tracker.md`).
- **P2 protected minimum, 3 deep blocks:** Tue significance rebuild (0.15) — **no state.json trace as of Tue 2:36pm; if it didn't run, it folds into Wed/Fri**; Wed metric-trees re-test + metric-drop first contact; Fri cold re-tests due.
- **P3 convert week:** **LaCroix loop CLOSED Jul 7** (thank-you sent same day). **Anicito call RAN Jul 8, went well — thank-you drafted, awaiting Veer's send (tripwire 2).** Akash comment Thu → message Fri. No new cold sends. Funnel: 2 sent → 2 replies → 2 booked → **2 completed**.
- **P1 US version v0, 2 deep blocks:** Mon's 10-line scope SLIPPED (no artifact in either repo — **now a 3rd carry**); Thu's deep block is the catch, already in that briefing: if the scope isn't on paper, the scope IS the block (first move: open USITC DataWeb, write line 1); Sat first ranked cut.
- **Dr. G (Infisum)**: active-routing mode; await intros. Update him at significant US-version progress.
- **PM Club @ Purdue**: minimal through the Aug–Oct crunch; still open: follow @pmclubpurdue on Instagram.
- **Google APM**: window closes early-to-mid Oct 2026 — the hard anchor (timeline in `context/key-dates.md`).
- **SFF flag RESOLVED (Jul 5):** genuine pull, not avoidance — it's a disciplined spec bundle (`~/Desktop/study app advisor`, 33 components locked, no code). Ruling: off the committed calendar through the APM window; lives in after-3:30 personal time; never displaces a morning block; stops at the wind-down cue. Revisit at the Aug recovery week or when the APM app ships.
- July 4th (Cole Miller's dad): WENT, was good — closed, logged in PROGRESS. Next beat organic (wakeboarding invite if it comes).

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
