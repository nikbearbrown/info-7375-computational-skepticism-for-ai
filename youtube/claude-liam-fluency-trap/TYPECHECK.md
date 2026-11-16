# TYPECHECK.md — GATE T

Reel: `claude-liam-fluency-trap`  |  Checked: 2026-07-24T09:32  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B01 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | no video | SKIP | — |
| B03 | ? | no video | SKIP | — |
| B04 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | min-size §8.1: min text-run height 49px >= floor 35px | PASS | — |
| B07 | ? | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B08 | ? | no video | SKIP | — |
| B09 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B10 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B12 | ? | no-wordy-card §8.5: pull-quote (5 words ≤ 12) | PASS | — |
| B13 | ? | no video | SKIP | — |
| B14 | ? | min-size §8.1: min text-run height 49px >= floor 35px | PASS | — |
| B15 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B16 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B18 | ? | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B19 | ? | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B20 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | min-size §8.1: no text blobs detected (frame may be title-card or slate) | PASS | — |
| B22 | ? | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B23 | ? | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B24 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | no-wordy-card §8.5: FluencyChipGrid: per-element check passed (max 2 words in 'chips[3]') | PASS | — |
| B26 | ? | no video | SKIP | — |
| B27 | ? | no video | SKIP | — |
| B28 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | ? | min-size §8.1: min text-run height 65px >= floor 35px | PASS | — |
| B32 | ? | no-wordy-card §8.5: pull-quote (7 words ≤ 12) | PASS | — |
| B33 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B34 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B35 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 17 | 0 |
| min-size §8.1 | 30 | 0 |
| overflow §8.2 | 30 | 0 |
| contrast §8.3 | 30 | 0 |
| kerning §8.4 | 8 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
