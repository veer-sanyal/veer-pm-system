# Daily Briefing Instructions (calendar-delivered)

**Filename note:** kept as `daily-email-instructions.md` so existing references in `scheduling-blueprint.md`, `direction.md`, `key-dates.md`, and the realignment spec still resolve. The mechanism is no longer email. The Gmail connector can only create drafts; it cannot send or schedule mail, so a scheduled 9:00 AM email was never buildable. Delivery is Google Calendar, because it pushes to Veer's phone without him initiating, which is the whole point for someone whose growth edge is initiation.

This file governs how the daily plan is composed and delivered. The planner reads it first to know the format, tone, content, and constraints.

---

## How delivery works

The plan lives on Veer's primary Google Calendar (Pacific time). Nothing is emailed. The week is written during the Sunday session, and Google pushes each event's reminder at the cue time. Veer never has to ask "what's today's plan." It is already on his calendar, with notifications that fire at the moment of action.

There are two layers:

1. **A recurring spine** (set once, never rewritten): the fixed daily shape.
2. **A content layer** (written each Sunday): the specific work for the week.

Removing the initiation step is the design. The calendar shows up whether Veer initiates or not.

## The recurring spine (already on the calendar)

These recur on fixed times and only need retitling, never recreating:

- Deep work block, Mon-Sat 9:45-11:15, reminder at start
- Secondary block, Mon-Sat 11:45-1:00, reminder at start
- Workout + lunch, daily 1:00-2:30
- Small visible item + admin, Mon-Sat 2:30-3:30, reminder at start
- Sunday planning session, Sundays 4:00, with its protocol in the event description

All times Pacific. Reminders fire at the start of each block so the notification itself is the trigger, not a heads-up 45 minutes early.

## The content layer (written each Sunday)

For each day Mon-Sat, the Sunday session produces two things.

### A. Three work-block titles

Retitle that day's deep, secondary, and small-item events so each reads as the specific action, not the generic label. The title is what the phone reminder shows, so it has to name the move.

Format: `[Block]: [specific action] (Pillar N)`

Examples:
- `Deep block: add telemetry to the dashboard (Pillar 1)`
- `Secondary: Khan Academy Statistics, first unit (Pillar 2)`
- `Small item: send 1 more alumni message, reach 3 this week (Pillar 3)`

The hardest pillar work goes in the deep block. A different category goes in the secondary to reduce attention residue. The small item is a guaranteed shipped artifact even on a bad day. The recurring blocks stay generic underneath, so if a Sunday is missed the time skeleton still appears (graceful degradation for the start-strong-then-drift pattern).

### B. One Morning Briefing event at 9:00 (15 min)

This is the connective tissue, not a re-list of the blocks (the blocks already carry the what). Its description holds, in order:

**1. Yesterday's question.** One specific question about yesterday's primary commitment. The calendar has no reply mechanism, so this is a self-check: Veer brings the answer to the Sunday session, or drops it in `PROGRESS.md` or the cowork chat. If Veer is not capturing answers for 3+ days running, the planner notes it at the Sunday session as a drift signal.

Examples:
- "Did you finish the data scout for Option B? What did you find?"
- "Did the deep block start on time? If not, what got in the way?"
- "Did you send the alumni message? If you drafted but did not send, what stopped you?"

**2. This week feeds.** One sentence linking today to the week's deliverable. Not motivation, just the link.

Examples:
- "This week feeds: Pillars 2 and 3 turn on while Pillar 1 awaits Dr. G."
- "This week feeds: dashboard iteration plus the first 3 alumni messages out by Saturday."

**3. Citation (optional).** Only when today's move rests on specific research and the move is not obvious. Maximum one. Skip otherwise.

Examples:
- "Why morning block: attention-residue research shows cognitive performance degrades through the day from accumulated unfinished loops. Hardest work goes first."
- "Why send before perfecting: Flynn and Lake found requesters underestimate compliance by up to 50%."

**4. Signature line (constant):**

```
If anything in today's plan has shifted, note it for the Sunday session. We adjust there by default.
```

## What the briefing does NOT include

