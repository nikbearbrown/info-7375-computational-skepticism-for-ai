# Professor Bear's feedback — Zhenhao's Computational Skepticism final project
_Source for a deep-explainer reel. FIRST NAME ONLY: "Zhenhao." The reel is Bear's
feedback on the project idea below._

## The student's proposal (Zhenhao)
Topic: detecting silent failures in LLM-generated SQL. Building a natural-language-to-SQL
system over a Bitcoin blockchain database, Zhenhao noticed the dangerous failure mode is
NOT the query that throws an error — it's the query that executes cleanly and returns a
plausible-looking number that is wrong. Example: asked for an address balance, the model
summed all outputs paid to that address (gross received) rather than current balance,
because it ignored that some outputs were later spent. The query ran fine and returned a
well-formed answer — nothing in the output signals it's wrong.

Plan: measure how often this happens and whether it can be detected automatically. Bitcoin
is a good testbed because ground truth is independently recomputable — the same question can
be answered via SQL and again via direct RPC calls to a node, so disagreement between the two
paths flags an error without a human oracle. Deliverables: a verification framework, an error
taxonomy, and a calibration analysis. Hope: the takeaway generalizes to any setting where a
model produces output that looks correct and can't be checked by inspection alone.

## The core problem (why this is worth doing)
Most LLM-to-SQL evaluation treats correctness as binary and detectable — matches gold SQL or
not. Zhenhao's observation cuts against that. His failure is a SEMANTIC failure that survives
every check that only inspects surface behavior (does it run, return rows, right shape).
Beyond SQL, it's an instance of a larger problem: outputs wrong in ways that look like success.
A model that fails LOUDLY is manageable (catch the exception, flag the empty result). A model
that fails QUIETLY needs a different kind of verification — one that doesn't depend on surface
plausibility, because surface plausibility is exactly what's compromised. Bitcoin offers a rare
gift: a second, INDEPENDENT computational path (RPC/UTXO reconstruction) to the same truth, so
"is this correct?" becomes disagreement-detection between two paths unlikely to be wrong the
SAME way.

## Part 1 — the error taxonomy (separate by MECHANISM, not symptom)
1. **Semantic misinterpretation of domain concepts** — balance-vs-gross-received: right SQL
   competence, wrong domain model (UTXO requires tracking spent status). A knowledge gap
   disguised as a syntax success.
2. **Silent aggregation errors** — double-counting via unintended joins; undercounting via
   overly restrictive WHERE clauses that drop rows instead of erroring.
3. **Temporal/state confusion** — a point-in-time snapshot treated as current state, or vice
   versa ("as of block N" vs "currently").
4. **Null/edge-case swallowing** — SQL silently skips NULL in SUM; missing data looks like
   zero, which for a balance is catastrophically different from "no data."
5. **Off-by-reference-frame errors** — satoshis vs BTC; an address's own txns vs where it
   appears as a change output; block height vs block time.
Build it EMPIRICALLY: run ~50–100 questions, inspect every SQL-vs-RPC disagreement, let the
taxonomy emerge from real patterns before finalizing. Top-down risks missing the category the
system actually fails at most.

## Part 2 — the benchmark question set (difficulty = # of implicit domain assumptions)
- Tier 1 (single-table, no domain semantics): "How many txns in block X?" — low risk.
- Tier 2 (one domain concept): "Total ever sent to address X?" — filter outputs; no spent-tracking.
- Tier 3 (state-tracking): "Current balance of X?" — the UTXO problem.
- Tier 4 (multi-hop): "Current balance of X, excluding change outputs from its own txns?"
Compute the RPC ground truth FIRST, independently, before running the NL-to-SQL system — else
you anchor "correct" on the SQL path and bias the sample toward errors that already look wrong.

## Part 3 — detection strategy 1: cross-validation against independent computation (the backbone)
Same question, two independent paths (SQL vs RPC); disagreement flags error. Subtlety: RPC and
SQL aren't symmetric — a naive RPC call can encode the SAME silent bug (e.g. `getreceivedbyaddress`
also returns gross received, not balance, unless you reconstruct balance from the UTXO set via
`scantxoutset`). Rigor = documenting, per question type, exactly what RPC calls constitute ground
truth and why they're immune to the SQL path's failure mode.

## Part 4 — detection strategy 2: self-consistency (and its LIKELY NEGATIVE RESULT)
Sample the model N times (temp>0), execute all candidates, check agreement. Hypothesis to test
explicitly: does disagreement correlate with error, or does the model fail CONSISTENTLY on the
silent cases (all N samples make the same UTXO mistake) — giving self-consistency ZERO signal
for exactly the failure this project cares about most? Flag this as a likely negative result and
REPORT it as a finding: sampling-based agreement is not sufficient for semantic (vs syntactic)
errors. Don't bury it.

## Part 5 — detection strategy 3: differential testing on synthetic DBs (most rigorous)
Construct small synthetic databases engineered so two candidate query semantics (correct vs
plausible-but-wrong) produce DIFFERENT outputs. Balance case: a synthetic address with 3 received
outputs, 2 later spent — gross-received (10.0) and current-balance (2.0) diverge by construction.
Run the generated query; if it returns gross received, the bug is caught definitively, independent
of what real data happened to show. This is property-based testing (QuickCheck) for SQL semantics
— frame it that way to connect to established methodology.

## Part 6 — calibration: does stated confidence track accuracy?
Emit a confidence per query; bin and plot a reliability diagram. The headline to look for: is the
model EQUALLY confident on Tier 3 (UTXO/balance) as Tier 1 (counting), despite far higher real
error on Tier 3? Skeptical caveat: verbalized LLM confidence is known to be poorly calibrated —
just reconfirming that says nothing new. The NOVEL angle: is the model overconfident SPECIFICALLY
on state-tracking (Tier 3/4) even if its overall curve looks fine? Calibration BY TIER, not just
aggregate — that's the version that would actually be new.

## What makes this strong vs. merely competent
- Report negative results as FINDINGS (self-consistency failing on systematic errors IS a
  contribution — tells builders sampling-agreement isn't enough for semantic bugs).
- Decide up front whether the taxonomy is domain-specific or generalizes — the "beyond SQL"
  claim needs one concrete paragraph, e.g. is a "silent aggregation error" structurally the same
  as an LLM agent silently double-booking a calendar slot? Name one adjacent domain explicitly.
- Justify tolerance thresholds — `delta < TOLERANCE` is a hidden design decision;
  BTC/satoshi rounding noise could be misclassified as a semantic error.

## Reference lineage
QuickCheck (Claessen & Hughes) for Part 5; Self-Consistency (Wang et al. 2022) for Part 4 — the
negative result pushes back on its generality; LLM calibration (Kadavath et al. 2022, "Language
Models Mostly Know What They Know") for Part 6 — differentiate, don't reconfirm; Spider / BIRD
text-to-SQL benchmarks (execution-match against gold SQL — exactly the check this project shows
is insufficient); Bitcoin Core RPC (`scantxoutset`, `gettxout`) for correct balance reconstruction.
