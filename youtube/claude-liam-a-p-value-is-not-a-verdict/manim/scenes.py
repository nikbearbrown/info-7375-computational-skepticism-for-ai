"""Manim scenes — claude-liam-a-p-value-is-not-a-verdict
Deep-explainer: LLM text watermarking — what the statistic can and cannot say.
Palette: claude stage — cream #FAF9F5, ink #3D3929, terracotta #D97757, mute #8B7355.

LAYOUT LAW (Simon's Ant post-mortem):
  - No hardcoded move_to([x, y, 0]); use next_to() / arrange() / to_edge() / shift().
  - Rows/columns: VGroup(...).arrange(DIR, buff=N).
  - Text inside a box: max_width derived from the box width.
  - bbox-overlap assertion (check_overlaps) at end of every construct().

REVERSAL BEATS (do not soften into captions):
  B07  switch drawn and STRUCK THROUGH; bar descends to 57.2%
  B11  10×10 grid physically SORTS into 8 ink / 92 terracotta
  B15  wall labelled IMPOSSIBLE opens doors; RELABELS to UNBUILT
  B20  ABSENT card STRIKES THROUGH and resets to PRESENT
"""
from manim import *
import random

# ── palette ──────────────────────────────────────────────────────────────────
CREAM = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"
MUTE  = "#8B7355"

config.background_color = CREAM
config.frame_rate        = 24
config.pixel_height      = 2160
config.pixel_width       = 3840


# ── helpers ──────────────────────────────────────────────────────────────────
def _t(text, size=34, color=INK, **kw):
    return Text(text.replace(" ", " "), color=color, font_size=size, font="EB Garamond", **kw)

def _m(tex, size=38):
    return MathTex(tex, color=INK, font_size=size)

def _box(content, h_pad=0.28, v_pad=0.20, stroke=INK, sw=2.0, fill=CREAM,
         corner=0.12):
    r = RoundedRectangle(
        corner_radius=corner,
        width=content.width + 2 * h_pad,
        height=content.height + 2 * v_pad,
        color=stroke, stroke_width=sw, fill_color=fill, fill_opacity=1
    )
    r.move_to(content)
    return VGroup(r, content)

def check_overlaps(*mobs, margin=0.12, label=""):
    def _bb(m):
        return (m.get_left()[0], m.get_bottom()[1], m.get_right()[0], m.get_top()[1])
    bbs = [(m, _bb(m)) for m in mobs]
    viol = []
    for i, (ma, (la, ba, ra, ta)) in enumerate(bbs):
        for j, (mb, (lb, bb_y, rb, tb)) in enumerate(bbs):
            if j <= i:
                continue
            if la < rb + margin and ra > lb - margin and ba < tb + margin and ta > bb_y - margin:
                viol.append(f"  mob[{i}] × mob[{j}]")
    tag = f"[BBOX {label}]" if label else "[BBOX]"
    if viol:
        print(f"{tag} {len(viol)} overlap(s):\n" + "\n".join(viol))
    else:
        print(f"{tag} OK")


