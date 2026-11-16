# AUDIT.md — claude-liam-cs-07-turkeys-model
**Topic**: Why the Turkey's Model Was Perfect Until Thanksgiving
**STD Retrofit Date**: 2026-07-25

## Beat Classification

| Beat | ID | Classification | Reason |
|------|----|---------------|--------|
| B00 | intro | EXEMPT | Bookend — Remotion, not animatable |
| B01 | hook title | TELLS→SHOWS | Static text → Manim title reveal |
| B02 | hook scene | TELLS→SHOWS | Narration describes mechanism — animated |
| B03 | composer ask | EXEMPT | ClaudeComposerAsk — Remotion component |
| B04 | mechanism explanation | TELLS→SHOWS | Narration enacts concept with animation |
| B05 | mechanism deepening | TELLS→SHOWS | Narration describes process — animated |
| B06 | result | EXEMPT | ClaudeWindow — Remotion component |
| B07 | KEY ANIMATION | TELLS→SHOWS | **TERRACOTTA MOMENT** — highest-impact beat |
| B08 | named mechanism | TELLS→SHOWS | Technical term shown as diagram |
| B09 | AI implication | TELLS→SHOWS | Implication shown structurally |
| B10 | implication quote | TELLS→SHOWS | Quote shown with visual framing |
| B11 | the fix | TELLS→SHOWS | Checklist / fix steps animated |
| B12 | worked example | TELLS→SHOWS | Domain example visualized |
| B13 | handoff | EXEMPT | HANDOFF beat — Remotion |
| B14 | your turn | EXEMPT | Remotion component |
| B15 | outro | EXEMPT | ClaudeTitleOutro — Remotion |

## TELLS Beats Rebuilt as Manim
- B01, B02, B04, B05, B07, B08, B09, B10, B11, B12 — all rebuilt in scenes.py

## EXEMPT Beats (no animation needed)
- B03: ClaudeComposerAsk (Remotion)
- B06: ClaudeWindow / result (Remotion)
- B13: HANDOFF narration (Remotion)
- B14: Your Turn (Remotion)
- B15: ClaudeTitleOutro (Remotion)

## Terracotta Moment
**B07_KeyAnimation** — One `ACCENT = "#D97757"` accent used as the join/filter/threshold highlight.

## Production Notes
- All audio frozen — no MP3 regeneration
- Palette: CREAM `#F2F0E9`, INK `#3D3929`, ACCENT `#D97757`, MUTE `#7A7265`, TEAL `#2A9D8F`, CRIMSON `#C1121F`
- Font: EB Garamond serif (primary), Montserrat caps (labels)
- Safe zone: 5% inset (96–1824 x 54–1026 px)
- Render: `python3 -m manim scenes.py <ClassName> --format mp4 -r 1920,1080 --fps 30 -ql`
