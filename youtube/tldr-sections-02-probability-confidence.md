# tldr sections — Chapter 2: Probability, Uncertainty, and the Confidence Illusion

Source: `chapters/02-probability-uncertainty-and-the-confidence-illusion.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 2 deferred · course film: carries the course credit (bookloop exception)

Numbers below are copied from the chapter as written. The chapter carries ZERO `[verify]` flags in its body (the only match is the CHAPTERIZED header comment), but it is a rough draft with SIX unresolved git-merge blocks (`<<<<<<< HEAD` … `>>>>>>> d78899b`, at lines 158, 205, 258, 391, 457, 637). Where a card's numbers sit on one side of a conflict, the card says which side. Every number is re-verified at `factcheck` for whichever film builds.

Already on this chapter, different genre: `claude-liam-deep-02-probability-confidence` (deep-explainer register — a walk of the chapter). Shorter cs/vox reels also touch single ideas here (`claude-liam-cs-01-base-rate-trap`, `cs-02-confident-and-wrong`, `cs-09-heavy-tail-yank`, `cs-10-calibration-curve`, `vox-calibration-curve`, `vox-heavy-tail-yank`, `cli-base-rate-bayes-calculator`, `cli-calibration-curve-auditor`). A tldr film is additive: one aha, taught 3b1b-style, HOOK → INSTANCE → NAIVE → SHIFT → TRANSFORM → ABSTRACTION, not a casebook beat.

Ranked by how visible the representation already is in the source (a counted population, a filled table and a tree first; a figure whose numbers the film must generate last).

## S1 · The Test That Is 99% Accurate                                  tier: single-insight
- question:        The test is 99% accurate and it came back positive — so why is the patient almost certainly fine?
- key case:        disease base rate 1 in 10,000; test 99% accurate; 10,000 people → 1 true positive + 0.01 × 9,999 ≈ 100 false positives → 1/101 ≈ 1%; Bayes: 0.0001 × 0.99 / (0.0001 × 0.99 + 0.9999 × 0.01) ≈ 0.000099 / 0.010098 ≈ 0.0098 (the chapter's term table prints ≈ 0.0099 — carry both, reconcile at factcheck)
- naive:           "99% accurate, positive result, therefore ~99% sick" — the chapter's engineers answer 90–95%; Casscells, Schoenberger & Graboys 1978 (1-in-1,000 version, 60 Harvard house officers, most ≈ 95%); it is the right answer to the wrong question, P(positive | disease) read as P(disease | positive)
- representation:  the 10,000-dot population grid (Figure 2.5): one dot lit sick, then 1% of the 9,999 healthy dots lit as false positives; pull every lit dot into a "positives" pool and the single sick dot is one among ~101 — the grid is the denominator intuition forgot
- abstraction:     P(A_i | B) = P(A_i)·P(B | A_i) / Σ_k P(A_k)·P(B | A_k); posterior ∝ prior × likelihood — the prior sits in the numerator with the same weight as the test's sensitivity
- boundary:        "99% accurate" is doing double duty as sensitivity AND specificity (the chapter flags its own shortcut — one dim caption, not a beat); Glimmer 2.3: vary the base rate 1/100 → 1/100,000 and lock where the PPV curve crosses 50% → YOUR TURN
- terms (prereq):  base rate / prior, conditional probability P(A | B) (read "given"), false positive
- equations:       Bayes' theorem (the disease form); the counting identity 1 / (1 + 0.01 × 9,999)      ← one TANGENT (Bayes); the count is arithmetic
- predict beat:    the chapter's own "Stop. Don't read on yet. Pick a number. Lock it in." — before the grid lights
- instances:       (1) the 10,000-person count; (2) the same case through Bayes; (3) scale-shift PAYOFF: Epic Sepsis Model — alert on 18% of hospitalized patients, sensitivity 33% / 67% of sepsis missed (Wong et al., JAMA IM 2021); the base-rate table (fraud ~0.1–1%, security ~0.01–0.1%, screening ~0.01–1%, moderation ~0.01–0.1%, jailbreaks ~0.001–0.01%) as one dim strip, not a beat
- source span:     §"The test that is 99% accurate, and the patient it kills", §"Bayes' theorem — the bookkeeping made explicit" (term table), §"The false-positive structure is everywhere"; Figures 2.5, 2.6, 2.10; Glimmer 2.3. HEAD side of the line-258 conflict holds the sensitivity/specificity precision note
- status:          published (unlisted) → tldr-the-99-percent-test · https://youtu.be/xVxzt7rXEXA · 2026-09-24

## S3 · Which Model Made the Mistake?                                   tier: standard
- question:        No single model reports the pipeline's error rate — and when an output IS wrong, which model most likely produced it? (Not the one with the most traffic.)
- key case:        three versions in production: A handles 40% of traffic and errs 2%, B 30% / 3%, C 30% / 5% → P(D) = 0.40 × 0.02 + 0.30 × 0.03 + 0.30 × 0.05 = 0.032; run backward: P(C | D) = 0.015 / 0.032 ≈ 0.469, P(A | D) = 0.008 / 0.032 = 0.25, P(B | D) = 0.009 / 0.032 ≈ 0.28 (the chapter's table prints 25% / 28% / 47%)
- naive:           forward: "average the three error rates" (2+3+5)/3 — ignores who handles what; backward: "the wrong output most likely came from A, it handles the most traffic" — 40% vs the honest 25%
- representation:  a strip partitioned 40 / 30 / 30 (Figure 2.3), each band with its error slice shaded (2%, 3%, 5% of its width); gather the three shaded slivers end to end → 3.2% of the strip; then throw away everything unshaded and read the slivers' shares of what remains — C's sliver is almost half. Same objects, the second act only changes what counts as the whole
- abstraction:     P(B) = Σ_i P(A_i)·P(B | A_i) (total probability), then P(A_i | B) = P(A_i)·P(B | A_i) / P(B) — "the same piece of machinery, deployed in opposite directions"
- boundary:        Markov chains (the recursive use of total probability — the Alice example, deferred below); Exercise 14: C scaled to 50%, A to 20%, B stays 30% — recompute P(D) and P(C | D) → YOUR TURN
- terms (prereq):  partition (mutually exclusive + collectively exhaustive), conditional probability
- equations:       the total probability theorem; Bayes' theorem (partition form)                   ← two TANGENTs
- predict beat:    "A defective output lands on your desk — which version do you blame?" before the unshaded strip is thrown away
- source span:     §"The total probability theorem — decomposing complex problems" (worked example — the fleet's error rate), §"Worked example — factory revisited" (share-of-defectives table); Figure 2.3; Exercise 14. NOTE: HEAD calls this a fraud-screening pipeline with versions A/B/C; the Bayes subsection still says "factory revisited" / "machine C" (d78899b wording) — the film must pick one framing; card uses the pipeline framing (HEAD, and Exercise 14 agrees)
- status:          pick

## S2 · A "Task Complete" Is a Product, Not a Bit                       tier: single-insight
- question:        The agent said "task complete" — one word, one bit. What is that word actually claiming?
- key case:        three tool calls that must all land, in order: P(A_1) = 0.9, P(A_2 | A_1) = 0.85, P(A_3 | A_1 ∩ A_2) = 0.8 → 0.9 · 0.85 · 0.8 = 0.612; the independence shortcut 0.9³ = 0.729 — "twelve points of unearned confidence" (numbers the chapter marks as invented to keep the arithmetic clean)
- naive:           read the report as a fact ("it said complete"); or, one step better, "each step is about 0.9 reliable, so multiply 0.9 three times" — treating dependent steps as independent, and the error runs in the optimistic direction
- representation:  the probability tree (Figure 2.2): one edge per step, each edge labelled with its conditional, the widths shrinking as the chain goes deeper because each call runs on the state the last one left; multiply along the path to the success leaf. Beside it the same tree with every edge held at 0.9 — the leaf is fatter by exactly the dependence that was assumed away
- abstraction:     P(A ∩ B) = P(B)·P(A | B) → the chain rule P(∩ A_i) = P(A_1)·P(A_2 | A_1)·P(A_3 | A_1 ∩ A_2)…; independence is the special case P(A | B) = P(A) where it collapses to P(A)·P(B)
- boundary:        where each conditional NUMBER comes from (a model card, a log, an assumption) — the LLM Exercise's Task 1, not this film; Exercise 4: 3 red + 7 blue, two drawn without replacement, both red, by the chain rule → YOUR TURN
- terms (prereq):  conditional probability P(A | B) = P(A ∩ B) / P(B) (introduced from the chapter's triage-flag instance, see below), joint probability, independence
- equations:       the multiplication rule; the n-event chain rule                                   ← one TANGENT (chain rule); the two-event rule is its own arrival
- predict beat:    "Three steps, each about ninety percent — what's the chance the whole task landed?" before the shrinking edges appear
- instances:       (1) the triage-flag conditional as the first moving instance of "given": 76% flagged, 45% high-acuity, 30% both → P(A | B) = 0.30 / 0.76 ≈ 0.395, LOWER than the unconditional 45% (a Venn/area shrink, Figure 2.1); (2) the three-call chain; (3) the independent tree
- source span:     §"Conditional probability — the probability that updates on what you know" (illustration), §"The multiplication rule", §"Worked example — an agent's tool-call chain"; Figures 2.1, 2.2. NOTE: the agent chain and the independence paragraph are the HEAD side of the line-158 conflict; the d78899b side is a card-drawing chain (39/52 · 38/51 · 37/50 ≈ 0.413) with a different Figure 2.2 caption
- status:          pick

## S4 · Accurate Is Not Calibrated                                      tier: standard
- question:        The model says 0.91. Does that mean 91 out of 100 such cases come out positive — and how would you know?
- key case:        "seventy percent confident" on a thousand cases → want ≈ 700 positives; 400 → overconfident, 900 → underconfident; the modern-net pattern: about right at "sixty percent", says "ninety-nine" when it should say "eighty-five"; the fix: softmax(z / T), one parameter T > 1 fit on a held-out set — ranking unchanged, only the stated number moves (Guo, Pleiss, Sun & Weinberger, ICML 2017)
- naive:           "94% accuracy on validation, so the 0.94 on this case is trustworthy" — accuracy is one number over all cases; it says nothing about whether the STATED probabilities track the frequencies
- representation:  the reliability diagram (Figure 2.8): stated confidence on x in ten bins, empirical accuracy on y, the diagonal drawn first; bin by bin the dots land — on the line through the middle, then peeling below it at the high end; then divide every logit by T and watch the dots slide back toward the diagonal while the ORDER of the cases (a side rail of ranked cases) never changes
- abstraction:     calibrated ⇔ among cases the model scores p, a fraction ≈ p turn out positive; temperature scaling softmax(z/T) rescales stated confidence without touching the decision — "direct evidence that the confidence and the correctness were separable all along"
- boundary:        a T fit in-distribution goes stale silently under distribution shift (the chapter's own caveat — one line, points at the deferred shift card); your own 90% intervals contain the truth ≈ 0.4–0.6 of the time (the calibration baseline); Glimmer 2.4 steps 1–7 (emit, lock, bin, plot, fit T, name the decorative number) → YOUR TURN
- terms (prereq):  logit / pre-softmax score, softmax, held-out set, accuracy (as a single rate)
- equations:       softmax(z / T)                                                                       ← one TANGENT; the calibration definition is a sentence, no equation in the chapter
- predict beat:    Glimmer 2.4 step 2 lifted into the film: "track the diagonal, sag below it, or rise above it — and where does it peel off?" before the dots land
- source span:     §"Calibration — the most operationally important diagnostic in this chapter", Glimmer 2.4, §"The calibration baseline"; Figure 2.8. NOTE: the 700/400/900 and 99→85 numbers are the chapter's illustrative sentences, not a logged run — any dots the film draws are generated at build and fact-checked as our own
- status:          pick  (overlaps `cs-10-calibration-curve` / `vox-calibration-curve` / `cli-calibration-curve-auditor` in subject; differs in genre)

## S5 · The Average That Never Settles                                  tier: single-insight
- question:        You averaged a thousand observations. Why can the thousand-and-first move the average by a lot?
- key case:        Glimmer 2.1: a Monte Carlo of sample means from a Gaussian settles; the same simulation from a Cauchy does not — "you compute the average of a thousand observations and the next observation moves the average by a lot"; then the deployment reading: Exercise 10's security-alert system, false positive costs $10, false negative $500,000 — average loss is the wrong quantity
- naive:           "more data → the average tightens" (the CLT, remembered without its two requirements: independent, finite variance); Gaussian confidence intervals computed on heavy-tailed data "look exactly like normal confidence intervals"
- representation:  two running-mean traces drawn one observation at a time on the same axis (Figure 2.9): the Gaussian trace narrows into a flat line; the Cauchy trace flattens, then one arriving dot yanks it, then again — the SAME procedure, the same n, one distribution swapped
- abstraction:     the CLT needs independence and finite variance; when variance is infinite the sample mean does not converge, and a deployment evaluated on average loss "is being evaluated on a quantity that does not converge in any useful sense"
- boundary:        deciding a real loss distribution is heavy-tailed BEFORE the catastrophe — the chapter admits "tail estimation from a sample is mathematically impolite" and offers a heuristic (assume heavy tails when the cost includes harm to people), not a calculation; Glimmer 2.2 / Exercise 10 → YOUR TURN
- terms (prereq):  sample mean, variance (as "how spread out"), the Central Limit Theorem (stated, not derived)
- equations:       none landed as a formula in the chapter (the CLT is stated in prose) — no TANGENT
- predict beat:    "Lock your prediction of where the Cauchy mean settles" (Glimmer 2.1's own instruction) before the second trace runs
- source span:     §"When the Central Limit Theorem politely declines to help", Glimmers 2.1–2.2, Exercise 10; Figure 2.9 (caption is inside the line-457 conflict: HEAD "the next observation can move your average dramatically" vs d78899b "Two distributions overlaid on the same x-axis"). NOTE: the chapter gives no seed, n or numbers for the simulation — every number on screen is generated at build and fact-checked as our own
- status:          pick  (overlaps `cs-09-heavy-tail-yank` / `vox-heavy-tail-yank` in subject; differs in genre)

## Deferred

### D1 · Hume's Induction Problem as Distribution Shift                  not-yet-sectionable
- reason:          the passage states the abstraction (training set = the past, deployment = the future, the model's confidence "is calculated under the assumption that the world is the world it learned") with one cited real case (DeGrave, Janizek & Lee, Nat. Mach. Intell. 2021 — COVID-era imaging models selecting shortcuts) but no worked case, no numbers, no before/after pair. Figure 2.7 is captioned two ways across the line-391 conflict ("confidence does not move when the world moves" vs "two overlapping bell curves") and either way pictures the claim, not a case. A representation exists in principle (two input distributions drifting apart while a confidence readout stays fixed and an outcomes counter falls) but the drift would be invented and then fact-checked as our own. Sectionable once the chapter, or a companion research note, supplies one logged shift with numbers. Its BOUNDARY role is already carried by S4.

### D2 · Alice's Two-State Markov Chain                                  pending merge
- reason:          the example (up-to-date stays 0.8 / falls behind 0.2; behind catches up 0.4 / stays 0.6; P(U_2) = 0.72, P(U_3) = 0.688) has a strong representation (a two-state diagram, Figure 2.4, with probability mass sloshing between the states week by week) and would section cleanly — but it exists ONLY on the d78899b side of the line-205 conflict; the HEAD side drops it. Not sectioned until the merge is resolved in its favour. If kept, it is a natural second act on S3 (total probability run recursively).

## Not sectioned (by design)
- "What probability actually is" / the three axioms / classical–frequentist–Bayesian — definitions and two tables, no case; the axioms serve every card as prerequisite vocabulary, never as a film.
- "From Boolean to probabilistic" — a stance ("every model output is a probabilistic claim"), restated in the VERDICT of S4, not a section.
- Synthesis "four questions" + Figure 2.11, "What would change my mind", "Connections forward", chapter summary, LLM Exercise (Agentic Red-Team Casebook), AI Wayback Machine (Frank Ramsey), the D3 "Prompts" block — back matter and practice; the four questions map onto S1 (base rate), S4 (calibration), S5 (cost distribution), D1 (what changed) and belong in each film's YOUR TURN, not on their own.
- The triage-flag conditional (0.30 / 0.76 ≈ 0.395) as its own film — one computation; folded into S2 as its first INSTANCE.

## Multi-act candidates (need explicit approval)
- S3 is already two acts on one key case (total probability forward, Bayes backward) — that is why it is tier standard, not a multi-act request.
- S1+S3 both land Bayes' theorem but on DIFFERENT key cases (a patient; a fleet); they do not meet the sectioning exception and stay two films. If Bear wants one "Bayes forward and backward" film anyway, S3's fleet would have to be re-told as the denominator of S1's positive pool — log the reason at GATE S.
- D2+S3 (if the merge keeps Alice): the recursive total-probability act would share S3's machinery but not its objects — a second film, not an act.

## Chapter flags carried into these cards
- 6 unresolved merge-conflict blocks (HEAD vs d78899b "Update chapters 1-14"): lines 158, 205, 258, 391, 457, 637. The HEAD side is the agent/pipeline framing; d78899b is the cards/factory/Alice framing. Cards above follow HEAD and say so.
- 0 `[verify]` flags in the body (the header comment says flags were "preserved", but none survive).
- Posterior printed two ways: ≈ 0.0098 (prose) vs ≈ 0.0099 (term table).
- "Fleet"/"versions" vs "factory"/"machine" naming drift inside the total-probability → Bayes worked example.
- Figure captions 2.5, 2.7, 2.9 differ across the conflict; the d78899b Figure 2.5 caption is truncated mid-sentence ("arranged as a").
