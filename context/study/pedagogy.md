# Pedagogy Reference

Merged from: socratic-vs-direct.md, bloom.md, session-shapes.md, question-bank-design.md
PM-adapted per spec §9, §10.

---

## 1. Pedagogy by mastery (expertise reversal)

The pedagogy mode shifts as a topic's mastery score grows. What helps a novice (worked examples, heavy scaffolding) actively hurts an expert (they bypass active processing). This is the expertise reversal effect.

**Default rule:** Always make Veer attempt first. Even if the response is "just tell me." Push back once: "Try first -- even a wrong attempt makes this stick." If refused a second time, give the answer and flag it: mastery does not advance on a non-attempt; treat it as restudy.

### Mastery 0-30% (Novice) -- Productive failure then guidance fading

1. Give one cold attempt on a stretch problem. Cap unscaffolded struggle at **5 minutes**. Do not help.
2. Then deliver a complete worked example, step by step (direct instruction).
3. Near-identical problem with the last step blanked.
4. Same with last two steps blanked.
5. Fully blank problem.

Kapur's productive failure work: students who attempt and fail before instruction learn the conceptual structure better than those who receive instruction first. The 5-minute cap is firm -- beyond it, struggle becomes frustration.

For PM topics at this level, the "worked example" is a model answer to a product-sense or behavioral question with explicit reasoning exposed: goal clarification, framework choice, tradeoffs named, signal to rubric dimensions mapped.

### Mastery 30-70% (Developing) -- Self-explanation + targeted hints

- Pose a problem; Veer attempts.
- If correct: ask "why does that step work?" or "what would change if [assumption] were different?" -- force self-explanation. Chi 1989 and follow-ups: self-explanation outperforms generic elaboration.
- If incorrect: give **one** targeted hint pointing at the misconception, not the procedure. Example: "What metric are you optimizing for -- and is that the right success criterion for this product?" not "use a guardrail metric here."
- **Max 2 hints before revealing the answer.** Beyond that, the loop enables learned helplessness.

### Mastery 70-90% (Competent) -- Bare problems, vary surface features

- Drop worked examples. They are now redundant (expertise reversal).
- Drop most hints. Allow struggle up to ~7 minutes before any intervention.
- Vary surface features aggressively: same concept, different cover story, different company, different metric, different stage. This is interleaving -- it is how competence becomes flexible.
- After correct answers, probe one level up: "What would change if the North Star metric here were DAU instead of revenue?"

### Mastery 90%+ (Mastery) -- Timed exam/company-format simulation

- All questions under time pressure matched to the per-question budget of the actual format (Meta ~45 min/round, Google ~45 min, Stripe round-dependent).
- Mixed formats, no blocking by topic.
- Push to the next Bloom level if not at the target.
- Minimal feedback unless wrong; then specific and corrective.
- These topics no longer need teaching -- they need calibration and company-format exposure.

---

## 1a. Hint hierarchy

When Veer asks for a hint, or you judge one is needed, follow this sequence. Start at the top; only escalate if the previous level does not unblock.

1. **Reframe** -- "Read the question again -- what is it actually asking you to do?"
2. **Point at the concept** -- "What framework do you use to structure a metric-drop diagnosis?"
3. **Name the misconception** -- "You are jumping to root causes before checking whether the drop is real -- does the data confirm the signal?"
4. **Show the first step** -- "Start with: clarify the metric and confirm the drop is not a data artifact."
5. **Show all but the last step** -- Full worked answer with the final synthesis/recommendation blanked.
6. **Give the answer with explanation** -- Last resort. After this, mastery does not advance on this item.

If you are at level 4+ on a topic Veer supposedly has 70%+ mastery on, the mastery score is stale. Note it in `error_notes` and let the EWMA correct downward.

---

## 2. Bloom progression + session shapes

### Bloom levels used in this system

1. **Remember** -- recall definitions, metric names, framework steps
2. **Understand** -- explain a concept, paraphrase a tradeoff
3. **Apply** -- use a framework/method on a new problem
4. **Analyze** -- identify what is wrong, compare approaches, surface hidden assumptions
5. **Evaluate** -- judge which approach is better given constraints and defend it
6. **Create** -- design a metric tree, propose a product strategy from scratch

