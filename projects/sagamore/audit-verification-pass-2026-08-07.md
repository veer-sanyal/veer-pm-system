# Audit verification pass — 2026-08-07

**What this is.** The Aug 4 website and social audits were captured with headless Chrome, logged out. This pass re-ran every checkable claim in Veer's real, signed-in browser. It exists because several Aug-4 findings turned out to be artifacts of the capture method rather than facts about the client, and they were three days from reaching Bryon.

**Method note that explains most of the errors.** Headless, logged-out Chrome gets bot-blocked. Facebook served a login wall, Google and DuckDuckGo served challenges, and `beascout.org` returned 403 to a headless agent while returning a clean 301 to a real one. **Every Aug-4 claim that depended on an anonymous automated request needs to be treated as suspect until re-checked signed in.** That is the durable lesson, not any individual number.

**Two tooling limits found here, worth carrying forward:**
- `resize_window` reports success and does nothing when the Chrome window is maximized on macOS. It failed identically with one agent and with two. **A "mobile" number obtained by trusting that success message is a desktop number.** The workaround that does work: a same-origin iframe at 375x812, verified with `innerWidth` and `matchMedia('(max-width:600px)')` before trusting any measurement.
- `save_to_disk: true` returned capture IDs and wrote no files, on all three runs of the MCP browser. **Resolved a different way:** `projects/sagamore/tools/capture-audit-screenshots.sh` drives headless Chrome directly and writes real files, which is how the Aug-4 images were made in the first place. Thirteen `v2-` captures now back the public claims. What headless cannot reach — Facebook behind its login wall — is listed in `MANUAL-SHOT-LIST.md` for Veer to shoot himself. **Do not solve that by loading a browser profile; cookie stores are credentials.**
- **`web-05-beascout-403.png` has been renamed `WRONG-web-05-beascout-403-was-a-botblock.png`.** It is a picture of our own tooling being blocked, it was sitting in the evidence folder under a name that invited reuse, and a false image is more dangerous than a false sentence because nobody argues with a screenshot.
- **The capture script found a real defect on its first run:** `sagamorebsa.org/join/` is a hard 404. Every interior page is served from `sagamorebsa.org/htdocs/wordpress/`. The web-root misconfiguration was already noted as a low-priority item; it turns out to also mean the obvious URL for the join page does not resolve.

---

## WEBSITE AUDIT

| # | Aug-4 claim | Verdict | Verified fact |
|---|---|---|---|
| 1 | "CLICK HERE TO JOIN NOW" **403s** | **FALSE** | Href is `http://www.beascout.org`; it **301s to `https://beascout.scouting.org/` and loads**. The 403 was a headless bot-block. Residual real issue is minor: an unencrypted legacy domain reached via redirect. |
| 2 | A parent searching **cannot find the join path** | **FALSE** | `/join/` ranks **#1** for "sagamore council join" and **#2** for "boy scouts lafayette indiana". Homepage #1 for "sagamore council"; cub scouts #1 for "cub scouts lafayette indiana". |
| 3 | Word "join" appears **0 times** on the mobile homepage | **TRUE, mechanism corrected** | 0 occurrences at a verified 375px viewport. But it is **hidden, not absent**: `UL.nav-menu {display:none}` below 600px. Tapping the "Menu" toggle sets it to `inline-block` and the count goes **0 → 2**. Honest wording: *zero until you tap Menu.* |
| 4 | Mobile page **overflows 375px** horizontally | **FALSE** | `scrollWidth` 375 = `innerWidth` 375. No sideways scroll. |
| 5 | Donate button sits **~4,332px** down | **TRUE** | Measured **4,384px** on a 5,599px page — **78% down**. Links to donations.scouting.org. |
| 6 | Mobile header's **largest text reads "BOY SCOUTS OF AMERICA"** | **FALSE** | Largest visible text is **"Sagamore Council" (24px)**; the biggest element is the Scouting America wordmark image. "BOY SCOUTS OF AMERICA" appears only as small curved text inside the patch and in the logo's alt attribute. |
| 7 | Logo alt text is literally `alt="Boy Scouts of America"` | **TRUE** | Confirmed on `cropped-SC-Logo-3.jpg`. Still ~18 months past Scouting America's Feb 8 2025 renaming deadline. |
| 8 | `/join/` has **zero inbound links** | **TRUE** | Homepage carries 90 links, **zero** to `/join/`; `/cub-scouts/` also zero. Nav "JOIN SCOUTING" points **offsite** to beascout.scouting.org rather than to their own good page. |
| 9 | New Parents link carries a **`chrome-extension://` prefix** | **TRUE** | Href is literally `http://chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://scoutingevent.com/.../Parent_Guide_2022.pdf` — a pasted Adobe Acrobat extension path. Dead for every visitor. |
| 10 | **Cost stated nowhere** | **TRUE** | Zero dollar figures and zero occurrences of fee/cost/dues/price on the homepage or `/join/`. The only figures sitewide are on `/cub-scouts/`: **$225 early bird / $250 after June 2** — day camp, not membership. |

