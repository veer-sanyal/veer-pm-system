# Sagamore posting toolkit — how the calendar actually gets posted

> Companion to `Sagamore Council Promotional Calendar - Draft.xlsx`. The calendar answers *what to post
> and when*. This answers *how to produce it in the time Bryon actually has*.
> Constraints it is built against: **$0 marketing budget, organic only, one person posting, ~30 min/day
> in 10-minute blocks across ~6 pages** (Bryon, Jul 20 call).

## The problem with the calendar as it stands

156 dated rows is 156 sessions. At 30 min/day that is roughly **15 hours a month**, and it front-loads
the boring half (making graphics) over the half that actually earns engagement (replying to people).
His own best post proves where the value is: the Jun 28 Eagle Scout post got 132 comments and ~770
interactions, his best organic post in three years, and it was a real photo plus a dad's quote.

## The stack

| Job | Tool | Cost | Why this one |
|---|---|---|---|
| Design | **Canva Pro via Canva for Nonprofits** | $0 | Full Pro, up to 50 seats, free to eligible 501(c)(3) |
| Batch generation | **Canva Bulk Create** | $0 (needs Pro) | CSV in, a month of graphics out, up to 300 rows |
| Scheduling | **Meta Business Suite** | $0 | Multi-page publish + IG crosspost + Reels, server-side |
| Captions | **Claude** (free tier is enough) | $0 | One reusable prompt, no install, no API, no permissions |

**Scheduling deliberately stays in Meta Business Suite, not Canva.** Canva's Content Planner works but
cannot schedule Reels, Stories or carousels and caps at 25 posts per rolling 24 hours. Meta Business
Suite publishes one composition to multiple Pages, which is the real problem given ~6 pages. **Design in
Canva, schedule in Meta.**

**What was ruled out and why.** Social-posting MCP servers (Postiz, Socialync, Outstand, Hootsuite
connectors) are all paid SaaS, which fails the $0 constraint. Building a direct integration fails
harder: publishing to a Facebook Page needs `pages_manage_posts` + `pages_read_engagement` +
`pages_show_list`, every one of which requires full Meta App Review with written justification and a
screencast per permission, decided on Meta's timeline with no guarantee. Computer-use automation fails
worst of all — it would run on Veer's machine with Veer's session and would need the council's
credentials, so it dies the day the externship ends. **Anything Veer runs is a dependency, not a
capability.** The test every option had to pass: does it still work in October when nobody from Purdue
is answering?

## Step 1 — Canva for Nonprofits (Bryon, ~20 min, then wait)

`canva.com/canva-for-nonprofits`. Sagamore Council is a 501(c)(3). Canva decides eligibility, so this is
an application with a wait, not an instant unlock. It grants Pro features (Brand Kit, Magic Resize,
Bulk Create, Content Planner) to up to 50 users. **This is the whole unlock and it is the first thing to
do**, because Bulk Create is Pro-only.

## Step 2 — the two templates (Veer builds, Bryon reuses)

Only **76 of the 156 rows need a graphic at all.** The other 80 are `Real photo, no graphic` (52) and
`Phone camera` (28), and they should stay that way — that is where the engagement lives.

Two Canva templates, with text fields named to match the CSV columns exactly so Bulk Create's
auto-match works without dragging fields by hand:

**A. Event template → `sagamore-bulk-event-posts.csv` (52 rows)**
Fields: `KICKER` · `HEADLINE` · `DATE` · `STORY_ANGLE` · `OBSERVANCE`
- `KICKER` is the urgency band: LAST CALL / COMING UP / SAVE THE DATE. Small, all-caps, top.
- `HEADLINE` is the event name. Largest element.
- Build it as a **frame around a photo slot**, not a solid-color card. A graphic with no faces is the
  format that has never worked for this council.
- Square (1080x1080) as the master; Magic Resize handles the rest.

**B. Education template → `sagamore-bulk-education-posts.csv` (24 rows)**
Fields: `KICKER` · `HEADLINE` · `OBSERVANCE`
- `KICKER` defaults to DID YOU KNOW or HOW TO JOIN.
- These are the recruitment-adjacent posts (cost, time, where to start, what a den meeting looks like),
  so every one of them needs the join link in the caption.

**Brand Kit first.** Council colors and two fonts locked in the Brand Kit means every future post looks
like the council without Bryon making a single design decision.

## Step 3 — the monthly batch (Bryon, ~2 hours once a month)

1. Open the Posting Schedule tab, filter to next month.
2. Open the matching CSV in Canva → Bulk Create → Upload data → Auto-match fields → Generate.
3. Drop a real photo into each generated design. **This is the only slow part and it is the part that
   matters.** No photo, no post: run it as a story or a Reel instead.
4. Download all as PNG.
5. Meta Business Suite → Planner → schedule the month, crosspost toggle on for Instagram.
6. Keep 10 min/day for replying to comments. That is the whole daily commitment after batching.

**15 hours a month becomes about 2 hours plus 10 minutes a day**, and the 10 minutes go to the thing
that actually compounds.

## Step 4 — the caption prompt (paste into Claude, free tier is fine)

Reverse-engineered from the Jun 28 Eagle Scout post, which is the only format with proof behind it:
real photo, a named real person, that person's own words, a short opening and closing written by Bryon,
one or two emoji. No stock language, no org-speak.

```
You write Facebook captions for Scouting America, Sagamore Council, a youth
organization in central Indiana. I am the only person doing communications and
I have about ten minutes.

Audience: mostly parents in their mid-20s to 40s with elementary-age kids, plus
donors and volunteers. We rebranded from Boy Scouts of America to Scouting
America and girls participate in every program, so never write "Boy Scouts" for
the organization.

The best post we have ever run was an Eagle Scout story: a real photo, the
boy's name, a direct quote from his dad, one opening line and one closing line
from me, an American flag and an eagle emoji. 132 comments. Copy that shape.

Rules:
- 4 to 6 short lines. No paragraphs.
- Name a real person whenever I give you one. Never write "a local Scout."
- Use their own words as a quote if I give you any.
- One clear closing line: what the reader should do next.
- One or two emoji, not more.
- No hashtags on Facebook. Up to five on Instagram, local ones.
- Never invent a fact, a name, a date or a quote. If something is missing, leave
  a [BRACKET] for me to fill.

Here is this week's schedule and what I have:
[paste the rows from the Posting Schedule tab, plus any photo, name or quote]

Write one caption per row. Facebook version first, then a shorter Instagram
version if the post is worth crossposting.
```

## Honest limits

- **Canva for Nonprofits is an application.** Canva decides. Not instant, and it could be declined.
- **Bulk Create makes images, not captions.** That is what the prompt above is for.
- **The real bottleneck is photos, and no tool fixes it.** The council needs a way to get real photos
  from unit leaders and parents. A standing ask in the monthly newsletter plus one shared album is the
  $0 version. Without it, the batch pipeline produces good-looking graphics with no faces, which is
  worse than posting nothing.
- **Do not assume Bryon has a paid Claude account.** The prompt is written to work on the free tier.
- Canva's Instagram scheduling needs an **Instagram Business** account linked to the Facebook Page, not
  a Creator account. Worth checking which one the council has — it also gates Meta Business Suite
  crossposting.

## Files

- `~/Downloads/sagamore-bulk-event-posts.csv` — 52 rows, event template
- `~/Downloads/sagamore-bulk-education-posts.csv` — 24 rows, education template
- Generated by `tools/make-bulk-create-csv.py` from the Posting Schedule tab; re-run it after Bryon
  answers the open questions and the calendar changes.
