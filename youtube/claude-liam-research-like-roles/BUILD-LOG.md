# BUILD-LOG — Research-Like Roles.

## Gate log

| Gate | Status | Notes |
|------|--------|-------|
| Plan | AUTO | Beat sheet authored in prior session from source doc |
| GATE P | PASS | Narration verified beat-by-beat against source |
| FACTCHECK | CLEAN | All claims sourced; no invented statistics |
| GATE T (type-check) | PENDING | Run when advancing to review cut |
| Gate D1 (slate previz) | DONE | claude-liam-research-like-roles-slate.mp4 — 386.8s (6:27), $0.00 |
| Gate D2 (SHOPPING.md) | PENDING | Write after reviewing previz — 5 VOX slots need pantry stills |

## Decisions

- FIRST NAME ONLY: student referred to as "Zening" throughout per user instruction.
- Beat_sheet restructured: top-level `remotion` keys moved into `shot.remotion` to match pipeline schema.
- CARD beats (B01, B05, B10, B14, B18, B20) use ClaudeComposerAsk with empty `command` and `runningText: "act N"` — acts as a segment card.
- MANIM beats (B06, B07, B12, B16, B21, B22, B23, B24): pre-rendered manim/ files found and compiled in. Five beats flagged for replacement (B07 3.9×, B12 3.3×, B21 3.4×, B22 3.7×, B24 4.3× slow-mo) — manim renders too short for their beat durations; regen before review cut.
- VOX beats (B02, B03, B08, B11, B15) will render as slates — pantry stills not yet sourced.
- Build mode: UNATTENDED through full-length SLATE PREVIZ per user instruction.

## QC pass — Gate D1 (2026-07-24)

QC report: `_qc/REPORT.md` — 0 BLOCKER · 0 MAJOR · 1 MINOR (resolved)

**D3 — B21 illustrative label off-screen (FIXED)**  
`move_to([7.5, 3.8, 0])` in scenes.py placed the label past the Manim frame boundary (±7.11). Only "ill" showed. Fixed to `to_corner(UR, buff=0.35)`. Re-rendered; recompiled. Verified with late-frame grab.

**D4 — B21 extreme slow-mo (for final)**  
Manim render 4.8s slowed 3.4× into 16.4s beat. Acceptable in previz. For final: extend `B21_FakeTrendChart` to ~16s (add trend-line draw phase, hold).

**D5 — Remotion 53% warning is a counting artifact**  
Compiler counts 15 "remotion" beats = 53%. Of those, 10 are structural framing (4 bookends + 6 act cards) — non-optional. Content-layer Remotion beats: 5. Not an excess. Concept-illustration beats (posting split, trend, sensitivity) correctly use Manim for precision.

**Laws verified:** AUDIO-FIRST ✓ · IN-FOR-BEAR ✓ · FIRST NAME ONLY ✓ · DOUBLE-CHECK ✓ · ILLUSTRATE ✓ · 14pt floor ✓ · NO PUBLISH ✓
