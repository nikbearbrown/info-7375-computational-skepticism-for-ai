# BUILD-PROMPT.md — Two Models, Twice the Price

Paste-ready end-to-end build prompt for this reel.

## Reel
`books/computational-skepticism-for-ai/youtube/claude-liam-two-models-twice-the-price/`

## What it is
Deep-explainer in the `claude-liam` channel. Teardown register. 37 body beats, 7 acts. Topic: how to read a model comparison table without getting played (5 traps: headline purity, system score, unmatched effort, per-task cost, compliance gate). All content is mechanism or explicitly-labeled illustration — no specific benchmark numbers appear as facts.

## To build from here

**1. Generate audio (Kokoro, free):**
```bash
cd books && python3 brutalist-art/runtime/scripts/generate_audio_kokoro.py \
  computational-skepticism-for-ai/youtube/claude-liam-two-models-twice-the-price/
```

**2. Render Manim scenes:**
```bash
cd books && ./brutalist-art/art run \
  computational-skepticism-for-ai/youtube/claude-liam-two-models-twice-the-price/ \
  --height 1080
```
(Run.sh will also trigger remotion_scenes.py and compile.)

**3. Review the slate:**
Open `mp4/claude-liam-two-models-twice-the-price-slate.mp4`

**4. Source pantry stills (Gate D2):**
After audio lock, run `pantry_search.py` per vox beat. Check SHOPPING.md for Tier 1 stills to source.

**5. Final cut (after pantry filled):**
```bash
./brutalist-art/art final computational-skepticism-for-ai/youtube/claude-liam-two-models-twice-the-price/
```

## Voice lock
Kokoro `am_onyx`. Not ElevenLabs. Not any other voice.

## Outro lock
ClaudeTitleOutro · title = "Two Models, Twice the Price" · handle = @NikBearBrown (hardcoded) · one seeded mascot · no subline.

## Beat mix (body beats only)
VOX 24.3% (9) · MANIM 24.3% (9) · REMOTION 40.5% (15) · CARD 10.8% (4) · Total 37
