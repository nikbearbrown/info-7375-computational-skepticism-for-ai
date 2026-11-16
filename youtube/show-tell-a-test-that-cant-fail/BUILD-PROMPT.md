# BUILD-PROMPT — show-tell-a-test-that-cant-fail

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-THREE-MOVES.md`): "Make individual show-tell films on radical doubt, induction and falsifiability … **Falsifiability.** Talk about Karl Popper. You need to frame a question beforehand in a way that it can be wrong. If your test always passes, it's not a test. If your agent always succeeds no matter what it does, it's just doing stuff. If we don't design things beforehand so they could be wrong, we're essentially asserting that they'll always work no matter what." This is Film 3 of that brief: a show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md`, rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "A Test That Can't Fail Isn't a Test"; greeting Namaste.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-a-test-that-cant-fail
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# audio-only respellings live in narration_text: "Namastay" (plain "Namaste" phonemizes /nˈæmæst/, last vowel lost) and
# "INFO seventy-three seventy-five"; build_srt.py maps both back (and "Claude three point seven Sonnet" to "Claude 3.7 Sonnet").
# Whisper-check (medium.en) every beat. Pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), write ffprobe
# durations back to actual_duration_s, then re-run make_sheet.py (it carries them and sets BDEFS props.durationSeconds).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (a header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-induction-until-it-changes/scenes.py` with a larger end slack `_END = 0.15`, and this film's scenes); edit it in place now. `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

The chapter file has uncommitted edits: read it, never edit or stage it. Popper is quoted verbatim only twice, from his own English: *LScD* §6 p. 18 and *C&R* ch. 1 n. 3 p. 38 (both local copies in `sources/`); everything else he says is reported speech with the page in FACTCHECK. The eclipse ruler's three ticks come from Dyson, Eddington & Davidson 1920 §1; the film claims only that the expeditions "reported" Einstein's value. The Claude 3.7 Sonnet case is attributed aloud and on screen.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
