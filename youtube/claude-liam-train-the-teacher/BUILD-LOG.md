# BUILD-LOG — claude-liam-train-the-teacher

Deep-explainer · @NikBearBrown · Liam in for Bear (Kokoro `am_onyx`) ·
Teardown register · 16:9 · built 2026-09-07.

---

## The decision that shaped the film

The human supplied two documents: an essay, and an adversarial audit of that
essay. The obvious film is the essay's argument. **That is not the film I
built.**

The essay's own thesis — the binding constraint is teacher capability — is
sound, and the audit says so. But a film of just the essay would have to repeat
five sentences the audit demonstrates are wrong, including the statistic the
essay opens on. Building that film would mean shipping known errors into a
channel whose whole register is teardown.

So the film's subject is the **pair**: an argument published, then audited, and
what survived. That framing does three things a straight explainer could not.
It lets every corrected number appear on screen as a correction rather than as
a fact. It makes the film's method identical to its subject. And it turns the
audit's least comfortable finding — that the central claim is a bet rather than
a finding — into the film's third act instead of a footnote nobody reads.

The essay comes out of this better, not worse. That is stated in the verdict.

---

## VOX LAW — why there is no pantry

Zero vox beats, and no `SHOPPING.md`.

The evidence in this story is statutes, cost tables and effect sizes. There is
no photograph that IS any of it. Under the VOX LAW added to
`skills/make/explainer/SKILL.md` on 2026-09-02, a still here could only be
atmosphere, and atmosphere is exactly what that law removed. Zero is the correct
outcome, not a skipped step — the skill says so in its own hard rule 1.

Consequence: **Gate D2 does not apply, and every beat renders.** There is no
slate in this cut anywhere.

---

## The PPT TEST, and why eight new components exist

Standing feedback on the two previous films in this register:

> "Every single frame is a slate cut ... your basic instructions are to render
> EVERY frame you can with sound .... no frames were renders"

Mechanically those beats were real renders. The substantive complaint was
correct anyway: they read as slides. A typographic system was built and called
illustration.

The fix here was to make motion load-bearing. Before authoring, GATE L was run
against the 536-scene library for each visual need. Ten components were library
hits and are reused. Eight needs were genuine misses, and each miss was turned
into a component whose animation carries the claim — not a component that
decorates a claim.

The design rule is written into the file header:

> If a beat here would survive as a PowerPoint slide, it is in the wrong
> component.

The per-component justification table is in `CHECKS-REPORT.md`. The short
version: a lag, an arrest, a strike sweeping through a word, a meter that
refuses to move, a bar shrinking in place, a camera pulling back to reveal a
denominator, and rows dissolving one at a time — none of these has a still.

New components live in `brutalist.art/runtime/remotion/src/TrainTeacher.tsx`,
registered in `Root.tsx` under the folder `TrainTeacher`, and indexed by
`./art scene-index` so the next reel finds them.

---

## GATE F — four defects caught before audio spend

Factchecking my own narration before generating audio found four problems. All
four were the same failure mode, which is the failure mode this film is about:
**a number on screen that the source does not state.**

1. **B18 `TtScaleDecay`** printed `0.31` → `0.11` SD. The audit documents that
   larger effectiveness studies produce smaller effects; it publishes no pooled
   effect per scale tier. I had invented two plausible figures and written
   "illustrative" in a footnote. That is the exact move the film spends five
   beats criticising.
   **Fix:** added `showValue: boolean` and `qualitative: string[]` to the
   component. The bar still shrinks; it now reads "larger" → "smaller"; the
   on-screen note says the source gives direction, not a number.

2. **B19 `TtNullResult`** printed `+58` for the teacher-knowledge meter. The
   source says knowledge improved, not by how much.
   **Fix:** added `showValues: boolean`, set false. The meter fills; the
   numeral is gone.

3. **B31 `TtNullResult`** printed `+42` on both sides of a *hypothetical*
   result. A number on a thought experiment is worse than a number on a study.
   **Fix:** same flag.

