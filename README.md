# Veer PM Execution System (planning project)

This is the coaching and planning system for landing a Summer-2027 PM internship. It is separate from the dashboard product, which lives in `veer-sanyal/india-msme-digital-trade-exposure`.

## What changed and why this exists

The old setup tried to deliver a daily plan by scheduled Gmail send, which the Gmail connector cannot do (it only drafts). It was also synced to the dashboard repo, so the planning docs were never actually in the synced source and edits did not persist. This project fixes both: delivery moved to Google Calendar, and the planning docs get their own synced repo.

## Setup

1. Create a NEW, PRIVATE GitHub repo (for example `veer-pm-system`). It holds your psychological profile and PROGRESS.md with real names, so it must be private.
2. Push the contents of this folder to that repo (keep the `docs/`, `files/`, `specs/` folders as they are; the two-tier research convention depends on the folder split).
3. In the cowork project, paste the contents of `SYSTEM-PROMPT.md` into the project's custom-instructions field. Do not upload it as a doc; it is the standing prompt.
4. Sync the cowork project to the private repo.
5. Enable the Google Calendar connector on the project so the Sunday session can write the week directly. If it is not enabled, the assistant will output the events for you to add by hand.

## How delivery works now

- Google Calendar (your primary, Pacific) is the channel. The recurring spine is already on it: Deep block 9:45, Secondary 11:45, Workout 1:00, Small item 2:30 (Mon-Sat), and the Sunday planning session at 4:00.
- Each Sunday session retitles that week's three work blocks with the specific action and writes six 9:00 Morning Briefing events. The block titles are the triggers; the briefing holds yesterday's question, "this week feeds," and an optional citation.
- Full spec in `docs/daily-email-instructions.md`.

## Keeping it current

Because the project syncs from GitHub, saving means committing. The assistant updates `memory.md` (current state) and `PROGRESS.md` (the log), or outputs the exact edits for you to commit. Product decisions still go to `DECISIONS.md` in the dashboard repo.

## File map

See `file-index.md` for the full manifest.

## Still open (carried over)

- The two stale calendar events on your Google Calendar ("SQL Practice FAANG Prep" and "LinkedIn Networking 5 Alumni Outreaches") are from the pre-realignment plan and should be deleted.
