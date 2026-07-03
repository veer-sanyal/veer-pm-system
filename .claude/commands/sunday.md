---
description: Sunday planning session - reconcile the week, plan the next one, write the calendar, maintain the system
---

# /sunday

The weekly structural session. Everything mid-week sessions refuse to do (replans, system changes, new commitments) happens here.

## Read (beyond the standard session-start set)

1. `context/scheduling-blueprint.md` (the behavioral science governing the plan)
2. `context/daily-briefing-instructions.md` (how blocks and Morning Briefings are composed; the Sunday sequence lives there)
3. The full past week of PROGRESS.md, plus `context/patterns.md`
4. `context/key-dates.md` (timeline + Application Pipeline)
5. `context/study/state.json` (P2/P4 learning state)
6. `DECISIONS.md` from the product repo if product decisions are in play

## Sequence

1. **Reconcile first.** Run `/reconcile`, then compare the past week's WRITTEN calendar block titles against PROGRESS.md and commits: scheduled vs actually-done vs slipped, before any planning.
2. Review what shipped, slipped, surprised (data, not analysis). Name the week's pattern briefly; record any TESTING pattern verdicts in `context/patterns.md`.
3. Define next week's commitments by pillar; turn each into an implementation intention (when X, you Y).
4. **Pipeline rule:** any application deadline within ~2 weeks still at Stage < Ready becomes a candidate "draft <Company> resume" work block.
5. **Study targets:** from state.json, rewrite the PROGRESS.md Pillar 2 & 4 ledgers, refresh the memory.md learning-state summary, and pick the week's P2/P4 targets (due/weak topics + days-to-next-milestone); write them into block titles and briefings.
6. **Write the calendar** (per daily-briefing-instructions.md): retitle the week's three work blocks per day with the specific action, and write six 9:00 Morning Briefing events (done-check on yesterday's block, yesterday's question, "this week feeds," optional citation). If the Calendar connector is unavailable, output the exact titles and briefing text and say so plainly.
7. Persist everything (memory.md, PROGRESS.md, patterns.md), commit, push.

## System maintenance (part of every Sunday)

- **Archive:** if PROGRESS.md's dated entries extend back more than ~4 weeks, roll the oldest closed weeks into `PROGRESS-archive.md` (append chronologically). Nothing is deleted; the archive is the complete history.
- **memory.md size check:** it should stay a snapshot (~1,500 words max). Compress closed items to one line each; the narrative already lives in PROGRESS.md.

## Monthly system health check (first Sunday of the month)

Read `session-log.jsonl` and answer, briefly, in the Sunday summary:

1. Session mix: counts by type (reconcile / quick / coaching / sunday / tutor / apply). Is the system being used for what it was built for?
2. Reconcile yield: how often did a reconcile actually find drift or a tripwire? If it is mostly no-ops, lengthen the cadence; if it keeps catching late replies, shorten it.
3. Tripwire latency: median days from a tripwire opening to closing. This is the system's core KPI (it exists to close loops).
4. Dead weight: files no session consulted this month are candidates to compress or retire; capabilities never invoked are candidates to cut.
5. Size budgets: word counts of memory.md and PROGRESS.md vs their budgets; archive/prune if over.

Fold any resulting change into this session's system work (cap: the 90-minute weekly optimization budget from direction.md still applies).
