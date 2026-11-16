# CHECKS-REPORT — tldr-robust-against-what

Written before the first compile, per the ai-explainer PROOF GATE and the tldr Gate-1 audit.

    14 SHOW / 0 justified-HOLD / 1 CARD (B03 TERMS) / 0 PUNT-flagged

    Teaching arc: FRAMEWORK ✓ (B14 SHIFT) | WORKED EXAMPLE ✓ (B11, B12, B16) | FALSIFIABILITY ✓ (B15 predict → B16)
                  SCAFFOLDED TASK ✓ (BHTF) | BOOKENDS ✓ (B00 · BVDT · BHTF · BOUT) | NO-SOURCE-NO-VERDICT ✓

17 beats: 4 opening bookends (WHAT · WHY · QUESTION · TERMS) · 10 LEARN (one section, B10–B19, pure Manim) · 3 closing. No section card (single-section film). Zero pantry, zero shopping list, zero AI video — by rule.

## Cold open template
B00 `ClaudeTldrWhat` + B01 `ClaudeTldrWhy` — two cards on the TL;DR page (not the Claude.ai interface). The composer appears only at BHTF.

## TERMS
Four prerequisites the lesson uses without stopping: clean accuracy, perturbation budget ε, transfer attack, distribution shift. The film's own answer — "a profile", and the three-section disclosure — is NOT defined in TERMS; it lands in B18.

## The one representation
The disclosure table filling one row at a time: a clean bar fixed at 94 in every row while each row's robust bar grows to its own height — rows as separate axes (Figure 4.5), then Sections 2 and 3 as blanks the word never fills.

## Gate-1 audit (tldr `reference/pedagogy.md` §13)

| Check | Ref | Pass? |
|---|---|---|
| Key case named | §1.1 | ✓ the chapter's disclosure template, Section 1: clean 94 everywhere; robust 71 (white-box, ε = 0.03) · 58 (transfer) · 87 (natural shift) — template values, captioned illustrative |
| Section opens unsolved; zero vocabulary before the felt problem | §1.2, §2 | ✓ B10: "94% accurate, and robust" — the number has a bar, the word has none; "profile" is not said in the LEARN section until B14 |
| ≥ 2 moving instances before each abstraction | §1.3 | ✓ B11, B12 (rows fill), B15/B16 (row three), B17 (budget moves) precede B18 |
| Every definition arrives as an endpoint; TERMS holds prerequisites only | §1.4 | ✓ B03 = prerequisites; the three-section structure is named in B18 |
| Natural wrong turn shown (NAIVE) | §3, §4 | ✓ B13 — fold two rows back into one word; the numbers vanish on screen |
| One representation named in one sentence (SHIFT) | §10 | ✓ B14: "each row is its own axis — not a score, a profile" |
| Exactly one TRANSFORM per section | §4 | ✓ B16 (row three lands past both guides; the word morphs into two blank fields) |
| Every landed equation followed by a TANGENT | §4 | ✓ n/a — the card lands no equation (sections file: "equations: none"); ε = 0.03 is a table value, not a landed equation |
| PAYOFF returns the HOOK's persistent object | §4 | ✓ B19 brings back the slide's sentence and the 94 bar (row one's clean bar) |
| Nothing "for completeness"; deferrals logged | §1.5, §6 | ✓ deferred: the toolkit table, certified radii (S5), scaling ceiling (S6), NIST citation |
| Mystery-framed opener | §2 | ✓ B10 — "robust — against what?" |
| Discovery voice; no "it can be shown that" | §3 | ✓ swept |
| Every LEARN beat has a `learn` block; next_question chains | §9 | ✓ B10→B19 |
| One `predict: true` beat before the TRANSFORM | §12 | ✓ B15 ("where does row three land — and could the attack rows have told you?") |
| Boundary: not-taught + transfer exercise → BHTF | §7 | ✓ B19 caption "not taught: what each defense costs"; BHTF = exercise 6 (facial recognition, five questions) |
| Length derived + tier reported | §5 | ✓ single-insight; ~6.5 min estimated before audio lock (the BHTF prompt is long — exercise 6 read in full) |

## Honesty notes
- Template values: "template" spoken in B00, B12, B16; dim caption "template values — illustrative" on the stage B11–B19.
- The transfer row has no ε in the chapter; the film never ranks white-box against transfer.
- B17's ε = 0.06 is a hypothetical with no number shown — "?" is the honest value.

## TL;DR paradox check
B00 gives away the conclusion (a profile, not a number; three robust numbers under one word). It does not show the fold, the unfold, the row-three reveal or the blanks — the reveal is *seeing* B13–B16.
