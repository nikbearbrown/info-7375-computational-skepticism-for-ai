# tldr sections — Chapter 4: Robustness — What "Understanding" Means When a Pixel Can Break the Model

Source: `chapters/04-robustness-what-understanding-means-when-a-pixel-can-break-the-model.md` (INFO 7375 Computational Skepticism for AI, Nik Bear Brown, Northeastern) · read 2026-09-23 · 4 sections · 2 deferred · course film: carries the course credit (bookloop exception)

Numbers below are copied from the chapter as written. The chapter is a rough draft (header: "CHAPTERIZED 2026-07-02 … Rough draft for hand-rewrite; [verify]/[verify-xref] flags preserved") and carries 13 unresolved git merge-conflict blocks (`<<<<<<< HEAD` … `>>>>>>> d78899b`, every figure caption plus the next-chapter preview and the Prompts appendix — the HEAD side numbers figures 4.x, the other side 8.x) and 8 `[verify]` flags. Flags that touch a card are carried into it. Everything re-verifies at `factcheck` for whichever film builds.

Already on this chapter, different genre (deep-explainer register, not lessons): `claude-liam-deep-04-robustness` ("The Model Isn't Broken. It's Honest."), plus the cs/vox shorts `claude-liam-cs-05-million-pixel-flip`, `claude-liam-cs-17-panda-proxy` / `claude-liam-vox-panda-proxy`, and the cli films `claude-liam-cli-adversarial-perturbation-detector`, `claude-liam-cli-llm-prompt-sensitivity-tester`, `claude-liam-cli-distribution-shift-detector`. A tldr film is additive: one aha, taught 3b1b-style, not a walk of the chapter.

Ranked by how visible the representation already is in the source (a filled table and an equation with a worked structure first; a conceptual decomposition last).

## S4 · Robust Against What?                                           tier: single-insight
- question:        A vendor says the model is "94% accurate and robust." Robust against what?
- key case:        the chapter's disclosure template, Section 1: clean 94% everywhere, but robust accuracy 71% under L∞ white-box at ε = 0.03 (FGSM/PGD), 58% under a transfer attack (surrogate ResNet-50 trained on the same data), 87% under natural shift (Q4 2023 → Q1 2024, time-shift only) — three different numbers hiding behind one word
- naive:           "robust" as a single adjective, or a single number — the chapter's phrase: decoration on the marketing page; the fluency trap in a lab coat
- representation:  the table filling one row at a time: a 94% bar that stays fixed in the clean column while the robust column drops to a different height per attack class; the rows are separate axes (Figure 4.5: adversarial robustness and distribution-shift robustness do not guarantee each other) — then Sections 2 and 3 appear as blanks the sentence "it's robust" never fills
- abstraction:     robustness is a profile, not a number: attack class × budget × robust accuracy at that budget, plus residual risk and a monitoring trigger; a claim without this structure is not a claim
- boundary:        what each toolkit tool buys and costs (the six-row toolkit table) is its own reading; YOUR TURN = exercise 6: five questions that turn a facial-recognition vendor's "robust" into a specification
- terms (prereq):  clean accuracy, perturbation budget ε (L∞ = no pixel moves more than ε), transfer attack (surrogate model), distribution shift (Chapter 2)
- equations:       none
- note:            the three rows are the chapter's TEMPLATE values (a disclosure form with blanks), not a measured model; the film must caption them as illustrative
- source span:     §"Distribution shift, returning from Chapter 2" (Figure 4.5); §"Towards honest robustness disclosure" (Sections 1–3 template); exercises 3, 6, 13
- status:          built → tldr-robust-against-what (master 2026-09-23 12:43, verdict pending)

## S2 · The Tiny Push That Adds Up                                      tier: standard
- question:        How can a change too small to see in any one pixel flip a classifier — with higher confidence than before?
- key case:        the chapter's linear classifier f(x) = wᵀx: perturb by δ with every coordinate capped at ε; choose δ = ε·sign(w) and the activation moves by ε‖w‖₁, which grows with the number of dimensions d while ε stays invisible
- naive:           "the change is a fraction of a percent per pixel, so the total change must be a fraction of a percent" — true for one coordinate, false for thousands acting in concert
- representation:  a row of d coordinate cells each nudged by ±ε in the sign of its weight (Figure 4.3, rebuilt): per-cell bars stay tiny, a running-sum bar on the right climbs by ε|wᵢ| per cell; hold ε fixed and grow d (a handful → hundreds → thousands of cells) — the per-cell push never changes, the sum crosses the decision threshold; then the same picture with sign(∇ₓL) in place of sign(w) for a piecewise-linear (ReLU) network
- abstraction:     Δf = wᵀδ = ε Σᵢ|wᵢ| = ε‖w‖₁ — the linearity hypothesis; FGSM is this move on the loss gradient: x′ = x + ε·sign(∇ₓL(f(x), y)), a gradient-ASCENT step on the loss
- boundary:        why neural nets are MORE vulnerable than other linear classifiers (boundary tilting → S3); PGD, the iterated version with projection back into the ε-ball, named not taught; YOUR TURN = exercise 4 (identify each term of FGSM; say why it is ascent, not descent)
- terms (prereq):  dot product wᵀx, sign function, L∞ budget (max coordinate), gradient (as "the direction that raises the loss fastest")
- equations:       Δf = ε‖w‖₁; x′ = x + ε·sign(∇ₓL)                                    ← two TANGENTs
- predict beat:    "ε stays the same; I double d. Does the total push double, stay, or shrink?" before the sum bar grows
- source span:     §"The linearity hypothesis" (Figure 4.3); exercise 4; PGD equation in §"Adversarial training and its scaling limits" (boundary only)
- status:          pick

