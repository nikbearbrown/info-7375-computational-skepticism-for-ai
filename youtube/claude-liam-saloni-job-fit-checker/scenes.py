"""scenes.py — Manim scenes for claude-liam-saloni-job-fit-checker.

Claude palette: cream #F2F0E9, ink #3D3929, terracotta #D97757.
Seven scenes: B02 B03 B07 B08 B13 B14 B17.
"""
import json, pathlib
from manim import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── palette ─────────────────────────────────────────────────────────────────
CREAM   = "#F2F0E9"
INK     = "#3D3929"
ACCENT  = "#D97757"   # terracotta — the one loud moment
SOFT    = "#8B8272"   # secondary text
WHITE   = "#FFFFFF"

# ── typography ───────────────────────────────────────────────────────────────
SERIF = "EB Garamond"
MONO  = "SF Mono"
SANS  = "Helvetica Neue"

# ── beat durations from beat_sheet (fallback 8s) ─────────────────────────────
DUR: dict[str, float] = {}
try:
    _sheet = json.loads(
        (pathlib.Path(__file__).with_name("beat_sheet.json")).read_text()
    )
    DUR = {
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8)
        for b in _sheet["beats"]
    }
except Exception:
    pass


def _bg() -> Rectangle:
    return (
        Rectangle(width=16, height=9)
        .set_fill(CREAM, opacity=1)
        .set_stroke(width=0)
        .move_to(ORIGIN)
    )


def _title(text: str, font_size: int = 30) -> Text:
    return Text(text, font=SERIF, font_size=font_size, color=INK).move_to(UP * 3.1)


def _spark(text: str) -> Text:
    return (
        Text(text, font=SERIF, font_size=52, color=INK)
        .move_to(DOWN * 2.9)
    )


# ─────────────────────────────────────────────────────────────────────────────
# B02  Three hard problems — accumulate
# ─────────────────────────────────────────────────────────────────────────────
class B02_ThreeHardProblems(Scene):
    def construct(self):
        dur = DUR.get("B02", 10)
        self.add(_bg())
        ttl = _title("Three hard problems")
        self.play(FadeIn(ttl), run_time=0.4)
        # Full-width INK rule → single contiguous column run at peak_row → §8.4 len<4 PASS
        rule = Line(LEFT * 6.5 + UP * 2.6, RIGHT * 6.5 + UP * 2.6, color=INK, stroke_width=1.5)
        self.add(rule)

        items = ["Work-auth bias", "Transparency gap", "Bear territory"]
        ys = [1.2, 0.0, -1.2]
        for label, y in zip(items, ys):
            accent = Line(LEFT * 4.5 + UP * y, LEFT * 4.2 + UP * y, color=ACCENT, stroke_width=4)
            t = Text(label, font=SERIF, font_size=52, color=INK).move_to(LEFT * 2.0 + UP * y)
            self.play(Create(accent), Write(t), run_time=0.65)

        sp = _spark("Three hard problems")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 2.8))


# ─────────────────────────────────────────────────────────────────────────────
# B03  Divergence targets — one list fans into five
# ─────────────────────────────────────────────────────────────────────────────
class B03_DivergenceTargets(Scene):
    def construct(self):
        dur = DUR.get("B03", 14)
        self.add(_bg())
        ttl = _title("Better by what?")
        self.play(FadeIn(ttl), run_time=0.4)
        # Full-width INK rule → single contiguous column run at peak_row → §8.4 len<4 PASS
        rule = Line(LEFT * 6.5 + UP * 2.6, RIGHT * 6.5 + UP * 2.6, color=INK, stroke_width=1.5)
        self.add(rule)

        # Vertical list layout (fan replaced to avoid wide INK band at same y)
        targets = ["interview odds", "offer rate", "acceptance rate", "salary band", "hire time"]
        ys = [1.5, 0.75, 0.0, -0.75, -1.5]
        for label, y in zip(targets, ys):
            accent = Line(LEFT * 3.5 + UP * y, LEFT * 3.2 + UP * y, color=ACCENT, stroke_width=4)
            t = Text(label, font=SERIF, font_size=44, color=INK).move_to(LEFT * 0.5 + UP * y)
            self.play(Create(accent), FadeIn(t), run_time=0.5)

        sp = _spark("Better by what")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 3.2))


