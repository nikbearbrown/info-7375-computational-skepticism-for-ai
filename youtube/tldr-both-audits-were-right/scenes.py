"""
Manim scenes for tldr-both-audits-were-right (tldr skill — LEARN section 1, B10–B19).

One persistent object: FORTY PEOPLE as dots — the chapter's two groups at base rates
30% and 50% (a CONSTRUCTED 20-per-group population, captioned "constructed" on the
stage). Ink dots reoffend, dim dots do not. A two-box calibrated score sorts each
group into HIGH and LOW boxes (high → 60% reoffend in both groups, low → 20%).
Northpointe reads INSIDE a box (the denominator is the box); ProPublica reads the
never-reoffended dots (the denominator is the outcome). B16 moves group two's four
flagged never-reoffended dots to LOW: the false-positive gap nearly closes and the
high box's share climbs to 82%.

State factory: `_Stage(scene, title, **state)` rebuilds the dots, boxes and readouts at
the previous beat's end state, so the last frame of Bk is the first frame of Bk+1.
Numbers are asserted at import (FACTCHECK.md). INK text on the cream stage;
terracotta is ONE accent per scene — a dot or an X beside a word, never text, never
a line, never a bar, never a ring (GATE T). Explicit coords inside ±6.2 × ±3.3.
Type floor 32 (titles 40). Captions ≤ 34 chars.

Pacing: the exemplar's `_TARGET` block, plus `_until(self, phrase)` — each reveal
waits until the spoken phrase's position in the measured narration (character
share × measured duration), so motion lands on the word.
"""
import json as _json, os as _os
from fractions import Fraction as F
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the constructed population (chapter base rates 30% / 50%) ═══════════
INK_IDS = {1: [1, 4, 7, 11, 15, 18], 2: [0, 2, 3, 5, 8, 9, 12, 14, 16, 19]}
HIGH_INK = {1: [1, 7, 15], 2: [0, 2, 3, 5, 8, 9, 12, 14, 16]}
DIM_IDS = {g: [i for i in range(20) if i not in INK_IDS[g]] for g in (1, 2)}
HIGH_DIM = {1: DIM_IDS[1][:2], 2: DIM_IDS[2][:6]}
MOVE_ORDER = list(reversed(HIGH_DIM[2]))[:4]            # group two's flagged never-reoffended, last first

def boxes(g, moved=0):
    hi = HIGH_INK[g] + HIGH_DIM[g]
    lo = [i for i in INK_IDS[g] if i not in HIGH_INK[g]] + [i for i in DIM_IDS[g] if i not in HIGH_DIM[g]]
    mv = MOVE_ORDER[:moved] if g == 2 else []
    hi = [i for i in hi if i not in mv]
    return hi, lo + mv

def counts(g, moved=0):
    hi, lo = boxes(g, moved)
    ink = set(INK_IDS[g])
    hr = sum(i in ink for i in hi); lr = sum(i in ink for i in lo)
    neg = 20 - len(ink)
    return dict(hi=len(hi), hr=hr, lo=len(lo), lr=lr, fp=len(hi) - hr, neg=neg, fn=lr, r=len(ink))

C1, C2 = counts(1), counts(2)
assert len(INK_IDS[1]) == 6 and len(INK_IDS[2]) == 10                           # base rates 30% / 50%
assert F(C1["hr"], C1["hi"]) == F(C2["hr"], C2["hi"]) == F(3, 5)                 # high means 60% in both
assert F(C1["lr"], C1["lo"]) == F(C2["lr"], C2["lo"]) == F(1, 5)                 # low means 20% in both
assert (C1["fp"], C1["neg"], C2["fp"], C2["neg"]) == (2, 14, 6, 10)
assert (C1["fn"], C1["r"], C2["fn"], C2["r"]) == (3, 6, 1, 10)
MOVES = [counts(2, m) for m in range(5)]
def pct(a, b): return int(F(a, b) * 100 + F(1, 2))                                # round half up, as spoken
HI_PCT = [pct(c["hr"], c["hi"]) for c in MOVES]; LO_PCT = [pct(c["lr"], c["lo"]) for c in MOVES]
assert HI_PCT == [60, 64, 69, 75, 82] and LO_PCT == [20, 17, 14, 13, 11]
assert [c["fp"] for c in MOVES] == [6, 5, 4, 3, 2]
for c in (C1, C2):                                                               # the chapter's identity
    v = F(c["hr"], c["hi"]); p = F(c["r"], 20); t = F(c["hr"], c["r"]); f = F(c["fp"], c["neg"])
    assert v / (1 - v) == p / (1 - p) * t / f
