> This file holds CURRENT STATE only — what's shipped, the active focus, and next moves.
> Strategy (goal, four pillars, targets, decision rules) lives in `direction.md`.
> The full day-by-day narrative lives in `PROGRESS.md` (project root).
> Last refreshed 2026-06-13. Sanity-check against the live site and latest GitHub commits before trusting — this file has drifted before.

**Current state**

- Live site (ground truth for what's shipped): **https://veer-sanyal.github.io/india-msme-digital-trade-exposure/** — a single-scroll **static "Guided Walkthrough"** on GitHub Pages. As of 2026-06-01 the project **migrated off Streamlit** (DECISIONS Entry 009); there is no server runtime.
- Structure is four data "Acts":
  - **Act I — Overview** (WTO Digitally Delivered Services): is the digital-services trade real and growing?
  - **Act II — Service Categories** (WTO TiSMoS): where it concentrates; Mode 1 vs all-modes.
  - **Act III — MSME Base** (MoMSME Udyam Bulletin VII + Annual Report 2024-25): how many small firms per industry.
  - **Act IV — Exposure Index**: which sectors are most exposed (the MSME crosswalk — the differentiating insight).
- **Exposure score v0 is built and live.** Formula = two min-max-normalised components (MSME scale in the mapped ISIC section(s) + Mode 1 trade in USD bn), summed. v0 scores: Other business services 2.00, Transport 1.37. "Other business services" is further **disaggregated** into sub-sector exposure (consulting/accounting/legal/architecture/advertising supply most firms). Read as direction, not calibrated magnitude.
- **Dr. G (Infisum) follow-up: sent 2026-06-02 — awaiting reply.** Went out with the live site link + de-identified repo + the exposure-score methodology question (Entry 008).
- `DECISIONS.md` is current through **Entry 011**. The exposure-score methodology is logged (Entry 008) — not an open item.
- **Application-docs capability folded in (2026-06-13):** resume/cover-letter generation now lives in this repo. Profile source-of-truth in `context/applications/profile/`, workflow in `context/applications/application-docs-workflow.md`, outputs in `applications/` (12 legacy companies migrated, copy-only). Deadlines tracked in `context/key-dates.md` (Application Pipeline).

---

**Next moves**

- **Resolve the deferred exposure-score components:** the 3rd (digital adoption) is deferred pending a verified ASUSE 2023-24 substitute after ICRIER 2025 was ruled out (Entry 007/008); the 4th (policy sensitivity) waits on OECD Digital STRI (~Week 4).
- **Pillars 2 and 3 are now on** (week of Jun 8): metrics + statistics fluency leads Pillar 2 (Khan Academy + Amplitude Academy), not SQL (demoted per the 2026-06-04 realignment). Pillar 3 state as of 2026-06-09: LinkedIn profile finished (headline/About/Projects/Featured all carry the live dashboard), `alumni-tracker.md` (planning repo root) holds a 10-name verified shortlist + bench, warmest leads Daniel Anicito and Steven LaCroix (2nd-degree with mutuals). Sequence: Veer finalizes the first LinkedIn post (drafted, in his hands; charts in `files/linkedin/`), then 3 alumni messages/week start.
- Google APM application prep over the coming months (close estimated **early-to-mid October 2026**).
- Handle Dr. G's reply when it lands (respond on methodology; if silent past the window, a brief nudge).

---

**Operating principles** (durable — how to work with Veer and this project)

- The **deployed GitHub Pages site is ground truth** for what's shipped — not the README, and no longer Streamlit.
- **`PROGRESS.md` (project root) is the everything-log**; `DECISIONS.md` (repo) is curated product decisions only; `memory.md` is the current-state snapshot. Keep all three current — see the self-updating protocol in the project prompt.
- **Check live artifacts and prior context BEFORE planning, not after** — Veer caught Claude generating plans on stale roadmap assumptions; this file itself drifted (still said "Streamlit") until reconciled against commits on 2026-06-04.
- When Veer proposes system improvements, distinguish genuine improvements from avoidance patterns and name the real problem being solved.
- Communication: **direct and short**; accepts pushback when grounded, but expects flaws flagged before building, with concrete alternatives and honest trade-offs.

---

**Tools & resources**

- **GitHub repo**: `veer-sanyal/india-msme-digital-trade-exposure` (public)
- **Live site**: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/ (GitHub Pages, published from `site/`)
- **Progress log**: `PROGRESS.md` at the project root (private; not in the public repo)
- **Stack**: static HTML + CSS + client-side Plotly on a small design system (IBM Plex; warm paper / cool ink; indigo + clay). Python (pandas) only builds the processed CSVs and `site/data.js` — `scripts/build_processed.py`, `build_msme_nic.py`, `build_site_data.py`.
- **Data sources**: WTO DDS, WTO TiSMoS, MoMSME Udyam Bulletin VII + Annual Report 2024-25, EBOPS-ISIC crosswalk. Raw files processed in Python for reproducibility.
- **Web-fetch limitations**: GitHub repo pages not always reliably fetchable — pasting file contents directly is more reliable than URL fetches.
