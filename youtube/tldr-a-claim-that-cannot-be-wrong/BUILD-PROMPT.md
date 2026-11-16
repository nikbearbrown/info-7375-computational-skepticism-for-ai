# BUILD-PROMPT — tldr-a-claim-that-cannot-be-wrong

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) of chapter 1 §"What I mean by skepticism" — Popper's falsifiability, the rhetorical-claim table and the sepsis model — from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-01-skeptics-toolkit.md`.

**Why.** A claim counts only in the form that names the result that would make it false. The film draws every claim as the region of outcomes it forbids, and lets one external result settle what five favorable checks never could.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-a-claim-that-cannot-be-wrong
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (chapter numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
# card lengths = measured audio; cues scaled proportionally (see BUILD-LOG); BOUT apad 1.0 s, actual_duration_s from ffprobe
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Then LOOK at frames (B00/B01 at ~50% and ~90%; B02 at ~90% — "prove it wrong" on screen; B16 after the drop). Fix at the source, never by hand-timing. To stage (Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim; transform-don't-cut via the `_Stage` factory (one tile, one axis, one region). Course credit spoken in B00. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
