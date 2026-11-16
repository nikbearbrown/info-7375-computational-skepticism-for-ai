"""scenes.py — claude-liam-vox-bias-pipe Manim scenes (STD retrofit)

9 TELLS beats — all SLATE stubs pending full build:
  B02 B04 B05 B07 B08 B09 B10 B11 B12

Render (from this folder):
  python3 -m manim scenes.py B02_ThreeTeams -r 1920,1080 --fps 30 --format mp4
  (etc.)
"""
import json, pathlib
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

# ── Palette ──────────────────────────────────────────────────────────────────
CREAM   = "#F2F0E9"
INK     = "#3D3929"
ACCENT  = "#D97757"
MUTE    = "#7A7265"
TEAL    = "#2A9D8F"
CRIMSON = "#C1121F"
GOLD    = "#E9C46A"
SLATE_C = "#8D99AE"

config.background_color = CREAM

# ── Durations from beat sheet ─────────────────────────────────────────────────
DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
        for b in _bs["beats"]
    })
except Exception:
    pass

def dur(bid): return DUR.get(bid, 8.0)

def serif(txt, sz=40, clr=INK, **kw):
    return Text(txt, font="EB Garamond", font_size=sz, color=clr, **kw)

def caps(txt, sz=24, clr=MUTE, **kw):
    return Text(txt.upper(), font="Montserrat", font_size=sz, color=clr,
                weight=BOLD, **kw)


# ─────────────────────────────────────────────────────────────────────────────
# B02_ThreeTeams — Two expert teams fixed model + data; both produced same gap
# ─────────────────────────────────────────────────────────────────────────────
class B02_ThreeTeams(Scene):
    def construct(self):
        d = dur("B02")  # 10.7s
        eyebrow = caps("the intervention that wasn't enough", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        teams = VGroup(
            serif("Team A: rewrote the loss function", sz=36, clr=INK),
            serif("Team B: resampled training data", sz=36, clr=INK),
            serif("Result: same disparity gap", sz=36, clr=CRIMSON),
        ).arrange(DOWN, buff=0.4).move_to([0, 0.2, 0])

        for line in teams:
            self.play(FadeIn(line, shift=UP * 0.08), run_time=0.6)
            self.wait(0.2)

        punch = serif("The model wasn't the only pipe.", sz=40, clr=INK)
        punch.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(punch, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.5))


# ─────────────────────────────────────────────────────────────────────────────
# B04_NaiveExpect — "Bias is in the model" assumption laid out, then undercut
# ─────────────────────────────────────────────────────────────────────────────
class B04_NaiveExpect(Scene):
    def construct(self):
        d = dur("B04")  # 7.7s
        eyebrow = caps("the intuitive assumption", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        assume = serif('"bias lives in the model —\nfix the model, fix the bias"', sz=42, clr=INK)
        assume.move_to([0, 0.5, 0])
        self.play(FadeIn(assume, shift=UP * 0.1), run_time=0.7)
        self.wait(0.4)

        strike = Line(assume.get_left() + LEFT * 0.2, assume.get_right() + RIGHT * 0.2,
                      color=CRIMSON, stroke_width=6)
        strike._qc_intentional = True
        self.play(GrowFromPoint(strike, strike.get_left()), run_time=0.5)

        correction = serif("Bias flows through multiple pipes.", sz=38, clr=TEAL)
        correction.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(correction, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.0))


