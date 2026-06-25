# Veer Progress Log

The running narrative log for the PM internship execution system. Everything I work on, day by day, plus pillar 2/3/4 progress, system signals, and notes from external conversations (Dr. G replies, alumni, etc).

Different from `DECISIONS.md`, which is only curated product decisions with explicit trade-offs. This is the everything log — the raw record.

Read at the start of every chat. Updated at the end of work sessions, or mid-chat when something new happens. Lives in the repo (not a Google Doc), so it is readable and writable in-session.

---

## How to use this file

**Daily entry format:**

```
### YYYY-MM-DD (Day of week)

Pillar 1 (project):
- What I did today (pulled from GitHub commits + chat updates)

Pillar 2 (technical):
- SQL / Python / system design work

Pillar 3 (network):
- Messages sent, replies, conversations had

Pillar 4 (interview):
- Mock reps, solo reps, framework practice

System signals (note only if relevant):
- Sleep / workout / unusual factors

Notes:
- External: Dr. G replies, alumni notes, anything that changes the plan
- Internal: what blocked me, what I'm thinking about
```

**Sources Claude pulls from to update this:**
1. GitHub commits at github.com/veer-sanyal/india-msme-digital-trade-exposure
2. Whatever Veer says in the current chat
3. `memory.md` (current-state snapshot) and past-chat search for things missed

**Rules:**
- `DECISIONS.md` stays the curated product log. This stays the everything log.
- One entry per day. Don't backfill more than 3 days — anything older becomes a Sunday-session note instead.
- Read the tail by default: at the start of a conversation, read only the trailing ~3-4 weeks of dated entries here (memory.md holds current state). Pull older history only in Sunday planning mode or when asked about something specific.
- Archive monthly: when a month closes, move its dated entries into `PROGRESS-archive.md` (chronological order; create it if missing), keeping this file to the trailing ~3-4 weeks. The standing sections below the daily entries (Pillar 2/3 running ledgers, External relationships log, System signals) stay here. Nothing is deleted — the archive holds the complete history.
- The Sunday session reviews the past week of entries to populate the Sunday email "last week's reflection."
- Pull GitHub commits before writing an entry so it matches what actually shipped.


**Study/practice trace:** study/practice (tutor mode) sessions append a one-line dated trace at close (the commit-equivalent for Pillars 2 & 4), e.g. `Pillar 2: 18-item metrics session, 72% acc, metric-drop still red`.


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

## Week 4 (June 8-14, 2026) — Pillars 2 and 3 turn on

### 2026-06-09 (Tue)

Pillar 3:
- Alumni tracker created (`alumni-tracker.md`, project root): 10-slot shortlist, LinkedIn recipes, targeting criteria, message blueprint
- **Shortlist complete: 10 names, all verified live on LinkedIn** (Claude drove the Alumni Tool via Chrome). Mix: Microsoft x3, Meta, Amazon, AWS, Google, Fidelity, Elanco + 4 on the bench. Two 2nd-degree with mutuals (Anicito, LaCroix). Corrected one research-doc error: Akash Ravi is AI PM at Microsoft, not Amazon
- Next: first 3 messages this week per the briefing
- LinkedIn profile finished (Monday's small item, completed via Claude driving Chrome): headline rewritten (dropped "Aspiring PM", now leads with the live dashboard), About updated (dashboard paragraph + why-product close, Firmly/StudyFlowForge/SMIF content kept), dashboard added to Projects (May 2026-Present, live + repo links, the 29.4x IP-licensing correction as the measured-over-vibes proof point), Featured section created with the live site link. Remaining gap: zero posts — first post should be the dashboard walkthrough, before outreach starts
- StudyFlowForge dated honestly on the profile: now Feb 2026 - Apr 2026 (was "Present"). Decision: don't restart it, don't remove it — one anchor project, SFF stands as a finished past artifact
- First LinkedIn post drafted (sitting unposted in the composer): dashboard announcement with live + repo links in the body (chose artifact-access over the link-in-comment reach tactic — audience is alumni/recruiters who click through, not the algorithm). Veer is rewriting it himself: the draft's "10x from an earlier note" framing misrepresented the error-catch — the accurate story is the no-hardcoded-numbers build rule catching a placeholder (Entry 009). Two feed-ready charts generated from `site/data.js` and saved to `files/linkedin/` (chart_A_consulting.png: 13x consulting surge; chart_B_ip_licensing.png: the ~10x placeholder vs computed 29.4x). Post goes up before the first alumni messages

### 2026-06-10 (Wed)

Pillar 3:
- First post redrafted from scratch (`files/linkedin/post-01-v2.md`), per Veer's call to discard the old draft. Built on the research structure (hook/tension/substance/takeaway/invitation) with the accurate Entry 009 story: the no-hardcoded-numbers rule catching the ~10x placeholder (computed 29.4x, $0.67B to $19.8B). Chart B attached; links stay in the body per the 06-09 decision
- Second angle drafted on request (`post-01-v3.md`): Veer asked for a version not built on the Entry 009 error-catch. v3 leads with the consulting 13x / exposure-index finding, chart A
- v4 drafted (`post-01-v4.md`) after reading the full research original + the product repo's DECISIONS.md per Veer: keeps v3's finding hook, adds the named user/policy anchor (Entry 012), the $90B-vs-92k-firms contrast (Entry 010), and the ship-v0-honestly framing (Entry 008). Current pick. Next: Veer reviews, posts when he has 60-90 min to engage, then alumni messages start

System:
- Purdue clubs/resources question answered from `research-purdue-network-recruiting.md`. Junior-year club priority confirmed: (1) PM Club @ Purdue (confirm undergrad access — MEM-incubated), (2) Data Mine (10-13 hrs/wk vs fall recruiting crunch, weigh at Sunday session), (3) Morgan Center optional; keep SMIF + EPICS, add nothing else. Tactical add this week: PM Club DM tacked onto Thursday's small item (already in LinkedIn for the alumni message)
- **Week 4 candidates for the Sunday session: Data Mine registration check (seats commit before fall — if in, act this month); CCO resume review timing (slots after resume v1, due mid-July)**
- Context system restructured for token efficiency (deep-research-backed): new `context/` tier holds compressed working copies (14 docs, ~45% smaller, all facts/dates/citations preserved); the system prompt now reads `context/` instead of `docs/`; the five `docs/` summaries of two-tier research reports were deleted (replaced by compressed copies; full originals stay in `files/`). Three docs left uncompressed for now (interview reality check, adjacent roles, Purdue network) — read from `docs/`.

### 2026-06-13 (Sat)

Pillar 1:
- Closed the week's open dashboard items (the telemetry add, the iteration item, and the decision-log entry that had slipped Mon-Fri) via a Claude Code session. Instrumented the published walkthrough with **GoatCounter** usage telemetry: one hosted async script in `<head>` plus custom events wired into `walkthrough.js`, all routed through a guarded `track()` helper so the page degrades silently if the script is blocked, still loading, or unconfigured. Five named custom events beyond auto page views: `<section>-viewed` (each titled Act fires once per load when it scrolls into view, e.g. `act4-viewed`); `flow-toggle-exp` / `flow-toggle-imp` (the Act I exports/imports toggle, the page's one such control); `score-table-interact` (first interaction with the Act IV full score table); `expander-open` (any methodology/breakdown `<details>` opened); and `sublink-click` (outbound source-link clicks — binds to nothing in v0, begins reporting if a link is added). Live site code wired (`veersanyal.goatcounter.com`), the `YOUR_CODE` placeholder replaced.
- Surfaced the central credibility caveat in the UI at the Act IV ranking: the **EBOPS→ISIC crosswalk** (from the WTO correspondence) that joins each sector to its NIC/ISIC industry is a modeled assumption that a sector's firms trade what their industry code implies, not an observed join — no public dataset records which individual MSMEs actually export digitally delivered services, so the trade intensity attributed to each sector is inferred and read as direction, not a calibrated measurement.
- DECISIONS.md **Entry 013** (telemetry instrumentation): GoatCounter for v0 over Amplitude — free, privacy-friendly, cookieless, so a public static site needs no consent banner; one async script, no build step, no new dependency. Revises Entry 012's Amplitude note for v0; Amplitude kept as the documented later option if the questions outgrow flat event counts.
- Still open: the **telemetry readout** (the Fri Jun 12 item) is deferred until ~1 week of live data accrues; the only remaining manual step is confirming the wired events actually fire on the live site.

