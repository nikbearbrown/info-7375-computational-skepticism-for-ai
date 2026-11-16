# PLAN — claude-liam-a-refusal-is-not-a-verdict

**Title:** A Refusal Is Not a Verdict
**Skill:** `deep-explainer` (ai-explainer chassis) · **Channel:** `claude-liam`, Kokoro `am_onyx`, free
**Reel:** `computational-skepticism-for-ai/youtube/claude-liam-a-refusal-is-not-a-verdict/`
**Register:** Teardown · **Estimated runtime:** 7:00–8:00 · ~42 beats

**Status: plan gate. No `beat_sheet.json` written.**

The title is a deliberate sibling of `claude-liam-a-p-value-is-not-a-verdict`. That is the series and the series is the argument.

---

## The claim

**A refusal is a detector output, not a verdict. So is a compliance.**

Fifth in the arc, and the same shape every time:

| Piece | The instrument | The mistake |
|---|---|---|
| p-value | z-test against a binomial null | reading a probability as a decision |
| watermark | keyed statistical skew | reading processing as authorship |
| type gate | text-height measurement | reading no-detection as clean |
| context engineering | embedding distance | reading retrieval as judgment |
| **this one** | **a safety classifier** | **reading a refusal as a verdict** |

## The two cases

**Case 1 — the false positive with unambiguous ground truth.** Bear wrote prompt-injection tests for a Hetzner server. Claude Code refused to run them, reading them as prompt injections. **They were.** At the token level the classifier was correct; the strings in a prompt-injection test are prompt injections. It was wrong about intent, and intent is not in the tokens. This is the cleanest example in the arc because the detector didn't hallucinate — it fired accurately on a surface feature and something downstream mistook the firing for a decision.

**Case 2 — the refusal that was locally plausible and globally incoherent.** In the session this reel is made from, the model declined to build a walkthrough of a public, CI-tested, MIT-licensed provenance-stripping tool. Three turns earlier, in the same conversation, it had argued that the Claude watermark proves *processing, not authorship*, and that treating it as authorship evidence would reproduce the false-positive fiasco that flagged over half of non-native English speakers' essays. Both positions cannot stand. Bear named the contradiction; the model changed.

**These are different failures and the film must not blur them.** Case 1 is a detector correct on the surface and blind to intent. Case 2 is a judgment that never checked itself against its own prior claims. One is a sensor problem. The other is a consistency problem.

## What Fable 5's fix reveals

The workaround was not an argument that the tests were safe. It **partitioned the context** so the classifier never saw the trigger — instructing the agent not to read the canary folder while doing everything else. That is `isolate`, straight out of write / select / compress / isolate, pointed at a safety classifier instead of an attention budget. **Refusal engineering is context engineering.** It closes the loop with `claude-liam-context-engineering-who-chooses`.

The Teardown judgment on it: that fix works, and it works for the same reason the refusal failed — neither the classifier nor the workaround is reasoning about intent. One partitions tokens, the other fired on tokens. The intent never enters the system at any point.

## The verdict — and the guard on it

The tempting conclusion is "models disagree, so shop around." That is a shopping tip and it has a bad tail: **if you route around every refusal until something complies, you have not verified anything. You have found the permissive one.** Compliance is a detector output too.

What made the Case 2 reversal legitimate was not that a second model would have done it anyway. It was a contradiction pointed at inside the first model's own argument, which then held up under checking. Had the argument been bad, being routed around would have been the correct outcome. **Coherence-checking, not vote-counting.** The film says that out loud.

## Act map

