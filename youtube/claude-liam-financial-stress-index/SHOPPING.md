# SHOPPING — claude-liam-financial-stress-index
_Gate D2: pantry stills needed for VOX beats. All Tier 1 illustrative._
_Audio locked 2026-07-24. Kokoro am_onyx. 34 narrated beats, 8.2 min._

## Pantry stills (7 VOX beats → 7 stills)

### A1V — The question / one number six drivers
**File**: `pantry/A1V.png`
**Brief**: abstract financial dashboard: a single bold index line above a fan of six faint coloured sub-components; warm ink on cream; minimal, no real institution logos — Tier 1 illustrative
**Duration**: 19.07s · motion: kenburns · focus: [0.5, 0.45]
**Priority**: HIGH (ACT I opening VOX beat)

### A2V1 — No unique decomposition / correlation matrix
**File**: `pantry/A2V1.png`
**Brief**: correlation matrix heatmap of six financial stress components, warm terracotta tones in the high-correlation cells; a statistical artifact, not a real index — Tier 1 illustrative
**Duration**: 15.21s · motion: kenburns · focus: [0.5, 0.42]
**Priority**: HIGH (vox run R1 beat 1)
**Note**: vox_run R1 — last frame must hold camera position [0.52, 0.44, 1.35x] for A2V2 handoff

### A2V2 — VIF spike is the finding
**File**: `pantry/A2V2.png`
**Brief**: VIF time-series chart for a financial stress component, 2005-2023, showing dramatic spikes at 2008 and 2020; clean axes, warm ink on cream — Tier 1 illustrative
**Duration**: 15.32s · motion: drawon · focus: [0.5, 0.5]
**Priority**: HIGH (vox run R1 beat 2)
**Note**: vox_run R1 — opens at A2V1 handoff camera position, pans to VIF chart

### A3V — Window instability diagram
**File**: `pantry/A3V.png`
**Brief**: a crisis-window diagram: a time segment with a shaded block and dotted boundary lines showing ±1-month perturbation; two indicator ranking bars shown as reordered under the shift; warm ink on cream, no real data — Tier 1 illustrative
**Duration**: 18.01s · motion: kenburns · focus: [0.5, 0.48]

### A4V — TDA cross-validation
**File**: `pantry/A4V.png`
**Brief**: abstract two-panel comparison: LEFT a stylized bar chart (contribution analysis result), RIGHT a stylized persistence diagram; a check-mark convergence symbol in terracotta between them; clean, no real data — Tier 1 illustrative
**Duration**: 15.47s · motion: kenburns · focus: [0.5, 0.5]

### A5V — Causal verb audit / draft page
**File**: `pantry/A5V.png`
**Brief**: a draft paper page with four circled phrases in terracotta: 'drove', 'caused', 'triggered', 'led to'; the body text is illegible lorem-ipsum filler, not real text; editorial markup feel — Tier 1 illustrative
**Duration**: 16.94s · motion: drawon · focus: [0.5, 0.5]

### A6V — Publication note / peer review
**File**: `pantry/A6V.png`
**Brief**: abstract peer-review scenario: a manuscript page with two reviewer comment bubbles marked in terracotta — one pointing to a collinearity section, one to a crisis-N table; no real identifiers; editorial feel — Tier 1 illustrative
**Duration**: 18.07s · motion: kenburns · focus: [0.5, 0.47]

## Manim scenes (9 scenes — for agent / Phase 2 build)

| Beat | Scene | Short spec |
|------|-------|-----------|
| A1M | A1M_ThreeMethodsOneProblem | Three method boxes + six input bars + correlation lines converging to r≈0.9 |
| A2M1 | A2M1_CorrelatedBarsNoDecomposition | Two bars (CREDIT, VOL) with r=0.9 arc; SHAP 40%+40%=80% with question mark |
| A2M2 | A2M2_VIFSpikesInCrisis | Time series 2005-2023 VIF; crisis blocks at 2008/2020; VIF spikes to 15-20 |
| A2M3 | A2M3_TwoDefinitionsTwoAnswers | Two card panels: SHAP vs REGRESSION DECOMP; 'Pick one. Justify. Or report both.' |
| A3M | A3M_ThreeEpisodesSmallN | Time axis 2005-2025; crisis blocks N=1, N=2, N=3; final 'N≈3 independent episodes' |
| A4M | A4M_TDAParameterSensitivity | 2×2 grid of persistence diagram sketches; star on 'cleanest-looking'; 'all four are the same data' |
| A5M | A5M_CausalVerbAudit | Four verb pairs appearing with strikethrough: CAUSED → accounts for, etc. |
| A6M1 | A6M1_BandedNotCrisp | Two-panel: crisp waterfall LEFT vs banded/uncertain RIGHT |
| A6M2 | A6M2_SmallMultiplesDiagrams | 2×2 persistence diagrams with terracotta agreement band; 'robust' caption |

## Remotion beats (8 REMOTION + 5 BOOKEND/CARD = rendered via remotion_scenes.py)

All Remotion beats use existing patterns: ClaudeComposerAsk, ClaudeWindow, ClaudeVerdictArtifact, ClaudeTitleOutro, ChipGrid, DeckPattern, SlateCard. No new patterns needed.

## Slate previz status

First compile: all MANIM + VOX beats render as SlateCards. Remotion + CARD beats render as SlateCards (no Remotion run yet). This is the expected state for a slate previz.
