"""
Manim scenes for tldr-five-boxes-one-deployment (tldr skill — LEARN section 1, B10–B19).

One persistent object: the chapter's five-row accountability CHECKLIST, run against the
chapter's Application A2 paragraph (four sentences, a constructed exercise case).

  left   five grey-outlined boxes + requirement names; under each name, the EVIDENCE slot
         (the A2 fragment filed there, or "not mentioned")
  right  the chapter's verification TEST for each row (dim) and, under it, the FAILURE MODE
         the chapter names when the test fails (ink)
  bottom the 18-month bar ("running for 18 months") — a clock with no box

State factory: `_Board(scene, title, **state)` rebuilds the board at the previous beat's end
state, so the last frame of Bk is the first frame of Bk+1 (transform, don't cut).

INK text on the cream stage; terracotta is ONE accent per scene — a dot or an X beside a
word, never text, never a line, never a ring (GATE T). Box outlines in DIM (a dark outline
around dark text reads as nested labels). Explicit coords inside ±6.2 × ±3.3. Type floor 32
(titles 40). Captions ≤ 34 chars. Text changes cross-fade (FadeTransform); the paced play
never lets an animation straddle the clip's 50% frame (GATE T samples it).
"""
import json as _json, os as _os
from manim import *

CREAM = "#FAF9F5"; STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# ═══════════ the chapter's material (FACTCHECK rows 2, 5–11) ═══════════
A2_LINES = ["The system flags posts for review.",
            "Moderators can appeal a flag",
            "by contacting the support team.",
            "The company's trust and safety team",
            "reviews reported issues periodically.",
            "The system has been running for 18 months."]
SENT_OF_LINE = [0, 1, 1, 2, 2, 3]
REQS = ["Specifications", "Audit trail", "Recourse", "Independent review", "Sanctions"]
FRAG = {0: "“flags posts for review”", 2: "“appeal … support team”", 3: "“reviews … periodically”"}   # row → A2 fragment
FROM_SENT = {0: 0, 2: 1, 3: 2}                                                              # row → A2 sentence
TESTS = ["could a reviewer predict success?", "incident rebuilt in under an hour?",
         "can an outsider find it and use it?", "named, outside the team, can halt?",
         "can a named role lose something?"]
FAILS = ["“the model said so” is the audit", "review reconstructs nothing",
         "routes to support, no resolution", "the company grades its own work",
         "no one bears the cost"]
PASSES = [False, False, False, False, False]
assert len(REQS) == 5 and len(TESTS) == 5 and len(FAILS) == 5
assert sorted(FRAG) == [0, 2, 3] and sum(PASSES) == 0            # three filed by words; none pass
assert all(len(s) <= 36 for s in TESTS + FAILS) and all(len(s) <= 26 for s in FRAG.values())

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
    _NARR = {b["beat_id"]: b["narration_text"] for b in _SHEET["beats"]}
except Exception:
    _TARGET, _NARR = {}, {}

def _bid(self): return type(self).__name__.split("_")[0]
def _elapsed(self):
    rt = getattr(getattr(self, "renderer", None), "time", None)
    return float(rt) if isinstance(rt, (int, float)) else 0.0

if not getattr(Scene.play, "_paced", False):
    _orig_play = Scene.play
    def _paced_play(self, *anims, **kw):
        # never let an animation straddle the clip's midpoint (GATE T samples the 50% frame)
        rt = kw.get("run_time")
        target = _TARGET.get(_bid(self), 0)
        if rt and target:
            mid, t0 = target / 2.0, _elapsed(self)
            if t0 < mid + 0.1 and t0 + rt > mid - 0.1:
                if mid - 0.1 - t0 >= 0.3:
                    kw["run_time"] = mid - 0.1 - t0          # finish before the midpoint
                else:
                    self.wait(mid + 0.12 - t0)               # or start just after it
        return _orig_play(self, *anims, **kw)
    _paced_play._paced = True
    Scene.play = _paced_play

def _until(self, phrase, lead=0.25):
    """Wait until `phrase` is spoken (its character share of the narration × the measured duration)."""
    n, target = _NARR.get(_bid(self), ""), _TARGET.get(_bid(self), 0)
    if not n or not target or phrase not in n:
        return
    gap = target * n.index(phrase) / len(n) - lead - _elapsed(self)
    if gap > 0.05:
        self.wait(gap)

