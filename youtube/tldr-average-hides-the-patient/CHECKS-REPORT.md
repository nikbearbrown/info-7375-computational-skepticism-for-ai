# CHECKS-REPORT — tldr-average-hides-the-patient

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B16, B18) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

The film has 17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS), 10 LEARN beats (one section, B10–B19, pure Manim) and 3 closing beats. There is no section card, because this is a single-section film. By rule there is no pantry, no shopping list and no AI video.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy`: two cards on the TL;DR page, not the Claude.ai interface. The composer appears only at BHTF.

## TERMS (B03)
The film keeps TERMS, because the viewer arrives needing four prerequisites: calibration, calibration error (ECE), subgroup and confidence bin. The term the film EARNS, "subgroup calibration error" (ECE_g), is held back for B17.

## The one representation
Width is patients, height is error, area is how loudly a row speaks in the global. The five table rows are drawn first as equal columns, the way the table prints them. They then resize to their patient counts, so the rare-disease row becomes a sliver 0.7% of the width. The collision (B16) moves that sliver's area two ways. Poured over everyone, it becomes a hairline. Divided by its own 95, it becomes the tallest thing on the stage.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ global ECE 0.018 on 12,955 vs rare-disease 0.103 on 95 (the chapter's table) |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10 asks "both true — how?"; "subgroup calibration error" is not said until B17 |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (rows near the global), B12 (rows far above), B14, B15 all precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 holds calibration, ECE, subgroup and bin; ECE_g is earned in B16 → B17 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13, "the global is the average of the rows": 0.053, not 0.018 |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: width = patients, height = error, area = the row's voice in the global |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (pour and lift) |
| Every landed equation followed by a TANGENT | §4 | ✓ B17 lands ECE_g → B18 |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 opens on B10's one wide bar and the rare row |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ Deferred: MCE, base rates, the [verify] thresholds, conformal, temperature scaling, the halt threshold (boundary) |
| Mystery-framed opener | §2 | ✓ "How does the big one hide inside the small one?" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10 → B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 names the halt threshold and construct validity; BHTF is exercise A5 (5% can move the global, 0.7% cannot) |
| Length derived + tier reported | §5 | ✓ single-insight; measured narration 5:48 |

## Detours and what they got (density rule §6)
- Why the global sits BELOW the patient-weighted average (0.018 < 0.028): answered inline, one sentence and one line in the tangent (B18).
- MCE (0.176 on the rare row): cut.
- What threshold should halt a deployment: deferred to the BOUNDARY (the chapter's "Still puzzling").
- Construct validity (the sepsis model encoding clinician suspicion): deferred to the BOUNDARY, one sentence.

## TL;DR paradox check
B00 gives away the claim (0.018 overall, 0.103 on the 95, both true; the 95 cannot move the average). It does not show the widths, the pour, or the lift. The reveal is *seeing* B14–B16.
