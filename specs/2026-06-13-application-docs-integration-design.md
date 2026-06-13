# Application-Docs Integration — Design Spec

Date: 2026-06-13
Status: Approved for implementation (pending spec review)
Owner: Veer

## Goal

Fold Veer's previously separate resume / cover-letter generation system into the
`veer-pm-project` planning repo so everything lives in one place, organized along the
project's existing three-tier convention. The resume system is currently scattered across
three locations:

1. **Profile data** — 12 structured memory files (contact, education, experiences, project,
   design portfolio, leadership, skills, role-positioning, reusable bullets, workflow
   prefs) living in a Claude app session space:
   `~/Library/Application Support/Claude/local-agent-mode-sessions/.../spaces/.../memory/`.
2. **Generation instructions** — `PROJECT_INSTRUCTIONS.md`
   (`~/Documents/Claude/Projects/Internship Resume/Coverletter/`) plus the overlapping
   `feedback_resume_workflow.md` (in the memory space above).
3. **Outputs + research** — per-company `.tex`/`.pdf` in
   `~/Downloads/Internships/ApplicationDocuments/<Company>/` (12 companies, 16 PDFs but only
   2 `.tex`), the master resume `~/Downloads/Internships/Veer_Sanyal_Resume.pdf`, and three
   deep-research docs in `~/Downloads/Internships/ResearchContext/`.

After integration, the planning assistant gains an on-demand capability: given a job
listing, produce a tailored single-page resume (LaTeX + PDF), and a matching cover letter
on request, reading from in-repo profile data and writing into an in-repo output tree —
with application deadlines wired into the existing key-dates + Sunday planning flow.

## Scope decisions (confirmed with Veer)

- **Repo scope: everything in one tree.** Profile, instructions, research, AND all
  per-company outputs (`.tex` + `.pdf`) live inside the repo and are version-controlled.
- **Migration is copy-only.** Originals in Downloads / Documents / the Library app space are
  left untouched. No deletion, no move.
- **Workflow surface: on-demand capability + deadline wiring.** A dedicated workflow doc
  referenced from `SYSTEM-PROMPT.md`; plus an Application Pipeline table in `key-dates.md`
  that the Sunday session can turn into work blocks. The existing Sunday / mid-week modes
  are otherwise unchanged.
- **Compression: selective.** The two ~40 KB best-practices research docs
  (`ResumeDeepResearch`, `CoverLetterDeepResearch`) get compressed `context/` copies (read
  these) with full originals in `files/`. `Summer2026_Internship_Research.md` (8.8 KB) stays
  uncompressed and is read directly, matching the project's existing "not-yet-compressed,
  read directly" precedent.

## Environment facts (verified 2026-06-13)

- LaTeX is installed: `pdflatex` and `latexmk` at `/Library/TeX/texbin/`. The repo can
  render PDFs from source.
- PM repo remote is `github.com/veer-sanyal/veer-pm-system.git` (private). Commits per the
  SYSTEM-PROMPT convention are safe and correctly scoped.
- Only 2 of 16 past PDFs have `.tex` sources (Handshake AI ×2). The rest are PDF-only;
  sources were not retained and will **not** be fabricated.
- A canonical LaTeX template is embedded in the existing `.tex`: `10pt letterpaper`,
  `0.6in` L/R + `0.55in` T/B margins, ATS-safe single column, `titlesec` section rule, an
  `\entry{Title}{Location}{Subtitle}{Dates}` helper, in-body header (not PDF header/footer)
  for ATS parsing. This is extracted into a reusable template.
- `~/Downloads/Internships/README.md` is about an unrelated "Options Trading Platform" — it
  is **not** part of the resume system and is **not** migrated.

## Target structure in `veer-pm-project`

