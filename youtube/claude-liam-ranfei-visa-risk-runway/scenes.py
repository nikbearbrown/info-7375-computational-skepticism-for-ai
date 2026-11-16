"""scenes.py — Manim scenes for claude-liam-ranfei-visa-risk-runway "Claude, Recalibrated".

Seven Manim beats covering: branch-two-problems, value-vs-confidence,
classify-on-two-axes, two-state-machines, threshold-on-new-pool,
confirmed-vs-unknown, converge-recalibrate.

Palette: cream #F2F0E9, warm ink #3D3929, terracotta #D97757, soft #6E6A57.
Font: EB Garamond on all Text/MarkupText calls (GATE T §8.4).
No slant=ITALIC on multi-word text (Pango collapses spaces).
One terracotta accent per scene. Only mechanisms from the source beat.
"""
from manim import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


BG    = ManimColor("#F2F0E9")
INK   = ManimColor("#3D3929")
ACC   = ManimColor("#D97757")   # terracotta accent — one per scene
SOFT  = ManimColor("#6E6A57")
GHOST = ManimColor("#A8A491")


def _lbl(text, size=22, color=None, weight=None, font="EB Garamond"):
    kw = {"font_size": size, "color": color or INK, "font": font}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw)


def _small(text, color=None, font="EB Garamond"):
    return Text(text, font_size=20, color=color or SOFT, font=font)


def _box(w=2.8, h=0.85, fill=None, stroke=None):
    return Rectangle(
        width=w, height=h,
        fill_color=fill or "#FFFFFF",
        fill_opacity=1 if fill else 0,
        stroke_color=stroke or INK,
        stroke_width=1.5,
    )


