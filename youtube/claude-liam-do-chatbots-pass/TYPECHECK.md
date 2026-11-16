# TYPECHECK.md — GATE T

Reel: `claude-liam-do-chatbots-pass`  |  Checked: 2026-07-24T08:59  |  Overall: PASS  |  Beats checked: 33  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | REMOTION | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| A1 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A2 | VOX | no video | SKIP | — |
| A3 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A4 | DOODLE | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A5 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A6 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A7 | VOX | no video | SKIP | — |
| A8 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A9 | VOX | no video | SKIP | — |
| A10 | VOX | no video | SKIP | — |
| A11 | MANIM | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| A12 | DOODLE | min-size §8.1: min text-run height 50px >= floor 35px | PASS | — |
| A13 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A14 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A15 | DOODLE | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A16 | VOX | no video | SKIP | — |
| A17 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A18 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A19 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A20 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A21 | VOX | no video | SKIP | — |
| A22 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A23 | DOODLE | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A24 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A25 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A26 | MANIM | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A27 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A28 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A29 | VOX | no video | SKIP | — |
| C1 | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| C2 | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| C3 | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 26 | 0 |
| overflow §8.2 | 26 | 0 |
| contrast §8.3 | 26 | 0 |
| kerning §8.4 | 22 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