# ── B02_GreenListBoost ───────────────────────────────────────────────────────
class B02_GreenListBoost(Scene):
    """13.2 s  prev_token → hash → vocab split GREEN/RED → δ-boost on green bars."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # token at top
        tok_lbl = _t("prev_token", size=30)
        tok_box = _box(tok_lbl, h_pad=0.35, v_pad=0.22)
        tok_box.to_edge(UP, buff=0.65)
        self.play(FadeIn(tok_box), run_time=0.4)
        self.wait(0.7)

        # hash arrow down
        a_start = tok_box.get_bottom() + DOWN * 0.06
        a_end   = a_start + DOWN * 1.0
        h_arrow = Arrow(a_start, a_end, color=INK, stroke_width=2.5,
                        tip_length=0.18, buff=0)
        h_lbl = _t("hash(·)", size=22, color=MUTE).next_to(h_arrow, RIGHT, buff=0.14)
        self.play(GrowArrow(h_arrow), FadeIn(h_lbl), run_time=0.6)
        self.wait(0.2)

        # vocabulary strip — splits into GREEN LIST (25%) and RED LIST (75%)
        voc_total_w = 9.5
        g_w = voc_total_w * 0.25
        r_w = voc_total_w * 0.75
        h_ht = 0.60

        green_rect = Rectangle(width=g_w, height=h_ht,
                               color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2)
        red_rect   = Rectangle(width=r_w, height=h_ht,
                               color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2)
        bands = VGroup(green_rect, red_rect).arrange(RIGHT, buff=0)
        bands.next_to(a_end, DOWN, buff=0.12)

        g_lbl = _t("GREEN LIST", size=20).move_to(green_rect)
        r_lbl = _t("RED LIST",   size=20).move_to(red_rect)
        γ_lbl = _t("γ = 0.25 →", size=18, color=MUTE).next_to(green_rect, UP, buff=0.08)

        self.play(FadeIn(bands), FadeIn(g_lbl), FadeIn(r_lbl), FadeIn(γ_lbl),
                  run_time=0.7)
        self.wait(0.4)

        # logit bars below bands
        bar_w   = 0.50
        bar_gap = 0.10
        n_g, n_r = 5, 7
        base_heights_g = [1.0, 1.2, 0.8, 1.4, 1.1]
        base_heights_r = [0.9, 0.7, 1.1, 0.6, 1.3, 0.8, 1.0]

        g_bars = VGroup(*[
            Rectangle(width=bar_w, height=h,
                      color=INK, fill_color=INK, fill_opacity=0.55, stroke_width=1.5)
            for h in base_heights_g
        ]).arrange(RIGHT, buff=bar_gap)
        r_bars = VGroup(*[
            Rectangle(width=bar_w, height=h,
                      color=INK, fill_color=INK, fill_opacity=0.55, stroke_width=1.5)
            for h in base_heights_r
        ]).arrange(RIGHT, buff=bar_gap)

        bar_row = VGroup(g_bars, r_bars).arrange(RIGHT, buff=0.55)
        bar_row.next_to(bands, DOWN, buff=0.50)
        # baseline-align all bars
        for b in [*g_bars, *r_bars]:
            b.align_to(bar_row, DOWN)

        self.play(FadeIn(bar_row), run_time=0.5)
        self.wait(0.5)

        # δ-boost on green bars — ONE terracotta moment
        delta_rise = 0.58
        anims = []
        for b in g_bars:
            new_h = b.height + delta_rise
            nb = Rectangle(width=bar_w, height=new_h,
                           color=TERRA, fill_color=TERRA, fill_opacity=0.72,
                           stroke_width=2.0)
            nb.set_x(b.get_x()).align_to(b, DOWN)
            anims.append(ReplacementTransform(b.copy(), nb))
            anims.append(FadeOut(b))

        δ_lbl = _t("+ δ = 2.0", size=30, color=TERRA)
        δ_lbl.next_to(g_bars, UP, buff=0.30)

        self.play(*anims, FadeIn(δ_lbl), run_time=0.9)
        self.wait(0.5)

        # parameters + citation
        cite = _t("γ = 0.25  ·  δ = 2.0  —  Kirchenbauer, Geiping, Wen, Katz, Miers, Goldstein"
                  "  —  ICML 2023, PMLR 202",
                  size=19, color=MUTE)
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cite), run_time=0.4)
        self.wait(1.8)

        check_overlaps(tok_box, bands, bar_row, cite, label="B02")


# ── B03_OneProportionZ ───────────────────────────────────────────────────────
class B03_OneProportionZ(Scene):
    """13.4 s  Token strip counts green hits; chance line at γ=0.25; z-stat; p-value falls."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        n = 24
        sq_s = 0.36
        gap  = 0.07
        # watermarked: 9 green hits (37.5% > 25% chance)
        green_idx = {1, 4, 7, 9, 12, 15, 17, 20, 22}

        squares = VGroup(*[
            Square(side_length=sq_s, color="#A08060", fill_color=CREAM,
                   fill_opacity=1, stroke_width=1.5)
            for _ in range(n)
        ]).arrange(RIGHT, buff=gap)
        squares.to_edge(UP, buff=1.10)

        self.play(FadeIn(squares), run_time=0.4)
        self.wait(0.4)

        # accumulate green hits
        count   = 0
        c_disp  = _t("0", size=44, color=INK)
        c_disp.next_to(squares, RIGHT, buff=0.30)
        self.play(FadeIn(c_disp), run_time=0.2)

        for i, sq in enumerate(squares):
            if i in green_idx:
                count += 1
                new_sq = sq.copy().set_fill(TERRA, opacity=0.85).set_stroke(TERRA, 2)
                new_c  = _t(str(count), size=44, color=INK).move_to(c_disp)
                self.play(FadeIn(new_sq), Transform(c_disp, new_c), run_time=0.15)
            else:
                self.wait(0.08)

        self.wait(0.3)

        # chance line at γ=0.25
        chance_line = Line(
            LEFT * 5.5, RIGHT * 5.5,
            color="#A08060", stroke_width=2.0
        )
        chance_line.next_to(squares, DOWN, buff=0.75)

        chance_lbl = _t("expected by chance  (0.25 x T)", size=26, color="#A08060")
        chance_lbl.next_to(chance_line, DOWN, buff=0.12)

        self.play(Create(chance_line), FadeIn(chance_lbl), run_time=0.5)
        self.wait(0.3)

        # observed bar rising above chance line
        obs_bar = Rectangle(width=0.6, height=0.0,
                            color=INK, fill_color=INK, fill_opacity=0.80,
                            stroke_width=0)
        obs_bar.next_to(chance_line, UP, buff=0).align_to(chance_line, DOWN)

        final_h = 1.35
        self.play(
            obs_bar.animate.stretch_to_fit_height(final_h).next_to(
                chance_line, UP, buff=0),
            run_time=0.7
        )
        obs_lbl = _t(f"{count}/{n}", size=28, color=TERRA)
        obs_lbl.next_to(obs_bar, UP, buff=0.10)
        self.play(FadeIn(obs_lbl), run_time=0.25)
        self.wait(0.3)

        # z statistic
        z_eq = _t("z = (s - pT) / sqrt(p(1-p)T)", size=32, color=INK)
        z_eq.next_to(chance_lbl, DOWN, buff=0.45)
        self.play(Write(z_eq), run_time=0.8)
        self.wait(0.4)

        # p-value counter falls
        p_seq = ["p = 0.78", "p = 0.31", "p = 0.062", "p = 0.008", "p = 0.0003"]
        p_lbl = _t(p_seq[0], size=34, color=TERRA)
        p_lbl.next_to(z_eq, DOWN, buff=0.45)
        self.play(FadeIn(p_lbl), run_time=0.2)
        for pv in p_seq[1:]:
            new_p = _t(pv, size=34, color=TERRA).move_to(p_lbl)
            self.play(Transform(p_lbl, new_p), run_time=0.22)
        self.wait(1.5)

        check_overlaps(squares, chance_line, obs_bar, z_eq, p_lbl, label="B03")


