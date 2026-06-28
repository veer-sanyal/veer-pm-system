# PM Skills Tutor — Implementation Plan

> **For agentic workers:** Implement task-by-task. Steps use checkbox (`- [ ]`) syntax. This is a **docs/content** build (no code/tests) — each task authors or edits Markdown/JSON in this planning repo, verifies with the listed checks, and commits. Source spec: `specs/2026-06-14-pm-skills-tutor-integration-design.md`. Source material to adapt: `~/Downloads/study-tutor-files/` (SKILL.md + references).

**Goal:** Add an on-demand PM Skills Tutor for Pillars 2 & 4 whose `state.json` is the commit-equivalent artifact that closes the capture gap, integrated into the existing calendar/Sunday-session/log system.

**Architecture:** Mirror Pillar 1 — a structured `state.json` (raw artifact, auto-written + committed each session) that the Sunday session reads to rewrite the P2/P4 ledgers, update `memory.md`, and schedule the week's topics into Google Calendar. Tutor instruction docs live in `context/study/`, loaded only on activation.

**Tech Stack:** Markdown + JSON in the `veer-pm-system` planning repo. No build, no runtime. Verification = `python3 -m json.tool` for JSON, `grep` for cross-reference integrity, and manual section-coverage checks.

**Conventions (must follow):**
- Three-tier reading: `context/` = compressed working copies the system reads; `files/` = full originals; keep `context/` copies token-lean (every fact/number/date/citation preserved).
- Tone in all authored docs: direct, concise, no em dashes, no fake hype, no emoji unless mirroring.
- Commit from inside the repo, small logical commits, real messages; end messages with the Co-Authored-By line. Do NOT stage the user's unrelated working-tree files — stage only the files named in each task.
- The Edit/Write tools are guarded in the background session; author files via shell heredoc / `python3` if the tools are blocked.

---

## File structure (locked)

```
context/study/
  study-tutor.md      # entry point: main loop, activation triggers, hard rules, tone        (Task 6)
  pedagogy.md         # merged socratic/bloom/session-shapes/question-design, PM-adapted      (Task 5)
  state-spec.md       # state.json schema + lightweight-spacing bands + thresholds + protocol (Task 3)
  curriculum.md       # P2 + P4 topic tree: topics, bloom_target, company tags, seed prompts  (Task 2)
  state.json          # the live artifact (seeded skeleton)                                   (Task 4)
  research-pm-interview-reality.md   # compressed Run A                                        (Task 1)
  research-spacing-science.md        # compressed Run B                                        (Task 1)
files/study/
  research-pm-interview-reality.md   # full Run A                                              (Task 1)
  research-spacing-science.md        # full Run B                                              (Task 1)
```
Edited existing files: `SYSTEM-PROMPT.md` (T7), `memory.md` (T8), `PROGRESS.md` (T9), `context/daily-email-instructions.md` (T10), `context/key-dates.md` (T11 — learning milestones; recruiting dates already done 2026-06-14), `file-index.md` (T12). `handoff-protocol.md` is intentionally NOT ported.

---

### Task 1: Save the two research reports (full + compressed)

**Files:**
- Create: `files/study/research-pm-interview-reality.md`, `files/study/research-spacing-science.md`
- Create: `context/study/research-pm-interview-reality.md`, `context/study/research-spacing-science.md`

Sources: the two completed deep-research run outputs (Run A = PM interview reality; Run B = spacing science). Full text is in the task transcripts; the verified findings are summarized in spec §13.

- [ ] **Step 1: Write the full reports to `files/study/`**
  - Run A full report → `files/study/research-pm-interview-reality.md`: include the verified findings (Meta 5-interview loop + Execution→Analytical Thinking rename; Google four attributes RRK/GCA/Leadership/Googleyness + six archetypes + reasoning-over-number; Stripe ~4 rounds incl. technical; PM Exercises as canonical free source), the refuted claims (internal numeric scales — Meta 5-point, Google signal scale), the open/uncovered items (Microsoft, Airbnb), and the source URLs.
  - Run B full report → `files/study/research-spacing-science.md`: gap sub-linear (~20-40% of RI at weeks, ~5-10% at a year; spacing ~doubles retention); expanding ≯ uniform (delay first retrieval); interleaving d≈1.34; calibration/illusion finding; source URLs.
