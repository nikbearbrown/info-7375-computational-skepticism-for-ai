# SAVE-STATE — 2026-07-27 (updated 20:35)

## BATCH COMPILE V2 — Current State

**All 124 reels reset to NEW-RULE. Batch running unattended.**

### Steps completed

1. **GATE BANNED-CARD** — `brutalist-art/runtime/qc/banned_card_check.py` created + wired into run.sh. Blockers: BC-1 SlateCard, BC-2 ClaudeWindow artifact body, BC-3 banned prop keys, BC-4 OutroSeries/OutroCTA. ART_STRICT=0 → warns, never blocks.

2. **BEAT SHEET FIX** — `fix_cs_new_rules.py` ran on all 124: SlateCard→FormACard, ClaudeWindow artifact body→FormACard, bookends added to cs-* reels. Backups: `beat_sheet.json.bak-newrules`.

3. **VOX-* BC-4 FIX** (2026-07-27) — `fix_vox_bc4.py` ran on 19 vox-* reels. 17 OutroSeries beats replaced with FormACard placeholder `["OUTRO — BC-4", "needs new bookend", "(OutroSeries → BVDT)"]`. MISSES.md written. 2 reels (bias-pipe, calibration-curve) already clean.

4. **STALE MP4 DELETED** — ~85 old-rule renders deleted across cs-* + vox-* reels.

5. **BATCH COMPILE V2** — PID 91533, running since 18:45. Log: `BATCH-COMPILE-V2.log`. Settings: ART_FACTS=0 ART_STRICT=0.

### Batch script corrections
- ~~vox-* skip line~~ REMOVED — all 19 vox-* reels now in batch
- ~~pre-compile banned_card gate that skipped reels on exit 2~~ REMOVED — style gates warn-only

### Slates ready to watch (as of 20:35)
All in `computational-skepticism-for-ai/youtube/claude-liam-*/`:
- bd-01-meet-gru-and-v0, bd-02-build-the-sdd, bd-03-boondoggle-score, bd-04-reflection-and-ship
- bnb-01-build-and-suspect, bnb-02-loop-and-calibration, bnb-03-robustness-and-data-frame, bnb-04-values-and-honesty, bnb-05-the-confession, bnb-06-assemble-and-ship
- bs-01-pick-and-scope, bs-02-five-component-spec, bs-03-adapt-and-justify

### Next after batch completes
1. Check BATCH-COMPILE-V2.log for FAILs; fix root causes
2. For 17 vox-* reels with placeholder OUTRO: run REFACTOR skill → proper BVDT/BHTF/BOUT
3. Bear reviews slate cuts → feedback

---

# ORIGINAL SAVE-STATE (2026-07-27 earlier session)

## Primary Request and Intent

The user asked to rebuild all `claude-liam-*` reels in `books/computational-skepticism-for-ai/youtube/` under a locked design system. Full original spec (verbatim):

**SCOPE:** Every `claude-liam-*` subdir with a beat_sheet.json (124 total). Skip non-`claude-liam-*` (nbb-*, bare vox-*/cli-*), `_to_delete/`, and loose scripts/logs.

**STAGING:** PILOT FIRST — 8 reels spanning types (cs-*, deep-*, cli-*, vox-*, bd-/cb-/ra-). Rebuild, compile SILENT slates, STOP for review. After approval, continue in batches of ~15.

**GATES:** GATE P — SILENT slate only, no audio spend. Money rule: stop before any paid action. NEVER publish.

**REPORT after pilot:** per-reel one-line beat→form summary, NEEDED ICONS list (deduped), any STOPPED reel with reason, overall light/dark polarity balance. Then wait for go.

## Key Technical Concepts

- **GATE B (Manim layout audit)**: `brutalist-art/runtime/qc/manim_layout_audit.py` renders scene classes, captures snapshots at each `wait`/`play-end`, checks for: (1) text off-frame, (2) text outside safe area (±6.3x, ±3.4y warns), (3) text-on-text overlap, (4) text centerline struck by a line/curve segment. **Strict mode blocks on both errors AND warnings.**
- **`_struck()` function**: Checks if any stroke segment crosses the text's horizontal OR vertical centerline (each inset 0.15 world units from edges). This is exact segment intersection, no pixel tolerance.
- **Stroke detection**: `_collect_strokes()` collects all non-text leaf VMobjects where `get_stroke_opacity() > 0.02` — critically this checks **opacity** not `stroke_width`, so `stroke_width=0` objects still contribute if default stroke_opacity is >0.
- **`_qc_intentional = True`**: Escape hatch attribute that exempts a mobject's subtree from being included in the stroke list. Used for structural containers (bucket rects), thematic tracks (acc_line/base_line in B05), and annotation connectors (arrows).
- **`self.remove()` timing**: `self.remove(mob)` removes instantly (no animation). A frame captured immediately after (by the next `play` or `wait`) will not see the mobject.
- **GATE B strict mode**: Despite failure message saying "layout errors," it also blocks on warnings — any non-zero warning count blocks.
- **Safe area**: ±6.3x / ±3.4y. Text outside this gets WARN. Text outside ±7.12x / ±4.05y (frame bounds) gets ERROR "off-frame."
- **`beat_sheet.json`**: Pipeline source of truth; only this file is read.
- **Kokoro voice**: Free/local. `voice_kokoro` field (not `voice`) in beat_sheet.json beats.

## Files Modified This Session

- **`books/computational-skepticism-for-ai/youtube/claude-liam-cs-01-base-rate-trap/scenes.py`**
  — 10 Manim scene classes (B01–B12), all GATE B CLEAN. Fixes: eyebrow buffs → 0.8 throughout; B02 scale_lbl shown/removed before grid; B04/B07 bucket rects + crimson bars + tp_dots marked `_qc_intentional`; B05 acc_line/base_line/arrow marked `_qc_intentional`; B07 legend labels repositioned from off-frame x=-6.5 to row at y=2.5; B08 strike `_qc_intentional` + correct_lbl moved to x=-3.8; B09/B12 queue bars marked `_qc_intentional`; B10 old_bg + strike marked `_qc_intentional`.

- **`books/computational-skepticism-for-ai/youtube/claude-liam-chinese-room/scenes.py`**
  — A16_CombinatoricsWall: `overflow_arrow._qc_intentional = True`, `lbl_b` moved to `[-5.0, row_b_y, 0]`. GATE B CLEAN.

- **`books/computational-skepticism-for-ai/youtube/claude-liam-vox-bias-pipe/scenes.py`**
  — NEW FILE. 9 stub Manim scene classes (B02_ThreeTeams through B12_ExampleLending). All GATE B CLEAN.

## Current State

**GATE B status — pilot 8 reels:**
- cs-01: ✓ ALL 10 scenes CLEAN
- chinese-room: ✓ A16 CLEAN
- cli-adversarial: N/A (pure Remotion, no Manim)
- vox-bias-pipe: ✓ ALL 9 stubs CLEAN
- bd-01: N/A (no Manim classes, has audio)
- ra-01: N/A (no Manim classes, has audio)
- cb-01: BLOCKED (no audio, no scenes.py)
- deep-01: BLOCKED (no audio, no scenes.py)

**Pilot report delivered.** User approved with "go" on 2026-07-27.

## Pending Tasks

1. Compile silent slates for 4 ready reels: cs-01, chinese-room, cli-adversarial, vox-bias-pipe
2. Assess bd-01 and ra-01 visual fills
3. Note cb-01 and deep-01 as BLOCKED (no audio)
4. Proceed to batch 1 (~15 reels) after pilot compilation review
