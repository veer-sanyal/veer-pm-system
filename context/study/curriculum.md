# PM Tutor Curriculum: Pillar 2 (Metrics) + Pillar 4 (Core PM Skills)

*Topic backbone for the PM Skills Tutor. Each entry has a `topic_id` that is copied verbatim into `state.json` (Task 4). Do not rename without updating state.*

---

## Pillar 2: Metrics Fluency (P2)

topic_id format: `P2.<area>.<topic>`

---

- topic_id: P2.trees.metric_tree_construction
  name: Metric trees -- goal to NSM to input metrics
  bloom_target: Apply
  dominant_format: goal-setting / metric decomposition
  company_tags: Meta, Google, Microsoft

- topic_id: P2.metrics.nsm_guardrail_primary_secondary
  name: NSM / guardrail / primary / secondary metric hierarchy
  bloom_target: Apply
  dominant_format: goal-setting / metric definition
  company_tags: Meta, Google, Airbnb

- topic_id: P2.metrics.numerator_denominator_discipline
  name: Numerator-denominator precision -- defining metrics implementably
  bloom_target: Apply
  dominant_format: metric definition
  company_tags: Meta, Microsoft, Airbnb

- topic_id: P2.metrics.leading_vs_lagging
  name: Leading vs. lagging indicators and measurement windows
  bloom_target: Apply
  dominant_format: goal-setting / metric decomposition
  company_tags: Meta, Google, Microsoft

- topic_id: P2.analysis.funnel_analysis
  name: Funnel analysis -- drop-off localization across AARRR stages
  bloom_target: Analyze
  dominant_format: debugging / metric drop
  company_tags: Meta, Google, Microsoft, Airbnb

- topic_id: P2.analysis.retention_cohort
  name: Retention and cohort analysis -- curve flattening and smile curve
  bloom_target: Analyze
  dominant_format: debugging / product execution
  company_tags: Meta, Airbnb

- topic_id: P2.stats.ab_test_reading
  name: A/B test reading -- p-value, confidence interval, peeking trap
  bloom_target: Apply
  dominant_format: trade-off / analytical thinking
  company_tags: Meta, Google, Stripe, Airbnb

- topic_id: P2.stats.significance_foundations
  name: Stats foundations -- significance tests, confidence intervals, power
  bloom_target: Apply
  dominant_format: analytical thinking
  company_tags: Meta, Google, Stripe

- topic_id: P2.diagnosis.metric_drop_diagnosis
  name: Metric-drop diagnosis -- clarify, segment-first, MECE internal/external, walk funnel, check instrumentation
  bloom_target: Analyze
  dominant_format: debugging / metric drop
  company_tags: Meta, Google, Microsoft

- topic_id: P2.diagnosis.mece_cause_framework
  name: MECE cause classification -- internal (bug/release/feature) vs. external (seasonality/competitor/tracking)
  bloom_target: Analyze
  dominant_format: debugging
  company_tags: Meta, Microsoft

---

## Pillar 4: Core PM Interview Skills (P4)

topic_id format: `P4.<area>.<topic>`

---

- topic_id: P4.sense.product_design_improvement
  name: Product sense -- design and improvement questions
  bloom_target: Analyze
  dominant_format: product sense / design
  company_tags: Meta, Google, Microsoft, Airbnb

- topic_id: P4.strategy.product_strategy
  name: Product strategy -- market entry, ecosystem, big-bet prioritization
  bloom_target: Evaluate
  dominant_format: strategy
  company_tags: Google, Stripe

- topic_id: P4.estimation.game_framework
  name: Estimation and analytical -- GAME framework (Goals, Actions, Metrics, Evaluation)
  bloom_target: Analyze
  dominant_format: estimation / analytical
  company_tags: Google, Meta, Microsoft

- topic_id: P4.behavioral.star_stories
  name: Behavioral and leadership -- STAR story framework
  bloom_target: Evaluate
  dominant_format: leadership and drive / behavioral
  company_tags: Meta, Microsoft, Google, Stripe

- topic_id: P4.behavioral.conflict_story
  name: STAR sub-topic -- conflict resolution story
  bloom_target: Evaluate
  dominant_format: behavioral
  company_tags: Meta, Microsoft

- topic_id: P4.behavioral.failure_story
  name: STAR sub-topic -- failure and recovery story
  bloom_target: Evaluate
  dominant_format: behavioral
  company_tags: Meta, Google, Microsoft

- topic_id: P4.behavioral.learning_story
  name: STAR sub-topic -- learning and growth story
  bloom_target: Evaluate
  dominant_format: behavioral
  company_tags: Meta, Microsoft

