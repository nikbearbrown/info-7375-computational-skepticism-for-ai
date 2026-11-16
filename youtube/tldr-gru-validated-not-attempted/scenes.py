"""
Manim scenes for tldr-gru-validated-not-attempted (tldr skill — LEARN section 1, B10–B19).

The persistent world: Gru's FIVE PHASES as squares in a row (1 problem · 2 needs ·
3 principles · 4 components · 5 SDD), a GATE (an upright) in front of each —
thin ghost = open, thick ink = closed/validated. Below: one NEED under phase 2
(its dot at NEED, its label to the left), and COMPONENTS under phase 4 (dots at
x=1.6, labels to the right): the single-page address form (A) and the
recommendation widget (W). A trace is a line from a component back to where it
lands. A vague need is drawn as a pale FOG around the need that any trace can
land in; a validated need is a single point. B16 is the collision: the fog from
the one-pass draft collapses onto the specific need, the address form's trace
still lands, the widget's trace is left hanging, and gate 4 turns it back.

State factory: `_Stage(scene, title, **state)` rebuilds the world at the previous
beat's end state, so the last frame of Bk is the first frame of Bk+1.

Structure asserted at import (FACTCHECK.md). INK text on the cream stage;
terracotta is ONE accent per scene — a dot or an X, never text, never a line,
never a bar, never a ring (GATE T). No text inside any outline (GATE T §8.6b).
Explicit coords inside ±6.2 × ±3.3 (never get_right() — Gate A's stub). Type
floor 32 (titles 40). Text is faded, never morphed.

Pacing: `_until(self, phrase)` — each reveal waits for the spoken phrase
(character share of the narration × measured audio); `_finish` holds to the end.
"""
import json as _json, os as _os
import numpy as np
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the paste's structure (asserted — FACTCHECK rows 3–9) ═══════════
PHASES = {1: "problem", 2: "needs", 3: "principles", 4: "components", 5: "SDD"}
NEEDS_PHASE, COMPONENTS_PHASE = 2, 4                     # gate 4 traces components to needs from phase 2 (the gate list)
SPEC = ["reduce abandonment", "caused by the 3-step", "address form"]   # the paste's passing need, on three lines
VAGUE = "improve user experience"                                        # the paste's failing need
assert " ".join(SPEC) == "reduce abandonment caused by the 3-step address form"
assert len(PHASES) == 5 and PHASES[NEEDS_PHASE] == "needs" and PHASES[COMPONENTS_PHASE] == "components"
for line in SPEC + [VAGUE]:
    assert not line.lower().startswith("w")              # Pango shifts a Paragraph line that starts with 'w'

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}
_BASE_DEFAULT = 20.0


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
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)


# ═══════════ geometry ═══════════
PX = {1: -4.8, 2: -2.4, 3: 0.0, 4: 2.4, 5: 4.8}
NODE_Y, NS = 2.15, 0.42
LAB_Y = 1.5
GATE_X = {i: PX[i] - 1.0 for i in PX}
GATE_Y0, GATE_Y1 = 1.85, 2.45
CHECK_Y = 1.0
NEED = np.array([-1.6, 0.3, 0])
NEED_LAB_X = -1.85
COMP = {"A": np.array([1.6, 0.3, 0]), "W": np.array([1.6, -1.05, 0])}
COMP_NAME = {"A": "single-page address form", "W": "recommendation widget"}
COMP_LAB_X = 1.85
FOG_C, FOG_R = np.array([-0.9, -0.15, 0]), 0.9
FOG_END = np.array([-0.6, -0.6, 0])                     # where the widget's trace ends (in the fog, or in empty space)
BAND_Y = -1.95
assert np.linalg.norm(NEED - FOG_C) < FOG_R and np.linalg.norm(FOG_END - FOG_C) < FOG_R   # both land inside the fog
assert FOG_C[0] + FOG_R < COMP_LAB_X                     # the fog never reaches a component label


# ═══════════ text + mark helpers ═══════════
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _title(txt, size=40): return _t(txt, size).move_to([0, 3.02, 0])
def _cap(txt, x=3.2, y=-3.05): return _t(txt, 32, DIM).move_to([x, y, 0])
def _band(txt, y=BAND_Y, bold=False): return _t(txt, 32, INK, bold).move_to([0, y, 0])
def _para(lines, size=32, align="center"): return Paragraph(*lines, font=SERIF, color=INK, font_size=size, alignment=align, line_spacing=0.95)
def _tdot(x, y, r=0.12): return Dot([x, y, 0], color=TERRA, radius=r)
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _check(x, y, s=0.17, color=INK):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.8, 0], color=color, stroke_width=6),
                  Line([x - s * 0.3, y - s * 0.8, 0], [x + s * 1.1, y + s * 0.9, 0], color=color, stroke_width=6))