# ── B07_GradientNotSwitch ────────────────────────────────────────────────────
class B07_GradientNotSwitch(Scene):
    """14.4 s  Bar at 100%. Terracotta switch tries to snap to 0% — STRUCK THROUGH.
               Bar descends smoothly to 57.2%. Citation small."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # bar at 100% — cap height so 100% label stays within title-safe
        bar_max_h = 2.8
        bar_w     = 1.4
        axis_bot  = DOWN * 0.6

        bar = Rectangle(
            width=bar_w, height=bar_max_h,
            color=INK, fill_color=INK, fill_opacity=0.80, stroke_width=0
        )
        bar.align_to(axis_bot, DOWN).shift(LEFT * 0.7)

        label_100 = _t("100%", size=30, color=INK)
        label_100.next_to(bar, UP, buff=0.18)
        label_detect = _t("DETECTION", size=22, color=MUTE)
        label_detect.next_to(bar, DOWN, buff=0.30)

        self.play(FadeIn(bar), FadeIn(label_100), FadeIn(label_detect), run_time=0.5)
        self.wait(1.0)

        # terracotta switch element — tries to snap the bar to 0
        switch = VGroup(
            Line(ORIGIN, RIGHT * 1.8, color=TERRA, stroke_width=3.5),
            Triangle(color=TERRA, fill_color=TERRA, fill_opacity=1).scale(0.22)
                     .rotate(-PI / 2).next_to(ORIGIN + RIGHT * 1.8, RIGHT, buff=0)
        )
        switch_lbl = _t("\"one paraphrase kills it\"", size=26, color=TERRA)
        switch.next_to(bar, RIGHT, buff=0.55).shift(UP * 1.0)
        switch_lbl.next_to(switch, UP, buff=0.18)

        self.play(FadeIn(switch), FadeIn(switch_lbl), run_time=0.4)
        self.wait(0.3)

        # STRUCK THROUGH — cross over the switch
        strike_h = Line(
            switch.get_left() + LEFT * 0.1,
            switch.get_right() + RIGHT * 0.1,
            color=INK, stroke_width=5
        )
        strike_v = Line(
            switch.get_top() + UP * 0.1,
            switch.get_bottom() + DOWN * 0.1,
            color=INK, stroke_width=5
        )
        self.play(Create(strike_h), Create(strike_v), run_time=0.35)
        self.play(FadeOut(switch), FadeOut(switch_lbl), FadeOut(strike_h),
                  FadeOut(strike_v), run_time=0.25)
        self.wait(0.2)

        # bar descends smoothly to 57.2% — use Transform for the label so it moves
        target_h = bar_max_h * 0.572
        new_bar = bar.copy().stretch_to_fit_height(target_h).align_to(axis_bot, DOWN)
        new_label = _t("57.2%", size=30, color=TERRA)
        new_label.next_to(new_bar, UP, buff=0.18)

        self.play(
            Transform(bar, new_bar),
            Transform(label_100, new_label),
            run_time=1.1
        )
        self.wait(0.4)

        # citation
        cite1 = _t("at 1% FPR  ·  Krishna, Song, Karpinska, Wieting, Iyyer  —  NeurIPS 2023 (DIPPER)",
                   size=20, color=MUTE)
        cite2 = _t("strong human paraphrase — still detectable near 800 tokens  (Kirchenbauer et al., ICLR 2024)",
                   size=20, color=MUTE)
        cites = VGroup(cite1, cite2).arrange(DOWN, buff=0.18, aligned_edge=LEFT)
        cites.to_edge(DOWN, buff=0.45)

        self.play(FadeIn(cites), run_time=0.4)
        self.wait(2.5)

        check_overlaps(bar, cites, label="B07")


# ── B11_PositivePredictiveValue ───────────────────────────────────────────────
class B11_PositivePredictiveValue(Scene):
    """14.6 s  Two spec lines; prevalence drops; 10×10 grid fills; SORTS 8 ink / 92 terra."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        random.seed(42)

        # spec lines
        spec_sens = _t("SENSITIVITY 90%", size=30, color=MUTE)
        spec_fpr  = _t("FALSE-POSITIVE RATE 1 in 100,000", size=30, color=MUTE)
        tick_s    = _t("✓", size=30, color=INK)
        tick_f    = _t("✓", size=30, color=INK)

        row_s = VGroup(spec_sens, tick_s).arrange(RIGHT, buff=0.0)
        row_f = VGroup(spec_fpr,  tick_f).arrange(RIGHT, buff=0.0)
        spec_block = VGroup(row_s, row_f).arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        spec_block.to_edge(UP, buff=0.65)

        self.play(FadeIn(spec_block), run_time=0.5)
        self.wait(0.4)

        # prevalence marker
        prev_lbl = _t("PREVALENCE 1 in 1 000 000", size=30, color=TERRA)
        prev_arrow = Arrow(ORIGIN, DOWN * 0.5, color=TERRA, stroke_width=2.5,
                           tip_length=0.18)
        prev_row = VGroup(prev_arrow, prev_lbl).arrange(RIGHT, buff=0.22)
        prev_row.next_to(spec_block, DOWN, buff=0.55)

        self.play(FadeIn(prev_row), run_time=0.5)
        self.wait(0.4)

        # 10×10 grid of alarm marks
        sq_s  = 0.42
        sq_gap = 0.08
        n_ink  = 8
        n_all  = 100

        # choose which 8 of 100 are "true positives"
        true_idx = set(random.sample(range(n_all), n_ink))

        grid_marks = []
        for i in range(n_all):
            mk = Square(side_length=sq_s,
                        color=MUTE, fill_color="#DDD9D0", fill_opacity=1, stroke_width=0)
            grid_marks.append(mk)

        grid = VGroup(*grid_marks).arrange_in_grid(10, 10, buff=sq_gap)
        grid.next_to(prev_row, DOWN, buff=0.55)
        # Scale if needed to fit screen
        if grid.width > 11.0:
            grid.scale(11.0 / grid.width)

        self.play(FadeIn(grid), run_time=0.6)
        self.wait(0.3)

        # color change: 8 ink, 92 terra
        ink_mks   = [grid_marks[i] for i in true_idx]
        terra_mks = [grid_marks[i] for i in range(n_all) if i not in true_idx]

        self.play(
            AnimationGroup(
                *[m.animate.set_fill(TERRA, opacity=0.85).set_stroke(TERRA, 1.8)
                  for m in terra_mks],
                lag_ratio=0.008, run_time=0.9
            )
        )
        self.play(
            AnimationGroup(
                *[m.animate.set_fill(INK, opacity=0.80).set_stroke(INK, 0)
                  for m in ink_mks],
                lag_ratio=0.06, run_time=0.5
            )
        )
        self.wait(0.2)

        # SORT: ink marks drift UP-LEFT, terra marks drift DOWN-RIGHT
        self.play(
            AnimationGroup(
                *[m.animate.shift(LEFT * 0.25 + UP * 0.22) for m in ink_mks],
                lag_ratio=0.04, run_time=0.6
            ),
            AnimationGroup(
                *[m.animate.shift(RIGHT * 0.10 + DOWN * 0.08) for m in terra_mks],
                lag_ratio=0.004, run_time=0.6
            )
        )
        self.wait(0.3)

        # PPV label
        ppv = _t("positive predictive value ≈ 8%", size=24, color=WHITE)
        ppv.to_edge(DOWN, buff=0.50)
        self.play(FadeIn(ppv), run_time=0.4)
        self.wait(1.5)

        check_overlaps(spec_block, prev_row, ppv, label="B11")


