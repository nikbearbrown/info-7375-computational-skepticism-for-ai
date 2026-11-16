# TYPECHECK.md — GATE T

Reel: `claude-liam-saloni-job-fit-checker`  |  Checked: 2026-07-24T08:20  |  Overall: PASS  |  Beats checked: 29  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ASK | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| C01 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| C02 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | MANIM | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B04 | VOX | no video | SKIP | — |
| B05 | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B06 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | MANIM | min-size §8.1: min text-run height 76px >= floor 35px | PASS | — |
| C03 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | MANIM | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| B09 | VOX | no video | SKIP | — |
| B10 | VOX | no video | SKIP | — |
| B11 | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B12 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | MANIM | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |
| C04 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | MANIM | min-size §8.1: min text-run height 76px >= floor 35px | PASS | — |
| B15 | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 3 words in 'sparkLine') | PASS | — |
| B16 | VOX | no video | SKIP | — |
| C05 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | MANIM | min-size §8.1: min text-run height 105px >= floor 35px | PASS | — |
| B18 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 7 words in 'left.note') | PASS | — |
| C06 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 5 words in 'right.note') | PASS | — |
| V01 | REMOTION | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| H01 | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| O01 | CARD | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 25 | 0 |
| overflow §8.2 | 25 | 0 |
| contrast §8.3 | 25 | 0 |
| kerning §8.4 | 7 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
