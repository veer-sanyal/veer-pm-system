# Strategic Docs ↔ Research Realignment — Design Spec (v2)

- **Date:** 2026-06-04
- **Status:** Approved (design, incl. research-driven additions); pending spec review → implementation plan
- **Scope:** The PM-internship strategic planning docs in this project's `docs/` folder
- **Out of scope:** The original research files in `files/` (untouched). NOTE: `scheduling-blueprint.md` now takes ONE small edit (outreach cadence) — see below.

---

## Problem

A read-through of the five original research docs against the strategic planning docs found that the two "strategic core" docs (`direction.md`, `scheduling-blueprint.md`) are largely faithful to the research, but specific divergences cluster downstream — chiefly in `about-me.md` and in how the **technical pillar** and **recruiting strategy** were operationalized. Five confirmed divergences:

1. **Mock-interview target.** `about-me.md` sets the bar at "30 mocks"; research baseline is ~10 with 5 people, and `direction.md` itself says "the bar is 10, not 30."
2. **SQL over-weighting.** Plan makes SQL the flagship technical skill; research demotes SQL and ranks product-metrics + statistics fluency #1, API/data-model literacy #2.
3. **Technical sequencing inversion.** Plan front-loads SQL into summer; research prescribes metrics fluency *before* technical credibility.
4. **Adjacent roles absent operationally.** Research calls adjacent roles the *realistic* path (direct FAANG-PM odds 2–10%), but they appear only as a footnote with no milestones.
5. **Target list re-inflated.** `about-me.md` lists ~15 companies incl. phantom programs ("Figma APM," "Uber APM") and miscasts Meta RPM as a summer-2027 internship.

Four supplementary deep-research reports were then commissioned (saved in `docs/`) to harden parts of the system that rested on assumptions. These both confirm the decisions below and add substance, plus surface a sixth issue: the dashboard's premise was not data-defensible.

---

## Decisions (resolved with user)

| # | Decision | Choice | Basis |
|---|---|---|---|
| 1 | Technical pillar weighting | **Metrics-first.** Metrics + statistics fluency = lead summer technical workstream; API/data-model literacy second; one language; system-design-lite; SQL only if targeting data/ads/growth/infra teams. | Original interview research's technical-curriculum priority order |
| 2 | Adjacent roles | **Parallel track** with its own fall/winter milestones, framed as a primary realistic route. | Original recruiting + college-leverage research; reinforced by adjacent-roles + Purdue reports |
| 3 | Target-company list | **Prune to research tiers.** `about-me.md` matches `direction.md`; remove invented programs; Meta RPM flagged post-grad. | Original recruiting research |
| 4 | Mock-interview target | **Tiered: 10 bar / 30 stretch.** | Original interview research |
| 5 | Pillar 1 (dashboard) | **Reframe to sector-level policy exposure.** Drop the firm-level four-component index (not data-defensible). v1 = rank India's MSME-relevant service sub-sectors by exposure to the WTO e-commerce moratorium (MC14). User = digital-trade policy-research analyst (concretely the mentor, Dr. G). The "index" = transparent screening heuristic with labeled proxies; EBOPS→NIC crosswalk surfaced as a known limitation. | `research-infisum-dashboard-user-problem.md` |
| 6 | Pillar 3 outreach cadence | **3 alumni messages/week year-round** (up from 2). | `research-purdue-network-recruiting.md` outreach math (≈124–150 messages → 20+ interviews) |

