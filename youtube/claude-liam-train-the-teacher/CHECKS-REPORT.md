# CHECKS-REPORT — claude-liam-train-the-teacher

Written **before** the previz compile, per the deep-explainer PROOF GATE.

## Per-beat classification

```
30 SHOW  /  5 CARD  /  0 justified-HOLD  /  0 PUNT-flagged
```

- **30 SHOW** — every bookend and every body beat names its on-screen artifact
  in `shot.show` and renders it from a registered composition.
- **5 CARD** — B02, B07, B16, B23, B28. The five act cards. A CARD is the
  correct classification for an act name; none of them carries a factual claim.
- **0 HOLD, 0 PUNT.** No beat is slated, no beat asks the human for media, no
  beat defers.

Verified against the library rather than asserted:

```
./art scenes --check <Name>   → RENDERABLE, 16:9, for all 18 distinct components
```

## Components used

| Component | Beats | Origin |
|---|---|---|
| `ClaudeComposerAsk` | B00, B33 | shared bookend |
| `BrutalistHesitantWriter` | B01 | shared bookend |
| `ClaudeVerdictArtifact` | B32 | shared bookend |
| `ClaudeTitleOutro` | B34 | shared bookend — OUTRO-LOCK, @NikBearBrown only |
| `ReqSegmentCard` | B02, B07, B16, B23, B28 | reused from RequireReport |
| `ReqDefinitionDrop` | B05 | reused |
| `ReqLevers` | B06, B29 | reused |
| `ReqLedger` | B10, B20, B30 | reused |
| `ReqRingWord` | B14, B22, B26 | reused |
| `ReqBars` | B17, B21, B27 | reused |
| `TtTwoAnswers` | B03 | **new** |
| `TtFrontLoaded` | B04 | **new** |
| `TtCorrection` | B09, B11, B13, B15, B25 | **new** |
| `TtDenominator` | B12 | **new** |
| `TtScaleDecay` | B18 | **new** |
| `TtNullResult` | B19, B31 | **new** |
| `TtAbsence` | B24 | **new** |
| `TtVerdictGrid` | B08 | **new** |

Eight new components, ten reused. GATE L was run before authoring: the reused
ten are library hits; the eight new ones are punts turned into design cards and
are now in `scenes.json`, so the next reel finds them.

## PPT TEST — the check this reel exists to pass

The last two films in this register were correctly called out as slideshows.
Every new component here was designed against a single test: **would a still
frame of this beat carry the claim?** If yes, the component is wrong.

| Component | What the motion does that a frame cannot |
|---|---|
| `TtTwoAnswers` | Both answers *travel* toward the question and *arrest* short of it. The gap is created by the movement. |
| `TtFrontLoaded` | The benefit line is given the same screen time as the cost line and visibly does nothing for a year. A lag has no still. |
| `TtCorrection` | A terracotta rule sweeps *through* the wrong span; the span greys as the strike passes. The correction is an event. |
| `TtNullResult` | Both meters are given the identical animation window. One fills, one doesn't. Watching the null happen is the finding. |
| `TtScaleDecay` | The bar shrinks *in place*, leaving a dashed ghost of its starting height, while the scale label ticks up. Attenuation is a direction. |
| `TtDenominator` | The headline starts at 300px and the camera pulls back until the real denominator assembles around it. Either end of that move is one of the two mistakes; the move is the correction. |
| `TtAbsence` | Candidate rows rise, then blur and fall away one at a time as each disqualifier lands. The emptiness has to arrive. |
| `TtVerdictGrid` | Seven rows land in argument order and each takes a stamped verdict behind it. |

Two-consecutive-scheme lint: **clean.** No component appears in three
consecutive beats (checker runs in `author_sheet.py`).

## Teaching arc

```
Teaching arc: FRAMEWORK ✓ | WORKED EXAMPLE ✓ | FALSIFIABILITY ✓
              SCAFFOLDED TASK ✓ | BOOKENDS ✓ | NO-SOURCE-NO-VERDICT ✓
```

- **FRAMEWORK before examples** — B08 decomposes the claim into seven ruled
  sub-claims *before* Act II works any of them. The viewer gets the method
  before the verdicts.
- **WORKED EXAMPLE** — B12 is the full worked correction: the headline, the
  arithmetic, the denominator, the restated claim. B09 is a second, shorter one.
- **FALSIFIABILITY** — B31 is a dedicated beat drawing the result that would
  kill the thesis, and the verdict card (B32) closes on it.
- **SCAFFOLDED TASK** — B33 hands the viewer the audit prompt itself, read in
  full, generalised to "something you published".
- **BOOKENDS** — B00 cold open (ask answered), B01 executive summary, B32
  verdict, B33 your turn, B34 title restate. Five, in order.
- **NO-SOURCE-NO-VERDICT** — every verdict beat names its source on screen.
  B18's note says explicitly that the source documents a direction and not a
  number, and the component prints no number as a result.

## Laws checked

| Law | Status |
|---|---|
| COLD OPEN LAW — B00 is `ClaudeComposerAsk`, ask lands answered | ✓ three output lines |
| EXECUTIVE-SUMMARY LAW — B01 is `BrutalistHesitantWriter`, ≥ 9s floor | ✓ pending measured audio |
| VOX LAW — a still only where the still IS the evidence | ✓ zero vox beats, rationale in `metadata.vox_rationale` |
| ILLUSTRATE LAW — no Claude UI outside bookends | ✓ |
| DOODLE-BANNED | ✓ no Doodle components |
| OUTRO-LOCK — @NikBearBrown, exact title restate, no subline | ✓ B34 |
| IN-FOR-BEAR LAW — Liam says so aloud, twice | ✓ B00, B34 |
| SPARK-LINE LAW | ✓ every illustration beat carries a `spark` |
| Gate D2 (shopping list) | N/A — zero pantry assets |
| GATE F (factcheck) | ✓ PASS — `FACTCHECK.md`, 4 defects fixed pre-audio |
| GATE T (type-lock) | ⚠ **no implementation in this tree** — see BUILD-LOG |

## Outstanding

- **GATE T cannot run here.** `scripts/type_check.py` and the `kerning` skill
  do not exist in `brutalist.art`, while seven documents in this tree assert
  GATE T as mandatory. Type QC for this reel is a manual frame read, recorded in
  `BUILD-LOG.md`. This is a toolkit gap, not a reel gap, and it is not being
  silently passed.
