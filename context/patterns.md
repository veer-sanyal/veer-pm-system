# Identified Patterns

A living ledger of Veer's recurring behavioral patterns, each with dated evidence and a build-around. The point is forward planning: once a pattern is named and its counter-move is known, the week can be designed to route around it instead of rediscovering it every session.

**Ownership.** This file OWNS the recurring-pattern ledger. `about-me.md` owns the static operating manual (who Veer is, durable psychology); this file is the dynamic, evidence-accumulating layer that tracks how those tendencies actually show up over time and what counters them. Where about-me states a trait, this file logs its dated instances and the evolving counter-move. Cross-link, never duplicate.

**How it self-updates** (maintained during `/reconcile` and `/sunday`):
- A candidate becomes a logged pattern once observed in at least 2 distinct instances.
- When a logged pattern recurs, add the dated instance under Evidence and sharpen the build-around if the counter-move changed.
- If a counter-move is being trialed, mark the pattern TESTING and record the verdict at the next Sunday session.
- Revise or retire a pattern if the evidence stops: mark it DORMANT with the date, never delete the history.
- Maintained during the auto-reconcile (when the session names the week's pattern) and mid-session whenever an instance shows up. Keep it tight. This is a synthesis layer, not a second progress log.

**Status legend:** ACTIVE (currently showing up) / TESTING (a counter-move is being trialed) / WATCH (real but not always a problem) / DORMANT (no recent evidence).

---

## P1. Insight without action (initiation-aversion under uncertainty) — ACTIVE

**What it looks like.** Veer reflects clearly and can name exactly what to do, but the doing stalls. The gap is initiation, not understanding. Second-order reflection ("why am I like this") becomes the avoidance itself.

**Evidence.**
- 2026-06-14 to 16: the Dr. G scheduling reply sat finished in Drafts; sending it was one click and it stalled until named and pinned.
- 2026-06-13 to 18: the Claude Corps application was complete except for two short courses and sat blocked on the smallest remaining step.

**Cost.** High-leverage actions sit at 90% done for days, losing timing and momentum.

**Build-around.** Cue-based starts ("when X, I do Y"), not time slots alone. Shrink the action until starting it takes under 2 minutes. When Veer ruminates, put one small physical action in front of him instead of validating the analysis. Name the avoidance directly when an item stalls a second time. (Durable version in `about-me.md`.)

---

## P2. Reactive over proactive (external deadline beats self-directed work) — ACTIVE

**What it looks like.** In any week with a real external event, the work with a person waiting on the other end gets done, and the self-directed compounding work with no external deadline gets sacrificed, often to zero.

**Evidence.**
- Week of 2026-06-15: the Dr. G call and the Claude Corps submission both landed; Pillar 2 metrics study went to absolute zero (6 scheduled blocks, 0 sessions) and alumni finished 1 of 3.
- Week of 2026-07-13 (W2, unplanned): externship externals all landed (When2Meet filled Jul 7, mentor meeting ran ~Jul 15, client meeting locked) while every self-directed thread went to zero — `state.json` untouched 16 days, zero study blocks, zero outreach. The pattern at full strength whenever Sunday doesn't run.
- Week of 2026-06-22: the cued deep block produced the **first ever study rep** — a 35-min first-contact session Jun 23 (metric trees to an Apply floor; NSM introduced). The Jun 21 build-around got its first rep on the board (tentative win). Caveats: only 1 of ~4 planned study blocks ran, and the session nearly read as zero because the tutor did not persist `state.json` until prompted — a tooling gap, not avoidance. Verdict on whether the full-week habit holds is a Sunday call.

**Cost.** The biggest technical gap (metrics and statistics fluency) is precisely the work most likely to get dropped, because no one is waiting on it.

**Build-around (updated 2026-06-25).** First clean test produced a rep: cued deep block + first-contact teach mode (taught, not interrogated) got the first session done. Keep it — cued start (first 25 min non-negotiable) over the secondary slot that yields first; first-contact teach mode for any topic at mastery 0; pre-commit a non-zero floor in big-external-event weeks. Watch item: persist `state.json` at session close so progress is actually visible (a missed write nearly hid this rep). Verdict on full-week consistency stays a Sunday call.

**Verdict (2026-06-28 Sunday).** Build-around HOLDS *conditionally*: the cued deep block produced 2 sessions this week (after 1 last week), clearing the week's due topics. But only 2 of 4 study blocks ran, and the misses trace to the 11–1 wake (the morning block elapsed before he was up), not to the study cue. So the gating variable has moved upstream to **sleep** (see the sleep-fix workstream). The study build-around is no longer the binding constraint; holding the 9:00 wake is. Keep the cue; the leverage this week is the wake.

---

## P3. Starts strong, then fades (the week-4 / mid-project drop) — ACTIVE

**What it looks like.** High output at the start of a project or stretch, then a fall-off. Projects get started and not finished; the urge to rebuild before launching is the specific failure mode.

**Evidence.**
- StudyFlowForge ran Feb to Apr 2026 and was dated honestly as a finished past artifact rather than restarted.
- Stated tendency confirmed across the profile: starts projects, does not finish.
- **2026-06-28: Veer restarted StudyFlowForge** ("a project I want to work on") — the exact move this pattern warns against (returning to an old project / second anchor) at a moment when the dashboard still has open items (the US-version commitment to Dr. G), the externship starts Jul 6, and the metrics habit is only two sessions old. Reversal of the Jun 9 "keep SFF a finished artifact, one anchor" decision. Flagged for a genuine-pull-vs-avoidance check, not folded into the plan.
- **2026-07-05 (RESOLVED at the Sunday session): genuine pull, bounded.** The "restart" turned out to be a disciplined greenfield SPEC project (`~/Desktop/study app advisor`: 33 components locked, decision engine, graded research; no code, explicitly not reusing the old app). Not avoidance — but it consumed Jul 4's morning blocks and ran to 1:30am against the wind-down. Ruling: off the committed calendar through the APM window; lives in after-3:30 personal time; hard boundaries = never displaces a morning block, stops at the wind-down cue. The P3 risk being managed is no longer "will he restart it" but "will spec-world eat ship-world" — watch the boundary, not the project.

**Cost.** Effort that does not compound into a shipped, iterated artifact; focus split across two unfinished projects so neither reaches iterated-with-users.

**Build-around.** Bias to lower sustainable weekly volume (one that survives week 4, 9, 16). Ship v1 in 1 to 2 weeks, iterate weekly, refuse rebuilds of working work. One anchor project, not many. The India dashboard is the anchor; the US version is deliberately scoped as a tight v0 to avoid this pattern. When a second project resurfaces, ask whether it is a genuine pull or avoidance of the harder anchor work before it earns calendar time.

---

## P4. Finishes one click from done, then stalls — ACTIVE

**What it looks like.** A task reaches roughly 90% and parks there. The remaining step is small and known, but it does not get taken without a trigger. A close relative of P1, specific to the last step.

**Evidence.**
- 2026-06: the Dr. G reply complete in Drafts; the Claude Corps app complete but for two courses. Both flagged as one click from done.
- 2026-07-05: externship teammate kickoff email drafted Jul 3, still in Drafts on Jul 5 morning with a hard Jul 6 start — two full days parked one click from send, deadline absorbing the slack (also P5-adjacent).
- 2026-07-05 (counter-evidence, build-around working): both parked sends (kickoff email, Trice reply) closed within ~20 minutes of the last action being named while Veer was live in-session. Naming the single physical move works; the gap is that nothing names it between sessions. The Morning Briefing now carries the day's last-action tripwires for exactly this reason.
- 2026-07-23: the Bryon thank-you/recap, drafted at the Mon Jul 20 debrief with "sends tonight" on record, still in Drafts Thu — 3 days parked one click from send while Bryon delivered his own promised artifact Mon night and got silence. Same shape as the kickoff email; the between-sessions gap again (no briefing carried it after Mon).
- 2026-07-25 (same item, escalated): still unsent at **5 days**, and the deadline it was pegged to — send it before the Thursday team meeting — passed without the send. Naming the last action in-session (Jul 23) was not enough this time; the send only closes when it happens *during* the session. Adjustment to the build-around: when a parked send is named and the session ends without it going out, treat the naming as failed and do the send inside the session before moving on.
- 2026-07-26 (same item, **third escalation, 6 days**): the Jul-25 amendment was written and then not applied to this item — the session that wrote it closed two other sends live (Naveen, GenAI Studio) and left this one in Drafts. It was even logged as sent in error before Veer corrected it. Three sessions have now named this exact draft. **The amendment is upgraded from guidance to a rule: a send that has been named in two consecutive sessions does not get named a third time — it gets done first, before any other work in the session, or it is explicitly killed as no-longer-worth-sending.** A draft the system re-lists weekly is a system pretending to track something it is not moving.

- 2026-07-30 (same Bryon item, **sixth naming, 10 days**): still in Drafts. The Jul-26 rule ("named twice = done first in the session or explicitly killed") has now failed four times running. Recorded here as evidence that **the rule itself is the failure**, not the item: a rule that fires inside a session cannot move an item on days when the session does not open with it. No seventh rewrite of the rule — it goes to Veer as a binary. **Counter-evidence the same day:** the RCAC thread shows the opposite behaviour — Veer opened a second ticket unprompted at 04:42 and it converted into a meeting offer by 16:26. The pattern is not "he cannot send things"; it is specific to sends that have aged past their original purpose.

- 2026-08-03 (**the pattern stops being about one draft — FOUR simultaneous, plus a new sub-shape**): every outbound message owed to a human is unsent at once. **Bryon 14 days** (seventh naming) · **Mihir Ahlawat / RCAC 4 days**, where the man asked for times "next week" and that week arrived unanswered · **Naveen 5 days** · **Sudip Uncle never messaged at all** about a call he brokered · **Storie Pedley 4 days**. Combined send time: **under ten minutes.** Against that, 35 stick-dev commits landed in the same four days. **Logged as one instance, not four** — four independent stalls on the same day is not coincidence, it is the behaviour. **The new sub-shape, and it is the sharpest evidence yet: revision as avoidance.** The Naveen note was written as a file Jul 30 23:20, then **edited twice more on Aug 1** — 06:00 "name Nextdoor, cut 'that's honest', re-time the opener" and 06:37 "state the STICK omission plainly, drop the apology" — **and still not sent.** Both edits made it a better note. Both made it later. Editing a draft is indistinguishable from working on it and cannot reject him, which is where P4 and P7 turn out to be the same mechanism seen from two ends. **Instrument consequence: a second revision pass on an unsent message is now itself the tripwire.** When a draft gets edited without being sent, the next action is send-as-is with a re-timed opener, never another pass.

- 2026-08-05 (**strong counter-evidence, and it should be cited before the dread argument runs again**): all five of the Aug-3 stalled sends went out within ~48 hours of being named as one behaviour. Bryon's landed Aug 4 and came back **"This is an amazing start!!! Unbelievable work!!"**; the RCAC times reply converted into a booked meeting; Naveen's note drew a 👍 inside the hour; Storie and Sudip both went. **Every human who replied replied warmly.** Fifteen days of accumulated dread on the Bryon item resolved to enthusiasm from a message that took minutes. The predictive claim P4 rests on — that the send is dangerous — was falsified five times in two days.

- 2026-08-07 (**a new variant, one instance, below the 2-instance bar: the returned ball**). Every P4 instance logged before this was an *unsent* message. This one was sent, landed, and produced a warm reply inside ~80 minutes — **Sudip Uncle, Wed Aug 5 7:18 PM: "Sure ... I am fine anytime late-night IST works better let say after 10 PM IST tonight or tomorrow"** — and then the thread sat two days while both offered windows expired. **The hard part succeeded and the loop still did not close, because closing it needed one more small action after the win.** No scheduling obstacle existed: 10:00 PM IST is 11:30 AM in his local zone, half an hour clear of his own 11:00 floor. The cost lands on someone doing him a favour, which is the same cost shape as the Bryon silence. **Build-around candidate, do not adopt until a second instance: a send tripwire does not close on "sent", it closes on "a time exists."** Watch specifically for replies that arrive fast and warm — the speed of the reply appears to be what removes the urgency.

- 2026-08-09 (**the binary rule actually fires**): both Sudip (3 expired windows) and Mama (16 days) hit the "named 3+ sessions" threshold at the Sunday reconcile, and instead of a fourth re-draft, Veer chose to send both live rather than kill either — the rule worked as designed for the first time since it was written Jul 26. Worth watching whether the sends actually go out (Mama is one Gmail click away; Sudip has no send tool in this system and needs Veer's own tap), since choosing to send in-session and the send actually happening are not the same event, per the Jul-25 lesson.

**Cost.** The last 10% carries most of the value (the sent message, the submitted app), so stalling there forfeits the payoff of work already done.

**Build-around.** Name the single smallest physical last action and make it the tripwire ("open the draft, change one sentence, hit send before 9:15"). Do not re-list the whole task; decompose to the final move.

---

## P5. Outreach and admin batch to the deadline, then under-deliver — TESTING

**What it looks like.** Recurring small-volume commitments (alumni messages) get deferred toward the end of the week and then mostly miss.

**Evidence.**
- Week of 2026-06-15: all 3 alumni messages were spread across the week, slipped to the end, and only 1 went out.

**Cost.** The 3-per-week funnel the whole networking plan depends on does not actually run at 3.

**Build-around (testing, week of Jun 22).** Front-load the 3 sends to Monday through Wednesday instead of spreading them to Saturday. Verdict to be recorded at the Sunday Jun 28 session: did front-loading raise the hit rate?

**Verdict (2026-06-28 Sunday): no clean test — confounded by the wake problem.** New cold sends finished 1 of 3 again (LaCroix only, and it slipped to Thu); Akash + Allan never went. But the Mon–Wed slots fired during the 11–1 wake window, so front-loading failed for the sleep reason, not batching-per-se. Two mitigating facts: the funnel is now converting on *replies* (2 sent → 2 replies → 1 call booked), so raw send-count is a weaker bottleneck than relationship conversion; and the free-connect-note quota (~3–5/month) caps volume anyway. Action: re-test front-loading once the 9:00 wake holds; meanwhile weight P3 toward converting live calls + comment-then-message over hitting a rigid 3-cold-send number. Stays TESTING.

---

## P6. System-optimization can become the work — WATCH

**What it looks like.** Refining the planning system, drafting, or re-analyzing can substitute for executing the pillars. Not always avoidance (Sunday is the right time for structural change), but worth checking when it happens mid-week or in place of a stalled action.

**Evidence.**
- Repeated system rebuilds (2026-06-04, 06-15, 06-18, and this patterns doc on 06-21) were genuine improvements, but the standing guard exists because the urge can mask avoidance.

**Cost.** Hours spent past the marginal-hour point buy polish, not progress.

**Build-around.** Structural changes happen at the Sunday session, capped at the marginal-hour point (more than 90 minutes per week refining the system means stop and ship). When a system tweak is requested mid-week or exactly when a hard action is due, name it and redirect to the action.

---

## P7. Does the version of the work that cannot reject him — ACTIVE

**What it looks like.** Effort routes to the form of the work where no human or runtime can say no: documentation, specs, design passes, rubrics, system audits, researching new goals. The rejectable form of the same work (a send, a deploy, a run, a person shown) sits untouched, however small. Sharper than P1 (this isn't failure to start — he works hard, at the wrong valence) and than P6 (it covers product work, not just system work). Documentation cannot say no; a professor, an API key, or a client can.

**Evidence.**
- 2026-07-16 (STICK audit): >1.1MB of prose about a ~150KB app (8x); 97/101 spec components LOCKED behind a formal challenge-bar on an n=1 premise; 103 agents run verifying a report while `GEMINI_API_KEY` — his own STATE.md owner-action #1 — sat unset; the GenAI Studio email draft gated on "working prototype exists," condition met, never sent; zero outreach ever on the pilot.
- 2026-07-17 to 19 (the falsifiable test, resolved): the Jul 16 test was "key set this week → demo was the blocker; another design pass → the demo was the gate." Result: +13 commits, ALL prose (D176/D177 design sweep), zero `app/`, key still unset, email still unsent. The test resolved toward the pattern, on the record.
- 2026-06-29 to Jul 15 (US-version, 5 carries): same shape earlier — the scope doc that no one could reject never even got written; the block work it displaced was always documentation-flavored.
- 2026-07-19 (~10:45pm, live): with `/sunday` unrun and both STICK tripwires open at 3 days, the session opened with a Rhodes Scholarship question — a maximally prestigious goal three years away that cannot reject him in 2026. Named in the moment; parked; `/sunday` ran.
- 2026-07-25 (**the pattern's disguise changes**): W3 carried exactly one rejectable artifact in a block title — "show the demo to one person, design work does not count." The block window passed with zero people shown, while 15 `app/` commits landed in two days (Slice 2, admin shell, migrations, a Gemini model swap). The prose-vs-code instrument reads *healthy* and the pattern is still running: shipping product code into a repo nobody has looked at is as unrejectable as writing specs about it. **Consequence for the instrument:** the `app/`-ratio is now confirmed necessary-but-not-sufficient (the F5 gameability watch-item, arrived at honestly rather than by padding). The pillar metric is the artifact shown to a human, and only that.

- 2026-07-26 (**the pattern acquires a fake gate**): 13 more `app/` commits landed Sunday — Slice 2 closed through step 11, D192 owner-actions all cleared, a `/cairn:audit` run, a WCAG sweep, a queue cleanup. The step-11 milestone is literally named **owner-verify**, and OPEN-DECISIONS records "all three found by *the owner* clicking the deployed gate." That is the pattern's most sophisticated form yet: a verification ritual that looks exactly like the gate — it has a name, a pass/fail, findings, rulings — and cannot reject him, because he is both the user and the judge. The weekend that was supposed to close the human gate moved the counter from zero humans to zero humans. **Instrument consequence:** "verified" in stick-dev now has to be read for *who did the verifying*. Owner-verify is a code-quality gate, not a pillar artifact, and does not count toward the weekly minimum.

- 2026-07-30 (**the cleanest instance on record, because the excuse was named and then removed in one day**): the Jul-29 reconcile gave a specific diagnosis — the demo was embarrassing to show (sign-in said "StudyFlow", a confirmed calendar rendered "stage 8 of 4", failed files read "failed at undefined") and the dev DB had been empty since Jul 27, a **five-minute re-enroll**. Within 24 hours **all three defects were closed** (OD-146→D239, OD-152→D226, OD-153→D227) across **10 `app/` commits, the largest single-day product-code run in the repo's history** — and **the five-minute re-enroll did not happen, and no human saw the app.** Fourth consecutive deep block named for the gate, fourth zero. **What this establishes:** the stated blockers are real work that gets done fast when named, and they are not what is blocking. Naming a blocker reliably produces the *fixable* version of it. The gate is the person, and only the person.

- 2026-08-03 (**highest amplitude recorded — the unrejectable form acquires statistical validation**): Aug 2 produced the largest single research day in the repo's history. A **148-agent workflow**, three graded reports (**U** Purdue document topology, **W** multi-topic algorithm design, **X** the update-rule adjudication), a **3-rater inter-rater reliability study returning κ=0.915**, and a 76-item corpus count — all to select a mastery-blame update rule (D267) for an app **no human outside Veer has ever opened.** Four-day totals: **35 commits, 2 touching `app/`.** Day eight at zero humans; grep for student/professor/pilot/user-test/enroll across all 35 commits returns nothing; STATE.md's measured dev DB still reads **sections 0 · enrollments 0 · attempts 0**, so the five-minute re-enroll is now five days old. **What is new here:** the research is *good* — U's finding that 6 of 7 verified Purdue Math syllabi contain no week-by-week grid is real and load-bearing, and the inter-rater test corrected Veer's own 46% down to 34–38%, a correction he published against himself. **That is precisely why it is the strongest instance.** The unrejectable form has evolved from documentation into genuine research with adversarial review and reproducibility statistics attached — work that is more defensible, more effortful, and more rigorous than the thing it displaces, and still cannot say no to him. **The same four days produced zero of the five messages that could.** State the pair together and no capacity explanation survives: a κ=0.915 study got done on a Sunday; ten minutes of sends did not.

- 2026-08-09 (**the ratio keeps climbing, the gate stays at zero, day 13**): `app/` ratio 21.4% of the last 14 days, up from 16.3% a day earlier — the trend line the instrument was built to reward keeps improving, and it still cannot substitute for the one thing that closes the gate. New wrinkle: a genuine technical blocker surfaced this session (D52, no student-data reads possible) that does NOT actually block the gate action (a single in-person observation needs no database read) but is exactly the shape of fact that could get mistaken for a reason to wait. Named explicitly so it doesn't become excuse layer number six.

**Cost.** The pilot, the professor, and the demo — the things the entire Pillar-1 story depends on — receive zero minutes while the effort meter reads full. 1/265 commits touching product code is what this pattern looks like in telemetry. Two weeks later, 66/490 commits touch product code, every named defect is closed, and the number of humans who have used it is still zero.

**Build-around.** Pillar-1 progress is counted ONLY in rejectable artifacts: something external that can fail or say no (a send, a deploy, a key set + first run, a user shown). Design/spec/doc commits count as zero toward the pillar regardless of volume — the `session-start.sh` app/-vs-prose ratio instrument makes this visible every session. Weekly minimum: one rejectable artifact, named in the Sunday plan and carried in a block title. When a design pass is proposed while a rejectable action sits open, name P7 and put the under-2-minute starter of the rejectable action in front of him instead.

---

_Last updated: 2026-08-09 (`/sunday`) — P4: the binary send-or-kill rule actually fired for the first time (Sudip + Mama, both named 3+ sessions) — Veer chose to send both rather than kill either; watch whether the sends land. P7: `app/` ratio kept climbing (21.4%, up from 16.3%) with the gate still at zero on day 13; a real technical blocker (D52, no student-data reads) surfaced but was named explicitly as not actually blocking the gate action, to keep it from becoming a sixth excuse layer. Earlier: 2026-08-07 (`/reconcile`) — P4: two entries added, and they point opposite ways. **Counter-evidence (Aug 5):** all five stalled sends went out inside ~48 hours of being named as one behaviour, and every human who replied replied warmly — cite this before the dread argument runs again. **New variant (Aug 7), one instance, below the bar: the returned ball** — Sudip answered in ~80 minutes and the reply sat two days until both his offered windows expired, so the loop failed *after* the hard part succeeded. Candidate build-around held in reserve: a send tripwire closes on "a time exists", not on "sent". P7: no new instance this session, but its shape moved — STICK's `app/`-commit ratio hit ~31% of a three-day window (52 of 170) while the dev DB stayed at zero humans on day 12, so the unrejectable form has evolved again, from documentation to research to **tuning**. Earlier: 2026-08-03 (`/reconcile`) — P7: highest-amplitude instance recorded (the Aug 2 148-agent research block with κ=0.915 inter-rater validation, against day eight at zero humans); the unrejectable form has evolved from documentation into rigorous research. P4: four simultaneous unsent messages logged as ONE instance, plus a new sub-shape — **revision as avoidance** (the Naveen note edited twice on Aug 1 and still unsent), with the instrument consequence that a second revision pass on an unsent message is now itself the tripwire. Earlier: 2026-07-26 (`/reconcile`) — P7: new evidence, owner-verify identified as a fake gate (he is both user and judge); "verified" now has to be read for who verified. P4: Bryon send at 6 days, third escalation — build-around upgraded to a rule (named twice = done first or killed). Earlier: 2026-07-25 (`/reconcile`) — P7: new evidence, the pattern survived the metric (product code up, people shown still zero) → `app/`-ratio confirmed necessary-but-not-sufficient; P4: Bryon send escalated to 5 days, build-around amended (close named sends inside the session). Earlier: 2026-07-19 (Sunday session) — P7 logged (formalized from the Jul 16 candidate; the falsifiable test resolved toward the pattern); P2: new evidence — W2 externals landed, self-directed at zero for 16 days. Earlier: 2026-06-28 — P2 verdict: build-around holds but the gating variable moved to sleep; P5 verdict: no clean front-load test (confounded by the 11–1 wake), funnel converting on replies, stays TESTING; P3: new evidence — SFF restart on Jun 28._
