# TYPECHECK.md — GATE T

Reel: `claude-liam-arguing-in-good-faith`  |  Checked: 2026-08-22T12:11  |  Overall: PASS  |  Beats checked: 16  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B05] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B09] narration recites the card (0.92) — discuss it, don't read it
> - §8.10 [B11] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B12] narration recites the card (1.00) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B07 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | REMOTION | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| BVDT | BOOKEND | light | min-size §8.1: min text-run height 48px >= floor 41px | PASS | — |
| BHTF | BOOKEND | light | min-size §8.1: min text-run height 53px >= floor 41px | PASS | — |
| BOUT | BOOKEND | dark | min-size §8.1: min text-run height 66px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 12 | 0 |
| min-size §8.1 | 16 | 0 |
| overflow §8.2 | 16 | 0 |
| contrast §8.3 | 16 | 0 |
| contrast-local §8.3b | 16 | 0 |
| bbox-overlap §8.6b | 16 | 0 |
| card-clip §8.13 | 16 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 7 | 4 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
