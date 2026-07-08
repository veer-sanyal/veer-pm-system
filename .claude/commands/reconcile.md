---
description: Reality-sync the system (product commits, calendar, Gmail, tripwires) and persist what changed
---

# /reconcile

Reality is the source of truth, not the docs. Run this at the first session of the day (the `Last reconciled:` stamp in memory.md is stale) or when Veer asks. If the stamp is from today, do not re-run a full scan unless asked.

Keep it fast and quiet. Report only what CHANGED, in one or two lines ("reconciled: Anicito confirmed Jul 8; teammate kickoff email still unsent"), not the whole scan. If a data source is unavailable this session, say so plainly and reconcile from what is available. Never claim a reconcile happened if it did not.

Context discipline: the scans below are noisy. Fan them out to parallel subagents on a cheaper model (commits, calendar, and the three Gmail scans can run concurrently; give each the live names/rows it needs) and keep only their findings in the main session. The main context is for judgment and persistence, not raw digests.

## What to scan

Scan targets are read from the live files, never hard-coded here: the Application Pipeline in `context/key-dates.md` (rows not yet closed), the live names in `alumni-tracker.md`, the external-relationships log in PROGRESS.md, and any tripwires in memory.md.

1. **Product commits.** Pull recent commit history of the product repo: `gh api repos/veer-sanyal/india-msme-digital-trade-exposure/commits --jq '.[0:15][] | .sha[0:7] + " " + .commit.message' 2>/dev/null` (fallback: shallow-clone to a temp dir and `git log`). Compare against memory.md "what's shipped"; fix any drift.
2. **Calendar.** Read the trailing ~7 days of work blocks and Morning Briefings on Veer's primary calendar (Pacific), via the Google Calendar connector. Infer which committed actions actually happened, cross-referencing commits and PROGRESS.md.
3. **Gmail, three scans** (Gmail connector; it can only draft, never send):
   - **Drafts:** any tracked outbound still sitting unsent is a live tripwire; surface it.
   - **Inbound:** search for new replies or updates since the last reconcile on every live pipeline row and tracked thread (from the files above). Purdue-addressed mail (vsanyal@purdue.edu) reaches the connected gmail, so include Purdue threads. An application moving to take-home or interview stage is a flag for the Sunday session.
   - **LinkedIn replies via Gmail:** Pillar-3 outreach lives on LinkedIn, so an email-thread scan alone misses replies. LinkedIn sends a named notification per 1:1 message from `messaging-digest-noreply@linkedin.com` with subject "<Name> just messaged you". Query `from:messaging-digest-noreply@linkedin.com newer_than:<days since last reconcile>d` and match subject names against the live names in `alumni-tracker.md`; any hit is a tripwire (reply landed: draft the response, book the call). The digest can batch or lag, so treat it as a tripwire, not a clock; LinkedIn itself (via the Chrome connector if available) stays authoritative. Ignore other LinkedIn senders: `invitations@linkedin.com` connection-accepts, InMail/recruiter spam ("is waiting for your response"), and marketing.

## Closed-loop checks (while scanning)

- **Done-check:** record in PROGRESS.md whether yesterday's committed block actually happened.
- **Stuck items:** anything carried >2 sessions/days gets decomposed to the single smallest physical next action (under 2 minutes to start) and marked a tripwire. Never restate a stuck item verbatim; if it stalls a second time, name the avoidance.
- **Ahead-of-schedule replan:** for any FUTURE calendar block whose task is already done, retitle it honestly ("... — DONE early") and backfill the freed block with the next-highest-value action from the existing backlog (memory.md next moves, the Application Pipeline, pillars at zero this week). Match backfill to block type (deep = hardest pillar work; secondary = different category; small item = one shippable artifact), respect the 3-substantive-items-a-day ceiling, and prefer the most time-sensitive open tripwire. This only refills freed slots from the existing backlog; structural replans wait for Sunday. A freed block already in the past is just marked done, never backfilled.
- **Briefing refresh:** the Morning Briefings were written on Sunday and go stale as the week diverges. While the calendar is open, update TOMORROW's briefing if reality has moved: the done-check line names what actually happened (done, slipped, folded elsewhere), and the description carries the day's last-action tripwires (the P4 between-sessions gap). Tomorrow only; the rest of the week stays Sunday-owned.

## Persist

1. Update memory.md so CURRENT STATE matches reality (prune what is no longer true) and set the `Last reconciled:` stamp (date + time + what sources were reachable).
2. Append or adjust PROGRESS.md (dated entry).
3. Update `context/patterns.md` only if a logged pattern recurred or a new one crossed the 2-instance bar.
4. Commit and push.
5. Append the session's line to `session-log.jsonl` at session end (type `reconcile` if this was the session's main work). Give every tripwire a short stable slug the day it opens (`tripwires_opened`) and log the same slug the day it closes (`tripwires_closed`); the monthly health check computes loop-closing latency from those.