**New, and stronger than what it replaces:**
- **Sagamore is absent entirely from "how much does scouting cost."** Four peer councils rank on it (capitolareascouting.org, wdboyce.org, greaterlascouting.org, scoutingatl.org). This is the true version of the dead search finding: they rank fine on their own name, and are invisible on the question a new parent actually asks.
- **The `/join/` page's main content is a 768×1024 JPEG flyer (`Cub-Scouts-Rocks.jpg`) with `alt=""`.** All of its text is invisible to Google and to screen readers. Both images on the page have empty alt. This is the mechanism behind the page underperforming — and it is an accessibility failure as well as an SEO one.
- **At 375px the two header logos overlap**, the patch partially covering the wordmark.
- Site is served from `sagamorebsa.org/htdocs/wordpress/` — the install path leaks into every URL.
- `/join/` contains only 8 content links total.

**Not verifiable from this machine:** "cub scouts near me" — the browser geolocates to Mexico and returned Cancún troops. "cub scouts lafayette indiana" was substituted and is labeled as a proxy. **Do not present it as the same query.**

---

## SOCIAL AUDIT

| # | Aug-4 claim | Verdict | Verified fact |
|---|---|---|---|
| 1 | **3,512 followers** | **UNSOURCEABLE** | Logged-in Facebook shows only **"3.5K"** everywhere; mbasic is dead. Cite 3.5K or drop the digit. Page created Sept 25 2009. |
| 2 | **10 Reels**; best 9,300; worst 206; four biggest shot one day | **TRUE, numbers refreshed** | Exactly **10** reels. Views newest→oldest: 207, 844, 482, 698, 394, 3.4K, 3.5K, 2.3K, **9.4K**, 446. Best **9.4K** against ~3.5K followers. Worst **207**. The four biggest are a **contiguous block**, consistent with one shoot. **Dates not visible in the player — "December" is unverified.** |
| 3 | Named human + no link = 58/55/77; link posts = 2 and 10 | **HALF FALSE** | **The link penalty is real and brutal.** Across 20 posts, all five with external links scored 1, 1, 2, 4, 11. **The "named human" half is dead:** a photo full of Scouts scored **5**, while two person-free posts scored **29** and **56**. |
| 4 | The Aug 1 Eagle post re-ran the benchmark format (55 reactions, 27 shares) | **NUMBERS TRUE, READING WRONG** | **56 / 8 / 27.** But it is **not** a named-Eagle-Scout post — it is a generic branded graphic whose caption asks followers to *post their own Eagle year, troop number and city.* It is a **UGC prompt**, and that is what earned the 27 shares. Adults did reply with theirs. |
| 5 | Jun 28 benchmark: 132 comments / 770 interactions, best in 3 years | **TRUE, one label wrong** | **770 reactions / 132 comments / 6 shares = 908 total interactions.** 770 was reactions, not the total. Highest observed by ~3x (next best 279). "Best in 3 years" not verifiable without full history. |
| 6 | Six satellite pages, **2,863 followers**, four reactions on a shared post | **CORRECTED** | Takachsin Lodge **613** · Camp Buffalo **~1K** · Wabash Valley **376** · North Star **358** · Peshewa **332** · Wood Badge **100** ≈ **2,779**. **There is no "University of Scouting" page** — that is an event; the ~600 page is the Order of the Arrow lodge. The "four reactions" claim was **not verified**. |
| 7 | Content mix ~55% event promotion, ~0% for non-Scout parents | **HALF FALSE, HALF CONFIRMED** | Over 20 posts (Aug 7 → Jul 27): event promotion **25%**, recognition/celebration **45%**, service/admin **10%**, merch & camp life **15%**, unreadable 5%. **Aimed at a parent without a Scout: 0%. Confirmed.** Caveat: **6 of 20 are one Jamboree recap series**, so this window overstates recognition. |
| 8 | Instagram: 178 followers, 59 posts, dead 199 days | **TRUE** | **59 posts confirmed** (was flagged unsourced), **179** followers, 55 following, last post Jan 18 2026 = **201 days** today, 198 on Aug 4. |
| 9 | Linktree has no Join and no Donate link | **TRUE** | Eight items: Camp Buffalo RSVP → **National Jamboree Sign Up** → Jamboree Info → Website → Instagram → Facebook → LinkedIn → YouTube. No Join, no Donate. The "four days after the contingent came home" timing is **not verifiable** — Linktree exposes no dates. |
| 10 | Footer Twitter link 404s; X carries the old BSA logo | **TRUE, with a root cause** | `twitter.com/SagamoreBSA` → 404, because **that handle does not exist**. The real account is **@SagamoreCouncil**: 229 posts, 646 followers, joined Sept 2009, still using the **old round "BOY SCOUTS OF AMERICA" avatar**. Last post Jan 19. |

