"""
Manim scenes for tldr-where-the-human-steps-fall (tldr skill — LEARN section 1, B10–B19).

The persistent world: the Paper Summarizer's SIX STEP BOXES in a row (Figure 9.3,
rebuilt from its caption) — 1 taxonomy · 2 parse · 3 extract · 4 audit · 5 format ·
6 sign-off. Human-owned boxes are filled ink (1, 4, 6); AI boxes are outlined
(2, 3, 5). Under each box a schematic "looks like work" bar (dim — the foil):
tall under the AI steps, short under the human steps. From B14 the bars become
five-cell columns — the five Boondoggle questions — light (small dim square) or
dark (large ink square). B16 is the collision: every bar morphs into its column
and the dark columns land exactly under the ink boxes.

State factory: `_Stage(scene, title, **state)` rebuilds the world at the previous
beat's end state, so the last frame of Bk is the first frame of Bk+1.

Structure asserted at import (FACTCHECK.md). INK text on the cream stage;
terracotta is ONE accent per scene — a dot or an X beside a word, never text,
never a line, never a bar, never a ring (GATE T). Explicit coords inside
±6.2 × ±3.3 (never get_right() — Gate A's stub). Type floor 32 (titles 40).
Captions ≤ 34 chars at x ≈ 3.2. Text is faded, never morphed (GATE T samples the
50% frame).

Pacing: the exemplar's `_TARGET` block plus `_until(self, phrase)` — each reveal
waits for the spoken phrase (character share of the narration × measured audio).
"""
import json as _json, os as _os
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's score (asserted — FACTCHECK rows 4, 11, 21, 22) ═══════════
STEPS = {1: "taxonomy", 2: "parse", 3: "extract", 4: "audit", 5: "format", 6: "sign-off"}
HUMAN = {1, 4, 6}; AI = {2, 3, 5}
ROWS = ["verification", "stakes", "distribution", "reversibility", "audit trail"]
DARK = {1: {"stakes", "distribution"}, 2: set(), 3: set(), 4: {"verification", "stakes", "distribution"},
        5: set(), 6: {"verification", "stakes", "reversibility"}}
assert HUMAN | AI == set(STEPS) and not HUMAN & AI and AI == {2, 3, 5}
assert all(bool(DARK[s]) == (s in HUMAN) for s in STEPS)
assert all(a in AI and b in HUMAN for a, b in [(3, 4), (5, 6)])
assert len("on the training set only".split()) == 5

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
    self.wait(max(0.3, target - _elapsed(self)) if target else 2.0)