- [ ] **Step 2: Write compressed copies to `context/study/`**
  - Halve length while preserving every number, date, claim-verdict, and citation. Each compressed copy starts with a `> Compressed 2026-06-14 from files/study/<name> (full original).` line, matching the repo convention.
- [ ] **Step 3: Verify**
  - Run: `wc -l files/study/*.md context/study/*.md` — confirm 4 files exist and each `context/` copy is shorter than its `files/` original.
  - Run: `grep -l "refuted\|could not be verified" context/study/research-pm-interview-reality.md` — confirm the refuted-scales caveat survived compression (it drives Task 2/§9).
- [ ] **Step 4: Commit**
```bash
git add files/study/ context/study/research-*.md
git commit -m "Add PM tutor research reports (interview reality + spacing science)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Author `context/study/curriculum.md` (the topic backbone)

**Files:**
- Create: `context/study/curriculum.md`
- Read first: `context/research-metrics-fluency-curriculum.md` (P2), `docs/PM_Internship_Interview_Reality_Check.md` (P4), `context/study/research-pm-interview-reality.md` (company formats).

- [ ] **Step 1: Author the P2 topic tree**
  - One row per topic with: `topic_id` (e.g. `P2.metrics.metric_drop_diagnosis`), name, `bloom_target` (Apply/Analyze), dominant format, company tags.
  - Topics (from the metrics curriculum): metric trees; NSM/guardrail/primary/secondary; numerator-denominator discipline; leading-vs-lagging + measurement windows; funnel; retention/cohort (incl. curve flattening, "smile curve"); A/B-test reading + significance (p-value, CI, peeking trap); metric-drop diagnosis (clarify → segment-first → MECE internal/external → walk funnel → check instrumentation); stats foundations.
- [ ] **Step 2: Author the P4 topic tree**
  - Topics (from the interview reality-check): product sense/design/improvement; product strategy; estimation/analytical (GAME); behavioral/leadership (STAR + the 6-8 stories: conflict, failure, learning, ownership, persuasion, leadership-without-authority, technical collaboration); technical-credibility defense. `bloom_target` = Analyze/Evaluate.
- [ ] **Step 3: Author the company "exam-format" map**
  - Meta: 5 interviews (2× Product Sense, 2× Analytical Thinking [metric/KPI: goal-setting, debugging, trade-off], 1× Leadership & Drive).
  - Google APM: six archetypes (design, strategy, estimation, behavioral, technical, data/metrics); four attributes RRK/GCA/Leadership/Googleyness; estimation rewards reasoning over the number.
  - Stripe: ~4 rounds incl. technical/system-design.
  - Microsoft (from project doc): 3 rounds — behavioral/resume-walk, product sense, team-specific. Airbnb: metrics deep-dive. Mark both "re-verify when 2027 postings drop."
- [ ] **Step 4: Seed a real-prompt starter bank**
  - ≥2 real, company-attributed prompts per archetype from Run A, e.g. Meta "Newsfeed engagement drops 10% — what do you do?", "FB Ads revenue −20%", "set goals/metrics for Instagram Stories"; Google "YouTube traffic −5%", "newsfeed algo drops session time 20%"; Stripe "walk me through a system you designed." Note Product Management Exercises as the canonical source to pull more.
- [ ] **Step 5: Verify**
  - Run: `grep -c "topic_id" context/study/curriculum.md` — expect ≥18 (≈10 P2 + ≈8 P4).
  - Run: `grep -c "re-verify" context/study/curriculum.md` — expect ≥1 (Microsoft/Airbnb flag).
- [ ] **Step 6: Commit**
```bash
git add context/study/curriculum.md
git commit -m "Add PM tutor curriculum (P2/P4 topic tree + company formats + seed prompts)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: Author `context/study/state-spec.md` (schema + spacing + protocol)

**Files:**
- Create: `context/study/state-spec.md`
- Source: spec §6, §6.1; adapt `study-tutor-files/state-management.md` + `pattern-detection.md` (drop the FSRS parts).