# ── B12_ForensicsVersusScreening ─────────────────────────────────────────────
class B12_ForensicsVersusScreening(Scene):
    """15.5 s  One doc under magnifier (FORENSICS). Pull-back to field of pages (SCREENING).
               10 marks flare terracotta. Same detector glyph over both. "same instrument"."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # ── State 1: FORENSICS — one document under a magnifier
        doc1 = Rectangle(width=1.6, height=2.0, color=INK,
                         fill_color=CREAM, fill_opacity=1, stroke_width=2.5)
        # document lines
        for i in range(4):
            ln = Line(LEFT * 0.55, RIGHT * 0.55, color=MUTE, stroke_width=1.0)
            ln.move_to(doc1.get_center() + UP * (0.5 - i * 0.28))
            doc1 = VGroup(doc1, ln)

        # magnifier circle
        mag_c = Circle(radius=1.0, color=INK, stroke_width=3.0, fill_opacity=0)
        mag_h = Line(ORIGIN, DOWN * 0.7, color=INK, stroke_width=3.5)
        mag_h.next_to(mag_c, DOWN, buff=-0.05)
        magnifier = VGroup(mag_c, mag_h)

        forensics_group = VGroup(doc1, magnifier).arrange(RIGHT, buff=-0.3)
        forensics_group.shift(LEFT * 3.0)

        label_for = _t("FORENSICS", size=24, color=INK)
        label_for.next_to(forensics_group, UP, buff=0.35)
        sub_for = _t("ONE DOCUMENT  ·  A REAL PRIOR", size=18, color=MUTE)
        sub_for.next_to(label_for, DOWN, buff=0.14)
        tick_for = _t("✓", size=30, color=INK)
        tick_for.next_to(sub_for, RIGHT, buff=0.25)

        self.play(FadeIn(forensics_group), FadeIn(label_for), FadeIn(sub_for),
                  FadeIn(tick_for), run_time=0.6)
        self.wait(1.4)

        # detector glyph (shared — shows same instrument)
        det_lbl = _t("DETECTOR", size=20, color=INK)
        det_box = _box(det_lbl, h_pad=0.30, v_pad=0.18, corner=0.08)
        det_box.to_edge(UP, buff=0.55)
        self.play(FadeIn(det_box), run_time=0.4)
        self.wait(0.4)

        # ── State 2: pull-back to SCREENING — dense field of page marks
        # Create field of 60 small rects
        pages = VGroup(*[
            Rectangle(width=0.28, height=0.36, color=MUTE,
                      fill_color=CREAM, fill_opacity=1, stroke_width=0.8)
            for _ in range(60)
        ]).arrange_in_grid(6, 10, buff=0.14)
        pages.shift(RIGHT * 3.0)

        label_scr = _t("SCREENING", size=24, color=INK)
        label_scr.next_to(pages, UP, buff=0.35)
        sub_scr = _t("1 000 000 PAGES", size=18, color=MUTE)
        sub_scr.next_to(label_scr, DOWN, buff=0.14)

        self.play(FadeIn(pages), FadeIn(label_scr), FadeIn(sub_scr), run_time=0.7)
        self.wait(0.5)

        # ten flare terracotta
        flare_idx = [3, 7, 11, 18, 24, 32, 38, 45, 52, 57]
        flare_idx = [i for i in flare_idx if i < len(pages)]
        self.play(
            AnimationGroup(
                *[pages[i].animate.set_fill(TERRA, opacity=0.9).set_stroke(TERRA, 1.5)
                  for i in flare_idx],
                lag_ratio=0.12, run_time=0.8
            )
        )
        self.wait(0.4)

        # "same instrument" caption
        same_lbl = _t("same instrument", size=28, color=INK)
        same_lbl.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(same_lbl), run_time=0.4)
        self.wait(1.8)

        check_overlaps(forensics_group, pages, det_box, same_lbl, label="B12")


# ── B15_WallWithDoors ────────────────────────────────────────────────────────
class B15_WallWithDoors(Scene):
    """15.1 s  IMPOSSIBLE wall draws. Two doors open. NOT IN PRODUCTION seals.
               IMPOSSIBLE STRIKES THROUGH → UNBUILT. Citations small."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # Heavy ink wall across the safe area — fill_opacity=0.45 for contrast gate
        wall = Rectangle(
            width=11.5, height=2.4,
            color=INK, fill_color=INK, fill_opacity=0.45, stroke_width=0
        )
        wall.shift(UP * 0.4)
        wall_lbl = _t("IMPOSSIBLE", size=36, color=CREAM, weight=BOLD)
        wall_lbl.move_to(wall)

        self.play(DrawBorderThenFill(wall), run_time=0.5)
        self.play(Write(wall_lbl), run_time=0.4)
        self.wait(1.0)

        # Two doorways open within the wall. Doors must be WIDER than their
        # labels ("ZERO-KNOWLEDGE" at size 24 ≈ 2.9u) and the center strip
        # between them must clear the wall label ("UNBUILT" ≈ 2.0u) — the
        # original 2.6-wide doors with size-30 labels overprinted all three.
        door_w, door_h = 3.4, 2.4
        door_gap = 2.6

        door_L = Rectangle(
            width=door_w, height=door_h,
            color=CREAM, fill_color=CREAM, fill_opacity=1, stroke_width=0
        )
        door_R = door_L.copy()

        doors = VGroup(door_L, door_R).arrange(RIGHT, buff=door_gap)
        doors.move_to(wall)

        lbl_L = VGroup(
            _t("PUBLIC-KEY", size=24, color=TERRA),
            _t("VERIFICATION", size=24, color=TERRA),
        ).arrange(DOWN, buff=0.12)
        lbl_L.move_to(door_L)
        lbl_R = VGroup(
            _t("ZERO-KNOWLEDGE", size=24, color=TERRA),
            _t("PROOF", size=24, color=TERRA),
        ).arrange(DOWN, buff=0.12)
        lbl_R.move_to(door_R)

        self.play(FadeIn(door_L), FadeIn(lbl_L), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(door_R), FadeIn(lbl_R), run_time=0.5)
        self.wait(0.5)

        # NOT IN PRODUCTION seals — no INK border (avoids bbox-overlap §8.6b nesting)
        def seal(label):
            t = _t(label, size=30, color=TERRA)
            b = RoundedRectangle(corner_radius=0.10,
                                 width=t.width + 0.4, height=t.height + 0.28,
                                 color=CREAM, fill_color=CREAM, fill_opacity=1,
                                 stroke_width=0)
            b.move_to(t)
            return VGroup(b, t)

        seal_L = seal("NOT IN PRODUCTION")
        seal_R = seal("NOT IN PRODUCTION")
        seal_L.next_to(lbl_L, DOWN, buff=0.28)
        seal_R.next_to(lbl_R, DOWN, buff=0.28)

        self.play(FadeIn(seal_L), FadeIn(seal_R), run_time=0.4)
        self.wait(0.6)

        # IMPOSSIBLE → UNBUILT relabel
        strike = Line(
            wall_lbl.get_left() + LEFT * 0.1,
            wall_lbl.get_right() + RIGHT * 0.1,
            color=TERRA, stroke_width=6
        )
        self.play(Create(strike), run_time=0.35)
        self.wait(0.1)

        new_lbl = _t("UNBUILT", size=36, color=CREAM, weight=BOLD)
        new_lbl.move_to(wall_lbl)
        self.play(FadeOut(wall_lbl), FadeOut(strike), FadeIn(new_lbl), run_time=0.4)
        self.wait(0.4)

        # citations
        cites = VGroup(
            _t("Fairoze et al., Publicly-Detectable Watermarking for Language Models", size=24, color=TERRA),
            _t("PVMark  —  USENIX Security 2026", size=24, color=TERRA)
        ).arrange(DOWN, buff=0.16, aligned_edge=LEFT)
        cites.to_edge(DOWN, buff=0.45)

        self.play(FadeIn(cites), run_time=0.4)
        self.wait(2.0)

        # door LABELS included — their omission is how the overprint shipped
        check_overlaps(door_L, door_R, lbl_L, lbl_R, new_lbl, cites, label="B15")


