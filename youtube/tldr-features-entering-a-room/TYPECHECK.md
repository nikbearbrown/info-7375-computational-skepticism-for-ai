# TYPECHECK.md — GATE T

Reel: `tldr-features-entering-a-room`  |  Checked: 2026-09-23T13:53  |  Overall: PASS  |  Beats checked: 17  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

> **§8.10 REDUNDANCY (advisory — does not block cut):**
> Narration should DISCUSS on-screen text, not recite it.
> Exception: LITERAL beats (viewer types/copies/runs the text) are exempt.

> - §8.10 [B01] narration recites the card (0.95) — discuss it, don't read it

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B01 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | bookend | light | min-size §8.1: min text-run height 68px >= floor 41px | PASS | — |
| B03 | bookend | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B10 | manim | light | min-size §8.1: min text-run height 57px >= floor 41px | PASS | — |
| B11 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px | PASS | — |
| B12 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B13 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px | PASS | — |
| B14 | manim | light | min-size §8.1: min text-run height 52px >= floor 41px | PASS | — |
| B15 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B16 | manim | light | min-size §8.1: min text-run height 51px >= floor 41px | PASS | — |
| B17 | manim | light | min-size §8.1: min text-run height 50px >= floor 41px | PASS | — |
| B18 | manim | light | min-size §8.1: min text-run height 49px >= floor 41px | PASS | — |
| B19 | manim | light | min-size §8.1: hand-drawn pattern (B19_Payoff) — §8.1 hachure/crossbar fragments are false… | PASS | — |
| BVDT | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | bookend | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | bookend | dark | min-size §8.1: min text-run height 65px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 3 | 0 |
| min-size §8.1 | 17 | 0 |
| overflow §8.2 | 17 | 0 |
| contrast §8.3 | 17 | 0 |
| contrast-local §8.3b | 17 | 0 |
| bbox-overlap §8.6b | 17 | 0 |
| card-clip §8.13 | 17 | 0 |
| kerning §8.4 | 10 | 0 |
| redundancy §8.10 (advisory) | 3 | 1 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
