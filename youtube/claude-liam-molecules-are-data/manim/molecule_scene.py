"""
molecule_scene.py  —  Data-driven small-molecule renderer.

Chain: name or CID  →  PubChem REST  →  canonical SMILES  →  2D SDF
       (atom x/y + bond table)  →  Manim skeletal diagram.

No image generation.  No RDKit.  Correctness is upstream in the SMILES.

Brutalist / Claude palette
  CREAM  #F2F0E9   canvas
  INK    #3D3929   bonds, C/H implicit, N/S/P labels
  ACC    #D97757   O/F/Cl/Br atom labels  (terracotta — one accent per beat)
  SOFT   #A09A8A   formula / subtitle lines

Single molecule (env var):
  MOLECULE_NAME="caffeine"   manim -qk --fps 24 molecule_scene.py MoleculeScene
  MOLECULE_CID=2519           manim -qk --fps 24 molecule_scene.py MoleculeScene

Twenty-molecule gallery:
  manim -qk --fps 24 molecule_scene.py MoleculeGallery
"""

from __future__ import annotations

import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
from manim import *

# ── Palette ───────────────────────────────────────────────────────────────────
INK   = "#3D3929"
ACC   = "#D97757"
SOFT  = "#A09A8A"
CREAM = "#F2F0E9"
FONT  = "EB Garamond"

config.background_color = CREAM

# Atom-label colour routing (terracotta = electronegative; ink = everything else)
ACCENT_ELEMENTS = frozenset({"O", "F", "Cl", "Br", "I"})
INK_ELEMENTS    = frozenset({"N", "S", "P", "Se", "Si", "B"})
SKIP_LABELS     = frozenset({"C", "H"})   # skeletal convention: implied

# ── Network / cache ───────────────────────────────────────────────────────────
_CACHE = Path(__file__).parent / ".mol_cache"
_CACHE.mkdir(exist_ok=True)

_HEADERS = {
    "User-Agent": (
        "BearTextbooks/MoleculeRenderer "
        "(educational; non-commercial; contact ni.brown@northeastern.edu)"
    )
}


def _get(url: str) -> bytes:
    req = urllib.request.Request(url, headers=_HEADERS)
    with urllib.request.urlopen(req, timeout=20) as r:
        return r.read()


# ── PubChem resolvers ─────────────────────────────────────────────────────────

def resolve_cid(name_or_cid: str | int) -> int:
    """Name or bare integer string → canonical PubChem CID (int)."""
    s = str(name_or_cid).strip()
    if s.isdigit():
        return int(s)
    slug  = s.lower().replace(" ", "_").replace("/", "_")
    cache = _CACHE / f"cid_{slug}.json"
    if cache.exists():
        return int(json.loads(cache.read_text())["cid"])
    url  = (
        "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"
        f"{urllib.parse.quote(s)}/cids/JSON"
    )
    data = json.loads(_get(url))
    cid  = int(data["IdentifierList"]["CID"][0])
    cache.write_text(json.dumps({"name": s, "cid": cid}))
    time.sleep(0.25)
    return cid


def fetch_info(cid: int) -> dict:
    """Return {cid, title, smiles, iupac, formula, weight}.

    PubChem returns the SMILES under the key 'SMILES' (not 'CanonicalSMILES')
    when requested via the IsomericSMILES property name.
    """
    cache = _CACHE / f"info_{cid}.json"
    if cache.exists():
        return json.loads(cache.read_text())
    url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}"
        "/property/IsomericSMILES,IUPACName,MolecularFormula,"
        "MolecularWeight,Title/JSON"
    )
    props = json.loads(_get(url))["PropertyTable"]["Properties"][0]
    result = {
        "cid":     cid,
        "title":   props.get("Title", str(cid)),
        "smiles":  props.get("SMILES", ""),       # PubChem returns SMILES not CanonicalSMILES
        "iupac":   props.get("IUPACName", ""),
        "formula": props.get("MolecularFormula", ""),
        "weight":  str(props.get("MolecularWeight", "")),
    }
    cache.write_text(json.dumps(result))
    time.sleep(0.25)
    return result


def fetch_sdf(cid: int) -> str:
    """Return the PubChem 2D SDF string (V2000, Kekulé form)."""
    cache = _CACHE / f"sdf_{cid}.sdf"
    if cache.exists():
        return cache.read_text(encoding="utf-8", errors="replace")
    url = (
        f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}"
        "/SDF?record_type=2d&response_type=display"
    )
    sdf = _get(url).decode("utf-8", errors="replace")
    cache.write_text(sdf, encoding="utf-8")
    time.sleep(0.30)
    return sdf


