# BUILD-PROMPT — tldr-where-the-human-steps-fall

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) of chapter 9's worked walkthrough — the Research Paper Summarizer's six-step Boondoggle Score — from INFO 7375 Computational Skepticism for AI. Section S3 of `youtube/tldr-sections-09-delegation-trust.md`.

**Why.** The human steps in an AI pipeline fall where verifying takes judgment and a wrong call reaches a reader — not where the work looks heavy. The film morphs the "looks like work" bars into five-question risk columns and the dark columns land under the human steps.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-where-the-human-steps-fall
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (structure asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # durations from audio (BOUT from ffprobe), B00/B01 cues on the spoken clauses
rm -f $R/manim/*.mp4 $R/media/*.mp4
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Re-run `lock_cards.py` after ANY re-run of `make_sheet.py` (it restores the audio lock). If the BOUT mp3 is regenerated, pad it again before `lock_cards.py`.

Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90% to confirm lines land on their clauses; B02 at ~90% — the correction must be on screen; B16 at ~95% — every column filled, dark columns under the ink boxes). Fix at the source, never by hand-timing. To stage (Bear's word only): `python3 brutalist.art/runtime/scripts/stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory. Course credit spoken in B00. OUTRO-LOCK. Honesty captions: schematic bars, constructed sentence, "our reading" cells, "a heuristic — not validated".

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
