# SHOTLIST — claude-liam-computational-epistemology
# Pass 1 work order · 2026-07-21
# Gate F: CLOSED · Gate P: SIGNED · Audio lock: 8:19
#
# STATUS KEY:
#   REMOTION  — remotion_scenes.py renders; pattern reconciled to real Composition ID
#   MANIM     — scenes.py class renders; Claude palette; scenes.py on disk
#   PANTRY    — human-supplied media needed; renders as SLATE until pantry/ fills
#   SLATE     — machine-generated slate (SlateCard or equivalent) — intentional pass-1 placeholder

| Beat | Act                     | Lane     | Window (s) | Pattern / Class           | Status  | Notes                                                         |
|------|-------------------------|----------|------------|---------------------------|---------|---------------------------------------------------------------|
| B00  | OPEN                    | bookend  | 17.78      | ClaudeComposerAsk         | REMOTION| Cold open; greeting 'Yassou, Liam'; output 3 lines           |
| B01  | I — The Flood           | card     | 6.67       | SlateCard                 | REMOTION| Act I card; eyebrow 'ACT I'                                  |
| B02  | I — The Flood           | vox      | 11.11      | —                         | PANTRY  | Seminar room; Tier 1 gen; pantry/B02.png                     |
| B03  | I — The Flood           | remotion | 11.86      | SlateCard                 | SLATE   | Scale mismatch; pass-1 slate (no ScaleComparison match)      |
| B04  | I — The Flood           | remotion | 12.72      | DivergentFates            | REMOTION| Two failure modes; first-person vs third-person tracks       |
| B05  | II — Lucky Truths       | card     | 6.02       | SlateCard                 | REMOTION| Act II card; eyebrow 'ACT II'                                |
| B06  | II — Lucky Truths       | manim    | 10.61      | B06_JTBStack              | MANIM   | JTB three-card stack → 'knowledge' lock                      |
| B07  | II — Lucky Truths       | vox      | 11.76      | —                         | PANTRY  | Gettier portrait; Tier 3 rights; pantry/B07.png + source.txt |
| B08  | II — Lucky Truths       | manim    | 14.45      | B08_TwoRails              | MANIM   | Truth rail + justification rail; snap + fall                 |
| B09  | II — Lucky Truths       | ask      | 7.27       | ClaudeComposerAsk         | REMOTION| ASK micro-beat; exempt from vox quota count                  |
| B10  | II — Lucky Truths       | remotion | 14.81      | ClaudeCodeBeat            | REMOTION| gettier_check.py; 15-line code reveal; sparkLine set         |
| B11  | II — Lucky Truths       | manim    | 13.68      | B11_GettierCoefficient    | MANIM   | Equation G_r = T·(1−S_NLI); bar worked example              |
| B12  | II — Lucky Truths       | manim    | 11.78      | B12_AxesApart             | MANIM   | Blend-then-lose; axes re-split                               |
| B13  | III — Show Your Work    | card     | 5.18       | SlateCard                 | REMOTION| Act III card; eyebrow 'ACT III'                              |
| B14  | III — Show Your Work    | vox      | 8.76       | —                         | PANTRY  | Ledger tight (R1 1/2); ≥2400px; pantry/B14.png serves B15  |
| B15  | III — Show Your Work    | vox      | 10.49      | —                         | PANTRY  | Ledger wide (R1 2/2); same plate as B14; vox_run R1         |
| B16  | III — Show Your Work    | remotion | 15.48      | DivergentFates            | REMOTION| Stated reasoning vs actual computation; interpretability     |
| B17  | III — Show Your Work    | manim    | 14.81      | B17_CalibrationGap        | MANIM   | Reliability diagram; 90/60 illustrative pair labeled         |
| B18  | III — Show Your Work    | remotion | 13.94      | ClaudeCodeBeat            | REMOTION| reliabilist_verifier.py; should_trust highlighted            |
| B19  | IV — Web and Bedrock    | card     | 5.30       | SlateCard                 | REMOTION| Act IV card; eyebrow 'ACT IV'                                |
| B20  | IV — Web and Bedrock    | manim    | 13.49      | B20_Regress               | MANIM   | Chain drop → bedrock block + coherence web                  |
| B21  | IV — Web and Bedrock    | remotion | 14.50      | ClaudeScienceLayerStack   | REMOTION| RAG as foundationalism; 3-layer stack; 1280×720 comp         |
| B22  | IV — Web and Bedrock    | vox      | 12.50      | —                         | PANTRY  | String wall parallax; Tier 1; TWO plates B22-bg + B22-mid   |
| B23  | IV — Web and Bedrock    | manim    | 14.11      | B23_OneWitness            | MANIM   | Three models on one corpus; agree-cards merge               |
| B24  | IV — Web and Bedrock    | remotion | 16.78      | ClaudeCodeBeat            | REMOTION| consensus.py; independence_weight highlighted                |
| B25  | IV — Web and Bedrock    | manim    | 13.90      | B25_LatentConfounder      | MANIM   | Two DAGs; latent L node pulses terracotta                    |
| B26  | V — The Demon Ships     | card     | 4.22       | SlateCard                 | REMOTION| Act V card; eyebrow 'ACT V'                                  |
| B27  | V — The Demon Ships     | vox      | 10.03      | —                         | PANTRY  | Descartes portrait (R2 1/3); Tier 3; pantry/B27.png + sidecar|
| B28  | V — The Demon Ships     | vox      | 12.43      | —                         | PANTRY  | Synthetic grid (R2 2/3); Tier 1 gen; pantry/B28.png         |
| B29  | V — The Demon Ships     | vox      | 15.74      | —                         | PANTRY  | Hume portrait (R2 3/3); Tier 3; pantry/B29.png + sidecar    |
| B30  | V — The Demon Ships     | remotion | 15.72      | ClaudeScienceSourceFlow   | REMOTION| Provenance chain; feeds→destApp; 1280×720 comp               |
| B31  | V — The Demon Ships     | manim    | 12.79      | B31_ProvenanceCap         | MANIM   | r(o)=min(p,c); min-gate clamps tall bar; terracotta on min() |
| B32  | VI — Belief as Number   | card     | 5.95       | SlateCard                 | REMOTION| Act VI card; eyebrow 'ACT VI'                                |
| B33  | VI — Belief as Number   | manim    | 15.46      | B33_CredenceDial          | MANIM   | Credence dial; evidence cards; phi+ML labels converge        |
| B34  | VI — Belief as Number   | remotion | 15.38      | BinaryBranch              | REMOTION| Sequential Bayesian vs majority vote; resolver block         |
| B35  | VI — Belief as Number   | manim    | 16.10      | B35_Surprise              | MANIM   | Two cards, different swing; S=−log₂P formula fades in        |
| B36  | VI — Belief as Number   | remotion | 13.30      | SlateCard                 | SLATE   | Threshold gate; pass-1 slate (Threshold not registered)      |
| B37  | CLOSE                   | bookend  | 18.89      | ClaudeVerdictArtifact     | REMOTION| Five recap lines; lead_silence_s 0.5                         |
| B38  | CLOSE                   | bookend  | 28.94      | ClaudeComposerAsk         | REMOTION| Your Turn; full 5-stage prompt types out                     |
| B39  | CLOSE                   | bookend  | 4.08       | ClaudeTitleOutro          | REMOTION| Title re-read; handle @NikBearBrown; subline set             |

