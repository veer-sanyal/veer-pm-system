# Knowledge freshness ledger

The `context/` research docs are cached domain knowledge. Undated cached knowledge is a bet
wearing a verified badge: recruiting timelines, program existence, and interview formats rot;
behavioral-science and strategy syntheses do not. This ledger tiers each doc so staleness is a
structural trigger, not a model's guess (it can't feel stale knowledge).

**Two tiers.** LIVING = decision-priority AND likely to change AND low certainty → carries a
verified-as-of date and an event trigger; the `/sunday` freshness sweep re-verifies it when the
trigger fires. STATIC = durable (refresh only on direct contradiction). A doc earns LIVING only
if a wrong, stale fact in it would change a real decision — most don't, and shouldn't.

**Cheap surveillance gates rare re-verification.** The sweep is a no-op unless a trigger fired;
most weeks nothing does. A fired trigger means: re-read the doc's time-sensitive claims against a
current source (careers page, program site, a quick web check), then either note "still true
(re-verified YYYY-MM-DD)" or update the doc + `key-dates.md`. Hard ceiling: any LIVING doc
untouched for a full recruiting cycle gets a re-verify pass regardless of triggers.

## LIVING (surveil on event)

| Doc | Verified as of | Refresh trigger |
|---|---|---|
| `Product_Management_Internship_Recruiting_for_Summer_2027.md` | 2026-06-15 | A recruiting cycle opening (Google APM ~mid-Sept 2026), any program deadline reached, or a program's existence/eligibility in doubt. Highest priority — deadline errors are costly (cf. Salesforce "deadline ~1hr — likely closed"). |
| `key-dates.md` | live (maintained; own file) | Not stale — this is the operational owner, updated at reconcile/Sunday. Listed here only to record that it DERIVES from the recruiting doc above; when that doc is re-verified, reconcile the two. |
| `PM_Internship_Interview_Reality_Check.md` | 2026-06-15 | Entering interview prep for a specific company, or a cycle opening. Round structures and take-home formats shift year to year. |
| `research-adjacent-roles-to-pm.md` | 2026-06-15 | Considering an APM-adjacent pivot (analyst/TPM/APM-variant). Role landscape + program lists drift. |
| `research-purdue-network-recruiting.md` | 2026-06-15 | Planning a networking push; specific people/roles drift (live contacts are owned by `alumni-tracker.md`, not this doc). |
| `research-linkedin-presence.md` | 2026-06-15 | A LinkedIn profile/posting push; platform norms shift slowly. Low priority. |

## STATIC (refresh only on contradiction)

Durable behavioral science, strategy, curriculum, and banked-artifact grounding — content that
does not expire on a calendar:

- `Sustained_Execution_on_Long-Horizon_Goals.md`, `The_College-as_Leverage_Thesis_Examined_Honestly.md`
- `Genuine_Networking_for_Competitive_PM_Internships.md` (tactics durable; live contacts live in `alumni-tracker.md`)
- `research-metrics-fluency-curriculum.md` (PM metrics fundamentals — curriculum, not news)
- `research-infisum-dashboard-user-problem.md`, `infisum-dashboard-roadmap.md` (banked artifact; frozen by design)
- `emotional-regulation/research-emotional-regulation-synthesis.md`, `scheduling-blueprint.md`
- `about-me.md`, `veer-full-profile.md`, `sleep-protocol.md` (operating manual; owned/updated on change, not surveilled)

If a STATIC doc is contradicted by reality, fix it in place — it does not wait for the sweep.
