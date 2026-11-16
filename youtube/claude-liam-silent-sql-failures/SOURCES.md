# SOURCES.md — claude-liam-silent-sql-failures

## Primary source

**`books/computational-skepticism-for-ai/youtube/silent-sql-failures-source.md`**
Professor Bear's feedback on Zhenhao's Computational Skepticism final project.
This document IS the reel — the body is Bear's feedback, delivered via Liam's narration.

## References cited in source (for paper / SHOPPING.md context; not named in narration)

- **QuickCheck**: Claessen, K. & Hughes, J. (2000). "QuickCheck: A Lightweight Tool
  for Random Testing of Haskell Programs." ICFP 2000.
  — Referenced in source for Part 5 (differential testing / property-based testing framing).

- **Self-Consistency**: Wang et al. (2022). "Self-Consistency Improves Chain of Thought
  Reasoning in Language Models." arXiv:2203.11171.
  — Referenced in source for Part 4. The reel's angle pushes back on its generality
  for semantic (vs syntactic) errors.

- **LLM Calibration**: Kadavath et al. (2022). "Language Models (Mostly) Know What They Know."
  Anthropic. arXiv:2207.05221.
  — Referenced in source for Part 6. Reel differentiates from aggregate calibration.

- **Text-to-SQL benchmarks**: Spider (Yu et al. 2018) and BIRD (Li et al. 2023).
  — Referenced in source as baseline comparison (execution-match evaluation, which
  Zhenhao's project shows is insufficient for quiet failures).

- **Bitcoin Core RPC**: `getreceivedbyaddress`, `scantxoutset`, `gettxout`.
  — Standard Bitcoin Core RPC documentation (https://developer.bitcoin.org/reference/rpc/).

## Technical references (verified)

- Bitcoin UTXO model: standard Bitcoin protocol documentation.
- SQL NULL handling (SUM skips NULLs): SQL ISO standard (SQL:1999+).

## Credits

- Narration voice: Kokoro am_onyx (free, local). No ElevenLabs spend.
- Manim scenes: generated in this session (Claude Code + scenes.py).
- Remotion patterns: ClaudeComposerAsk, SlateCard, DeckPattern, ChipGrid,
  ClaudeVerdictArtifact, ClaudeTitleOutro (brutalist-art runtime).
- VOX stills: to be AI-generated (Tier 1, all generic/illustrative). See SHOPPING.md.
