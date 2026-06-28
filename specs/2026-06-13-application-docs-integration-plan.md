# Application-Docs Integration Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Fold Veer's scattered resume / cover-letter system (profile data, generation instructions, deep research, per-company outputs) into the `veer-pm-project` planning repo along its three-tier convention, with application deadlines wired into key-dates + Sunday planning.

**Architecture:** Copy-only migration into a new `applications/` vertical. Profile → `context/applications/profile/`; merged workflow + LaTeX template → `context/applications/`; research → `files/applications/` (full) + `context/applications/research/` (compressed, large docs only); outputs → top-level `applications/`. Five existing system files are edited to wire it in.

**Tech Stack:** Markdown, LaTeX (`pdflatex`/`latexmk` at `/Library/TeX/texbin/`), git. No application code or test framework — verification is shell assertions (file counts, link greps, a template compile).

**Source paths (read-only; copy-only, never modified or deleted):**
- `MEM` = `/Users/veersanyal/Library/Application Support/Claude/local-agent-mode-sessions/41f5c0c7-cd68-4055-8f05-69668e6fba71/dc6d873b-5e80-4924-8339-e682a5c63ba0/spaces/4a9c0286-abea-4725-9508-52fd774d1b3c/memory`
- `INSTR` = `/Users/veersanyal/Documents/Claude/Projects/Internship Resume/Coverletter/PROJECT_INSTRUCTIONS.md`
- `DL` = `/Users/veersanyal/Downloads/Internships`

**Destination:** `REPO` = `/Users/veersanyal/Desktop/veer-pm-project`

**Reference:** design spec at `specs/2026-06-13-application-docs-integration-design.md`.

**Git note:** All git operations run from inside `REPO` only. Each task commits locally with a real message. **Do not push** — pushing to `master` requires Veer's explicit authorization (deferred to the final handoff). Every task begins by confirming the repo root ends in `/veer-pm-project`.

---

## Task 0: Repo safety preamble (run before every commit)

This snippet is referenced by later commit steps. It aborts if run in the wrong repo.

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
top=$(git rev-parse --show-toplevel)
case "$top" in
  */veer-pm-project) : ;;
  *) echo "WRONG REPO: $top — aborting"; exit 1;;
esac
```

---

## Task 1: Create the directory skeleton

**Files:**
- Create dirs: `context/applications/profile/`, `context/applications/research/`, `files/applications/`, `applications/_master/`

- [ ] **Step 1: Create directories**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
mkdir -p context/applications/profile context/applications/research files/applications applications/_master
```

- [ ] **Step 2: Verify they exist**

```bash
ls -d context/applications/profile context/applications/research files/applications applications/_master
```
Expected: all four paths print, no "No such file" error.

---

## Task 2: Migrate profile files (copy + drop `user_` prefix)

**Files:**
- Create: `context/applications/profile/{contact,education,experience-firmly,experience-smif,project-studyflowforge,experience-etsy-design,leadership-epics,skills-inventory,role-positioning,reusable-bullets}.md` and `MEMORY.md`
- Source: `MEM/user_*.md` and `MEM/MEMORY.md`

