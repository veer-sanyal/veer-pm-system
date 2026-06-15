# Dynamic tracking + organization upgrade

Design + implementation plan. Authored 2026-06-15.

## Why

The system is strong at planning and recording but weak at three things that matter for its one purpose (land a Summer-2027 PM internship by driving *action*, not insight):

1. **The loop never closes.** It writes the plan to the calendar but never reads back whether the plan happened. The single highest-leverage action (the Dr. G reply) has stayed an unsent draft across multiple sessions, re-described instead of broken. That is the exact "insight without action" failure the system exists to prevent.
2. **State drifts because facts have no owner.** The same fact (pillar criteria, ship dates, outreach cadence) lives in up to four files and already contradicts itself. memory.md carries a scar ("this file has drifted before / still said Streamlit until 2026-06-04").
3. **The three-tier doc convention has a manual mirror step that silently drifts.** "Refresh the compressed `context/` copy in the same session" fails the moment a session forgets.

## Decisions (locked with Veer 2026-06-15)

- **Auto-reconcile: full auto, every session.** At the start of every session the assistant pulls product-repo commits, reads the calendar, and scans Gmail drafts, reconciles `memory.md` + `PROGRESS.md` to reality, and commits — before doing the user's ask. Mid-week sessions accept the added cost.
- **Docs: collapse three tiers to two.** Keep `context/` (the single read tier) + `files/` (full deep-research originals). Remove the `docs/` mirror entirely.
- **Single source of truth: canonical owner + pointers.** Each fact is owned by exactly one file; other files link, never restate.
- **Subsystem scope: tutor fixes now, application-docs versioning deferred.**

## Design

### 1. Auto-reconcile protocol (system prompt)

A new standing block, run silently at session start before substantive work:

1. **Commits** — pull the product repo's recent commit history; compare to memory.md "what's shipped"; fix drift.
2. **Calendar** — read the trailing ~7 days of work blocks + Morning Briefings; infer which committed actions happened (cross-ref commits / PROGRESS.md).
3. **Gmail drafts** — scan for tracked outbound still unsent (e.g. the Dr. G reply); surface as a live tripwire.
4. **Persist** — update memory.md (current state) and append/adjust PROGRESS.md; commit + push with a clear message.

Rules: report only what *changed* (one line: "reconciled: X, Y"), not the whole scan. If a connector is unavailable, say so plainly and proceed with what is available. Never claim a reconcile happened if it did not.

### 2. Closed-loop accountability (system prompt + daily-briefing spec)

- **Done-check:** each Morning Briefing leads with one line on yesterday's committed block ("Yesterday: <action> - done?"); the answer is recorded in PROGRESS.md.
- **Auto-decompose stuck items:** any work item carried across >2 sessions/days is broken into the single smallest physical next action (<=2 min to start) and marked a tripwire. Never re-list a stuck item verbatim. If the pattern repeats, name the avoidance.
- **Sunday reconcile-first:** the Sunday session opens by comparing the past week's *written* calendar block titles against PROGRESS.md / commits - scheduled vs. actually-done vs. slipped - before planning the new week.

### 3. Two-tier reading convention

- `context/` = working copies the assistant READS for all day-to-day work (one canonical copy per doc).
- `files/` = full deep-research originals; opened only for deep dives.
- `docs/` removed. The 9 mirrored originals are dropped (their `context/` copy wins); the 3 uncompressed originals move into `context/`.

### 4. Single-source-of-truth ownership map

| Truth | Owner | Others |
|-------|-------|--------|
| Strategy: goal, four pillars, success criteria, decision rules | `context/direction.md` | link only |
| Current state: shipped / focus / next moves | `memory.md` | link only |
| Day-by-day narrative + pillar ledgers + relationships log | `PROGRESS.md` | link only |
| Recruiting timeline + deadlines + application pipeline | `context/key-dates.md` | link only |
| Learning state (Pillars 2/4 mastery) | `context/study/state.json` | memory.md mirrors a regenerated summary, never hand-edited |
| Live operational schedule | Google Calendar | - |
| Product decisions with trade-offs | `DECISIONS.md` (product repo) | - |

Restated facts found elsewhere are replaced with a pointer to the owner.

### 5. Stale-content fixes (content, not structure)

- Atlassian AU/NZ window (Feb-Jun 2026): mark closed/past.
- Resume v1 timing: resolve the mid-July vs. post-Daniels contradiction (Daniels runs Jul 6-Aug 1).
- Google APM eligibility: add a one-line contingency (if ineligible -> named fallback primary).
- Daniels weekly-hours: add the contingency that protects the daily floor if hours run high.
- Outreach cadence: reconcile "3/week" vs. the milestone implying ~1.25/week.

### 6. Tutor micro-rules (the holes that bite on cold start)

- **Question-generation rubric:** what makes a valid item per topic (scope coverage + company-format match), so on-the-fly generation stays valid.
- **Bloom-promotion window:** define "2 consecutive correct" precisely (counts across sessions on the same topic; gap resets handled).
- **Ambiguous-answer rule:** clarify before rating rather than guessing the Bloom level.
- **Fatigue vs. weakness:** separate a real accuracy drop from end-of-session fatigue before suggesting a close.

## Implementation plan (phased, each phase a commit)

1. **Spec** - this file.
2. **System prompt** - rewrite `SYSTEM-PROMPT.md`: add auto-reconcile, closed-loop accountability, two-tier convention, ownership map; trim now-redundant restatement.
3. **Reorg** - move the 3 uncompressed `docs/` files into `context/`; delete the 9 mirrored `docs/` originals; remove `docs/`; fix every `docs/` reference across the repo.
4. **Ownership pass** - in `memory.md`, `context/direction.md`, `context/about-me.md`, `context/scheduling-blueprint.md`, `context/key-dates.md`, replace duplicated facts with pointers to the owner; fix the cadence contradiction.
5. **Stale fixes** - apply the section 5 content corrections in `context/key-dates.md` + `context/direction.md`.
6. **Tutor** - add the section 6 micro-rules to `context/study/curriculum.md`, `context/study/state-spec.md`, `context/study/study-tutor.md`.
7. **Index + README** - rewrite `file-index.md` for two tiers; update `README.md`.
8. **Commit + push** each phase to origin master.

## Out of scope (deferred)

- Application-docs profile-change tracking / legacy-resume versioning.
- Any new connector or external automation beyond the existing Calendar/Gmail/GitHub access.
