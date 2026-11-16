# SHARPNESS GATE — claude-liam-deep-test-you-did-not-design

Compiled master: `claude-liam-deep-test-you-did-not-design-slate.mp4`
Median Laplacian variance: **397.3**
Failure threshold: 198.7 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 718.3 | 181% | PASS — 181% |
| B01 | 193.4 | 49% | PASS — 49% |
| A1C | 152.0 | 38% | SKIP (exempt — no pixel-art rotation possible) |
| A1R | 574.6 | 145% | PASS — 145% |
| A1K | 505.1 | 127% | PASS — 127% |
| A1M | 480.6 | 121% | PASS — 121% |
| A1V | 407.9 | 103% | SKIP (exempt — no pixel-art rotation possible) |
| A1M2 | 303.0 | 76% | PASS — 76% |
| A2C | 160.3 | 40% | SKIP (exempt — no pixel-art rotation possible) |
| A2R | 325.1 | 82% | PASS — 82% |
| A2M | 393.2 | 99% | PASS — 99% |
| A2R2 | 629.7 | 158% | PASS — 158% |
| A2V1 | 162.7 | 41% | SKIP (exempt — no pixel-art rotation possible) |
| A2V2 | 108.1 | 27% | SKIP (exempt — no pixel-art rotation possible) |
| A2M2 | 401.5 | 101% | PASS — 101% |
| A2M3 | 447.1 | 113% | PASS — 113% |
| A3C | 139.6 | 35% | SKIP (exempt — no pixel-art rotation possible) |
| A3V1 | 469.7 | 118% | PASS — 118% |
| A3R | 528.3 | 133% | PASS — 133% |
| A3V2 | 441.3 | 111% | PASS — 111% |
| A3R2 | 537.5 | 135% | PASS — 135% |
| A3M | 265.6 | 67% | PASS — 67% |
| A4C | 134.0 | 34% | SKIP (exempt — no pixel-art rotation possible) |
| A4M | 354.8 | 89% | PASS — 89% |
| A4V | 150.7 | 38% | SKIP (exempt — no pixel-art rotation possible) |
| A4R | 652.6 | 164% | PASS — 164% |
| A4R2 | 995.2 | 250% | PASS — 250% |
| A5C | 138.4 | 35% | SKIP (exempt — no pixel-art rotation possible) |
| A5R | 479.4 | 121% | PASS — 121% |
| A5V | 440.5 | 111% | SKIP (exempt — no pixel-art rotation possible) |
| A5M | 318.9 | 80% | PASS — 80% |
| A5R2 | 449.5 | 113% | PASS — 113% |
| A6C | 151.8 | 38% | SKIP (exempt — no pixel-art rotation possible) |
| A6K | 283.9 | 71% | PASS — 71% |
| A6M | 290.7 | 73% | PASS — 73% |
| A6R | 442.9 | 111% | PASS — 111% |
| A6M2 | 294.9 | 74% | PASS — 74% |
| BVDT | 588.3 | 148% | PASS — 148% |
| BHTF | 729.5 | 184% | PASS — 184% |
| BOUT | 274.2 | 69% | PASS — 69% |
