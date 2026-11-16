# BUILD-PROMPT — tldr-five-boxes-one-deployment

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 12 §"The five accountability requirements…" from INFO 7375 Computational Skepticism for AI, with Application A2 as the key case and SyRI as the real instance. Section S5 of `youtube/tldr-sections-12-accountability.md`.

**Why.** A deployment paragraph that mentions an appeal and a review team reads like accountability; the chapter's five verification tests show it passes none. The film makes the viewer file the words, then run the tests.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-five-boxes-one-deployment
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (counts asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_audio.py                                          # actual_duration_s, card durations, B00/B01 cues on the clauses (re-run after any make_sheet.py)
rm -f $R/manim/*.mp4                                              # only for scenes you changed; clear media/videos/scenes/2160p24/partial_movie_files too
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90% so lines land on their clauses; B02 at ~90% so the correction is on screen). Fix at the source, never by hand-timing. To stage (Bear's word only): `python3 brutalist.art/runtime/scripts/stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Board` state factory. Course credit spoken in B00. The tier taxonomy (`[verify]`) stays out. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
