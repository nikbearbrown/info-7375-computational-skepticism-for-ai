# TYPECHECK.md — GATE T

Reel: `claude-liam-yuqing-design-sponsorship-triage`  |  Checked: 2026-07-24T08:53  |  Overall: PASS  |  Beats checked: 26  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ASK | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| C01 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| C02 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | MANIM | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B04 | VOX | no video | SKIP | — |
| B05 | VOX | no video | SKIP | — |
| B06 | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B07 | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 7 words in 'left.note') | PASS | — |
| C03 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | MANIM | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B10 | VOX | no video | SKIP | — |
| C04 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | min-size §8.1: min text-run height 43px >= floor 35px | PASS | — |
| C05 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 3 words in 'sparkLine') | PASS | — |
| B13 | VOX | no video | SKIP | — |
| C06 | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'left.note') | PASS | — |
| B15 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'right.note') | PASS | — |
| B16 | MANIM | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
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
| min-size §8.1 | 22 | 0 |
| overflow §8.2 | 22 | 0 |
| contrast §8.3 | 22 | 0 |
| kerning §8.4 | 5 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
