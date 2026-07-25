> Compressed 2026-06-10. Canonical working copy (docs/ tier removed 2026-06-15).

# Direction

If an activity doesn't serve a pillar, it doesn't go in the plan.

---

## The goal

> **Restated 2026-07-25 (Veer, in session).** Until this date the goal line read "land a PM internship for summer 2027" and the whole system optimized for it. That was never the terminal goal and the effort data said so: the most productive build fortnight on record sitting next to 22 days of zero interview prep is a motivation gradient tracking a goal mismatch, not a discipline problem.

**Terminal: build a company.** Near-term that means STICK in front of real users, and by summer 2027 working on his own thing.

**Instrumental, and pursued for real: a PM internship for summer 2027** at a FAANG-tier or equivalent company. Not a consolation path and not abandoned. It buys a credential that lowers the cost of founding later, a look inside how a real product org prioritizes at scale, a network, income, and optionality if the company does not work.

**The decision rule (Veer's, and it is correct):** do not choose between a hypothetical offer and hypothetical traction. Run both through the school year, get both real, and decide when both are actually on the table. **Named cost: this is more work, not less. The failure mode is not choosing wrong, it is running both at 50%** and arriving at spring with a weak application and a product nobody uses. Every plan built from this file must admit that tension rather than pretend the tracks are free.

**What this changes, concretely:** nothing is dropped. Product-sense and metrics fluency are dual-use and stay (Pillar 2). Interview-format drilling is purely instrumental and re-times to Sept–Dec against the real loops instead of running year-round (Pillar 4). Pillar 1 stops being "an anchor project that makes a good interview story" and becomes the actual point, which is what it already was in practice.

**What does NOT change:** the mechanism. Progress is still counted only in rejectable artifacts. A founder's rejectable artifacts are users, customers, investors, cofounders (patterns.md P7). The reframe changes what fills the mechanism, never the mechanism itself. "Founder" is also a goal nobody can reject you from, which is exactly why the artifact rule has to bind harder here, not looser.

### The internship target (unchanged research, instrumental now)

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

### Pillar 1: Ship something real — THE MAIN EVENT (elevated 2026-07-25)

Under the founder-primary restatement this pillar stops being "an anchor project that makes a good interview story" and becomes the actual work. That is what it already was in practice; the file was the last thing still pretending otherwise. The interview story is now a **by-product** of this pillar, not its purpose. Practical consequence: when Pillar 1 and any other pillar compete for the same hour, Pillar 1 wins unless someone external is waiting on the other one.

One anchor product with real users, real instrumentation, real iteration over 6-12 weeks. Must solve a problem Veer or a client understands, have at least one external user, a recorded metric or behavioral proxy, a dated decision log, and change after first user contact.

Bar: "I identified a real user problem, scoped a narrow solution, shipped it, measured usage or failure, and changed the product based on what I learned." Atlassian, Microsoft, Databricks, Snowflake expect customer interviews, OKRs, telemetry, iteration cycles. Vibe-coded AI wrappers and tutorial-clone CRUD apps signal tool access, not judgment.

**Veer's risk:** Starts projects, doesn't finish — ship v1 in 1-2 weeks, iterate weekly; rewriting-before-launch is the failure mode.

**Current anchor (re-pointed 2026-07-16; formalized at the 2026-07-19 Sunday session): STICK** (`~/Desktop/stick-dev`) — an AI study tool (LLM question generation, server-graded MCQ, confidence ratings, FSRS scheduling) targeting a professor-sponsored pilot in Purdue MA 16100, Fall 2026. It clears this pillar's bar better than the dashboard did: a real user problem Veer understands firsthand, narrow scope, a working walking skeleton, a measurable pilot path. Build state, decisions, and next actions are OWNED by stick-dev (read its `STATE.md` first); this file holds only the strategy-level read. Point, never mirror.

**Gates to a real pilot (re-cut 2026-07-25 — the first two are now CLOSED):**
1. ~~GenAI Studio email~~ **CLOSED 2026-07-25**, sent to `rcac-help@purdue.edu` after 9 days' latency. Re-pointed on the way out from model-selection to institutional-inference-at-scale, since Gemini went live in the interim. Now an open external loop under **S-01** (economic-model feasibility); chase Q4 (free vs. charged) if the reply buries it.
2. ~~The demo runs end-to-end~~ **CLOSED** — key set, extraction verified, `gemini-3.6-flash` solve pass at 7/7 (D190).
3. **THE LIVE GATE: humans in front of it.** Not a deployment, not Slice 3. A person who is not Veer using it while he watches. Zero to date. Everything downstream (professor, pilot, any YC application, the interview story) is blocked on this one and nothing else.
4. Professor outreach for the MA 16100 Fall 2026 pilot — early Aug, now, with the demo in hand.

**Why the order changed:** gates 1 and 2 were both engineering-shaped, so they closed. Gate 3 is the one that can say no, which is why it has survived three weeks of being scheduled. See patterns.md P7 and its 2026-07-25 entry, where 15 `app/` commits landed in two days beside zero people shown.

**Open question, raised by Veer 2026-07-25: WHO PAYS?** STICK is designed free-to-student, which he correctly flags as a fundability question worth taking seriously rather than waving off. Framing settled in session: *free to the end user* is not the problem (institution-paid edtech is a standard model — Canvas, Top Hat, Packback, and Boilerexams as the local comparable). The real gap is an **unpicked payer**. Candidates: a department or the university, a professor's course budget, students directly on a freemium tier, or nobody.

**This is answered by the pilot, not by analysis, and the answering is already in motion.** (a) The GenAI Studio email sent 2026-07-25 IS this question — Q4 (free to the Purdue community vs. charged) decides whether near-zero marginal cost makes free-to-student viable; this is S-01. (b) The professor conversation tells us whether an institutional payer exists. (c) Students in front of it tell us whether anyone wants it at all. All three are on the W4 calendar. **No separate fundability research track gets block time** — it would be the unrejectable version of this question (P7).

**Standing caution against idea-shopping-by-market:** "pick a more fundable space" cuts against cairn/Conscience too (goals and productivity are not a hot category either), which is a sign the filter is not load-bearing. Veer's only real edge is being a Purdue student who understands the MA 16100 problem firsthand and can walk into the building — that is distribution, it is rare, and it does not transfer to whatever is hot this quarter. Early-stage investors fund people over markets (YC: 40% of funded companies are just an idea). Odd-but-used beats trendy-but-unused.

**Success criteria (pillar level):**
- Demo runs end-to-end; at least ONE rejectable external artifact per week (a send, a deploy, a run, a person shown) — design/spec prose counts as zero regardless of volume (patterns.md P7; the session-start commit-ratio instrument enforces visibility)
- One student through a manually-seeded course by early fall; usage measured; iteration documented (stick-dev already over-documents — the binding constraint is external contact, not logging)
- Can explain in 90 seconds: user, problem, decision, trade-off, metric, what changed

**Banked:** India MSME digital-trade dashboard v1 — live on GitHub Pages with telemetry and a decision log through Entry 014. Remains the shipped-artifact interview story until STICK reaches users. Dr. G is a warm relationship in active-routing mode, not a project to serve.

**Killed (2026-07-16):** the US-version dashboard — 5 carries with zero artifact, no responsive user. Not to be revived.

---

### Pillar 2: Build technical credibility — RE-POINTED 2026-07-25

**The content stays; the target changes.** Metrics and applied-statistics fluency is dual-use and non-negotiable either way: a founder who cannot read a funnel or tell a real signal from noise fails for the same reason a PM candidate does. Veer's weakest topic (significance/CIs, mastery 0.15, crux *inconclusive ≠ proven-no-effect*) is precisely the skill that stops a founder fooling himself about whether the product works.

**But it stops being abstract homework and points at STICK's live open decisions.** As of 2026-07-25 that means: **OD-06** (cold-start seeds + mastery EMA α), **CH-03** (the challenge to the 0.85 FSRS retention target), and whether the ENG-10 solve-pass move from 1/7 to 7/7 is a real effect or a small-n artifact. Same curriculum, real stakes, and it produces something that can be wrong.

**Why this is the fix and not a re-schedule.** This pillar went 22 days at zero (2026-07-03 to 07-25) across two consecutive planned weeks while Pillar 1 had its most productive fortnight on record. It was the only pillar whose output nobody could reject: a `state.json` row cannot push back, an EMA constant that degrades the product can. Re-scheduling identical blocks failed twice; changing the target is the actual intervention.

Interview-format drilling is NOT here. It moved to Pillar 4 and re-times to Sept–Dec.

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

### Pillar 3: Build the network — TWO TRACKS AS OF 2026-07-25

**Track A, PM/alumni (the existing playbook below, unchanged).** Still runs; it feeds the instrumental goal.

**Track B, builders and the startup ecosystem (new).** Under founder-primary this is no longer a nice-to-have. Its rejectable artifacts are cofounder conversations, users, and design partners, and it converts faster than alumni outreach because the ask is "will you use this" rather than "will you advise me."

- **Live: Neal (surfaced 2026-07-25).** Already an unprompted user of cairn — used it without being asked, gave real product feedback (the README-jargon complaint), said the onboarding interview was the good part, then forked it into his own `neal-pm-system` repo and expanded it. Also building in the same space (`Conscience`, a goals product) and showed genuine product judgment on his own landing page ("would you buy the product if this was the landing page? I wouldn't"). **He is the only organic pull anywhere in the portfolio**, n=1 and a friend, so not product-market fit, but it is the exact signal STICK has been trying to manufacture for two months. Open question is cofounding; the rejectable action is the actual conversation.
- Existing institutional surface already listed below: High Alpha, Burton D. Morgan Center, Purdue Foundry/Anvil orbit, The Data Mine.

**Standing caution:** cofounder and ecosystem conversations are cheap to enjoy and easy to substitute for building. They count when someone can say no or start using something. Coffee about startups is not a Pillar 3 artifact.

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

### Pillar 4: Interview readiness — DORMANT BY DESIGN UNTIL ~SEPT 2026 (re-timed 2026-07-25)

**Deliberately off, not dropped.** This is the purely instrumental pillar: case frameworks, mock loops, estimation, STAR drilling. It has a shelf life measured in weeks and is only useful pointed at a real loop. Google APM opens ~mid-Sept and closes early-to-mid Oct, so loops land roughly Oct–Dec. Drilling it in July was always the wrong month, and the honest resolution of "I don't want to drop anything" is that nothing is dropped, one thing is scheduled later.

**Turn-on trigger:** the Google APM posting going live (or the first confirmed loop for any target), which is the same event that fires the `Product_Management_Internship_Recruiting_for_Summer_2027.md` freshness re-verify in `knowledge-freshness.md`. When it fires, this pillar takes back the secondary block and ramps to the mock volume in the success criteria below.

**The one exception that keeps running:** free reps that already exist and cost nothing to attend. Cosentino Summer Case Classes (Purdue, free) ran Jul 13 and 15; Session 1/4 is Mon Jul 27, 8:00–9:30pm PT. Attend them. They are not a drilling program and do not count as pillar volume.

**Do not let this pillar's dormancy leak into Pillar 2.** Product sense and metrics are dual-use and stay live all summer; only the interview-shaped drilling waits.

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

- **Founder vs. internship, when they actually conflict:** they mostly do not, and both paths converge on the same next action for the rest of 2026 (STICK in front of real users). When a genuine conflict arrives, it does not get resolved by preference — it gets resolved by which option is real. Do not trade a live offer for a hypothetical company, or a company with users for a hypothetical offer. Revisit only when both are concrete.
- **Both at 50% is the failure mode, not choosing wrong.** If a review week shows both tracks half-done, cut the internship track's volume (fewer, better applications) before cutting Pillar 1. Pillar 1 is the one with compounding returns and no deadline to rescue it.
- **YC and accelerators:** an application counts as a Pillar-1 rejectable artifact. *Researching* accelerators does not and gets no block time. YC runs ~4 batches a year, so a missed deadline costs one quarter, never the opportunity — which means a rushed weak application is always the wrong trade against a real one a quarter later. Verify any deadline against the live page before planning around it (never assume).
- **Shipping vs. interview prep:** Shipping wins through August; interview prep ramps September.
- **Technical depth vs. network:** Both, weekly. Neither falls to zero for more than two weeks.
- **Polish vs. volume:** Volume wins in alumni outreach and mocks. Polish wins in project artifacts and resume.
- **Optimization vs. execution:** Execution wins. >90 minutes refining the planning system in a week = stop and ship.

## What the planner will refuse to do

- Add more pillars; build a daily plan with more than 3-4 substantive items
- Suggest tracking metrics that don't change behavior
- Optimize past the marginal-hour point; treat any rejection or setback as definitive evidence about Veer's odds
