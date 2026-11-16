# BUILD-PROMPT — claude-liam-molecules-are-data

Paste this into Claude Code (`claude --dangerously-skip-permissions`) from `books/`.
It builds the full review cut end-to-end after Bear approves the beat sheet (GATE P).

---

```
You are building the review cut for:
  books/computational-skepticism-for-ai/youtube/claude-liam-molecules-are-data/

REEL="computational-skepticism-for-ai/youtube/claude-liam-molecules-are-data"

## GATE P check (human must confirm before proceeding past this point)
Read beat_sheet.json. Print each beat's narration_text in order.
STOP and ask Bear to confirm before generating any audio.

## Step 1 — generate Kokoro audio (free; no ElevenLabs spend)
cd books
python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py "$REEL"

## Step 2 — render Manim beats
# B03: single 5-FU molecule
cd "$REEL/manim"
MOLECULE_NAME=fluorouracil manim -qk --fps 24 molecule_scene.py MoleculeScene
cp media/videos/molecule_scene/*/MoleculeScene.mp4 ../media/B03.mp4

# B06: twenty-molecule gallery
manim -qk --fps 24 molecule_scene.py MoleculeGallery
cp media/videos/molecule_scene/*/MoleculeGallery.mp4 ../media/B06.mp4

## Step 3 — render Remotion beats (B00, B01, B02, B04, B05, B07, B08, B09)
cd books
python3 brutalist-art/runtime/scripts/remotion_scenes.py "$REEL"

## Step 4 — compile review cut
python3 brutalist-art/runtime/scripts/compile.py "$REEL"

## Step 5 — Visual QC (frame-level audit, mandatory)
# Sample frames at 2 fps + each beat at 15/50/85% of its span
ffmpeg -i "$REEL/mp4/claude-liam-molecules-are-data.mp4" -vf fps=2 "$REEL/_qc/frames/%05d.png"
# Read the PNGs. Audit 9-point rubric (edge bleed, title-safe, overflow,
# collision, offscreen, legibility, brand bug, aspect, canvas fill).
# Log defects and fixes in "$REEL/_qc/REPORT.md".

## Step 6 — CHECKS-REPORT.md (write this, then STOP)
Write "$REEL/CHECKS-REPORT.md" with:
- Gate P status (confirmed / pending)
- Manim render status for B03 and B06 (rendered / error)
- Remotion render status per beat
- Compile status
- Visual QC summary (PASS / FAIL per rubric point)
- Any BLOCKER or MAJOR defects found
STOP. Do not run art final, art post, or upload anything.
Bear reviews the slate cut and CHECKS-REPORT.md.
```

---

## Manim rendering notes

Both scenes in `manim/molecule_scene.py` fetch from PubChem on first run and
cache results in `manim/.mol_cache/`. Re-runs are fast (no network call).

If a molecule fails to resolve (unusual name or transient network error), the
gallery shows a text placeholder for that cell — log it in BUILD-LOG.md.

Render commands from inside `$REEL/manim/`:
```bash
# Single molecule (any name):
MOLECULE_NAME="caffeine" manim -qk --fps 24 molecule_scene.py MoleculeScene

# Gallery:
manim -qk --fps 24 molecule_scene.py MoleculeGallery
```

Output lands in `manim/media/videos/molecule_scene/<quality>/`.
Copy the mp4 to `$REEL/media/B03.mp4` (or B06.mp4) before running compile.py.