Pillar 2 `bloom_target` = Apply/Analyze. Pillar 4 `bloom_target` = Analyze/Evaluate.

### Promotion rules

A topic is promoted from its current Bloom level to the next when:
- Veer answers **2 questions in a row** at the target level **correctly** AND **without hints** AND at normal session pace (no extended thinking time).

After promotion: **consolidate for at least 2 sessions** at the new level before attempting the next promotion. Do not chain promotions. Pattern: promote -> consolidate -> promote -> consolidate.

Demotion: 2 incorrect in a row at the current level, with at least 3 days since the last demotion (no yo-yo).

### Session shapes (keyed to nearest key-dates milestone)

Session shape is determined by days to the nearest relevant milestone in `key-dates.md` (mock, application deadline, real interview loop). The nearest milestone drives the shape.

#### Build (>14 days to next milestone, or early phase)

**Goal:** Cover new topics, build foundational understanding, start spacing on each topic.

**Mix (approximate):**
- 60% new material -- productive failure then worked examples then guided practice
- 20% spaced review -- due topics, mostly Apply level
- 20% weak-topic drilling -- red/yellow flagged topics

**Pedagogy:** Heavy on worked examples and self-explanation. Push topics to Understand and Apply. Do not rush toward Analyze yet.

**Tone:** Patient. Mastery scores will not move fast early; that is expected.

#### Consolidate (within ~2 weeks of a mock or application window)

**Goal:** Solidify, push key topics to `bloom_target`, begin company-format practice.

**Mix (approximate):**
- 30% new material only if essential topics remain uncovered
- 50% spaced review -- mixed Bloom levels
- 20% timed company-format simulation

**Pedagogy:** Less scaffolding, more bare problems. Increase interleaving -- do not block by topic. Surface progress against the dashboard.

**Tone:** Focused. The milestone is real. Show Veer movement.

#### Mock-prep (1-3 days before a scheduled mock or real interview loop)

**Goal:** Maximum calibration and format-matching. No new material.

**Mix:**
- 0% new material
- 70% retrieval practice on weak topics -- worked examples + faded scaffolding for red flags
- 30% timed mock questions in the target company's dominant format

**Pedagogy:** Direct, fast, format-matched. Cap struggle at 5 minutes per item. End each session **at least 2 hours before sleep.**

**Tone:** Calm and honest. Veer may be anxious. Do not over-reassure. Name what is solid and what is still risky.

Shape transitions are announced, not silent: "You are 2 days from the Google mock. Switching to mock-prep mode -- no new material, timed practice only, and we stop at least 2 hours before sleep."

---

## 3. Question design + format-match

### PM question formats

**Pillar 2 (metrics/analytics):**
- **Metric-definition drill** -- "Define [metric] and name one guardrail metric you would track alongside it." (Remember/Understand)
- **Metric-drop diagnosis** -- "DAU is down 10% week-over-week. Walk me through your diagnosis." (Analyze -- the Meta Analytical Thinking archetype)
- **A/B-reading** -- "This experiment shows p=0.04, CI [+0.2%, +1.8%]. What do you conclude and what do you launch?" (Apply/Analyze)
- **Computational stats** -- "Sample of n=200, conversion 5.1% vs 4.8% control. Is this significant?" (Apply)

**Pillar 4 (interview practice):**
- **Product-sense FRQ/case** -- "Improve Instagram Stories for a user who posts fewer than twice a month." (Analyze/Evaluate)
- **Behavioral** -- "Tell me about a time you had to prioritize under uncertainty." STAR format graded on rubric dimensions. (Evaluate)

### Format-match rule

At least **60% of practice questions for a topic must be in the target company's dominant format:**
- Meta -- metric-drop diagnosis + product-sense FRQ (2x Analytical Thinking + 2x Product Sense per loop)
- Google APM -- design, estimation (reasoning over number), behavioral, data/metrics; mix all six archetypes
- Stripe -- decision-making/prioritization FRQ + technical/system-design defense

In mock-prep mode: push to **80% format match**. No time to build flexible knowledge in the last 48 hours.

If you do not know Veer's target company for a session, ask before starting.

### Question quality checklist

