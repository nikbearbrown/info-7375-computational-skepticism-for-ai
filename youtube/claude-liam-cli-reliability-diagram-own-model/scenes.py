import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass

INK = "#2A1A0E"; CREAM = "#FFFFFF"; CRIMSON = "#C8102E"; SLATE = "#545454"
GREEN = "#2A7A2A"; ORANGE = "#D97757"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_ReliabilityDiagram(Scene):
    """Two-panel reliability diagram: in-distribution vs shifted slice.
    Left panel: well-calibrated, ECE=0.08. Right panel: overconfident, ECE=0.19.
    """

    def construct(self):
        # Pre-computed bin data (hardcoded — no runtime random)
        # (mean_predicted, fraction_positives) per bin
        INDIST_PTS = [
            (0.05, 0.06), (0.15, 0.14), (0.25, 0.23), (0.35, 0.35),
            (0.45, 0.43), (0.55, 0.54), (0.65, 0.62), (0.75, 0.74),
            (0.85, 0.84), (0.95, 0.93),
        ]
        SHIFTED_PTS = [
            (0.05, 0.03), (0.15, 0.09), (0.25, 0.17), (0.35, 0.26),
            (0.45, 0.38), (0.55, 0.51), (0.65, 0.60), (0.75, 0.69),
            (0.85, 0.73), (0.95, 0.78),
        ]
        ECE_INDIST = 0.08
        ECE_SHIFTED = 0.19

        def to_panel(p, frac, x_off):
            """Map (predicted, empirical) to scene coords with x_off shift."""
            return (x_off + (-2.0 + p * 4.0), -1.8 + frac * 3.6, 0)

        # ── Title ─────────────────────────────────────────────────────────────
        title = Text("RELIABILITY DIAGRAM", color=INK, weight=BOLD,
                     font_size=30, font='EB Garamond').move_to([0, 3.4, 0])

        # ── Two panel labels ──────────────────────────────────────────────────
        left_label = Text("In-Distribution", color=SLATE, font_size=20, font='EB Garamond'
                          ).move_to([-3.5, 2.85, 0])
        right_label = Text("Shifted Slice (high feature-X)", color=CRIMSON, font_size=20, font='EB Garamond'
                           ).move_to([3.5, 2.85, 0])

        # ── Draw one panel ────────────────────────────────────────────────────
        def make_axes(x_off, color=INK):
            x_ax = Line([x_off - 2.0, -1.8, 0], [x_off + 2.0, -1.8, 0],
                        color=color, stroke_width=2)
            y_ax = Line([x_off - 2.0, -1.8, 0], [x_off - 2.0, 1.8, 0],
                        color=color, stroke_width=2)
            return VGroup(x_ax, y_ax)

        def make_diagonal(x_off):
            return Line([x_off - 2.0, -1.8, 0], [x_off + 2.0, 1.8, 0],
                        color=SLATE, stroke_width=1.5, stroke_opacity=0.6)

        def make_curve(pts, x_off, clr):
            coords = [to_panel(p, f, x_off) for p, f in pts]
            dots = VGroup(*[Dot(c, radius=0.07, color=clr) for c in coords])
            lines = VGroup(*[
                Line(coords[i], coords[i + 1], color=clr, stroke_width=2.5)
                for i in range(len(coords) - 1)
            ])
            return VGroup(dots, lines)

        def ece_label(ece_val, x_off, color=INK):
            bg = Rectangle(width=1.8, height=0.38,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0).move_to([x_off + 1.1, -1.4, 0])
            txt = Text(f"ECE = {ece_val:.2f}", color=color, font_size=20, font='EB Garamond'
                       ).move_to([x_off + 1.1, -1.4, 0])
            return VGroup(bg, txt)

        left_axes    = make_axes(-3.5)
        left_diag    = make_diagonal(-3.5)
        left_curve   = make_curve(INDIST_PTS, -3.5, GREEN)
        left_ece     = ece_label(ECE_INDIST, -3.5, GREEN)

        right_axes   = make_axes(3.5, CRIMSON)
        right_diag   = make_diagonal(3.5)
        right_curve  = make_curve(SHIFTED_PTS, 3.5, CRIMSON)
        right_ece    = ece_label(ECE_SHIFTED, 3.5, CRIMSON)

        # ── Gap arrow in right panel ──────────────────────────────────────────
        gap_start = to_panel(0.85, 0.85, 3.5)   # perfect diagonal at 0.85
        gap_end   = to_panel(0.85, 0.73, 3.5)   # actual shifted curve at 0.85
        gap_arrow = Arrow(gap_start, gap_end, color=ORANGE, buff=0.05, stroke_width=3)
        gap_bg = Rectangle(width=1.5, height=0.32,
                           fill_color=CREAM, fill_opacity=1,
                           stroke_width=0).move_to([6.2, 0.4, 0])
        gap_txt = Text("overconfident", color=ORANGE, font_size=16, font='EB Garamond').move_to([6.2, 0.4, 0])
        gap_label = VGroup(gap_bg, gap_txt)

        # ── Divider line ──────────────────────────────────────────────────────
        divider = Line([0, -2.0, 0], [0, 2.8, 0],
                       color=SLATE, stroke_width=1, stroke_opacity=0.4)

        # ─────────────────── ANIMATION ────────────────────────────────────────
        self.add(title)
        self.play(FadeIn(left_label), FadeIn(right_label), run_time=0.6)
        self.play(Create(left_axes), Create(right_axes),
                  Create(divider), run_time=0.8)
        self.play(Create(left_diag), Create(right_diag), run_time=0.7)
        self.play(Create(left_curve), Create(right_curve), run_time=1.5)
        self.play(FadeIn(left_ece), FadeIn(right_ece), run_time=0.8)
        self.play(Create(gap_arrow), FadeIn(gap_label), run_time=0.8)
        self.wait(DUR.get("B04", 19.0) - 5.2)