| Beats | Act | Carries |
|---|---|---|
| B00 | Cold open · `ClaudeComposerAsk` | The ask lands answered; Liam signs in |
| B01–B06 | **The tests that failed their own test** | The canary incident. Ground truth is unambiguous |
| B07–B13 | **The classifier was right** | Surface vs intent; a prompt-injection test *is* a prompt injection; intent is not in the tokens |
| B14–B20 | **The fix, and what it admits** | Fable 5 partitions context; `isolate` aimed at a classifier; intent never enters the system |
| B21–B29 | **The other failure** | This session. Locally plausible, globally incoherent. The contradiction shown side by side |
| B30–B36 | **Correction or capitulation** | Four models, four verdicts, no oracle. Why shopping is not verifying |
| B37–B39 | Verdict · Your turn · Outro | |

## Vox plates — all Tier 1, all Bear's own material

Deep-explainer needs ~20–25% vox. This reel's evidence *is* screenshots, which makes the quota honest rather than decorative. Seven vox beats across five plates:

| Plate | Beats | Tier | Note |
|---|---|---|---|
| Cowork model picker (four models, Opus checked) | B31, B32 | 1 — Bear's screenshot | Already supplied |
| Claude Code refusal message | B03, B04 | 1 — Bear's session | **Needed** |
| The canary test file / folder listing | B08 | 1 — Bear's repo | **Needed** |
| Fable 5's rewritten prompt | B16, B17 | 1 — Bear's session | **Needed** |
| This session — the two contradictory passages side by side | B24 | 1 — this transcript | Extractable now |

**Zero Tier 2, zero Tier 3, zero rights escalations.** Four plates still need capturing — that is the shopping list, and it is entirely on Bear's own machine.

## FACTCHECK — the guard that matters most

This film is about generalising from a surface feature. **It must not do that to a product.**

1. **n = 1, twice.** One Claude Code incident and one Opus session. Neither is a benchmark. The narration says so explicitly, on screen, in the act where the four-model picker appears. No sentence may imply Fable 5 is better at judgment, or Claude Code worse, as a general property. The observation is: *these two systems reached different conclusions on this input on this day.*
2. **Sourcing.** The canary incident is Bear's own account. FACTCHECK requires either the session transcript or Bear on record as the source, named on the SOURCES card. No paraphrase of what a model "thought" — only what it output.
3. **Quote the refusals verbatim or not at all.** Both of them, including this session's.
4. **Model versions date fast.** Per DOUBLE-CHECK LAW, name the models — the story is unintelligible without them — but timestamp the incidents on screen and never phrase a finding in the present tense ("Claude Code refuses…"). Past tense, dated, once.
5. **The self-referential passage is checkable.** Case 2 comes from this transcript; the two contradictory passages get quoted exactly, with turn positions.

## Sourcing ladder

Rung 1 throughout: Bear's own screenshots (pantry), Remotion concept illustrations, Manim for the surface-vs-intent beat. **No gen-AI, no doodle, no `style_preset: "doodle"`, no rights escalations.**

## Manim beats

| Beat | Fragment |
|---|---|
| B10 | The token-level view: a prompt-injection *test* and a prompt-injection *attack* rendered as identical token streams, diverging only in a field the classifier cannot see |
| B18 | `isolate` as a partition — the same diagram from the context-engineering reel, redrawn with a classifier on the boundary instead of a sub-agent |
| B33 | Four verdicts on one input; the distribution shown, then the question "which of these is evidence of anything?" left standing |

## Open question

The Manim text path in this repo has two live bugs — word-space collapse and no collision management — confirmed in `_qc/BEAR-VISUAL-CHECK.md` on the p-value reel. Three Manim beats here. **Fix the renderer before this reel's build, or the same defect ships.**

## Gates

1. Write `beat_sheet.json` — 42 beats, lanes, `show` blocks, vox runs and handoff blocks.
2. **GATE F** — the five factcheck items above. The n=1 guard is a blocker, not a note.
3. **GATE P** — narration on an animated slate, no audio spend.
4. Audio → clock → align → **GATE D2** shopping list (four plates) → **GATE D1** slate previz → VISUAL QC → GATE T → `art final`.

Never publish. Never stage to TOPOST.
