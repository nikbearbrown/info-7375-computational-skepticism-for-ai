# BUILD-PROMPT — show-tell-doubt-what-matters

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (brief `../SHOW-TELL-THREE-MOVES.md`, Film 1): "Radical doubt. Talk about Descartes. Talk about how you can't doubt everything, and add risk to that: you should doubt the things that are important to doubt. You can't doubt everything, but you should doubt what your job depends on — health, important things." A show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md`, rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Greeting: Salaam.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-doubt-what-matters
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# audio-only respellings live in narration_text: "Day-cart" (Kokoro reads "Descartes" as "discards") and
# "INFO seventy-three seventy-five"; build_srt.py maps both back for the captions. Whisper-check (medium.en) every beat.
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to
# actual_duration_s and re-run make_sheet.py (it carries them forward and sets BDEFS props.durationSeconds).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Facts: everything attributed to Descartes is checked against his own texts in `sources/` (Meditations 1641, Latin + Veitch; Discourse 1637 Part III, Veitch; Principles 1644 Part I, Veitch). The question "what would have to be true for this to be wrong?" is the course's adaptation of his move, and risk-weighted doubt is Bear's rule, not Descartes'; the narration keeps both attributions. The chapter file has uncommitted edits: read it, never edit or stage it.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
