"""
Manim scenes for tldr-the-report-is-not-the-world (tldr skill — LEARN section 1, B10–B19).

Case #1 of Agents of Chaos as chapter 8 of INFO 7375 retells it, on ONE stage:
the WORLD on the right (mail server with the email · local client with its copy ·
the owner's mail, which depends on the client) and, from B14 on, ASH'S LEDGER on
the left (a window through the client — all the agent's tools can see). The
report is written from the left; the task lives on the right.

`_Stage` is the state factory: every scene rebuilds the same objects at the
previous beat's end state (before / after the reset), and `reset()` / `rewind()`
are the transforms between them (transform, don't cut).

INK text on the cream stage; terracotta is ONE accent per scene — a dot or an
X-mark beside a word or shape, never text, never a ring, never a bar. Explicit
coordinates only; every scene adds a NEW geometric object before its final play
(Gate A). All text inside ±6.2 × ±3.3; captions ≤ 34 chars centred at x ≈ 3.2;
type floor 32 (titles 40); no slant on multi-word text.
"""
import json as _json, os as _os
import numpy as np
from manim import *

STAGE = "#F2F0E9"; INK = "#3D3929"; TERRA = "#D97757"; DIM = "#8B8F96"; GHOST = "#D9D4C7"; SOFT = "#6E6A57"
SERIF = "EB Garamond"
config.background_color = STAGE

_HERE = _os.path.dirname(_os.path.abspath(__file__))

# The chapter's own strings and counts (FACTCHECK rows 2, 3, 10) — asserted, not retyped.
REPORT = "Email account RESET completed."
CLAIM = "and: the secret is deleted"
APPROVALS = 2
assert REPORT.split()[2] == "RESET" and APPROVALS == 2

# ═══════════ pacing ═══════════
try:
    _SHEET = _json.load(open(_os.path.join(_HERE, "beat_sheet.json")))
    _TARGET = {b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 0) for b in _SHEET["beats"]}
except Exception:
    _TARGET = {}
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

def _finish(self):
    target = _TARGET.get(type(self).__name__.split("_")[0], 0)
    rt = getattr(getattr(self, "renderer", None), "time", None)
    elapsed = float(rt) if isinstance(rt, (int, float)) else 0.0
    self.wait(max(1.0, target - elapsed) if target else 2.0)

# ═══════════ text helpers ═══════════
def _title(txt, size=40): return Text(txt, font=SERIF, color=INK, font_size=size).move_to([0, 3.0, 0])
def _t(s, size=32, color=INK, bold=False): return Text(s, font=SERIF, color=color, font_size=size, weight="BOLD" if bold else "NORMAL")
def _tl(s, x, y, size=32, color=INK, bold=False): return _t(s, size, color, bold).move_to([x, y, 0], aligned_edge=LEFT)
def _cap(txt, x=3.2, size=32): return Text(txt, font=SERIF, color=DIM, font_size=size).move_to([x, -3.05, 0])
def _x(x, y, s=0.2, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=TERRA, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=TERRA, stroke_width=w))
def _spark(x, y, r=0.14): return Dot([x, y, 0], color=TERRA, radius=r)

# ═══════════ stage geometry ═══════════
SX, SY, SW, SH = 3.3, 0.95, 2.6, 1.1           # mail server  (x 2.0 … 4.6, y 0.4 … 1.5)
CX, CY, CW, CH = 1.9, -1.05, 2.2, 1.0          # local client (x 0.8 … 3.0, y −1.55 … −0.55)
OX, OY, OW, OH = 4.8, -1.05, 1.9, 1.0          # owner's mail (x 3.85 … 5.75)
AX, AY = -1.0, -1.05                           # Ash
NX, NY = -4.6, -1.05                           # Natalie
WX, WY, WW, WH = -3.3, 0.55, 3.6, 1.5          # Ash's window (x −5.1 … −1.5, y −0.2 … 1.3)
RX, RY1, RY2 = -3.25, -2.2, -2.75              # report slot (two lines, left-aligned at LX)
ROW_Y = -2.75                                  # the world's free row (right side)
LX = -5.8                                      # left-column text margin

def _env(x, y, w=1.0, h=0.62, color=INK):
    box = Rectangle(width=w, height=h, stroke_color=color, stroke_width=3, fill_color=STAGE, fill_opacity=1).move_to([x, y, 0])
    flap = VMobject(stroke_color=color, stroke_width=3).set_points_as_corners(
        [np.array([x - w / 2, y + h / 2, 0]), np.array([x, y - 0.02, 0]), np.array([x + w / 2, y + h / 2, 0])])
    return VGroup(box, flap)

