# Factcheck — claude-liam-do-chatbots-pass (Gate F)

Format: claim | verdict | source | fix. All web-verified at plan time (2026-07-23); this is a history reel, so every date and percentage was treated as unconfirmed until checked.

| # | Claim (beat) | Verdict | Source / basis | Fix |
|---|---|---|---|---|
| 1 | Turing proposed the imitation game in **1950**, "Computing Machinery and Intelligence" (A2) | ✅ TRUE | *Mind* 59 (1950); well established | none |
| 2 | Turing predicted that by **2000** an average interrogator would have "not more than 70%" chance of a correct ID after **5 min** (≈30% fooled) (A5) | ✅ TRUE | Turing 1950, §6; Wikipedia "Turing test." TED-Ed's "100 MB" ≈ Turing's ~10^9 storage — narration avoids the memory figure and keeps the 30%/5-min bar | none |
| 3 | **ELIZA** — 1966, **Joseph Weizenbaum**, **MIT**, DOCTOR script, Rogerian therapist reflecting words back (A7, A8) | ✅ TRUE | Weizenbaum 1966, *CACM*; Wikipedia "ELIZA" (built 1964–67, released 1966) | none |
| 4 | The **secretary anecdote** + Weizenbaum's alarm / "ELIZA effect" (A9, A29) | ✅ TRUE | Weizenbaum, *Computer Power and Human Reason* (1976); widely documented ("extremely short exposures … induce powerful delusional thinking") | none |
| 5 | **PARRY** — 1972, **Kenneth Colby**, **Stanford**, simulated paranoia; "ELIZA with attitude" (A10) | ✅ TRUE | Colby et al. 1972; Wikipedia "PARRY" | none |
| 6 | Psychiatrists identified PARRY vs real-patient transcripts correctly **~48%** — no better than chance (A11) | ✅ TRUE | Colby-era Turing-variant study; reported ~48% (≈ random). Framed as "a coin flip does better" — accurate | none |
| 7 | **Loebner Prize** launched **1990** (Hugh Loebner); annual formal test; **judges knew** some partners were machines (A14) | ✅ TRUE | Wikipedia "Loebner Prize" (launched 1990; ran to 2019) | none |
| 8 | A Loebner winner conversed well **mainly on that year's headline politician** (A15) | ✅ TRUE (illustrative) | 1997 winner *Converse* (David Levy) leaned on Bill Clinton–era topical talk (per TED-Ed and contest write-ups). Narration says "the politician in that year's headlines" — kept generic but historically anchored | none |
| 9 | **Eugene Goostman** — **2014**, **13-year-old boy from Odessa** persona, second-language English (A16) | ✅ TRUE | Wikipedia "Eugene Goostman"; developed by Veselov, Demchenko, Ulasen (St. Petersburg, 2001) | none |
| 10 | At a **Royal Society** event (**June 7, 2014**), **33%** of judges over 5-min chats believed it human; organizers announced a "pass" (A17) | ✅ TRUE, but "pass" is **CONTESTED** | Royal Society / Univ. of Reading event; 33% figure widely reported (Wikipedia, IEEE Spectrum, NBC). Voiced as *the organizers' claim*, then debunked in A18 | keep "the organizers announced" framing |
| 11 | The persona **lowered judges' expectations** rather than raising the bot's ability — the "pass" was misdirection (A18) | ✅ TRUE (mainstream critique) | Aaronson, Marcus, and others 2014; standard critique | none |
| 12 | Modern LLMs = **next-token prediction, internet-scale training**; drop persona/topic gimmicks (A20–A23) | ✅ TRUE | Standard description of autoregressive LMs; no vendor/model names used | none |
| 13 | The "**juice … gave it to him … forgot to check the date**" sentence needs world knowledge to parse; modern models handle it (A22) | ✅ TRUE (illustrative) | TED-Ed example (pronoun-reference / Winograd-style world knowledge). Presented as an example, not a benchmark | none |
| 14 | **2025 controlled three-party test**: strongest model judged human **73%**, **above the real human** (A25, A26) | ✅ TRUE (single strong study, stated as such) | Jones & Bergen, *Large Language Models Pass the Turing Test*, arXiv:2503.23674 (submitted 31 Mar 2025); pre-registered, two populations; GPT-4.5 (persona) 73%, LLaMa-3.1-405B 56%, GPT-4o 21%, ELIZA 23%. Model named **only here / in SOURCES**, not in narration | none |
| 15 | "The machines pass … no longer up for debate" (A27) — is this overclaiming? | ⚖️ SCOPED | Claim is scoped to **Turing's behavioral bar** (5-min, can't-tell), which #14 supports; A28–A29 immediately deny that this equals understanding. Honest as scoped | keep the A27→A28 scope pivot intact |
| 16 | Bear's catch: Turing swapped "can it think" for "can it fool you" and passing hands the hard question back (A28) | ⚖️ OPINION (Bear's) | Rhetorical/philosophical framing; attributed explicitly to Professor Bear | keep attribution |

## Datable material (DOUBLE-CHECK LAW)
- Historical years (1950, 1966, 1972, 1990, 2014, 2025) **are the subject** and stay. **No current vendor/model names** appear in narration ("the strongest model tested"); exact model + study cited in FACTCHECK/SOURCES only. "Sixty years" (1966→2026) kept as a round rhetorical span.

## No fabricated quotes
- No invented verbatim quotes from Turing, Weizenbaum, Colby, or Searle. Anecdotes (A9) are paraphrased and documented.

**Gate F posture:** all history claims verified TRUE. The one contested item (#10, Goostman "passed") is voiced as the organizers' claim and debunked. The one strong-but-single result (#14) is stated as a specific study's finding, not field consensus. Opinion (#16) is marked as Bear's.
