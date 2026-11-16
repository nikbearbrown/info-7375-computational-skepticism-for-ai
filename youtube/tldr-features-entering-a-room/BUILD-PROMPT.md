# BUILD-PROMPT — tldr-features-entering-a-room

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 5 §"The mathematics of Shapley values" + §"A worked example" (Figures 5.2–5.4) from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-05-explainability.md`.

**Why.** "How much did this feature contribute?" has a different answer in every room the feature walks into. The film fills the chapter's six-ordering table, averages it, and shows the three averages fill the gap exactly — then names it.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-features-entering-a-room
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # actual_duration_s (BOUT via ffprobe), B00/B01/B03 durationSeconds, cues on the clauses
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Re-run `lock_cards.py` after ANY `make_sheet.py` run (make_sheet resets the measured values). Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90%; B02 at ~90% — the correction must be on screen). Fix at the source, never by hand-timing. To stage (on Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates (two tangents for two landed equations). Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory. Course credit spoken in B00. Constructed example captioned. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
