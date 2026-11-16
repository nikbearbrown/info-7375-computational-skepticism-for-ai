# FACTCHECK — claude-liam-financial-stress-index
_Source: books/computational-skepticism-for-ai/youtube/financial-stress-index-source.md_

VERDICT: PASS

## Claims verified

| Beat | Claim | Source line | Verdict |
|------|-------|------------|--------|
| B00 | Index collapses credit markets, bank funding, interest rates, volatility, leverage, investor risk appetite | Source §intro | PASS |
| B00 | "trouble isn't the ambition — it's the construction" | Source §core problem | PASS |
| A1V | One headline number, six sub-components | Source §intro | PASS |
| A1V | Three methods: contribution analysis, ML, TDA | Source §intro | PASS |
| A1M | In a crisis, "everything correlates to 1" | Source §Part 1 | PASS |
| A1M | Credit spreads move with vol, which moves with funding stress | Source §Part 1 | PASS |
| A2M1 | SHAP reports each of two 0.9-correlated indicators at ~40% | Source §Part 1 "SHAP splits credit fairly" | PASS |
| A2V1 | Collinear inputs → no single correct decomposition | Source §Part 1 "When inputs are collinear" | PASS |
| A2V1 | SHAP, regression decomposition, LMG give different answers | Source §Part 1 "Regression decomposition gives DIFFERENT attributions" | PASS |
| A2V2 | Lead with multicollinearity diagnostic (VIF / correlation heatmap) | Source §Part 1 "Feedback angle" | PASS |
| A2V2 | VIF that spikes during crises IS itself a finding | Source §Part 1 | PASS |
| A2M2 | VIF illustration: calm ~2-3, crisis spikes 15-20 | Illustrative — no specific numbers in source; consistent with VIF dynamics for near-perfectly correlated inputs | ILLUSTRATIVE — labeled as stylized |
| A2R | SHAP and regression decomp encode different definitions; both valid | Source §Part 1 | PASS |
| A3M | Modern crisis episodes: 2008 GFC, 2020 COVID, 2022 rate shock | Source §Part 2 "three or four episodes" | PASS |
| A3M | Feature importance on ≈3 data points | Source §Part 2 | PASS |
| A3V | Small window shifts can reorder importance ranking | Source §Part 2 "small shifts to the window boundaries could reorder" | PASS |
| A3R | Robustness check: perturb ±1 month, recompute ranking | Source §Part 2 "Feedback angle" | PASS |
| A4M | TDA sensitive to: embedding dim, delay, distance metric, filtration range, window length | Source §Part 3 | PASS |
| A4V | Easy to produce striking topology diagram that is an artifact of one parameter choice | Source §Part 3 "easy to produce a striking 'topological signature'" | PASS |
| A4R | Parameter-sensitivity sweep as first-class methodological step | Source §Part 3 "Feedback angle" | PASS |
| A4R2 | Cross-validate TDA against Part 1: convergence = evidence; divergence = investigate | Source §Part 3 "ask whether TDA findings are cross-validated" | PASS |
| A5C | Decomposition is not causal identification | Source §Part 4 | PASS |
| A5M | "accounts for 40% of variance" is descriptive; "caused the spike" is causal | Source §Part 4 exact language | PASS |
| A5V | Methods: statistical association/decomposition, not exogenous shocks | Source §Part 4 | PASS |
| A5R | Audit draft for causal verbs: drove, caused, triggered | Source §Part 4 "Feedback angle" | PASS |
| A6C | Visualization honesty under collinearity | Source §Part 5 | PASS |
| A6M | Stacked-area / waterfall contribution charts imply cleanliness collinear inputs don't support | Source §Part 5 | PASS |
| A6V | Where VIF shows serious collinearity — communicate uncertainty, not crisp percentages | Source §Part 5 | PASS |
| A6R | Cross-method comparison charts should show agreement AND disagreement | Source §Part 5 | PASS |
| BVDT | Reviewers probe collinearity handling and crisis-sample size | Source §Close "publication note" | PASS |
| BHTF | "Your turn" close — open questions for Mickey | Source §Close "End with one or two open questions" | PASS |

## Caution flag

- A2M2 VIF numbers (calm ~2-3, crisis 15-20) are illustrative, not empirical. Beat narration says "stylized, not real data" and Manim spec says the same. The visual is clearly labeled.
- Student is called "Mickey" throughout — never a last name. PASS.

## Source fidelity

All substantive claims trace directly to the source document. No claims exceed the source's scope. The description/causation distinction (Part 4) is faithfully preserved — no causal language used in narration.
