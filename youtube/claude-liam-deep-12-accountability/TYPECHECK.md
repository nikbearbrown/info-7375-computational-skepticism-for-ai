# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-12-accountability`  |  Checked: 2026-07-24T02:38  |  Overall: PASS  |  Beats checked: 39  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | no video | SKIP | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1K | ASK | no video | SKIP | — |
| A1R | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 10 words in 'artifactHeadi… | PASS | — |
| A1M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 7 words in 'sparkLine') | PASS | — |
| A2M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A3C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 9 words in 'note') | PASS | — |
| A3M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'sparkLine') | PASS | — |
| A4M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R2 | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'right.note') | PASS | — |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A5M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A5M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'note') | PASS | — |
| A6V1 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V2 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V3 | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7R | REMOTION | no-wordy-card §8.5: no prose payload found | PASS | — |
| A7R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 10 words in 'artifactLines… | PASS | — |
| BVDT | CLOSING | no video | SKIP | — |
| BHTF | CLOSING | no video | SKIP | — |
| BOUT | CLOSING | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 34 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
