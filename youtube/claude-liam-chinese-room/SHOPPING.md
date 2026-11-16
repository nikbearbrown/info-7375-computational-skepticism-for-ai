# SHOPPING — claude-liam-chinese-room (Gate D2)

Duration-locked after audio. Six pantry stills needed — drop as `<BID>.png` into `pantry/`.
Tier governs rights handling. Tier 1 = free to generate or find stock. Tier 2 = verify object
rights before use. Tier 3 = archival photograph of a real person — rights check escalates to human.

| BID | Duration | Tier | Asset | Source guidance |
|---|---|---|---|---|
| A2 | 14.19s | 3 | Alan Turing portrait (c. 1950 era) | Archival photo. Well-known options: the 1951 Elliot & Fry portrait is widely reproduced. Confirm licensing before use — rights check to human. |
| A3 | 11.01s | 1 | Vintage teletype / paper-tape terminal (generic) | Generic machine, no person needed. Stock or AI-generated fine. AI: disclosure sidecar required. |
| A7 | 11.71s | 3 | John Searle portrait (c. 1980 era) | Archival photo. Academic or book-jacket shot preferred. Rights check to human before use. |
| A8 | 8.58s | 2 | "Minds, Brains, and Programs" — *Behavioral and Brain Sciences* 3(3), 1980 | Journal cover or first-page scan. Verify the item's rights (scholarly fair-use vs. publisher restrictions). Object shot only — no text extraction. |
| A25 | 10.45s | 1 | Person at a terminal / typing at a screen (generic) | No real person needed; stock or AI-generated fine. If AI: add disclosure sidecar (`A25.source.txt` → `generated: true`). |
| A28 | 10.35s | 1 | Vast compute / server racks at scale (generic) | Generic infrastructure image. Stock or AI fine. If AI: disclosure sidecar. |

## Pantry intake
After dropping each file into `pantry/`:

```bash
./brutalist-art/art pantry computational-skepticism-for-ai/youtube/claude-liam-chinese-room
```

Then set `shot.focus` on each beat in `beat_sheet.json` and fill `.source.txt` sidecars in `media/`.

## Gate D2 — signed
Written after audio lock (2026-07-22). Durations above are ground truth.