# ── SDF V2000 parser ──────────────────────────────────────────────────────────

def parse_sdf(sdf: str) -> tuple[list[dict], list[dict]]:
    """Parse a V2000 SDF block.

    Returns:
        atoms  — list of {symbol: str, x: float, y: float}
        bonds  — list of {a1: int, a2: int, order: int}  (0-indexed atoms)

    Bond order 4 (aromatic) is normalised to 1 (PubChem gives Kekulé
    alternating anyway, but guard against edge cases).
    """
    lines  = sdf.split("\n")
    counts = lines[3]
    natoms = int(counts[0:3])
    nbonds = int(counts[3:6])

    atoms: list[dict] = []
    for i in range(natoms):
        ln = lines[4 + i]
        atoms.append({
            "symbol": ln[31:34].strip(),
            "x":      float(ln[0:10]),
            "y":      float(ln[10:20]),
        })

    bonds: list[dict] = []
    for i in range(nbonds):
        ln    = lines[4 + natoms + i]
        order = int(ln[6:9])
        if order == 4:
            order = 1   # normalise aromatic to single
        bonds.append({
            "a1":    int(ln[0:3]) - 1,   # → 0-indexed
            "a2":    int(ln[3:6]) - 1,
            "order": order,
        })

    return atoms, bonds


# ── Manim geometry builder ────────────────────────────────────────────────────

_LABEL_TRIM = 0.20    # back off this many Manim units near labelled atoms
_DOUBLE_GAP = 0.09   # lateral gap between the two lines of a double bond
_TRIPLE_GAP = 0.12


def _auto_scale(atoms: list[dict], bonds: list[dict]) -> float:
    """Compute scale so median bond length ≈ 1.50 Manim units."""
    if not bonds:
        return 1.0
    xs = np.array([a["x"] for a in atoms])
    ys = np.array([a["y"] for a in atoms])
    lengths = []
    for b in bonds[:30]:
        dx = xs[b["a1"]] - xs[b["a2"]]
        dy = ys[b["a1"]] - ys[b["a2"]]
        lengths.append(np.hypot(dx, dy))
    med = float(np.median(lengths))
    return (1.50 / med) if med > 0 else 1.0


def build_molecule_vgroup(
    atoms: list[dict],
    bonds: list[dict],
    *,
    extra_scale: float = 1.0,
    stroke_width: float = 2.8,
    font_size: float = 36,
) -> VGroup:
    """Build a complete skeletal-formula VGroup (bonds + heteroatom labels).

    Hydrogen atoms from the SDF are included in the coordinate table but
    bonds to H are drawn and H labels are shown (SKIP_LABELS skips only
    bare label rendering, not bonds — but H bonds from SDF appear as single
    bonds and are drawn).  In practice PubChem 2D SDFs omit most implicit H;
    explicit H atoms attached to heteroatoms ARE present and should be shown.
    """
    xs = np.array([a["x"] for a in atoms], dtype=float)
    ys = np.array([a["y"] for a in atoms], dtype=float)

    # Centre on the geometric mean
    xs -= xs.mean()
    ys -= ys.mean()

    scale = _auto_scale(atoms, bonds) * extra_scale
    P     = np.column_stack([xs * scale, ys * scale, np.zeros(len(xs))])

    def trim_at(idx: int) -> float:
        return _LABEL_TRIM if atoms[idx]["symbol"] not in SKIP_LABELS else 0.0

    def make_line(
        i1: int, i2: int,
        *,
        trim_a: float = 0.0,
        trim_b: float = 0.0,
        offset: np.ndarray | None = None,
        sw: float = stroke_width,
    ) -> Line:
        s = P[i1].copy()
        e = P[i2].copy()
        d = e - s
        n = np.linalg.norm(d)
        if n > 1e-6:
            u = d / n
            s = s + u * trim_a
            e = e - u * trim_b
        if offset is not None:
            s = s + offset
            e = e + offset
        return Line(s, e, color=INK, stroke_width=sw)

    def lateral(i1: int, i2: int, gap: float) -> np.ndarray:
        d = P[i2] - P[i1]
        n = np.linalg.norm(d)
        if n < 1e-6:
            return np.array([gap, 0.0, 0.0])
        u  = d / n
        perp = np.array([-u[1], u[0], 0.0])
        return perp * gap

    group = VGroup()

    # ── bonds ─────────────────────────────────────────────────────────────────
    for b in bonds:
        i1, i2, order = b["a1"], b["a2"], b["order"]
        ta = trim_at(i1)
        tb = trim_at(i2)
        if order == 1:
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb))
        elif order == 2:
            lv = lateral(i1, i2, _DOUBLE_GAP)
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb, offset= lv, sw=stroke_width * 0.85))
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb, offset=-lv, sw=stroke_width * 0.85))
        elif order >= 3:
            lv = lateral(i1, i2, _TRIPLE_GAP)
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb))
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb, offset= lv, sw=stroke_width * 0.8))
            group.add(make_line(i1, i2, trim_a=ta, trim_b=tb, offset=-lv, sw=stroke_width * 0.8))

    # ── atom labels (heteroatoms; C/H implied) ────────────────────────────────
    for i, a in enumerate(atoms):
        sym = a["symbol"]
        if sym in SKIP_LABELS:
            continue
        color  = ACC   if sym in ACCENT_ELEMENTS else INK
        weight = BOLD  if sym in ACCENT_ELEMENTS else NORMAL
        lbl = Text(sym, font=FONT, font_size=font_size, color=color, weight=weight)
        lbl.move_to(P[i])
        group.add(lbl)

    return group