Pillar 3 / External:
- **Accepted into the Purdue Daniels School of Business Summer Externship** (acceptance email Jun 8, Storie Pedley). 4-week virtual program, **Jul 6 – Aug 1, 2026**, team-based consulting for a local business: Wk 1 (Jul 7-11) Accenture intro-to-consulting modules + NACE competencies + team/business/alumni-mentor assignments + client outreach; Wks 2-3 (Jul 14-25) research + solution; Wk 4 (Jul 28-Aug 1) final proposal presentation. Implications: warm Pillar-3 contacts (assigned alumni mentor + business owner + teammates) at near-zero initiation cost — exactly the surface his cold-outreach aversion blocks; Pillar-4 behavioral stories (client mgmt, teamwork, persuasion, leadership w/o authority); a Daniels-branded line for resume v1 (mid-July, "selected for"). Watch-out: runs the last 4 weeks of summer, overlapping resume v1 + metrics/stats study + outreach — assigned team work (low initiation cost) must not crowd out the self-directed dashboard (the differentiator). Open: weekly hours TBD; scheduling integration deferred to the Jun 14 Sunday session.
- **Nudge to Dr. G (Infisum) drafted** — saved as a Gmail reply in the existing thread (to badri@infisum.com), pending send. Carries the telemetry + Act IV caveat update and one focused question: whether the modeled EBOPS→NIC crosswalk is defensible to ship as a flagged screening heuristic. He has been silent since the June 2 follow-up.

System:
- Integrated the resume / cover-letter system into the planning repo (copy-only; originals untouched). Profile source-of-truth (12 files) → `context/applications/profile/`; merged the two instruction docs into `context/applications/application-docs-workflow.md`; extracted a canonical ATS-safe LaTeX template (`context/applications/resume-template.tex`, compiles clean); deep-research docs → `files/applications/` with compressed copies of the two large ones in `context/applications/research/` (Resume 417→131, CoverLetter 427→171 lines); 12 legacy company outputs + master resume → `applications/`. Wired application deadlines into `context/key-dates.md` (new Application Pipeline table) + a Sunday-session rule in SYSTEM-PROMPT. Only 2 of 12 legacy companies have `.tex` sources; rest are PDF-only, flagged for on-demand regeneration. Spec + plan in `specs/2026-06-13-application-docs-integration-*.md`.

### 2026-06-14 (Sun)

