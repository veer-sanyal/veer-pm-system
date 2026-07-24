> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-23 (Thu) ~13:40 PT** — sources: stick-dev git + STATE.md, Gmail, Calendar; iMessage/WhatsApp blind. Open deltas: **(1)** Bryon delivered his 12-mo Communication Grid Excel (Mon; "promotions begin 90-120 days in advance") — thank-you/recap **STILL in drafts, 3-day slip (P4)**; send before the Thu team meeting, acknowledge the Excel. **(2)** STICK moved: G0 CLOSED Jul 22, Slice 1 + battery CLOSED Jul 23 (61/61); demo proper still awaiting owner; **GenAI Studio email unsent, 7-day latency** — Sunday decides if the OD-36 gate still holds. **(3)** SMIF bios reminder Jul 22 (new contact smif26@purdue.edu) — submit status unknown, ask Veer. **(4)** Team plan meeting Thu 3pm PT / 6pm ET (Prisha + Izzy confirmed; Jiada dark). Client-call recap sent to team Mon (Prisha briefed). Quiet: Databricks (Thu = submit), Trice (ask if Naveen replied), LinkedIn, Shawn/Storie.

---

**Current state**

- **India MSME dashboard — BANKED artifact** (the Pillar-1 interview story until STICK reaches users): live at **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** (Guided Walkthrough, exposure score v0 with EBOPS→NIC caveat in-UI; GoatCounter live); `DECISIONS.md` through Entry 014; HEAD `84ec4ca`. **US-version KILLED 2026-07-16.**
- **Purdue Daniels Externship, Jul 6 – Aug 1**: team Veer (**Timeline & PM**) + Prisha + Jiada + Izzy; mentor **Shawn Heggland**; client **Scouting America (Sagamore Council)**, contact **Bryon Haverstick (COO)**. Deliverable: comms + marketing plan. **Now W3 (review week, Jul 20–26); W4 finals starts Jul 27.** Externship takes priority over the secondary block. Statics: `context/externship-scouting-america.md`; contacts in `alumni-tracker.md`.
- Applications via `/apply`; pipeline rows in `context/key-dates.md`. Live: **Trice** (handed to Naveen, WhatsApp-blind — TW3); **Databricks P-982 Ready, unsubmitted** (Thu = verify + submit). TikTok submitted Jun 29 (off-strategy); Claude Corps rejected Jun 23.
- **PILLAR 1 = STICK** (re-pointed 2026-07-16, formalized in `direction.md` Jul 19). The system was planning around a dead MSME anchor while the real work lived in `~/Desktop/stick-dev`, so every STICK hour read as defection. STICK clears the Pillar-1 bar (real user problem; pilot path MA 16100 Fall 2026). **HARD RULE: point, never mirror** — stick-dev owns all build state; memory holds only the pillar read (moving or not, in front of a user or not, next physical action).
- **STICK ground truth (Jul 20):** walking skeleton built (Vite/React/TS + Supabase + edge + FSRS, 32/32) and **the AI has run live** (GEMINI_API_KEY set as Supabase secret; real extraction verified 4/4 MCQs). Open: demo proper, GenAI Studio email, thesis n=1, zero student interviews, zero confirmed professor. Commit mix still ~all prose. Detail in stick-dev + PROGRESS.
- **P7 formalized Jul 19** ("does the version of the work that cannot reject him") — owned by `patterns.md`; build-around = rejectable artifacts only, weekly minimum 1.
- **Integration (Jul 16, permanent):** CLAUDE.md routes STICK reads to stick-dev (STATE.md first); `/reconcile` scans its git; `session-start.sh` prints the `app/`-vs-prose ratio with a <10% warning.
- **Daily workflow (Jul 16):** open this system first, get pointed at ONE thing, go do it — most days the one thing IS STICK. A non-STICK item only exists when someone is waiting. Check-in ~5 min, ends with ONE action not a plan; 20+ min means it became the work (P6 by architecture).

---

**Live tripwires**