# containers are scaffolding (dim): GATE T reads an INK frame around ink contents as two overlapping text runs
def _box(x, y, w, h, color=DIM): return Rectangle(width=w, height=h, stroke_color=color, stroke_width=3, fill_opacity=0).move_to([x, y, 0])

def _owner_arrows(color=INK):
    kw = dict(color=color, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.22, tip_length=0.16)
    return VGroup(Arrow([OX - 0.5, OY + 0.18, 0], [OX + 0.5, OY + 0.18, 0], **kw),
                  Arrow([OX + 0.5, OY - 0.18, 0], [OX - 0.5, OY - 0.18, 0], **kw))

def _dep_whole(): return Line([CX + CW / 2, CY, 0], [OX - OW / 2, OY, 0], color=INK, stroke_width=3)
def _dep_broken():
    return VGroup(Line([CX + CW / 2, CY, 0], [CX + CW / 2 + 0.28, CY, 0], color=DIM, stroke_width=3),
                  Line([OX - OW / 2 - 0.28, OY, 0], [OX - OW / 2, OY, 0], color=DIM, stroke_width=3))

def _pulse(): return Arrow([AX + 0.1, AY, 0], [CX - CW / 2 - 0.02, CY, 0], color=INK, stroke_width=7, buff=0, max_tip_length_to_length_ratio=0.3)
def _report(): return VGroup(_tl(REPORT, LX, RY1), _tl(CLAIM, LX, RY2))
def _empty_note(): return _t("no email", 32, SOFT).move_to([WX, WY, 0])


class _Stage:
    """The one stage. after=False: before the reset; after=True: after it.
    parts: 'server' · 'world' (client, owner, links) · 'ash' · 'natalie' · 'report' · 'ledgers'."""
    def __init__(self, scene, title, after=False, parts=("server", "world", "ash")):
        self.scene, self.after, self.parts = scene, after, set(parts)
        self.t = _title(title); scene.add(self.t)
        # world: server
        self.server = _box(SX, SY, SW, SH); self.s_lab = _t("mail server").move_to([SX, 1.85, 0]); self.env_s = _env(SX, SY)
        # world: client + owner
        self.client = _box(CX, CY, CW, CH); self.c_lab = _t("local client").move_to([CX, -1.95, 0])
        self.env_c = _env(CX, CY, 0.8, 0.5)
        self.sync = Line([2.25, SY - SH / 2, 0], [1.95, CY + CH / 2, 0], color=INK, stroke_width=3)
        self.owner = _box(OX, OY, OW, OH, GHOST if after else DIM); self.o_lab = _t("owner's mail").move_to([OX, -1.95, 0])
        self.o_arr = _owner_arrows(DIM if after else INK)
        self.dep = _dep_broken() if after else _dep_whole()
        # Ash + Natalie
        self.ash = Dot([AX, AY, 0], color=INK, radius=0.13); self.a_lab = _t("Ash").move_to([AX, -1.5, 0])
        self.wire = Line([AX + 0.13, AY, 0], [CX - CW / 2, CY, 0], color=INK, stroke_width=3)
        self.nat = Dot([NX, NY, 0], color=INK, radius=0.13); self.n_lab = _t("Natalie").move_to([NX, -1.5, 0])
        self.req = Arrow([NX + 0.15, NY, 0], [AX - 0.18, AY, 0], color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.08)
        self.r_lab = _t("delete the email").move_to([-2.8, -0.62, 0])
        self.report = _report()
        # ledgers
        self.divider = Line([0.4, 2.6, 0], [0.4, -1.75, 0], color=GHOST, stroke_width=3)
        self.h_left = _t("Ash's ledger", 36).move_to([-3.3, 2.4, 0]); self.h_right = _t("the world", 36).move_to([3.3, 2.4, 0])
        self.sub = _t("what its tools can see", 32, DIM).move_to([-3.3, 1.85, 0])
        self.window = _box(WX, WY, WW, WH); self.env_w = _env(WX, WY, 0.8, 0.5); self.empty = _empty_note()
        self.link = DashedLine([AX - 0.1, AY + 0.14, 0], [-1.55, -0.25, 0], color=DIM, stroke_width=3)
        self.rep_arrow = Arrow([WX, WY - WH / 2 - 0.1, 0], [WX, RY1 + 0.3, 0], color=INK, stroke_width=3, buff=0, max_tip_length_to_length_ratio=0.15)
        p = self.parts
        if "server" in p: scene.add(self.server, self.s_lab, self.env_s)
        if "world" in p:
            scene.add(self.client, self.c_lab, self.sync, self.owner, self.o_lab, self.o_arr, self.dep)
            if not after: scene.add(self.env_c)
        if "ash" in p: scene.add(self.ash, self.a_lab, self.wire)
        if "natalie" in p: scene.add(self.nat, self.n_lab, self.req, self.r_lab)
        if "report" in p: scene.add(self.report)
        if "ledgers" in p:
            scene.add(self.divider, self.h_left, self.h_right, self.sub, self.window, self.link, self.rep_arrow)
            scene.add(self.empty if after else self.env_w)

    def reset(self):
        """before → after: the client's copy goes, the owner's mail goes dark, the server does not move."""
        a = [FadeOut(self.env_c, scale=0.6), ReplacementTransform(self.dep, _dep_broken()),
             self.owner.animate.set_stroke(GHOST), self.o_arr.animate.set_color(DIM)]
        if "ledgers" in self.parts: a += [FadeOut(self.env_w, scale=0.6), FadeIn(self.empty)]
        return a

    def rewind(self):
        """after → before (B14 only)."""
        whole = _dep_whole()
        a = [FadeIn(self.env_c), ReplacementTransform(self.dep, whole), self.owner.animate.set_stroke(DIM), self.o_arr.animate.set_color(INK)]
        self.dep = whole
        return a


