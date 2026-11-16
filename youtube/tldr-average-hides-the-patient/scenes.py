"""
Manim scenes for tldr-average-hides-the-patient (tldr skill — LEARN section 1, B10–B19).

One persistent object: the chapter's subgroup calibration table as FIVE INK COLUMNS on
one cream axis (adults 18–64, children 0–17, 65 and over, pregnancy-related, rare
disease). Height is the row's calibration error (ECE). Width has three modes:
  one       the five columns fused edge to edge = one bar at the global 0.018 over
            all 12,955 patients (the report as the reader receives it)
  equal     five equal columns, the way the table prints its rows
  patients  each column as wide as its row's N: the rare-disease row (95 of 12,955)
            becomes a sliver 0.7 % of the axis
The global line (0.018) is fixed on every beat.

State factory: `_Stage(scene, title, mode, heights, ...)` rebuilds the columns, value
labels, names and reference lines at the previous beat's end state, so the last frame
of Bk is the first frame of Bk+1; `raise_to()` and `remode()` return the animations that morph them
(transform, don't cut). Numbers are the chapter's or recomputed from its inputs and
asserted at import (FACTCHECK.md). INK text on the cream stage; terracotta is ONE
accent per scene — a dot or an X beside a word, never text, never a line, never a bar
(GATE T). Explicit coords inside ±6.2 × ±3.3. Type floor 32 (titles 40). Captions
≤ 34 chars. Self-contained (Gate A copies only this file).

Pacing: the exemplar's `_TARGET` block, plus `_until(self, phrase)` — each reveal
waits until the spoken phrase's position in the measured narration (character share
× measured duration), so motion lands on the word.
"""
import json as _json, os as _os
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
# the columns are DIM, not INK: GATE T reads INK-coloured blobs as text runs, and an INK chart
# block encloses its own value labels (§8.6b false overlap). Reference lines are INK.
COL = DIM
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's table ═══════════
N = [8420, 1210, 2850, 380, 95]
ECE = [0.019, 0.029, 0.044, 0.071, 0.103]
GN, GE = 12955, 0.018
assert sum(N) == GN
SHARE = [n / GN for n in N]
PULL = [s * e for s, e in zip(SHARE, ECE)]
ROW_AVG = sum(ECE) / 5
assert round(ROW_AVG, 3) == 0.053 and round(PULL[0], 3) == 0.012 and round(PULL[4], 4) == 0.0008
assert round(SHARE[4], 4) == 0.0073 and SHARE[4] < 0.01                    # worst case (every gap = 1) < a hundredth
assert [e > 2 * GE for e in ECE] == [False, False, True, True, True]       # three of five above twice global
assert round(sum(PULL), 3) == 0.028 and GE <= sum(PULL)                     # pooled <= patient-weighted (same bins)
assert round(ECE[4] / GE, 1) == 5.7

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
_BASE_DEFAULT = 30.0

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
def _m(tex, size=56, color=INK): return MathTex(tex, font_size=size, color=color)
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _note(txt, y, size=40, bold=False): return _t(txt, size, INK, bold).move_to([-5.6, y, 0], aligned_edge=LEFT)
def _dot(x, y, r=0.13): return Dot([x, y, 0], color=TERRA, radius=r)
def _x(x, y, s=0.2, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))

# ═══════════ stage geometry ═══════════
BASE_Y, YS = -2.3, 40.0                      # ECE 0.103 → 4.12 units tall
X_L, X_R = -5.8, 2.6                         # the axis: 8.4 units = every patient
def Y(v): return BASE_Y + v * YS
GY = Y(GE)                                   # the global line, −1.58

def geom(mode):
    if mode == "equal":
        return [(X_L + i * 1.725, 1.5) for i in range(5)]
    wu, gap = (8.4 / GN, 0.0) if mode == "one" else (8.16 / GN, 0.06)
    out, x = [], X_L
    for n in N:
        w = n * wu; out.append((x, w)); x += w + gap
    return out
