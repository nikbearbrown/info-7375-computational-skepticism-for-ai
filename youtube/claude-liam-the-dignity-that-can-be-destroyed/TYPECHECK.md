# TYPECHECK.md — GATE T

Reel: `claude-liam-the-dignity-that-can-be-destroyed`  |  Checked: 2026-09-08T02:40  |  Overall: PASS  |  Beats checked: 27  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | — | no video | SKIP | — |
| B01 | BOOKEND | — | no video | SKIP | — |
| B02 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | REMOTION | — | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B04 | REMOTION | — | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B05 | REMOTION | — | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B06 | REMOTION | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| BASK1 | BOOKEND | — | no video | SKIP | — |
| B07 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | — | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B09 | REMOTION | — | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B10 | REMOTION | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B11 | REMOTION | — | no-wordy-card §8.5: pull-quote (8 words ≤ 12) | PASS | — |
| B12 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | REMOTION | — | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B14 | REMOTION | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B15 | REMOTION | — | no-wordy-card §8.5: pull-quote (5 words ≤ 12) | PASS | — |
| B16 | REMOTION | — | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B17 | CARD | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| BASK2 | BOOKEND | — | no video | SKIP | — |
| B18 | REMOTION | — | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B19 | REMOTION | — | no-wordy-card §8.5: pull-quote (7 words ≤ 12) | PASS | — |
| B20 | REMOTION | — | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B21 | REMOTION | — | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B22 | BOOKEND | — | no video | SKIP | — |
| B23 | BOOKEND | — | no video | SKIP | — |
| B24 | BOOKEND | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 20 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| card-clip §8.13 | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
