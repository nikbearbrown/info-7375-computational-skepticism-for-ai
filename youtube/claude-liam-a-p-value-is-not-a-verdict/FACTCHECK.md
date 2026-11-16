# FACTCHECK.md — claude-liam-a-p-value-is-not-a-verdict

Gate F. The source is a research brief **plus its own correction addendum**. Both
were checked independently against primary sources. The addendum fixed several
real errors — and introduced at least one of its own.

**Headline: 4 claims from the original brief failed. The addendum's AUC citation is CONFIRMED ACCURATE — FACTCHECK.md's initial finding was wrong (see B20 GATE RESOLVED below).**

---

## ✅ GATE B20 — RESOLVED 2026-08-13

**Claim under test:** the addendum cites Kirchenbauer et al., *On the Reliability
of Watermarks for Large Language Models* (arXiv:2306.04634 / ICLR 2024) as
reporting *"AUC stayed above roughly 0.85 at 200 tokens and above roughly 0.9 at
600 tokens in the paraphrase conditions they tested."*

**Human check result:** FIGURES PRESENT. A human opened the published HTML of
arXiv:2306.04634v1 and searched it. The figures appear verbatim in the abstract:

> *"ROC-AUC remains above 0.85 when T=200 tokens are available, and above 0.9
> with T=600 tokens."*

Also in Section 4.1: *"by the 600 token mark, under the GPT and Dipper
model-based attacks, the watermark recovers to an AUC greater than 0.9."*

**The addendum's citation is ACCURATE.** The addendum paraphrased the abstract
correctly. The initial FACTCHECK.md finding ("absent from all four sources") was
itself an instance of the failure mode this film documents: the research pass
that used primed queries returned confirmations of absence; the neutral-framed
query returned uncertainty. A human resolved the conflict by going to the source.

**FACTCHECK's own error** (now corrected): the initial research pass marked these
figures absent. They are in the abstract — the first place any factcheck should
look. This is logged in BUILD-LOG.md and is the subject of the new B20 beat.

**Consequence:** B20 redesigned. It no longer accuses the addendum of fabricating
a citation. It now shows the reel's own production process catching and correcting
its initial wrong finding — demonstrating the thesis on itself. See BUILD-LOG.md
2026-08-13 entry.

**The original FACTCHECK.md caveat was prescient but drew the wrong conclusion:**
*"Priming contamination is exactly the failure mode this film is about"* — yes.
And the research pass was the thing that was contaminated, not the addendum.

---

## Claims corrected or cut

| # | Beat | Claim (source) | Verdict | Source | Fix applied |
|---|---|---|---|---|---|
| 1 | B02 | KGW defaults γ=0.5, δ=2.0 (brief) | CORRECTED | authors' repo: *"we suggest default values of gamma=0.25 and delta=2.0"* | γ=0.25, δ=2.0 on screen; γ=0.5 was a theory illustration the brief mixed with production defaults |
| 2 | B07 | "One paraphrase pass defeats it" (brief) | CORRECTED | Krishna et al., NeurIPS 2023 | Real number used: 100% → 57.2% detection at 1% FPR after DIPPER; kill-switch drawn and struck through on screen |
| 3 | B17 | California SB 942 / AB 853 mandates text watermarking | CORRECTED | Bus. & Prof. Code §22757.2/.3; Morgan Lewis, Aug 2026 | Film states "California's rules are audio-visual" — accurate; duties attach only to image/video/audio content |
| 4 | B17 | The EU/California date match is "coincidental timing" | EXEMPT | AB 853 operative date shifted 1 Jan → 2 Aug 2026; no legislative record states a rationale | Cut — the film does not characterise the date match at all |
| 5 | B17 | China mandates AI watermarking that reaches text | CORRECTED | CAC Measures + GB 45438-2025, eff. 1 Sep 2025 | For text: visible label + file metadata; digital watermarks encouraged not required; stated accurately in B17 |
| 6 | B18 | OpenAI said its detector was 99.9% accurate | EXEMPT | OpenAI, 4 Aug 2024 post; *WSJ* reporting | 99.9% and "held two years" are WSJ from internal documents, not OpenAI statements; both kept off screen; only published reasons attributed |
| 7 | B16 | ETH SRI reverse-engineered SynthID without the key | CORRECTED | sri.inf.ethz.ch/blog/probingsynthid | Decomposition was read off the published Nature paper; actual finding on screen instead: ~4% spoof, >90% scrub |
| 8 | B17 | India has only proposed AI labelling rules | EXEMPT | MeitY SGI amendments notified 10 Feb 2026, effective 20 Feb 2026 | Stale — binding but audio-visual only; cut from the film |
| 9 | ALL | No paper validates watermark substitutions semantically | CORRECTED | Fu et al., AAAI 2024 38(16):18003–18011 | Narrow surviving gap stated accurately; not made a beat (needs caveat a 15-second beat cannot carry) |

