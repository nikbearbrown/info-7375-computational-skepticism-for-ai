# CHECKS-REPORT — claude-liam-consent-to-publish-is-not-consent-to-be-scored

Written **before** the Gate D1 previz compile, per the PROOF GATE.

```
32 SHOW / 0 justified-HOLD-without-artifact / 0 PUNT-flagged
(7 of the 32 are HOLD-class vox beats — each names a real pantry artifact in
 shot.visual_intent and is tier-tagged in SHOPPING.md, so none is a bare CARD)

Teaching arc:
  FRAMEWORK           ✓  B09 (Nowak three-pronged) and B14 (Art. 6(1)(f) three gates)
                         are both drawn BEFORE they are applied
  WORKED EXAMPLE      ✓  B10 applies the Nowak test prong by prong to this feature
  FALSIFIABILITY      ✓  B12 (needle held mid-scale), B20 (the film limits its own
                         strongest argument), B25 (NOT_DETERMINABLE stamp),
                         B27 (names what would change the answer)
  SCAFFOLDED TASK     ✓  BHTF — four named things to look for, not "go read the policy"
  BOOKENDS            ✓  B00 cold open · BVDT verdict · BHTF your turn · BOUT outro
  NO-SOURCE-NO-VERDICT ✓ B25 labels the missing evidence as missing rather than
                         inferring from it; BVDT asserts nothing beyond FACTCHECK.md
```

## Lane mix (linted)

| Lane | Count | Share | Band | Result |
|---|---|---|---|---|
| VOX | 7 | 21.9% | 15–30% pass | ✓ |
| MANIM | 10 | 31.3% | 25–40% | ✓ |
| REMOTION | 10 | 31.3% | 30–45% | ✓ |
| CARD | 5 | 15.6% | remainder | ✓ |

**Body beats: 32.** No run of 3+ consecutive same-lane beats. Two deliberate 2-beat
vox runs (R1 = B03–B04, R2 = B22–B23); neither crosses an act boundary; max run
length 3 respected.

## Duration

**457 s ≈ 7:37** — inside the genre's 5–10 min band, and an output of the five-act
arc rather than a target. Body beats run 7–14 s; bookends are exempt and run 8–30 s.
Estimated at ~2.9 words/sec. **The measured Kokoro audio is the only clock that counts** —
these numbers are planning figures and will be replaced on generation.

## Component check

Every `remotion.pattern` resolves to a real component in
`runtime/remotion/src/scenes/`, and props were written against the live zod schemas:

`ClaudeComposerAsk` · `ClaudeVerdictArtifact` · `ClaudeTitleOutro` · `DeckPattern`
(`pattern` enum is `divergence | threshold` — both used, nothing invented) ·
`StepStream` (`state` enum `done | active | pending`) · `SpectrumDial` ·
`EvidenceChip` (`tier` enum includes `NOT_DETERMINABLE`) · `ScaleCompare`
(`mode: bars`) · `DecisionFork` · `FlowDiagram` (nodes carry `tier`, edges carry
`kind` from the enum) · `SlateCard`.

**DOODLE-BANNED LAW:** no `DoodleScene`, no `DoodleChart`. ✓

## Open items before the review cut

1. **`SHOPPING.md` B26 constraint** — if no self-published score can be sourced, cut
   B26 and its redistribution point. Vox share drops to 6/31 = 19.4%, still in band.
2. **`FACTCHECK.md` Correction 1** — confirm the 21 vs 26 July opt-out discrepancy on
   the live help page. If it's real, it earns a new beat in Act I.
3. **10 Manim scenes** to author in `scenes.py`: `B06_SharedFloor`,
   `B09_NowakThreePronged`, `B11_Article44`, `B14_ThreeGates`, `B15_GatesTwoThree`,
   `B18_AIActFiftyFour`, `B20_ScopeLimit`, `B24_CausalArchitecture`,
   `B27_EscalationLadder`, `B31_LabelVsFunction`.
4. **TYPECHECK.md** (GATE T, `kerning`) not yet run — required before review cut.
