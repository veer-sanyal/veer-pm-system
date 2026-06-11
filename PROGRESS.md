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
- The Sunday session reviews the past week of entries to populate the Sunday email "last week's reflection."
- Pull GitHub commits before writing an entry so it matches what actually shipped.

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

---

## Pillar 2 running ledger (technical)

- SQL: 0 hrs
- Python outside project work: 0 hrs (Python is used heavily *inside* the project — `build_processed.py`, `build_msme_nic.py`, `build_site_data.py` — but dedicated pillar-2 skill-building has not started)
- System design: 0 hrs
- APIs: none yet

Status: not started. Gated behind the Pillar 1 milestone, which is now met — confirm start in a Sunday session.

---

## Pillar 3 running ledger (network)

- Alumni messages sent: 0
- Replies received: 0
- Conversations completed: 0
- Tracker: started 2026-06-09 — `alumni-tracker.md` (project root)

Note: Dr. G (Infisum) is the one live external thread — see the external relationships log.

---

## Pillar 4 running ledger (interview prep)

- Mock interviews: 0
- Solo reps recorded: 0
- PM books read: 0
- Frameworks practiced (CIRCLES, GAME, STAR): 0

Status: not started.

---

## External relationships log

### Dr. Badri Narayanan Gopalakrishnan (Infisum)
- 2026-05-17: Resume sent
- 2026-06-02: Substantive follow-up sent — live guided-walkthrough site + de-identified repo + the exposure-score methodology question (Entry 008)
- Status: awaiting reply
- Next move: if no reply by the agreed window, a brief nudge; otherwise respond to whatever he raises on methodology

### Alumni / PM professionals
(Empty — Pillar 3 outreach starts week 3)

---

## System signals (Sunday-session-relevant only)

- Sleep: target 7-8 hrs, bedtime 1:00-1:30 AM. Not tracked daily here; flagged if it drops below 6
- Workout: 1:00-2:30 PM. Flagged if missed
- Sunday sessions: May 24 (logged); May 31 (architecture redesign shipped, Entry 009 — consistent with a Sunday session)
- Reply-to-daily-email rate: TBD (daily emails not yet confirmed running)
