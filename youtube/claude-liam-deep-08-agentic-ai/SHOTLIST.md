# SHOTLIST — claude-liam-deep-08-agentic-ai · "You Broke My Toy"
# Pass 1 work order · 2026-07-23
# Gate F: OPEN (FACTCHECK.md complete · SHOTLIST.md + PROMPTS.md written) · Audio lock: ~6:46
#
# STATUS KEY:
#   REMOTION  — remotion_scenes.py renders; pattern reconciled to real Composition ID
#   MANIM     — scenes.py class renders; Claude palette; scenes.py on disk
#   PANTRY    — human-supplied still needed; renders as SLATE until pantry/ fills
#   SLATE     — machine-generated slate (SlateCard) — intentional pass-1 placeholder

| Beat  | Act                              | Lane     | Window (s) | Pattern / Class                | Status   | Notes                                                                    |
|-------|----------------------------------|----------|------------|-------------------------------|----------|--------------------------------------------------------------------------|
| B00   | cold open                        | bookend  | 21.48      | ClaudeComposerAsk              | REMOTION | Merhaba cold open; 3-line output; greeting override                      |
| A1C   | ACT I — You Broke My Toy         | card     | 8.88       | SlateCard                      | REMOTION | Act I card; eyebrow 'ACT I'                                              |
| A1V1  | the setup                        | vox      | 14.06      | —                              | PANTRY   | R1 beat 1/3 — agent receives delete request; zoom-out start; pantry/A1V1.png |
| A1V2  | the misbehavior                  | vox      | 14.47      | —                              | PANTRY   | R1 beat 2/3 — console: "RESET completed"; same plate wider; pantry/A1V2.png |
| A1V3  | the consequence                  | vox      | 13.25      | —                              | PANTRY   | R1 beat 3/3 — wide: inbox intact, local client wiped; pantry/A1V3.png   |
| A1R   | the asymmetry                    | remotion | 14.95      | ClaudeWindow                   | REMOTION | Agent's view: done. Owner's view: broken. Two-pane code window           |
| A2M   | ACT II — Prediction vs Consequence | manim  | 15.41      | A2M_PredictionVsConsequence    | MANIM    | Split panel; bounded loss vs growing loss bar; broken replay arrow       |
| A2R   | three reasons                    | remotion | 17.45      | ChipGrid                       | REMOTION | 3 chips: State Change · Irreversibility · Audit Trail Was Also Wrong     |
| A2V   | the trail was wrong              | vox      | 12.43      | —                              | PANTRY   | Audit-trail scroll; faint world-state behind confident line; pantry/A2V.png |
| A3C   | ACT III — What Agents Lack       | card     | 6.22       | SlateCard                      | REMOTION | Act III card; eyebrow 'ACT III'                                          |
| A3R   | three deficits                   | remotion | 18.70      | ClaudeWindow                   | REMOTION | Three deficits in Claude window; code/comment format                     |
| A3K   | ask                              | ask      | —          | ClaudeComposerAsk              | REMOTION | ASK micro-beat; null duration; mp3/beat-A3K.mp3 anullsrc hold           |
| A3M   | reach without judgment           | manim    | 17.04      | A3M_AutonomyGap                | MANIM    | Vertical ladder; ACTIONS top, UNDERSTANDING bottom; terracotta gap band  |
| A3R2  | four categories                  | remotion | 17.26      | ChipGrid                       | REMOTION | 4 chips: Autonomy–Competence · Prompt Injection · Data Scope · Multi-Agent |
| A4M   | ACT IV — The Attack Surface      | manim    | 19.10      | A4M_InstructionDataConflation  | MANIM    | Context window token stream; planted terracotta instruction re-routes    |
| A4R   | effective scope                  | remotion | 19.10      | DeckPattern (divergence)       | REMOTION | Documented scope vs Effective scope; two-column split                    |
| A4M2  | identity across a boundary       | manim    | 19.63      | A4M2_ChannelBoundarySpoof      | MANIM    | Two channels; Ch1 ID mismatch→REFUSE(green); Ch2 fresh→ACCEPT→compromise |
| A4V   | the social vector                | vox      | 16.01      | —                              | PANTRY   | Chat request dressed as tech housekeeping; urgent precise tone; pantry/A4V.png |
| A5M   | ACT V — When Agents Talk         | manim    | 18.82      | A5M_CascadingHallucination     | MANIM    | Agent chain A→E; P(error)=1-(1-p)^n writes on; bar climbs to ~5%        |
| A5R   | two more modes                   | remotion | 19.82      | ChipGrid                       | REMOTION | 2 chips (+ context): Resource Exhaustion · Authority Laundering          |
| A5V   | identity confusion               | vox      | 16.78      | —                              | PANTRY   | Agent facing mirror image of own messages; duotone uncanny; pantry/A5V.png |
| A6R   | ACT VI — Fundamental vs Contingent | remotion | 17.76    | DeckPattern (divergence)       | REMOTION | Contingent (engineering fixes) vs Fundamental (architecture); two-column |
| A6M   | the patch that ships the failure | manim    | 17.71      | A6M_PatchShipsFailure          | MANIM    | Surface crack + patch; terracotta fault line below; new crack opens      |
| A7C   | ACT VII — The Boundary You Defend | card    | 7.46       | SlateCard                      | REMOTION | Act VII card; eyebrow 'ACT VII'                                          |
| A7K   | ask                              | ask      | —          | ClaudeComposerAsk              | REMOTION | ASK micro-beat; null duration; mp3/beat-A7K.mp3 anullsrc hold           |
| A7M   | the false-success catch          | manim    | 18.14      | A7M_FalseSuccessCatch          | MANIM    | Action→OWNER GATE→execute→agent report vs world check→comparator→STOP   |
| A7R   | four lenses, reshaped            | remotion | 20.16      | ClaudeWindow                   | REMOTION | Four validator prompts in Claude window; each prefixed with beat ID      |
| A7R2  | validate, don't redesign         | remotion | 17.35      | DeckPattern (threshold)        | REMOTION | Threshold card: "the agent should have been built with..." is design     |
| A7SRC | sources                          | card     | 14.11      | SlateCard                      | REMOTION | Sources card; SLATE pass-1 (chapter has unconfirmable arXiv ID)          |
| BVDT  | verdict                          | bookend  | 32.86      | ClaudeVerdictArtifact          | REMOTION | Five recap lines; lead_silence_s 0.5                                     |
| BHTF  | your turn handoff                | bookend  | 28.32      | ClaudeComposerAsk              | REMOTION | Your Turn; full 5-stage prompt types out                                 |
| BOUT  | outro                            | bookend  | 7.34       | ClaudeTitleOutro               | REMOTION | Title re-read; handle @claude-liam; subline set                          |

---

## Lane summary (pass 1)

| Lane     | Count | Status                                                                   |
|----------|-------|--------------------------------------------------------------------------|
| bookend  | 4     | REMOTION — B00, BVDT, BHTF, BOUT                                        |
| card     | 4     | REMOTION — A1C, A3C, A7C, A7SRC                                        |
| vox      | 6     | PANTRY — A1V1 (R1·1/3), A1V2 (R1·2/3), A1V3 (R1·3/3), A2V, A4V, A5V  |
| manim    | 7     | MANIM — A2M, A3M, A4M, A4M2, A5M, A6M, A7M                             |
| remotion | 10    | REMOTION — A1R, A2R, A3R, A3R2, A4R, A5R, A6R, A7R, A7R2 + ask×2     |
| ask      | 2     | REMOTION (anullsrc) — A3K, A7K                                          |

## Vox continuity run

**R1 — the Ash case:** A1V1 → A1V2 → A1V3. One continuous zoom-out from the delete request
to the "RESET completed" report to the wide reveal of the email still alive. Author as one plate
at three crops if possible; see SHOPPING.md for exact motion spec.
