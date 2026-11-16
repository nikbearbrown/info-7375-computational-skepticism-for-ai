# PLAN — deep-explainer · "Two Models, Twice the Price"

*Plan gate deliverable. No audio, no spend. Approve / adjust before beats are written.*

## Framing (locked this turn)
**Skeptic's case study.** Not "Model A beats Model B, here are the numbers." The episode
is a durable field guide: *how to read an AI model-comparison table without getting played*,
using the pasted routing doc as the specimen on the table. Per the skill's DOUBLE-CHECK /
strip-datable law and rule 5 (never inherit an unverified source's confidence):

- **Mechanisms stay** (they're timeless): per-token vs per-task cost, figure contamination,
  fallback/harness scoring, effort mismatch, compliance-before-capability.
- **Specific numbers → labeled illustrations.** No on-screen "43.3% vs 33.7%" as fact. Any
  bar/curve is captioned *illustrative*. The doc's own UNKNOWN/UNSOURCED tags become a
  teaching point, not something to launder into confidence.
- **Model names compressed.** "the premium model / the cheaper model," "a safeguarded
  public model vs an unrestricted twin" — no "Opus 5 / Fable 5 / Mythos 5," which would
  date the film in weeks and can't be verified anyway.
- **Note flagged for you:** the pasted source is actually *two* stitched analyses with
  small internal disagreements (e.g. FrontierBench Fable 33.7 vs 33.8; second half adds
  SWE-bench Pro / AA-Briefcase). The case-study framing dissolves this — we teach the
  traps, not the rows — so no reconciliation needed.

## Where it lands (confirm at gate)
- **Book:** `computational-skepticism-for-ai`  →  `youtube/`
- **Slug:** `claude-liam-two-models-twice-the-price`
- **Title:** *Two Models, Twice the Price* — *reading an AI comparison table without getting played*
- **Channel:** claude-liam (Liam in for Bear, Kokoro `am_onyx`, free). ElevenLabs only if you say so.

## Spine
```
B00 cold open (ClaudeComposerAsk — Liam brings the table, ask answered, Liam signs in)
  ACT I    The table wants to fool you        (setup: the naive read)
  ACT II   Trap 1 — the headline isn't pure   (figure contamination)
  ACT III  Trap 2 — you're scoring a system   (fallback / harness)
  ACT IV   Trap 3 — unmatched effort          (the compute confound)
  ACT V    The reframe — price isn't cost      (per-token vs per-task)  ← the verdict-flipper
  ACT VI   The trap capability can't fix       (compliance before capability)
  ACT VII  How to trust the analysis           (a source that shows its seams)
VERDICT recap (ClaudeVerdictArtifact — the reusable lens)
YOUR TURN (ClaudeComposerAsk — a paste-ready table-interrogation prompt, read aloud)
TITLE re-read outro (ClaudeTitleOutro — title + @NikBearBrown + seeded mascot)
```

## Act map — body beats (lane · gist ~25–35 words final)
Cold open + closing block are exempt from the mix count.

| # | Act | Lane | Beat gist | shot |
|--|--|--|--|--|
| 1 | I | CARD | Act card: "The Table Wants to Fool You" | segment card |
| 2 | I | **VOX** | printed two-column comparison, a pen circling the "winning" rows `[run R1]` | STILL · kenburns |
| 3 | I | **VOX** | pull out to the price row — one model twice the other `[R1]` | STILL · kenburns |
| 4 | I | REMOTION | the naive read: higher price = better? count the win-rows? two tempting inferences | C2 |
| 5 | I | MANIM | the scoreboard the table invites — 5 win / 3 / 1 tie tally | isotype |
| 6 | I | REMOTION | thesis: a comparison table is a rhetorical object, not a neutral one | C3 |
| 7 | II | CARD | Act card: "Trap 1 — The Headline Isn't Pure" | segment card |
| 8 | II | REMOTION | the headline column shows the *higher of two variants* — public vs unrestricted twin | C3 |
| 9 | II | **VOX** | glossy launch chart; terracotta ring draws onto a starred row | STILL · drawon |
| 10 | II | MANIM | the footnote reveal: "this row = the other variant" — the contamination tell | state card |
| 11 | II | REMOTION | generalize: a column that blends variants isn't the number you can buy | C2 |
| 12 | III | REMOTION | Act spark-line: "Trap 2 — You're Scoring a System" | segment (spark) |
| 13 | III | REMOTION | routing diagram — flagged prompt reroutes to a fallback; the "model" wraps two | C3 |
| 14 | III | **VOX** | server racks, slow push in `[run R2]` | STILL · kenburns |
| 15 | III | **VOX** | pan to one lit node — "part of the score came from here, not the model under test" `[R2]` | STILL · kenburns |
| 16 | III | MANIM | score = f(model, harness, fallback); the harness term lights up | equation tangent |
| 17 | III | REMOTION | production ≠ benchmark — reroute rules differ by surface and by date | C2 |
| 18 | IV | REMOTION | Act spark-line: "Trap 3 — Unmatched Effort" | segment (spark) |
| 19 | IV | MANIM | two dials at different settings — compute budgets unmatched | state card |
| 20 | IV | MANIM | the non-monotonic curve — score vs compute rises, then dips | equation tangent |
| 21 | IV | REMOTION | "UNKNOWN effort" is the honest label; an unlabeled effort column is the warning | C2 |
| 22 | IV | **VOX** | a spec sheet with the effort field blank; ring draws around the gap | STILL · drawon |
| 23 | V | CARD | Act card: "The Reframe — Price Isn't Cost" | segment card |
| 24 | V | REMOTION | per-token price tag vs per-task receipt — two different numbers | C3 |
| 25 | V | MANIM | build the formula: cost/task = price × tokens ÷ pass-rate (× retries) | equation tangent |
| 26 | V | MANIM | *illustrative* bars — cheaper-per-token + higher pass-rate → lower cost/task, and the inverse | bar (labeled illustrative) |
| 27 | V | **VOX** | a long itemized receipt beside a single price sticker `[run R3]` | STILL · kenburns |
| 28 | V | **VOX** | pan down the receipt — retries, verbosity, re-runs adding up `[R3]` | STILL · kenburns |
| 29 | V | REMOTION | the flip: the per-token winner can be the per-task loser | C2 |
| 30 | VI | REMOTION | Act spark-line: "The Trap Capability Can't Fix" | segment (spark) |
| 31 | VI | REMOTION | a funnel — compliance (data-retention / privacy) filters *before* capability | C3 |
| 32 | VI | **VOX** | a locked records room / redacted compliance page | STILL · kenburns |
| 33 | VI | MANIM | the gate: "can't deploy it → its benchmark lead is zero" | state card |
| 34 | VII | CARD | Act card: "How to Trust the Analysis" | segment card |
| 35 | VII | REMOTION | the good analysis shows its seams — evidence for AND against, a disconfirming section, an unresolved section, its own UNKNOWN labels | C3 |
| 36 | VII | MANIM | the checklist assembles — the traps + the per-task reframe as one reusable lens | isotype |
| 37 | VII | REMOTION | distrust the seamless table; trust the one that labels what it doesn't know | C2 |

## Lane histogram (mix contract)
Body beats: **37**

```
VOX       ████████████         9  · 24.3%   (target 15–30 → PASS)
MANIM     ████████████         9  · 24.3%   (target 25–40 → slightly light, acceptable)
REMOTION  ████████████████    15  · 40.5%   (target 30–45 → PASS)
CARD      ████                 4  · 10.8%   (remainder — act openers)
```
No lane runs >2 consecutive except inside vox runs (by design). Vox runs: **R1** (2–3),
**R2** (14–15), **R3** (27–28) — all 2-beat, within one act, ≤3, handoff blocks authored
at plan time.

**Estimated duration:** ~37 body beats + bookends ≈ **7–8 min** (measured audio is the only
real clock; this is a planning estimate at ~2.9 w/s).

## Vox-still preview (real Gate D2 comes after audio lock)
All 9 vox stills are **Tier 1 — generic/illustrative** (no named real person or place), so
sourcing burden is low and there's no rights escalation:

1. printed 2-column comparison table + pen  ·  2. same, price row  ·  3. glossy launch chart
·  4. server racks (one plate, reused across R2)  ·  5. spec sheet, effort field blank
·  6. long itemized receipt vs price sticker (one plate across R3)  ·  7. locked records /
redacted compliance page.

That's ~5 distinct plates (two reused across their runs). No Tier 3 person rights to clear.

## Closing block (exempt, but here's the intent)
- **VERDICT recap:** the lens, compressed — 5 traps + the per-task reframe.
- **YOUR TURN (read aloud):** a paste-ready prompt the viewer can point at *any* comparison
  table — "which rows blend variants? which scores came from a harness/fallback, not the
  model? is effort matched? what's the cost per completed task, not per token? does any
  compliance constraint eliminate a model before capability is even discussed? what does the
  source admit it doesn't know?"
- **TITLE re-read:** *Two Models, Twice the Price* + hardcoded `@NikBearBrown` + one seeded
  mascot under the handle (OUTRO-LOCK).

## Next gates (after you approve this plan)
`factcheck` (mark every retained claim verified-or-illustrative; strip datable names) →
GATE P (narration on an animated slate, before any audio spend) → audio lock → Gate D2
shopping list → Gate D1 full-length slate previz for your review.
