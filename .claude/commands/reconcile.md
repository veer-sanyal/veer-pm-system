---
description: Reality-sync the system (product commits, calendar, Gmail, tripwires) and persist what changed
---

# /reconcile

Reality is the source of truth, not the docs. Run this at the first session of the day (the `Last reconciled:` stamp in memory.md is stale) or when Veer asks. If the stamp is from today, do not re-run a full scan unless asked.

Keep it fast and quiet. Report only what CHANGED, in one or two lines ("reconciled: Anicito confirmed Jul 8; teammate kickoff email still unsent"), not the whole scan. If a data source is unavailable this session, say so plainly and reconcile from what is available. Never claim a reconcile happened if it did not.

Context discipline: the scans below are noisy. Fan them out to parallel subagents on a cheaper model (commits, calendar, and the three Gmail scans can run concurrently; give each the live names/rows it needs) and keep only their findings in the main session. The main context is for judgment and persistence, not raw digests.

## What to scan

Scan targets are read from the live files, never hard-coded here: the Application Pipeline in `context/key-dates.md` (rows not yet closed), the live names in `alumni-tracker.md`, the external-relationships log in `ledgers.md`, and any tripwires in memory.md.

1. **Product commits — Pillar 1 is STICK (`~/Desktop/stick-dev`), local git, no remote** (re-pointed 2026-07-16; the India dashboard is a banked, finished artifact — scan it only if Veer touches it: `gh api repos/veer-sanyal/india-msme-digital-trade-exposure/commits --jq '.[0:15][] | .sha[0:7] + " " + .commit.message' 2>/dev/null`).

   Recent history: `git -C ~/Desktop/stick-dev log --oneline -15`. Compare against memory.md; fix any drift. **Read `~/Desktop/stick-dev/STATE.md` for phase + owner-actions rather than inferring from commits** — that file is authoritative and it self-updates.

   **The one number that matters — product code vs. prose.** STICK's failure mode is not idleness, it is that effort routes to documentation instead of the app (Jul 16 baseline: **1 of 250 commits touched `app/`**; >1.1MB of prose vs ~150KB of code). The session-start hook prints this automatically; confirm and interpret it here, don't recompute:

   ```
   git -C ~/Desktop/stick-dev rev-list --count HEAD              # all commits
   git -C ~/Desktop/stick-dev rev-list --count HEAD -- app/      # commits touching product code
   ```

   Zero `app/` commits across a window in which doc/process commits landed is **not** a quiet week; it is the pattern running, and it gets named directly (not re-listed). A run of `app/` commits is the counter-evidence and is worth saying out loud.

   **Never mirror STICK's build state into this repo.** `stick-dev` owns its own state (`STATE.md`, `DECISIONS.md`, `OPEN-DECISIONS.md`, `HISTORY.md`); memory.md points at it and records only the pillar-level read (is it moving, is it in front of a user, what's the next physical action). Two copies means one of them is lying by Tuesday.
2. **Calendar.** Read the trailing ~7 days of work blocks and Morning Briefings on Veer's primary calendar (Pacific), via the Google Calendar connector. Infer which committed actions actually happened, cross-referencing commits and PROGRESS.md.
3. **Gmail, three scans** (Gmail connector; it can only draft, never send):
   - **Drafts:** any tracked outbound still sitting unsent is a live tripwire; surface it.
   - **Inbound:** search for new replies or updates since the last reconcile on every live pipeline row and tracked thread (from the files above). Purdue-addressed mail (vsanyal@purdue.edu) reaches the connected gmail, so include Purdue threads. An application moving to take-home or interview stage is a flag for the Sunday session.
   - **LinkedIn replies via Gmail:** Pillar-3 outreach lives on LinkedIn, so an email-thread scan alone misses replies. LinkedIn sends a named notification per 1:1 message from `messaging-digest-noreply@linkedin.com` with subject "<Name> just messaged you". Query `from:messaging-digest-noreply@linkedin.com newer_than:<days since last reconcile>d` and match subject names against the live names in `alumni-tracker.md`; any hit is a tripwire (reply landed: draft the response, book the call). The digest can batch or lag, so treat it as a tripwire, not a clock; LinkedIn itself (via the Chrome connector if available) stays authoritative. Ignore other LinkedIn senders: `invitations@linkedin.com` connection-accepts, InMail/recruiter spam ("is waiting for your response"), and marketing.

4. **iMessage + WhatsApp — the hard channels.** The iMessage DB read runs ONLY while the README automation section says visibility is ON (Veer's explicit opt-in): when ON, query `~/Library/Messages/chat.db` read-only for recent messages matching the live tracked names and the externship team thread. **WhatsApp: read it via WhatsApp Web in Veer's real Chrome (the claude-in-chrome connector), read-only — Veer opted in 2026-08-05.** Load the Chrome tools, open/select a tab at `web.whatsapp.com`, and read the chat list + the tracked threads (Naveen/Trice, Sudip Uncle, Mama). Open a thread only to read it; never type, send, or mark-up anything. If Chrome isn't running, WhatsApp Web is logged out, or the connector is unavailable, the channel is blind this session — say so. **When a channel is blind, do not just annotate it — actively ask Veer.** Real relationship state lives here: the Trice/Naveen WhatsApp thread, the externship team iMessage, the family side-thread. Close the scan with ONE short question naming the specific open threads that ride on these channels, and fold his answer in. Note which channels were actually read in the stamp; never treat absence as evidence nothing happened.

5. **PM-internship openings feed (Neal's scraper — borrowed, not built).** Neal (`nealtheseal108`) runs an ATS + tracker scraper on GitHub Actions every 8h and commits the merged PM feed to his repo. Read it, do not rebuild it:

   ```bash
   curl -sL "https://raw.githubusercontent.com/nealtheseal108/neal-pm-system/neal/Downloads/veer-pm-system-master/recruiting/feed-pm.json" | jq -r --argjson since <epoch of last reconcile> '"feed \(.updated|todate), \(.count) roles", (.roles[] | select(.firstSeen > $since) | select((.term // "") | test("2026") | not) | "\(.company) — \(.title) [\(.location)] \(.url)")'
   ```

   Third-party and unpinned: default branch is `neal`, the path carries `veer-pm-system-master` from the zip Neal forked, and either can move. If the curl or the jq returns nothing parseable, say "openings feed unreachable" and move on — never infer that no roles opened.

   **Relevance is a judgment call, not a field.** The feed filters on title keywords only; it carries no major or eligibility data, which is exactly Veer's CS-major worry. Two filters in order: (a) **term** — Veer needs Summer 2027; explicit 2026 rows are the wrong cycle and are already excluded above, and `unspecified` rows are usually 2026 long-tail, so verify the term on the posting before it earns a pipeline row. (b) **degree line** — "CS or related technical field" is defensible for IBE (precedent: the Databricks P-982 and Salesforce JR348039 rows in `key-dates.md`); "CS/EE required" plus coding deliverables is a skip, and say so rather than adding the row.

   **Do not auto-write pipeline rows.** Surface Summer-2027 hits that pass both filters as a short list for Veer to accept or kill; only accepted ones get a row in `context/key-dates.md`.

   **Expect it quiet until ~mid-September** (as of Jul 29: 30 roles, exactly 2 Summer 2027, both already closed rows). Quiet is the correct output in July, not a broken scan. It goes live with the Google APM posting, which is the same trigger that wakes Pillar 4.

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
