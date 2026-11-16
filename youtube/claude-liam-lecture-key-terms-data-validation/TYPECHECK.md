# TYPECHECK.md — GATE T

Reel: `claude-liam-lecture-key-terms-data-validation`  |  Checked: 2026-11-12T07:05  |  Overall: PASS  |  Beats checked: 55  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| BOPEN | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BIDEA | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BDEFS | bookend | light | min-size §8.1: min text-run height 103px >= floor 41px | PASS | — |
| B0101 | screen | — | no video | SKIP | — |
| B0102 | screen | — | no video | SKIP | — |
| B0103 | screen | — | no video | SKIP | — |
| B0104 | screen | — | no video | SKIP | — |
| B0201 | screen | — | no video | SKIP | — |
| B0202 | screen | — | no video | SKIP | — |
| B0203 | screen | — | no video | SKIP | — |
| B0301 | screen | — | no video | SKIP | — |
| B0302 | screen | — | no video | SKIP | — |
| B0401 | screen | — | no video | SKIP | — |
| B0402 | screen | — | no video | SKIP | — |
| B0403 | screen | — | no video | SKIP | — |
| B0404 | screen | — | no video | SKIP | — |
| B0501 | screen | — | no video | SKIP | — |
| B0502 | screen | — | no video | SKIP | — |
| B0503 | screen | — | no video | SKIP | — |
| B0504 | screen | — | no video | SKIP | — |
| B0601 | screen | — | no video | SKIP | — |
| B0602 | screen | — | no video | SKIP | — |
| B0603 | screen | — | no video | SKIP | — |
| B0701 | screen | — | no video | SKIP | — |
| B0702 | screen | — | no video | SKIP | — |
| B0703 | screen | — | no video | SKIP | — |
| B0801 | screen | — | no video | SKIP | — |
| B0802 | screen | — | no video | SKIP | — |
| B0803 | screen | — | no video | SKIP | — |
| B0804 | screen | — | no video | SKIP | — |
| B0901 | screen | — | no video | SKIP | — |
| B0902 | screen | — | no video | SKIP | — |
| B0903 | screen | — | no video | SKIP | — |
| B1001 | screen | — | no video | SKIP | — |
| B1002 | screen | — | no video | SKIP | — |
| B1003 | screen | — | no video | SKIP | — |
| B1004 | screen | — | no video | SKIP | — |
| B1101 | screen | — | no video | SKIP | — |
| B1102 | screen | — | no video | SKIP | — |
| B1103 | screen | — | no video | SKIP | — |
| B1104 | screen | — | no video | SKIP | — |
| B1201 | screen | — | no video | SKIP | — |
| B1202 | screen | — | no video | SKIP | — |
| B1203 | screen | — | no video | SKIP | — |
| B1204 | screen | — | no video | SKIP | — |
| B1205 | screen | — | no video | SKIP | — |
| B1301 | screen | — | no video | SKIP | — |
| B1302 | screen | — | no video | SKIP | — |
| B1303 | screen | — | no video | SKIP | — |
| B1304 | screen | — | no video | SKIP | — |
| B1305 | screen | — | no video | SKIP | — |
| B1306 | screen | — | no video | SKIP | — |
| BVDT | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BHTF | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |
| BOUT | bookend | light | min-size §8.1: min text-run height 41px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 0 | 0 |
| min-size §8.1 | 6 | 0 |
| overflow §8.2 | 6 | 0 |
| contrast §8.3 | 6 | 0 |
| contrast-local §8.3b | 6 | 0 |
| bbox-overlap §8.6b | 6 | 0 |
| card-clip §8.13 | 6 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 0 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