Pillar 3 (network):
- First LinkedIn post finalized to **v7** (`files/linkedin/post-01-v7.md`) and saved in the LinkedIn composer, via Claude driving Chrome. Veer handed Claude the call ("make the best possible post, loop until done"). Big change: **angle**. v2-v6 all led with build discipline (nothing hardcoded / the 30x story); v7 leads with the surprising **finding** (India's largest digitally-delivered export category is no longer software, it's "other business services" / consulting, the sub-code grew ~13x, <$7B 2005 to ~$92B 2022), with discipline kept as one credibility paragraph (v0 honesty + modeled-assumption flag + computed-from-source). Rationale: a first post to a cold alumni/recruiter audience needs a hook that makes a stranger care; the reframe does that, and `research-linkedin-presence.md` endorses "one chart + what surprised me." Ran the draft through the-humanizer skill (LinkedIn): real paragraphs, contrarian-specific hook, genuine closing question, no em dashes, no buzzwords. Deliberate override: humanizer's "link-in-body kills reach / use first comment" rule was refuted by Veer's own research; link stays in body per the 2026-06-09 artifact-access decision.
  - Media call: **lead image = `chart_A_consulting.png`** (it is the hook: consulting 13x, $92B vs $16B; clean and on-message). Restyled 2026-06-14 to match the live dashboard: IBM Plex Serif/Sans/Mono + the dashboard palette (paper #FBFAF7, indigo #2E6FB0, grey #858B96, grid #ECEAE3), data read straight off the live Plotly traces. Generator now committed as `make_chart_A.py` (was a bare PNG before). Optional 2nd = a screenshot of the live Act IV "Exposure ranking by category" view (shows the product + the visible modeled-assumption caveat). Chart B / the 30x discipline angle is now OFF this post and kept as a ready **second-post** seed (post-01-v6.md + chart_B_ip_licensing_v3.png).
  - Still manual for Veer: attaching the image (LinkedIn image upload is a native OS file picker the browser tools cannot drive) and hitting Post. Text + draft are done.
  - Earlier in the session: drafted v5 in composer, then v6 (round-30x reframe, declining the false "I typed 30x" version since the real placeholder was ~10x per product DECISIONS Entry 009), before Veer redirected to a full best-post pass (v7).
  - **UPDATE (later 2026-06-14): the first LinkedIn post went LIVE — Veer posted it.** This clears the gate that was holding Pillar-3 outreach; 3 alumni messages/week now start.

Pillar 3 / External (Dr. G):
- **Nudge sent** (2026-06-13 ~5:30pm PT, in-thread to badri@infisum.com) — the telemetry + Act IV caveat update + the EBOPS→NIC-crosswalk-as-screening-heuristic question.
- **Dr. G replied 2026-06-14: "Thanks a lot Veer, let's catch up soon."** He did not answer the crosswalk/methodology question in writing — do not treat the reply as validation of the approach; that conversation moves to the call. The reply is a warm opening from someone who already offered to route Veer to clients.
- **Move made:** drafted a short in-thread reply to convert "soon" into a booked 30-min slot on his calendar (same path as the May 14 call). Pending Veer's send. Naming the pattern: a vague "soon" dies if not pinned — this is the insight-without-action trap, so the action is to lock the time now.

System:
- Made PROGRESS.md a tail-read so the log stops eating context as it grows. SYSTEM-PROMPT's start-of-conversation step now says read only the trailing ~3-4 weeks (full history only in Sunday mode or on request). Added a monthly-archive rule: when a month closes, roll its entries into `PROGRESS-archive.md` and keep this file to ~3-4 weeks plus the standing ledgers/logs — nothing deleted. Documented in PROGRESS Rules + file-index. Not archiving yet (file is small today).

New opportunity — Claude Corps Fellow (CodePath + Anthropic):
- Veer raised the **Claude Corps Fellow** program (job-boards.greenhouse.io/claudecorps/jobs/4250200009) and decided to **apply, accepting that it would mean a leave of absence from Purdue for the fellowship year**. Key facts: 12-month full-time, in-person, paid ($85K + benefits), relocation required, employed by CodePath. Cohort 1 starts **Oct 19, 2026**; rolling review, **deadline Jul 17, 2026**. Eligibility: under 2 years full-time experience (internships don't count), 18+, US work-authorized, no degree required. Process: short app → take-home → 25-min conversation → Super Day (two 1:1s); if selected, match-interview with 2-3 host orgs.
- **Strategic flag raised before building:** this path *replaces* the Summer 2027 PM internship plan, not supplements it (the fellowship window swallows junior year + that summer). Veer chose to proceed anyway. The dashboard (Pillar 1) doubles as his strongest Claude Corps artifact, so continuing it is right either way. The four-pillar plan + Purdue leave logistics need a deliberate revisit if he advances.
- **Application work done this session:** built a Claude-Corps-tailored 1-page resume (`applications/Claude Corps/VeerSanyal_ClaudeCorps_Resume.tex` + `.pdf`, compiles clean) leading with end-to-end builds (MSME dashboard, StudyFlowForge), AI/Claude fluency, and EPICS community/teaching; drafted both 350-word short answers (community impact = EPICS museum build; setback = Firmly QA "definition of done" failure → edge-case matrix, reinforced by the dashboard compute-from-source rule); assembled a full paste-ready form answer key. All in `applications/Claude Corps/Claude-Corps-Application.md`. Pipeline row added to key-dates.md (Stage: Drafting).
- **Gating items only Veer can do:** (1) complete both Skilljar courses (AI Fluency + Claude 101) and upload the completion certificates — required, and they grade how he prompts; (2) confirm the personal fields left marked [CONFIRM] (work authorization/sponsorship, age, email choice, education-level dropdown, demographics, how-heard); (3) final review + submit (not auto-submitted — personal data + irreversible).

### 2026-06-15 (Mon)

Claude Corps application:
- Polished the tailored resume (`applications/Claude Corps/VeerSanyal_ClaudeCorps_Resume.tex/.pdf`) against the live FAQ (anthropic.com/claude-corps/fellow). Three commits: (1) retuned the summary tagline from builder-first to mission-first ("uses AI to ship real tools for civic, small-business, and community problems") to hit the societal-impact selection criterion the resume was thinnest on; (2) reframed the dashboard's lead bullet to open with why it matters (helping a researcher ground a policy call in data) before the scoped/shipped mechanics; (3) trimmed the StudyFlowForge stack tags to `React, TypeScript, Supabase, Gemini API` (dropped redundant SQL/PostgreSQL, kept the LLM/AI signal). Trimmed the tagline to one line. Confirmed the page is not cramped and stays one page. Added a `.gitignore` rule for LaTeX build artifacts (*.aux/*.log/*.out).
- Confirmed admission is rolling: Jul 17 is the Cohort 1 hard deadline (starts Oct 19, 2026); later applicants roll to the Jan/Aug 2027 cohorts. Earlier submission = earlier review + more of the ~100 Cohort-1 slots open. Real blocker remains the two Skilljar courses (AI Fluency + Claude 101) that gate submission, not the resume.
- **Registered for Claude 101 on Anthropic's Skilljar** (~11:30pm PT) and created the Anthropic Education account. The gating course track is now started, not just identified. Still open: finish Claude 101, do AI Fluency, upload both certificates, confirm the [CONFIRM] fields, submit.

**Sunday planning session (run Mon Jun 15, a day late):**
- Recon (Gmail + Calendar, past 7 / next 14 days): **Dr. G's reply confirmed in-thread** ("Thanks a lot Veer, let's catch up soon," Jun 14 03:20 UTC). **Veer's scheduling reply is still an unsent DRAFT** (composed Jun 15 03:27 UTC, to badri@infisum.com). This is the highest-leverage open action and it is stuck exactly where the system predicts. Named it: a vague "soon" dies if not pinned; send the draft, book the 30-min slot. Next 14 days are clear (summer, home) apart from the recurring spine and the Jun 21/28 Sunday sessions. No alumni replies (outreach not yet started). No new application emails beyond the Skilljar registration.
- Pattern named: insight-without-action is showing up as two finished things sitting one click from done (the Dr. G reply in Drafts; the Claude Corps app blocked only on two short courses). The week's job is to convert both, plus turn Pillar 3 on for real now that the LinkedIn-post gate is cleared.
- Week's commitments by pillar: **P1** verify GoatCounter events fire (Mon), then write the first telemetry readout from ~1 week of data (Fri draft, Sat write) — the "measured usage" evidence. **P2 (lead)** metrics/stats fluency begins: Khan Academy stats (significance, CIs/p-values, A/B reading) + first PM-tutor sessions (metric trees, NSM/guardrail, numerator-denominator). **P3** send the Dr. G reply + first 3 alumni messages by Saturday (Anicito, LaCroix, one cold lead). **Claude Corps** finish both Skilljar courses, upload certs, review + submit.
- Calendar written directly (connector on): all 18 Mon-Sat block titles retitled and six 9:00 Morning Briefings created.
- **Later 2026-06-15: Claude 101 Skilljar course COMPLETED** — certificate of completion earned and saved to `applications/Claude Corps/Skilljar_Claude101_Certificate.pdf`. One of the two gating courses is now done; only AI Fluency remains. Calendar adjusted: Wed small item pulled forward to AI Fluency, Fri small item becomes upload-both-certs + confirm [CONFIRM] fields.

New opportunity — Trice Systems (warm intro via Veer's mom):
- Veer was introduced (through his mother) to **Trice Systems** (tricesystems.com), a Hyderabad hyperlocal community-commerce startup digitizing local micro-entrepreneurs (street vendors, home chefs, home bakers, small stores) — discovery, order aggregation, prepaid payments, delivery. Early stage: ~$1.07M raised (single round, Dec 2021), ~₹25Cr valuation, ~200 communities / 75-100K residents / 3,000+ sellers in Hyderabad; advisors include Raja Koduri (Intel), SS Rajamouli, Shobu Yarlagadda. Founders: Jaya Priyankha Raghuraman, Naveen Kl, Goutham Reddy.
- **Strong thematic fit:** Trice digitizes exactly the India MSMEs the dashboard models. A product/data role here would make Veer's whole narrative cohere. Flagged the two unknowns that decide it (the role family, and the hours/dates/onsite-vs-remote load vs. protecting the dashboard + Daniels Jul 6–Aug 1 + the Claude Corps fork). Told Veer to ask the contact those three questions before deciding — it's a Sunday-session structural call, not a snap yes.
- **Contact asked for Veer's resume.** Built a tailored one-page resume → `applications/Trice/VeerSanyal_Trice_Resume.{tex,pdf}` (compiles clean, 1 page): product/builder-forward, leads with the India MSME dashboard (thematic fit) + StudyFlowForge, Firmly framed as an e-commerce/payments product story, SMIF + EPICS for breadth/leadership; honest-proficiency skills. Re-tilt to pure SWE if the role turns out engineering-specific.
- **Profile gap fixed:** the India MSME dashboard was not in the resume profile source-of-truth; added `context/applications/profile/project-msme-dashboard.md` (flagship Pillar-1 project) and indexed it (profile MEMORY + file-index). Pipeline row added to key-dates (Stage: Ready, no posting deadline).
- **DECISION + SENT (2026-06-15):** Veer chose **Trice over Mantrika** — the contact is closer to the Trice people and can get him started ASAP, and the MSME-dashboard connection makes the story cohere. He **sent the message + Trice resume over WhatsApp to "Sudip Uncle"** (the family contact, via his mom). This is a genuine closed-loop Pillar-3 action (warm outreach + artifact actually out, not stuck in drafts). Awaiting Sudip Uncle's intro to the right person at Trice. Open question still to resolve once connected: role family (product vs SWE/ops), hours/dates, remote vs Hyderabad-onsite — and how it fits against the dashboard + Daniels (Jul 6–Aug 1).

### 2026-06-16 (Tue)

Pillar 1 — telemetry:
- **GoatCounter events CONFIRMED firing on the live site** (the Mon done-check item, completed). Pulled the dashboard (`veersanyal.goatcounter.com`): all five wired custom events are logging — hero-viewed (13), thesis-viewed (12), concepts-viewed (11), act4-viewed (9), next-viewed (7), act1-viewed (7), learned-viewed (6), notclaim-viewed (6), act3-viewed (6). Clean section-view funnel from hero (~13) down to the later acts (~6). This clears the only remaining manual telemetry step; the readout now just waits on more accrued data.
- **First-week traffic (past 7 days): 101 visits.** **66% (67 visits) came from LinkedIn** — the first post is driving real traffic; remaining 34% direct/unknown. 100% United States. 57% phones / 43% desktop; Safari 58 / Chrome 43; iOS 58 / macOS 24 / Windows 19. Read: LinkedIn-on-mobile is the dominant arrival path, as expected from a single post.

System signals:
- **System upgrade shipped (2026-06-15), spec `specs/2026-06-15-dynamic-tracking-system-upgrade.md`.** Five structural changes, each its own commit: (1) **Auto-reconcile** — the system prompt now reconciles state against reality (product-repo commits + calendar + Gmail drafts) at the start of every session and commits the diff, so memory.md/PROGRESS.md stop drifting. (2) **Closed-loop accountability** — Morning Briefings carry a done-check on yesterday's block; any item stuck >2 sessions is auto-decomposed to the smallest physical next action instead of re-listed (the Dr. G draft is the live test case). (3) **Two-tier docs** — collapsed `docs/` into `context/` (read) + `files/` (deep research); removed the manual mirror-refresh that drifted. (4) **Single source of truth** — each fact now has one owner (direction.md = strategy, memory.md = current state, PROGRESS.md = narrative, key-dates.md = timeline, state.json = learning); duplicated facts replaced with pointers, and the outreach-cadence contradiction (3/week vs "5 by August") fixed. (5) **Stale fixes + tutor micro-rules** — Atlassian window flagged closed, APM-ineligibility + Daniels-hours contingencies added, resume v1 timing resolved; tutor got a question-generation rubric, a precise Bloom-promotion window, and ambiguous-answer / fatigue-vs-weakness handling. This was a system change, not pillar work; the anti-avoidance guard still applies (system-optimization is not a substitute for sending the Dr. G reply).

### 2026-06-18 (Thu)

Pillar 3 / External (Dr. G):
- **Call happened (rescheduled to 3:45pm PT) and went well.** Two concrete outcomes: (1) Dr. G will **share the dashboard with policy contacts in India and check whether they have data Veer could use** — a potential source for the modeled EBOPS→NIC crosswalk join and/or the deferred digital-adoption component; (2) he said **he could use something similar for the US**, but flagged that Veer should **first check whether a US equivalent already exists** before building one. The relationship moved from "let's catch up" to active routing.
- Open follow-through: (a) send a specific thank-you within 24h (reference the India share + the US idea, confirm the next step); (b) run a prior-art check on a US version before committing to build it; (c) await his India intros/data.

Claude Corps:
- **AI Fluency: Framework & Foundations Skilljar course DONE** (certificate saved to `applications/Claude Corps/Skilljar_AIFluency_Certificate.pdf`). With Claude 101 (Jun 15), **both gating courses are now complete.** The application is no longer blocked on coursework. Remaining (all small, all on Veer): upload both certificates into the application, confirm the [CONFIRM] personal fields, final review + submit. Deadline Jul 17 (rolling; earlier = better).
- **Essay review + edits (later 2026-06-18).** Reviewed both 350-word short answers with Veer. Essay 2 (Firmly setback): Veer worried it leans on a 15-month-old project he can't fully reconstruct for an interview and asked whether to switch topics. Verdict: keep it — every specific is grounded in `experience-firmly.md` (PayPal recovery flow, ~15 edge cases incl. missing billing/shipping data, edge-case matrix/release checklist adopted as team standard), it is his only real-stakes failure-for-a-real-user story, and the "what changed" lives in present work (dashboard compute-from-source rule) he can defend cold. De-risk by re-internalizing from his own profile notes + bridging to the present in interviews; know both numbers (~15 validated edge cases, 20+ matrix test cases). Made one edit: "cannot-reproduce loops dropped" → "the bugs we couldn't reproduce dropped off" (de-jargoned). Essay 1 (EPICS museum): rewrote the hedged ending around the true outcome Veer confirmed — team took the museum from a stalled paper concept to a finalized design + working prototype, did NOT finish the final build — and trimmed one self-reflection beat so the community outcome carries the close (341 words, was 314). Essays now: E1 341, E2 304, both under 350.
- **Built a Firmly-setback interview spine** (`applications/Claude Corps/Firmly-Setback-Interview-Spine.md`): 15-sec hook, STAR, numbers to know, probe Q&A, and the bridge-to-present move — to close Veer's "can't reconstruct a 15-month-old project under pressure" worry with prep, not just reassurance.
- **Claude Corps application SUBMITTED (2026-06-18).** Filled the entire Greenhouse form via Claude driving Chrome from the answer key (all basics, education = Some College/No Degree, six eligibility dropdowns, completed-both-courses Yes, resume + combined-cert PDFs attached, start 10/13/2026, both essays pasted, "done"/comfortable/built checkboxes, three host-org domains, CodePath = No). One judgment call: "How did you hear" had no family option → chose Friend/referral (dad referred him); GitHub field = live dashboard URL. Left pronouns/accommodations/research-opt-in/demographics blank (optional, his discretion). Veer reviewed and submitted himself (personal data + irreversible). Stage Ready → **Submitted**, ahead of the Jul 17 rolling deadline. Next: take-home → 25-min conversation → Super Day. Closed loop: the second of the two "one-click-from-done" items the system flagged this week is now actually done. **Confirmation email received same day** ("your application is in... may take a few weeks before you hear from us; we'll update you at each stage") — submission verified, multi-week wait expected, no action pending.
- **Auto-reconcile upgrade:** added an inbound-Gmail scan to the start-of-session reconcile (SYSTEM-PROMPT step 3b). The reconcile previously only checked Gmail *drafts* (outbound tripwires); it now also searches the inbox for replies/updates on live applications and tracked threads (Claude Corps take-home/interview/decision, Dr. G, Trice, alumni) so an inbound like a take-home invite can't slip past. Prompted by Veer asking to ensure the system watches for Claude Corps updates.
- **System fix (mount/git):** discovered the workspace is a virtiofs FUSE mount that denies file *deletion* to the sandbox (unlink blocked; rename works), so git cannot clean up its own lock files and committing against the mounted `.git` strands undeletable `*.lock` files — the manual lock-deletion Veer was doing every session. Root cause is the mount, not a grantable permission. Fixed permanently by rewriting SYSTEM-PROMPT's COMMIT AND PUSH protocol to commit from a clean sandbox clone and push to GitHub (works every time); retired the unworkable `find .git -name '*.lock' -delete` step. Mounted local `.git` now lags GitHub by design (harmless; `git pull` from Veer's own Terminal resyncs).

### 2026-06-19 (Fri)

Mid-week reconcile (calendar):
- **Reconciled the live calendar against reality.** Stale items found and fixed: the Claude Corps application was **submitted Jun 18, three days ahead** of the two blocks still holding its steps — Fri Jun 19 small item ("upload certs + confirm [CONFIRM] fields") and Sat Jun 20 small item ("review + submit"). Both retitled: Friday's (already elapsed) marked "DONE early"; Saturday's freed slot **backfilled** with the next-highest-value open action.
- **Verified before rewriting:** checked the Dr. G Gmail thread + drafts. The post-call **thank-you was never sent** (last send was the Jun 14 nudge; no draft exists), so it is now overdue past the 24h window and a live tripwire. Reassigned it to Saturday's freed small-item block (smallest start named in the event: open the Jun 14 thread, three sentences referencing the India share + the US-version idea, send before the deep block). Sat Morning Briefing rewritten to drop the stale "are both certs uploaded" framing and carry an honest week scorecard.
- **Week's honest scorecard:** shipped — Dr. G call (went well, Jun 18), Claude Corps submitted (Jun 18), telemetry confirmed firing (Jun 16). Slipped — **alumni outreach at 0 of 3** (whole pillar at zero this week) and the **Dr. G thank-you unsent**. Both flagged for the Sunday Jun 21 session; alumni catch-up is its first fix for next week. Not pulling next week's plan forward mid-week (Sunday owns structural replans).

System:
- **New standing rule added to SYSTEM-PROMPT.md (CLOSED-LOOP ACCOUNTABILITY): "Ahead-of-schedule replan."** When a scheduled block's task is finished before its day, the auto-reconcile now (a) retitles the original as done so the record is honest and (b) backfills the freed future block with the next-highest-value action from the existing backlog (memory.md Next moves + key-dates Pipeline + open pillar criteria + any pillar at zero), matched to the block type (deep/secondary/small) and capped at 3 substantive items/day, preferring the most time-sensitive open tripwire. Explicitly scoped as mid-week reconcile that refills from the existing backlog only — not a structural replan, which still happens only on Sunday; elapsed blocks are just marked done, never backfilled. This is the rule behind today's Claude-Corps-early → Dr.-G-thank-you swap.

### 2026-06-20 (Sat)

Reconcile: no drift. Product repo last commit still the Jun 13 telemetry work; calendar matches the log; no new inbound on any tracked thread (Claude Corps "application is in" already logged Jun 18, no take-home/interview yet; nothing from Trice; no alumni replies). Confirmed against Gmail that the Dr. G thank-you had not been started (no draft existed).

Pillar 1 / prior-art:
- **US prior-art check DONE** (one of the three open Dr. G follow-throughs). Finding: no US equivalent of the sector-level small-business exposure screen exists. What exists is general trade data + official dashboards (USITC *Recent Trends in U.S. Services Trade* annual report w/ interactive sector dashboards; BEA Digital Economy series; WTO DDS; UNCTAD) and country-level policy indices (OECD Digital STRI; ECIPE DTRI) — none rank SME sectors by exposure to a specific digital-trade rule. Bonus: US sector data is richer than India's, so the modeled EBOPS→NIC crosswalk that limits the India build would be a much smaller problem in a US version. Real opening if he wants to pursue it.

Pillar 3 (network):
- **First alumni outreach message SENT — Daniel Anicito** (Fidelity Labs incoming APM, 2nd-degree, Purdue peer who just ran the APM process), as a LinkedIn connection note. Knocks the pillar off zero. Sent the night of Sat Jun 20 after a coaching call: the plan wasn't broken, the send was, so action tonight beat deferring to "fix the plan tomorrow." Trimmed the drafted note to LinkedIn's 200-char free connect-note cap. Verified live on the Sent invitations page. The other 17 sent invites are peers/classmates, not PM-funnel contacts — they don't count. Remaining 2 of 3 this week (Steven LaCroix queued) roll into the Sunday plan.

Pillar 3 / External (Trice):
- Surfaced from a WhatsApp screenshot that **Sudip Uncle replied Jun 16 "Sure in 1-2 days will close"** (missed in earlier reconciles). No intro by Jun 20, so Veer **sent a light nudge**. See the Trice entry in the external-relationships log.

Pillar 3 / External (Dr. G):
- **Post-call thank-you SENT 2026-06-20** (in-thread to badri@infisum.com). References (1) the India share + data check, (2) the US-version idea grounded in the prior-art finding, commits to building a US version (he had nudged Veer toward it): will start now and send an update at significant progress; confirms he'll follow up. Kept short to respect his time. The overdue tripwire is fully closed (insight-without-action loop converted again). **Flag for the Sunday Jun 21 session: a US version is now a committed Pillar-1 track — slot it into the plan there (scope, how it fits against the India dashboard + Daniels + study) rather than over-planning mid-week.**

### 2026-06-21 (Sun) — Sunday planning session

Reconcile (commits + calendar + Gmail, past 7 / next 14 days):
- **Product repo:** no new commits since Jun 13 (last is the GoatCounter site-code wire). The Jun 20 deep block "write the telemetry readout → PROGRESS + DECISIONS" did **not** happen — no DECISIONS entry, no readout. That day's real work was the US prior-art check + first alumni message + Dr. G thank-you. Telemetry readout still owed (slipped since ~Jun 12).
- **Dr. G thank-you: confirmed SENT** (final in-thread message 2026-06-21 05:30 UTC = late Jun 20 PT). Two earlier same-thread drafts (05:16, 05:19 UTC) are superseded versions, now redundant — flagged to trash.
- **Inbound:** Claude Corps "application is in" (already logged Jun 18); no take-home/interview yet. Nothing new from Trice (WhatsApp channel) or alumni. No other live tracked tripwires in Drafts.

**Scheduled-vs-done for the week (Jun 15–20):**
- Shipped: GoatCounter verify (Jun 16), AI Fluency course (Jun 18), Claude Corps SUBMITTED (Jun 18), Dr. G call (Jun 18, went well), US prior-art check (Jun 20), alumni msg 1 — Anicito (Jun 20), Dr. G thank-you (Jun 20).
- **Slipped hard — Pillar 2 metrics study went to ZERO.** Six study blocks were on the calendar (Mon Khan, Tue PM tutor, Wed Khan, Thu PM tutor, Fri Khan, Sat PM tutor consolidate) and `state.json` confirms zero sessions, every topic still "new," 0 attempts. The Jun 19 reconcile flagged alumni (0/3 at the time) but **missed that study was also at zero.**
- Slipped — alumni finished at 1 of 3 (only Anicito; LaCroix + cold lead never sent). Telemetry readout never written.

**Pattern named (no deep diagnosis):** the week had two big external events (the Dr. G call, the Claude Corps submission). Everything with a person waiting on the other end got done; the self-directed compounding work with no external deadline — metrics study — got sacrificed entirely. This is the insight-without-action pattern in its "reactive over proactive" form. The fix is not more study blocks (last week had six and got zero) but protecting fewer, cued, concrete study reps in the deep slot, in a week with no big external event to crowd them out.

**Week of Jun 22–27 commitments by pillar (calendar written directly, connector on):**
- **P2 (the week's priority):** establish the metrics habit. Study is the protected DEEP block 4 days — Mon (metric-tree baseline), Tue (NSM/guardrail + numerator-denominator), Thu (Khan: significance/CIs/p-values), Sat (metric-drop diagnosis + consolidate); plus a lighter secondary touch midweek. Implementation intention: *when I sit down with morning coffee, I open the tutor and do the first rep for 25 min before anything else.* First session just sets a baseline (lowest activation energy).
- **P1:** finish the owed telemetry readout (Wed deep → PROGRESS + DECISIONS); scope the **US version** as a tight v0 only (Fri deep scope + Thu secondary data pull) — reuse the India architecture, do not start a second build. The US version is now a committed track (told Dr. G he'd build it), but the India dashboard stays the differentiator and finishes its open items first.
- **P3:** 3 alumni messages, **front-loaded Mon–Wed** (LaCroix Mon, Akash Ravi Tue after a Mon comment, Allan Tan Wed) so they don't slip to a Saturday scramble. Draft for Allan in Tue secondary.
- Externship (Jul 6) is 2 weeks out; resume v1 (mid-July, carries the Daniels line) is the next pipeline item after that. Not this week.

---

### 2026-06-23 (Tue)

Tutor fix before P2 study starts. Veer flagged that he doesn't know any Pillar 2 topics and the tutor would quiz him on never-seen material. Ran a deep-research pass (5 fan-out search agents + 1 adversarial verification) on first-exposure pedagogy; wrote `context/study/research-first-contact-acquisition.md`. Finding: attempt-first / productive failure is a *consolidation* design that needs a prior-knowledge floor and fails/reverses for true novices (Sinha & Kapur 2021 g=0.36; Kirschner-Sweller-Clark 2006; worked-example effect g=0.48, Barbieri 2023; Alfieri 2011 enhanced-discovery d=+0.30 vs unassisted d=-0.38). Added a **first-contact teach mode** to `pedagogy.md` and `study-tutor.md`: a topic at `bloom_achieved` null / mastery 0 is taught first (explain + worked example + faded practice, questions woven in), and only switches to productive failure once it clears a floor (Bloom Understand/Apply + >=2 unaided-correct). Directly relevant to this week's P2-baseline priority — the first sessions are now teach-first, not interrogation.

Reconcile (start-of-session, Tue Jun 23): **Claude Corps REJECTED** — Greenhouse decision email arrived today; application not advanced for Cohort 1 (no take-home/interview reached), invited to reapply to future cohorts. This **closes the fork**: the four-pillar Summer-2027 PM plan stays the single primary track and the Purdue leave-of-absence question is moot (no four-pillar revisit triggered — the revisit was conditional on *advancing*, which didn't happen). Updated memory.md + key-dates.md pipeline row. No other live tripwires: two leftover superseded Dr. G drafts still sit in Drafts (harmless, flagged-to-trash since Jun 21); nothing new from Trice or alumni.

**Pillar 2: first tutor session ever — the pillar-at-zero is broken.** ~5 items, ~80% acc, first-contact/build mode. Metric trees taught and cleared to a floor (bloom Apply, mastery 0.45, yellow): he made the canonical mistake first — picking revenue (the goal) as the North Star — corrected after one prompt, then chose "completed deliveries" and decomposed it cleanly (active users x deliveries per user; placed avg delivery time as a deeper driver). Guardrails introduced but session ended before an unaided attempt (owed next session). Calibration habit not sticking: skipped the confidence number on 2 of 3 prompts. Next review of both topics: 2026-06-25. Emotional note: Veer took the Claude Corps rejection hard ("sad I got rejected so soon") and paused mid-session before resuming; handled directly, reframed as variance + fork-closing, then he came back and finished the reps.

---

### 2026-06-25 (Thu)

Reconcile (start-of-session, mid-week). Initial findings + a Jun 25 correction:
- **P2 metrics study is ON the board — pillar-at-zero broken (corrected).** The first reconcile read `state.json` as 0 sessions and I called it a second straight zero week. That was wrong: the tutor's close-out had not persisted the session yet. Once saved, `state.json` shows a **35-min first-contact session on Jun 23** — metric trees taught first-contact and cleared to an Apply floor (mastery 0.45, yellow; the goal-vs-NSM separation corrected after one prompt, then a clean decomposition), NSM/guardrail introduced but not yet retrieved unaided. First ever tutor session; the Jun 21 build-around (cued deep-block reps in a no-external-event week) produced its first rep. Open for today: both topics due for cold re-test (next_review 2026-06-25); calibration habit not sticking (confidence number skipped on 2 of 3 prompts — hold number-first every item).
- **System signal: state.json write lag.** The Jun 23 session existed but was not written to `state.json` until Veer manually triggered the save on Jun 25, which nearly made the reconcile misjudge reality. The tutor close-out should persist state at session end automatically — flag to verify/fix the close-out protocol so reconciles read truth (reality, not the doc, is source of truth — this is the case in point).
- **Telemetry readout still unwritten.** Product repo last commit is still Jun 13 (GoatCounter wire); no DECISIONS entry, no PROGRESS readout. Wed Jun 24's deep block slipped. The item has stalled since ~Jun 12 across many sessions — decomposed to the smallest physical action: paste the already-captured Jun 16 numbers (101 visits, 66% from LinkedIn, section-view funnel ~13→6) as a 5-line DECISIONS entry and commit. Marked a tripwire; naming it plainly — this is a parked task, not a hard one.
- **Alumni (LaCroix / Akash Ravi / Allan Tan): confirmed NOT sent (Veer).** Week finished 1 of 3 again. But the root cause is not P5 batching: Veer isn't following the Sunday calendar at all, because it is anchored to a 9am wake and he is waking **11am-1pm** (screen-driven late nights, behavioral not pure circadian). The entire fixed-9am plan misfires at the source, which is why outreach + study keep slipping regardless of the per-pillar fixes.
- **Study trace (P2 tutor session):** 2026-06-25: 6 items, ~92% accuracy, topics: metric trees, NSM/guardrail, numerator-denominator, significance/CIs. Cleared the week's due P2 topics. Metric-tree goal-vs-NSM crux **passed cold unaided** (0.45→0.62); guardrails taught then **2 unaided-correct → graduated past first-contact** (Apply, ~0.56); numerator-denominator taught, 1 borderline (per-day/per-user volume vs an eligible base) → 1 clean rep (~0.40); significance/CIs taught + 1 correct read (p>0.05 + CI includes 0 → don't ship, ~0.30). Calibration tell is **underconfidence** (60-80 on correct reads), not overconfidence. Two tutor system changes this session: (1) **confidence number is now a hard gate** (no grade until Veer gives a 0-100, every item) and (2) **state.json now writes after every item, not just at close** — the direct fix for the Jun 23 lost-session bug. Both wired into `study-tutor.md` / `pedagogy.md` / `state-spec.md`.
- **NEW WORKSTREAM — fix the sleep schedule + make the daily plan wake-anchored.** Veer's mechanism idea: send `initialize` each morning as a wake signal so the day's blocks build from real wake time instead of a fixed 9am. Target: consistent 9am by early Aug (before classes resume ~Aug 24 give external structure). Summer is the ideal window. A tailored deep-research prompt was drafted this session (behavioral/revenge-bedtime-procrastination primary, circadian light+low-dose-melatonin support for a ~2-4h advance, plus a recommendation on wake-anchored vs fixed scheduling). System wiring is a Sunday-grade structural change. **This is upstream of all four pillars** and likely the highest-leverage fix on the board.
- Two superseded Dr. G drafts (Jun 21) still in Drafts (today's small-item cleanup, not yet done). No new inbound on tracked threads since the Jun 23 Claude Corps rejection.

---

## Pillar 2 running ledger (technical)

Regenerated from `context/study/state.json` at each Sunday session - topics touched, mastery, weak topics, calibration, last-practiced. A passed week shows as stale last_practiced dates.

- **As of 2026-06-21: zero sessions logged.** All 10 P2 topics still `new` (mastery 0.0, 0 attempts, last_practiced null). Tutor installed 2026-06-14; no practice has happened in the 7 days since. Calibration: n/a (no data).
- **This is a pillar at zero for the week** — flagged at the Sunday session; the week of Jun 22 makes establishing the first reps the priority (metric trees, NSM/guardrail, numerator-denominator, significance/CIs, metric-drop diagnosis).

---

## Pillar 3 running ledger (network)

- Alumni messages sent: 1 (Daniel Anicito, Fidelity Labs incoming APM, 2026-06-20)
- Replies received: 0
- Conversations completed: 0
- Tracker: started 2026-06-09 — `alumni-tracker.md` (project root)
- Week of Jun 22 target: 3 sends (LaCroix, Akash Ravi, Allan Tan), front-loaded Mon–Wed. Note the LinkedIn free-connect-note cap (~3–5 personalized invites/month, ≤200 chars) — Anicito used one; mix connect-notes with comment-then-message for 3rd-degree contacts.

Note: Dr. G (Infisum) is the one live external thread — see the external relationships log.

---

## Pillar 4 running ledger (interview prep)

Regenerated from `context/study/state.json` at each Sunday session - topics touched, mastery, weak topics, calibration, last-practiced. A passed week shows as stale last_practiced dates.

- As of 2026-06-21: all 13 P4 topics still `new`, 0 attempts. Expected — interview prep ramps in Phase 2 (Aug–Oct per direction.md); not a focus this summer beyond keeping stories warm. Shipping + metrics study win through August.

---

## External relationships log

### Dr. Badri Narayanan Gopalakrishnan (Infisum)
- 2026-05-17: Resume sent
- 2026-06-02: Substantive follow-up sent — live guided-walkthrough site + de-identified repo + the exposure-score methodology question (Entry 008)
- 2026-06-13: Nudge sent (Gmail in-thread) — telemetry + Act IV caveat update + the EBOPS→NIC-crosswalk-as-screening-heuristic question
- 2026-06-14: Dr. G replied — "Thanks a lot Veer, let's catch up soon." Did not answer the methodology question in writing
- 2026-06-15: scheduling reply confirmed STILL UNSENT (sitting in Gmail Drafts, composed Jun 15). Queued as Monday's small item this week
- **2026-06-16 (~12:02am PT): reply SENT** (in-thread to badri@infisum.com) — proposed a 30-min slot Thursday 1pm, offered to flex. **Dr. G's appointment scheduler immediately BOOKED it: 30-min Google Meet, Thu Jun 18 2026, 1:00–1:30pm PT** (meet.google.com/vnx-fvoc-mgi). The stuck-draft tripwire is fully closed — insight-without-action loop converted.
- **2026-06-18: call RESCHEDULED to 3:45–4:15pm PT** (Dr. G's scheduler moved it the evening of Jun 17 from the original 1:00–1:30pm slot; same Meet link meet.google.com/vnx-fvoc-mgi). The new slot no longer collides with the workout (1:30–3:00).
- **2026-06-18: call DONE, went well.** Outcomes: Dr. G will share the dashboard with India policy contacts and check for usable data; he raised a US version as a possible direction (Veer to check prior art first). See the 2026-06-18 daily entry.
- **2026-06-20: thank-you SENT** (in-thread) — references the India share + the US-version idea, commits to building a US version (will start now, update at significant progress), confirms follow-up. **US prior-art check DONE** (no US equivalent of the SME-sector exposure screen exists; data building blocks do, and US sector data is richer so the crosswalk caveat shrinks).
- **2026-06-21 (reconcile): thank-you send CONFIRMED** (final in-thread message, SENT). Two leftover same-thread drafts are superseded versions — to be trashed.
- Status: **call complete; relationship now in active-routing mode.** A **US version is now a committed Pillar-1 track** (Veer told Dr. G he'd start it and send an update at significant progress).
- Next move: scope the US v0 tightly this week (reuse India architecture, do not rebuild); send Dr. G a progress update only at a real milestone; await his India intros/data.

### Trice Systems (via Sudip Uncle — family contact)
- 2026-06-15: Sudip Uncle (family friend, introduced through Veer's mom) offered intros to two of his contacts' companies — Trice Systems (Hyderabad hyperlocal MSME-commerce) and Mantrika.ai (AI HR-tech). He is closer to the Trice people and can get Veer started ASAP.
- 2026-06-15: Veer chose Trice and **sent a thank-you message + the Trice resume over WhatsApp to Sudip Uncle**. Awaiting the intro to the right person at Trice.
- 2026-06-16: **Sudip Uncle replied "Sure in 1-2 days will close"** (he expected to close the intro within 1-2 days). Logged from a WhatsApp screenshot Jun 20 — the reply had been missed in earlier reconciles.
- 2026-06-20: still no intro (4 days on, past his own 1-2 day estimate), so **Veer sent a light nudge over WhatsApp** ("checking in on the Trice intro whenever you have a moment, no rush").
- Next move: await the intro; when connected, find out role family / hours / remote-vs-onsite before committing; protect dashboard + Daniels. If no movement in another ~3-4 days, nudge once more or treat as cooled.

### Alumni / PM professionals
(Empty — Pillar 3 outreach starts week 3)

---

## System signals (Sunday-session-relevant only)

- Sleep: target 7-8 hrs, bedtime 1:00-1:30 AM. Not tracked daily here; flagged if it drops below 6
- Workout: 1:00-2:30 PM. Flagged if missed
- Sunday sessions: May 24 (logged); May 31 (architecture redesign shipped, Entry 009 — consistent with a Sunday session)
- Reply-to-daily-email rate: TBD (daily emails not yet confirmed running)
