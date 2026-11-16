# FACTCHECK — claude-liam-deep-09-delegation-trust

**Gate F not yet run.** This file pre-stages the claims that need verification before GATE P, per DOUBLE-CHECK LAW and the deep-explainer "unverified-source caution" rule. The source chapter is a *rough draft* (header notes preserved `[verify]` flags; read at HEAD — no git merge markers survived into the read). Treat named numbers and prevalence claims as unconfirmed until checked against the primary source, not against the chapter.

| Claim in narration | Beat | Status | Note |
|---|---|---|---|
| Two teams, identical loan pipeline, only the delegation map differs; committee tables the vague one | B00, A1R, A1M, A1V | HOLDS (illustrative) | The chapter frames this as "a controlled experiment that ran itself," i.e. a teaching story, not a cited study. Narration keeps it as an illustration ("Picture the room…"), never asserts it as measured data. |
| Delegation is a contract, not a partition; handoff condition is load-bearing and must be testable | A2R, A2M, BVDT | HOLDS | Core chapter thesis; argument, not a datable fact. |
| Testability is graded — some conditions testable only by a qualified reviewer | A2R2 | HOLDS | Chapter states this explicitly (the "wrinkle" section). |
| Five supervisory capacities each have an operational form + artifact; no artifact → capacity didn't happen | A3R, A3V, BVDT | HOLDS | Chapter's own framing; "if the artifact is not there, the capacity did not happen." |
| Eight-item map; items 1–4 broken-if-missing, 5–8 unsupervised-if-missing | A3R2, A3M | HOLDS | Directly from the "full delegation map structure" table. |
| Boondoggle = five questions (verification cost, stakes, distribution match, reversibility, audit-trail clarity); sorts into 3 buckets | A4R, A4M2 | HOLDS | Matches the chapter. |
| **Boondoggle Score is a validated diagnostic** | A4M2 | **HEDGED** | Chapter is explicit: it is the author's *own* instrument with *no external validation* — "heuristic, not a diagnostic." Narration says verbatim: "one engineer's heuristic, not a validated instrument." Do NOT upgrade. |
| Irreversible actions gated behind explicit human approval | A4M | HOLDS | Chapter's reversibility question. |
| Paper Summarizer: 6 steps, Claude owns 2/3/5, human owns 1/4/6; two riskiest handoffs are AI→human (3→4, 5→6); EI gap flagged | A5R, A5M, A5R2 | HOLDS | Matches the worked walkthrough and "Score summary." |
| Dropped-qualifier example: "outperformed baselines" vs "on the training set only" | A5V1–3 | HOLDS | Taken directly from the chapter's Step-4 example. |
| Overtrust = automation complacency; monitoring degrades under low signal rates; no immediate flags | A6R | VERIFY | Mechanism is well-documented in the human-automation literature — Parasuraman & Riley (1997); Lee & See (2004). Verify both citations; keep as established *mechanism*. |
| **Overtrust is the MOST COMMON failure in current AI deployments** | A6R | **HEDGED — do not assert** | Chapter explicitly refuses this: the prevalence claim is *not* established; author holds it "as a working hypothesis, not a finding." Narration mirrors this exactly ("Whether it's the most common failure in AI today, I hold as a working hypothesis, not a finding"). Any edit that makes it a claim FAILS factcheck. |
| Override 14/200 ≈ 7% vs error 6/40 ≈ 15% → overtrust | A6K, A6M2 | HOLDS (illustrative) | These are the chapter's *exercise* numbers (Application Q7), i.e. a constructed hypothetical. Narration labels it "an illustrative case" and the on-screen spec tags the numbers as an illustrative worked case. Do not present as a deployment finding. |
| The disposition/audit data is already logged; the closable gap is reading it, not collecting it | A6V, A6R2, BVDT | HOLDS | Chapter: "the field's most easily closable failure." |
| AI Use Disclosure must be granular / honest / time-stamped / tied to evidence | A6R2 | HOLDS | Directly from the Disclosure section. |

## VERIFY list (carry into Gate F)
1. **Parasuraman & Riley (1997)** — *Humans and Automation: Use, Misuse, Disuse, Abuse*, Human Factors 39(2). Confirm citation + that it grounds the complacency/misuse mechanism. (A6R)
2. **Lee & See (2004)** — *Trust in Automation: Designing for Appropriate Reliance*, Human Factors 46(1). Confirm citation + appropriate-reliance framing. (A6R)
3. **Overtrust prevalence** — confirm no source upgrades "well-documented mechanism" to "most common failure." Keep hedged. (A6R)
4. **Boondoggle Score validation status** — confirm the chapter still carries the "no external validation / heuristic" caveat in the final draft; keep narration hedged. (A4M2)

## Gate F — RUN 2026-07-23 · VERDICT: PASS (no narration changes)
1. **Parasuraman & Riley (1997)** — ✅ VERIFIED. *Human Factors* 39(2): 230–253, "Humans and Automation: Use, Misuse, Disuse, Abuse" (SAGE/HFES, DOI 10.1518/001872097778543886). The four-way taxonomy the chapter attributes to it is the paper's own title and frame. Grounds the misuse/complacency mechanism as stated. Keep as *mechanism*.
2. **Lee & See (2004)** — ✅ VERIFIED. *Human Factors* 46(1): 50–80, "Trust in Automation: Designing for Appropriate Reliance" (SAGE/HFES, DOI 10.1518/hfes.46.1.50_30392). Appropriate-reliance / calibrated-trust framing is the paper's thesis. Attribution accurate.
3. **Overtrust prevalence** — ✅ HEDGE HOLDS. Both sources establish the *mechanism* only; both predate contemporary AI deployment (1997 / 2004) and make no prevalence claim about modern AI. Chapter text refuses the prevalence claim verbatim ("a working hypothesis... not a finding"). Narration mirrors it. Do NOT upgrade — any edit to a claim FAILS.
4. **Boondoggle Score validation status** — ✅ HEDGE HOLDS. Pasted chapter carries the caveat verbatim ("The Boondoggle Score is my own instrument. I have no external validation... Treat it as a heuristic, not a diagnostic."). Narration frames it as "one engineer's heuristic, not a validated instrument." Keep.

**Gate F signature:** verified by Claude session 2026-07-23 against the pasted Ch.9 draft + live citation lookup. Human counter-sign: ____________

## Datable / promotional material stripped (DOUBLE-CHECK LAW)
- **Gru tool + URL** (`nikbearbrown.com/tools/gru-tool`, "Claude Project", `/claude` and `/v0` commands) — omitted from narration. The five questions and the score are narrated generically as method; no vendor tool, product name, or link carried into audio.
- No model version numbers, no "as of <month>" claims, no specific API/model names ("GPT-4 API" from the chapter's Disclosure sample is dropped; narration says "the AI"/"the model").
- Illustrative numbers (200/186/14/40/6) are kept only because they are explicitly constructed teaching values, and are labeled illustrative on-screen and in narration.