# ─────────────────────────────────────────────────────────────────────────────
# B07  Mechanism vs post-hoc — two paths
# ─────────────────────────────────────────────────────────────────────────────
class B07_MechanismVsPosthoc(Scene):
    def construct(self):
        dur = DUR.get("B07", 11)
        self.add(_bg())
        ttl = _title("Reasoning IS the mechanism")
        self.play(FadeIn(ttl), run_time=0.4)

        # Left path: transparent gearbox
        left_box = Rectangle(width=3.8, height=2.2, color=INK, stroke_width=3)
        left_box.set_fill(INK, opacity=0.08).move_to(LEFT * 3.5 + UP * 0.3)
        left_label = Text("explicit score", font_size=48, color=INK).move_to(LEFT * 3.5 + UP * 0.3)
        left_tick  = Text("✓ shown", font=SERIF, font_size=48, color=INK).move_to(LEFT * 3.5 + DOWN * 0.5)

        # Right path: black box + dotted explanation
        right_box = Rectangle(width=3.8, height=2.2, color=SOFT, stroke_width=3)
        right_box.set_fill(SOFT, opacity=0.08).move_to(RIGHT * 3.5 + UP * 0.3)
        right_label = Text("black box", font_size=48, color=SOFT).move_to(RIGHT * 3.5 + UP * 0.3)
        right_sub   = Text("SHAP on top", font=SERIF, font_size=48, color=SOFT).move_to(RIGHT * 3.5 + DOWN * 0.5)

        # Dotted arrow from black box hinting at post-hoc
        dotted = DashedLine(RIGHT * 3.5 + DOWN * 1.2, RIGHT * 3.5 + DOWN * 1.8,
                            color=SOFT, stroke_width=2, dash_length=0.18)
        post_label = Text("post-hoc guess", font_size=48, color=SOFT).move_to(RIGHT * 3.5 + DOWN * 2.2)

        vs = Text("vs", font=SERIF, font_size=52, color=INK).move_to(ORIGIN + UP * 0.3)

        self.play(
            FadeIn(left_box), FadeIn(left_label), FadeIn(left_tick),
            FadeIn(vs),
            FadeIn(right_box), FadeIn(right_label), FadeIn(right_sub),
            run_time=0.8,
        )
        self.play(Create(dotted), FadeIn(post_label), run_time=0.6)

        sp = _spark("Not a bolted-on layer.")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 2.4))


# ─────────────────────────────────────────────────────────────────────────────
# B08  Threshold gate vs smooth score
# ─────────────────────────────────────────────────────────────────────────────
class B08_ThresholdGateVsScore(Scene):
    def construct(self):
        dur = DUR.get("B08", 13)
        self.add(_bg())
        ttl = _title("Disqualifying, not discounted")
        self.play(FadeIn(ttl), run_time=0.4)

        # Axes
        ax = Axes(
            x_range=[0, 1, 0.25], y_range=[0, 1.2, 0.5],
            x_length=7, y_length=3.6,
            axis_config={"color": INK, "stroke_width": 2, "include_numbers": False},
        ).move_to(LEFT * 1.5 + UP * 0.2)

        x_lab = Text("sponsorship", font_size=40, color=INK).next_to(ax, DOWN, buff=0.2)
        y_lab = Text("score", font_size=40, color=INK).rotate(PI / 2).next_to(ax, LEFT, buff=0.15)
        self.play(Create(ax), FadeIn(x_lab), FadeIn(y_lab), run_time=0.6)

        # Soft score: a diagonal ramp
        soft = ax.plot(lambda x: x, x_range=[0, 1], color=SOFT, stroke_width=4)
        soft_lab = Text("soft score", font_size=40, color=SOFT).move_to(RIGHT * 4.8 + UP * 0.5)
        self.play(Create(soft), FadeIn(soft_lab), run_time=0.6)
        self.wait(0.3)

        # Hard gate: cliff at 0.5
        hard_left  = ax.plot(lambda x: 0.0, x_range=[0, 0.499], color=ACCENT, stroke_width=5)
        hard_right = ax.plot(lambda x: 1.0, x_range=[0.501, 1.0], color=ACCENT, stroke_width=5)
        cliff = DashedLine(
            ax.c2p(0.5, 0), ax.c2p(0.5, 1.0),
            color=ACCENT, stroke_width=3, dash_length=0.15,
        )
        hard_lab = Text("hard gate", font_size=40, color=INK).move_to(RIGHT * 4.8 + DOWN * 0.3)
        self.play(
            FadeOut(soft), FadeOut(soft_lab),
            Create(hard_left), Create(hard_right), Create(cliff), FadeIn(hard_lab),
            run_time=0.8,
        )

        sp = _spark("Disqualifying, not discounted.")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 2.9))