- [ ] **Step 1: Copy + rename the 10 content files**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
MEM="/Users/veersanyal/Library/Application Support/Claude/local-agent-mode-sessions/41f5c0c7-cd68-4055-8f05-69668e6fba71/dc6d873b-5e80-4924-8339-e682a5c63ba0/spaces/4a9c0286-abea-4725-9508-52fd774d1b3c/memory"
P="context/applications/profile"
cp "$MEM/user_contact.md"               "$P/contact.md"
cp "$MEM/user_education.md"             "$P/education.md"
cp "$MEM/user_experience_firmly.md"    "$P/experience-firmly.md"
cp "$MEM/user_experience_smif.md"      "$P/experience-smif.md"
cp "$MEM/user_project_studyflowforge.md" "$P/project-studyflowforge.md"
cp "$MEM/user_experience_etsy_design.md" "$P/experience-etsy-design.md"
cp "$MEM/user_leadership_epics.md"     "$P/leadership-epics.md"
cp "$MEM/user_skills_inventory.md"     "$P/skills-inventory.md"
cp "$MEM/user_role_positioning.md"     "$P/role-positioning.md"
cp "$MEM/user_reusable_bullets.md"     "$P/reusable-bullets.md"
```

- [ ] **Step 2: Verify 10 files copied**

```bash
ls context/applications/profile/*.md | wc -l
```
Expected: `10`

- [ ] **Step 3: Write the profile `MEMORY.md` index** (rewritten links to new filenames)

Create `context/applications/profile/MEMORY.md` with exactly:

```markdown
# Profile memory — Veer's resume source-of-truth

These are the canonical building blocks for every tailored resume / cover letter.
Read the relevant ones (ordered per `role-positioning.md`) before drafting. Workflow
and Veer's preferences live in `../application-docs-workflow.md`.

- [Contact / Header](contact.md) — name, phone, email, LinkedIn, location
- [Education](education.md) — Purdue IBE, May 2028, coursework
- [Firmly internship](experience-firmly.md) — Product/Eng Intern, Summer 2025, PayPal checkout flow
- [SMIF analyst](experience-smif.md) — Equity Research, $400K AUM, U.S. Bancorp report
- [Etsy + design portfolio](experience-etsy-design.md) — Etsy digital-products shop (~50 sold), Photoshop/Illustrator/Lightroom design
- [StudyFlowForge project](project-studyflowforge.md) — AI study platform, React/TS/Supabase/Gemini
- [EPICS leadership](leadership-epics.md) — Build Lead, museum billboard prototype
- [Skills inventory](skills-inventory.md) — full list grouped by category
- [Role-family positioning](role-positioning.md) — what to emphasize for PM vs SWE vs finance
- [Reusable bullet phrasings](reusable-bullets.md) — battle-tested CAR/PAR bullets
```

- [ ] **Step 4: Verify no dangling wikilinks or markdown links in profile**

The `[[...]]` body cross-refs use frontmatter slugs (`user-skills-inventory`, `user-experience-etsy-design`) which are **preserved unchanged** inside the files, so they still resolve to each other. Confirm the only `[[...]]` targets present are slugs that exist as a `name:` in some profile file:

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project/context/applications/profile"
echo "--- wikilink targets used ---"; grep -oh '\[\[[a-z-]*\]\]' *.md | sort -u
echo "--- slugs defined ---"; grep -h '^name:' *.md | sed 's/name: *//' | sort -u
```
Expected: every target shown in the first list (e.g. `[[user-skills-inventory]]`, `[[user-experience-etsy-design]]`) appears as a defined slug in the second list. (The `feedback_resume_workflow.md` `[[user-*]]` links are NOT here — they move into the workflow doc in Task 3.)

- [ ] **Step 5: Commit** (after Task 0 preamble)

```bash
git add context/applications/profile
git commit -m "Add resume profile source-of-truth to context/applications/profile

Copied the 12 profile memory files from the Claude app session space,
dropping the user_ prefix; rewrote the MEMORY index to new filenames.
Frontmatter slugs preserved so [[wikilink]] cross-refs still resolve."
```

---

## Task 3: Author the merged workflow doc

**Files:**
- Create: `context/applications/application-docs-workflow.md`
- Sources merged: `INSTR` (PROJECT_INSTRUCTIONS.md) + `MEM/feedback_resume_workflow.md`

- [ ] **Step 1: Write the file** with exactly this content:

````markdown
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
  `project-studyflowforge.md`, `leadership-epics.md`, `skills-inventory.md`,
  `role-positioning.md`, `reusable-bullets.md`. Add `experience-etsy-design.md` for design /
  digital-media / creative roles.
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
````

- [ ] **Step 2: Verify no old paths survive**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -n "Internships/" context/applications/application-docs-workflow.md || echo "CLEAN: no Internships/ paths"
```
Expected: `CLEAN: no Internships/ paths`