# ── Twenty molecules for the gallery ─────────────────────────────────────────
# (display_name, pubchem_lookup, classification_line)
GALLERY_MOLECULES: list[tuple[str, str, str]] = [
    ("5-Fluorouracil",         "fluorouracil",                "antimetabolite · drug"),
    ("Imatinib",               "imatinib",                    "BCR-ABL inhibitor · drug"),
    ("Caffeine",               "caffeine",                    "methylxanthine · alkaloid"),
    ("Aspirin",                "aspirin",                     "analgesic · drug"),
    ("Dopamine",               "dopamine",                    "catecholamine · neurotransmitter"),
    ("Serotonin",              "serotonin",                   "indolamine · neurotransmitter"),
    ("Adenine",                "adenine",                     "purine · nucleobase"),
    ("Uracil",                 "uracil",                      "pyrimidine · nucleobase"),
    ("Thymine",                "thymine",                     "pyrimidine · nucleobase"),
    ("Glucose",                "glucose",                     "hexose · metabolite"),
    ("Nicotine",               "nicotine",                    "alkaloid · drug"),
    ("Penicillin G",           "penicillin g",                "beta-lactam · antibiotic"),
    ("Acetylcholine",          "acetylcholine",               "ester · neurotransmitter"),
    ("Epinephrine",            "epinephrine",                 "catecholamine · hormone"),
    ("Resveratrol",            "resveratrol",                 "stilbene · polyphenol"),
    ("Capsaicin",              "capsaicin",                   "vanilloid · alkaloid"),
    ("GABA",                   "gamma-aminobutyric acid",     "amino acid · neurotransmitter"),
    ("α-Ketoglutarate",        "alpha-ketoglutaric acid",     "keto acid · metabolite"),
    ("5-Aminolevulinic acid",  "5-aminolevulinic acid",       "porphyrin precursor · drug"),
    ("Methotrexate",           "methotrexate",                "antifolate · drug"),
]


# ── Scene: single molecule ────────────────────────────────────────────────────

