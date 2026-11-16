# CHECKS-REPORT.md — claude-liam-simons-ant

Date: 2026-08-13  |  Reel: 28 beats, 8:41  |  Slate cut: `claude-liam-simons-ant.mp4`

---

## Gate roster — all green

| Gate | Result |
|------|--------|
| GATE-F (format) | PASS |
| GATE-L (lint) | PASS |
| GATE-BANNED-CARD | PASS |
| GATE-SWEEP-WARN | PASS |
| GATE-P (phase) | PASS |
| GATE-G | PASS |
| GATE-V (visual QC, 56 frames) | PASS |
| GATE-T (typography) | **PASS — 0 FAILs / 28 beats** |
| GATE-SHARPNESS | PASS — 28 beats, median LV=138.8 |
| GATE-BOOKEND | PASS |
| GATE-AUDIO | PASS — mean_volume −24.1 dB |
| GATE-RECEIPTS | PASS |

---

## GATE-T detail — formerly-failing beats

All 5 beats that failed in the prior compile now pass.

| Beat | Was | Now | Fix |
|------|-----|-----|-----|
| B02 | 25px (FAIL) | **41px** | label sz 20→32, buff 0.35→0.5; annot sz 34→48 |
| B03 | 25px (FAIL) | **41px** | label sz 20→32, buff 0.35→0.5; note sz 20→32 |
| B15 | 25px (FAIL) | **36px** | defn sz 34→48 (MUTE is detected by ink_mask) |
| B20 | 19px (FAIL) + contrast | **35px** | fill_opacity 0.7→1.0 (opaque circles filtered by w/h<1.5); summary sz 30→48 with 2-line split |
| B24 | 22px (FAIL) | **37px** | title sz 20→32; DESCRIPTION sz 20→32; quote sz 34→48; question sz 38→48; note sz 18→28 |

Floor: 35px (3.2% of 1080px logical).

---

## Root causes

1. **MUTE text is detected** — `visible_text_mask` unions both INK (#3D3929) and MUTE (#5D584F) masks. MUTE text below the floor fails §8.1. Several scenes had MUTE labels at sz=20 (≈25px) or sz=34 EB Garamond (≈25px ascender).

2. **Overflow: buff too small** — B02/B03 used `to_edge(UP, buff=0.35)`, placing the label top at pixel ≈47 < safe-zone top 54. Fixed to `buff=0.5`.

3. **Overlapping semi-transparent MUTE circles** — B20 had two MUTE circles at `fill_opacity=0.7`. Where they overlapped, blended pixels fell within the MUTE ink mask, creating a ≈19px detected blob (plus a 2.11:1 contrast failure). Fix: `fill_opacity=1.0` — fully-opaque circles have w/h≈1.0 < 1.5 and are filtered as text runs.

4. **B24 note overflow (GATE-V)** — At sz=32, the 50-char all-caps note line exceeded the 1728px safe-zone width. At sz=28 (≈35px, passing the 34px floor) the line fits. Also, `title = caps("THE SECOND LIMIT", sz=20)` (missed in the first pass) was promoted to sz=32.

---

## Build-time geometry guard

`assert_no_overlap(*mobs, tol=0.02, scene="")` was added to all Manim scenes. It fires before the raster gate can be fooled by fused blobs: two fully-overlapping MUTE runs collapse to one detected blob, making the bbox-overlap check see only 1 run and return PASS despite a real collision. The assertion catches this at render time.

---

## §8.6c fused-run heuristic (type_check.py)

`check_bbox_overlap` now appends an ADVISORY note when any text run height is > 1.8× the median run height in the same frame — signalling a potential fused blob. Advisory only; does not change PASS/FAIL.

---

## STOP — waiting for Bear

Slate cut is ready. `art final` / `art post` / TOPOST / publish are Bear's call.
