# Sagamore / Scouting America — STATE

Live state for the Purdue Daniels Externship client engagement. **This file owns it.** `memory.md`
carries a pointer and the pillar-level read only, the same contract stick-dev has (point, never
mirror). Two copies means one of them is lying by Tuesday.

Static brief (client, team, plan params, locked decisions): `externship-scouting-america.md`.
Narrative and reasoning trail: `PROGRESS.md` on the dates named below.

**Last updated: 2026-08-15** (Bryon CONFIRMED the new time: closing call is Mon Aug 17, 4:00 PM ET)

## Phase

**Overtime delivery.** The externship's official window was Jul 6 – Aug 1; the Aug 1 handoff passed
with no client contact, and the work resumed. The client relationship is warm — Bryon replied to the
Aug 4 promotional-calendar send with "This is an amazing start!!! Unbelievable work!!" after 15 days
of silence.

## Owner actions (Veer)

1. **Canva templates + Bulk Create — the Aug 10 deadline was MISSED (Veer confirmed 2026-08-15; trip
   + illness). Now slotted: Sun Aug 16, before the Mon final call.** Build exactly TWO Canva
   templates with field names matching the CSV columns, then run Bulk Create. Not one template per
   row: 76 of 156 rows need a graphic, the other 80 stay untemplated on purpose. Field spec and the
   two row-types: `sagamore-posting-toolkit-2026-08-04.md`. Both CSVs generated Aug 7, in
   `~/Downloads/`: `sagamore-bulk-event-posts.csv` (52 rows), `sagamore-bulk-education-posts.csv`
   (24). Regenerate with `tools/make-bulk-create-csv.py` if lost. If Sunday slips, the fallback is
   honest: demo one template live on the call and hand over the CSVs + instructions, do not claim
   finished graphics.
2. ~~Send the two audits to Izzy~~ **DONE — Veer confirmed sent (2026-08-15).**
3. **The Eagle-photo consent liability — second skip, does not get a third.** The benchmark Eagle
   post used a photo taken off a dad's personal Facebook page: consent and copyright, on an image of
   a child, for a youth org. It rides Monday's call agenda.

## Open queue

- **Closing call CONFIRMED: Mon Aug 17, 4:00 PM ET (1:00 PM PT).** Bryon replied Thu Aug 13
  2:57 AM ET on the "Final meeting" thread (Gmail thread `19fe6a87fd853589`): "I can do Monday at
  4:00 PM." Izzy cc'd throughout. **This is the last team meeting — agenda below.**
- **DONE 2026-08-15 ~9pm PT: real Teams invite SENT from Veer's Purdue Outlook** (organizer
  vsanyal@purdue.edu) for Mon Aug 17 4:00–4:45 PM ET, attendees Bryon.Haverstick@Scouting.org +
  iyura@purdue.edu + pgoswami@purdue.edu, Teams join link attached, client-facing agenda in the
  body (body was recipient-checked per the send protocol). Google Calendar synced: stale Thu
  placeholder retitled as moved (it was also 3h timezone-wrong), Mon 1:00 PM PT block created.
- **Final-call agenda (covering everything, since this closes the engagement):** (1) walk the
  delivered set — promotional calendar, both audit halves (Veer's conversion/cost/accessibility +
  Izzy's design markup), posting toolkit/templates; (2) the mix recommendation — keep-alive posts
  vs membership-moving posts are different jobs, label them so Bryon knows which rows he can phone
  in; (3) **the Eagle-photo consent flag — third listing, cannot skip again** (photo of a child
  taken off a dad's personal Facebook page; consent + copyright for a youth org); (4) what happens
  after: where the files live for him, who he contacts, the thank-you/close.
- `sagamore-package-monday` guard: retired 2026-08-15 — the call is confirmed and booked-by-email;
  delivery rides the call itself now.
- ~~UNVERIFIED after the trip~~ **Resolved 2026-08-15 by Veer directly: audits went to Izzy;
  Canva/Bulk-Create did not happen** — see owner action 1.
- **Unconfirmed:** whether Prisha's Canva templates are DONE with a date. "The templates are good"
  is not that claim.
- **Veer's synthesis, still to be written into the calendar:** keep-alive posts and membership-moving
  posts are different jobs and must be labelled differently, so Bryon knows which rows he is allowed
  to phone in. (From Prisha's point that Bryon does not have to originate every post — reposts,
  holidays and seasonal touches keep the page alive at near-zero effort.)
- **Two stale Bryon drafts still in Gmail Drafts** (`r-2984936810873573256`, `r1375487513162206080`,
  both Aug 4, "Scouting America meeting" thread), superseded by the Outlook send Bryon praised.
  Kill both, send neither.

## What is delivered

- **Promotional calendar** — sent Tue Aug 4 2:08 AM ET from Purdue Outlook to Bryon + Izzy + Prisha
  (SharePoint xlsx, describe-and-offer tone). Bryon's reply is above. Built by
  `tools/add-observance-layer.py` (month-long and single-day observances incl. Scout Sunday layered
  onto the v0.2 posting calendar, with a `Status` column so it reads as a menu to approve, not a
  commitment), then run through `tools/make-client-copy.py`.
- **Two audits, done Aug 4, verified Aug 7** — browser-driven vision passes with screenshots,
  read-only, sourced to named publications. Internal: `sagamore-website-audit-2026-08-04.md` ·
  `sagamore-social-audit-2026-08-04.md`. Client versions: the two `CLIENT-*.md`.
  - **Website:** the word "join" appears nowhere in the mobile homepage text; cost is stated on none
    of 34 pages; the mobile header's largest text reads "BOY SCOUTS OF AMERICA"; the good `/join/`
    page has zero inbound links.
  - **Social (the stronger one):** 11 accounts not 6; Facebook Reels are an abandoned reach machine
    (best 9,300 views vs 3,512 followers, worst 206 on a link-led Reel); named-human-no-link scored
    58/55/77 against 2/10 for link posts; six satellite pages returned four reactions from 2,863
    followers; the Linktree has no Join and no Donate link; **parents comment their children's names
    and nobody replies** — the FOS list identifying itself.
  - **Retired by the Aug 7 verification pass** (`audit-verification-pass-2026-08-07.md`): the join-link
    403 was a bot-block, and "a parent cannot find the join path" was false. Do not re-raise either.
- **Izzy's half, received Aug 7** — handwritten markup over dated screenshots: homepage hero
  redesign, an event grid of equal-sized click-through photo cards, move the trading-post block,
  center the uniform section, an FAQ page, "still says Boy Scouts", blurry logo, bold the pre-camp
  swim-check line, format the two Cub camps consistently. Does not collide with Veer's.

## Build

- `tools/build-audit-html.sh` — self-contained HTML with screenshots embedded → `build/`. This is
  what the client receives.
- `tools/build-audit-docx.sh` — editable Word, styled from `audit-reference.docx`.
- `tools/capture-audit-screenshots.sh` / `capture-facebook-screenshots.sh` → `audit-screenshots/`.
- `build/` is gitignored: the source is versioned, the deliverable is one command. Do not commit it,
  and do not leave the only copy on the Desktop.
- **Before sending anything from here, read it as the recipient** — the send protocol in the root
  `CLAUDE.md` exists because this project is where it failed on 2026-08-04.
