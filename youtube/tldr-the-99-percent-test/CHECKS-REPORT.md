# CHECKS-REPORT — tldr-the-99-percent-test

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    13 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B16, B18) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video, by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy`: two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS (B03), kept
The LEARN section uses "base rate", "false positive" and the "given" bar without stopping. All three are prerequisites; the film EARNS Bayes' theorem (posterior ∝ prior × likelihood), which is not in TERMS.

## The one representation
The population, counted: 10,000 people as a 100×100 grid of squares, so the base rate is a visible count and "a positive" is a pile you can gather (Figure 2.5, rebuilt as Manim).

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ base rate 1/10,000, a 99% test, one positive → 1 true + ≈ 100 false among 10,000 → ≈ 1% |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: one patient, one positive, an empty rail with '?' ("Bayes" not said until B17) |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (100 sick), B12 (100 healthy), B16 (10,000) precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B17 names the pile Bayes' theorem after the viewer has built it |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13: "99% accurate, positive, so 99%" — knob to 99%, the engineers' band and the 1978 study, walked to the flipped bar |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: count the population, one square per person |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (light the positives, gather the pile, knob falls to ≈ 1%) |
| Every landed equation followed by a TANGENT | §4 | ✓ B17 lands Bayes → B18. The count 1/(1 + 100) is arithmetic on screen, not a landed equation |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 returns the patient dot, the 'positive' tag and the rail |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: base-rate-by-domain table, the fleet/total-probability example (S3), sensitivity vs specificity as two numbers (one caption only) |
| Mystery-framed opener | §2 | ✓ B10: "how likely is it that this patient is sick?" with the answer rail empty |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10 → B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 (the chapter's own "Pick a number. Lock it in.") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not found here: the coin-flip point"; BHTF = Glimmer 2.3 (vary the base rate, predict where the positive becomes a coin flip) |
| Length derived + tier reported | §5 | ✓ single-insight; ≈ 5 min estimated before audio lock |

## Density decisions (§6)
- The chapter's term-table posterior (≈ 0.0099) vs prose (≈ 0.0098): answered inline in B18 (one sentence) — it is a viewer question the tangent raises.
- Sepsis model: one sentence + one dim line in B19 as the scale shift; product name kept off screen.
- Domain base-rate table: cut (ranges without sources).

## TL;DR paradox check
B00 gives away the conclusion (≈ 1%, about 100 false vs 1 true, the base-rate trap). It does not show the pile gathering or the formula's numerator; the reveal is *seeing* B16.