def _finish(self):
    target = _TARGET.get(_bid(self), 0)
    self.wait(max(0.1, target - _elapsed(self)) if target else 2.0)

# ═══════════ text + mark helpers ═══════════
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _title(txt): return _t(txt, 40).move_to([0, 3.05, 0])
def _cap(txt, x=3.2): return _t(txt, 32, DIM).move_to([x, -3.1, 0])
def _constructed(): return _t("constructed exercise case", 32, DIM).move_to([-3.6, -3.1, 0])
def _dot(x, y, r=0.12): return Dot([x, y, 0], color=TERRA, radius=r)
def _x(x, y, s=0.2, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))

# ═══════════ board geometry ═══════════
NY = [2.35, 1.37, 0.39, -0.59, -1.57]        # row name lines
SUB = 0.47                              # evidence / failure line sits this far below
BOX_X, NAME_X, RX = -5.85, -5.45, -0.2
DOT_L, DOT_R = -1.6, -0.55              # terracotta dot columns (beside a name / beside a test)
BAR_Y, BAR_X0, BAR_W, BAR_H = -2.6, -5.85, 2.8, 0.2
HOOK_Y = [2.2, 1.6, 1.0, 0.4, -0.2, -0.8]
HOOK_X = -5.6

def _box(i): return Square(side_length=0.36, color=DIM, stroke_width=3).move_to([BOX_X, NY[i], 0])
def _name(i): return _t(REQS[i], 34).move_to([NAME_X, NY[i], 0], aligned_edge=LEFT)
def _tick(i, color=INK):
    x, y = BOX_X, NY[i]
    return VGroup(Line([x - 0.13, y + 0.0, 0], [x - 0.04, y - 0.11, 0], color=color, stroke_width=6),
                  Line([x - 0.04, y - 0.11, 0], [x + 0.15, y + 0.14, 0], color=color, stroke_width=6))
def _frag_right(i): return _t(FRAG[i], 32).move_to([RX, NY[{0: 0, 2: 1, 3: 2}[i]], 0], aligned_edge=LEFT)
def _evid(i): return _t(FRAG[i], 32).move_to([NAME_X, NY[i] - SUB, 0], aligned_edge=LEFT)
def _nm(i): return _t("not mentioned", 32, DIM).move_to([NAME_X, NY[i] - SUB, 0], aligned_edge=LEFT)
def _test(i): return _t(TESTS[i], 32, DIM).move_to([RX, NY[i], 0], aligned_edge=LEFT)
def _fail(i): return _t(FAILS[i], 32, INK).move_to([RX, NY[i] - SUB, 0], aligned_edge=LEFT)
def _bar():
    g = VGroup(); w = BAR_W / 18
    for k in range(18):
        g.add(Rectangle(width=w, height=BAR_H, fill_color=INK, fill_opacity=1, stroke_color=STAGE, stroke_width=2)
              .move_to([BAR_X0 + w * (k + 0.5), BAR_Y, 0]))
    return g
def _bar_label(txt="running for 18 months"): return _t(txt, 32).move_to([BAR_X0 + BAR_W + 0.2, BAR_Y, 0], aligned_edge=LEFT)
def _rule_line(): return Line([HOOK_X, -1.45, 0], [2.8, -1.45, 0], color=DIM, stroke_width=3)
def _hook_line(k): return _t(A2_LINES[k], 36).move_to([HOOK_X, HOOK_Y[k], 0], aligned_edge=LEFT)
def _tally(n): return _t(f"ticked: {n} of 5", 36, INK, bold=True).move_to([4.2, BAR_Y, 0])
def _divider(): return Line([-0.85, 2.6, 0], [-0.85, -2.3, 0], color=DIM, stroke_width=3)
SYRI_HEAD = ("SyRI · Dutch welfare scoring", "struck down · The Hague · 2020")
def _syri_head(): return VGroup(_t(SYRI_HEAD[0], 32, INK, bold=True).move_to([RX, NY[0], 0], aligned_edge=LEFT),
                                _t(SYRI_HEAD[1], 32, DIM).move_to([RX, NY[0] - SUB, 0], aligned_edge=LEFT))
