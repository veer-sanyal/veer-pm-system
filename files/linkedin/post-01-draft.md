# First LinkedIn post — draft (2026-06-09)

Attach: `chart_A_consulting.png`. Links in body per the 2026-06-09 decision (artifact access over algorithm reach; audience is alumni/recruiters who click through).

---

India's consulting exports grew 13x since 2005, to $92B in 2022. Everything else in the same WTO services category barely moved past $16B.

I found this while building my first solo data project, which went live this week: an exposure index that connects WTO trade data to India's MSME registry to ask which small-business sectors have the most at stake in digital trade policy. Professional services come out on top, and the firms behind that category are mostly small ones: consultancies, accounting and legal practices, architecture and engineering firms.

One build rule shaped the whole project: no hardcoded numbers. Every figure on the site is computed from the raw source data at build time. That rule caught me once. An early placeholder said IP licensing fees grew about 10x since 2005. The computed answer was 29.4x, to $19.8B in 2025. The gap between what sounds right and what the data says is why the rule exists.

Live site: https://veer-sanyal.github.io/india-msme-digital-trade-exposure/
Code and data pipeline: https://github.com/veer-sanyal/india-msme-digital-trade-exposure

Built on WTO TiSMoS and DDS data plus India's Udyam MSME registry. The exposure score is v0 and I would rather have it pulled apart now than later, so if you work in trade, policy, or product analytics, tell me what is wrong with it.

---

## Design notes

- Hook: one number with stakes (13x, $92B vs $16B), matches the attached chart so the image confirms the claim instantly.
- Para 2 introduces the project in one sentence, then delivers the actual finding. No "excited to announce."
- Para 3 is the credibility beat: the accurate version of the error-catch story (build rule caught the placeholder, per DECISIONS Entry 009), not the "earlier note" misframe.
- Closer is a specific ask (critique the v0 methodology), not engagement bait. It invites the substantive comments alumni outreach can reference later.
- ~1,350 characters. Real paragraphs, not one-line-per-sentence. No em dashes, no hashtags.
- Known tradeoff: links in body suppress reach. Already decided 2026-06-09; audience is people, not the algorithm.