```
veer-pm-project/
├── SYSTEM-PROMPT.md     (EDIT)
├── README.md            (EDIT)
├── memory.md            (EDIT)
├── PROGRESS.md          (EDIT)
├── file-index.md        (EDIT)
├── context/
│   ├── key-dates.md      (EDIT: + Application Pipeline table)
│   └── applications/
│       ├── application-docs-workflow.md   (NEW: merged + path-rewritten instructions)
│       ├── resume-template.tex            (NEW: canonical LaTeX template)
│       ├── profile/                       (NEW: 12 source-of-truth files)
│       │   ├── MEMORY.md
│       │   ├── contact.md
│       │   ├── education.md
│       │   ├── experience-firmly.md
│       │   ├── experience-smif.md
│       │   ├── project-studyflowforge.md
│       │   ├── experience-etsy-design.md
│       │   ├── leadership-epics.md
│       │   ├── skills-inventory.md
│       │   ├── role-positioning.md
│       │   └── reusable-bullets.md
│       └── research/                      (NEW: compressed working copies)
│           ├── ResumeDeepResearch.md
│           └── CoverLetterDeepResearch.md
├── files/
│   └── applications/                      (NEW: deep-research originals, read on demand)
│       ├── ResumeDeepResearch.md
│       ├── CoverLetterDeepResearch.md
│       └── Summer2026_Internship_Research.md
└── applications/                          (NEW: output tier)
    ├── README.md          (artifact inventory: company → has .tex? → status)
    ├── _master/
    │   └── Veer_Sanyal_Resume.pdf
    ├── Cloudflare/
    ├── Tesla/
    ├── SAP/
    ├── Cisco/
    ├── SpaceX/
    ├── Tiktok/
    ├── Samsung PM/
    ├── Samsung Profit Management/
    ├── Paccar/
    ├── Handshake AI - Finance Expert/
    ├── Handshake AI - 2D 3D Digital Media/
    └── Daniels Externship/
```

Note: the `feedback_resume_workflow.md` content is **workflow**, not profile, so it is folded
into `application-docs-workflow.md` rather than copied into `profile/`.

## Component design

### 1. Profile data → `context/applications/profile/`

These are canonical, read-at-task-time reference (peer to `context/about-me.md`), so they
belong in the `context/` tier. The 10 content files plus a `MEMORY.md` index are copied with
the `user_` filename prefix dropped (cleaner under a `profile/` dir).

- Filenames change: `user_contact.md` → `contact.md`, `user_experience_firmly.md` →
  `experience-firmly.md`, etc.
- The `name:` frontmatter slug in each file (e.g. `user-contact`) is **kept as-is** so it
  stays a stable identifier, but every `[[wikilink]]` body reference is audited so it still
  resolves to an existing slug. (Current cross-refs in scope:
  `user_experience_etsy_design.md` → `[[user-skills-inventory]]`;
  `user_skills_inventory.md` → `[[user-experience-etsy-design]]`;
  `feedback_resume_workflow.md` → the nine `[[user-*]]` read-list links, which move into the
  workflow doc.) No dangling links after migration.
- `MEMORY.md` index links are rewritten to the new relative filenames.

### 2. Workflow → `context/applications/application-docs-workflow.md`

A single merged doc reconciling `PROJECT_INSTRUCTIONS.md` and `feedback_resume_workflow.md`
(they overlap heavily and agree). All paths are rewritten from the old scattered locations to
in-repo paths:

| Old reference | New reference |
|---|---|
| `Internships/ResearchContext/ResumeDeepResearch.md` | `context/applications/research/ResumeDeepResearch.md` (full: `files/applications/...`) |
| `Internships/ResearchContext/CoverLetterDeepResearch.md` | `context/applications/research/CoverLetterDeepResearch.md` |
| `Internships/ResearchContext/Summer2026_Internship_Research.md` | `files/applications/Summer2026_Internship_Research.md` |
| `Internships/Veer_Sanyal_Resume.pdf` (master) | `applications/_master/Veer_Sanyal_Resume.pdf` |
| `Internships/ApplicationDocuments/<Company>/` | `applications/<Company>/` |
| memory `[[user-contact]]` … | `context/applications/profile/contact.md` … |

The doc preserves the original rules verbatim in spirit: 1-page hard cap; ATS-safe
single-column; CAR/PAR bullets; mirror JD vocabulary; reorder so strongest proof is in the
top third; never invent metrics; produce both `.tex` and `.pdf` for every deliverable; read
profile before old PDFs; read the cover-letter research doc only when a cover letter is
requested; update profile memory after each build; concise/no-preamble comms. It also adds:
use `resume-template.tex` as the starting preamble; compile with `pdflatex`/`latexmk`; verify
single page before saving.

### 3. Research → two tiers

- Full originals → `files/applications/` (all three docs).
- Compressed working copies → `context/applications/research/` for the two large
  best-practices docs only. Compression preserves every fact, number, date, and citation per
  the project convention. `Summer2026_Internship_Research.md` is read directly from `files/`.

### 4. Outputs → `applications/`

- `_master/Veer_Sanyal_Resume.pdf` — the full experience inventory.
- One folder per company, contents copied as-is (folder names kept as in the source, e.g.
  `Samsung PM`, `Samsung Profit Management`, `Handshake AI - 2D 3D Digital Media`).
