# TYPECHECK.md — GATE T

Reel: `claude-liam-deep-test-you-did-not-design`  |  Checked: 2026-09-03T13:09  |  Overall: PASS  |  Beats checked: 40  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | BOOKEND | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | BOOKEND | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| A1C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A1R | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'left.note') | PASS | — |
| A1K | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| A1M | MANIM | light | min-size §8.1: min text-run height 56px >= floor 41px | PASS | — |
| A1V | VOX | — | no video | SKIP | — |
| A1M2 | MANIM | light | min-size §8.1: min text-run height 59px >= floor 41px | PASS | — |
| A2C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A2R | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 5 words in 'sparkLine') | PASS | — |
| A2M | MANIM | light | min-size §8.1: min text-run height 88px >= floor 41px | PASS | — |
| A2R2 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'right.note') | PASS | — |
| A2V1 | VOX | — | no video | SKIP | — |
| A2V2 | VOX | — | no video | SKIP | — |
| A2M2 | MANIM | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| A2M3 | MANIM | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| A3C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A3V1 | VOX | — | no video | SKIP | — |
| A3R | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'left.note') | PASS | — |
| A3V2 | VOX | — | no video | SKIP | — |
| A3R2 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 8 words in 'left.note') | PASS | — |
| A3M | MANIM | light | min-size §8.1: min text-run height 44px >= floor 41px | PASS | — |
| A4C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A4M | MANIM | light | min-size §8.1: min text-run height 46px >= floor 41px | PASS | — |
| A4V | VOX | — | no video | SKIP | — |
| A4R | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 11 words in 'chips[0]') | PASS | — |
| A4R2 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A5R | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 10 words in 'right.note') | PASS | — |
| A5V | VOX | — | no video | SKIP | — |
| A5M | MANIM | light | min-size §8.1: min text-run height 47px >= floor 41px | PASS | — |
| A5R2 | REMOTION | light | no-wordy-card §8.5: DeckPattern: per-element check passed (max 12 words in 'title') | PASS | — |
| A6C | CARD | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6K | ASK | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| A6M | MANIM | light | min-size §8.1: min text-run height 41px >= floor 41px | PASS | — |
| A6R | REMOTION | light | no-wordy-card §8.5: ChipGrid: per-element check passed (max 8 words in 'chips[3]') | PASS | — |
| A6M2 | MANIM | light | min-size §8.1: min text-run height 67px >= floor 41px | PASS | — |
| BVDT | CLOSING | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | CLOSING | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | CLOSING | dark | min-size §8.1: min text-run height 239px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 16 | 0 |
| min-size §8.1 | 33 | 0 |
| overflow §8.2 | 33 | 0 |
| contrast §8.3 | 33 | 0 |
| contrast-local §8.3b | 33 | 0 |
| bbox-overlap §8.6b | 33 | 0 |
| card-clip §8.13 | 33 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 2 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
