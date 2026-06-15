# Claude Corps Fellow — Application Packet

**Role:** Claude Corps Fellow (CodePath + Anthropic partnership)
**Apply at:** https://job-boards.greenhouse.io/claudecorps/jobs/4250200009
**Cohort 1 deadline:** July 17, 2026 (rolling review). Cohort 1 starts October 19, 2026.
**Decision on record:** Veer is applying and is willing to take a leave of absence from Purdue for the fellowship year (Oct 2026 – Oct 2027).

This is everything ready to paste in. Two things gate submission and only Veer can do them:

1. **Complete both Skilljar courses and download the completion certificates** (the application requires this AND an upload of the certificates as one document):
   - AI Fluency: https://anthropic.skilljar.com/ai-fluency-framework-foundations
   - Claude 101: https://anthropic.skilljar.com/claude-101
   These also quietly grade how you prompt, so do them yourself and take them seriously.
2. **Final review + submit.** I'm not auto-submitting an application that carries your personal data. Review, then submit.

A few fields below I left for you to confirm because I shouldn't guess them (work authorization, age, how you heard, demographics). They're marked **[CONFIRM]**.

---

## Short answer 1 — Community impact (350 words max)

> *Prompt: Tell us about something you've done that made a real difference for a community you're part of — a neighborhood, school, workplace, team, or any group you belong to. What was the problem, what did you do, and what drove you to put your time into it?*

In my second year at Purdue I joined EPICS, a program where student teams build real things for local organizations that cannot afford to hire engineers. My team's client was a small museum that wanted a rotating billboard display to pull foot traffic past its entrance. The project had stalled. There was a design on paper and no clear path to actually building it. I stepped in as build lead for a seven-person team.

The real problem was not engineering. It was that nobody owned the gap between a nice concept and a thing that exists. I broke the build into weekly tasks, ran the check-ins, and made the unglamorous calls. The hardest one was prism count. The original design called for 22 rotating prisms, but our checks on dimensions and cut angles showed that 18 would hold tolerance and still rotate cleanly. Cutting four prisms felt like losing ambition. It was actually the difference between a prototype the museum could use and one that looked good in a review and then broke.

What drove me was something I had been honest with myself about. I am quick to see what should be done and slower to do it. EPICS put a group of people and a real client on the other side of that gap, which made closing it non-optional. I did not want to hand a museum a polished slide deck when what it needed was a working object. We presented at two formal reviews to faculty, sponsors, and the museum, defended the trade-offs, and handed off something buildable.

The lesson stuck. The part of this work I care about is not the idea. It is whether something real exists and keeps running after you walk away. That is most of why this fellowship pulls at me. The whole point is to leave behind something that still works once you are gone.

---

## Short answer 2 — A setback and what changed (350 words max)

> *Prompt: Tell us about a time something went wrong — a mistake, a setback, or a plan that didn't work out — and what you learned from it. Focus on what changed: how do you think or work differently now because of that experience?*

Early in my internship at Firmly, a fintech checkout platform, I shipped a fix for a payment failure and called it done. I had tested it the way the bug was reported, and it worked. A few days later it failed again in a slightly different case, missing billing data instead of missing shipping data, and a user hit the same dead end we thought we had closed. The fix was not wrong. My definition of done was.

That one stung because it was a payment flow, the exact moment a customer is trying to give the company money. I had validated against the single path I was handed and assumed the rest would hold. They did not.

What changed is how I treat my own work. I stopped trusting that something works because it worked once. I built an edge-case matrix for the checkout flow covering around fifteen high-risk failure paths, plus a release checklist, and ran every fix through it before calling anything done. The team adopted it as the standard for verifying fixes, and our cannot-reproduce loops dropped.

The deeper shift was assuming I am probably wrong until I have checked. It shows up in everything I build now. On a data dashboard I shipped this spring, I made a rule to compute every number from the source data instead of typing it in, and that rule caught a figure I had carried over that was off by roughly three times. Same instinct Firmly taught me: catch your own mistakes before a user does.

I would rather find the hole myself and fix it quietly than defend work that does not hold. That habit, more than any single tool, is what I would bring to an organization where people are trusting AI output they cannot easily check themselves.

---

## Form answer key (paste-ready)

