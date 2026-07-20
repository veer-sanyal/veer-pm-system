> This file holds CURRENT STATE only — what's shipped, the active focus, next moves, live tripwires.
> Strategy lives in `context/direction.md`; the day-by-day narrative lives in `PROGRESS.md`.
> Keep it a snapshot (~1,500 words max): closed items compress to one line; the story is already in PROGRESS.md.

**Last reconciled: 2026-07-19 (Sun) ~23:15 PT — SUNDAY SESSION RAN (late-night; the second-Sunday miss was averted).** Delta-scan since the 12:55 reconcile found nothing material (one off-strategy IBE-tutor recruiting email, one LinkedIn invite — both ignorable). **W3 (Jul 20–26) is PLANNED AND ON THE CALENDAR:** 18 blocks retitled and re-timed forward from the 11:00 wake anchor (briefing 11:00, deep 11:30–1:00, secondary 2:30, small item 3:30), 6 Morning Briefings written, **Bryon client meeting blocked Mon 3:00pm PT with a 2:30 prep block and a 4:00 /debrief slot**. P7 formalized in patterns.md; the Pillar-1 anchor swap formalized in direction.md (STICK in, US-version retired); ledgers regenerated. iMessage still blind (Full Disk Access not granted); WhatsApp not visible.

---

**Current state**