- [ ] **Step 3: Commit** (after Task 0 preamble)

```bash
git add context/applications/application-docs-workflow.md
git commit -m "Add merged application-docs workflow

Reconciles PROJECT_INSTRUCTIONS.md and feedback_resume_workflow.md into
one doc with all paths rewritten to in-repo locations."
```

---

## Task 4: Extract the canonical LaTeX template

**Files:**
- Create: `context/applications/resume-template.tex`
- Source pattern: `DL/ApplicationDocuments/Handshake AI - Finance Expert/VeerSanyal_HandshakeAI_Resume.tex` (preamble reference)

- [ ] **Step 1: Write the template** with exactly this content:

```latex
% Canonical ATS-safe single-column resume template for Veer Sanyal.
% Copy this to applications/<Company>/VeerSanyal_<Company>_Resume.tex and fill the body.
% Compile: pdflatex VeerSanyal_<Company>_Resume.tex   (or: latexmk -pdf <file>.tex)
% Rules: 1 page hard cap; do not drop font below 10pt or margins below ~0.5in.
\documentclass[10pt,letterpaper]{article}

\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[left=0.6in,right=0.6in,top=0.55in,bottom=0.55in]{geometry}
\usepackage{enumitem}
\usepackage{titlesec}
\usepackage{hyperref}
\usepackage{xcolor}
\hypersetup{colorlinks=true,urlcolor=black,linkcolor=black}
\pagestyle{empty}
\setlength{\parindent}{0pt}

% Section formatting: bold heading + horizontal rule
\titleformat{\section}{\large\bfseries}{}{0pt}{}[\vspace{1pt}\hrule\vspace{3pt}]
\titlespacing{\section}{0pt}{6pt}{2pt}

% Tight list formatting
\setlist[itemize]{leftmargin=1.3em,topsep=1pt,itemsep=1pt,parsep=0pt,label=\textbullet}

% Entry header helper: \entry{Title}{Location}{Subtitle}{Dates}
\newcommand{\entry}[4]{%
  \textbf{#1}\hfill #2\\[1pt]
  \textit{#3}\hfill \textit{#4}\\[2pt]
}

\begin{document}

% ===== HEADER (in body, ATS-safe — never in \pagestyle header/footer) =====
\begin{center}
  {\LARGE \textbf{Veer Sanyal}}\\[3pt]
  Sammamish, WA $\cdot$ 360-643-9424 $\cdot$ vsanyal@purdue.edu $\cdot$ linkedin.com/in/veersanyal
\end{center}

% ===== EDUCATION =====
\section*{Education}
\textbf{Purdue University --- Mitch Daniels School of Business}\hfill West Lafayette, IN\\[1pt]
\textit{B.S. Integrated Business and Engineering (IBE), Expected May 2028}\hfill \textit{Aug. 2024 -- Present}
\begin{itemize}
  \item Relevant coursework: % fill per role (see profile/education.md)
\end{itemize}

% ===== EXPERIENCE (reorder sections per profile/role-positioning.md) =====
\section*{Experience}
\entry{Company}{Location}{Title}{Dates}
\begin{itemize}
  \item % CAR/PAR bullet
\end{itemize}

% ===== PROJECTS =====
\section*{Projects}
\entry{Project}{}{Subtitle}{Dates}
\begin{itemize}
  \item % CAR/PAR bullet
\end{itemize}

% ===== SKILLS (3-4 categories, names mirroring the JD) =====
\section*{Skills}
\textbf{Category:} item, item, item

\end{document}
```

