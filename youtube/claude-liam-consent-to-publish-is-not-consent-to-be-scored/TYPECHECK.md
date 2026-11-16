# TYPECHECK.md — GATE T

Reel: `claude-liam-consent-to-publish-is-not-consent-to-be-scored`  |  Checked: 2026-08-17T04:37  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B01 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | VOX | — | no video | SKIP | — |
| B04 | VOX | — | no video | SKIP | — |
| B05 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 9 words in 'right.note') | PASS | — |
| B06 | MANIM | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B07 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | VOX | — | no video | SKIP | — |
| B09 | MANIM | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | MANIM | light | min-size §8.1: min text-run height 38px >= floor 35px | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | MANIM | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 38px >= floor 35px | PASS | — |
| B16 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'sparkLine') | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | MANIM | light | min-size §8.1: min text-run height 39px >= floor 35px | PASS | — |
| B19 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | MANIM | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B21 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | VOX | — | no video | SKIP | — |
| B23 | VOX | — | no video | SKIP | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 123px >= floor 35px | PASS | — |
| B25 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'note') | PASS | — |
| B26 | VOX | — | no video | SKIP | — |
| B27 | MANIM | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B28 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | VOX | — | no video | SKIP | — |
| B30 | REMOTION | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | MANIM | light | min-size §8.1: min text-run height 44px >= floor 35px | PASS | — |
| B32 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'note') | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 59px >= floor 35px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 15 | 0 |
| min-size §8.1 | 29 | 0 |
| overflow §8.2 | 29 | 0 |
| contrast §8.3 | 29 | 0 |
| contrast-local §8.3b | 29 | 0 |
| bbox-overlap §8.6b | 29 | 0 |
| card-clip §8.13 | 29 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