def _node(i, filled=True):
    return Square(NS, stroke_color=INK if filled else DIM, stroke_width=3,
                  fill_color=INK, fill_opacity=1 if filled else 0).move_to([PX[i], NODE_Y, 0])
def _label(i): return _t(f"{i} {PHASES[i]}", 32).move_to([PX[i], LAB_Y, 0])
def _gate(i, closed):
    return Line([GATE_X[i], GATE_Y0, 0], [GATE_X[i], GATE_Y1, 0],
                color=INK if closed else GHOST, stroke_width=9 if closed else 4)
def _need_label(kind):
    if kind == "spec":
        return _para(SPEC, align="right").move_to([NEED_LAB_X, NEED[1], 0], aligned_edge=RIGHT)
    return _t(VAGUE, 32).move_to([NEED_LAB_X, NEED[1], 0], aligned_edge=RIGHT)
def _ndot(color=INK): return Dot(NEED, color=color, radius=0.1)
def _cdot(c, color=INK): return Dot(COMP[c], color=color, radius=0.1)
def _clab(c): return _t(COMP_NAME[c], 32).move_to([COMP_LAB_X, COMP[c][1], 0], aligned_edge=LEFT)
def _trace(c, color=INK):
    end = NEED if c == "A" else FOG_END
    return Line(COMP[c], end, color=color, stroke_width=4)
def _fog():
    f = Circle(radius=FOG_R, stroke_width=0, fill_color=GHOST, fill_opacity=1).move_to(FOG_C)
    f.set_z_index(-5)
    return f

ALL_F = {i: "f" for i in PX}
QUOTE = "“a guess wearing a decision’s clothes” — Gru"
RULE = ("phase gate: no valid output from the next phase", "until this one is validated — not attempted")


class _Stage:
    """The world at a given state. nodes {i: 'f'|'h'}, gates {i: 'o'|'c'} (absent = no gate), checks, need None|'spec'|'vague',
    fog, comps (subset of 'A','W'), traces (subset), dim (downstream shapes in DIM), plus the beat-end extras."""
    def __init__(self, scene, title, nodes=None, gates=None, checks=False, need=None, fog=False, comps=(), traces=(),
                 dim=False, band=None, band_bold=False, cap=None, tdot=None, wx=False, needx=False, rule=False, quote=False,
                 ghostring=False, band_y=BAND_Y, lcap=None):
        s = scene
        self.title = _title(title); s.add(self.title)
        nodes = nodes or ALL_F
        self.nodes = {i: _node(i, nodes[i] == "f") for i in PX}
        self.labels = {i: _label(i) for i in PX}
        s.add(*self.nodes.values(), *self.labels.values())
        self.gates = {i: _gate(i, k == "c") for i, k in (gates or {}).items()}
        s.add(*self.gates.values())
        self.checks = [_check(PX[i], CHECK_Y) for i in PX] if checks else []
        s.add(*self.checks)
        shape = DIM if dim else INK
        self.fog = _fog() if fog else None
        if fog: s.add(self.fog)
        self.need_label = _need_label(need) if need else None
        self.ndot = _ndot(shape) if need else None
        if need: s.add(self.need_label, self.ndot)
        self.traces = {c: _trace(c, shape) for c in traces}
        s.add(*self.traces.values())
        self.cdots = {c: _cdot(c, shape) for c in comps}
        self.clabs = {c: _clab(c) for c in comps}
        s.add(*self.cdots.values(), *self.clabs.values())
        self.band = _band(band, band_y, band_bold) if band else None
        if band: s.add(self.band)
        self.cap = _cap(cap) if cap else None
        if cap: s.add(self.cap)
        self.lcap = _cap(lcap, x=-3.2) if lcap else None
        if lcap: s.add(self.lcap)
        self.tdot = _tdot(*tdot[:2], r=0.15 if tuple(tdot[:2]) in ((NEED[0], NEED[1]), (COMP["W"][0], COMP["W"][1])) else 0.12) if tdot is not None else None
        if tdot is not None: s.add(self.tdot)
        self.wx = _x(FOG_END[0], FOG_END[1]) if wx else None
        if wx: s.add(self.wx)
        self.needx = _x(-3.8, -0.25) if needx else None
        if needx: s.add(self.needx)
        self.rule = VGroup(_band(RULE[0], -1.75), _band(RULE[1], -2.3)) if rule else None
        if rule: s.add(self.rule)
        self.quote = _t(QUOTE, 32, DIM).move_to([0, -3.05, 0]) if quote else None
        if quote: s.add(self.quote)
        self.ghostring = DashedVMobject(Circle(radius=0.16, color=GHOST, stroke_width=4).move_to(COMP["W"]), num_dashes=8) if ghostring else None
        if ghostring: s.add(self.ghostring)


