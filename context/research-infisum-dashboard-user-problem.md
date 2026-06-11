> Compressed 2026-06-10 from `docs/research-infisum-dashboard-user-problem.md` (kept for reference).

# Research: "Digital Trade Exposure Index" Dashboard — India MSME Sector

**Purpose:** Identify the narrowest, most defensible user + problem for a PM portfolio project joining India's digitally-delivered services trade data with MSME sector data into a "digital trade exposure index."
**For:** Purdue undergraduate builder; mentorship follow-up with Dr. Badri Narayanan Gopalakrishnan (GTAP/Purdue advisory board; NCAER; editor, forthcoming *Digital Trade Across Borders: WTO and the SMEs*). **Date:** 2026-06-04

---

## Executive Summary

**Do not build a broad "exposure index for all Indian small business."** Udyam is granular by sector/district but says nothing about digital posture; WTO/OECD digitally-delivered-services data is economy-level only. No public dataset joins "which Indian MSME sector" to "how much it trades digitally" — claiming that join is fabricating granularity.

**Recommended anchor:** A **policy-research analyst at a think tank (ICRIER / NCAER / Pahle India) — specifically the mentor's team** — whose recurring decision is: *"Which MSME-heavy sectors are most exposed to a specific digital-trade policy change (WTO e-commerce moratorium, data-localization rules, platform-fee shift), so we know where to commission the next deep-dive or write the next brief?"*

**v1 product:** Sector-screening dashboard scoring ~20–30 sub-sectors on (i) digital-trade intensity (WTO/OECD EBOPS data), (ii) platform/e-commerce dependence (ICRIER survey aggregates), (iii) policy sensitivity (OECD Digital STRI + moratorium logic). A **prioritization heuristic for analysts**, not a firm-level index.

Confidence: data findings **high**; "single best user" **moderate** (opinionated by design).

---

## (a) Potential Users and Decisions

