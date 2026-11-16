# BUILD-LOG.md — claude-liam-a-p-value-is-not-a-verdict

## 2026-08-13 — GATE B20 RESOLVED; B20 and B21 rewritten (Bear approved)

### Finding: figures ARE in the paper

A human opened arXiv:2306.04634 HTML (the Kirchenbauer et al. ICLR 2024
"reliability" paper) and searched it. The addendum's cited figures appear
**verbatim in the abstract**:

> *"ROC-AUC remains above 0.85 when T=200 tokens are available, and above 0.9
> with T=600 tokens."*

Also in Section 4.1: *"by the 600 token mark, under the GPT and Dipper
model-based attacks, the watermark recovers to an AUC greater than 0.9."*

The addendum's citation is accurate. FACTCHECK.md's initial finding was wrong.
The research pass hit the exact failure mode the film is about: primed queries
confirmed absence; the neutral-framed query returned uncertainty; a human
resolved it by going to the abstract.

### Beat rewrites (Bear approved: Option 1 — most honest, most powerful)

**B20 redesigned** — `B20_TheCheckThatCorrectedItself` (was `B20_TheNumberThatIsntThere`):
- New narration: the reel's own factcheck initially marking figures absent, the
  query divergence signalling the conflict, a human opening the abstract, the
  correction made before shipping. The addendum was right; the factcheck was not
  — until someone went and looked.
- Visual: two query paths diverge (PRIMED → ABSENT, NEUTRAL → UNCERTAIN in
  terracotta); OPEN ABSTRACT drops; figures resolve SOLID in ink; ABSENT card
  strikes through to PRESENT.
- No longer an accusation. Demonstrates the thesis on the reel itself.

**B21 revised** — narration and show block:
- New narration: "Which is the thesis, caught in this reel's own production…"
  Three exhibits recalled: alarm grid (B11, stays terracotta — the systemic
  inference failure), retraction heading (B19, resolves ink), factcheck
  correction (B20, resolves ink). Two corrections sorted from one failure.
- DeckPattern note updated to name the reel's own process, not the brief's.

### What changed across files

- `beat_sheet.json`: metadata `purpose`, `source`, `color_semantics`, `gate_note`,
  `note`; B20 beat (narration, show block, scene_class, mechanic, note);
  B21 beat (narration, show block, DeckPattern note, motion_claim).
- `FACTCHECK.md`: headline updated; B20 gate section replaced with resolution.
- `BUILD-LOG.md`: this entry.

### Structural note: why this ending is stronger

The original B20 accused a source. This B20 demonstrates the thesis on the
film's own production process, which is a harder and more honest move: the
reel built around epistemic failure caught itself doing it, corrected before
shipping, and shows the correction on screen. The ending now closes with two
examples of the right process (source corrects itself; film corrects itself)
bracketing the one ongoing failure (institutional inference without checking
the base rate). The thesis lands on the film's own behaviour, not someone else's.

---

## 2026-08-13 — PLAN authored (Gate 1 pending human approval)

**Skill:** `deep-explainer` · **Channel:** `claude-liam`, Kokoro `am_onyx`, free.
**Book:** `computational-skepticism-for-ai/`. **Greeting:** `Jambo, Liam.` (Swahili
— rotated; Sawubona and Vanakkam are spent on recent reels).

### Lane mix — PASS

```
MANIM     ████████   8   40.0%
REMOTION  ███████    7   35.0%
VOX       █████      5   25.0%   ← dead centre of the 20–25% target
```

No run exceeds 2 consecutive same-lane beats. Estimated **6:55**, inside the band
with no padding.

### ZERO GEN-AI PUNTS — by construction

Every VOX still is a real published artifact:

| Beat | Still | Tier |
|---|---|---|
| B05 | Dathathri et al., *Nature* 634 (2024) — first page | 2 |
| B08 | EU Code of Practice — the free-form-text token threshold | 2 |
| B13 | Liang et al., *Patterns* (2023) — the TOEFL result | 2 |
| B16 | Jovanović et al., ICML 2024 — watermark stealing, first page | 2 |
| B19 | the source brief's own addendum, retraction visible | 1 (author's own text) |

Each carries a written GRAPHIC/own fallback scene in
`shot.vox.shopping.fallback`. **No stock photograph is requested anywhere in this
sheet.** This is the first reel authored under the corrected tier-1 rule: a beat
with no specific real referent is a drawn beat, not a shopping-list entry.