def centers(mode): return [xl + w / 2 for xl, w in geom(mode)]

def _col(xl, w, h):
    H = max(h * YS, 0.02)
    return Rectangle(width=max(w, 0.04), height=H, fill_color=COL, fill_opacity=1, stroke_color=COL, stroke_width=1).move_to([xl + w / 2, BASE_Y + H / 2, 0])
def _cols(mode, H): return VGroup(*[_col(xl, w, h) for (xl, w), h in zip(geom(mode), H)])

EQ_NAMES = ["adults", "children", "65+", "pregnancy", "rare"]
RIGHT_NAMES = {3: "pregnancy", 4: "rare disease"}
EQ_LY = [-1.24, -0.55, 0.15, 0.84, 2.12]     # value-label heights, equal mode (clear of every reference line)
PT_LY = -0.2                                  # value-label row, patient mode (rows 0–2)
RX = 2.85                                     # right label column (line tags, patient-mode names)

def _vlabel(mode, i, h):
    if mode == "equal":
        return _t(f"{h:.3f}").move_to([centers("equal")[i], EQ_LY[i], 0])
    if i < 3:
        return _t(f"{h:.3f}").move_to([centers("patients")[i], PT_LY, 0])
    return _t(f"{RIGHT_NAMES[i]} {h:.3f}").move_to([RX, Y(h), 0], aligned_edge=LEFT)
def _names(mode):
    if mode == "equal":
        return VGroup(*[_t(s).move_to([c, -2.65, 0]) for s, c in zip(EQ_NAMES, centers("equal"))])
    return VGroup(*[_t(s).move_to([c, -2.65, 0]) for s, c in zip(EQ_NAMES[:3], centers("patients")[:3])])

def _hline(v, color=INK): return Line([X_L, Y(v), 0], [X_R, Y(v), 0], color=color, stroke_width=3)
def _htag(txt, v): return _t(txt).move_to([RX, Y(v), 0], aligned_edge=LEFT)


class _Stage:
    """The table as columns on one axis at a given width mode and heights (+ its labels)."""
    def __init__(self, scene, title, mode, H, labels=(), names=True):
        self.scene, self.mode, self.H = scene, mode, list(H)
        self.t = _title(title)
        self.axis = Line([X_L, BASE_Y, 0], [X_R, BASE_Y, 0], color=INK, stroke_width=3)
        self.cols = _cols(mode, H)
        self.gline = _hline(GE); self.gtag = _htag("global 0.018", GE)
        scene.add(self.t, self.axis, self.cols, self.gline, self.gtag)
        self.labels = {}
        for i in labels:
            self.labels[i] = _vlabel(mode, i, H[i]); scene.add(self.labels[i])
        self.names = None
        if names and mode != "one":
            self.names = _names(mode); scene.add(self.names)

    def raise_to(self, i, h):
        """animations: column i to height h, its value label cross-fades (never morphs mid-glyph)."""
        self.H[i] = h
        xl, w = geom(self.mode)[i]
        anims = [Transform(self.cols[i], _col(xl, w, h))]
        new = _vlabel(self.mode, i, h)
        if i in self.labels:
            anims.append(FadeOut(self.labels[i]))
        anims.append(FadeIn(new)); self.labels[i] = new
        return anims

    def remode(self, mode):
        """animations: every column to its width in `mode` (heights kept); labels and names cross-fade."""
        anims = [Transform(self.cols, _cols(mode, self.H))]
        for i in list(self.labels):
            anims.append(FadeOut(self.labels[i]))
            self.labels[i] = _vlabel(mode, i, self.H[i]); anims.append(FadeIn(self.labels[i]))
        if self.names is not None:
            anims.append(FadeOut(self.names))
        self.names = _names(mode) if mode != "one" else None
        if self.names is not None:
            anims.append(FadeIn(self.names))
        self.mode = mode
        return anims


