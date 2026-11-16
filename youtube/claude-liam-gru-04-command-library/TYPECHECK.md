# TYPECHECK.md — GATE T

Reel: `claude-liam-gru-04-command-library`  |  Checked: 2026-07-24T02:43  |  Overall: PASS  |  Beats checked: 9  |  FAILs: 0

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 1.6× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | no video | SKIP | — |
| B01 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| B02 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 12 words in 'artifactLines… | PASS | — |
| B03 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 11 words in 'artifactLines… | PASS | — |
| B04 | ? | no video | SKIP | — |
| B05 | ? | no-wordy-card §8.5: ClaudeWindow: per-element check passed (max 12 words in 'artifactLines… | PASS | — |
| BVDT | ? | no video | SKIP | — |
| BHTF | ? | no video | SKIP | — |
| BOUT | ? | no video | SKIP | — |

---

## Failures requiring action before cut

*None — GATE T PASS.*
---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 4 | 0 |
| min-size §8.1 | 0 | 0 |
| overflow §8.2 | 0 | 0 |
| contrast §8.3 | 0 | 0 |
| kerning §8.4 | 0 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