def _nosent(i): return _t("no sentence to file here", 32, DIM).move_to([RX, NY[i], 0], aligned_edge=LEFT)
def _paper(i): return _t("on paper, not in function", 32).move_to([RX, NY[i], 0], aligned_edge=LEFT)
def _court(i, y=None): return _t("supplied by the court, late", 32).move_to([RX, NY[i] - SUB if y is None else y, 0], aligned_edge=LEFT)
RULE = [("present when the test passes,", 34, True, 2.1), ("not when the word appears", 34, True, 1.5),
        ("five tests: an audit instrument", 32, False, 0.4), ("can't tick all five:", 32, False, -0.7),
        ("a slogan, not a practice", 36, True, -1.3)]
def _rule(k): s, z, b, y = RULE[k]; return _t(s, z, INK, b).move_to([RX, y, 0], aligned_edge=LEFT)


class _Board:
    """The checklist at a given state.
    rows: rows drawn (0–5) · right: A2 rows whose fragment still waits in the right column ·
    evid: rows whose fragment sits in its evidence slot · nm: rows reading 'not mentioned' ·
    ticks: rows with a tick · tests: rows with their test shown · fails: rows with the failure mode ·
    bar: the 18-month bar (+ label text) · cons: the 'constructed' caption · tally: n or None ·
    divider: the column rule."""
    def __init__(self, scene, title, rows=5, right=(), evid=(), nm=(), ticks=(), tests=(), fails=(),
                 bar=True, label="running for 18 months", cons=True, tally=None, divider=False):
        self.t = _title(title); scene.add(self.t)
        self.boxes = VGroup(*[_box(i) for i in range(rows)]); self.names = VGroup(*[_name(i) for i in range(rows)])
        scene.add(self.boxes, self.names)
        self.right = {i: _frag_right(i) for i in right}
        self.evid = {i: _evid(i) for i in evid}
        self.nm = {i: _nm(i) for i in nm}
        self.ticks = {i: _tick(i) for i in ticks}
        self.tests = {i: _test(i) for i in tests}
        self.fails = {i: _fail(i) for i in fails}
        for d in (self.right, self.evid, self.nm, self.ticks, self.tests, self.fails):
            for m in d.values(): scene.add(m)
        self.bar = self.label = None
        if bar:
            self.bar = _bar(); self.label = _bar_label(label); scene.add(self.bar, self.label)
        self.cons = _constructed() if cons else None
        if cons: scene.add(self.cons)
        self.tally = _tally(tally) if tally is not None else None
        if self.tally: scene.add(self.tally)
        self.div = _divider() if divider else None
        if divider: scene.add(self.div)


# ═══════════ B10 — HOOK: the paragraph and the clock ═══════════
class B10_TheParagraph(Scene):
    def construct(self):
        self.add(_title("One Deployment, Four Sentences"))
        lines = [_hook_line(k) for k in range(6)]
        _until(self, "Here is a whole")
        self.play(FadeIn(_constructed()), run_time=0.5)
        for phrase, ks in (("The system flags", [0]), ("Moderators can", [1, 2]),
                           ("The company's", [3, 4]), ("The system has been", [5])):
            _until(self, phrase)
            self.play(*[FadeIn(lines[k], shift=RIGHT * 0.1) for k in ks], run_time=0.6)
        _until(self, "eighteen months")
        self.play(GrowFromEdge(_bar(), LEFT), FadeIn(_bar_label()), GrowFromCenter(_dot(-5.98, HOOK_Y[5])), run_time=0.9)
        _until(self, "It sounds careful")
        self.play(Create(_rule_line()), run_time=0.6)
        _until(self, "So, when")
        self.play(FadeIn(_t("accountable?", 40, INK, bold=True).move_to([4.6, 1.3, 0])), run_time=0.6)
        _finish(self)


