# IBM — Product Manager Intern 2027 (req 128509) — Match Map

Built 2026-08-21. Audited against `listing.md` (verbatim posting) and `context/applications/profile/*`.
Role family: **technical / AI product management.** Positioning per `profile/role-positioning.md`
"AI / ML / Data" plus PM: STICK leads, because IBM's own framing is "AI enabled and data-driven
software products."

## Requirement to proof

| # | JD requirement (verbatim or close) | Proof used | Source |
|---|---|---|---|
| R1 | "Understanding of product management principles and user-centered thinking" | STICK bullet 1: defined the product strategy, choosing bounded AI steps over an open chatbot so output stays reviewable (a stated product decision with a stated reason). MSME bullet 1: scoped end-to-end against one named researcher's recurring decision and iterated through a public decision log. That pairing is the user-centered half. | `project-stick.md`, `project-msme-dashboard.md` |
| R2 | "Familiarity with AI/ML concepts or data workflows through coursework or projects" | STICK bullet 1: multi-step LLM pipeline (extract, classify, grade) on Deno edge functions turning raw exam PDFs into structured, verified question data. | `project-stick.md` |
| R3 | "Support product strategy, roadmap planning, and prioritization" | STICK: defined the bounded-AI product strategy and scoped a single-course pilot as the first real-user test. Externship: PM of a 4-person team, owned scope and delivery timeline. | `project-stick.md`, `experience-externship.md` |
| R4 | "Translate technical concepts, such as APIs, ML models, and data flows, into clear user stories" | Firmly bullet 1: defined requirements for the PayPal recovery flow and partnered with senior engineers to ship it. EPICS: translated product requirements into build specifications. | `experience-firmly.md`, `leadership-epics.md` |
| R5 | "Use analytics and user feedback to assess product performance" | MSME dashboard bullet 2: instrumented the live site with usage telemetry and five named custom events to measure real usage. Firmly bullet 2: built and tracked error rate and recovery rate via server-side logging. | `project-msme-dashboard.md`, `experience-firmly.md` |
| R6 | "Apply responsible and ethical AI practices" (also preferred: "familiarity with responsible AI or ethics framework") | STICK bullet 2: human-in-the-loop review queue over model output, 53 verified / 2 rejected / 0 unreviewed across 30 live topics. STICK bullet 3: yield fix plus automated release gates after tracking 24+ escaped defects, which is the quality-measurement half. **This is the single best-matched requirement on the posting and it sits in the top third.** | `project-stick.md` (refreshed 2026-08-21) |
| R7 | "Ability to analyze data and communicate insights clearly" | Externship bullet 2: audited the client's Facebook and website presence, quantified a roughly 25x gap between best- and worst-performing content styles, turned it into prioritized recommendations for a non-technical COO. | `experience-externship.md` |
| R8 | "Collaborate with cross-functional teams"; "collaborative work environments"; "communicate updates and findings to stakeholders"; "design reviews" | Firmly (engineering, UX, support), Externship (4-person team plus client COO), EPICS (7-person team, two formal design reviews to faculty, sponsors, and museum stakeholders). Proven in bullets, never listed as a soft skill. | `experience-firmly.md`, `experience-externship.md`, `leadership-epics.md` |
| P1 | Preferred: "Exposure to product analytics or data visualization tools" | MSME dashboard: Plotly visualization plus GoatCounter telemetry with five named custom events. Named in Skills with the exact tool names. | `project-msme-dashboard.md` |
| P2 | Preferred: "Coursework or projects related to AI, data, or software engineering" | Education line (Statistics, Engineering Design & Project Execution) plus three shipped software projects. | `education.md` |

## Honestly NOT claimed

- **"Experience with Agile practices" (a REQUIRED line).** Not claimed anywhere on this resume, and
  the word "Agile" appears nowhere in it. Per `skills-inventory.md` (hard calibration rule, set
  2026-06-15), Veer does not know the Scrum/Agile framework and cannot defend it if quizzed;
  claiming it is exactly the stack-inflation rejection signal the profile warns about. The adjacent
  half of that requirement, "and collaborative work environments," IS proven (R8). How he actually
  worked is described honestly: iterative build cycles, a decision ledger, formal review milestones.
  **Interview note: if asked about Agile, say plainly that he has not worked in a formal Scrum
  process, then describe the real cadence. Do not bluff.**