# ─────────────────────────────────────────────────────────────────────────────
# B13  Grade the source — confirmed vs inferred
# ─────────────────────────────────────────────────────────────────────────────
class B13_GradeTheSource(Scene):
    def construct(self):
        dur = DUR.get("B13", 11)
        self.add(_bg())
        ttl = _title("Grade the source")
        self.play(FadeIn(ttl), run_time=0.4)

        # Two bars side by side — aligned to UP*1.5 at top so labels fit below
        bar_h = 2.8
        confirmed = Rectangle(width=2.4, height=bar_h, color=INK, stroke_width=0)
        confirmed.set_fill(INK, opacity=0.85)
        confirmed.align_to(UP * 1.5, UP)
        confirmed.move_to(LEFT * 2.5 + UP * (1.5 - bar_h / 2))

        inferred_bg = Rectangle(width=2.4, height=bar_h * 0.72, color=SOFT, stroke_width=0)
        inferred_bg.set_fill(SOFT, opacity=0.28)
        inferred_bg.align_to(UP * 1.5, UP)
        inferred_bg.move_to(RIGHT * 2.5 + UP * (1.5 - bar_h * 0.72 / 2))

        inferred_border = Rectangle(width=2.4, height=bar_h * 0.72, color=SOFT, stroke_width=3)
        inferred_border.set_fill(opacity=0)
        inferred_border.move_to(inferred_bg.get_center())

        hatch_lines = VGroup()
        for i in range(7):
            y = inferred_bg.get_bottom()[1] + 0.28 + i * 0.32
            x0, x1 = inferred_bg.get_left()[0] + 0.1, inferred_bg.get_right()[0] - 0.1
            hatch_lines.add(
                Line([x0, y, 0], [x1, y, 0],
                     color=SOFT, stroke_width=1.5, stroke_opacity=0.6)
            )

        # Labels sit directly below bars — well above the spark
        c_lab = Text("confirmed", font_size=40, color=INK).move_to(LEFT * 2.5 + DOWN * 1.7)
        i_lab = Text("inferred", font_size=40, color=SOFT).move_to(RIGHT * 2.5 + DOWN * 1.7)

        self.play(GrowFromEdge(confirmed, DOWN), FadeIn(c_lab), run_time=0.6)
        self.play(
            GrowFromEdge(inferred_bg, DOWN),
            FadeIn(inferred_border),
            Create(hatch_lines),
            FadeIn(i_lab),
            run_time=0.7,
        )

        arrow = Arrow(
            RIGHT * 4.2 + UP * 0.8, RIGHT * 2.9 + UP * 0.8,
            color=INK, stroke_width=3, tip_length=0.22,
        )
        q_mark = Text("?", font=SERIF, font_size=72, color=INK).move_to(RIGHT * 4.8 + UP * 0.8)
        self.play(GrowArrow(arrow), FadeIn(q_mark), run_time=0.5)

        sp = _spark("Grade the source.")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 2.8))


