> Compressed working copy. Full original (with all source-citation tokens and Mermaid diagrams): files/applications/ResumeDeepResearch.md

# College Resume Best Practices — Compressed

Source anchors: MIT, Stanford Career Education, Purdue Center for Career Opportunities, U-Michigan Engineering Career Resource Center, NACE (employer survey data), plus McKinsey / Microsoft / Amazon recruiting advice, O*NET (keyword/tool signals), UIC Career Services, and TheLadders eye-tracking research.

## Core principles (what consistently works)
- **One page, one column, standard headings, conservative fonts, white space.** Undergrad = 1 page (Purdue explicit; MIT same unless extensive experience/advanced degree). 2 pages only for grad/PhD/unusually extensive.
- **Bullets as impact statements (CAR/PAR), short.** Replace "responsible for…" with action + scope (tools/context) + outcome. 1–2 lines each.
- **Quantify honestly.** Scale (users, $, rows, time), quality (error rate, accuracy, coverage), speed (latency, throughput). Mark estimates with ~ or ≈; never inflate (Microsoft requires honest representation; McKinsey: be honest, quantify).
- **Tailoring is mandatory** in 2026 screening. NACE: skills-based hiring widely used for entry-level screening/interviews. Translate coursework/projects/campus roles into skills + outcomes language.
- **Keyword mirroring in context, not stuffing.** Integrate JD terms naturally inside bullets/skills.

## How student resumes are screened — two gates
- **Gate A — human skim.** Recruiters decide in seconds; MIT: format must surface relevant info immediately. Stanford: employers may spend under 30 seconds. TheLadders eye-tracking: avg initial screen 7.4 seconds; strong resumes scan easily (clear layout), weak ones fail via clutter, multiple columns, keyword stuffing.
- **Gate B — ATS / keyword search.** Keep formatting simple, standard headings, JD language. Skills evidence must be both machine-parseable (text + matching keywords) and human-clear (impact).
- Why evidence focus matters for students: NACE Job Outlook 2025 — ~90% of employers look for evidence of problem solving, nearly 80% for teamwork (also written communication, initiative, work ethic, technical skills). NACE 2026: skills-based hiring widely used. NACE career-readiness framework = 8 competencies (critical thinking, communication, teamwork, technology, etc.) — turn behavior descriptions into bullets.

## Length & layout
- Length: undergrad 1 page (Purdue); MIT 1 page unless extensive/advanced; Stanford allows 1–2 (treat as ceiling, not target).
- Fonts/margins: readable standard fonts 10–12 pt; margins ≥ ~0.5 in (MIT: ≥ half-inch, font ≥ 10 pt; Purdue: 10–12 pt, ~0.5–1 in; Stanford: 10–12, ~0.75–1.0 in).

### Formatting choice → ATS risk
| Choice | ATS risk | Mechanism | Recommendation |
|---|---|---|---|
| Single-column | Low | Parsers read top-to-bottom reliably | Default to one column (incl. Skills) |
| Multi-column | Med–High | Some ATS misread/merge sections, read out of order; hurts F-pattern scan | Avoid; use spacing/tabs not side-by-side |
| Tables / text boxes | High | ATS may parse cell-by-cell or drop content | Plain text + tabs; no text boxes for Skills/dates |
| Graphics/icons/photos | High (US) | ATS ignores non-text; distracts; photos discouraged in US | Text-only; visuals go in portfolio |
| Excessive color/shading | Med | Reduces contrast, OCR/parse quality | Subtle only; never essential to meaning |
| Headers/footers for contact | Med–High | Some ATS skip headers/footers | Put name/contact in document body at top |
| Non-standard headings | Med | ATS maps to structured fields | Use Education, Experience, Projects, Skills |
| PDF vs DOC/DOCX | Variable | Employers/ATS differ | Follow JD; else clean PDF, validate via copy/paste |
| LaTeX-generated PDF | Variable–High | Some centers warn LaTeX→PDF may fail ATS depending on encoding/structure | Ensure selectable text, single-column, clean copy/paste; consider Word for strict ATS |
| Dense paragraphs vs bullets | Med | Hurts keyword prominence + scan | Use bullets; most 1–2 lines |

