# Match map — Jane Street, Strategy and Product Internship (NYC, May-August)

Posting verbatim: `listing.md`. Resume: `VeerSanyal_JaneStreet_Resume.tex` / `.pdf`.
Built 2026-08-21 per `context/applications/application-docs-workflow.md`.

## Role read

SP is Jane Street's merged Business Development + Tech PM internship: an analytical
generalist who sits between markets, product, and internal operations. The posting names
three learning domains in order (global market dynamics, technical systems and tooling,
operational infrastructure) and four behaviors (structured problem solving, communication,
driving projects, attention to detail). Veer is one of the few candidates who has a real
artifact in each of those three domains, so the resume is ordered to show all three in the
top two-thirds: SMIF (markets), Firmly (technical systems + payment infrastructure),
Externship (driving a project for a live client), then STICK and the MSME dashboard as the
build-and-framework proof.

Section order deviates from the default PM ordering in `profile/role-positioning.md`: SMIF
leads Experience instead of sitting in Leadership, because "global market dynamics" is the
first discipline the posting names and equity research under committee questioning is the
closest analogue on the page to how SP work gets pressure-tested.

## Requirement to proof

| # | Posting requirement (their words) | Proof used | Source file |
|---|---|---|---|
| 1 | "structured and careful approach to solving problems" | Firmly: defined requirements with eng + support, then validated the recovery flow across ~15 high-risk payment edge cases. Externship: discovery with the COO, then a 156-row dated calendar built from the client's own event grid. | `experience-firmly.md`, `experience-externship.md` |
| 2 | "build frameworks to tackle business questions" | MSME dashboard: a framework ranking which Indian small-business service sectors are most exposed to a given digital-trade policy. SMIF: 3-statement model with DCF, comps, and sensitivity analysis. | `project-msme-dashboard.md`, `experience-smif.md` |
| 3 | "use data to inform decisions" | Firmly: server-side error and recovery-rate logging built specifically to judge whether the fix worked. EPICS: the 18 versus 22 prism call settled on measured tolerance and manufacturability data. | `experience-firmly.md`, `leadership-epics.md` |
| 4 | "communicates effectively" (proven, never listed) | SMIF: 10-slide pitch to a 30+ member investment committee, assumptions defended live. Externship: audit findings converted into prioritized recommendations for a non-technical executive. | `experience-smif.md`, `experience-externship.md` |
| 5 | "can drive projects forward" | Externship: project manager of a 4-person team for Scouting America, owned the timeline and delivered the calendar. STICK: sole developer of a deployed web app. | `experience-externship.md`, `project-stick.md` |
| 6 | "exceptional attention to detail" | STICK: human review queue with 53 verified, 2 rejected, none left unreviewed. MSME: every figure computed from WTO and government source data rather than hardcoded, which surfaced a published statistic off by roughly 3x. | `project-stick.md`, `project-msme-dashboard.md` |
| 7 | "global market dynamics" | SMIF equity research: ~$400K AUM real-money portfolio, U.S. Bancorp coverage, Buy at $57.35 (~11.5% implied upside). | `experience-smif.md` |
| 8 | "technical systems and tooling" | STICK: LLM pipeline on Deno edge functions, React/TypeScript + Supabase. Firmly: Node.js/Express server-side logging. Skills "Technical" line. | `project-stick.md`, `experience-firmly.md` |
| 9 | "operational infrastructure" | Firmly: instrumented the payment path and built a 20+ test-case QA workflow adopted as the team standard for release verification. | `experience-firmly.md` |
| 10 | "eager to ask questions, admit mistakes, deepen understanding" | STICK: root-caused a generation-quality failure and raised yield from 1/5 and 0/8 to 8/8 (a bullet that names the failure before the fix). SMIF: refined the revenue and risk framing from what came back in committee questioning. | `project-stick.md`, `experience-smif.md` |
| 11 | "currently pursuing a Bachelor's degree" / "available full-time September 2028" | Purdue IBE, expected May 2028. Graduation date printed in the Education line. | `education.md`, `contact.md` |

## Alternatives considered and why they lost

