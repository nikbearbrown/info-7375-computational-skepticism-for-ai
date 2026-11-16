# SAVE-STATE.md — 2026-07-29

## Reel
`computational-skepticism-for-ai/youtube/claude-liam-two-models-twice-the-price/`

## What was completed (builds 1–6)
- 9 Manim scenes written in `scenes.py` (B05, B10, B16, B19, B20, B25, B26, B33, B36)
- All scene geometry/safe-area/contrast bugs fixed iteratively across 6 build runs
- B19 arc_fill changed ACC→INK (was causing GATE T contrast FAIL)
- B19 caption buff raised to 0.6 (layout WARN fix)
- GATE T: PASS (41/41), GATE V: PASS, GATE SHARPNESS: PASS, GATE BOOKEND: PASS

## New work (2026-07-29 — pilot fix session) — COMPLETE

11 violations identified and fixed (AUDIT.md has full before→after log):
- B02, B03, B09, B14, B15, B22, B27, B28, B32: gen-AI STILL shots → Manim drawn diagrams
- B13 (FormACard "routing diagram"), B31 (FormACard "funnel") → Manim drawn diagrams

11 new Manim scene classes added to scenes.py:
B02_ComparisonTable, B03_PriceRowReveal, B09_FootnoteChart, B13_RoutingDiagram,
B14_InferenceStack, B15_FallbackNode, B22_BlankEffortField, B27_ReceiptVsSticker,
B28_ReceiptDetail, B31_ComplianceFunnel, B32_ComplianceBinary

beat_sheet.json: all 11 beats updated (shot.type→GRAPHIC, source→own, graphic.manim section added)
B13 and B31: lane changed REMOTION→MANIM
Stale media clips deleted before each rebuild.

Builds 7–12: GATE T iteration across 4 builds to fix ACC-as-text contrast violations
in the new scenes (box strokes, SurroundingRectangles, label color=col patterns).
All resolved — no content or pedagogy changes needed.

Final build 12 gates: GATE T PASS (41/41) · GATE SHARPNESS PASS · GATE BOOKEND PASS
GATE BANNED-CARD PASS · GATE F PASS · GATE V non-blocking (BLOCKER=0)

Motion histogram: remotion:21 / graphic:20 (51% remotion — advisory only, not blocking)

AUDIT.md written · SHOPPING.md updated (no needed assets) · CHECKS-REPORT.md updated

STOP — awaiting Bear's review of compiled slate.

## Hard constraints
- Voice: Kokoro am_onyx only, no ElevenLabs
- Outro: ClaudeTitleOutro · @NikBearBrown · no subline
- No gen-AI, no paid generation, no publish, no 4K
- STOP after slate — Bear reviews
