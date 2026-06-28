> Compressed 2026-06-10. Canonical working copy (docs/ tier removed 2026-06-15).

# Infisum Dashboard Project Roadmap

Pillar 1 (Ship Something Real) of the PM internship execution system. Weekly Sunday sessions plan against this; mid-week decisions check against it.

## Project in one sentence

Interactive dashboard ranking ~20-30 India MSME-relevant service and trade sub-sectors by exposure to a named digital-trade policy (v1: WTO e-commerce moratorium at MC14), so a digital-trade policy-research analyst can quickly identify which 2-3 sectors to deep-dive, survey, or cite.

Deliberately sector-level, not firm-level: no public dataset joins an individual MSME's sector to its digitally-delivered-services trade. Data lives at sector altitude; product lives there too.

## Who it is for

User: digital-trade policy-research analyst, specifically Dr. Badri Narayanan Gopalakrishnan and his NCAER / ICRIER / GTAP-Purdue orbit. Decision: "When a specific digital-trade policy is in play, which 2-3 MSME-heavy sectors do I flag as most exposed, without rebuilding the data pull each time."

Every other candidate user (DGFT, FIEO, fintech) needs district or firm granularity that doesn't exist publicly. Building for them requires fabricating granularity.

## Why this project

1. **Pillar 1 PM-application evidence.** Shipped artifact with real user, real iteration, real decisions, real telemetry. Defensible in interviews. The honest scoping (sector-level, proxies labeled, no fabricated join) is itself an interview-ready design story.
2. **Substantive update for Dr. Gopalakrishnan.** Working prototype on his research turf, anchored to the moratorium. Transforms the May 30 follow-up from "checking in" to "here's what I built, here's the one assumption I want your read on."

If Infisum opportunity materializes, dashboard pivots into client work. Either way, this is v1, not final form.

---

## What the dashboard does

Centerpiece: single-screen ranked filterable table/heatmap scoring sub-sectors on moratorium exposure, with adjustable weights and linked sources showing each assumption.

| Page | What it shows | Data source |
|---|---|---|
| Sector Exposure Ranking | ~20-30 sub-sectors ranked by moratorium-exposure score, weights adjustable, every proxy labeled | All sources + EBOPS-to-NIC crosswalk |
| Digital Trade Layer | India digitally delivered services trade by EBOPS category over time (economy-level) | WTO Digitally Delivered Services, BaTIS, TiSMoS |
| MSME Platform Dependence | Platform/e-commerce dependence and sector weights (e.g. ICRIER finding: only ~12% of surveyed MSMEs run own e-store) | ICRIER aggregates + Udyam/NSS sector weights |
| Policy Lens | Moratorium and policy-sensitivity axis, with named-policy definition of "exposure" | OECD Digital STRI + moratorium-exposure logic |

### Exposure score is a screening heuristic, not a measured index

Transparent screening heuristic with explicitly labeled proxy components, computed at sector level. Not a firm-level index.

Composite multiplies three labeled, user-adjustable axes:

- **Digital-trade intensity** (proxy): WTO Digitally Delivered Services + BaTIS/TiSMoS EBOPS categories, crosswalked to NIC service divisions. Crosswalk shown to user, not hidden.
- **MSME platform/e-commerce dependence** (proxy): ICRIER survey aggregates + Udyam/NSS sector weights.
- **Policy sensitivity** (proxy): OECD Digital STRI pillars + moratorium-exposure logic, adjustable per scenario.

"Exposure" is undefined until a policy is named. V1 names one: WTO e-commerce moratorium (cheap digital imports and lost tariff space). Exposure to DPDP data-localization or platform-fee shifts is v2.

Phase B scenario toggle: analyst swaps the named policy (moratorium to DPDP data-localization to platform-fee changes) and sees ranking shift.

---

## What this project is NOT

- Not a firm-level index; not fabricating the MSME-sector-to-digital-trade join; not proving causal impact; not tracking individual firms; not a full econometric model; not policy advocacy.