class B10_TheReport(Scene):
    BASE = 11.0
    def construct(self):
        self.add(_title("Done, Says The Report"))
        rep = _report()
        self.play(FadeIn(rep[0], shift=UP * 0.1), run_time=0.9)
        self.play(FadeIn(rep[1], shift=UP * 0.1), run_time=0.7)
        self.wait(0.8)
        server = _box(SX, SY, SW, SH)
        self.play(Create(server), FadeIn(_t("mail server").move_to([SX, 1.85, 0])), run_time=0.9)
        self.play(FadeIn(_env(SX, SY)), run_time=0.6)
        self.play(GrowFromCenter(_spark(4.2, SY)), run_time=0.4)
        self.play(FadeIn(_t("what was it describing?", 40).move_to([-3.25, 0.9, 0])), run_time=0.7)
        self.play(FadeIn(_cap("report: done · server: still there")), run_time=0.5)
        _finish(self)


class B11_ThePieces(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "The Pieces", parts=("server",))
        rep = _report(); q = _t("what was it describing?", 40).move_to([-3.25, 0.9, 0])
        self.add(rep, q)
        self.play(FadeOut(rep), FadeOut(q), run_time=0.6)
        self.play(Create(st.client), Create(st.sync), FadeIn(st.c_lab), run_time=0.9)
        self.play(FadeIn(st.env_c), run_time=0.5)
        self.play(Create(st.dep), Create(st.owner), FadeIn(st.o_lab), FadeIn(st.o_arr), run_time=0.9)
        self.play(GrowFromCenter(st.ash), FadeIn(st.a_lab), Create(st.wire), run_time=0.7)
        self.play(FadeIn(_tl("Chris owns Ash, the agent", LX, 1.6)), run_time=0.6)
        self.play(FadeIn(_tl("Natalie is not an owner", LX, 1.05)), GrowFromCenter(st.nat), FadeIn(st.n_lab), run_time=0.6)
        self.play(GrowArrow(st.req), FadeIn(st.r_lab), run_time=0.8)
        self.play(FadeIn(_tl("no tool deletes email", LX, 0.4)), run_time=0.5)
        self.play(Create(_x(-1.8, 0.4)), run_time=0.4)
        self.play(FadeIn(_cap("Case #1 · one exploratory study")), run_time=0.5)
        _finish(self)


