# tldr sections — Chapter 13: The Limits of AI: What the Tools Cannot Do

Source: `chapters/13-the-limits-of-ai-what-the-tools-cannot-do.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 2 deferred · course film: carries the course credit (bookloop exception)

The chapter is a marked rough draft ("CHAPTERIZED 2026-07-02 … rough draft for hand-rewrite"). It carries three unresolved git-merge blocks (`<<<<<<< HEAD` at lines 212, 254, 496 — the `d78899b` side numbers this as Chapter 14 and adds an "AI Wayback Machine" section the HEAD side lacks) and two `[verify]` flags (line 248: the *Irreducibly Human* dependency; line 299: the calibration-baseline ranges are "an expected pattern, not a measured finding"). Numbers below are copied exactly as the chapter states them; flags are carried into the cards; the opening clinical case is labelled by the chapter itself as a composite, and that label is carried too.

Already on this chapter, different genre (not lessons): `claude-liam-deep-13-limits-of-ai` (deep-explainer, "Scaling Moves the Boundary. It Never Removes It." — PLAN gate, no master), `claude-liam-limits-of-ai` (ai-explainer, "What the Tools Cannot Do" — built, mp3 + srt). Adjacent single-case reels from other chapters touch two of the key cases: `claude-liam-cs-07-turkeys-model` / `claude-liam-vox-heavy-tail-yank` (the turkey, Extremistan) and `claude-liam-chinese-room` / `claude-liam-do-chatbots-pass` (Searle, Turing). A tldr film is additive: one aha, taught 3b1b-style, pure Manim, not a walk of the chapter.

Ranked by how visible the representation already is in the source (a worked case with a figure first, then tables, then a contrast the chapter only asserts).

## S1 · The Boundary Scaling Cannot Cross                              tier: single-insight
- question:        If more data always makes the model better, why can't enough data make it safe?
- key case:        Taleb's turkey — fed every day for 1,000 days, confidence in "the human cares about me" rising monotonically, catastrophic failure on the morning of day 1,001 (Thanksgiving); then the chapter's transfer: "a system tested on ten thousand routine cases with 99.7% accuracy may still be a turkey"
- naive:           the functionalist — "the mismatch is frequent, not structural; a better model reduces the frequency; scale it enough and the limit shrinks to nothing"
- representation:  a shaded SAMPLE region growing inside an unshaded WORLD, one enlargement at a time — every enlargement still has an edge, and the edge is where the gap lives (Figure 13.1 rebuilt); beside it the turkey's confidence curve climbing day by day with the event sitting off the axis the curve was fitted on
- abstraction:     the parts of the world not in the data are not learnable from the data — covered region and excluded region are complementary by construction, so no enlargement crosses a boundary defined by what the enlargement did not reach (Hume 1748, §IV: induction has no non-circular justification)
- boundary:        whether meaning and intentionality are "really" categorical — the chapter says the metaphysics is contested and lets both inherit their bite from this gap; Mediocristan vs Extremistan (which world the deployment lives in) is the transfer exercise → YOUR TURN
- terms (prereq):  sample, training distribution / in-distribution, distribution shift (Ch. 4 name for the same thing)
- equations:       none (complementarity is stated in words; no TANGENT)
- predict beat:    "Day 1,000 — is the turkey's confidence higher or lower than on day 500?" before the curve reaches 1,001
- source span:     §"Three categorical limits" (the functionalist objection, the Hume argument, Figure 13.1, Limit 3, Taleb's turkey); Exercise 3b
- status:          built → tldr-the-boundary-scaling-cannot-cross (master 2026-09-23 15:58, verdict pending)

## S3 · The Signal That Came Second                                    tier: single-insight
- question:        How does a sepsis model pass internal validation and still not catch sepsis early?
- key case:        the Epic Sepsis Model — proprietary early-warning tool deployed across hundreds of hospitals; external validation (Wong et al., 2021) found it performing far worse than marketed, missing a large fraction of sepsis cases while flooding clinicians with alerts; the model had partly learned to confirm clinical suspicion (a blood-culture order → a sepsis label) rather than form it. The chapter gives NO numbers for the Wong result — "far worse", "large fraction" only; factcheck must source any figure from the paper, never from this card
- naive:           "the vendor's internal validation metrics looked fine, and the performance report reads fluently — so the claim *this model helps clinicians catch sepsis earlier* is supported"
- representation:  one patient's timeline, one state at a time: clinician suspects → blood culture ordered → model alert fires → diagnosis; the "early warning" window is drawn, then the alert slides to AFTER the suspicion it was supposed to precede — the arrow from data to alert is a loop back through the clinician (Figure 13.2, the circular signal, rebuilt)
- abstraction:     a model can learn a confirmatory signal instead of a predictive one, and the metric that scored it cannot tell the two apart; noticing requires standing outside the data and asking whether its frame matches the world — the operation the data-world gap says no data performs on itself
- boundary:        the five components of the high-stakes engineering practice (specify / oversight / override infrastructure / visibility to affected parties / stop condition) — named, not taught; the transfer is the Glimmer's AUDIT side: name the irreducibly-human decision the deployer skipped
- terms (prereq):  early-warning tool, external vs internal validation, blood culture (as a clinician's confirmatory order), alert
- equations:       none
- predict beat:    "In this timeline, which comes first — the blood-culture order or the model's alert?" before the arrow slides
- source span:     §"Skepticism as safety mechanism" (the Epic Sepsis paragraph, Figure 13.2); §"AI's cognitive profile" → *Plausibility auditing* (same case, second telling); Glimmer 13.1 AUDIT
- status:          pick

## S5 · Three Tiers, One Question Each                                  tier: standard
- question:        Which of my tasks can I hand to the model, and how do I decide without guessing at how smart it is?
- key case:        Exercise 4's five tasks sorted live: (a) running missingness analysis on a dataset · (b) explaining why a column has a high missing rate · (c) deciding whether deployment shift is significant enough to pause the system · (d) generating a first-draft Layer 1 summary · (e) signing off a validation report for a clinical deployment
- naive:           delegate by capability — "the model is good enough at (c) and (e) now, or will be next generation" — the chapter's target: these are withheld "not because AI is insufficiently capable, but because they are structurally unavailable to any system that cannot be wrong in a way that matters to it"
- representation:  the three-column table (delegate freely / with verification / do not delegate) filling one task at a time, each task routed by a three-question gate that is the same for every task — is the output checkable by inspection? · does it require connecting the representation to the world? · does it require being answerable for the consequence? — the third gate is the one no task ever passes
- abstraction:     the cognitive profile → the delegation map: strong (retrieval/synthesis, generation to spec, pattern recognition on well-defined inputs) → delegate freely; weak (problem formulation, plausibility auditing, interpretive judgment under stakes) → keep the work; absent (accountability — a relationship between a judgment and the person answerable for it) → cannot be delegated at all. Where you delegate you retain the obligation to verify
- boundary:        the extended-mind catalog and the "cognitive extremophile" reframe (Legg-Hutter 2007) — named as the reason, not taught; Exercise 9's writing-assistant task list is the transfer → YOUR TURN
- terms (prereq):  delegation, Layer 1 summary (Ch. 11), verb taxonomy (Ch. 11), EDA / missingness analysis (Ch. 3)
- equations:       none
- predict beat:    "Task (c) — pause the system on shift. Which column?" before the gate routes it
- source span:     §"AI's cognitive profile" (three tables: strengths, weaknesses, delegation categories); Exercise 4, Exercise 9
- status:          pick  (two abstractions — profile then map — hence standard; the two share the five tasks end to end)

## S4 · What Turing and Searle Each Actually Proved                      tier: single-insight
- question:        Didn't Turing prove a machine that talks like us is intelligent — and didn't Searle prove it can't understand?
- key case:        the Chinese Room: a person who does not speak Chinese, a rulebook, slips through a slot; to the observer outside, inputs and outputs are indistinguishable from a Chinese speaker's; the person does not understand Chinese — set beside the imitation game's move: we demand only behavioral evidence from other humans
- naive:           the two overclaims the chapter names — "Turing proved AI can be intelligent" and "Searle proved AI cannot understand"
- representation:  two cases differing in one respect: one arrow from BEHAVIOR to ATTRIBUTION — Turing's arrow (behavior warrants the attribution; methodological) and Searle's crossed arrow (behavior does not entail understanding; sufficiency fails) — then the chapter's four-column table (claims / does NOT claim / common misreading) filling row by row, with each overclaim drawn as a longer arrow and erased
- abstraction:     Turing settles a methodological question, not a metaphysical one; Searle shows sufficiency fails, not necessity; the operational stance is both moves at once — behavior is testable evidence AND behavior is not the whole of meaning
- boundary:        the Systems Reply and whether embedding structure / multimodal grounding constitute "something more" — live, not settled (Exercise 14 is the transfer)
- terms (prereq):  behavioral evidence, sufficient vs necessary, symbol manipulation / syntax vs semantics
- equations:       none
- source span:     §"Turing and Searle — what each argument settles, what each does not" (both arguments, the table); Exercise 2, Exercise 14
- status:          pick  (note: `claude-liam-chinese-room` and `claude-liam-do-chatbots-pass` exist from other chapters; this card is the sufficiency/necessity aha, not a retelling of the room)

## S2 · Ninety-Four Percent and Three Patients                          tier: single-insight
- question:        Every test was green — how did the deployment still hurt people?
- key case:        the chapter's opener, a labelled COMPOSITE (not a single sourced incident — carry the label on screen): clinical decision-support, 94% validation accuracy, every threshold met, fairness and robustness within tolerance; live six months, three patients harmed by accepted recommendations. Tested question: *does this presentation match a category in the training data?* Harm question: *what is going on with this specific patient?* Paired with Exercise 3: a parts classifier at 99.1% vs rare-disease recommendations at 94%
- naive:           "94% and all thresholds passed, therefore safe to deploy" — the accuracy is real; it is over the question the data could answer
- representation:  two deployments side by side, same green test-scoreboard on both; under each, the deployment region drawn against the sample region — the parts line sits entirely inside the sample (limits do not bite; skepticism is methodology), the clinic's region spills past the edge (limits bite; skepticism is the safety mechanism) — and the three harmed cases are placed in the spilled part, where no test-arrow reaches
- abstraction:     a validation framework is scoped to the question it was built to answer; "is this system safe to deploy?" is a question about the world the system enters, and the metrics cannot ask it — so the supervisor's authority to refuse deployment is the structurally most important authority in the system
- boundary:        the override-fiction test ("documented but practically impossible … is a fiction in the documentation", Exercise 7) — not designed here; Exercise 8 (the tests the engineers did not run) is the transfer
- terms (prereq):  validation set, deployment distribution, threshold
- equations:       none
- source span:     §"The model that passed every test and failed in deployment"; §"Skepticism as safety mechanism — when the limits bite" (the two-deployment contrast, the five components, the stop condition); Exercise 3, 7, 8
- status:          pick  (lowest-ranked: the key case is the chapter's own composite and the contrast is asserted, not tabulated; the representation borrows S1's sample/world object)

## Not-yet-sectionable (deferred, with reason)
- **The third calibration baseline** — a clean representation exists (90% intervals scored across three baselines: 0.4–0.6 → 0.6–0.75 → 0.7–0.85) but the chapter flags those exact ranges `[verify]`: "an expected pattern, not a measured finding — there is no data source behind the exact numbers." A film would have to invent the data. Deferred until the book records a measured trajectory.
- **Rapid prototyping for skepticism** — a six-step procedure (specify → falsifier → design → pre-register → run → decide) with no worked case in the chapter; the case would be ours and would need its own fact-check. Deferred.

## Not sectioned (by design)
- Limits 1 and 2 (meaning, intentionality) as their own films — the chapter itself declines to settle the metaphysics and routes both limits' bite through the data-world gap; they are a BOUNDARY line in S1, not sections.
- "The extended mind arrives" and the cognitive-extremophile reframe — an assertion and a catalog (pH meter, GPS, microscope, printing press, peer review), no moving case; the `[verify]` dependency on *Irreducibly Human* sits here. A BOUNDARY line in S5.
- "Where AI is absent — accountability" as its own film — an argument (a relationship, not a skill), no case; it is the third gate in S5's representation.
- Glimmer 13.1, "What would change my mind", chapter summary, connections to the research project, the closing argument, Exercises, the LLM Exercise (Red-Team Casebook memo), the AI Wayback Machine (present only on the `d78899b` side of an unresolved merge) — back matter and practice; the Glimmer's BUILD/AUDIT pair and Exercises 3b, 4, 7, 8, 9, 14 feed the YOUR TURN beats above.

## Multi-act candidates (need explicit approval)
- **S1+S2** share one persistent object — the shaded sample region inside the world — end to end; S2's HOOK (94% and three patients) is the chapter's opener and S1's BOUNDARY names where it bites. One ~8–10 min film "The Boundary, and Where It Bites" is legal under the sectioning exception. Default remains two films; S2 alone is the weaker card because its case is a composite.
- **S3+S5** share the Epic Sepsis case (S5's *plausibility auditing* row retells it) but not a persistent on-screen object; not recommended as multi-act.

## What the chapter itself flags as unresolved
- Three git-merge conflict blocks left in the text (lines 212–218, 254–262, 496–519): HEAD numbers figures 13.3/13.4; the `d78899b` side numbers them 14.1/14.2 (with a duplicated "Figure 14.1" caption) and carries the AI Wayback Machine section. Any film citing a figure number must wait for the resolution or cite by caption.
- `[verify]` ×2 in the body: line 248 (the tiered *Irreducibly Human* account is forthcoming and uncheckable — the chapter says the checkable claim stands on Hume, Taleb, Legg-Hutter) and line 299 (calibration ranges are unmeasured).
- The opening clinical case is a composite by the chapter's own label; the named instance is the Epic Sepsis Model, for which the chapter reports no numbers (Wong et al., 2021 must be pulled at factcheck).
- The LLM Exercise references "the seven-tier extended-mind taxonomy from Chapter 12" — a cross-reference this chapter does not restate (the chapter's own profile is three-tier: strong / weak / absent).
