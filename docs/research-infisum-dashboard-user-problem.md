# Research: Anchoring a "Digital Trade Exposure Index" Dashboard for India's MSME Sector

**Purpose:** Identify the single narrowest, most defensible user + problem to anchor a Product Management portfolio project that connects India's digitally-delivered services trade data with MSME sector data into a "digital trade exposure index."

**Prepared for:** Purdue undergraduate builder; substantive follow-up to mentorship with Dr. Badri Narayanan Gopalakrishnan (GTAP/Purdue advisory board; NCAER; editor of forthcoming *Digital Trade Across Borders: WTO and the SMEs*).

**Date:** 2026-06-04

---

## Executive summary

The strongest version of this project is **not** a broad "exposure index for all Indian small business." The available public data cannot support that claim honestly: India's MSME data (Udyam) is granular by sector and district but says little about digital posture, while the WTO/OECD digitally-delivered-services data is rich on digital trade but **economy-level only** — there is no public dataset that joins "which Indian MSME sector" to "how much it trades digitally" at the firm or sub-sector level. Anyone who claims that join is fabricating granularity.

The defensible move is to **narrow the user to one decision-maker who already thinks in sectors and already lacks a quick screening tool**, and to reframe the "index" as a **transparent, assumption-explicit screening heuristic** rather than a measured quantity.

**Recommended anchor (detailed in the final section):** a **policy-research analyst at a trade-policy think tank (ICRIER / NCAER / Pahle India type), and specifically the team around the builder's mentor**, whose concrete recurring decision is: *"Which MSME-heavy sectors should we flag as most exposed to a specific digital-trade policy change (the WTO e-commerce moratorium, data-localization rules, or a platform-fee/policy shift), so we know where to commission the next deep-dive or write the next brief?"* The v1 is a **sector-screening dashboard** that scores ~20–30 service/trade sub-sectors on a composite of (i) digital-trade intensity (proxied from WTO/OECD economy + EBOPS category data), (ii) platform/e-commerce dependence (from ICRIER survey aggregates), and (iii) policy sensitivity (from OECD Digital STRI components and moratorium-exposure logic). It is explicitly a **prioritization heuristic for analysts**, not a measured firm-level index.

Confidence in the data findings is **high**; confidence in any single "best user" is **moderate** — the recommendation is opinionated by design, as requested.

---

## (a) Concrete potential users and the specific decision each would make

A credible PM project names a user who makes a **recurring, specific decision** that the tool changes. Below, ranked roughly by how cleanly the available data serves their decision.

