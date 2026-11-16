# CHECKS-REPORT — tldr-features-entering-a-room

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11–B15, B17, B18) | FALSIFIABILITY ✓ (B14 predict → B15)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy` — two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS
Four prerequisites the lesson uses without stopping: feature, prediction, baseline, coalition. The film's answer — the Shapley value, and Efficiency — is NOT in TERMS; both land in B16.

## The one representation
The room ledger: one row per arrival order of the three features, recording the bump income makes when it walks in — six rows, six bumps — set above a prediction line whose gap (0.55 → 0.72) the averaged bumps must fill.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ the chapter's worked example: f̂(x) = 0.72, E[f̂] = 0.55; income's six bumps +0.08 +0.08 +0.07 +0.09 +0.06 +0.06; φ = 0.073 / 0.062 / 0.035 — constructed, captioned so |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: "how much of the 0.17 is income's?" — no φ, no "Shapley", no "marginal" until B16 |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (first in, +0.08), B13 (middle, +0.07 / +0.09), plus B12 and B14's rows, all before B16 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 = prerequisites; "Shapley value" and "efficiency" named in B16 after the bars filled the gap |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B12 — "drop it and see": a real measurement (+0.06) that disagrees on screen with B11's (+0.08) |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: "don't pick a room — take every order the three could arrive in" |
| Exactly one TRANSFORM per section | §4 | ✓ B15 (six bars merge into one; three bars fill the span to 0.72) |
| Every landed equation followed by a TANGENT | §4 | ✓ two equations land in B16 (the Shapley formula; the efficiency sum) → B17 tangent (formula; W4's weight 1/6 as the worked value) and B18 tangent (sum; plugged in over the bars) |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19: the same prediction line, span and question from B10, answered on the filled force plot |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: Symmetry/Dummy/Additivity and uniqueness; the 2^|F| blow-up and KernelSHAP/TreeSHAP; correlated features (S2); Rung 1 vs Rung 2 (S4) |
| Mystery-framed opener | §2 | ✓ B10 — one gap, three features, "it sounds like it should have one answer" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B14 ("do the averages fill 0.17 exactly, overshoot, or fall short? commit") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not taught: what 0.035 means"; BHTF = build your own three-feature v(S), predict, enumerate, check efficiency, and say what zip's share does not tell you (W1/W4/W5) |
| Length derived + tier reported | §5 | ✓ standard tier (one section, two equations → two tangents); measured narration 5:17 |

## Honesty notes
- Constructed example: "constructed example" caption on the LEARN stage B10–B19 (the chapter's own "Suppose"/"Say").
- The film shows v(S) levels only where the chapter's inputs fix them (0.55, 0.63, 0.66, 0.72); the middle-seat bumps are shown as bumps only.
- φ_debt and φ_zip are presented as "the same six-order average" — the chapter's stated values; their tables are not invented.
- "Every SHAP bar … estimates this average" — "estimates" because SHAP approximates the exact average (the chapter's §Computational shortcuts).

## TL;DR paradox check
B00 gives away the conclusion (the fair share is the average bump over every order; the bars fill the gap). It does not show the two disagreeing single-room answers, the ledger, the merge or the stop at 0.72 — the reveal is *seeing* B12–B15.
