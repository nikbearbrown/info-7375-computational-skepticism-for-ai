# FACTCHECK — tldr-features-entering-a-room

Status: **GATE F verified 2026-09-23 by Claude (Opus 5.5) against the chapter as written. Every number on screen is the chapter's own or recomputed from its own inputs; `make_sheet.py` and `scenes.py` assert them at import. Human sign-off pending.**

Source: `chapters/05-model-explainability-distinguishing-explanation-from-the-appearance-of-explanation.md` (HEAD side of every merge-conflict block — Figures 5.2–5.4), §"What SHAP is, and what SHAP isn't", §"The mathematics of Shapley values" (value function, marginal contribution, Shapley value, Efficiency) and §"A worked example"; exercises W4, W5. Section S1 of `youtube/tldr-sections-05-explainability.md`.

**The worked example is constructed.** The chapter introduces it with "Suppose we have a model…", "Say the six orderings produce…" and "Suppose the same calculation produces φ_x2 = 0.062 … φ_x3 = 0.035". The film captions it "constructed example" once, small, dim, and keeps the caption on the LEARN stage B10–B19.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | Course credit: chapter five of INFO 7375, Computational Skepticism for AI, Northeastern | ✓ PASS | course-film convention (spoken + on the cards' course line) | — |
| 2 | B10, B19 | One applicant: f̂(x) = 0.72 (chance of approval), E[f̂] = 0.55, gap 0.17 | ✓ PASS (constructed) | §A worked example: "f̂(x) = 0.72 (72% probability of approval) and E[f̂] = 0.55 … 0.72 − 0.55 = 0.17"; asserted | captioned constructed |
| 3 | B03, B10 | Three features: income, debt-to-income ratio, zip code | ✓ PASS | §A worked example | on-screen short forms "debt", "zip" after B10 |
| 4 | B11 | With no features known the model predicts the average (v(∅) = E[f̂]) | ✓ PASS | §The value function: "v(∅) = E[f̂]: with no features, predict the global average" | — |
| 5 | B11 | Income first → +0.08; score 0.55 → 0.63 | ✓ PASS (recomputed) | Table row (x1, x2, x3): Δ = +0.08 with coalition ∅; 0.63 = 0.55 + 0.08 = v({x1}), asserted in make_sheet.py | — |
| 6 | B11 | "the other two still averaged over the data" | ✓ PASS | §A worked example: "averaging the model's output over random draws of the remaining features from the training data" | — |
| 7 | B12 | Full room 0.72; without income 0.66; income worth 0.06 = income arriving last | ✓ PASS (recomputed) | v(F) = f̂(x) = 0.72; rows (x2, x3, x1), (x3, x2, x1): Δ = +0.06 with coalition {x2, x3} ⇒ v({x2, x3}) = 0.66, asserted | — |
| 8 | B13 | Debt then income: +0.07; zip then income: +0.09 | ✓ PASS | Table rows (x2, x1, x3) and (x3, x1, x2) | — |
| 9 | B14 | 3! = 6 orders, equally likely; two start with income, two end with it, two put it in the middle | ✓ PASS | "There are 3! = 6 orderings"; "Every ordering is equally likely"; the table | — |
| 10 | B15, B16, B19, BVDT | φ_income = (0.08 + 0.08 + 0.07 + 0.09 + 0.06 + 0.06)/6 = 0.073 | ✓ PASS | chapter's own sum; recomputed 0.0733… → 0.073 (asserted) | — |
| 11 | B15, B18 | φ_debt = 0.062, φ_zip = 0.035 ("the same six-order average") | ✓ PASS (constructed) | "Suppose the same calculation produces φ_x2 = 0.062 … φ_x3 = 0.035". Consistency: a value function exists that gives these (v(∅)=.55, v1=.63, v2−v3 ≈ .037, v23=.66, vF=.72); the film shows no v(S) for debt or zip | — |
| 12 | B15, B16, B18, BVDT | Efficiency: 0.073 + 0.062 + 0.035 = 0.17 = 0.72 − 0.55; nothing left over | ✓ PASS | "Efficiency check … The values sum exactly to the prediction deviation"; asserted | — |
| 13 | B16 | Grouped by coalition: 2/6·0.08 + 1/6·0.07 + 1/6·0.09 + 2/6·0.06 = 0.073 | ✓ PASS (derivation) | weight |S|!(|F|−|S|−1)!/|F|! for |F| = 3: |S| = 0 → 2/6, |S| = 1 → 1/6, |S| = 2 → 2/6; weighted sum = 0.44/6 = 0.0733, asserted equal to the ordering average | — |
| 14 | B16, B17 | The Shapley formula φᵢ = Σ_{S⊆F∖{i}} |S|!(|F|−|S|−1)!/|F|! [v(S∪{i}) − v(S)] | ✓ PASS | chapter's formula, typeset as MathTex | — |
| 15 | B17 | The weight is the fraction of orderings in which S arrives before i and the rest after | ✓ PASS | "The weight … counts the fraction of all |F|! orderings in which the features in S all precede i and all features not in S ∪ {i} follow i" | — |
| 16 | B17 | |F| = 3, |S| = 1: 1!·1!/3! = 1/6 (and |S| = 0: 0!·2!/3! = 2/6) | ✓ PASS | exercise W4; asserted | — |
| 17 | B16, B18 | Σφᵢ = f̂(x) − E[f̂] | ✓ PASS | Efficiency axiom as stated | — |
| 18 | B18 | "A force plot is efficiency, drawn" | ✓ PASS | "the force-plot visualization … is exactly this property rendered visually"; Figure 5.4 caption | — |
| 19 | B01 | "Every SHAP bar in a model report estimates this average" | ✓ PASS (hedged) | §What SHAP is: SHAP computes the marginal contribution "averaged over all possible orderings"; §Computational shortcuts: in practice approximated (KernelSHAP, permutation) — hence "estimates" | — |
| 20 | B01 | "the bars must add up to the gap" | ✓ PASS | "the numbers add up — across features — to the model's deviation from a baseline" | — |
| 21 | B19, BVDT | φ_zip = 0.035 is a real number about the model and says nothing about the world (proxy, persistence, mediation) | ✓ PASS | "The attribution to zip code … is a real number describing the model's behavior, and it tells you nothing about the world" | — |
| 22 | BHTF | YOUR TURN: build a 3-feature value function, predict, enumerate orders, check Efficiency, say what zip's share does not tell you | ✓ PASS | transfer of the worked example + exercises W1, W4, W5; no model output shown or simulated | — |
| 23 | all | Nothing datable on screen: no model names, versions, "as of" | ✓ PASS | sweep of the sheet | — |

Deferred (density rule): the four axioms as a set and uniqueness; the 2^|F| blow-up, KernelSHAP / permutation / TreeSHAP; the correlated-feature problem (S2); Rung 1 vs Rung 2 (S4 — named only as B19's boundary). Not used: every `[verify]` flag in the chapter (none touches this card). The three-family table's "income contributed +0.18" (a different illustrative number) is not used.
