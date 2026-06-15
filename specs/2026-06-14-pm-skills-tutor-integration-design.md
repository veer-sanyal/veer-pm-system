# PM Skills Tutor — integration design

> Spec. Status: drafted 2026-06-14, pending review. Folds in two deep-research runs (PM interview reality; spacing science) completed 2026-06-14 — see §13 and the saved reports under `files/study/` + `context/study/`.

## 1. Problem

Pillar 1 self-tracks: every bit of work leaves a GitHub commit, an automatic artifact the Sunday session reads to write the narrative. Pillars 2 (technical credibility) and 4 (interview readiness) have no equivalent. A study or practice block produces nothing the system can see unless Veer reports it and it gets written down. So the ledger reads "not started" not necessarily because nothing happened, but because nothing was *captured* — and that is exactly how a learning pillar goes to zero unnoticed until the Friday/Sunday review.

The fix is a tutoring subsystem whose **state file is the missing artifact** — the commit-equivalent for the learning pillars — plus an evidence-based practice loop so the captured work is real retrieval practice, not passive reading.

The source material is an existing exam-study-tutor skill (built for college exams in a web-Claude project) provided in `study-tutor-files/`: `SKILL.md` + references (state-management, fsrs, pattern-detection, bloom, socratic-vs-direct, cramming-protocol, handoff-protocol, question-bank-design, session-shapes) + a `Crib_Sheet` example. This spec adapts that machinery for PM-internship prep in this repo.

## 2. Goal / non-goals

**Goal.** An on-demand tutoring mode for Pillars 2 and 4 that (a) runs adaptive retrieval practice, (b) persists structured per-topic state automatically, and (c) feeds the Sunday session real ledger numbers so a learning pillar can never silently read zero.

