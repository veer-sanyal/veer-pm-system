# Sleep Protocol (operational)

Started 2026-06-25. This file OWNS the wake-time target and the live sleep-fix config.
Everything else in the system links here instead of hard-coding a wake time. Evidence base
and citations: `files/sleep-circadian-research-2026-06-25.md`. Read that for the why; read
this for the what-to-do.

**Why this exists.** The whole calendar spine was anchored to a fixed 9am wake Veer kept
missing (he wakes 11am-1pm, screen-driven late nights, behavioral not insomnia). That made
every downstream block misfire, which is why outreach and study kept slipping regardless of
per-pillar fixes. Fixing the wake time is upstream of all four pillars and the highest-
leverage item on the board. Summer (no fixed mornings until classes ~Aug 24) is the window.

---

## The core lever (strongest evidence)

**A fixed wake time, held all 7 days, regardless of when he fell asleep, plus no naps.**
This rebuilds homeostatic sleep pressure so the late screen time collapses on its own. It
beats trying to force an earlier bedtime directly: you do not chase a bedtime clock, you fix
the *wake* and let rising sleep pressure pull bedtime earlier on its own. (Bootzin Stimulus
Control Therapy; Verreault 2024 NMA of 23 RCTs.)

Everything else below supports this one lever. If only one thing happens, it is the fixed wake.

## Veer's chosen config (set 2026-06-25, refined same session)

- **Wake: hard fixed 9:00, every day, starting Fri Jun 26. No ramp.** He chose the pure
  cold-turkey version over a gradual advance. Up at 9:00 regardless of when he fell asleep.
- **Behavioral first.** No melatonin, no light device to start. The spine is fixed wake +
  no naps + the nightly wind-down + if-then plans. Circadian aids are held as escalation
  (see below), added only if the schedule has not moved after ~2 weeks.
- **Phone friction: cue + app limits only.** Phone stays near (no relocation). Because this
  is the weakest friction option, the if-then plans and the fixed wake carry the load.
- **Tracking: 2 indicators** — actual wake time, and the time he decides to go to sleep.

## Expect a hard first week (this is the mechanism, not failure)

Coming from a ~3-4am sleep, waking at 9:00 night one means a short, rough first few nights.
That sleep deprivation is exactly what rebuilds Process S, shortens how long it takes to
fall asleep, and makes the late phone time collapse. Do not "recover" it with a sleep-in or
a nap. Typical pattern: roughest around nights 2-4, then onset starts migrating earlier and
the 9:00 wake stops feeling brutal. The clock itself only advances ~30-50 min/day, so a sane
~1:30am bedtime is a 1-2 week arrival, not night one.

## Daily cues

- **9:00 wake (hard):** alarm at 9:00, up on the first alarm. The one non-negotiable.
- **Morning daylight when up:** get outside or to a bright window for a bit. Not a timed
  light therapy (that is the escalation), just the free zeitgeber. Helpful, not required.
- **Caffeine cutoff: ~2:00pm** (moving earlier is better as bedtime advances).
- **Wind-down cue (~12:30am to start, pull earlier as onset migrates):** phone app
  limits / Downtime kick in; that is the cue to put the phone down and lights down. Phone
  stays in the room, so the app-limit timer and the if-then plan are what do the work here.

## If-then plans (carrying the most weight, since phone friction is weak)

With the phone staying near, the proven physical lever (removing it) is off the table, so the
intention-action plans do the heavy lifting (Valshtein/Oettingen/Gollwitzer 2020, MCII beats
sleep-hygiene advice). Pre-commit these:
- "When the app-limit/Downtime cue fires, I put the phone face-down on the far nightstand
  and turn the light off."
- "If I pick the phone back up after the cue, I set it back down and close my eyes."
- "When the 9:00 alarm goes off, I stand up and open the curtains before deciding anything."
Set the app limits aggressively (social/video apps blocked from the wind-down time) to make
up for the phone staying within reach.

## Bad-night rule (do not lose the schedule)

A bad night is expected and is data, not failure (no streaks; recoverable consistency).
**Get up at 9:00 anyway.** Do not sleep in to "recover" and do not nap — that bleeds off the
sleep pressure that fixes the next night. One rough morning at 9:00 beats resetting.

## Weekend / social drift (the reset risk)

Hold wake within <1h of 9:00 on weekends. The all-7-days rule IS the social-jetlag control
(Bootzin). A Saturday slept to 1pm undoes days of progress. After a late social night, still
get up within ~1h of 9:00 and take the tiredness; do not chase it with a sleep-in.

## Escalation (only if stalled after ~2 weeks, i.e. ~Jul 9)

