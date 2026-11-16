# BUILD-PROMPT — show-tell-the-slice-you-can-see

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-27 (in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-KANT.md`): "Show and tell video, Liam persona, on Immanuel Kant, and how we need some humility in our perspective. … Phenomena (the world as it appears to a mind structured by space, time, and causal categories) vs. noumena (the thing-in-itself, forever inaccessible). Gravity as something inferred from effects rather than directly seen is almost a textbook Kantian example … Kant's response to 'will tools ever close the gap' is a flat no … That's a stronger claim than mine; I think the gap is contingent-but-permanent (finite minds, expanding tools, asymptotic) … we only see a slice of the universe. And we should be aware not only of what we can't see, but that there are things we can't see." A show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md`, rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo beside the three "moves" films, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "You Only See a Slice"; greeting Hallo.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-the-slice-you-can-see
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# the generator re-voices EVERY beat on each run: re-pad BOUT afterwards (use --only <BID> for single re-voices).
# audio-only respellings live in narration_text: "Kahnt" (plain "Kant" voices as "can't"), "Noomenna" (plain "noumena"
# voices "now-MEE-na"; "Noomena" stresses the middle), "Proleg-omena", and "INFO seventy-three seventy-five";
# build_srt.py maps each back. Whisper-check (medium.en) every beat. Pad BOUT with 1.0 s of silence (keep the unpadded
# mp3 in _superseded/), write ffprobe durations back to actual_duration_s, then re-run make_sheet.py (it carries them
# and sets BDEFS props.durationSeconds).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (a header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-a-test-that-cant-fail/scenes.py` with its end slack `_END = 0.15`, and this film's scenes); edit it in place now. `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Kant is quoted verbatim only from public-domain translations, both fetched raw into `sources/`: Meiklejohn's 1855 *Critique of Pure Reason* (B xxvi, "while we surrender the power of cognizing, we still reserve the power of thinking objects, as things in themselves"; A43/B60, "we should not thereby advance one step nearer to a knowledge of the constitution of objects as things in themselves") and Carus's 1902 *Prolegomena* (Preface, "the suggestion of David Hume was the very thing, which many years ago first interrupted my dogmatic slumber"). Everything else Kant holds is reported speech with the A/B page in FACTCHECK. Bear's "asymptotic" view is attributed to Bear aloud ("This is Bear's view, not Kant's") and on screen ("Bear's view"), never to Kant. No portrait of Kant or Hume: objects only.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
