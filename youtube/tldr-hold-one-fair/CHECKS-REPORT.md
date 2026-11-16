# CHECKS-REPORT — tldr-hold-one-fair

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    16 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B13, B18) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video, by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy`: two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS
B03 holds four prerequisites (base rate, TPR, FPR, PPV). The film earns the trade (the odds identity and "one must give"); calibration and equalized odds are named in the HOOK as the two asks, in plain words first.

## The one representation
Each group is a unit square whose positive column is as wide as its base rate; the model's flags fill the columns from the bottom; the flagged area, gathered into one pile, is dark (truly positive) and grey (not). **The pile's dark-to-grey ratio is the world's width ratio times the model's height ratio.** The odds identity is that picture written down.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ base rates 0.6 / 0.3; the chapter's two tables (PPV 0.75/0.75 with TPR/FPR 0.60/0.30 vs 0.70/0.10; TPR/FPR 0.70/0.15 both with PPV 0.88/0.67) |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: two groups, two asks, "tune our way to both?" (the identity is not said until B17) |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11, B12, B13 (+ B15) precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 = base rate, TPR, FPR, PPV; the identity and "one must give" are earned in B14–B19 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13: "a better model" — both piles improve, the gap survives |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: the pile's mix is the world's widths times the model's heights |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (pin PPV: columns move, piles align, heights split; release; re-pin) |
| Every landed equation followed by a TANGENT | §4 | ✓ B17 lands the odds identity → B18. The cross-group ratio is folded into B17's words ("pin one, the other splits") and B16's 2 vs 7, not landed as a second equation (density rule §6) |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19: the same two squares, swung between the two tables |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: KMR three-way proof, demographic parity's general incompatibility, COMPAS (chapter-6 film), thresholds |
| Mystery-framed opener | §2 | ✓ B10 — "Can we tune our way to both?" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 ("must B's false-alarm column go up, or down?") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not taught: the three-way proof"; BHTF = Exercise 6's 40% / 20% base rates |
| Length derived + tier reported | §5 | ✓ single-insight arc (one abstraction, three instances) at ~5:04 measured narration; the sections card said "standard" — scope was cut to one landed equation |

## Continuity
One `_Stage` state factory: the squares, fills, readouts, asks and marks, piles and ratio lines are rebuilt at the previous beat's end state; `to(cfg)` moves every object between the chapter's tables (transform, don't cut). B10's extras fade at the head of B11; B18 is the split-stage tangent; B19 rebuilds the HOOK's squares.

## TL;DR paradox check
B00 gives away the conclusion (hold one fair, the other breaks; 0.75/0.75 vs split errors). It does not show the pile, the widths-times-heights reading or the seesaw; the reveal is *seeing* B14–B16.

## Scope against the parallel chapter-6 film
"Both Audits Were Right" (chapter 6) uses the same impossibility on the AUDIT side with COMPAS. This film stays on the CHOICE side: no COMPAS, no ProPublica/Northpointe, only the chapter's two constructed tables and the choice they force.
