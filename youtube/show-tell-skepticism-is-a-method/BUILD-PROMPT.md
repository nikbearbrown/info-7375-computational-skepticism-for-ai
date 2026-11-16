# BUILD-PROMPT — show-tell-skepticism-is-a-method

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27: "show tell film Liam persona mention the film is for /Users/bear/Documents/CoWork/bear-textbooks/books/info-7375-computational-skepticism-for-ai" + the pasted section "What I mean by skepticism" (chapter 1). A show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md`, rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N").

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-skepticism-is-a-method
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# audio-only respellings live in narration_text: "Day-cart" (Kokoro reads "Descartes" as "discards") and
# "INFO seventy-three seventy-five"; build_srt.py maps both back for the captions. Whisper-check (medium.en) every beat.
# pad BOUT with 1.0 s of silence (keep the unpadded mp3 in _superseded/), then write ffprobe durations back to
# actual_duration_s and BDEFS props.durationSeconds (re-running make_sheet.py does the latter from the sheet).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

The chapter file has uncommitted edits and an unresolved merge conflict around the Knight Capital paragraph: read it, never edit or stage it. Every external number is checked against the primaries in `sources/` (SEC order 34-70694, Lazer et al. 2014, Wong et al. 2021): the loss is "more than $460 million, per the SEC" (not the chapter's $440M) and the turkey's surprise is on day 1,001.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
