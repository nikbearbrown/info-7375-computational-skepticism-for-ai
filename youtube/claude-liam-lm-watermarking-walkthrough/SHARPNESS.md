# SHARPNESS GATE — claude-liam-lm-watermarking-walkthrough

Compiled master: `claude-liam-lm-watermarking-walkthrough.mp4`
Median Laplacian variance: **304.8**
Failure threshold: 152.4 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 641.7 | 211% | PASS — 211% |
| B01 | 392.5 | 129% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 344.9 | 113% | SKIP (exempt — no pixel-art rotation possible) |
| B03 | 647.3 | 212% | PASS — 212% |
| B04 | 276.4 | 91% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 262.1 | 86% | PASS — 86% |
| B06 | 218.5 | 72% | PASS — 72% |
| B07 | 168.0 | 55% | PASS — 55% |
| B08 | 601.2 | 197% | PASS — 197% |
| B09 | 481.8 | 158% | PASS — 158% |
| B10 | 273.1 | 90% | PASS — 90% |
| B11 | 291.5 | 96% | PASS — 96% |
| B12 | 402.8 | 132% | SKIP (exempt — no pixel-art rotation possible) |
| B13 | 111.6 | 37% | PASS — 37% |
| B14 | 258.8 | 85% | SKIP (exempt — no pixel-art rotation possible) |
| B15 | 416.4 | 137% | SKIP (exempt — no pixel-art rotation possible) |
| B16 | 258.9 | 85% | PASS — 85% |
| B17 | 73.6 | 24% | PASS — 24% |
| B18 | 273.2 | 90% | SKIP (exempt — no pixel-art rotation possible) |
| B19 | 352.8 | 116% | PASS — 116% |
| B20 | 411.9 | 135% | SKIP (exempt — no pixel-art rotation possible) |
| B21 | 245.3 | 80% | SKIP (exempt — no pixel-art rotation possible) |
| B22 | 574.2 | 188% | PASS — 188% |
| B23 | 203.1 | 67% | PASS — 67% |
| B24 | 1203.2 | 395% | PASS — 395% |
| B25 | 284.6 | 93% | SKIP (exempt — no pixel-art rotation possible) |
| B26 | 669.0 | 220% | PASS — 220% |
| B27 | 269.9 | 89% | PASS — 89% |
| B28 | 1128.4 | 370% | PASS — 370% |
| B29 | 252.8 | 83% | SKIP (exempt — no pixel-art rotation possible) |
| B30 | 621.1 | 204% | PASS — 204% |
| B31 | 179.5 | 59% | PASS — 59% |
| B32 | 614.7 | 202% | PASS — 202% |
| B33 | 302.6 | 99% | SKIP (exempt — no pixel-art rotation possible) |
| B34 | 306.9 | 101% | PASS — 101% |
| B35 | 357.4 | 117% | SKIP (exempt — no pixel-art rotation possible) |
| B36 | 483.0 | 158% | PASS — 158% |
| B37 | 245.9 | 81% | SKIP (exempt — no pixel-art rotation possible) |
| B38 | 283.7 | 93% | SKIP (exempt — no pixel-art rotation possible) |
| B39 | 466.9 | 153% | SKIP (exempt — no pixel-art rotation possible) |
| B40 | 745.5 | 245% | PASS — 245% |
| B41 | 139.1 | 46% | PASS — 46% |
