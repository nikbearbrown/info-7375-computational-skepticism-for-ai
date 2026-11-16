# BUILD-PROMPT — show-tell-induction-until-it-changes

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-THREE-MOVES.md`): "Make individual show-tell films on radical doubt, induction and falsifiability … **Induction.** Talk about induction and Hume … if the state of the system changes … then its history is no longer likely to hold up. Don't say induction isn't useful. It's very useful. When induction doesn't hold up, it's because the system has changed: we've had COVID …". This is Film 2 of that brief: a show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md`, rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "Induction Works Until the World Changes"; greeting Konnichiwa.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-induction-until-it-changes
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# audio-only respellings live in narration_text: "Konnee-cheewa" (plain "Konnichiwa" comes out "Kaneshua") and
# "INFO seventy-three seventy-five"; build_srt.py maps both back for the captions. Whisper-check (medium.en) every beat.
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), write ffprobe durations back to
# actual_duration_s, then re-run make_sheet.py (it carries them and sets BDEFS props.durationSeconds).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (the header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-skepticism-is-a-method/scenes.py`, and this film's scenes); edit it in place now. `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

The chapter file has uncommitted edits: read it, never edit or stage it. The COVID number comes from the Census release of August 18, 2020 (11.8 → 16.1 percent) and the revised series (11.9 → 16.3); the film says "about twelve … about sixteen". "Stationary" describes the quarterly steps, not the rising share. "Ergodic" is said once as a definition and once as the shops picture.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
