# SHARPNESS GATE — claude-liam-cli-adversarial-perturbation-detector

Compiled master: `claude-liam-cli-adversarial-perturbation-detector-slate.mp4`
Median Laplacian variance: **701.7**
Failure threshold: 350.9 (50% of median)

> Soft beats = rotation applied to `crispEdges` pixel-art.
> Fix: use translation/scale only — never rotate. See PIXEL-ART LAW in
> `ClaudeMascotScene.tsx`.

| Beat | LV | % of median | Status |
|------|----|-------------|--------|
| B00 | 481.2 | 69% | PASS — 69% |
| B01 | 351.7 | 50% | PASS — 50% |
| B02 | 705.2 | 101% | PASS — 101% |
| B03 | 701.7 | 100% | PASS — 100% |
| B04 | 391.4 | 56% | PASS — 56% |
| B05 | 764.7 | 109% | PASS — 109% |
| B06 | 391.8 | 56% | PASS — 56% |
| B07 | 296.7 | 42% | PASS — 42% |
| B08 | 313.3 | 45% | PASS — 45% |
| BVDT | 729.7 | 104% | PASS — 104% |
| BHTF | 941.5 | 134% | PASS — 134% |
| B09 | 960.4 | 137% | PASS — 137% |
| BOUT | 966.1 | 138% | PASS — 138% |
