# Sagamore Council Posting Toolkit

*Prepared by the Purdue Daniels externship team, August 2026*

The promotional calendar answers what to post and when. This document answers how to produce
those posts in the time you actually have: a $0 tool stack, about 2 hours of batching once a
month, and 10 minutes a day for the part that earns the most.

## The stack (all free)

| Job | Tool | Cost | Why this one |
|---|---|---|---|
| Design | Canva Pro via Canva for Nonprofits | $0 | Full Pro for eligible 501(c)(3)s, up to 50 seats |
| Batch generation | Canva Bulk Create | $0 (needs Pro) | CSV in, a month of graphics out, up to 300 rows |
| Scheduling | Meta Business Suite | $0 | Publishes one composition to multiple Pages, crossposts to Instagram, schedules Reels |
| Captions | Claude (claude.ai, free tier) | $0 | One reusable prompt, included below |

Design in Canva, schedule in Meta Business Suite. Canva has its own Content Planner, but it
cannot schedule Reels, Stories or carousels and it caps at 25 posts per rolling 24 hours.
With around six Pages to publish to, Meta Business Suite is the right scheduler.

## Step 1: Canva for Nonprofits (about 20 minutes, then a wait)

Apply at canva.com/canva-for-nonprofits. Sagamore Council is a 501(c)(3), which meets the
eligibility bar, but Canva reviews each application, so treat this as an application with a
wait rather than an instant unlock. It grants Pro features (Brand Kit, Magic Resize, Bulk
Create) to up to 50 users. This is the first thing to do, because Bulk Create is Pro only.

Once approved, set up the Brand Kit first: council colors and two fonts. After that, every
future post looks like the council without any design decisions.

## Step 2: the templates

The Templates folder in this package contains the Canva templates we built, exported as PDFs,
plus a link to the live Canva files. The two that matter for batching are matched to the two
CSV files, with text field names that line up with the CSV columns so Bulk Create's auto-match
works without dragging fields by hand:

- **Event template + `sagamore-bulk-event-posts.csv` (52 rows).** The KICKER field is the
  urgency band (LAST CALL, COMING UP, SAVE THE DATE) and the HEADLINE is the event name. It is
  built as a frame around a photo slot rather than a solid color card, because graphics without
  real photos have not performed on your pages.
- **Education template + `sagamore-bulk-education-posts.csv` (24 rows).** KICKER defaults to
  DID YOU KNOW or HOW TO JOIN. These are the recruitment posts (cost, time commitment, where to
  start, what a den meeting looks like), so each caption should carry the join link.

Only 76 of the 156 calendar rows need a graphic at all. The other 80 are real-photo or
phone-camera posts, and they should stay that way. That is where the engagement lives.

## Step 3: the monthly batch (about 2 hours, once a month)

1. Open the Posting Schedule tab of the calendar and filter to next month.
2. In Canva: Bulk Create, upload the matching CSV, auto-match fields, generate.
3. Drop a real photo into each generated design. This is the only slow part and it is the part
   that matters. If there is no photo for a post, run it as a story or a Reel instead.
4. Download all as PNG.
5. Meta Business Suite, Planner: schedule the month, with the Instagram crosspost toggle on.
6. Keep 10 minutes a day for replying to comments. That is the whole daily commitment after
   batching.

That turns roughly 15 hours a month of one-at-a-time posting into about 2 hours of batching
plus 10 minutes a day, and the 10 minutes go to the thing that compounds.

## Step 4: the caption prompt

Paste this into Claude (claude.ai, the free tier is enough), then paste the week's rows under it:

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

## What the numbers say should come first

From the social media audit, in priority order:

1. **A raw vertical Reel at every event you already attend.** Your ten existing Reels
   out-reach everything else on the page; the best hit 9,400 views against about 3,500
   followers, and it was an unedited phone pan of a room.
2. **Replying to commenters by name**, especially parents who comment their children's names.
   Ten minutes a day.
3. **This graphics pipeline** for the event and education posts that remain.

One standing rule: keep external links out of the post itself. In your recent posts, the ones
carrying a registration or shop link scored in single digits, while your Jamboree Day 5 recap
with no link took 279 reactions. Put the link in the first comment, except for the education
posts, where the join link in the caption is the point.

## Honest limits

- Canva for Nonprofits is an application. Canva decides, and it could be declined. If it is,
  Bulk Create needs a paid Canva Pro seat.
- Bulk Create makes images, not captions. The prompt in Step 4 covers the captions.
- The real bottleneck is photos, and no tool fixes it. A standing ask in the monthly
  newsletter plus one shared photo album is the $0 version. Without real photos the pipeline
  produces good-looking graphics with no faces, which is the format that has not worked on
  your pages.
- The caption prompt works on Claude's free tier. No paid account needed.
- Canva's Instagram scheduling and Meta Business Suite crossposting need an Instagram
  Business account linked to the Facebook Page, not a Creator account. Worth checking which
  one the council has.
