# BUILD-PROMPT — tldr-missing-is-not-one-thing

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 3's missingness paragraph from INFO 7375 Computational Skepticism for AI. Section S2 of `youtube/tldr-sections-03-data-validation.md`.

**Why.** The same 18% blank can be harmless (MCAR), fixable by a visible column (MAR) or invisible from inside the data (MNAR). The film's one representation — sort the matrix rows by a column and watch whether the blanks line up — makes the difference visible, and shows that for MNAR the only column that lines them up is the one never recorded.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-missing-is-not-one-thing
python3 $R/world.py                                               # the constructed table; every relation asserted
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_audio.py      # actual_duration_s (BOUT from ffprobe of the padded mp3), card durationSeconds, B00/B01 cues
# NOTE: make_sheet.py rewrites beat_sheet.json from scratch — ALWAYS re-run lock_audio.py after it
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90%; B02 at ~90% — the correction must be on screen). Fix at the source. To stage (Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim; transform-don't-cut via the `_Matrix` state factory (`sort_to(order)` glides every row). Constructed table captioned on screen; direction only, no dollar figures. Course credit spoken in B00. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
