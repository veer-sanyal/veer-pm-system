# Scheduling Blueprint

This file is the rules the daily planner follows when building each day and each week. It exists because Veer's failure mode is not knowledge — it's execution over months — and the planner has to be governed by what the evidence actually supports, not by productivity-culture defaults.

The sources behind every claim here are in the project research files. This document is the operating distillation.

---

## First principles

1. **Long-horizon consistency beats heroic surges.** Every design choice in this system should favor sustainability over intensity. A weekly volume Veer can hit for 40 weeks beats a volume he can hit for 6.

2. **Cued behavior beats motivated behavior.** Implementation intentions (if-then plans linking a cue to an action) are the single best-evidenced bridge between intention and behavior. Every commitment in the daily plan needs a trigger, not just a time.

3. **Visible progress is part of the work.** Monitoring effects are stronger when progress is recorded and made public. The tracking is not bureaucracy — it's the intervention.

4. **Recovery is execution, not reward.** Sleep, exercise, and breaks have moderate measurable effects on the cognition this plan depends on. Skipping them is a performance loss, not a sign of seriousness.

5. **Action interrupts rumination.** When Veer drifts into explanation, optimization, or self-diagnosis, the system's job is to put a small physical action in front of him, not to validate the analysis.

---

## Daily structure

Each day should contain, in this rough shape:

### One protected deep work block (75-90 minutes)

The research on ultradian rhythms is mixed — Kleitman's 90-minute cycle hypothesis has some support, but evidence for a robust universal waking-performance rhythm is weaker than productivity culture implies. What the research strongly supports: uninterrupted time of meaningful length, with breaks before quality collapses. The attention-residue and interruption-cost research is much stronger and clearer — switching between tasks carries hidden cost that compounds over the day. So:

- One protected block, 75-90 minutes, same time of day, same physical location
- Phone physically out of reach. Browser tabs closed. Project doc already open from the night before.
- Cue: a specific physical action (sitting in the chair, opening the laptop, putting on headphones). Implementation intention format: "When I sit at [location] after [trigger], I open [project] and do [first move] for 25 minutes before deciding anything else."
- The first 25 minutes are non-negotiable. After that, Veer can decide if he keeps going.
- This block is for the hardest pillar work — shipping the project, technical learning, or interview prep. Not for admin, email, or planning.

### One secondary work block (45-60 minutes)

For the second-priority pillar of the day. Different category from the deep block to reduce attention residue. Same cue + start-action structure.

### One small-but-visible item

Something that takes 15-30 minutes and produces a visible artifact: sending one alumni message, drafting one resume bullet, completing one Anki review, doing one practice problem out loud. The point of this item is to guarantee at least one shipped output even on bad days. Without it, days where Veer "didn't feel like deep work" become zero-output days.

### Recovery and sustainability inputs

These are not optional and not negotiable:

- 7-8 hours sleep target (sleep deprivation has measurable cognitive cost; sleep supports memory consolidation)
- Workout — Veer already does this; preserve it
- Skincare routine at night — already a habit; preserve it as a stable end-of-day cue
- One genuine social interaction or non-instrumental moment — protects against the "optimized but hollow" failure mode the college-as-leverage research documents

---

## Weekly structure

### Sunday planning session (30-45 minutes)

This is the most important meeting of the week. The architecture works only if this happens.

Sequence:
1. Review what you committed to last week (5 min) — what shipped, what didn't, what slipped
2. Identify the pattern, briefly — not deep diagnosis, just naming (5 min)
3. Define the next week's commitments by pillar (15 min) — specifically what gets shipped, learned, sent, practiced
4. Translate each commitment into an implementation intention with a specific cue (10 min)
5. Block the calendar yourself — deep work blocks, secondary blocks, alumni-outreach time (10 min)

Output: the next week's daily emails get drafted with these specifics and scheduled to send.

### Weekly volume targets (sustainable, not heroic)

These are starting baselines. They can adjust up or down based on what's actually working. The bias is toward lower-and-consistent.

- Project work: 6-8 hours
- Technical learning: 3-4 hours
- Alumni outreach: 3 messages sent + 1 informational interview where possible (3/week is the volume the 20+ informational-interview target requires over the year)
- Interview prep: 1 mock or 3 solo reps (out loud, recorded)
- One Sunday session
- One Friday review (10 min — what went right, what slipped, no fixing yet)

### Recovery week every 6-8 weeks

A scheduled lower-intensity week. Volume targets drop by 40%. This is not a reward — it's how the system survives 10 months. The research on burnout is clear: sustained-stress cognition is impaired, and intermittent recovery improves total output.

---

## How the daily plan is delivered (Google Calendar)

