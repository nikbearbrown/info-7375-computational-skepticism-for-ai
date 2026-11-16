# FACTCHECK.md — claude-liam-two-models-twice-the-price

**Source status:** The planning document is self-labeled UNKNOWN/UNSOURCED. Per deep-explainer Rule 5 and PLAN framing, no specific benchmark number from the source appears as fact. All retained claims are either MECHANISM (timeless, derivable from first principles) or ILLUSTRATIVE (explicitly labeled on screen).

| # | Beat | Claim in narration | Type | Verdict | Source / derivation |
|---|---|---|---|---|---|
| 1 | B02–B03 | A comparison table is a rhetorical object | MECHANISM | PASS | definitional — table designers choose rows/cols/order |
| 2 | B04–B06 | Headline column can show the higher of two variants | MECHANISM | PASS | documented practice in benchmarking; no specific number |
| 3 | B07 | A column blending two non-interchangeable variants doesn't describe a buyable product | MECHANISM | PASS | logical inference; no citation needed |
| 4 | B10–B11 | Production inference systems include routers, safety filters, fallback paths | MECHANISM | PASS | architectural fact about LLM serving infrastructure |
| 5 | B12–B13 | A benchmark score depends on model + harness + fallback rate | MECHANISM | PASS | decomposition of a scored system; no specific values |
| 6 | B14–B15 | The same model at different compute budgets produces different scores | MECHANISM | PASS | established in inference-scaling research |
| 7 | B20–B21 | Score vs compute budget is non-monotonic in some regimes | MECHANISM | PASS | documented behavior; shown ILLUSTRATIVE on screen |
| 8 | B25–B26 | cost/task = (price/token × tokens) ÷ pass_rate × (1 + retries) | MECHANISM | PASS | algebraic definition; no prices or rates cited |
| 9 | B27–B28 | A lower per-token price model can have a higher per-task cost | MECHANISM | PASS | follows from the formula; no real prices cited |
| 10 | B31–B32 | Compliance constraints (data retention, privacy) can exclude a model regardless of capability | MECHANISM | PASS | known constraint in regulated-industry deployments |
| 11 | B33–B34 | If a model cannot be deployed, its benchmark lead is zero | MECHANISM | PASS | logical inference; not a measurement claim |
| 12 | ALL | All bar charts and curves labeled "illustrative" | ILLUSTRATIVE | PASS | on-screen captions enforce this |
| 13 | ALL | No specific benchmark numbers (percentages, scores, prices) appear | SOURCING RULE | PASS | enforced in narration text and Manim specs |
| 14 | ALL | No model version names (Opus/Fable/Mythos + numbers) appear | SOURCING RULE | PASS | enforced throughout |

**FACTCHECK VERDICT: PASS — all retained claims are mechanisms or explicitly labeled illustrations. No numbers from the unverified source appear as facts.**

Status: Signed by build agent 2026-07-28 — all claims verified as mechanisms or explicitly labeled illustrative; no unverified benchmark numbers present.
