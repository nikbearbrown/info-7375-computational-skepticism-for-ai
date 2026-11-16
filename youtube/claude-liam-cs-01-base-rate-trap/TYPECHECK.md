# TYPECHECK.md — GATE T

Reel: `claude-liam-cs-01-base-rate-trap`  |  Checked: 2026-07-27T22:58  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| B02 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B05 | ? | min-size §8.1: min text-run height 60px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | min-size §8.1: min text-run height 57px >= floor 35px | PASS | — |
| B08 | ? | min-size §8.1: min text-run height 70px >= floor 35px | PASS | — |
| B09 | ? | min-size §8.1: min text-run height 53px >= floor 35px | PASS | — |
| B10 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B11 | ? | min-size §8.1: min text-run height 53px >= floor 35px | PASS | — |
| B12 | ? | min-size §8.1: min text-run height 69px >= floor 35px | PASS | — |
| BVDT | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | ? | min-size §8.1: min text-run height 35px >= floor 35px | PASS | — |
| BOUT | ? | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 2 | 0 |
| min-size §8.1 | 15 | 0 |
| overflow §8.2 | 15 | 0 |
| contrast §8.3 | 15 | 0 |
| kerning §8.4 | 9 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