class B12_TheReset(Scene):
    BASE = 15.0
    def construct(self):
        st = _Stage(self, "The Reset", parts=("server", "world", "ash", "natalie"))
        self.play(FadeIn(_tl("option: reset it all, locally", LX, 1.6)), run_time=0.7)
        steps = [("1  approved", 1.0), ("   double-checked", 0.5), ("2  approved again", 0.0)]
        for i, (s, y) in enumerate(steps):
            if i == 1:
                self.play(FadeIn(_tl(s, LX + 0.33, y)), run_time=0.6)
                continue
            tok = Dot([NX + 0.2, NY + 0.22, 0], color=INK, radius=0.09)
            self.add(tok)
            self.play(tok.animate.move_to([AX - 0.3, AY + 0.22, 0]), FadeIn(_tl(s, LX, y)), run_time=0.9)
            self.play(FadeOut(tok), run_time=0.2)
        pulse = _pulse()
        self.play(GrowArrow(pulse), run_time=0.7)
        self.play(*st.reset(), FadeOut(pulse), run_time=1.4)
        self.play(GrowFromCenter(_spark(CX, CY)), run_time=0.4)
        rep = _report()
        self.play(FadeIn(rep[0], shift=UP * 0.1), run_time=0.7)
        self.play(FadeIn(rep[1], shift=UP * 0.1), run_time=0.6)
        self.play(FadeIn(_cap("the reset landed on the client")), run_time=0.5)
        _finish(self)


class B13_TheTrail(Scene):
    BASE = 15.0
    def construct(self):
        st = _Stage(self, "Read The Trail", after=True, parts=("server", "world", "ash", "natalie", "report"))
        self.play(FadeOut(st.nat), FadeOut(st.n_lab), FadeOut(st.req), FadeOut(st.r_lab), run_time=0.6)
        trail = ["request: delete the email", "approved", "double-checked", "approved again", "reset executed"]
        for i, s in enumerate(trail):
            self.play(FadeIn(_tl(s, LX, 1.6 - 0.5 * i), shift=RIGHT * 0.1), run_time=0.55)
        self.play(Indicate(st.report[0], color=INK, scale_factor=1.04), run_time=0.6)
        bracket = VMobject(stroke_color=INK, stroke_width=3).set_points_as_corners(
            [np.array([-1.25, 1.8, 0]), np.array([-0.95, 1.8, 0]), np.array([-0.95, -0.6, 0]), np.array([-1.25, -0.6, 0])])
        self.play(Create(bracket), FadeIn(_t("true", 36).move_to([-0.35, 0.6, 0])), run_time=0.7)
        self.play(GrowFromCenter(Dot([0.2, RY1, 0], color=INK, radius=0.1)), run_time=0.4)
        self.play(Create(_x(-1.4, RY2)), run_time=0.5)
        self.play(FadeIn(_cap("no line ever read the server")), run_time=0.5)
        _finish(self)


class B14_TwoLedgers(Scene):
    BASE = 14.0
    def construct(self):
        st = _Stage(self, "Two Ledgers", after=True, parts=("server", "world", "ash", "report"))
        self.play(FadeOut(st.report), *st.rewind(), run_time=1.3)
        self.play(Create(st.divider), run_time=0.7)
        self.play(FadeIn(st.h_left), FadeIn(st.h_right), run_time=0.6)
        self.play(FadeIn(st.sub), Create(st.window), run_time=0.8)
        self.play(Create(st.link), FadeIn(st.env_w), run_time=0.7)
        self.play(GrowArrow(st.rep_arrow), run_time=0.7)
        self.play(GrowFromCenter(_spark(-1.2, WY)), run_time=0.4)
        self.play(FadeIn(_cap("simplified: one server, one client")), run_time=0.5)
        _finish(self)


class B15_Predict(Scene):
    BASE = 9.0
    def construct(self):
        st = _Stage(self, "Commit", parts=("server", "world", "ash", "ledgers"))
        poised = DashedLine([AX + 0.2, AY + 0.3, 0], [CX - CW / 2 - 0.1, CY + 0.3, 0], color=INK, stroke_width=3)
        self.play(Create(poised), run_time=0.6)
        self.play(GrowFromCenter(_spark(4.2, SY)), run_time=0.4)
        self.play(FadeIn(_t("gone from the server?", 36).move_to([3.3, ROW_Y, 0])), run_time=0.6)
        self.play(FadeIn(_tl("what will Ash see?", LX, RY1, 36)), run_time=0.6)
        _finish(self)


class B16_BothSides(Scene):
    BASE = 11.0
    def construct(self):
        st = _Stage(self, "Play Both Sides", parts=("server", "world", "ash", "ledgers"))
        pulse = _pulse()
        self.play(GrowArrow(pulse), run_time=0.6)
        self.play(*st.reset(), FadeOut(pulse), run_time=1.8)
        rep = _report()
        self.play(FadeIn(rep[0], shift=DOWN * 0.15), run_time=0.6)
        self.play(FadeIn(rep[1], shift=DOWN * 0.15), run_time=0.5)
        self.play(FadeIn(_t(CLAIM).move_to([3.1, ROW_Y, 0])), run_time=0.6)
        self.play(Create(_x(5.55, ROW_Y)), run_time=0.4)
        _finish(self)


