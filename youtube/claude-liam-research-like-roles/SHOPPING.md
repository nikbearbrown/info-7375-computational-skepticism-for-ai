# SHOPPING.md — Research-Like Roles
**Gate D2 — written after audio lock (2026-07-24)**  
**Reel:** claude-liam-research-like-roles | **Total runtime:** ~387s (6:27)

All pantry assets are Tier 1 (generic/illustrative — AI-generated; no real persons, no specific named places). No rights escalation required.

---

## Asset manifest

| Beat | Duration | File needed | Tier | Prompt summary | Status |
|------|----------|-------------|------|----------------|--------|
| B02 | 15.17s | pantry/B02.png | 1 | Abstract wall of job listings / posting cards on screens, blurred, cool office light, no readable text | ☐ NEEDED |
| B03 | 15.57s | pantry/B03.png | 1 | Small team 2–3 people at workstations, one pointing at screen, warm ambient light, no identifiable faces | ☐ NEEDED |
| B08 | 14.12s | pantry/B08.png | 1 | Two researchers at a table, each reviewing an annotation/coding sheet with checkboxes, close crop on hands and sheets, neutral light | ☐ NEEDED |
| B11 | 15.10s | pantry/B11.png | 1 | Close crop of a single job posting on a monitor or phone, text visible as dense paragraphs (no specific company logos), cool screen glow | ☐ NEEDED |
| B15 | 16.49s | pantry/B15.png | 1 | Stylized/illustrative small research team in a minimal lab — blackboard, vintage desk, no computers, warm sepia or desaturated palette, 2–3 people | ☐ NEEDED |

---

## Motion requirements

| Beat | Motion | Minimum asset size | Notes |
|------|--------|--------------------|-------|
| B02 | kenburns | 2000×1200px recommended | Push in toward center; need headroom for crop |
| B03 | kenburns | 2000×1200px recommended | Drift left-to-right; wide shot preferred |
| B08 | kenburns | 1800×1200px | Push toward annotation sheets at lower frame |
| B11 | drawon | 1800×1200px | Hold + terracotta ring draw-on; posting text area should be center-frame |
| B15 | kenburns | 2000×1200px | Push in toward blackboard/team |

---

## Sourcing notes

All five assets are Tier 1 (generic illustrative scenes). Generate via your preferred AI image tool (Midjourney, Flux, DALL-E). No real persons, no named institutions, no logos. After generating:

1. Drop file into `pantry/B02.png`, `pantry/B03.png`, etc.
2. Run `python3 runtime/scripts/compile.py <REEL_DIR>` — compile picks up the new files automatically
3. Inspect `_qc/` frames to confirm motion lands correctly

During the previz, these beats render as AI-VIDEO slates. The prompts above appear on each slate card.
