# Prompt: teach cairn to grow its own filesystem

Written 2026-08-07 out of `/cairn:audit` Run 2 on `veer-pm-project`. Paste the block below into a
fresh session with the cairn plugin repo as cwd. Everything in it was verified against the installed
cairn **0.10.9** at `~/.claude/plugins/cache/cairn-marketplace/cairn/0.10.9/` — re-verify against the
version you actually open, since the file layout may have moved.

---

I want to fix a structural gap in the cairn plugin. Read `docs/PRINCIPLES.md`, `skills/build/SKILL.md`,
`skills/review/SKILL.md`, `skills/audit/SKILL.md` and `templates/instance/` before proposing anything.

## The claim

**A cairn instance is born with its filesystem and dies with it.** Nothing in the plugin ever creates
a new file or directory in response to what the system learns about its user. As the instance
accumulates entities — projects, clients, people, recurring threads — their facts get sharded into the
fixed file set established at build time, and their artifacts pile up flat in whatever directory is
nearest in spirit.

## Evidence for it (verified against 0.10.9 — re-check, don't trust me)

1. `skills/review/SKILL.md` memory consolidation offers exactly three operations: **SKIP / MERGE /
   INSERT**. Grep it for `SPLIT`, `PROMOTE`, `NEW FILE` — zero hits. Every operation writes into files
   that already exist. There is no operation whose output is a new file.
2. `templates/instance/` is a fixed 7-file skeleton (`CLAUDE.md`, `HOT.md`, `SYSTEM-MAP.md`,
   `README.md`, `docs/MANUAL.md`, `settings.json`, `commands/`). No per-entity directory concept, and
   nothing that would ever add one.
3. **P2 ("fine-grained facts live in files") and P4 ("index-first layout; progressive disclosure") are
   both read-path doctrine** — where facts live, how they load, what boots. Neither governs when the
   file *set* grows. That is the actual hole: the doctrine is complete about layout and silent about
   allocation.
4. The build interview elicits the north star, objectives and flows. Check whether it elicits the
   *entities* the user works with — I believe it does not, which is why an instance starts with no
   entity axis at all.

## The field evidence, from one audited non-cairn system

Measured in a real Claude Code system with ~2 months of daily use and its own telemetry (46 logged
sessions). Its ownership map has 11 rows and **every one is a kind of fact** — current state,
narrative, ledgers, strategy, dates, patterns, static profile. There is no entity axis. Consequences:

- **One client project occupied 7 locations.** 12 tracked files across 5 directories, plus two
  uncommitted locations outside the repo — including the one holding the actual client deliverables,
  which were therefore not version-controlled at all.
- **A `tools/` directory that was 8-of-9 single-project scripts**, under a name promising general
  utilities.
- **A `networking/` directory of 26 flat entries holding four unrelated kinds of thing** — call preps,
  send queues, client deliverables, and 13MB of mechanical-engineering CAD.
- **The hot-tier cost, which is the part that matters.** The system's always-loaded state file had
  grown to 8,450 words against a self-declared 1,500-word cap. A single entity's live state accounted
  for **10,570 bytes of it** — because that entity had no home, and the always-loaded file is where
  homeless state goes by default.

**The internal control is what makes this more than an anecdote.** In the same system, in the same
weeks, one entity DID get a home — its own repo with its own state/decisions/history files, and a
CLAUDE.md rule of "point, never mirror." That entity costs the hot tier 7 lines. The entity with no
home cost it 10,570 bytes. Same system, same discipline, opposite outcomes, and the difference is
solely whether a directory was ever allocated.

**And the system had already predicted its own need and failed to act on it.** Its weekly command
carried an armed trigger — "per-contact files owning the tracker row + prep sheet + relationship
history" — dated a month earlier and never built, because the trigger was reviewed only inside a
command that fired 3 times in 46 sessions. Two other correctly-predicted needs were parked the same
way. **A cairn governor should catch exactly this**, which is part of why I think it belongs in the
plugin rather than in one instance.

## What I want you to work out — do not assume my fix is right

I have a hypothesis, not a design. Push back on it hard; I would rather be told the doctrine already
covers this than get machinery I do not need.

- **Is the missing axis real?** Is "organize by kind of fact" vs "organize by entity" the right
  framing, or is the actual defect something else — no compaction pressure, no size signal, no
  allocation trigger? Argue for the framing you land on.
- **Where does allocation belong?** Candidates: a new principle in `PRINCIPLES.md`; a fourth
  consolidation verb in `/cairn:review` alongside SKIP/MERGE/INSERT; an entity-elicitation pass in
  `/cairn:build`; a lens in `/cairn:audit`. Possibly several, possibly one. Say which and why the
  others are wrong.
- **What triggers it?** An allocation rule that fires on vibes will scatter an instance into a
  thousand directories, which is worse than the disease and directly contradicts the ladder in P23 and
  P20. The trigger has to be cheap, mechanical and measurable — a byte or word threshold on the hot
  file, an entity's fact count crossing a bound, an artifact count in a directory, N sessions
  mentioning the same proper noun. Propose one you can actually compute, and name the false-positive
  it will produce.
- **What is the reverse operation?** If instances can grow directories they can sprawl, and P1 says
  content that isn't needed actively hurts. Deallocation — folding a dead entity's directory back down
  to a one-line pointer — probably matters as much as allocation. Design both or justify skipping one.
- **Does this need research, or is it a design call?** Apply cairn's own four-clause research bar
  (load-bearing ∧ contested ∧ generalizable evidence plausibly exists ∧ narrow enough for one run). My
  guess is it fails the bar and is a straight design decision from P1/P2/P4/P23 — but check, and if it
  clears, run `/cairn:research` rather than guessing a threshold.

## Constraints

- **The fix must be enforcement, not prose.** The same audit that produced this found that every
  hand-applied fix from the previous run had regressed to worse-than-before within 14 days, purely
  because the invariant was written into the least-run command instead of a deterministic hook. P8/P9.
  If your answer is a paragraph in a template telling the agent to consider making folders, it will not
  hold — and this document will read as evidence against you in three weeks.
- **Respect P1 and P23's ladder.** The lowest rung that works. A new subsystem is almost certainly the
  wrong answer; a verb added to an existing pipeline is more likely the right one.
- Whatever you build, say plainly how it would be falsified — what an instance would look like in a
  month if the fix were not working.
