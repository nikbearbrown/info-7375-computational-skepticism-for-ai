# TYPECHECK.md — GATE T

Reel: `claude-liam-dashboard-that-lied`  |  Checked: 2026-08-12T09:45  |  Overall: PASS  |  Beats checked: 37  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | BOOKEND | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | — | no video | SKIP | — |
| B03 | ? | light | min-size §8.1: min text-run height 49px >= floor 35px | PASS | — |
| B04 | ? | light | min-size §8.1: min text-run height 41px >= floor 35px | PASS | — |
| B05 | ? | — | no video | SKIP | — |
| B06 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | — | no video | SKIP | — |
| B08 | ? | — | no video | SKIP | — |
| B09 | ? | light | no-wordy-card §8.5: pull-quote (7 words ≤ 12) | PASS | — |
| B10 | ? | light | min-size §8.1: min text-run height 48px >= floor 35px | PASS | — |
| B11 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | light | min-size §8.1: min text-run height 49px >= floor 35px | PASS | — |
| B13 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B14 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B15 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B16 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B18 | ? | light | no-wordy-card §8.5: pull-quote (7 words ≤ 12) | PASS | — |
| B19 | ? | — | no video | SKIP | — |
| B20 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B23 | ? | — | no video | SKIP | — |
| B24 | ? | — | no video | SKIP | — |
| B25 | ? | light | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B26 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | ? | light | no-wordy-card §8.5: pull-quote (7 words ≤ 12) | PASS | — |
| B28 | ? | light | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B28B | remotion | light | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B29 | ? | light | no-wordy-card §8.5: pull-quote (4 words ≤ 12) | PASS | — |
| B30 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B31 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B32 | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BVDT | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | light | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| BOUT | ? | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 14 | 0 |
| min-size §8.1 | 30 | 0 |
| overflow §8.2 | 30 | 0 |
| contrast §8.3 | 30 | 0 |
| contrast-local §8.3b | 30 | 0 |
| bbox-overlap §8.6b | 30 | 0 |
| kerning §8.4 | 8 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
