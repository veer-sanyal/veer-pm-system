# Infisum Dashboard Project Roadmap

The build plan for the India MSME Digital Trade Exposure Dashboard. This is Pillar 1 (Ship Something Real) of the broader PM internship execution system.

The roadmap exists so weekly Sunday sessions have a target to plan against, and so mid-week decisions can be checked against the larger arc rather than re-derived every time.

---

## The project in one sentence

An interactive dashboard that ranks India's MSME-relevant service and trade sub-sectors by their exposure to a named digital-trade policy (v1: the WTO e-commerce moratorium at MC14), so a digital-trade policy-research analyst can quickly see which 2-3 sectors to deep-dive, survey, or cite.

This is a sector-level, policy-anchored screening tool. It is deliberately not a firm-level index, because (as the user-problem research found) no public dataset joins an individual MSME's sector to its digital-services trade. The data lives at sector altitude, so the product lives there too.

## Who it is for

The user is a digital-trade policy-research analyst, concretely the mentor, Dr. Badri Narayanan Gopalakrishnan, and his NCAER / ICRIER / GTAP-Purdue orbit. His recurring decision is narrow and real: "When a specific digital-trade policy is in play, which 2-3 MSME-heavy sectors do I flag as most exposed, so I know where to commission the next deep-dive or what to cite in a submission, without rebuilding the data pull each time."

This matters because it is the only user whose decision sits at the sector altitude the public data can honestly support. Every other candidate user (DGFT, FIEO, fintech) needs district or firm granularity that does not exist publicly. Building for them would force fabricating granularity. Building for the analyst does not.

## Why this project

Two roles, equally important:

1. **Pillar 1 evidence for PM applications.** A shipped artifact with a real, reachable user, real iteration, real decisions, real telemetry. Defensible in interviews. The thing that turns "well-prepared candidate with no proof" into "candidate with shipped work." The honest scoping (sector-level, proxies labeled, no fabricated join) is itself an interview-ready design story.

2. **Substantive update for Dr. Gopalakrishnan.** A working prototype on his research turf, anchored to a live policy fight he tracks (the moratorium), shows you read his work and built something rather than waited. Transforms the May 30 follow-up from "checking in" to "here's what I made, and here is the one assumption I most want your read on."

If Infisum opportunity materializes, dashboard pivots into client work. If not, dashboard stays yours and keeps iterating. Either way, this is the v1, not the final form.

---

## What the dashboard does

The centerpiece is a single screen: a ranked, filterable table or heatmap that scores roughly 20-30 MSME-relevant service and trade sub-sectors on their exposure to the WTO e-commerce moratorium. Each sector cell links to its underlying sources and shows the assumption behind its score. The user can change the weights and watch the ranking move.

The supporting pages exist to make that ranking legible and trustworthy:

| Page | What it shows | Data source |
|---|---|---|
| Sector Exposure Ranking | ~20-30 sub-sectors ranked by moratorium-exposure score, weights adjustable, every proxy labeled | All sources + the EBOPS to NIC crosswalk |
| Digital Trade Layer | India digitally delivered services trade by EBOPS category and over time (economy-level) | WTO Digitally Delivered Services, BaTIS, TiSMoS |
| MSME Platform Dependence | Platform / e-commerce dependence and sector weights (e.g. the ICRIER finding that only ~12% of surveyed MSMEs run their own e-store) | ICRIER aggregates + Udyam / NSS sector weights |
| Policy Lens | The moratorium and the policy-sensitivity axis, with the named-policy definition of "exposure" | OECD Digital STRI + moratorium-exposure logic |

### The exposure score is a screening heuristic, not a measured index

This is the most important framing point. The score is a transparent screening and storytelling heuristic, with explicitly labeled proxy components, computed at the sector level. It is not a measured firm-level index and does not pretend to be one.

The composite multiplies three labeled axes, weights visible and user-adjustable:

