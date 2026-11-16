# TYPECHECK.md — GATE T

Reel: `claude-liam-lm-watermarking-walkthrough-short`  |  Checked: 2026-08-12T18:28  |  Overall: PASS  |  Beats checked: 24  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B29] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B33] narration recites the card (1.00) — discuss it, don't read it
> - §8.10 [B37] narration recites the card (0.88) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | ? | — | no video | SKIP | — |
| B02 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B05 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | ? | — | no video | SKIP | — |
| B10 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B13 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B14 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B16 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B18 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B21 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B22 | ? | — | no video | SKIP | — |
| B25 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B26 | ? | — | no video | SKIP | — |
| B28 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B30 | ? | — | no video | SKIP | — |
| B33 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B34 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B36 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B37 | ? | — | no-wordy-card §8.5: no prose payload found | PASS | — |
| B41 | ? | — | no video | SKIP | — |
| END | ? | — | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 17 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| contrast-local §8.3b | 0 | 0 |
| bbox-overlap §8.6b | 0 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 10 | 3 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
