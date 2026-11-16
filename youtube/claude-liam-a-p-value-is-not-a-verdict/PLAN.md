# A P-Value Is Not a Verdict — plan gate

`deep-explainer` · `claude-liam` (Liam in for Bear, Kokoro `am_onyx`, free) ·
built into `computational-skepticism-for-ai/youtube/claude-liam-a-p-value-is-not-a-verdict/`

**Source:** the watermarking research brief **and its own correction addendum**
**Estimated runtime:** 6:55 · 25 beats · 20 body beats · **zero gen-AI punts**
**Greeting:** `Jambo, Liam.` (Swahili)

---

## The act map

| | Act | Beats | What it does |
|---|---|---|---|
| **B00** | cold open | 1 | Two true statements about one detector: wrong 1 in 100,000; wrong 92% of the times it fires. The gap is the film. |
| **B01** | executive summary | 1 | The mechanism works. The failure is one layer up, in what an institution concludes. |
| **I** | **THE MECHANISM IS REAL** | B02–B05 | Green-list boost drawn honestly (γ=0.25, δ=2.0) → the z-test → SynthID is a *different* family (tournament sampling, distribution-preserving) → 20M Gemini responses, thumbs-up differs by 0.01%. **A full act with no criticism in it.** |
| **II** | **WHAT A NEGATIVE DOESN'T SAY** | B06–B09 | The asymmetry fans out → "one paraphrase kills it" struck through, replaced with 100%→57.2% → the 200-token floor, conceded in the EU's own text → metadata ≠ watermark. |
| **B10** | ask micro-beat | 1 | *"How often is a positive correct?"* → **"Depends what you are screening."** |
| **III** | **THE BASE RATE** | B11–B13 | 100 alarms sort into 8 true and 92 false → same instrument, forensics vs screening, ten accused per million pages → and those ten aren't drawn evenly: 61% false-positive rate on non-native English writers. |
| **IV** | **WHO HOLDS THE KEY** | B14–B18 | Symmetric key → the audit questions bounce off the box → the wall is relabelled UNBUILT, not IMPOSSIBLE → $50 buys spoof and scrub → the legal map narrows to one entry → the incentive, drawn without accusing anyone. |
| **V** | **THE BRIEF DID IT TO ITSELF** | B19–B21 | It published a self-correction → and put a number in it that isn't in the paper → which is the thesis, demonstrated on the person arguing it. |
| **BVDT / BHTF / BOUT** | close | 3 | Five-line verdict · a prompt that reads your own institution's policy · title restate. |

---

## Lane histogram (body beats, n = 20)

```
MANIM     ████████        8   40.0%    target 25–40%    PASS
REMOTION  ███████         7   35.0%    target 30–45%    PASS
VOX       █████           5   25.0%    target 20–25%    PASS — dead centre
```

No run of more than 2 consecutive same-lane beats.

**Zero gen-AI punts, by construction.** All five VOX stills are real published
artifacts — the Nature paper, the EU Code of Practice page, the *Patterns* paper,
the ICML watermark-stealing paper, and the brief's own addendum. Every one is
tier 2 (tier 1 only for the author's own document), and every one carries a
written GRAPHIC/own fallback scene. Nothing in this sheet asks a human for a
stock photograph.

**One deviation logged:** there are no vox *runs*. All five stills are document
annotations — the plate holds and the terracotta pen works. Ken Burns runs across
unrelated papers would be decoration, which SHOW-DON'T-TELL bans more strongly
than the genre asks for continuity.

---

## The three decisions worth arguing about

**1. Act I contains no criticism at all.** Four beats, ~65 seconds, spent
establishing that the mechanism works exactly as published — the boost, the
z-test, the fact that SynthID is a *different* family that preserves the
distribution, and the 20-million-response validation. A reel that strawmans the
thing it audits has no standing to audit it. Cutting this act would save a minute
and cost the film its credibility.

**2. The film corrects the brief AND the addendum, on camera, three times.**
B07 draws the "one paraphrase kills it" kill-switch and strikes it through — that
overstatement is in the *original* brief, and the addendum's own replacement
figures are the ones that failed factcheck, so B07 uses Krishna's real number
instead. B15 draws the wall labelled IMPOSSIBLE, opens two doors in it, and
relabels it UNBUILT. B17 dims four of five jurisdictions as their real duties are
read.

**3. The kicker.** The addendum cites two figures from the reliability paper.
They are precise, plausible, correctly formatted — and they don't appear in the
paper. Which is the film's thesis, performed by the person arguing it: a number
becomes evidence when somebody goes and looks.

> **This beat is gated.** It's an accusation, and the research pass that found it
> hit exactly the priming contamination the film is about — primed queries
> confirmed the numbers, the neutral one didn't. A human opens the PDF and
> searches it before B20 renders. If the numbers are there, B20 is cut and Act V
> rebuilds around the California retraction alone. Details in FACTCHECK.md.

---

## What was cut

- **γ=0.5** — wrong. The authors' repo says γ=0.25, δ=2.0. The brief paired a
  theory-section γ with a production δ.
- **"AUC > 0.85 at 200 / > 0.9 at 600"** — used only as the exhibit in B20, never
  as a fact.
- **99.9% and "held for two years"** — *WSJ* reporting from internal documents,
  not OpenAI statements. Only OpenAI's two published reasons are attributed.
- **The "coincidental timing" framing** on the EU/California date match —
  unsupported in both directions. AB 853 moved the date; no record says why. The
  film doesn't characterise it.
- **"China mandates text watermarking"** — false. Visible label plus file
  metadata; watermarks *encouraged*. B17 says exactly that.
- **India as "only proposed"** — stale since February 2026. Cut rather than
  stated wrong.
- **"Nobody validates semantic equivalence"** — too strong; Fu et al. (AAAI 2024)
  exists. The narrow surviving gap is logged in FACTCHECK.md for the description,
  not made a beat.
- **Anthropic's own scheme** — undisclosed, asserted nowhere.

---

## Nothing has been rendered

`BUILD-PROMPT.md` is the paste-ready local run. Six pantry stills → sorry, **five**,
all real documents, all with drawn fallbacks. Steps 1–7 run without them.
