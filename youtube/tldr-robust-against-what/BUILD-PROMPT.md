# BUILD-PROMPT — tldr-robust-against-what

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 4 §"Towards honest robustness disclosure" + Figure 4.5 from INFO 7375 Computational Skepticism for AI. Section S4 of `youtube/tldr-sections-04-robustness.md`.

**Why.** "Robust" is one word standing in for a table. The film fills the chapter's template table row by row and shows the word cannot hold what the rows hold.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-robust-against-what
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (template values asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
python3 $R/lock_cards.py                                          # B00/B01/B03 durationSeconds = measured audio; cues on the spoken clauses
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
#   then set BOUT actual_duration_s = ffprobe of the padded mp3 (art refuses a mismatch)
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90% to confirm lines land on their clauses; B02 at ~90% — the correction must be on screen). Fix at the source, never by hand-timing. To stage (on Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Table` state factory. Course credit spoken in B00. Template values captioned illustrative. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
