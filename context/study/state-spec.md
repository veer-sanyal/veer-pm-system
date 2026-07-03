# PM Tutor State Spec

*The schema, spacing rules, and write protocol for `state.json`. Load alongside `study-tutor.md` at session start.*

---

## 1. state.json Schema

`context/study/state.json` is the canonical artifact for Pillars 2 and 4 learning state. It is committed every session, making it the commit-equivalent for learning pillars.

### Top-level structure

```json
{
  "schema_version": "1.0",
  "user": {
    "name": "Veer",
    "goal": "Summer-2027 PM internship"
  },
  "pillars": {
    "P2": { "topics": [ /* per-topic objects; see below */ ] },
    "P4": { "topics": [ /* per-topic objects; see below */ ] }
  },
  "habits": {
    "sessions": [
      /* one entry per session: { date, duration_min, session_type, items, accuracy } */
    ],
    "median_session_min": null,
    "fatigue_threshold_min": 60
  },
  "calibration_overall": {
    "mean_overconfidence": null,
    "n_judgments": 0
  },
  "milestones": {}
}
```

**Top-level fields:**

| Field | Type | Notes |
|---|---|---|
| `schema_version` | string | `"1.0"` - bump if schema changes |
| `user.name` | string | Veer |
| `user.goal` | string | Human-readable goal driving study |
| `pillars.P2.topics` | array | P2 topic objects (metrics fluency) |
| `pillars.P4.topics` | array | P4 topic objects (core PM interview skills) |
| `habits.sessions` | array | Append-only session log; each entry: `date`, `duration_min`, `session_type` (Build / Consolidate / Mock), `items`, `accuracy` |
| `habits.median_session_min` | number\|null | Derived from sessions array; null until >=3 sessions |
| `habits.fatigue_threshold_min` | number | Default 60; update once fatigue pattern is detected |
| `calibration_overall.mean_overconfidence` | number\|null | Cross-topic mean; null until >=20 confidence judgments |
| `calibration_overall.n_judgments` | number | Total confidence judgments logged |
| `milestones` | object | Placeholder; learning milestones added as they are confirmed in `key-dates.md` |

### Per-topic object

```json
{
  "topic_id": "P2.diagnosis.metric_drop_diagnosis",
  "name": "Metric-drop diagnosis",
  "bloom_target": "Analyze",
  "bloom_achieved": null,
  "mastery": 0.0,
  "weakness_flag": "unknown",
  "attempts": 0,
  "last_practiced": null,
  "review_band": "new",
  "next_review": null,
  "format_breakdown": {},
  "calibration": {
    "mean_confidence": null,
    "mean_accuracy": null,
    "mean_overconfidence": null
  },
  "company_tags": ["Meta", "Google", "Microsoft"],
  "error_notes": []
}
```

**Per-topic field reference:**

| Field | Type | Notes |
|---|---|---|
| `topic_id` | string | Verbatim from `curriculum.md`; never rename without updating state |
| `name` | string | Human-readable name |
| `bloom_target` | string | Highest Bloom level required; from curriculum (Apply / Analyze / Evaluate) |
| `bloom_achieved` | string\|null | Highest level demonstrated under timed conditions (2 consecutive correct); null until earned |
| `mastery` | float | EWMA of accuracy, 0.0-1.0; see Section 3 for alpha rules |
| `weakness_flag` | string | `green` / `yellow` / `red` / `unknown`; see Section 3 for thresholds |
| `attempts` | integer | Total attempts across all sessions |
| `last_practiced` | string\|null | ISO date (YYYY-MM-DD) of last session touching this topic; null = never |
| `review_band` | string | `new` / `short` / `medium` / `long`; drives next_review; see Section 2 |
| `next_review` | string\|null | ISO date; `last_practiced + band_days`, hard-capped at 30 days |
| `format_breakdown` | object | Keyed by question format (e.g. `"metric_drop"`, `"goal_setting"`, `"behavioral"`); each value: `{attempts, correct}` |
| `calibration.mean_confidence` | float\|null | Mean pre-answer confidence (0-1); null until >=6 judgments |
| `calibration.mean_accuracy` | float\|null | Mean accuracy on judged items; null until >=6 judgments |
| `calibration.mean_overconfidence` | float\|null | `mean_confidence - mean_accuracy`; null until >=6 judgments |
| `company_tags` | array | Company names this topic is tested by; from curriculum |
| `error_notes` | array | Dated misconception strings; cap at 5 most recent, older ones drop off |