**Non-goals.**
- Not Pillar 3. Outreach is not a learning activity; it already has its artifact in `alumni-tracker.md`. Excluded.
- Not a replacement for the dashboard (Pillar 1) — that stays the only end-to-end-owned artifact and the differentiator.
- Not a flashcard app, content generator, or confidence booster (inherits the source skill's "what this is NOT").
- Not a full FSRS implementation (see §6).

## 3. Scope decisions (locked with Veer 2026-06-14)

1. **Scope = Pillars 2 + 4.** Pillar 3 stays on `alumni-tracker.md`.
2. **Trigger = on-demand mid-week; Sunday schedules the week's topics** into the existing Deep/Secondary calendar blocks + morning briefings.
3. **State = structured file, integrated into existing logs** (mirrors how Pillar 1's commits feed PROGRESS/memory). Prose-only-into-PROGRESS was rejected: it throws away the structured mastery/calibration data and re-deriving mastery from prose is the exact anti-pattern the source `state-management.md` warns against.
4. **Spacing = lightweight** (mastery %, last-practiced, Bloom, calibration, weak flags + banded review intervals), not full FSRS stability/difficulty/retrievability math. Matches a soft 4-16 month horizon and avoids hand-computation drift.

## 4. Architecture (mirror Pillar 1)

Pillar 1: raw artifact (commits) → Sunday session reads it → writes the narrative (PROGRESS ledger, memory.md). The tutor takes the same shape:

```
study session  →  state.json (raw artifact, auto-written + committed each session)
                    │  + dated one-liner appended to PROGRESS.md (the "commit" trace)
                    ▼
Sunday session reads state.json
                    │
                    ├─→ rewrites PROGRESS.md Pillar 2 & 4 ledgers from real numbers
                    ├─→ updates memory.md P2/P4 current-state (doubles as the tutor's session-start dashboard)
                    └─→ picks the week's topics → Deep/Secondary block titles + morning briefings (Google Calendar)
```

No separate `dashboard.md` file (the source skill had one): the human-readable current-state view lives in `memory.md`'s P2/P4 section, which is already read at the start of every conversation — honors the repo's token-lean convention.

## 5. File structure

New, under the three-tier convention (the tutor's instruction docs are compressed working copies the system reads; loaded **only on activation**, not every session):

```
context/study/
  study-tutor.md   # main loop, activation triggers, hard rules, tone (adapted SKILL.md)
  pedagogy.md      # merged: socratic-vs-direct + bloom + session-shapes + question-bank-design, PM-adapted
  state-spec.md    # state.json schema + lightweight-spacing rules + pattern-detection thresholds + write protocol
  curriculum.md    # the P2 + P4 topic tree: topics, target Bloom, company-format tags (from the research + existing project docs)
  state.json       # the live artifact — committed each session
  research-pm-interview-reality.md   # compressed copy of the Run A report
  research-spacing-science.md        # compressed copy of the Run B report
files/study/
  research-pm-interview-reality.md   # full Run A report (originals, for deep dives)
  research-spacing-science.md        # full Run B report
```

Edits to existing files:
- `SYSTEM-PROMPT.md` — activation clause (load `context/study/study-tutor.md` only on study/practice intent) + a Sunday-session step that reads `state.json` and updates the P2/P4 ledgers + schedules topics.
- `memory.md` — a "Pillar 2 & 4 learning state" current-state section (weak topics, calibration, last-practiced, next focus). Doubles as the tutor's dashboard.
- `PROGRESS.md` — the Pillar 2 & 4 running ledgers change from static ("0 hrs / not started") to being regenerated from `state.json`; the daily-entry format gets a note that study/practice sessions append a one-liner.
- `context/daily-email-instructions.md` — Sunday session writes P2/P4 study targets into block titles + briefings.
- `context/key-dates.md` — carries the "exam-equivalent" milestones that drive session shape (see §7).
- `file-index.md` — index all new files.

**Dropped from the port:** `handoff-protocol.md` entirely (manual state.json copy-paste existed only because web-Claude couldn't write project files; this repo writes directly + auto-commits — keep only the "mini-checkpoint between sub-topics" idea, folded into the main loop). Full FSRS math (replaced by §6). `Crib_Sheet` not ported as system mechanism, but "tutor can generate a one-page PM metrics/framework crib sheet" is an optional study aid noted in `pedagogy.md`.

## 6. State schema (lightweight)

`context/study/state.json`. Per-topic fields (simplified from the source FSRS schema):

```json
{
  "schema_version": "1.0",
  "user": { "name": "Veer", "goal": "Summer-2027 PM internship" },
  "pillars": {
    "P2": { "topics": [ /* see below */ ] },
    "P4": { "topics": [ /* see below */ ] }
  },
  "habits": { "sessions": [ /* date, minutes, type, items, accuracy */ ],
              "median_session_min": null, "fatigue_threshold_min": 60 },
  "calibration_overall": { "mean_overconfidence": null, "n_judgments": 0 },
  "milestones": { /* mirror of the key-dates "exam-equivalents"; see §7 */ }
}
```

Per topic:
```json
{
  "topic_id": "P2.metrics.metric_drop_diagnosis",
  "name": "Metric-drop diagnosis",
  "bloom_target": "Analyze",
  "bloom_achieved": "Apply",
  "mastery": 0.0,                 // EWMA of accuracy, alpha 0.3 (0.5 after a >7-day gap)
  "weakness_flag": "unknown",     // green ≥0.8 / yellow 0.5-0.8 / red <0.5, each ≥5 attempts; else unknown
  "attempts": 0,
  "last_practiced": null,         // drives spacing + the "going cold" check
  "review_band": "new",           // new | short | medium | long  (see §6.1)
  "next_review": null,            // last_practiced + band length, capped at 30 days
  "format_breakdown": { /* per question format: attempts, correct */ },
  "calibration": { "mean_confidence": null, "mean_accuracy": null, "mean_overconfidence": null },
  "company_tags": ["Meta:AnalyticalThinking", "Google:data", "Microsoft:execution"],
  "error_notes": [ /* dated misconceptions, cap 5 most recent */ ]
}
```

No `stability`, `difficulty`, `retrievability`, `reps`, `lapses` (FSRS-specific) — replaced by `review_band` + `last_practiced`.

### 6.1 Lightweight spacing rules (evidence-based — §13 Run B)

The optimal study gap is a **sub-linear** fraction of the retention interval (~20-40% at weeks-scale, ~5-10% at year-scale; Cepeda 2006/2008), so a linear formula overshoots. Use fixed **bands** keyed to mastery, hard-capped so nothing goes cold:

| Band | Enter when | Review interval |
|---|---|---|
| `new` | never practiced, or red flag | 1-3 days |
| `short` | mastery < 0.5 (developing) | ~7 days |
| `medium` | mastery 0.5-0.8 | 14 days |
| `long` | mastery ≥ 0.8 (solid) | 28 days (**hard cap; nothing exceeds ~30 days untouched**) |

- **Expanding vs. uniform doesn't matter** (Karpicke 2007, Kang 2014): what matters is delaying first retrieval and not massing. So bands are uniform within a level; promotion shifts the band.
- **Due selection each session:** overdue first (oldest `last_practiced`), then due-today, then fill by session shape. A topic past its band length OR untouched >30 days is surfaced as "going cold."
- **Interleaving is enforced, not optional** (d≈1.34, can double scores, but feels worse — Rohrer/Taylor, Foster, Kornell): after every 3-4 items on a topic, insert one item from a different topic (prefer due/weak). Never block a whole session on one topic even if Veer prefers it.

## 7. Session shape — the "exam date" replacement

No single exam, so `key-dates.md` milestones supply soft deadlines. The nearest relevant milestone drives the shape:

- **Build** (>14 days to next milestone, or early phase): new topics + foundations. Pillar 2 mix-heavy.
- **Consolidate** (within ~2 weeks of a mock or application window): exam-format practice, push topics to their `bloom_target`, more interleaving.
- **Mock/interview prep** (1-3 days before a scheduled mock or real loop) — the source skill's "Cram," re-pointed: timed, format-matched, no new material, end ≥2 hours before sleep. The cramming-protocol survives almost intact.

Milestones to encode in `key-dates.md`: first solo mocks (Phase 2, Aug-Oct 2026), Google APM application (~early-mid Oct 2026), 2-3 mocks/week by Feb 2027, real loops spring 2027, plus the Application Pipeline deadlines already tracked.

## 8. Content mapping (curriculum.md)

**Pillar 2 topics** (from `research-metrics-fluency-curriculum.md`): metric trees, NSM/guardrail/primary/secondary, numerator/denominator discipline, leading/lagging + measurement windows, funnel, retention/cohort, A/B-test reading + significance (p-value, CI, peeking), metric-drop diagnosis, stats foundations. Formats: metric-definition drill, metric-drop diagnosis, A/B-reading, computational stats. `bloom_target` = Apply/Analyze.

**Pillar 4 topics** (from `PM_Internship_Interview_Reality_Check.md` + Run A): product sense/design/improvement, product strategy, estimation/analytical (GAME), behavioral/leadership (STAR + the 6-8 stories), technical-credibility defense. Formats: FRQ/case + behavioral. `bloom_target` = Analyze/Evaluate.

**Company "exam formats"** (from Run A — drives format-match per target):
- **Meta**: 5 interviews — 2× Product Sense, 2× Analytical Thinking (renamed from Execution; metric/KPI: goal-setting, metric-drop debugging, trade-offs), 1× Leadership & Drive. ~45 min each.
- **Google APM**: six archetypes (design, strategy, estimation, behavioral, technical, data/metrics); estimation grades *reasoning over the number*.
- **Stripe**: ~4 rounds incl. a technical/system-design round.
- **Microsoft / Airbnb**: from `PM_Internship_Interview_Reality_Check.md` (Microsoft 3 rounds: behavioral/resume-walk, product sense, team-specific; Airbnb metrics deep-dive). Not freshly re-verified in Run A — flagged for re-check (§14).

## 9. Rubric grading (competency dimensions — NOT fabricated scales)

Right/wrong grading works for Pillar 2 metrics/stats (clean answers). Pillar 4 (product sense, behavioral) is rubric-graded. **Critical constraint from Run A:** the exact internal numeric scales (Meta's claimed 5-point scale, a Google "hiring-committee signal scale") could not be verified and failed adversarial verification. The tutor therefore grades on **competency dimensions** (well-verified), as *the tutor's own rubric*, never claiming to reproduce a company's internal score labels.

Verified dimensions to grade against:
- **Google**: Role-Related Knowledge, General Cognitive Ability, Leadership, Googleyness — emphasis on clear communication, user-centered thinking, comfort with ambiguity, structured problem-solving.
- **Meta**: Product Sense, Analytical Thinking (metric selection, goal-setting, trade-offs, debugging), Leadership & Drive.
- **Stripe** (coach-derived, label as such): decision-making speed/intentionality, user empathy, prioritization; technical competency + data-driven decisions.

Tutor grade = a simple ordinal per dimension (strong / borderline / weak) → mapped to the topic's mastery EWMA. Calibration tracks Veer's pre-answer confidence prediction vs. the tutor's ordinal (see §6 + §10).

## 10. Pedagogy (ported, PM-adapted)

From the source `socratic-vs-direct.md` + `bloom.md` + `session-shapes.md` + `question-bank-design.md`, merged into `pedagogy.md`:
- **Pedagogy by mastery** (expertise-reversal): novice → productive failure then worked examples + fading; developing → self-explanation + ≤2 targeted hints; competent → bare problems, vary surface features; mastery → timed exam-format simulation.
- **Hard rules retained**: never let "studying" be reading; always make Veer attempt before the answer; calibrate don't comfort; match the exam (company) format ≥60%; no new material in mock-prep mode; persist state every session; tone = concise, no over-praise, no em dashes (matches the project's standing tone).
- **Calibration step** kept and validated (§13 Run B): predict confidence (0-100) before answering; track overconfidence. Directly attacks the Pillar 4 risk ("freezes under evaluation / overconfidence kills points").

## 11. Question bank (§7.1 resolved: seed a small real-prompt bank)

Run A confirms **Product Management Exercises** is the canonical free repository of real, company-tagged prompts; Exponent/IGotAnOffer/RocketBlocks are paid, curated, company-tagged; Glassdoor/Blind/Reddit are the raw first-hand layer. Approach:
- **Seed** `curriculum.md` with a starter set of real, company-attributed prompts per archetype (Run A surfaced e.g. Meta "Newsfeed engagement drops 10%", "FB Ads revenue −20%", "set goals for Instagram Stories"; Google "YouTube traffic −5%", "newsfeed algo drops session time 20%"; Stripe "walk me through a system you designed").
- **Generate** the rest on the fly per `question-bank-design.md` quality rules; **prefer real prompts** Veer pastes (PM Exercises, a mock prompt) over generated ones — they reflect the real format/distribution.
- Build distractors from `error_notes` (the loop that makes the bank smarter over time).

## 12. Activation ("only when needed")

- Tutor mode is **off by default**; normal PM coaching runs. Activates on study/practice intent: "quiz me," "mock me," "drill/study [topic]," "I have a mock," "practice metrics."
- On activation: read `state.json` silently → greet from `memory.md` P2/P4 summary → run the loop (diagnose shape → predict/ask/wait/feedback/rate → interleave → fatigue/context check → close) → at close, write `state.json` + append a dated one-liner to `PROGRESS.md` + commit. No manual paste.
- `SYSTEM-PROMPT.md` gets a short clause: load `context/study/study-tutor.md` *only* on activation (every other session stays lean).

## 13. Research findings folded in (2026-06-14)

Two deep-research runs (fan-out search → fetch → 3-vote adversarial verification → synthesis). Full reports saved to `files/study/`; compressed to `context/study/`.

**Run A — PM interview reality** (24 sources, 95 claims, 17/25 verified, 8 refuted):
- Confirmed: Meta 5-interview loop + Execution→Analytical Thinking rename (metric/KPI focus); Google four attributes (RRK/GCA/Leadership/Googleyness) + six archetypes + reasoning-over-number estimation; Stripe ~4 rounds incl. technical; PM Exercises as canonical free prompt source.
- Refuted (do not encode): specific internal numeric rubric scales (Meta 5-point; Google signal scale). → §9 uses dimensions only.
- Uncovered: Microsoft and Airbnb loops didn't survive fresh verification (use existing project docs, re-check closer to 2027); AI-product-sense is AI-track only.

**Run B — spacing science** (23 sources, 101 claims, 21/25 verified):
- Gap is sub-linear (~20-40% of RI at weeks, ~5-10% at a year); spacing ~doubles long-term retention (Cepeda 2006/2008). → §6.1 bands, not a linear formula.
- Expanding ≯ uniform; delay first retrieval, don't mass (Karpicke 2007, Kang 2014). → drop FSRS expansion.
- Interleaving d≈1.34, can double scores, feels worse → enforce it (Rohrer/Taylor, Foster, Kornell).
- Learners can't self-judge (78% better spaced yet believed massing equal) → keep the confidence-prediction step.

## 14. Open questions / re-verify before relying

1. **Milestone dates** — finalize the P2/P4 "exam-equivalents" + dates in `key-dates.md` (decision, not research).
2. **Microsoft + Airbnb loops** — not freshly verified; rely on `PM_Internship_Interview_Reality_Check.md` and re-verify when 2027 postings drop.
3. **No public internal scales exist** — never fabricate them; grade on dimensions (§9).
4. **Minimum maintenance cadence / many-topics-at-limited-hours** — Run B budget-dropped these angles from final verification; the 30-day cap + due-first ordering is a reasoned heuristic, revisit after real usage.
5. **Helper script** — only if hand-tracking the mastery EWMA proves error-prone after a few real sessions. Deferred.

## 15. Success criteria

- Any P2/P4 session auto-writes + commits `state.json` and a PROGRESS one-liner — no manual paste.
- The Sunday session produces real Pillar 2 & 4 ledger numbers (topics touched, mastery, weak topics, calibration, last-practiced) instead of "not started."
- A pillar can no longer silently read zero — a passed week surfaces via stale `last_practiced` dates at Sunday review.
- "Quiz me on X" mid-week runs a real adaptive session (predict → attempt → feedback → rate → interleave) and persists.

## 16. Implementation outline (for the plan)

1. Save the two research reports (`files/study/` + compressed `context/study/`).
2. Author `context/study/`: `study-tutor.md`, `pedagogy.md`, `state-spec.md`, `curriculum.md` (adapted from `study-tutor-files/`, applying §5-§12).
3. Seed `context/study/state.json` (P2 + P4 topic skeletons, empty progress).
4. Edit `SYSTEM-PROMPT.md` (activation + Sunday integration), `memory.md` (P2/P4 learning-state section), `PROGRESS.md` (ledger regeneration + daily-entry note), `context/daily-email-instructions.md` (Sunday scheduling), `context/key-dates.md` (milestones), `file-index.md` (index new files).
5. Commit per the repo's discipline (small logical commits, real messages, from inside the project repo).