# ── B18_PrincipalAgent ───────────────────────────────────────────────────────
class B18_PrincipalAgent(Scene):
    """15.8 s  REGULATOR ↔ PROVIDER. Two ticked reason cards. ONE terracotta arrow
               curves from PROVIDER back to its own interest. "principal–agent, not conspiracy"."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # two principals
        reg_t = _t("REGULATOR", size=32, color=INK, weight=BOLD)
        reg_sub = _t("WANTS DETECTION", size=30, color=INK)
        reg_col = VGroup(reg_t, reg_sub).arrange(DOWN, buff=0.18)

        prv_t = _t("PROVIDER", size=32, color=INK, weight=BOLD)
        prv_sub = _t("BUILDS THE DETECTOR", size=30, color=INK)
        prv_col = VGroup(prv_t, prv_sub).arrange(DOWN, buff=0.18)

        principals = VGroup(reg_col, prv_col).arrange(RIGHT, buff=3.0)
        principals.shift(UP * 1.8)

        self.play(FadeIn(principals), run_time=0.5)
        self.wait(0.8)

        # two ink reason cards, appearing between the principals (no INK border — §8.6b)
        def reason_card(text):
            lbl = _t(text, size=30, color=MUTE)
            bx  = _box(lbl, h_pad=0.35, v_pad=0.24, corner=0.10, sw=0)
            return bx

        card1 = reason_card("breaks under translation\nand rewriting")
        card2 = reason_card("risks disproportionately flagging\nnon-native English writers")
        cards = VGroup(card1, card2).arrange(DOWN, buff=0.40)
        cards.move_to(ORIGIN + DOWN * 0.1)

        tick1 = _t("OK", size=30, color=INK).next_to(card1, RIGHT, buff=0.20)
        tick2 = _t("OK", size=30, color=INK).next_to(card2, RIGHT, buff=0.20)

        self.play(FadeIn(card1), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(tick1), run_time=0.2)
        self.play(FadeIn(card2), run_time=0.4)
        self.wait(0.5)
        self.play(FadeIn(tick2), run_time=0.2)
        self.wait(0.4)

        # ONE terracotta arrow: PROVIDER → back to itself (interest loop)
        # Curved arrow from provider bottom, loops right and returns
        prv_center = prv_col.get_center()
        arc_arrow = CurvedArrow(
            prv_col.get_bottom() + DOWN * 0.05,
            prv_col.get_bottom() + RIGHT * 1.6 + DOWN * 0.05,
            angle=-TAU / 4,
            color=TERRA, stroke_width=2.8, tip_length=0.20
        )
        self.play(Create(arc_arrow), run_time=0.5)
        self.wait(0.3)

        # caption
        caption = _t("PRINCIPAL-AGENT · NOT CONSPIRACY", size=30, color=INK)
        caption.to_edge(DOWN, buff=0.65)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(2.2)

        check_overlaps(principals, cards, arc_arrow, caption, label="B18")


# ── B20_TheCheckThatCorrectedItself ──────────────────────────────────────────
class B20_TheCheckThatCorrectedItself(Scene):
    """18.0 s  Central question. Two query paths diverge (PRIMED→ABSENT, NEUTRAL→UNCERTAIN).
               OPEN ABSTRACT. Figures resolve solid ink. ABSENT STRIKES THROUGH → PRESENT.
               Caption: 'the addendum was right; the factcheck was not — until checked.'"""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # addendum pull-quote at top
        quote = _t("\"AUC above ~0.85 at 200 tokens · above ~0.9 at 600 tokens\"",
                   size=24, color=MUTE)
        quote.to_edge(UP, buff=0.65)
        self.play(FadeIn(quote), run_time=0.4)
        self.wait(0.5)

        # central serif question
        question = _t("Are these figures in the paper?", size=34, color=INK)
        question.next_to(quote, DOWN, buff=0.55)
        self.play(Write(question), run_time=0.5)
        self.wait(0.5)

        # two query paths diverge — LEFT (primed) and RIGHT (neutral)
        # Left branch
        primed_lbl = _t("PRIMED QUERY", size=30, color=MUTE)
        absent_t   = _t("ABSENT", size=28, color=INK, weight=BOLD)
        absent_box = _box(absent_t, h_pad=0.35, v_pad=0.22, stroke=INK, sw=2.5)

        left_group = VGroup(primed_lbl, absent_box).arrange(DOWN, buff=0.28)
        left_group.next_to(question, DOWN, buff=0.80).shift(LEFT * 2.8)

        # Right branch
        neutral_lbl = _t("NEUTRAL QUERY", size=30, color=MUTE)
        uncert_t    = _t("UNCERTAIN", size=28, color=TERRA, weight=BOLD)
        uncert_box  = _box(uncert_t, h_pad=0.35, v_pad=0.22, stroke=TERRA, sw=2.5,
                           fill=CREAM)

        right_group = VGroup(neutral_lbl, uncert_box).arrange(DOWN, buff=0.28)
        right_group.next_to(question, DOWN, buff=0.80).shift(RIGHT * 2.8)

        # branch arrows from question
        arr_L = Arrow(question.get_bottom(),
                      absent_box.get_top(),
                      color=INK, stroke_width=2, tip_length=0.16, buff=0.1)
        arr_R = Arrow(question.get_bottom(),
                      uncert_box.get_top(),
                      color=MUTE, stroke_width=2, tip_length=0.16, buff=0.1)

        self.play(
            GrowArrow(arr_L), FadeIn(left_group),
            GrowArrow(arr_R), FadeIn(right_group),
            run_time=0.7
        )
        self.wait(0.9)

        # PHASE 2 — clear branches, then open abstract in freed space
        self.play(
            FadeOut(arr_L), FadeOut(arr_R),
            FadeOut(left_group), FadeOut(right_group),
            run_time=0.4
        )

        open_lbl = _t("OPEN ABSTRACT", size=30, color=INK)
        open_arrow = Arrow(ORIGIN, DOWN * 0.7, color=INK, stroke_width=2.5,
                           tip_length=0.18)
        open_action = VGroup(open_lbl, open_arrow).arrange(RIGHT, buff=0.22)
        open_action.next_to(question, DOWN, buff=0.45)

        abs_band = Rectangle(
            width=8.5, height=1.1,
            color=INK, fill_color=CREAM, fill_opacity=1, stroke_width=2
        )
        abs_band.next_to(open_action, DOWN, buff=0.30)

        self.play(FadeIn(open_action), run_time=0.4)
        self.play(FadeIn(abs_band), run_time=0.4)

        confirmed = _t(
            "\"ROC-AUC remains >0.85 when T=200 tokens available · >0.9 with T=600 tokens\"",
            size=20, color=INK
        )
        confirmed.move_to(abs_band)
        self.play(FadeIn(confirmed), run_time=0.5)
        self.wait(0.5)

        # PHASE 3 — clear abstract, re-show left branch, correct ABSENT → PRESENT
        self.play(
            FadeOut(open_action), FadeOut(abs_band), FadeOut(confirmed),
            run_time=0.3
        )

        self.play(GrowArrow(arr_L), FadeIn(left_group), run_time=0.45)

        strike = Line(
            absent_t.get_left() + LEFT * 0.05,
            absent_t.get_right() + RIGHT * 0.05,
            color=TERRA, stroke_width=5
        )
        self.play(Create(strike), run_time=0.30)

        present_t = _t("PRESENT", size=28, color=INK, weight=BOLD)
        present_t.move_to(absent_box)

        present_sub = _t("ABSTRACT, FIRST PARAGRAPH", size=30, color=MUTE)
        present_sub.next_to(absent_box, DOWN, buff=0.10)

        tick_present = _t("✓", size=28, color=INK)
        tick_present.next_to(absent_box, RIGHT, buff=0.20)

        self.play(
            FadeOut(absent_t), FadeOut(strike),
            FadeIn(present_t), FadeIn(present_sub), FadeIn(tick_present),
            run_time=0.45
        )
        self.wait(0.5)

        # caption
        caption = _t(
            "the addendum was right  ·  the factcheck was not — until checked",
            size=30, color=MUTE
        )
        caption.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(2.2)

        check_overlaps(quote, question, left_group, caption, label="B20")


# ── B05_TwentyMillion (fallback — GRAPHIC/own) ───────────────────────────────
class B05_TwentyMillion(Scene):
    """13.23 s  Watermarked vs not; 20M responses; thumbs-up Δ0.01%; cited Nature 634 (2024)."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # title
        title = _t("VALIDATION AT SCALE", size=30, color=INK)
        title.to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.3)

        # two bars: watermarked vs not — nearly equal heights
        bar_ht_A = 3.0   # WATERMARKED
        bar_ht_B = 2.97  # NOT WATERMARKED (differing by a hair)
        bar_w = 1.6

        bar_A = Rectangle(width=bar_w, height=bar_ht_A,
                          color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)
        bar_B = Rectangle(width=bar_w, height=bar_ht_B,
                          color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)

        bars = VGroup(bar_A, bar_B).arrange(RIGHT, buff=2.6)
        bars.shift(DOWN * 0.3)
        for b in [bar_A, bar_B]:
            b.align_to(bars, DOWN)

        lbl_A = _t("WATERMARKED", size=26).next_to(bar_A, DOWN, buff=0.22)
        lbl_B = _t("NOT WATERMARKED", size=26).next_to(bar_B, DOWN, buff=0.22)

        self.play(
            FadeIn(bar_A), FadeIn(bar_B),
            FadeIn(lbl_A), FadeIn(lbl_B),
            run_time=0.7
        )
        self.wait(0.5)

        # terracotta delta callout on bar A — ONE terracotta moment
        delta_line = Line(
            bar_A.get_top(), bar_B.get_top(),
            color=TERRA, stroke_width=2.5
        )
        # delta callout — LEFT of bars; abbreviated to fit within title-safe
        delta_lbl = _t("Δ up  +0.01 %", size=28, color=TERRA)
        delta_sub = _t("Δ down  −0.02 %", size=28, color=MUTE)
        delta_grp = VGroup(delta_lbl, delta_sub).arrange(DOWN, buff=0.12)
        delta_grp.next_to(bars, LEFT, buff=0.30)
        delta_grp.align_to(bar_A, UP)

        self.play(Create(delta_line), FadeIn(delta_grp), run_time=0.6)
        self.wait(0.5)

        # annotation: "measured: user feedback"
        note = _t("measured: user feedback", size=28, color=INK)
        note_under = Line(note.get_left(), note.get_right(), color=INK, stroke_width=1.5)
        note_under.next_to(note, DOWN, buff=0.06)
        note_grp = VGroup(note, note_under)
        note_grp.next_to(bars, UP, buff=0.60)

        self.play(FadeIn(note_grp), run_time=0.4)
        self.wait(0.4)

        # sub-caption: 20M responses
        sub = _t("≈ 20 million live Gemini responses", size=26, color=MUTE)
        sub.next_to(note_grp, DOWN, buff=0.22)
        self.play(FadeIn(sub), run_time=0.35)
        self.wait(0.4)

        # citation
        cite = _t(
            "Dathathri et al., Nature 634, 818–823 (2024)",
            size=26, color=MUTE
        )
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cite), run_time=0.35)
        self.wait(2.8)

        check_overlaps(title, bar_A, bar_B, lbl_A, lbl_B,
                       delta_grp, note_grp, cite, label="B05")


