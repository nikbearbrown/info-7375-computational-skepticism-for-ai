# SOURCES — claude-liam-molecules-are-data

## Data source

**PubChem (NCBI / National Library of Medicine)**
- URL: https://pubchem.ncbi.nlm.nih.gov/
- License: Public Domain (US Government work)
- Usage: canonical SMILES, 2D SDF coordinates, compound names, molecular formulas
- REST endpoints used:
  - `/rest/pug/compound/name/{name}/cids/JSON` — name → CID resolution
  - `/rest/pug/compound/cid/{cid}/property/.../JSON` — compound properties
  - `/rest/pug/compound/cid/{cid}/SDF?record_type=2d` — 2D structure coordinates

All 20 structures in the gallery are PubChem public-domain data.
The 2D coordinates come from PubChem's own layout engine (OEChem).
No RDKit, no external 2D depiction library — coordinates used verbatim from SDF.

## Thesis sources

The claim that canonical SMILES pins every atom and bond is definitional:
the canonical SMILES specification (Weininger 1988, JCIM 28(1):31–36) and
PubChem's own documentation establish canonical SMILES as the authoritative
structural representation.

The claim that image generators can fabricate bonds is from the class of
known failures documented in: "Hallucination in neural networks" (general ML
literature) and the specific failure mode in molecule image generation
discussed in the Computational Skepticism for AI course materials.

## 5-FU scene lineage

`manim/molecule_scene.py` generalises the 5-FU scene from:
`illustrae-pipeline/manim/5fu_scene.py`
The palette (CREAM/INK/ACC/SOFT) and EB Garamond typography are unchanged.
The animation sequence pattern (title → ring → substituents) is preserved
but now driven by coordinate data rather than hand-coded vertex positions.

## Build log

See BUILD-LOG.md for decisions made during the build.
