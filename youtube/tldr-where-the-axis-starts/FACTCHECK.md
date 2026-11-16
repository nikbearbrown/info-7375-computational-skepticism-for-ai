# FACTCHECK — tldr-where-the-axis-starts

Status: **GATE F verified 2026-09-23 by Claude (Fable 5.1) — every ratio recomputed with exact fractions from Exercise 1's own inputs (A = 92.1, B = 94.3, floor 91, top 96); `make_sheet.py` and `scenes.py` assert the values at import. Human sign-off pending.**

Source: `chapters/10-visualization-under-validation-honest-misleading-and-the-choices-between.md` — §"The deceptive visualization catalog" (truncated axes; inconsistent axes across panels), §"Uncertainty has two faces" ("where you start the y-axis … these are choices"), §"Why this chapter" (an AI will pick a default axis), Exercises 1 and 3. Section S4 of `youtube/tldr-sections-10-visualization.md`. Everything used sits on the HEAD side or outside the chapter's four merge-conflict blocks.

| # | Beat | Claim (as spoken / shown) | Verdict | Source / derivation | Fix |
|---|---|---|---|---|---|
| 1 | B00, B01 | Course credit: chapter ten of INFO 7375, Computational Skepticism for AI, Northeastern | PASS | course-film convention (spoken + on the cards' course line) | — |
| 2 | B10, B11, B13, B19 | The chart: y-axis 91% to 96%; Model A 92.1%, Model B 94.3% | PASS | Exercise 1 verbatim: "The y-axis runs from 91% to 96% … Model A: 92.1%, Model B: 94.3%" | — |
| 3 | B10–B19 | This chart is a constructed exercise, not a documented published chart | PASS | Exercise 1 is a warm-up problem ("A colleague shows you…"); captioned "Exercise 1 · constructed values" on the stage B10–B19 | — |
| 4 | B00, B02, B10, B11 | B's bar stands three times as tall as A's | PASS | Exercise 1: "roughly three times"; recomputed (94.3 − 91)/(92.1 − 91) = 3.3/1.1 = 3 exactly | — |
| 5 | B11, B17, B18 | A bar's height is its value minus the axis floor: 1.1 and 3.3 on the 91 floor | PASS | 92.1 − 91 = 1.1; 94.3 − 91 = 3.3 (asserted) | — |
| 6 | B01, B19, B03, BVDT | The real gap is 2.2 percentage points | PASS | 94.3 − 92.1 = 2.2 (asserted) | — |
| 7 | B00, B12, B16, B18, BVDT | On a zero floor B's bar is 1.02 times A's | PASS | 94.3/92.1 = 1.02389 → 1.02 (asserted); Exercise 1 asks "What would the chart look like on a zero-baseline axis?" | — |
| 8 | B15, B16, B18 | B looks exactly twice A when the floor is 89.9 | PASS | solve (94.3 − f) = 2(92.1 − f) → f = 89.9; (94.3 − 89.9)/(92.1 − 89.9) = 4.4/2.2 = 2 (asserted) | — |
| 9 | B16 | Floor 80 → 1.18 | PASS | 14.3/12.1 = 1.1818 (asserted). 80 is the chapter's own catalog example ("starting at 80 instead of 0") | — |
| 10 | B16 | Floor 92 → B looks 23 times A | PASS | 2.3/0.1 = 23 exactly (asserted); a value recomputed from the exercise's inputs, not stated in the chapter | — |
| 11 | B17, B18, BVDT | Visual ratio = (B − floor)/(A − floor); grows without limit as the floor approaches A | PASS | algebra of bar height = value − floor; denominator → 0⁺ as floor → A⁻ while numerator → 2.2 | — |
| 12 | B17 | "Truncated axis" is the name of the move | PASS | chapter catalog item "Truncated axes. A bar chart with the y-axis starting at 80 instead of 0 makes a small difference look large." | — |
| 13 | B19, BVDT, B01 | Truncation is legitimate when the range is narrow or zero is not meaningful; stock prices are shown on truncated axes for good reason | PASS | chapter: "Legitimate uses: when the relevant range really is narrow, when zero is not meaningful … (stock prices are routinely shown on truncated axes for good reason)" | — |
| 14 | B19, BVDT | The pixels look the same either way; the choice is the difference | PASS | chapter: "The chart looks the same in both cases. The choice is the difference." | — |
| 15 | B01 | An AI will draw the chart and pick a default axis, with no stake in honesty | PASS (paraphrase) | chapter §"Why this chapter": "An AI will draw the chart. It will pick a default axis … without any stake in whether the result is honest." | — |
| 16 | B13 | "Every number is true, so the chart is honest" is the defense people give | PASS (paraphrase) | chapter Exercise 10: "My dashboard is accurate. Every number in it is true. If the reader draws wrong conclusions, that's a communication problem" | — |
| 17 | B19 | Not taught here: side-by-side panels with different floors | PASS | chapter catalog "Inconsistent axes across panels"; Exercise 3 | — |
| 18 | BHTF | Exercise 3 panels: 70–100, 85–100, 60–100; "the three groups look about the same" | PASS | Exercise 3 verbatim; the equal-fraction prediction (B > A > C) asserted in make_sheet.py for h = 1/4, 1/2, 3/4 | — |
| 19 | B03 | Definitions: axis floor, accuracy, percentage point | PASS | standard usage; 94.3 and 92.1 are 2.2 points apart (row 6) | — |
| 20 | all | Nothing datable: no model names, versions, product UIs, or "as of" claims | PASS | sweep of the sheet | — |

Deferred (density rule): Tufte's "lie factor" (not in the chapter; see BUILD-LOG manuscript note), the other seven catalog items, the stock-price instance as a drawn chart (the chapter gives no stock data — spoken only, no invented numbers), Exercise 3's panels as a drawn instance (it is the YOUR TURN).