- **Digital-trade intensity** (proxy): how active is digital services trade in this category, from WTO Digitally Delivered Services + BaTIS / TiSMoS EBOPS categories, crosswalked to NIC service divisions. The crosswalk is shown to the user, not hidden.
- **MSME platform / e-commerce dependence** (proxy): from ICRIER survey aggregates plus Udyam / NSS sector weights.
- **Policy sensitivity** (proxy): from OECD Digital STRI pillars and moratorium-exposure logic, adjustable per scenario.

"Exposure" is undefined until the policy is named, so v1 names one: exposure to the WTO e-commerce moratorium (cheap digital imports and lost tariff space). Exposure to data-localization under DPDP, or to platform-fee shifts, is a different vector and is a v2 scenario, not v1.

Scenario toggle in Phase B: let the analyst swap the named policy (moratorium to DPDP data-localization to platform-fee changes) and see how the ranking moves.

---

## What this project is NOT

Important so I do not overclaim in conversations with Dr. G, in interviews, or in the README:

- Not a firm-level index. It does not claim firm-level or sub-sector-within-firm granularity. The public data does not support that, and claiming it would be fabricating granularity.
- Not fabricating a join the data cannot support. No public dataset links an Indian MSME's sector to its digitally-delivered-services trade. The dashboard does not pretend one exists. The EBOPS to NIC link is a labeled analyst crosswalk, not a measured join.
- Not proving causal impact of digital trade on MSME growth
- Not tracking every Indian MSME firm individually
- Not a full econometric model
- Not policy advocacy

It is:
- A sector-level screening and prioritization tool for a policy-research analyst
- A transparent, assumption-explicit heuristic, with every proxy and weight visible
- A data storytelling product that joins three data worlds (trade, MSME, policy) which usually sit apart
- A way to turn the data's biggest limitation (no firm-level join) into a deliberate, defensible design choice

---

## Data sources (priority order)

The central finding of the user-problem research drives this whole section: no public dataset joins an MSME's sector to its digital-services trade. The trade data is economy-level; the MSME data is registration-level. The dashboard bridges them only through a labeled crosswalk, never a measured link.

