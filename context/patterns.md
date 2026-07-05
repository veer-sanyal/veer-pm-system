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

**Cost.** Effort that does not compound into a shipped, iterated artifact; focus split across two unfinished projects so neither reaches iterated-with-users.

**Build-around.** Bias to lower sustainable weekly volume (one that survives week 4, 9, 16). Ship v1 in 1 to 2 weeks, iterate weekly, refuse rebuilds of working work. One anchor project, not many. The India dashboard is the anchor; the US version is deliberately scoped as a tight v0 to avoid this pattern. When a second project resurfaces, ask whether it is a genuine pull or avoidance of the harder anchor work before it earns calendar time.

---

## P4. Finishes one click from done, then stalls — ACTIVE

**What it looks like.** A task reaches roughly 90% and parks there. The remaining step is small and known, but it does not get taken without a trigger. A close relative of P1, specific to the last step.

**Evidence.**
- 2026-06: the Dr. G reply complete in Drafts; the Claude Corps app complete but for two courses. Both flagged as one click from done.
- 2026-07-05: externship teammate kickoff email drafted Jul 3, still in Drafts on Jul 5 morning with a hard Jul 6 start — two full days parked one click from send, deadline absorbing the slack (also P5-adjacent).

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

_Last updated: 2026-06-28 (Sunday session) — P2 verdict: build-around holds but the gating variable moved to sleep; P5 verdict: no clean front-load test (confounded by the 11–1 wake), funnel converting on replies, stays TESTING; P3: new evidence — SFF restart on Jun 28._
