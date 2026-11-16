# SHARPNESS GATE — claude-liam-ra-01-dangerous-shape-and-domain

Compiled master: `claude-liam-ra-01-dangerous-shape-and-domain-slate.mp4`
Median Laplacian variance: **787.8**
Failure threshold: 393.9 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 620.4 | 79% | PASS — 79% |
| B01 | 767.3 | 97% | PASS — 97% |
| B02 | 857.7 | 109% | PASS — 109% |
| B03 | 787.8 | 100% | PASS — 100% |
| BVDT | 947.2 | 120% | PASS — 120% |
| BHTF | 823.9 | 105% | PASS — 105% |
| BOUT | 231.9 | 29% | PASS — 29% |
