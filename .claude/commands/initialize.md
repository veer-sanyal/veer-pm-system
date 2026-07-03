---
description: Morning wake signal - log sleep indicators, confirm the wake target, build today's plan
---

# /initialize

Veer's morning wake cue. `context/sleep-protocol.md` OWNS the wake target and the live sleep-fix config; read it before acting. Be fast: this runs while he is starting his day.

1. If the `Last reconciled:` stamp in memory.md is stale, run `/reconcile` as part of this (it usually is; this is typically the first session of the day).
2. Log the tracked sleep indicators (per sleep-protocol.md: actual wake time + the time he decided to go to sleep) into today's PROGRESS.md "System signals" line. Ask for any indicator he did not give.
3. Confirm whether the wake target held (or note the slip; the target never moves back because of a bad night). Run any escalation check the protocol currently defines.
4. Build today's plan: if he woke at or before target, run the fixed spine (times in `context/about-me.md` / the calendar); if he woke later, rebuild the blocks forward from actual wake so the day is not zeroed.
5. Surface tonight's cues per sleep-protocol.md (caffeine cutoff, wind-down trigger).

Behavioral-first: no melatonin or light cues unless the protocol's escalation condition is met.
