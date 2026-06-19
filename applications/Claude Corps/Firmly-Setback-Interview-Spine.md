# Firmly Setback — Interview Spine

Defensible delivery prep for the "tell me about a setback / failure / what changed" story. Grounded in `context/applications/profile/experience-firmly.md` and short answer 2 of the Claude Corps packet. Built because the worry isn't honesty (every detail here is real), it's reconstructing a 15-month-old project under pressure. Re-read this for 10 minutes before any interview. You freeze when you try to recall live; the fix is to overlearn the spine and bridge to the present, which you know cold.

---

## The 15-second hook (memorize this, lead with it)

"At my Firmly internship I shipped a fix for a payment-checkout failure, tested it the way the bug was reported, and called it done. Days later it failed again on a slightly different case. The fix wasn't wrong — my definition of done was. So I built a process to catch my own mistakes before a user does, and I still work that way."

Everything else hangs off that. If you blank, say the hook and keep going.

## STAR breakdown (60–90 seconds out loud)

- **Situation.** Firmly is a fintech / e-commerce checkout platform. Small team, remote, summer 2025. PayPal checkout failures were dropping users on a generic error page.
- **Task.** I owned building a failure-recovery flow — replacing that dead-end error page with a guided recovery path — and fixing a specific payment-failure bug inside it.
- **Action (the setback).** I shipped the fix, validated it against the path the bug was reported on, and called it done. A few days later it failed again in a different case — missing billing data instead of missing shipping data — and a user hit the same dead end we thought we'd closed.
- **Result + what changed.** Root cause was mine: I'd validated one path and assumed the rest held. I built an edge-case matrix (20+ test cases) plus a release checklist covering the high-risk payment paths, and ran every fix through it before calling anything done. The team adopted it as the standard for verifying fixes, and the cannot-reproduce bugs dropped off. The durable shift: assume I'm probably wrong until I've checked.

## Numbers and facts to have straight

- **~15** high-risk payment edge cases I validated the original fix against.
- **20+** test cases in the QA matrix I built (don't conflate the two numbers — a probe may test whether you know your own work).
- Role: **Product & Engineering Intern, Jun–Aug 2025**, remote.
- Built **server-side error logging** (Node.js / Express) capturing request context + exception states → improved triage; tracked **error rate and recovery rate** as the signal.
- The recovery flow **replaced a generic error page** with a guided recovery path.

## The bridge to the present (your strongest move)

When they ask "how do you work differently now," do NOT stay in 2025. Jump to work you remember in full:

"On a data dashboard I shipped this spring I made a rule to compute every number from the source data instead of typing it in, and it caught a figure I'd carried over that was off by about three times — before any viewer saw it. Same instinct Firmly taught me: find the hole yourself and fix it quietly."

This is the answer to the actual question. Firmly is the origin; the dashboard is the living proof. The present-day example is unimpeachable because you built it weeks ago.

## Likely probes and honest answers

- **"What was the actual bug?"** → A PayPal recovery path failed when an expected field was missing. I'd verified the reported case (missing shipping data); it later failed on a different missing field (billing). Honest tag if pressed on specifics: "exact field mapping is fuzzy 15 months on, but the failure mode was a recovery path I'd verified too narrowly."
- **"Give me examples of those edge cases."** → missing billing data, missing shipping data, expired session, declined-then-retry, partial address. (Have 3–4 ready; you don't need all 15.)
- **"How did you know the fix held after that?"** → the matrix + release checklist run before "done," plus the server-side logging giving real recovery-rate and error-rate signal, so I wasn't guessing.
- **"What would you do differently?"** → write the failure matrix before the fix, not after the incident. Treat "it worked once" as a hypothesis, not a conclusion.
- **"How does this connect to working with AI output?"** → it's the same problem one level up: people trust AI output they can't easily check. The habit I built is verifying before trusting, which is exactly what you need when the output looks confident and might be wrong.
- **If you sense you're getting vague** → say it plainly: "This was 15 months ago so some specifics are fuzzy, but the habit it created is one I used last week." Self-aware honesty reads as strength here; bluffing detail reads as weakness.

## Delivery reminders (your known failure mode)

- Target 60–90 seconds. Don't narrate a framework out loud ("first the situation, then…"); just tell it.
- Pre-answer routine: one slow exhale, then the hook sentence. Don't start until you've said the hook in your head.
- It's a story about catching your own mistakes — let it be a little self-critical. That's the point, not a risk.
