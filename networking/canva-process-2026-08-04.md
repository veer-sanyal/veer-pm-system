# The Canva process, step by step

> How the promotional calendar turns into actual posts. Written for Veer to run, and for Bryon to run
> after the externship ends. Companion to `sagamore-posting-toolkit-2026-08-04.md` (the why) and
> `sagamore-social-audit-2026-08-04.md` (what actually performs).

## Before anything: what this does and does not solve

**Read this first or the rest is wasted effort.** The social audit measured his own page over four days:

- Posts with a named person and no link: **58, 55, 77** reactions
- Posts with a registration or shop link: **2 and 10**
- Best Facebook Reel: **9,300 views against 3,512 followers.** Worst: 206, and it opened with a pasted link

**Canva touches none of the winners.** The Reels are a phone camera. The named-person posts are a real
photograph and someone's words. Neither needs a template and neither should get one.

What Canva is for is the **76 rows out of 156** where a graphic genuinely helps: the event promotions
(52) and the community education posts (24). Those have to exist, because events have to be promoted.
This process makes them cost one sitting a month instead of thirty ten-minute sessions.

**The other 80 rows are marked `Real photo, no graphic` (52) and `Phone camera` (28) in the workbook and
they must stay that way.** Running them through a template would actively make the feed worse.

---

## Step 1 — Canva for Nonprofits

Apply at **canva.com/canva-for-nonprofits**. Sagamore Council is a 501(c)(3), which is the eligibility
bar. Approval grants full Canva Pro to up to **50 users**, free, permanently.

You need Pro for the two features this whole process rests on: **Brand Kit** and **Bulk Create**.

**This is an application, not a signup.** Canva reviews it and decides, so start it before building
anything. Have the EIN and the determination letter to hand.

**While waiting:** everything in Step 2 except Brand Kit can be built on a free account. Bulk Create is
the part that is gated.

---

## Step 2 — Brand Kit (once, about 30 minutes)

Brand Kit is the thing that means nobody ever makes a design decision again.

1. Canva home, left sidebar, **Brand** → **Brand Kits** → **Add new**.
2. **Colours.** Pull the exact hex values off the current logo rather than eyeballing them. Add the
   Scouting America palette plus one accent for urgency bands (the LAST CALL strip).
3. **Fonts.** Two, no more. One for headlines, one for body. Set the heading, subheading and body slots.
4. **Logos.** Upload the current Scouting America Sagamore Council mark. **Do not upload the old Boy
   Scouts of America patch.** If it is not in the kit, nobody can accidentally use it, which is a real
   risk given the website header still shows it.

Once this exists, every template pulls from it, and a volunteer who has never designed anything cannot
produce something off-brand.

---

## Step 3 — build the two templates (once, an evening)

This is the part Veer does and hands over.

**The critical rule: the text field names must exactly match the CSV column headers.** Canva's Bulk
Create auto-matches by name. Get this right and it is one click; get it wrong and it is dragging fields
by hand across 52 designs.

The columns, from `tools/make-bulk-create-csv.py`:

```
DATE · KICKER · HEADLINE · STORY_ANGLE · OBSERVANCE · NOTE
```

### Template A — event posts (52 rows)

Create → **Instagram Post (Square)**, 1080x1080. Square is the master because Magic Resize handles the
rest later.

Layout, top to bottom:

| Element | Field | Notes |
|---|---|---|
| Small all-caps strip at the top | `KICKER` | LAST CALL / COMING UP / SAVE THE DATE. Accent colour behind it. This is the urgency signal. |
| The largest text on the design | `HEADLINE` | The event name. Should be readable as a thumbnail on a phone. |
| Small line beneath | `DATE` | |
| Optional small line | `OBSERVANCE` | Only populated on some rows; the design has to look right when it is blank |
| Logo | fixed | From Brand Kit |

**Build it as a frame around a photograph, not a solid colour card.** In Canva: **Elements → Frames**,
drop a frame covering most of the canvas, and place the text over a darkened overlay on top of it.

This matters more than any other design choice on this page. A graphic with no faces has never worked on
this council's feed. The template's job is to make a real photo look finished, not to replace it.

**Name each text field:** click the text box, then the **⋮** menu → **Rename**. Type the column name
exactly, in caps. Do this for all five.

### Template B — education posts (24 rows)

Same construction. Fields: `KICKER` (defaults to DID YOU KNOW or HOW TO JOIN), `HEADLINE`, `OBSERVANCE`.

These are the recruitment-adjacent posts, the ones about cost, time, where to start, what a den meeting
looks like. **They are the only posts in the calendar aimed at a parent who does not already have a
Scout**, which the social audit found to be roughly 0% of current content. Treat them as the most
important 24 rows in the file.

### Design check before you leave

