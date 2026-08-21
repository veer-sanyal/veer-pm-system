---
description: Build a tailored resume / cover letter for a role
argument-hint: <company / role / posting link>
---

# /apply $ARGUMENTS

Follow `context/applications/application-docs-workflow.md` end to end. The short version (the workflow doc is authoritative):

- Read `context/applications/profile/` (ordered per `profile/role-positioning.md`) and `context/applications/research/ResumeDeepResearch.md` BEFORE any old PDF. Read `CoverLetterDeepResearch.md` only when a cover letter is requested.
- Produce BOTH a `.tex` (from `context/applications/resume-template.tex`) and a compiled `.pdf` into `applications/<Company>/`.
- Never invent metrics. One page.
- Save the posting verbatim to `applications/<Company>/listing.md` and the requirement->proof
  table to `match-map.md` in the same folder.
- After compiling: `tools/resume-check.sh <file.tex>` must print clean, then spawn the
  FRESH-context reviewer subagent (workflow step 5) and apply or explicitly waive its
  findings. This applies to edits of existing deliverables too.
- Afterward: fold any new metric/bullet/skill back into `context/applications/profile/*.md`, update `applications/README.md`, and if the listing has a deadline add/update its row in the `context/key-dates.md` Application Pipeline (timing lives there, not in the README).
