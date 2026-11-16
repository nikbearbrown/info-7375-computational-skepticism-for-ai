# TYPECHECK.md — GATE T

Reel: `claude-liam-lm-watermarking-walkthrough`  |  Checked: 2026-08-12T18:03  |  Overall: PASS  |  Beats checked: 42  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B01] narration recites the card (0.81) — discuss it, don't read it
> - §8.10 [B04] narration recites the card (0.85) — discuss it, don't read it
> - §8.10 [B29] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B33] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B35] narration recites the card (0.82) — discuss it, don't read it
> - §8.10 [B37] narration recites the card (0.88) — discuss it, don't read it
> - §8.10 [B38] narration recites the card (0.80) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B01 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B09 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B10 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B20 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B23 | ? | light | min-size §8.1: min text-run height 50px >= floor 35px | PASS | — |
| B24 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B25 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B27 | ? | light | min-size §8.1: min text-run height 37px >= floor 35px | PASS | — |
| B28 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B31 | ? | light | min-size §8.1: min text-run height 40px >= floor 35px | PASS | — |
| B32 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B33 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B35 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B37 | ? | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B38 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B39 | ? | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B40 | ? | light | min-size §8.1: min text-run height 36px >= floor 35px | PASS | — |
| B41 | ? | light | min-size §8.1: min text-run height 64px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 31 | 0 |
| min-size §8.1 | 42 | 0 |
| overflow §8.2 | 42 | 0 |
| contrast §8.3 | 42 | 0 |
| contrast-local §8.3b | 42 | 0 |
| bbox-overlap §8.6b | 42 | 0 |
| kerning §8.4 | 4 | 0 |
| redundancy §8.10 (advisory) | 20 | 7 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
