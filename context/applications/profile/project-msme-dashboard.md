---
name: user-project-msme-dashboard
description: "India MSME Digital-Trade Exposure Dashboard — Veer's flagship shipped product (Pillar 1), May 2026–Present. Solo, end-to-end, live, instrumented, iterated for a real policy-research user. Use as lead project for PM, product, data, AI, and India/commerce/civic-domain roles."
metadata:
  node_type: memory
  type: user
  originSessionId: trice-session
---

**India MSME Digital-Trade Exposure Dashboard** — Independent product build — May 2026 – Present
*Subtitles used: "Digital-Trade Exposure Dashboard", "Solo build; live for a policy-research user"*

The flagship Pillar-1 artifact: a real product, real user, real instrumentation, real iteration. This is the strongest "I shipped something" story Veer has and should usually lead PM/product resumes. Product repo: `github.com/veer-sanyal/india-msme-digital-trade-exposure` (public); live on GitHub Pages.

**Stack:** Static HTML/CSS + client-side Plotly (no server runtime). Python/pandas builds the processed data + `site/data.js`. Tools: Git/GitHub, GoatCounter telemetry, Claude Code (AI-assisted dev).

**Role:** Sole builder — problem definition → data pipeline → shipped UI → telemetry → iteration. Intended user is a trade economist / policy researcher (Dr. Gopalakrishnan, GTAP/Purdue/NCAER) who repeatedly needs to flag which India MSME service sub-sectors are most exposed to a given digital-trade policy.

**Key facts (all defensible — never inflate):**
- Live single-scroll "Guided Walkthrough" site; migrated off Streamlit to a static build 2026-06-01.
- Exposure index = transparent, labeled proxies (MSME scale in the mapped ISIC section(s) + Mode 1 digitally-delivered trade), every score linked to source; read as direction, not calibrated magnitude.
- Data: WTO Digitally Delivered Services, WTO TiSMoS, India MoMSME Udyam Bulletin + Annual Report 2024-25, EBOPS–ISIC crosswalk.
- Central credibility caveat (EBOPS→NIC/ISIC crosswalk is a modeled assumption, not a measured join) surfaced *in the UI*, not buried.
- Instrumented with GoatCounter usage telemetry + five named custom events (per-Act views, a chart toggle, score-table interaction, expander opens, outbound link clicks).
- Public decision log (`DECISIONS.md`, 13+ entries with explicit trade-offs).
- "Compute every figure from source" build rule caught a published/placeholder figure off by ~3x (IP-licensing growth: corrected to a computed ~29.4x).

**Headline accomplishments (proof bullets):**
- Built and shipped a live tool that flags which of India's small businesses (MSMEs) are most exposed to digital-trade policy, so a researcher grounds the call in data rather than guesswork; scoped and iterated end-to-end over 8+ weeks against a public decision log.
- Constructed a transparent exposure index from public WTO + Indian government (MoMSME Udyam) data, every proxy labeled and linked to source; surfaced the central modeled-assumption caveat directly in the interface rather than burying it.
- Instrumented the live site with usage telemetry (custom event tracking) to measure real usage; computed every figure from source data instead of hardcoding (caught a published statistic off by ~3x). Built with AI-assisted development (Claude Code).

**Skills demonstrated:** Product scoping, data pipeline (Python/pandas), data visualization (Plotly), telemetry instrumentation, transparent methodology + assumption-labeling, decision logging, iterating on a real user's problem, India MSME / digital-commerce domain.

**Tailoring notes:**
- PM/product: lead with problem→ship→measure→iterate + the public decision log + telemetry. This is the cleanest "shipped, measured usage, changed it" narrative.
- India / commerce / small-business / civic-domain roles (e.g. Trice): lead — the MSME/digital-commerce domain fit is the differentiator.
- Data/analytics: lead with the index construction, source-linked proxies, and computed-from-source discipline.
- AI roles: mention Claude Code AI-assisted build + the verify-everything discipline.
- Honest framing: it is a screening heuristic with a stated modeled-assumption limitation, not a calibrated measurement — say so; the honesty is a strength in interviews.