If by ~Jul 9 the 9:00 wake is not holding or bedtime is not migrating earlier, add the
circadian aids he is currently skipping, in this order:
1. **Morning bright light** within ~5 min of the 9:00 wake: outdoors 10-30 min, or a
   5,000-10,000 lux lamp ~30 min at ~40cm. Strongest accelerant (Crowley & Eastman 2015);
   only works alongside the fixed wake, not alone (AASM/Auger 2015: light-alone gets NO
   recommendation for adults).
2. **0.5mg melatonin** ~5h before target bed (~8:30pm for a 1:30am bed) as a clock-shifter,
   NOT a sedating dose at lights-out. Timing matters more than dose (Burgess 2010). Get a
   true low dose; most products are 1-3mg+.
Combined they roughly halve the calendar time (~0.5h/day advance) but cost money and add
timing steps, which is why they are the fallback, not day one.

## The 2 tracked indicators (and the noise to ignore)

Logged each morning via `initialize` into the daily PROGRESS "System signals" line; the
Sunday session reviews wake-time consistency across the week.
1. **Wake time** (actual vs 9:00) — the top signal. Wake-time variability shrinking toward
   9:00 is the leading indicator the schedule is locking.
2. **Time he decides to go to sleep** (when he gets in bed to sleep / phone goes down) — the
   bedtime-migration readout; should drift earlier as pressure rebuilds.

Do NOT track (noise, demotivating, non-predictive): total sleep hours, "sleep quality"
scores, wearable sleep-stage breakdowns, and (per his choice) minute-precise onset latency.
This is behavioral data only, not mood or energy, so it fits the system's "tracking is the
intervention" rule without breaking "no feelings-tracking."

## How "initialize" works now (no ramp)

Because the target is a hard fixed 9:00 with no ladder, each morning's `initialize` is
simple: log the 2 indicators, confirm the 9:00 wake happened, and run the normal fixed
9:45/11:45 spine. If he wakes past 9:00 (a slip), the day's blocks rebuild forward from
actual wake so the day is not zeroed, and the target stays 9:00 (never moves back). No step
to advance — the only structural change is the ~Jul 9 escalation check above.

## Status

- 2026-06-25: protocol set; first night tonight; hard 9:00 wake starts Fri Jun 26.
  Behavioral-first (no aids yet); phone stays near with app-limits + wind-down cue; tracking
  2 indicators. Escalation check ~Jul 9. Held through August to lock before classes ~Aug 24.
  Daily indicators logged in `PROGRESS.md`; current config mirrored in `memory.md`.
- 2026-07-05 (week-1 verdict, Sunday session): NOT holding yet but trending — Jun 29/30
  initialize came ~2pm; Jul 1-4 per Veer "mixed, trending earlier"; Jul 5 up before ~9:40.
  **ESCALATION STEP 1 ACTIVE from Mon Jul 6: morning bright light** — outside within ~5 min
  of the 9:00 alarm, 10-30 min (briefings carry the cue). **Melatonin decision Thu Jul 9**
  (in that day's briefing): if the wake hasn't landed 9:00-10:00 on 3 of the last 4 days,
  start 0.5mg ~8:30pm as the clock-shifter. Named risk to the keystone: late-night StudyFlow
  spec sessions (1:30am commits Jul 4) — the wind-down cue now explicitly closes those too.
- 2026-07-16 (Veer check-in, ~2:45am): **anchor moved off 9:00 to a fixed ~11:00 for the
  summer, at Veer's direction.** His report: sleep is much more consistent now (alarm-driven,
  waking ~11), and the daily `initialize` interrogation ("when did you wake, rebuild the
  blocks") reads as friction, not help. Ruling, consistent with the core lever above: the
  target was never 9:00 for its own sake, it was *one fixed wake held all 7 days* so Process S
  rebuilds and late nights collapse. A held 11:00 satisfies that. So: **operating wake = fixed
  ~11:00 (summer)**; `initialize` strips to a 5-second wake-time stamp plus planning the spine
  forward from 11:00 (drop the rebuild dialogue). Keep exactly ONE tracked indicator: actual
  wake time (the schedule-holding signal). Clock-shift-to-9 is moot at an 11 anchor, so the
  melatonin decision (memory tripwire 4) closes HOLD. **Two caveats on record:** (1)
  NOT-YET-VERIFIED — Veer was in the STICK project at 2:41am tonight, so the fixed-wake +
  earlier-bedtime loop is not closed; the 11:00 only works if held after a late night (no
  recovery sleep-in). (2) **Walk-back required before classes ~Aug 24** (real mornings):
  advance 11:00 toward ~9:00 in mid-August. **Sunday re-verifies** from a real week of wake
  stamps; the block-schedule reflow to an 11:00 base (about-me.md's 9:45/11:45 table) is a
  Sunday task, not done here.