assert F(3, 7) * F(7, 2) == F(3, 2) and 1 * F(3, 2) == F(3, 2)                  # B17 plug-ins: 1.5 = 3/7·3.5 = 1·1.5

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
_BASE_DEFAULT = 10.0

def _stretch_for(self):
    f = getattr(self, "_stretch", None)
    if f is None:
        target = _TARGET.get(type(self).__name__.split("_")[0], 0)
        base = getattr(self, "BASE", _BASE_DEFAULT) - 2.0
        f = 1.0 if not target or base <= 0 else max(1.0, min(1.8, (target - 2.0) / base))
        self._stretch = f
    return f

if not getattr(Scene.play, "_paced", False):
    _orig_play = Scene.play
    def _paced_play(self, *anims, **kw):
        if "run_time" in kw:
            kw["run_time"] = kw["run_time"] * _stretch_for(self)
        return _orig_play(self, *anims, **kw)
    _paced_play._paced = True
    Scene.play = _paced_play

def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0

def _until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured duration)."""
    bid = type(self).__name__.split("_")[0]
    n, target = _NARR.get(bid, ""), _TARGET.get(bid, 0)
    if not n or not target or phrase not in n:
        return
    t = target * n.index(phrase) / len(n) - lead
    gap = t - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)

def _finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    self.wait(max(1.0, target - _elapsed(self)) if target else 2.0)

# ═══════════ text + mark helpers ═══════════
def _title(txt, size=40): return Text(txt, font=SERIF, color=INK, font_size=size).move_to([0, 3.0, 0])
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -2.85, 0])
def _cons(): return _t("constructed · 20 per group", 32, DIM).move_to([-3.8, -2.85, 0])
def _m(tex, size=52, color=INK): return MathTex(tex, font_size=size, color=color)
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)
def _check(x, y, s=0.16, color=INK):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.8, 0], color=color, stroke_width=6),
                  Line([x - s * 0.3, y - s * 0.8, 0], [x + s * 1.1, y + s * 0.9, 0], color=color, stroke_width=6))

# ═══════════ panel geometry ═══════════
X0 = {1: -5.9, 2: 0.4}                     # panel left edges
DR, DS = 0.12, 0.36                        # dot radius, dot pitch
BWID, BHT = 8 * DS + 0.2, 2 * DS + 0.24    # box outline 3.08 × 0.96
HI_Y, LO_Y = 1.3, 0.0                      # box centres
HDR_Y, FP_Y, MISS_Y, BAR_Y, NOTE_Y = 2.3, -0.95, -1.5, -2.05, -2.15
def BXL(g): return X0[g] + 1.05            # box left edge
def RDX(g): return BXL(g) + BWID + 0.2     # readout left edge
def LINE_C(g): return BXL(g) + BWID / 2    # lineup centre x

def slot(g, box, k):
    """Position of the k-th dot in a box (rows of 8, two rows)."""
    cy = HI_Y if box == "hi" else LO_Y
    return [BXL(g) + 0.1 + DS / 2 + (k % 8) * DS, cy + (0.18 if k < 8 else -0.18), 0]

def lineup(g, i):
    return [LINE_C(g) - 4.5 * DS + (i % 10) * DS, 0.85 - (i // 10) * 0.4, 0]

HOOK_ROW_Y = (-1.85, -2.3)
def hook_pos(idx):                          # idx 0..39: group one first
    return [-5.23 + (idx % 20) * 0.55, HOOK_ROW_Y[idx // 20], 0]

def _box(g, which): return Rectangle(width=BWID, height=BHT, color=DIM, stroke_width=3).move_to([BXL(g) + BWID / 2, HI_Y if which == "hi" else LO_Y, 0])
def _boxlabel(g, which): return _t("high" if which == "hi" else "low", 32, INK).move_to([X0[g] + 0.1, HI_Y if which == "hi" else LO_Y, 0], aligned_edge=LEFT)
def _hdr(g): return _t(f"group {g} · base rate {30 if g == 1 else 50}%", 32, INK).move_to([X0[g], HDR_Y, 0], aligned_edge=LEFT)
def _share(g, which, moved=0):
    v = (HI_PCT if which == "hi" else LO_PCT)[moved] if g == 2 else (60 if which == "hi" else 20)
    return _t(f"{v}%", 36, INK).move_to([RDX(g), HI_Y if which == "hi" else LO_Y, 0], aligned_edge=LEFT)
def _fp(g, moved=0):
    c = counts(g, moved)
    return _t(f"false positives: {c['fp']} of {c['neg']}", 32, INK).move_to([X0[g] + 0.1, FP_Y, 0], aligned_edge=LEFT)
def _miss(g):
    c = counts(g)
    return _t(f"misses: {c['fn']} of {c['r']}", 32, INK).move_to([X0[g] + 0.1, MISS_Y, 0], aligned_edge=LEFT)
BAR_UNIT = 4.0
def _fpbar(g, moved=0):
    c = counts(g, moved); w = max(BAR_UNIT * c["fp"] / c["neg"], 0.02)
    return Rectangle(width=w, height=0.2, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([X0[g] + 0.1 + w / 2, BAR_Y, 0])
def _fptrack(g): return Line([X0[g] + 0.1, BAR_Y - 0.2, 0], [X0[g] + 0.1 + BAR_UNIT, BAR_Y - 0.2, 0], color=GHOST, stroke_width=3)
def _guide():
    x = X0[2] + 0.1 + BAR_UNIT * 2 / 14
    return Line([x, BAR_Y - 0.3, 0], [x, BAR_Y + 0.3, 0], color=DIM, stroke_width=4)
def _checks(moved=0):
    """Northpointe's checks beside the four share readouts (group two's high one drops once calibration breaks)."""
    g = VGroup()
    for gg in (1, 2):
        for w, y in (("hi", HI_Y), ("lo", LO_Y)):
            if gg == 2 and moved:
                continue
            g.add(_check(RDX(gg) + 1.05, y))
    return g


class _Stage:
    """The forty people at a given state.
    g1/g2: 'hook' | 'ghost' (lineup, ghost colour) | 'lineup' (coloured) | 'boxed';
    hdr: which group headers; shares: which groups show box readouts; checks: Northpointe's
    checks; fp / miss: which groups show those readouts; bars: B15 false-positive bars;
    moved: B16 dots moved (0–4); cons: the constructed caption."""
    def __init__(self, scene, title, g1="boxed", g2="boxed", hdr=(1, 2), shares=(1, 2), checks=False,
                 fp=(), miss=(), bars=False, moved=0, cons=True, faded=None):
        self.scene = scene
        self.t = _title(title); scene.add(self.t)
        self.dots = {1: [], 2: []}
        self.boxes, self.labels, self.hdrs, self.shares = VGroup(), VGroup(), VGroup(), {1: {}, 2: {}}
        for g, st in ((1, g1), (2, g2)):
            hi, lo = boxes(g, moved)
            for i in range(20):
                ink = i in INK_IDS[g]
                if st == "hook":
                    pos, col = hook_pos((g - 1) * 20 + i), DIM
                elif st == "ghost":
                    pos, col = lineup(g, i), DIM
                elif st == "lineup":
                    pos, col = lineup(g, i), INK if ink else DIM
                else:
                    pos = slot(g, "hi", hi.index(i)) if i in hi else slot(g, "lo", lo.index(i))
                    col = INK if ink else DIM
                    if faded == "ink" and ink: col = GHOST
                    if faded == "dim" and not ink: col = GHOST
                d = Dot(pos, radius=DR, color=col); self.dots[g].append(d); scene.add(d)
            if st == "boxed":
                for w in ("hi", "lo"):
                    b = _box(g, w); l = _boxlabel(g, w); self.boxes.add(b); self.labels.add(l); scene.add(b, l)
            if g in hdr:
                h = _hdr(g); self.hdrs.add(h); scene.add(h)
            if g in shares:
                for w in ("hi", "lo"):
                    s = _share(g, w, moved); self.shares[g][w] = s; scene.add(s)
        self.checks = _checks(moved) if checks else None
        if checks: scene.add(self.checks)
        self.fp = {g: _fp(g, moved) for g in fp}; [scene.add(v) for v in self.fp.values()]
        self.miss = {g: _miss(g) for g in miss}; [scene.add(v) for v in self.miss.values()]
        self.bars = None
        if bars:
            self.bars = {g: _fpbar(g, moved) for g in (1, 2)}
            self.tracks = VGroup(_fptrack(1), _fptrack(2)); self.guide = _guide()
            scene.add(self.tracks, self.guide, *self.bars.values())
        self.cons = _cons() if cons else None
        if cons: scene.add(self.cons)

    def all_dots(self, g=None):
        return VGroup(*(self.dots[1] + self.dots[2] if g is None else self.dots[g]))


# ═══════════ B10 — HOOK ═══════════
def _headlines():
    L = VGroup(_t("ProPublica", 40, INK, bold=True).move_to([-3.2, 2.05, 0]),
               _t("errors fell unevenly", 32, INK).move_to([-3.2, 1.5, 0]),
               _t("biased", 40, INK, bold=True).move_to([-3.2, 0.95, 0]))
    R = VGroup(_t("Northpointe", 40, INK, bold=True).move_to([3.2, 2.05, 0]),
               _t("each score meant the same", 32, INK).move_to([3.2, 1.5, 0]),
               _t("fair", 40, INK, bold=True).move_to([3.2, 0.95, 0]))
    return L, R
def _connectors():
    return (Line([-3.0, -0.05, 0], [-1.8, -1.6, 0], color=INK, stroke_width=3),
            Line([3.0, -0.05, 0], [1.8, -1.6, 0], color=INK, stroke_width=3))


class B10_TwoHeadlines(Scene):
    BASE = 99
    def construct(self):
        t = _title("Two Audits")
        self.add(t)
        dots = VGroup(*[Dot(hook_pos(i), radius=DR, color=DIM) for i in range(40)])
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.03), run_time=1.4)
        L, R = _headlines(); cL, cR = _connectors()
        _until(self, "In 2016 ProPublica")
        self.play(FadeIn(L[0]), run_time=0.6)
        _until(self, "Black defendants")
        self.play(FadeIn(L[1]), run_time=0.6)
        _until(self, "Biased.")
        self.play(FadeIn(L[2]), Create(cL), run_time=0.8)
        _until(self, "The maker, Northpointe")
        self.play(FadeIn(R[0]), run_time=0.6)
        _until(self, "within each score")
        self.play(FadeIn(R[1]), run_time=0.6)
        _until(self, "Fair.")
        self.play(FadeIn(R[2]), Create(cR), run_time=0.8)
        _until(self, "Same tool, same people")
        self.play(Indicate(dots, color=INK, scale_factor=1.05), run_time=1.0)
        _until(self, "Somebody's arithmetic")
        q = _t("which one is wrong?", 36, INK).move_to([0, 0.35, 0])
        self.play(FadeIn(q), GrowFromCenter(_dot(2.3, 0.35)), run_time=0.6)
        _finish(self)


# ═══════════ B11 — INSTANCE 1: group one ═══════════
class B11_GroupOne(Scene):
    BASE = 99
    def construct(self):
        t = _title("Two Audits")
        dots = [Dot(hook_pos(i), radius=DR, color=DIM) for i in range(40)]
        L, R = _headlines(); cL, cR = _connectors()
        q = _t("which one is wrong?", 36, INK).move_to([0, 0.35, 0]); d0 = _dot(2.3, 0.35)
        self.add(t, *dots, L, R, cL, cR, q, d0)
        self.wait(0.3)
        self.play(FadeOut(L), FadeOut(R), FadeOut(cL), FadeOut(cR), FadeOut(q), FadeOut(d0),
                  Transform(t, _title("Group One")),
                  *[dots[i].animate.move_to(lineup(1, i)) for i in range(20)],
                  *[dots[20 + i].animate.move_to(lineup(2, i)) for i in range(20)], FadeIn(_cons()), run_time=1.6)
        _until(self, "Six of them will reoffend")
        self.play(*[dots[i].animate.set_color(INK) for i in INK_IDS[1]], run_time=0.8)
        _until(self, "That's a base rate")
        self.play(FadeIn(_hdr(1)), run_time=0.6)
        _until(self, "Now the score sorts")
        hi, lo = boxes(1)
        self.play(Create(_box(1, "hi")), Create(_box(1, "lo")), FadeIn(_boxlabel(1, "hi")), FadeIn(_boxlabel(1, "lo")),
                  *[dots[i].animate.move_to(slot(1, "hi", hi.index(i))) for i in hi],
                  *[dots[i].animate.move_to(slot(1, "lo", lo.index(i))) for i in lo], run_time=1.6)
        _until(self, "sixty percent")
        self.play(FadeIn(_share(1, "hi")), GrowFromCenter(_dot(RDX(1) + 1.05, HI_Y)), run_time=0.6)
        _until(self, "twenty percent")
        self.play(FadeIn(_share(1, "lo")), run_time=0.6)
        _finish(self)


# ═══════════ B12 — INSTANCE 2: group two ═══════════
class B12_GroupTwo(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Group One", g2="ghost", hdr=(1,), shares=(1,))
        dhold = _dot(RDX(1) + 1.05, HI_Y); self.add(dhold)
        self.play(Transform(st.t, _title("Group Two")), FadeOut(dhold), run_time=0.8)
        d2 = st.dots[2]
        _until(self, "and ten reoffend")
        self.play(*[d2[i].animate.set_color(INK if i in INK_IDS[2] else DIM) for i in range(20)], run_time=0.8)
        self.play(FadeIn(_hdr(2)), run_time=0.5)
        _until(self, "Same score, same boxes")
        hi, lo = boxes(2)
        self.play(Create(_box(2, "hi")), Create(_box(2, "lo")), FadeIn(_boxlabel(2, "hi")), FadeIn(_boxlabel(2, "lo")),
                  *[d2[i].animate.move_to(slot(2, "hi", hi.index(i))) for i in hi],
                  *[d2[i].animate.move_to(slot(2, "lo", lo.index(i))) for i in lo], run_time=1.6)
        _until(self, "sixty percent")
        self.play(FadeIn(_share(2, "hi")), run_time=0.5)
        _until(self, "twenty percent")
        self.play(FadeIn(_share(2, "lo")), run_time=0.5)
        _until(self, "High means sixty")
        self.play(Create(_checks()), run_time=1.0)
        _until(self, "That's Northpointe's audit")
        self.play(FadeIn(_t("Northpointe: calibrated", 36, INK).move_to([-2.2, NOTE_Y, 0])),
                  GrowFromCenter(_dot(0.55, NOTE_Y)), run_time=0.6)
        _finish(self)


# ═══════════ B13 — NAIVE: redo ProPublica's count ═══════════
class B13_RedoTheCount(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Group Two", checks=True)
        note = _t("Northpointe: calibrated", 36, INK).move_to([-2.2, NOTE_Y, 0]); dn = _dot(0.55, NOTE_Y)
        self.add(note, dn)
        self.wait(0.3)
        ask = _t("did ProPublica fudge it?", 36, INK).move_to([-2.4, NOTE_Y, 0])
        self.play(Transform(st.t, _title("Redo The Count")), FadeOut(dn), ReplacementTransform(note, ask), run_time=0.9)
        _until(self, "starts from the grey dots")
        self.play(*[st.dots[g][i].animate.set_color(GHOST) for g in (1, 2) for i in INK_IDS[g]], run_time=0.9)
        _until(self, "Group one has fourteen")
        hd1 = [st.dots[1][i] for i in HIGH_DIM[1]]
        self.play(Indicate(VGroup(*hd1), color=INK, scale_factor=1.4), run_time=0.8)
        self.play(FadeIn(_fp(1)), run_time=0.5)
        _until(self, "Group two has ten")
        hd2 = [st.dots[2][i] for i in HIGH_DIM[2]]
        self.play(Indicate(VGroup(*hd2), color=INK, scale_factor=1.4), run_time=0.8)
        self.play(FadeIn(_fp(2)), run_time=0.5)
        _until(self, "Nobody fudged")
        self.play(Create(_x(0.5, NOTE_Y)), run_time=0.5)
        _finish(self)


# ═══════════ B14 — SHIFT: same dots, two filters ═══════════
class B14_TwoFilters(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Redo The Count", checks=True, fp=(1, 2), faded="ink")
        ask = _t("did ProPublica fudge it?", 36, INK).move_to([-2.4, NOTE_Y, 0]); xx = _x(0.5, NOTE_Y)
        self.add(ask, xx)
        self.wait(0.3)
        ink = [st.dots[g][i] for g in (1, 2) for i in INK_IDS[g]]
        dim = [st.dots[g][i] for g in (1, 2) for i in DIM_IDS[g]]
        low = [st.dots[g][i] for g in (1, 2) for i in boxes(g)[1]]
        self.play(Transform(st.t, _title("Same Dots, Two Filters")), FadeOut(ask), FadeOut(xx),
                  *[d.animate.set_color(INK) for d in ink], run_time=1.0)
        _until(self, "Northpointe's filter")
        n1 = _t("Northpointe divides by the box", 36, INK).move_to([-0.6, NOTE_Y, 0])
        ul = VGroup(*[Line([BXL(g), HI_Y - BHT / 2 - 0.1, 0], [BXL(g) + BWID, HI_Y - BHT / 2 - 0.1, 0], color=INK, stroke_width=5) for g in (1, 2)])
        self.play(*[d.animate.set_color(GHOST) for d in low], FadeIn(n1), Create(ul), run_time=1.0)
        _until(self, "ProPublica's filter")
        n2 = _t("ProPublica divides by the outcome", 36, INK).move_to([-0.6, NOTE_Y, 0])
        self.play(*[d.animate.set_color(INK if d in ink else DIM) for d in low], FadeOut(ul), run_time=0.6)
        self.play(*[d.animate.set_color(GHOST) for d in ink], ReplacementTransform(n1, n2), run_time=1.0)
        _until(self, "And the misses")
        self.play(*[d.animate.set_color(INK) for d in ink], *[d.animate.set_color(GHOST) for d in dim],
                  FadeIn(_miss(1)), FadeIn(_miss(2)), run_time=1.0)
        _until(self, "one of ten in group two", lead=0.2)
        cap = _t("same dots, two denominators", 36, INK).move_to([-0.8, NOTE_Y, 0])
        self.play(*[d.animate.set_color(DIM) for d in dim], FadeOut(n2), FadeIn(cap), GrowFromCenter(_dot(2.3, NOTE_Y)), run_time=0.8)
        _finish(self)


# ═══════════ B15 — predict ═══════════
class B15_Commit(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Same Dots, Two Filters", checks=True, fp=(1, 2), miss=(1, 2))
        cap = _t("same dots, two denominators", 36, INK).move_to([-0.8, NOTE_Y, 0]); d0 = _dot(2.3, NOTE_Y)
        self.add(cap, d0)
        self.wait(0.3)
        self.play(Transform(st.t, _title("Commit")), FadeOut(cap), FadeOut(d0), FadeOut(st.miss[1]), FadeOut(st.miss[2]), run_time=0.8)
        tracks = VGroup(_fptrack(1), _fptrack(2))
        self.play(Create(tracks), GrowFromEdge(_fpbar(1), LEFT), GrowFromEdge(_fpbar(2), LEFT), run_time=1.0)
        self.play(Create(_guide()), run_time=0.5)
        _until(self, "Can you also make")
        qq = _t("hold 60%: equal false positives?", 32, INK).move_to([2.9, -2.85, 0])
        self.play(FadeIn(qq), GrowFromCenter(_dot(5.9, -2.85)), run_time=0.6)
        _finish(self)


# ═══════════ B16 — TRANSFORM: move the dots ═══════════
class B16_MoveTheDots(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Commit", checks=True, fp=(1, 2), bars=True)
        qq = _t("hold 60%: equal false positives?", 32, INK).move_to([2.9, -2.85, 0]); dq = _dot(5.9, -2.85)
        self.add(qq, dq)
        self.wait(0.3)
        self.play(Transform(st.t, _title("Move The Dots")), FadeOut(qq), FadeOut(dq), run_time=0.7)
        d2 = st.dots[2]
        cues = ["One.", "Two.", "Three.", "Four."]
        for m in range(1, 5):
            _until(self, cues[m - 1], lead=0.1)
            i = MOVE_ORDER[m - 1]
            hi, lo = boxes(2, m)
            self.play(d2[i].animate.move_to(slot(2, "lo", lo.index(i))),
                      Transform(st.shares[2]["hi"], _share(2, "hi", m)), Transform(st.shares[2]["lo"], _share(2, "lo", m)),
                      Transform(st.fp[2], _fp(2, m)), Transform(st.bars[2], _fpbar(2, m)), run_time=0.9)
        _until(self, "And the high box")
        g2checks = VGroup(*st.checks[2:])
        self.play(FadeOut(g2checks), Indicate(st.shares[2]["hi"], color=INK, scale_factor=1.3), run_time=0.8)
        _until(self, "Eighty-two percent")
        self.play(Create(_x(RDX(2) + 1.15, HI_Y)), run_time=0.5)
        _until(self, "Every dot that closes")
        cap = _t("close one gap, open the other", 32, DIM).move_to([2.9, -2.85, 0])
        self.play(FadeIn(cap), run_time=0.6)
        _finish(self)


# ═══════════ B17 — ABSTRACTION: the chapter's line ═══════════
EQ_X = [-3.0, -1.35, 0.35, 1.75, 3.0]       # columns: v-odds · = · p-odds · (·) · t/f
EQ_Y, REF_Y, R1_Y, R2_Y = 1.75, 0.75, -0.55, -1.45

def _eq_parts(size=60):
    return VGroup(_m(r"\frac{v}{1-v}", size).move_to([EQ_X[0], EQ_Y, 0]), _m(r"=", size).move_to([EQ_X[1], EQ_Y, 0]),
                  _m(r"\frac{p}{1-p}", size).move_to([EQ_X[2], EQ_Y, 0]), _m(r"\cdot", size).move_to([EQ_X[3], EQ_Y, 0]),
                  _m(r"\frac{t}{f}", size).move_to([EQ_X[4], EQ_Y, 0]))

def _plug(row_y, vals, size=48):
    return VGroup(*[_m(v, size).move_to([EQ_X[k], row_y, 0]) for k, v in enumerate(vals)])


class B17_TheLine(Scene):
    BASE = 99
    def construct(self):
        st = _Stage(self, "Move The Dots", checks=False, fp=(1, 2), bars=True, moved=4)
        self.add(_x(RDX(2) + 1.15, HI_Y))
        self.wait(0.3)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not st.t], Transform(st.t, _title("One Line")), run_time=1.0)
        eq = _eq_parts()
        sep = Line([-5.9, 0.15, 0], [4.2, 0.15, 0], color=GHOST, stroke_width=3)
        l1 = _t("group 1", 32, INK).move_to([-5.0, R1_Y, 0]); l2 = _t("group 2", 32, INK).move_to([-5.0, R2_Y, 0])
        _until(self, "For each group")
        self.play(Write(eq), Create(sep), FadeIn(l1), FadeIn(l2), FadeIn(_cons()), run_time=1.6)
        _until(self, "v is Northpointe's")
        r1 = _t("Northpointe's 60%", 32, DIM).move_to([EQ_X[0], REF_Y, 0])
        self.play(FadeIn(r1), run_time=0.5)
        _until(self, "f is ProPublica's")
        r3 = _t("ProPublica's number", 32, DIM).move_to([EQ_X[4] + 0.4, REF_Y, 0])
        self.play(FadeIn(r3), run_time=0.5)
        _until(self, "p is the base rate")
        r2 = _t("base rate", 32, DIM).move_to([EQ_X[2], REF_Y, 0])
        self.play(FadeIn(r2), run_time=0.5)
        _until(self, "Lock v in both groups")
        p1 = _plug(R1_Y, ["1.5", "=", r"\frac{3}{7}", r"\cdot", "3.5"]); p2 = _plug(R2_Y, ["1.5", "=", "1", r"\cdot", "1.5"])
        self.play(Write(p1), run_time=1.0)
        _until(self, "group two, one and a half")
        self.play(Write(p2), run_time=1.0)
        _until(self, "Calibration and equal error rates")
        name = _t("unequal base rates: not both", 40, INK, bold=True).move_to([-0.8, -2.15, 0])
        self.play(FadeIn(name), GrowFromCenter(_dot(2.8, -2.15)), run_time=0.7)
        _finish(self)


# ═══════════ B18 — TANGENT: read the line ═══════════
class B18_ReadTheLine(Scene):
    BASE = 99
    def construct(self):
        t = _title("Read The Line")
        eq0 = _eq_parts()
        self.add(t, eq0)
        self.wait(0.3)
        eq = VGroup(_m(r"\frac{v}{1-v}", 52).move_to([-4.85, 1.7, 0]), _m("=", 52).move_to([-3.75, 1.7, 0]),
                    _m(r"\frac{p}{1-p}", 52).move_to([-2.65, 1.7, 0]), _m(r"\cdot", 52).move_to([-1.75, 1.7, 0]),
                    _m(r"\frac{t}{f}", 52).move_to([-1.1, 1.7, 0]))
        self.play(Transform(eq0, eq), run_time=1.0)
        self.play(Create(Line([0.2, 2.35, 0], [0.2, -2.5, 0], color=GHOST, stroke_width=2)), run_time=0.5)
        zones = [(r"\frac{v}{1-v}", "Northpointe's, as odds", "Left: Northpointe"),
                 (r"\frac{p}{1-p}", "the base rate, as odds", "First factor"),
                 (r"\frac{t}{f}", "how hard the flag leans", "Second factor"),
                 (r"f", "ProPublica's number", "ProPublica's number lives"),
                 (r"=", "the lock", "The equals sign")]
        ZY = [2.05, 1.0, -0.2, -1.1, -1.9]
        for k, (sym, mean, cue) in enumerate(zones):
            y = ZY[k]
            _until(self, cue)
            self.play(FadeIn(_m(sym, 40).move_to([1.0, y, 0])), FadeIn(_t(mean, 32).move_to([1.8, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.1), run_time=0.6)
            if k == 1:
                self.play(FadeIn(_t("no audit chose it", 32, DIM).move_to([1.8, y - 0.45, 0], aligned_edge=LEFT)), run_time=0.4)
        self.play(GrowFromCenter(_dot(3.55, ZY[4])), run_time=0.4)
        _until(self, "Two ways out")
        w = _t("two ways out", 32, INK).move_to([-3.1, 0.4, 0])
        e1 = _m(r"p_a = p_b", 48).move_to([-3.1, -0.4, 0]); o = _t("or a perfect score", 32, DIM).move_to([-3.1, -1.1, 0])
        e2 = _m(r"t = 1,\; f = 0", 48).move_to([-3.1, -1.8, 0])
        self.play(FadeIn(w), Write(e1), run_time=0.8)
        self.play(FadeIn(o), Write(e2), run_time=0.8)
        _finish(self)


# ═══════════ B19 — PAYOFF: both right ═══════════
class B19_BothRight(Scene):
    BASE = 99
    def construct(self):
        t = _title("Read The Line")
        self.add(t, _eq_parts())
        self.wait(0.2)
        self.play(*[FadeOut(m) for m in self.mobjects if m is not t], Transform(t, _title("Two Audits")), run_time=0.8)
        dots = VGroup(*[Dot(hook_pos(i), radius=DR, color=INK if (i % 20) in INK_IDS[1 + i // 20] else DIM) for i in range(40)])
        L, R = _headlines(); cL, cR = _connectors()
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.02), FadeIn(L), FadeIn(R), Create(cL), Create(cR), run_time=1.4)
        _until(self, "ProPublica: two in fourteen")
        n1 = _t("2 of 14 · 6 of 10", 32, INK).move_to([-3.2, 0.4, 0])
        self.play(FadeIn(n1), run_time=0.6)
        _until(self, "Correct.")
        self.play(Create(_check(-1.35, 0.42)), run_time=0.4)
        _until(self, "Northpointe: sixty")
        n2 = _t("60% · 60%", 32, INK).move_to([3.2, 0.4, 0])
        self.play(FadeIn(n2), run_time=0.6)
        self.play(Create(_check(4.45, 0.42)), run_time=0.4)
        _until(self, "Both audits were right")
        both = _t("both right: different denominators", 36, INK).move_to([-0.4, -0.75, 0])
        self.play(FadeOut(cL), FadeOut(cR), FadeIn(both), GrowFromCenter(_dot(3.45, -0.75)), run_time=0.7)
        _until(self, "Not taught here")
        self.play(FadeIn(_cap("not taught: which to hold")), FadeIn(_cons()), run_time=0.6)
        _finish(self)
