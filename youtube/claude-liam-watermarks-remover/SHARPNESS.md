# SHARPNESS GATE — claude-liam-watermarks-remover

Compiled master: `claude-liam-watermarks-remover.mp4`
Median Laplacian variance: **336.2**
Failure threshold: 168.1 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 426.7 | 127% | PASS — 127% |
| B01 | 277.8 | 83% | PASS — 83% |
| B02 | 526.3 | 157% | PASS — 157% |
| B03 | 430.3 | 128% | SKIP (exempt — no pixel-art rotation possible) |
| B04 | 282.5 | 84% | SKIP (exempt — no pixel-art rotation possible) |
| B05 | 196.5 | 58% | PASS — 58% |
| B06 | 258.2 | 77% | PASS — 77% |
| B07 | 389.3 | 116% | PASS — 116% |
| B08 | 312.5 | 93% | SKIP (exempt — no pixel-art rotation possible) |
| B09 | 292.1 | 87% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 255.3 | 76% | PASS — 76% |
| B11 | 343.5 | 102% | PASS — 102% |
| B12 | 250.0 | 74% | PASS — 74% |
| B13 | 258.6 | 77% | SKIP (exempt — no pixel-art rotation possible) |
| B14 | 467.6 | 139% | SKIP (exempt — no pixel-art rotation possible) |
| B15 | 200.7 | 60% | PASS — 60% |
| B16 | 76.1 | 23% | PASS — 23% |
| B17 | 305.6 | 91% | PASS — 91% |
| B18 | 352.3 | 105% | SKIP (exempt — no pixel-art rotation possible) |
| B19 | 336.2 | 100% | SKIP (exempt — no pixel-art rotation possible) |
| B20 | 227.6 | 68% | PASS — 68% |
| B21 | 1303.4 | 388% | PASS — 388% |
| B22 | 302.7 | 90% | SKIP (exempt — no pixel-art rotation possible) |
| B23 | 498.8 | 148% | SKIP (exempt — no pixel-art rotation possible) |
| B24 | 407.4 | 121% | SKIP (exempt — no pixel-art rotation possible) |
| B25 | 215.0 | 64% | SKIP (exempt — no pixel-art rotation possible) |
| B26 | 382.4 | 114% | SKIP (exempt — no pixel-art rotation possible) |
| B27 | 381.9 | 114% | SKIP (exempt — no pixel-art rotation possible) |
| B28 | 211.8 | 63% | PASS — 63% |
| B29 | 682.8 | 203% | PASS — 203% |
| B30 | 341.7 | 102% | SKIP (exempt — no pixel-art rotation possible) |
| B31 | 344.3 | 102% | SKIP (exempt — no pixel-art rotation possible) |
| B32 | 221.0 | 66% | PASS — 66% |
| B33 | 1031.6 | 307% | PASS — 307% |
| B34 | 317.1 | 94% | SKIP (exempt — no pixel-art rotation possible) |
| B35 | 323.5 | 96% | SKIP (exempt — no pixel-art rotation possible) |
| B36 | 348.9 | 104% | SKIP (exempt — no pixel-art rotation possible) |
| BSRC | 852.2 | 253% | PASS — 253% |
| BVDT | 720.8 | 214% | PASS — 214% |
| BHTF | 406.3 | 121% | PASS — 121% |
| BOUT | 121.4 | 36% | PASS — 36% |
