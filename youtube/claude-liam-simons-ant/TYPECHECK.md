# TYPECHECK.md — GATE T

Reel: `claude-liam-simons-ant`  |  Checked: 2026-08-28T02:07  |  Overall: **FAIL**  |  Beats checked: 28  |  FAILs: 1

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 1.9% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 3.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | polarity | worst finding | status | fix |
|------|------|----------|---------------|--------|-----|
| B00 | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| B01 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B02 | MANIM | light | min-size §8.1: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a capt… | **FAIL** | Increase font_size in scenes.py or Remotion component |
| B03 | MANIM | light | min-size §8.1: min text-run height 41px >= floor 20px | PASS | — |
| B04 | MANIM | light | min-size §8.1: min text-run height 28px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B05 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B06 | MANIM | light | min-size §8.1: min text-run height 37px >= floor 20px | PASS | — |
| B07 | MANIM | light | min-size §8.1: min text-run height 97px >= floor 20px | PASS | — |
| B08 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B09 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B10 | MANIM | light | min-size §8.1: min text-run height 37px >= floor 20px | PASS | — |
| B11 | REMOTION | dark | no-wordy-card §8.5: no prose payload found | PASS | — |
| B12 | MANIM | light | min-size §8.1: min text-run height 36px >= floor 20px | PASS | — |
| B13 | MANIM | light | min-size §8.1: min text-run height 36px >= floor 20px | PASS | — |
| B14 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B15 | MANIM | light | min-size §8.1: min text-run height 36px >= floor 20px | PASS | — |
| B16 | MANIM | light | min-size §8.1: min text-run height 37px >= floor 20px | PASS | — |
| B17 | MANIM | dark | min-size §8.1: min text-run height 37px >= floor 20px | PASS | — |
| B18 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B19 | MANIM | light | min-size §8.1: min text-run height 128px >= floor 20px | PASS | — |
| B20 | MANIM | light | min-size §8.1: min text-run height 35px >= floor 20px | PASS | — |
| B21 | MANIM | light | min-size §8.1: min text-run height 21px >= floor 20px (individual-char fallback at 1×) | PASS | — |
| B22 | REMOTION | light | no-wordy-card §8.5: no prose payload found | PASS | — |
| B23 | MANIM | light | min-size §8.1: min text-run height 36px >= floor 20px | PASS | — |
| B24 | MANIM | light | min-size §8.1: min text-run height 37px >= floor 20px | PASS | — |
| BVDT | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeVerdictArtifact) — §8.1 hachure/crossbar fragment… | PASS | — |
| BHTF | REMOTION | light | min-size §8.1: hand-drawn pattern (ClaudeComposerAsk) — §8.1 hachure/crossbar fragments ar… | PASS | — |
| BOUT | REMOTION | light | min-size §8.1: min text-run height 97px >= floor 41px | PASS | — |

---

## Failures requiring action before cut

### B02 (MANIM)
- **min-size §8.1**: smallest text run 10px < floor 20px (1.9% of 1080px logical); likely a caption/label too small — increase font_size or check if this is a data label needing §7 treatment
- **Fix:** Increase font_size in scenes.py or Remotion component

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 7 | 0 |
| min-size §8.1 | 28 | 1 |
| overflow §8.2 | 28 | 0 |
| contrast §8.3 | 28 | 0 |
| contrast-local §8.3b | 28 | 0 |
| bbox-overlap §8.6b | 28 | 0 |
| card-clip §8.13 | 28 | 0 |
| kerning §8.4 | 17 | 0 |
| redundancy §8.10 (advisory) | 1 | 0 (advisory — no exit effect) |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
