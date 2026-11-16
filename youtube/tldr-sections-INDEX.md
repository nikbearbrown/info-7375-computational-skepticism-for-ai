# tldr sections — Computational Skepticism for AI (book index)

**What this is.** Step one of the `tldr` skill run on all 13 canonical chapters (2026-09-23): one sections file per chapter, one card per learning section, 71 cards in all. Nothing is built. GATE S — Bear picks which cards become films; the default is one film per section.

**Why it matters before any build.** Every sections file surfaces the same manuscript problem: the chapter files carry unresolved git merge-conflict blocks (`<<<<<<< HEAD … >>>>>>> d78899b`) at figure captions and closing sections, and in several chapters a key case exists on only one side of a conflict (Ch 1 Knight Capital and the DeGrave X-ray are HEAD-only; Ch 2's Alice Markov chain is d78899b-only). Per the book's AGENTS.md the conflicts were NOT resolved; cards follow HEAD and say so. A film built from a HEAD-only case should be checked against your intended side before factcheck. Duplicate chapter files (05-data-validation, 10-delegation, 13-accountability) were treated as older copies, as the deep-explainer index did; each sections file notes what the duplicate holds that the canonical file lacks.

**Existing coverage.** Every chapter already has a `claude-liam-deep-NN-*` deep-explainer at the PLAN gate (superseded by the lecture series) and many have topic shorts. A tldr film is a different genre: one aha, taught 3Blue1Brown-style in pure Manim. Each file names its overlaps at the top.

## Recommended first pick per chapter (the top-ranked card — its representation is already a worked case, table or figure in the source)

| Ch | File | First pick | Tier | Cards | Manuscript flags |
|---|---|---|---|---|---|
| 01 | `tldr-sections-01-skeptics-toolkit.md` | S1 A Claim That Cannot Be Wrong Is Not a Claim | standard | 6 (+1 deferred) | 3 conflict blocks; Knight Capital + DeGrave HEAD-only |
| 02 | `tldr-sections-02-probability-confidence.md` | S1 The Test That Is 99% Accurate | single-insight | 5 (+2) | 6 conflict blocks; 0.0098 vs 0.0099 posterior drift |
| 03 | `tldr-sections-03-data-validation.md` | S2 Missing Is Not One Thing | single-insight | 5 (+4) | six-failures list differs across table/prose/exercise; figs 3.7/3.8 absent |
| 04 | `tldr-sections-04-robustness.md` | S4 Robust Against What? | single-insight | 4 (+2) | 13 conflict blocks; 8 [verify]; disclosure table is a template, not a measurement |
| 05 | `tldr-sections-05-explainability.md` | S1 Features Entering a Room | standard | 5 (+1) | conflict markers at every caption; 3 [verify] |
| 06 | `tldr-sections-06-bias-where-it-enters.md` | S3 Both Audits Were Right | standard | 5 (+2) | 8 conflict blocks; 2 [verify]; the three-team parable is self-labelled constructed |
| 07 | `tldr-sections-07-fairness-metrics.md` | S1 Hold One Fair, Watch the Other Break | standard | 5 | 7 conflict blocks; arithmetic tables re-checked by hand |
| 08 | `tldr-sections-08-agentic-ai.md` | S1 The Report Is Not the World | single-insight | 5 (+2) | 8 conflict blocks; 3 [verify]; "rough draft for hand-rewrite" |
| 09 | `tldr-sections-09-delegation-trust.md` | S3 Where the Human Steps Fall | standard | 5 | figs 9.2–9.4 have no image files; body vs Exercise 9 disagree on "overtrust dominant" |
| 10 | `tldr-sections-10-visualization.md` | S4 Where the Axis Starts | single-insight | 6 | 4 conflict blocks; 3 [verify]; Challenger prose/table contradict |
| 11 | `tldr-sections-11-communicating-uncertainty.md` | S2 Where the Average Hides the Patient | single-insight | 6 (+3) | 7 conflict blocks; 2 [verify]; Brier REL/CAL labels reversed vs Murphy 1973; S6 overlaps the PE book's temperature film |
| 12 | `tldr-sections-12-accountability.md` | S5 Five Boxes, One Deployment | standard | 6 (+2) | 1 [verify] (load-bearing taxonomy); fig 12.6 skipped |
| 13 | `tldr-sections-13-limits-of-ai.md` | S1 The Boundary Scaling Cannot Cross | single-insight | 5 (+2) | 3 conflict blocks; 2 [verify]; Epic Sepsis passage carries no numbers |

## How to pick
- `pick 02.S1 07.S1 11.S2` — build those, one reel each, in that order.
- `first picks` — the 13 recommended cards above, one film per chapter.
- `all` — every `status: pick` card (71 films); not recommended in one go.
- Multi-act joins (two cards sharing a key case) are listed per file and need an explicit `+`.

## Built — 2026-09-23 (GATE S: the 13 first picks)
All 13 masters cut, every gate PASS (bookend, F, A, W, B, V, T); none staged or published. Masters in `tldr-<slug>/exports/landscape/`.

| Ch | Reel | Runtime | Greeting |
|---|---|---|---|
| 01 | tldr-a-claim-that-cannot-be-wrong | 5:14 | Vanakkam |
| 02 | tldr-the-99-percent-test | 5:04 | Ahoj |
| 03 | tldr-missing-is-not-one-thing | 4:42 | Vanakkam |
| 04 | tldr-robust-against-what | 5:01 | Merhaba |
| 05 | tldr-features-entering-a-room | 5:18 | Kumusta |
| 06 | tldr-both-audits-were-right | 5:23 | Kumusta |
| 07 | tldr-hold-one-fair | 5:04 | Kumusta |
| 08 | tldr-the-report-is-not-the-world | 4:52 | Talofa |
| 09 | tldr-where-the-human-steps-fall | 5:12 | Bula |
| 10 | tldr-where-the-axis-starts | 5:21 | Jambo |
| 11 | tldr-average-hides-the-patient | 5:47 | Salaam |
| 12 | tldr-five-boxes-one-deployment | 4:52 | Sawubona |
| 13 | tldr-the-boundary-scaling-cannot-cross | 4:57 | Aloha |

Greeting repeats (parallel builders chose before central assignment): Vanakkam ×2, Kumusta ×3. Fix = new greeting on B00, regenerate B00 audio, re-render B00, `art final`.

Manuscript problems the builds exposed (each logged in its reel's BUILD-LOG; none fixed in the chapters): see each BUILD-LOG. Headline ones — ch1 never states the sepsis vendor's claim; ch1 says the turkey's model predicts a meal "on day one thousand" (one of the fed days) while ch13 has it fail on day 1,001; ch2 prints the posterior as 0.0098 and 0.0099; ch3 dates Rubin's labels 1976 in the body and 1987 in its footnote; ch4's transfer row has no ε budget; ch5's debt/zip shares have no table and income appears as 0.073, +0.18 and +0.3; ch6 frames the base-rate identity as needing calibration; ch7's "same model" tables can't be the same model; ch8's opener makes Ash the owner and its responsibility section says the whole server was deleted; ch9's Exercise 9 contradicts the body; ch10's Exercise 1 ratio is ambiguous (3.0 vs ~84); ch11's subgroup table flags pediatric against its own rule and its base rate doesn't reconcile; ch12's exercise renames the five requirements. Missing figure images: 3.2, 8.1, 8.6, 8.11, 9.2–9.4, 13.1, 13.2. Unresolved merge-conflict blocks remain in chapters 1, 2, 4–8, 10, 11, 13.