### Dropped FSRS fields (not used)

The following fields appear in the source `state-management.md` schema but are **not used** in this system. The lightweight banded approach (Section 2) replaces them:

- `stability` (FSRS memory stability parameter)
- `difficulty` (FSRS item difficulty)
- `retrievability` (FSRS predicted recall probability)
- `reps` (FSRS repetition count)
- `lapses` (FSRS lapse count)

Do not add these fields. If a future session requires more granular scheduling, bump `schema_version` and document the change.

---

## 2. Lightweight Spacing Bands (Evidence-Based)

Spacing science (Cepeda 2006/2008, Karpicke 2007, Kang 2014) shows the optimal gap is sub-linear relative to the retention interval. A simple linear formula overshoots. Fixed bands keyed to mastery, with a hard 30-day cap, capture the relevant behavior without drift-prone hand-computation.

### The four bands

| Band | Enter when | Review interval |
|---|---|---|
| `new` | Never practiced, OR red flag (mastery <0.5 after >=5 attempts) | 1-3 days |
| `short` | mastery <0.5 (developing) | ~7 days |
| `medium` | mastery 0.5-0.8 | 14 days |
| `long` | mastery >=0.8 (solid) | 28 days |

**Hard cap:** nothing exceeds ~30 days untouched. Any topic with `last_practiced` more than 30 days ago is surfaced as "going cold" regardless of band.

**Why uniform (not expanding) intervals:** Karpicke 2007 and Kang 2014 show expanding vs. uniform intervals produce equivalent long-term retention, provided the first retrieval is delayed (not massed). Uniform bands are simpler to track and less prone to drift. Promotion between bands is what provides expansion.

### Due selection order within a session

1. Overdue first: topics past their `next_review` date, sorted by oldest `last_practiced`.
2. Due today: topics where `next_review` equals today.
3. Fill with session shape (Build / Consolidate / Mock) logic after the above are cleared.
4. Any topic with `last_practiced` >30 days ("going cold") is treated as overdue regardless of `review_band`.

### Interleaving (mandatory, not optional)

Interleaving produces d=1.34 effect size and can double scores vs. blocking (Rohrer and Taylor, Foster, Kornell). It feels worse to learners, so it must be enforced structurally:

- After every 3-4 items on one topic, insert one item from a different topic.
- Prefer due or weak-flagged topics for the inserted item.
- Never block a full session on a single topic, even if requested.

The "feels worse" property is precisely why interleaving is not optional: learners who are allowed to self-select default to massing, which produces illusory fluency.

### Band transitions

- A session where accuracy pushes mastery EWMA above the next threshold triggers a band promotion at write time.
- A red-flag condition (mastery drops below 0.5 with >=5 attempts) resets `review_band` to `new`.

---

## 3. Pattern Thresholds and Write Protocol

### Mastery EWMA

```
mastery_new = (1 - alpha) * mastery_old + alpha * item_score

item_score = 1.0 Strong / 0.5 Borderline / 0.0 Weak. The EWMA now updates once per graded item (state is written incrementally), not once per session.
alpha = 0.3  (normal -- a single weak item cannot tank a solid topic; the weakness_flag also gates on attempts >=5)
alpha = 0.5  (on the first item back after a gap >7 days -- recent performance matters more after a long break)
```

A single bad session does not trigger a flag change. Only when the EWMA crosses a threshold does the `weakness_flag` update.

### Weakness flag thresholds

| Flag | Condition |
|---|---|
| `green` | mastery >=0.8 AND attempts >=5 |
| `yellow` | mastery 0.5-0.8 AND attempts >=5 |
| `red` | mastery <0.5 AND attempts >=5 |
| `unknown` | attempts <5 (not enough data to distinguish weak from unlucky) |

Never act aggressively on `unknown`. Surface as "tentative" if mastery looks low with n<5.