It is:
- Sector-level screening and prioritization tool for a policy-research analyst
- Transparent, assumption-explicit heuristic with every proxy and weight visible
- Data storytelling product joining trade, MSME, and policy data worlds that usually sit apart
- Design that turns the data's biggest limitation (no firm-level join) into a deliberate, defensible choice

---

## Data sources (priority order)

No public dataset joins an MSME's sector to its digital-services trade. Trade data is economy-level; MSME data is registration-level. Dashboard bridges them only through a labeled crosswalk, never a measured link.

| Priority | Dataset | Granularity | Status |
|---|---|---|---|
| 1 | WTO Digitally Delivered Services | Economy x 8 EBOPS sub-sectors x year. Economy-level only. | Downloaded May 19, pivot built |
| 2 | OECD-WTO BaTIS | Economy x 26 EBOPS categories x year. Hosted as GTAP resource (mentor's orbit). | Pending |
| 3 | WTO TiSMoS | Economy x 55 sectors x 4 modes. Best sector resolution, still economy-level. | Pending |
| 4 | ICRIER 2025 MSME Digitalisation Survey | Fixed-sample survey (2,365 MSMEs). Published aggregates only, not openly re-sliceable, not NIC-joinable. | Pending, Week 2 |
| 5 | Udyam / MSME Dashboard (GoI) | Reliably open as district x enterprise-category. Clean NIC 2-digit x size cuts NOT reliably public. | Pending, Week 2, confirm NIC access first |
| 6 | OECD Digital STRI | Country x 5 policy pillars x year. Applied as sensitivity multiplier. | Pending, Week 4 |
| 7 | NSS 73rd Round (2015-16) | Sector-joinable open microdata, stale (2015-16), no digital-trade variables. Use for sector weights only. | Optional |
| 8 | MoSPI Supply and Use Tables | 155 products x 67 industries. No trade-mode or MSME-size dimension. | Optional, Week 7+ |

Priorities 1-3: digital-trade-intensity axis (economy-level, reach sector only through crosswalk). Priorities 4-5: MSME platform-dependence axis and sector weights. Priority 6: policy-sensitivity axis. Everything after: depth, not MVP.

### The crosswalk is the central credibility risk — surface it, do not bury it

The EBOPS-to-NIC mapping (e.g. "telecom-computer-information services exports" to "IT-services MSMEs") is a modeled analyst assumption, not a measured link. It is the first thing a sharp interviewer or Dr. G will probe. Dashboard must: show it visibly (crosswalk view, per-cell assumption notes), version it (NIC 2025 vs NIC 2008, EBOPS 2010 vintages), and never present it as ground truth.

Two access caveats to clear before building sector weights:

- **Udyam NIC-level open access is unconfirmed.** District x category is reliably public. Granular NIC-cut from data.gov.in returned a 403. Confirm whether NIC 2-digit x size x geography is openly servable before designing sector weights around it.
- **ICRIER is sample, not census, and not openly re-sliceable.** Sector coverage is uneven. Verify which sectors the survey actually disaggregates before promising them in the UI.

---

## Constraints and key dates

| Date | Constraint |
|---|---|
| ~May 30 | Dr. G follow-up window opens. First hard date. 11 days from May 19. |
| ~June 5 | v1 target ship: sector exposure ranking computes end-to-end, supporting pages deployed publicly. |
| ~August 7 | Summer ends. 12 weeks total; ~9 weeks of iteration after v1. |
| End of September | Resume-bullet shape and demo-ready for Google APM (expected to close early-to-mid October 2026). |

---

## Phase A: May 30 follow-up readiness (May 19-30, 11 days)

Point: earn the right to a substantive follow-up message, not finish the project.

Must be true by May 30:
- Deployed prototype at live public URL
- Two pages working: Digital Trade Layer + first cut of Sector Exposure Ranking (even if scored on one or two proxies)
- Public GitHub repo with README and DECISIONS.md
- Decision log with at least 4-5 entries, including one naming the EBOPS-to-NIC crosswalk as the open question
- Specific ask drafted for Dr. G: not "what do you think" but "here is my EBOPS-to-NIC mapping, where would you push back"

Does NOT need to be true by May 30: full three-axis exposure score, MSME Platform Dependence page, policy scenario toggles, polished UX, all data sources.

---

## Phase B: v1 ship and iteration (June 1 through August 7)

After v1 ~June 5, the bar shifts from "did I build it" to "what did I decide, what did I measure, what changed." Highest-value iteration: hardening the crosswalk and moratorium exposure logic against Dr. G's read, not adding pages.

Pattern: each week, one feature add or one user feedback cycle, documented in the decision log.

---

## Week-by-week roadmap

Directional, not rigid. Slippage pushes everything right, does not delete weeks.

| Week | Dates | Focus |
|---|---|---|
| 1 | May 18-24 | Foundation |
| 2 | May 25-31 | Phase A push |
| 3 | Jun 1-7 | Platform-dependence axis + exposure score v0 |
| 4-5 | Jun 8-21 | First real iteration cycle |
| 6 | Jun 22-28 | User feedback round 1 |
| 7-8 | Jun 29-Jul 12 | Iteration round 2 |
| 9-10 | Jul 13-26 | Polish and depth |
| 11-12 | Jul 27-Aug 7 | Final iteration and wrap |

### Week 1 (May 18-24) — Foundation

- Mon May 18: System setup (done)
- Tue May 19: Option B committed, WTO data downloaded, pivot + chart built, decision log started (done)
- Wed May 20: BaTIS and TiSMoS download, stack chosen, repo live, decision log moved to repo
- Thu May 21: EBOPS categories processed, digital-trade-intensity view built
- Fri May 22: Streamlit app skeleton deployed at public URL with Digital Trade Layer chart working. Quality bar: it loads and shows one chart.
- Sun May 24: First Sunday session, plan week 2

### Week 2 (May 25-31) — Phase A push

- Mon-Tue: First cut Sector Exposure Ranking from EBOPS-to-NIC crosswalk, digital-trade-intensity axis only
- Wed-Thu: ICRIER report read, platform-dependence stats to manual CSV. Udyam sector cuts captured (check whether NIC-level is openly servable; data.gov.in granular resource returned 403). Not in deployed app yet — content for week 3.
- Fri May 29: Go/no-go decision on Dr. G outreach. Honest read of prototype state.
- Sat May 30: Send follow-up. Include live dashboard link, decision log link, one specific ask (crosswalk read).

### Week 3 (Jun 1-7) — Platform-dependence axis and exposure score v0

- Build MSME Platform Dependence page from ICRIER aggregates and Udyam/NSS sector weights
- Finalize v0 sector crosswalk (manual CSV: ebops_category, nic_service_division, msme_proxy, policy_sensitivity_note, assumption), render visibly in app
- First version of three-axis exposure score scoped to WTO e-commerce moratorium; two axes instead of three is fine
- **v1 ship milestone:** Sector Exposure Ranking computes end-to-end from crosswalk, supporting pages deployed

### Week 4-5 (Jun 8-21) — First real iteration cycle

- Add OECD Digital STRI for policy-sensitivity axis, tied to moratorium-exposure logic
- Harden EBOPS-to-NIC crosswalk against actual data vs. week-3 assumptions; document each revision
- Add policy scenario toggle (moratorium baseline, DPDP data-localization stubbed for v2)
- Add basic telemetry (Amplitude)
- If Dr. G replied: highest-signal iteration cycle of the summer. Incorporate his feedback on crosswalk and moratorium framing, document in decision log.

### Week 6 (Jun 22-28) — User feedback round 1

- Send v1 to 2-3 people. Candidates: Dr. G if engaged, Purdue econ professor, a senior with PM-adjacent work.
- Document feedback in decision log; pick top 2-3 changes, not all.

### Week 7-8 (Jun 29-Jul 12) — Iteration round 2

- Implement feedback changes
- Add Supply and Use Tables data if useful (priority 7)
- Write short blog-post-style writeup of learnings (resume + conversation material)

### Week 9-10 (Jul 13-26) — Polish and depth

- One technical depth-add: state-level breakdown if NSS data is workable, or a more interesting exposure model
- UX cleanup pass; second round of external feedback; resume v1 drafted

### Week 11-12 (Jul 27-Aug 7) — Final iteration and wrap

- Final polish from second feedback round
- Decision log finalized with full narrative arc
- Project README written for recruiter audience: problem, user, decisions, trade-offs, what changed, what to do differently
- Practice 90-second pitch out loud, recorded

---

## Success criteria

- v1 live with at least one external viewer (Dr. Gopalakrishnan minimum) by June 5
- 8-12 weeks of documented iteration after v1
- At least one piece of real telemetry or usage data captured
- Public decision log maintained with weekly entries
- 90-second explanation: analyst user, moratorium-ranking problem, decision, trade-off, metric, what changed
- Answer "what did you cut from scope and why" without hesitation (lead with: no firm-level join, so tool stays at sector altitude)
- Answer "what surprised you in the data" with a specific example
- Defend the EBOPS-to-NIC crosswalk as a labeled assumption when probed; not claim a measured link
- Code public on GitHub, README readable by a recruiter

---

## Decision log discipline

Not optional. Converts the work into interview material by September.

Format per entry:
```
Date:
What I decided / did:
Why (the trade-off I made):
What's still unknown / next move:
```

Rules: one entry per work session (not per decision); write the honest "why," not the resume "why"; stored at `DECISIONS.md` in public GitHub repo; reviewed every Sunday session — not write-only.

---

## May 30 follow-up message protocol

Do not ask for an internship. Ask for input on a specific question, or for a brief conversation.

The Berkeley referral-ask protocol says ask only after the person understands your fit and feels comfortable. The Cornell follow-up framing says the strongest follow-up shows evidence of motion, not desire for attention. The dashboard link is the evidence of motion. The decision log is evidence of judgment.

Anti-pattern: long wall of text. Flynn-Lake research shows requesters underestimate compliance by up to 50% — the message does not need to over-justify.

Target length: under 400 characters where possible, 800 maximum. Format:
- One line of context (what was discussed last time)
- One line on what was built and why
- One specific question or ask
- Link to dashboard
- Link to decision log

---

## Roadmap adjustment signals

Adjust at Sunday sessions, not mid-week.

Adjust if: same week slipping twice in a row; v1 milestone slips past June 12; telemetry not added by end of week 5; decision log has fewer than 4 entries by end of any week; adding a second scenario policy before moratorium ranking works end-to-end.

Working if: Sunday sessions tighten the plan rather than rebuild it; decision log entries are about real trade-offs; each week ends with one shipped change visible to external viewers; pitch gets shorter and sharper over time.

---

## Stack and infrastructure

| Component | Choice |
|---|---|
| Frontend/app | Streamlit + Python (Streamlit Cloud deployment, handles pandas natively) |
| Data | Pandas in `/data` folder; raw CSVs version-controlled until size is an issue |
| Deploy | Streamlit Community Cloud (free, public) |
| Code | GitHub, public repo |
| Decision log | `DECISIONS.md` in repo root |
| Telemetry | Amplitude (preferred), added week 4-5. Plausible or GA as fallback. |
| Fallback stack | Plotly Dash, Next.js + Recharts |

Stack decisions logged in DECISIONS.md when made or changed.

### Pillar 1 feeds Pillar 2

Amplitude use here is deliberate: both the dashboard's telemetry tool and hands-on practice for the product-metrics fluency Pillar 2 prioritizes (funnels, retention, cohorts, north-star metric). Amplitude Academy free courses in the Pillar 2 curriculum map directly onto the events being wired up here.

---

## Explicitly out of scope until Phase B at earliest

Firm-level or district-level exposure claims; causal modeling of digital trade impact on MSME growth; state-level or firm-level granularity in v1; mobile-responsive design; user authentication; ML/NLP/"AI features" without a clear user problem; reading every ICRIER paper end-to-end; switching stacks before v1 ships; adding extra scenario pages before moratorium ranking works end-to-end.

These are the things that will feel important during weeks 3-5 and that the Sunday session should refuse to add.