class MoleculeScene(Scene):
    """Animated single-molecule render.

    Env vars (set before calling manim):
        MOLECULE_NAME   — common name, e.g. "caffeine"
        MOLECULE_CID    — PubChem CID, e.g. "2519"
    MOLECULE_CID takes precedence if both are set.
    """

    def construct(self) -> None:
        target = (
            os.environ.get("MOLECULE_CID", "").strip()
            or os.environ.get("MOLECULE_NAME", "caffeine").strip()
        )
        cid          = resolve_cid(target)
        info         = fetch_info(cid)
        sdf          = fetch_sdf(cid)
        atoms, bonds = parse_sdf(sdf)

        mol = build_molecule_vgroup(atoms, bonds)

        # Title block ─────────────────────────────────────────────────────────
        title = Text(info["title"], font=FONT, font_size=52, color=INK, weight=BOLD)
        sub   = Text(
            f"CID {cid}  ·  {info['formula']}  ·  MW {info['weight']}",
            font=FONT, font_size=24, color=SOFT,
        )
        smiles_raw   = info["smiles"]
        smiles_shown = smiles_raw[:72] + ("…" if len(smiles_raw) > 72 else "")
        smiles_card  = Text(smiles_shown, font="Courier New", font_size=18, color=SOFT)

        title.to_edge(UP, buff=0.45)
        sub.next_to(title, DOWN, buff=0.10)
        smiles_card.to_edge(DOWN, buff=0.40)

        mol.move_to(ORIGIN).shift(UP * 0.20)

        # Fit to safe area (leave room for title + smiles)
        max_dim = max(mol.width, mol.height)
        if max_dim > 5.5:
            mol.scale(5.5 / max_dim)

        # Animation ───────────────────────────────────────────────────────────
        self.play(Write(title), run_time=0.7)
        self.play(FadeIn(sub, shift=UP * 0.05), run_time=0.3)
        self.wait(0.2)
        self.play(Create(mol), run_time=2.2)
        self.play(FadeIn(smiles_card, shift=UP * 0.05), run_time=0.5)
        self.wait(3.5)


# ── Scene: 4 × 5 gallery ─────────────────────────────────────────────────────

class MoleculeGallery(Scene):
    """Render all twenty GALLERY_MOLECULES in a 4-row × 5-col grid."""

    COLS = 5
    ROWS = 4

    def construct(self) -> None:
        # ── Header ─────────────────────────────────────────────────────────
        title = Text(
            "Molecules Are Data",
            font=FONT, font_size=38, color=INK, weight=BOLD,
        )
        sub = Text(
            "twenty structures  ·  each rendered from canonical SMILES  ·  correct by construction",
            font=FONT, font_size=19, color=SOFT,
        )
        title.to_edge(UP, buff=0.28)
        sub.next_to(title, DOWN, buff=0.06)

        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(sub), run_time=0.3)
        self.wait(0.1)

        # ── Grid geometry ──────────────────────────────────────────────────
        # Frame: ≈14.2 × 8.0 Manim units (16:9).
        # Header occupies ≈ 1.3 units from top; bottom margin 0.25.
        # Grid spans from title bottom down to bottom-safe.
        grid_w    = 13.6
        grid_h    = 6.0
        cell_w    = grid_w / self.COLS     # 2.72
        cell_h    = grid_h / self.ROWS     # 1.50

        grid_top  = title.get_bottom()[1] - 0.22
        grid_left = -grid_w / 2

        mols:   list[VGroup] = []
        labels: list[Text]   = []

        for idx, (display_name, lookup, _cls) in enumerate(GALLERY_MOLECULES):
            row = idx // self.COLS
            col = idx %  self.COLS
            cx  = grid_left + (col + 0.5) * cell_w
            cy  = grid_top  - (row * cell_h) - cell_h * 0.45

            try:
                cid          = resolve_cid(lookup)
                sdf          = fetch_sdf(cid)
                atoms, bonds = parse_sdf(sdf)
                mol_vg = build_molecule_vgroup(
                    atoms, bonds,
                    extra_scale = 0.55,
                    stroke_width= 1.5,
                    font_size   = 16,
                )
                # Fit within cell (70 % of cell width, 80 % of cell height)
                max_dim = max(mol_vg.width, mol_vg.height, 1e-6)
                budget  = min(cell_w * 0.70, cell_h * 0.78)
                if max_dim > budget:
                    mol_vg.scale(budget / max_dim)
                mol_vg.move_to([cx, cy + 0.08, 0])
            except Exception:
                mol_vg = Text(
                    f"({display_name[:12]})",
                    font=FONT, font_size=11, color=SOFT,
                )
                mol_vg.move_to([cx, cy + 0.08, 0])

            name_lbl = Text(
                display_name, font=FONT, font_size=12, color=INK,
            )
            name_lbl.move_to([cx, grid_top - row * cell_h - cell_h * 0.88, 0])

            mols.append(mol_vg)
            labels.append(name_lbl)

        # ── Animate row by row ─────────────────────────────────────────────
        for row in range(self.ROWS):
            sl = slice(row * self.COLS, (row + 1) * self.COLS)
            anims = []
            for m, lbl in zip(mols[sl], labels[sl]):
                anims += [Create(m), FadeIn(lbl)]
            self.play(*anims, run_time=1.4)
            self.wait(0.1)

        self.wait(3.0)
