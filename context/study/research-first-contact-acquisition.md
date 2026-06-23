# Research: first-contact acquisition vs. attempt-first (the novice boundary)

*Deep-research pass, 2026-06-23. Question: for a true novice (mastery ~0, never seen the topic), should the tutor teach first (explanation + worked example, questions woven in) before asking them to attempt, or attempt-first / productive-failure? Five fan-out search angles + one adversarial verification pass. Every effect size below was either reported by the search agents and spot-checked, or independently verified in the verification pass.*

## The one-line finding

For genuinely new material where the learner has no relevant schema, **teach first, then retrieve**. Attempt-first / productive failure is a *consolidation* design that needs a floor of prior knowledge to work; it is not a first-contact design. The current tutor applies attempt-first to topics Veer has never seen (every P2 topic is `mastery 0.0`, `bloom_achieved: null`, flag `unknown`), which is the wrong tool for first contact. Fix: add a first-contact teach mode and switch to attempt-first only once a topic clears the floor.

## 1. Productive Failure needs a prior-knowledge floor; it is not for raw novices

- Problem-solving-before-instruction (PS-I / PF) beats instruction-first **overall**, but only as a moderate effect: **Hedges g = 0.36, 95% CI [0.20, 0.51]** (Sinha & Kapur, 2021, *Review of Educational Research*, 53 studies / 166 comparisons / ~12,000 learners). VERIFIED. Rises to g ≈ 0.37–0.58 only under high-fidelity PF design.
- The effect **reverses to favor instruction-first for the youngest / least-equipped learners (~grades 2–5)** and for domain-general skills (Sinha & Kapur, 2021). VERIFIED. The mechanistic read (Hartmann, van Gog & Rummel, 2022, *npj Science of Learning*): lower working-memory capacity and an inability to isolate deep features unaided. In their well-powered test (n=228, equivalent fractions) a full canonical PF design showed **no advantage** over direct instruction (F[1,224]=1.01, p=0.32).
- PF is *defined* as a state where learners hold initial "pre-concepts" but not enough to solve — i.e., it assumes a floor of relevant prior knowledge (Kapur; Hartmann et al. 2022 confirmed their participants had sufficient prerequisite knowledge, pretest ~4–5/10, to even generate attempts).
- PF only works when the failed problem-solving is followed by a **consolidation phase that contrasts student-generated solutions against the canonical one** (Loibl, Roll & Rummel, 2017; Loibl & Rummel, 2014). The active mechanism is *awareness of knowledge gaps* — which requires enough schema to notice the gap. Strip the consolidation and the benefit disappears.

**The apparent counter-finding, reconciled.** Kapur, Saba & Roll (2023, *npj Science of Learning*) found that within PF, "inventive production" (how many solution representations a student generates) predicts learning *far more* than prior math achievement — students benefited "regardless of prior math achievement." This sounds like it refutes the floor, but it does not (verification pass). Both schools in that study shared **high, statistically equivalent topic-specific prerequisite knowledge** (~8.6/10) and differed only in *general* achievement. The authors explicitly concede the study "may not extend to the lower end of the spectrum" — they never tested learners below the prerequisite floor. **Precise synthesis: PF needs a floor of relevant prerequisite knowledge to attempt the generation; above that floor, additional general ability is not the main moderator. A true novice at mastery 0 is below the floor.**

## 2. Cognitive Load Theory: novices should study worked examples before attempting

- **Worked-example effect**: for novices, studying worked examples beats equivalent unguided problem-solving. Sweller & Cooper (1985) — worked-example learners reached posttest ~twice as fast with ~1/5 the errors. Meta-analytic size on math: **Hedges g = 0.48** (Barbieri, Miller-Cotto, Clerjuste & Chawla, 2023, *Educational Psychology Review*, 55 studies / 181 effect sizes). VERIFIED. A medium effect.
- The advantage holds **only at the early stage of skill acquisition** (Renkl 2014; Sweller, van Merriënboer & Paas 1998) and **reverses** as expertise grows — the **expertise reversal effect** (Kalyuga, Ayres, Chandler & Sweller, 2003; Kalyuga, Chandler, Tuovinen & Sweller, 2001, "When Problem Solving Is Superior to Studying Worked Examples"). Mechanism: redundancy — guidance that duplicates an expert's existing schema adds extraneous working-memory load.
- So the design is **fade the guidance** as competence grows (example → completion problem → unassisted problem), not keep it forever. (See §5.)
- Boundary: worked examples must be well-structured (no split attention) or they help no more than problem-solving (Ward & Sweller, 1990). And the expertise-reversal pattern is cleanest in *well-structured* domains; in ill-structured ones it may not reverse the same way (Nievelstein et al., 2013 — CONTESTED).

## 3. The minimal-guidance debate: for novices, guided beats unguided — full stop

- Kirschner, Sweller & Clark (2006) argue minimally-guided instruction (pure discovery, unscaffolded PBL/inquiry) is less effective for novices because unguided search overloads working memory absent schemas. They concede the advantage of guidance only recedes once learners have enough prior knowledge to self-guide.
- Meta-analytic adjudication (Alfieri, Brooks, Aldrich & Tenenbaum, 2011, 164 studies / 580 comparisons): **unassisted discovery is worse than explicit instruction, d = −0.38 [−0.44, −0.31]**, but **enhanced/guided discovery (scaffolding, feedback, worked examples, elicited self-explanation) beats other instruction, d = +0.30 [0.23, 0.36]**. VERIFIED both signs. The active ingredient is guidance/feedback, not "generating" per se — pure unaided generation showed no benefit (d = −0.15).
- Direct test for initial acquisition: Klahr & Nigam (2004) — direct instruction produced **77% mastery vs 23%** for discovery on the control-of-variables strategy, **with no transfer penalty** (the directly-taught kids transferred just as well). VERIFIED exactly (40/52 vs 12/52).
- The rebuttals (Hmelo-Silver, Duncan & Chinn 2007; Kuhn 2007) are largely *definitional* — they agree scaffolding matters and argue good PBL/inquiry is heavily scaffolded. **Current consensus: the live question is how much guidance and when to fade it, not whether novices need it. They do.**