def _fill(node): return node.animate.set_fill(INK, 1).set_stroke(INK)
def _hollow(node): return node.animate.set_fill(INK, 0).set_stroke(DIM)


class B10_LooksFinished(Scene):
    BASE = 20.0
    def construct(self):
        self.add(_title("A Design That Looks Finished"))
        cues = {1: "the problem", 2: "the needs", 3: "the principles", 4: "the components", 5: "the assembled design"}
        for i in PX:
            _until(self, cues[i], lead=0.15)
            self.play(GrowFromCenter(_node(i)), FadeIn(_label(i)), run_time=0.45)
        _until(self, "Every one of them has words")
        self.play(*[Create(_check(PX[i], CHECK_Y)) for i in PX], run_time=0.9)
        self.play(FadeIn(_cap("constructed example")), run_time=0.4)
        _until(self, "at two in the morning")
        self.play(GrowFromCenter(_cdot("W")), FadeIn(_clab("W")), run_time=0.6)
        _until(self, "why does this exist")
        self.play(FadeIn(_band("why does this exist?", bold=True)), GrowFromCenter(_tdot(-2.2, BAND_Y)), run_time=0.5)
        _finish(self)


class B11_TracesToANeed(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "A Design That Looks Finished", checks=True, comps=("W",), band="why does this exist?", band_bold=True,
                    tdot=(-2.2, BAND_Y), cap="constructed example")
        self.play(*[FadeOut(c) for c in st.checks], FadeOut(st.cdots["W"]), FadeOut(st.clabs["W"]), FadeOut(st.band),
                  FadeOut(st.tdot), FadeOut(st.cap), FadeOut(st.title), FadeIn(_title("Every Component Traces to a Need")),
                  FadeIn(_cap("gate 4 rule: trace to a need", x=-3.2)), run_time=0.8)
        _until(self, "Take the need")
        self.play(GrowFromCenter(_ndot()), FadeIn(_need_label("spec")), run_time=0.7)
        _until(self, "Now propose a component")
        self.play(GrowFromCenter(_cdot("A")), FadeIn(_clab("A")), run_time=0.6)
        _until(self, "Draw its line back")
        self.play(Create(_trace("A")), run_time=1.0)
        _until(self, "It lands")
        self.play(GrowFromCenter(_tdot(NEED[0], NEED[1], r=0.15)), run_time=0.4)
        _until(self, "That component has a reason")
        self.play(FadeIn(_band("its reason is written down")), run_time=0.5)
        _finish(self)


class B12_NowhereToLand(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Every Component Traces to a Need", need="spec", comps=("A",), traces=("A",),
                    band="its reason is written down", tdot=(NEED[0], NEED[1]), lcap="gate 4 rule: trace to a need")
        self.play(FadeOut(st.band), FadeOut(st.tdot), run_time=0.5)
        _until(self, "Propose a recommendation widget")
        self.play(GrowFromCenter(_cdot("W")), FadeIn(_clab("W")), run_time=0.6)
        _until(self, "try to draw its line back")
        self.play(Create(_trace("W")), run_time=1.2)
        _until(self, "The line has nowhere to land")
        self.play(Create(_x(FOG_END[0], FOG_END[1])), run_time=0.5)
        _until(self, "asks which need it serves")
        self.play(FadeIn(_band("which need does it serve?")), run_time=0.5)
        _until(self, "scope creep")
        self.play(FadeIn(_cap("otherwise: scope creep")), run_time=0.4)
        _finish(self)


