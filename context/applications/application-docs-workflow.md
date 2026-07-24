# Application-Docs Workflow

How the assistant produces Veer's tailored resumes and cover letters. This is an
on-demand capability: given a job listing (URL, pasted text, or company name), produce a
tailored single-page resume (LaTeX + PDF), and a matching cover letter only when explicitly
requested.

## Files to read

**Always (resume tasks), before reading any old PDF:**
- `context/applications/profile/` — Veer's source-of-truth. Read the ones relevant to the
  target role, ordered per `profile/role-positioning.md`. The default resume set is:
  `contact.md`, `education.md`, `experience-firmly.md`, `experience-smif.md`,
  `experience-externship.md`, `project-stick.md`, `project-studyflowforge.md`,
  `leadership-epics.md`, `skills-inventory.md`, `role-positioning.md`, `reusable-bullets.md`.
  Add `experience-etsy-design.md` for design / digital-media / creative roles.
  (STICK is the CURRENT product; StudyFlowForge is a superseded past build — see Step 0.)
- `context/applications/research/ResumeDeepResearch.md` — resume best-practices (compressed
  working copy; full original in `files/applications/`).
- `files/applications/Summer2026_Internship_Research.md` — Veer's target roles, profile
  strengths, status notes (read directly; small, uncompressed).

**Additionally, only when a cover letter is requested:**
- `context/applications/research/CoverLetterDeepResearch.md` (full original in
  `files/applications/`). Do NOT read it for resume-only tasks.

**Only if the profile is missing a needed detail:**
- `applications/_master/Veer_Sanyal_Resume.pdf` — master resume (full experience inventory).
- Prior tailored resumes in `applications/<Company>/` — mine for proven phrasings/metrics.

## Output structure

Write into `applications/<Company or Job Identifier>/`. Create the folder if missing. Use a
clear identifier (e.g. `Cisco`, `Cloudflare`, `Gates Ventures - Alzheimers PM`).

For every deliverable produce BOTH:
- `.tex` source — start from `context/applications/resume-template.tex`
- `.pdf` rendered from that source

Naming:
- Resume: `VeerSanyal_<Company>_Resume.tex` + `.pdf`
- Cover letter: `VeerSanyal_<Company>_CoverLetter.tex` + `.pdf`

Never leave a stray PDF without its source `.tex`.

## Resume rules
- **One page, hard constraint.** If content overflows, cut weaker bullets — do not shrink
  fonts below 10 pt or margins below ~0.5 in.
- One column, standard headings (Education, Experience, Projects, Skills), no
  tables/text-boxes/graphics, ATS-safe. Header in the document body (not PDF header/footer).
- Bullets follow CAR/PAR: action verb + tools/context + quantified outcome.
- Mirror the posting's exact tool/skill terms in context (no keyword stuffing).
- Reorder sections so the strongest proof for *this* role sits in the top third
  (see `profile/role-positioning.md`).
- Pull details only from profile + master + prior resumes — never invent metrics. Mark
  unverified numbers `~` or omit.

## Cover letter rules (when requested)
- One page, 3–4 paragraphs, 10–12 pt, business-letter format.
- Same font + header as the resume for visual consistency.
- Opening: role + specific "why this company" + 2–3 skill thesis.
- 1–2 body paragraphs, each a proof story (action → scope → result).
- Don't restate the resume; add detail, motivation, or fit narrative.
- Address a named hiring manager when findable; else "Dear Hiring Manager."

## Workflow
0. **Currency check (do this FIRST — the profile is a derived snapshot and drifts).** The
   `profile/*.md` files are a hand-written view of live reality; the authoritative owners are
   elsewhere and move faster. Before drafting, reconcile the profile against the current owners
   and **patch any stale `profile/*.md` in place** so the resume reflects what Veer is actually
   doing now, not a months-old snapshot:
   - **Current focus / what's shipped** → `memory.md` (fast read).
   - **Pillar-1 product (STICK)** → `~/Desktop/stick-dev/STATE.md` is authoritative. Do NOT pull
     its large docs into context — spawn a subagent to return honest, quizzable resume facts +
     current numbers, then update `profile/project-stick.md` if it drifted. STICK ≠ StudyFlowForge
     (from-scratch rebuild); never carry StudyFlowForge's "18 screens"/dashboards into STICK.
   - **Externship** → `context/externship-scouting-america.md` + `PROGRESS.md` tail; refresh
     `profile/experience-externship.md`.
   - Any NEW experience/project Veer mentions that has no profile file yet → gather real facts
     (subagent if noisy), create the `profile/*.md`, then use it. Never invent metrics to fill a gap.
   This is the "keep the apply stream current" guarantee: even if nobody synced the profile, apply
   self-heals here. Then proceed.
1. Decode the listing: top requirements, exact keywords, must-prove skills.
2. Read profile first (per role family); only fall back to master/prior PDFs for gaps.
3. Match-map each top requirement to the strongest proof from profile + `reusable-bullets.md`.
4. Draft `.tex` from the template → compile (`pdflatex VeerSanyal_<Company>_Resume.tex`, or
   `latexmk -pdf`) → verify single page → save both files in the company folder.
5. Cover letter requested → repeat with `CoverLetterDeepResearch.md` loaded.
6. Update profile memory with anything new surfaced (new project, metric, bullet, skill) —
   edit the relevant `profile/*.md` in place; correct, don't append duplicates.
7. Update `applications/README.md` inventory; if the listing has a deadline, add/update its
   row in `context/key-dates.md` (Application Pipeline table).

## Deadlines
Application deadlines live in `context/key-dates.md` (Application Pipeline table) — the single
source of truth for timing. `applications/README.md` is a file inventory only and holds no
dates. When the Sunday planning session runs, any pipeline deadline within ~2 weeks still at
Stage < Ready is a candidate "draft `<Company>` resume" work block.

## Defaults / preferences
- Resume is a 1-page hard cap; don't shrink below 10 pt / 0.5 in.
- Always include EPICS for leadership signal (1–2 bullets).
- Match skills-category headers to the JD's framing; choose 3–4 per resume.
- If a listing is ambiguous about role family (PM vs SWE vs finance), ask before drafting.
- Convert relative dates in listings to absolute dates when noting deadlines.
- Veer prefers concise, direct communication. Skip preamble and post-hoc summaries; let the
  delivered files speak.
