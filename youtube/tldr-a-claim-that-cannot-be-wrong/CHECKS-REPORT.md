# CHECKS-REPORT — tldr-a-claim-that-cannot-be-wrong

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    15 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B17) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

**The one representation (SHIFT, one sentence):** a claim is drawn as the region of outcomes it forbids on an outcome axis — "robust" shades nothing, "error < 2% over 30 days" carves a region.

**TERMS kept (not skipped):** held-out test set, recall, precision, out-of-distribution — all four are used by the LEARN section without stopping (B11, B12, B14, B16). "Falsifiable" — the earned term — is NOT in TERMS; it arrives in B18.

**Equations:** none (thresholds, not formulas) → no TANGENT beat; the tenth LEARN slot is a post-shift INSTANCE (B17, stage 5 "develop the insight": the four table rows).

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy` — two cards on the TL;DR page. The composer appears only at BHTF.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ the chapter's table ("The system is robust." → < 2% OOD error / 30 days …) + the sepsis model's five favorable checks vs the Michigan external validation (27,697 patients; caught ≈ 1 in 3) |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: the tile survives a terrible result — "what would non-robust look like?" ("falsifiable" not said until B18) |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (region carved on the error axis), B12 (region slides to the other side), B15/B16, B17 precede B18 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ TERMS = four prerequisites; "falsifiable" earned in B18 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 — count the favorable checks; the bar never reaches certain |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: "that is the claim, drawn: the outcomes it rules out" |
| Exactly one TRANSFORM per section | §4 | ✓ B16 — the black swan drops into the region; the bar falls to zero |
| Every landed equation followed by a TANGENT | §4 | ✓ n/a — no equations in the chapter or the film |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 opens on the B10 tile, axis and three dots |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: 18% alert share, PSI's definition, the patient composite, COMPAS/Knight/Zillow/GFT (other sections) |
| Mystery-framed opener | §2 | ✓ B10 |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 "not taught here: the line first"; BHTF = Warm-Up 2 (94% accuracy) |
| Length derived + tier reported | §5 | ✓ card tier "standard" (table + sepsis); estimate ~5 min before audio lock |

## TL;DR paradox check
B00 gives away the conclusion (name what would make it false; claims drawn as what they forbid; unrefuted looks like passed). It does not show the region, the swan stack or the drop — the reveal is *seeing* B16.

## Simplifications marked on screen (once each)
"constructed observations" (B10) · "confidence: schematic, not measured" (B13) · "threshold: the table's row, applied" (B14) · "PSI is named here, not taught" (B17).