# ── B08_TokenFloor (fallback — GRAPHIC/own) ──────────────────────────────────
class B08_TokenFloor(Scene):
    """14.36 s  Length axis with 200-token floor; below = greyed; cited EU Code of Practice."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # title
        title = _t("THE REGULATOR'S THRESHOLD", size=30)
        title.to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.3)

        # horizontal axis
        axis_len = 10.0
        axis = Line(LEFT * (axis_len / 2), RIGHT * (axis_len / 2),
                    color=INK, stroke_width=2.0)
        axis.shift(DOWN * 0.2)

        tick_labels = []
        for tok, frac in [(0, 0), (100, 0.25), (200, 0.5), (300, 0.75), (400, 1.0)]:
            x = -axis_len / 2 + frac * axis_len
            tick = Line(UP * 0.12, DOWN * 0.12, color=INK, stroke_width=1.5)
            tick.move_to([x, axis.get_center()[1], 0])
            lbl = _t(str(tok), size=20).next_to(tick, DOWN, buff=0.16)
            tick_labels.append(VGroup(tick, lbl))

        axis_lbl = _t("tokens", size=20, color=MUTE)
        axis_lbl.next_to(axis, RIGHT, buff=0.22)

        axis_grp = VGroup(axis, axis_lbl, *tick_labels)
        self.play(FadeIn(axis_grp), run_time=0.6)
        self.wait(0.4)

        # grey zone left of 200 tokens — fill_opacity=0.70 for contrast gate
        floor_x = -axis_len / 2 + 0.5 * axis_len   # 200/400 = 0.5
        grey_rect = Rectangle(
            width=axis_len * 0.5,
            height=2.0,
            color=INK, fill_color=MUTE, fill_opacity=0.70, stroke_width=0
        )
        grey_rect.next_to(axis, UP, buff=0.0)
        grey_rect.align_to(axis, LEFT)

        no_power = _t("NO STATISTICAL POWER", size=22, color=MUTE)
        no_power.move_to(grey_rect)

        self.play(FadeIn(grey_rect), FadeIn(no_power), run_time=0.5)
        self.wait(0.4)

        # 200-token floor line — ONE terracotta moment
        floor_line = DashedLine(
            [floor_x, axis.get_center()[1] - 0.3, 0],
            [floor_x, axis.get_center()[1] + 2.3, 0],
            color=TERRA, stroke_width=3, dash_length=0.18
        )
        floor_lbl = _t("200 tokens", size=24, color=TERRA)
        floor_lbl.next_to(floor_line, UP, buff=0.14)

        exemption = _t("the exemption is an admission", size=20, color=INK)
        exemption.next_to(floor_lbl, UP, buff=0.22)

        self.play(Create(floor_line), FadeIn(floor_lbl), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(exemption), run_time=0.35)
        self.wait(0.5)

        # citation
        cite = _t(
            "EU Code of Practice on marking and labelling AI-generated content",
            size=18, color=MUTE
        )
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cite), run_time=0.35)
        self.wait(3.0)

        check_overlaps(title, grey_rect, floor_line, floor_lbl,
                       exemption, cite, label="B08")


# ── B13_UnevenBurden (fallback — GRAPHIC/own) ────────────────────────────────
class B13_UnevenBurden(Scene):
    """17.88 s  Two FP bars: non-native 61%, US 8th-grade ~0%; unanimity; Patterns 2023."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # title
        title = _t("FALSE POSITIVES ARE NOT EVENLY DISTRIBUTED", size=36)
        title.to_edge(UP, buff=0.65)
        self.play(FadeIn(title), run_time=0.4)
        self.wait(0.3)

        # two bars
        bar_w = 1.8
        ht_nonnative = 1.8   # 61%
        ht_usgr8     = 0.30  # near zero (min 35px for type_check §8.1)

        bar_N = Rectangle(width=bar_w, height=ht_nonnative,
                          color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)
        bar_U = Rectangle(width=bar_w, height=ht_usgr8,
                          color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)

        bar_pair = VGroup(bar_N, bar_U).arrange(RIGHT, buff=2.2)
        bar_pair.shift(DOWN * 0.2)
        for b in [bar_N, bar_U]:
            b.align_to(bar_pair, DOWN)

        lbl_N = _t("NON-NATIVE WRITERS", size=28).next_to(bar_N, DOWN, buff=0.22)
        lbl_U = _t("8TH GRADE ESSAYS", size=28).next_to(bar_U, DOWN, buff=0.22)

        self.play(FadeIn(bar_N), FadeIn(bar_U), FadeIn(lbl_N), FadeIn(lbl_U),
                  run_time=0.7)
        self.wait(0.4)

        # 61% label — ONE terracotta moment
        pct_N = _t("61.22%", size=34, color=TERRA)
        pct_N.next_to(bar_N, UP, buff=0.14)
        pct_U = _t("NEAR ZERO", size=30, color=INK)
        pct_U.next_to(bar_U, UP, buff=0.14)

        self.play(FadeIn(pct_N), FadeIn(pct_U), run_time=0.5)
        self.wait(0.5)

        # unanimity line
        unanimity = _t("18 OF 91 FLAGGED BY ALL 7 DETECTORS", size=34, color=INK)
        unanimity.next_to(bar_pair, UP, buff=0.55)
        unanimity_under = Line(unanimity.get_left(), unanimity.get_right(),
                               color=INK, stroke_width=1.5)
        unanimity_under.next_to(unanimity, DOWN, buff=0.06)
        unani_grp = VGroup(unanimity, unanimity_under)
        self.play(FadeIn(unani_grp), run_time=0.4)
        self.wait(0.5)

        # label row: average FP rate
        avg_lbl = _t("AVG. FALSE-POSITIVE RATE — 7 COMMERCIAL DETECTORS", size=30, color=INK)
        avg_lbl.next_to(unani_grp, UP, buff=0.28)
        self.play(FadeIn(avg_lbl), run_time=0.35)
        self.wait(0.5)

        # citation
        cite = _t(
            "Liang, Yuksekgonul, Mao, Wu & Zou — Patterns (Cell Press), 2023",
            size=20, color=MUTE
        )
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cite), run_time=0.35)
        self.wait(4.0)

        check_overlaps(title, bar_N, bar_U, pct_N, pct_U,
                       unani_grp, cite, label="B13")