- **Cairn (open-source agentic scaffolder).** The single most on-topic artifact for AI-agent
  roles, but SP is not an agent role, and the page could not hold a third project. STICK
  already carries the "builds technical systems" signal. Hold Cairn for the interview if the
  conversation turns to tooling.
- **StudyFlowForge.** Superseded by STICK; its "18 screens" framing adds nothing here.
- **Etsy design experience.** Off-family for SP.
- **SMIF in Leadership instead of Experience.** Rejected: markets are the first discipline
  the posting names, so the strongest markets proof belongs in Experience and in the top
  third.
- **Dropping EPICS to buy space.** Rejected; the standing default keeps one leadership
  bullet, and the prism-decision bullet doubles as a data-informed-decision proof. Space was
  bought by tightening bullets and section spacing instead (font stayed 10pt, margins 0.55in).

## Not claimable, named honestly

- **No finance-industry work experience.** SMIF is a student-managed fund, labeled as such.
  The posting explicitly does not require a finance background, so this is not a gap to fake.
- **No trading, market-making, or exchange-infrastructure exposure.** Nothing on the resume
  implies otherwise.
- **STICK has zero real students.** No user, retention, or engagement number appears; every
  STICK figure on the page is a pipeline or review-queue count verified by database query.
- **Externship deliverable is a received proposal, not an executed plan.** The bullets say
  built and delivered, never implemented or "drove engagement."
- **No SQL/TypeScript/React proficiency claim.** Those sit behind "(built with)" in the
  Skills block per the calibration rule in `skills-inventory.md`.
- **GPA (3.3) omitted** per the convention in `contact.md`.

## Independent review, 2026-08-21

Fresh-context reviewer read the research checklist, the full profile set, the posting, this
file, the `.tex`, and both `pdftotext` modes.

**Applied:**
- Restored the profile's actual SMIF language: the bullet now defends the assumptions AND
  refines the framing from what came back, which is what `experience-smif.md` says and what
  posting requirement #10 needs. As first drafted it showed only the defending half.
- Named the client (Scouting America) and changed "rebuilt" to "delivered" on the externship
  bullet. Honest per the inflation block: delivered is true, implemented is not.
- STICK subtitle now says "sole developer of a deployed web app," which `project-stick.md`
  explicitly permits and the first draft was leaving on the table.
- **Integrity fix, the important one.** `SQL/Postgres data modeling` and `Plotly` were sitting
  bare on the Data \& Analytics line, outside the `(built with)` qualifier, which contradicted
  this file's own "not claimable" entry and broke the calibration rule in `skills-inventory.md`.
  Both moved onto the Technical line behind `(built with)`.
- STICK's review-queue bullet said "between model and student." STICK has zero students.
  Reworded to "over the model's output rather than shipping it directly."
- MSME entry: date corrected to `2026 -- Present` (it is described as live) and the URL slot
  changed from Veer's GitHub profile, already in the header, to the actual repo path.
- Reading order: the reviewer caught raw `pdftotext` emitting location and dates BEFORE the
  employer name on the first entry of two sections, an ATS mis-pairing risk that
  `resume-check.sh` misses because it reads `-layout` mode. Re-verified after the edits: every
  entry title now leads its own block.

**Waived:**
- **Verb tense (A4).** Every bullet is past tense, including the two roles dated Present.
  Waived deliberately: each bullet describes a completed accomplishment inside an ongoing role,
  which is standard, and half-converting would read worse. Uniform past tense is the convention
  for this document.
- **Adding the Postgres/RLS bullet (B2).** `project-stick.md` holds stronger "technical systems
  and tooling" proof (46 migrations, 33+ row-level-security policies, automated RLS probe) than
  anything currently on the page, but the page is at its one-page limit and buying the space
  would cost the MSME framework bullet. Not added. **Use it in the interview:** it is the best
  answer available if Jane Street asks what he has actually built.

**Clean on review:** no em dashes, no en dashes outside date ranges, 1 page, all bullets 1-2
lines, quantification 10/11 bullets, all 11 posting requirements covered, every claim traceable
to a profile file, no private-repo language, no third-party names, GPA correctly omitted.