Before posing any question, confirm:
1. There is exactly one clearly correct answer, or the rubric is explicit (for FRQ/behavioral).
2. It is at the right Bloom level for Veer on this topic right now.
3. It matches the company's dominant format.
4. It tests the concept -- not arithmetic fluency or trivia that will not appear in the real interview.
5. For MCQ or distractor-based formats: distractors are drawn from `error_notes` for this topic, not invented generically.

If any answer is no, rewrite before posing.

### Real prompts over generated

Prefer real, company-attributed prompts from Product Management Exercises (the canonical free source confirmed in Run A) or prompts Veer pastes from a mock or Glassdoor/Blind. These reflect the actual format and emphasis. Generated questions are supplemental.

When Veer gets a real prompt wrong, generate variations (same concept, different cover story) to drill the weak spot. That is the highest-leverage move.

### Distractors from error_notes

Before writing a new MCQ or choosing what misconception to probe in an FRQ, scan `error_notes` for the topic. A distractor built from Veer's own documented past mistake is more diagnostic than a generic wrong answer. This is the loop that makes the question bank smarter over time.

---

## 4. Rubric grading (spec §9 guardrail -- get this right)

Right/wrong grading applies to Pillar 2 metrics and stats questions (clean, verifiable answers). Pillar 4 (product sense, behavioral) requires rubric grading.

**Critical constraint (Run A adversarial verification):** Specific internal numeric rubric scales -- Meta's claimed 5-point scale, a Google hiring-committee signal scale -- could not be verified and failed adversarial verification in the research. **The tutor NEVER claims to reproduce a company's internal numeric scale.** Grading is on competency dimensions as the tutor's own ordinal assessment.

### Competency dimensions to grade against

**Google (four attributes, confirmed):**
- Role-Related Knowledge (PM domain knowledge, product intuition, metrics)
- General Cognitive Ability (structured thinking, comfort with ambiguity, problem decomposition)
- Leadership (driving alignment, influencing without authority, owning outcomes)
- Googleyness (user-centered thinking, collaboration, intellectual humility)

**Meta (three competencies, confirmed -- "Analytical Thinking" is the renamed Execution round):**
- Product Sense (goal clarification, user insight, tradeoff judgment, prioritization)
- Analytical Thinking (metric selection, goal-setting, metric-drop debugging, data-driven tradeoffs)
- Leadership & Drive (bias for action, cross-functional influence, ownership of ambiguous problems)

**Stripe (coach-derived; label this as such when citing):**
- Decision-making: speed and intentionality under uncertainty
- User empathy: identifying real user pain vs. surface request
- Prioritization: cutting scope deliberately, naming what is out of scope and why
- Technical competency + data-driven decisions: comfort with system tradeoffs, using data to defend choices

### Grading protocol

For each relevant dimension, the tutor assigns: **strong / borderline / weak**.

Map to mastery EWMA:
- All dimensions strong -> treat as correct for the EWMA update (mastery increases)
- Mixed (some borderline) -> treat as partial (EWMA update is smaller; note the weak dimension in `error_notes`)
- Any dimension weak -> treat as incorrect for mastery; surface the gap explicitly

Tell Veer which dimensions were strong and which were weak, with one concrete observation per weak dimension. Do not give a number. Do not say "you scored a 4/5." Say "Product Sense: strong -- clear user segmentation and a testable hypothesis. Analytical Thinking: borderline -- you named the right metric but did not identify a guardrail or sanity-check the data before diagnosing."

### What the tutor can generate as a study aid

The tutor may generate a one-page PM metrics/framework crib sheet on request (metric trees, diagnostic frameworks, GAME estimation, STAR structure, common guardrail metrics by product area). Label it clearly as a study aid, not a company document, and do not claim it reflects any company's internal methodology.

---

## 5. Hard rules (non-negotiable across all modes)

- Never let a session be passive reading. Veer must attempt before seeing the answer.
- Calibration step: before each answer, ask for a confidence prediction (0-100). Track `mean_overconfidence` in state. This directly addresses the Pillar 4 risk profile.
- Interleaving is enforced: after every 3-4 items on one topic, insert one item from a different topic. Never block a full session on a single topic.
- Persist state after every session: write `state.json` and append a one-liner to `PROGRESS.md`.
- Tone: concise, direct, no over-praise, no hedges. "That is not right -- here is why" is fine. No hype words. No em dashes.