- [ ] **Step 2: Smoke-compile the template** to confirm LaTeX works on this machine

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project/context/applications"
/Library/TeX/texbin/pdflatex -interaction=nonstopmode -halt-on-error resume-template.tex >/tmp/tex.log 2>&1 && echo "COMPILE OK" || (echo "COMPILE FAILED"; tail -20 /tmp/tex.log)
ls -la resume-template.pdf
```
Expected: `COMPILE OK` and a `resume-template.pdf` exists.

- [ ] **Step 3: Remove compile byproducts** (keep only the `.tex`; don't commit the test PDF/aux)

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project/context/applications"
rm -f resume-template.pdf resume-template.aux resume-template.log resume-template.out
```

- [ ] **Step 4: Commit** (after Task 0 preamble)

```bash
git add context/applications/resume-template.tex
git commit -m "Add canonical ATS-safe resume LaTeX template

Extracted preamble + \entry helper from existing tailored resumes."
```

---

## Task 5: Migrate research docs (full + compressed)

**Files:**
- Create (full): `files/applications/{ResumeDeepResearch.md,CoverLetterDeepResearch.md,Summer2026_Internship_Research.md}`
- Create (compressed): `context/applications/research/{ResumeDeepResearch.md,CoverLetterDeepResearch.md}`
- Source: `DL/ResearchContext/`

- [ ] **Step 1: Copy the three full originals to `files/applications/`**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
DL="/Users/veersanyal/Downloads/Internships"
cp "$DL/ResearchContext/ResumeDeepResearch.md"          files/applications/
cp "$DL/ResearchContext/CoverLetterDeepResearch.md"     files/applications/
cp "$DL/ResearchContext/Summer2026_Internship_Research.md" files/applications/
ls files/applications/ | wc -l   # expect 3
```
Expected: `3`

- [ ] **Step 2: Author compressed copy of `ResumeDeepResearch.md`**

Read `files/applications/ResumeDeepResearch.md` in full. Write a compressed version to
`context/applications/research/ResumeDeepResearch.md` that preserves EVERY fact, number, rule,
percentage, and citation while cutting roughly half the tokens (remove restatement, hedging,
and prose padding; keep all concrete guidance as tight bullets). Add a first line:
`> Compressed working copy. Full original: files/applications/ResumeDeepResearch.md`

- [ ] **Step 3: Verify compression fidelity (numbers preserved)**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
echo "--- numbers in original not found in compressed ---"
comm -23 \
  <(grep -oE '[0-9]+(\.[0-9]+)?%?' files/applications/ResumeDeepResearch.md | sort -u) \
  <(grep -oE '[0-9]+(\.[0-9]+)?%?' context/applications/research/ResumeDeepResearch.md | sort -u)
echo "--- (empty above = all numbers preserved) ---"
wc -l files/applications/ResumeDeepResearch.md context/applications/research/ResumeDeepResearch.md
```
Expected: the diff list is empty (every number in the original survives), and the compressed line count is meaningfully lower than the original. If any number is missing, add it to the compressed copy and re-run.

- [ ] **Step 4: Author + verify compressed copy of `CoverLetterDeepResearch.md`** (same procedure as Steps 2–3)

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
comm -23 \
  <(grep -oE '[0-9]+(\.[0-9]+)?%?' files/applications/CoverLetterDeepResearch.md | sort -u) \
  <(grep -oE '[0-9]+(\.[0-9]+)?%?' context/applications/research/CoverLetterDeepResearch.md | sort -u)
```
Expected: empty diff. First line of the compressed copy:
`> Compressed working copy. Full original: files/applications/CoverLetterDeepResearch.md`

- [ ] **Step 5: Commit** (after Task 0 preamble)

```bash
git add files/applications context/applications/research
git commit -m "Add application research: full originals + compressed copies

Full ResearchContext docs in files/applications/; compressed working
copies of the two large best-practices docs in context/applications/research/.
Summer2026 doc kept uncompressed (small, read directly)."
```

---

## Task 6: Migrate per-company outputs + master, build inventory

**Files:**
- Create: `applications/<Company>/...` (12 folders) + `applications/_master/Veer_Sanyal_Resume.pdf` + `applications/README.md`
- Source: `DL/ApplicationDocuments/` and `DL/Veer_Sanyal_Resume.pdf`

- [ ] **Step 1: Copy the master resume**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
DL="/Users/veersanyal/Downloads/Internships"
cp "$DL/Veer_Sanyal_Resume.pdf" applications/_master/
```