- `applications/README.md` is an artifact inventory: a table of `Company | Role (if known) |
  Files present | Has editable .tex? | Notes`. PDF-only companies are flagged "PDF-only —
  source not retained; regenerate `.tex` on demand." It deliberately holds **no deadline
  data** (that lives in `key-dates.md`) to avoid two-source drift.

### 5. Deadline wiring (recommended shape)

Minimal by design — one table and one rule, not a tracker subsystem:

- **`context/key-dates.md`** gains an **Application Pipeline** section: a table with
  `Company / Role | Deadline (absolute date) | Stage | Docs →`, where Stage ∈
  {Researching, Drafting, Ready, Submitted} and "Docs →" points at `applications/<Company>/`.
  This is the single source of truth for application timing. Seeded empty (or with any known
  current targets) since the migrated outputs are historical.
- **`SYSTEM-PROMPT.md`** gains a Sunday-session rule: any pipeline deadline within ~2 weeks
  still at Stage < Ready is a candidate "draft `<Company>` resume" work block for the week;
  if the Calendar connector is on, optionally write one deadline event per open application.
  Markdown stays the source of truth; the calendar is a delivery surface.

### 6. Wiring into existing system files

- **`SYSTEM-PROMPT.md`**:
  - Add to the "CONSULT WHEN RELEVANT" list: *Resume / cover letter / application doc
    request → `context/applications/application-docs-workflow.md` (+ `profile/` + `research/`)*.
  - Add a short "APPLICATION DOCUMENTS (on-demand capability)" paragraph summarizing the
    workflow and the profile-memory-update obligation after each build.
  - Add the Sunday deadline rule above.
- **`file-index.md`**: add a new "Applications" section documenting every new file/folder and
  which tier it sits in.
- **`README.md`**: one paragraph noting the project now also houses the application-docs
  system, with a pointer to the workflow doc.
- **`memory.md`**: note the new capability under current state.
- **`PROGRESS.md`**: a dated 2026-06-13 entry recording the integration.

## Data flow (resume request, post-integration)

1. Veer gives a listing (URL / text / company name).
2. Assistant reads `context/applications/application-docs-workflow.md`, then the relevant
   `profile/` files (ordered by `role-positioning.md`), then
   `context/applications/research/ResumeDeepResearch.md` (compressed). Cover letter requested
   → also read `…/CoverLetterDeepResearch.md`.
3. Match-map JD requirements → strongest proof from profile + reusable bullets.
4. Draft `.tex` from `resume-template.tex` → compile with `pdflatex`/`latexmk` → verify 1
   page → write `.tex` + `.pdf` into `applications/<Company>/`.
5. Update `applications/README.md` inventory; if the listing has a deadline, add/update the
   row in `key-dates.md`.
6. Update any new metric/bullet/skill into the relevant `profile/` file.
7. Commit + push per the SYSTEM-PROMPT convention.

## Error handling / edge cases

- **PDF-only legacy companies:** migrated as-is, flagged in the inventory; `.tex` regenerated
  only on explicit request, never fabricated from the PDF.
- **Wikilink integrity:** every `[[...]]` is audited post-rename; build fails loud if a link
  dangles (checked in implementation verification, see below).
- **Compression fidelity:** compressed research copies are diffed against originals for every
  number/citation before the originals are relied upon.
- **Repo-scope safety:** all git operations run from inside `veer-pm-project`; never from the
  home dir (a different, unrelated repo).
- **Unrelated content:** the Options-Trading `README.md` and any non-resume files in
  `Downloads/Internships` are excluded from migration.

## Verification (definition of done)

- All 12 company folders + `_master` present under `applications/`; file counts match source.
- All 10 profile files + `MEMORY.md` present under `context/applications/profile/`; no `user_`
  prefix; `grep` for `[[` finds only links whose target slug exists.
- `application-docs-workflow.md` contains no surviving `Internships/...` path.
- Compressed research copies exist for the two large docs; full originals in `files/`.
- `key-dates.md` has the Application Pipeline table; `SYSTEM-PROMPT.md`, `file-index.md`,
  `README.md`, `memory.md`, `PROGRESS.md` updated.
- A smoke test: compile `resume-template.tex` (with a minimal body) via `pdflatex` to confirm
  the template builds on this machine.
- Changes committed and pushed to `origin master`.

## Out of scope

- Deleting or moving any original source files (copy-only by decision).
- Regenerating `.tex` for the 14 PDF-only legacy companies (on-demand later).
- Building any new tailored resume as part of this integration (this is plumbing only).
- Touching the Library app-session memory space (app-managed).
- Auto-scraping deadlines or any calendar automation beyond the documented Sunday rule.