Sequencing fix (divergence #3) falls out of Decision 1.

---

## Research-driven content to fold in (beyond the mechanical fixes)

- **Pillar 1 reframe (Decision 5):** sector-level, policy-anchored; honest reframing of "index"; data-join limitation made explicit. Substantial rewrite of `infisum-dashboard-roadmap.md`.
- **Pillar 2 concrete curriculum:** beginner entry = Khan Academy Statistics & Probability + Amplitude Academy free funnel/retention/cohort courses (Amplitude doubles as the dashboard's telemetry tool — ties Pillar 1↔2). Exponent (~$12/mo) the one justified paid add. DataCamp "A/B Testing in Python" = later endpoint, not entry. ~6–8 week sequence.
- **Pillar 3 supply side:** sourced warm-list employers (Amazon, Microsoft, Google, JPMorgan, Big 4, PepsiCo, Eli Lilly, Cummins; IBE→High Alpha tie); verified clubs (Product Management Club @ Purdue, The Data Mine, EPICS, Burton D. Morgan); LinkedIn Alumni Tool / School-filter / Boolean method; Stanford 5-part template; 0/+7/+14 cadence; outreach math.
- **Adjacent-track specifics:** priority order for this hybrid candidate — (1) product/data-analyst intern at a product company (highest supply + best-evidenced feeder + best hybrid fit), (2) TPM/product-ops + re-up SWE as floor, (3) BizOps/chief-of-staff at a startup as a networked stretch. NACE 63.1% intern→FT conversion is the core rationale ("land any elite-tech intern, transfer internally"). Apply Sep 2026–Feb 2027 (rolling), after the narrow PM windows (Aug–Oct 2026).
- **APM-eligibility clarification:** distinguish Google/Atlassian's full-time new-grad APM from the penultimate-year **APM Intern**; the Intern is the valid S2027 target for a 2028 grad. Add a "confirm wording at posting time" note.

---

## Per-file change plan

### `direction.md` (all fair to edit)
- **Pillar 1** — reframe per Decision 5: user, the policy/moratorium v1 problem, "index"→screening heuristic, crosswalk limitation. Update success criteria to the sector-level, policy-anchored version.
- **Pillar 2** — reorder to metrics-first; name the concrete curriculum (Khan + Amplitude Academy; Exponent paid add; DataCamp endpoint); SQL conditional. Reorder success criteria (metrics first, SQL last/conditional).
- **Pillar 3** — add the sourced supply side (warm-list, clubs, LinkedIn method); set cadence to 3/week; keep 20+ interview target now that it's math-backed.
- **Pillar 4** — keep "bar is 10," add 30 as explicit stretch ceiling.
- **"The goal"** — add adjacent roles as a primary realistic route with the specific priority order + NACE-conversion rationale; add the Google/Atlassian APM-Intern vs full-time-APM clarification.
- **Phase 1 (summer)** — SQL → metrics curriculum (Khan + Amplitude); reframed dashboard v1 (moratorium sector-ranking).
- **Phases 2–4** — add adjacent-role application items (Sep 2026–Feb 2027, rolling) alongside the PM/APM postings.

### `about-me.md` (primary reconciliation)
- **"The goal this project serves"** — replace the flat ~15-company list with `direction.md`'s tiers (primary public PM pipelines; low-visibility/warm-outreach; Meta RPM = post-grad 2028; no "Figma APM"/"Uber APM"). Add the adjacent-roles route with its priority order.
- **"What success looks like"** — "30 mocks" → "10 (bar) / 30 (stretch)"; technical-credibility criterion reordered to metrics-first; reflect the dashboard reframe (sector-level policy-exposure tool with a real user).
- **"Starting profile" SQL-gap note** — reframe: SQL is a smaller lift; priority technical gap is metrics fluency.

### `scheduling-blueprint.md` (one edit only)
- **Weekly volume targets** — alumni outreach "2 messages sent" → "3 messages sent" per Decision 6. Everything else untouched. (Add a one-line note that 3/week is the volume the 20+ interview target requires.)

### `key-dates.md`
- **Summer milestones** — "SQL working knowledge" → metrics + statistics fluency (Khan + Amplitude); reframed dashboard v1 (moratorium sector-ranking).
- **Internal milestones (fall/winter)** — promote adjacent-roles into dated application targets (product/data-analyst, TPM/product-ops, BizOps/CoS), Sep 2026–Feb 2027; note PM windows are Aug–Oct 2026.
- **APM rows** — clarify APM Intern (penultimate-year) vs full-time APM; keep the re-verify rule.
- **Sources line** — correct the filename reference; add the four new `research-*.md` docs.

### `daily-email-instructions.md`
- **Example 3** — replace the SQL-practice block with a metrics/analytics-practice example (Khan/Amplitude or a north-star/guardrail drill). Update the SQL-referencing citation.

### `infisum-dashboard-roadmap.md` (substantial reframe per Decision 5)
- Rewrite the one-sentence project description, the user, and the "what it does" to the sector-level, policy-anchored framing (v1 = WTO e-commerce moratorium sector exposure ranking).
- Reframe the exposure score as a transparent screening heuristic with labeled proxies (not a firm-level index).
- Update "What this is NOT" (not a firm-level index; not fabricated granularity).
- Update data sources to reflect the join limitation: economy-level trade data (WTO/BaTIS/TiSMoS) + district×category Udyam + ICRIER aggregates; flag the **EBOPS→NIC crosswalk as the central credibility risk to surface, not bury**; note the data.gov.in Udyam 403 to confirm.
- Add the Pillar 1↔2 tie: Amplitude telemetry as the metrics-fluency vehicle.

### New research docs (now first-class sources)
- `research-adjacent-roles-to-pm.md`, `research-purdue-network-recruiting.md`, `research-infisum-dashboard-user-problem.md`, `research-metrics-fluency-curriculum.md` — referenced from the docs they inform. No edits; they are sources.

---

## Acceptance criteria

- No strategic doc sets the mock bar at 30 as *the* bar (10 bar / 30 stretch everywhere).
- No strategic doc leads the technical pillar with SQL; metrics + statistics fluency leads (with the named curriculum), SQL conditional.
- Adjacent roles appear as a dated workstream with a specific priority order in both `direction.md` and `key-dates.md`.
- `about-me.md`'s target list matches `direction.md` tiers; Meta RPM post-grad; no "Figma APM"/"Uber APM."
- `infisum-dashboard-roadmap.md` (and Pillar 1 in `direction.md`) reflect the sector-level, policy-anchored reframe with the data-join limitation surfaced.
- `scheduling-blueprint.md` outreach cadence = 3/week; Pillar 3 in `direction.md`/`key-dates.md` carry the sourced supply side.
- The four `research-*.md` docs are cited as sources in the docs they inform.
- Original `files/` research docs unchanged.

## Open questions
- Confirm Google/Atlassian **APM Intern** (penultimate-year) eligibility wording when the 2027 postings drop — handled by the existing key-dates re-verify rule; not a blocker.