- [ ] **Step 2: Copy all company folders (exclude .DS_Store)**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
DL="/Users/veersanyal/Downloads/Internships"
rsync -a --exclude='.DS_Store' "$DL/ApplicationDocuments/" applications/
```

- [ ] **Step 3: Verify folder + file counts match source**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
DL="/Users/veersanyal/Downloads/Internships"
echo "src company dirs:"; find "$DL/ApplicationDocuments" -mindepth 1 -maxdepth 1 -type d | wc -l
echo "dst company dirs:"; find applications -mindepth 1 -maxdepth 1 -type d ! -name _master | wc -l
echo "src pdf:"; find "$DL/ApplicationDocuments" -name '*.pdf' | wc -l
echo "dst pdf:"; find applications -name '*.pdf' ! -path '*/_master/*' | wc -l
echo "src tex:"; find "$DL/ApplicationDocuments" -name '*.tex' | wc -l
echo "dst tex:"; find applications -name '*.tex' | wc -l
```
Expected: company dirs 12 = 12; pdf 16 = 16; tex 2 = 2.

- [ ] **Step 4: Write `applications/README.md`** with exactly this content:

```markdown
# Applications — output tier

Generated tailored resumes and cover letters, one folder per company. This is a **file
inventory only** — application deadlines and pipeline status live in
`../context/key-dates.md`. The generation workflow is
`../context/applications/application-docs-workflow.md`.

- `_master/Veer_Sanyal_Resume.pdf` — master resume, full experience inventory.
- Legacy folders were migrated 2026-06-13 from `~/Downloads/Internships/ApplicationDocuments`.
  Most are PDF-only — their `.tex` source was not retained and will NOT be fabricated;
  regenerate a source on demand from the profile + template when an edit is needed.

| Company / Job | Files present | Editable .tex? |
|---|---|---|
| Cisco | Resume.pdf | No — regenerate on demand |
| Cloudflare | Resume.pdf | No — regenerate on demand |
| Daniels Externship | Resume.pdf, CoverLetter.pdf | No — regenerate on demand |
| Handshake AI - 2D 3D Digital Media | Resume.tex, Resume.pdf | Yes |
| Handshake AI - Finance Expert | Resume.tex, Resume.pdf | Yes |
| Paccar | Resume.pdf, CoverLetter.pdf | No — regenerate on demand |
| SAP | Resume.pdf, CoverLetter.pdf | No — regenerate on demand |
| Samsung PM | Resume.pdf | No — regenerate on demand |
| Samsung Profit Management | Resume.pdf | No — regenerate on demand |
| SpaceX | Resume.pdf, CoverLetter.pdf | No — regenerate on demand |
| Tesla | Resume.pdf | No — regenerate on demand |
| Tiktok | Resume.pdf | No — regenerate on demand |

New applications: add a row here when the folder is created.
```

- [ ] **Step 5: Reconcile the inventory table against reality**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project/applications"
for d in */; do [ "$d" = "_master/" ] && continue; echo "== $d"; ls "$d"; done
```
Expected: the file lists match the README table rows. If any company's actual files differ from the table (extra/missing file, or a `.tex` present that the table marks "No"), correct that row.

- [ ] **Step 6: Commit** (after Task 0 preamble)

```bash
git add applications
git commit -m "Migrate per-company application outputs + master resume

Copied 12 company folders (16 PDFs, 2 .tex) and the master resume into
applications/. Added README inventory flagging PDF-only legacy folders."
```

---

## Task 7: Wire deadlines into `key-dates.md`

**Files:**
- Modify: `context/key-dates.md` (append a new section)

- [ ] **Step 1: Read the file to find a clean insertion point**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
tail -20 context/key-dates.md
```
Note the final heading so the new section is appended cleanly at the end.

