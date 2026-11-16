# CHECKS-REPORT — tldr-missing-is-not-one-thing

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B13) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

## The one representation
**Sort the rows of the missingness matrix by a column and watch whether the blanks line up** — a block means the blanks depend on that column. Scattered under every recorded column + a block under the never-recorded value = MNAR.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ income 18% blank (9 of 50, constructed): table A = under-25s skipped (MAR, ex. 8), table B = top earners left it blank (MNAR) |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: same count, same look — "which fill is safe?" (MCAR/MAR/MNAR not said until B17) |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (two random wipes), B12, B13, B14, B15, B16 precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 = missingness matrix / impute / subgroup; the taxonomy is earned in B17 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 — the age-group fill: works for A, fails silently for B |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14 (above) |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (the sort by the never-recorded value) |
| Every landed equation followed by a TANGENT | §4 | ✓ n/a — no equation lands (the taxonomy is stated in words, per the sections card); B18 is a post-shift INSTANCE (seven-stage template stage 5), not a tangent |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 rebuilds the HOOK's two matrices in file order and sorts them |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: choosing an imputation method (multiple imputation etc.), join-dropped rows (S1), co-missing columns, sensitivity analysis |
| Mystery-framed opener | §2 | ✓ "One fill lands on the truth. The other lands somewhere else. Which is which?" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept ("Here's the move", "watch where the blanks go", "commit") |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption; BHTF = pain_score clustered in evening appointments: predict, tell a MAR and an MNAR story, name the question no plot answers |
| Length derived + tier reported | §5 | ✓ single-insight; ~6:40 estimated from word counts, 4:42 measured after audio lock (BHTF is the long beat) |

## Detours (density rule §6)
- Why random loss still costs precision (smaller n) → one clause in B11 ("shrinks your sample"), cut otherwise.
- missingno the library → cut (tooling-aging note; the film names the representation).
- Co-missing columns (the matrix's other use) → cut.
- Rubin 1976 vs Little & Rubin 1987 label history → deferred to FACTCHECK; on screen "after Rubin (1976)".

## TL;DR paradox check
B00 gives away the conclusion (the reason decides; some blanks line up, some never will; the worst kind looks harmless). It does not show the sort, the hidden column, or the block at the top — the reveal is *seeing* B16.
