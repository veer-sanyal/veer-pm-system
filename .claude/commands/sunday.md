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
2. Review what shipped, slipped, surprised (data, not analysis). Name the week's pattern briefly; record any TESTING pattern verdicts in `context/patterns.md`. Include one line of StudyFlow-bundle activity (`~/Desktop/study app advisor` git log) as DATA — visible, never counted toward pillar volume, and checked against its two boundaries (no morning blocks, stops at wind-down). Ruling of 2026-07-05; revisit post-APM-app.
3. Define next week's commitments by pillar; turn each into an implementation intention (when X, you Y).
4. **Pipeline rule:** any application deadline within ~2 weeks still at Stage < Ready becomes a candidate "draft <Company> resume" work block.
5. **Study targets:** from state.json, rewrite the PROGRESS.md Pillar 2 & 4 ledgers, refresh the memory.md learning-state summary, and pick the week's P2/P4 targets (due/weak topics + days-to-next-milestone); write them into block titles and briefings.
6. **Write the calendar** (per daily-briefing-instructions.md): retitle the week's three work blocks per day with the specific action, and write six 9:00 Morning Briefing events (done-check on yesterday's block, yesterday's question, "this week feeds," optional citation). If the Calendar connector is unavailable, output the exact titles and briefing text and say so plainly.
7. Persist everything (memory.md, PROGRESS.md, patterns.md), commit, push.

## System maintenance (part of every Sunday)

Every living file has a size budget so context stays lean as the system ages. Git history is the archive of record: compression never loses information, it moves it out of the per-session read path. Check whichever files this week touched; the full sweep is monthly (below).

| File | Budget | When over |
|---|---|---|
| `memory.md` | ~1,500 words | Compress closed items to one line each; the narrative already lives in PROGRESS.md. |
| `PROGRESS.md` | dated entries ~4 weeks back | Roll the oldest closed weeks into `PROGRESS-archive.md` (append chronologically; the archive is the complete history). |
| `context/patterns.md` | ~5 evidence bullets per pattern | Compress the oldest instances to one line ("+N earlier instances, Jun-Jul 2026, git history has the detail"); keep the freshest evidence and the current build-around verbatim. DORMANT patterns compress to header + one-line history. |
| `alumni-tracker.md` | live names only in the working tables | Closed or unresponsive contacts move to a one-line-each Closed section at the bottom. |
| `context/key-dates.md` | future dates only | Delete past deadlines outright; closed Application Pipeline rows compress to one line. |
| `networking/` | live calls only | Once a call is debriefed, mark its prep sheet historical (header + file-index row). |
| `session-log.jsonl` | one calendar year | Each January, roll to `session-log-<year>.jsonl` and start fresh with the schema line. |

## Monthly system health check (first Sunday of the month)

Read `session-log.jsonl` and answer, briefly, in the Sunday summary:

1. Session mix: counts by type (reconcile / quick / coaching / sunday / tutor / apply / debrief). Is the system being used for what it was built for?
2. Reconcile yield: how often did a reconcile actually find drift or a tripwire? If it is mostly no-ops, lengthen the cadence; if it keeps catching late replies, shorten it.
3. Tripwire latency: median days from a slug appearing in `tripwires_opened` to the same slug in `tripwires_closed`. This is the system's core KPI (it exists to close loops).
4. Dead weight: files no session consulted this month are candidates to compress or retire; capabilities never invoked are candidates to cut.
5. Size budgets: run the full maintenance-table sweep above; archive/prune what is over.
6. **One live experiment.** The system improves by testing, not accreting: at most ONE structural experiment at a time (e.g. "briefing refresh at reconcile vs Sunday-only", "every-other-day reconcile"). It gets a hypothesis, the single metric that decides it, and a verdict date; record it in PROGRESS.md System signals and close it with a verdict before opening the next. No live experiment is also a valid state — do not invent one to fill the slot.

Fold any resulting change into this session's system work (cap: the 90-minute weekly optimization budget from direction.md still applies).