- topic_id: P4.behavioral.ownership_story
  name: STAR sub-topic -- ownership and initiative story
  bloom_target: Evaluate
  dominant_format: behavioral / leadership
  company_tags: Meta, Google

- topic_id: P4.behavioral.persuasion_story
  name: STAR sub-topic -- persuasion and influencing without authority story
  bloom_target: Evaluate
  dominant_format: behavioral
  company_tags: Meta, Microsoft

- topic_id: P4.behavioral.leadership_without_authority_story
  name: STAR sub-topic -- leadership without formal authority story
  bloom_target: Evaluate
  dominant_format: behavioral / leadership
  company_tags: Meta, Google, Microsoft

- topic_id: P4.behavioral.technical_collaboration_story
  name: STAR sub-topic -- technical collaboration story
  bloom_target: Evaluate
  dominant_format: behavioral / technical
  company_tags: Microsoft, Stripe, Google

- topic_id: P4.technical.credibility_defense
  name: Technical-credibility defense -- projects, APIs, languages, system-design lite
  bloom_target: Evaluate
  dominant_format: technical
  company_tags: Microsoft, Stripe, Google

---

## Company Exam-Format Map

*Drives format matching in practice. Re-verify loop structures when 2027 postings drop.*

### Meta RPM

- **5 interviews total, ~45 min each.**
- Screen: 1x Product Sense + 1x Analytical Thinking.
- Onsite: 1x Product Sense + 1x Analytical Thinking + 1x Leadership and Drive.
- Analytical Thinking subtypes: (1) goal-setting / metric definition, (2) metric-drop debugging, (3) trade-off navigation.
- Interviewers grade on judgment and convergence to a decision, not framework completeness.
- Guardrail gaming and metric conflicts are standard follow-up pressure.
- Source confidence: high, 3-0 (IGotAnOffer, Exponent, StellarPeers).

### Google APM

- **Six question archetypes:** design, strategy, estimation, behavioral, technical, data analysis (metrics).
- **Four evaluated attributes throughout:** Role-Related Knowledge (RRK), General Cognitive Ability (GCA), Leadership, Googleyness.
- Onsite: multiple 45-min rounds. Product Alliance reports 5 total: 4 PM-led product + 1 engineer-led technical.
- Estimation: interviewers grade reasoning and approach, not the precise number.
- Googleyness reframing (Dec 2024) is language-only; attributes unchanged.
- Source confidence: high, 3-0.

### Stripe

- **~4 virtual onsite rounds, 45-60 min each**, preceded by recruiter screen.
- Includes a Technical round (system design + data analysis) with an engineer; often 2-part: walk through a past system + live design exercise.
- Bar is technical credibility, not CS-degree gate: APIs, data, developer experience, execution tradeoffs.
- Round taxonomy least settled; treat as approximate.
- Source confidence: medium.

### Microsoft PM Intern

- **3 Superday rounds, 45-60 min each**, preceded by 30-45 min recruiter screen.
- Round 1: behavioral + resume walkthrough -- line-by-line probe of technical projects, languages, APIs.
- Round 2: product sense / strategy via unconventional prompts ("design a parking lot"; "walk through your calendar and map it to PM behaviors").
- Round 3: team-specific -- may include Responsible AI, privacy, data-ethics tradeoffs; asks which AI tools you use and why.
- **Re-verify when 2027 postings drop.** No Microsoft intern claims survived the 2026 research verification run; structure drawn from `context/PM_Internship_Interview_Reality_Check.md`.

### Airbnb

- **Re-verify when 2027 postings drop.** No Airbnb intern listing found in May 2026 archive; no intern-specific claims survived verification.
- Proxy pattern: metrics deep-dive round alongside product sense; expect north-star metric selection, A/B-test reasoning, and two-sided-marketplace trade-offs (guest wins must not burden hosts).
- Source confidence: low (proxies only).

---

## Seed Real-Prompt Starter Bank

*Company-attributed, verified prompts only. For more: productmanagementexercises.com (canonical free source, company-tagged).*

### Metric Drop / Debugging

Mapped formats: P2.diagnosis.metric_drop_diagnosis, P2.analysis.funnel_analysis

| Company | Prompt | Source |
|---|---|---|
| Meta | "Newsfeed engagement drops 10%. What do you do?" | IGotAnOffer, Exponent RPM guide |
| Meta | "FB Ads revenue dropped 20%. What do you do?" | Leland; YouTube interview walkthroughs |
| Meta | "Events invite acceptance rate is down 5%. How do you approach fixing it?" | IGotAnOffer facebook-rpm |
| Google | "YouTube traffic is down 5% yesterday. How would you report this to Sundar Pichai?" | productmanagementexercises.com/4581 |
| Google | "The Newsfeed algorithm change drops average session time 20%. What do you do?" | productmanagementexercises.com/6532 |
| Microsoft | "Teams WAU dropped 10%. What do you do?" | IGotAnOffer Microsoft PM guide (re-verify exact wording) |