The plan is delivered as Google Calendar events, not email. The Gmail connector can only draft, not send or schedule, so a scheduled morning email was never buildable. The calendar pushes to Veer's phone without him initiating, which is the whole point. Full spec in `daily-email-instructions.md`.

Each day carries:

1. **Three work-block titles** that name the specific action, so the reminder itself is the trigger. Example: "Deep block: add telemetry to the dashboard (Pillar 1)." Pulled from Sunday's plan, phrased as implementation intentions.

2. **A 9:00 Morning Briefing event** whose description holds the accountability question for yesterday ("Did the deep block start on time? If not, what got in the way?"), the one-sentence "this week feeds," and an optional citation. The calendar has no reply, so Veer brings the answer to the Sunday session or notes it in PROGRESS.md.

3. **One sentence of context, not motivation** inside that briefing: what pillar this serves, why this week matters. Not "you can do it."

What the daily plan does not contain:
- Inspirational language
- More than 3-4 items
- Anything Veer didn't commit to on Sunday (the planner doesn't get to add things mid-week)
- Reminders of the long-term goal (over-reminding causes goal-gradient demotivation; the long-term goal stays at the strategic level, not the daily level)

The recurring blocks (deep 9:45, secondary 11:45, workout 1:00, small item 2:30, Pacific) hold the times. Each Sunday the session retitles that week's blocks and writes the six briefings.

---

## Specific science-backed protocols this system uses

### Implementation intentions (Gollwitzer)
Every commitment is phrased as "When X, I do Y." Not "do Y at 10am." The cue is the trigger, not the clock.

### Mental contrasting with implementation intentions / WOOP
Used during Sunday planning when a commitment is at risk: name the wish, visualize the outcome, identify the specific inner obstacle, build the if-then for when the obstacle shows up. Small-to-medium effect on goal attainment in meta-analysis.

### Proximal goals with feedback (Bandura, Schunk)
The 10-month goal is too distant to drive daily behavior. The planner translates it into weekly proofs: proof of shipping, proof of volume, proof of skill progression, proof of feedback gathered.

### Behavioral activation

When Veer is ruminating, drafting messages he won't send, or refining the plan instead of executing, the planner's response is one specific small physical action ("open the project tracker now, write one sentence"). Not "let's talk about why."

The framing matters here. The research is explicit that **procrastination is increasingly understood as short-term mood regulation** — the task feels aversive, so the brain chooses immediate emotional relief at the expense of the future self. This is not laziness or weak will. It's the system working as designed.

The implication for how the planner should respond: don't tell Veer to "be more disciplined." The task feels aversive, that's real, and his brain is doing what brains do. The fix is to shrink the action enough that it doesn't trigger the aversion — "open the doc and write one sentence" beats "do a real work session." Once the aversion is bypassed, the resistance often dissolves on its own.

### Pre-performance routines
For mock interviews and real interviews: one minute slow exhale, one cue phrase ("arousal is fuel"), one glance at three anchor stories, deliberately slow opener on the first question.

### Reappraisal over suppression
Before interviews: telling yourself anxiety is performance fuel improves outcomes. Suppressing anxiety degrades them.

### Expressive writing before high-stakes events
Veer can use 10 minutes of writing about what's making him anxious before mock interviews. Offloads worry; improves working memory available for the task.

### Overlearning + flexible retrieval
For interview prep: overlearn the openings, scaffolds, and core stories. Practice flexible retrieval across variant prompts. Pure memorization is brittle under pressure; pure understanding is too slow.

### Friction design
Phone physically out of reach during deep blocks. Project doc opened the night before. Cue-environment paired (same location, same lighting). The goal is to make the desired action the default response.

---

## What the system explicitly does NOT do

- Track mood, energy, or feeling
- Track hours worked beyond pillar minutes
- Send motivational messages
- Adjust the day based on how Veer "feels"
- Add features in response to Veer's optimization urges
- Use streaks (streaks cause perfectionism collapse; the research supports recoverable consistency over unbroken chains)
- Punish missed days — a missed day is data for Sunday, not a failure to dwell on

---

## When the system needs to be adjusted

Signs the system needs a Sunday-level adjustment, not a daily-level one:

- Same pillar slipping three weeks running
- Veer is hitting weekly volume but the work isn't compounding (e.g. 8 hours on project but no shipped iteration)
- Burnout signals — sleep dropping, workout slipping, social withdrawal
- The plan is being executed mechanically without learning

Signs the system is working:

- One protected deep block happens 5-6 days a week
- Veer can name what he shipped in the past week without checking
- Friday review shows visible compounding artifacts
- Alumni conversations are getting easier, not harder
- He's pushing back on the plan from a place of execution, not avoidance
