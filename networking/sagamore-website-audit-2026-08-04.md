# Sagamore Council website audit — 2026-08-04

> **INTERNAL VERSION. Do not send as-is.** Run the same pass the workbook got before this reaches
> Bryon: no third-person references, no meta-commentary, no notes about our own process. See CLAUDE.md
> "Before telling him to send anything."
> Site: **sagamorecouncil.org**, which redirects to **sagamorebsa.org**. Audited desktop 1280x800 and
> mobile 375x812. Deliverable for the externship's "adjustments to the council website" ask.

## The headline measurement

A 25-year-old parent of a kindergartener lands on the mobile homepage:

| What they need | Clicks | Result |
|---|---|---|
| What it costs | any number | **Not on the site anywhere.** The membership fee is never stated on any of 34 pages. |
| How to join | 2 taps | Menu, then "Join Scouting", which leaves for the national BeAScout page with a blank ZIP field. |
| Nearest unit | never | The site does not name a single pack, troop or town. |
| When it meets | never | No meeting day, time or cadence on any page. |

**The word "join" does not appear anywhere in the rendered text of the mobile homepage** (verified in
browser: `indexOf('join')` returns -1 across all 2,628 characters of visible body text). The nav
collapses behind "Menu" and the homepage content offers a popcorn sale, a Trade-o-Ree and a merit badge
workshop.

**The Donate button sits 4,332px down the mobile homepage — 5.3 full screens.** On desktop it is a
prominent sidebar button; on mobile the sidebar drops below all content.

Both of Bryon's stated goals, money and new kids, are structurally unreachable on the device his
priority audience uses.

## Findings, ranked

**1. The main join button is broken (403).** The Cub Scouts page and `/join/` both link to
`http://www.beascout.org/`, which returns a CloudFront "403 ERROR. The request could not be satisfied."
The working URL is `https://beascout.scouting.org/`, which the top nav already uses correctly. Highest
intent click on the site, dead, no recovery path. **10 min.**

**2. Cost appears nowhere, and the only price shown is wrong by ~3x.** Every dollar figure sitewide:
license plates ($40), a 2025 bike ride ($17-60), Cub Day Camp ($225/$250), donor cost-per-Scout ($153),
honorarium levels ($50). The national membership fee is never stated. So the only price a parent meets
on the Cub Scouts page is **"$225 early bird / $250 normal"** for an optional day camp, and they
conclude that is what Cub Scouts costs. For the query "how much does cub scouts cost", four peer
councils rank and Sagamore does not, because no such page exists. Peer wording worth copying: Atlanta
Area Council states pack dues "typically range from $40 to $85 annually"; Simon Kenton lists national
and council fees as separate line items. **45-60 min, and it is the highest-return hour on the site.**

**3. On mobile the largest text in the header reads "BOY SCOUTS OF AMERICA."** The council patch image
overlaps the wordmark by 169x71px, covering **57%** of it, cutting it to "Scouting Sagam...". The patch's
boldest text is the old name. Compounding: the logo's alt text is literally `alt="Boy Scouts of
America"`, all 28 content pages carry "Trademark 2013 Boy Scouts of America" in the footer, the domain
is sagamore**bsa**.org, and the Google Business Profile still reads "Sagamore Council - Boy Scouts of
America". **Source: Scouting America's own Digital Renaming Guidance** (filestore.scouting.org, SE
packet 2024-10-07): council websites "should be updated no later than **February 8, 2025**" and new
domains "should not contain the following abbreviations: bsa, sa." Sagamore is ~18 months past it.
Girls are 20-25% of new members; a mother of a daughter reads that header and self-selects out. One of
their own Google reviews reads "My daughter is a scout. Now I'm a den leader." **15 min** for alt text,
footer and GBP name; **1-2 hrs** for the header overlap.

**4. The best page on the site is orphaned.** `/join/` is genuinely good: big red join CTA above the
fold, a real warm photo of real kids that visibly includes a girl, den-by-grade breakdown, and the line
"Scouting is for the whole family! Boys, girls, moms, dads, step-parents, grandparents." **Zero of the
34 crawled pages link to it.** Not in the nav, not in the mobile menu, not in the site's own sitemap
page. The "Join Scouting" nav item bypasses it for the national site, so the council never learns who
was interested. Its "New Parents, Click HERE" link is
`http://chrome-extension//efaidnbmnnnibpcajpcglclefindmkaj/https://scoutingevent.com/...Parent_Guide_2022.pdf`
— someone pasted a URL out of their own Adobe Acrobat viewer. Dead for every visitor on earth; the fix
is deleting 52 characters. **15 min, the best 15 minutes available on this site.**

**5. Publicly advertised events that already happened.** Buffalo Stampede, a top-level nav item and the
council's main public-facing event, is entirely the 2025 edition ("Next event: Saturday, October 25,
2025"), over 9 months stale. The Cub Scouts page advertises June 2026 camp sessions ~6 weeks past.
Recharter describes a "NEW PROCESS... beginning March 1, 2024" 2.5 years later. **Friends of Scouting,
the main donor page, promotes AmazonSmile, which Amazon shut down in February 2023.** Contact Us lists a
North Star DE the council's own Facebook page replaced yesterday. **30-40 min, four 10-minute blocks.**