class B13_OnePass(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Every Component Traces to a Need", need="spec", comps=("A", "W"), traces=("A", "W"), wx=True,
                    band="which need does it serve?", cap="otherwise: scope creep", lcap="gate 4 rule: trace to a need")
        self.play(FadeOut(st.wx), FadeOut(st.traces["W"]), FadeOut(st.band), FadeOut(st.cap), FadeOut(st.lcap),
                  FadeOut(st.title), FadeIn(_title("The Obvious Approach: One Pass")), run_time=0.8)
        _until(self, "ask Claude for the whole design")
        b1 = _band("one pass, reviewed at the end")
        self.play(FadeIn(b1), run_time=0.5)
        _until(self, "All five sections fill at once")
        self.play(*[Indicate(st.nodes[i], color=INK, scale_factor=1.25) for i in PX], run_time=0.9)
        _until(self, "improve user experience")
        self.play(GrowFromCenter(_fog()), FadeOut(st.need_label), FadeIn(_need_label("vague")), run_time=1.0)
        _until(self, "The address form traces")
        self.play(Indicate(st.traces["A"], color=INK, scale_factor=1.05), run_time=0.7)
        _until(self, "So does the widget")
        self.play(Create(_trace("W")), run_time=1.0)
        _until(self, "Every check passes")
        self.play(FadeOut(b1), FadeIn(_band("every component traces. every check passes.")),
                  GrowFromCenter(_tdot(COMP["W"][0], COMP["W"][1] - 0.45)), run_time=0.6)
        _finish(self)


class B14_FiveGates(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "The Obvious Approach: One Pass", need="vague", fog=True, comps=("A", "W"), traces=("A", "W"),
                    band="every component traces. every check passes.", tdot=(COMP["W"][0], COMP["W"][1] - 0.45))
        self.play(FadeOut(st.band), FadeOut(st.tdot), FadeOut(st.title), FadeIn(_title("Five Phases, Five Gates")), run_time=0.7)
        _until(self, "Put a gate in front")
        self.play(*[Create(_gate(i, False)) for i in PX], run_time=1.0)
        _until(self, "Gru's rule")
        self.play(*[_hollow(st.nodes[i]) for i in (2, 3, 4, 5)],
                  *[m.animate.set_color(DIM) for m in [st.ndot, *st.traces.values(), *st.cdots.values()]], run_time=0.8)
        _until(self, "Validated.")
        b1 = _band("validated — not attempted", bold=True)
        self.play(FadeIn(b1), run_time=0.5)
        _until(self, "The problem passes")
        self.play(Create(_gate(1, True)), run_time=0.6)
        _until(self, "could this need turn out to be wrong")
        self.play(FadeOut(b1), FadeIn(_band("gate 2: could this need turn out wrong?")), run_time=0.6)
        _until(self, "It fails the gate")
        self.play(Create(_x(-3.8, -0.25)), run_time=0.5)
        _finish(self)


GATED = dict(nodes={1: "f", 2: "h", 3: "h", 4: "h", 5: "h"}, gates={1: "c", 2: "o", 3: "o", 4: "o", 5: "o"},
             need="vague", fog=True, comps=("A", "W"), traces=("A", "W"), dim=True)