## S3 · The Boundary That Leans on the Data                             tier: single-insight
- question:        Two classifiers separate the same training data perfectly. Why can one be pushed across its boundary by a step you cannot see, and the other not?
- key case:        Tanay and Griffin's observation, as the chapter states it: a well-regularized, wide-margin linear classifier does not show adversarial vulnerability at the same rate; the vulnerable model's boundary lies nearly tangent to the data manifold in the low-variance directions the training data never forced it to close (Figure 4.4)
- naive:           "training accuracy is 100%, so the boundary is in the right place" — it is in the right place along the axis the data varies most; nothing checked the other axis
- representation:  a 2-D scatter stretched along one axis (high variance) and thin along the other (low variance) with a separating line; TILT the line about the cloud: separation along the long axis is held invariant (training accuracy unchanged) while the perpendicular distance from the thin edge of the cloud to the line collapses; the same short arrow that failed to cross the well-placed boundary now crosses the tilted one
- abstraction:     adversarial examples live where the decision boundary is poorly constrained in low-variance directions — directions with little training signal; a perturbation is a gradient-guided search for exactly those directions
- boundary:        neither geometric account is complete on its own (the chapter says so); the "not bugs, features" data-level account → S1; YOUR TURN = exercise 5 (what tilting adds to linearity, and where you should expect vulnerability to concentrate)
- terms (prereq):  decision boundary, data manifold (as "where the training points actually lie"), variance along a direction, margin
- equations:       none
- predict beat:    "I tilt the line and the training score does not move. Which direction does the attacker's arrow get shorter in?" before the tilt
- source span:     §"The boundary-tilting perspective" (Figure 4.4); closing paragraph of §"Why adversarial examples exist"
- status:          pick

## S1 · The Proxy, Not the Panda                                        tier: single-insight
- question:        The panda did not move. What did?
- key case:        the chapter's opener: Goodfellow, Shlens & Szegedy 2015, Figure 1 — panda classified "panda" with high confidence; an imperceptible perturbation added; classified "gibbon" with even higher confidence; the two pictures indistinguishable side by side
- naive:           "the model is fragile — harden it" (Figure 4.2, left column): harden against this δ and a slightly different δ finds a new proxy; the attack surface moves, the gap does not
- representation:  the image decomposed into two stacked channels (Figure 4.9, rebuilt): a ROBUST channel (shape, posture, colouring) and a NON-ROBUST channel (the high-frequency statistical signature); the perturbation slides only the non-robust channel from "panda-signature" toward "gibbon-signature" while the robust channel is held fixed; the model's weight sits on the channel that moved — two cases differing in exactly one respect
- abstraction:     an adversarial perturbation is a deliberate manipulation of non-robust features; the model learned a proxy that co-occurred with the label, and is "honest about what this training produced" — the diagnosis changes the response from hardening to representation interrogation
- boundary:        whether non-robust features are universal data properties or artifacts of the supervised objective is contested (chapter: `[Verify: status of "features not bugs" debate, 2023–2025]`) — named, not settled; the Rung 3 counterfactual opened, not closed; YOUR TURN = exercise 7 (map the panda onto Case #8 owner-identity spoofing, then name where the analogy breaks)
- terms (prereq):  classifier, confidence, perturbation, training distribution
- equations:       none
- note:            closest in subject to the existing `claude-liam-deep-04-robustness`; differs in genre (one aha on the two-channel picture, not the chapter walk). The chapter gives no confidence percentages for the panda/gibbon — do not add the paper's; if wanted, they must be fact-checked as our own
- source span:     opening (Figure 4.1); §"What adversarial examples actually expose" (Figure 4.2); §"Non-robust features — the deepest account" (Figure 4.9); §"Case #8" (Figure 4.12) as the transfer case
- status:          pick

## S5 · Voting Through the Noise (randomized smoothing)                 tier: single-insight
- question:        How can anyone GUARANTEE a classifier will not flip inside a radius, when the attacker gets to search?
- key case:        the chapter gives the smoothed classifier g(x) = argmax_c E_{δ~N(0,σ²I)}[1[f(x+δ)=c]] and the certified radius R = (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)) with Figure 4.7 ("votes by majority across thousands of noisy versions") — but no worked instance: no σ, no p_A, no p_B, no R
- naive:           "test a thousand perturbations and none flipped it, so it's safe" — sampling is not a guarantee
- representation:  a cloud of noisy copies of x, each voted, tallying into two bars p_A and p_B; the certified circle grows with the gap between the bars and with σ — while the copies blur until the base classifier can no longer read them (the clean-accuracy cost)
- abstraction:     R = (σ/2)(Φ⁻¹(p_A) − Φ⁻¹(p_B)); certification is a lower bound inside R and says nothing outside it
- boundary:        thousands of Monte Carlo samples per prediction; radius shrinks with dimension; nothing outside R
- terms (prereq):  Gaussian noise, inverse normal CDF Φ⁻¹, majority vote
- equations:       g(x); R                                                          ← two TANGENTs
- source span:     §"Certified defenses — what 'guaranteed' means and costs" (Figure 4.7)
- status:          deferred — representation is drawable, but every INSTANCE (σ, p_A, p_B, R) would be our own number, computed and fact-checked against Cohen, Rosenfeld & Kolter 2019, not the chapter's; hold until the chapter carries a worked instance