# ═══════════ text + mark helpers ═══════════
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _title(txt, size=40): return _t(txt, size).move_to([0, 3.02, 0])
def _cap(txt, x=3.2, y=-3.05): return _t(txt, 32, DIM).move_to([x, y, 0])
def _band(txt, x=0.0, y=-2.52, bold=False): return _t(txt, 32, INK, bold).move_to([x, y, 0])
def _left(txt, x, y, size=32, bold=False, color=INK): return _t(txt, size, color, bold).move_to([x, y, 0], aligned_edge=LEFT)
def _dot(x, y, r=0.12): return Dot([x, y, 0], color=TERRA, radius=r)
def _x(x, y, s=0.18, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _check(x, y, s=0.17, color=INK):
    return VGroup(Line([x - s, y, 0], [x - s * 0.3, y - s * 0.8, 0], color=color, stroke_width=6),
                  Line([x - s * 0.3, y - s * 0.8, 0], [x + s * 1.1, y + s * 0.9, 0], color=color, stroke_width=6))

# ═══════════ geometry ═══════════
CX = {1: -2.45, 2: -0.9, 3: 0.65, 4: 2.2, 5: 3.75, 6: 5.3}
BOX_Y, BW, BH = 2.15, 0.78, 0.66
NAME_Y = 1.52
RAIL_Y = 0.95
ROW_Y = [0.42, -0.13, -0.68, -1.23, -1.78]
ROW_X = -3.35                                            # row labels right-aligned here
BAR_BASE, BAR_W = -2.05, 0.7
BAR_H = {1: 0.6, 2: 2.4, 3: 2.65, 4: 0.75, 5: 2.2, 6: 0.55}
assert all(BAR_H[s] < 1.0 for s in HUMAN) and all(BAR_H[s] > 2.0 for s in AI)   # schematic: AI steps look like work
LIGHT, DARKSZ = 0.3, 0.46

def _box(s, x=None, human=None):
    x = CX[s] if x is None else x
    human = (s in HUMAN) if human is None else human
    r = Rectangle(width=BW, height=BH, stroke_color=INK, stroke_width=3,
                  fill_color=INK, fill_opacity=1 if human else 0).move_to([x, BOX_Y, 0])
    n = _t(str(s), 36, CREAM if human else INK, bold=True).move_to([x, BOX_Y, 0])
    return VGroup(r, n)
def _name(s, txt=None, x=None): return _t(txt or STEPS[s], 32).move_to([CX[s] if x is None else x, NAME_Y, 0])
def _bar(s, h=None):
    h = BAR_H[s] if h is None else h
    return Rectangle(width=BAR_W, height=h, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([CX[s], BAR_BASE + h / 2, 0])
def _cell(s, i, kind, x=None):
    x = CX[s] if x is None else x
    if kind == "dark":
        return Square(DARKSZ, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([x, ROW_Y[i], 0])
    if kind == "light":
        return Square(LIGHT, fill_color=DIM, fill_opacity=1, stroke_width=0).move_to([x, ROW_Y[i], 0])
    return Square(DARKSZ, stroke_color=DIM, stroke_width=3, fill_opacity=0).move_to([x, ROW_Y[i], 0])
def _kind(s, i): return "dark" if ROWS[i] in DARK[s] else "light"
def _column(s, filled=True, x=None): return VGroup(*[_cell(s, i, _kind(s, i) if filled else "ghost", x) for i in range(5)])
def _rowlabels(): return VGroup(*[_t(r, 32).move_to([ROW_X, y, 0], aligned_edge=RIGHT) for r, y in zip(ROWS, ROW_Y)])
def _paper():
    page = Rectangle(width=0.62, height=0.8, stroke_color=INK, stroke_width=3, fill_color=CREAM, fill_opacity=1).move_to([-4.75, BOX_Y, 0])
    lines = VGroup(*[Line([-4.95, BOX_Y + dy, 0], [-4.55, BOX_Y + dy, 0], color=DIM, stroke_width=3) for dy in (0.2, 0.05, -0.1, -0.25)])
    arrow = Arrow([-4.3, BOX_Y, 0], [-2.95, BOX_Y, 0], color=INK, stroke_width=4, buff=0.05, max_tip_length_to_length_ratio=0.2)
    label = _t("paper", 32).move_to([-4.75, NAME_Y, 0])
    return VGroup(page, lines, arrow, label)
def _pointer(s): return Triangle(color=INK, fill_color=INK, fill_opacity=1, stroke_width=0).scale(0.13).move_to([CX[s], RAIL_Y, 0])

# the B11/B12 panel (x positions measured from EB Garamond 32: sentence 9.91 wide; "The model outperformed baselines " 5.77)
PX = -4.35
P_Y, C_Y, Q_Y = 0.42, -0.45, -1.35
QUAL_X0, QUAL_X1 = PX + 5.8, PX + 9.8                    # "on the training set only" span in the paper sentence
SENT = "The model outperformed baselines on the training set only."
CLAIM = "The model outperformed baselines."
CITE = "“The model outperformed baselines on the training set only.”"
def _panel_labels(): return VGroup(_left("paper", -6.05, P_Y, bold=True), _left("claim", -6.05, C_Y, bold=True), _left("citation", -6.05, Q_Y, bold=True))
def _hookq(): return VGroup(_left("three short bars,", -6.05, 0.4), _left("three human steps.", -6.05, -0.1), _left("why?", -6.05, -0.6, bold=True))


class _Stage:
    """The world at a given state. Keys: owners, bars (set), cols {s: 'ghost'|'filled'}, rows, paper, names {s: text}, hookq, panel."""
    def __init__(self, scene, title, owners=True, bars=frozenset(STEPS), cols=None, rows=False, paper=True, names=None,
                 hookq=False, panel=None, pointer=None):
        self.scene = scene
        self.title = _title(title); scene.add(self.title)
        self.paper = _paper() if paper else None
        if paper: scene.add(self.paper)
        self.boxes = {s: _box(s, human=(s in HUMAN) if owners else False) for s in STEPS}
        self.names = {s: _name(s, (names or {}).get(s)) for s in STEPS}
        scene.add(*self.boxes.values(), *self.names.values())
        self.bars = {s: _bar(s) for s in bars}; scene.add(*self.bars.values())
        self.cols = {s: _column(s, filled=(k == "filled")) for s, k in (cols or {}).items()}; scene.add(*self.cols.values())
        self.rows = _rowlabels() if rows else None
        if rows: scene.add(self.rows)
        self.hookq = _hookq() if hookq else None
        if hookq: scene.add(self.hookq)
        self.pointer = _pointer(pointer) if pointer else None
        if pointer: scene.add(self.pointer)
        self.panel = {}
        if panel:
            self.panel["labels"] = _panel_labels()
            self.panel["sent"] = _left(SENT, PX, P_Y)
            corrected = panel.get("corrected", False)
            self.panel["claim"] = _left(SENT if corrected else CLAIM, PX, C_Y)
            if not corrected: self.panel["tag"] = _left("· LOW", 1.8, C_Y, bold=True)
            self.panel["cite"] = _left(CITE, PX, Q_Y)
            if panel.get("check"):
                self.panel["check"] = _check(-5.8, -2.3); self.panel["found"] = _left("found word for word", -5.4, -2.3)
            if panel.get("underlines"):
                self.panel["ul"] = VGroup(Line([PX, P_Y - 0.3, 0], [PX + 9.8, P_Y - 0.3, 0], color=INK, stroke_width=4),
                                          Line([PX + 0.1, Q_Y - 0.3, 0], [PX + 10.2, Q_Y - 0.3, 0], color=INK, stroke_width=4))
            if panel.get("qual"):
                self.panel["qul"] = Line([QUAL_X0, P_Y - 0.3, 0], [QUAL_X1, P_Y - 0.3, 0], color=INK, stroke_width=7)
            if panel.get("spot"):
                self.panel["done"] = _left("step 4: corrected", 0.9, -2.3, bold=True)
                self.panel["spot"] = _spot_group()
            scene.add(*self.panel.values())
    def fade_panel(self): return [FadeOut(m) for m in self.panel.values()]

def _spot_group():
    txt = _left("HIGH entries: 1 in 5 opened", -1.0, -2.95)
    sq = VGroup(*[Square(0.3, stroke_color=INK, stroke_width=3, fill_color=INK, fill_opacity=1 if i == 0 else 0).move_to([4.75 + i * 0.36, -2.95, 0]) for i in range(5)])
    return VGroup(txt, sq)


class B10_SixSteps(Scene):
    BASE = 20.0
    def construct(self):
        self.add(_title("One Summarizer, Six Steps"))
        paper = _paper()
        self.play(FadeIn(paper[0]), FadeIn(paper[1]), FadeIn(paper[3]), run_time=0.6)
        self.play(GrowArrow(paper[2]), run_time=0.5)
        boxes = {s: _box(s, human=False) for s in STEPS}
        cues = {1: "a section taxonomy", 2: "parsing", 3: "claim extraction", 4: "an audit", 5: "formatting", 6: "a sign-off"}
        bars = {s: _bar(s) for s in STEPS}
        for s in STEPS:
            _until(self, cues[s], lead=0.15)
            self.play(Create(boxes[s][0]), FadeIn(boxes[s][1]), FadeIn(_name(s)), GrowFromEdge(bars[s], DOWN), run_time=0.45)
        self.play(FadeIn(_cap("bars: looks like work · schematic")), run_time=0.4)
        _until(self, "Three of them look like real work")
        self.play(*[Indicate(bars[s], color=INK, scale_factor=1.06) for s in (2, 3, 5)], run_time=0.9)
        _until(self, "Three look like somebody")
        self.play(*[Indicate(bars[s], color=INK, scale_factor=1.15) for s in (1, 4, 6)], run_time=0.7)
        _until(self, "the humans get the three short bars")
        self.play(*[boxes[s][0].animate.set_fill(INK, 1) for s in HUMAN], *[FadeTransform(boxes[s][1], _box(s)[1]) for s in HUMAN], run_time=0.8)
        _until(self, "Why would you keep")
        q = _hookq()
        self.play(FadeIn(q[0]), FadeIn(q[1]), run_time=0.5)
        self.play(FadeIn(q[2]), GrowFromCenter(_dot(-4.8, -0.6)), run_time=0.4)
        _finish(self)


class B11_StepThree(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "One Summarizer, Six Steps", hookq=True)
        cap = _cap("bars: looks like work · schematic"); self.add(cap)
        self.play(*[FadeOut(b) for b in st.bars.values()], FadeOut(st.hookq), FadeOut(cap),
                  FadeOut(st.title), FadeIn(_title("Step 3: Claim Extraction")), run_time=0.7)
        labels = _panel_labels()
        self.play(GrowFromCenter(_pointer(3)), FadeIn(labels), FadeIn(_cap("constructed sentence")), run_time=0.5)
        _until(self, "The paper says")
        self.play(FadeIn(_left(SENT, PX, P_Y)), run_time=0.6)
        _until(self, "The AI pulls out the core claim")
        self.play(FadeIn(_left(CLAIM, PX, C_Y)), run_time=0.5)
        _until(self, "tags it low")
        self.play(FadeIn(_left("· LOW", 1.8, C_Y, bold=True)), run_time=0.4)
        _until(self, "attaches a citation")
        self.play(FadeIn(_left(CITE, PX, Q_Y)), run_time=0.5)
        _until(self, "So checking one is a search", lead=0.6)
        self.play(Create(Line([PX + 0.1, Q_Y - 0.3, 0], [PX + 10.2, Q_Y - 0.3, 0], color=INK, stroke_width=4)),
                  Create(Line([PX, P_Y - 0.3, 0], [PX + 9.8, P_Y - 0.3, 0], color=INK, stroke_width=4)), run_time=1.0)
        _until(self, "Seconds")
        self.play(Create(_check(-5.8, -2.3)), FadeIn(_left("found word for word", -5.4, -2.3)), run_time=0.5)
        self.play(GrowFromCenter(_dot(-1.5, -2.3)), run_time=0.3)
        _finish(self)


class B12_StepFour(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Step 3: Claim Extraction", bars=frozenset(), pointer=3, panel={"check": True, "underlines": True})
        cap = _cap("constructed sentence"); self.add(cap)
        self.play(FadeOut(st.title), FadeIn(_title("Step 4: Plausibility Audit")), FadeOut(st.panel["ul"]), FadeOut(cap),
                  st.pointer.animate.move_to([CX[4], RAIL_Y, 0]), run_time=0.8)
        _until(self, "The claim isn't")
        self.play(Indicate(st.panel["claim"], color=INK, scale_factor=1.04), run_time=0.6)
        _until(self, "It dropped five words")
        self.play(Create(Line([QUAL_X0, P_Y - 0.3, 0], [QUAL_X1, P_Y - 0.3, 0], color=INK, stroke_width=7)), run_time=0.7)
        self.play(GrowFromCenter(_dot(QUAL_X1 + 0.3, P_Y - 0.3)), run_time=0.3)
        _until(self, "Corrected")
        self.play(FadeOut(st.panel["claim"]), FadeOut(st.panel["tag"]), run_time=0.3)
        self.play(FadeIn(_left(SENT, PX, C_Y)), FadeIn(_left("step 4: corrected", 0.9, -2.3, bold=True)), run_time=0.5)
        _until(self, "And one in five")
        spot = _spot_group()
        self.play(FadeIn(spot[0]), *[GrowFromCenter(sq) for sq in spot[1]], run_time=0.7)
        _finish(self)


class B13_JustGlance(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Step 4: Plausibility Audit", bars=frozenset(), pointer=4,
                    panel={"check": True, "qual": True, "corrected": True, "spot": True})
        self.play(*st.fade_panel(), FadeOut(st.pointer), FadeOut(st.title), FadeIn(_title("The Obvious Rule")), run_time=0.7)
        self.play(*[GrowFromEdge(_bar(s), DOWN) for s in STEPS], run_time=0.8)
        rule = VGroup(_left("the obvious rule:", -6.05, 0.4), _left("the AI lifts,", -6.05, -0.1), _left("I glance.", -6.05, -0.6, bold=True))
        self.play(FadeIn(rule), run_time=0.5)
        _until(self, "Step four becomes a glance")
        self.play(FadeOut(st.names[4]), FadeIn(_name(4, "glance")), run_time=0.5)
        _until(self, "Step six becomes a glance")
        self.play(FadeOut(st.names[6]), FadeIn(_name(6, "glance")), run_time=0.5)
        token = RoundedRectangle(corner_radius=0.05, width=0.3, height=0.38, fill_color=INK, fill_opacity=1, stroke_width=0).move_to([CX[3], RAIL_Y, 0])
        _until(self, "It leaves step three")
        self.play(GrowFromCenter(token), run_time=0.4)
        _until(self, "A glance waves it through")
        self.play(token.animate.move_to([CX[4], RAIL_Y, 0]), run_time=0.6)
        self.play(Create(_check(CX[4] + 0.42, RAIL_Y + 0.02, 0.13)), run_time=0.3)
        _until(self, "Formatting makes it tidy")
        self.play(token.animate.move_to([CX[5], RAIL_Y, 0]), run_time=0.6)
        _until(self, "Another glance signs it")
        self.play(token.animate.move_to([CX[6], RAIL_Y, 0]), run_time=0.6)
        self.play(Create(_check(CX[6] + 0.42, RAIL_Y + 0.02, 0.13)), run_time=0.3)
        _until(self, "And the reader gets")
        self.play(token.animate.move_to([-3.35, -2.52, 0]), run_time=0.9)
        self.play(FadeOut(token), FadeIn(_left("summary: “The model outperformed baselines.”", -2.95, -2.52)), Create(_x(-3.35, -2.52)), run_time=0.5)
        _until(self, "The bars told us")
        self.play(FadeIn(_cap("effort says nothing about failure", x=3.2, y=-3.07)), run_time=0.5)
        _finish(self)


class B14_FiveQuestions(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "The Obvious Rule", names={4: "glance", 6: "glance"})
        rule = VGroup(_left("the obvious rule:", -6.05, 0.4), _left("the AI lifts,", -6.05, -0.1), _left("I glance.", -6.05, -0.6, bold=True))
        summ = _left("summary: “The model outperformed baselines.”", -2.95, -2.52); xx = _x(-3.35, -2.52)
        cap = _cap("effort says nothing about failure", x=3.2, y=-3.07)
        self.add(rule, summ, xx, cap)
        self.play(FadeOut(rule), FadeOut(summ), FadeOut(xx), FadeOut(cap), FadeOut(st.names[4]), FadeOut(st.names[6]),
                  FadeIn(_name(4)), FadeIn(_name(6)), FadeOut(st.title), FadeIn(_title("Five Questions, Every Step")), run_time=0.7)
        labels = _rowlabels()
        for i, ph in enumerate(["How costly is it to verify", "What does a wrong answer cost", "Is the input the kind", "Can the output be undone", "Does it leave a trail"]):
            _until(self, ph, lead=0.1)
            self.play(FadeIn(labels[i], shift=RIGHT * 0.1), run_time=0.4)
        _until(self, "Score step three")
        ghost = _column(3, filled=False)
        self.play(ReplacementTransform(st.bars[3], ghost), FadeIn(_cap("cells: our reading of the text")), run_time=0.9)
        reasons = [("Verifying it is a search", "verification: a search, in seconds"),
                   ("A mistake gets caught", "stakes: a mistake is caught at step 4"),
                   ("Unsure extractions arrive tagged", "distribution: the unsure ones arrive tagged"),
                   ("The next step can undo", "reversibility: undone at the next step"),
                   ("And the claims, citations", "audit trail: claims, citations, tags")]
        band = None
        for i, (ph, txt) in enumerate(reasons):
            _until(self, ph, lead=0.1)
            nb = _band(txt)
            anims = [Transform(ghost[i], _cell(3, i, "light")), FadeIn(nb)]
            if band is not None: anims.append(FadeOut(band))
            self.play(*anims, run_time=0.5); band = nb
        _until(self, "Five light cells")
        self.play(FadeOut(band), FadeIn(_band("five light cells: hand it to the AI", bold=True)), GrowFromCenter(_dot(-3.3, -2.52)), run_time=0.5)
        _finish(self)


class B15_Commit(Scene):
    BASE = 8.0
    def construct(self):
        st = _Stage(self, "Five Questions, Every Step", bars=frozenset({1, 2, 4, 5, 6}), cols={3: "filled"}, rows=True)
        self.play(ReplacementTransform(st.bars[4], _column(4, filled=False)), run_time=0.8)
        self.play(GrowFromCenter(_dot(CX[4] + 0.62, BOX_Y)), run_time=0.3)
        _until(self, "Which of the five rows")
        self.play(FadeIn(_band("step 4: which rows go dark?", bold=True)), run_time=0.5)
        _until(self, "Pick yours")
        self.play(FadeIn(_cap("commit before it fills")), run_time=0.4)
        _finish(self)


class B16_BarsBecomeColumns(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Five Questions, Every Step", bars=frozenset({1, 2, 5, 6}), cols={3: "filled", 4: "ghost"}, rows=True)
        col4 = st.cols[4]
        for i, ph in [(0, "takes domain judgment"), (1, "misleads the reader"), (2, "the model itself was unsure")]:
            _until(self, ph, lead=0.1)
            anims = [Transform(col4[i], _cell(4, i, "dark"))]
            if i == 2: anims += [Transform(col4[3], _cell(4, 3, "light")), Transform(col4[4], _cell(4, 4, "light"))]
            self.play(*anims, run_time=0.45)
        _until(self, "let every bar become its column")
        self.play(*[ReplacementTransform(st.bars[s], _column(s)) for s in (1, 2, 5, 6)], run_time=1.8)
        _until(self, "The short bars go dark")
        self.play(FadeIn(_band("dark column = human step", bold=True)), GrowFromCenter(_dot(-2.85, -2.52)), run_time=0.5)
        _finish(self)


class B17_TheSeams(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Five Questions, Every Step", bars=frozenset(), cols={s: "filled" for s in STEPS}, rows=True)
        band = _band("dark column = human step", bold=True); self.add(band)
        self.play(FadeOut(band), FadeOut(st.title), FadeIn(_title("Where Light Hands to Dark")), run_time=0.6)
        arrows = {}
        for a, b, ph in [(3, 4, "Three into four"), (5, 6, "and five into six")]:
            _until(self, ph, lead=0.1)
            arrows[a] = Arrow([CX[a] + 0.3, RAIL_Y, 0], [CX[b] - 0.3, RAIL_Y, 0], color=INK, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.3)
            br = VGroup(Line([CX[a] - 0.3, -2.25, 0], [CX[b] + 0.3, -2.25, 0], color=INK, stroke_width=3),
                        Line([CX[a] - 0.3, -2.25, 0], [CX[a] - 0.3, -2.12, 0], color=INK, stroke_width=3),
                        Line([CX[b] + 0.3, -2.25, 0], [CX[b] + 0.3, -2.12, 0], color=INK, stroke_width=3))
            self.play(GrowArrow(arrows[a]), Create(br), run_time=0.6)
        _until(self, "The score calls those")
        self.play(FadeIn(_cap("both run AI to human", x=3.2, y=-3.1)), run_time=0.4)
        _until(self, "the danger is waving")
        self.play(FadeIn(_t("waved through", 32).move_to([1.2, -2.62, 0])), GrowFromCenter(_dot(-0.4, -2.62)), run_time=0.5)
        _until(self, "it's signing the summary")
        self.play(FadeIn(_t("proofread, not read", 32).move_to([4.45, -2.62, 0])), run_time=0.5)
        _finish(self)


class B18_NameIt(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "Where Light Hands to Dark", bars=frozenset(), cols={s: "filled" for s in STEPS}, rows=True)
        extra = VGroup(*[Arrow([CX[a] + 0.3, RAIL_Y, 0], [CX[b] - 0.3, RAIL_Y, 0], color=INK, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.3) for a, b in [(3, 4), (5, 6)]])
        brs = VGroup(*[VGroup(Line([CX[a] - 0.3, -2.25, 0], [CX[b] + 0.3, -2.25, 0], color=INK, stroke_width=3),
                              Line([CX[a] - 0.3, -2.25, 0], [CX[a] - 0.3, -2.12, 0], color=INK, stroke_width=3),
                              Line([CX[b] + 0.3, -2.25, 0], [CX[b] + 0.3, -2.12, 0], color=INK, stroke_width=3)) for a, b in [(3, 4), (5, 6)]])
        lab = VGroup(_t("waved through", 32).move_to([1.2, -2.62, 0]), _t("proofread, not read", 32).move_to([4.45, -2.62, 0]))
        cap = _cap("both run AI to human", x=3.2, y=-3.1)
        self.add(extra, brs, lab, cap)
        self.play(FadeOut(brs), FadeOut(lab), FadeOut(cap), run_time=0.5)
        _until(self, "These are the five Boondoggle questions")
        brk = VGroup(Line([-6.05, 0.62, 0], [-6.05, -1.98, 0], color=INK, stroke_width=4),
                     Line([-6.05, 0.62, 0], [-5.9, 0.62, 0], color=INK, stroke_width=4),
                     Line([-6.05, -1.98, 0], [-5.9, -1.98, 0], color=INK, stroke_width=4))
        self.play(FadeOut(st.title), FadeIn(_title("The Five Boondoggle Questions")), Create(brk), run_time=0.7)
        self.play(GrowFromCenter(_dot(-6.05, 0.95)), run_time=0.3)
        _until(self, "A step goes to the AI")
        self.play(FadeIn(_band("AI step: cheap to verify · bounded · undone next step")), run_time=0.6)
        _until(self, "Every dark row pushes")
        self.play(FadeIn(_cap("a dark row pushes toward a human")), run_time=0.5)
        _finish(self)


class B19_StepSeven(Scene):
    BASE = 20.0
    def construct(self):
        st = _Stage(self, "The Five Boondoggle Questions", bars=frozenset(), cols={s: "filled" for s in STEPS}, rows=True)
        extra = VGroup(*[Arrow([CX[a] + 0.3, RAIL_Y, 0], [CX[b] - 0.3, RAIL_Y, 0], color=INK, stroke_width=5, buff=0, max_tip_length_to_length_ratio=0.3) for a, b in [(3, 4), (5, 6)]])
        brk = VGroup(Line([-6.05, 0.62, 0], [-6.05, -1.98, 0], color=INK, stroke_width=4),
                     Line([-6.05, 0.62, 0], [-5.9, 0.62, 0], color=INK, stroke_width=4),
                     Line([-6.05, -1.98, 0], [-5.9, -1.98, 0], color=INK, stroke_width=4))
        band = _band("AI step: cheap to verify · bounded · undone next step"); cap = _cap("a dark row pushes toward a human")
        self.add(extra, brk, band, cap)
        self.play(FadeOut(st.rows), FadeOut(brk), FadeOut(band), FadeOut(cap), FadeOut(st.title), FadeIn(_title("Back to the Puzzle")), run_time=0.6)
        q = VGroup(_left("three short bars,", -6.05, 0.4), _left("three human steps.", -6.05, -0.1))
        self.play(FadeIn(q), run_time=0.5)
        _until(self, "Now you can see why")
        ans = _band("short on effort · heavy on judgment", bold=True)
        self.play(FadeIn(ans), run_time=0.5)
        _until(self, "Two honest limits")
        world = VGroup(*st.boxes.values(), *st.names.values(), *st.cols.values(), extra)
        self.play(FadeOut(q), FadeOut(st.paper), run_time=0.4)
        _until(self, "The score has a gap")
        self.play(world.animate.shift(LEFT * 1.55), run_time=1.0)
        b7 = DashedVMobject(Rectangle(width=BW, height=BH, color=INK, stroke_width=3), num_dashes=16).move_to([CX[6], BOX_Y, 0])
        n7 = _t("7", 36, INK, bold=True).move_to([CX[6], BOX_Y, 0])
        self.play(Create(b7), FadeIn(n7), FadeIn(_t("?", 32).move_to([CX[6], NAME_Y, 0])), run_time=0.6)
        _until(self, "No step integrates")
        self.play(FadeIn(_column(6, filled=False)), GrowFromCenter(_dot(CX[6] + 0.62, BOX_Y)), run_time=0.6)
        _until(self, "a step seven is required")
        self.play(FadeOut(ans), run_time=0.3)
        self.play(FadeIn(_band("missing: executive integration", x=1.0, bold=True)), run_time=0.5)
        _until(self, "And the score is the author's own")
        self.play(FadeIn(_cap("a heuristic — not validated")), run_time=0.5)
        _finish(self)
