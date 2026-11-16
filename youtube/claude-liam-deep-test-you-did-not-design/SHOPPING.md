# SHOPPING.md — claude-liam-deep-test-you-did-not-design (Gate D2)

Written AFTER audio lock (Kokoro `am_onyx`, 2026-09-02; `mp3/timings.json` is ground truth — 39 narrated beats, 578.9 s + 12 s silent outro ≈ 9:51).
Tier-0/archival pass done first (`pantry_search.py` over Smithsonian · NLM · Wellcome · NASA). Five of seven VOX plates are IN and treated; two remain, both real-referent plates the tier law hands to the human. No entry here may be AI-generated.

---

## ☐ A3V1 — Alan Turing, archival portrait (Act III) · kenburns · window **15.41 s**

- **File:** `pantry/A3V1.png` (→ `media/A3V1.png`) · **Tier 3 — real named person — escalates to Bear**
- **Camera:** slow push toward the eyes, focus [0.5, 0.38]. **Floor: ≥1600 px long edge.**
- **Sourcing:** an archival photograph — e.g. the 1951 Elliott & Fry sitting (National Portrait Gallery, London), King's College Cambridge archive (AMT/K), or a Commons entry citing a clear PD/CC source.
- **Rights line (human):** the PHOTOGRAPH's rights govern (photographer's term), not the sitter's. Record URL · licence · credit in `media/A3V1.source.txt`.
- **Never:** AI generation, a likeness model, a drawing standing in for the photograph.
- **Fallback if uncleared:** Remotion citation card — "Turing, 1950 — *Computing Machinery and Intelligence*, *Mind*" on the cream stage (PROMPTS.md); strike this entry naming the scene.

## ☐ A3V2 — Searle, "Minds, Brains, and Programs" (1980), first page (Act III) · DOCUMENT drift · window **16.64 s**

- **File:** `pantry/A3V2.png` (→ `media/A3V2.png`) · **Tier 2 — specific real document — escalates to Bear**
- **Camera:** top-anchored document crop, slow drift down the title block; terracotta ring lands on the title on "Searle". **Floor: ≥2000 px wide.**
- **Sourcing:** *Behavioral and Brain Sciences* 3(3), 1980, 417–457 (Cambridge University Press) — the publisher's stated terms for an editorial excerpt; the author's own hosted PDF; a library scan. Object shot only — no text extraction.
- **Rights line (human):** the ITEM's stated rights, never the hosting site's reputation. Record in `media/A3V2.source.txt`.
- **Fallback if uncleared:** Manim quote card of the title + journal line (PROMPTS.md); strike this entry naming the scene.

---

## ☑ Filled at Tier 0 / archival (for the record — closed entries)

- [x] **A1V** — NLM IHM `nlm:nlmuid-101612150-img`, "[Hospital ward]" ([England?], 1914–18?) — NLM public-domain statement · window 15.30 s · `media/A1V.png` + sidecar.
- [x] **A2V1 → A2V2 (run R1, one plate)** — Smithsonian NMAH "Kettle", 1920s, CC0 (`ld1-1643398853934-1643398861445-0`, image `NMAH-AHB2014q054851`) · windows 11.30 s + 16.62 s · A2V1 seated as the tight crop (lid + spout), A2V2 as the whole kettle; museum color bar cropped · sidecars.
- [x] **A4V** — NLM IHM `nlm:nlmuid-101449037-img`, "[Physician examining a patient at bedside]" — NLM public-domain statement · window 13.86 s · `media/A4V.png` + sidecar.
- [x] **A5V** — NASA `S69-34038`, Apollo 10 flight director's console, 18 May 1969 — NASA public domain · window 16.42 s · `media/A5V.png` + sidecar.

Intake note: `pantry.py`'s beat-id regex (`^[A-Z]{1,3}\d+`) does not match this series' `A1V`-style ids, so the five plates were treated and slotted by hand (desaturate 80% · contrast 1.15 · seated on cream `#F2F0E9` · warm-ink vignette · whole image visible per STILL FIT LAW). Logged in BUILD-LOG.md.

The review cut waits on the two open entries, or an explicit "ship with slates" from Bear logged in BUILD-LOG.md.
