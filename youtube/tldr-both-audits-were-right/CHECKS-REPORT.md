# CHECKS-REPORT — tldr-both-audits-were-right

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B13, B16) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy` — two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS
Four prerequisites the lesson uses without stopping: base rate, calibrated, false positive rate, false negative rate. The film's own answer — that calibration and equal error rates cannot coexist when base rates differ — is NOT in TERMS; it lands in B17 as the name for what B16 showed.

## The one representation
Forty people as dots (ink = reoffended, dim = did not) sorted into a calibrated score's HIGH and LOW boxes, read through two filters: Northpointe divides by the BOX, ProPublica divides by the OUTCOME. Same dots, two denominators.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ COMPAS — ProPublica (unequal false positives) vs Northpointe (calibrated), rebuilt as a constructed 20-per-group population at the chapter's base rates 30% / 50% |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: two opposite verdicts drawn onto the same forty dots — "which one is wrong?"; "calibration" is not used in the LEARN section before B12's check |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (group 1 sorts), B12 (group 2 sorts), B13 (recount), B16 (dots move) precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 = prerequisites; the impossibility is named in B17 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 — "one of them fudged it": ProPublica's count redone on the same dots comes out clean (2 of 14 vs 6 of 10); X beside "fudge" |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: "Same dots, two filters … the denominator is the box … the denominator is the outcome" |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (four dots walk high → low: the false-positive gap nearly closes while the high box climbs 60 → 82%) |
| Every landed equation followed by a TANGENT | §4, EQUATIONS.md | ✓ B17 lands v/(1−v) = p/(1−p)·t/f → B18 tangent (five zones on the split stage, two escapes; explain, never derive) |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 rebuilds B10's two headlines and forty dots (now coloured by outcome) and puts each audit's number under its headline |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: which criterion to hold (chapter 7, boundary line); re-arrest vs crime (one boundary line); the full proof and the three-way KMR version (chapter 7); demographic parity |
| Mystery-framed opener | §2 | ✓ B10 — "Same tool, same people, opposite verdicts. Somebody's arithmetic is wrong. Right?" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept ("Let's build a small version we can count", "Try it", "Is that just a bad repair, or is it forced?") |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19; B19's next_question empty (last beat) |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 ("Keep high meaning sixty percent in both groups. Can you also make the two false positive rates match? … Pick one.") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not taught: which to hold" + spoken re-arrest line; BHTF = a changed instance (readmission flag, base rates 20% / 40%) on the AUDIT side |
| Length derived + tier reported | §5 | ✓ tier: standard (card) — one section, one abstraction + tangent, 4 instances; measured audio 5:21 + holds (≈ 5.5 min) |

## Honesty notes
- The forty dots are constructed (caption "constructed · 20 per group" on stage B11–B16 and B19); the chapter supplies the base rates and the calibration claim, not counts.
- COMPAS is narrated at the chapter's level of detail (direction of the error pattern) — no rates are attributed to the real tool.
- B16 says "nearly closes" (2/10 vs 2/14), not "closes".
- Framing kept on the AUDIT side; chapter 7's CHOICE-side film ("Hold One Fair, Watch the Other Break") owns the pin-and-choose framing.

## TL;DR paradox check
B00 gives away the conclusion (base rates differ → not calibrated and equal errors at once; one audit did not cheat). It does not show the two filters, the recount or the moving dots — the reveal is *seeing* B13–B16.