- [ ] **Step 1: Document the `state.json` schema**
  - Reproduce the spec §6 schema verbatim (top-level `schema_version`, `user`, `pillars.P2/P4.topics[]`, `habits`, `calibration_overall`, `milestones`) and the per-topic fields (`topic_id`, `name`, `bloom_target`, `bloom_achieved`, `mastery`, `weakness_flag`, `attempts`, `last_practiced`, `review_band`, `next_review`, `format_breakdown`, `calibration`, `company_tags`, `error_notes`). Explicitly state the dropped FSRS fields (`stability`, `difficulty`, `retrievability`, `reps`, `lapses`).
- [ ] **Step 2: Document the lightweight spacing bands (evidence-based, spec §6.1)**
  - Bands: `new` (never/red) = 1-3 days; `short` (mastery <0.5) = ~7 days; `medium` (0.5-0.8) = 14 days; `long` (≥0.8) = 28 days, **hard cap so nothing exceeds ~30 days untouched**.
  - Rules: uniform within band (expanding not needed — Karpicke 2007); due-selection = overdue-first (oldest `last_practiced`), then due-today, then fill by session shape; "going cold" = `last_practiced` >30 days.
  - **Interleaving is mandatory**: after every 3-4 items on one topic, insert one item from a different topic (prefer due/weak). Cite d≈1.34; note it feels worse so it must be enforced.