| User | The specific decision the index would inform | Fit with available data |
|---|---|---|
| **Policy-research analyst at a think tank (ICRIER, NCAER, Pahle India, RIS)** | "Which sectors do we flag for the next brief / deep-dive / survey wave on digital-trade exposure?" A *prioritization/screening* decision, not a measurement one. | **Best.** They already work at sector altitude, tolerate proxies if assumptions are explicit, and publish in exactly this space ([ICRIER MSME digitalisation survey](https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/)). |
| **Trade-policy submission author (India's WTO delegation context; think-tankers feeding DGFT)** | "Which MSME-heavy sectors should our MC14 moratorium submission cite as most exposed?" India is actively contesting the e-commerce moratorium and needs sector-level exposure narratives ([Business Standard](https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html)). | Good for the *policy framing*; weak on quantified firm impact. |
| **Export Promotion Council / FIEO / FISME analyst** | "Which member sub-sectors should we target with e-commerce-export capacity-building?" FIEO already promotes cross-border e-commerce exports and runs MSME programs ([FIEO](https://fieo.org/en/)); FISME frames competitiveness via digital interoperability ([FISME](https://fisme.org.in/)). | Good intent fit, but they need *district/cluster* granularity the public services-trade data lacks. |
| **DGFT / "Districts as Export Hubs" program officer** | "Which districts/sectors get the next Amazon/Shiprocket/DHL e-commerce-export capacity MoU?" DGFT has signed MoUs across 75+ districts ([Amazon press](https://press.aboutamazon.com/in/2023/11/amazon-and-dgft-sign-mou-to-leverage-districts-as-export-hubs-initiative-and-boost-msme-exports-from-india); [PIB](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1979068)). | Decision is real and recurring, but it is *district x product*, which the digitally-delivered-services data cannot reach. |
| **MSME advisory / consulting firm (Deloitte/CMR-style)** | "Which client segments do we pitch digital-export readiness services to?" Reports already segment MSME digital readiness ([Business Standard / Deloitte](https://www.business-standard.com/industry/news/structural-issues-hit-msme-productivity-digital-readiness-strong-report-125110500711_1.html); [CMR](https://cmrindia.com/67-of-msmes-demonstrate-digital-readiness-across-core-and-advanced-technologies-finds-cmr-study/)). | Plausible but commercially fuzzy; weakest "single decision." |
| **B2B fintech/SaaS serving MSMEs (lending, GST, cataloging)** | "Which sectors should our risk/credit model weight as platform-revenue-dependent?" ICRIER shows e-commerce-integrated firms get easier finance ([KNN India](https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey)). | Interesting, but needs firm-level data a portfolio project can't access. |
| **MSME Ministry / Udyam policy unit** | "Where is digital-trade vulnerability concentrated in the formalized base?" Udyam now has 7.86 crore registrations ([MSME Dashboard](https://dashboard.msme.gov.in/)). | Important user, but government adoption is out of scope for a portfolio v1. |

**Takeaway:** Most users want *district x product* granularity, which the digitally-delivered-services data fundamentally cannot provide. Only the **think-tank policy analyst** makes a decision that is genuinely *sector-level and tolerant of explicit proxies* — which is exactly the altitude where the public data lives.

---

## (b) Comparable tools, indices, dashboards, and reports — and the gaps they leave

**1. WTO Global Services Trade Data Hub & Digitally Delivered Services dataset.** Economy-level estimates of cross-border services via computer networks (Mode 1 / GATS), 200+ economies, **eight sub-sectors**, 2005–2025; lets users build charts and reports ([WTO dataset page](https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm); [WTO Data](https://data.wto.org/en/dataset/dideliveredservices); [Data Hub](https://www.wto.org/english/res_e/statis_e/services_trade_data_hub_e.htm)). India is the **4th-largest exporter** of digitally delivered services, ~US$257bn, +17% ([Manorama/WTO](https://www.manoramayearbook.in/current-affairs/india/2024/04/12/digitally-delivered-services.html)).
> **Gap:** It is **national-aggregate only** — no breakdown by the domestic industry/firm that supplies the service, and nothing about MSMEs. It tells you India trades a lot digitally; it cannot tell you *which small-business sector* is exposed.

**2. OECD Digital Services Trade Restrictiveness Index (Digital STRI).** Catalogues and scores cross-cutting *regulatory barriers* to digital services trade across 129 countries, five pillars: infrastructure/connectivity, electronic transactions, e-payments, IP, and other barriers ([OECD Digital STRI](https://www.oecd.org/en/topics/sub-issues/services-trade-restrictiveness-index/digital-stri.html); [working paper](https://ideas.repec.org/p/oec/traaab/221-en.html)). India scores above the OECD average; 2024 saw minor liberalization (courier monopoly end; equalisation-levy removal) but data-transfer restrictions remain under the 2023 DPDP Act ([OECD STRI country note – India](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/services-trade-restrictiveness-index/oecd-stri-country-note-ind.pdf)).
> **Gap:** It measures the **policy environment**, not who is *exposed* to it. It is the right input for the "policy sensitivity" axis, but it is country-level and not MSME-aware.

**3. OECD–WTO BaTIS (Balanced Trade in Services).** Reconciled bilateral services trade, 202 economies, **26 EBOPS 2010 categories**, 2005–2023 ([OECD BaTIS](https://www.oecd.org/en/publications/the-oecd-wto-balanced-trade-in-services-database-batis_c321a7a7-en.html); [methodology](https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-WTO-Balanced-Trade-in-Services-database-methodology-BPM6.pdf)). Notably hosted as a GTAP resource — squarely in the mentor's GTAP/Purdue orbit ([GTAP](https://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=5217)).
> **Gap:** Service *category* granularity, still economy-level; no firm/MSME dimension.

**4. WTO TiSMoS (Trade in Services by Mode of Supply).** 200+ economies, **55 sectors**, four GATS modes, 2005–2022; India contributed survey data ([WTO TiSMoS](https://www.wto.org/english/res_e/statis_e/gstdh_mode_supply_e.htm); [methodology](https://www.wto.org/english/res_e/statis_e/daily_update_e/Tismos_methodology.pdf)).
> **Gap:** Best sector granularity in the trade-data family, but still national and supply-side-modeled, not MSME-linked.

**5. ICRIER Annual Survey of MSMEs (digitalisation/e-commerce, Phase 3, 2025).** Survey of **2,365 MSMEs across 12 states and 20+ clusters**; shows e-commerce-integrated firms outperform on turnover, profit, employment, and finance access, and that **only ~12% of surveyed MSMEs run their own e-store** (i.e., heavy platform dependence) ([ICRIER report page](https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/); [exec summary PDF](https://icrier.org/pdf/ES_Annual-Survey-MSMEs_India_2025.pdf); [KNN India](https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey)).
> **Gap:** It is a **sample survey**, not a census or open microdata; aggregates are published but firm-level data is not openly downloadable or NIC-joinable. It measures *e-commerce* (goods platforms) more than *digitally-delivered-services trade*.

**6. Digital-readiness assessments (Deloitte, CMR, Vi "ReadyForNext", DAI).** Firm-level self-assessment / survey snapshots of MSME digital adoption ([Deloitte via Business Standard](https://www.business-standard.com/industry/news/structural-issues-hit-msme-productivity-digital-readiness-strong-report-125110500711_1.html); [CMR](https://cmrindia.com/67-of-msmes-demonstrate-digital-readiness-across-core-and-advanced-technologies-finds-cmr-study/)).
> **Gap:** "Readiness," not "trade exposure"; vendor-driven and not sector-systematic.

**7. ECIPE Digital Trade Restrictiveness Index.** Academic alternative to OECD ([ECIPE DTRI](http://ecipe.org/wp-content/uploads/2018/05/DTRI_FINAL.pdf)).
> **Gap:** Same as Digital STRI — policy index, country-level, not MSME-linked.

**The white space that justifies the project:** No existing tool **combines** (digital-trade intensity) × (MSME platform dependence) × (policy sensitivity) at a **sector** level for India and presents it as a screening view. Each input exists; nobody has *joined and visualized* them for an MSME-policy audience. That join — done honestly, with proxies labeled — is the product.

---

## (c) Which datasets are actually available and granular enough — and where they break

### Available and usable (with caveats)

| Dataset | Granularity that actually exists | Joinable at MSME sector level? |
|---|---|---|
| **WTO Digitally Delivered Services** | Economy × 8 sub-sectors × year (2005–25), Mode 1 ([WTO](https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm)). The eight map to EBOPS digitally-deliverable categories: insurance/pension; financial; charges for IP n.i.e.; telecom-computer-information; other business services; personal/cultural/recreational (incl. audiovisual) ([WTO digital-trade chapter](https://www.wto.org/english/res_e/booksp_e/digital_trade_23_ch4_e.pdf)). | **No firm/industry split.** Joinable only by mapping EBOPS service category → broad NIC service division (a *modeled* crosswalk, not a measured link). |
| **OECD Digital STRI** | Country × 5 policy pillars × year ([OECD](https://www.oecd.org/en/topics/sub-issues/services-trade-restrictiveness-index/digital-stri.html)). | Only as a **policy-sensitivity multiplier** applied uniformly; not sector-specific to MSMEs. |
| **OECD–WTO BaTIS** | Economy × 26 EBOPS categories × year ([OECD](https://www.oecd.org/en/publications/the-oecd-wto-balanced-trade-in-services-database-batis_c321a7a7-en.html)). | Same crosswalk caveat; better category resolution than the 8-sector digital file. |
| **WTO TiSMoS** | Economy × 55 sectors × 4 modes ([WTO](https://www.wto.org/english/res_e/statis_e/gstdh_mode_supply_e.htm)). | Best sector resolution in the trade family; still national. |
| **Udyam registration data (MSME Ministry)** | 7.86 crore registrations; **state/district × enterprise category (micro/small/medium) × broad activity (mfg/services/trade)** via the open MSME Dashboard and data.gov.in ([MSME Dashboard](https://dashboard.msme.gov.in/); [data.gov.in Udyam](https://www.data.gov.in/catalog/udyam-registration-msme-registration)). Sector split as of Feb-2026: trading 42.89%, services 36.22%, manufacturing 20.89%. | **NIC code is collected at registration**, so sector-level counts in principle exist; however, the **openly downloadable** cuts are mostly *district × category*, not clean *NIC 2-digit × category* tables. NIC-level data exists internally but is not reliably public-downloadable. |
| **NSS 73rd round (2015–16), unincorporated non-ag enterprises** | ~63.4m enterprises split mfg/trade/other-services, with state and sector detail; microdata on MoSPI/microdata.gov.in ([microdata.gov.in](https://microdata.gov.in/NADA/index.php/catalog/139); [MoSPI KI report](https://www.mospi.gov.in/sites/default/files/publication_reports/NSS_KI_73_2.34.pdf)). | **Yes, sector-joinable** and microdata is open — but it is **2015–16 and pre-digital-trade**; no platform/cross-border-digital variables. Useful for *sector employment/structure weights*, not digital exposure. |
| **MoSPI Supply-Use Tables (2022-23/2023-24 base)** | 155 product groups × 67 industries, with NPCSS service-product detail ([MoSPI SUT](https://mospi.gov.in/publication/supply-use-tables); [PIB release](https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150113)). | **Yes for service-sector structure** (output, intermediate use), and it is the **best public bridge** between service products and industries — but no trade-mode or MSME-size dimension. |

### Where the data is too thin or not joinable

- **The core join does not exist publicly.** There is **no dataset that links an Indian MSME's sector to its digitally-delivered-services trade**. WTO/OECD data stops at the national border-aggregate; Udyam stops at registration attributes; ICRIER is a sample. Any "firm-level exposure index" claim is **not defensible**.
- **EBOPS/TiSMoS → NIC crosswalk is modeling, not measurement.** Mapping "telecom-computer-information services exports" to "IT-services MSMEs" is a reasonable *assumption*, but it is an analyst's crosswalk and must be labeled as such.
- **Udyam NIC-level open downloads are inconsistent.** District × category is reliably public; clean NIC 2-digit × size × geography is not consistently downloadable (the granular cut requested via data.gov.in returned 403 / is not openly served).
- **ICRIER microdata is not open.** Only published aggregates and charts; you cannot re-slice by arbitrary sector.
- **NSS is stale for this purpose.** 2015–16, no digital-trade variables; the 2023–24 MSME estimates exist as numbers but not as open digital-posture microdata.
- **NIC 2025 vs NIC 2008 break.** MoSPI introduced NIC 2025 in Nov-2025 ([context](https://blog.tatanexarc.com/msme/nic-code-for-udyam-registration/)); crosswalks across older datasets need care.

**Net:** You can honestly build a **sector-level screening composite** from (WTO/OECD trade categories) + (ICRIER aggregate platform-dependence) + (Digital STRI policy axis) + (Udyam/SUT/NSS for sector weights). You **cannot** honestly build a firm-level "exposure index." The data dictates the scope.

---

## (d) The single narrowest defensible user + problem a v1 can credibly solve

**User:** One policy-research analyst at a digital-trade/MSME think tank — concretely, the **mentor's research team (Dr. Badri Narayanan Gopalakrishnan's domain: GTAP/Purdue, NCAER, the forthcoming *Digital Trade Across Borders: WTO and the SMEs*)**.

**Problem (narrow):** *"When a specific digital-trade policy is in play — most timely, the WTO e-commerce moratorium at MC14 — I need to quickly rank India's MSME-relevant service/trade sub-sectors by their exposure to that policy, so I know which 2–3 sectors to commission a deep-dive on or cite in a submission, without rebuilding the data pull each time."*

**Why this is the narrowest defensible cut:**
- It is **sector-level**, matching the only altitude the data supports.
- It reframes "index" as a **transparent screening heuristic** (explicit weights, every proxy labeled), which is interview-defensible precisely because it is honest about its limits.
- It anchors to a **real, current decision** — India is actively contesting the moratorium and needs sector-exposure narratives ([Business Standard](https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html); [IISD](https://www.iisd.org/articles/policy-analysis/wto-moratorium-customs-duties-electronic-transmission)).
- It maps onto a **real person** the builder can actually interview and validate with, satisfying the "real user" bar that recruiters probe.

---

## Recommended anchor user + problem

**Anchor user:** A **digital-trade policy-research analyst** (archetype: the mentor's team at NCAER / GTAP-Purdue / Pahle India / ICRIER).

**Anchor problem:** *"Rank India's MSME-relevant service and trade sub-sectors by exposure to a named digital-trade policy shift (v1: the WTO e-commerce moratorium; v2 toggles: data-localization under DPDP, platform-fee/policy changes), so I can prioritize which sectors to deep-dive, survey, or cite — in minutes, with sources and assumptions visible."*

**The v1 product (one screen):** A ranked, filterable sector table/heatmap scoring ~20–30 sub-sectors on a composite of three labeled axes:
1. **Digital-trade intensity** — from WTO Digitally Delivered Services + BaTIS/TiSMoS EBOPS categories, crosswalked to NIC service divisions (crosswalk shown to the user).
2. **MSME platform/e-commerce dependence** — from ICRIER survey aggregates (e.g., the ~12%-own-e-store / heavy-platform-dependence finding) and Udyam/NSS sector weights.
3. **Policy sensitivity** — from OECD Digital STRI pillars + moratorium-exposure logic, adjustable per scenario.

Each sector cell links to its underlying sources and shows the assumption behind its score. The user can change weights and see the ranking move.

### Why this user and this problem win

1. **Data honesty.** It is the *only* user whose decision lives at the sector altitude the public data actually supports. Every other user (DGFT, FIEO, fintech) needs district/firm granularity that does not exist publicly — building for them forces you to either fabricate granularity or disappoint. (Sources throughout §c.)
2. **A real, reachable user.** The mentor publishes in exactly this domain and sits on GTAP's Purdue advisory board ([mentor profile](https://sites.google.com/site/badrinarayanang); [Pahle India](https://pahleindia.org/dt_team/dr-badri-narayanan-gopalakrishnan/)). The builder can run genuine discovery interviews and iterate against a real critic — the difference between a portfolio project and a toy.
3. **Live policy relevance.** The moratorium fight at MC14 makes "which MSME sectors are exposed" a question someone is asking *right now* ([Business Standard](https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html)).
4. **Defensible "index" framing.** Calling it a *screening heuristic with explicit assumptions* turns the data's biggest weakness (no firm-level join) into a deliberate, interview-ready design choice — "I scoped to what the data can honestly support, and made the proxies legible to the user."
5. **Clean iteration path.** v1 = one policy (moratorium), static scores. v2 = scenario toggles (DPDP data-localization, platform-fee shifts). v3 = if you ever get ICRIER/NCAER aggregate access or a district overlay, you extend toward FIEO/DGFT users — without ever having lied about granularity.

**What to explicitly NOT build in v1:** firm-level exposure scores; district-level cuts; anything implying the WTO data is sector-resolved within India; a general "all MSMEs" claim.

---

## Open questions / limitations

- **Confidence.** Data-availability findings: **high confidence** (verified against primary WTO/OECD/MoSPI/ICRIER pages). "Single best user": **moderate** — opinionated by request; a discovery interview with the mentor could redirect toward DGFT/FIEO if a district overlay becomes feasible.
- **The crosswalk is the credibility risk.** EBOPS service category → NIC service division is an analyst assumption; the project must surface it, not bury it. This is the first thing a sharp interviewer will probe.
- **ICRIER data is sample, not census, and not openly re-sliceable.** Platform-dependence inputs come from published aggregates, so sector coverage is uneven. Verify which sectors the survey actually disaggregates before promising them in the UI. (Could not extract the full PDF tables programmatically; relied on ICRIER's published summary/exec-summary and press coverage.)
- **Udyam NIC-level open access unconfirmed.** District × category is public; NIC 2-digit × size × geography may require a data request or scraping the MSME Dashboard — confirm before designing sector weights around it (the granular data.gov.in resource returned 403 on fetch).
- **NIC 2025 vs NIC 2008 / EBOPS 2010 vintage mismatches** require an explicit version note.
- **"Exposure" is undefined until the policy is named.** Exposure to the moratorium (cheap digital imports / lost tariff space) is a different vector than exposure to data-localization (compliance cost) or platform-fee changes (margin). v1 must pick **one** and say so.
- **Not validated with a second user type.** Recommendation rests on desk research + the mentor relationship; no interviews conducted here.

---

## Sources

- WTO — Digitally Delivered Services Trade Dataset: https://www.wto.org/english/res_e/statis_e/gstdh_digital_services_e.htm
- WTO Data — Digitally Delivered Services: https://data.wto.org/en/dataset/dideliveredservices
- WTO — Global Services Trade Data Hub: https://www.wto.org/english/res_e/statis_e/services_trade_data_hub_e.htm
- WTO — Digital trade chapter (sub-sector definitions): https://www.wto.org/english/res_e/booksp_e/digital_trade_23_ch4_e.pdf
- WTO — TiSMoS (mode of supply): https://www.wto.org/english/res_e/statis_e/gstdh_mode_supply_e.htm
- WTO — TiSMoS methodology: https://www.wto.org/english/res_e/statis_e/daily_update_e/Tismos_methodology.pdf
- India 4th in digitally delivered services exports (WTO data, ~$257bn): https://www.manoramayearbook.in/current-affairs/india/2024/04/12/digitally-delivered-services.html
- OECD — Digital STRI: https://www.oecd.org/en/topics/sub-issues/services-trade-restrictiveness-index/digital-stri.html
- OECD — Digital STRI working paper/methodology: https://ideas.repec.org/p/oec/traaab/221-en.html
- OECD — STRI country note, India: https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/services-trade-restrictiveness-index/oecd-stri-country-note-ind.pdf
- OECD–WTO BaTIS: https://www.oecd.org/en/publications/the-oecd-wto-balanced-trade-in-services-database-batis_c321a7a7-en.html
- OECD–WTO BaTIS methodology (EBOPS categories): https://www.oecd.org/content/dam/oecd/en/data/methods/OECD-WTO-Balanced-Trade-in-Services-database-methodology-BPM6.pdf
- BaTIS as GTAP resource (Purdue): https://www.gtap.agecon.purdue.edu/resources/res_display.asp?RecordID=5217
- ECIPE — Digital Trade Restrictiveness Index: http://ecipe.org/wp-content/uploads/2018/05/DTRI_FINAL.pdf
- ICRIER — Annual Survey of MSMEs (digitalisation) report page: https://icrier.org/publications/annual-survey-of-micro-small-and-medium-enterprises-msmes-in-india-the-role-of-digitalisation-in-enterprise-development/
- ICRIER — Executive summary PDF: https://icrier.org/pdf/ES_Annual-Survey-MSMEs_India_2025.pdf
- ICRIER MSME survey — coverage/findings (KNN India): https://knnindia.co.in/news/newsdetails/msme/e-commerce-linked-msmes-have-greater-market-access-icrier-survey
- MSME Dashboard (Udyam, sector split, totals): https://dashboard.msme.gov.in/
- data.gov.in — Udyam Registration catalog: https://www.data.gov.in/catalog/udyam-registration-msme-registration
- NSS 73rd round microdata (unincorporated non-ag enterprises): https://microdata.gov.in/NADA/index.php/catalog/139
- MoSPI — NSS 73rd round key indicators: https://www.mospi.gov.in/sites/default/files/publication_reports/NSS_KI_73_2.34.pdf
- MoSPI — Supply-Use Tables: https://mospi.gov.in/publication/supply-use-tables
- PIB — SUT 2020-21/2021-22 release (product-industry detail): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2150113
- Deloitte MSME productivity/digital-readiness (Business Standard): https://www.business-standard.com/industry/news/structural-issues-hit-msme-productivity-digital-readiness-strong-report-125110500711_1.html
- CMR — MSME digital readiness study: https://cmrindia.com/67-of-msmes-demonstrate-digital-readiness-across-core-and-advanced-technologies-finds-cmr-study/
- FIEO: https://fieo.org/en/
- FISME: https://fisme.org.in/
- DGFT — E-commerce Exports Handbook for MSMEs: https://content.dgft.gov.in/Website/EcommExportHandbokMSME_E.pdf
- Amazon–DGFT MoU, Districts as Export Hubs: https://press.aboutamazon.com/in/2023/11/amazon-and-dgft-sign-mou-to-leverage-districts-as-export-hubs-initiative-and-boost-msme-exports-from-india
- PIB — Districts as Export Hubs / e-commerce: https://www.pib.gov.in/PressReleasePage.aspx?PRID=1979068
- WTO e-commerce moratorium — India position (Business Standard): https://www.business-standard.com/india-news/wto-need-to-re-examine-implications-of-moratorium-of-customs-says-india-124022900607_1.html
- WTO moratorium analysis (IISD): https://www.iisd.org/articles/policy-analysis/wto-moratorium-customs-duties-electronic-transmission
- Dr. Badri Narayanan Gopalakrishnan — profile: https://sites.google.com/site/badrinarayanang
- Dr. Badri Narayanan Gopalakrishnan — Pahle India profile: https://pahleindia.org/dt_team/dr-badri-narayanan-gopalakrishnan/
