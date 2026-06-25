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

## Veer's chosen config (set 2026-06-25)

- **Approach: stepped advance** (not cold-turkey). Wake target steps ~45 min earlier every
  ~3 days, holding a step until it sticks, converging on a hard 9:00 lock.
- **Circadian levers: both.** Morning bright light at wake + 0.5mg melatonin ~5h before bed.
- **Phone friction: across the room** (out of arm's reach, not out of the bedroom). Because
  this is partial friction, lean harder on the if-then plans below.
- **Tracking: the 3 leading indicators** (wake time, minutes-to-sleep, phone-down time).

## The wake-target ladder (the single source of truth for "what time is wake")

Advance to the next step only when the current target is being hit (roughly the last 2 of
2-3 days) and onset is not blowing out. If a step is not sticking, hold it a few more days.
A bad night does NOT reset the ladder. `memory.md` mirrors the current step as live state.

| Step | Dates (default cadence) | Wake target | Backstop bed (wake - 7.5h) | 0.5mg melatonin (~5h before bed) |
|---|---|---|---|---|
| 1 | Fri Jun 26 - Sun Jun 28 | 11:15 | ~3:45a (let sleep come earlier) | ~10:45p |
| 2 | Mon Jun 29 - Wed Jul 1 | 10:30 | ~3:00a | ~10:00p |
| 3 | Thu Jul 2 - Sat Jul 4 | 9:45 | ~2:15a | ~9:15p |
| 4 | Sun Jul 5 onward | 9:00 (hard lock) | ~1:30a | ~8:30p |

After Step 4, hold the hard 9:00 anchor every day through August so it is deeply locked
before classes resume ~Aug 24 and external structure takes over. Backstop bed = the time to
stop lying in bed awake, not a forced lights-out; let onset move earlier as pressure builds.

Why stepped and not cold-turkey: the clock only advances ~30-50 min/day (Crowley & Eastman
2015), so 1pm to 9am is a ~1-2 week shift, not a one-night jump. And cold-turkey 9am would
put morning light *before* the body-temperature minimum (which sits late when delayed) and
risk pushing him *later* (Khalsa 2003). Stepping keeps light landing after CBTmin the whole
way down.

## Daily cues (anchored to the current step)

- **At wake (within 5 min):** bright light. Outdoors 10-30 min, or a 5,000-10,000 lux lamp
  ~30 min at ~40cm while doing something (coffee, briefing). This is the circadian accelerant;
  it works *with* the fixed wake, not instead of it.
- **Late afternoon/evening:** 0.5mg melatonin at the step's time above (~5h before backstop
  bed). This is a clock-shifter, NOT a sleeping pill. Do not take a higher sedating dose at
  lights-out; timing matters more than dose (Burgess 2010). If evening grogginess, push it 30
  min later; if not advancing, nudge 30 min earlier.
- **Caffeine cutoff:** none after ~2:00p early in the ladder, moving earlier as wake advances
  (aim ~8h before backstop bed).
- **Wind-down cue (~45 min before backstop bed):** move the phone to the across-the-room
  charger, lights down. This is the nightly anchor the spine was missing.

## If-then plans (carrying extra weight, since phone friction is only partial)

The proven behavioral lever is removing the phone; "across the room" is weaker, so the
intention-action plans do real work here (Valshtein/Oettingen/Gollwitzer 2020, MCII beats
sleep-hygiene advice). Pre-commit these as if-then cues:
- "When the wind-down cue fires, I put the phone on the far charger before I sit back down."
- "If I pick the phone back up after wind-down, I put it back on the charger and get in bed."
- "When my alarm goes off, I stand up and turn the light on before deciding anything."
(WOOP framing when a step is at risk: wish = hit tomorrow's wake target; obstacle = one more
video; plan = the if-then above.)

## Bad-night rule (do not lose the schedule)

A bad night is expected and is data, not failure (no streaks; recoverable consistency).
**Keep the fixed wake time anyway.** Do not sleep in to "recover" — that bleeds off the sleep
pressure that fixes the next night. One rough morning at the current target beats resetting
the ladder. The day's work blocks degrade gracefully (see the wake-anchored rebuild in
`daily-briefing-instructions.md`); the wake target does not move backward.

## Weekend / social drift (the reset risk)

Hold wake within <1h of target on weekends. The all-7-days rule IS the social-jetlag control
(Bootzin). A Saturday slept to 1pm undoes days of advance. If a late social night happens,
still get up within ~1h of target and take the tiredness; do not chase it with a sleep-in.

## The 3 tracked indicators (and the noise to ignore)

Logged each morning via `initialize` into the daily PROGRESS "System signals" line; the
Sunday session reviews wake-time consistency across the week.
1. **Wake time** (actual vs the step target) — the top signal.
2. **Minutes to fall asleep** once the phone was down (should shorten as pressure rebuilds).
3. **Time the phone went to the charger** (the behavioral-lever readout).

Do NOT track (noise, demotivating, non-predictive): total sleep hours, "sleep quality"
scores, wearable sleep-stage breakdowns. This is behavioral data only, not mood or energy,
so it fits the system's "tracking is the intervention" rule without breaking "no
feelings-tracking."

## How to tell if it is working (leading, not lagging)

Wake-time variability shrinking toward the target, and minutes-to-sleep dropping, are the
early wins, before total sleep or how he "feels" changes. If after ~4-5 days at a step the
wake target is reliably hit and onset is under ~20-30 min, advance. If wake is still all over
the place, hold the step and tighten the phone if-then plan before adding anything.

## Status

- 2026-06-25: protocol set; levers chosen; first night tonight. Step 1 (wake 11:15) starts
  Fri Jun 26. Hard 9:00 lock targeted ~Jul 5, held through August. Current step is mirrored
  in `memory.md`; daily indicators logged in `PROGRESS.md`.
