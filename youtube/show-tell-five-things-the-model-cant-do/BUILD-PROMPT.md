# BUILD-PROMPT — show-tell-five-things-the-model-cant-do

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-FIVE-CAPACITIES.md`): "Look at the latest show tell skills to make sure you have the latest changes and updates in it. Make a show tell film on the five supervisory capacities." (He dictated "supervisee"; the chapter's term is *supervisory*.) The source is the chapter's section "The Five Supervisory Capacities" (`chapters/01-the-skeptics-toolkit.md`, lines 152–180, read only, copied verbatim to `SOURCE.md`). This is a show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md` as modified 2026-09-27 20:59, with `ShowTellCard.tsx` at 21:03; rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "Five Things the Model Can't Do for Itself"; greeting Ciao.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-five-things-the-model-cant-do
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# The generator re-voices EVERY beat on a full run and drops BOUT's pad: after any full run, re-pad BOUT with a 1.0 s
# silent tail (keep the unpadded mp3 in _superseded/), write ffprobe durations back to actual_duration_s and
# mp3/timings.json, then re-run make_sheet.py (it carries them and sets BDEFS props.durationSeconds).
# For a single beat use --only <BID> (this build re-voiced B03..B09 that way after the Law 9 split; BOUT's pad survived).
# Audio-only respellings: "INFO seventy-three seventy-five" and "five percent" (build_srt.py maps them back to "INFO 7375"
# and "5%"). Whisper-check (faster-whisper medium.en) every beat.
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (a header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-cheap-to-make-dear-to-check/scenes.py` with its end slack `_END = 0.15`, and this film's scenes); edit it in place now. Before the first 4K run, pre-audit every scene: Gate A (`runtime/qc/static_scene_check.py`) from a scratch folder holding ONLY `scenes.py`, and the layout audit (`runtime/qc/manim_layout_audit.py --curve-strict`) in the reel folder, then move the audit's `media/` cache to `_superseded/`. Render low-res stills (30/50/97%) and look at them before anything at 4K; then a 1080p render with the local GATE T / Gate V pre-check (`type_check` at the midpoint, `final_frame_check.analyze_frame` at 25–99%). `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

The chapter file has uncommitted edits: read it, never edit or stage it. Every example and number is the chapter's own, attributed aloud; the one number on screen (5%) is captioned "the chapter's example"; the 0.7 confidence example and the table's chapter column are not used. No ShowTellCard: every body beat fails the card test (see `SHOTLIST.md`, "why a card"). Cast, whole film: model block, output slip, supervisor peg (terracotta badge), the patient on a chair as the world, five kraft tiles that return as five plinths.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
