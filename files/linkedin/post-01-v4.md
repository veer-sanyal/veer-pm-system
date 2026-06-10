# First LinkedIn post, v4 (2026-06-10)

Built from the full research original (`files/research-linkedin-presence.md`) and the product repo's `DECISIONS.md`. Keeps v3's finding hook (no Entry 009 error-catch story) but adds what the decision log uniquely offers: the named user and policy anchor (Entry 012), the consulting numbers (Entries 010/011), and the ship-v0-honestly call (Entry 008). The research basis: build-in-public content that shows judgment is the verified high-fit type, and "specificity is the substitute for authority."

---

## Post body

India's consulting exports grew from $6.8B to $92B since 2005. They sit in a category most analyses skip past: "other business services."

I found this while building a public dashboard over the past three weeks. The question: which of India's small businesses (MSMEs) are most exposed to digital trade policy?

I built it for one concrete user: a trade-policy analyst who, when something like the WTO e-commerce moratorium is on the table, has to decide which sectors deserve a deep dive. That one choice shaped everything downstream: sector-level rankings instead of the firm-level index the public data can't actually support, direction over false precision, and methodology caveats on the page instead of buried in a footnote.

The build: joined WTO services trade data to India's official MSME registrations through an industry crosswalk, then ranked all 11 service categories with a first-version exposure index. What topped it wasn't computer services, India's famous export line. It was "other business services." Disaggregated, that's almost entirely a consulting story: legal, accounting, and management consulting, roughly $90B in cross-border trade flowing through a sector with about 92,000 registered small firms.

The index is deliberately labeled v0: two components, equal weights, and an open methodology question (how do you honestly combine a firm count and a dollar flow into one score?) that I'm bringing to a domain expert instead of tuning alone.

The lesson I keep coming back to: the most useful decision in this project wasn't technical. Naming one real user and one live policy turned a vague "exposure score" into an answer to a question someone actually asks.

Live site: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/
Code and decision log: https://github.com/veer-sanyal/india-msme-digital-trade-exposure

For anyone who builds data products: where do you draw the line between shipping a v0 metric with known limitations and waiting until the methodology is defensible?

---

## Why this version (traceability)

- Hook: concrete number-led line (research: "concrete beats clever"; the $6.8B to $92B line is Entry 011's finding).
- User-and-policy paragraph: Entry 012's canonical-user decision. This is the PM-judgment signal the research says substitutes for seniority.
- $90B vs 92k firms: Entry 010. The single most quotable contrast in the log.
- v0 honesty paragraph: Entry 008 (ship simplest visible version, frame the question, bring it to the expert). Preempts methodology pushback in comments and turns it into the conversation you want.
- Closing question targets builders and PMs, invites substantive replies (golden-hour mechanism, verified).
- "Code and decision log" framing makes DECISIONS.md itself part of the artifact a recruiter clicks into.

## Posting notes

- **Attach `chart_A_consulting.png`** (13x consulting surge vs flat remainder; matches the hook).
- Links in body stays your call (06-09 decision: artifact access for alumni/recruiters over the unverified link-penalty dodge).
- Post when you have 60-90 min to reply; seed the conversation by answering early comments substantively.
- Hashtags low-stakes, 3-5 if used: #productmanagement #buildinpublic #datavisualization
- Supersedes v2 and v3; pick this one unless you want the shorter v3.