# ─────────────────────────────────────────────────────────────────────────────
# B05_ThreePaths — Three causal paths: model / proxy / review-context
# ─────────────────────────────────────────────────────────────────────────────
class B05_ThreePaths(Scene):
    def construct(self):
        d = dur("B05")  # 10.7s
        eyebrow = caps("three paths, one outcome", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        protected = serif("protected attribute", sz=30, clr=MUTE).move_to([-4.5, 0, 0])
        outcome   = serif("outcome", sz=30, clr=INK).move_to([4.5, 0, 0])
        self.play(FadeIn(protected), FadeIn(outcome), run_time=0.4)

        path_data = [
            (0.8,  CRIMSON, "model path"),
            (0.0,  TEAL,    "proxy path"),
            (-0.8, GOLD,    "review-context path"),
        ]
        for y, clr, label in path_data:
            arrow = Arrow([-3.5, y, 0], [3.5, y, 0], color=clr, stroke_width=3, buff=0)
            arrow._qc_intentional = True
            lbl = caps(label, sz=18, clr=clr).move_to([0, y + 0.35, 0])
            self.play(GrowArrow(arrow), FadeIn(lbl), run_time=0.5)

        punch = serif("Block one path — the others reroute.", sz=36, clr=INK)
        punch.to_edge(DOWN, buff=0.9)
        self.play(FadeIn(punch, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


# ─────────────────────────────────────────────────────────────────────────────
# B07_PipeGraph — Full causal chain drawn; three simultaneous flows
# ─────────────────────────────────────────────────────────────────────────────
class B07_PipeGraph(Scene):
    def construct(self):
        d = dur("B07")  # 7.3s
        eyebrow = caps("the full causal chain", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        nodes = {
            "attr":   ([-5.0,  0.0, 0], "protected\nattribute", MUTE),
            "model":  ([-1.0,  1.5, 0], "model\ndecision",      CRIMSON),
            "proxy":  ([-1.0,  0.0, 0], "proxy\nvariable",      TEAL),
            "review": ([-1.0, -1.5, 0], "review\ncontext",      GOLD),
            "out":    ([ 4.0,  0.0, 0], "outcome",              INK),
        }
        dots = {}
        for key, (pos, label, clr) in nodes.items():
            dot = Dot(radius=0.15, color=clr).move_to(pos)
            dot._qc_intentional = True
            lbl = serif(label, sz=22, clr=clr).next_to(dot, DOWN, buff=0.15)
            dots[key] = dot
            self.add(dot, lbl)

        edges = [
            ("attr", "model"), ("attr", "proxy"), ("attr", "review"),
            ("model", "out"),  ("proxy", "out"),  ("review", "out"),
        ]
        for a, b in edges:
            line = Line(dots[a].get_center(), dots[b].get_center(),
                        color=MUTE, stroke_width=2)
            line._qc_intentional = True
            self.play(Create(line), run_time=0.25)

        self.wait(max(0.01, d - 4.0))


# ─────────────────────────────────────────────────────────────────────────────
# B08_QuoteModelPath — Most interventions only block model path; others persist
# ─────────────────────────────────────────────────────────────────────────────
class B08_QuoteModelPath(Scene):
    def construct(self):
        d = dur("B08")  # 9.3s
        eyebrow = caps("what most interventions actually do", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        quote = serif('"Most interventions block one path —\nthe one through the model."', sz=38, clr=INK)
        quote.move_to([0, 0.4, 0])
        self.play(FadeIn(quote, shift=UP * 0.1), run_time=0.8)
        self.wait(0.5)

        sub = caps("proxy + review paths remain open", sz=22, clr=CRIMSON).to_edge(DOWN, buff=0.9)
        self.play(FadeIn(sub, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.0))


# ─────────────────────────────────────────────────────────────────────────────
# B09_ModelBlock — Model path blocked; flow reroutes through proxy + review
# ─────────────────────────────────────────────────────────────────────────────
class B09_ModelBlock(Scene):
    def construct(self):
        d = dur("B09")  # 6.6s
        eyebrow = caps("team one blocked the model path", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        blocked = serif("model path: BLOCKED", sz=40, clr=CRIMSON)
        blocked.move_to([0, 0.8, 0])
        self.play(FadeIn(blocked), run_time=0.5)

        reroute = VGroup(
            serif("proxy path: still open →", sz=34, clr=TEAL),
            serif("review-context path: still open →", sz=34, clr=GOLD),
        ).arrange(DOWN, buff=0.35).move_to([0, -0.7, 0])
        self.play(FadeIn(reroute, shift=LEFT * 0.1), run_time=0.6)

        self.wait(max(0.01, d - 4.0))


# ─────────────────────────────────────────────────────────────────────────────
# B10_ReviewBlock — Deployment-context pipe blocked; carries the largest flow
# ─────────────────────────────────────────────────────────────────────────────
class B10_ReviewBlock(Scene):
    def construct(self):
        d = dur("B10")  # 6.9s
        eyebrow = caps("team three blocked the deployment pipe", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        result = VGroup(
            serif("review-context path: BLOCKED", sz=36, clr=TEAL),
            serif("(carried most of the flow)", sz=30, clr=MUTE),
            serif("gap closed — measurably.", sz=38, clr=INK),
        ).arrange(DOWN, buff=0.4).move_to([0, 0.1, 0])

        for line in result:
            self.play(FadeIn(line, shift=UP * 0.08), run_time=0.5)
            self.wait(0.1)

        self.wait(max(0.01, d - 4.5))


# ─────────────────────────────────────────────────────────────────────────────
# B11_QuoteLeverage — Intervene on what's inside your boundary
# ─────────────────────────────────────────────────────────────────────────────
class B11_QuoteLeverage(Scene):
    def construct(self):
        d = dur("B11")  # 7.1s
        eyebrow = caps("where your leverage actually sits", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        quote = serif('"Intervene on what is in your house.\nYour leverage is at the pipe you own."',
                       sz=38, clr=INK)
        quote.move_to([0, 0.2, 0])
        self.play(FadeIn(quote, shift=UP * 0.1), run_time=0.9)
        self.wait(max(0.01, d - 3.5))


# ─────────────────────────────────────────────────────────────────────────────
# B12_ExampleLending — 22-point gap; engineers find proxy column, remove it, gap closes
# ─────────────────────────────────────────────────────────────────────────────
class B12_ExampleLending(Scene):
    def construct(self):
        d = dur("B12")  # 19.0s
        eyebrow = caps("lending model — 22-point approval gap", sz=26, clr=MUTE).to_edge(UP, buff=0.8)
        self.play(FadeIn(eyebrow), run_time=0.3)

        gap_before = VGroup(
            serif("Group A approval rate: 74%", sz=36, clr=TEAL),
            serif("Group B approval rate: 52%", sz=36, clr=CRIMSON),
            serif("gap: 22 points", sz=40, clr=ACCENT, weight=BOLD),
        ).arrange(DOWN, buff=0.4).move_to([0, 0.8, 0])

        for line in gap_before:
            self.play(FadeIn(line, shift=UP * 0.08), run_time=0.5)
        self.wait(0.5)

        fix = serif("Engineers audit proxy column → remove it.", sz=34, clr=INK)
        fix.move_to([0, -1.3, 0])
        self.play(FadeIn(fix, shift=UP * 0.1), run_time=0.6)
        self.wait(0.4)

        gap_after = serif("gap: 4 points", sz=40, clr=TEAL)
        gap_after.to_edge(DOWN, buff=0.9)
        self.play(
            Transform(gap_before[2], gap_after),
            run_time=0.8
        )
        self.wait(max(0.01, d - 10.0))
