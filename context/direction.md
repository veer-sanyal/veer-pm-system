> Compressed 2026-06-10. Canonical working copy (docs/ tier removed 2026-06-15).

# Direction

If an activity doesn't serve a pillar, it doesn't go in the plan.

---

## The goal

Land a PM internship for summer 2027 at a FAANG-tier or equivalent company.

**Primary targets:** Google APM Intern, Microsoft PM Intern, Atlassian APM Intern (AU/NZ cycle), Snowflake PM Intern, Databricks PM Intern.

**Secondary / low-visibility** (no public PM intern in most recent cycle; pursue via warm outreach, off-cycle openings, or adjacent roles): Stripe, Airbnb, Linear, Figma, Notion, Uber, DoorDash, Coinbase.

**Not summer-intern path:** Meta RPM — full-time rotational for new grads. Apply post-graduation.

In 2024-2026, public PM intern supply concentrated in 5-6 firms; secondary path requires warm outreach, off-cycle openings, or adjacent-role applications (data, ops, strategy, founder's office).

Eligibility note: Google's and Atlassian's new-grad APM programs differ from their penultimate-year APM Intern. The Intern is the summer-2027 target for a 2028 grad. Verify exact wording when 2027 postings drop. **Contingency:** if the 2027 APM Intern posting excludes Veer's class year, Microsoft PM Intern and Databricks PM Intern become the primary public targets (repeat intern pipelines, lighter class-year gating). A single-program ineligibility does not stall the cycle; the strategy is breadth across 5-6 programs, not single-logo.

**Adjacent-role route (primary realistic path, not a footnote):** Direct PM/APM internships are sub-1% at top programs. NACE: 63.1% intern-to-full-time conversion; ~28% of PMs in most-cited sample entered via internal move. Priority: (1) product/data-analyst intern at a product company (highest supply, best-evidenced feeder), (2) TPM/product-ops intern with SWE re-up as floor, (3) BizOps/chief-of-staff at growth-stage startup via referrals (highest breadth, thinnest supply). Apply Sep 2026-Feb 2027, after PM/APM windows (Aug-Oct 2026).

## The goal beneath the goal

Become a candidate whose profile makes the offer likely, not one who performs readiness.

- Market rewards "AI-enabled builders with real technical fluency and proof of shipping" — Stripe, Figma, Databricks, Microsoft APM 2026 listings confirm.
- "Smart sophomore with good GPA" is no longer differentiated.
- Return-intern conversion ~56% average, 70%+ at some companies — fewer external slots.
- Signal moved to **judgment, instrumentation, iteration, technical-product fluency**.
- Odds: **2-10%** per top program as a beginner with no shipped work; **8-20%** all-in across 5-6 elite programs at 90th-percentile profile.

Strategy: 90th-percentile candidate profile + broad application across 5-6 visible programs + warm-network plays at low-visibility ones. Single-logo optimization is the wrong frame.

---

## The four pillars

### Pillar 1: Ship something real

One anchor product with real users, real instrumentation, real iteration over 6-12 weeks. Must solve a problem Veer or a client understands, have at least one external user, a recorded metric or behavioral proxy, a dated decision log, and change after first user contact.

Bar: "I identified a real user problem, scoped a narrow solution, shipped it, measured usage or failure, and changed the product based on what I learned." Atlassian, Microsoft, Databricks, Snowflake expect customer interviews, OKRs, telemetry, iteration cycles. Vibe-coded AI wrappers and tutorial-clone CRUD apps signal tool access, not judgment.

**Veer's risk:** Starts projects, doesn't finish — ship v1 in 1-2 weeks, iterate weekly; rewriting-before-launch is the failure mode.

**Current anchor (re-pointed 2026-07-16; formalized at the 2026-07-19 Sunday session): STICK** (`~/Desktop/stick-dev`) — an AI study tool (LLM question generation, server-graded MCQ, confidence ratings, FSRS scheduling) targeting a professor-sponsored pilot in Purdue MA 16100, Fall 2026. It clears this pillar's bar better than the dashboard did: a real user problem Veer understands firsthand, narrow scope, a working walking skeleton, a measurable pilot path. Build state, decisions, and next actions are OWNED by stick-dev (read its `STATE.md` first); this file holds only the strategy-level read. Point, never mirror.

**Gates to a real pilot (order settled 2026-07-16):**
1. GenAI Studio email — its answer decides the model/API the build stands on (stick-dev OD-36); needs no demo.
2. The demo: `GEMINI_API_KEY` set, one hand-seeded MA 16100 topic, one generated question graded end-to-end.
3. Professor outreach early Aug, demo in hand.

**Success criteria (pillar level):**
- Demo runs end-to-end; at least ONE rejectable external artifact per week (a send, a deploy, a run, a person shown) — design/spec prose counts as zero regardless of volume (patterns.md P7; the session-start commit-ratio instrument enforces visibility)
- One student through a manually-seeded course by early fall; usage measured; iteration documented (stick-dev already over-documents — the binding constraint is external contact, not logging)
- Can explain in 90 seconds: user, problem, decision, trade-off, metric, what changed

**Banked:** India MSME digital-trade dashboard v1 — live on GitHub Pages with telemetry and a decision log through Entry 014. Remains the shipped-artifact interview story until STICK reaches users. Dr. G is a warm relationship in active-routing mode, not a project to serve.

**Killed (2026-07-16):** the US-version dashboard — 5 carries with zero artifact, no responsive user. Not to be revived.

---

### Pillar 2: Build technical credibility

Priority order:
1. Product-metrics and applied-statistics fluency (lead workstream)
2. API and data-model literacy
3. Python at honest working fluency
4. Light system-design reasoning
5. SQL working fluency (only if targeting data/ads/growth/infra teams)
6. Basic AI/LLM understanding (last)

**Curriculum (near-zero budget):**

| Resource | Purpose | Cost |
|---|---|---|
| Khan Academy Statistics & Probability | Significance tests, p-values, confidence intervals | Free |
| Amplitude Academy (funnel, retention, cohort) | Hands-on product-analytics | Free |
| Exponent | Structured question banks + peer mocks | ~$12/mo annual |
| IGotAnOffer / RocketBlocks / Product Management Exercises | Interview frameworks | Free |

DataCamp "A/B Testing in Python" — later endpoint, not entry point (assumes Python + prior hypothesis testing; beginners stall). Sequence ~6-8 weeks.

Meta, Microsoft, Airbnb probe: metric trees, North Star vs. guardrail metrics, numerator/denominator discipline, leading vs. lagging indicators, measurement windows, funnel/retention/cohort analysis, A/B test reading, metric-drop diagnosis. Google 2026 APM required CS/Engineering/Math/Stats or related; Microsoft walks line-by-line through every project on the resume. Resume-stack inflation is a top rejection signal.

**Veer's risk:** (1) Front-loading SQL — metrics/stats is the #1 gap. (2) Stack inflation. Make claims defensible; don't maximize the list.

**Success criteria:**
- Metrics/stats: metric tree from goal, North Star with window, guardrails, numerator/denominator, p-value + CI, metric-drop diagnosis (clarify, MECE segment, walk funnel, check logging)
- APIs: requests, responses, entities, events, logging, frontend vs backend truth
- Python: scripts, data handling, explain data structures
- System design: scope a flow, name requirements, interfaces, dependencies, failure modes
- AI: one tool, one workflow, one result, one limitation from own work
- SQL (data/ads/growth/infra only): joins, aggregations, window functions, explain slow query
- One mock where a technical follow-up doesn't crack the answer

---

### Pillar 3: Build the network

Substantive informational interviews — not referral mining (Patrick McKenzie's permission-based approach; Adam Grant's giver/taker frame).

Meta RPM takes no referrals. Ashby: 40% of referred applicants reach interview vs. much lower for cold. Only 9% of graduates report alumni network was helpful — requires active, specific, reciprocal outreach.

**Veer's risk:** Cold outreach activates initiation aversion. Flynn-Lake: requesters underestimated compliance by up to 50%; Bohns (14,000+ strangers) shows consistent pessimism. Fix: volume + specificity + low expectations.

**Playbook:**

- *Message format (LinkedIn data):* <400 characters = 22% higher response; >800 = below average. Format: shared context / why this person specifically / one small ask. Complete your LinkedIn profile first.
- *Follow-up:* Thank-you within 24-48 hours; after that only message with a real update. Generic check-ins are net negative.
- *Referral ask (Berkeley's protocol):* Ask only after they understand your fit. Frame: "If you think I'm a good fit and would feel comfortable, would you be open to a referral?" Provide the exact role link, tailored resume, two-sentence why-you, and a line making refusal easy.
- *Anti-patterns:* referral ask in first message; walls of text; generic praise; "any advice?" with no specificity; dominating conversation; ghosting; unfinished LinkedIn.

**Supply side:**

| Source | Notes |
|---|---|
| Amazon, Microsoft, Google, JPMorgan, Big 4, PepsiCo, Eli Lilly, Cummins | Heavy Purdue/IBE hires — warmest PM/adjacent surface |
| High Alpha (Indianapolis venture studio) + portfolio | IBE High Alpha capstone — warmest startup PM/analyst contacts |
| Product Management Club @ Purdue | Most on-target org; each speaker event = warm contact |
| The Data Mine | Year-long applied data-science projects with 60+ corporate partners; direct contacts |
| EPICS | In IBE curriculum; product-style delivery story |
| Burton D. Morgan Center | 0-to-1 product muscle |

*Finding Purdue alumni:* LinkedIn Alumni Tool (Purdue "People" tab, filter by Product Management); Boolean: `("Product Manager" OR "Associate Product Manager" OR APM) AND (Google OR Amazon OR Microsoft)`. Alumni reply rates ~20-40% vs ~5-15% generic.

**Success criteria:**
- 20+ substantive informational interviews by start of junior fall (~25% reply × ~65% reply-to-call requires ~124-150 messages, front-loaded before Aug-Nov 2026 crunch)
- Tracker: name, role, date, discussion, follow-up, what Veer did with advice
- At least 5 deep relationships where the person saw Veer take their advice and report back; 3 outreach messages/week as baseline

---

### Pillar 4: Interview readiness

Fluent, automatic structured product thinking under pressure. Frameworks (CIRCLES for design, GAME for execution/metrics, STAR for behavioral) as scaffolding, not crutch. Exponent: at least 10 sessions with 5 different people.

**Failure modes to drill:**
1. **Jumping to features before problem understanding** (most common fail). Always clarify first.
2. **Mechanical framework use.** Candidates who "live and die by frameworks" sound identical (Blind interviewers).
3. **Weak segmentation/prioritization.** Brainstorming without choosing reads as unfocused.
4. **Metrics theater.** "Engagement," no time periods, no primary vs. guardrail, no numerator/denominator.
5. **Company-context blindness.** Not tied to Meta's ecosystem / Google's product judgment / Microsoft's domain.
6. **Inflated technical credibility.** Microsoft walks line-by-line. Stripe's HackerRank screen exposes bluffing.

**Veer's risk:** Freezes under evaluation — self-monitoring hijacks working memory. Overlearn openings, scaffolds, and core stories; drill flexible retrieval.

**Success criteria:**
- 10+ mocks with at least 5 different partners by application window (30 = stretch ceiling, not target); shorter solo reps out loud, recorded; self-review on at least 5 sessions
- One pre-performance routine: one minute slow exhale, one cue phrase, one glance at three anchor stories
- 6-8 stories ready: conflict, failure, learning, ownership, persuasion, leadership without authority, technical collaboration; product sense answer not jumping to features in first 90 seconds

---

## Phase plan

| Phase | Dates | Key actions |
|---|---|---|
| 1 | Now – Aug 7, 2026 (~12 weeks) | Data scout; lock v1 scope by Friday; ship v1 within 2 weeks (~20-30 sub-sectors, moratorium exposure); Dr. G follow-up ~May 30; if Infisum materializes pivot dashboard, else iterate with 2-3 external viewers; Khan Academy + Amplitude Academy; 3 alumni messages/week from week 3; PM book pass (Decode and Conquer or Cracking the PM Interview, orientation); resume v1 mid-July |
| 2 | Aug 8 – Oct 31 | Apply Google APM; Microsoft, Databricks, Uber Freight likely posted; resume v2 around Infisum work; adjacent-role apps (rolling Sep 2026-Feb 2027): product/data-analyst first, TPM/product-ops, SWE as floor; 8-10 more alumni conversations; first solo mocks; APIs + system design |
| 3 | Nov – Feb | Atlassian AU/NZ APM Intern window; continue adjacent-role apps (product/data-analyst, TPM/product-ops, BizOps/chief-of-staff at growth-stage startups via referrals); mock interviews with partners; 2-3 mocks/week by February |
| 4 | Mar – Apr | Stripe accelerator apply; Snowflake PM Intern (April postings expected); convert any landed adjacent-role internship to inside track; final round prep |
| Summer 2027 | — | Internship if landed; else Plan B (more Infisum work, independent ship, niche internship) |

---

## Decision rules

- **Shipping vs. interview prep:** Shipping wins through August; interview prep ramps September.
- **Technical depth vs. network:** Both, weekly. Neither falls to zero for more than two weeks.
- **Polish vs. volume:** Volume wins in alumni outreach and mocks. Polish wins in project artifacts and resume.
- **Optimization vs. execution:** Execution wins. >90 minutes refining the planning system in a week = stop and ship.

## What the planner will refuse to do

- Add more pillars; build a daily plan with more than 3-4 substantive items
- Suggest tracking metrics that don't change behavior
- Optimize past the marginal-hour point; treat any rejection or setback as definitive evidence about Veer's odds