- [ ] **Step 2: Append the Application Pipeline section** to the end of `context/key-dates.md`:

```markdown

## Application Pipeline

Single source of truth for application timing. The on-demand application-docs workflow
(`context/applications/application-docs-workflow.md`) writes outputs to `applications/<Company>/`
and updates the row here. Stage ∈ {Researching, Drafting, Ready, Submitted}.

**Sunday rule:** any deadline within ~2 weeks still at Stage < Ready becomes a candidate
"draft `<Company>` resume" work block for the week (see SYSTEM-PROMPT).

| Company / Role | Deadline (absolute) | Stage | Docs |
|---|---|---|---|
| _(none active — 12 legacy applications archived in `applications/`)_ | — | — | `applications/` |

Add a row when a new target is identified; convert any relative deadline to an absolute date.
```

- [ ] **Step 3: Verify the section is present**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -n "## Application Pipeline" context/key-dates.md
```
Expected: one match.

- [ ] **Step 4: Commit** (after Task 0 preamble)

```bash
git add context/key-dates.md
git commit -m "Add Application Pipeline table to key-dates

Single source of truth for application timing; feeds the Sunday session
candidate-work-block rule."
```

---

## Task 8: Wire the capability into `SYSTEM-PROMPT.md`

**Files:**
- Modify: `SYSTEM-PROMPT.md`

- [ ] **Step 1: Add a route to the "CONSULT WHEN RELEVANT" list.** Find the line beginning
  `- LinkedIn posting / profile / content -> context/research-linkedin-presence.md` and insert
  immediately after it:

```markdown
- Resume / cover letter / any application document -> context/applications/application-docs-workflow.md (reads context/applications/profile/ + research/; outputs to applications/<Company>/)
```

- [ ] **Step 2: Add the capability + Sunday rule.** Find the `ALSO READ IN SUNDAY PLANNING
  MODE` block. Immediately BEFORE it, insert a new standalone section:

```markdown
APPLICATION DOCUMENTS (on-demand capability):
When Veer asks for a resume or cover letter for a role, follow context/applications/application-docs-workflow.md. In short: read context/applications/profile/ (ordered per profile/role-positioning.md) and context/applications/research/ResumeDeepResearch.md before any old PDF; produce BOTH a .tex (from context/applications/resume-template.tex) and a compiled .pdf into applications/<Company>/; never invent metrics; keep the resume to one page. Read context/applications/research/CoverLetterDeepResearch.md only when a cover letter is requested. After each build, update the relevant context/applications/profile/*.md with any new metric/bullet/skill, update applications/README.md, and if the listing has a deadline add/update its row in context/key-dates.md (Application Pipeline). Application timing lives in key-dates.md, not in the README.

```

- [ ] **Step 3: Add the deadline planning rule to the Sunday list.** In the `ALSO READ IN
  SUNDAY PLANNING MODE` numbered list, append a new item after the existing last item
  (currently item 9, the full past week of PROGRESS.md):

```markdown
10. context/key-dates.md Application Pipeline - any application deadline within ~2 weeks still at Stage < Ready becomes a candidate "draft <Company> resume" work block for the week; if the Calendar connector is on, optionally write one deadline event per open application.
```

- [ ] **Step 4: Verify all three edits landed**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -c "application-docs-workflow.md" SYSTEM-PROMPT.md   # expect >= 2
grep -c "APPLICATION DOCUMENTS (on-demand capability)" SYSTEM-PROMPT.md  # expect 1
grep -c "Application Pipeline" SYSTEM-PROMPT.md           # expect 1
```
Expected: counts `2` (or more), `1`, `1`.

- [ ] **Step 5: Commit** (after Task 0 preamble)

```bash
git add SYSTEM-PROMPT.md
git commit -m "Wire application-docs capability into SYSTEM-PROMPT

Adds the consult-when-relevant route, the on-demand capability section,
and the Sunday deadline -> work-block rule."
```

---

## Task 9: Update `file-index.md`

**Files:**
- Modify: `file-index.md` (add an Applications section)

- [ ] **Step 1: Append a new top-level section** to `file-index.md`, before the closing
  `## Delivery note` section (or at end if simpler):

```markdown
## 6. Application documents (resume / cover letter system)

On-demand capability folded in 2026-06-13. Workflow:
`context/applications/application-docs-workflow.md`.

| Path | Tier | Purpose |
|------|------|---------|
| `context/applications/application-docs-workflow.md` | instructions | How to produce tailored resumes/cover letters end-to-end. |
| `context/applications/resume-template.tex` | template | Canonical ATS-safe single-column LaTeX template; start every resume here. |
| `context/applications/profile/` | source-of-truth (read these) | Veer's contact, education, experiences (Firmly, SMIF), project (StudyFlowForge), design portfolio (Etsy), leadership (EPICS), skills, role-positioning, reusable bullets, + MEMORY index. |
| `context/applications/research/` | compressed research (read these) | Compressed ResumeDeepResearch + CoverLetterDeepResearch. |
| `files/applications/` | deep research (full) | Full ResumeDeepResearch, CoverLetterDeepResearch, Summer2026_Internship_Research (last read directly, uncompressed). |
| `applications/` | output | Per-company tailored resumes/cover letters (.tex + .pdf), `_master/` master resume, `README.md` inventory. |

Application timing lives in `context/key-dates.md` (Application Pipeline table), not in the
applications/ README.
```

- [ ] **Step 2: Verify**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -n "Application documents (resume / cover letter system)" file-index.md
```
Expected: one match.

- [ ] **Step 3: Commit** (after Task 0 preamble)

```bash
git add file-index.md
git commit -m "Index the application-docs files in file-index"
```

---

## Task 10: Update README, memory, PROGRESS

**Files:**
- Modify: `README.md`, `memory.md`, `PROGRESS.md`

- [ ] **Step 1: Append to `README.md`** a new section (after the existing `## File map`):

```markdown
## Application documents (resume / cover letter)

This project also houses Veer's resume / cover-letter system (folded in 2026-06-13). Ask for
a resume or cover letter for a role and the assistant follows
`context/applications/application-docs-workflow.md`: it reads the profile in
`context/applications/profile/`, drafts from `context/applications/resume-template.tex`, and
writes `.tex` + `.pdf` into `applications/<Company>/`. Application deadlines live in
`context/key-dates.md` (Application Pipeline) and can flow into the Sunday plan.
```

- [ ] **Step 2: Append to `memory.md`** under its current-state content a line noting the
  capability. Read the file first to match its format:

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"; tail -15 memory.md
```
Then add (matching the surrounding format — adapt the heading to whatever section holds
capabilities/tools):

```markdown
- Application-docs capability live (2026-06-13): resume/cover-letter generation folded in. Profile source-of-truth in context/applications/profile/; workflow in context/applications/application-docs-workflow.md; outputs in applications/. Deadlines tracked in context/key-dates.md (Application Pipeline).
```

- [ ] **Step 3: Add a dated entry to `PROGRESS.md`.** Read the latest entry to match its exact
  format (heading style, date format), then prepend/append a new entry consistent with it:

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"; head -40 PROGRESS.md
```
Entry content (reformat to match the file's convention):

```markdown
2026-06-13 — Integrated the resume / cover-letter system into the planning repo. Migrated (copy-only) the profile source-of-truth (12 files) to context/applications/profile/, merged the two instruction docs into context/applications/application-docs-workflow.md, extracted a canonical LaTeX template, brought the deep-research docs into files/applications/ (+ compressed copies of the two large ones in context/applications/research/), and copied all 12 legacy company outputs + master resume into applications/. Wired application deadlines into context/key-dates.md (Application Pipeline) and the Sunday-session rule in SYSTEM-PROMPT. Originals left untouched. Only 2 of 12 legacy companies have .tex sources; the rest are PDF-only, flagged for on-demand regeneration.
```

- [ ] **Step 4: Verify all three updated**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -l "application" README.md memory.md && grep -c "2026-06-13" PROGRESS.md
```
Expected: `README.md` and `memory.md` listed; PROGRESS.md `2026-06-13` count >= 1.

- [ ] **Step 5: Commit** (after Task 0 preamble)

```bash
git add README.md memory.md PROGRESS.md
git commit -m "Document application-docs integration in README, memory, PROGRESS"
```

---

## Task 11: Final integration verification

**Files:** none (read-only checks)

- [ ] **Step 1: Structure + count assertions**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
echo "profile files (expect 11):"; ls context/applications/profile/*.md | wc -l
echo "research compressed (expect 2):"; ls context/applications/research/*.md | wc -l
echo "research full (expect 3):"; ls files/applications/*.md | wc -l
echo "company dirs (expect 12):"; find applications -mindepth 1 -maxdepth 1 -type d ! -name _master | wc -l
echo "master pdf present:"; ls applications/_master/Veer_Sanyal_Resume.pdf
echo "template present:"; ls context/applications/resume-template.tex
echo "workflow present:"; ls context/applications/application-docs-workflow.md
```
Expected: 11, 2, 3, 12, and all three file listings succeed.

- [ ] **Step 2: No old paths leaked into any in-repo doc**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
grep -rn "Internships/" context/applications applications/README.md file-index.md || echo "CLEAN"
```
Expected: `CLEAN` (the only acceptable matches would be inside files/ research originals, which are excluded here).

- [ ] **Step 3: No dangling wikilinks across profile + workflow**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project/context/applications"
targets=$(grep -roh '\[\[[a-z-]*\]\]' . | tr -d '[]' | sort -u)
slugs=$(grep -rh '^name:' profile | sed 's/name: *//' | sort -u)
for t in $targets; do echo "$slugs" | grep -qx "$t" || echo "DANGLING: [[$t]]"; done; echo "link check done"
```
Expected: `link check done` with no `DANGLING:` lines.

- [ ] **Step 4: Originals untouched (copy-only sanity)**

```bash
DL="/Users/veersanyal/Downloads/Internships"
ls "$DL/ApplicationDocuments" >/dev/null && ls "$DL/ResearchContext" >/dev/null && echo "ORIGINALS INTACT"
```
Expected: `ORIGINALS INTACT`.

- [ ] **Step 5: Git log shows the task commits, working tree clean**

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
git status -s    # expect empty
git log --oneline -11
```
Expected: clean working tree; commits from Tasks 2–10 present.

