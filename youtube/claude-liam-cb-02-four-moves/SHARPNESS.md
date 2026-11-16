# SHARPNESS GATE — claude-liam-cb-02-four-moves

Compiled master: `claude-liam-cb-02-four-moves-slate.mp4`
Median Laplacian variance: **946.1**
Failure threshold: 473.1 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 916.6 | 97% | PASS — 97% |
| B01 | 975.7 | 103% | PASS — 103% |
| B02 | 986.0 | 104% | PASS — 104% |
| B03 | 986.0 | 104% | PASS — 104% |
| B04 | 986.0 | 104% | PASS — 104% |
| BVDT | 455.4 | 48% | PASS — 48% |
| BHTF | 457.8 | 48% | PASS — 48% |
| BOUT | 461.2 | 49% | PASS — 49% |