0. **STICK unblock sequence — top of the board** (armed Jul 16; gates owned by `direction.md`). **(a)** GenAI Studio email — draft `outreach/2026-06-27-genai-studio-inference-request.md` send-ready except one now-untrue line ("working prototype"); **still unsent, 7-day latency**; Sunday decides whether its model-stack purpose (OD-36) still holds now Gemini is live. **(b)** Demo proper — HALF done (key set + extraction verified); OPEN for topic seeded + question generated + graded end-to-end. **(c)** Professor early Aug with demo in hand. Reasoning trail: PROGRESS Jul 16.
1. **Externship first client meeting RAN Mon Jul 20** (Veer + Izzy live; Prisha absent, Jiada dark), debriefed same day. Went well; Bryon warm, gave **cell 765-250-6139** + IG/FB/X handles. **Plan params locked:** FB-first (3,000 vs 178 IG), organic only / $0 budget, ~30 min/day across ~6 pages, priority audience parents ~24-26 w/ K-1st, success = engagement laddering to money + membership. **Open loops:** (a) his Communication Grid Excel landed Mon (90-120-day promo rule) — fold in; (b) **thank-you/recap in drafts 3 days (P4) — send before Thu meeting**; (c) timeline-drift flag for Sunday (delivery may extend past Aug-1; W4 final still Aug 1, logistics undiscussed); (d) raise Jiada internally (Izzy already named it to the client). Facts/quotes: `ledgers.md` relationships log; transcript `networking/bryon-call-transcript-2026-07-20.md`.
2. **CLOSED Jul 19: `/sunday` RAN** — W3 planned, calendar + briefings written, ledgers regenerated, P7 logged, anchor swap formalized. Residual: W2 stays on record as an unplanned week (data for the Aug 2 health check); the Jul-15 audit adoption list (Q1–6 / S1–5) stays parked.
3. **Trice — Naveen WhatsApp SENT** (Veer, Jul 21). Ball with Naveen; channel WhatsApp-blind → **check with Veer Thu Jul 24 if nothing surfaces**. Agenda: role family, weekly hours, remote-vs-Hyderabad + externship disclosure. No hour commitments until sized against real externship hours.
4. **Sleep anchor fixed ~11:00** (Veer, Jul 16) — melatonin CLOSED (HOLD). Walk back toward 9:00 before classes ~Aug 24; Sunday re-verifies from real wake stamps. Config + caveats in `sleep-protocol.md`. Keep one indicator: actual wake time.
5. **Alumni loops closed & healthy (Jul 19):** LaCroix + Anicito both keep-updated, next touches event-based. Optional, low stakes: a short LinkedIn note to Shawn (fine to skip).
6. **Family side-thread OPENED Jul 23:** Mama (Bangalore doctor, VC-funded) sent a prototype spec (external-sealing enema nozzle), asked for a look; **Veer's reply overdue.** Research done (2 adversarially-verified runs): CDSCO Class A via SLA MD-3→MD-5 path; FDA 876.5210 Class I exempt but "inserted" wording risk (no non-inserting 510(k) precedent); **STERILAB patent US9227006B2 ACTIVE to Aug 2032 claims the generic external-sealing mechanism (the call headline)**; vendors Spectroplast / Ami Polymer / iMake. Call sheet: `networking/mama-enema-nozzle-call-prep.md`. Next: WhatsApp reply + schedule call (Fri/Sat IST). Bounded: do not displace STICK gates or externship W4.

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-07-19: **NO study in 16 days** (state.json last write Jul 3; W2 a full study zero, P2 logged). All 4 active topics overdue: metric trees 0.62, NSM/guardrail 0.54, num-denom 0.45, **significance/CIs 0.15 (weakest; crux: inconclusive ≠ proven-no-effect)**. Untouched 6 incl. metric-drop diagnosis (5+ weeks, 0 attempts).
- Calibration tell FLIPPED: three straight over-confident reads. Confidence-number-first stays the hard gate; the tutor must append the `habits.sessions` row at close (known gap).
- P4: all topics new — ramps Phase 2 (Aug+). Free reps: Cosentino ran Jul 13 + 15.

---

**Next moves — W3 (Jul 20–26), calendar written; follow the block titles**

- **STICK (P1):** demo end-to-end (seeded MA 16100 topic, question generated + graded); second topic + screenshot; **Sat = show the demo to ONE person (weekly rejectable-artifact minimum, P7).**
- **Externship W3:** comms/marketing plan through client review; W4 finals Jul 27; raise Jiada at the next internal touch, not in front of the client.
- **P2 restart:** significance rebuild; trees + metric-drop first contact; cold re-tests. Persist state.json + append the session row.
- **Pipeline:** Thu = verify Databricks P-982 still open + submit (Veer submits himself).
- **Google APM:** opens ~mid-Sept, closes early-to-mid Oct 2026 — the hard anchor (`context/key-dates.md`).
- **Rhodes:** parked, no 2026 action (grad-school path, points away from APM).
- **SFF ruling (Jul 5) stands:** after-3:30 personal time only; never displaces a morning block; stops at wind-down.

---

**Operating principles** (durable)

- The **deployed GitHub Pages site is ground truth** for what's shipped — not the README, not memory.
- Check live artifacts and prior context BEFORE planning, not after.
- When Veer proposes system improvements, distinguish genuine improvement from avoidance (P6) and name the real problem.
- Communication: direct and short; flag flaws before building, with concrete alternatives and honest trade-offs.

---

**Tools & resources**

- Product repo: `veer-sanyal/india-msme-digital-trade-exposure` (public) · live site above · static HTML/CSS + client-side Plotly; Python (pandas) builds the processed CSVs and `site/data.js`.
- This planning repo: `veer-sanyal/veer-pm-system` (PRIVATE). `gh` CLI authenticated as veer-sanyal; git works natively.