FULL = [ECE[0], ECE[1], ECE[2], ECE[3], ECE[4]]
FLAT = [GE] * 5


class B10_OneNumber(Scene):
    BASE = 30.0
    def construct(self):
        t = _title("One Number")
        axis = Line([X_L, BASE_Y, 0], [X_R, BASE_Y, 0], color=INK, stroke_width=3)
        self.add(t)
        self.play(Create(axis), run_time=0.8)
        bar = _cols("one", FLAT)
        self.play(GrowFromEdge(bar, LEFT), run_time=1.6)
        pts = _t("12,955 patients").move_to([-1.6, -2.65, 0])
        self.play(FadeIn(pts), run_time=0.5)
        _until(self, "one number:")
        gline = _hline(GE); gtag = _htag("global 0.018", GE)
        self.play(Create(gline), FadeIn(gtag), FadeIn(_note("the report: error 0.018", 2.1)), run_time=0.8)
        _until(self, "Now one row")
        r1 = _note("rare disease: 95 patients", 1.35)
        self.play(FadeIn(r1), run_time=0.6)
        _until(self, "error zero point one zero three")
        r2 = _note("error 0.103", 0.7, bold=True)
        self.play(FadeIn(r2), GrowFromCenter(_dot(-2.5, 0.7)), run_time=0.6)
        _until(self, "Both numbers")
        self.play(FadeIn(_note("both true. how?", 0.05)), run_time=0.6)
        self.play(FadeIn(_cap("an illustrative table")), run_time=0.5)
        _finish(self)


def _hook_notes():
    return VGroup(_note("the report: error 0.018", 2.1), _note("rare disease: 95 patients", 1.35),
                  _note("error 0.103", 0.7, bold=True), _note("both true. how?", 0.05))


