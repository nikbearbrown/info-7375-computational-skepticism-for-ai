# TYPECHECK.md — GATE T

Reel: `claude-liam-watermarks-remover`  |  Checked: 2026-08-14T23:51  |  Overall: PASS  |  Beats checked: 41  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B02] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B03] narration recites the card (0.93) — discuss it, don't read it
> - §8.10 [B09] narration recites the card (0.93) — discuss it, don't read it
> - §8.10 [B14] narration recites the card (0.91) — discuss it, don't read it
> - §8.10 [B19] narration recites the card (0.95) — discuss it, don't read it
> - §8.10 [B23] narration recites the card (0.90) — discuss it, don't read it
> - §8.10 [B24] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B25] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B26] narration recites the card (0.96) — discuss it, don't read it
> - §8.10 [B27] narration recites the card (0.96) — discuss it, don't read it
> - §8.10 [B30] narration recites the card (0.85) — discuss it, don't read it
> - §8.10 [B31] narration recites the card (0.83) — discuss it, don't read it
> - §8.10 [B34] narration recites the card (0.89) — discuss it, don't read it
> - §8.10 [B35] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| B01 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | BODY | light | min-size §8.1: min text-run height 111px >= floor 35px | PASS | — |
| B08 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | BODY | light | min-size §8.1: min text-run height 78px >= floor 35px | PASS | — |
| B13 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | BODY | light | min-size §8.1: min text-run height 81px >= floor 35px | PASS | — |
| B18 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B27 | BODY | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B28 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B31 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B32 | BODY | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | BODY | light | min-size §8.1: min text-run height 125px >= floor 35px | PASS | — |
| B34 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | BODY | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| BSRC | BODY | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 210px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 32 | 0 |
| min-size §8.1 | 40 | 0 |
| overflow §8.2 | 40 | 0 |
| contrast §8.3 | 40 | 0 |
| contrast-local §8.3b | 40 | 0 |
| bbox-overlap §8.6b | 40 | 0 |
| kerning §8.4 | 4 | 0 |
| redundancy §8.10 (advisory) | 23 | 14 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