# ── B16_CheapAttack (fallback — GRAPHIC/own) ──────────────────────────────────
class B16_CheapAttack(Scene):
    """15.32 s  $50 large; SPOOF/SCRUB pairs for deployed vs SynthID; ICML 2024."""

    def construct(self):
        # Bottom accent rule — ink bbox floor from frame 0 (burn-in safe: buff=0.53)
        _rule = Line(LEFT * 6.0, RIGHT * 6.0, color=INK, stroke_width=2.0)
        _rule.set_stroke(color=INK, width=2.0, opacity=0.30)
        _rule.to_edge(DOWN, buff=0.53)
        self.add(_rule)

        # large cost figure — ONE terracotta moment
        cost = _t("< $50", size=60, color=TERRA)
        cost.to_edge(UP, buff=0.55)
        cost_sub = _t("to attack several deployed watermarking schemes", size=22, color=MUTE)
        cost_sub.next_to(cost, DOWN, buff=0.18)

        self.play(FadeIn(cost), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(cost_sub), run_time=0.35)
        self.wait(0.4)

        bar_w   = 1.2
        bar_gap = 1.5   # space between the two bars in each pair

        # SPOOF / FORGE row bars
        spoof_L = Rectangle(width=bar_w, height=1.4,
                            color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)
        spoof_R = Rectangle(width=bar_w, height=0.18,
                            color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)
        # SCRUB row bars
        scrub_L = Rectangle(width=bar_w, height=1.4,
                            color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)
        scrub_R = Rectangle(width=bar_w, height=1.6,
                            color=INK, fill_color=INK, fill_opacity=0.60, stroke_width=2)

        spoof_pair = VGroup(spoof_L, spoof_R).arrange(RIGHT, buff=bar_gap)
        scrub_pair = VGroup(scrub_L, scrub_R).arrange(RIGHT, buff=bar_gap)
        for b in [spoof_L, spoof_R]:
            b.align_to(spoof_pair, DOWN)
        for b in [scrub_L, scrub_R]:
            b.align_to(scrub_pair, DOWN)

        all_rows = VGroup(spoof_pair, scrub_pair).arrange(DOWN, buff=0.70)
        all_rows.next_to(cost_sub, DOWN, buff=0.45)

        # value labels — just above each bar
        val_sL  = _t("> 80 %",      size=20, color=INK)
        val_sR  = _t("mostly fails", size=20, color=MUTE)
        val_scL = _t("> 80 %",      size=20, color=INK)
        val_scR = _t("> 90 %",      size=20, color=INK)
        val_sL.next_to(spoof_L,  UP, buff=0.10)
        val_sR.next_to(spoof_R,  UP, buff=0.10)
        val_scL.next_to(scrub_L, UP, buff=0.10)
        val_scR.next_to(scrub_R, UP, buff=0.10)

        # column headers — above value labels, aligned to bar x-centers
        col_lbl_L = _t("DEPLOYED SCHEMES", size=20, color=INK)
        col_lbl_R = _t("SYNTHID", size=20, color=INK)
        col_lbl_L.next_to(val_sL, UP, buff=0.08)
        col_lbl_R.next_to(val_sL, UP, buff=0.08)   # same y as col_lbl_L
        col_lbl_R.set_x(spoof_R.get_x())            # x-align to right column

        # row labels — placed after bars are positioned
        row_lbl_spoof = _t("FORGE", size=20, color=MUTE)
        row_lbl_scrub = _t("SCRUB", size=20, color=MUTE)
        row_lbl_spoof.next_to(spoof_pair, LEFT, buff=0.40)
        row_lbl_scrub.next_to(scrub_pair, LEFT, buff=0.40)

        self.play(FadeIn(col_lbl_L), FadeIn(col_lbl_R), run_time=0.4)
        self.wait(0.2)
        self.play(
            FadeIn(spoof_pair), FadeIn(scrub_pair),
            FadeIn(row_lbl_spoof), FadeIn(row_lbl_scrub),
            FadeIn(val_sL), FadeIn(val_sR), FadeIn(val_scL), FadeIn(val_scR),
            run_time=0.7
        )
        self.wait(0.5)

        # citation
        cite = _t(
            "Jovanović, Staab, Wattenhofer & Gündel — ICML 2024, PMLR 235",
            size=18, color=MUTE
        )
        cite.to_edge(DOWN, buff=0.45)
        self.play(FadeIn(cite), run_time=0.35)
        self.wait(3.5)

        check_overlaps(cost, cost_sub, col_lbl_L, col_lbl_R,
                       spoof_pair, scrub_pair, row_lbl_spoof, row_lbl_scrub,
                       cite, label="B16")