**New, and one of them is the best finding in either audit:**
- **The Aug 6 "Membership fee update" post drew 29 reactions, 26 shares and 19 comments — real questions about fees and renewal mechanics — and nobody from the council has answered a single one.** Put that beside the website audit: cost appears nowhere on 34 pages, and the council is invisible on cost searches. **Parents cannot find the price on the site, cannot find it in search, so they ask in the comments, and get silence.** One story, three independent sources, all verified.
- **X and Instagram both went dark on the same day, 2026-01-19.** That is a single abandonment event, not two separate lapses.
- **The Aug 1 neckerchief post is labeled "AI content" by Facebook.** For a youth-serving organization asking parents for trust, an AI label on a merchandise post is a brand risk worth one sentence.
- **What actually performs, from the 20-post table:** live recaps of things that happened (Jamboree Day 5 = **279**), people news (new District Executive = **69/22/8**), and service information (fee update = **29/19/26**). **Event promotion — 25% of their output — is among the worst-performing no-link content** (Trade-O-Ree 7, Eagle Reception 2). They are posting to fill events and it is the thing that works least.

---

## Privacy — must be handled before anything ships

Captures from this pass contain **identifiable minors**: the Jun 28 Eagle post and Jamboree posts 9, 11, 13, 15, 17, 19, 20, plus three post-sample frames showing nine children's faces and several commenters' full names. **No child's name was transcribed into any report, and none should enter the client version.** Any screenshot used in the deliverable needs cropping to metrics only.

This is the same class of issue as the live liability already flagged: the benchmark Eagle post was built from a photo taken off the dad's personal Facebook page — consent and copyright, on an image of a child, for a youth-serving org.

---

## What has to happen before Monday

1. **Strike the 403 and the "parent cannot find join" findings** from both the internal and client website audits. They are false and they are the most quotable lines in the document.
2. **Rewrite the reaction-spread finding** around the link penalty, and drop the named-human thesis. The `soc-06-facebook-embed.png` caption argues the dead version — it still proves the link penalty and should be recaptioned, not deleted.
3. **Re-caption the Aug 1 Eagle post as a UGC prompt**, and make "ask people to tell you something about themselves" the recommendation.
4. **Add the cost story** — invisible on site, absent from search, asked about in unanswered comments — as the lead finding across both audits.
5. Fix the follower figure to 3.5K, the satellite total to ~2,779, Takachsin instead of University of Scouting, and the content-mix percentages.
6. **Re-capture screenshots** if the client version uses images; this pass wrote no files.
