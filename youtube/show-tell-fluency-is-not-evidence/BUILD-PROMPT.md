# BUILD-PROMPT — show-tell-fluency-is-not-evidence

**What this is.** How to rebuild this film from scratch. Run everything from `books/`.

Bear, 2026-09-28 (dictated, in `info-7375-computational-skepticism-for-ai/youtube/SHOW-TELL-FLUENCY-TRAP.md`): "Yes. Show and tell leads to Sonia. On the phone, we trap." Read as: a show-tell film, Liam persona, on the fluency trap. The source is the chapter's section "The fluency trap" (`chapters/01-the-skeptics-toolkit.md`, lines 182–209, read only, copied verbatim to `SOURCE.md`; the file carries uncommitted edits and merge-conflict blocks elsewhere, never edit or stage it). This is a show-tell film (`brutalist.art/skills/make/show-tell/SKILL.md` as modified 2026-09-27 23:41, with `ShowTellCard.tsx` at 21:03; rules from `anthropics/youtube/SHOW-TELL-BATCH.md`), built into the course repo, carrying the INFO 7375 credit (spoken in BIDEA; on screen in the BDEFS title and the BHTF composer topic; never on the outro, never "Lecture N"). Title "The Shape of a Sentence Is Not Evidence"; greeting Hola.

```bash
R=info-7375-computational-skepticism-for-ai/youtube/show-tell-fluency-is-not-evidence
python3 $R/make_sheet.py
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py $R
# The generator re-voices EVERY beat on a full run and drops BOUT's pad: after any full run, re-pad BOUT with a 1.0 s
# silent tail (keep the unpadded mp3 in _superseded/), write ffprobe durations back to actual_duration_s and
# mp3/timings.json, then re-run make_sheet.py (it carries them and sets BDEFS props.durationSeconds).
# For a single beat use --only <BID> (this build re-voiced B14 that way; BOUT's pad survived).
# Audio-only respelling: "INFO seventy-three seventy-five" (build_srt.py maps it back to "INFO 7375").
# Whisper-check (faster-whisper medium.en) every beat; "Descartes" and "Popper" transcribe as homophones
# ("discards", "pauper") while the Kokoro phonemes are right (dᵻskˈɑːɹts, pˈɑːpɚ).
./brutalist.art/art run   $R --height 2160
./brutalist.art/art final $R --height 2160 --out $R/exports/landscape
```

`scenes.py` is assembled from three parts (a header docstring, the ISO KIT + pacing + midpoint guard copied from the sibling `show-tell-five-things-the-model-cant-do/scenes.py` with its end slack `_END = 0.15`, and this film's scenes); edit it in place now. Before the first 4K run, pre-audit every scene: Gate A (`runtime/qc/static_scene_check.py`) from a scratch folder holding ONLY `scenes.py`, and the layout audit (`runtime/qc/manim_layout_audit.py --curve-strict`) in the reel folder, then move the audit's `media/` cache to `_superseded/`. Render low-res stills (30/50/97%) and look at them before anything at 4K; then a 1080p render with the local GATE T / Gate V pre-check (`type_check` at the midpoint, `final_frame_check.analyze_frame` at 25–99%). `art run` renders only scenes whose `manim/<BID>.mp4` is missing: after editing a scene, move its old clip AND `media/videos` to `_superseded/` first. Don't re-run `make_sheet.py` after the final (it drops the build stamps); if you do, re-run `art final`.

Gate A trap met here (SKILL.md, 23:41 text): a scene whose only new non-text shape arrives in its FIRST play fails "shapes never change", because the stub snapshots after each play and ignores text, moves and removals inside a group. Every such scene got a grey ring pulse (`pulse()`: GrowFromCenter in one play, FadeOut in the next; a `Succession` in ONE play does not count, the net membership is unchanged).

Every claim is the chapter's own, attributed aloud; no number is spoken or shown. No ShowTellCard: every body beat fails the card test (see `SHOTLIST.md`, "why a card"). Cast, whole film: the upright page, the reader peg, two gauges, the world block (the account), the model block, and the page as two sheets (form, content) bound by one terracotta dot.

Then STOP. Staging (`art post`, then `python3 <reel>/build_srt.py` after `stage_publish.py` writes the per-beat SRT) and publishing happen only on Bear's word. For the YouTube title/description, use the course strings in `../LECTURE-CREDIT.md` without a lecture number.
