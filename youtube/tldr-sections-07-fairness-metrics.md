# tldr sections — Chapter 7: Fairness Metrics: Choosing a Definition and Defending It

Source: `chapters/07-fairness-metrics-choosing-a-definition-and-defending-it.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 0 deferred · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre: `claude-liam-deep-07-fairness-metrics` (deep-explainer register, walks the chapter) and the CLI trio `claude-liam-cli-fairness-impossibility-demonstrator` / `cli-fairness-impossibility-demonstrator` / `nbb-cli-fairness-impossibility-demonstrator` (build-it-with-Claude register). A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Chapter state the cards inherit: the file is a CHAPTERIZED rough draft (header comment 2026-07-02) with **seven unresolved merge-conflict blocks** (`<<<<<<< HEAD … ======= … >>>>>>> d78899b`) at the Figure 7.1, 7.2, 7.3, 7.4, 7.5, 7.6 captions and from the Chapter-8 preview to end of file; the `d78899b` side carries truncated captions ("Figure 7.4 — Causal graph with nodes: A (sensitive attribute /"). Zero `[verify]` flags in the body (the header comment only says they were preserved). Both numeric tables in "The arithmetic" re-check by hand (see S1). Numbers are re-verified at `factcheck` for whichever film builds.

Ranked by how visible the representation already is in the source (worked tables and worked cases first).

## S1 · Hold One Fair, Watch the Other Break                            tier: standard
- question:        Why can't a classifier be calibrated for both groups AND make its mistakes evenly — isn't that just a matter of tuning harder?
- key case:        base rates p_a = 0.6, p_b = 0.3, threshold 0.5. Calibration-satisfying table: TPR 0.60 / 0.70, FPR 0.30 / 0.10, PPV 0.75 / 0.75, positive-prediction rate 0.48 / 0.28 (check: 0.3·0.70 / (0.3·0.70 + 0.7·0.10) = 0.21/0.28 = 0.75). Equalized-odds-satisfying table (thresholds 0.5 / 0.6): TPR 0.70 / 0.70, FPR 0.15 / 0.15, PPV 0.88 / 0.67, rate 0.48 / 0.32
- naive:           "satisfy all three — better model, more data, a smarter threshold"; the chapter's own line: not the tools, not the data — a theorem
- representation:  two side-by-side 2×2 confusion grids (group A, group B) with base rate as the row split; the odds identity as a balance v/(1−v) = p/(1−p) · t/f. Act 1: pin PPV equal (0.75 = 0.75) and watch t/f get pushed apart as the p/(1−p) arms differ (1.5 vs 0.43). Act 2: pin t and f equal and watch PPV split (0.88 vs 0.67). One quantity held invariant while the others are forced to move — the table fills as the pin moves
- abstraction:     v/(1−v) = p/(1−p) · t/f; take the ratio across groups: t_a/f_a = [p_b(1−p_a)] / [p_a(1−p_b)] · t_b/f_b — the coefficient is 1 only when p_a = p_b. Calibration (v_a = v_b) and equalized odds (t_a = t_b, f_a = f_b) cannot both hold unless base rates are equal or prediction is perfect (t = 1, f = 0)
- boundary:        the three-way KMR version (calibration + balance for positives + balance for negatives) and demographic parity as a fourth constraint — named, not proved; the escape hatches (equal base rates, perfect prediction) → YOUR TURN: redo the pin with Exercise 6's 40% / 20% health-care base rates, qualitatively
- terms (prereq):  base rate (prevalence), true-positive rate, false-positive rate, positive predictive value (precision), calibrated
- equations:       Bayes for PPV v = pt / (pt + (1−p)f); the odds identity; the cross-group ratio          ← three TANGENTs (fold the first two into one)
- predict beat:    "Group B has half the base rate. To keep PPV at 0.75, does its FPR have to go UP or DOWN?" before Act 1 moves
- source span:     §"Three definitions" (the three equations + values table), §"The arithmetic — the actual proof, not a gesture", both numeric tables, Figure 7.1 (the triangle — REBUILD, caption is inside a merge conflict)
- status:          built → tldr-hold-one-fair (master 2026-09-23 13:56, verdict pending)

## S3 · Same Equation, Opposite Guarantee                                tier: single-insight
- question:        If the fairness condition is a clean inequality, how can the same inequality both force two people to be treated alike and permit them to be treated differently?
- key case:        two loan applicants, identical credit history, income and debt-to-income ratio, different zip codes. d on the financial variables only → d(x, y) small → M(x) and M(y) forced close. d encoding zip-code distance → d(x, y) large → the condition permits divergent treatment. Same equation, opposite guarantee (Exercise 9 is the same case)
- naive:           fairness through unawareness — "just drop race from the model"; zip code, surname, occupation reconstruct it, so the direct use is blocked and the indirect use is untouched
- representation:  two dots (the applicants) on a feature plane with a leash between them (d) and a second leash between their outcome distributions (D). The dots never move; the METRIC does — stretch the zip-code axis and the d-leash lengthens, the D-bound slackens, and the two outcome bars are allowed to drift apart. A quantity (the people) held fixed while the ruler changes
- abstraction:     M is (D, d)-Lipschitz: D(M(x), M(y)) ≤ d(x, y) for all x, y; D = total variation ½ Σ|P(a) − Q(a)|; the guarantee is exactly as good as d, and choosing d is the values claim (fairness through awareness)
- boundary:        verifying every pair is computationally hard — spot-check a sample of similar pairs (one line); FTA vs FTU as a documentation choice → YOUR TURN: write the d that calls two people similar when one was historically denied the features' inputs, and say what it bakes in
- terms (prereq):  similarity metric, distribution over outcomes, total variation distance
- equations:       the Lipschitz condition; D_TV                                                          ← one TANGENT (D_TV explained inside it)
- predict beat:    "Add zip code to d. Does the condition get STRICTER or LOOSER for these two?" before the axis stretches
- source span:     §"Beyond group metrics: individual fairness", §"The (D, d)-Lipschitz condition", §"Fairness through awareness vs. unawareness"; Figure 7.2 (REBUILD); Exercise 9
- status:          pick

## S2 · Both Sides Were Right                                             tier: single-insight
- question:        ProPublica said COMPAS was biased; Northpointe said it was fair. Both had the data. How can both be telling the truth?
- key case:        Broward County: ProPublica — Black defendants who were not re-arrested were labeled high-risk at ~2× the rate of white defendants (an equalized-odds violation, real). Northpointe — at every score bucket the same fraction of Black and white defendants re-offended (calibration parity, real). Base rates of re-arrest in the data differed
- naive:           "one of them must have the numbers wrong — more data will settle it"; the chapter's line: a values disagreement dressed as a factual one
- representation:  the SAME two confusion grids from S1's family, read two ways. Read by ROW (condition on what actually happened): the false-positive cell over the true-negative row → ProPublica's number, unequal. Read by COLUMN (condition on the score): positives over the predicted-positive column → Northpointe's number, equal. Highlight the rows, then the columns, on unchanged cells — two conditionings, one table
- abstraction:     FPR = P(Ŷ=1 | Y=0, A) vs calibration P(Y=1 | P̂=p, A) = p are different conditionals on the same cells; with unequal base rates the theorem (S1) says they cannot both be equal across groups, so the dispute is which one should win — and COMPAS's implicit choice (calibration) was never signed as a values claim
- boundary:        the sentencing-context judgment (whose liberty bears the false positive) and "who should have decided" (the court, not the engineers) — stated as the audit deliverable, not argued from data → YOUR TURN: Warm-Up 3, in your own words, naming the kind of disagreement
- terms (prereq):  false-positive rate, calibration (a score means the same thing in both groups), base rate
- equations:       none new (the two conditionals are S1's)
- source span:     §"The COMPAS case — the theorem in public" (the two-column table), §"Who should have decided"; Angwin et al. 2016 / Dieterich et al. 2016 as cited
- status:          pick  (note: the chapter gives "~2×" and no cell counts; the grids animate with S1's hypothetical numbers unless factcheck pulls Broward cell counts from the public repo)

## S4 · Flip One Cause, Hold the Rest                                     tier: standard
- question:        Two models show the same correlation between race and the prediction. Why can the data alone never tell you which one is discriminating?
- key case:        loan-default model with A (race) → E (educational credential) → Y (default), plus a direct path A → Ŷ. Ask: had this person been white instead of Black, U held fixed, would the predicted default probability move? E sits downstream of A, so flipping A flips E, the prediction moves — criterion violated
- naive:           read the A–Ŷ correlation off the data (Rung 1) — direct, mediated and confounded disparities all look identical there; or drop A (S3's naive, returning)
- representation:  one small causal graph with three paths from A to Ŷ lit one at a time — direct (A → Ŷ), indirect (A → M → Ŷ), spurious (A ← C → Ŷ) — each producing the same A–Ŷ correlation bar. Then the three-step process on ONE individual: abduction (back out U from the observed x, a), action (set A ← a′), prediction (propagate to Ŷ) — a process one state at a time, the U node held fixed while A flips
- abstraction:     counterfactual fairness: P(Ŷ_{A←a}(U) = y | X = x, A = a) = P(Ŷ_{A←a′}(U) = y | X = x, A = a); the subscript is a counterfactual on an observed individual (Rung 3), not a population intervention (Rung 2); the price is a full causal graph plus a signed list of which paths are illegitimate
- boundary:        disparate treatment vs disparate impact as the legal mirror of direct vs indirect (one line); the remedy (drop variables downstream of A on illegitimate paths) — named, not built → YOUR TURN: Exercise 12's three first-gen paths (SAT, direct, family-income confounder): block or keep, one sentence each
- terms (prereq):  structural causal model, mediator, confounder, Pearl's three rungs (from Chapter 6)
- equations:       the counterfactual-fairness criterion                                                   ← one TANGENT (the subscript notation is the whole tangent)
- predict beat:    "Flip A. E is downstream. Does the prediction move?" before the propagation step runs
- source span:     §"Causal fairness: what the data cannot tell you", §"Structural causal models and the fairness question", §"Counterfactual fairness" (three steps), the four-row comparison table; Figures 7.3–7.4 (REBUILD; both captions inside merge conflicts)
- status:          pick

## S5 · Collapse Each Group to Its Mean                                   tier: single-insight
- question:        A group audit says the model is fair. Can it still be treating people inside each group wildly unequally — and how much?
- key case:        Exercise 10: Group A (n = 200, μ_A = 0.65, GE_A(2) = 0.05), Group B (n = 200, μ_B = 0.45, GE_B(2) = 0.04), overall μ = 0.55. Between-group term: every A gets 0.65, every B gets 0.45 → GE(2) = ½·(0.1/0.55)² ≈ 0.0165. Weighted within-group: 0.5·(0.65/0.55)²·0.05 + 0.5·(0.45/0.55)²·0.04 ≈ 0.0349 + 0.0134 ≈ 0.0483. Total ≈ 0.065; within-group ≈ 75%. (Computed here from the exercise's givens — the chapter poses, does not solve; re-verify at factcheck.) Warm-Up 5 as the first INSTANCE: μ = 0.6, σ = 0.3 → GE(2) = ½(0.5)² = 0.125
- naive:           report the two group means (0.65 vs 0.45) and call the gap "the unfairness" — that is only the between-group term; a clean group audit can hide a large within-group term (Exercise 15)
- representation:  400 dots of benefit on one axis, colored by group. Step 1: collapse every dot onto its group's mean — the spread that survives is the BETWEEN term. Step 2: restore each group's spread around its own mean — the extra is the WITHIN term. A decomposition: total = within + between, drawn as one stacked bar that splits as the dots collapse and re-spread
- abstraction:     GE(2) = ½(σ/μ)²; GE(α) = Σ_g (n_g/N)(μ_g/μ)^α GE_g(α) + GE_between(α); the ratio steers the remedy (mostly between → reweight / thresholds; mostly within → how the model treats individuals inside a group)
- boundary:        general α (what low vs high α weights) and the Theil / MLD special cases — named only; GE needs a cardinal b_i and is not causal → YOUR TURN: Exercise 15 — build the pattern where between = 0 and within is large, and say why a group audit passes it
- terms (prereq):  benefit b_i, mean μ, standard deviation σ, coefficient of variation
- equations:       GE(2) = ½(σ/μ)²; the within/between decomposition                                      ← two TANGENTs
- predict beat:    "Collapse both groups to their means. Is more than half the unfairness gone, or less?" before the dots move
- source span:     §"The Generalized Entropy Index" (formula, GE(2) special case, decomposition, "What the GE Index does not do"); Figures 7.5–7.6 (REBUILD; 7.5 caption inside a merge conflict); Warm-Up 5, Exercises 10 and 15
- status:          pick  (lowest rank: the body states the formula and the decomposition without a worked example; the numbers live in the exercises)

## Not sectioned (by design)
- "Three definitions" as its own film — three equations and a values table with no case; it is S1's TERMS beat and the chapter's own opener already motivates them.
- "Each metric is a values claim" — assertion, no case; folded into S1's ABSTRACTION line and S2's PAYOFF.
- "The toolkit and what it cannot do" (pre- / in- / post-processing) — a taxonomy table, no worked case, no representation that moves; a `not-yet-sectionable` reading unless a chapter revision adds one intervention re-computed on the S1 numbers (Glimmer 7.1 step 5 would supply it).
- "The defense as deliverable" (the six-box scaffold, Figure 7.7) — a checklist, not a mechanism; it is every card's YOUR TURN surface, not a section.
- "Who should have decided", "Two Botspeak pillars", "The persistent limits", "What would change my mind / Still puzzling" — argument and back matter; S2 carries the one line that matters.
- AI Wayback Machine (Mill), Glimmer 7.1, the LLM Exercise, the D3 prompts — practice and back matter.

## Multi-act candidates (need explicit approval)
- S1+S2 share the confusion-grid objects end to end; S2's HOOK ("both were right") is S1's BOUNDARY ("one of them has to give — which is not a math question"). One ~9–11 min film "The Theorem, Then the Trial" is legal under the sectioning exception. Default remains two films.
- S3, S4, S5 are the chapter's "three exits, one bill" run, but they share a narrative, not a key case (loan applicants / loan-default graph / hiring benefit scores) — NOT eligible for multi-act; three films.
