# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-09-delegation-trust`  |  Checked: 2026-07-24T11:00  |  Overall: PASS  |  Beats checked: 36  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | BOOKEND | min-size §8.1: min text-run height 47px >= floor 35px | PASS | — |
| A1C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 5 words in 'left.note') | PASS | — |
| A1M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1V | VOX | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'right.note') | PASS | — |
| A2C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2K | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A2R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'left.note') | PASS | — |
| A2M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A3R | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 10 words in 'artifactLines… | PASS | — |
| A3V | VOX | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'sparkLine') | PASS | — |
| A3R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A3M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4R | REMOTION | no-wordy-card §8.5: ChipGrid: per-element check passed (max 6 words in 'chips[0]') | PASS | — |
| A4M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4V | VOX | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5C | CARD | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactHeadi… | PASS | — |
| A5M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5V1 | VOX | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 9 words in 'sparkLine') | PASS | — |
| A5V2 | VOX | no-wordy-card §8.5: DeckPattern: per-element check passed (max 9 words in 'right.note') | PASS | — |
| A5V3 | VOX | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A5R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 12 words in 'artifactLines… | PASS | — |
| A6M | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R | REMOTION | no-wordy-card §8.5: DeckPattern: per-element check passed (max 11 words in 'note') | PASS | — |
| A6K | ASK | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| A6M2 | MANIM | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6V | VOX | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| A6R2 | REMOTION | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| BVDT | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BHTF | CLOSING | min-size §8.1: no text-run blobs above noise threshold (smallest raw blob was noise/stroke… | PASS | — |
| BOUT | CLOSING | min-size §8.1: min text-run height 96px >= floor 35px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 30 | 0 |
| min-size §8.1 | 36 | 0 |
| overflow §8.2 | 36 | 0 |
| contrast §8.3 | 36 | 0 |
| kerning §8.4 | 10 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