- Inspirational language ("you got this")
- Motivational quotes
- The Google APM countdown (Sunday-level only)
- A progress visual (Sunday-level only)
- More than 3 substantive items in a day
- Reminders of the long-term goal (over-reminding causes goal-gradient demotivation)
- Anything Veer did not commit to on Sunday (no mid-week additions)
- Emoji (Veer flagged this)
- Em dashes (Veer flagged this)
- Streaks, scores, gamification
- Praise that dilutes edge

## Tone rules

- Direct without preachy
- Warm but not soft
- Specific over general
- Concise. If it can be said in 3 sentences, do not use 6
- No fake hype
- Treat Veer as capable. He does not need encouragement, he needs structure

When something needs flagging (slipped commitment, missed capture, drift signal), name it without drama and redirect to action. Not punitive, not coddling.

## The Sunday session writes the calendar

This is the keystone. The architecture works only if it happens. The same sequence lives in the Sunday-session event description:

1. Review `PROGRESS.md`: what shipped, what slipped, what surprised.
2. Name the pattern briefly. No deep diagnosis.
3. Define next week's commitments by pillar: what ships, gets learned, gets sent, gets practiced.
4. Turn each commitment into an implementation intention with a cue (when X, you Y).
5. Write the calendar:
   a. Retitle the coming week's three work blocks (Mon-Sat) with the specific action for each day.
   b. Write six Morning Briefing events at 9:00 with yesterday's question, this week feeds, and any short why.

The recurring blocks already hold the times, so the Sunday work is retitling plus the six briefings. No email send.

## The arc (visible, set rarely)

All-day banner events mark when pillars and phases turn on, so Veer can scroll forward and see the trajectory without asking. Examples already on the calendar: "Week 3: Pillars 2 + 3 turn ON," "Phase 2: fall recruiting opens," "Phase 3: Atlassian APM Intern window." Update these only when phases actually shift, not weekly.

## Sunday-level content

The Sunday Morning Briefing (or a dedicated Sunday event) carries what the daily ones do not:
- Last week's reflection: 3-4 sentences naming what shipped, slipped, surprised. Data, not analysis.
- The week's headline goal: one sentence on what this week produces.
- The Google APM countdown lives here, not in daily briefings.

Before each Sunday session the planner scans the past 7 days of Gmail and Calendar (Dr. G replies, alumni replies, application emails, events that landed, conflicts) and the next 14 days of Calendar (classes, commitments affecting deep-work scheduling), and opens the session with a brief summary so Veer does not re-explain.

## Mid-week updates

When something material happens between Sundays (Dr. G responds, an application opens, Veer wants to shift a block), Veer messages the planner directly. The planner:

1. Acknowledges the new information.
2. Updates the current week's calendar if needed (retitle a block, move a time).
3. Notes the change for the next Sunday session.
4. Does NOT rebuild the system or trigger a major replan. Sunday is where structural changes happen.

If Veer wants to skip the Sunday session or feels the system needs a major restructure, that is a signal to push back, not accommodate. The Sunday cadence is the keystone.

## Example: one day on the calendar (Mon Jun 8)

Calendar that day:
- 9:00 Morning briefing (description below)
- 9:45 Deep block: add telemetry to the dashboard (Pillar 1)
- 11:45 Secondary: Khan Academy Statistics, first unit (Pillar 2)
- 1:00 Workout + lunch
- 2:30 Small item: finish your LinkedIn profile (Pillar 3)

Morning briefing description:

```
Yesterday's question: Did you set this week's three commitments at the Sunday session? Bring the answer Sunday.

This week feeds: Pillars 2 and 3 turn on while Pillar 1 awaits Dr. G. By Saturday: telemetry live, first metrics modules done, first alumni messages sent.

Why telemetry now: the 2027 research moved the bar from "I built it" to "I measured usage or failure." Even page views let you answer what users do with data.

If anything in today's plan has shifted, note it for the Sunday session. We adjust there by default.
```

## When the system breaks

If the planner notices any of these across 2+ weeks, it surfaces them at the Sunday session:

- Sunday session getting skipped or rushed
- Veer not capturing answers to the daily question
- One pillar at zero output for 2+ weeks
- Veer asking to rebuild or redo the system mid-week
- Sleep dropping below 6 hours regularly
- Workout slipping (a leading indicator for him)

The response is not punishment. It is reducing volume, fixing cues, or finding what off-system pressure is eating bandwidth. The Sunday session is where this gets diagnosed and adjusted.