**6. Search engines are given almost nothing.** Zero meta descriptions. Zero Open Graph tags, so every
link Bryon posts to a 3,000-follower Facebook page renders as a bare URL with no image. No structured
data. No city name in any title tag. Both sitemaps broken in opposite directions: `wp-sitemap.xml`
regenerated this morning and contains **zero URLs**; the other has 39 URLs and a header reading
`generated-on="May 22, 2014"`, WordPress 3.7.1, all `http://`. No robots.txt. Every URL contains
`/htdocs/wordpress/`. Observed results: for "scouts Logansport Indiana" the council does not appear at
all; for "cub scouts Lafayette Indiana" four individual packs on free platforms outrank the council in
its own second-largest city; for "boy scouts Kokomo Indiana" a printer-cartridge store outranks it.
**Read: nobody is competing for these queries, which is why the fixes are cheap.** Adding city names to
3 title tags is **15 min** and the biggest single SEO win available.

**7. Every CTA button fails contrast, including Donate.** Donate, Contact Us, Submit Unit Service Hours
and Newsletter Archives all render white 18px text on mid-blue at **3.10:1**. WCAG 2.2 SC 1.4.3 (AA)
requires **4.5:1**; the large-text 3:1 exemption needs 24px, or 18.66px bold, so these do not qualify.
Footer "Email Marketing" is 2.85:1 at 10px. One hex change fixes all four. **20 min.**

**8. Mobile menu and tap targets.** The menu toggle is an `<h3>`, not a `<button>`: `tabIndex: -1`, no
`aria-expanded`, 11px text in a 52x30px box. **Keyboard users cannot open the navigation at all.**
Homepage event links are **19px tall** — below Apple's 44pt guideline, Google's 48dp, and the WCAG 2.2
SC 2.5.8 floor of 24px (though the inline exception arguably applies). The open menu is a flat wall of
33 links with section headers at the same visual weight as the links under them.

**9. Broken and misdirected links.** `beascout.org` 403s (x3). The chrome-extension Parent Guide link.
`www.new.campbuffalo.com` has no DNS record (drop the "new."). Contact Us renders
`Camp Ranger –sam.williamson@scouting.org"> Sam Williamson` as visible broken markup, leaking a staff
email in plain text and defeating the obfuscation plugin; the same malformed pattern appears on 10
pages. A Wabash Valley DE phone with a **865** area code (Tennessee) that may be a typo for 765.
**30 min for all of it.**

**10. Imagery.** 39 of 44 body images have missing or empty alt text (**89%**), failing WCAG 2.2 SC
1.1.1 (Level A). **The homepage contains zero photographs of youth** — every image is a logo, social
icon or event graphic. The Scouts BSA page's only real photo is `Camp-Buffalo-2012-133.jpg`, from 2012.
The Programs page has zero images. The University of Scouting graphic bakes date, venue and sponsors
into a JPEG with empty alt, invisible to Google and screen readers (WCAG 2.2 SC 1.4.5). The good news
is the `/join/` photo, the best asset on the site, which almost nobody sees. **45 min.**

## Sorted by who can do it

**(A) Bryon himself, 10-minute blocks, ~2 hours total.** Repoint the two beascout.org links (10) ·
point "Join Scouting" nav at `/join/` (10) · strip the chrome-extension prefix (5) · logo alt text (2) ·
footer trademark line (5) · delete AmazonSmile (5) · delete expired camp dates (10) · Buffalo Stampede
banner (10) · fix new.campbuffalo.com (3) · fix the Camp Ranger markup (10) · update North Star DE (5) ·
rename the Google Business Profile (5) · repoint the GBP website link over HTTPS (5) · city names in 3
title tags (15) · 3 meta descriptions (20). **If he does nothing else, the first three rows.**

**(B) A few hours, no outside help.** The "What Scouting Costs" page (45-60 min) · add cost, meeting
cadence and district towns to `/join/` (60) · rebuild the homepage above-the-fold around a join CTA and
the `/join/` photo (2-3 hrs) · alt text pass (45) · SEO plugin for Open Graph (45) · fix the sitemaps
and add robots.txt (45) · darken the CTA color (20).

**(C) Needs someone else, may be undoable at $0.** The mobile header overlap (theme CSS — the most
visible problem on the site and the one he is least able to fix; realistic route is a Scouting parent
who does web work, asked for as in-kind) · mobile menu semantics · **moving off `/htdocs/wordpress/`
URLs — recommend NOT attempting at $0**, the gain is smaller than the cost pages and a botched
migration is worse than the status quo · the domain migration off sagamorebsa.org, officially expected
but a project not a task · the national donation form at donations.scouting.org, which offers no
suggested giving amounts and still uses old BSA artwork, and which he almost certainly cannot change.

## Not checked, and it matters

- **The BeAScout ZIP search was not submitted** (read-only audit). So whether packs actually appear for
  Kokomo, Lafayette or Logansport ZIPs, with current meeting times and contacts, is unverified.
  **This is the highest-value thing Bryon should check himself, today** — if the pins are stale or
  empty, every fix above is moot, because the handoff lands on an empty result.
- No donation completed, so behavior past the first form screen is unknown.
- Scouting America's Brand Center is login-gated; the publicly hosted Digital Renaming Guidance PDF is
  cited instead.
- No indexed-page count (needs Search Console, which Bryon has).
- Two adjacent Google Maps entries ("BoyScouts of America", and a "Boy Scouts of America" with a
  1.0-star review) may be duplicates splitting local authority. Ownership unconfirmable from public
  data. Worth a manual check.
- WordPress admin not accessed, so theme-level effort estimates are ranges.

## Two things worth not breaking

**Speed is fine.** 91.7KB homepage, 0.35s TTFB, 0.41s total. Ignore anyone selling a performance plugin.

**The Google Business Profile is an underused asset:** 4.6 stars, 18 reviews, correct address, hours,
phone and category. The only defects are the name and the website link, both 5-minute fixes. Nothing
else on this list buys that much credibility that cheaply.
