# BUILD-PROMPT — claude-liam-train-the-teacher

Paste-ready prompt to rebuild this reel end to end from a clean session.

---

Build a **deep-explainer** on the pair of documents below, into
`info-7375-computational-skepticism-for-ai/youtube/claude-liam-train-the-teacher/`.

**Sources (both required — the film's subject is the pair):**

1. Nik Bear Brown, "Not the App. Not the Ban. Train the Teacher.",
   skepticism.ai, 2026-05-16.
2. The adversarial evidence audit of that essay, 2026-09-07.

**Governing rule: where the essay and the audit disagree, the audit wins, and
the film shows the correction on screen rather than quietly using the corrected
figure.** Do not build a film of the essay alone — it would require repeating
five sentences the audit demonstrates are wrong, including the statistic the
essay opens on.

**Channel and register**

- `@NikBearBrown`, Teardown register (`skills/make/nbb`), Liam in for Bear.
- Kokoro `am_onyx`. Free and local. Never a paid TTS engine.
- IN-FOR-BEAR LAW: Liam says he is standing in for Bear aloud in B00 and B34.
- OUTRO-LOCK: `ClaudeTitleOutro`, exact title restate "Train the Teacher",
  hardcoded handle, slug-seeded mascot, no subline.

**VOX LAW — zero vox beats**

The evidence here is statutes, cost reports and effect sizes. No still IS any of
it. Do not create `pantry/`, do not write `SHOPPING.md`, do not run Gate D2.
Zero is the correct outcome. Every beat renders.

**The PPT TEST is the acceptance criterion**

Before authoring any beat, run GATE L:

```bash
./art scenes "<what the beat needs, in plain words>"
./art scenes --check <ComponentName>
```

A genuine miss is a design card, never a licence to slate. For each new
component, the test is: **would a still frame of this beat carry the claim?** If
yes, the component is wrong. Eight components in
`brutalist.art/runtime/remotion/src/TrainTeacher.tsx` exist because their claims
are movements — a lag, an arrest, a strike sweeping through a word, a meter that
refuses to move, a bar shrinking in place, a camera pulling back to reveal a
denominator, rows dissolving one at a time, verdicts stamping in order.

Register new components in `Root.tsx`, then `./art scene-index`.

**Structure — 35 beats, five acts**

```
B00  cold open        ClaudeComposerAsk — the audit ask, answered
B01  overview         BrutalistHesitantWriter — BLUF, ≥ 9s floor
ACT I    Two Answers, One Question    the argument as published (B02–B06)
ACT II   Then Somebody Audited It     the five corrections (B07–B15)
ACT III  What Survived                coaching, and its limits (B16–B22)
ACT IV   The Hole in the Middle       the missing trial (B23–B27)
ACT V    What Would Settle It         the study design (B28–B31)
B32  verdict          ClaudeVerdictArtifact
B33  your turn        ClaudeComposerAsk — the audit prompt, generalised
B34  outro            ClaudeTitleOutro
```

**Hard authoring rule for this reel specifically**

**Never print a number the source does not state.** This film spends five beats
criticising exactly that. Where a source documents a direction and not a
magnitude, use the `showValue: false` / `showValues: false` flags on
`TtScaleDecay` and `TtNullResult` — the bar still moves, no numeral is
asserted, and the on-screen note says why. Four such defects were caught in the
first draft; see `BUILD-LOG.md` → GATE F.

**State the verification boundary.** The audit's primary sources were not
independently opened. `FACTCHECK.md` must say so at the top, and the film must
carry the audit's own limits forward — never say a number of states, and put
"the 3.5 million observation count — could not confirm" on screen rather than
dropping it.

**Pipeline**

```bash
python3 author_sheet.py                                   # 35 beats
# GATE F — write FACTCHECK.md, fix defects, BEFORE audio
python3 brutalist.art/runtime/scripts/generate_audio_kokoro.py <reel>
# after any full re-author: regenerate ALL audio, never --only
./brutalist.art/art run   <reel>                          # review cut
./brutalist.art/art final <reel>                          # clean master
```

**Never publish.** Master stays in the reel folder. YouTube posting happens only
from `books/youtube/TOPOST/` with a `staged.json` entry, produced by the `post`
skill — and only when the human asks.
