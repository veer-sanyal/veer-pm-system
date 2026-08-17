# Sagamore / Scouting America — STATE

Live state for the Purdue Daniels Externship client engagement. **This file owns it.** `memory.md`
carries a pointer and the pillar-level read only, the same contract stick-dev has (point, never
mirror). Two copies means one of them is lying by Tuesday.

Static brief (client, team, plan params, locked decisions): `externship-scouting-america.md`.
Narrative and reasoning trail: `PROGRESS.md` on the dates named below.

**Last updated: 2026-08-17** (final closing call RAN — engagement in closeout)

## Phase

**Closeout.** The final closing call RAN Mon Aug 17, 1:00 PM PT (Teams: Veer + Bryon + Izzy +
Prisha). Went well: Bryon grateful, said the work will actually be used to make improvements and
that the team's input "would have a lasting impact." One deliverable-shaped promise came out of it:
**Bryon asked for a final consolidated ZIP of all deliverables.** That ZIP + the thank-you email
that carries it is the last owed artifact; when it sends, the engagement is closed.

Call honesty notes (Veer's own debrief, 2026-08-17): he did NOT go deep on the two audits — he
mentioned they exist as documents; Izzy did not walk her markup either. So **the ZIP and its email
carry the audit depth the call skipped** — the email should explicitly point Bryon at the two audit
reports as the place the recommendations are argued with numbers.

## Owner actions (Veer)

1. **`sagamore-final-zip` — assemble + send the consolidated deliverables ZIP with the thank-you
   email, from Purdue Outlook.** Contents = CLIENT copies only: promotional calendar xlsx, the two
   `CLIENT-*` audit HTMLs (and/or docx) from `build/`, the two Bulk Create CSVs + posting-toolkit
   instructions, Izzy's markup (her call whether it's included — ask her). **Every file gets
   recipient-checked per the send protocol before the ZIP is zipped** — this project is where that
   rule failed on Aug 4. Draft email staged in `networking/sends-2026-08-17.md`. Veer presses send.
2. **UNCONFIRMED from the call — ask Veer:** (a) did the Eagle-photo consent flag actually get said
   (it was the third listing)? (b) what was shown for the templates — did the Canva/Bulk-Create run
   happen Sunday, or did the honest fallback (demo + CSVs) run? Both answers gate what the ZIP can
   claim.
3. ~~Send the two audits to Izzy~~ **DONE (2026-08-15).**

## Open queue

- **`sagamore-final-zip` is the only live item** — see owner action 1. Everything else below is
  residue to clear when convenient.
- **Closing call RAN 2026-08-17, 1:00 PM PT** (confirmed Aug 13 on thread `19fe6a87fd853589`;
  Bryon formally Accepted the Outlook invite Aug 16). Outcome in Phase above. Call-prep one-pager:
  `call-prep-2026-08-17.html` — historical now.
- **Team close message staged** in `networking/sends-2026-08-17.md` — Veer wanted to say "good
  job" live but everyone dropped off when Bryon did; the group-chat message is the substitute.
- **Two stale Bryon drafts still in Gmail Drafts** (`r-2984936810873573256`, `r1375487513162206080`,
  both Aug 4), superseded twice over. Kill both, send neither.
- Retired with the call: the final-call agenda (delivered), the `sagamore-package-monday` guard,
  the keep-alive vs membership-moving labelling question (presented on the call as the mix
  recommendation).

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
