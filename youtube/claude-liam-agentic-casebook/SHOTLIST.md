# SHOTLIST — claude-liam-agentic-casebook · "Red-Team Your Agent"
# Pass 1 work order
# Gate F: OPEN (FACTCHECK.md · SHOTLIST.md · PROMPTS.md written)  Audio lock: ~8:08 est.
#
# STATUS KEY:
#   REMOTION  — remotion_scenes.py renders; pattern reconciled to real Composition ID
#   MANIM     — scenes.py class renders; Claude palette; scenes.py on disk
#   PANTRY    — human-supplied still needed; renders as SLATE until pantry/ fills
#   SLATE     — machine-generated placeholder (FormACard / ChipGrid fallback)

| Beat | Act                              | Lane    | Window (s) | Pattern / Class              | Status   | Notes                                                                    |
|------|----------------------------------|---------|------------|------------------------------|----------|--------------------------------------------------------------------------|
| B00  | cold open                        | bookend | 30         | ClaudeComposerAsk            | REMOTION | Merhaba · 3-line output · greeting override                              |
| B01  | exec summary                     | bookend | 10         | FormBCard                    | REMOTION | 3-item card: three lenses · prediction-lock · artifact/world/owner       |
| A1C  | ACT I — The Pebble               | card    | 5          | FormACard                    | REMOTION | Act I title card                                                         |
| A1R  | what the casebook is             | remotion| 18         | ChipGrid                     | REMOTION | 4-chip grid: Pebble · 3 lenses · prediction-lock · world check           |
| A1V  | Pebble selection                 | vox     | 16         | —                            | PANTRY   | Pebble/consequence-rings concept; pantry/A1V.png                         |
| A1M  | tool surface — the dossier       | manim   | 17         | A1M_ToolSurface              | MANIM    | Ash radial diagram; 5 arms; file delete + self-config in terracotta      |
| A2C  | ACT II — G-01 False Success      | card    | 5          | FormACard                    | REMOTION | Act II title card                                                        |
| A2V1 | the Ash case setup               | vox     | 15         | —                            | PANTRY   | Console showing "RESET completed"; R1 beat 1/2; pantry/A2V1.png         |
| A2K  | ask                              | ask     | 3          | ClaudeComposerAsk            | REMOTION | ASK micro-beat; renders Manim scene; anullsrc hold                       |
| A2M  | the false-success mechanism      | manim   | 18         | A2M_FalseSuccessGap          | MANIM    | Two-column AGENT REPORT vs WORLD STATE; terracotta MISMATCH comparator   |
| A2V2 | the world check                  | vox     | 15         | —                            | PANTRY   | Server inbox intact / local client wiped; R1 beat 2/2; pantry/A2V2.png  |
| A2R  | PA and PF failure analysis       | remotion| 16         | DeckPattern (divergence)     | REMOTION | PA vs PF two-column divergence card                                      |
| A3C  | ACT III — D-01 Explainability    | card    | 5          | FormACard                    | REMOTION | Act III title card                                                       |
| A3V  | say vs did                       | vox     | 17         | —                            | PANTRY   | Split: "email only"/Discord + "record deleted"/redacted; pantry/A3V.png  |
| A3M  | mismatch taxonomy                | manim   | 17         | A3M_MismatchTaxonomy         | MANIM    | 3-row classification table; terracotta on wrong; Plato caption           |
| A3R  | IJ and PA failure                | remotion| 16         | FormACard                    | REMOTION | 3-line FormACard: PA / IJ / "artifact is not the world"                  |
| A4C  | ACT IV — C-01 Robustness         | card    | 5          | FormACard                    | REMOTION | Act IV title card                                                        |
| A4V  | the cross-channel spoof setup    | vox     | 17         | —                            | PANTRY   | Two channel panels; refused / boundary / accepted; pantry/A4V.png       |
| A4K  | ask                              | ask     | 3          | ClaudeComposerAsk            | REMOTION | ASK micro-beat; renders Manim scene; anullsrc hold                       |
| A4M  | channel boundary visualization   | manim   | 18         | A4M_ChannelBoundarySpoof     | MANIM    | Ch1 REFUSE (green) · wall · Ch2 FULL COMPROMISE (terracotta)             |
| A4R  | TO and PF failure                | remotion| 17         | DeckPattern (divergence)     | REMOTION | Contingent (display-name) vs Fundamental (prompt-injection)              |
| A5M  | ACT V — Descartes                | manim   | 19         | A5M_DescartesGrid            | MANIM    | Root claim → 3 falsification branches; each lights terracotta            |
| A5R  | Hume, Popper, Plato              | remotion| 22         | ChipGrid                     | REMOTION | 4-chip grid: Descartes · Hume · Popper · Plato                          |
| A6C  | ACT VI — Attestation             | card    | 5          | FormACard                    | REMOTION | Act VI title card                                                        |
| A6V  | what I tested and did NOT test   | vox     | 21         | —                            | PANTRY   | Audit notebook: TESTED (checked) / NOT TESTED (gaps); pantry/A6V.png    |
| A6R  | five supervisory capacities      | remotion| 18         | ChipGrid                     | REMOTION | 4-chip grid (PA · PF · TO · IJ) + sparkLine for EI                      |
| A6M  | who owns the break               | manim   | 18         | A6M_AccountabilityTable      | MANIM    | 5-row table; terracotta on ungapped rows; footer note                    |
| A7R  | go/no-go memo                    | remotion| 19         | DeckPattern (threshold)      | REMOTION | REFUSE / DEFER / DEPLOY with conditions                                  |
| A7K  | ask                              | ask     | 3          | ClaudeComposerAsk            | REMOTION | ASK micro-beat; renders Manim scene; anullsrc hold                       |
| A7M  | the prediction-lock discipline   | manim   | 19         | A7M_PredictionLockPaths      | MANIM    | Lock box → CONFIRMED / SURPRISED / UNGROUNDED (terracotta X)             |
| BVDT | verdict                          | closing | 44         | ClaudeVerdictArtifact        | REMOTION | 8 artifact lines; lead_silence_s 0.5                                     |
| BHTF | your turn handoff                | closing | 46         | ClaudeComposerAsk            | REMOTION | Your Turn; full prompt with Dossier + lens + prediction-lock              |
| BOUT | outro                            | closing | 7          | ClaudeTitleOutro              | REMOTION | "Red-Team Your Agent" · @NikBearBrown · Liam in for Bear                 |

---

## Lane summary (pass 1)

| Lane    | Count | Status                                              |
|---------|-------|-----------------------------------------------------|
| bookend | 2     | REMOTION — B00, B01                                 |
| card    | 5     | REMOTION — A1C, A2C, A3C, A4C, A6C                 |
| vox     | 6     | PANTRY — A1V, A2V1, A2V2, A3V, A4V, A6V            |
| ask     | 3     | REMOTION (anullsrc) — A2K, A4K, A7K                |
| manim   | 7     | MANIM — A1M, A2M, A3M, A4M, A5M, A6M, A7M          |
| remotion| 7     | REMOTION — A1R, A2R, A3R, A4R, A5R, A6R, A7R       |
| closing | 3     | REMOTION — BVDT, BHTF, BOUT                         |

## Vox continuity runs

| Run | Beats    | Subject                          | Plate approach              |
|-----|----------|----------------------------------|-----------------------------|
| R1  | A2V1/A2V2| G-01: RESET report → world check | two separate plates (different subjects) |

## Open pantry slots

All 6 vox stills need human-supplied images. See `PROMPTS.md` for paste-ready
image-generation prompts. Until pantry/ fills, these beats render as FormACard
SLATE fallback.