## Section order — relevance optimization (1 page + fast scan)
Build a master resume, then include/order by the posting. Default architecture: Heading → Education (often first for students) → Experience (internships, campus jobs, research, TA) → Projects (esp. technical / early-year) → Leadership/Activities/Volunteering (if targeted) → Skills.
**Rule: most job-relevant proof in the top half of page one.** Reorder triggers:
- Education first for current students / very recent grads (Michigan).
- Projects above Experience when limited work history + projects align to the role (common SWE/data).
- Research near top for labs/R&D/analytics.
- Leadership/Service near top when role values it (consulting, some product/ops); use descriptive headings ("Leadership and Teamwork," "Project Management").

## Bullets, quantification, translation
- **CAR (Context→Action→Result)** = **PAR (Problem→Action→Result)** = Purdue "power verb + task + purpose/method/result." Synthesis: **Action verb + what you built/analyzed/led + tools/constraints + outcome metric (or why it mattered).**
- Convert task descriptions → impact statements (Michigan before→after). 1–2 lines/bullet; embed tools/skills in context (MIT); believable + verifiable (Stanford).
- **Quantification toolkit** (MIT taxonomy: financial performance, % change, quantity/scale):
  - Scale: users/day-week; data volume (rows/events/files/surveys/interviews); system scale (endpoints/services/repos/test cases); budget/funds/$ influenced.
  - Quality: error-rate reduction, defect escape, incidents; accuracy/precision/recall/model perf, audit findings; test coverage, SLA adherence.
  - Speed: time saved/task, cycle-time, throughput, latency/runtime, "from X min to Y min."
  - Estimation (untracked): logs/analytics (commits, issues, dashboard views, traffic); time studies (avg min × frequency); bounded ranges ("~200–300 attendees"); conservative, mark ~/≈.
- **Skills section:** objective + relevant + scannable; prove soft skills in bullets (Michigan warns against listing soft skills without evidence; "Python" not "team player"). Use categories (Languages, Frameworks, Data/Analytics, Tools). No self-rating bars ("80% Python"). Mirror exact tool names when truthful (SQL + PostgreSQL, Tableau, Power BI).
- **Projects block:** name + stack/tools + 1-line scope; 2–4 CAR/PAR bullets (technical depth + outcome metric); links as plain text.
- **Translate research/TA/volunteer/campus jobs:** (1) deliverable, (2) audience/customer, (3) constraint, (4) measurable proxy.

## Common mistakes → fixes
- Multi-column/designed templates break parsing → one column, no tables/boxes, standard headings, test ATS.
- Duties not outcomes → CAR/PAR with results (even "enabled X decision" / "reduced dependence on Y").
- Keyword stuffing → integrate keywords where actually used; keep human-readable.
- Unverified/inflated metrics → conservative estimates, explainable; employers require honesty.
- Typos/inconsistent formatting → proofread; consistent dates, indentation, verb tense.

## Tailoring workflow (single posting → one tailored resume; ~45–70 min)
| Step | Time | Output | Do |
|---|---|---|---|
| Job decode | 8–12 min | Keyword list + success criteria | Highlight required skills/tools/deliverables; note repeated terms |
| Match map | 6–10 min | Requirement→proof | Pair each key requirement with 1–2 experiences/projects |
| Section reordering | 3–6 min | New order | Move most relevant sections/bullets up |
| Bullet rewrite | 15–25 min | 6–10 bullets | Convert to CAR/PAR; add tools + metrics |
| Keyword integration | 5–8 min | Final placement | Core terms appear naturally across bullets/skills |
| ATS-readability | 3–6 min | Parser-safe | Copy/paste to plain text; verify order/chars; remove tables/headers |
| Final proof | 4–7 min | Submission-ready | Date formats, tense, spelling, alignment |

ATS/keyword discipline: use JD language in context (Stanford, Purdue, UIC "Adobe Photoshop" not "image-editing software"); avoid stuffing (TheLadders; Michigan "don't go overboard"); treat keywords as evidence labels (NACE — show where/how skills used). Placement rubric: optional headline only if you truly match; top 3–6 requirements each backed by ≥1 matching-language bullet; synonym pairing ("natural language processing (NLP)," "continuous integration (CI)").