| User | Specific decision | Fit with available data |
|---|---|---|
| **Policy-research analyst — think tank (ICRIER, NCAER, Pahle India, RIS)** | Prioritize sectors for next brief / deep-dive / survey wave. | **Best.** Sector altitude, tolerates explicit proxies ([ICRIER MSME survey](https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/)). |
| **Trade-policy submission author (WTO delegation / think-tankers feeding DGFT)** | Which sectors to cite in MC14 moratorium submission ([Business Standard](https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html)). | Good for policy framing; weak on quantified firm impact. |
| **Export Promotion Council / FIEO / FISME analyst** | Which sub-sectors to target with e-commerce-export capacity-building ([FIEO](https://fieo.org/en/); [FISME](https://fisme.org.in/)). | Good intent fit; needs district/cluster granularity the data lacks. |
| **DGFT / "Districts as Export Hubs" program officer** | Which districts/sectors get the next Amazon/Shiprocket/DHL MoU — 75+ districts already ([Amazon press](https://press.aboutamazon.com/in/2023/11/amazon-and-dgft-sign-mou-to-leverage-districts-as-export-hubs-initiative-and-boost-msme-exports-from-india); [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1979068)). | Decision real; requires district × product granularity the data cannot reach. |
| **MSME advisory / consulting firm (Deloitte/CMR-style)** | Which client segments to pitch digital-export readiness services to ([Deloitte](https://www.business-standard.com/industry/news/structural-issues-hit-msme-productivity-digital-readiness-strong-report-125110500711_1.html); [CMR](https://cmrindia.com/67-of-msmes-demonstrate-digital-readiness-across-core-and-advanced-technologies-finds-cmr-study/)). | Commercially fuzzy; weakest single decision. |
| **B2B fintech/SaaS serving MSMEs** | Which sectors are platform-revenue-dependent in risk/credit models ([KNN India](https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey)). | Needs firm-level data a portfolio project cannot access. |
| **MSME Ministry / Udyam policy unit** | Where is digital-trade vulnerability concentrated in the 7.86 crore registration base ([MSME Dashboard](https://dashboard.msme.gov.in/)). | Out of scope for portfolio v1. |

**Takeaway:** Only the **think-tank policy analyst** makes a sector-level decision tolerant of explicit proxies — the only altitude the public data supports.

---

## (b) Comparable Tools and Gaps

| Tool | Coverage | Gap |
|---|---|---|
| **WTO Digitally Delivered Services** ([dataset](https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm); [WTO Data](https://data.wto.org/en/dataset/dideliveredservices); [Hub](https://www.wto.org/english/res_e/statis_e/services_trade_data_hub_e.htm)) | 200+ economies, **8 sub-sectors**, 2005–2025. India 4th-largest exporter, ~US$257bn, +17% ([Manorama](https://www.manoramayearbook.in/current-affairs/india/2024/04/12/digitally-delivered-services.html)). | National-aggregate only; no firm/MSME breakdown. |
| **OECD Digital STRI** ([OECD](https://www.oecd.org/en/topics/sub-issues/services-trade-restrictiveness-index/digital-stri.html); [India note](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/services-trade-restrictiveness-index/oecd-stri-country-note-ind.pdf)) | Regulatory barriers, 129 countries, 5 pillars. India above OECD average; 2024: minor liberalization (courier monopoly end; equalisation-levy removal); data-transfer restrictions remain under 2023 DPDP Act. | Policy environment only; country-level, not MSME-aware. |
| **OECD–WTO BaTIS** ([OECD](https://www.oecd.org/en/publications/the-oecd-wto-balanced-trade-in-services-database-batis_c321a7a7-en.html); [GTAP](https://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=5217)) | 202 economies, **26 EBOPS 2010 categories**, 2005–2023. GTAP-hosted (mentor's domain). | Economy-level; no MSME dimension. |
| **WTO TiSMoS** ([WTO](https://www.wto.org/english/res_e/statis_e/gstdh_mode_supply_e.htm)) | **55 sectors**, 4 GATS modes, 2005–2022; India contributed survey data. | Best sector granularity in the trade-data family; still national. |
| **ICRIER Annual Survey of MSMEs (Phase 3, 2025)** ([report](https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/); [exec PDF](https://icrier.org/pdf/ES_Annual-Survey-MSMEs_India_2025.pdf); [KNN](https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey)) | **2,365 MSMEs, 12 states, 20+ clusters**; e-commerce-integrated firms outperform on turnover, profit, employment, finance; **only ~12% run own e-store** (heavy platform dependence). | Sample survey; firm-level microdata not open or NIC-joinable. Measures goods e-commerce more than digitally-delivered-services trade. |
| **Digital-readiness assessments (Deloitte, CMR, Vi, DAI)** | Firm-level MSME digital adoption snapshots. | "Readiness" not "trade exposure"; vendor-driven. |
| **ECIPE DTRI** ([ECIPE](http://ecipe.org/wp-content/uploads/2018/05/DTRI_FINAL.pdf)) | Academic alternative to OECD Digital STRI. | Same gap: policy index, country-level, not MSME-linked. |

**White space:** No tool combines (digital-trade intensity) × (MSME platform dependence) × (policy sensitivity) at a sector level for India. Each input exists; the join — done honestly, proxies labeled — is the product.

---

## (c) Available Datasets: Granularity and Joinability

| Dataset | Granularity | Joinable at MSME sector level? |
|---|---|---|
| **WTO Digitally Delivered Services** ([WTO](https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm); [sub-sector defs](https://www.wto.org/english/res_e/booksp_e/digital_trade_23_ch4_e.pdf)) | Economy × 8 sub-sectors × year (2005–25), Mode 1. Categories: insurance/pension; financial; charges for IP n.i.e.; telecom-computer-information; other business services; personal/cultural/recreational incl. audiovisual. | No firm/industry split. Joinable only via modeled EBOPS → NIC crosswalk (not a measured link). |
| **OECD Digital STRI** | Country × 5 policy pillars × year. | As policy-sensitivity multiplier only; not sector-specific. |
| **OECD–WTO BaTIS** ([methodology](https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-WTO-Balanced-Trade-in-Services-database-methodology-BPM6.pdf)) | Economy × 26 EBOPS categories × year. | Same crosswalk caveat; better category resolution than the 8-sector file. |
| **WTO TiSMoS** ([methodology](https://www.wto.org/english/res_e/statis_e/daily_update_e/Tismos_methodology.pdf)) | Economy × 55 sectors × 4 modes. | Best sector resolution; still national. |
| **Udyam registration** ([MSME Dashboard](https://dashboard.msme.gov.in/); [data.gov.in](https://www.data.gov.in/catalog/udyam-registration-msme-registration)) | 7.86 crore registrations; state/district × enterprise category × broad activity. Feb-2026 sector split: trading 42.89%, services 36.22%, manufacturing 20.89%. | NIC code collected at registration; clean NIC 2-digit × size × geography not consistently downloadable (data.gov.in granular resource returned 403). |
| **NSS 73rd round (2015–16)** ([microdata](https://microdata.gov.in/NADA/index.php/catalog/139); [KI report](https://www.mospi.gov.in/sites/default/files/publication_reports/NSS_KI_73_2.34.pdf)) | ~63.4m enterprises, open microdata, state + sector detail. | Sector-joinable, open — but **2015–16 and pre-digital-trade**. Use for sector employment/structure weights only. |
| **MoSPI Supply-Use Tables (2022-23/2023-24 base)** ([SUT](https://mospi.gov.in/publication/supply-use-tables); [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150113)) | 155 product groups × 67 industries, NPCSS service-product detail. | Best public bridge between service products and industries; no trade-mode or MSME-size dimension. |

**Where data breaks:**
- No dataset links an Indian MSME's sector to its digitally-delivered-services trade. Any "firm-level exposure index" claim is indefensible.
- EBOPS/TiSMoS → NIC crosswalk is modeling, not measurement; must be labeled as such.
- Udyam NIC 2-digit open access unconfirmed; district × category is reliably public.
- ICRIER microdata not open; only published aggregates available.
- NSS 2015–16 has no digital-trade variables.
- NIC 2025 (introduced Nov-2025) vs NIC 2008 / EBOPS 2010 vintage mismatches require explicit version note.

**Net:** A sector-level screening composite is honest. A firm-level "exposure index" is not.

---

## (d) Recommended Anchor User + Problem

**User:** Policy-research analyst — concretely, **the mentor's team (Dr. Badri Narayanan Gopalakrishnan: GTAP/Purdue, NCAER, forthcoming *Digital Trade Across Borders: WTO and the SMEs*)**.

**Problem:** *"When a digital-trade policy is in play — most timely, the WTO e-commerce moratorium at MC14 — quickly rank India's MSME-relevant service/trade sub-sectors by exposure, to know which 2–3 sectors to commission a deep-dive on or cite in a submission, without rebuilding the data pull each time."*

**v1 product (one screen):** Ranked, filterable sector table/heatmap, ~20–30 sub-sectors, three labeled axes:
1. **Digital-trade intensity** — WTO Digitally Delivered Services + BaTIS/TiSMoS EBOPS categories crosswalked to NIC service divisions (crosswalk shown to user).
2. **MSME platform/e-commerce dependence** — ICRIER survey aggregates (e.g., ~12%-own-e-store finding) + Udyam/NSS sector weights.
3. **Policy sensitivity** — OECD Digital STRI pillars + moratorium-exposure logic, adjustable per scenario.

Each cell links to sources and shows the assumption behind its score; user can change weights and see ranking move.

**Why this user + problem win:**
1. **Data honesty.** Only user whose decision lives at the sector altitude the data supports; all others (DGFT, FIEO, fintech) need district/firm granularity that does not exist publicly.
2. **Real, reachable user.** Mentor publishes in this domain, sits on GTAP's Purdue advisory board ([profile](https://sites.google.com/site/badrinarayanang); [Pahle India](https://pahleindia.org/dt_team/dr-badri-narayanan-gopalakrishnan/)). Genuine discovery interviews possible.
3. **Live policy relevance.** Moratorium fight at MC14 makes sector-exposure a question being asked right now.
4. **Defensible framing.** "Screening heuristic with explicit assumptions" turns the data's biggest weakness (no firm-level join) into a deliberate design choice.
5. **Clean iteration.** v1 = moratorium, static scores. v2 = scenario toggles (DPDP data-localization, platform-fee shifts). v3 = extend toward FIEO/DGFT if district overlay becomes available.

**Do NOT build in v1:** firm-level exposure scores; district-level cuts; any implication WTO data is sector-resolved within India; a general "all MSMEs" claim.

---

## Open Questions / Limitations

- "Single best user": **moderate confidence** — discovery interview with mentor could redirect toward DGFT/FIEO if district overlay becomes feasible.
- **The crosswalk is the credibility risk.** EBOPS → NIC is an analyst assumption; must be surfaced, not buried. First thing a sharp interviewer will probe.
- **ICRIER sector coverage is uneven.** Verify which sectors the survey disaggregates before promising them in the UI. Full PDF tables not extractable programmatically; relied on published summary/exec-summary and press coverage.
- **Udyam NIC-level open access unconfirmed.** Confirm before designing sector weights (data.gov.in returned 403).
- **"Exposure" undefined until policy is named.** Moratorium (cheap digital imports / lost tariff space), data-localization (compliance cost), platform-fee changes (margin) are different vectors. v1 must pick one.
- **Not validated with a second user type.** Rests on desk research + mentor relationship; no interviews conducted.

---

## Sources

- WTO Digitally Delivered Services dataset: https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm
- WTO Data — Digitally Delivered Services: https://data.wto.org/en/dataset/dideliveredservices
- WTO Global Services Trade Data Hub: https://www.wto.org/english/res_e/statis_e/services_trade_data_hub_e.htm
- WTO Digital trade chapter (sub-sector defs): https://www.wto.org/english/res_e/booksp_e/digital_trade_23_ch4_e.pdf
- WTO TiSMoS: https://www.wto.org/english/res_e/statis_e/gstdh_mode_supply_e.htm
- WTO TiSMoS methodology: https://www.wto.org/english/res_e/statis_e/daily_update_e/Tismos_methodology.pdf
- India 4th, ~$257bn digitally delivered services: https://www.manoramayearbook.in/current-affairs/india/2024/04/12/digitally-delivered-services.html
- OECD Digital STRI: https://www.oecd.org/en/topics/sub-issues/services-trade-restrictiveness-index/digital-stri.html
- OECD Digital STRI working paper: https://ideas.repec.org/p/oec/traaab/221-en.html
- OECD STRI country note – India: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/services-trade-restrictiveness-index/oecd-stri-country-note-ind.pdf
- OECD–WTO BaTIS: https://www.oecd.org/en/publications/the-oecd-wto-balanced-trade-in-services-database-batis_c321a7a7-en.html
- OECD–WTO BaTIS methodology: https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-WTO-Balanced-Trade-in-Services-database-methodology-BPM6.pdf
- BaTIS as GTAP resource: https://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=5217
- ECIPE DTRI: http://ecipe.org/wp-content/uploads/2018/05/DTRI_FINAL.pdf
- ICRIER Annual Survey of MSMEs: https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/
- ICRIER exec summary PDF: https://icrier.org/pdf/ES_Annual-Survey-MSMEs_India_2025.pdf
- ICRIER survey findings (KNN India): https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey
- MSME Dashboard (Udyam): https://dashboard.msme.gov.in/
- data.gov.in Udyam Registration: https://www.data.gov.in/catalog/udyam-registration-msme-registration
- NSS 73rd round microdata: https://microdata.gov.in/NADA/index.php/catalog/139
- MoSPI NSS 73rd round key indicators: https://www.mospi.gov.in/sites/default/files/publication_reports/NSS_KI_73_2.34.pdf
- MoSPI Supply-Use Tables: https://mospi.gov.in/publication/supply-use-tables
- PIB SUT release: https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150113
- Deloitte MSME digital-readiness (Business Standard): https://www.business-standard.com/industry/news/structural-issues-hit-msme-productivity-digital-readiness-strong-report-125110500711_1.html
- CMR MSME digital readiness: https://cmrindia.com/67-of-msmes-demonstrate-digital-readiness-across-core-and-advanced-technologies-finds-cmr-study/
- FIEO: https://fieo.org/en/
- FISME: https://fisme.org.in/
- DGFT E-commerce Exports Handbook for MSMEs: https://content.dgft.gov.in/Website/EcommExportHandbokMSME_E.pdf
- Amazon–DGFT MoU, Districts as Export Hubs: https://press.aboutamazon.com/in/2023/11/amazon-and-dgft-sign-mou-to-leverage-districts-as-export-hubs-initiative-and-boost-msme-exports-from-india
- PIB Districts as Export Hubs: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1979068
- WTO moratorium – India position: https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html
- WTO moratorium analysis (IISD): https://www.iisd.org/articles/policy-analysis/wto-moratorium-customs-duties-electronic-transmission
- Dr. Badri Narayanan Gopalakrishnan profile: https://sites.google.com/site/badrinarayanang
- Dr. Badri Narayanan Gopalakrishnan – Pahle India: https://pahleindia.org/dt_team/dr-badri-narayanan-gopalakrishnan/
