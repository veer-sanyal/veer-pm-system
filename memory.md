> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-15 (Wed) ~15:35 PT** (Gmail + Calendar + product repo reachable, HEAD `84ec4ca` no drift; **iMessage toggle ON but chat.db NOT readable — Full Disk Access not granted, so the team-channel scan is still blind**; WhatsApp not visible). **Sunday Jul 12 session was MISSED — W2 (externship midpoint, started Jul 13) has NO plan; the Jul 13–16 calendar is generic placeholders with no briefings.** A belated `/sunday` or a tight tactical W2 plan is the real next move (tripwire 2) — offered to Veer, not run inside the reconcile.

---

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — static "Guided Walkthrough" on GitHub Pages (migrated off Streamlit 2026-06-01, DECISIONS Entry 009). Four data Acts: I Overview (WTO DDS), II Service Categories (TiSMoS), III MSME Base (Udyam), IV Exposure Index (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 live**: two min-max-normalised components (MSME scale + Mode 1 trade), summed; "Other business services" disaggregated into sub-sectors. Read as direction, not calibrated magnitude; the EBOPS→NIC crosswalk caveat is surfaced in the UI at Act IV. Components 3 (digital adoption; awaits a verified ASUSE 2023-24 substitute) and 4 (policy sensitivity; awaits OECD Digital STRI) stay deferred.
- **Telemetry DONE**: GoatCounter + 5 custom events confirmed firing (Jun 16); readout shipped as DECISIONS Entry 014 (Jun 25). First-week data: 101 visits, 66% from LinkedIn, funnel holds (~half scroll into the Acts). Product `DECISIONS.md` current through Entry 014; product HEAD `84ec4ca`.
- **US-version dashboard is a committed Pillar-1 track** (told Dr. G, Jun 20): no US equivalent exists (prior-art check done); scoped as a tight v0 reusing the India architecture — do not rebuild. Update Dr. G at significant progress.
- **Purdue Daniels Summer Externship, Jul 6 – Aug 1**: ASSIGNED (Jul 1 email) — team Veer + Prisha Goswami + Jiada Li + Isabel Yura; mentor **Shawn Heggland**; client **Scouting America (Sagamore Council)**, contact **Bryon Haverstick (COO)**. **Scope READ (Jul 3): build a communications + marketing plan** — posting schedule/frequency/channels for 4 content buckets across 5 audiences, plus website/social adjustment recommendations. All static facts + contacts now in `context/externship-scouting-america.md` (one-pager original in Veer's Drive). Week 1: 5 Accenture video modules (Jul 2 "NEW LINK" email), internal team meeting BEFORE any mentor/client email, first client meeting, mentor initial meeting; W2 Jul 13 midpoint, W3 Jul 20 review, W4 finals. **W1 DONE:** kickoff ran Jul 6 3pm (Veer got **Timeline & Project Manager**), 5 videos, recap sent Jul 6. **Now W2 — the midpoint week, started Mon Jul 13.** Mentor intro meeting FINALLY booked (Prisha's Teams invite Jul 15, see tripwire 1); Bryon client-scope email drafted by Izzy Jul 15, greenlit, awaiting send. The real weekly-hours read + Trice sizing were the missed Sunday's job — still open. Secondary block yields first; protect the deep block + metrics/stats minimum. Contact rows in `alumni-tracker.md`.
- Application-docs capability lives in this repo (`/apply`); pipeline rows in `context/key-dates.md`. Latest: **Trice handoff set (Jul 8): Sudip passed Veer to Naveen, a Trice founding member** — Naveen will ping Veer on WhatsApp directly; if no ping by Thu Jul 10, Veer messages him at +91 99490 33255 (ref Sudip or Mr Gautham). Reply to Sudip sent Jul 9 (tripwire 3); role/hours/remote still unknown, sizing was the Jul 12 Sunday's job (missed — still unsized; whether Naveen pinged is a blind spot, see tripwire 3). TikTok Category Mgmt Intern SUBMITTED via referral 2026-06-29 (off-strategy, logged + flagged); Claude Corps REJECTED 2026-06-23 (no revisit needed; four-pillar plan stays primary).

---

**Live tripwires (as of Jul 15 reconcile)**

1. **Externship mentor meeting BOOKED (Jul 15):** Prisha sent a Microsoft Teams invite today ("First meeting with alumni mentor" → Shawn Heggland + Izzy + vsanyal@purdue.edu; **Jiada NOT on it**) after Shawn hadn't sent a link; Veer confirmed receipt ("I got it"). **Slot: ~6pm ET today per the team thread ("does 6pm tmr est work," said Jul 14) — CONFIRM exact time with Veer** (the `.ics` isn't machine-readable and the invite went to his Purdue email, so it never synced to his Google Calendar → have him add it). **`/debrief` right after** (outcome, same-day thank-you to Shawn, next tripwire), and **raise Jiada at this meeting** (zero visible engagement W1–W2). Open: **(b)** Bryon scope email drafted by Izzy, greenlit, **awaiting send** — log it when it goes; client meeting follows once Bryon replies. **(c)** shared-files home (Drive) still unset.
2. **Sunday Jul 12 MISSED → W2 has no plan.** Jul 13–16 calendar is generic placeholders with no briefings; study ledger unreconciled (state.json cold since Jul 3); the US-version structural verdict, Trice sizing, and the melatonin close were all deferred there and remain open. **Next move: a belated `/sunday` or a tight tactical W2 plan — Veer's call.** (New on the calendar: Cosentino case classes/comp Jul 13 + Jul 15 — free P4 reps, fold in.)
3. **Trice (blind):** the Jul 11 pre-set send day passed with no visibility (no email channel; iMessage/WhatsApp dark). Unknown whether Naveen pinged or Veer messaged him. Smallest action if unactioned: one WhatsApp to Naveen (+91 99490 33255), ref Sudip / Mr Gautham. Agenda unchanged (role family, weekly hours, remote-vs-Hyderabad, + externship disclosure on the call). No hour commitments until sized against real externship hours.
4. **Melatonin decision — 6 days past due** (due Jul 9; the Sunday that was to close it was missed). No in-system wake log all week. **Default HOLD**; close from Veer's self-report (rule: wake landed 9:00–10:00 on 3 of last 4 days → hold; else 0.5mg ~8:30pm). Morning light continues regardless.
5. **Alumni loops closed & healthy** (LaCroix + Anicito — both keep-updated, next touches event-based). One tiny open Anicito move: **send one short text to open the text channel** (his cell, his preferred); unverifiable this session (iMessage blind) — confirm with Veer.

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-07-05: 4 tutor sessions logged (Jun 23, 25, 30, Jul 3). Active: metric trees 0.62 (due **Jul 9**), NSM/guardrail 0.54 (due Jul 14), numerator-denominator 0.45 (due **Jul 10**), significance/CIs **0.15 — cold-dropped from 0.30 on the Jul 3 re-test, weakest topic** (due Jul 10; Tue rebuild in teach mode). Untouched: leading-vs-lagging, funnel, retention/cohort, A/B reading, **metric-drop diagnosis (0 attempts, 4 weeks — Wed first contact, 25 min counts)**, MECE causes.
- Calibration: mean overconfidence −0.15 over 6 judgments (tell is UNDER-confidence on correct reads). Confidence-number-first is a hard gate; state.json writes after every item.
- P4: all topics new — interview prep ramps Phase 2 (Aug+). Monthly STAR audit Mon Jul 6 5pm (standing, cheap).
- **Gating variable is sleep, not the study cue**: misses trace to the late wake, not avoidance of the block. Week 1 of the 9:00 wake: mixed, trending earlier → morning light active from Jul 6, melatonin check Jul 9.