4. **B27 narration** conflated two different TALIS survey items — "70% of
   non-AI-users lack the knowledge" with "67% cite other responsibilities / 59%
   cite scheduling", which are barriers to *professional learning*, a separate
   question. The original line ("two of the three barriers are not about
   knowing") was a clean, wrong sentence.
   **Fix:** narration and chart labels now name the two questions separately.
   The point survives — buy the hours as well as the content — and is now true.

One inference is **flagged rather than fixed**: B24 asserts that almost no
trials of AI-specific teacher PD measured on student outcomes exist. The audit
does not print that sentence; it reclassifies the thesis as a recommendation
rather than a proven formula, proposes the missing trial, and rules every
supporting study to be about something adjacent. The film states the implication
those three moves carry, and constrains it on screen: "Not a claim that
training fails. A claim that nobody has run the study." Recorded in
`FACTCHECK.md` row 20.

---

## Verification boundary — stated, not implied

The audit's primary sources were **not** independently opened. This session's
knowledge cutoff precedes most of them, and the audit itself records several as
retrieved indirectly (the Figlio & Özek figures come from the authors' own
Education Next account; the NBER original could not be retrieved).

The film therefore inherits the audit's confidence, and it inherits the audit's
stated limits with it — which is why the reel never states a number of states,
and why B10 puts "the 3.5 million observation count — could not confirm" on
screen instead of quietly dropping it.

This is written out in full at the top of `FACTCHECK.md`. For a film whose
subject is citation discipline, an unstated verification boundary would be a
defect on its own terms.

---

## MISSING — toolkit gaps hit during this build

**`MISSING: runtime/models/kokoro/*` in the public cut.** The free default audio
engine had no model files in `brutalist.art`. `./setup --install` is documented
to fetch them (~330MB), so this is expected for a fresh clone rather than a bug
— but it means the DOT tree could not generate audio as it stood. Resolved for
this build by symlinking the sandbox's copies; both patterns are already
gitignored (`runtime/models/kokoro/*.onnx`, `*.bin`), so nothing enters the
public repo.

**`MISSING: scripts/type_check.py` — GATE T has no implementation here.** The
deep-explainer SKILL.md hard rule 7 says GATE T "ALWAYS RUN", and seven
documents in this tree assert it as mandatory. Neither `type_check.py` nor the
`kerning` skill was ever ported into `brutalist.art`. GATE T could not run.

This is not a silent pass. Type QC for this reel is a manual frame read against
`_qc/`, recorded below after the compile. The toolkit gap stands and is the
human's call: port `type_check.py` + `skills/make/kerning/`, or strike the GATE
T claims from the seven documents that make them. Leaving both — a mandatory
gate with no implementation — is the worst of the three options, because it
reads as passing.

Prior evidence that this matters: GATE T caught five real type defects on the
riff film that Gate V passed clean.

---

## Duration

Planning estimate 10:10 at 2.9 words/sec plus a 0.9s per-beat pad — top of the
5–10 minute band, and over it if the estimate holds. Per `duration-planner`
doctrine, duration is an output: the measured mp3s are the only clock, and the
arc is five genuine acts. The measured total is recorded below. If it lands
above 10:00 the trim candidates, in order, are B10 (scope ledger, folds into
B09's note) and B27 (the TALIS barriers beat).

---

## Build steps run

| Step | Status |
|---|---|
| GATE L — library search per visual need | ✓ 10 hits reused, 8 punts built |
| Components authored + `tsc --noEmit` | ✓ clean |
| Registered in `Root.tsx`, `./art scene-index` | ✓ 618 renderable |
| `./art scenes --check` on all 18 components | ✓ all RENDERABLE |
| Beat sheet authored, 35 beats | ✓ |
| Consecutive-scheme lint | ✓ clean |
| GATE F — `FACTCHECK.md` | ✓ PASS, 4 defects fixed, 1 inference flagged |
| `CHECKS-REPORT.md` written before the compile | ✓ |
| Audio — Kokoro `am_onyx`, all 35 beats | see below |
| Compile | see below |
| Gate V — frame read | see below |
| GATE T | ✗ no implementation (above) |

---

## Compile record

Thirteen compile passes. The film was watchable after pass 2; passes 3–13 were
gate work, and every one of them found something a frame read or a gate caught
that the previous pass had not.

| Pass | What changed | Result |
|---|---|---|
| 1–2 | first full render; 4 component defects found by reading frames | watchable cut sent to Bear |
| 3–4 | GATE F (new in run.sh mid-session) needed SHOTLIST.md + PROMPTS.md | written, both real documents |
| 5–8 | GATE T §8.5/§8.9/§8.3/§8.1 — 16 FAILs -> 1 | see below |
| 9–12 | §8.1 chase; two checker patches tried and reverted | see "What I got wrong" |
| 13 | correction body type floor raised to 52px | **GATE T PASS** |

**Final gate state**

```
GATE F   PASS   FACTCHECK.md · SHOTLIST.md · PROMPTS.md
GATE L   PASS   beat-mix lint clean
GATE T   PASS   0 FAILs across §8.1 §8.2 §8.3 §8.3b §8.4 §8.5 §8.6b §8.13
GATE V   0 BLOCKER · 16 MAJOR (all `underfill`)
AUDIO    PASS   mean_volume -23.7 dB
LANE     PASS   35 beats, no violations, known_slates=[]
```

The 16 Gate V majors are accepted, not hidden: 12 are the five act cards and the
hesitant-writer overview, which are sparse by design (an act card is a breath);
3 are `TtCorrection` sampled at its 50% mark, before the correction card drops —
the 85% frames pass; 1 is `ReqDefinitionDrop` at 43% against a 55% floor. For
comparison, the two previously shipped reels in this register carry 10 and 20.

**Defects the gates did NOT catch — found by reading frames**

1. `ReqBars` appends a hardcoded `%`, so Kraft's **0.49 SD** rendered as "49%"
   and a **4 percentage-point** gain as "4%". Wrong units, on screen, in a film
   about wrong numbers. Built `TtEffectBars`, which takes the printed value as a
   verbatim string and scales bars to the data max.
2. `TtCorrection`'s strike-through never drew: an absolutely-positioned child of
   a *wrapping* inline span has no usable containing block, so `width: N%`
   resolved to nothing — on the beat whose entire point is the strike.
3. Raising the note to 50px (for §8.1) put it through B04's axis labels. §8.6b
   bbox-overlap reported 0 FAILs.
4. The review master carried burn-in (`B13 REMOTION VIDEO 192.6s`). Caught by
   sampling the bottom sixth before staging; the clean master is verified clean.

**What I got wrong**

- I told Bear `ART_STRICT=0` would let `./art final` run. It does not — the
  public cut's `compile.py` calls the Gate V checker unconditionally with no
  lenient flag. Corrected in-session.
- Bear chose "fix the §8.1 checker". I tried twice — a short-word filter, then a
  line-merge from raw glyph blobs — and the second made things worse (my reel
  1 -> 11 FAILs, by merging punctuation into wide short "lines"). Both reverted;
  `type_check.py` is byte-identical to how I found it. The diagnosis was right
  (at 4K, serif letters touch in pairs, and a pair with no ascender is pure
  x-height ~40px against a 41px floor); the fix was not, and I stopped rather
  than keep patching a shared checker.
- The eventual fix was on the merits: raise the correction body type to a 52px
  floor. That is the film's payload text and it was the smallest body type on
  screen, so it should have been larger anyway.

**Publish**

```
staged   books/youtube/TOPOST/  — master + .md + .srt, staged.json entry
master   3840x2160 · 514.1s · 35 MB · all 35 beats natively 2160 (none upscaled)
video    https://www.youtube.com/watch?v=4WdtEp7uhOs   (unlisted)
playlist Computational Skepticism (found, not created)
captions 146 cues, all 1,679 narration words
```

`stage_publish.py` overwrote the caption track with its own 35-cue version whose
first cue ends mid-sentence ("...and where the"). Regenerated before staging.
That truncation defect is live in the dignity reel's shipped SRT.

Topaz 8K variant complete: `claude-liam-train-the-teacher-topaz.mp4`,
7680x4320 HEVC, 2.7 GB, model `prob-3`, decodes clean. Recorded in
`staged.json` under `files.topaz_8k`.