### Deviation logged: no vox runs

The genre's vox-run continuity contract is unused. All five stills are document
annotations — `drawon`/`annotate`, the plate holds and the terracotta pen moves.
Chaining Ken Burns across five unrelated papers would be decoration, which
SHOW-DON'T-TELL bans more strongly than the genre asks for continuity. B19 is the
only Ken Burns beat and it stands alone.

### Structural decision: Act I contains no criticism

Four beats and roughly 65 seconds establish that the mechanism works exactly as
published — the γ-partition and δ-boost, the one-proportion z-test, the fact that
SynthID is a categorically *different* family (tournament sampling, non-distortionary),
and the 20-million-response live validation. A reel that strawmans the thing it
audits has no standing to audit it. This act is not padding and should not be cut
for runtime.

### The film corrects its own source three times, on camera

1. **B07** — the *original brief's* "one paraphrase defeats it" is drawn as a
   switch and struck through. The addendum's replacement figures failed
   factcheck, so the beat uses Krishna et al.'s real number: **100% → 57.2%** at
   1% FPR.
2. **B15** — the brief's "independent verification is structurally impossible" is
   drawn as a wall, two doors open in it (public-key, ZKP), and it relabels to
   **UNBUILT**.
3. **B17** — the jurisdiction map: four of five chips visibly dim as their actual
   duties are read. For text with a machine-readable duty the list is one entry.

### ⚠ GATE B20 — VERIFY BEFORE RENDER

B20 states that the addendum's citation of *"AUC above ~0.85 at 200 tokens, above
~0.9 at 600 tokens"* does not appear in Kirchenbauer et al., *On the Reliability
of Watermarks* (arXiv:2306.04634 / ICLR 2024).

Checked against arXiv v1, current arXiv, ICLR 2024 proceedings, and a repository
deposit — absent from all four. **But the research pass hit exactly the failure
mode this film is about:** queries primed with the numbers returned
confirmations; the one neutrally-framed query did not. Held at PLAUSIBLE, not
CONFIRMED.

**A human opens the PDF and searches it before B20 renders.** Figures present →
B20 is cut and Act V rebuilds around the California retraction alone. This is
step zero of BUILD-PROMPT.md, not step nine — three beats change if it flips, and
it's cheaper to know before audio.

### Claims cut or corrected at factcheck

Nine failed or needed narrowing; full table in `FACTCHECK.md`. The four that
matter most: **γ=0.25 not 0.5**; **99.9% and "held two years" are WSJ reporting,
not OpenAI statements** (kept off screen entirely); **China requires a visible
label plus metadata, not a watermark**; **the EU/California date match is
characterised in neither direction** because no legislative record states a
rationale.

The brief's "nobody validates semantic equivalence" is too strong — Fu et al.
(AAAI 2024) exists. The narrow surviving gap (no *local causal counterfactual
audit*) is logged in FACTCHECK.md for the description rather than made a beat; it
needs a caveat paragraph a 15-second beat can't carry.

### Layout law applied from the start

Authored after the Simon's Ant post-mortem. Every `production_viz.mechanic`
describes relative layout; the build prompt forbids hardcoded `move_to` and
requires a bbox-overlap assertion at the end of every `construct()`. If that
helper doesn't exist in the toolkit yet, this reel writes it.

### MISSING / blocked

- `SHOPPING.md` not written — Gate D2 forbids it before audio lock.
- Nothing compiled, rendered, or voiced. This plan was authored in a cloud
  session with no access to the render toolchain. Execution is `BUILD-PROMPT.md`,
  run locally.
- `BVDT` has five `artifactLines`; confirm `ClaudeVerdictArtifact` handles five
  without overflow, or merge lines 2 and 3.

## 2026-08-30 — HUMAN FEEDBACK (Bear): text on top of text (TOPOST review)

B15_WallWithDoors: "PUBLIC-KEY VERIFICATION", "UNBUILT", and "ZERO-KNOWLEDGE
PROOF" overprinted — size-30 labels wider than their 2.6u doors spilled onto
the wall label, and the scene's check_overlaps() omitted the door labels, so
the gate never saw it. Fixed: doors 3.4u, labels size 24, labels added to the
overlap check. Re-rendered, recompiled (369.5s, GATE AUDIO PASS), frame
verified, re-staged to TOPOST.
