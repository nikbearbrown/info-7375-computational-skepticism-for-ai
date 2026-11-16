# FACTCHECK.md — claude-liam-silent-sql-failures
## Gate F — RUN 2026-07-24

Source: `books/computational-skepticism-for-ai/youtube/silent-sql-failures-source.md`
(Professor Bear's feedback document on Zhenhao's project — largely pedagogical guidance,
not external empirical claims)

---

## Claims verified against external sources

| Claim | Verdict | Source | Note |
|-------|---------|--------|------|
| Bitcoin tracks unspent transaction outputs (UTXO), not account balances | VERIFIED | Bitcoin Core documentation; standard Bitcoin protocol | Foundational Bitcoin architecture |
| `getreceivedbyaddress` RPC returns gross received, not current balance | VERIFIED | Bitcoin Core RPC reference; this is documented behavior — the call sums all outputs received regardless of spent status | Exactly as described in source |
| `scantxoutset` reconstructs the current UTXO set for an address | VERIFIED | Bitcoin Core RPC reference; designed for UTXO set scanning, providing true current balance | Correct description |
| SQL `SUM()` silently skips NULL values (treats them as non-existent, not as zero) | VERIFIED | SQL ISO standard (SQL:1999 and later); `SUM(NULL, NULL) = NULL` but `SUM(5, NULL) = 5` — NULL is excluded, not treated as 0 | Standard SQL semantics |
| QuickCheck = property-based testing framework (Claessen & Hughes) | VERIFIED | Claessen & Hughes (2000) "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs" — ICFP 2000 | Standard reference |
| Self-Consistency paper = Wang et al. 2022 | VERIFIED | Wang et al. (2022) "Self-Consistency Improves Chain of Thought Reasoning in Language Models" — referenced in source | Not named in narration; source reference only |
| Kadavath et al. 2022 LLM calibration paper | VERIFIED | Kadavath et al. (2022) "Language Models (Mostly) Know What They Know" — Anthropic | Not named in narration; source reference only |
| Spider and BIRD are text-to-SQL benchmarks using execution-match against gold SQL | VERIFIED | Well-established benchmarks in the NL-to-SQL literature; execution-match is the standard evaluation protocol | Not named in narration; source reference only |

## Claims presented as hypotheses (explicitly flagged in narration)

| Claim | How narrated | Status |
|-------|-------------|--------|
| Self-consistency likely fails on systematic UTXO errors | "Here's the likely finding" / "likely negative result" | Hypothesis, NOT asserted as fact ✅ |
| "Most domains have something equivalent" to Bitcoin's RPC path | Pedagogical invitation in BHTF | Invitation, not empirical claim ✅ |
| Calibration overconfidence specifically on Tier 3 | "The novel calibration angle ... look for" | Hypothesis to test, not claimed as true ✅ |

## Stripped / compressed from source

- No tool version numbers, model names, or "as of [date]" claims in narration.
- Zhenhao's full name: never used in narration — first name only throughout. ✅
- Source references (QuickCheck, Self-Consistency, Kadavath, Spider, BIRD) cited in
  SOURCES.md for the paper but not named in narration to avoid datability.

## GATE F — VERDICT: PASS

All factual claims in narration verified. Hypotheses explicitly framed as hypotheses.
No fabricated-but-fluent claims detected. Source is Bear's own pedagogical feedback
document; claims that are pedagogical design (taxonomy, tiers, strategies) are
correctly attributed to that design, not to external empirical findings.