# ═══════════ B11 — INSTANCE 1: five boxes; file sentence one ═══════════
class B11_FiveBoxes(Scene):
    def construct(self):
        t = _title("One Deployment, Four Sentences"); self.add(t)
        lines = [_hook_line(k) for k in range(6)]
        bar, lab, cons = _bar(), _bar_label(), _constructed()
        dot = _dot(-5.98, HOOK_Y[5]); q = _t("accountable?", 40, INK, bold=True).move_to([4.6, 1.3, 0])
        rl = _rule_line()
        self.add(*lines, bar, lab, cons, dot, q, rl)
        self.wait(0.3)
        frags = {i: _frag_right(i) for i in (0, 2, 3)}
        self.play(FadeOut(dot), FadeOut(q), FadeOut(rl), Transform(t, _title("Five Boxes")),
                  FadeTransform(lines[0], frags[0]), FadeTransform(VGroup(lines[1], lines[2]), frags[2]),
                  FadeTransform(VGroup(lines[3], lines[4]), frags[3]), FadeOut(lines[5]), run_time=1.2)
        for i, nm in enumerate(REQS):
            _until(self, nm + ".")
            self.play(Create(_box(i)), FadeIn(_name(i)), run_time=0.5)
        _until(self, "First sentence")
        self.play(frags[0].animate.move_to([NAME_X, NY[0] - SUB, 0], aligned_edge=LEFT), run_time=1.0)
        _until(self, "pencil in a tick")
        self.play(Create(_tick(0)), GrowFromCenter(_dot(DOT_L, NY[0])), run_time=0.6)
        _finish(self)


# ═══════════ B12 — INSTANCE 2: file the rest ═══════════
class B12_FileTheRest(Scene):
    def construct(self):
        st = _Board(self, "Five Boxes", right=(2, 3), evid=(0,), ticks=(0,))
        d = _dot(DOT_L, NY[0]); self.add(d)
        self.play(Transform(st.t, _title("File The Rest")), FadeOut(d), run_time=0.6)
        _until(self, "that sounds like recourse")
        self.play(st.right[2].animate.move_to([NAME_X, NY[2] - SUB, 0], aligned_edge=LEFT), run_time=1.0)
        _until(self, "so in it goes")
        self.play(Create(_tick(2)), run_time=0.5)
        _until(self, "that sounds like independent")
        self.play(st.right[3].animate.move_to([NAME_X, NY[3] - SUB, 0], aligned_edge=LEFT), run_time=1.0)
        _until(self, "Tick.")
        self.play(Create(_tick(3)), GrowFromCenter(_dot(DOT_L, NY[3])), run_time=0.5)
        _until(self, "Audit trail and sanctions")
        self.play(FadeIn(_nm(1)), FadeIn(_nm(4)), FadeIn(_nosent(1)), FadeIn(_nosent(4)), run_time=0.6)
        _finish(self)


# ═══════════ B13 — NAIVE: count the words, lean on the clock ═══════════
class B13_TheEasyReading(Scene):
    def construct(self):
        st = _Board(self, "File The Rest", evid=(0, 2, 3), nm=(1, 4), ticks=(0, 2, 3))
        d = _dot(DOT_L, NY[3]); ns = VGroup(_nosent(1), _nosent(4)); self.add(d, ns)
        self.play(Transform(st.t, _title("The Easy Reading")), FadeOut(d), FadeOut(ns), run_time=0.6)
        tally = [("three boxes hold words", 36, False, 1.6), ("two are blank", 36, False, 1.0),
                 ("18 months, still running", 36, False, 0.4), ("mostly accountable?", 40, True, -0.4)]
        for (s, z, b, y), phrase in zip(tally, ("Three boxes", "Two are blank", "but it's been running", "mostly accountable")):
            _until(self, phrase)
            self.play(FadeIn(_t(s, z, INK, b).move_to([RX, y, 0], aligned_edge=LEFT), shift=RIGHT * 0.1), run_time=0.5)
        _until(self, "It has no box")
        self.play(Create(_x(1.6, BAR_Y)), run_time=0.5)
        _until(self, "It's a clock")
        self.play(FadeIn(_cap("a clock, not a check")), run_time=0.5)
        _finish(self)


