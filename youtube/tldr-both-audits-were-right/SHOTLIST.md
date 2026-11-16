# SHOTLIST — tldr-both-audits-were-right
Typed work order per slot. Every slot is pipeline-owned: **zero human media, zero pantry, zero gen-AI** (tldr rule 6). Every rate on screen is recomputed from the constructed 20-per-group population at the chapter's base rates (30% / 50%) and asserted in `make_sheet.py` / `scenes.py`.

| Beat | Role | Type × source | Owner | What it is |
|---|---|---|---|---|
| B00 | TL;DR · WHAT | REMOTION own (bookend) | pipeline | ClaudeTldrWhat — "Kumusta, Liam"; the question writes on; three numbered lines land on their clauses |
| B01 | TL;DR · WHY | REMOTION own (bookend) | pipeline | ClaudeTldrWhy — the stake writes on; three dashed consequences land |
| B02 | THE QUESTION | REMOTION own (bookend) | pipeline | BrutalistHesitantWriter — "Which audit got it wrong" → "How can both be right" (phrase trigger) |
| B03 | TERMS | REMOTION own (card) | pipeline | ClaudeDefinitions — base rate · calibrated · false positive rate · false negative rate |
| B10 | HOOK | GRAPHIC own | Manim `B10_TwoHeadlines` | forty grey dots; ProPublica "biased" and Northpointe "fair" both drawn onto the same dots; "which one is wrong?" |
| B11 | INSTANCE | GRAPHIC own | Manim `B11_GroupOne` | group one's 20 dots: six darken (30%); two boxes; 3 of 5 high (60%), 3 of 15 low (20%); "constructed" caption |
| B12 | INSTANCE | GRAPHIC own | Manim `B12_GroupTwo` | group two: ten darken (50%); 9 of 15 high (60%), 1 of 5 low (20%); four checks; "Northpointe: calibrated" |
| B13 | NAIVE | GRAPHIC own | Manim `B13_RedoTheCount` | "did ProPublica fudge it?"; reoffenders ghost; false positives 2 of 14 vs 6 of 10; X beside "fudge" |
| B14 | SHIFT | GRAPHIC own | Manim `B14_TwoFilters` | the same dots through Northpointe's filter (the box) and ProPublica's (the outcome); misses 3 of 6 vs 1 of 10 |
| B15 | INSTANCE · predict | GRAPHIC own | Manim `B15_Commit` | false-positive bars with group one's level as a guide on group two's track; "hold 60%: equal false positives?"; hold |
| B16 | TRANSFORM | GRAPHIC own | Manim `B16_MoveTheDots` | four grey dots walk from high to low in group two: FP 6/10 → 2/10 while the high box climbs 60 → 82%; X beside 82% |
| B17 | ABSTRACTION | GRAPHIC own | Manim `B17_TheLine` | v/(1−v) = p/(1−p)·t/f in MathTex, referents beneath; plug-ins 1.5 = 3/7·3.5 and 1.5 = 1·1.5; "unequal base rates: not both" |
| B18 | TANGENT | GRAPHIC own | Manim `B18_ReadTheLine` | split stage: equation left, five zones right; two ways out: p_a = p_b, or t = 1, f = 0 |
| B19 | PAYOFF | GRAPHIC own | Manim `B19_BothRight` | the HOOK's headlines and forty dots return (now coloured); each audit's number with a check; "both right: different denominators"; boundary caption |
| BVDT | VERDICT | REMOTION own (bookend) | pipeline | ClaudeVerdictArtifact — four lines |
| BHTF | YOUR TURN | REMOTION own (bookend) | pipeline | ClaudeComposerAsk "Your turn." — the hypothetical readmission-flag audit pair, read in full |
| BOUT | OUTRO | REMOTION own (bookend) | pipeline | ClaudeTitleOutro — spoken title + "At Nik Bear Brown", 1.0 s tail, no jingle |
