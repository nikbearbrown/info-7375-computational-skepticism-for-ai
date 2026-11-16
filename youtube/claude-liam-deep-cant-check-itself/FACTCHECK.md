# FACTCHECK — You Can't Check a Model With Itself
`claude-liam-deep-cant-check-itself` | Gate: PLAN | 2026-07-28

---

## Method

Every specific claim below was evaluated before authoring. Two categories:

- **VERIFIED-STRUCTURAL**: a logical / first-principles claim that holds without a citation (e.g., "a model's self-review uses the same weights that produced the output"). These are defensible on mechanism alone.
- **VERIFIED-OBSERVED**: directly observed in this or prior sessions (the Icon Incident).
- **UNSOURCED**: a qualitative directional claim where the pattern is plausible and widely discussed but where a specific paper/number was not confirmed for this build. Stated qualitatively in the narration. No specific numbers, no arXiv IDs.
- **SPECULATIVE**: future/hypothetical model names used only as framing devices, labeled as speculative in narration and in the B00 cold-open `modelLabel` field.

**Hard rule applied**: any claim that required a specific citation to be asserted as fact was either (a) restated qualitatively, (b) flagged UNSOURCED below, or (c) cut. No inherited confidence from the seed brief.

---

## Claim-by-Claim Log

| Beat | Claim | Verdict | Notes |
|---|---|---|---|
| B00 / A1R | "Fable 5" and similar next-gen model names | SPECULATIVE | Labeled as speculative in narration ("call it Fable 5, or whatever the next generation lands as") and in `modelLabel: "Fable 5 (speculative)"`. Used only as a framing device — no benchmark scores, no product claims made. |
| A1R2 | "The benchmark race is real" | VERIFIED-STRUCTURAL | Benchmarks exist and are actively contested. No specific scores cited. |
| A1M | "Can you trust any model to catch its own errors? The answer — structurally — is no." | VERIFIED-STRUCTURAL | The structural claim is: a model's self-review uses the same weights, training data, and statistical tendencies that produced the original output. This is a mechanical claim about how autoregressive language models work, not an empirical claim requiring a citation. |
| A2M | "review and original share a source → model won't catch its own errors" | VERIFIED-STRUCTURAL | Same as above. First-principles claim: the priors that generated the error are the priors that run the review. |
| A2R | "more samples from the same distribution → compounds, doesn't correct" | VERIFIED-STRUCTURAL | Logical consequence of A2M. A model drawing additional samples from its own distribution does not escape the distributional bias that produced the error. |
| A2V | "confidence is indistinguishable from correctness until you check from outside" | VERIFIED-STRUCTURAL | A language model produces confidence-calibrated outputs, but calibration is itself an in-distribution property. External verification is required to distinguish confident-and-correct from confident-and-wrong. |
| A2M2 | "stronger model → more articulate rationalization of wrong answer" | UNSOURCED | Directional claim: more capable models produce more fluent, more structured arguments. This is plausible and widely observed qualitatively but no specific study is cited here. Stated qualitatively ("tends to"). |
| A3R | "errors cluster within a model family" | UNSOURCED | Qualitative directional claim. The pattern that models trained on similar data and methods share failure modes is plausible and is discussed in the literature on model diversity, but no specific paper or number is cited. The word "tend" is used throughout. |
| A3M | "errors correlate more within a family than across families" (two-bar viz) | UNSOURCED | The two-bar Manim scene conveys the qualitative shape only — no numeric values on the bars. The scene description explicitly notes: "Flag in FACTCHECK: direction of stronger-model effect is UNSOURCED." The bars are concept-only, not data. |
| A3M | "stronger models tend to cluster tighter within their family" | UNSOURCED | Counterintuitive directional claim stated qualitatively ("tend to"). The mechanism is plausible (more capable models trained more deeply on the same corpus → stronger prior alignment within family) but the specific direction of this effect was not confirmed against a paper for this build. No numbers. |
| A3R2 | "upgrade can degrade your verification stack" | VERIFIED-STRUCTURAL | Logical consequence of A3M: if within-family correlation increases with capability, then choosing the most capable family member reduces inter-model diversity. This follows from the definitions, conditional on the UNSOURCED directional claims in A3M. |
| A4R | "human is the least-correlated verifier in the stack" | VERIFIED-STRUCTURAL | A human reviewer does not share the model's training data, weights, or distributional priors. The correlation between a human's errors and a model's errors is lower than the correlation between two instances of the same or similar model. This is a structural claim, not an empirical one. |
| A4V | "'I watch them' is non-parallelizable" | VERIFIED-STRUCTURAL | Human attention is a finite, serial resource. Throughput scaling does not scale review capacity. |
| A4M / A4R2 | "default = 'human reviews everything' is a bet throughput stays low" | VERIFIED-STRUCTURAL | If a human reviews every output and throughput doubles, review time per item halves — or review capacity becomes the bottleneck. Standard operations logic. |
| A5V + A5V2 | The Icon Incident — false premise accepted, phantom workstream ran, assets already existed | VERIFIED-OBSERVED | Directly observed in the session that commissioned this video. The sequence of events (premise arrived → accepted → request card written → work began → library already had the icons → output gate reported all-clear) is factual. |
| A5R | "output gate checks completion, not premises" | VERIFIED-OBSERVED | The output gate (`todo.py` / `build` status in beat_sheet) checks whether beats are filled (VIDEO / SLATE status). It does not audit the premises under which generation began. |
| A5SH / A5M | "a quality gate surfaces the decisions the pipeline made" | VERIFIED-STRUCTURAL | A quality gate that only reports done/not-done is a process gate by definition. To be a quality gate, it must surface the decisions and their inputs — standard quality-engineering terminology. |
| A6R | "single-vendor = availability bet" | VERIFIED-STRUCTURAL | Any dependency on a single provider creates availability risk independent of capability. This is standard systems-reliability reasoning. |
| A6R | "with safeguard routing, you may not know which model ran" | UNSOURCED-GENERAL | This describes a real operational pattern (provider-side model abstraction, routing layers) that exists in some products. No specific provider's terms of service or API documentation is cited. Stated carefully: "you may not know." |
| A6V | "keep several model families warm — different failure modes" | VERIFIED-STRUCTURAL | Follows from A3R: if families have different failure modes, maintaining multiple families provides coverage. |
| A6R2 | "voting amplifies shared error; adversarial checking surfaces disagreement" | VERIFIED-STRUCTURAL | Voting (majority / average) over correlated errors will not reduce bias — it will reflect it. Adversarial probing is designed to surface disagreement, not consensus. Standard ensemble-and-diversity argument. |

---

## UNSOURCED Summary (no numeric claims shipped)

Four claims are marked UNSOURCED and stated qualitatively in the narration:

1. **A2M2** — stronger model → more articulate rationalization. Stated as "tends to." No citation.
2. **A3R / A3M** — errors cluster within families more than across families. Stated as "tend to." No bars have values. No citation.
3. **A3M** — stronger models cluster tighter within family. Stated as "tend to." No values. No citation.
4. **A6R** — safeguard routing opacity. Stated as "you may not know." No specific provider cited.

If Bear can source any of these (ML diversity literature, model mixture papers, provider routing documentation), promote to VERIFIED and add source to SOURCES.md.

---

## What was cut or not claimed

- Specific benchmark numbers for any named model: CUT.
- Any arXiv ID from the seed brief: NOT CITED (treated as unverified per the brief's own instruction).
- Specific "model A is more correlated with model B" pair data: CUT.
- "As of [month]" temporal claims: NONE SHIPPED.
- Named model families (OpenAI / Anthropic / Google / Meta): NOT NAMED (the argument is family-agnostic).

---

`gate: PLAN — FACTCHECK.md complete before audio spend, per workflow step 2.`
