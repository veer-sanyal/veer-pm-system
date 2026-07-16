# System audit: every workflow, the usage record, and an efficiency review

Date: 2026-07-15. Method: two parallel subagent extractions (all protocol files; telemetry + git history), synthesis in the main session. Companion visual: `specs/system-map.tex` (compiles with pdflatex; `system-map.pdf` alongside).

This is a point-in-time audit. Protocol changes it recommends are Sunday-session decisions, not things a mid-week session should silently apply.

---

## 0. Veer's journeys (the rider's view: every path through the system)

Every journey passes the same front door (hook banner + memory.md; first session of the day auto-reconciles first) and the same exit (persist owner files, commit + push, one telemetry line). Journeys chain freely in one day: initialize, then tutor, then debrief is one day, three journeys. Visual: map 1 in `system-map.pdf`.

| # | Veer does | What happens | Ends as |
|---|---|---|---|
| J1 | Wakes up, says **initialize** | Sleep indicators logged, wake target checked | Today's plan (spine, or rebuilt forward from actual wake) |
| J2 | Study intent: **quiz me / drill X / mock me** | Tutor loop: predict, answer, feedback; state saved every item | state.json + PROGRESS one-liner, committed |
| J3 | Found a posting: **/apply** link | Profile read, match-map, .tex from template, compile | Tailored PDF in applications/, pipeline row in key-dates |
| J4 | Just finished a call: **/debrief** | Outcome captured in his words, thank-you drafted same day | Loop closed, next action tripwired |
| J5 | Sunday 4pm: **/sunday** | Week reviewed, next week planned, maintenance | Calendar written (6 briefings + retitled blocks) |
| J6 | Mid-week ask: **help me with X / should I Y** | Tactical, action-first coaching | Help delivered; no mid-week replans (structure is Sunday's) |
| J7 | Drops a **screenshot** (WhatsApp / iMessage / team) | Facts extracted, record corrected | Tripwires re-armed; how blind channels reach the system |
| J8 | Lookup: **where is X at? / why?** | Answered from memory.md alone | A why gets a brief answer, then redirect to the next move |
| J9 | System work: **audit / improve / add** | P6 avoidance check first | Structural changes park for Sunday |
| J10 | (passive) 9:00 **Morning Briefing** on the calendar | Done-check question + today's blocks | No Claude session at all |

Observed frequency (telemetry, Jul 3 to 15): J6-style reconcile/tactical sessions dominate; J4 once; J5 once (one missed); J1 and J2 never fired in-window, which is the usage gap behind the cold state.json and the empty wake log, not a missing capability.

## 1. Complete workflow inventory

### A. Named commands (6)

| # | Workflow | Trigger | Main-session reads | Subagents spawned | External tools | Writes | Protocol size |
|---|---|---|---|---|---|---|---|
| 1 | `/reconcile` | Stale stamp (auto, no ask), first session of day, or explicit | key-dates.md pipeline rows, alumni-tracker.md, ledgers.md relationships, memory.md tripwires | **5 parallel, "cheaper model"**: product commits (gh api), calendar trailing ~7d, Gmail drafts, Gmail inbound, Gmail LinkedIn digest; +1 conditional (iMessage chat.db if opted in) | gh (r), Calendar (r+w tomorrow's briefing only), Gmail (r, draft-only), iMessage db (r, gated) | memory.md stamp+tripwires, PROGRESS.md entry, patterns.md (only on 2-instance bar), tomorrow's briefing event, commit+push, telemetry line | 40 lines |
| 2 | `/initialize` | Morning wake signal | sleep-protocol.md first, memory.md stamp, about-me.md spine / calendar | None of its own; nests `/reconcile` if stamp stale (inherits its fan-out) | Calendar (r) | PROGRESS.md sleep-indicators line; today's plan (spine or rebuilt-forward) | 15 lines |
| 3 | `/sunday` | Weekly, Sun 4:00 PT; monthly health check on first Sunday | scheduling-blueprint.md, daily-briefing-instructions.md, PROGRESS.md past week, ledgers.md, patterns.md, key-dates.md, study/state.json, product DECISIONS.md (conditional), session-log.jsonl (monthly) | Nests `/reconcile` as step 1 (inherits fan-out) | Calendar (w: 6 briefings + 3 retitled blocks/day), git log on StudyFlow bundle (r, data only) | memory.md, PROGRESS.md, patterns.md verdicts, ledgers.md regenerated, calendar, archives/compression per budget table, commit+push | 60 lines |
| 4 | `/apply` | On-demand, role/link given | Defers to application-docs-workflow.md (90 lines): profile/ in role order, ResumeDeepResearch.md, Summer2026 research, CoverLetterDeepResearch.md only if CL asked; master PDF only as gap fallback | None | pdflatex/latexmk local | applications/\<Co\>/ .tex+.pdf, profile/*.md fold-back, applications/README.md, key-dates.md pipeline row | 13 + 90 lines |
| 5 | `/tutor` | Explicit study intent phrases only | Defers to study-tutor.md (143 lines); on-demand loads: pedagogy.md, state-spec.md (235), curriculum.md, first-contact research; state.json silently | None | git only | state.json after EVERY graded item; PROGRESS.md one-liner + commit at close | 14 + 143 lines |
| 6 | `/debrief` | Immediately after any networking/externship/client call | alumni-tracker.md row, networking/ prep sheet | None | Gmail (draft-only thank-you) | alumni-tracker.md, ledgers.md (relationships + P3 funnel), prep sheet marked historical, memory.md tripwire+slug, commit+push, telemetry | 14 lines |

### B. Automatic / system workflows (run without being asked)

7. **SessionStart hook** (`.claude/hooks/session-start.sh`, every session): prints stamp + staleness verdict, tripwire headers, state.json mtime (catches unpersisted study sessions), uncommitted-diff repair directive, auto-push of stranded commits, telemetry-gap detector (last commit newer than last log line = a session died unlogged; backfill a reconstruction line).
8. **Session-start gate** (CLAUDE.md): memory.md always; stale stamp = auto-`/reconcile` before the ask; plan/week/behavior asks also read PROGRESS tail + ledgers + patterns.md; pure lookups read nothing else.
9. **Routing table** (CLAUDE.md): 14 topic-to-doc routes; covering doc read before any substantive answer, cited specifically.
10. **Decomposition rule**: any item carried > 2 sessions/days gets its smallest physical next action named and tripwired; a second stall gets the avoidance named.
11. **Session end** (every session): persist owner files, commit+push (real messages), exactly one telemetry line.
12. **Telemetry January roll**: session-log.jsonl rolls to session-log-\<year\>.jsonl each January.
13. **Monthly system health check** (inside first-Sunday `/sunday`): session mix, reconcile yield, tripwire latency (core KPI), dead-weight files, size-budget sweep, single live experiment slot, architecture watch over 3 dormant triggers (tripwires.json, per-contact files, generated daily briefing).

### C. Deferred protocol docs (loaded only when their command fires)

application-docs-workflow.md (90), study-tutor.md (143) + state-spec.md (235) + pedagogy.md + curriculum.md, daily-briefing-instructions.md (126, the calendar content contract for /sunday and /initialize). This lazy-loading is the system's main context-economy mechanism and it works.

### D. Unnamed but recurring workflows (observed in telemetry/commits, no protocol file)

14. **Screenshot capture**: Veer pastes a WhatsApp/iMessage/team-thread screenshot; the session extracts facts, corrects the record, re-arms tripwires. Occurred in 3 of the last 4 reconciles and supplied their highest-value facts (When2Meet correction, Trice handoff, LaCroix reply).
15. **Outbound review**: reviewing a teammate's or Veer's draft email before send (Izzy's Bryon email, Jul 15).
16. **Prep-sheet creation**: networking/ call-prep docs before a call (LaCroix, Anicito, Dr. G).
17. **LinkedIn drafting**: files/linkedin/ post iterations + chart scripts.
18. **Spec/design work**: specs/ docs for system upgrades (5 to date).
19. **Mid-week tactical support**: the catch-all "quick"/"coaching" session; explicitly protocol-light by design.

Verdict on D: only #14 deserves a protocol line (see improvement Q6). The rest are fine as ad-hoc.

---

## 2. What the usage record actually shows

Telemetry: 10 session records, 2026-07-03 to 07-15 (13 days). Git: 187 commits since Jun 9 (37 days). Pre-Jul-3 sessions predate telemetry (Cowork era); git is the only record there.

**Session mix**: reconcile 5, system 2, sunday 1, debrief 1, quick 1 (a self-labeled backfill). Zero logged: tutor, apply, coaching. `initialize` is not even in the schema enum.

**Cadence**: 5 of 13 days dark (38%); longest streak Jul 12-15 (4 days), which is also the missed Sunday. Sunday hit rate in range: 1 of 2. Commits come in session-end bursts (6 days with 12+ commits), matching "batch persist at close," not drip commits.

**Subagent usage**: the parallel fan-out exists only inside `/reconcile` and only since the Jul 8 system upgrade; 3 of 5 reconciles name it. No line records subagent count, model, or duration, so fan-out cost is unmeasurable from the log.

**Scan yield (the interesting one)**: across the 5 reconciles, the automated scans (commits, calendar, Gmail x3) mostly confirmed quiet; the highest-yield sensor was **Veer's own screenshots** (3 of 4 recent reconciles got their key fact there). The channels where his real signal lives (iMessage team thread, WhatsApp) are exactly the ones the system cannot read (iMessage toggle ON but Full Disk Access not granted; WhatsApp never visible).

**Self-healing worked once**: the Jul 9 session that died unlogged was caught by the hook's telemetry-gap detector and backfilled next session. Keep that mechanism.

**Schema drift**: `coaching|tutor|apply` never used; multi-purpose sessions get one lossy type (the Jul 5 line bundles reconcile + coaching + sunday; the Jul 7 line hides a full debrief inside a reconcile). Line 1 of the log is a `_schema` object with a different shape; any parser must skip it.

---

## 3. Findings

**Working well, leave alone**: lazy-loaded protocol docs; owner-file discipline (one fact one owner); the hook's repair duties; /reconcile's fan-out architecture; /apply's read ordering (profile before old PDFs); state-spec's write-per-item rule; two-tier context/ vs files/ reading.

**Gaps**:

1. "Cheaper model" is never pinned to a model name anywhere; a session can legally run all 5 scans on the expensive session model.
2. Three Gmail scans are three separate subagent spawns; each pays its own startup + Gmail tool-schema load for one query apiece.
3. Reconcile reads README.md every run solely for the iMessage toggle, and the hook banner already prints iMessage readability.
4. Telemetry cannot answer cost questions: no duration, no subagent count; `initialize` missing from the enum; the core KPI (tripwire latency) is computable but nothing about efficiency is.
5. Scan windows drift per run (calendar Jul 2-12, then 9-13, then 8-16); harmless but unstandardized.
6. The single highest-yield input (Veer screenshots) has no place in the protocol; the scans it compensates for are the blind ones.
7. The costliest failure mode is not tokens, it is availability: one missed Sunday cost a planned week plus 4 dark days. Nothing in the system detects a missed Sunday until the next human-initiated session.
8. The largest per-session fixed context cost is now outside the repo entirely: user-level plugin boilerplate (superpowers dump, ponytail, n8n/options/stitch skill listings) injected into every session dwarfs memory.md. The repo's own read discipline is fine.

---

## 4. Improvements, ranked

### Quick fixes (one-line protocol edits; adopt at the belated Sunday)

- **Q1. Pin the model**: in reconcile.md and CLAUDE.md, replace "a cheaper model" with "haiku". One word, guarantees the fan-out is cheap.
- **Q2. Merge the 3 Gmail scans into 1 subagent** running all three queries (drafts, inbound, LinkedIn digest). 5 spawns become 3; one Gmail schema load instead of three. Same coverage.
- **Q3. Fix the telemetry schema**: add `initialize` to the enum; add optional `subagents` (int) and `dur_min` (approx int). Keeps one line per session, makes the monthly health check able to see cost. Note in the schema line that parsers skip line 1.
- **Q4. Drop the README read from reconcile**: trust the hook banner's iMessage readability line (it probes the actual condition, not the documented toggle). One fewer file read per reconcile, and it also fixes the current half-enabled state where the toggle says ON but chat.db is unreadable.
- **Q5. Standardize scan windows**: calendar/Gmail trailing 7 days + forward 2, always.
- **Q6. Make screenshots first-class**: one line in reconcile.md: "Veer-supplied screenshots are a scan source; ask for one when a blind channel (iMessage/WhatsApp) is the likely locus of drift."

### Structural (Sunday-session decisions)

- **S1. Sunday-miss tripwire in the hook** (top pick): ~4 lines of bash; if no `"type": "sunday"` telemetry line within the last 7 days and today is Monday+, print a SUNDAY MISSED banner with the instruction to offer a 20-minute tactical week plan. Caps the blast radius of the exact failure that just happened. No new files, no new architecture.
- **S2. Codify "belated Sunday" mode** in sunday.md: a named 20-minute subset (reconcile + next-week commitments + calendar retitles only; skip maintenance and deep review) so a missed Sunday has a cheap standard recovery instead of an ad-hoc one.
- **S3. Finish or kill the iMessage channel**: either grant Full Disk Access (2-minute Veer action, already tripwired) or set the toggle OFF so no session budgets for a scan that cannot run.
- **S4. Prune user-level plugins for this project**: the n8n, options-advisor, google-stitch, cowork-plugin-management skill sets load into every session here and are unrelated to this system. Largest single context saving available anywhere in the stack; entirely outside this repo (user settings).

### Explicitly do NOT build (architecture watch confirmed dormant)

tripwires.json, per-contact files, generated daily briefings: none of their trigger conditions have fired. Token-count telemetry: Claude cannot reliably observe its own token spend; `subagents` + `dur_min` is the honest ceiling. A second experiment slot: the one-experiment rule is load-bearing; keep it.

---

## 5. Context-cost snapshot (approx, per session type)

| Read set | Files | ~Lines into main context |
|---|---|---|
| Every session (floor) | hook banner + memory.md | ~100 |
| + plan/behavior ask | + PROGRESS tail, ledgers.md, patterns.md | ~450 |
| /reconcile main-session adds | reconcile.md, key-dates.md, alumni-tracker.md | ~300 (scans stay in subagents) |
| /sunday adds | blueprint, briefing-instructions, state.json, full week | ~700 |
| /tutor adds | study-tutor + state-spec + pedagogy/curriculum on demand | ~500-700 |
| User-level plugin boilerplate (outside repo) | superpowers + skill listings + MCP instructions | larger than any row above |

The repo's read discipline is already tight; the leverage order is: plugins (S4) > fan-out model pin (Q1) > spawn count (Q2) > everything else.

---

## 6. Addendum (same day, second pass)

### 6.1 The remembered "fork" does not exist; the capability does

No forks and no PRs on `veer-pm-system` or the product repo. The five remote `claude/*` branches are fully merged web-session branches, zero commits ahead (safe to delete). What was remembered is the **Indeed jobs connector** attached to the Claude workspace (`search_jobs`, `get_job_details`, `get_company_data`, `get_resume`). Tested 2026-07-15: full-time PM searches return real postings; internship-filtered queries return nothing, consistent with the Summer 2027 window not opening until Aug-Oct (key-dates.md) and big-tech PM internships living on company portals, not Indeed.

Verdict: a weekly scout for adjacent roles (analyst / APM-adjacent, the `research-adjacent-roles-to-pm.md` track) and off-cycle internships; not a pipeline replacement. **S5 (Sunday adoption):** one paragraph in sunday.md's pipeline step: run 2-3 fixed connector queries, add relevant new rows to the key-dates Application Pipeline.

### 6.2 Usage telemetry exists; what it says is used vs idle

`session-log.jsonl` is the usage telemetry (one line per session, `read` field = files consulted). From the 13-day window:

- **Hot (consulted repeatedly):** memory.md, PROGRESS.md tail, ledgers.md, patterns.md, key-dates.md, alumni-tracker.md, about-me.md, direction.md, externship doc, daily-briefing-instructions.md, sleep-protocol.md, study/state.json, README.md, CLAUDE.md + commands + hook.
- **Idle by design (on-demand routing, keep):** the research library in context/, files/ originals, application profile docs, study protocol docs. Their commands or routes simply did not fire in-window.
- **True dead-weight candidates for the Aug 2 monthly health check:** `files/linkedin/` (post live since Jun 14, drafting history), `context/emotional-regulation/` (no build decision since Jun), `context/veer-full-profile.md` (unconsulted), pre-July specs (historical by design, cheap to keep).

The measurement gap stays Q3: add `subagents` + `dur_min` fields and `initialize` to the enum; with 4+ weeks of lines the monthly check can then make retire/keep calls on data.

### 6.3 Boot-up cost: where it actually is and the exact levers

The repo's fixed boot cost is already small (banner + memory.md, ~100 lines; CLAUDE.md 82 lines). The heavy per-session weight is user-level and invisible to this repo: plugin SessionStart dumps (superpowers, ponytail) plus skill listings and MCP tool inventories from servers this project never uses (Supabase, Vercel, Slack, computer-use, browser, codegraph, n8n).

Levers (project-scoped, verified against current Claude Code docs):

```json
// .claude/settings.json additions, this project only
{
  "enabledPlugins": {
    "superpowers@<marketplace>": false,
    "ponytail@<marketplace>": false,
    "options-advisor@<marketplace>": false,
    "cowork-plugin-management@<marketplace>": false
  },
  "disabledMcpjsonServers": ["computer-use", "claude-in-chrome", "codegraph"]
}
```

Notes: get exact plugin IDs from `/plugin list`; connector-type servers (Gmail, Calendar, Drive, Supabase, Vercel, Slack, jobs) are managed in the app's connector UI, not `disabledMcpjsonServers`. **Never disable Gmail or Calendar for this project; /reconcile is blind without them.** Measure before/after with `/context` (shows the startup token breakdown by category).

### 6.4 Sleep module: shrink, do not delete (Sunday decision)

Request on the table: remove the sleep part. The record argues against deletion: memory.md names sleep as the gating variable for the P2 study misses ("misses trace to the late wake, not avoidance of the block"), and sleep-protocol.md was consulted in-window. What is actually failing is the entry point: `/initialize` fired zero times, so there is no wake log and the melatonin decision has no data. Deleting the module removes the instrument, not the problem.

Shrink option for the belated Sunday: retire the standalone ceremony; fold the two indicators (actual wake time, time he decided to sleep) into the first session of any day as one question inside the existing front door. sleep-protocol.md stays as the owner of the wake target; initialize.md collapses to a stub or is absorbed. Cost drops to one question a day; the keystone signal survives.
