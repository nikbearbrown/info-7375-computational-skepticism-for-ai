# TYPECHECK.md — GATE T

Reel: `claude-liam-cs-07-turkeys-model`  |  Checked: 2026-07-24T02:36  |  Overall: PASS  |  Beats checked: 15  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

> **§8.6 GOLDEN STRINGS:**

> - B03: headline 75 chars — adversarial overflow risk (golden LONGEST test fails at this length)
> - B06: headline 76 chars — adversarial overflow risk (golden LONGEST test fails at this length)

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B01 | ? | no video | SKIP | — |
| B02 | ? | no video | SKIP | — |
| B03 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | no video | SKIP | — |
| B05 | ? | no video | SKIP | — |
| B06 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | no video | SKIP | — |
| B08 | ? | no video | SKIP | — |
| B09 | ? | no video | SKIP | — |
| B10 | ? | no video | SKIP | — |
| B11 | ? | no video | SKIP | — |
| B12 | ? | no video | SKIP | — |
| B13 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | no-wordy-card §8.5: no prose payload found | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 5 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
