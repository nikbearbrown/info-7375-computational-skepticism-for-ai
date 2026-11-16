# tldr sections — Chapter 5: Model Explainability: Distinguishing Explanation from the Appearance of Explanation

Source: `chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 5 sections · 1 deferred · course film: carries the course credit (bookloop exception)

Already on this chapter, different genre (deep-explainer / vox / cs register, not lessons): `claude-liam-deep-05-explainability` ("It Explained the Model. Not the World."), `claude-liam-cs-15-shapley-room` + `claude-liam-vox-shapley-room` ("Why Fair Credit-Splitting Has Exactly One Answer"), `claude-liam-cs-16-language-game` + `claude-liam-vox-agent-deleted` ("Why the AI Wasn't Lying When It Said 'Deleted'"), `claude-liam-fluency-trap`. A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Chapter state the cards inherit: the file is a CHAPTERIZED rough draft (header comment, 2026-07-02) and still carries unresolved git conflict markers (`<<<<<<< HEAD` / `>>>>>>> d78899b`) at every figure caption (5.x vs 6.x numbering) and in the back matter; three in-body `[verify]` flags (the "need and misalignment co-occur" aphorism; the Proton-side persistence mechanics of the Ash case; "What would change my mind"). Every number below is the chapter's own and is re-verified at `factcheck` for whichever film builds.

Ranked by how visible the representation already is in the source (worked table and figures first).

## S1 · Features Entering a Room                                       tier: standard
- question:        How do you split one prediction fairly among three features — and why isn't "drop it and see" enough?
- key case:        loan applicant, three features (income x₁, debt-to-income x₂, zip code x₃); f̂(x) = 0.72, E[f̂] = 0.55, payout 0.17; the six-ordering table for income: +0.08, +0.08, +0.07, +0.09, +0.06, +0.06 → φ₁ = 0.073; φ₂ = 0.062, φ₃ = 0.035; Efficiency check 0.073 + 0.062 + 0.035 = 0.17
- naive:           measure income's contribution once — add it to the empty room (+0.08) or remove it from the full one (+0.06) — and get two different answers; "the" contribution depends on who was already in the room
- representation:  the room (Figure 5.3): three features walk in, in each of the 3! = 6 orders; a table row fills per arrival with the marginal bump on a prediction bar; the six bumps are averaged into one bar; then the three bars snap end-to-end from 0.55 to 0.72 (the force plot, Figure 5.4) with nothing left over
- abstraction:     φᵢ = Σ_{S⊆F∖{i}} |S|!(|F|−|S|−1)!/|F|! · [v(S∪{i}) − v(S)] — the average marginal contribution over every ordering; Efficiency: Σφᵢ = f̂(x) − E[f̂]
- boundary:        the four axioms as a set and uniqueness; the 2^|F| blow-up and KernelSHAP/TreeSHAP; and the sentence the chapter turns on — φ_zip = 0.035 tells you nothing about the world (→ S4)
- terms (prereq):  feature, prediction, baseline (average prediction), coalition
- equations:       the Shapley formula; the Efficiency sum                       ← two TANGENTs (the weight, via W4: |F|=3, |S|=1 → 1!·1!/3! = 1/6, is an INSTANCE, not a third)
- source span:     §"The mathematics of Shapley values" (value function, marginal contribution, Shapley value, Efficiency), §"A worked example"; Figures 5.2–5.4; exercises W4, W5
- status:          built → tldr-features-entering-a-room (master 2026-09-23 13:55, verdict pending)

## S2 · Frankenstein Instances                                          tier: single-insight
- question:        If two features always move together, why does SHAP hand one of them credit for combinations that never happened?
- key case:        10-feature model, coalition S = {x₁, x₂}: the other 8 are drawn from their marginals; x₃ and x₄ strongly correlated → sampled pairs the data never contains; exercise A5's numbers as the second instance: marginal φ_zip = 0.19, φ_income = 0.31 → conditional φ_zip = 0.04, φ_income = 0.46
- naive:           "fix the features I know, average over the rest" — sounds like the definition of v(S), and it is; the trap is WHICH distribution "the rest" come from
- representation:  a scatter of real (x₃, x₄) pairs as a tight diagonal cloud; marginal sampling drops probe points into the empty corners the model never trained on (the model's output there is extrapolation); conditional sampling keeps the probes on the cloud — and then a feature with no direct effect picks up a non-zero bar through its partner
- abstraction:     marginal SHAP asks "how much does this feature move the model on average?"; conditional SHAP asks "how much, given what we already know?" — different questions, and conditional can violate Dummy
- boundary:        neither version can say whether zip code is a proxy for income; that is a Rung 2 question (→ S4); the practitioner's rule: when two features are correlated, run both and compare
- terms (prereq):  marginal vs conditional distribution, correlation, the Dummy axiom (one line)
- equations:       v(S) = E_{x_S̄}[f̂(x_S, x_S̄)]; P(x_S̄ | x_S)                        ← two TANGENTs
- predict beat:    "Which way does zip code's bar move when we stop making Frankenstein applicants — up or down?" before the conditional re-run
- source span:     §"The value function", §"The correlated feature problem"; Figure 5.5; exercises A5, S2, S3
- status:          pick

## S4 · The Model's Counterfactual Is Not the World's                    tier: single-insight
- question:        "If your income were $5,000 higher you'd be approved" — is that a fact about you, or about the model?
- key case:        the chapter's three-family table: SHAP "income contributed +0.18", LIME's local line, the counterfactual "if income were $5,000 higher, the prediction would flip to approve"; the radiologist composite as the stakes (0.84 confidence, features X and Y present, benign biopsy — the chapter labels it a composite, not a sourced incident)
- naive:           the counterfactual is written as an intervention, so it must be causal — read it as "raise your income and the loan is approved"
- representation:  two lanes side by side, the MODEL lane and the WORLD lane; three explanation outputs are placed on Pearl's ladder — SHAP and LIME on Rung 1, the counterfactual on Rung 2 — and an intervention arrow (income +$5,000) moves the prediction in the model lane while the world lane's outcome stays a blank; the five-row "can SHAP answer it?" table fills Yes/No beside them
- abstraction:     attribution is Rung 1 in the model; a counterfactual is Rung 2 in the model; Rung 2 in the model is not Rung 2 in the world — the residual gap is not a tooling defect, it is supervisory territory
- boundary:        which of the many counterfactuals the method picked and why; feasibility of the intervention; the "need and misalignment co-occur" aphorism (chapter flags it [verify] — not taught as a theorem)
- terms (prereq):  Pearl's ladder (Rung 1 association, Rung 2 intervention — the Chapter 4 sketch), counterfactual, attribution
- equations:       none
- source span:     §"What SHAP is, and what SHAP isn't" (the five-row table), §"Counterfactuals are closer to what you actually want" (the three-family table), the worked example's turning sentence, opener; Figures 5.1, 5.6
- status:          pick  (note: closest in subject to the existing `claude-liam-deep-05-explainability`; differs in genre — one aha on one intervention arrow)

## S6 · One Word, Two Games                                              tier: single-insight
- question:        The agent said "the secret has been deleted" and every command it ran was real — so how was the report false?
- key case:        Ash's agent (Agents of Chaos, arXiv:2602.20021): reset the password, renamed an alias, archived the message locally → "deleted" in the agent's scope; the data persists on Proton's servers — backups, recovery window, sync model — outside its scope [verify: chapter flags the provider-side persistence mechanics against the primary]; the two reports of Figure 5.8
- naive:           the agent lied, or the model was wrong — a mis-diagnosis that would send you to a truth-check on the commands, all of which pass
- representation:  nested boxes: the agent's operational scope inside the provider's storage; the word "deleted" is a checklist that fills completely inside the inner box and not at all in the outer; the one report sentence slides across the boundary unchanged and its truth value flips; the second report, with the gap named, stays true in both
- abstraction:     the same explanation can be correct in one language game and misleading in another; the supervisory move is the audience question — who is reading this, and what does the word mean in their game?
- boundary:        why no SHAP/LIME attribution catches this (it would be correct in the local game); operationalizing the audience check at scale — the chapter's own "still puzzling"; Glimmer 5.1 as YOUR TURN
- terms (prereq):  language game (Wittgenstein, one line — the chapter's own reading, not Wittgenstein's claim), scope
- equations:       none
- source span:     §"A short detour through Wittgenstein", §"Back to Ash"; Figures 5.7–5.8; exercise A3
- status:          pick  (note: cs-16-language-game / vox-agent-deleted already tell this case; this card is the lesson on the nested-scope representation, not the story)

## S5 · Three Words That Don't Entail Each Other                         tier: single-insight
- question:        The vendor shipped SHAP on every prediction — so is the sepsis model explainable? Interpretable? To whom?
- key case:        the chapter's three cases: open code, weights and data yet uninterpretable (175 billion parameters); SHAP on every prediction yet no mental model; interpretable to the developer, not to the loan applicant — plus exercise A2's contract ("every prediction must be accompanied by an explainable reason") met by shipping SHAP
- naive:           transparent ⇒ explainable ⇒ interpretable — one dial, turned up
- representation:  three independent switches (system / output / understanding-in-a-person) with an audience column; the chapter's rows fill the table one switch on and the others off — the row that has all three on for the developer and none for the patient is the common failure mode
- abstraction:     transparency is a property of the system, explainability of outputs, interpretability of the understanding a human builds; none entails another, and interpretability is indexed to an audience
- boundary:        Rudin's argument for inherently interpretable models in high-stakes decisions — named, not argued; exercise W2 as YOUR TURN
- terms (prereq):  none (the three words are the ABSTRACTION, not prerequisites)
- equations:       none
- source span:     §"Three words that don't mean the same thing" and its table; exercises W2, A2
- status:          pick  (weakest representation of the five — a table filling, no moving quantity; safest as a short single-insight)

## S3 · LIME Run Twice                                                   tier: —
- question:        Same input, same model, two different explanations — which one is right?
- key case:        the chapter asserts it ("Run the same input twice, and you can get different explanations, because the perturbations are sampled randomly") and exercise A1 poses it, but gives no input, no perturbation cloud, no coefficients
- naive:           one of the two runs is the correct explanation
- representation:  a perturbation cloud around one point with a fitted line; resample → a different line — nameable, but every number on it would be ours
- abstraction:     LIME is a local linear surrogate; its coefficients are a sample, not a property
- boundary:        —
- terms (prereq):  perturbation, surrogate model
- equations:       none in the chapter
- source span:     §"LIME, in a different shape"; exercise A1
- status:          deferred — not-yet-sectionable: the source states the abstraction without a worked case; the cloud and both lines would have to be invented and then fact-checked as our own

## Not sectioned (by design)
- The radiologist opener — a labelled composite with one number (0.84); stakes for S4's HOOK, not a section of its own.
- The four axioms as a set (Symmetry, Dummy, Additivity/Linearity, uniqueness) — Efficiency is earned in S1, Dummy is a BOUNDARY line in S2; the rest is a survey, no case.
- "Computational shortcuts" (KernelSHAP, antithetic/permutation sampling, TreeSHAP O(TLD)) and its method table — a comparison table with no worked instance.
- Glimmer 5.1, the LLM Exercise (Red-Team Casebook), exercises, "Where this leaves us", "What would change my mind" / "Still puzzling", the AI Wayback Machine (Reichenbach), the D3 figure prompts — practice and back matter; Glimmer 5.1 and W2/A3/A5 feed YOUR TURN beats.

## Multi-act candidates (need explicit approval)
- S1+S4 share the 0.72/0.55 loan applicant: S4's HOOK ("φ_zip = 0.035 is a real number about the model") is S1's BOUNDARY, and the force-plot bars stay on screen. One ~9–11 min film "The Room and the Rung" is legal under the sectioning exception. Default remains two films.
- S1+S2 share the same applicant and the same v(S); S2's HOOK is where S1's "average over the rest" comes from. Legal, but S2's scatter cloud is a new object, so the join is weaker than S1+S4.