---

## Task 12: Push handoff (requires Veer's authorization)

**Do not run without Veer's explicit OK to push to `master`.**

- [ ] **Step 1: Confirm with Veer**, then push:

```bash
cd "/Users/veersanyal/Desktop/veer-pm-project"
git push origin master
```
Expected: push succeeds; `git log origin/master..HEAD` is empty afterward.

If Veer prefers a PR or a branch instead of pushing to `master`, create a branch from these
commits and push that instead.

---

## Self-review notes (author)

- **Spec coverage:** profile migration (T2), merged workflow (T3), template (T4), research
  two-tier + compression (T5), outputs + inventory (T6), deadline wiring (T7), SYSTEM-PROMPT
  capability + Sunday rule (T8), file-index (T9), README/memory/PROGRESS (T10), verification
  incl. dangling-link + compile + copy-only checks (T4 compile, T11) — all spec sections map
  to a task.
- **PDF-only legacy:** handled in T6 inventory; never fabricated (spec out-of-scope honored).
- **Copy-only:** every source op is `cp`/`rsync` from read-only source paths; T11 Step 4
  asserts originals intact; no `rm`/`mv` touches sources.
- **Push safety:** isolated to T12 behind explicit authorization; all earlier tasks commit
  locally only; Task 0 preamble guards repo identity before each commit.
