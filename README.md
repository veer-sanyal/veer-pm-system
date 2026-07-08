# Veer PM Execution System (planning project)

The coaching and planning system for landing a Summer-2027 PM internship. It is separate from the dashboard product, which lives in `veer-sanyal/india-msme-digital-trade-exposure`.

**PRIVATE.** This repo holds a psychological profile and logs with real names. Never make it public.

## How it runs (Claude Code, since 2026-07-03)

The system runs in **Claude Code** with this folder as the working directory. Migrated from the Cowork project 2026-07-03: the standing prompt moved from the pasted custom-instructions field into `CLAUDE.md` (auto-loaded every session), and the per-capability protocols became slash commands in `.claude/commands/`. Native git replaced the Cowork clone-commit workaround (the old sandbox mount couldn't delete git lock files; that whole class of problem is gone).

| Piece | Where |
|---|---|
| Standing prompt (durable protocol only) | `CLAUDE.md` |
| Daily reality-sync | `/reconcile` |
| Morning wake signal | `/initialize` |
| Sunday planning session | `/sunday` |
| Resume / cover letter | `/apply <company>` |
| Study / practice (Pillars 2 & 4) | `/tutor` |
| Post-call debrief (same-day loop close) | `/debrief <name>` |
| Session status banner (staleness, tripwires, git, telemetry gaps) | `.claude/hooks/session-start.sh` via the SessionStart hook in `.claude/settings.json` |
| Current state + live tripwires | `memory.md` (always read; carries the `Last reconciled:` stamp) |
| Running log | `PROGRESS.md` (tail) + `PROGRESS-archive.md` (history) |
| Standing ledgers + relationships log + system signals | `ledgers.md` (split from PROGRESS.md 2026-07-08) |
| Session telemetry | `session-log.jsonl` (one line per session; feeds the monthly health check in `/sunday`) |
| File manifest | `file-index.md` (reference; consulted when looking for where something lives) |

Connectors: Gmail and Google Calendar come through the claude.ai connectors (MCP) in Claude Code; Gmail can only draft, never send, so the daily plan is delivered via **Google Calendar** (the recurring spine + Sunday-written block titles and Morning Briefings — spec in `context/daily-briefing-instructions.md`). LinkedIn is read via the Chrome connector when available.

## Setup on a new machine

1. Clone this repo (stays private) and `cd` into it.
2. Authenticate `gh` (`gh auth login`) so `/reconcile` can pull the product repo's commits.
3. Run `claude` in the folder. `CLAUDE.md` loads automatically; connectors are per-account (claude.ai), not per-machine. The tracked `.claude/settings.json` registers the SessionStart status banner; if a session opens without the `=== veer-pm-system status ===` banner, check that file.

## Daily rhythm (quick reference)

- **Morning (phone or laptop):** say "initialize" → wake log + today's plan, rebuilt forward if the wake slipped. This runs fine from claude.ai Code on the phone against this repo, so a laptop is not required at 9:00.
- **First session of the day, if the banner says STALE:** `/reconcile` runs before substantive work (usually folded into /initialize).
- **After any call:** `/debrief <name>` — log it, thank-you out same day, next tripwire opened.
- **Anything else mid-week:** just talk; the system reads what it needs. Structural changes wait for Sunday.
- **Sunday:** `/sunday` — week review, next week's calendar written, maintenance; first Sunday of the month adds the telemetry health check.

## Automation options (opt-in, deliberately not wired)

- **Phone-first /initialize** (recommended first): open this repo in Claude Code on claude.ai from the phone and run `/initialize` at wake. Fixes the missed-wake-log gap without new machinery. Verify on first run that the Calendar connector is reachable there.
- **Headless morning reconcile:** `claude -p "/reconcile"` from cron/launchd can pre-run the daily scan. Costs money per run, acts on Gmail/Calendar unattended, and needs pre-approved permissions — only wire it if manual reconciles are actually being missed, and start with a dry week (no calendar writes).
- **Fewer calendar-write prompts:** reconcile and Sunday sessions retitle blocks and write briefings weekly, and each write currently needs approval (the Jul 6 retitle denial was this). To pre-approve, add under `permissions.allow` in `.claude/settings.json`: `"mcp__claude_ai_Google_Calendar__create_event"` and `"mcp__claude_ai_Google_Calendar__update_event"` (deletes stay prompted). Veer adds this himself, or says "add the calendar permissions" in a session — the assistant is blocked from widening its own permissions without those exact words.
- **iMessage visibility — Status: OFF.** The externship team channel lives in iMessage, which reconcile cannot see (a recurring blind spot in the logs). The scan is wired in `/reconcile` but runs only while this line says ON. To opt in: change OFF to ON here, and grant the terminal app Full Disk Access (System Settings → Privacy & Security) so `~/Library/Messages/chat.db` is readable. This means the system reads personal messages — flip it deliberately.

## Reading convention (two tiers)

`context/` holds the working copies the assistant reads day-to-day (one canonical copy per doc, roughly half the tokens of the originals); `files/` holds the full deep-research originals for deep dives only. When a doc changes, its `context/` copy is updated in the same session. Full map in `file-index.md`.

## Keeping it current

Saving means committing: every change is committed and pushed before a session ends (rule in `CLAUDE.md`). Product decisions still go to `DECISIONS.md` in the dashboard repo.
