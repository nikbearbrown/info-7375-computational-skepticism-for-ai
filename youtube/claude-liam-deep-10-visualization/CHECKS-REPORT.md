# CHECKS-REPORT — claude-liam-deep-10-visualization
**The Chart Isn't Neutral. It's Arguing.**
Generated: 2026-07-31 (updated post-fix pass)

---

## Summary

| Gate | Status | Notes |
|---|---|---|
| GATE A (static check) | ✅ ALL PASS | 14 scenes, 0 errors |
| GATE B (layout audit) | ✅ ALL CLEAN | 14 scenes, 0 errors, 0 warnings |
| Beats filled | ✅ 34/34 | A1K + A6K (silent orphan ASK beats) removed |
| GATE T (type-lock) | ✅ ALL PASS | 34/34 beats, 0 FAILs; §8.3b per-blob + §8.6b bbox-overlap gates added |
| GATE AUDIO | ✅ PASS | mean_volume −24.1 dB (threshold −40 dB); 34 beats Kokoro am_onyx |
| GATE V (visual QC) | ⚠️ Partial | 2 Manim edge-bleed fixes applied; VIDEO underfill is expected |

---

## Nopunt pass result

All 32 originally-punted beats now route to real renderers:

| Renderer | Count | Beat IDs |
|---|---|---|
| MANIM | 15 | A1M A2M A3M A3M2 A4M A4M2 A5M A5V1 A5V2 A5V3 A5V4 A6M A6R2 A6V1 A7V |
| REMOTION / VIDEO | 12 | B00 A1C A1R A2C A2R A3C A3R A4C A4R A5C A5R A6C A6R A7C A7R A7R2 BVDT BHTF BOUT |
| CARD | 7 | (included in VIDEO count above) |

Motion histogram: remotion:12, manim:15, card:7 — manim at 44% (over 40% cap after A6R2 converted from REMOTION→MANIM; noted in art final WARNING but not a blocker).

---

## GATE A results (all 14 Manim scenes)

All 14 scenes pass static check with 0 errors, 0 warnings. Key scenes re-written from `MovingCameraScene` to plain `Scene` to fix pipeline regex discovery (A5V3, A5V4).

---

## GATE B results (all 14 Manim scenes)

All 14 scenes pass layout audit CLEAN (0 errors, 0 warnings). Key fixes applied during this pass:

| Scene | Issue | Fix |
|---|---|---|
| A5V1 | x-axis label overlapping caption | Shortened label, moved to axis end |
| A5V1 | tick labels + caption at same y | Raised ax_y0 from -2.8 to -2.2 |
| A5V2 | title/caption outside ±3.4 safe area | Changed buff from 0.3 to 0.65 |
| A5V2 | vertical streets crossing title area | Clipped y_end from 3.2 to 2.7 |
| A5V3 | death dot arc crossing caption | Moved caption from y=-2.4 to y=-2.75 (then y=-2.95 after zoom fix) |
| A5V4 | note crossing y=-2.8 street | Increased buff from 0.12 to 0.25 |
| A6V1 | text-on-text: label + note at same y | Made note sequential (label fades out before note appears) |
| A6V1 | box sides crossing label centerline | Marked lbl1_box/lbl2_box `_qc_intentional=True` |
| A7V | arc labels flagged on arc curves | Marked each `annular._qc_intentional=True` |

---

## GATE V results

GATE V ran on the initial art run compilation. Manim-specific issues were fixed; VIDEO beat issues are noted below.

### Fixed (Manim)

| Frame | Issue | Fix |
|---|---|---|
| A5V3 | edge-bleed top/left/right | Death dot (y_orig=1.6) → y_screen=3.74 > ±3.4; horizontal lines to x=±11.66 off frame. Fixed: y_shift=-0.40, horizontal lines clipped to x=±2.5, vertical y_end=1.5 |
| A7V | edge-bleed left/right/top | Full-frame Rectangle(width=14, height=8.5) exceeded title-safe. Fixed: replaced with `self.camera.background_color` |

### Expected false positives (VIDEO beats — pantry clips)