## Claims verified and used

| Beat | Claim | Source |
|---|---|---|
| B02 | Hash previous token → γ-partition → +δ on green logits | Kirchenbauer et al., ICML 2023, PMLR 202:17061–17084 |
| B03 | Detection is a one-proportion z-test, z = (\|s\|_G − γT)/√(Tγ(1−γ)) | ibid. |
| B04 | SynthID uses **tournament sampling**, not logit boosting; non-distortionary config preserves the distribution | Dathathri et al., *Nature* 634, 818–823 (2024) |
| B05 | ~20M live Gemini responses; thumbs-up differed **0.01%**, thumbs-down **0.02%**, both inside 95% CIs | ibid. |
| B07 | 100% → **57.2%** detection at 1% FPR after DIPPER | Krishna, Song, Karpinska, Wieting & Iyyer, NeurIPS 2023 |
| B07 | Strong human paraphrase still detectable near **800 tokens** at 1e-5 FPR | Kirchenbauer et al., ICLR 2024 |
| B08 | EU Code of Practice applies watermarking to free-form text **>200 tokens**; interoperability target **2 Feb 2027** | EU Code of Practice on transparency of AI-generated content |
| B11 | sens 0.90 · FPR 1e-5 · prevalence 1e-6 → **PPV = 8.26%** | verified arithmetic |
| B12 | 1e-5 × 1,000,000 = **10** expected false positives | verified arithmetic |
| B13 | TOEFL essays: **61.22%** average FPR across seven detectors; **18/91 (19.78%)** flagged unanimously; US 8th-grade near-perfect | Liang, Yuksekgonul, Mao, Wu & Zou, *Patterns* (Cell Press), 2023 |
| B15 | Public-key and ZKP watermark verification exist; **zero in production** | Fairoze et al., *Publicly-Detectable Watermarking*; PVMark, USENIX Security 2026 |
| B16 | Under **$50**, spoof and scrub deployed schemes at **>80%**; SynthID **~4% spoof / >90% scrub** | Jovanović, Staab & Vechev, ICML 2024, PMLR 235:22570–22593; ETH SRI blog |
| B17 | EU AI Act Art. 50(2) covers **text**, applies **2 Aug 2026**; carries an assistive/standard-editing exemption | artificialintelligenceact.eu/article/50 |
| B17 | Korea AI Framework Act in force 22 Jan 2026 — notice duty reaching text, **no machine-readable format** | Cooley; FPF |
| B17 | EO 14110 revoked 20 Jan 2025; S.2765 died with the 118th; S.1396 still in committee — **no US federal statute** | congress.gov |
| B18 | OpenAI's two published reasons: breaks under translation/rewriting; risks disproportionately flagging non-native English writers | OpenAI, 4 Aug 2024 |

## The narrow gap that survives — and is NOT overclaimed on screen

The brief's "nobody validates semantic equivalence" is too strong. The version
that holds: **no published work performs a local causal counterfactual audit** —
matched watermarked/unwatermarked generations from the same prompt and model,
isolating the exact token positions the watermark changed, with domain experts
rating meaning preservation in high-precision registers.

Closest existing work: arXiv:2509.07755 (medical texts) — same prompt/model
matched pairs, 6 raters including practitioners, finds watermarking introduces
new disease entities in **11–13%** of content. It does **not** localise the
changed token positions.

**The film does not make this a beat.** It's a real gap but it needs a caveat
paragraph to state honestly, and a 15-second beat can't carry it. Logged here for
the description and for a future reel.

## Datable material stripped

- No model version numbers or vendor product names in narration
- "As of August 2026" framings removed; the regulatory beat states duties, not dates, except the two statutory dates that are the point
- **Anthropic's own scheme is not asserted anywhere** — it has not been publicly disclosed

Status: PASS — all retained claims verified or corrected; B20 gate resolved 2026-08-13 by human check (figures present in abstract). Signed by build agent 2026-08-13.
