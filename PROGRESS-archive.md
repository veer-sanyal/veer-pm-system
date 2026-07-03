# Veer Progress Log — Archive

Closed-month/older dated entries rolled out of `PROGRESS.md` to keep the per-session tail read small (see the archive rule in PROGRESS.md). Chronological; nothing is ever deleted. PRIVATE.

---

## Week 1 (May 18-24, 2026) — Foundation

### 2026-05-18 (Mon)
System setup day. about-me, direction, scheduling-blueprint, daily-email-instructions, key-dates, research files all locked in. No project work yet.

### 2026-05-19 (Tue)
Pillar 1:
- Option B committed (India MSME digital services trade exposure) over Option C (WTO e-commerce moratorium visualizer)
- WTO Digitally Delivered Services dataset downloaded
- First pivot table + chart built locally
- DECISIONS.md started (Entry 001: scope decision)

### 2026-05-20 (Wed)
Pillar 1:
- WTO TiSMoS downloaded
- Stack chosen (at the time): Streamlit + Python + pandas + Plotly, deploy via Streamlit Community Cloud
- GitHub repo set up: github.com/veer-sanyal/india-msme-digital-trade-exposure (public)
- v0 scaffolding deployed; Overview wired with the DDS trend and category breakdown
- DECISIONS.md Entries 002 (stack), 003 (deploy empty before features), 004 (data-pipeline shape + EBOPS-ISIC crosswalk find)

### 2026-05-21 (Thu)
Pillar 1:
- Overview charts given narrative framing with live-computed figures (no hardcoded numbers)
- DECISIONS.md Entry 005 (citation/computed-figure policy) and Entry 006 (MSME data sourcing — MoMSME has no NIC-2-digit by size cross-tab; aggregate Udyam Bulletin VII top-50 NIC-5-digit up to ISIC section; BaTIS deferred)

### 2026-05-22 (Fri)
Pillar 1:
- Service Categories page built from the actual TiSMoS data; app converted to multipage
- Mode 1 / All-modes toggle added to the diverging category chart; chart redundancy, Transport caveat, palette, and titles cleaned up
- Two pages live: Overview + Service Categories
- Note: ahead of roadmap by ~3-4 days (Fri target "loads and shows one chart" already cleared)

### 2026-05-23 (Sat)
No work logged.

### 2026-05-24 (Sun)
First Sunday session. Set up this progress log and the two-log split:
- `DECISIONS.md` = curated product decisions only
- This file = everything else (daily work, pillars 2-4, system signals, external conversations)
- Claude reads both at the start of every chat, plus GitHub commits since the last entry
Sunday session held at 4:00 PM.

---

## Week 2 (May 25-31, 2026) — Exposure index + architecture pivot

### 2026-05-27 (Wed)
Pillar 1:
- Built Act III (MSME Base) and Act IV (Exposure Index v0) pages — the MSME crosswalk that gives the dashboard product value beyond a trade visualizer
- Exposure score v0 = two min-max-normalised components (MSME scale in the mapped ISIC section(s) + Mode 1 trade in USD bn), summed. v0 scores: Other business services 2.00, Transport 1.37
- DECISIONS.md Entry 007 (drop ICRIER 2025 as a source after reading its methodology) and Entry 008 (exposure-score methodology + the open question framed for Dr. G; two components, not three — digital-adoption component deferred pending a verified ASUSE 2023-24 substitute; policy-sensitivity component waits on OECD Digital STRI)

### 2026-05-31 (Sun)
Pillar 1:
- Major architecture pivot: replaced the Streamlit multipage app with a single static "Guided Walkthrough" site — one top-to-bottom scroll narrative (question -> concepts -> four data "Acts" -> scope, findings, roadmap, provenance). Static HTML + CSS + client-side Plotly on a small design system (IBM Plex; warm paper / cool ink; indigo + clay). No server runtime; Python (pandas) now only builds the processed CSVs and `site/data.js`
- DECISIONS.md Entry 009 (Streamlit -> static; figures stay computed from source via `build_site_data.py` so the scatter, ranked bar, and score table cannot disagree). The build also caught a hardcoded mock figure: IP-licensing fees "~10x since 2005" was wrong — computing from `dds_india.csv` gives 29.4x, to $19.8B in 2025
- Inferred Sunday session (major structural decision day; fits the Sunday cadence)

---

## Week 3 (June 1-7, 2026) — Disaggregation + external send

### 2026-06-01 (Mon)
Pillar 1:
- Disaggregated "Other business services" (EBOPS `SJXSJ34` -> ISIC sections L+M+N) into sub-sector exposure in Act IV. Administrative/support + professional/scientific activities (management consultancy, accounting, legal, architecture and engineering, advertising) supply most of the firms; real estate the least. Ranking read as direction, not calibrated magnitude, because part of that firm count is domestically oriented activity that does not cross a border digitally
- DECISIONS.md Entry 010 (constructed sub-code disaggregation of Other business services)

### 2026-06-02 (Tue)
Pillar 1:
- Redesigned the disaggregation section per a design handoff; surfaced the consulting-boom finding. DECISIONS.md Entry 011
- De-identified the repo and prepped it for external send
Pillar 3 / External:
- Substantive follow-up to Dr. G sent — live guided-walkthrough site link + de-identified repo + the exposure-score methodology question. Status: awaiting reply

### 2026-06-04 (Thu)
System:
- Overhauled the cowork project system itself: rewrote the conversation prompt (tiered reading + auto-consult research triggers so research is read when relevant, not only on request), restructured `memory.md` to current-state-only, canonicalised the research docs into a docs-summary / files-original two-tier, archived the retired "Purdue" project, and moved this progress log into the repo as `PROGRESS.md` (self-updating from here)

---