# ═══════════ B14 — SHIFT: every box has a test ═══════════
class B14_EachBoxHasATest(Scene):
    def construct(self):
        st = _Board(self, "The Easy Reading", evid=(0, 2, 3), nm=(1, 4), ticks=(0, 2, 3))
        tl = VGroup(_t("three boxes hold words", 36).move_to([RX, 1.6, 0], aligned_edge=LEFT),
                    _t("two are blank", 36).move_to([RX, 1.0, 0], aligned_edge=LEFT),
                    _t("18 months, still running", 36).move_to([RX, 0.4, 0], aligned_edge=LEFT),
                    _t("mostly accountable?", 40, INK, True).move_to([RX, -0.4, 0], aligned_edge=LEFT))
        xx = _x(1.6, BAR_Y); c0 = _cap("a clock, not a check")
        self.add(tl, xx, c0)
        self.play(Transform(st.t, _title("Every Box Has A Test")), FadeOut(tl), FadeOut(xx), FadeOut(c0), run_time=0.7)
        for i, phrase in enumerate(("Specifications: could", "Audit trail: could", "Recourse: could", "Review: someone", "Sanctions: can")):
            _until(self, phrase)
            self.play(FadeIn(_test(i), shift=RIGHT * 0.1), run_time=0.5)
        _until(self, "Run the first")
        self.play(GrowFromCenter(_dot(DOT_R, NY[0])), run_time=0.4)
        _until(self, "The tick comes out")
        self.play(Uncreate(st.ticks[0]), FadeIn(_fail(0)), run_time=0.7)
        _finish(self)


# ═══════════ B15 — predict ═══════════
class B15_Commit(Scene):
    def construct(self):
        st = _Board(self, "Every Box Has A Test", evid=(0, 2, 3), nm=(1, 4), ticks=(2, 3), tests=range(5), fails=(0,))
        d = _dot(DOT_R, NY[0]); self.add(d)
        self.play(Transform(st.t, _title("Commit")), FadeOut(d), run_time=0.6)
        _until(self, "recourse and review")
        self.play(Create(Line([-0.8, NY[2] + 0.28, 0], [-0.8, NY[3] - SUB - 0.2, 0], color=INK, stroke_width=4)),
                  GrowFromCenter(_dot(DOT_R, NY[2] - SUB)), run_time=0.7)
        _until(self, "commit")
        self.play(FadeIn(_cap("how many ticks survive? commit")), run_time=0.5)
        _finish(self)


# ═══════════ B16 — TRANSFORM: run the tests ═══════════
class B16_RunTheTests(Scene):
    def construct(self):
        st = _Board(self, "Commit", evid=(0, 2, 3), nm=(1, 4), ticks=(2, 3), tests=range(5), fails=(0,))
        br = Line([-0.8, NY[2] + 0.28, 0], [-0.8, NY[3] - SUB - 0.2, 0], color=INK, stroke_width=4)
        d = _dot(DOT_R, NY[2] - SUB); c0 = _cap("how many ticks survive? commit")
        self.add(br, d, c0)
        self.play(Transform(st.t, _title("Run The Tests")), FadeOut(br), FadeOut(c0), run_time=0.6)
        _until(self, "The tick comes out")
        self.play(Uncreate(st.ticks[2]), FadeIn(_fail(2)), run_time=0.7)
        _until(self, "Review.")
        self.play(d.animate.move_to([DOT_R, NY[3] - SUB, 0]), run_time=0.5)
        _until(self, "Out.")
        self.play(Uncreate(st.ticks[3]), FadeIn(_fail(3)), run_time=0.7)
        _until(self, "The blank boxes")
        self.play(FadeIn(_fail(1)), FadeIn(_fail(4)), FadeOut(d), run_time=0.6)
        _until(self, "Zero of five")
        tal = _tally(0)
        self.play(FadeIn(tal), Create(Line([2.65, BAR_Y - 0.32, 0], [5.75, BAR_Y - 0.32, 0], color=INK, stroke_width=3)),
                  GrowFromCenter(_dot(2.3, BAR_Y)), run_time=0.6)
        _finish(self)


