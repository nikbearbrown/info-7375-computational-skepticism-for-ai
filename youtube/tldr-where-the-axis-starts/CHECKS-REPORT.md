# CHECKS-REPORT — tldr-where-the-axis-starts

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B18) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy` — two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS
Kept (3 rows): axis floor, accuracy, percentage point — prerequisites the LEARN section uses without stopping. "Truncated axis" and the visual-ratio rule are the film's answer and are earned in B17, not defined up front.

## The one representation
Every bar is a shared part below the floor (thrown away) plus a sliver above it (stretched to fill the frame): a truncated axis is a zoom on the slivers, and the floor decides where the slivers begin (B14). The persistent object is the colleague's two-bar chart, driven by one floor value (`_Chart` state factory); B12 and B16 move only that value.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ Exercise 1 (constructed): axis 91–96, A 92.1%, B 94.3%; bars 1.1 / 3.3 → ×3.0; zero floor ×1.02 |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: every label is correct, the bar is three times as tall — "is B three times better?" ("truncated axis" is not said until B17) |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11 (braces from the floor), B12 (floor slide 91 → 0), B15/B16 precede B17 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ see TERMS above |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 — "every number on the chart is true, so the chart is honest", walked through three passing checks to the unprinted ×3 |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: "a truncated axis is a zoom on the slivers; the floor decides where the slivers begin" |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (the floor sweep 91 → 89.9 → 80 → 0 → 92) |
| Every landed equation followed by a TANGENT | §4 | ✓ B17 lands looks = (B − floor)/(A − floor) → B18 |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 opens on the B10 chart at floor 91, ×3.0 |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: the other catalog items, lie factor, a drawn stock-price chart (no chapter data), mismatched panels (→ BHTF) |
| Mystery-framed opener | §2 | ✓ B10 — "Nothing on this chart is false. Something on it is still lying to you." |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 ("where must the floor go for ×2 — up or down, and how far?") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not taught here: mismatched panels"; BHTF = Exercise 3 (70–100 / 85–100 / 60–100) |
| Length derived + tier reported | §5 | ✓ single-insight; ~5 min estimated before audio lock (1 HOOK + 3 INSTANCE + NAIVE + SHIFT + TRANSFORM + ABSTRACTION + TANGENT + PAYOFF) |

## TL;DR paradox check
B00 gives away the conclusion (the floor sets the ratio; ×3 then nearly equal). It does not show the cut at 91, the ×2 answer at 89.9, or the ×23 blow-up — the reveal is *seeing* B14 and B16.
