# Product Metrics & Applied Statistics for PM Interviews: A Beginner's Efficient Curriculum

**Audience:** A non-CS (business + engineering) undergraduate, beginner at PM, targeting Product Management internships, for whom *product metrics and applied statistics* are the #1 technical learning priority.

**Date:** 2026-06-04
**Author:** Research analyst (web-sourced)

---

## Executive Summary

For a beginner, the highest-leverage path to honest working fluency in product metrics and applied statistics is **not** to start with a polished paid course or with code. It is to build two foundations in parallel and only then add interview drilling:

1. **A free conceptual statistics base** — Khan Academy's free Statistics & Probability units on significance tests, p-values, and confidence intervals ([khanacademy.org](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)). This is the correct *entry point* for the stats half.
2. **A free hands-on product-analytics base** — Amplitude Academy's free, short, demo-account courses on funnel, retention, and cohort analysis ([academy.amplitude.com](https://academy.amplitude.com/)). This is the correct *entry point* for the product-metrics half, and it doubles as the tool you'll use for your dashboard project.

The **verified lead is confirmed and important**: DataCamp's *A/B Testing in Python* is explicitly an **Advanced** course (~4 hours, 57 exercises, covering p-values, power, MDE, and the Delta method for ratio metrics) that **requires the *Hypothesis Testing in Python* prerequisite and strong Python** ([datacamp.com/courses/ab-testing-in-python](https://www.datacamp.com/courses/ab-testing-in-python)). It is an **endpoint, not an entry point** for a beginner. *Hypothesis Testing in Python* is itself intermediate and assumes pandas + intro stats ([datacamp.com/courses/hypothesis-testing-in-python](https://www.datacamp.com/courses/hypothesis-testing-in-python)). A beginner who starts there will stall.

For interview content specifically, the **single best conceptual map** of what analytical/execution interviews test is Ben Erez's "definitive guide to mastering analytical thinking interviews" on Lenny's Newsletter — though note its full framework is **paywalled** ([lennysnewsletter.com](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)). Free substitutes (IGotAnOffer, RocketBlocks blog, Product Management Exercises, Exponent free content) cover ~90% of the same ground.

