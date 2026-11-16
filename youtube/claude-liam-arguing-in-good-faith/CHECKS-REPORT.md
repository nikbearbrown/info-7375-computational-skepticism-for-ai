# CHECKS-REPORT — claude-liam-arguing-in-good-faith

Slate cut compiled: 2026-08-22  |  Runtime: 265.0s (4:25)  |  Canvas: 3840×2160 @ 24fps

## Gate roster

| Gate | Result | Notes |
|------|--------|-------|
| GATE-F (factcheck) | **PASS** | 9 rows, all PASS or EXEMPT |
| GATE-L (beat-lint) | **PASS** | 12 card-over-runtime advisories — see below |
| GATE-BANNED-CARD | **PASS** | — |
| GATE-V (visual QC) | **PASS** | BLOCKER=0 · STRUCTURAL=0 · COSMETIC=0 |
| GATE-T (type-lock) | **PASS** | 4 §8.10 redundancy advisories — see below |
| GATE-SHARPNESS | **PASS** | Median LV=375.6, 16 beats |
| GATE-BOOKEND | **PASS** | B00/BVDT/BHTF/BOUT structure correct |
| GATE-AUDIO | **PASS** | Mean −24.0 dB |
| GATE-MASTER | **PASS** | 3840×2160 · 24fps · yuv420p · h264 |
| GATE-LOUDNESS | **PASS** | −24.33 LUFS · tp=−2.76 dBTP |
| GATE-RECEIPTS | **PASS** | — |

## Advisories (non-blocking)

### Card-over-runtime (GATE-L, §8.5 advisory)

B01–B12 are all FallacyCard or FormACard beats lasting 11–21s with no `motion_claim`. The
stagger-reveal spring animation (icon → title → badge → rule → definition → examples → test)
IS the motion — each element slides in over ~3s of dwell. These are deliberate predict/commit
beats: the card reveals progressively while Liam's narration arrives. Motion is baked into the
component; adding a `motion_claim` per beat would accurately describe this.

**Bear decision needed:** add `motion_claim` entries to B01–B12 naming the spring-reveal
stages, or accept the advisory as-is.

### §8.10 Redundancy advisories (GATE-T, advisory — does not block cut)

| Beat | Score | Issue |
|------|-------|-------|
| B05 | 1.00 | FormACard narration recites the card text |
| B09 | 0.92 | FormACard narration closely paraphrases the card |
| B11 | 1.00 | FormACard narration recites the card text |
| B12 | 1.00 | FormACard dark narration recites the card text |

These beats are **commentary cards**: the narration IS the card. The §8.10 exemption for
"LITERAL beats" does not technically apply (not viewer-typed text), but the design intent
is to let Liam read each FormACard aloud as the reveal completes — the card IS the script.
Advisory only; does not block.

### Remotion dominance warning

All 16 beats are Remotion (100% vs 40% pantry cap). This is by design — the reel is a
pure FallacyCard / FormACard / bookend composition with no Manim or pantry stills.

## QC frame review

- QC contact sheet: `_qc/REPORT.md` — BLOCKER=0
- `qc-sheet.png` in reel folder

## Standing-order stop

Per standing order: slate cut complete, stopped here. No `art final`, no TOPOST, no publish.
Bear reviews `claude-liam-arguing-in-good-faith.mp4` and decides next steps.