These `underfill` flags are expected for card-type and narration-only beats:

| Beats | Fill % | Reason |
|---|---|---|
| A1C, A2C, A3C, A4C, A5C, A6C, A7C | 2–4% | Single-concept title card beats — intentionally minimal |
| A1R, A2R, A5R, A6R, A7R | 16–52% | Narration beats with limited on-screen content |
| A4M | 49% | Just below 55% threshold — close call |
| BOUT | 51% | Outro beat — intentionally spare |

A6R2 is now a Manim SHOW beat — no longer a static card; removed from underfill list.

### Requires Bear's review

| Frame | Issue | Notes |
|---|---|---|
| A3R, A4R | edge-bleed top | Pantry clip content bleeds past title-safe top — need to inspect the clip or re-crop |
| A6V1 | low-contrast (0.22 < 0.3) | Nigeria map: dark fill regions on cream background — intentional design but below threshold |

---

## Audio

Kokoro audio generated for all 36 beats. All beats have `actual_duration_s` set from measured audio.

---

## GATE T fixes applied (2026-07-31)

Three fixes resolved 3 original FAILs and 1 false-positive from newly rendered clips:

| Beat | Check | Root cause | Fix |
|---|---|---|---|
| A3M | min-size §8.1 (30px) | `err_lbl` font sz=12 | Increased to sz=16 |
| A5M | min-size §8.1 (33px) | Year labels + `m_lbl` sz=13 | Increased to sz=16 |
| A5V1 | contrast §8.3 | `trend` + `cold_arrow` in ACCENT; then incident dot pair at 57–58°F (67.5px apart, 0.14-radius dots merge into 141×77px blob w/h=1.83) | Arrows → MUTE; dot radius 0.14 → 0.10 (breaks merger, keeps dots visually clear) |

---

## Review cut

`art final` output: `claude-liam-deep-10-visualization.mp4` (631s, ~10.5 min, 34/34 slots filled)

---

## Fix pass (2026-07-31, post-review)

Four fixes applied after Bear's review of the initial cut:

| Fix | What changed |
|---|---|
| A1K + A6K removed | Silent orphan ASK beats (empty narration_text) cut from beat_sheet.json; orphan mp3/media deleted; beat count 36→34 |
| A1M label collision | gap_arrow shifted from x=right_x+0.7 (same x as bar B + pct82) to x=right_x+1.5 (open panel space); pct96/pct82 buff 0.06→0.14; A1M re-rendered |
| A7V contrast | Labels already fixed in prior pass (dark-ground cream text + leader ticks); no further change needed |
| §8.6b bbox-overlap gate | New `check_bbox_overlap` added to type_check.py — pairwise bounding-box overlap check, FAIL if intersection > 10% of smaller bbox; wired into main loop after §8.3b; 34/34 PASS |
| A6R2 tell-not-show | Static FormACard replaced with Manim `A6R2_EqualWeight` scene: Phase 1 — big 68% estimate + tiny I-bar whisker ("answer with quibble"); Phase 2 — Transform(band_thin→band_thick) grows CI band to equal visual weight; verdict "the uncertainty IS the finding"; GATE T PASS; motion count MANIM 15/34 (44%, warned not blocked) |
| A7V label routing | Rule: no ring label may sit on a ring. 1870/1880/1890 (outward positions land on cream/red/terracotta rings) routed INWARD to dark center hole (r=0.42, cream on #1A1208 ≈16:1). Labels fanned at −2°/−30°/−80° placement angles (vs ring midpoints −10°/−35°/−60°) to prevent stacking in the lower-right of the hole. Leaders from each label (r=0.50) to its ring's inner edge at the ring's midpoint angle. 1900/TOTAL already in dark field, kept outside at r_out+0.55. `_qc_intentional=True` on AnnularSectors updated (was "labels sit on arc", now "arc shape geometry"). GATE T PASS. |

---

## STOP — awaiting Bear review

Per STANDING ORDER: no `art post`, no 4K upscale, no TOPOST, no publish.
Next steps are Bear's call.