# ── B19_SelfRetraction (fallback — GRAPHIC/own) ───────────────────────────────
class B19_SelfRetraction(Scene):
    """14.31 s  Retraction heading + verbatim clause in terracotta; brief's addendum."""

    def construct(self):
        # document frame — Rectangle (no rounded corners → no tiny arc blobs §8.1)
        doc_rect = Rectangle(
            width=11.0, height=5.8,
            color=INK, stroke_width=2.0, fill_color=CREAM, fill_opacity=1
        )
        doc_rect.shift(DOWN * 0.3)
        self.play(DrawBorderThenFill(doc_rect), run_time=0.5)
        self.wait(0.2)

        # document header
        heading = _t("ADDENDUM — CORRECTIONS TO BRIEF", size=36, color=INK, weight=BOLD)
        heading.move_to(doc_rect.get_top() + DOWN * 0.55)

        self.play(FadeIn(heading), run_time=0.45)
        self.wait(0.3)

        # RETRACTION heading — INK for §8.3 contrast gate (4.5:1 WCAG)
        ret_heading = _t("RETRACTION", size=38, color=INK, weight=BOLD)
        ret_heading.next_to(heading, DOWN, buff=0.38)

        self.play(FadeIn(ret_heading), run_time=0.4)
        self.wait(0.4)

        # verbatim retraction clause
        clause_1 = _t('"One paraphrase defeats it" — the claim', size=36, color=MUTE)
        clause_2 = _t("is overstated. The effect is a gradient,", size=36, color=MUTE)
        clause_3 = _t("not a switch. Corrected figures follow.", size=36, color=MUTE)
        clause = VGroup(clause_1, clause_2, clause_3).arrange(DOWN, buff=0.16,
                                                              aligned_edge=LEFT)
        clause.next_to(ret_heading, DOWN, buff=0.32)
        clause.shift(RIGHT * 0.1)

        # terracotta highlight rect behind clause
        hi_rect = Rectangle(
            width=clause.width + 0.4,
            height=clause.height + 0.24,
            color=TERRA, fill_color=TERRA, fill_opacity=0.12, stroke_width=0
        )
        hi_rect.move_to(clause)

        self.play(FadeIn(hi_rect), FadeIn(clause), run_time=0.5)
        self.wait(0.5)

        # attribution
        attrib = _t("THE SOURCE BRIEF'S ADDENDUM", size=36, color=INK)
        attrib.next_to(doc_rect, DOWN, buff=0.28)

        self.play(FadeIn(attrib), run_time=0.35)
        self.wait(3.5)

        check_overlaps(doc_rect, heading, ret_heading, clause, attrib, label="B19")