class B11_SplitRows(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Split It Into Rows", "one", FLAT)
        hook = _hook_notes(); pts = _t("12,955 patients").move_to([-1.6, -2.65, 0])
        cap0 = _cap("an illustrative table")
        self.add(hook, pts, cap0)
        self.wait(0.4)
        self.play(FadeOut(hook), FadeOut(pts), FadeOut(cap0), run_time=0.6)
        _until(self, "split the report")
        self.play(*st.remode("equal"), run_time=1.6)
        self.play(FadeIn(_note("one column per row", 1.8)), run_time=0.5)
        _until(self, "Adults")
        self.play(*st.raise_to(0, ECE[0]), run_time=0.9)
        _until(self, "Children")
        self.play(*st.raise_to(1, ECE[1]), run_time=0.9)
        _until(self, "So far")
        self.play(FadeIn(_note("close to the global, so far", 1.1)), run_time=0.6)
        self.play(FadeIn(_cap("five rows, one column each")), run_time=0.5)
        _finish(self)


class B12_ThreeClimb(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Three Rows Climb", "equal", [ECE[0], ECE[1], GE, GE, GE], labels=(0, 1))
        self.wait(0.3)
        _until(self, "People over")
        self.play(*st.raise_to(2, ECE[2]), run_time=0.9)
        _until(self, "Pregnancy")
        self.play(*st.raise_to(3, ECE[3]), run_time=0.9)
        _until(self, "Rare disease")
        self.play(*st.raise_to(4, ECE[4]), run_time=1.0)
        _until(self, "Now draw")
        twice = _hline(2 * GE); ttag = _htag("twice global", 2 * GE)
        self.play(Create(twice), FadeIn(ttag), run_time=0.9)
        _until(self, "Three of the five")
        self.play(FadeIn(_note("three of five above it", 1.4)), GrowFromCenter(_dot(2.62, EQ_LY[4])), run_time=0.6)
        self.play(FadeIn(_cap("the flag: above twice global")), run_time=0.5)
        _finish(self)


class B13_AverageRows(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Average The Rows?", "equal", FULL, labels=range(5))
        twice = _hline(2 * GE); ttag = _htag("twice global", 2 * GE)
        self.add(twice, ttag)
        self.wait(0.3)
        self.play(FadeOut(twice), FadeOut(ttag), run_time=0.5)
        _until(self, "Add the five")
        avg = _hline(ROW_AVG, INK); atag = _htag("row average 0.053", ROW_AVG)
        self.play(Create(avg), FadeIn(atag), run_time=1.0)
        n1 = _note("average of the rows: 0.053", 1.6, size=36)
        self.play(FadeIn(n1), run_time=0.5)
        _until(self, "The report says")
        self.play(FadeIn(_note("the report: 0.018", 0.9, size=36)), run_time=0.5)
        _until(self, "So the global")
        self.play(Create(_x(-0.3, 1.6)), run_time=0.5)
        self.play(FadeIn(_cap("the global does not weigh rows")), run_time=0.5)
        _finish(self)


class B14_WeighPatients(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Weigh By Patients", "equal", FULL, labels=range(5))
        avg = _hline(ROW_AVG, INK); atag = _htag("row average 0.053", ROW_AVG)
        self.add(avg, atag)
        self.wait(0.3)
        self.play(FadeOut(avg), FadeOut(atag), run_time=0.5)
        _until(self, "So make each column")
        self.play(*st.remode("patients"), run_time=2.2)
        self.play(FadeIn(_note("wide: patients. tall: error.", 2.0, size=36)), run_time=0.6)
        _until(self, "The rare-disease column")
        self.play(GrowFromCenter(_dot(2.8, 1.2)), run_time=0.5)
        _until(self, "Adults: zero")
        self.play(FadeIn(_note("adults' area: 0.012", 1.35, size=36)), run_time=0.5)
        _until(self, "The rare row")
        self.play(FadeIn(_note("rare disease area: 0.0008", 0.7, size=36)), run_time=0.5)
        self.play(FadeIn(_cap("area: patients times gap")), run_time=0.5)
        _finish(self)


class B15_Predict(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Commit", "patients", FULL, labels=range(5))
        self.wait(0.4)
        self.play(FadeIn(_note("95 of 12,955 patients", 1.6)), run_time=0.6)
        _until(self, "Here is a line", lead=0.7)
        hund = _hline(GE + 0.01); htag = _htag("a hundredth up", GE + 0.0125)
        self.play(Create(hund), FadeIn(htag), run_time=0.6)
        _until(self, "Is there any error")
        self.play(FadeIn(_note("any error big enough?", 0.9)), GrowFromCenter(_dot(2.8, 1.2)), run_time=0.6)
        self.play(FadeIn(_cap("commit before it moves")), run_time=0.5)
        _finish(self)


class B16_PourAndLift(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Pour It In, Lift It Out", "patients", FULL, labels=range(5))
        hund = _hline(GE + 0.01); htag = _htag("a hundredth up", GE + 0.0125)
        self.add(hund, htag)
        self.wait(0.3)
        # 1 — pour: the sliver's area spread over the whole axis, on top of the global line
        sliver = st.cols[4]
        film = Rectangle(width=8.4, height=PULL[4] * YS, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([-1.6, GY + PULL[4] * YS / 2, 0])
        self.play(FadeOut(st.labels[4]), run_time=0.4)
        self.play(ReplacementTransform(sliver, film), run_time=1.8)
        n1 = _note("spread over everyone: 0.0008", 1.6, size=36)
        self.play(FadeIn(n1), run_time=0.5)
        # 2 — the worst case: every gap on the row = 1 → share 0.0073, still under the hundredth line
        _until(self, "Push that row's error")
        worst = Rectangle(width=8.4, height=SHARE[4] * YS, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([-1.6, GY + SHARE[4] * YS / 2, 0])
        n2 = _note("at error 1: 0.0073", 0.95, size=36)
        self.play(FadeIn(n2), run_time=0.5)
        self.play(Transform(film, worst), run_time=1.5)
        _until(self, "It never reaches")
        self.play(Transform(film, Rectangle(width=8.4, height=PULL[4] * YS, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([-1.6, GY + PULL[4] * YS / 2, 0])), run_time=0.9)
        # 3 — lift: gather back into the sliver, then give it its own denominator
        _until(self, "Now lift it out")
        xl, w = geom("patients")[4]
        back = _col(xl, w, ECE[4])
        others = VGroup(*[st.cols[i] for i in range(4)], *[st.labels[i] for i in range(4)], st.names, hund, htag)
        self.play(ReplacementTransform(film, back), FadeOut(others), FadeOut(n1), FadeOut(n2), run_time=1.2)
        tower = Rectangle(width=8.4, height=ECE[4] * YS, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([-1.6, BASE_Y + ECE[4] * YS / 2, 0])
        self.play(Transform(back, tower), run_time=1.6)
        inner = Line([X_L, GY, 0], [X_R, GY, 0], color=STAGE, stroke_width=4)
        self.play(Create(inner), run_time=0.5)
        self.play(FadeIn(_t("on its own 95: 0.103", 40).move_to([-1.6, 2.3, 0])), GrowFromCenter(_dot(0.9, 2.3)), run_time=0.5)
        self.play(FadeIn(_cap("almost six times the global")), run_time=0.5)
        _finish(self)


# the ECE_g formula, built from explicitly placed pieces (no get_* positioning — Gate A stub)
FY = 1.35
def _formula(size=56, y=FY, dx=0.0):
    return VGroup(_m(r"\mathrm{ECE}_g \;=", size).move_to([-4.3 + dx, y, 0]),
                  _m(r"\sum_{m}", size).move_to([-2.55 + dx, y, 0]),
                  _m(r"\frac{|B_m^g|}{N_g}", size).move_to([-1.35 + dx, y, 0]),
                  _m(r"\left|\,\mathrm{acc}(B_m^g) - \mathrm{conf}(B_m^g)\,\right|", size).move_to([2.35 + dx, y, 0]))


class B17_NameIt(Scene):
    BASE = 30.0
    def construct(self):
        t = _title("A Number Per Group")
        axis = Line([X_L, BASE_Y, 0], [X_R, BASE_Y, 0], color=INK, stroke_width=3)
        tower = Rectangle(width=8.4, height=ECE[4] * YS, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([-1.6, BASE_Y + ECE[4] * YS / 2, 0])
        inner = Line([X_L, GY, 0], [X_R, GY, 0], color=STAGE, stroke_width=4)
        gtag = _htag("global 0.018", GE)
        self.add(t, axis, tower, inner, gtag)
        self.wait(0.3)
        # the tower folds back to the rare row's sliver, parked at the lower right
        sliver = Rectangle(width=0.08, height=1.1, fill_color=COL, fill_opacity=1, stroke_width=0).move_to([5.5, -2.35, 0])
        self.play(Transform(tower, sliver), FadeOut(inner), FadeOut(axis), FadeOut(gtag), run_time=1.2)
        self.play(FadeIn(_t("subgroup calibration error", 44, INK, bold=True).move_to([0, -1.3, 0])), run_time=0.6)
        f = _formula()
        _until(self, "Same formula")
        self.play(FadeIn(f[0]), run_time=0.5)
        _until(self, "Sum over")
        self.play(FadeIn(f[1]), FadeIn(_t("every bin").move_to([-2.7, -0.45, 0])), run_time=0.5)
        _until(self, "weigh each bin")
        self.play(FadeIn(f[2]), run_time=0.5)
        _until(self, "take the gap")
        self.play(FadeIn(f[3]), FadeIn(_t("the gap").move_to([2.35, 0.05, 0])), run_time=0.5)
        # the sliver flies into the denominator: N_g is the width we just divided by
        _until(self, "But count the shares", lead=1.0)
        under = Rectangle(width=0.7, height=0.07, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([-1.35, 0.62, 0])
        self.play(Transform(tower, under), FadeIn(_t("the group's own size").move_to([-0.9, 0.05, 0])), run_time=0.8)
        self.play(GrowFromCenter(_dot(-0.62, 0.62, 0.11)), run_time=0.4)
        _until(self, "Then report")
        self.play(FadeIn(_t("report the global and every group", 36).move_to([0, -1.95, 0])), run_time=0.5)
        _until(self, "and flag")
        self.play(FadeIn(_t("flag any group above twice the global", 36).move_to([0, -2.55, 0])), run_time=0.5)
        _finish(self)


class B18_Tangent(Scene):
    BASE = 34.0
    def construct(self):
        self.add(_title("Read The Line"))
        f = _formula(size=48, y=1.95, dx=0.3)
        self.play(FadeIn(f), run_time=0.7)
        self.play(Create(Line([0.55, 1.05, 0], [0.55, -1.75, 0], color=GHOST, stroke_width=3)), run_time=0.4)
        rows = [("Left", "left: the error for group g", 0.85), ("Right", "right: a sum over confidence bins", 0.3),
                ("In each bin", "each bin: group share times gap", -0.25)]
        for ph, s, y in rows:
            _until(self, ph)
            self.play(FadeIn(_t(s).move_to([-5.8, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.15), run_time=0.6)
        _until(self, "The only new symbol")
        self.play(FadeIn(_m(r"N_g", 44).move_to([-5.45, -0.9, 0])), FadeIn(_t("the group's own size").move_to([-4.85, -0.9, 0], aligned_edge=LEFT)), run_time=0.6)
        _until(self, "in the global", lead=1.3)
        self.play(Write(_m(r"\frac{95}{12955} = 0.0073", 48).move_to([3.1, 0.8, 0])), run_time=0.8)
        self.play(FadeIn(_t("its weight in the global").move_to([3.1, -0.05, 0])), run_time=0.4)
        _until(self, "In its own number")
        self.play(Write(_m(r"\frac{95}{95} = 1", 48).move_to([3.1, -0.9, 0])), GrowFromCenter(_dot(4.45, -0.9)), run_time=0.7)
        self.play(FadeIn(_t("its weight in its own number").move_to([3.1, -1.7, 0])), run_time=0.4)
        _until(self, "One more thing")
        self.play(Write(_m(r"0.018 \le 0.028", 48).move_to([-4.3, -2.45, 0])), run_time=0.7)
        self.play(FadeIn(_t("the pooled number can sit lower:").move_to([-2.4, -2.2, 0], aligned_edge=LEFT)),
                  FadeIn(_t("opposite gaps cancel in a bin").move_to([-2.4, -2.75, 0], aligned_edge=LEFT)), run_time=0.6)
        _finish(self)


class B19_BothTrue(Scene):
    BASE = 30.0
    def construct(self):
        st = _Stage(self, "Both True", "one", FLAT)
        hook = _hook_notes(); pts = _t("12,955 patients").move_to([-1.6, -2.65, 0])
        self.add(hook, pts)
        self.wait(0.6)
        _until(self, "Both true")
        self.play(FadeOut(hook), FadeOut(pts), FadeIn(_note("both true", 1.9, size=44, bold=True)), GrowFromCenter(_dot(-2.75, 1.9)), run_time=0.6)
        _until(self, "The global weighs")
        st.H = list(FULL)
        st.labels = {i: _vlabel("patients", i, FULL[i]) for i in range(5)}
        twice = _hline(2 * GE); ttag = _htag("twice global", 2 * GE)
        self.play(Transform(st.cols, _cols("patients", FULL)), *[FadeIn(st.labels[i]) for i in range(5)], FadeIn(_names("patients")), run_time=2.0)
        self.play(Create(twice), FadeIn(ttag), FadeIn(_note("report every group", 1.2)), run_time=0.7)
        _until(self, "Not taught here")
        self.play(FadeIn(_cap("not taught here: when to halt")), run_time=0.5)
        _finish(self)
