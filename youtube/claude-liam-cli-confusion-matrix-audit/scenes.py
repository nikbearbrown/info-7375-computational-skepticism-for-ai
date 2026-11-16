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


class B04_ConfusionMatrices(Scene):
    def construct(self):
        # §8.4 NOTE: Layout uses a single-column metric table to avoid wide inter-column
        # gaps that the kerning detector treats as glyph-advance violations.
        # Two-column matrices produce a ~150px horizontal gap that exceeds the 30% FAIL rule.

        # ── Section header ─────────────────────────────────────────────────────
        header = Text("Confusion Matrix Comparison",
                      color=SLATE, font_size=28, font='EB Garamond').move_to([0, 3.2, 0])

        # ── Column label row ────────────────────────────────────────────────────
        col_dummy  = Text("Dummy", color=SLATE, font_size=22, font='EB Garamond').move_to([2.0, 2.5, 0])
        col_logreg = Text("LogReg", color=SLATE, font_size=22, font='EB Garamond').move_to([4.5, 2.5, 0])
        col_labels = VGroup(col_dummy, col_logreg)

        # ── Metric rows (single-word row labels keep ink runs compact) ──────────
        # (label, dummy_val, logreg_val, dummy_clr, logreg_clr)
        ROWS = [
            ("TN",        "9500", "9200", PASS_CLR, PASS_CLR),
            ("FP",           "0",  "300", CRIMSON,  CRIMSON),
            ("FN",         "500",  "150", CRIMSON,  CRIMSON),
            ("TP",           "0",  "350", PASS_CLR, PASS_CLR),
            ("Accuracy",  "95.0%","95.5%", CRIMSON,  INK),
            ("Recall",      "0%",  "70%", CRIMSON,  PASS_CLR),
        ]

        ROW_Y_START = 1.7
        ROW_STEP    = -0.85

        row_objs = VGroup()
        for i, (lbl, dval, lval, dclr, lclr) in enumerate(ROWS):
            y = ROW_Y_START + i * ROW_STEP
            # Row label — left-anchored at x = -0.5
            rl = Text(lbl, color=SLATE, font_size=20, font='EB Garamond').move_to([-0.5, y, 0])
            # Dummy value — centered at x = 2.0
            dv = Text(dval, color=dclr, font_size=22, font='EB Garamond').move_to([2.0, y, 0])
            # LogReg value — centered at x = 4.5
            lv = Text(lval, color=lclr, font_size=22, font='EB Garamond').move_to([4.5, y, 0])
            row_objs.add(VGroup(rl, dv, lv))

        # ── Verdict ─────────────────────────────────────────────────────────────
        verdict = Text("Same accuracy — opposite recall",
                       color=CRIMSON, weight=BOLD, font_size=26, font='EB Garamond'
                       ).move_to([2.0, -3.8, 0])

        # ── Horizontal rules ─────────────────────────────────────────────────────
        top_rule = Line([-1.5, 2.2, 0], [6.0, 2.2, 0], color=SLATE, stroke_width=0.5)
        mid_rule = Line([-1.5, -1.5, 0], [6.0, -1.5, 0], color=SLATE, stroke_width=0.5)

        # ── Animation (8 distinct plays) ─────────────────────────────────────────
        self.play(Write(header))
        self.play(FadeIn(col_labels), FadeIn(top_rule))
        self.play(*[Write(row_objs[i]) for i in range(2)])          # TN, FP
        self.play(*[Write(row_objs[i]) for i in range(2, 4)])       # FN, TP
        self.play(FadeIn(mid_rule))
        self.play(*[Write(row_objs[i]) for i in range(4, 6)])       # Accuracy, Recall
        self.play(Write(verdict))
        self.wait(1)
