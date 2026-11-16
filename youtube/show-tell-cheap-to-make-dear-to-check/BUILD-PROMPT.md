# BUILD-PROMPT — show-tell-cheap-to-make-dear-to-check

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-SOLVE-VERIFY.md`): "Look at the most recent updates to the show tell skill to make sure you have the most recent instructions for that. Show tell film on the solve-verify asymmetry." The source is the chapter's section "The solve-verify asymmetry" (`chapters/01-the-skeptics-toolkit.md`, read only, copied verbatim to `SOURCE.md`). This is a show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md` as modified 2026-09-27 19:03; rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "Cheap to Make, Dear to Check"; greeting Bonjour.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-cheap-to-make-dear-to-check
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# The generator re-voices EVERY beat on a full run and drops BOUT's pad: after any full run, re-pad BOUT with a 1.0 s
# silent tail (keep the unpadded mp3 in _superseded/), write ffprobe durations back to actual_duration_s and
# mp3/timings.json, then re-run make_sheet.py (it carries them and sets BDEFS props.durationSeconds).
# For a single beat use --only <BID>, which leaves BOUT's pad alone. Audio-only respelling: "INFO seventy-three
# seventy-five" (build_srt.py maps it back to "INFO 7375"). Whisper-check (faster-whisper medium.en) every beat.
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (a header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-a-test-that-cant-fail/scenes.py` with its end slack `_END = 0.15`, and this film's scenes); edit it in place now. Before the first 4K run, pre-audit every scene: Gate A (`runtime/qc/static_scene_check.py`) from a scratch folder holding ONLY `scenes.py`, and the layout audit (`runtime/qc/manim_layout_audit.py --curve-strict`) in the reel folder, then move the audit's `media/` cache to `_superseded/`. `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

The chapter file has uncommitted edits: read it, never edit or stage it. Every cost in the film is the chapter's own framing, spoken as "the chapter's numbers" and never shown as a digit; the drawn bars are labelled illustrative and carry no values. No ShowTellCard: every body beat fails the card test (see `SHOTLIST.md`, "why a card").

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