## S6 · Why Scale Cannot Buy the Last Ten Percent                      tier: single-insight
- question:        If bigger models are more robust, why does the curve stop at 90%?
- key case:        Bartoldson et al. 2024 as the chapter reports it: on CIFAR-10, L∞ robustness grows with scale and plateaus around 90% — and human accuracy on the fooling set ALSO plateaus near 90%, because at standard budgets the perturbed images start to genuinely look like the target class; the "10³⁰ FLOPs to reach human level by scale alone" figure is **[verify]** (chapter: not confirmed in the abstract)
- naive:           "just scale up"
- representation:  two curves on one axis — model robust accuracy rising and flattening, human accuracy flat at the same ceiling — with an ε slider beneath: as ε grows the image itself crosses into the target class, so the ceiling is semantic, not computational
- abstraction:     the accuracy–robustness ceiling is governed by the semantics of the perturbation budget; scale cannot cross a semantic limit
- boundary:        the 10³⁰ figure until verified; Lipschitz-bounded architectures as the other route (its "as low as 6" also **[verify]**; the confirmed 2025 figure is a 10-Lipschitz transformer at ~21% accuracy)
- terms (prereq):  scaling law, perturbation budget ε
- equations:       none
- source span:     §"Adversarial training and its scaling limits" (Figure 4.6); §"What would change my mind"
- status:          deferred — the chapter supplies only the plateau value and the qualitative shape; the curve points would have to be lifted from arXiv:2404.09349 and the load-bearing 10³⁰ number is flagged unverified in the source itself

## Not sectioned (by design)
- "A taxonomy of attacks" (six-row table) — a reference table, not an aha; feeds the TERMS beat and BOUNDARY of S4.
- "The robustness toolkit" (six-row table) and Lipschitz / formal verification (α,β-CROWN) — survey of tools with costs; each row is an assertion, no worked case; S4's boundary names them.
- "Prompt sensitivity" — `not-yet-sectionable`: the chapter's example pair ("List the key points…" / "What are the main takeaways…") has no actual outputs, and the IPS framework is described, not computed; any moving representation would be invented. Also already covered by `claude-liam-cli-llm-prompt-sensitivity-tester`.
- "Cross-domain transfer" table and Case #8 owner-identity spoofing — the chapter itself bounds "same structure" as an analogy, not a mechanism; used as S1's transfer exercise (exercise 7), not a section.
- "Pearl's Ladder Rung 3 — opened, not closed" — the chapter deliberately does not close it (Chapter 12 does); a BOUNDARY line in S1, not a film.
- Glimmer 4.1, the calibration baseline, "What would change my mind", synthesis, exercises, the LLM Exercise / casebook prompt, AI Wayback Machine (von Neumann), the D3 Prompts appendix — practice and back matter.

## Multi-act candidates (need explicit approval)
- S2+S3 ("Why adversarial examples exist — two geometric accounts"): S3's HOOK is S2's BOUNDARY (linearity explains why the push works; tilting explains why nets are especially exposed). They do NOT share one key case (a weight vector vs a 2-D cloud), so the exception is weak; default remains two films.
- S1+S4: the panda opens the chapter and the "94% and calls it robust" line sits in the same opening paragraph, but the objects on screen differ (two feature channels vs a disclosure table). Not recommended as multi-act.

## Chapter flags carried (for the hand-rewrite, not for the films)
- 13 unresolved merge-conflict blocks (`<<<<<<< HEAD` / `>>>>>>> d78899b`), one per figure caption plus the next-chapter preview (Chapter 5 vs Chapter 9) and the Prompts appendix; figure numbering is 4.x on HEAD and 8.x on the other side.
- 8 `[verify]` / `[Verify: …]` flags: header `[verify]/[verify-xref]`; PGD-AT "≈9×" cost; Bartoldson 10³⁰ FLOPs (twice — flagged in the toolkit section, then stated unflagged in "What would change my mind"); Lipschitz "as low as 6"; status of the "features not bugs" debate; state of the art in representation-level robustness.
- Figure 4.1 alt text carries the typo "invisble" on the non-HEAD side and in the Prompts appendix.
