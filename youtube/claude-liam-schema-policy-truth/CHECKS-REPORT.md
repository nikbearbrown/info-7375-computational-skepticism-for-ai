# CHECKS-REPORT — claude-liam-schema-policy-truth

**Date:** 2026-08-05  
**Reel:** `computational-skepticism-for-ai/youtube/claude-liam-schema-policy-truth`  
**Status:** READY FOR BEAR REVIEW  
**Slate cut:** `claude-liam-schema-policy-truth.mp4` (175.6s / 2:55)  
**Slots:** 9/9 filled — B00:VIDEO B01:MANIM B02:MANIM B03:MANIM B04:VIDEO B05:MANIM BVDT:VIDEO BHTF:VIDEO BOUT:VIDEO

---

## Gate results

| Gate | Result | Notes |
|------|--------|-------|
| GATE P (Pedagogy) | **PASS** | Signed by Bear 2026-08-04. See PEDAGOGY.md |
| GATE T (Type/kerning) | **PASS** | 9/9 beats, 0 FAILs. See TYPECHECK.md |
| GATE V (Visual QC) | ⚠ 4 MAJOR (0 BLOCKER) | Underfill on B04 + BVDT — see below |
| GATE L (Beat-mix lint) | ⚠ advisory | B04 held 37.6s with no motion_claim |
| GATE AUDIO | **PASS** | Mean −24.2 dB |
| GATE SHARPNESS | **PASS** | Median LV=374.2 |
| GATE BOOKEND | **PASS** | Four bookends correct |
| GATE BANNED-CARD | **PASS** | — |

---

## GATE T — changes made to reach PASS

All min-size failures were caused by font sizes below the 35px floor (EB Garamond Bold ~1.19× ratio at 1080p). One bbox-overlap failure was caused by the thick WARM_INK border animation.

| Scene | Change |
|---|---|
| B01_PolicyDrift | `policy_label` 26→32, `audit_word` ("UNAUDITABILITY") 28→32 |
| B02_RecordRender | `record_title` 24→30; `lbl_1`/`lbl_sep`/`lbl_n` 28→32; removed `record_rect.set_stroke(width=5.0)` border-pulse (thick WARM_INK border density ~5.5% passed blob filter → bbox-overlap with title text inside) |
| B03_PriorArtGrid | `topo_l`/`topo_sep`/`topo_r` ("ONE SOURCE \| N DERIVED") 26→32 |
| B05_ProsesDrift | `left_header` ("DOCUMENT SAID") 28→32, `right_header` ("LIVE SITE") 28→32 |

---

## GATE V — 4 MAJOR underfills (no BLOCKERs)

| Beat | Fill | Finding |
|---|---|---|
| B04 | 20% | FormACard — 4 lines in full frame, large cream margins; deliberate Claude-skin whitespace |
| B04 | 20% | (same, second sample frame) |
| BVDT | 54% | ClaudeVerdictArtifact — 1% below 55% floor; borderline |
| BVDT | 54% | (same, second sample frame) |

**B04:** 20% fill is a structural issue. The FormACard renders 4 short lines with heavy padding. GATE L also flags it as a long card (37.6s, no motion_claim). Options:
- Replace with a Manim scene for the gap-audit content
- Accept and add `motion_claim` to stand down the GATE L advisory
- Shorten the narration to fit under 8s

**BVDT:** 54% is 1% below floor. Likely acceptable — defer to Bear's eye.

---

## GATE L — advisory

B04 is a 37.6s card beat with no `motion_claim`. Over 8s a card should either upgrade the lane, shorten the narration, or declare the deliberate dwell with a `motion_claim`.

---

## Standing Order: STOP

Per STANDING ORDER, work stops here. Bear reviews the slate cut and gives go/no-go.

To watch: `open claude-liam-schema-policy-truth.mp4`