- **"Participate in Agile ceremonies."** Same reason. Not claimed.
- **"Roadmap planning"** (first line under What You'll Do). No profile file backs a roadmap
  artifact, so no roadmap claim is made. The nearest honest proof is the Externship's "set the
  delivery timeline." Covered by adjacency, not claimed outright. **Interview note: if asked for a
  roadmap example, use the STICK slice sequencing and say plainly it is a personal build, not a
  team roadmap.**
- **Any STICK user, adoption, retention, or outcome number.** STICK has zero real users; the student
  write path has fired once, in testing. The resume says "sole developer" and describes the
  pipeline, never a user base.
- **Cairn adoption count.** One verified external adopter who forked and extended it. Phrased as
  "adopted unprompted by an external builder who forked and extended it," never "users."
- **STICK extraction accuracy as a general rate.** The 12/12 answer-key match is n=1, one exam. The
  bullet says "a real 14-page, 12-question exam," never "the accuracy."

## Alternatives considered and why they lost

- **SMIF (Equity Research Analyst, ~$400K AUM, U.S. Bancorp report).** Dropped entirely. It is the
  strongest single proof for R7 (analyze data, communicate insights) but it is finance-domain and
  costs roughly four lines that AI-product proof uses better on a page this full. The Externship
  audit bullet covers R7 with a product-adjacent story instead. Reinstate SMIF if a future IBM
  round asks for business or financial analysis depth.
- **StudyFlowForge.** Superseded by STICK; carrying its "18 screens" would be stale and, per
  `project-stick.md`, must never be blended into STICK.
- **STICK's multi-agent build-workflow bullet** (used on the TikTok AI Agent resume). Cut here: it
  is on-topic for agent-infrastructure roles, off-topic for a general AI-product PM intern, and the
  space buys the human-in-the-loop responsible-AI bullet, which maps to an explicit JD line.
- **Cairn (open-source agentic-system scaffolder).** Drafted in, then CUT on the one-page constraint.
  Its unique value is the explicit North Star / metric-tree / guardrail vocabulary against R1, but
  its framing is agent-infrastructure, which this posting is not, and R1 is covered instead by
  STICK's stated product decision plus MSME's single-user scoping. It cost roughly five lines that
  bought back the STICK quality bullet (R6) and kept the page at one. **Reinstate Cairn if IBM's
  team turns out to be agent- or platform-flavored, or in a cover letter, where the metric-tree
  story has room to breathe.**
- **Firmly's QA-workflow bullet as its own line.** Compressed into bullet 2 to save a line.
- **Etsy design experience.** Not relevant to this role family.

## Independent review, 2026-08-21

A fresh-context reviewer audited the draft against the research checklist, the full profile set,
this match-map, and the ATS extraction. Findings and disposition:

**APPLIED (all substantive findings):**
- **Integrity, the one real inflation.** The draft said Veer "wrote the specification" at Firmly. No
  profile file supports a specification document; `experience-firmly.md` and `reusable-bullets.md`
  both say "defined requirements." Changed to "defined the requirements with engineering and
  support." This is the class of small upgrade that dies in a line-by-line walkthrough.
- **Biggest proof miss.** STICK bullet 1 had no result. Folded in the strongest AI-pipeline fact on
  the profile: the real 14-page, 12-question exam with all 12 auto-proposed answer keys matching the
  instructor's published key. Still phrased as one exam, never as a rate.
- **"Ranking" overstated the MSME instrument** (`project-msme-dashboard.md`: direction, not
  calibrated magnitude). Changed to "flags," and added the modeled-assumption-caveat clause, which
  also strengthens the responsible-AI story for a business unit that markets trusted data.
- **Skills rule.** "evaluation and human-review design for model output" was a capability claim
  already proven in a bullet. Replaced with Gemini API, a real tool name.
- **Education bullet.** "Rare business and engineering hybrid degree" was an unsupported adjective
  in the most-read slot; `role-positioning.md` puts that framing in the cover letter, not the
  resume. Changed to "Combined business and engineering curriculum."
- **Two free exact-keyword wins.** "two formal design reviews" (the JD says design reviews, and
  `leadership-epics.md` uses that exact phrase) and REST APIs in Tools (the JD names APIs).
- **Completion gap.** Externship bullet 1 now says "delivered," which closes the question of whether
  the calendar shipped. The COO praise stays off the resume per `experience-externship.md`.
- **ATS mechanics.** Added hyphenation suppression (Managerial Accounting was splitting across
  lines), replaced the Unicode arrows with commas, and moved the STICK date out of the empty
  `\entry` slot.

**NOTED, NOT CHANGED:**
- **"30 live topics"** is verbatim from `project-stick.md` and traceable, but it sits near a project
  with zero students and could be misread as "live with users." Kept. **Interview note: say "live in
  the content database," and volunteer the zero-students fact rather than waiting to be asked.**
- **Reviewer's optional swap of the MSME public decision log for the caveat clause.** Took the
  caveat, dropped the decision log. The decision log is the better generic PM signal; the caveat is
  the better IBM signal.

## Waivers

_(none: every reviewer finding was applied or explicitly noted above)_
