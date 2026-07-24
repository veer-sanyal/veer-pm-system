# Applications — output tier

Generated tailored resumes and cover letters, one folder per company. This is a **file
inventory only** — application deadlines and pipeline status live in
`../context/key-dates.md` (Application Pipeline table). The generation workflow is
`../context/applications/application-docs-workflow.md`.

- `_master/Veer_Sanyal_Resume.pdf` — master resume, full experience inventory.
- Legacy folders were migrated 2026-06-13 (copy-only) from
  `~/Downloads/Internships/ApplicationDocuments`. Most are PDF-only — their `.tex` source was
  not retained and will NOT be fabricated; regenerate a source on demand from the profile +
  `resume-template.tex` when an edit is needed.

| Company / Job | Files present | Editable .tex? |
|---|---|---|
| Claude Corps (ACTIVE) | VeerSanyal_ClaudeCorps_Resume.tex + .pdf, Claude-Corps-Application.md (essays + form answer key) | Yes |
| Trice (ACTIVE — warm intro) | VeerSanyal_Trice_Resume.tex + .pdf | Yes |
| Cisco | VeerSanyal_Cisco_Resume.pdf | No — regenerate on demand |
| Databricks (ACTIVE — PM Intern Summer 2027) | VeerSanyal_Databricks_Resume.tex + .pdf | Yes |
| Salesforce (ACTIVE — Summer 2027 APM Intern, JR348039) | VeerSanyal_Salesforce_Resume.tex + .pdf | Yes |
| Cloudflare | VeerSanyal_Cloudflare_Resume.pdf | No — regenerate on demand |
| Daniels Externship | Daniels_Externship_Resume.pdf, Daniels_Externship_Cover_Letter.pdf | No — regenerate on demand |
| Handshake AI - 2D 3D Digital Media | VeerSanyal_HandshakeAI_DigitalMedia_Resume.tex + .pdf | Yes |
| Handshake AI - Finance Expert | VeerSanyal_HandshakeAI_Resume.tex, VeerSanyal_Resume.pdf | Yes |
| Paccar | VeerSanyalResume.pdf, VeerSanyalPaccarCoverLetter.pdf | No — regenerate on demand |
| Samsung PM | VeerSanyalResume.pdf | No — regenerate on demand |
| Samsung Profit Management | VeerSanyalResume.pdf | No — regenerate on demand |
| SAP | VeerSanyalResume.pdf, VeerSanyalCoverLetter.pdf | No — regenerate on demand |
| SpaceX | Veer_Sanyal_Resume.pdf, Veer_Sanyal_Cover_Letter.pdf | No — regenerate on demand |
| Tesla | Veer_Sanyal_Resume.pdf | No — regenerate on demand |
| Tiktok (legacy) | VeerSanyalResume.pdf | No — regenerate on demand |
| Tiktok - Category Mgmt Intern (ACTIVE) | VeerSanyal_TikTok_CategoryMgmt_Resume.tex + .pdf | Yes |

New applications: create `applications/<Company>/`, save `.tex` + `.pdf` (see workflow), and
add a row here. For consistency, prefer the `VeerSanyal_<Company>_Resume.{tex,pdf}` naming on
new docs even though legacy filenames vary.