### Calibration surface rule

Do not surface per-topic calibration insights (show `calibration.mean_overconfidence`) until:
- >=6 confidence judgments on that topic, AND
- `calibration_overall.n_judgments` >=20

Before that threshold, collect judgments silently. Early calibration numbers are noise.

### Bloom promotion and demotion (defines "2 consecutive correct")

`bloom_achieved` is the highest Bloom level demonstrated. "Consecutive" is counted over the topic's own attempt history, NOT within a single sitting:

- **Promote** one level when the last 2 *attempts on this topic at the candidate level* are both rated Strong with no hints used. Interleaved items on other topics in between do not break the streak (the streak is per-topic). A Borderline/Weak rating, or a correct answer that needed a hint, resets the streak to 0.
- **Cross-session:** the streak carries across sessions. Two Strong attempts on different days still promote.
- **Gap / going cold:** if `last_practiced` is more than 30 days old, do not trust a previously earned `bloom_achieved`. Require one clean Strong (no hint) at that level to re-confirm it before testing one level higher; treat the streak counter as reset by the gap.
- **Demote** one level on 2 consecutive Weak ratings at the achieved level, or whenever the red-flag reset fires (mastery <0.5 with >=5 attempts). Demotion also resets `review_band` to `new` per Section 2.

The streak counter is computed from `format_breakdown` / recent ratings at write time; it is not a stored field.

### Error-note retention

`error_notes` keeps the 5 most recent misconception strings (newest wins). Additionally, drop a note when the same topic later earns a Strong rating on an item that targets that misconception -- a fixed misconception should not keep surfacing as a live weakness. When in doubt, keep it; a stale note is cheaper than a missed one.

### Write protocol (incremental -- write per item, commit at close)

The tutor writes state continuously, after every graded item, not only at close. No manual copy-paste, no separate dashboard file. Rationale: a session that ends abruptly (the tab closes, the chat ends, context runs out) must never lose work already done. The 2026-06-23 session was lost this way until manually re-saved two days later; incremental writes prevent a repeat.

**After every graded item (incremental, silent -- do this BEFORE asking the next question):**

1. Compute that item's updates in memory: increment `attempts`; update the mastery EWMA with the item score; recompute `weakness_flag` / `review_band` / `next_review`; update the topic `calibration` fields and `calibration_overall.n_judgments`; apply any Bloom streak change; add an `error_note` if a new misconception surfaced; update `format_breakdown`; set `last_practiced` to today.
2. Overwrite `context/study/state.json` in place with the new values. This write is silent (never shown to the user) and is the durability guarantee.

**At session close (or a fatigue/length trigger):**

1. Confirm the final item's write landed, then add or refresh the `habits.sessions` entry for this session (`date`, `duration_min`, `session_type`, `items`, `accuracy`) and `habits.median_session_min`. The per-topic fields are already current from the incremental writes -- verify, do not re-derive from scratch.
2. Append a dated one-liner to `PROGRESS.md`:
   ```
   YYYY-MM-DD: P2/P4 session - N items, X% accuracy, topics: [topic names]. Weak: [red/yellow flags if any].
   ```
3. Stage and commit (native git; the old Cowork clone workaround is retired):
   ```
   git add context/study/state.json PROGRESS.md
   git commit -m "Study session YYYY-MM-DD: [pillar] [session_type] - N items, X% accuracy"
   ```

**Commit cadence:** write the file every item; commit once at close. Do NOT commit per item -- the per-item disk writes (not commits) are the in-session durability guarantee.

**Safety net:** because `state.json` on disk is always current, a session that ends without a clean close is recovered by the next start-of-session reconcile, which reads `state.json`, detects the drift against the last commit, and commits it. Progress is never lost even if close-out never runs.

**Anti-patterns to avoid:**

- Do not dump `state.json` content to the user unless debugging. Reading and writing are silent.
- Do not commit on every item (too slow). Write the file every item; commit at close.
- Do not create a separate `dashboard.md` file. The human-readable current-state view lives in `memory.md`'s P2/P4 section, which is already read at session start.
- Do not add schema fields without bumping `schema_version` and documenting the change.
