# BUILD-PROMPT — tldr-both-audits-were-right

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 6 §"The dataset as epistemic artifact" (COMPAS, the 30% / 50% sketch, the identity) from INFO 7375 Computational Skepticism for AI. Section S3 of `youtube/tldr-sections-06-bias-where-it-enters.md`.

**Why.** Two audits of one risk score reached opposite verdicts, and both were right. The film counts a constructed forty people two ways — by score box (Northpointe) and by outcome (ProPublica) — and shows that unequal base rates lock the two apart.

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-both-audits-were-right
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (every rate asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # actual_duration_s (BOUT from ffprobe of the padded mp3); B00/B01/B03 durationSeconds; cues on the spoken clauses
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

Re-run `lock_cards.py` after every `make_sheet.py` (make_sheet rewrites the sheet without measured durations). Then LOOK at frames (`_qc/`, `qc-sheet.png`; B00/B01 at ~50% and ~90% to confirm lines land on their clauses; B02 at ~90% — the correction must be on screen). Fix at the source, never by hand-timing. To stage (on Bear's word only): `stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz`.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory; reveals land on the spoken phrase via `_until()`. Course credit spoken in B00. Constructed population captioned. AUDIT side only — chapter 7's CHOICE-side film is separate. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
