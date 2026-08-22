# Jane Street SP Internship, application form answer key

Form captured 2026-08-21. Posting: `listing.md`. Resume: `VeerSanyal_JaneStreet_Resume.pdf`.
Nothing here is submitted. Veer presses submit.

## The one line on this form that changes strategy

> "When we receive an application, we consider it for all available positions worldwide to
> determine the best fit. If you are interested in additional roles or offices other than what
> you've applied for above, you do not need to submit multiple applications."

**One application covers every Jane Street role and every office.** This supersedes the earlier
note to pick one location before applying: there is nothing to pick, and no second application to
spend. The `key-dates.md` row has been corrected.

## Fields to fix before submitting

| Field | Currently | Should be | Why |
|---|---|---|---|
| Current or most recent employer * | `NA` | `Firmly` | Not true as filled. Firmly, Product and Engineering Intern, Jun-Aug 2025, is on the resume being uploaded. A reviewer who sees "NA" next to a resume listing three roles reads it as careless, and it is the one field on this form that directly contradicts the attachment. |
| How did you hear about us? * | `Bright Network` | whatever is actually true | Only Veer knows this. If it was a job board, a friend, a Purdue posting, or a search, pick that. It also has to match the free-text answer below, so set the dropdown first and tell me what it says. |
| Upload your resume as a PDF file * | empty | `VeerSanyal_JaneStreet_Resume.pdf` | Not yet attached. |

Correct as filled: name, email x2, phone, pronouns (his own selection), LinkedIn URL, no prior
Jane Street interview, currently a student, Purdue University, Purdue email, Undergraduate,
Integrated Business and Engineering, high school 2024.

Note there is no GPA field and no work-authorization question on this form.

## Free-text box

**Researched 2026-08-21 against Jane Street's own words. The first draft in this file was wrong
and has been replaced.**

### What they actually say

Jane Street's hiring FAQ, verbatim:

> "If there's something you think we should know about that doesn't fit nicely onto your
> resume/CV, feel free to include it in the text box at the bottom of our application. If not,
> feel free to leave this blank."

And on their interviewing page, asked whether a cover letter is needed: **"Nope!"**

The form itself repeats it: "We don't need a cover letter, but if there's additional information
that could be helpful..."

**So the box is an exceptions box, not a persuasion surface.** It exists to catch information the
resume format cannot hold. It is not a short-form cover letter, and a polished four-paragraph
essay with a thesis and a closing line is precisely the thing they said twice they do not want.
Submitting one signals that the applicant did not read the instruction, at a firm that lists
"exceptional attention to detail" as one of four named traits. That is a real cost, not a
theoretical one.

The first draft in this file was exactly that mistake: a cover letter wearing a text box.

### The test to apply

Their test, used literally: **does this thing belong on the resume, and did it fail to fit?**

| Candidate content | Passes? | Why |
|---|---|---|
| Cairn (github.com/veer-sanyal/cairn) | **Yes** | Genuinely cut from the resume for space this session, verifiable in `match-map.md`. Public artifact, unprompted external adopter. Cannot be seen any other way. |
| Interest in the London and Hong Kong offices | **Yes** | The form explicitly names this box as where to indicate interest in other roles or offices. Literally the stated use. |
| "How I handle being wrong" narrative | No | Persuasion, not information. This is interview material. |
| IBE degree, SMIF, STICK, the externship | No | All on the resume. Repeating them wastes the one signal the box carries. |
| How he heard about them | Only if the dropdown is incomplete | There is a dropdown for it. Worth a line only if the true answer has detail the dropdown cannot express, e.g. a specific person. |

### Draft, informational register, no thesis and no closing flourish

---

One thing that did not fit on my resume: I open-sourced Cairn
(github.com/veer-sanyal/cairn), a tool that scaffolds long-lived AI agent systems around a North
Star metric, an input-lever metric tree, and guardrails. The part I spent the most time on is a
research engine that tries to refute its own claims before it will use them. Someone I have never
met found it, used it, and forked it to extend it further.

I applied to the New York posting and would be glad to be considered for London or Hong Kong as
well.

---

**Use the second paragraph only if it is true.** Drop it if he wants New York specifically.

**If the whole thing feels thin, that is correct and intended.** Blank is an answer Jane Street
explicitly endorses. Two accurate sentences beat four persuasive paragraphs here.

## The thing that actually decides this application

Not the resume, and not the box.

Jane Street's own SP interviewing page describes the first stage as an **online assessment,
multiple-choice and short-answer, about an hour.** Third-party guides (interviewquery,
aptitudeprep, candidate reports) consistently characterize the SP version as **HackerRank, roughly
4 modules and ~10 questions in 60 minutes, math / probability / reasoning rather than coding,
weighted toward expected-value intuition and problems built to reward cleverness over brute
force.** First-party confirms the format and length; the probability-heavy characterization is
third-party and should be treated as likely but unverified.

**This matters more than anything else in this folder.** Submitting starts that clock, and
`context/study/state.json` has been cold since 2026-07-03, with significance and confidence
intervals sitting at 0.15 mastery, the weakest active topic. Expected value under time pressure is
a trainable skill and the single highest-leverage prep for this application. Route it through
`/tutor` before submitting, not after the OA link arrives.

Jane Street also states there is **no GPA or degree requirement** and that they "hire students of
all tenures from many different universities," which removes the last thing that could have
screened him out.

Sources: janestreet.com/join-jane-street/interviewing, .../sp/interviewing, the Gradcracker Jane
Street hub FAQ, interviewquery, aptitudeprep. Verified 2026-08-21.

## What the resume-side draft refuses to do

- **No inflation.** The study app is "built and deployed," never in production and never with
  students, which it does not have. Every number traces to a profile file.
- **Cairn adoption phrased at n=1**, honestly: "someone I have never met found it, used it, and
  forked it," never "users," never a count.
- **No em dashes**, per the outbound-artifact rule.