---

**Next moves — W2 (Jul 13–17) is UNPLANNED (Sunday Jul 12 missed); plan it (tripwire 2)**

- **Week-of-Jul-6 outcome:** externship W1 spine ran (kickoff, roles, 5 videos, recap); P3 convert week DELIVERED (LaCroix + Anicito both completed, closed same-day). But P1 US-version produced zero artifact (carry now spans the missed week), P2 study went unpersisted (state.json cold since Jul 3), the wake had no in-system log — then the system fell dark Jul 12–15.
- **Externship (live spine):** mentor meeting today + `/debrief` (tripwire 1); Bryon email send (Izzy) then client meeting; raise Jiada at the mentor meeting. Cosentino case classes/comp now on the calendar (Jul 13, Jul 15) — free P4 reps.
- **Keystone (sleep):** hold the 9:00 wake + morning light; close the melatonin decision (tripwire 4).
- **P1 US version v0:** still not started after ~5 carries — first physical move unchanged (open USITC DataWeb, write line 1); the structural verdict belongs to the belated Sunday.
- **Dr. G (Infisum):** active-routing mode; update him at significant US-version progress.
- **PM Club @ Purdue**: minimal through the Aug–Oct crunch; still open: follow @pmclubpurdue on Instagram.
- **Google APM**: window closes early-to-mid Oct 2026 — the hard anchor (timeline in `context/key-dates.md`).
- **SFF (ruling Jul 5):** off the committed calendar through the APM window; after-3:30 personal time only; never displaces a morning block; stops at the wind-down cue.

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
