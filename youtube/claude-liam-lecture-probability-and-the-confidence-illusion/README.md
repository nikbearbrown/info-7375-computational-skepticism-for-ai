# Probability and the Confidence Illusion — Lecture 2 of 13, INFO 7375 Computational Skepticism for AI

## Executive summary
**What this is.** One whole-chapter lecture film (lecture skill, Liam in for Bear, Kokoro `am_onyx`, greeting "Hola", channel @NikBearBrown): why a confident number is not a correct number. Ten acts, 66 body beats: probability as degree of belief, conditioning and the chain rule, the 99%-accurate test and Bayes' theorem, rare events and alert fatigue, outputs as conditional claims and distribution shift (Hume), calibration and temperature scaling, heavy tails, and four closing questions.
**Why.** It is the second film of the course's lecture series, one film per chapter. The source chapter is Chapter 2 (updated version, HEAD side of its six merge blocks); the deck folder held only a skeleton, used for section order.
**What was found.** The chapter has errors, all corrected in the film and recorded in FACTCHECK.md: the Casscells study's "most answered 95%" (it was a plurality of 27 of 60, with 11 correct), the DeGrave et al. mechanism (shortcut learning, not pre-2020 imaging drift), the "0.4–0.6" interval hit rate, the reason the triage flag lowers the estimate, the sepsis alert rate (of hospitalizations, not patients), and a posterior printed two ways (1/101 versus 1/102). Every worked number is computed by a script and shown from its output (`evidence/`). Nothing is staged or published.

## Files (all in this folder)
- `beat_sheet.json`, `make_sheet.py`, `beats_data.py` — the sheet and its sources
- `ACTS.md` — coverage map, cast per act, SOURCE CONFLICTS, DECK vs CHAPTER, LEFT OUT
- `SHOTLIST.md`, `CHECKS-REPORT.md`, `FACTCHECK.md`, `SOURCES.md`, `PROMPTS.md`, `BUILD-PROMPT.md`, `BUILD-LOG.md`, `RESUME.md`
- `scenes.py` — one Manim scene per body beat and act title
- `evidence/` — `evidence.py`, `bayes_run.py`, their stdout, `calib.json`, `series.json` (seeded)
- `mp3/`, `media/`, `manim/`, `opening/`, `exports/landscape/` — audio, clips, opening card, the master
- `build_srt.py`, `pad_audio.py`, `whisper_check.py`, `WHISPER-CHECK.md`

## Reading it
Professor Bear's phrase "plausibility auditing" (hearing the wrong note in a number before you can prove it wrong) is his and is attributed as such in the film's sentence defining it. The simulated calibration and Cauchy runs say "our simulation" on screen; constructed examples say "constructed" or "made-up".
sha256 c4fc5a63acd058226696c5377d1c24c2138e93abd59a926e98bd91a5adfc6c21
