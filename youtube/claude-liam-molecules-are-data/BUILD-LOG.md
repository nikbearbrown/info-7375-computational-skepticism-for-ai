# BUILD-LOG — claude-liam-molecules-are-data

## 2026-07-30 — Initial scaffold

**Build phase**: scaffold (beat_sheet.json + manim/molecule_scene.py)
**Status**: GATE P pending — narration not yet approved, no audio generated

### Decisions

**Why no RDKit for the draw step?**
The thesis is that correctness lives in the SMILES, not in a drawing library.
Using RDKit to re-derive 2D coordinates would add a dependency and muddy the
argument: "we used PubChem's own 2D layout — the same data the database ships."
PubChem's `/SDF?record_type=2d` endpoint gives OEChem-generated 2D coordinates
directly. The SDF parser is ~15 lines of pure Python. This is cleaner and
truer to the thesis.

**RDKit IS installed** (confirmed 2026-07-30) for other uses in the codebase,
but molecule_scene.py deliberately does not import it.

**20 molecule selection rationale**
Chosen to span the four categories the illustrae-pipeline tracks (drug,
metabolite, nucleobase, alkaloid/polyphenol) and to include at least one
molecule from each channel (cancer drugs: 5-FU, imatinib, methotrexate;
neuroscience: dopamine, serotonin, acetylcholine, GABA, epinephrine;
nucleobases: adenine, uracil, thymine; metabolites: glucose, α-ketoglutarate,
5-ALA; natural products: caffeine, nicotine, capsaicin, resveratrol, penicillin G;
food: aspirin). All have well-established PubChem entries with 2D SDFs.

**Gallery layout: 4×5 not 5×4**
Landscape layout (5 columns) puts more molecules per row, which reads better
as a "gallery scan" left-to-right. 4 rows × 5 cols fits in the 16:9 frame
with the title block.

**Imatinib and methotrexate included despite size**
These are the largest molecules in the set (~50 atoms each). The gallery uses
`extra_scale=0.55` and a per-cell fit budget, so they scale down automatically.
The point: even a complex molecule is drawn correctly from data.

**B04 uses ClaudeCodeBeat, not a concept illustration**
The four-step chain IS the concept. The code is the most direct expression
of it. CODE-SIM Priority feedback requires code beats to use a code-sim skin
first; ClaudeCodeBeat satisfies this in the Claude brand.

### Open items
- [ ] GATE P: Bear reviews narration before audio spend
- [ ] Test MoleculeScene render (fluorouracil) — verify SDF cache, confirm layout
- [ ] Test MoleculeGallery render — check all 20 molecules resolve + fit
- [ ] Check imatinib and methotrexate gallery cell fit at extra_scale=0.55
- [ ] Run type_check.py after first compile — ensure TYPECHECK.md passes
