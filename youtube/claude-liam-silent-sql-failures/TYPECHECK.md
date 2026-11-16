# TYPECHECK.md — GATE T

Reel: `claude-liam-silent-sql-failures`  |  Checked: 2026-07-24T13:57  |  Overall: **FAIL**  |  Beats checked: 33  |  FAILs: 7

Spec: `skills/make/kerning/reference/type-spec.md` §8.  Floor: 3.2% frame-height.  Contrast: 4.5:1 WCAG.  Kern threshold: 2.5× expected advance.  Wordy budget: 2 elements.

| beat | lane | worst finding | status | fix |
|------|------|---------------|--------|-----|
| B00 | ? | no video | SKIP | — |
| A1C | ? | no video | SKIP | — |
| A1R | ? | no video | SKIP | — |
| A1M | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A1R2 | ? | no video | SKIP | — |
| A1V | ? | no video | SKIP | — |
| A2C | ? | no video | SKIP | — |
| A2M | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A2R | ? | no video | SKIP | — |
| A2V | ? | no video | SKIP | — |
| A3C | ? | no video | SKIP | — |
| A3R | ? | no video | SKIP | — |
| A3M | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A3M2 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A3R2 | ? | no video | SKIP | — |
| A3V | ? | no video | SKIP | — |
| A4C | ? | no video | SKIP | — |
| A4M | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A4R | ? | no video | SKIP | — |
| A4V | ? | no video | SKIP | — |
| A5C | ? | no video | SKIP | — |
| A5R | ? | no video | SKIP | — |
| A5M | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A5V | ? | no video | SKIP | — |
| A5M2 | ? | contrast §8.3: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must s… | **FAIL** | Use INK on cream; add backing plate under accent text |
| A5R2 | ? | no video | SKIP | — |
| A6C | ? | no video | SKIP | — |
| A6M | ? | no-wordy-card §8.5: no prose payload found | PASS | — |
| A6R | ? | no video | SKIP | — |
| A6V | ? | no video | SKIP | — |
| BVDT | ? | no video | SKIP | — |
| BHTF | ? | no video | SKIP | — |
| BOUT | ? | no video | SKIP | — |

---

## Failures requiring action before cut

### A1M (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A2M (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A3M (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A3M2 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A4M (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A5M (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

### A5M2 (?)
- **contrast §8.3**: terracotta accent #D97757 on cream 2.74:1 < 4.5:1 WCAG — accent text must switch to INK #3D3929 or carry a backing plate
- **Fix:** Use INK on cream; add backing plate under accent text

---

## Check summary

| Check | Beats checked | FAILs |
|-------|---------------|-------|
| no-wordy-card §8.5 | 8 | 0 |
| min-size §8.1 | 8 | 0 |
| overflow §8.2 | 8 | 0 |
| contrast §8.3 | 8 | 7 |
| kerning §8.4 | 8 | 0 |

---

*GATE T: any FAIL blocks `./art run` and `./art final`. Fix the flagged beats and re-run `scripts/type_check.py` until green.*
