# Chapter problems found while building the terminology decks

Found 2026-11-10 by the deck builders. Nothing in the chapters was changed. Chapter numbers follow the course README (files `03-`, `09-`, `12-` are the live ones; `05-data-validation`, `10-delegation`, `13-accountability` are stale duplicates).

**Merge-conflict markers (`<<<<<<<`) still in the chapter file:** 2, 4, 5, 6, 7, 8, 10, 11, 13. Several also have duplicate or stale figure numbers (5.x/6.x, "Figure 3.x" in 6, 9.x in 8, 11/12 in 11, 13.3 to 14.2 in 13) and two conflicting "Preview of next chapter" blocks (5).

**Numbers and claims to check**
- Ch 1: the capacity table maps capacities to Ch. 3, 4, 6, 8, 13, which looks stale. Netflix 2017 and Gomez-Uribe claims are unchecked (the review deck says so too).
- Ch 2: posterior 0.0098 in the formula, 0.0099 in the table. "Twelve points" independence gap is 11.7. The Casscells "two orders of magnitude" line is nearer 1.5. The "factory revisited" section refers to examples the kept text no longer has.
- Ch 3: "six" silent failures, but the table and prose also cover a seventh-like row (missing data, MNAR). "Mark" is never defined.
- Ch 4: figures tagged [verify]: about 9x adversarial-training cost, 10^30 FLOPs (still stated unhedged in one place), Lipschitz bound "as low as 6".
- Ch 5: TreeSHAP written O(TLD); the literature and the review deck say O(TLD^2). KernelSHAP called "Monte Carlo sampling" (it is weighted regression); "10 permutations by default" unchecked. Worked values sum to 0.1703, shown as 0.170. The exam compact list says LIME and SHAP are not on the exam.
- Ch 6: "three flavors" versus the review deck's four; the flavor table says "structural amplification" where the prose says publication bias. Agents of Chaos Kimi detail and Hardt and Madras citations are [verify].
- Ch 7: the second table gives B threshold 0.6 and A 0.5 on "the same model", yet B's positive rate rises 0.28 to 0.32. The COMPAS 44.9% and 23.5% come from the review deck and ProPublica; the chapter says "about 2x".
- Ch 8: Case #4 relay "about 60,000 tokens over nine days" versus "about an hour" in the review deck. The agent "deleted the owner's entire mail server" in one place, only wiped the local client elsewhere. Case #7: Ash complied with each demand, then refused to delete MEMORY.md. "Three" and "four" multi-agent failure modes both appear. Mirsky L2/L4 is [verify].
- Ch 9: Exercise 9 and the Overtrust section say overtrust is "dominant"; the chapter holds it only as a working hypothesis. The Paper Summarizer disclosure says "GPT-4 API" though the walkthrough uses Claude; disclosure examples lack the timestamps the chapter requires.
- Ch 10: the compact exam list marks it not on the exam. Catalonia poll unsourced; perception-rank error percentages unverified. "99 out of 1,000" false positives should be 99 of 990 (8.3%). The opening example says truncated axes "squeeze" disparity; the catalog says they amplify.
- Ch 11: the subgroup table flags Pediatric, but 0.029 is only 1.6x the global 0.018 (3 of 5 groups pass 2x, not the review deck's four). Subgroup base rates weight to about 0.044, not 0.041. Brier 0 means perfect predictions, not "perfect calibration". The exam list quotes "spread of the data" for aleatoric uncertainty; that phrase is not in the chapter. Unsourced: Epic "clinician suspicion", "dominant failure mode in medical AI". [verify]: ECE thresholds, the Guo and Minderer extension to LLMs.
- Ch 12: the Irreducibly Human tier taxonomy is an unpublished, uncheckable source (the chapter says so). No heading "A small experiment".
- Ch 13: the compact exam list marks it not on the exam, to be confirmed in class. "94%" accuracy recomputes to 93.9%. No numbers given for the Epic Sepsis Model. [verify]: expected calibration-baseline ranges.