---

## Lane summary (pass 1)

| Lane    | Count | Status                                               |
|---------|-------|------------------------------------------------------|
| bookend | 4     | REMOTION — B00, B37, B38, B39                       |
| card    | 6     | REMOTION (SlateCard) — B01, B05, B13, B19, B26, B32 |
| manim   | 11    | MANIM — B06, B08, B11, B12, B17, B20, B23, B25, B31, B33, B35 |
| remotion| 10    | REMOTION — B03(slate), B04, B10, B16, B18, B21, B24, B30, B34, B36(slate) |
| vox     | 8     | PANTRY — B02, B07, B14, B15, B22, B27, B28, B29     |
| ask     | 1     | REMOTION (exempt from quota) — B09                   |
| **TOTAL**| **40**|                                                     |

**Vox quota check:** 8/35 body beats = 22.9% — PASSES the 15–30% band.

## Pantry status (8 open slots)

B03 and B36 are **machine slates** (SlateCard pass-1 placeholder, not pantry — no human action needed).

The 8 PANTRY slots that wait on Bear:

| Slot       | File(s)                    | Tier | Method           |
|------------|----------------------------|------|------------------|
| B02        | pantry/B02.png             | 1    | Gen prompt below |
| B07        | pantry/B07.png + source.txt| 3    | Archive only     |
| B14        | pantry/B14.png             | 1    | Gen prompt below |
| B15        | (same plate as B14)        | —    | No separate file |
| B22        | pantry/B22-bg.png + B22-mid.png | 1 | Gen prompt below |
| B27        | pantry/B27.png + source.txt| 3    | Archive only     |
| B28        | pantry/B28.png             | 1    | Gen prompt below |
| B29        | pantry/B29.png + source.txt| 3    | Archive only     |

See PROMPTS.md for generation prompts and SHOPPING.md for archive search links.

## Vox-run handoffs

**R1 (B14→B15):** One ledger plate (≥2400px). B14 tight at 2.1× on ink
entries; B15 eases OUT revealing the full ledger + surrounding volumes.
Single pantry/B14.png file serves both beats.

**R2 (B27→B28→B29):** Three beats, two plates. B27 = Descartes portrait
(opens tight on eyes, eases out → stays as dimmed bg in B28). B28 = synthetic
grid plate (springs up over dimmed Descartes). B29 = Hume portrait cutout
(springs up beside the grid from B28 handoff frame).

## Open items / MISSING

- MISSING: `ClaudeScienceLayerStack` (B21) and `ClaudeScienceSourceFlow` (B30)
  are 1280×720 compositions — verify they scale acceptably in the 1920×1080
  timeline at compile; if not, the QC rubric will flag and they'll need
  1920×1080 wrappers or redrawn compositions.
- MISSING: Tier-3 portrait rights (B07 Gettier, B27 Descartes, B29 Hume)
  escalate to Bear — see SHOPPING.md for authored fallbacks.
- MISSING: `Threshold` Remotion composition not registered in Root.tsx;
  B36 uses SlateCard as pass-1 placeholder. Needs authored composition for
  final pass if the visual matters.
