# tldr sections — Chapter 9: Delegation, Trust, and the Supervisory Role

Source: `chapters/09-delegation-trust-and-the-supervisory-role.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 0 deferred · course film: carries the course credit (bookloop exception)

Chapter status the file itself carries: header comment `CHAPTERIZED 2026-07-02 … Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved` — but the body holds ZERO in-line `[verify]` flags; nothing below is chapter-flagged. Figures 9.2–9.4 are referenced by caption but no `images/09-*` files exist (0 found), so every "figure" named below is a caption, not a drawing — it will be REBUILT as Manim regardless (REBUILD LAW). One internal inconsistency to carry into factcheck: the body explicitly REFUSES to claim overtrust is "the dominant failure mode" (holds it as a working hypothesis, citing Parasuraman & Riley 1997; Lee & See 2004), while Exercise 9 says "the chapter claims that overtrust is the dominant failure mode". Films follow the body, not the exercise.

Duplicate-version note: `chapters/10-delegation-trust-and-the-supervisory-role.md` is the older, longer copy (11,044 words vs 9,614) that the deep-explainer index treated as superseded. Only 09 is sectioned here. 10 DOES contain material 09 lacks or compresses: (a) a TL;DR block; (b) the full Gru walkthrough as four separate steps — `/v0` naming sentence with the `[THING] is a [WHAT] inserted [WHERE] that produces [OUTPUT]` format and a weak-vs-strong answer pair, `/v1` intake, `/v2` architecture principles, `/v3` user flows — with Figure 10.1; 09 compresses all four into one paragraph; (c) the full copy-paste prompt bodies for the Claude steps of the Boondoggle Score (09 trims each to one line); (d) an "AI Wayback Machine" section on Donald Broadbent (vigilance decrement, *Perception and Communication* 1958, *Decision and Stress* 1971) with a run-this prompt. None of (a)–(d) changes the cards below; (b) is a candidate for a separate film only if 10's material is promoted.

Already on this chapter, different genre (deep-explainer register, not lessons): `claude-liam-deep-09-delegation-trust/` — "It Runs Beautifully. Nobody's Watching." (36 beats, est. 9m26s, PLAN gate; superseded 2026-09-09 by the LECTURE series, lecture-09 not yet packaged). A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter. S2 below shares its title-insight with the deep-09 folder — same aha, different register.

Ranked by how visible the representation already is in the source (the worked six-step score and the before/after tables first; the accept/override numbers last, because the chapter poses them as an exercise and does not print the answer).

## S3 · Where the Human Steps Fall                                       tier: standard
- question:        The AI does the parsing, the extracting, the formatting — so why are the three steps that "look like review" the ones a human has to own?
- key case:        the Paper Summarizer Boondoggle Score: six steps — Claude owns 2 (parsing), 3 (claim extraction), 5 (formatting); a human owns 1 (section taxonomy), 4 (plausibility audit), 6 (sign-off); Step 4 catches the model extracting "outperformed baselines" where the paper said "on the training set only"; spot-check one in five HIGH-confidence entries; the two highest-risk handoffs are 3→4 and 5→6; the score flags a missing Step 7 (executive integration)
- naive:           delegate by what looks like heavy lifting — "the AI does the hard part, I glance at the result" (the fluency trap at the level of a whole workflow)
- representation:  the six-step timeline (Figure 9.3, rebuilt) filling one step at a time, each step scored on a five-row grid — verification cost · stakes · distribution match · reversibility · audit trail — the same grid scored for Step 3 (cheap to verify, reversible at Step 4, clear trail → AI) and then for Step 4 (verification needs domain judgment, the dropped qualifier changes meaning → human); the human cells are the ones where the grid goes red, not the ones that look like work
- abstraction:     every step is AI, human, or hybrid by the five Boondoggle questions applied honestly — the determination is not aesthetic; AI steps are cheap to verify, bounded in failure, reversible at the next human step
- boundary:        the Boondoggle Score is Bear's own unvalidated heuristic (the chapter says so: "no external validation"); the five capacities as a system (Chapter 1; the five-capacities deep-explainer already exists in the conducting-ai book); Step 7 for a two-person lab → YOUR TURN (Exercise 13 / 16)
- terms (prereq):  pipeline step, handoff, the five supervisory capacities (as names only), solve-verify asymmetry
- equations:       none
- predict beat:    "Six steps. Which three would you hand to the AI?" before the grid scores
- source span:     §"The Boondoggle questions" (table), §"A worked walkthrough" → §"Generating the Boondoggle Score" (STEP 1–6 + Score summary), §"What the Boondoggle Score reveals"; Figures 9.2–9.3 (captions only)
- status:          built → tldr-where-the-human-steps-fall (master 2026-09-23 15:01, verdict pending)

## S1 · "Looks Good" Is Not a Handoff Condition                          tier: single-insight
- question:        Two loan pipelines, identical code — why does one survive the adoption committee and the other get tabled?
- key case:        the two-teams opener: Team 1 — "AI scores the application, the loan officer reviews and decides, the system logs both"; Team 2 — explanation checked against application data, three named edge-case patterns on an embedded checklist, one of four justification codes, scores below 0.3 or above 0.7 pass without further review, 0.3–0.7 requires a second independent officer; the committee's question "who is responsible if a loan decision is challenged?"
- naive:           "the human reviews it" — reads as supervision, is not: hand it to five loan officers and get five behaviours all called "reviewing"; no fact of the matter about whether the step worked
- representation:  the condition sentence on stage with every interpretive word circled ("reasonable", "reviews"), each circle replaced by a specifiable criterion until a stranger reading the log can answer yes/no for any case; then the three-domain table (loan / triage / moderation) filling its "what got pinned down" column — *fair* = FPR within 2 pp across four named groups; *edge cases* = a named 200-case set, sensitivity ≥ 0.95, escalation within 30 min; *respects context* = decision changes ≤ 2% on a 500-case context-flip set
- abstraction:     the handoff condition is the load-bearing clause of a delegation, and it has exactly one non-negotiable property: a non-author can read it, observe the system, and determine whether it was met
- boundary:        testability is graded — some conditions are testable only by a qualified reviewer (a narrower guarantee than "anyone can check"); the map does not prove the second team makes better DECISIONS, only that it survives review → YOUR TURN: Exercise 2's Condition A rewritten (content moderation)
- terms (prereq):  delegation, pipeline, adoption review
- equations:       none
- source span:     opener (two teams), §"The handoff condition: the contract, not the partition" + the three-domain table
- status:          pick

## S2 · Broken vs Unsupervised                                           tier: single-insight
- question:        A pipeline is missing a piece of its documentation. Why does one kind of gap stop the pipeline cold while another lets it run for months?
- key case:        the eight-item delegation map — 1 step name · 2 owner · 3 inputs · 4 outputs · 5 handoff condition · 6 failure mode · 7 verification · 8 audit trail; a pipeline missing any of 1–4 will not run; a pipeline missing any of 5–8 "runs beautifully, right up until the uncaught error surfaces downstream, usually discovered by the person it harmed"
- naive:           documentation completeness = "does it run?" — if the pipeline executes, the map must be complete enough
- representation:  two copies of the same eight-slot map, differing in which slot is empty: pull item 3 and the pipeline halts at that step (the gap announces itself); pull item 5 and the pipeline keeps flowing, the error rides through every later step and lands on the end user, with nothing on the trail to show where it entered
- abstraction:     items 1–4 are engineering documentation, items 5–8 are the supervisory additions; missing 1–4 = broken, missing 5–8 = unsupervised — "the failure that costs you is the one that does not stop the pipeline"
- boundary:        hierarchical mapping when the pipeline has a hundred or a thousand steps (tight at the seams, lighter inside settled components); reconciling map-vs-trail automatically is the chapter's own "still puzzling" → YOUR TURN: Exercise 12
- terms (prereq):  delegation map, handoff condition (S1's endpoint, named only), audit trail
- equations:       none
- predict beat:    "Which four of the eight can you drop and still have the pipeline run?" before the pull
- source span:     §"The full delegation map structure" (numbered list + "what missing looks like" table), §"Where the map scales — and where it does not"
- status:          pick  (note: same aha as the deep-09 folder's title; differs in genre)

## S5 · The Correction Is Not Embarrassing                               tier: single-insight
- question:        Two AI Use Disclosures — one reports no corrections, one reports a fix. Which pipeline do you trust more?
- key case:        the Paper Summarizer's per-paper Disclosure: Step 3 — HIGH-confidence citations spot-checked "verified 4 of 20"; 2 LOW-confidence entries corrected (Methods: AI dropped "on training data only"; Limitations marked unverifiable); Step 2 and Step 5 — "none required"; Step 6 — signed with name and date
- naive:           a clean disclosure ("AI helped; reviewed") is the good one; a correction is a mark against the pipeline
- representation:  the six-field table (step name · tool · input · output · verification done · correction made) filling twice on the same stage — the vague column ("AI helped" / "An LLM" / "Reviewed" / field omitted) versus the specific column — with the correction row lighting as the one row that PROVES a check ran; the four properties (granular · honest · time-stamped · tied to evidence) arriving as the names for what the specific column has
- abstraction:     a Disclosure functions as a supervisory log — a record of where which supervisory capacity was exercised — only when it is granular, honest, time-stamped and tied to evidence; the correction is the data point that shows the pipeline caught a domain-critical qualification
- boundary:        the course-form Disclosure as an assignment deliverable; how regulators' formats will differ — not taught → YOUR TURN: write the Step 4 entry for a paper where the spot-check finds nothing (Exercise 9's overtrust-visibility question)
- terms (prereq):  AI Use Disclosure (as a form), the Summarizer's Step 3/4 (S3's objects, named only)
- equations:       none
- source span:     §"The AI Use Disclosure as supervisory log" (Step 2/3/5/6 entries + field table)
- status:          pick

## S4 · Reliance Should Track Reliability                                tier: single-insight
- question:        The supervisor overrides the AI 7% of the time. Is that too much, too little, or just right?
- key case:        Exercise 7's medical-imaging deployment: 200 cases, 186 accepted / 14 overridden; a ground-truth audit of 40 random cases finds 6 AI errors — override rate 14/200 = 7.0%, estimated error rate 6/40 = 15% [derived: the chapter poses the numbers as an exercise and does not print the answer — factcheck computes it]; plus the body's own monitorable question: over the last fifty papers, how often did Step 4 find a correction in a HIGH-confidence extraction?
- naive:           "trust the AI" / "don't trust the AI" as a general stance — trust as an attitude toward the model rather than a rate matched to this kind of case in this deployment
- representation:  two bars on one axis — the supervisor's override rate and the AI's audited error rate — moving independently; the three named regions appear as the gap between them: overrides ≪ errors = overtrust (errors ride through uncaught), overrides ≫ errors = undertrust (value thrown away), bars level = calibrated; the Step 4 disposition tally (confirmed / corrected / unverifiable) is the same two bars already sitting in the audit trail
- abstraction:     calibrated trust is a property of the deployment, not the model: reliance matches the AI's actual reliability for this kind of input, which requires (1) monitoring data and (2) a workflow that acts on it
- boundary:        the chapter refuses to claim overtrust is "the dominant" failure mode — well-documented (Parasuraman & Riley 1997; Lee & See 2004), prevalence NOT established; a film must carry that hedge or fail factcheck; 14 overrides and 6 errors are not the same cases (overrides can be wrong too) — say so in one dim caption → YOUR TURN: the Step 4 fifty-paper tally for your own pipeline
- terms (prereq):  override, error rate, audit sample
- equations:       override rate = overrides / cases; estimated error rate = audited errors / audited cases (arithmetic, no tangent)
- source span:     §"Trust calibration" (three failure modes + the Step 4 fifty-paper question), Figure 9.4 (caption only), Exercise 7
- status:          pick  (lowest-ranked: representation is inferred from an exercise, not shown in the body)

## Not sectioned (by design)
- "The Five Supervisory Capacities as pipeline jobs" as its own film — a table of five assertions ("if the artifact is missing, the capacity did not happen") with no case of its own beyond the Summarizer's step labels; folded into S3 (the capacity label on each human step, and the missing Step 7). A five-capacities deep-explainer already exists in the conducting-ai book.
- The compressed Gru `/v0`–`/v3` specification paragraph — 09 states it in one paragraph without the weak-vs-strong answer pair; the case lives in chapter 10 (see duplicate-version note). `not-yet-sectionable` from 09 alone.
- "Where the map scales" / hierarchical mapping — an assertion plus the author's "still puzzling"; a BOUNDARY line in S2, not a section.
- The two-teams opener as a film about *decision quality* — the chapter explicitly says the story proves review-survival, not better decisions; S1 carries that as its boundary.
- Glimmer 9.1, Warm-Up/Application/Synthesis/Challenge exercises, the LLM Exercise (Red-Team Casebook prompt), "The shape of the rest", "What would change my mind" — back matter and practice; Exercises 2, 7, 9, 12, 13 feed the YOUR TURN beats above.

## Multi-act candidates (need explicit approval)
- S1+S2 share the loan-pipeline object: S1 ends on "the handoff condition is the load-bearing clause", S2 opens by placing that clause as item 5 of the eight and pulling it out. One ~8 min film "The Contract, Not the Partition" is legal under the sectioning exception. Default remains two films.
- S3+S5 share the Summarizer's Step 3/4 objects end to end (the "on training data only" qualifier is the same correction in both); S5's HOOK is S3's 3→4 highest-risk handoff. Legal as a two-act film; default remains two.
- S4+S5 are conceptually paired (the Disclosure IS the monitoring data S4 needs) but share no drawn object; not proposed.
