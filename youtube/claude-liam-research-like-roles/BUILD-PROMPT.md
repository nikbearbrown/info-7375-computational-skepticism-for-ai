# BUILD-PROMPT — claude-liam-research-like-roles
**Gate D2 → Final cut**  
**Date:** 2026-07-24 | Use after reviewing slate previz and supplying pantry stills.

---

## Status going in

- Slate previz: `claude-liam-research-like-roles-slate.mp4` (386.8s / 6:27) — REVIEWED
- 23/28 slots filled · 5/28 SLATE (B02, B03, B08, B11, B15 need pantry stills)
- QC: 0 BLOCKER · 0 MAJOR · 1 MINOR open (B21 slow-mo for final)
- Audio: locked — do NOT regenerate unless narration is edited

---

## Step 1 — Supply pantry stills (human task)

Generate 5 images with your preferred AI image tool (Midjourney, Flux, DALL-E).  
Specs from SHOPPING.md:

| File | Size | Prompt |
|------|------|--------|
| pantry/B02.png | 2000×1200 | Abstract wall of job listings / posting cards on screens, blurred, cool office light, no readable text |
| pantry/B03.png | 2000×1200 | Small team 2–3 people at workstations, one pointing at screen, warm ambient light, no identifiable faces |
| pantry/B08.png | 1800×1200 | Two researchers at a table, each reviewing an annotation/coding sheet with checkboxes, close crop on hands and sheets, neutral light |
| pantry/B11.png | 1800×1200 | Close crop of a single job posting on a monitor or phone, text visible as dense paragraphs (no specific company logos), cool screen glow |
| pantry/B15.png | 2000×1200 | Stylized/illustrative small research team in a minimal lab — blackboard, vintage desk, no computers, warm sepia or desaturated palette, 2–3 people |

Drop each file into the `pantry/` directory with the exact filename.

---

## Step 2 — Fix B21 slow-mo (Claude task)

Before final compile, extend `B21_FakeTrendChart` in `manim/scenes.py` to ~16s:
- Add a trend-line draw phase AFTER the CI bands appear (~6s of animation)
- Hold the final state for 3–4s

Then re-render:
```
cd manim/ && python3 -m manim scenes.py B21_FakeTrendChart -ql --disable_caching
cp media/videos/scenes/1080p30/B21_FakeTrendChart.mp4 B21.mp4
```

---

## Step 3 — Final compile (Claude task)

```bash
python3 runtime/scripts/compile.py \
  /Users/bear/Documents/CoWork/bear-textbooks/books/computational-skepticism-for-ai/youtube/claude-liam-research-like-roles
```
(No `--review` flag — final cut mode.)

Expected output: `claude-liam-research-like-roles.mp4` (all 28 slots VIDEO/MANIM, no slates)

---

## Step 4 — QC the final cut

1. Check `_qc/` frames — all 5 formerly-SLATE beats should now show pantry still + kenburns/drawon motion
2. Confirm B02 slow push-in, B03 drift left-to-right, B08 push toward annotation sheets, B11 drawon ring, B15 push toward blackboard
3. Confirm B21 no longer shows extreme slow-mo warning in compile output

---

## Step 5 — Stage for upload (human task, when ready)

Run the `post` skill to stage the final cut:
```
cd /Users/bear/Downloads/brutalist.art-main
./art post /path/to/reel
```
This stages the hi-res master to `books/youtube/TOPOST/` per HARD GLOBAL RULE.  
Human uploads from TOPOST — never from the reel directory directly.

---

## Notes
- Voice: am_onyx (Kokoro) — Liam persona
- Channel: @NikBearBrown / Computational Skepticism for AI
- Listing: UNLISTED until human flips public