class B17_SameSide(Scene):
    BASE = 12.0
    def construct(self):
        st = _Stage(self, "Same Side, Again", after=True, parts=("server", "world", "ash", "ledgers", "report"))
        self.play(FadeOut(st.report), run_time=0.6)
        post = Rectangle(width=5.4, height=1.1, stroke_color=DIM, stroke_width=3, fill_opacity=0).move_to([RX, -2.45, 0])
        self.play(Create(post), run_time=0.7)
        self.play(FadeIn(_t("public post:", 32, SOFT).move_to([RX, -2.18, 0])), run_time=0.5)
        self.play(FadeIn(_t("“Nuclear options work.”", 32).move_to([RX, -2.72, 0])), run_time=0.7)
        self.play(GrowFromCenter(_spark(-0.25, -2.45)), run_time=0.4)
        self.play(FadeIn(_cap("written from the same side")), run_time=0.5)
        _finish(self)


class B18_TheCatch(Scene):
    BASE = 15.0
    def construct(self):
        st = _Stage(self, "The False-Success Catch", after=True, parts=("server", "world", "ash", "ledgers"))
        post = Rectangle(width=5.4, height=1.1, stroke_color=DIM, stroke_width=3, fill_opacity=0).move_to([RX, -2.45, 0])
        pl = VGroup(_t("public post:", 32, SOFT).move_to([RX, -2.18, 0]), _t("“Nuclear options work.”", 32).move_to([RX, -2.72, 0]))
        self.add(post, pl)
        self.play(*[FadeOut(m) for m in (post, pl, st.window, st.empty, st.link, st.rep_arrow, st.sub, st.h_left, st.h_right, st.divider)], run_time=0.8)
        self.play(FadeIn(_t("consequence system", 36, INK, bold=True).move_to([-3.3, 1.9, 0])), run_time=0.6)
        self.play(FadeIn(_t("output = a state change").move_to([-3.3, 1.35, 0])), run_time=0.6)
        self.play(FadeIn(st.report), run_time=0.6)
        self.play(FadeIn(_tl("3  check the world itself", LX, -0.55)), run_time=0.5)
        chk = Arrow([-1.3, -0.45, 0], [1.9, 0.85, 0], color=INK, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.08)
        self.play(GrowArrow(chk), run_time=0.8)
        self.play(GrowFromCenter(_spark(4.2, SY)), run_time=0.4)
        self.play(FadeIn(_t("false-success catch", 38, INK, bold=True).move_to([3.3, ROW_Y, 0])), run_time=0.6)
        self.play(FadeIn(_tl("2  act", LX, 0.0)), run_time=0.4)
        self.play(FadeIn(_tl("1  gate: owner, not requester", LX, 0.55)), run_time=0.5)
        gate = Line([0.3, AY - 0.28, 0], [0.3, AY + 0.28, 0], color=INK, stroke_width=9)
        self.play(Create(gate), FadeIn(_t("gate").move_to([0.3, -1.62, 0])), run_time=0.6)
        _finish(self)


class B19_Payoff(Scene):
    BASE = 13.0
    def construct(self):
        st = _Stage(self, "You Broke My Toy", after=True, parts=("server", "world", "ash", "report"))
        chk = Arrow([-1.3, -0.45, 0], [1.9, 0.85, 0], color=INK, stroke_width=4, buff=0, max_tip_length_to_length_ratio=0.08)
        gate = Line([0.3, AY - 0.28, 0], [0.3, AY + 0.28, 0], color=INK, stroke_width=9)
        self.add(chk, gate)
        self.wait(0.6)
        self.play(Indicate(st.env_s, color=INK, scale_factor=1.08), run_time=0.8)
        self.play(Create(_x(-1.4, RY2)), run_time=0.5)
        self.play(FadeIn(_t("an alert, when the reset ends", 32).move_to([-3.3, 1.0, 0])), run_time=0.7)
        self.play(FadeIn(_t("“you broke my toy.”", 40).move_to([-3.3, 0.2, 0])), run_time=0.7)
        self.play(FadeIn(_cap("not taught here: who is at fault")), run_time=0.5)
        _finish(self)
