# BUILD-PROMPT — tldr-hold-one-fair

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, one LEARN section on the 3Blue1Brown template, pure Manim) of chapter 7 §"The arithmetic — the actual proof, not a gesture" from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-07-fairness-metrics.md`.

**Why.** When base rates differ, a flag cannot mean the same in both groups while the mistakes land evenly. The film shows it on the chapter's two tables: the flagged pile is the world's widths times the model's heights, so pinning one test breaks the other.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-hold-one-fair
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # B00/B01/B03 durationSeconds + cues on the clauses; BOUT from ffprobe
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Re-running `make_sheet.py` wipes `actual_duration_s`; always re-run `lock_cards.py` after it. Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90%; B02 at ~90% for the correction; B17/B18 equations). Fix at the source. To stage (Bear's word only): `stage_publish.py` → `build_srt.py` → `art post --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory (`to(cfg)` moves every object between the chapter's tables). Course credit spoken in B00. OUTRO-LOCK. CHOICE side only (the chapter-6 film owns COMPAS).

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