## 4. Ordering study vs. test on new material: pretesting helps, but only with feedback, and not for concepts

This is the strongest case *for* keeping some attempt-first flavor even at first contact, so it is worth stating precisely.

- A failed first attempt before instruction (pretesting / errorful generation) can match or beat equal-time study — Kornell, Hays & Bjork (2009): for meaningful associates, test-then-study beat study, d up to 1.49 (and 0.94 at a 38-hr delay), even though learners guessed correctly only 3–5% of the time.
- **But three conditions gate it**, and they matter for our case:
  1. **Corrective feedback after the attempt is near-necessary** (Kornell et al. 2009; Pan & Carpenter 2023). A pretest with no answer supplied is wasted.
  2. **It is item-specific** — it helps the pretested item, not the surrounding new material (Richland, Kornell & Kao, 2009).
  3. **It fails for conceptual / inference learning** — pretesting benefits *factual* recall but "may not be efficacious for inference-making tasks" (Hausman & Rhodes, 2018; Pan & Carpenter, 2023). Pillar 2 is mostly conceptual/applied (metric-drop diagnosis, numerator/denominator discipline), exactly where pretesting underperforms.
- Effect sizes are positive but highly variable (d ≈ 0.40–2.68; Pan & Carpenter 2023), and arbitrary/unprocessable material gets ~no benefit (Kornell Exp. 2, d ≈ 0).

**Implication:** a single short *guess-then-immediately-teach* probe (≤1 min, always followed by the answer) is defensible as the opening of first contact and aids encoding. A 5-minute unscaffolded *struggle* on conceptual material the learner has never seen is not — that is the part to cut.

## 5. When to switch a topic from teach-first to attempt-first (the fade rule)

Convergent signal across the worked-example and ITS literatures: move from worked-example/teach mode to independent problem-solving once the learner can do the unscaffolded step correctly, quickly, without referencing the example.

- **Guidance fading** (Renkl & Atkinson, 2003; Atkinson, Renkl & Merrill, 2003): sequence is full worked example → completion problems with progressively more missing steps (backward fading) → unassisted problem. Fading improves *near* transfer; *far* transfer needs added self-explanation prompts (CONTESTED that fading alone suffices).
- **Adaptive fading beats fixed fading beats pure problem-solving** (Salden, Aleven, Schwonke & Renkl, 2010, Cognitive Tutors) — pace the fade to the individual's measured understanding.
- Operational thresholds used by real mastery systems (all conventions, not proven optima):
  - Cognitive Tutor / Bayesian Knowledge Tracing: skill "mastered" at **P(known) = 0.95** (Corbett & Anderson, 1995). VERIFIED. Note: 0.95 is a convention to limit over-practice; recent work (EDM 2025) suggests ~0.98 may be better — CONTESTED.
  - ALEKS: mastery = solving **2–3 problems correctly without following the example**.
  - Khan Academy: ~70% = "Familiar"; all-correct on less-scaffolded items = "Proficient/Mastered".
  - Bloom mastery learning: ~80% formative-test criterion before advancing (convention).
- Consolidation should be **spaced retrieval scheduled *after* first-contact instruction**, not in place of it (Roediger & Karpicke 2006; spacing effect, ~10% delayed-test gain for spaced over massed). This is what the existing FSRS/spacing layer already does — it just needs to fire *after* teach mode, not instead of it.

## Design rule this licenses (for the system update)

1. **Detect first contact.** A topic with `bloom_achieved: null` (or mastery below a small floor, ~0.15–0.20) and flag `unknown` is below the prior-knowledge floor → first-contact teach mode.
2. **Teach mode (first contact):** optional ≤1-min guess-then-reveal probe → short plain-language explanation → fully worked example with reasoning exposed → completion problem (last step blanked) → fuller problem. Weave check questions through it. No 5-minute unscaffolded struggle. Cite: worked-example effect (Sweller & Cooper 1985; Barbieri et al. 2023, g=0.48), KSC 2006, Alfieri et al. 2011 (enhanced discovery d=+0.30), Klahr & Nigam 2004 (77 vs 23).
3. **Switch to attempt-first / productive-failure** once the topic clears the floor — operationalize as `bloom_achieved` reaches Understand/Apply AND ≥2 unaided-correct, mirroring guidance fading + the ~0.95/2–3-correct mastery conventions. From there the existing PF novice path (productive failure → worked example → faded practice) and the spaced-retrieval layer apply as written. Cite: Sinha & Kapur 2021 (g=0.36, floor + consolidation required), expertise reversal (Kalyuga et al. 2003), guidance fading (Renkl & Atkinson 2003), adaptive fading (Salden et al. 2010).
4. **Keep the spacing layer after teach**, not instead of it (Roediger & Karpicke 2006).

### Confidence + contested points
- HIGH: worked examples beat unguided problem-solving for novices; unassisted discovery loses to guided; PF needs a floor + consolidation; switch via guidance fading.
- MEDIUM / CONTESTED: exact mastery threshold (0.95 vs 0.98 vs 80%) is convention, not proven optimum; whether fading alone yields far transfer (needs self-explanation); whether expertise reversal generalizes to ill-structured domains; whether errorful generation builds associations for unrelated material.
