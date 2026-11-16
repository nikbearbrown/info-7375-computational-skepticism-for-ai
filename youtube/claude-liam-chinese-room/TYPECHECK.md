# TYPECHECK.md — GATE T

Reel: `claude-liam-chinese-room`  |  Checked: 2026-07-27T21:40  |  Overall: PASS  |  Beats checked: 34  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | REMOTION | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| A1 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A2 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A3 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A4 | DOODLE | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A5 | DOODLE | min-size §8.1: min text-run height 221px >= floor 35px | PASS | — |
| A6 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A7 | VOX | no video | SKIP | — |
| A8 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A9 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A10 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A11 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A12 | DOODLE | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A13 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A14 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A15 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A16 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A17 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A18 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A19 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A20 | MANIM | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A21 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A22 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A23 | CARD | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A24 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A25 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A26 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A27 | DOODLE | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A28 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| A29 | MANIM | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| BVDT | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | REMOTION | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| C3 | REMOTION | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 33 | 0 |
| overflow §8.2 | 33 | 0 |
| contrast §8.3 | 33 | 0 |
| kerning §8.4 | 28 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
