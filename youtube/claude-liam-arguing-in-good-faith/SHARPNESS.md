# SHARPNESS GATE — claude-liam-arguing-in-good-faith

Compiled master: `claude-liam-arguing-in-good-faith.mp4`
Median Laplacian variance: **375.6**
Failure threshold: 187.8 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 459.6 | 122% | PASS — 122% |
| B01 | 199.8 | 53% | SKIP (exempt — no pixel-art rotation possible) |
| B02 | 340.4 | 91% | PASS — 91% |
| B03 | 410.8 | 109% | PASS — 109% |
| B04 | 433.2 | 115% | PASS — 115% |
| B05 | 195.8 | 52% | SKIP (exempt — no pixel-art rotation possible) |
| B06 | 450.2 | 120% | PASS — 120% |
| B07 | 259.2 | 69% | SKIP (exempt — no pixel-art rotation possible) |
| B08 | 536.2 | 143% | PASS — 143% |
| B09 | 301.5 | 80% | SKIP (exempt — no pixel-art rotation possible) |
| B10 | 442.0 | 118% | PASS — 118% |
| B11 | 234.3 | 62% | SKIP (exempt — no pixel-art rotation possible) |
| B12 | 255.8 | 68% | SKIP (exempt — no pixel-art rotation possible) |
| BVDT | 552.2 | 147% | PASS — 147% |
| BHTF | 692.2 | 184% | PASS — 184% |
| BOUT | 140.3 | 37% | PASS — 37% |