- **India MSME dashboard — BANKED shipped artifact** (the Pillar-1 interview story until STICK reaches users): live at **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** (static Guided Walkthrough, 4 Acts, exposure score v0 with the EBOPS→NIC caveat surfaced in-UI); telemetry live (GoatCounter, first-week 101 visits, 66% LinkedIn); `DECISIONS.md` through Entry 014; HEAD `84ec4ca`. **US-version: KILLED 2026-07-16** (superseded the Jun-20 commitment; Dr. G told at next natural touch, relationship in active-routing mode).
- **Purdue Daniels Summer Externship, Jul 6 – Aug 1**: team Veer (**Timeline & Project Manager**) + Prisha + Jiada + Izzy; mentor **Shawn Heggland**; client **Scouting America (Sagamore Council)**, contact **Bryon Haverstick (COO)**. Deliverable: **communications + marketing plan** (4 content buckets x 5 audiences + website/social recommendations); statics in `context/externship-scouting-america.md`. W1 done (kickoff, roles, videos, recap); mentor meeting ran ~Jul 15 (Shawn hands-off — see tripwire 1). **Now W3 (review week, Jul 20–26): first client meeting Mon 3pm PT; W4 finals starts Jul 27.** Secondary block yields to externship first; protect the deep block + metrics/stats minimum. Contact rows in `alumni-tracker.md`.
- Application-docs capability lives in this repo (`/apply`); pipeline rows in `context/key-dates.md`. Live rows: **Trice** (handed off to Naveen, WhatsApp-blind — tripwire 3); **Databricks P-982 Ready, unsubmitted** (Thu Jul 23 small item: verify + submit); TikTok submitted via referral Jun 29 (off-strategy, logged); Claude Corps rejected Jun 23.
- **2026-07-16 — PILLAR 1 RE-POINTED TO STICK; formalized in `direction.md` at the Jul 19 Sunday session.** Veer's own correct diagnosis: this system was planning around a dead MSME anchor while his real work lived in `~/Desktop/stick-dev`, so every STICK hour registered as defection. STICK clears the Pillar-1 bar (real user problem, pilot path: MA 16100 Fall 2026); **US-version KILLED**; India v1 = banked ship; Dr. G = warm relationship, not a project. Full narrative in PROGRESS Jul 16; strategy + gates now owned by direction.md.
- **STICK ground truth (audits Jul 16):** the walking skeleton IS built (Vite/React/TS + Supabase + edge functions + FSRS, verified 32/32) but is NOT deployed and **the AI has never run** (`GEMINI_API_KEY` unset), so there is no demo yet; PDF extraction stubbed 501; thesis is n=1, zero student interviews, zero confirmed professor. He experiences it as unbuilt because ~all commits are prose (1/265 touches `app/`). Detail lives in stick-dev + PROGRESS Jul 16.
- Pattern formalized Jul 19 as **P7 ("does the version of the work that cannot reject him") — owned by patterns.md**, incl. the build-around (rejectable artifacts only; weekly minimum 1).
- **Integration posture (done Jul 16, permanent):** CLAUDE.md routes STICK reads to stick-dev (STATE.md first); `/reconcile` scans stick-dev git; `session-start.sh` prints the `app/`-vs-prose ratio with a <10% warning. **HARD RULE: point, never mirror** — stick-dev owns all build state; this file holds only the pillar-level read.
- **Daily workflow (agreed Jul 16, Veer's proposal + one correction).** Open this system first, get pointed at the one thing, go do it. **Correction: there is no "PM work, then STICK" — STICK IS Pillar 1, so most days the one thing IS STICK.** A separate non-STICK item only exists on days someone is waiting (externship meeting, a reply owed, a booked call). **Hard cap: the check-in is ~5 minutes and ends with ONE action, not a plan.** If it runs 20+ min it has become the work (P6 by architecture — the daily front door is the highest-risk place for it). Deep sessions like Jul 16 are rare (monthly at most); the real replan is Sunday.

---

**Live tripwires (as of Jul 15 reconcile; tripwire 0 added Jul 16)**

0. **STICK unblock sequence — top of the board (armed Jul 16, revised order after Veer's correct pushback; gates now owned by `direction.md`).** Order: **(a)** GenAI Studio email — the draft at `outreach/2026-06-27-genai-studio-inference-request.md` is send-ready except ONE now-untrue line ("I have a working prototype"); its answer decides the model stack (OD-36: GenAI Studio hosts Llama/Mistral/Gemma/Phi, spec pins Gemini) and needs no demo. **(b)** Set `GEMINI_API_KEY` + hand-seed one MA 16100 topic + one generated question graded end-to-end = the demo (his own STATE.md owner-action #1). **(c)** Professor early Aug with demo in hand (60-sec myPurdue lookup gets the Fall-2026 MA 16100 name). **The Jul-16 falsifiable test resolved Jul 19 toward the pattern:** +13 commits since, all prose, zero `app/`, key still unset, email still unsent; both tripwires (`stick-genai-studio-email`, `stick-gemini-key-demo`) OPEN, latency 3 days. **Jul 19 Sunday: P7 formalized; the sequence is now carried in W3 block titles — Mon deep block = email + key, Tue = the demo, Sat = demo shown to one person (the weekly rejectable-artifact minimum).** Full reasoning trail: PROGRESS Jul 16 entries.
1. **Externship — first client meeting LOCKED Mon Jul 20 6:00pm ET (Bryon Haverstick); mentor meeting Jul 15 status UNKNOWN.** *Client (new Jul 19):* Bryon replied Jul 16 proposing Mon Jul 20 6pm ET on the "Initial meeting for Scouting America Marketing plan" thread; Izzy confirmed Jul 19 and sends the meeting link Monday. Nothing owed from Veer but to show up prepared (this is W3 review-week; the comms/marketing plan is the deliverable). **Jul 19 Sunday: now ON Google Calendar** (call 3:00–4:00pm PT + 2:30 prep block with 5 scope-discovery questions + 4:00 /debrief small item; Teams link still comes from Izzy Monday). **`/debrief` right after.** *Mentor: DONE — the Shawn meeting happened (~Jul 15).* Veer confirmed Jul 19. Shawn is **hands-off**: "if you guys need anything I'm here," no prescribed tasks. Key steer he gave: **the client often doesn't really know what they want** — which frames tonight's Bryon call as scope-discovery, not a pitch. No same-day thank-you was sent (4 days late now; a short LinkedIn note to Shawn is optional-low-stakes, he's a warm P3 contact). Still open: **raise Jiada's zero visible engagement** at the next team/mentor touch; **(c)** shared-files home (Drive) still unset.
2. **CLOSED Jul 19 (~23:15): `/sunday` RAN** — W3 planned, calendar + briefings written, ledgers regenerated, P7 logged, anchor swap formalized. Residual notes: W2 itself stays on the record as an unplanned week (data for the Aug 2 health check — Sunday cadence wobbling, 1 miss + 1 near-miss in a row); the Jul-15 audit adoption list (Q1–Q6 / S1–S5) stays parked — deliberately NOT taken up tonight (execution week, not system week); Trice sizing still blocked on contact (tripwire 3).
3. **Trice (blind):** the Jul 11 pre-set send day passed with no visibility (no email channel; iMessage/WhatsApp dark). Unknown whether Naveen pinged or Veer messaged him. Smallest action if unactioned: one WhatsApp to Naveen (+91 99490 33255), ref Sudip / Mr Gautham. Agenda unchanged (role family, weekly hours, remote-vs-Hyderabad, + externship disclosure on the call). No hour commitments until sized against real externship hours.
4. **Sleep anchor moved to fixed ~11:00 (Veer, Jul 16) — melatonin CLOSED (HOLD).** Veer reports a consistent alarm-driven ~11am wake and chose to anchor the day at 11:00 for the summer, dropping the `initialize` interrogation. Clock-shift-to-9 is moot at an 11 anchor, so tripwire 4 closes HOLD. Config + caveats (not-yet-verified; walk back toward 9:00 before classes ~Aug 24; Sunday re-verifies from real wake stamps) in `sleep-protocol.md` (2026-07-16 status). Keep one indicator: actual wake time.
5. **Alumni loops closed & healthy** (LaCroix + Anicito — both keep-updated, next touches event-based). One tiny open Anicito move: **send one short text to open the text channel** (his cell, his preferred); unverifiable (iMessage blind) — now Tue Jul 21's small item on the calendar. Optional, low stakes: a short LinkedIn note to Shawn (thank-you is 4 days late; fine to skip).

---

**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; do not hand-edit)

- As of 2026-07-19 regen: **NO study sessions in 16 days** (state.json last write Jul 3 17:32; W2 was a full study zero — P2 evidence logged). All 4 active topics overdue: metric trees 0.62, NSM/guardrail 0.54, numerator-denominator 0.45, **significance/CIs 0.15 (weakest; live crux: inconclusive ≠ proven-no-effect)**. Untouched 6 incl. metric-drop diagnosis (5+ weeks, 0 attempts).
- Calibration tell has FLIPPED: three straight OVER-confident reads on shaky answers (conf 60–80 on Weak/Borderline). Confidence-number-first stays the hard gate; state.json writes after every item, AND the tutor must append the `habits.sessions` row at close (Jun 30 / Jul 3 rows were never appended — known gap).
- W3 targets (in block titles): Tue significance rebuild (teach mode); Wed trees re-test + metric-drop FIRST CONTACT (25 min counts); Fri cold re-tests (num-denom + significance).
- P4: all topics new — ramps Phase 2 (Aug+). Free reps meanwhile: Cosentino ran Jul 13 + 15; next session Mon Jul 20 8pm (on calendar).
- Blocks now plan forward from the **fixed ~11:00 summer wake** (sleep-protocol.md owns it); one indicator kept: actual wake time.

---

**Next moves — W3 (Jul 20–26) planned at the Jul 19 late-night Sunday session. The calendar is written; follow the block titles.**

- **Mon Jul 20 is the hinge day:** deep block 11:30 = GenAI Studio email (open the draft, delete the one untrue "working prototype" line, send) + set `GEMINI_API_KEY`; client call 3:00pm PT (scope-discovery, per Shawn's steer) with 2:30 prep + 4:00 `/debrief`.
- **STICK week-shape (P1):** Tue = the demo end-to-end (one seeded MA 16100 topic, one question generated + graded); Thu = second topic + screenshot; **Sat = show the demo to ONE person — the week's rejectable-artifact minimum (P7 build-around; design/prose commits count as zero).**
- **Externship W3 (review week):** comms/marketing plan through client review (Wed/Thu/Fri per calendar); W4 finals starts Jul 27. Raise Jiada at the next internal team touch, not in front of the client.
- **P2 restart (3 secondaries):** Tue significance rebuild; Wed trees + metric-drop first contact; Fri cold re-tests. Persist state.json + append the session row.
- **P3 (small items):** Tue Anicito text; Wed Trice WhatsApp to Naveen if still unsent (blind — confirm with Veer first).
- **Pipeline:** Thu small item = verify Databricks P-982 still open + submit the Ready resume (built Jul 17; Veer submits himself — don't let it become a P4 park).
- **Google APM**: opens ~mid-Sept, closes early-to-mid Oct 2026 — the hard anchor (`context/key-dates.md`).
- **Rhodes Scholarship (asked Jul 19): parked, no 2026 action** — grad-school path, points away from APM, GPA-filtered; revisit senior year only if the goal itself changes. Logged as a P7-adjacent instance.
- **SFF ruling (Jul 5) stands**: after-3:30 personal time only; never displaces a morning block; stops at wind-down. No bundle activity visible this week (no git repo found at `~/Desktop/study app advisor`).

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
