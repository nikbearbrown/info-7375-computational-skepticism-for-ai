# BUILD-PROMPT — tldr-the-boundary-scaling-cannot-cross

**What this is.** A `tldr` film (Liam in for Bear, Claude skin, single LEARN section on the 3Blue1Brown template, pure Manim) of chapter 13 §"Three categorical limits" from INFO 7375 Computational Skepticism for AI. Section S1 of `youtube/tldr-sections-13-limits-of-ai.md`.

**Why.** More data moves the edge of a sample; it never removes it. The film teaches the chapter's complementarity argument on Taleb's turkey and Figure 13.1's nested regions (rebuilt from the caption).

**How to rebuild (from `books/`).**

```bash
R=info-7375-computational-skepticism-for-ai/youtube/tldr-the-boundary-scaling-cannot-cross
python3 $R/make_sheet.py                                          # 17 beats → beat_sheet.json (numbers asserted)
python3 brutalist.art/runtime/scripts/bookend_check.py $R         # GATE BOOKEND
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R # Liam am_onyx — measured mp3s are the clock
ffmpeg -y -i $R/mp3/beat-BOUT.mp3 -af apad=pad_dur=1.0 $R/mp3/beat-BOUT.pad.mp3 && mv $R/mp3/beat-BOUT.pad.mp3 $R/mp3/beat-BOUT.mp3
python3 $R/lock_cards.py                                          # actual_duration_s, card durations, B00/B01 cues on the clauses (re-run after ANY make_sheet.py)
rm -f $R/manim/*.mp4
./brutalist.art/art run   $R --height 2160                        # Gate F/L/A/W → Manim 4K → Gate B → Remotion → review compile → Gate V
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape   # GATE T pre-flight + clean master
```

(Only pad BOUT once: if the mp3 is already padded, skip the ffmpeg line.) Then LOOK at frames: B00/B01 at ~50% and ~90% (lines land on their clauses), B02 at ~90% (the correction on screen), B16 at ~95% (the event outside the stretched sample). Fix at the source, never by hand-timing. To stage: `python3 brutalist.art/runtime/scripts/stage_publish.py $R && python3 $R/build_srt.py && ./brutalist.art/art post $R --no-topaz` — the full-text SRT before post, always.

**Rules that shaped it.** tldr spine (WHAT → WHY → QUESTION → TERMS → LEARN → your-turn). Pedagogy gates. Pure Manim in the lesson; transform-don't-cut via the `_Stage` state factory. Course credit spoken in B00. The composite clinic captioned on screen. OUTRO-LOCK.

**Stop line.** Cut the master, send it to Bear. Do not stage or publish without his word.