class B15_Commit(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Five Phases, Five Gates", band="gate 2: could this need turn out wrong?", needx=True, **GATED)
        self.play(FadeOut(st.band), FadeOut(st.needx), run_time=0.5)
        _until(self, "Gate two is about to")
        b1 = _band("gate 2 will make the need specific")
        self.play(FadeIn(b1), run_time=0.5)
        _until(self, "where does the widget's line land")
        self.play(GrowFromCenter(_tdot(COMP["W"][0], COMP["W"][1], r=0.15)), FadeOut(b1),
                  FadeIn(_band("where does the widget's line land?")), run_time=0.6)
        _finish(self)


class B16_FogCollapses(Scene):
    BASE = 16.0
    def construct(self):
        st = _Stage(self, "Five Phases, Five Gates", band="where does the widget's line land?",
                    tdot=(COMP["W"][0], COMP["W"][1]), **GATED)
        self.play(FadeOut(st.tdot), run_time=0.4)
        _until(self, "The need becomes specific")
        self.play(FadeOut(st.need_label), FadeIn(_need_label("spec")), Create(_gate(2, True)), _fill(st.nodes[2]), run_time=0.8)
        _until(self, "collapses to one point")
        self.play(st.fog.animate.scale(0.08).move_to(NEED), run_time=1.2)
        self.play(FadeOut(st.fog), st.ndot.animate.set_color(INK), run_time=0.3)
        _until(self, "The address form's line finds it")
        self.play(st.traces["A"].animate.set_color(INK), st.cdots["A"].animate.set_color(INK), run_time=0.6)
        _until(self, "The widget's line finds nothing")
        wx = _x(FOG_END[0], FOG_END[1])
        self.play(Create(wx), run_time=0.5)
        _until(self, "Gate four holds")
        self.play(Create(_gate(3, True)), Create(_gate(4, True)), _fill(st.nodes[3]), _fill(st.nodes[4]), run_time=0.8)
        self.play(FadeOut(VGroup(st.cdots["W"], st.clabs["W"], st.traces["W"], wx), shift=RIGHT * 0.3), run_time=0.9)
        self.play(FadeOut(st.band), FadeIn(_band("gate 4: back with a question")), run_time=0.5)
        _finish(self)


DONE4 = dict(nodes={1: "f", 2: "f", 3: "f", 4: "f", 5: "h"}, gates={1: "c", 2: "c", 3: "c", 4: "c", 5: "o"},
             need="spec", comps=("A",), traces=("A",))
DONE5 = dict(nodes=ALL_F, gates={i: "c" for i in PX}, need="spec", comps=("A",), traces=("A",))


class B17_PhaseGate(Scene):
    BASE = 16.0
    def construct(self):
        st = _Stage(self, "Five Phases, Five Gates", band="gate 4: back with a question", **DONE4)
        self.play(FadeOut(st.band), FadeOut(st.title), FadeIn(_title("A Phase Gate")), run_time=0.7)
        _until(self, "A phase gate")
        self.play(FadeIn(_band(RULE[0], -1.75)), run_time=0.6)
        self.play(FadeIn(_band(RULE[1], -2.3)), GrowFromCenter(_tdot(-4.25, -1.75)), run_time=0.6)
        _until(self, "Skip one")
        self.play(Create(_gate(5, True)), _fill(st.nodes[5]), run_time=0.8)
        _until(self, "a guess wearing")
        self.play(FadeIn(_t(QUOTE, 32, DIM).move_to([0, -3.05, 0])), run_time=0.6)
        _finish(self)


class B18_TwoAM(Scene):
    BASE = 18.0
    def construct(self):
        st = _Stage(self, "A Phase Gate", rule=True, quote=True, tdot=(-4.25, -1.75), **DONE5)
        self.play(FadeOut(st.rule), FadeOut(st.quote), FadeOut(st.tdot),
                  FadeOut(st.title), FadeIn(_title("Back to Two in the Morning")), run_time=0.8)
        _until(self, "because there isn't one")
        ring = DashedVMobject(Circle(radius=0.16, color=GHOST, stroke_width=4).move_to(COMP["W"]), num_dashes=8)
        self.play(Create(ring), FadeIn(_cap("no widget: it never passed gate 4")), run_time=0.7)
        _until(self, "why does this exist")
        b1 = _band("why does this exist?", bold=True)
        self.play(FadeIn(b1), Indicate(st.cdots["A"], color=INK, scale_factor=1.6), run_time=0.7)
        _until(self, "Follow the line")
        trav = Dot(COMP["A"], color=INK, radius=0.13)
        self.play(GrowFromCenter(trav), run_time=0.3)
        self.play(trav.animate.move_to(NEED), run_time=1.4)
        _until(self, "The answer is sitting")
        self.play(GrowFromCenter(_tdot(-5.55, NEED[1])), FadeOut(b1), FadeIn(_band("the answer is in phase 2")), run_time=0.6)
        _finish(self)


class B19_TwoExits(Scene):
    BASE = 16.0
    def construct(self):
        st = _Stage(self, "Back to Two in the Morning", band="the answer is in phase 2", cap="no widget: it never passed gate 4",
                    ghostring=True, tdot=(-5.55, NEED[1]), **DONE5)
        self.play(FadeOut(st.need_label), FadeOut(st.ndot), FadeOut(st.traces["A"]), FadeOut(st.cdots["A"]), FadeOut(st.clabs["A"]),
                  FadeOut(st.band), FadeOut(st.cap), FadeOut(st.ghostring), FadeOut(st.tdot),
                  FadeOut(st.title), FadeIn(_title("Two Deliberate Exits")), run_time=0.9)
        _until(self, "Silent mode skips")
        arc = DashedVMobject(ArcBetweenPoints([GATE_X[1], 1.1, 0], [PX[5], 1.1, 0], angle=0.6, color=DIM, stroke_width=4), num_dashes=40)
        self.play(Create(arc), run_time=1.2)
        self.play(FadeIn(_band("silent: skips every gate", -0.3)), run_time=0.5)
        _until(self, "And slash claude")
        ring = VGroup(*[Dot([0.35 * np.cos(a), -1.4 + 0.35 * np.sin(a), 0], color=INK, radius=0.08)
                        for a in np.linspace(np.pi / 2, np.pi / 2 + 2 * np.pi, 5, endpoint=False)])
        self.play(*[GrowFromCenter(d) for d in ring], run_time=0.7)
        self.play(FadeIn(_band("/claude: scores what exists, any stage", -2.2)), GrowFromCenter(_tdot(-3.55, -2.2)), run_time=0.5)
        _until(self, "Neither is the default")
        self.play(FadeIn(_cap("neither is the default")), run_time=0.5)
        _finish(self)
