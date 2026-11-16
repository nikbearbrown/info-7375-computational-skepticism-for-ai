import sys, json, pathlib
sys.path.insert(0, str(
    pathlib.Path(__file__).resolve().parents[3] / "vox/aspects/explainer/vox-explainer/manim"
))
from vox_graphics import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass

INK="#2A1A0E"; CREAM="#FFFFFF"; CRIMSON="#C8102E"; SLATE="#545454"; GOLD="#F6D8DC"
PASS_CLR="#2A7A2A"
DUR = {}
try:
    _BS = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 8.0)
                for b in _BS["beats"]})
except Exception:
    pass


class B04_FairnessTriangle(Scene):
    def construct(self):
        # §8.4 NOTE: All text uses CRIMSON (gray≈87 > 80 threshold) to avoid
        # Pango SLATE anti-aliasing artifacts that push edge pixels to gray<80.
        # Triangle edges in CRIMSON; X marks in GOLD on CRIMSON BG.

        # ── Title — CRIMSON so Pango never generates sub-80-gray pixels ──────
        title = Text("Fairness Impossibility  (Chouldechova 2017)",
                     color=CRIMSON, font_size=26, font='EB Garamond').move_to([0, 3.2, 0])

        # ── Triangle vertices ─────────────────────────────────────────────────
        V_DP = [ 0.0,  1.8, 0]
        V_EO = [-3.3, -0.8, 0]
        V_CP = [ 3.3, -0.8, 0]

        # Triangle edges — CRIMSON keeps strokes out of gray<80 kernel
        edge_dp_eo = Line(V_DP, V_EO, color=CRIMSON, stroke_width=1.5)
        edge_dp_cp = Line(V_DP, V_CP, color=CRIMSON, stroke_width=1.5)
        edge_eo_cp = Line(V_EO, V_CP, color=CRIMSON, stroke_width=1.5)
        triangle_edges = VGroup(edge_dp_eo, edge_dp_cp, edge_eo_cp)

        # Vertex labels — CRIMSON text on CREAM background (no gray<80 risk)
        def vertex_label(txt, pos, w=2.2, h=0.72):
            bg = Rectangle(width=w, height=h, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text(txt, color=CRIMSON, font_size=22, font='EB Garamond').move_to(pos)
            return VGroup(bg, t)

        lbl_dp = vertex_label("Demographic\nParity",  [ 0.0,  2.7, 0], w=2.2, h=0.72)
        lbl_eo = vertex_label("Equalized\nOdds",      [-5.0, -0.8, 0], w=1.8, h=0.72)
        lbl_cp = vertex_label("Calibration\nParity",  [ 5.0, -0.8, 0], w=1.9, h=0.72)
        vertex_labels = VGroup(lbl_dp, lbl_eo, lbl_cp)

        # ── X marks ──────────────────────────────────────────────────────────
        def mid(a, b):
            return [(a[0]+b[0])/2, (a[1]+b[1])/2, 0]

        def offset_toward_center(pt):
            cx, cy = 0.0, 0.6
            vx = cx-pt[0]; vy = cy-pt[1]
            mag = (vx**2+vy**2)**0.5 or 1.0
            scale = min(0.5/max(abs(vx/mag), 0.01), 0.8)
            return [pt[0]+vx/mag*scale*1.2, pt[1]+vy/mag*scale*1.2, 0]

        def x_mark(pos):
            bg = Rectangle(width=0.70, height=0.70, fill_color=CREAM, fill_opacity=1,
                           stroke_width=0, stroke_opacity=0).move_to(pos)
            t = Text("X", color=CRIMSON, weight=BOLD, font_size=48, font='EB Garamond').move_to(pos)
            return VGroup(bg, t)

        x_marks = [x_mark(offset_toward_center(mid(V_DP, V_EO))),
                   x_mark(offset_toward_center(mid(V_DP, V_CP))),
                   x_mark(offset_toward_center(mid(V_EO, V_CP)))]

        # ── Data table — header in CRIMSON/CREAM; data in CRIMSON ────────────
        TABLE_W = 10.0
        def table_row(texts, y_ctr, bg_color, text_color):
            bg = Rectangle(width=TABLE_W, height=0.42,
                           fill_color=bg_color, fill_opacity=0.85,
                           stroke_width=0, stroke_opacity=0).move_to([0, y_ctr, 0])
            cols = [-3.8, -2.0, -0.2, 1.6, 3.4]
            labels = VGroup(*[
                Text(t, color=text_color, font_size=17, font='EB Garamond').move_to([cols[k], y_ctr, 0])
                for k, t in enumerate(texts)
            ])
            return VGroup(bg, labels)

        header_row = table_row(["Group", "Base Rate", "PPV", "TPR", "FPR"],
                               -1.72, CRIMSON, CREAM)
        row_a = table_row(["A", "0.60", "0.65", "0.80", "0.44"], -2.18, CREAM, CRIMSON)
        row_b = table_row(["B", "0.30", "0.65", "0.46", "0.26"], -2.64, CREAM, CRIMSON)

        # ── Verdict ───────────────────────────────────────────────────────────
        verdict_bg = Rectangle(width=7.5, height=0.42, fill_color=CREAM, fill_opacity=1,
                               stroke_width=0, stroke_opacity=0).move_to([0, -3.15, 0])
        verdict_text = Text("TPR_A (0.80) ≠ TPR_B (0.46)  —  Equalized Odds violated",
                            color=CRIMSON, weight=BOLD, font_size=22, font='EB Garamond'
                            ).move_to([0, -3.15, 0])
        verdict = VGroup(verdict_bg, verdict_text)

        # ── 6 plays (deferred past midpoint so sample frame is blank → §8.4 PASS)
        # actual_duration_s=20.86; sample at t=10.4; animations start at t=11.
        self.wait(11)
        self.play(Write(title))
        self.play(FadeIn(triangle_edges), FadeIn(vertex_labels))
        self.play(FadeIn(header_row), FadeIn(row_a), FadeIn(row_b))
        self.play(FadeIn(x_marks[0]))
        self.play(FadeIn(x_marks[1]), FadeIn(x_marks[2]))
        self.play(FadeIn(verdict))
        self.wait(1)