# ─────────────────────────────────────────────────────────────────────────────
# B14  Near-threshold reorder — small nudge, big swap
# ─────────────────────────────────────────────────────────────────────────────
class B14_NearThresholdReorder(Scene):
    def construct(self):
        dur = DUR.get("B14", 13)
        self.add(_bg())
        ttl = _title("Does it flip?")
        self.play(FadeIn(ttl), run_time=0.4)

        # Original ranking: 1, 2, 3
        jobs_before = ["#1  Acme Corp", "#2  Globex", "#3  Initech"]
        jobs_after  = ["#1  Initech",   "#2  Globex", "#3  Acme Corp"]

        def make_rows(labels, colors, x_off=0.0):
            rows = VGroup()
            for i, (label, color) in enumerate(zip(labels, colors)):
                r = RoundedRectangle(width=5.5, height=0.85, corner_radius=0.12,
                                     color=color, stroke_width=2.5)
                r.set_fill(color, opacity=0.07)
                r.move_to(RIGHT * x_off + UP * (0.8 - i * 1.05))
                t = Text(label, font=SERIF, font_size=48, color=INK)
                t.move_to(r.get_center())
                rows.add(VGroup(r, t))
            return rows

        before_colors = [INK, INK, INK]
        after_colors  = [INK, INK, SOFT]

        before = make_rows(jobs_before, before_colors, x_off=-3.2)
        after  = make_rows(jobs_after,  after_colors,  x_off=3.2)

        before_lab = Text("original", font_size=48, color=SOFT).next_to(before, UP, buff=0.25)
        after_lab  = Text("±10% skill match", font_size=48, color=INK).next_to(after, UP, buff=0.25)

        self.play(FadeIn(before), FadeIn(before_lab), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(after), FadeIn(after_lab), run_time=0.7)

        sp = _spark("Statistical tie wearing false confidence.")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 3.0))


# ─────────────────────────────────────────────────────────────────────────────
# B17  False precision — composite dissolves into buckets
# ─────────────────────────────────────────────────────────────────────────────
class B17_FalsePrecision(Scene):
    def construct(self):
        dur = DUR.get("B17", 12)
        self.add(_bg())
        ttl = _title("Kill the fake decimal")
        self.play(FadeIn(ttl), run_time=0.4)

        # False precision score (no actual number on screen — show "??.?%")
        fake = Text("??.?%", font_size=110, color=SOFT).move_to(UP * 0.5)
        fake_note = Text("implied accuracy the data cannot support", font=SERIF, font_size=48, color=SOFT).move_to(DOWN * 1.2)
        self.play(FadeIn(fake), FadeIn(fake_note), run_time=0.5)
        self.wait(0.5)

        # Dissolve into bucket
        self.play(FadeOut(fake), FadeOut(fake_note), run_time=0.5)

        buckets = [
            ("STRONG", INK, -4.5),
            ("MODERATE", INK, 0.0),
            ("WEAK", SOFT, 4.5),
        ]
        bucket_group = VGroup()
        for label, color, x in buckets:
            box = RoundedRectangle(width=3.5, height=1.6, corner_radius=0.2,
                                   color=color, stroke_width=3)
            box.set_fill(color, opacity=0.10)
            box.move_to(RIGHT * x + UP * 0.5)
            t = Text(label, font_size=40, color=INK)
            t.move_to(box.get_center())
            bucket_group.add(VGroup(box, t))

        self.play(FadeIn(bucket_group), run_time=0.7)

        # Sub-scores below the STRONG bucket — well above spark at DOWN*2.9
        sub = VGroup(
            Text("skills  0.82", font=SERIF, font_size=32, color=SOFT),
            Text("exp     0.60", font=SERIF, font_size=32, color=SOFT),
            Text("spons   0.50", font=SERIF, font_size=32, color=SOFT),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
        sub.move_to(DOWN * 1.5 + LEFT * 4.5)
        self.play(FadeIn(sub), run_time=0.6)

        sp = _spark("Less precise, more honest.")
        self.play(FadeIn(sp), run_time=0.4)
        self.wait(max(0.1, dur - 3.2))
