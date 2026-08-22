# Jane Street SP: what actually gets tested, and what to be fluent in before submitting

Researched 2026-08-22. First-party sources marked **[JS]**; everything else is converging
third-party report and is marked as such. Posting: `listing.md`. Form: `application-form-answers.md`.

## The process, first-party

**[JS]** SP interviewing page, verbatim on structure:

> "The process typically includes an online assessment, one or two video interviews, and a final
> round of in-person interviews."

| Stage | What it is **[JS]** | Length |
|---|---|---|
| 1. Online assessment | "multiple-choice and short-answer questions" | "typically takes an hour" |
| 2. Video interview(s), 1-2 | "longer form problem-solving exercises intended to explore how you gather and apply new information... a full-time SP poses a few hypothetical business scenarios and logic puzzles for you to work through together in real time" | not stated |
| 3. In-office final | "a day of in-office interviews... more challenging questions that are representative of SP work... both qualitative and technical areas" | a day |

**[JS]** Also worth knowing before submitting: every application "is reviewed by an actual human"
and they "respond to every application we receive, ideally within a week or so." So this is not a
black hole. Submitting produces a real signal fast.

## The line to take seriously, and the line to read carefully

**[JS]** "Our interviews are designed to require no preparation. We're most interested in
evaluating how quickly you learn and how you approach solving interesting problems, not in testing
any prior knowledge or frameworks you may bring with you into the interview."

That is true in a precise sense and false in a dangerous one.

**True:** there is no body of content to memorize. No finance. No frameworks. **[JS]** on the
trading side: interviews "won't require previous knowledge of finance or involve any complicated
math, such as what you might learn in a higher-level math course in college." **[JS]** three things
they say explicitly not to worry about: prior financial knowledge, a particular major, and coding
experience ("Understanding the information flow and interactions of technical systems is a
necessary skill for SPs, writing the code to support them isn't").

**False as commonly read:** "no preparation required" does not mean preparation does not help. It
means the *content* is not the gate. **Fluency is.** Nothing above is hard mathematics; all of it
is middle-school-to-early-college probability. The failure mode is not "did not know the formula."
It is **knew the formula and could not execute it in six minutes while talking.** That gap is
entirely trainable, and it is the whole reason to drill before submitting rather than after.

## What they are grading

**[JS]** "The strongest candidates are sharp, logical thinkers that can communicate clearly and
concisely. They enthusiastically engage with the problem space and interviewer, and they're capable
of **quickly updating and incorporating new information into their solutions.**"

**[JS]** Their own four-step instruction, from the trading interview page, and it reads as house
style rather than a trading-only rule:

> Approach the problem methodically. Communicate clearly. **Correct your mistakes.** Ask why.

**[JS]** On the final round: "we don't expect you to immediately understand the details or nuances
of the domain at hand. Instead, we encourage you to **ask clarifying questions**, explore natural
extensions of the problem, and **take the time to build confidence in your answers**."

Read those together and the grading rubric is not "right answer." It is: state your reasoning out
loud, put a number on your uncertainty, update visibly when the interviewer adds information, and
catch your own errors before they do.

## Proficiency spec, in priority order

### Tier 1: the OA gate. This is what stands between submitting and stage two.

Third-party and converging across guides, not first-party: HackerRank, roughly 4 modules,
~10 questions in 60 minutes, math / probability / reasoning rather than coding, escalating
difficulty, mix of multiple-choice and fill-in-the-blank requiring chart or data interpretation.
Treat the format as likely and the ~6 minutes per question as the real constraint.

1. **Expected value as a reflex.** Single stage, multi stage, and EV with an option to stop or
   re-roll (optimal stopping). The canonical shape: "roll a die, keep it or reroll once, what is
   your strategy and what is the EV?"
2. **Basic probability mechanics.** Complementary counting, independence, unions and
   intersections, at-least-one problems.
3. **Conditional probability and Bayes.** The rare-disease / accurate-test shape, stated in words
   rather than symbols.
4. **Combinatorics.** Combinations vs permutations, binomial probabilities.
5. **Canonical dice and coin results** worth knowing cold so they cost zero time: expected number
   of flips to the first head, E[max of two dice], expected rolls to see all six faces.
6. **Arithmetic without a calculator, fast.** Fractions, percentages, ratios. Whether a calculator
   is allowed is not documented anywhere; assume not.
7. **Reading a chart under time pressure** and pulling the one number the question needs.

### Tier 2: the video round.

8. **Structuring an ambiguous business scenario out loud.** Reported prompts include designing a
   car rental system, optimizing restaurant reservations, and evaluating a new auction format.
   These are not case-framework questions. Decompose, name assumptions, quantify, revise.
9. **Game theory basics.** Dominant strategies, first-price vs second-price auctions, information
   asymmetry, adverse selection.
10. **Estimation / Fermi.** Order-of-magnitude with stated assumptions.

### Tier 3: the in-office final.

11. **Market making.** Quoting a two-sided market, spread widening with uncertainty, and what it
    means to get picked off by someone who knows more than you.
12. **Confidence calibration.** Reported: candidates are given poker chips and asked to bet on
    their own answers, and to state confidence intervals on random quantities. A 99% interval means
    you would put up 99 chips to win 1.

## The personal read, and it is not comfortable

**Tier 3 is where his known weakness lives.** `memory.md` records the calibration tell as **three
straight over-confident reads**, with "confidence-number-first" already a hard gate in the tutor
protocol. `context/study/state.json` puts **significance and confidence intervals at 0.15 mastery,
the weakest of four active topics**, and the file has been cold since 2026-07-03.

So the single trait Jane Street built a poker-chip exercise to measure is the exact trait this
system has already flagged him on, twice, independently. That is not a coincidence to shrug at. It
is the highest-value thing to train, and unlike the probability content, it does not improve by
reading.

**Order of work:** Tier 1 to clear the OA, calibration threaded through every session from the
start, Tiers 2 and 3 after the OA is passed and a video round is actually scheduled.

## Sources

**[JS] first-party:** janestreet.com/join-jane-street/sp/interviewing, /trading-interviews/,
/join-jane-street/interviewing/, and the SP posting itself.
**Third-party, converging:** interviewquery SP guide, aptitudeprep OA guide, Wall Street Oasis
final-round threads, Glassdoor SP intern reports. Verified 2026-08-22. Re-check before the OA
actually arrives; format details are the kind of fact that expires.
