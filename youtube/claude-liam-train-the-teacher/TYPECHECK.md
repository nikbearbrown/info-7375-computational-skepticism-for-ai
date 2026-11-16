# TYPECHECK.md — GATE T

Reel: `claude-liam-train-the-teacher`  |  Checked: 2026-09-08T02:54  |  Overall: PASS  |  Beats checked: 35  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BOOKEND | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B02 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B03 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B04 | REMOTION | light | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: pull-quote (8 words ≤ 12) | PASS | — |
| B06 | REMOTION | light | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B07 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B09 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B10 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B11 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B12 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B13 | REMOTION | light | no-wordy-card §8.5: pull-quote (8 words ≤ 12) | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B15 | REMOTION | light | no-wordy-card §8.5: pull-quote (10 words ≤ 12) | PASS | — |
| B16 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B17 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B18 | REMOTION | light | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B19 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B20 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B21 | REMOTION | light | no-wordy-card §8.5: pull-quote (12 words ≤ 12) | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: pull-quote (6 words ≤ 12) | PASS | — |
| B23 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B24 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B25 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B26 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B27 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B28 | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B29 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B30 | REMOTION | light | no-wordy-card §8.5: pull-quote (11 words ≤ 12) | PASS | — |
| B31 | REMOTION | light | no-wordy-card §8.5: pull-quote (9 words ≤ 12) | PASS | — |
| B32 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| B33 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B34 | BOOKEND | light | min-size §8.1: min text-run height 44px >= floor 41px (individual-char fallback at 2×) | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 30 | 0 |
| min-size §8.1 | 35 | 0 |
| overflow §8.2 | 35 | 0 |
| contrast §8.3 | 35 | 0 |
| contrast-local §8.3b | 35 | 0 |
| bbox-overlap §8.6b | 35 | 0 |
| card-clip §8.13 | 35 | 0 |
| kerning §8.4 | 0 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
