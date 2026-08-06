# RCAC / GenAI Studio call prep: Mihir Ahlawat

> **HISTORICAL — the meeting RAN Thu Aug 6, 2026.** Outcome in `ledgers.md` (Ahlawat entry) and PROGRESS.md 2026-08-06. Thank-you: `ahlawat-thankyou-2026-08-06.md`.

**Thu Aug 6, 2026 · 12:00-12:30 PM ET (11:00 AM Riviera Maya) · Microsoft Teams**
Join: https://teams.microsoft.com/meet/258962435270761?p=FQVKuikV9gfYFyI6n3 (also on the Outlook invite and mirrored Google event)

Only 30 minutes. Lead with capacity; everything else is negotiable.

## Who he is and why this call exists

Mihir Ahlawat (mahlawat@purdue.edu), Senior AI Scientist at RCAC. He saw both tickets (#1585167 "is API access available", #1594129 cost/allocation + model access), skipped the help-desk queue, and emailed directly Jul 30: "I would like to set up a meeting to discuss your questions." He is warm, he initiated, and he is the person who runs the service STICK's entire cost model depends on (D41: institution-hosted inference at ~zero marginal cost).

**What this call feeds:** S-01, the project's single biggest open dependency. OD-163's options (probe first / hybrid / move everything / stay on Gemini) are all blocked on facts only RCAC can supply or unblock.

## Opening (2 min)

Do NOT open with "is there an API." He knows you have the key and have probed it. Open with 30 seconds of context, then the probe result:

- Context: student-built study tool; ingests scanned exams with vision models, generates verified practice. The workload is not a human at a chat box: unattended pipeline jobs, per-page calls, JSON-schema outputs at temperature 0, 30-second timeouts, automatic retries.
- Probe result (Jul 30, ~10-min window): auth and `/api/models` work perfectly (200 in 620 ms, all 34 models listed). But every inference request returned HTTP 400 in ~5 s: `OllamaException: "server busy, please try again. maximum pending requests exceeded" ... Fallbacks=None` (stack is LiteLLM -> Ollama). Ruled out client error: 7 models from 1B to 32B across four families, including a minimal control body against the 1B model, all failed identically.
- Frame it honestly: one window, so you are not claiming the service is down; you are asking what the ceiling is and how a batch workload should live under it.

## The three real questions, in order

1. **Capacity / quota for unattended retrying jobs (the blocker).** Is the pending-request ceiling per-user or global? Is there a quota, queue, or batch tier for programmatic use, or is the API pilot sized for interactive chat only? What retry behavior does he want from clients? Was Jul 30 a transient spike or known chronic saturation?
2. **Cost / allocation path for a student-built app serving other students.** The pilot is free today; ticket Q4 (free vs charged) decides the cost model. What is the path when it is not one student's key but an app with N student users: an allocation request, a sponsored account, a research/education tier? Who approves?
3. **Model tag pinning + quantization.** `:latest` tags can move mid-semester (content-trust failure for already-verified material). Can explicit tags be pinned or guaranteed for a term? And which quantization builds are actually served (q4_K_M vs fp16 matters for extraction accuracy)?

## If time allows (in priority order)

- Does `response_format` / JSON schema survive the Open WebUI proxy? Every call in the pipeline puts a schema on the request; undocumented.
- Is there or will there be a fallback group? `Fallbacks=None` plus retries means a saturated provider looks identical to failed extraction.
- Vision throughput expectations for `qwen3-vl:32b` on shared hardware (per-page calls, 30 s timeout).
- Is there written guidance on rate limits anywhere, so this stops being tribal knowledge?

## Data points to have at hand

- Gemini baseline: ~35 cents per 14-page exam, n=1; 11/12 symbol-perfect extraction on the test corpus. This is the bar and the comparison instrument.
- RCAC's own Mar-2026 review: 1.7B tokens through the LLM API in Jan 2026, 2,500+ users, 30+ models, no Gemini. So the port is real work and worth their while to support.
- The endpoint is OpenAI-compatible; the ask is small and concrete, not "host my app."

## What a good outcome looks like (leave with these)

1. An answer, or a named owner, for the capacity/quota question.
2. The allocation/cost path named, even roughly.
3. Green light and method to run the cheap probe (a schema'd call + `qwen3-vl:32b` on the same 14 pages, scored against the Gemini baseline). This alone resolves OD-163 option A.
4. A standing channel: can Veer email him directly as this develops.

## Traps

- Do not commit to migrating anything. This call is measurement, not a decision.
- Do not ask what the docs already answer (endpoint, auth, model list). It burns credibility and the 30 minutes.
- Do not oversell the app's scale. Honest current state: working product, pre-pilot, one campus.
- If he buries Q4 (free vs charged), chase it specifically. It decides the economics.

## After the call, same day

- `/debrief`: log outcome, send the thank-you before end of day, set the next tripwire.
- Write results into stick-dev via its own session (OD-163 wants a measured ruling; do not commit there from this repo).
