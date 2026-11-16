# STATUS — claude-liam-two-models-twice-the-price

41/41 beats filled. Derived from beat_sheet.json — edit the sheet, not this file.

---

## FIX — 2026-07-29 — text-layout bug repair (B26, B27)

**Shared root cause:** `bar()` in `B26_CostBars` positioned axis labels at the bar's
own x-center without accounting for label width (1.525–1.680 Manim units). With bar
centers only 1.3 units apart, labels physically overlapped in both Scenario A and B,
producing "cheaper/tokpremium/token". The same geometric oversight caused the other
two symptoms: the B26 caption split at its em-dash boundary was too narrow (Georgia's
'a'→consonant sidebearing ≈ 9.7 px, inter-word space ≈ 11.3 px — indistinguishable
after H.264 downscale), and the B27 `tag_note` at y=−0.45 sat inside the box
(bottom at y=−0.5), letting the INK stroke paint through the space between "one"
and "number".

**Changes in scenes.py:**
- `B26_CostBars` — increased bar-pair x-center separation from 1.3 → 2.0 Manim units:
  Scenario A: cheap=−4.85 / premium=−2.85 (was −4.5/−3.2)
  Scenario B: cheap=+1.85 / premium=+3.85 (was +2.2/+3.5)
  Scenario labels remain centred at midpoints (−3.85, +2.85) — no change needed.
- `B26_CostBars` caption — replaced single long Text() with a two-part VGroup
  (split at the em-dash, buff=0.22 ≈ 60 px at 4K) to make the phrase boundary
  unambiguous at any playback resolution.
- `B27_ReceiptVsSticker` `tag_note` — moved from y=−0.45 to y=−0.72 (0.22 units
  below box bottom at y=−0.5); stray border line and "onenumber" collapse eliminated.

**Beats re-rendered:** B26, B27 (4K / 3840×2160 / Manim -qk)
**Other beats:** untouched.

| beat | status | fill method | who | slot | suggested prompt / search |
|---|---|---|---|---|---|
| B00 | ✅ filled | remotion | pipeline | `media/B00.mp4` |  |
| B01 | ✅ filled | remotion | pipeline | `media/B01.mp4` |  |
| B02 | ✅ filled | remotion | pipeline | `manim/B02.mp4` |  |
| B03 | ✅ filled | remotion | pipeline | `manim/B03.mp4` |  |
| B04 | ✅ filled | remotion | pipeline | `media/B04.mp4` |  |
| B05 | ✅ filled | remotion | pipeline | `manim/B05.mp4` |  |
| B06 | ✅ filled | remotion | pipeline | `media/B06.mp4` |  |
| B07 | ✅ filled | remotion | pipeline | `media/B07.mp4` |  |
| B08 | ✅ filled | remotion | pipeline | `media/B08.mp4` |  |
| B09 | ✅ filled | remotion | pipeline | `manim/B09.mp4` |  |
| B10 | ✅ filled | remotion | pipeline | `manim/B10.mp4` |  |
| B11 | ✅ filled | remotion | pipeline | `media/B11.mp4` |  |
| B12 | ✅ filled | remotion | pipeline | `media/B12.mp4` |  |
| B13 | ✅ filled | remotion | pipeline | `manim/B13.mp4` |  |
| B14 | ✅ filled | remotion | pipeline | `manim/B14.mp4` |  |
| B15 | ✅ filled | remotion | pipeline | `manim/B15.mp4` |  |
| B16 | ✅ filled | remotion | pipeline | `manim/B16.mp4` |  |
| B17 | ✅ filled | remotion | pipeline | `media/B17.mp4` |  |
| B18 | ✅ filled | remotion | pipeline | `media/B18.mp4` |  |
| B19 | ✅ filled | remotion | pipeline | `manim/B19.mp4` |  |
| B20 | ✅ filled | remotion | pipeline | `manim/B20.mp4` |  |
| B21 | ✅ filled | remotion | pipeline | `media/B21.mp4` |  |
| B22 | ✅ filled | remotion | pipeline | `manim/B22.mp4` |  |
| B23 | ✅ filled | remotion | pipeline | `media/B23.mp4` |  |
| B24 | ✅ filled | remotion | pipeline | `media/B24.mp4` |  |
| B25 | ✅ filled | remotion | pipeline | `manim/B25.mp4` |  |
| B26 | ✅ filled | remotion | pipeline | `manim/B26.mp4` |  |
| B27 | ✅ filled | remotion | pipeline | `manim/B27.mp4` |  |
| B28 | ✅ filled | remotion | pipeline | `manim/B28.mp4` |  |
| B29 | ✅ filled | remotion | pipeline | `media/B29.mp4` |  |
| B30 | ✅ filled | remotion | pipeline | `media/B30.mp4` |  |
| B31 | ✅ filled | remotion | pipeline | `manim/B31.mp4` |  |
| B32 | ✅ filled | remotion | pipeline | `manim/B32.mp4` |  |
| B33 | ✅ filled | remotion | pipeline | `manim/B33.mp4` |  |
| B34 | ✅ filled | remotion | pipeline | `media/B34.mp4` |  |
| B35 | ✅ filled | remotion | pipeline | `media/B35.mp4` |  |
| B36 | ✅ filled | remotion | pipeline | `manim/B36.mp4` |  |
| B37 | ✅ filled | remotion | pipeline | `media/B37.mp4` |  |
| BVDT | ✅ filled | remotion | pipeline | `media/BVDT.mp4` |  |
| BHTF | ✅ filled | remotion | pipeline | `media/BHTF.mp4` |  |
| BOUT | ✅ filled | remotion | pipeline | `media/BOUT.mp4` |  |
