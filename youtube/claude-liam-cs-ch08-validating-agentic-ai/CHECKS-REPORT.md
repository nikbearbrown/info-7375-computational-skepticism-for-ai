# CHECKS-REPORT — claude-liam-cs-ch08-validating-agentic-ai

Reel: `claude-liam-cs-ch08-validating-agentic-ai`  
Title: "You Broke My Toy."  
Date: 2026-07-30  
Compiled: 309.0 s · 14/14 beats filled  
Build: slate cut only (`art run`) — stopped per standing order

---

## Gate summary

| Gate | Result | Notes |
|------|--------|-------|
| GATE F (factcheck) | BYPASS | `ART_FACTS=0` — previz build, no FACTCHECK.md required |
| GATE L (beat-mix lint) | WARN (advisory) | 3 card-over-runtime advisories — see §2 |
| GATE BANNED-CARD | PASS | — |
| GATE B (layout audit) | PASS (CLEAN) | 8 scenes, 0 errors, 0 warnings |
| GATE V (visual QC) | PASS w/ MAJORs | 0 BLOCKER; 8 MAJOR — all FormACard underfill, by design — see §3 |
| GATE T (type-lock) | PASS | 14/14 beats PASS — 0 FAILs |
| GATE SHARPNESS | PASS | 14 beats, median LV=652.4 |
| GATE BOOKEND | PASS | Four bookends correct |

---

## §1 — GATE T fixes applied (type-lock iteration)

Three passes were required to reach GATE T PASS.

### Pass 1 — Original build (pre-session edits)
- All 7 Manim scenes used stale cached renders (pipeline skipped re-render: "already filled").
- TYPECHECK failed on 6 beats: B01/B04/B07 contrast; B03/B05/B08 min-size.

### Pass 2 — Manim cache cleared, scenes.py from prior session
- Deleted `manim/B01.mp4`–`B08.mp4`, reset build status, re-rendered fresh.
- B01, B02 now PASS (contrast fixed in prior session: all text → INK).
- Remaining 5 FAILs:

| Beat | Finding | Root cause |
|------|---------|-----------|
| B03 | min-size 33px < 35px | sz=22 Montserrat BOLD → 33px at 1080p logical (calibration: 1.5 px/font_size) |
| B04 | contrast #D97757 2.74:1 | ACCENT-colored box strokes (sw=2.5) on thin rows (h=0.95) detected as "accent text" by type checker |
| B05 | min-size 30px + contrast | sz=20 EB Garamond → 30px; ACCENT-colored consequence/report box strokes detected |
| B07 | contrast #D97757 2.74:1 | ACCENT-colored fundamental-row box strokes (sw=2.0 on h=0.68 rows) detected |
| B08 | min-size 33px < 35px | sz=22 EB Garamond → 33px |

### Pass 3 — scenes.py fixes
All five beats fixed:

**B03** — sz=22→24 for both `label()` and `serif()` elements. Result: 36px (PASS).

**B04** — `stroke_clr = ACCENT if ash else INK` → `stroke=INK` for all rows. Highlighted rows still distinguished by stroke weight (sw=2.5 vs 1.5). No text color change.

**B05** — (a) Box strokes: `conseq_box` ACCENT→INK, `report_box` ACCENT→INK. (b) Font sizes: `a_text`/`c_text` sz=20→24, `lbl` sz=22→24. (c) Box geometry widened (3.8→4.6 units, centers ±2.9→±3.4) to prevent overflow at sz=24 for "Moltbook: 'Nuclear options work'" (32 chars). Result: 36px, no overflow.

**B07** — `stroke_clr = ACCENT if is_fundamental else MUTE` → `stroke_clr = INK if is_fundamental else MUTE`. Fundamental rows still distinguished by INK stroke (sw=2.0) vs MUTE (sw=1.2).

**B08** — sz=22→24 for both `label()` and `serif()`. Label anchor RIGHT*2.0→RIGHT*1.7 (left side); description anchor LEFT*2.6→LEFT*3.0 (right side) to prevent overflow of longest description ("Social engineering across channel boundaries", 44 chars at sz=24 EB Garamond). Result: 37px (PASS).

---

## §2 — GATE L advisories (not blocking)

Three beats have card-over-runtime advisories: B06 (22.0s), B09 (22.0s), B10 (26.0s). These are long FormACard beats with no `motion_claim`. These are intentional predict/commit beats — the viewer is meant to sit with the key principle before the narration unpacks it. No upgrade needed; the dwell is deliberate. Bear to confirm or upgrade at review.

---

## §3 — GATE V MAJORs (design decision)

8 MAJOR `underfill` findings — all on sparse-text FormACard/outro beats:

| Beat | Fill % | Safe-area min |
|------|--------|--------------|
| B06 | 10% | 55% |
| B09 | 7% | 55% |
| B10 | 18% | 55% |
| BOUT | 43% | 55% |

These are inherent to the FormACard and ClaudeTitleOutro Remotion components: short title + subtitle on cream field is sparse by design. The underfill is a characteristic of the component, not a defect. `ART_STRICT=0` was used to prevent these from blocking the compile; they are documented here for Bear's review. If the scan indicates a redesign is needed, the components themselves (not the beat_sheet props) would require changes.

---

## §4 — BOUT fix

`ClaudeTitleOutro` `subline` prop was incorrectly set to `"Computational Skepticism for AI · Chapter 8"` (GATE BOOKEND requires `subline=""`). Fixed in `beat_sheet.json` and `media/BOUT.mp4` re-rendered. GATE BOOKEND now PASS.

---

## §5 — BVDT fix

`ClaudeVerdictArtifact` `artifactHeading` was truncated from  
`"Chapter 8 — Validating Agentic AI: When Autonomous Systems Misbehave"` (wraps to 2 lines → BLOCKER edge-bleed)  
to `"Chapter 8 key rules"` (single line, no bleed).  
`artifactLines` reduced from 5 to 4 (dropped a redundant validator/designer line).  
`media/BVDT.mp4` deleted and re-rendered. GATE V BVDT now PASS (no edge-bleed).

---

## §6 — What Bear reviews

1. **QC contact sheet**: `qc-sheet.png` in reel folder — sample frames of all 14 beats.
2. **GATE L card advisories**: B06, B09, B10 long-hold FormACard beats. Deliberate? Add `motion_claim` to stand the gate down, or upgrade to Manim/Remotion.
3. **GATE V underfill MAJORs**: B06/B09/B10/BOUT sparse fill — confirm this is acceptable per design, or request component upgrades.
4. **B04/B07 visual change**: Highlighted rows now use INK stroke (was terracotta ACCENT) to pass GATE T contrast check. Differentiation is now stroke weight only. Confirm acceptable, or request an alternative indicator (e.g., subtle fill tint).
5. **B05 font size increase**: Action/consequence text grew from sz=20→24; boxes widened. Layout audit clean, but visual density is lower. Confirm legible at 1080p output.

---

*STOPPED — per standing order. No `art final`, no `art post`, no 4K, no TOPOST, no publish. Bear reviews; next step is Bear's decision.*