| Priority | Dataset | Granularity that actually exists | Status |
|---|---|---|---|
| 1 | WTO Digitally Delivered Services | Economy x 8 EBOPS sub-sectors x year. Economy-level only, no firm or industry split | Downloaded May 19, pivot built |
| 2 | OECD-WTO BaTIS | Economy x 26 EBOPS categories x year. Economy-level. Hosted as a GTAP resource (mentor's orbit) | Pending |
| 3 | WTO TiSMoS (Trade in Services by Mode of Supply) | Economy x 55 sectors x 4 modes. Best sector resolution in the trade family, still economy-level | Pending |
| 4 | ICRIER 2025 MSME Digitalisation Survey | Fixed-sample survey (2,365 MSMEs). Published aggregates only, not openly re-sliceable, not NIC-joinable | Pending, Week 2 |
| 5 | Udyam / MSME Dashboard (Government of India) | Reliably open as district x enterprise-category. Clean NIC 2-digit x size cuts are NOT reliably public | Pending, Week 2, confirm NIC access first |
| 6 | OECD Digital STRI | Country x 5 policy pillars x year. Policy-environment, country-level, applied as a sensitivity multiplier | Pending, Week 4 |
| 7 | NSS 73rd Round (2015-16) | Sector-joinable and open microdata, but stale (2015-16) with no digital-trade variables. Use for sector weights only | Optional |
| 8 | MoSPI Supply and Use Tables | 155 products x 67 industries. Best public bridge between service products and industries, no trade-mode or MSME-size dimension | Optional, Week 7+ |

Layers: priorities 1-3 give the digital-trade-intensity axis (economy-level, so they reach the sector only through the crosswalk). Priorities 4-5 give the MSME platform-dependence axis and the sector weights. Priority 6 gives the policy-sensitivity axis. Everything after that is depth, not MVP.

### The crosswalk is the central credibility risk, surface it, do not bury it

The EBOPS service-category to NIC service-division mapping (e.g. "telecom-computer-information services exports" to "IT-services MSMEs") is a modeled analyst assumption, not a measured link. It is the first thing a sharp interviewer or Dr. G will probe. The dashboard must show it to the user (a visible crosswalk view, per-cell assumption notes), version it (NIC 2025 vs NIC 2008, EBOPS 2010 vintages), and never present it as ground truth.

Two access caveats to clear before building sector weights:

- **Udyam NIC-level open access is unconfirmed.** District x category is reliably public. The granular NIC-cut requested via data.gov.in returned a 403 on fetch. Confirm whether NIC 2-digit x size x geography is openly servable (or requires a data request / dashboard scrape) before designing sector weights around it.
- **ICRIER is sample, not census, and not openly re-sliceable.** Platform-dependence inputs come from published aggregates, so sector coverage is uneven. Verify which sectors the survey actually disaggregates before promising them in the UI.

---

## Constraints that set the schedule

- **Dr. G follow-up window opens ~May 30.** This is the first hard date. Determines what must exist in 11 days from May 19.
- **v1 target ship date ~June 5.** The sector exposure ranking computes end-to-end and the supporting pages exist in some form, deployed publicly.
- **Summer ends ~August 7.** 12 weeks total. After v1 ships, that's ~9 weeks of iteration.
- **Google APM expected to close early-to-mid October 2026.** The project needs to be in resume-bullet shape and demo-ready by end of September. Iteration through August means September is polish, not building.

---

## Phase A: May 30 follow-up readiness (May 19-30, 11 days)

The point of Phase A is not to finish the project. It is to earn the right to a substantive follow-up message.

What needs to be true by May 30:

- Deployed prototype at a live public URL
- Two pages working: the Digital Trade Layer plus a first cut of the Sector Exposure Ranking, even if scored on one or two proxies
- Public GitHub repo with README and DECISIONS.md
- Decision log with at least 4-5 entries showing real thinking, including one that names the EBOPS to NIC crosswalk as the open question
- A specific question or ask drafted for Dr. G, not "what do you think" but "I'm crosswalking EBOPS categories to NIC sectors to rank exposure, here is my mapping, where would you push back"

What does NOT need to be true by May 30:

- Full three-axis exposure score
- MSME Platform Dependence page wired in
- Policy scenario toggles
- Polished UX
- All data sources integrated

The follow-up message says "I started building. Here is where I am. Here is one specific thing I am working through. Open to your input." It does not say "I finished a thing."

---

## Phase B: v1 ship and iteration (June 1 through August 7)

After v1 ships ~June 5, the work shifts from building to iterating. This is where the project actually becomes credible Pillar 1 evidence. The bar is no longer "did I build it," it is "what did I decide, what did I measure, what changed based on what I learned." For this project specifically, the highest-value iteration is hardening the crosswalk and the named-policy (moratorium) exposure logic against Dr. G's read, not adding pages.

The pattern: each week, one feature add or one user feedback cycle, documented in the decision log.

---

## Week-by-week roadmap

Directional, not rigid. Sunday sessions tighten each week. Slippage on one week pushes everything right, not deletes the week.

### Week 1 (May 18-24) — Foundation

- **Mon May 18:** System setup (done)
- **Tue May 19:** Option B committed, WTO Digitally Delivered Services downloaded, pivot + chart built, decision log started (done)
- **Wed May 20:** BaTIS and TiSMoS download, stack chosen, repo live, decision log moved to repo
- **Thu May 21:** EBOPS categories processed, digital-trade-intensity view built (service category breakdown)
- **Fri May 22:** Streamlit app skeleton deployed at public URL with the Digital Trade Layer chart working. Quality bar: it loads and shows one chart. That is enough.
- **Sun May 24:** First Sunday session, plan week 2 in detail

### Week 2 (May 25-31) — Phase A push

- **Mon-Tue:** First cut of the Sector Exposure Ranking from the EBOPS to NIC crosswalk, scored on the digital-trade-intensity axis alone for now
- **Wed-Thu:** ICRIER report read, platform-dependence stats extracted to manual CSV. Udyam sector cuts captured (and check whether NIC-level is openly servable; the data.gov.in granular resource returned 403). These do not need to be in the deployed app yet, they become content for week 3.
- **Fri May 29:** Decision day on Dr. G outreach. Read the prototype state honestly. Does it earn the send?
- **Sat May 30:** Send the follow-up. Draft together in Sunday/Friday session. Include link to live dashboard, link to decision log, one specific ask (the crosswalk read).

### Week 3 (Jun 1-7) — Platform-dependence axis and exposure score v0

- Build the MSME Platform Dependence page from collected ICRIER aggregates and Udyam / NSS sector weights
- Finalize the v0 sector crosswalk (manual CSV: ebops_category, nic_service_division, msme_proxy, policy_sensitivity_note, assumption) and render it visibly in the app
- First version of the three-axis exposure score scoped to the WTO e-commerce moratorium as the named policy, even if rough; two axes instead of three is fine
- **v1 ship milestone:** the Sector Exposure Ranking computes end-to-end from the crosswalk, supporting pages exist in some form, deployed at a public URL

### Week 4-5 (Jun 8-21) — First real iteration cycle

This is the part that matters for the PM story. The MVP exists; now the work is iterating on contact with reality.

- Add OECD Digital STRI for the policy-sensitivity axis, tied to moratorium-exposure logic
- Harden the EBOPS to NIC crosswalk against what the data actually shows vs what was assumed in week 3; this is the central credibility move, document each revision
- Add the policy scenario toggle (moratorium baseline, with DPDP data-localization stubbed for v2). The most interesting feature for Dr. G.
- Add basic telemetry. Need to be able to answer "what do users actually do here" later.
- If Dr. G replied: this is the highest-signal iteration cycle of the summer. Incorporate his feedback on the crosswalk and moratorium framing explicitly, document in decision log.

### Week 6 (Jun 22-28) — User feedback round 1

- Send v1 to 2-3 people for actual feedback. Candidates: Dr. G if engaged, an econ professor at Purdue, a senior who has done PM-adjacent work
- Document feedback in decision log
- Pick top 2-3 changes worth making — not all of them

### Week 7-8 (Jun 29-Jul 12) — Iteration round 2

- Implement feedback changes
- Add Supply and Use Tables data if useful (priority 7)
- Write short blog-post-style writeup of what learned. Resume material + conversation material.

### Week 9-10 (Jul 13-26) — Polish and depth

- One technical depth-add: state-level breakdown if NSS data is workable, or a more interesting exposure model
- UX cleanup pass
- Second round of external feedback
- Resume v1 drafted around this work

### Week 11-12 (Jul 27-Aug 7) — Final iteration and wrap

- Final polish based on second feedback round
- Decision log finalized with full narrative arc
- Project README written for a recruiter audience: problem, user, decisions, trade-offs, what changed, what would do differently
- Practice the 90-second pitch out loud, recorded

---

## Success criteria for the project

Pulled from Pillar 1 in direction.md, made specific to this build:

- v1 live with at least one external viewer (Dr. Gopalakrishnan minimum) by June 5
- 8-12 weeks of documented iteration after v1
- At least one piece of real telemetry or usage data captured
- Public decision log maintained with weekly entries
- Can explain in 90 seconds: the analyst user, the moratorium-ranking problem, decision, trade-off, metric, what changed
- Can answer "what did you cut from scope and why" without hesitation (lead with: no firm-level join, so the tool stays at sector altitude)
- Can answer "what surprised you in the data" with a specific example
- Can defend the EBOPS to NIC crosswalk as a labeled assumption when probed, not get caught claiming a measured link
- Code public on GitHub, README readable by a recruiter

---

## Decision log discipline

The decision log is not optional. It is the artifact that converts the work into interview material in September.

Format per entry — keep simple, do not over-structure:

```
Date:
What I decided / did:
Why (the trade-off I made):
What's still unknown / next move:
```

Rules:

- One entry per work session, not per decision
- Write the honest "why," not the resume "why"
- Stored at `DECISIONS.md` in the public GitHub repo
- Reviewed in each Sunday session — do not let it become write-only

---

## What earns the May 30 follow-up message

Read this before the May 29 go/no-go decision:

The Berkeley referral-ask protocol says ask only after the person understands your fit and feels comfortable. Applied to this case: do not ask for an internship in the May 30 message. The ask is for input on a specific question, or for a brief conversation.

The Cornell follow-up framing says the strongest follow-up shows evidence of motion, not desire for attention. The dashboard link is the evidence of motion. The decision log is evidence of judgment.

Anti-pattern to avoid: long wall of text describing everything built. The Flynn-Lake research shows requesters underestimate compliance by up to 50% — the message does not need to over-justify. Short, specific, one ask.

Target message length: under 400 characters where possible. Under 800 maximum. Format:

- One line of context (what was discussed last time)
- One line on what was built and why
- One specific question or ask
- Link to the dashboard
- Link to the decision log

---

## When to push back on the roadmap

Signs the roadmap needs to be adjusted at a Sunday session, not mid-week:

- Same week pattern slipping twice in a row (e.g. data download tasks consistently pushed)
- v1 milestone slipping past June 12 — this means Phase A succeeded but Phase B is not starting
- Telemetry not added by end of week 5
- Decision log has fewer than 4 entries by end of any given week
- Trying to add a second scenario policy before the moratorium ranking works end-to-end

Signs the roadmap is working:

- Sunday sessions are tightening the plan, not rebuilding it
- Decision log entries are about real trade-offs, not status updates
- Each week ends with one shipped change visible to external viewers
- The pitch gets shorter and sharper over time, not longer

---

## Stack and infrastructure (working assumptions)

- **Frontend / app:** Streamlit + Python (fast to build, deployable to Streamlit Cloud, handles pandas natively)
- **Data:** Pandas in a `/data` folder; raw CSVs version-controlled until size becomes an issue
- **Deploy:** Streamlit Community Cloud (free, public)
- **Code:** GitHub, public repo
- **Decision log:** `DECISIONS.md` in repo root
- **Telemetry:** Amplitude (preferred), added week 4-5. Plausible or simple GA as a lighter fallback.
- **Alternative if Streamlit hits a wall:** Plotly Dash, Next.js + Recharts

Stack decisions get logged in DECISIONS.md when made or changed.

### Pillar 1 feeds Pillar 2

Using Amplitude here is deliberate. It is the dashboard's telemetry tool and also the natural vehicle for building the product-metrics fluency that Pillar 2 prioritizes (funnels, retention, cohorts, a north-star metric). Instrumenting the exposure ranking for real, then reading the resulting funnel and cohort views, is hands-on metrics practice on a product I actually own, not a toy exercise. The Amplitude Academy free courses in the Pillar 2 curriculum map directly onto the events I will be wiring up here.

---

## What this roadmap deliberately leaves out

Things that are tempting but explicitly out of scope until Phase B at earliest:

- Any firm-level or district-level exposure claim. The public data cannot join an MSME's sector to its digital trade, so v1 must not imply it can.
- Causal modeling of digital trade impact on MSME growth
- State-level or firm-level MSME granularity in v1
- Mobile-responsive design
- User authentication
- ML models, NLP, or "AI features" without a clear user problem they solve
- Reading every ICRIER paper end-to-end (extract what is needed, move on)
- Switching stacks before v1 ships
- Adding extra scenario pages before the moratorium ranking works end-to-end

These are the things that will feel important during weeks 3-5 and that the Sunday session should refuse to add.