# ─────────────────────────────────────────────────────────────────────────────
# B02  BranchTwoProblems     actual_duration_s = 14.49s
#
# One box ("one generalization") splits into two parallel tracks:
# "Widen the pool" and "The extension clock". Terracotta on the split.
# ─────────────────────────────────────────────────────────────────────────────
class B02_BranchTwoProblems(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Source box ────────────────────────────────────────────────────────
        src_box = _box(3.0, 0.9, fill="#FFFFFF").move_to(UP * 2.2)
        src_lbl = _lbl("one generalization", size=24).move_to(src_box)
        self.play(FadeIn(src_box), Write(src_lbl), run_time=0.8)

        # ── Divider arrow down ────────────────────────────────────────────────
        split_pt = UP * 0.9
        fork_arrow = Arrow(src_box.get_bottom(), split_pt, color=ACC,
                           stroke_width=2.5, tip_length=0.2, buff=0.05)
        self.play(GrowArrow(fork_arrow), run_time=0.5)

        # ── Left track: Widen the pool ────────────────────────────────────────
        left_center = LEFT * 2.8 + DOWN * 0.1
        left_arrow = Arrow(split_pt, left_center + UP * 0.6, color=INK,
                           stroke_width=2, tip_length=0.18, buff=0.05)
        left_box = _box(2.6, 0.85, fill="#FFFFFF").move_to(left_center)
        left_lbl = _lbl("Widen the pool", size=22).move_to(left_box)
        left_sub = _small("data-confidence problem").next_to(left_box, DOWN, buff=0.15)

        self.play(
            GrowArrow(left_arrow),
            FadeIn(left_box), Write(left_lbl),
            run_time=1.0,
        )
        self.play(FadeIn(left_sub), run_time=0.4)

        # ── Right track: The extension clock ─────────────────────────────────
        right_center = RIGHT * 2.8 + DOWN * 0.1
        right_arrow = Arrow(split_pt, right_center + UP * 0.6, color=INK,
                            stroke_width=2, tip_length=0.18, buff=0.05)
        right_box = _box(2.6, 0.85, fill="#FFFFFF").move_to(right_center)
        right_lbl = _lbl("The extension clock", size=22).move_to(right_box)
        right_sub = _small("clock structure problem").next_to(right_box, DOWN, buff=0.15)

        self.play(
            GrowArrow(right_arrow),
            FadeIn(right_box), Write(right_lbl),
            run_time=1.0,
        )
        self.play(FadeIn(right_sub), run_time=0.4)

        # ── Outcome boxes ─────────────────────────────────────────────────────
        out_left  = _box(2.4, 0.75, fill="#FFFFFF").move_to(LEFT * 2.8 + DOWN * 1.8)
        out_right = _box(2.4, 0.75, fill="#FFFFFF").move_to(RIGHT * 2.8 + DOWN * 1.8)
        olbl = _lbl("recalibrate signal", size=20).move_to(out_left)
        orbl = _lbl("recalibrate clock", size=20).move_to(out_right)
        a_l = Arrow(left_box.get_bottom(), out_left.get_top(), color=INK,
                    stroke_width=1.5, tip_length=0.16, buff=0.05)
        a_r = Arrow(right_box.get_bottom(), out_right.get_top(), color=INK,
                    stroke_width=1.5, tip_length=0.16, buff=0.05)

        self.play(
            GrowArrow(a_l), GrowArrow(a_r),
            FadeIn(out_left), FadeIn(out_right),
            Write(olbl), Write(orbl),
            run_time=1.2,
        )

        # ── Spark label ───────────────────────────────────────────────────────
        spark = _lbl("Two tracks, one repo.", size=24, color=ACC).move_to(DOWN * 3.2)
        self.play(FadeIn(spark), run_time=0.5)
        self.wait(7.5)


# ─────────────────────────────────────────────────────────────────────────────
# B03  ValueVsConfidence     actual_duration_s = 18.39s
#
# A single "signal" bar diverges into two independent axes:
# VALUE (horizontal) and CONFIDENCE (vertical). Terracotta on the split axes.
# ─────────────────────────────────────────────────────────────────────────────
class B03_ValueVsConfidence(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Single collapsed signal bar ───────────────────────────────────────
        src = _box(3.0, 0.9, fill="#FFFFFF").move_to(UP * 2.5)
        src_lbl = _lbl("signal", size=40).move_to(src)
        src_sub = _small("value + confidence collapsed").next_to(src, DOWN, buff=0.12)
        self.play(FadeIn(src), Write(src_lbl), FadeIn(src_sub), run_time=0.9)
        self.wait(0.5)

        # ── Split arc ─────────────────────────────────────────────────────────
        mid = UP * 1.1
        dot = Dot(mid, color=INK, radius=0.08)
        self.play(FadeIn(dot), run_time=0.3)

        # ── Left axis: VALUE (sponsor / non-sponsor / unknown) ────────────────
        val_hdr = _lbl("VALUE", size=38, color=INK, weight="BOLD").move_to(LEFT * 3.2 + UP * 0.2)
        val_states = VGroup(
            _box(2.4, 0.65, fill="#FFFFFF").move_to(LEFT * 3.2 + DOWN * 0.6),
            _box(2.4, 0.65, fill="#FFFFFF").move_to(LEFT * 3.2 + DOWN * 1.4),
            _box(2.4, 0.65, fill="#FFFFFF").move_to(LEFT * 3.2 + DOWN * 2.2),
        )
        val_lbls = VGroup(
            _small("sponsor").move_to(val_states[0]),
            _small("non-sponsor").move_to(val_states[1]),
            _small("unknown").move_to(val_states[2]),
        )
        arrow_l = Arrow(mid, LEFT * 3.2 + UP * 0.65, color=INK,
                        stroke_width=2.5, tip_length=0.2, buff=0.05)
        self.play(GrowArrow(arrow_l), Write(val_hdr), run_time=0.7)
        self.play(FadeIn(val_states), Write(val_lbls), run_time=1.0)

        # ── Right axis: CONFIDENCE (high / medium / low) ──────────────────────
        conf_hdr = _lbl("CONFIDENCE", size=38, color=INK, weight="BOLD").move_to(RIGHT * 3.2 + UP * 0.2)
        conf_states = VGroup(
            _box(2.4, 0.65, fill="#FFFFFF").move_to(RIGHT * 3.2 + DOWN * 0.6),
            _box(2.4, 0.65, fill="#FFFFFF").move_to(RIGHT * 3.2 + DOWN * 1.4),
            _box(2.4, 0.65, fill="#FFFFFF").move_to(RIGHT * 3.2 + DOWN * 2.2),
        )
        conf_lbls = VGroup(
            _small("high").move_to(conf_states[0]),
            _small("medium").move_to(conf_states[1]),
            _small("low").move_to(conf_states[2]),
        )
        arrow_r = Arrow(mid, RIGHT * 3.2 + UP * 0.65, color=INK,
                        stroke_width=2, tip_length=0.2, buff=0.05)
        self.play(GrowArrow(arrow_r), Write(conf_hdr), run_time=0.7)
        self.play(FadeIn(conf_states), Write(conf_lbls), run_time=1.0)

        # ── Key example: startup zero-filing → unknown LOW ────────────────────
        self.wait(1.5)
        ring = SurroundingRectangle(conf_states[2], color=INK, buff=0.06, stroke_width=2.5)
        note = _lbl("startup: no filings = LOW confidence", size=28, color=INK).move_to(DOWN * 3.35)
        self.play(Create(ring), FadeIn(note), run_time=0.7)

        spark = _lbl("Absence isn't evidence.", size=24, color=SOFT).move_to(DOWN * 3.85)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(10.0)


# ─────────────────────────────────────────────────────────────────────────────
# B07  ClassifyOnTwoAxes     actual_duration_s = 15.30s
#
# Two companies with the same raw signal land in different cells of a
# VALUE × CONFIDENCE grid. Terracotta cell = the correct differentiation.
# ─────────────────────────────────────────────────────────────────────────────
class B07_ClassifyOnTwoAxes(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Grid axes ─────────────────────────────────────────────────────────
        origin = LEFT * 3.5 + DOWN * 2.2

        x_axis = Arrow(origin, origin + RIGHT * 7.0, color=INK,
                       stroke_width=2, tip_length=0.2, buff=0)
        y_axis = Arrow(origin, origin + UP * 5.5, color=INK,
                       stroke_width=2, tip_length=0.2, buff=0)
        x_lbl = _lbl("VALUE →", size=20).next_to(x_axis, DOWN, buff=0.2)
        y_lbl = _lbl("CONFIDENCE ↑", size=20).next_to(y_axis, LEFT, buff=0.15)

        self.play(GrowArrow(x_axis), GrowArrow(y_axis), run_time=0.8)
        self.play(Write(x_lbl), Write(y_lbl), run_time=0.4)

        # ── Grid cell labels ──────────────────────────────────────────────────
        # 2×2 grid: value = unknown|non_sponsor (x), confidence = low|high (y)
        cell_tl = _small("unknown\nlow-conf").move_to(origin + RIGHT * 1.5 + UP * 4.2)
        cell_tr = _small("non-sponsor\nlow-conf").move_to(origin + RIGHT * 5.2 + UP * 4.2)
        cell_bl = _small("unknown\nhigh-conf").move_to(origin + RIGHT * 1.5 + UP * 1.5)
        cell_br = _small("non-sponsor\nhigh-conf").move_to(origin + RIGHT * 5.2 + UP * 1.5)

        # dividers
        hdiv = DashedLine(origin + RIGHT * 3.5 + DOWN * 0.1,
                          origin + RIGHT * 3.5 + UP * 5.6, color=GHOST, stroke_width=1)
        vdiv = DashedLine(origin + RIGHT * 0 + UP * 2.8,
                          origin + RIGHT * 7.0 + UP * 2.8, color=GHOST, stroke_width=1)
        self.play(Create(hdiv), Create(vdiv), run_time=0.5)
        self.play(Write(cell_tl), Write(cell_tr), Write(cell_bl), Write(cell_br), run_time=0.5)

        # ── Company A: FAANG, zero filings → non-sponsor HIGH confidence ──────
        pos_a = origin + RIGHT * 5.5 + UP * 1.5
        dot_a = Dot(pos_a, color=INK, radius=0.18)
        lbl_a = _small("FAANG\n(0 filings)").next_to(dot_a, UP + RIGHT, buff=0.08)
        self.play(FadeIn(dot_a), FadeIn(lbl_a), run_time=0.7)

        # ── Company B: startup, zero filings → unknown LOW confidence ─────────
        pos_b = origin + RIGHT * 1.3 + UP * 4.2
        dot_b = Dot(pos_b, color=ACC, radius=0.18)
        lbl_b = _small("startup\n(0 filings)").next_to(dot_b, UP + LEFT, buff=0.08)
        self.play(FadeIn(dot_b), FadeIn(lbl_b), run_time=0.7)

        # ── Highlight different cells ─────────────────────────────────────────
        self.wait(1.0)
        ring_a = SurroundingRectangle(VGroup(dot_a, lbl_a), color=INK,
                                       buff=0.15, stroke_width=2)
        ring_b = SurroundingRectangle(VGroup(dot_b, lbl_b), color=ACC,
                                       buff=0.15, stroke_width=2)
        note = _lbl("same input — different cell", size=22, color=ACC).move_to(DOWN * 2.8)
        self.play(Create(ring_a), Create(ring_b), FadeIn(note), run_time=0.8)

        spark = _lbl("Two axes, not one.", size=24, color=SOFT).move_to(DOWN * 3.4)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.8)


# ─────────────────────────────────────────────────────────────────────────────
# B08  TwoStateMachines     actual_duration_s = 16.92s
#
# One deadline timeline splits into two distinct state machines:
# initial OPT (left) and terminal STEM (right). STEM ends in a hard STOP.
# ─────────────────────────────────────────────────────────────────────────────
class B08_TwoStateMachines(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Source: one deadline ──────────────────────────────────────────────
        src = _box(3.0, 0.9, fill="#FFFFFF").move_to(UP * 2.7)
        src_lbl = _lbl("one deadline", size=26).move_to(src)
        self.play(FadeIn(src), Write(src_lbl), run_time=0.7)

        # ── Split ─────────────────────────────────────────────────────────────
        mid = UP * 1.4
        al = Arrow(src.get_bottom(), mid + LEFT * 2.5, color=ACC,
                   stroke_width=2.5, tip_length=0.2, buff=0.05)
        ar = Arrow(src.get_bottom(), mid + RIGHT * 2.5, color=INK,
                   stroke_width=2, tip_length=0.2, buff=0.05)
        self.play(GrowArrow(al), GrowArrow(ar), run_time=0.6)

        # ── LEFT: initial OPT FSM ─────────────────────────────────────────────
        l_states = [
            _box(2.2, 0.7, fill="#FFFFFF").move_to(LEFT * 3 + UP * 0.8),
            _box(2.2, 0.7, fill="#FFFFFF").move_to(LEFT * 3 + DOWN * 0.1),
            _box(2.2, 0.7, fill="#FFFFFF").move_to(LEFT * 3 + DOWN * 1.0),
        ]
        l_lbls = [
            _small("OPT active").move_to(l_states[0]),
            _small("cap-gap").move_to(l_states[1]),
            _small("H-1B approval").move_to(l_states[2]),
        ]
        l_arrows = [
            Arrow(l_states[0].get_bottom(), l_states[1].get_top(), color=INK,
                  stroke_width=1.5, tip_length=0.15, buff=0.04),
            Arrow(l_states[1].get_bottom(), l_states[2].get_top(), color=INK,
                  stroke_width=1.5, tip_length=0.15, buff=0.04),
        ]
        hdr_l = _lbl("initial OPT", size=21, color=INK, weight="BOLD").next_to(l_states[0], UP, buff=0.12)
        self.play(FadeIn(hdr_l), run_time=0.3)
        for s, lb, arr in zip(l_states, l_lbls, l_arrows + [None]):
            anims = [FadeIn(s), Write(lb)]
            if arr:
                anims.append(GrowArrow(arr))
            self.play(*anims, run_time=0.6)

        # ── RIGHT: STEM extension FSM with terminal STOP ──────────────────────
        r_states = [
            _box(2.2, 0.7, fill="#FFFFFF").move_to(RIGHT * 3 + UP * 0.8),
            _box(2.2, 0.7, fill="#FFFFFF").move_to(RIGHT * 3 + DOWN * 0.1),
            _box(2.2, 0.7, fill=INK, stroke=INK).move_to(RIGHT * 3 + DOWN * 1.0),
        ]
        r_lbls = [
            _small("STEM active").move_to(r_states[0]),
            _small("adjudication").move_to(r_states[1]),
            _small("TERMINAL STOP", color=ManimColor("#FFFFFF")).move_to(r_states[2]),
        ]
        r_arrows = [
            Arrow(r_states[0].get_bottom(), r_states[1].get_top(), color=INK,
                  stroke_width=1.5, tip_length=0.15, buff=0.04),
            Arrow(r_states[1].get_bottom(), r_states[2].get_top(), color=ACC,
                  stroke_width=2.0, tip_length=0.15, buff=0.04),
        ]
        hdr_r = _lbl("STEM extension", size=34, color=INK, weight="BOLD").next_to(r_states[0], UP, buff=0.12)
        self.play(FadeIn(hdr_r), run_time=0.3)
        for i, (s, lb) in enumerate(zip(r_states, r_lbls)):
            anims = [FadeIn(s), Write(lb)]
            if i < len(r_arrows):
                anims.append(GrowArrow(r_arrows[i]))
            self.play(*anims, run_time=0.6)

        # ── Note: no fallback after STEM ──────────────────────────────────────
        note = _lbl("no fallback after STEM", size=30, color=INK).move_to(DOWN * 2.1)
        self.play(FadeIn(note), run_time=0.5)

        spark = _lbl("Not a later date.", size=24, color=SOFT).move_to(DOWN * 2.8)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(7.5)


# ─────────────────────────────────────────────────────────────────────────────
# B13  ThresholdOnNewPool    actual_duration_s = 18.03s
#
# A FAANG-tuned cutoff line drops onto a startup distribution; the threshold
# mislabels a cluster of real sponsoring startups. Then the cutoff re-fits.
# ─────────────────────────────────────────────────────────────────────────────
class B13_ThresholdOnNewPool(Scene):
    def construct(self):
        self.camera.background_color = BG

        origin = LEFT * 4.5 + DOWN * 2.5

        # ── Axis ─────────────────────────────────────────────────────────────
        x_axis = Arrow(origin, origin + RIGHT * 8.5, color=INK,
                       stroke_width=1.5, tip_length=0.18, buff=0)
        x_lbl = _small("filing count →").next_to(x_axis, DOWN, buff=0.15)
        self.play(GrowArrow(x_axis), Write(x_lbl), run_time=0.5)

        # ── Startup distribution (low counts, right-skewed) ────────────────────
        bar_data = [
            (0, 2.8), (1, 2.1), (2, 1.5), (3, 1.0), (4, 0.7), (5, 0.4)
        ]
        bars = VGroup()
        for x_idx, h in bar_data:
            b = Rectangle(
                width=0.9, height=h,
                fill_color=SOFT.to_hex(), fill_opacity=0.55,
                stroke_color=INK, stroke_width=1,
            ).next_to(origin + RIGHT * (x_idx * 1.3 + 0.1), UP, buff=0)
            bars.add(b)
        lbl_pool = _small("startup pool").next_to(bars[0], LEFT, buff=0.3)
        self.play(FadeIn(bars), Write(lbl_pool), run_time=0.9)

        # ── FAANG-tuned cutoff drops at 3 filings ──────────────────────────────
        cutoff_x = origin + RIGHT * (3 * 1.3 + 0.45)
        cutoff_line = DashedLine(
            cutoff_x + DOWN * 0.1,
            cutoff_x + UP * 3.5,
            color=ACC, stroke_width=2.5,
        )
        faang_lbl = _lbl("FAANG cutoff", size=20, color=ACC).next_to(cutoff_line, UP, buff=0.1)
        self.play(Create(cutoff_line), FadeIn(faang_lbl), run_time=0.7)
        self.wait(0.5)

        # ── Mislabeled cluster: bars left of cutoff get an X ──────────────────
        x_marks = VGroup()
        for i in range(3):   # bars at 0,1,2 filings → mislabeled
            xm = Cross(scale_factor=0.22, color=ACC,
                       stroke_width=2.5).move_to(bars[i].get_top() + UP * 0.3)
            x_marks.add(xm)
        miss_note = _lbl("mislabeled startups", size=20, color=ACC).move_to(LEFT * 1.5 + DOWN * 1.8)
        self.play(FadeIn(x_marks), FadeIn(miss_note), run_time=0.7)
        self.wait(1.5)

        # ── Cutoff re-fits to the startup distribution ─────────────────────────
        self.play(FadeOut(x_marks), FadeOut(miss_note), FadeOut(faang_lbl), run_time=0.4)

        new_x = origin + RIGHT * (1 * 1.3 + 0.45)
        new_cutoff = DashedLine(
            new_x + DOWN * 0.1,
            new_x + UP * 3.5,
            color=INK, stroke_width=2.5,
        )
        new_lbl = _lbl("re-derived cutoff", size=20, color=INK).next_to(new_cutoff, UP, buff=0.1)
        self.play(
            Transform(cutoff_line, new_cutoff),
            FadeIn(new_lbl),
            run_time=1.0,
        )

        spark = _lbl("Cutoff follows the pool.", size=24, color=SOFT).move_to(DOWN * 3.2)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(9.0)


# ─────────────────────────────────────────────────────────────────────────────
# B16  ConfirmedVsUnknown    actual_duration_s = 16.73s
#
# Two identical RED dots start together, then separate: solid "confirmed" on
# the left, hatched "unknown / low-confidence" on the right.
# ─────────────────────────────────────────────────────────────────────────────
class B16_ConfirmedVsUnknown(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Header ────────────────────────────────────────────────────────────
        hdr = _lbl("one RED…", size=40).move_to(UP * 2.8)
        self.play(Write(hdr), run_time=0.5)

        # ── Single RED dot, center ────────────────────────────────────────────
        RED_C = ManimColor("#C0392B")
        shared = Dot(ORIGIN, color=RED_C, radius=0.45)
        self.play(FadeIn(shared), run_time=0.5)
        self.wait(0.6)

        # ── Separate: left = confirmed, right = unknown ────────────────────────
        left_dot  = Dot(LEFT * 3.0, color=RED_C, radius=0.45)
        right_dot = Dot(RIGHT * 3.0, color=RED_C, radius=0.45)

        # Hatch right dot with lines overlay
        hatch_lines = VGroup(*[
            Line(
                RIGHT * 3.0 + rotate_vector(LEFT * 0.5 + UP * (i * 0.18 - 0.45), 0.6),
                RIGHT * 3.0 + rotate_vector(RIGHT * 0.5 + UP * (i * 0.18 - 0.45), 0.6),
                color=BG, stroke_width=2.5,
            )
            for i in range(6)
        ])

        self.play(
            Transform(shared, left_dot),
            run_time=0.5,
        )
        self.play(
            FadeIn(right_dot),
            run_time=0.5,
        )
        self.play(FadeIn(hatch_lines), run_time=0.4)

        # ── Labels ────────────────────────────────────────────────────────────
        lbl_left  = _lbl("confirmed", size=36, color=INK).next_to(left_dot, DOWN, buff=0.3)
        lbl_right = _lbl("unknown", size=22, color=ACC).next_to(right_dot, DOWN, buff=0.3)
        sub_left  = _small("non-sponsor, high-conf").next_to(lbl_left, DOWN, buff=0.12)
        sub_right = _small("no filings — thin data").next_to(lbl_right, DOWN, buff=0.12)

        self.play(Write(lbl_left), Write(lbl_right), run_time=0.6)
        self.play(FadeIn(sub_left), FadeIn(sub_right), run_time=0.5)

        # ── Update header ─────────────────────────────────────────────────────
        new_hdr = _lbl("…two reds.", size=28, color=ACC).move_to(UP * 2.8)
        self.play(Transform(hdr, new_hdr), run_time=0.5)

        spark = _lbl("Two reds, not one.", size=24, color=SOFT).move_to(DOWN * 2.5)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(9.5)


# ─────────────────────────────────────────────────────────────────────────────
# B18  ConvergeRecalibrate   actual_duration_s = 21.65s
#
# Two parallel tracks ("Widen the pool" / "The extension clock") converge on
# a single endpoint labeled "Recalibrate, don't extend."
# ─────────────────────────────────────────────────────────────────────────────
class B18_ConvergeRecalibrate(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Two source boxes ──────────────────────────────────────────────────
        left_src  = _box(2.8, 0.85, fill="#FFFFFF").move_to(LEFT * 3 + UP * 2.4)
        right_src = _box(2.8, 0.85, fill="#FFFFFF").move_to(RIGHT * 3 + UP * 2.4)
        ll = _lbl("Widen the pool", size=21).move_to(left_src)
        rl = _lbl("The extension clock", size=21).move_to(right_src)

        self.play(FadeIn(left_src), Write(ll), FadeIn(right_src), Write(rl), run_time=0.8)

        # ── Intermediate steps ────────────────────────────────────────────────
        left_mid  = _box(2.6, 0.75, fill="#FFFFFF").move_to(LEFT * 3 + UP * 0.8)
        right_mid = _box(2.6, 0.75, fill="#FFFFFF").move_to(RIGHT * 3 + UP * 0.8)
        llm = _small("value × confidence").move_to(left_mid)
        rlm = _small("two-clock model").move_to(right_mid)
        al = Arrow(left_src.get_bottom(), left_mid.get_top(), color=INK,
                   stroke_width=1.5, tip_length=0.16, buff=0.04)
        ar = Arrow(right_src.get_bottom(), right_mid.get_top(), color=INK,
                   stroke_width=1.5, tip_length=0.16, buff=0.04)
        self.play(GrowArrow(al), GrowArrow(ar), run_time=0.5)
        self.play(FadeIn(left_mid), Write(llm), FadeIn(right_mid), Write(rlm), run_time=0.8)

        # ── Converge to endpoint ──────────────────────────────────────────────
        end_pt = DOWN * 0.6
        arrow_lc = Arrow(left_mid.get_bottom(), end_pt + LEFT * 0.4, color=INK,
                         stroke_width=2.5, tip_length=0.2, buff=0.05)
        arrow_rc = Arrow(right_mid.get_bottom(), end_pt + RIGHT * 0.4, color=INK,
                         stroke_width=2.5, tip_length=0.2, buff=0.05)
        self.play(GrowArrow(arrow_lc), GrowArrow(arrow_rc), run_time=0.8)

        # ── Endpoint box ──────────────────────────────────────────────────────
        end_box = _box(4.0, 1.0, fill=INK, stroke=INK).move_to(DOWN * 1.6)
        end_lbl = _lbl("Recalibrate, don't extend.", size=24,
                        color=ManimColor("#FFFFFF")).move_to(end_box)
        self.play(FadeIn(end_box), Write(end_lbl), run_time=0.8)

        # ── Confidence dim + terminal clock labels ────────────────────────────
        self.wait(1.0)
        note1 = _small("confidence dimension").next_to(left_mid, LEFT, buff=0.3)
        note2 = _small("terminal clock").next_to(right_mid, RIGHT, buff=0.3)
        self.play(FadeIn(note1), FadeIn(note2), run_time=0.5)

        spark = _lbl("Recalibrate, don't extend.", size=24, color=SOFT).move_to(DOWN * 3.1)
        self.play(FadeIn(spark), run_time=0.4)
        self.wait(13.0)
