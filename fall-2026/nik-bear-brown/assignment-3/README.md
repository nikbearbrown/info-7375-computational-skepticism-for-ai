# Assignment 3 — Robustness and explanation

## Executive summary

**What it does.** Two small tools that try to break a result on purpose.

`probes.py` takes a baseline input, applies a transformation to it, and records what the model did — one row per probe: baseline input, transformed input, the relation that *should* hold, the observed output, pass or fail. Add whitespace, reorder a list, change a word that actually matters, feed it a slice from a different distribution. Invariance probes are expected to hold; semantic probes are expected to break. A probe that never fails is not reassuring, it is uninformative.

`scoring_rule.py` holds a decision rule small enough to read — two or three features — and enumerates every counterfactual over a small discrete input space: original score, the feature changed, the new score, whether the decision flipped, and whether that change is even feasible. Then Claude is asked to explain the rule from examples alone, and its narrative is put next to the enumerator's table. **Where the explanation names a feature the removal test says is doing nothing, the explanation is wrong.** That comparison is `explanation-audit.md`, and it is the point of the assignment.

**What it is for.** Fluency is not evidence. A model — or a person — can produce a confident, well-formed account of why something happened that is about the wrong cause entirely. These two tools replace the account with a measurement: change the input, run it again, write down what moved.

**What it does not claim.** A counterfactual of a program is an intervention on the program, not on the world: if removing a feature flips this rule's decision, that is a fact about the rule. And a finite suite that passes is evidence about those probes only.

**Status: not built.** The folder was created 2026-09-26; everything below is the plan, the prediction, and the acceptance criteria, written before any run exists. Nothing has been run and no claim here is verified. The baseline starts deliberately fragile so that at least one probe *can* fail. Process log: [`FRICTIONAL.md`](FRICTIONAL.md) here, [`../FRICTIONAL.md`](../FRICTIONAL.md) for the folder.

---

## What the assignment asks for

From [`assignments/fall-2026/assignment-03.md`](../../../assignments/fall-2026/assignment-03.md), bundling Lesson 4 (*Break the shortcut you just built*) and Lesson 5 (*A convincing explanation can explain the wrong thing*):

| Phase | What it requires |
|---|---|
| **Predict** | Which input changes should preserve the result and which should change it — named *before* probes are designed. Whether the feature named in a fluent explanation is necessary for the output, with a concrete removal test |
| **Build It** | A deterministic Python **probe runner** recording baseline input, transformed input, expected relation, observed output, pass/fail — covering whitespace or ordering invariance, a relevant semantic change, and a shifted slice. Plus an interpretable **scoring rule** (2–3 features) and a **counterfactual enumerator** over a small discrete input space |
| **Use It** | Ask Claude to critique the probe expectations and to name a shortcut the implementation may exploit. Run ≥3 frozen probes. Ask Claude to explain the rule from examples, then compare its narrative against executed feature changes — including a correlated proxy and a feature with no effect |
| **Ship It** | `robustness-profile.csv`, the baseline mechanism, probes, failures, a residual-risk note; `explanation-audit.md`, the scoring rule, counterfactual table, feasibility assumptions, tests — plus the four standard records below |
| **Verify** | Start from a **known fragile baseline** so at least one probe *can* fail, then repair it. Compute ≥2 cases by hand. Test unchanged inputs, unreachable decisions, infeasible feature changes |

Rubric: 60 implementation + 10 Frictional + 10 GitHub posting + 20 relative quartile.

## Planned files

| File | What it will be | Status |
|---|---|---|
| `baseline.py` | The small classifier or prompt workflow under test — deliberately fragile to start, so a probe can fail | not started |
| `probes.py` | The deterministic probe runner: baseline input, transformed input, expected relation, observed output, pass/fail | not started |
| `robustness-profile.csv` | One row per probe, as actually run | not started |
| `scoring_rule.py` | The interpretable rule, 2–3 features, plus the counterfactual enumerator over a small discrete space | not started |
| `explanation-audit.md` | Claude's narrative explanation of the rule beside the executed feature changes, and where they disagree | not started |
| `test_probes.py` | Unchanged inputs, unreachable target decisions, infeasible feature changes | not started |
| `residual-risk.md` | What the passing suite does **not** cover | not started |

## The standard submission files

The course asks every submission to carry the same four records, from [`templates/`](../../../templates/). The order matters: the prediction and the acceptance criteria are fixed **before** there is any output to be impressed by.

| File | What it holds | Status |
|---|---|---|
| [`PREDICTIONS.md`](PREDICTIONS.md) | The expectation and its measurable failure condition, dated before the first run | written, not yet reviewed |
| [`VERIFICATION.md`](VERIFICATION.md) | The acceptance criteria fixed in advance, and the checks as actually run | criteria written; nothing verified |
| [`CONTRIBUTIONS.md`](CONTRIBUTIONS.md) | What the human did, what Claude did, what is still unreviewed | current |
| [`FRICTIONAL.md`](FRICTIONAL.md) | This assignment's process log (the folder-level one is [`../FRICTIONAL.md`](../FRICTIONAL.md)) | current |

## What carries over from Assignment 2

The [Boondoggle Report](../boondoggle-report/) already produced an instance of exactly what this assignment measures: Claude Code specified the **wrong application** — greenhouse-watch, from a different class — and specified it fluently, for thirteen turns. Nothing in the output's quality signalled the error. That is the failure mode here, one layer up.

## The honest note about scope

A counterfactual of a program is not an intervention on the world. If removing a feature moves this scoring rule's decision, that is a fact about the rule — not evidence that the feature causes anything outside it. And a finite suite that passes is evidence about those probes only. Both limits get stated in the shipped files, not just here.