### Basics
| Field | Answer |
|---|---|
| First Name | Veer |
| Last Name | Sanyal |
| Preferred First Name | Veer |
| Email | **[CONFIRM]** Recommend your personal email (veer.orgami@gmail.com) over the Purdue one, since the fellowship may run during/after a leave from Purdue and you don't want to lose access mid-process. |
| Country | United States |
| Phone | 360-643-9424 |
| Location (City) | Sammamish, WA |
| Resume/CV | Upload `VeerSanyal_ClaudeCorps_Resume.pdf` (in this folder) |
| Pronouns | **[CONFIRM]** optional — fill if you want |
| Highest level of education completed | **[CONFIRM]** You're mid-degree, so the honest answer is "High school diploma/GED" or "Some college, no degree" — pick whichever the dropdown offers that matches "currently in college, no degree yet." |
| LinkedIn Profile | linkedin.com/in/veersanyal |
| GitHub/portfolio/personal site | https://veer-sanyal.github.io/india-msme-digital-trade-exposure/ (or github.com/veer-sanyal) |

### Eligibility / commitment
| Field | Answer |
|---|---|
| Legally authorized to work in the US? | **[CONFIRM]** — your call; the program cannot sponsor visas, so authorization is required to be eligible. |
| Will you ever require visa sponsorship (incl. F-1/CPT/OPT → H-1B)? | **[CONFIRM]** — answer honestly based on your status. |
| Fewer than 2 years of full-time professional experience? | **Yes** (internships and work-while-enrolled don't count toward the limit). |
| Can you commit to a full-time, in-person, one-year fellowship? | **Yes** |
| Willing to relocate? | **Yes** |
| 18 or older as of October 19, 2026? | **[CONFIRM]** — almost certainly yes; confirm. |
| Completed BOTH Claude 101 and AI Fluency? | **Not yet — do this first** (see gating items at top). Answer "Yes" only once done. |
| Upload completion certificates (one document) | Pending the two courses. |
| Earliest date you could start full-time | Recommend **10/19/2026** (cohort start). Put an earlier date only if you're prepared to leave Purdue sooner. |

### "Which of these have you done?" (check all that apply)
- **Built tech for a community org** — yes (EPICS: built a display prototype for a museum client).
- **Taught, tutored, or mentored** — **[CONFIRM]** check it if you've tutored/mentored anyone (you led/coordinated a 7-person EPICS team, which is arguably mentoring; your call).
- Worked or interned at a nonprofit — no (unless you count something I don't have).
- Volunteered 6+ months with one organization — **[CONFIRM]** EPICS ran ~5 months (Aug–Dec 2025), just under; check only if accurate.
- Community organizing / service program (AmeriCorps etc.) — no.

### "Which are you comfortable using?" (open a file and work without a tutorial)
- **Python** ✓
- **JavaScript / TypeScript** ✓
- **SQL** ✓
- **HTML / CSS** ✓
- Google Apps Script / no-code (Zapier, Airtable) — **[CONFIRM]** check only if true.

### "Which of these have you built?" (any context)
- **A script that cleans, merges, or analyzes data** ✓ (Python data pipeline for the dashboard)
- **A dashboard or data visualization** ✓ (the MSME dashboard; StudyFlowForge dashboards)
- **A simple website or web page** ✓ (the static dashboard site)
- **Something that uses an API** ✓ (Gemini API; telemetry events)
- **A chatbot or tool that uses Claude / another LLM** ✓ (Gemini integration in StudyFlowForge; built the dashboard with Claude Code)
- Optional link: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/

### Host-org domains (select up to 3)
Recommended fits for your background (your call):
1. **Small business and entrepreneurship** (your dashboard is literally about MSMEs / small business exposure)
2. **Civic technology and government services** (the dashboard serves a policy-research use case)
3. **Education** (StudyFlowForge; you build for students)

Alternatives if you'd rather: Financial health and economic opportunity; Workforce development and job training.

### Other
| Field | Answer |
|---|---|
| How did you hear about Claude Corps? | **[CONFIRM]** (e.g., Anthropic website) |
| CodePath member or alum? | No (**[CONFIRM]**) |
| Accommodations for interview? | **[CONFIRM]** your call |
| Research opt-in (optional) | **[CONFIRM]** your call; opting in or out does not affect selection |
| Voluntary self-identification (gender, race, veteran, disability) | **[CONFIRM]** entirely voluntary — your call, does not affect selection |

---

## What happens after you submit
Interview process per the listing: short application → a take-home assessment → a 25-minute conversation → a final-round "Super Day" of two 1:1 conversations. If selected, you then interview with 2–3 host organizations to match.

## Strategic note (for the record)
This path replaces the Summer 2027 PM internship plan, not supplements it. If you advance, we should revisit the four-pillar plan and the Purdue leave-of-absence logistics deliberately, not by drift. The dashboard (Pillar 1) doubles as your strongest Claude Corps artifact, so continuing it stays the right move either way.
