# TYPECHECK.md — GATE T

Reel: `claude-liam-two-models-twice-the-price`  |  Checked: 2026-07-29T01:21  |  Overall: PASS  |  Beats checked: 41  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B32 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| B37 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | BOOKEND | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | BOOKEND | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 37 | 0 |
| min-size §8.1 | 41 | 0 |
| overflow §8.2 | 41 | 0 |
| contrast §8.3 | 41 | 0 |
| kerning §8.4 | 20 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
