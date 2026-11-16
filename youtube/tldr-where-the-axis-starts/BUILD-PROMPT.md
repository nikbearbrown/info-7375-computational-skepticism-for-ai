# BUILD-PROMPT — tldr-where-the-axis-starts

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) of chapter 10 of INFO 7375 Computational Skepticism for AI — the truncated axis, on the chapter's Exercise 1. Section S4 of `youtube/tldr-sections-10-visualization.md`.

**Why.** A bar's height is its value minus the axis floor, so the floor — a setting the chart-maker (or the AI) picks — decides the ratio the reader sees. Same two numbers: ×3 on a 91 floor, ×1.02 on zero, ×23 on 92.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-where-the-axis-starts
python3 $R/make_sheet.py                                           # 17 beats → beat_sheet.json (ratios asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R  # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                           # actual_duration_s, card durations, B00/B01 cues on the clauses
rm -f $R/manim/*.mp4 $R/media/*.mp4
./brutalist.art/art run   $R --height 2160                         # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape    # GATE T pre-flight + clean master
```

`lock_cards.py` must be re-run after every `make_sheet.py` (the sheet generator does not know the measured durations). Then LOOK at frames (`_qc/`, `qc-sheet.png`; B17/B18 formulas at their revealed states; B00/B01 at ~50% and ~90%; B02 at ~90% for the correction). To stage, on Bear's word only: `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim; transform-don't-cut via the `_Chart` state factory (every scene rebuilds the same two bars at the previous beat's floor; B12/B16 move only the floor). Exercise 1 captioned constructed. Course credit spoken in B00. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
