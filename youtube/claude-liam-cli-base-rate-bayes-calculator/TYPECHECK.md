# TYPECHECK.md — GATE T

Reel: `claude-liam-cli-base-rate-bayes-calculator`  |  Checked: 2026-07-24T03:34  |  Overall: PASS  |  Beats checked: 12  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | min-size §8.1: min text-run height 46px >= floor 35px | PASS | — |
| B01 | ? | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| B02 | ? | min-size §8.1: min text-run height 53px >= floor 35px | PASS | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no video | SKIP | — |
| B05 | ? | min-size §8.1: min text-run height 53px >= floor 35px | PASS | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | ? | no video | SKIP | — |
| BHTF | ? | no video | SKIP | — |
| B09 | ? | min-size §8.1: min text-run height 103px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 9 | 0 |
| overflow §8.2 | 9 | 0 |
| contrast §8.3 | 9 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