- Does it read at thumbnail size on a phone?
- Does it still look right when `OBSERVANCE` is empty? Most rows have nothing there.
- Does the longest headline in the CSV fit? Check "Membership / Recruitment (spring + fall)".
- Is there room for a face in the photo frame, not just a landscape?

---

## Step 4 — generate the CSVs

Already done, and re-runnable whenever the calendar changes:

```bash
python3 tools/make-bulk-create-csv.py \
  ~/Downloads/"Sagamore Council Promotional Calendar - Draft.xlsx" \
  ~/Downloads
```

Produces `sagamore-bulk-event-posts.csv` (52 rows) and `sagamore-bulk-education-posts.csv` (24 rows), and
prints how many rows it skipped on purpose.

**Re-run it after Bryon answers the open questions**, since his answers will change dates and add or drop
observances.

**For a monthly workflow, filter to next month first.** Bulk Create caps at 300 rows, so the full year
fits in one run, but generating twelve months of graphics at once means twelve months of stale photos.
One month at a time.

---

## Step 5 — Bulk Create (about 20 minutes a month)

1. Open Template A.
2. Left sidebar → **Apps** → **Bulk Create**. (Sometimes under **More**.)
3. **Upload data** → select `sagamore-bulk-event-posts.csv`.
4. Click **Auto-match fields**. If the field names were set correctly in Step 3, everything binds at
   once. If not, drag each data field onto its text element.
5. Select the rows for the month you are producing.
6. **Generate.** Canva opens a new design with one page per row.
7. **Now the part that actually matters: drop a real photograph into each frame.** This is the slow step
   and it is the whole point. No photo means no post; run it as a Reel or a Story instead.
8. **Share → Download → PNG → All pages.**

---

## Step 6 — schedule in Meta Business Suite, not Canva

Canva's Content Planner works, but it **cannot schedule Reels, Stories or carousels**, and it caps at 25
posts per rolling 24 hours. Meta Business Suite publishes one composition to **multiple pages** at once,
which is the actual problem given the council runs seven Facebook pages.

**Design in Canva, schedule in Meta.**

1. business.facebook.com → **Planner** → **Create post**.
2. Select the council page. Per the social audit, **do not select the three district pages** — 2,863
   followers across the satellites returned four reactions on a shared post.
3. Upload the PNG, paste the caption, set the date and time.
4. Instagram crossposting: only if the Instagram account is revived. Currently it has been dormant since
   January and the recommendation is to park it.

Meta schedules server-side, so nothing needs to be running at post time.

---

## Step 7 — captions

Bulk Create makes images, not words. The reusable prompt is in
`sagamore-posting-toolkit-2026-08-04.md`, written to work on a free Claude account so it does not create
a subscription dependency.

**One rule that overrides everything the prompt produces: no link in the post.** Measured on this page,
link posts got 2 and 10 reactions against 55, 58 and 77. If there is something to register for, it goes
in the **first comment**.

---

## The month, end to end

| | Time |
|---|---|
| Filter the schedule to next month, re-run the CSV script | 5 min |
| Bulk Create both templates | 20 min |
| Drop in real photographs | 45 min |
| Write captions | 20 min |
| Schedule everything in Meta Business Suite | 30 min |
| **One sitting** | **~2 hours** |

Then, through the month, and this is the part that produces the results:

| | Time |
|---|---|
| One raw vertical Reel at each event already being attended | 10 min per event |
| The weekly named-person post | 15 min per week |
| Replying to commenters by name | 10 min per week |

**About two hours a month plus twenty-five minutes a week**, against the roughly fifteen hours a month
the current one-post-at-a-time approach costs. And the weekly items are the ones the data says actually
reach people.

---

## What breaks and how to tell

- **Auto-match does nothing.** The field names do not match the CSV headers exactly. Rename the text
  fields, caps and underscores included.
- **Blank gaps on some designs.** Rows with an empty `OBSERVANCE` or `STORY_ANGLE`. Expected. The design
  has to tolerate it, which is why it is checked in Step 3.
- **Headline overflows.** Canva does not auto-shrink in Bulk Create. Either shorten the headline in the
  source workbook or set the text box to shrink-to-fit before generating.
- **Bulk Create is missing from the sidebar.** It is Pro-only. The nonprofit application has not come
  through yet.

---

## The honest limit

Everything above solves production. **It does not solve photographs**, and photographs are the actual
constraint. The best post this council has ever run was a real picture of a named boy with his father's
own words.

The $0 version of a fix: a standing request in the monthly newsletter, one shared album, and a named
photo volunteer per district. Plus a photo release line on pack and troop registration, which also
settles the permission problem the social audit flagged.

Without that, this pipeline produces well-branded graphics with nobody in them, which is a worse feed
than the one they have now.
