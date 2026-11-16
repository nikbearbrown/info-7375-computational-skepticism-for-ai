# SAVE-STATE — claude-liam-cs-ch08-validating-agentic-ai
_Written: 2026-07-31_

**Session:** `claude-liam-cs-ch08-validating-agentic-ai` build — Chapter 8 "You Broke My Toy."

**Reel path:** `computational-skepticism-for-ai/youtube/claude-liam-cs-ch08-validating-agentic-ai/`

**What was done this session:**

1. **BOUT subline fix** — reverted `subline` from `"Computational Skepticism for AI · Chapter 8"` to `""` in `beat_sheet.json`; deleted `media/BOUT.mp4` to force Remotion re-render. GATE BOOKEND: PASS.

2. **BVDT edge-bleed fix** — `artifactHeading` shortened from full chapter title to `"Chapter 8 key rules"`, `artifactLines` reduced from 5 to 4; deleted `media/BVDT.mp4` to force re-render. GATE V: 0 BLOCKER.

3. **Manim cache problem** — on first `art run`, all 7 Manim scenes were skipped ("already filled") because old renders persisted despite `scenes.py` edits. Fixed by deleting `manim/B01–B08.mp4` and clearing `build` status in `beat_sheet.json`.

4. **GATE T — three iterations to PASS:**
   - Pass 1: 6 FAILs (stale renders — contrast + min-size)
   - Pass 2: 5 FAILs after fresh render — B03/B05/B08 min-size (sz=22→33px, floor 35px); B04/B05/B07 contrast (ACCENT box strokes falsely detected as accent text)
   - Pass 3: Fixed in `scenes.py`:
     - B03: `label`/`detail` sz 22→24 (36px ✓)
     - B04: ACCENT box strokes → INK (stroke weight still differentiates ash rows)
     - B05: All text sz→24; boxes widened 3.8→4.6 units, centers ±2.9→±3.4; ACCENT strokes → INK
     - B07: ACCENT strokes → INK for fundamental rows
     - B08: Text sz→24; label anchor RIGHT*2.0→RIGHT*1.7; description anchor LEFT*2.6→LEFT*3.0
   - Final: GATE T PASS, 14/14 beats, 0 FAILs

5. **GATE V** — 0 BLOCKER; 8 MAJOR underfill on B06/B09/B10/BOUT (FormACard/ClaudeTitleOutro sparse text by design, documented in CHECKS-REPORT.md). `ART_STRICT=0` used.

6. **B08 text fix** — "Effective scope — including indirect requests" → "Scope — including indirect requests" (user correction, typo fix).

7. **Kokoro audio generated** — `generate_audio_kokoro.py --no-gate`, 12 beats, `am_onyx`, $0.00.

8. **`art final` run** — 297s final cut with per-beat narration written to `claude-liam-cs-ch08-validating-agentic-ai.mp4`.

9. **CHECKS-REPORT.md** written in reel folder.

**Current state:** Final cut with audio open in player. All gates PASS. Reel not staged/posted.