## Industry mapping — proof keywords + tools
| Industry | Proof keywords | Tools (when truthful) |
|---|---|---|
| Software engineering | APIs, testing, CI/CD, performance, data structures, collaboration | Python, Java, SQL, AWS, Docker, Git |
| Data science / analytics | data mining, modeling, ML/NLP, visualization, reporting, experimentation | Python, R, Jupyter, SQL; Tableau/Power BI |
| Product / PM (incl. TPM) | requirements/specs, cross-functional, customer needs, success metrics, prioritization | Jira, Confluence, Excel, SQL, cloud (role-dependent) |
| Finance | valuation, modeling, investment thesis, risk, pitch/communication | Excel, PowerPoint; role-specific finance tools |
| Consulting | problem solving, analysis, stakeholder communication, recommendations, leadership | Excel, PowerPoint, SQL, Power BI, Tableau |
| Design (UI/UX/visual) | usability, prototyping, interaction design, visual systems, iteration | Figma, Adobe Creative Cloud; role-specific web tech |

## Before/after bullet models (action + tools/context + measurable outcome)
**SWE**
- Built a REST API in Python with PostgreSQL and documented endpoints; improved median request latency by 35% and supported ~5K requests/day.
- Wrote 120+ unit/integration tests (pytest) and added CI checks; increased coverage from 45% → 85% and reduced post-merge regressions.
- Partnered with a 4-person team using Git code reviews; shipped 3 user-facing features on schedule with zero Sev-1 bugs.

**Data/analytics**
- Queried and cleaned 2 years of customer data (SQL + Python/pandas); identified 3 churn drivers and proposed retention experiments adopted by the team.
- Developed a KPI dashboard (Tableau/Power BI); reduced manual reporting by ~2 hours/week and improved decision turnaround.
- Trained/evaluated a classification model in Python; improved F1 from 0.62 → 0.74 via feature engineering and cross-validation; 2-page technical report.

**Product/PM**
- Authored a PRD for a checkout error-recovery flow; aligned eng/support on edge cases, defined success metrics, reduced "generic error" drop-offs by ~X% (pilot).
- Coordinated design + engineering across 2 sprints; clarified requirements, unblocked dependencies, shipped a feature improving activation by 12% in A/B test.
- Conducted 15 user interviews, synthesized pain points into a prioritized backlog, presented tradeoffs to stakeholders.

**Finance**
- Built a 3-statement model and DCF in Excel; thesis supported by comps + catalysts; price target in a 10-slide pitch deck.
- Analyzed 12 equities, pitched 2 buy/avoid recommendations; risk/return scenarios defended in weekly investment committee.
- Developed sensitivity tables + scenario analysis; quantified downside cases; communicated in PowerPoint.

**Consulting**
- Structured analysis of cost drivers across 5 categories; identified ~$1.2M annual savings; presented prioritization plan to leadership.
- Led a 4-person team to redesign a process; cut cycle time 10 days → 6 days by removing 2 approval bottlenecks.
- Synthesized 20 stakeholder interviews + secondary research; recommendation memo with quantified tradeoffs.

**Design**
- Designed/prototyped a 12-screen mobile flow in Figma; usability tests with 8 users; cut time-to-task by 30%.
- Created a reusable visual system + asset templates; reduced production time for new collateral by ~40%.
- Partnered with engineering to ship a component library; documented interaction specs + accessibility.

## Checklist
- Target clarity: top third makes internship family obvious.
- ATS-safe: one column, no tables/boxes/graphics, standard headings, consistent dates.
- Evidence-first: each role/project 2–5 CAR/PAR bullets with tools + outcome.
- Quantification: ≥50% of bullets have a number/scope marker.
- Keyword alignment: each top requirement has a matching proof bullet, integrated not stuffed.
- Integrity: all metrics defensible, explainable in interview.
- Final scan test: school, major, target role, strongest evidence identifiable in <20 seconds.

## Templates
Header (ATS-safe, in body not header/footer): `FIRST LAST` / `City, ST | phone | email | LinkedIn URL | GitHub/Portfolio URL`.
Headings: `EDUCATION / EXPERIENCE / PROJECTS / LEADERSHIP & ACTIVITIES / SKILLS`.
Action verbs: Built • Designed • Implemented • Analyzed • Automated • Optimized • Led • Shipped • Validated • Presented.
(Full "top third of page" worked examples for SWE and data-analytics internships are in the original.)