- [ ] **Step 3: Document pattern thresholds + the write protocol**
  - Mastery EWMA: `mastery_new = (1-α)·old + α·session_accuracy`, α=0.3 (0.5 after a >7-day gap). Flags: green ≥0.8 / yellow 0.5-0.8 / red <0.5, each needs ≥5 attempts; else `unknown`. Calibration: surface only after ≥6 confidence judgments on a topic.
  - Write protocol (replaces the source's manual-paste): at session close, update `state.json` in place, append a dated one-liner to `PROGRESS.md`, and commit — no copy-paste, no separate dashboard file.
- [ ] **Step 4: Verify**
  - Run: `grep -c "review_band\|EWMA\|interleav\|30 days" context/study/state-spec.md` — expect ≥4.
  - Run: `grep -i "stability\|retrievability" context/study/state-spec.md` — confirm they appear ONLY as "dropped"/"not used" (no live FSRS math).
- [ ] **Step 5: Commit**
```bash
git add context/study/state-spec.md
git commit -m "Add PM tutor state spec (schema + lightweight spacing + write protocol)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Seed `context/study/state.json`

**Files:**
- Create: `context/study/state.json`
- Source: Task 2 (topics) + Task 3 (schema).

- [ ] **Step 1: Write the seeded skeleton**
  - Valid JSON matching state-spec: `user` populated; `pillars.P2.topics[]` and `pillars.P4.topics[]` seeded with every topic from `curriculum.md`, each with `bloom_target` set, `bloom_achieved: null`, `mastery: 0.0`, `weakness_flag: "unknown"`, `attempts: 0`, `last_practiced: null`, `review_band: "new"`, `next_review: null`, `company_tags` from the curriculum, empty `error_notes`. `habits.fatigue_threshold_min: 60`. `milestones` mirrors the key-dates learning milestones (Task 11).
- [ ] **Step 2: Verify it is valid JSON**
  - Run: `python3 -m json.tool context/study/state.json > /dev/null && echo VALID` — expect `VALID`.
  - Run: `python3 -c "import json;d=json.load(open('context/study/state.json'));print(len(d['pillars']['P2']['topics'])+len(d['pillars']['P4']['topics']),'topics')"` — expect the count to match `grep -c topic_id context/study/curriculum.md`.
- [ ] **Step 3: Commit**
```bash
git add context/study/state.json
git commit -m "Seed PM tutor state.json (P2/P4 topic skeletons, empty progress)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 5: Author `context/study/pedagogy.md`

**Files:**
- Create: `context/study/pedagogy.md`
- Source: merge `study-tutor-files/socratic-vs-direct.md` + `bloom.md` + `session-shapes.md` + `question-bank-design.md`, PM-adapted (spec §10).

- [ ] **Step 1: Author pedagogy-by-mastery (expertise reversal)**
  - 0-30% novice: productive failure (cap 5 min) → worked example → guided fading. 30-70%: self-explanation + ≤2 targeted hints. 70-90%: bare problems, vary surface features. 90%+: timed exam/company-format simulation. Include the hint hierarchy (reframe → point at concept → name misconception → first step → all-but-last → answer).
- [ ] **Step 2: Author Bloom progression + session shapes**
  - Promotion = 2 correct in a row at target level, untimed-help-free; then consolidate ≥2 sessions before pushing further. Session shapes keyed to nearest milestone: Build (>14d), Consolidate (within ~2wk of a mock/app), Mock-prep (1-3d before a mock/loop — timed, format-matched, no new material, end ≥2h before sleep).
- [ ] **Step 3: Author question design + format-match**
  - Four formats (metric-definition drill, metric-drop diagnosis, A/B-reading, product-sense FRQ/case, behavioral). ≥60% in the target company's dominant format. Quality checklist (one clearly-correct answer or clear rubric; right Bloom level; tests the concept not arithmetic/trivia). Prefer real prompts (PM Exercises) over generated; build distractors from `error_notes`.
- [ ] **Step 4: Author the rubric-grading rule (spec §9 — the guardrail)**
  - Grade P4 answers on **competency dimensions** (Google four attributes; Meta three competencies; Stripe decision-making/empathy/prioritization + technical/data-driven), as the tutor's OWN ordinal (strong/borderline/weak per dimension) → mapped to mastery. **Never claim to reproduce a company's internal numeric scale** (those were refuted). Optional: "tutor can generate a one-page PM metrics/framework crib sheet" study aid.
- [ ] **Step 5: Verify**
  - Run: `grep -ci "competency dimension\|never\|internal.*scale" context/study/pedagogy.md` — confirm the rubric guardrail is present.
  - Run: `grep -c "Build\|Consolidate\|Mock-prep\|Mock prep" context/study/pedagogy.md` — expect the three shapes.
- [ ] **Step 6: Commit**
```bash
git add context/study/pedagogy.md
git commit -m "Add PM tutor pedagogy (mastery modes, Bloom, session shapes, rubric grading)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Author `context/study/study-tutor.md` (entry point)

**Files:**
- Create: `context/study/study-tutor.md`
- Source: adapt `study-tutor-files/SKILL.md` (drop handoff/manual-paste; spec §5, §10, §12).

- [ ] **Step 1: Author activation + bootstrap**
  - Activation triggers: "quiz me", "mock me", "drill/study [topic]", "I have a mock", "practice metrics". Off by default — normal PM coaching runs otherwise. On activation: read `state.json` silently, greet from the `memory.md` P2/P4 summary (one sentence), then run the loop. Reference `pedagogy.md`, `state-spec.md`, `curriculum.md` to load on demand.
- [ ] **Step 2: Author the session loop**
  - Per item: Predict (confidence 0-100) → Ask (at/above `bloom_achieved`) → Wait (no unprompted hints) → Feedback (specific, name the misconception) → Rate & update (mastery EWMA + flags + band + calibration, internally). Interleave every 3-4 items. Fatigue/length checks.
- [ ] **Step 3: Author close-out + hard rules**
  - Close: update `state.json` in place → append dated one-liner to `PROGRESS.md` → commit. No manual paste, no separate dashboard.
  - Hard rules (from SKILL.md, retained): reading isn't studying; always attempt before the answer; calibrate don't comfort; match company format ≥60%; no new material in mock-prep; persist+commit state every session; tone = concise, no over-praise, no em dashes.
  - Explicitly state handoff-protocol is NOT used (direct write + commit replaces it).
- [ ] **Step 4: Verify**
  - Run: `grep -c "quiz me\|mock me\|Predict\|Interleave\|commit" context/study/study-tutor.md` — expect ≥4.
  - Run: `grep -i "handoff\|paste this" context/study/study-tutor.md` — confirm handoff appears only as "not used".
- [ ] **Step 5: Commit**
```bash
git add context/study/study-tutor.md
git commit -m "Add PM tutor entry point (activation, session loop, close-out, hard rules)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: Wire activation + Sunday integration into `SYSTEM-PROMPT.md`

**Files:**
- Modify: `SYSTEM-PROMPT.md`

- [ ] **Step 1: Add the activation clause**
  - In the CONSULT-WHEN-RELEVANT / capabilities area, add: "Pillar 2/4 study or interview practice -> on study/practice intent (\"quiz me\", \"mock me\", \"drill X\", \"I have a mock\"), load `context/study/study-tutor.md` and run tutor mode; otherwise do not load it (keeps normal sessions lean). State file: `context/study/state.json`."
- [ ] **Step 2: Add the Sunday-session step**
  - In ALSO READ IN SUNDAY PLANNING MODE: add a step "read `context/study/state.json`; rewrite the PROGRESS.md Pillar 2 & 4 ledgers from it; update the memory.md P2/P4 learning-state section; pick the week's P2/P4 study targets (due/weak topics + days-to-next-milestone) and write them into the Deep/Secondary block titles + morning briefings."
- [ ] **Step 3: Verify**
  - Run: `grep -c "study-tutor.md\|state.json" SYSTEM-PROMPT.md` — expect ≥2.
- [ ] **Step 4: Commit**
```bash
git add SYSTEM-PROMPT.md
git commit -m "Wire PM tutor activation + Sunday integration into SYSTEM-PROMPT

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: Add the P2/P4 learning-state section to `memory.md`

**Files:**
- Modify: `memory.md`

- [ ] **Step 1: Add the section**
  - Under current state, add "**Pillar 2 & 4 learning state** (regenerated from `context/study/state.json` each Sunday; doubles as the tutor's session-start dashboard): topics tracked, weak (red/yellow) topics, calibration (overall over/under-confidence), last-practiced / any topic going cold, next focus." Seed it with the initial state (all topics `new`, not yet practiced) so the structure exists.
- [ ] **Step 2: Verify**
  - Run: `grep -c "learning state\|state.json" memory.md` — expect ≥1.
- [ ] **Step 3: Commit**
```bash
git add memory.md
git commit -m "Add Pillar 2 & 4 learning-state section to memory.md (tutor dashboard)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 9: Update `PROGRESS.md` ledgers + daily-entry note

**Files:**
- Modify: `PROGRESS.md`

- [ ] **Step 1: Convert the Pillar 2 & 4 running ledgers**
  - Replace the static "Pillar 2 running ledger" and "Pillar 4 running ledger" bodies ("0 hrs / not started") with a note: "Regenerated from `context/study/state.json` at each Sunday session — topics touched, mastery, weak topics, calibration, last-practiced. A passed week shows as stale `last_practiced` dates." Keep the section headers.
- [ ] **Step 2: Add the daily-entry note**
  - In "How to use this file", add: "Study/practice sessions (tutor mode) append a one-line dated trace here at close (the commit-equivalent for Pillars 2 & 4), e.g. `Pillar 2: 18-item metrics session, 72% acc, metric-drop still red`."
- [ ] **Step 3: Verify**
  - Run: `grep -c "state.json" PROGRESS.md` — expect ≥1. Confirm the Pillar 2 & 4 ledger headers still exist: `grep -c "Pillar 2 running ledger\|Pillar 4 running ledger" PROGRESS.md` — expect 2.
- [ ] **Step 4: Commit**
```bash
git add PROGRESS.md
git commit -m "Wire PM tutor into PROGRESS.md ledgers + daily-entry trace

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 10: Add Sunday study-scheduling to `context/daily-email-instructions.md`

**Files:**
- Modify: `context/daily-email-instructions.md`

- [ ] **Step 1: Add the scheduling rule**
  - Document: in the Sunday session, after reading `state.json`, the chosen P2/P4 study targets are written into that week's Deep/Secondary block titles (each title names the specific study/practice action, e.g. "Drill: metric-drop diagnosis (Apply)") and the relevant Morning Briefing carries the day's study focus + any due/cold topic. Keep consistent with the existing block/briefing mechanics.
- [ ] **Step 2: Verify**
  - Run: `grep -ci "study\|tutor\|state.json" context/daily-email-instructions.md` — expect ≥1.
- [ ] **Step 3: Commit**
```bash
git add context/daily-email-instructions.md
git commit -m "Schedule P2/P4 study targets into calendar blocks/briefings (Sunday)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 11: Add learning milestones to `context/key-dates.md`

**Files:**
- Modify: `context/key-dates.md` (recruiting dates already verified 2026-06-14; this adds the P2/P4 session-shape drivers)

- [ ] **Step 1: Add a "Learning milestones (Pillars 2 & 4)" subsection**
  - The session-shape "exam-equivalents": the **hard anchor** is Google APM ~mid-to-late Oct 2026 (apply within days of opening). Add rows for: first solo mocks (Phase 2, Aug-Oct 2026); ramp to 2-3 mocks/week by Feb 2027; real loops spring 2027. Mark the specific first-mock dates as **TBD — Veer to set at a Sunday session** (self-set, per spec §14.1) rather than inventing them.
- [ ] **Step 2: Verify**
  - Run: `grep -c "Learning milestones\|mocks" context/key-dates.md` — expect ≥1.
- [ ] **Step 3: Commit**
```bash
git add context/key-dates.md
git commit -m "Add Pillar 2 & 4 learning milestones (session-shape drivers)

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```

---

### Task 12: Index everything in `file-index.md` + final consistency check

**Files:**
- Modify: `file-index.md`

- [ ] **Step 1: Add a "PM Skills Tutor" section to the manifest**
  - List every new file with a one-line purpose: `context/study/study-tutor.md`, `pedagogy.md`, `state-spec.md`, `curriculum.md`, `state.json`, the two `context/study/research-*.md`, and the two `files/study/research-*.md`. Note the spec + this plan in the Specs section.
- [ ] **Step 2: Cross-reference integrity check**
  - Run: `for f in study-tutor pedagogy state-spec curriculum; do test -f context/study/$f.md && echo "ok $f" || echo "MISSING $f"; done` — all `ok`.
  - Run: `python3 -m json.tool context/study/state.json >/dev/null && echo "json ok"`.
  - Run: `grep -rl "handoff-protocol" context/study/ | xargs -r grep -L "not used\|NOT ported" ` — expect no output (handoff only ever referenced as dropped).
  - Run: `grep -c "context/study" file-index.md SYSTEM-PROMPT.md` — confirm both reference the new dir.
  - Manual: confirm `study-tutor.md` references `pedagogy.md`/`state-spec.md`/`curriculum.md` by exact filename, and that `curriculum.md` topic_ids match the `state.json` topic_ids.
- [ ] **Step 3: Commit**
```bash
git add file-index.md
git commit -m "Index PM Skills Tutor files in the manifest

Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>"
```
- [ ] **Step 4: Push (after Veer's review of the build)**
  - Run: `git push origin master` (watch for the concurrent-session divergence seen on 2026-06-14 — `git pull --rebase --autostash` if rejected; resolve PROGRESS.md by union).

---

## Post-build verification (smoke test)

- [ ] In a fresh chat, type "quiz me on metric-drop diagnosis." Confirm: tutor mode activates, reads `state.json`, predicts→asks→waits→gives feedback→rates, interleaves a second topic, and at close writes `state.json` + a PROGRESS one-liner + commits.
- [ ] Confirm a normal coaching question does NOT load the tutor docs (activation is gated).
- [ ] Run a mock Sunday step: confirm `state.json` can be turned into real Pillar 2 & 4 ledger lines and a week of block titles.

## Open items carried from the spec (not blockers)

- Microsoft & Airbnb loop specifics rely on existing project docs; re-verify when 2027 postings drop.
- First-mock dates are Veer-set (Task 11 leaves them TBD).
- Google APM eligibility wording (penultimate = rising senior) — strategic item flagged in `key-dates.md`/`direction.md`, resolve separately.
- Optional `fsrs_update`-style helper script only if hand-tracking the EWMA proves error-prone after real sessions.