# ═══════════ B17 — INSTANCE (post-shift): SyRI ═══════════
class B17_SyRI(Scene):
    def construct(self):
        st = _Board(self, "Run The Tests", evid=(0, 2, 3), nm=(1, 4), tests=range(5), fails=range(5), tally=0)
        ul = Line([2.65, BAR_Y - 0.32, 0], [5.75, BAR_Y - 0.32, 0], color=INK, stroke_width=3); d0 = _dot(2.3, BAR_Y)
        self.add(ul, d0)
        gone = [*st.evid.values(), *st.nm.values(), *st.tests.values(), *st.fails.values(), st.tally, ul, d0, st.bar, st.label, st.cons]
        self.play(Transform(st.t, _title("A Real One: SyRI")), *[FadeOut(m) for m in gone], run_time=0.9)
        self.play(Create(_divider()), run_time=0.6)
        _until(self, "SyRI, a Dutch")
        self.play(FadeIn(_syri_head()[0]), run_time=0.6)
        _until(self, "on paper and not")
        self.play(FadeIn(_paper(2)), FadeIn(_paper(3)), run_time=0.6)
        _until(self, "a court in The Hague")
        dd = _dot(DOT_R, NY[0] - SUB)
        self.play(FadeIn(_syri_head()[1]), GrowFromCenter(dd), run_time=0.6)
        _until(self, "The court supplied")
        self.play(dd.animate.move_to([DOT_R, NY[3] - SUB, 0]), FadeIn(_court(3)), run_time=0.8)
        self.play(dd.animate.move_to([DOT_R, NY[4], 0]), FadeIn(_court(4, NY[4])), run_time=0.8)
        _until(self, "late, from outside")
        self.play(FadeIn(_cap("tested late, from outside")), run_time=0.5)
        _finish(self)


# ═══════════ B18 — ABSTRACTION: name it ═══════════
class B18_NameIt(Scene):
    def construct(self):
        st = _Board(self, "A Real One: SyRI", bar=False, cons=False, divider=True)
        head = _syri_head(); p2, p3 = _paper(2), _paper(3); c3, c4 = _court(3), _court(4, NY[4])
        dd = _dot(DOT_R, NY[4]); c0 = _cap("tested late, from outside")
        self.add(head, p2, p3, c3, c4, dd, c0)
        self.play(Transform(st.t, _title("Name It")), *[FadeOut(m) for m in (head, p2, p3, c3, c4, dd, c0)], run_time=0.8)
        _until(self, "A requirement is present")
        self.play(FadeIn(_rule(0)), run_time=0.6)
        _until(self, "not when its word")
        self.play(FadeIn(_rule(1)), Create(Line([RX, 1.18, 0], [4.6, 1.18, 0], color=INK, stroke_width=3)), run_time=0.7)
        _until(self, "Five boxes, five tests")
        self.play(FadeIn(_rule(2)), run_time=0.6)
        _until(self, "a regime that can't")
        self.play(FadeIn(_rule(3)), run_time=0.5)
        _until(self, "a slogan, not")
        self.play(FadeIn(_rule(4)), GrowFromCenter(_dot(DOT_R, RULE[4][3])), run_time=0.6)
        _finish(self)


# ═══════════ B19 — PAYOFF: back to the paragraph ═══════════
class B19_BackToTheParagraph(Scene):
    def construct(self):
        st = _Board(self, "Name It", bar=False, cons=False, divider=True)
        rl = VGroup(*[_rule(k) for k in range(5)]); ul = Line([RX, 1.18, 0], [4.6, 1.18, 0], color=INK, stroke_width=3)
        dd = _dot(DOT_R, RULE[4][3])
        self.add(rl, ul, dd)
        self.play(Transform(st.t, _title("Back To The Four Sentences")), FadeOut(rl), FadeOut(ul), FadeOut(dd), run_time=0.8)
        _until(self, "Back to the four")
        self.play(*[FadeIn(_evid(i), shift=RIGHT * 0.1) for i in (0, 2, 3)], FadeIn(_nm(1)), FadeIn(_nm(4)),
                  FadeIn(_constructed()), run_time=0.8)
        _until(self, "not one passes")
        self.play(*[FadeIn(_fail(i)) for i in range(5)], run_time=0.8)
        _until(self, "And eighteen months")
        self.play(GrowFromEdge(_bar(), LEFT), FadeIn(_bar_label("18 months nobody could rebuild")), run_time=0.9)
        _until(self, "nobody could reconstruct")
        self.play(GrowFromCenter(_dot(3.35, BAR_Y)), run_time=0.4)
        _until(self, "That's not taught")
        self.play(FadeIn(_cap("not taught: who holds each box")), run_time=0.5)
        _finish(self)
