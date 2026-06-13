# First LinkedIn post, v5 (2026-06-13)

Spined on the build discipline per Veer's reframe: the value of computing every figure from source isn't "I caught a wrong number" (that proves nothing). It's that a computed figure is accurate today and self-updating tomorrow, so there are no stale hardcoded constants to chase down when the data changes. The 29.4x IP-licensing figure is the concrete instance, not the lesson.

Incorporates the critical audit of v4: drops the $90B/92k overstate (it implied $90B flows through 92k small firms, which the modeled crosswalk can't support), fixes number hygiene (one number per figure), tightens to a single spine, and trims to one link in the body.

---

## Post body

There isn't a single hardcoded number on the dashboard I shipped this month. Every figure is computed from the raw data at build time.

First, what it is. Over the past three weeks I built a public dashboard that ranks India's service sectors by how exposed they are to digital-trade policy, things like the WTO e-commerce moratorium. It's built for one user: a trade-policy analyst who, when a policy is on the table, has to decide which sectors are worth a deep dive. Every score links back to the source data behind it.

Now the rule, and why it mattered. When I built the chart for India's payments for use of intellectual property, the number in my head was "about 10x since 2005." Round, memorable, easy to drop into a caption. Computed from the source, the real figure is 29.4x: $0.67B in 2005 to $19.8B in 2025.

The point isn't that I caught a wrong number. It's why I'd stopped typing numbers in by hand at all. A hardcoded constant is a guess that's wrong the day you write it and stale every day after. When the WTO updates the dataset, a "10x" in a caption just rots there until someone notices. A figure computed from source is right now and updates itself on the next build. One rule, no maintenance.

That same discipline is why I trust the headline result: the sector most exposed isn't software, India's famous export line. It's consulting and professional services. Not a result I went looking for, just the one the pipeline returned. The one thing the public data genuinely can't support, a firm-level link between a sector's trade and its small firms, is labeled on the page as a modeled assumption rather than buried.

Live walkthrough: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/

For people who build data products: where's your line between a figure you compute live and one you'll hardcode for speed?

---

## Why this version (traceability)

- Spine: build discipline, not the error-catch. The lesson is future-proofing and zero stale-constant maintenance (Veer's reframe, 2026-06-13). The 29.4x is the concrete example that makes "a guess goes stale" vivid, not the moral.
- Structure (Veer's note, 2026-06-13): first post, cold audience, so keep the hook but orient before the figures. Opener hook -> "First, what it is" (project in plain terms: what, for whom, the question) -> "Now the rule" (the 29.4x example + the discipline) -> finding + caveat -> link + question.
- Hook: the 29.4x / $0.67B-to-$19.8B figure (PROGRESS 2026-06-09; product DECISIONS Entry 009). Concrete and number-led (research: "concrete beats clever," "specificity substitutes for authority").
- Build-in-public over promotional, with a real "what surprised me" beat (consulting over software) — the verified high-fit content type.
- Fixed from v4: dropped the "$90B through 92k firms" line. It implied the trade flows through the small firms; the EBOPS-to-NIC crosswalk is a modeled assumption and direction.md flags it as the first thing a sharp reader probes. Replaced with the qualitative consulting-over-software surprise, which is safe and still non-obvious, plus an explicit on-page-caveat sentence.
- Number hygiene: one figure stated once. v4 wobbled between $90B and $92B in a post whose whole credibility play is computed-not-hardcoded.
- Length: single spine, ~290 words. The strongest line (29.4x) is in the first three lines, above the fold.
- Links: one link (live walkthrough). Repo link dropped from the body — the profile already carries both in Featured and About (the one 3-0 verified posting finding: links in static fields, not bodies). Keeping one live link is the deliberate June-9 call (artifact access for the alumni/recruiter audience); the redundant second link is what gets cut.
- Close: one genuine question to builders/PMs, on-topic for golden-hour seeding. Not engagement bait.

## Posting notes

- **Chart:** pair with a retitled Chart B (the IP-licensing 29.4x chart). The current Chart B title is the error-catch framing this version rejects, so it needs a new title before use. New title and the regeneration constraint are in the chat. Do not reuse the old Chart B title.
- Alternative with zero rework: Chart A (consulting) already carries "Every figure computed from the raw data" in its source line and needs no changes, at the cost of illustrating the consulting finding rather than the 29.4x example.
- Post when you have 60-90 min to reply; seed early comments substantively (golden hour, verified).
- Hashtags optional, 3-5 if used: #productmanagement #buildinpublic #datavisualization
- Supersedes v2, v3, v4.
