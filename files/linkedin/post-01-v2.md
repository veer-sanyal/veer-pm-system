# First LinkedIn post, v2 (fresh draft, 2026-06-10)

Built from scratch off `research-linkedin-presence.md` (hook / tension / substance / takeaway / invitation structure) and the accurate Entry 009 story: the no-hardcoded-numbers build rule catching the ~10x placeholder. Not derived from post-01-draft.md.

---

## Post body

I almost published "India's IP-licensing fees grew ~10x since 2005." The real number is 29.4x.

For the past three weeks I've been building a public dashboard on a question I couldn't find a clean answer to: which of India's small businesses (MSMEs) are most exposed to digital trade policy?

Early in the build I adopted a rule that felt like overkill for a student project: no hardcoded numbers. Every figure on the page has to be computed from the source data at build time.

Then the rule caught me. That ~10x line was a placeholder I typed while wiring up a chart. When the build computed it from the WTO dataset, the answer came back 29.4x: $0.67B in 2005 to $19.8B in 2025. The placeholder sounded plausible. Nobody would have questioned it. It was off by almost 3x.

The finished dashboard walks through WTO trade data and India's official MSME registrations, then combines them into a sector-level exposure index. The finding that surprised me most: what tops the index is "other business services" (consulting, accounting, legal, architecture). Consulting and professional services exports alone grew 13x since 2005 to $92B, while the rest of that category barely moved.

What I took away: in data work, plausible is the most dangerous kind of wrong. The 10x version would have shipped fine. It just wasn't true.

Live site: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/
Code and data pipeline: https://github.com/veer-sanyal/india-msme-digital-trade-exposure

For anyone who's built with public data: where do you draw the line between a good-enough estimate and a figure that has to trace to source?

---

## Posting notes

- **Attach `chart_B_ip_licensing.png`** (it is the story). Skip chart A in this post; it can anchor a follow-up post on the consulting finding.
- **Links in body is intentional**: your logged call (PROGRESS 2026-06-09) was artifact-access over the link-in-comment reach tactic, since the audience is alumni and recruiters who click through. The research backs the trade-off: link penalty exists but its size is refuted folklore.
- **Post when you have 60-90 min to reply to comments.** Your presence in the first hour matters more than any clock time (golden hour, verified; all "best time" tables refuted).
- Hashtags optional and low-stakes: if used, 3-5 relevant (e.g. #productmanagement #datavisualization #buildinpublic).
- The closing question is a real invitation, not engagement bait; answer early replies substantively.