**Recommended spend:** A beginner can reach honest working fluency on a **near-zero budget** (Khan Academy + Amplitude Academy + free Exponent/IGotAnOffer/PM Exercises content + a free A/B significance calculator). One optional paid add-on with the best beginner ROI is **Exponent (~$12/mo on the annual plan)** for structured question banks and mock interviews ([review](https://medium.com/javarevisited/review-is-exponents-product-management-interviews-course-worth-it-2025-443e9296bf03)). **GoPractice (~$1,190)** and **Reforge (~$2,000/yr)** are high-quality but **not justified for an internship candidate** — Reforge in particular is built for *experienced* PMs ([review](https://uxcel.com/blog/reforge-product-strategy-course-review)).

Confidence is **high** on resource specifics (verified on primary pages), **high** on interview archetypes (multiple corroborating sources), and **moderate** on the exact week-by-week sequencing, which is a reasoned recommendation rather than an empirically validated plan.

---

## (a) What PM Analytical / Execution Interviews Actually Test

Across Meta, Microsoft, and Airbnb, the "execution" / "analytical thinking" / "metrics" interview consistently probes a small, learnable set of concepts. Below, each concept is defined and tied to how it shows up.

### 1. Goal → Metric trees (the spine of the whole interview)
Strong answers start from the **product goal**, derive a **North Star metric (NSM)**, then branch downward into supporting/input metrics. A **metric tree / KPI tree / driver tree** deconstructs a high-level *output* metric (e.g., revenue, MRR) into a hierarchy of actionable *input* metrics that teams can influence ([Mixpanel KPI trees](https://mixpanel.com/blog/kpi-trees/); [Petra Wille](https://www.petra-wille.com/blog/kpi-trees-how-to-bridge-the-gap-between-customer-behavior-product-metrics-and-company-goals)). Think of it as an equation: root = business goal, branches = intermediate drivers, leaves = user behaviors you can move ([Made to Measure KPIs](https://madetomeasurekpis.com/building-kpi-tree/)).

### 2. North Star vs. guardrail metrics; primary vs. secondary metrics
- **North Star metric:** the single signal of long-term value creation across all ecosystem players (e.g., "total streaming hours per week"), defined with a specific timeframe ([Lenny's Newsletter / Ben Erez](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81); [ProductHQ](https://producthq.org/product-analytics/north-star-metrics/)).
- **Primary metrics:** the desired outcome of a *specific* product/team/initiative; 3–5 per ecosystem player is the recommended discipline ([Lenny's/Ben Erez](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)).
- **Guardrail / counter metrics:** metrics that ensure a win on the primary metric did not *harm* another part of the ecosystem (e.g., engagement up but complaints/latency up). Meta explicitly probes how a goal can be "gamed or counter-indicative of progress" ([IGotAnOffer Meta](https://igotanoffer.com/blogs/product-manager/facebook-execution-interview); [Prepfully Meta](https://prepfully.com/interview-guides/meta-pm-analytical-thinking)).
- Good metrics are **actionable, measurable, and not game-able** ([RocketBlocks](https://www.rocketblocks.me/blog/success-metrics-pm-interviews.php)).

### 3. Numerator / denominator discipline
Interviewers expect a metric defined so precisely "someone could implement it tomorrow" ([Lenny's/Ben Erez](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)). For rate metrics this means being explicit about both **numerator** (e.g., "users who completed checkout") and **denominator** (e.g., "users who started a session" vs. "users who added to cart"). Retention illustrates this: you must define "active" consistently — login vs. purchase vs. a specific engagement event — and apply it identically across all cohorts ([Adjust](https://www.adjust.com/blog/demystifying-cohort-retention-session-kpis/); [Amplitude cohort retention](https://amplitude.com/explore/analytics/cohort-retention-analysis)).

### 4. Leading vs. lagging indicators
**Lagging** indicators report outcomes after the fact (e.g., churn, revenue). **Leading** indicators predict them earlier (e.g., engagement frequency, time-to-first-value). Power users who log in frequently retain better, so engagement signals act as *leading* indicators of retention; cohort analysis turns retention from a lagging indicator into a predictive lens ([Amplitude](https://amplitude.com/explore/analytics/cohort-retention-analysis)).

### 5. Measurement windows
A metric is meaningless without a window. NSMs are defined per-period (weekly streaming hours, WAU) ([Lenny's/Ben Erez](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)). Retention is a **curve over time** (Day-1/Day-7/Day-30, or week-over-week), where the x-axis is the timeline and the y-axis the % still active ([Personizely](https://www.personizely.net/glossary/cohort-retention-rate)).

### 6. Funnel, retention, and cohort analysis
- **Funnel:** break the user journey into stages (awareness → acquisition → activation → engagement → retention → monetization → referral) and find where users drop ([Exponent](https://www.tryexponent.com/blog/top-product-manager-interview-questions); [Amplitude funnel docs](https://amplitude.com/docs/faq/funnel-analysis)).
- **Cohort:** track groups acquired in the same period and measure what % stay active over time ([Hubifi](https://www.hubifi.com/blog/cohort-retention-guide)).
- **Retention curve shape:** a healthy curve drops then **flattens**; a rare "smile curve" dips, flattens, then rises as churned users return ([Personizely](https://www.personizely.net/glossary/cohort-retention-rate)).

### 7. Reading A/B tests & statistical significance
You must interpret, not compute by hand:
- **p-value:** probability of seeing a difference this extreme if there were truly no difference; p < 0.05 (95% confidence) is the common threshold ([PM Toolkit](https://pmtoolkit.ai/learn/experimentation/ab-testing-guide); [Kissmetrics](https://www.kissmetrics.io/blog/ab-testing-statistical-significance)).
- **Confidence interval:** the range the true effect likely falls in; often more decision-useful than a bare p-value ([Medium / Gusarova](https://medium.com/@data.science.enthusiast/understanding-confidence-intervals-in-a-b-testing-exploring-the-range-of-effect-sizes-and-cd39650cb4c7)).
- **Common trap to name in interviews — "peeking":** stopping the test the first time you see p < 0.05 inflates the false-positive rate (potentially to ~30%) ([PM Toolkit](https://pmtoolkit.ai/learn/experimentation/ab-testing-guide)).
- Advanced vocabulary (power, MDE, Delta method for ratio metrics) is *recognition-level* for interns, and is exactly what DataCamp's advanced A/B course teaches ([datacamp.com/courses/ab-testing-in-python](https://www.datacamp.com/courses/ab-testing-in-python)).

### 8. Diagnosing a metric drop ("debugging")
The canonical archetype (e.g., "DAU dropped 20%, what do you do?"). The expected approach:
1. **Clarify** the metric, magnitude, and timeframe; ask whether the drop was sudden vs. gradual, temporary vs. permanent ([Prodbee](https://prodbee.com/how-to-solve-product-execution-problems-the-great-pm-interview/)).
2. **Segment** before theorizing — by geography, platform, user tenure, channel. Say "sharpest among newly-registered users; returning users stable," not "DAU dropped 20%" ([Towards Data Science](https://towardsdatascience.com/answering-the-data-science-metric-change-interview-question-the-ultimate-guide-5e18d62d0dc6/)).
3. **Structure causes MECE: internal vs. external** — internal (bug, new release, broken CTA/feed/search) vs. external (seasonality, competitor, channel/tracking issue) ([IGotAnOffer](https://igotanoffer.com/blogs/product-manager/product-metric-interview-questions)).
4. **Walk the funnel** to localize the stage, and **check for measurement/logging breakage** (is the metric real or an instrumentation artifact?).

---

## (b) Best Resources, Honestly Compared

> **Cost/level/prereqs below were verified on primary pages where possible; pricing changes frequently, so re-confirm before paying.** Quality judgments are subjective and flagged as such.

### Free — the core of a beginner's stack

| Resource | What it's best for | Level | Cost | Honest assessment |
|---|---|---|---|---|
| **Khan Academy — Statistics & Probability** ([link](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)) | p-values, significance tests, confidence intervals, distributions — the *conceptual* stats base | True beginner → high-school/AP | Free | The right stats **entry point**. Bite-sized videos + practice. No product/PM framing — you supply that. |
| **Amplitude Academy** ([link](https://academy.amplitude.com/)) | Funnel, retention, cohort analysis — hands-on in a real tool | Beginner | Free (free demo/account) | The right product-analytics **entry point**. Short on-demand courses; doubles as your dashboard tool. Vendor-specific but concepts transfer. |
| **IGotAnOffer PM metrics/execution guides** ([metrics](https://igotanoffer.com/blogs/product-manager/product-metric-interview-questions), [Meta](https://igotanoffer.com/blogs/product-manager/facebook-execution-interview)) | Interview frameworks + example answers, free | Beginner→Intermediate | Free articles | Best free written frameworks for metric-definition and metric-drop questions. |
| **RocketBlocks blog (metrics, execution)** ([metrics](https://www.rocketblocks.me/blog/success-metrics-pm-interviews.php), [execution guide](https://www.rocketblocks.me/guide/pm/product-execution-interviews.php)) | Concise concept reviews | Beginner | Free articles (platform/drills paid) | Good free explainers; the *drills* platform and coaching are paid. |
| **Product Management Exercises** ([metrics Qs](https://www.productmanagementexercises.com/interview-questions/metrics)) | Huge bank of real questions + community answers + free mock-interview matching | Beginner→Advanced | Free tier; paid course exists | Best free **practice volume**; company-tagged (Meta/Microsoft/Airbnb) question sets. |
| **Exponent — free content / YouTube** ([guides](https://www.tryexponent.com/guides/meta-pm-interview)) | Company guides, mock-interview videos | Beginner | Free portion | Several reviewers report doing fine on the **free** content alone ([IGotAnOffer review](https://igotanoffer.com/en/advice/tryexponent-alternatives)). |
| **Free A/B significance calculators** ([Subscription Index](https://www.subscriptionindex.com/tools/statistical-significance-calculator)) | Build intuition by plugging in conversions and seeing p-value/CI move | Beginner | Free | Excellent for *reading* A/B results without coding. |

### Low-cost — optional, good ROI

| Resource | Best for | Level | Cost (verify) | Assessment |
|---|---|---|---|---|
| **Exponent (full subscription)** ([review](https://medium.com/javarevisited/review-is-exponents-product-management-interviews-course-worth-it-2025-443e9296bf03)) | 800+ PM questions, video courses, unlimited peer mocks, Slack | Beginner→Intermediate | ~$12/mo annual; ~$79/mo monthly | Best paid ROI for an intern budget; reviews are mixed because much overlaps the free tier. |
| **DataCamp (subscription)** ([pricing](https://www.datacamp.com/pricing)) | Coding up stats/A-B testing if you want the engineering depth | Mixed | Free tier = first chapter of 700+ courses; Premium ~$14/mo annual (~$168/yr) | Worthwhile *only if* you want to learn the Python/stats stack; see sequencing caveat below. |

### Higher-cost — generally NOT recommended for an internship candidate

| Resource | Why it's strong | Why to skip (for now) | Cost (verify) |
|---|---|---|---|
| **GoPractice Simulator** ([course page](https://gopractice.io/course/pm/)) | 235 real cases, ~100+ hrs, real Amplitude data, A/B & hypothesis testing, free skills-assessment test, 14-day refund | Excellent but expensive; overkill for an internship loop; time-heavy (1–1.5 months @ 1 hr/day) | ~$1,190 |
| **Reforge — Mastering Product Analytics** ([course](https://www.reforge.com/courses/mastering-product-analytics), [review](https://uxcel.com/blog/reforge-product-strategy-course-review)) | Deep retention/segmentation/causality content | **Built for experienced PMs**; "if you don't understand cohort analysis, start elsewhere"; whole-platform pricing | ~$2,000/yr membership |
| **RocketBlocks coaching** ([site](https://www.rocketblocks.me/)) | 1:1 expert coaching | Pricey per-hour; use only for a final polish | ~$200/hr |
| **Ben Erez full analytical-thinking guide** ([Lenny's](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)) | The single clearest interview framework | Full framework is **paywalled** (paid Lenny's subscription); his Maven bootcamp is a larger spend ([Maven](https://maven.com/ben-erez/pm-interview)) | Lenny's subscription / Maven course |

**Bottom line on (b):** A beginner needs **zero** of the higher-cost options to reach honest working fluency. The free stack (Khan + Amplitude Academy + IGotAnOffer/RocketBlocks/PM Exercises/Exponent-free) covers everything an internship interview tests, with Exponent's paid tier as the one reasonable upgrade.

---

## (c) Sequenced 6–8 Week Plan (with a parallel dashboard project)

**Time budget:** ~6–8 hrs/week. The dashboard project runs *throughout* — it's where concepts become muscle memory. Build it in a **free Amplitude account** (use their demo dataset) or a Google Sheet if you prefer no-tool friction; the goal is to *define metrics, build funnels, and read retention/cohorts yourself*.

### Week 1 — Stats foundation + metric vocabulary (ENTRY POINT)
- **Stats:** Khan Academy — descriptive stats, distributions, intro to significance tests ([link](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)). Goal: comfortable with mean/variance, sampling, what a p-value *means*.
- **Metrics:** Read IGotAnOffer metrics guide ([link](https://igotanoffer.com/blogs/product-manager/product-metric-interview-questions)) + ProductHQ North Star ([link](https://producthq.org/product-analytics/north-star-metrics/)). Learn NSM vs. guardrail, primary vs. secondary.
- **Verify:** Write your own one-paragraph definitions of NSM, guardrail, leading/lagging — in your own words, with an example each.

### Week 2 — Product-analytics tooling + funnels (start the dashboard)
- **Tool:** Amplitude Academy funnel + cohort courses ([link](https://academy.amplitude.com/)). Create a free account.
- **Project:** Pick a product (e.g., a to-do app, a streaming service). Build a **funnel** in Amplitude (or sketch one in Sheets) and define each stage's numerator/denominator explicitly.
- **Verify:** Your funnel has ≥4 stages, each with a precise metric definition. Have a peer/AI try to "implement it tomorrow" — if they have questions, tighten it.

### Week 3 — Retention, cohorts, leading vs. lagging
- **Tool:** Amplitude Academy retention chart + cohort analysis ([link](https://amplitude.com/explore/analytics/cohort-retention-analysis)).
- **Project:** Add a **retention curve** and a **cohort table** to your dashboard. Identify one leading indicator that would predict your retention.
- **Verify:** You can explain why your retention curve should flatten, and name a "smile curve" scenario ([Personizely](https://www.personizely.net/glossary/cohort-retention-rate)).

### Week 4 — Metric/goal trees + numerator/denominator discipline
- **Read:** Mixpanel/Made-to-Measure KPI-tree guides ([Mixpanel](https://mixpanel.com/blog/kpi-trees/), [MtM](https://madetomeasurekpis.com/building-kpi-tree/)).
- **Project:** Build a **metric tree** for your product: NSM at the root, primary metrics per ecosystem player, guardrails, leaf-level behaviors. Connect it to your funnel/retention work.
- **Verify:** Every leaf is a behavior you could move; every node has a clear numerator/denominator and window.

### Week 5 — Reading A/B tests & significance
- **Stats:** Khan Academy two-sample significance tests + confidence intervals ([link](https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples)).
- **Practice:** Use a free A/B significance calculator ([link](https://www.subscriptionindex.com/tools/statistical-significance-calculator)); plug in conversion numbers and narrate the result. Read PM Toolkit's A/B guide for the "peeking" trap ([link](https://pmtoolkit.ai/learn/experimentation/ab-testing-guide)).
- **Verify:** Given a result table (control vs. variant conversions), you can say whether it's significant, what the CI implies, and one reason it might be misleading.

### Week 6 — Diagnosing a metric drop
- **Read:** IGotAnOffer + Towards Data Science metric-change guides ([IGAO](https://igotanoffer.com/blogs/product-manager/product-metric-interview-questions), [TDS](https://towardsdatascience.com/answering-the-data-science-metric-change-interview-question-the-ultimate-guide-5e18d62d0dc6/)).
- **Project:** Imagine a 20% drop in your dashboard's NSM and write a full MECE (internal/external) diagnosis, segmenting first.
- **Verify:** Your write-up segments before theorizing, walks the funnel, and checks for instrumentation breakage.

### Weeks 7–8 — Mock-interview integration + company tailoring
- **Practice:** 10–15 questions from Product Management Exercises tagged Meta/Microsoft/Airbnb ([metrics bank](https://www.productmanagementexercises.com/interview-questions/metrics)); do ≥3 live peer mocks (free matching) — strong candidates do 20+ before interviewing ([source](https://www.productmanagementexercises.com/)).
- **Optional paid:** If budget allows, add **Exponent (~$12/mo)** for structured mocks ([review](https://medium.com/javarevisited/review-is-exponents-product-management-interviews-course-worth-it-2025-443e9296bf03)).
- **Verify:** You can do a clean metric-tree answer and a metric-drop diagnosis end-to-end in ~10–12 minutes without notes.

**Optional stretch (post Week 8, only if Python-comfortable):** DataCamp *Hypothesis Testing in Python* → *A/B Testing in Python* (the advanced endpoint) ([HT](https://www.datacamp.com/courses/hypothesis-testing-in-python) → [A/B](https://www.datacamp.com/courses/ab-testing-in-python)). **Not required for internship interviews.**

---

## Recommended ENTRY POINT (the single clearest place to start)

> **Begin with two free things in Week 1, in parallel:**
> 1. **Khan Academy Statistics & Probability** — significance tests / p-values / confidence intervals ([link](https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample)). This is the beginner stats entry point.
> 2. **Amplitude Academy** funnel/retention/cohort courses on a free account ([link](https://academy.amplitude.com/)). This is the beginner product-analytics entry point *and* your dashboard tool.
>
> **Do NOT start with DataCamp's *A/B Testing in Python*.** It is verified **Advanced** (~4 hrs, 57 exercises, p-values/power/MDE/Delta method) and requires the **Hypothesis Testing in Python** prerequisite plus strong Python ([datacamp.com](https://www.datacamp.com/courses/ab-testing-in-python)). It is an **endpoint**. Likewise **skip GoPractice (~$1,190) and Reforge (~$2,000/yr)** — quality is high but they're built for budgets/experience levels above an internship candidate ([Reforge review](https://uxcel.com/blog/reforge-product-strategy-course-review)).

---

## (d) Practice Drills, Self-Evaluation, and Company Archetypes

### Universal drills (do these weekly)
1. **Metric-definition drill:** Pick any app. In 5 minutes, write NSM + 3 primary + 2 guardrail metrics, each with numerator/denominator/window. **Self-eval:** Could a data scientist implement each tomorrow? ([standard](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81))
2. **Metric-drop drill:** Pick a metric + a % drop. In 10 minutes, produce a MECE internal/external diagnosis, segmenting first. **Self-eval:** Did you segment before theorizing and check instrumentation? ([TDS](https://towardsdatascience.com/answering-the-data-science-metric-change-interview-question-the-ultimate-guide-5e18d62d0dc6/))
3. **A/B-reading drill:** Take a result table; state significance, CI implication, and one caveat. **Self-eval:** Did you catch peeking/sample-size/guardrail issues? ([PM Toolkit](https://pmtoolkit.ai/learn/experimentation/ab-testing-guide))
4. **Funnel drill:** Draw a funnel and name the most likely drop-off stage and the metric to confirm it.

### Self-evaluation rubric (score each answer 0–2)
- Started from product **goal**, not a metric list (0–2)
- Defined metrics with explicit **numerator/denominator + window** (0–2)
- Included **guardrails/counter-metrics** (0–2)
- **Segmented** before hypothesizing in drop questions (0–2)
- Converged to a **decision/recommendation** (Meta explicitly rewards this) (0–2)

### Company archetypes

**Meta — "Analytical Thinking" (formerly Product Execution), ~45 min.**
Three question types: **goal/metric**, **debugging (metric drop)**, and **trade-off** ([IGotAnOffer](https://igotanoffer.com/blogs/product-manager/facebook-execution-interview); [Aakash Gupta/Medium](https://aakashgupta.medium.com/cracking-metas-new-analytical-thinking-pm-interview-insights-and-tips-ab3b0b8f40c6)). You **define metrics from scratch** (not pick from a list); follow-ups push on guardrails, counter-metrics, gaming, and metric conflicts; and you must **converge to a decision** ([Prepfully](https://prepfully.com/interview-guides/meta-pm-analytical-thinking)). *Map your drills:* heaviest weight on Drills #1 (metric definition + guardrails) and #2 (metric drop) and on the "converge to a decision" rubric line.

**Microsoft — Execution / metrics (~30% execution, ~30% behavioral, ~40% product sense).**
Emphasis on **data literacy + root-causing**: interpret metrics, diagnose usage/engagement drops, select KPIs tied to business goals (classic prompt: "Teams WAU dropped 10% — what do you do?") ([IGotAnOffer](https://igotanoffer.com/blogs/product-manager/microsoft-program-manager-interview); [Product Alliance](https://www.productalliance.com/guides/microsoft-pm-interview-cheat-sheet)). It's OK to assume data you don't have, but state you'd verify it ([source](https://igotanoffer.com/blogs/product-manager/microsoft-program-manager-interview)). *Map your drills:* heaviest weight on Drill #2 (metric drop) and KPI selection in Drill #1.

**Airbnb — Metrics Deep Dive + Execution + impact measurement.**
The loop includes a dedicated **Metrics Deep Dive** alongside Product Sense, Execution, and Core-Values rounds ([Exponent guide](https://www.tryexponent.com/guides/airbnb-product-manager-interview); [Coding Interview](https://www.codinginterview.com/guide/airbnb-product-manager-interview/)). They assess **what to measure and why**, not SQL/modeling; expect **A/B-test reasoning** and **two-sided-marketplace trade-offs** (guest-side wins must not burden hosts) ([source](https://www.codinginterview.com/guide/airbnb-product-manager-interview/)). *Map your drills:* heaviest weight on Drill #3 (A/B reading) and on guardrail/trade-off reasoning in Drill #1.

---

## Open Questions / Limitations

- **Pricing volatility.** All dollar figures (DataCamp ~$168/yr, Exponent ~$12/mo annual, GoPractice ~$1,190, Reforge ~$2,000/yr, RocketBlocks ~$200/hr) were sourced from primary/recent pages but **change frequently with promos** — re-verify at purchase ([DataCamp](https://www.datacamp.com/pricing), [GoPractice](https://gopractice.io/course/pm/)).
- **Paywalled best-in-class content.** Ben Erez's analytical-thinking guide is the clearest single framework but is **mostly paywalled** ([Lenny's](https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81)); the plan routes around it with free substitutes that cover ~90% of the same ground — a subjective estimate.
- **Sequencing is a reasoned recommendation,** not an empirically tested syllabus. The 6–8 week cadence assumes ~6–8 hrs/week; adjust for your baseline (the engineering background should make the stats faster).
- **Subjective quality judgments** (e.g., "Exponent is the best paid ROI," "Reforge is overkill") reflect fit for an *internship beginner on a budget*, not absolute quality. For an experienced PM, Reforge/GoPractice rankings would rise.
- **Tool specificity.** Amplitude Academy is vendor-specific; concepts transfer to Mixpanel/Sheets, but the exact UI does not. Verified that funnel/retention/cohort courses require only a free demo account ([academy.amplitude.com](https://academy.amplitude.com/)).
- **DataCamp lead fully confirmed:** *A/B Testing in Python* = Advanced, ~4 hrs, 57 exercises, p-values/power/MDE/Delta method, requires *Hypothesis Testing in Python* + strong Python — an endpoint, not an entry point ([primary page](https://www.datacamp.com/courses/ab-testing-in-python)).

---

## Sources

- Khan Academy — Significance tests (one-sample): https://www.khanacademy.org/math/statistics-probability/significance-tests-one-sample
- Khan Academy — Two-sample significance/confidence intervals: https://www.khanacademy.org/math/statistics-probability/significance-tests-confidence-intervals-two-samples
- Amplitude Academy: https://academy.amplitude.com/
- Amplitude — Cohort retention analysis: https://amplitude.com/explore/analytics/cohort-retention-analysis
- Amplitude — Funnel analysis docs: https://amplitude.com/docs/faq/funnel-analysis
- DataCamp — A/B Testing in Python (Advanced; verified specifics): https://www.datacamp.com/courses/ab-testing-in-python
- DataCamp — Hypothesis Testing in Python: https://www.datacamp.com/courses/hypothesis-testing-in-python
- DataCamp — Pricing: https://www.datacamp.com/pricing
- GoPractice — PM Simulator (cost/level/prereqs): https://gopractice.io/course/pm/
- Reforge — Mastering Product Analytics: https://www.reforge.com/courses/mastering-product-analytics
- Reforge review (level/pricing): https://uxcel.com/blog/reforge-product-strategy-course-review
- Exponent — Meta PM guide: https://www.tryexponent.com/guides/meta-pm-interview
- Exponent — Airbnb PM guide: https://www.tryexponent.com/guides/airbnb-product-manager-interview
- Exponent — Top PM interview questions: https://www.tryexponent.com/blog/top-product-manager-interview-questions
- Exponent course review (Javarevisited/Medium): https://medium.com/javarevisited/review-is-exponents-product-management-interviews-course-worth-it-2025-443e9296bf03
- IGotAnOffer — TryExponent alternatives/review: https://igotanoffer.com/en/advice/tryexponent-alternatives
- Lenny's Newsletter / Ben Erez — Definitive guide to analytical thinking interviews (paywalled): https://www.lennysnewsletter.com/p/the-definitive-guide-to-mastering-f81
- Ben Erez — Maven PM Interview Bootcamp: https://maven.com/ben-erez/pm-interview
- IGotAnOffer — Meta Analytical Thinking (execution) interview: https://igotanoffer.com/blogs/product-manager/facebook-execution-interview
- Prepfully — Meta PM Analytical Thinking deep dive: https://prepfully.com/interview-guides/meta-pm-analytical-thinking
- Aakash Gupta — Cracking Meta's Analytical Thinking interview: https://aakashgupta.medium.com/cracking-metas-new-analytical-thinking-pm-interview-insights-and-tips-ab3b0b8f40c6
- IGotAnOffer — Microsoft PM/Program Manager interview: https://igotanoffer.com/blogs/product-manager/microsoft-program-manager-interview
- Product Alliance — Microsoft PM cheat sheet: https://www.productalliance.com/guides/microsoft-pm-interview-cheat-sheet
- Coding Interview — Airbnb PM guide: https://www.codinginterview.com/guide/airbnb-product-manager-interview/
- IGotAnOffer — Product metric interview questions (metric-drop framework): https://igotanoffer.com/blogs/product-manager/product-metric-interview-questions
- Towards Data Science — Metric change interview question guide: https://towardsdatascience.com/answering-the-data-science-metric-change-interview-question-the-ultimate-guide-5e18d62d0dc6/
- Prodbee — Diagnosing a product issue (RCA): https://prodbee.com/how-to-solve-product-execution-problems-the-great-pm-interview/
- RocketBlocks — Success metrics PM interview questions: https://www.rocketblocks.me/blog/success-metrics-pm-interviews.php
- RocketBlocks — Product execution/analytics interviews guide: https://www.rocketblocks.me/guide/pm/product-execution-interviews.php
- Product Management Exercises — Metrics questions: https://www.productmanagementexercises.com/interview-questions/metrics
- Product Management Exercises — home/mock matching: https://www.productmanagementexercises.com/
- ProductHQ — North Star metrics: https://producthq.org/product-analytics/north-star-metrics/
- Mixpanel — KPI trees: https://mixpanel.com/blog/kpi-trees/
- Made to Measure KPIs — Building a KPI tree: https://madetomeasurekpis.com/building-kpi-tree/
- Petra Wille — KPI trees: https://www.petra-wille.com/blog/kpi-trees-how-to-bridge-the-gap-between-customer-behavior-product-metrics-and-company-goals
- PM Toolkit — A/B testing & statistical significance guide: https://pmtoolkit.ai/learn/experimentation/ab-testing-guide
- Kissmetrics — A/B testing statistical significance: https://www.kissmetrics.io/blog/ab-testing-statistical-significance
- Medium (Gusarova) — Confidence intervals in A/B testing: https://medium.com/@data.science.enthusiast/understanding-confidence-intervals-in-a-b-testing-exploring-the-range-of-effect-sizes-and-cd39650cb4c7
- Subscription Index — Free statistical significance calculator: https://www.subscriptionindex.com/tools/statistical-significance-calculator
- Personizely — Cohort retention rate (retention curve / smile curve): https://www.personizely.net/glossary/cohort-retention-rate
- Hubifi — Cohort retention guide: https://www.hubifi.com/blog/cohort-retention-guide
- Adjust — Cohort retention & session KPIs (defining "active"): https://www.adjust.com/blog/demystifying-cohort-retention-session-kpis/
