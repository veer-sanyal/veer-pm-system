# Direction

This file is the strategic core. The daily planner and weekly sessions reference this to make sure daily activity actually rolls up to the goal. When in doubt about whether to do something, check whether it serves one of the four pillars below.

---

## The goal

Land a Product Management internship for summer 2027 at a FAANG-tier or equivalent company.

**Primary public targets (clear, currently visible PM internship pipelines):**
- Google APM Intern
- Microsoft PM Intern
- Atlassian APM Intern (AU/NZ cycle)
- Snowflake PM Intern
- Databricks PM Intern

**Secondary / low-visibility (no publicly visible PM internship in most recent cycle, but off-cycle networking can still produce opportunities):**
- Stripe, Airbnb, Linear, Figma, Notion, Uber, DoorDash, Coinbase

**Not summer-intern path but adjacent:**
- Meta RPM — full-time rotational role for new grads, not a summer internship. Apply post-graduation.

The supply compression matters: in 2024-2026, the publicly visible PM internship supply concentrated in 5-6 firms. For the 8 secondary companies, the realistic path is warm outreach, off-cycle openings, or adjacent-role applications (data, ops, strategy, founder's office) rather than a clean public funnel.

One eligibility note: Google's and Atlassian's full-time new-grad APM programs are not the same thing as their penultimate-year APM Intern. The Intern is the valid summer-2027 target for a 2028 grad; the full-time APM is a post-graduation role. Confirm the exact wording when the 2027 postings drop.

**The adjacent-role route (a primary realistic path, not a footnote):** Direct PM/APM internships are real but brutally scarce (sub-1% at top programs), so the highest-probability on-ramp is to land any elite-tech internship and transfer internally. NACE reports 63.1% intern-to-full-time conversion, and roughly 28% of PMs in the most-cited sample entered PM via an internal move, which makes "get inside, then move" the dominant strategy. For this hybrid (business + engineering) candidate the priority order is: (1) product/data-analyst intern at a product company (highest supply, best-evidenced feeder, best hybrid fit), (2) TPM/product-operations intern, with re-upping the SWE internship as the floor (highest-probability offer-in-hand), and (3) BizOps/chief-of-staff at a growth-stage startup as a networked stretch (highest breadth, thinnest supply, pursue via referrals). These apply Sep 2026-Feb 2027 on rolling timelines, after the narrow PM/APM windows (Aug-Oct 2026).

## The goal beneath the goal

Become a candidate whose profile makes the offer likely, not perform readiness. The research is explicit:

- The market is rewarding "AI-enabled builders with real technical fluency and proof of shipping" — Stripe, Figma, Databricks, Microsoft APM 2026 listings all confirm this
- "Smart sophomore with good GPA" is no longer differentiated
- Return-intern conversion at top programs is high (around 56% on average, 70%+ at some companies), meaning fewer slots for external candidates
- AI tools have collapsed the floor for "I can ship a demo," so the signal has moved to **judgment, instrumentation, iteration, and technical-product fluency** — what the candidate decided, why, what they measured, what broke, what changed
- Realistic odds for a sophomore starting from zero now, executing well: **2-10%** per top program if behaving like a beginner with no shipped work; **8-20%** all-in across 5-6 elite programs at the 90th-percentile candidate profile

This means: the work is to become a 90th-percentile candidate, then apply broadly across the 5-6 visible programs while running parallel warm-network plays at the low-visibility ones. Optimizing for a single logo is the wrong frame.

## The four pillars

Everything in the daily plan rolls up to one of these. If an activity doesn't serve one of these, it doesn't go in the plan.

### Pillar 1: Ship something real

**What this means:** One anchor product with real users, real instrumentation, real iteration — built and iterated over 6-12 weeks, not shipped once and shelved. A thing that solves a problem Veer personally understands or that an actual client needs, has at least one user beyond himself, has a recorded metric or behavioral proxy (telemetry, usage data, behavioral signal), has a dated decision log, and changes meaningfully after first contact with users.

**Why this matters most:** This is the single highest-leverage thing in the whole plan. The 2027 research is explicit: "one meaningful project over 6-12 weeks is much more credible than a pile of tiny artifacts." Atlassian, Microsoft, Databricks, Snowflake all expect customer interviews, OKRs, telemetry, and iteration cycles — things that require multiple cycles, not one launch. Without this, the rest of the work caps out at "well-prepared candidate with no proof." With it, every interview, every alumni conversation, every resume bullet becomes credible.

**The bar is no longer "I built something."** The bar is: "I identified a real user problem, scoped a narrow solution, shipped it, measured usage or failure, and changed the product based on what I learned." Vibe-coded AI wrappers and tutorial-clone CRUD apps now signal access to tools, not product judgment.

**Veer's specific risk on this pillar:** He starts projects and doesn't finish them. The structure here is to ship v1 in 1-2 weeks (small enough to actually finish), then iterate weekly for the rest of summer. Version 1 only needs to validate one user problem and one workflow. The rewriting-before-launch trap is the failure mode.

**Current plan: sector-level digital-trade exposure dashboard.**

The user is a digital-trade policy-research analyst, concretely the mentor, Dr. Gopalakrishnan (GTAP/Purdue, NCAER, editor of a forthcoming volume on WTO and SMEs). His recurring decision: "When a specific digital-trade policy is in play, which of India's MSME-relevant service and trade sub-sectors should I flag as most exposed, so I know which to commission a deep-dive on or cite in a submission, without rebuilding the data pull each time."

v1 is a ranked, filterable screen that scores roughly 20-30 service sub-sectors by their exposure to one named policy: the WTO e-commerce moratorium in play at MC14. This is the right scope because it is the only altitude the public data actually supports. India is actively contesting the moratorium right now, so "which MSME sectors are exposed" is a live question, and the mentor is a real, reachable user the prototype can be validated against.

The "exposure index" is not a measured firm-level quantity. It is a transparent screening heuristic with every proxy labeled: (i) digital-trade intensity (proxied from WTO Digitally Delivered Services + BaTIS/TiSMoS EBOPS categories), (ii) MSME platform/e-commerce dependence (from ICRIER survey aggregates and Udyam/NSS sector weights), (iii) policy sensitivity (from OECD Digital STRI pillars plus moratorium-exposure logic). The user can change the weights and watch the ranking move, and every score links to its source and the assumption behind it.

The central credibility limitation, surfaced not buried: there is no public dataset that joins an Indian MSME's sector to its digitally-delivered-services trade. The EBOPS service category to NIC service division mapping is an analyst's crosswalk, a modeled assumption, not a measured link. The honest framing (scoped to what the data can support, proxies made legible) is the design choice, and it is the first thing a sharp interviewer will probe.

The prototype serves two purposes:

1. Pillar 1 evidence — a shipped artifact with real economic data, then iterated over 8-12 weeks of summer
2. Substantive update for Dr. Gopalakrishnan follow-up around May 30 — shows he read Infisum's work, can talk to it, and built something rather than waited

Build arc:
- Data scouting Wed/Thu this week (confirm WTO/BaTIS/TiSMoS pulls, ICRIER aggregates, Udyam district x category access; note the data.gov.in Udyam 403 to confirm)
- Lock the v1 scope (moratorium sector-ranking) by Friday
- v1 shipped by ~June 5 (week 3)
- Weeks 4-12: iterate. Add features driven by user feedback (Dr. G's, then any users he routes you to, then any external viewer). Add telemetry. Document decisions. Iterate based on what the data actually surfaces vs. what you expected. v2 adds scenario toggles (data-localization under DPDP, platform-fee shifts).

If the Infisum opportunity materializes into real client work, the dashboard pivots into that — it's the v1, not the final form. If it doesn't materialize, the dashboard is still yours and still iterating.

**Success criteria:**
- v1 live with one external viewer (at minimum, Dr. Gopalakrishnan) within 2 weeks, ranking ~20-30 MSME-relevant sub-sectors by moratorium exposure
- The screening heuristic is transparent: weights adjustable, every proxy labeled, every score linked to its source
- The EBOPS-to-NIC crosswalk is surfaced in the UI as a stated limitation, not hidden
- 8-12 weeks of documented iteration after v1
- At least one piece of real telemetry or usage data captured
- Public decision log maintained
- Can explain in 90 seconds: user, problem, decision, trade-off, metric, what changed
- Can answer: "What did you cut from scope and why?" — strong signal in current interviews (here: no firm-level or district-level claims, because the data can't honestly support them)

**What "telemetry" actually means at this scale:**
Not Mixpanel infrastructure. At sophomore-project scale, telemetry means: page views, time on page, which views people use, which filters get clicked, drop-off points. Even a simple Google Analytics or Plausible setup counts. The point is you can answer "what do users actually do with this" with data, not vibes.

### Pillar 2: Build technical credibility

**What this means:** Enough technical fluency to be credible in interviews and on the job, not enough to pretend to be an engineer. In priority order:

1. Product-metrics and applied-statistics fluency (the lead technical workstream)
2. API and data-model literacy
3. One programming language at honest working fluency (Python is the obvious pick given his major)
4. Light system-design reasoning
5. SQL working fluency, only if targeting data/ads/growth/infra teams
6. Basic AI/LLM understanding beyond chatbot use, last

**The concrete curriculum (beginner entry, near-zero budget):**
- Khan Academy Statistics & Probability (free) for the conceptual stats base: significance tests, p-values, confidence intervals
- Amplitude Academy free courses (funnel, retention, cohort) for the hands-on product-analytics base. Amplitude doubles as the dashboard's telemetry tool, which ties Pillar 1 and Pillar 2 together.
- Exponent (~$12/mo on the annual plan) as the one justified paid add, for structured question banks and peer mocks.
- DataCamp "A/B Testing in Python" is a later endpoint, not an entry point: it is an advanced course that assumes Python and prior hypothesis testing. A beginner who starts there will stall.

Free IGotAnOffer / RocketBlocks / Product Management Exercises content covers most of the interview frameworks. The whole sequence is roughly 6-8 weeks.

**Why this matters:** The analytical/execution interview at Meta, Microsoft, Airbnb consistently probes a small, learnable set: metric trees, North Star vs guardrail metrics, numerator/denominator discipline, leading vs lagging indicators, measurement windows, funnel/retention/cohort analysis, reading A/B tests, and diagnosing a metric drop. That is the highest-leverage technical gap, and it is also what Pillar 1 needs to instrument a real product. The research is also explicit that resume-stack inflation is a top rejection signal: listing five languages when you've used each once. Google's 2026 APM intern listing required CS/Engineering/Math/Stats or related; Microsoft interviewers walk line-by-line through every technical project on the resume.

**Veer's specific risk on this pillar:** Two things. First, mistaking SQL for the priority and front-loading it, when metrics and statistics fluency is the actual #1 gap and SQL is a smaller, conditional lift. Second, stack inflation: listing things he's barely touched. The IBE major gives him a credible base; the work is making the technical claims defensible under questioning, not maximizing the list.

**Success criteria:**
- Metrics/stats: can build a metric tree from a goal, define a North Star with a window, name guardrails, be explicit about numerator/denominator, read a p-value and confidence interval, and structure a metric-drop diagnosis (clarify, segment, MECE internal vs external, walk the funnel, check for logging breakage)
- APIs: can explain requests, responses, entities, events, logging, frontend vs backend truth
- Python: can write small scripts, handle data, talk through data structures used
- System design: can scope a flow, name requirements, name interfaces, name dependencies, name failure modes
- AI: can name one tool, one workflow, one result, one limitation observed in own work
- SQL (only if targeting data/ads/growth/infra teams): can write joins, aggregations, window functions, and explain why a query is slow
- One mock interview where a technical follow-up doesn't crack his answer

### Pillar 3: Build the network

**What this means:** Substantive informational interviews with alumni and PM professionals — not referral mining. Patrick McKenzie's "permission-based" approach: ask permission, educate yourself, become useful, then ask. Adam Grant's giver/taker frame: optimize for being interested, not for being interesting.

**Why this matters:** Referrals are not decisive at offer stage for structured APM programs (Meta RPM explicitly takes no referrals), but they meaningfully increase odds of being seen at the recruiter screen — Ashby data shows 40% of referred applicants reach interview vs much lower for cold applicants. More importantly: the conversations themselves are how Veer learns what the bar actually looks like, what these companies actually care about, and where his profile is weak. The network is also the second-order benefit — people who saw him try, fail, iterate, and come back with updates become advocates over time.

**Counterweight from college-leverage research:** Only 9% of graduates report their alumni network was helpful in the job market. The network is not a passive asset that activates when needed. It only works through active, specific, reciprocal relationship-building. That is also why pillar 3 cannot be skipped — passive credentialing doesn't substitute for active outreach.

**Veer's specific risk on this pillar:** Cold outreach activates his initiation aversion harder than almost anything else. The Flynn-Lake research found requesters underestimated compliance by as much as 50%, and Bohns' review across 14,000+ strangers shows consistent pessimism about influence. The fix is volume + specificity + low expectations per message, not crafting the perfect message.

**Networking playbook (research-backed specifics):**

*Message format (LinkedIn data):* Messages under 400 characters get 22% higher response rates than average. Messages over 800 characters perform below average. Format: one line of shared context, one line showing why you chose them specifically, one small ask. Profile completeness matters before sending — make sure your LinkedIn looks like a real serious sophomore (photo, school, headline, projects, "why product" hint).

*Follow-up cadence (event-based, not interval-based):* Thank-you within 24-48 hours. After that, only message again with a real update — "I took your advice and here's what happened." Generic check-ins ("still interested!") are net negative. Cornell's institutional framing: the strongest follow-up shows evidence of motion, not desire for attention.

*Referral ask timing (Berkeley's protocol):* Ask only after the person understands your fit and feels comfortable. Frame as: "If you think I'm a good fit and would feel comfortable doing so, would you be open to considering a referral?" Reduce work for them with a four-item package: exact role link, tailored resume, two-sentence why-you summary, line making refusal easy.

*Anti-patterns that get you instantly ignored:* asking for a referral in the first message; long walls of text; generic copy-paste praise; "any advice?" with no specificity; dominating the conversation; ghosting after getting what you wanted; an unfinished-looking LinkedIn profile.

**The supply side (who to reach, where to find them):**

*Warm-list employers (Purdue / IBE volume):* the companies that already hire Purdue and IBE heavily are the warmest surface for PM and PM-adjacent outreach: Amazon, Microsoft, Google, JPMorgan Chase, the Big 4 (Deloitte, PwC, EY, KPMG), PepsiCo, Eli Lilly, Cummins. IBE has a direct, named tech tie through its High Alpha capstone sponsorship (an Indianapolis venture studio), so High Alpha and its portfolio are the warmest startup PM/analyst contacts.

*Verified on-campus orgs (signal + contacts):* Product Management Club @ Purdue (the single most on-target org; each speaker event is a warm contact), The Data Mine (year-long applied data-science projects with 60+ corporate partners, builds analytics + stakeholder skills plus direct corporate contacts), EPICS (already baked into the IBE curriculum, gives a product-style delivery story), and the Burton D. Morgan Center for entrepreneurship (0-to-1 product muscle).

*How to find Purdue alumni (the precision method):* the LinkedIn Alumni Tool at the Purdue school page (the "People" tab) with the three filter bars (where they live / where they work / what they do, set to Product Management); the People-search School filter when the Alumni Tool is too coarse; and Boolean operators (AND/OR/NOT uppercase, quotes for phrases, parentheses to group), e.g. `("Product Manager" OR "Associate Product Manager" OR APM) AND (Google OR Amazon OR Microsoft)`. Lead with the Purdue angle: alumni cold-outreach reply rates run ~20-40% vs ~5-15% generic.

**Success criteria:**
- 20+ substantive informational interviews logged by start of junior fall semester (math-backed: at a ~25% reply rate and ~65% reply-to-call conversion, this requires ~124-150 well-targeted alumni messages over the year, front-loaded before the Aug-Nov 2026 crunch)
- Tracker maintained with name, role, date, what was discussed, follow-up sent, what Veer did with the advice
- At least 5 of these are deep relationships where the person has seen Veer take their advice and report back
- Cold outreach reflex installed — sending 3 messages a week feels like baseline, not effort

### Pillar 4: Interview readiness

**What this means:** Fluent, automatic structured product thinking under time pressure. Frameworks (CIRCLES for design, GAME for execution/metrics, STAR for behavioral) used as scaffolding, not as crutch. Spoken delivery practiced enough that pressure doesn't break the structure.

**Why this matters:** The research is consistent — the gap between "knows the framework" and "can run the framework under interruption" is where most candidates fail. Frameworks themselves are taught well by Exponent, Lenny, IGotAnOffer; the differentiator is reps. Specifically, Exponent's recommendation is at least 10 practice sessions with 5 different people, not dozens.

**The specific failure modes to drill against (from interview research):**
1. **Jumping to features before establishing problem understanding.** The most common fail. Cue to drill: always start with clarifying questions, even when the answer feels obvious.
2. **Using framework mechanically.** Interviewers on Blind explicitly say candidates who "live and die by frameworks" sound identical and surface-level.
3. **Weak segmentation and prioritization.** Brainstorming three segments, five pains, ten features without choosing reads as unfocused.
4. **Metrics theater.** Defaulting to "engagement," not specifying time periods, not distinguishing primary from guardrail metrics, not explaining numerator/denominator.
5. **Company-context blindness.** Generic answers that don't tie back to Meta's ecosystem / Google's product judgment / Microsoft's domain.
6. **Inflated technical credibility.** Microsoft explicitly walks line-by-line through every framework, API, and language on the resume. Stripe's HackerRank-style screen exposes bluffing.

**Veer's specific risk on this pillar:** He freezes in case-style questions. This is exactly the failure mode the choking-under-pressure research describes — strong candidates whose working memory gets hijacked by self-monitoring under evaluation. The fix is overlearning the openings, scaffolds, and core stories so they survive pressure, plus practicing flexible retrieval across variant prompts.

**Success criteria:**
- 10+ mock interviews with at least 5 different partners by application window (this is the research-supported baseline; more is better but the bar is 10, not 30, with 30 as an explicit stretch ceiling, not the target)
- Many more shorter solo reps — out loud, recorded, reviewed
- Recorded self-review on at least 5 sessions
- One pre-performance routine drilled and reliable: one minute slow exhale, one cue phrase, one glance at three anchor stories
- Strong stories ready: conflict, failure, learning, ownership, persuasion, leadership without authority, technical collaboration (6-8 of these in fluent shape)
- Can deliver a product sense answer that doesn't jump to features in the first 90 seconds

## Phase plan across the 12 months

### Phase 1 (now through Aug 7, 2026 — sophomore summer, ~12 weeks)
- Data scout dashboard project this week, lock v1 scope by Friday
- Ship v1 of the dashboard within 2 weeks: a moratorium sector-exposure ranking of ~20-30 MSME-relevant sub-sectors
- Follow up with Dr. Gopalakrishnan around May 30 with prototype as substantive update
- If Infisum opportunity materializes: dashboard pivots into real client work
- If not: iterate prototype, get 2-3 external viewers, document decision log
- Begin metrics + statistics fluency in parallel: Khan Academy Statistics & Probability + Amplitude Academy (Pillar 2)
- Begin alumni outreach — 3 messages per week starting week 3 (Pillar 3)
- First PM book pass (one of Decode and Conquer, Cracking the PM Interview) — orientation only
- Resume v1 drafted by mid-July

### Phase 2 (Aug 8 - October 31 — fall semester starts, recruiting opens)
- Google APM opens (apply when posted)
- Microsoft postings begin appearing regionally
- Databricks, Uber Freight likely posted
- Resume v2 written around shipped Infisum work
- Begin adjacent-role applications (rolling, Sep 2026-Feb 2027): product/data-analyst intern at product companies first, then TPM/product-ops, plus re-up SWE as the floor
- 8-10 more alumni conversations
- First solo mock interviews (out loud, recorded)
- Continue technical work — APIs, system design fundamentals

### Phase 3 (November - February)
- Atlassian AU/NZ APM Intern window
- Continue adjacent-role applications (rolling): product/data-analyst, TPM/product-ops, and BizOps/chief-of-staff at growth-stage startups via referrals
- Mock interviews with partners begin
- Continue alumni outreach
- 2-3 mocks per week by February

### Phase 4 (March - April)
- Stripe accelerator apply
- Snowflake PM Intern (April postings expected)
- Convert any landed adjacent-role internship into the inside track, then position for an internal PM move
- Final round prep for any in-process interviews

### Summer 2027
- Internship starts (if landed); otherwise intensive plan B (more Infisum work, independent ship, niche internship)

## Decision rules when conflicts arise

- **Shipping work vs. interview prep:** Shipping wins through August. Interview prep ramps up September.
- **Technical depth vs. network:** Both, weekly. Neither can fall to zero for more than two weeks.
- **Polish vs. volume:** Volume wins in alumni outreach and mock interviews. Polish wins in project artifacts and resume.
- **Optimization vs. execution:** Execution wins. If Veer has spent more than 90 minutes refining the planning system in a given week, that's the signal to stop and ship something.

## What the planner will refuse to do

- Add more pillars
- Build a daily plan with more than 3-4 substantive items
- Suggest tracking metrics that don't change behavior
- Optimize past the point where the marginal hour helps execution
- Treat any single rejection or setback as definitive evidence about Veer's odds
