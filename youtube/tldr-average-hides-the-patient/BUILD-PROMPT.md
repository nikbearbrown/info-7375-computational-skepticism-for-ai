# BUILD-PROMPT — tldr-average-hides-the-patient

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) of chapter 11 of INFO 7375 Computational Skepticism for AI, §"Subgroup calibration: where aggregate metrics lie". It is section S2 of `youtube/tldr-sections-11-communicating-uncertainty.md`.

**Why.** A global calibration error weighs patients. Ninety-five rare-disease patients out of 12,955 are under 1% of that weight, so their 0.103 can never move the global 0.018 by even a hundredth. Give the group its own denominator and the hidden row stands up.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-average-hides-the-patient
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx; the measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # actual_duration_s, card durationSeconds, B00/B01 cues on clauses (re-run after any make_sheet.py)
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

After a scene edit: delete `$R/manim/<B>.mp4`, and delete `$R/media/videos/scenes/2160p24/partial_movie_files` in its own `rm -rf` with no globs. Then LOOK at frames: `_qc/`, `qc-sheet.png`, B00/B01 at ~50% and ~90%, and B02 at ~90% (the correction must be on screen). To stage (on Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.**
- tldr spine: WHAT → WHY → QUESTION → TERMS → LEARN → your-turn.
- The pedagogy gates.
- Pure Manim in the lesson. Transform-don't-cut via the `_Stage` state factory (`mode` = one / equal / patients; `heights`).
- The course credit is spoken in B00.
- OUTRO-LOCK.

**Stop line.** Cut the master and send it to Bear. Do not stage or publish without his word.