### Goal-Setting / Metric Definition

Mapped formats: P2.trees.metric_tree_construction, P2.metrics.nsm_guardrail_primary_secondary

| Company | Prompt | Source |
|---|---|---|
| Meta | "Set goals and measure success for Instagram Stories." | IGotAnOffer, Exponent RPM guide |
| Meta | "Set metrics and goals for Facebook Events." | IGotAnOffer facebook-rpm |
| Meta | "Set metrics and goals for Facebook Marketplace." | IGotAnOffer facebook-rpm |

### Product Sense / Design

Mapped format: P4.sense.product_design_improvement

| Company | Prompt | Source |
|---|---|---|
| Google | "Design a product for autonomous buses / public transportation." | IGotAnOffer Google APM guide |
| Google | "Design a fridge for colorblind users." | IGotAnOffer Google APM guide |
| Google | "Use Google's ecosystem to disrupt an industry." | IGotAnOffer Google APM guide |
| Microsoft | "Design a parking lot." | PM_Internship_Interview_Reality_Check.md |
| Microsoft | "Walk through your calendar/week and map each activity to a PM behavior." | PM_Internship_Interview_Reality_Check.md |

### Estimation

Mapped format: P4.estimation.game_framework

| Company | Prompt | Source |
|---|---|---|
| (generic) | "How many gas stations are there in the US?" | Generic Fermi-estimation warm-up (not company-attributed) |
| Google | "Estimate the number of queries Google Search handles per second." | Exponent Google APM guide |

### Technical Credibility

Mapped format: P4.technical.credibility_defense

| Company | Prompt | Source |
|---|---|---|
| Stripe | "Walk me through a system you have previously designed. Describe the architecture, components, and data flow." | Exponent Stripe PM guide (verified) |
| Microsoft | "Walk me through [resume project]. What language? What API calls? What would you change now?" | PM_Internship_Interview_Reality_Check.md |

### Behavioral / Leadership

Mapped formats: P4.behavioral.star_stories and sub-topic entries

| Company | Prompt | Source |
|---|---|---|
| Meta | "Tell me about a time you drove a project without formal authority." | IGotAnOffer Meta Leadership and Drive |
| Meta | "Tell me about a time you failed. What did you learn?" | IGotAnOffer Meta Leadership and Drive |
| Google | "Tell me about a time you had to persuade a skeptical stakeholder." | Exponent Google APM guide |
| Microsoft | "Tell me about a conflict with a teammate. How did you resolve it?" | PM_Internship_Interview_Reality_Check.md |

---

## Question-Generation Rubric

The seed bank above is a starter (~one prompt per topic), not a limit. When it is exhausted -- which happens fast -- generate new items, but a generated item is only valid if it passes this checklist. Generating freely without it drifts away from real interview format, which is the whole point of practice.

A valid generated item:

1. **Targets exactly one `topic_id`** and exercises the scope named in that topic's `name` field. E.g. `P2.analysis.funnel_analysis` must force drop-off localization across specific funnel stages, not a generic "how would you improve this metric."
2. **Matches the topic's `dominant_format`**, and in company mode the target company's format from the Company Exam-Format Map (honors the 60%-match rule, study-tutor §7.4). Meta -> Product Sense or Analytical Thinking; Google -> design / estimation / strategy graded on RRK + GCA; Microsoft -> resume-line probe or unconventional design; Stripe -> technical / system-design.
3. **Is pitched at the right Bloom level:** at `bloom_achieved` for consolidation, exactly one level above for a promotion attempt (never more than one above). Apply = run the procedure on a concrete case; Analyze = diagnose or decompose an ambiguous situation; Evaluate = make and defend a judgment under an explicit trade-off.
4. **Is concrete and grounded in a real surface** -- a named product, feature, change, or number -- not abstract ("how do you think about engagement?"). Borrow the shape of the verified seed prompts: one specific product, one specific change or number, one clear ask.
5. **Has a known good answer you can grade before you ask it.** If you cannot articulate what a Strong answer contains (and which rubric dimensions it hits), do not ask the question.

Anchor generated items to the seed prompts' shape. Do not invent company-specific facts, and do not claim a prompt came from a company's real loop unless it is in the seed bank above.
