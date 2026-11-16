# PROMPTS — claude-liam-dashboard-that-lied
## Pantry image generation prompts (Gate D2 · all Tier 1)

Five pantry files are needed — all Tier 1 generated per SHOPPING.md.
Generate via the ai-asset-gen skill (Higgsfield GPT Image 2 or equivalent).
Output to `pantry/` at ≥2000px (≥2800px wide for vox-run plates).

---

### B02 — pantry/B02.png
**Window:** 14.45s · Ken Burns push toward the glowing screen

**Prompt:**
A corporate conference room in near-darkness, team silhouettes seated facing a large wall monitor displaying a rising line chart rendered in vivid green. The room atmosphere is intimate and tense — the glow of the screen is the only significant light source, casting green light across the table. Editorial photorealistic style, neutral color grade except for the screen glow. No faces visible; figures in silhouette. Wide cinematic framing, plenty of headroom and foreground table for Ken Burns push. 1920×1080 minimum, ≥2000px on long edge.

**Ken Burns target:** slow push toward the glowing screen (focus x=0.55, y=0.42)

---

### B05 — pantry/B05.png
**Window:** 13.9s · Ken Burns drift across the open page

**Prompt:**
A printed investor deck lying open on a polished boardroom table, photographed from above at a slight angle. The open page shows a clear rising line chart printed in green. Empty chairs visible around the table. Neutral cold-office lighting. The chart page should be large and legible as the main subject. Editorial photorealistic, no people, no faces. Extra width so the Ken Burns drift can cross the page. 1920×1080 minimum, ≥2000px on long edge.

**Ken Burns target:** slow drift across the open deck page (focus x=0.48, y=0.5)

---

### B07 / B08 — pantry/B07.png  *(ONE plate serves both beats)*
**Window:** B07 = 15.05s · B08 = 15.34s · Ken Burns: tight → pull out
**Minimum width:** ≥2800px (camera eases from tight crop to full store view)

**Prompt:**
A large department-store window covered densely with red promotional signage — SALE, 50% OFF, CLEARANCE, percent-off tags on every pane and display. Tight framing fills the frame edge to edge with red promotional text. The scene should be WIDE enough that pulling out reveals the entire storefront is saturated with promotions — every aisle, every window, every rack labeled. Photorealistic editorial style, strong red accent on promotional tags, neutral surrounding retail environment. No people visible. Shot wide enough that the left-side tight crop and a pulled-out full-store view are both useful. ≥2800px wide minimum.

**Vox run R1 handoff:** B07 holds tight on red SALE tags (focus x=0.45, y=0.45, scale 1.9); B08 eases OUT to reveal the full promotional world.

---

### B19 — pantry/B19.png
**Window:** 13.61s · Ken Burns push down the aisle

**Prompt:**
A vast server room / enterprise data center corridor — rows of black server racks receding to a vanishing point under cold fluorescent light. The aisle is clean, orderly, and mechanical. The scale should feel enormous — the corridor seems to extend forever. No people. Cold blue-white light, neutral editorial grade. Plenty of depth for Ken Burns push down the central aisle. 1920×1080 minimum, ≥2000px on long edge.

**Ken Burns target:** slow push down the aisle toward the vanishing point (focus x=0.5, y=0.5)

---

### B23 / B24 — pantry/B23.png  *(ONE plate serves both beats)*
**Window:** B23 = 13.15s · B24 = 16.44s · Ken Burns: tight → pull out
**Minimum width:** ≥2800px (camera eases from tight crop to full floor view)

**Prompt:**
A financial trading floor with a dense wall of multiple monitors showing flickering numbers, charts, and financial data. Tight crop fills the frame with the screen glow and numerical data streams. The scene should be WIDE enough to also reveal the full floor when pulled out — rows of monitors, multiple trading stations, no humans visible in the frame (empty floor). Screen glow is the dominant light. Editorial photorealistic, cold blue/green screen light against dark surroundings. ≥2800px wide minimum.

**Vox run R2 handoff:** B23 holds tight on the flickering numbers (focus x=0.5, y=0.45, scale 1.9); B24 eases OUT to reveal the full unmanned trading floor.

---

## Usage notes

- All five prompts are Tier 1 (AI-generated); no rights escalations required.
- Vox treatment (applied by pipeline): desaturate ~80%, contrast ~1.15, cream-stage overlay, grain.
- Vox-run plates (B07, B23) must survive tight-crop AND wide-pull Ken Burns — generate at ≥2800px wide.
- Drop files directly into `pantry/` at the slugged path; the pipeline reads them by filename.
