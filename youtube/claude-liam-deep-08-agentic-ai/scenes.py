"""scenes.py — Manim scenes for claude-liam-deep-08-agentic-ai "You Broke My Toy".

Palette: cream #F2F0E9, warm ink #3D3929, terracotta #D97757 (ONE accent per scene).
All timings are proportioned to the beat's actual_duration_s from the beat sheet.

NO slant=ITALIC on multi-word text (Pango collapses spaces — see Manim Pango Italic Bug memory).
No invented axis units. Only mechanisms drawn from the chapter's logic.
"""
from manim import *
# §8.4 — EB Garamond default (Pango fallback kerning fix)
_Tx = Text; Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try: _Mx = MarkupText; MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError: pass


# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")   # claude cream ground
INK   = ManimColor("#3D3929")   # warm ink — all primary text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted labels
GHOST = ManimColor("#A8A491")   # dimmed / placeholder
CARD  = ManimColor("#FFFFFF")   # white card surface
GOOD  = ManimColor("#3D7A3D")   # a positive state (green — only A4M2 shield)


def _lbl(text, size=28, color=None, weight=None):
    """Single-line label. Never slant=ITALIC on multi-word strings."""
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw, font='EB Garamond')


def _small(text, color=None):
    return Text(text, font_size=28, color=color or SOFT, font='EB Garamond')


# ─────────────────────────────────────────────────────────────────────────────
# A2M_PredictionVsConsequence   actual_duration_s = 15.41s
#
# Split panel: PREDICTION (left) vs CONSEQUENCE (right).
# Left: output is a statement → bounded loss → replay loops.
# Right: output is a state change → loss bar grows → replay arrow broken.
# Terracotta marks the irreversibility on the right side.
# ─────────────────────────────────────────────────────────────────────────────
class A2M_PredictionVsConsequence(Scene):

    def construct(self):
        self.camera.background_color = BG

        # ── divider + column headers ──────────────────────────────────────────
        divider = Line(UP * 3.0, DOWN * 2.5, color=SOFT, stroke_width=1.5)
        self.play(Create(divider), run_time=0.4)

        pred_hdr = _lbl("PREDICTION", size=28, weight="BOLD").move_to(LEFT * 3.5 + UP * 3.1)
        cons_hdr = _lbl("CONSEQUENCE", size=28, weight="BOLD").move_to(RIGHT * 3.5 + UP * 3.1)
        self.play(Write(pred_hdr), Write(cons_hdr), run_time=0.6)

        # ── LEFT: prediction anatomy ─────────────────────────────────────────
        p_input  = Rectangle(width=2.5, height=0.8, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.5 + UP * 1.9)
        p_in_lbl = _small("input").move_to(p_input)

        p_output = Rectangle(width=2.5, height=0.8, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.5 + UP * 0.7)
        p_out_lbl = _lbl("prediction", size=28, color=SOFT).move_to(p_output)

        p_arrow  = Arrow(p_input.get_bottom(), p_output.get_top(), color=INK,
                         stroke_width=2, tip_length=0.18, buff=0.05)
        p_loss   = _lbl("bounded loss", size=28, color=SOFT).move_to(LEFT * 3.5 + DOWN * 0.2)
        p_re_arc = CurvedArrow(
            p_output.get_right() + RIGHT * 0.05,
            p_input.get_right() + RIGHT * 0.05,
            angle=-TAU / 4, color=SOFT, stroke_width=1.5, tip_length=0.16,
        )
        p_re_lbl = _small("re-run freely").next_to(p_re_arc, RIGHT, buff=0.1)

        self.play(
            FadeIn(p_input), FadeIn(p_in_lbl),
            GrowArrow(p_arrow),
            FadeIn(p_output), FadeIn(p_out_lbl),
            run_time=1.0,
        )
        self.play(FadeIn(p_loss), Create(p_re_arc), FadeIn(p_re_lbl), run_time=0.8)

        # ── RIGHT: consequence anatomy ────────────────────────────────────────
        c_input  = Rectangle(width=2.5, height=0.8, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.5 + UP * 1.9)
        c_in_lbl = _small("input").move_to(c_input)

        c_output = Rectangle(width=2.5, height=0.8, color=INK, stroke_width=2,
                              fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.5 + UP * 0.7)
        c_out_lbl = _small("state change").move_to(c_output)

        c_arrow  = Arrow(c_input.get_bottom(), c_output.get_top(), color=INK,
                         stroke_width=2.5, tip_length=0.18, buff=0.05)

        self.play(
            FadeIn(c_input), FadeIn(c_in_lbl),
            GrowArrow(c_arrow),
            FadeIn(c_output), FadeIn(c_out_lbl),
            run_time=1.0,
        )

        # loss bar grows with access scope
        loss_bg = Rectangle(width=2.4, height=0.35, color=GHOST, stroke_width=0,
                             fill_color=GHOST, fill_opacity=0.3).move_to(RIGHT * 3.5 + DOWN * 0.05)
        _lbg_lx = loss_bg.get_left()[0]
        _lbg_cy = loss_bg.get_center()[1]
        loss_fill = Rectangle(width=0.01, height=0.35, stroke_width=0,
                               fill_color=SOFT, fill_opacity=0.85).move_to(
            [_lbg_lx + 0.005, _lbg_cy, 0]
        )
        _loss_final = Rectangle(width=2.4, height=0.35, stroke_width=0,
                                 fill_color=SOFT, fill_opacity=0.85).move_to(
            [_lbg_lx + 1.2, _lbg_cy, 0]
        )
        loss_lbl = _small("loss bounded by access").next_to(loss_bg, DOWN, buff=0.15)

        self.play(FadeIn(loss_bg), FadeIn(loss_lbl), run_time=0.4)
        self.play(Transform(loss_fill, _loss_final), run_time=1.4)

        # broken replay arrow (crossed out)
        c_re_arc = CurvedArrow(
            c_output.get_right() + RIGHT * 0.05,
            c_input.get_right() + RIGHT * 0.05,
            angle=-TAU / 4, color=GHOST, stroke_width=1.5, tip_length=0.16,
        )
        cross_h = Line(LEFT * 0.3, RIGHT * 0.3, color=INK, stroke_width=3).move_to(
            c_re_arc.get_center()
        )
        cross_v = Line(UP * 0.3, DOWN * 0.3, color=INK, stroke_width=3).move_to(
            c_re_arc.get_center()
        )
        no_rewind = _lbl("no rewind", size=28, color=SOFT).next_to(c_re_arc, RIGHT, buff=0.1)

        self.play(Create(c_re_arc), FadeIn(no_rewind), run_time=0.6)
        self.play(Create(cross_h), Create(cross_v), run_time=0.5)

        # ── caption ───────────────────────────────────────────────────────────
        caption = _small("an agent is a consequence system — its output is the world").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.6)
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
# A3M_AutonomyGap   actual_duration_s = 17.04s
#
# Vertical scale: ACTIONS block at top, terracotta GAP in middle, UNDERSTANDING
# block at bottom. No continuous stroke lines — avoids text-on-stroke audit flag.
# ─────────────────────────────────────────────────────────────────────────────
class A3M_AutonomyGap(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Autonomy vs Competence", size=36, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        col_w = 11.0   # full-width blocks; margins handled by padding
        col_x = 0.0

        # ── ACTIONS block (top) ───────────────────────────────────────────────
        act_block = Rectangle(width=col_w, height=1.55, color=INK, stroke_width=2,
                               fill_color=CARD, fill_opacity=1).move_to([col_x, 1.8, 0])
        act_hdr = _lbl("ACTIONS", size=36, weight="BOLD").move_to(act_block).shift(UP * 0.22)
        act_sub = _lbl("install · reconfigure · execute", size=28, color=SOFT).move_to(act_block).shift(DOWN * 0.28)

        self.play(FadeIn(act_block), FadeIn(act_hdr), FadeIn(act_sub), run_time=0.7)

        # ── GAP region (terracotta) ───────────────────────────────────────────
        gap_h = 2.1
        gap_y = 0.3
        gap_rect = Rectangle(width=col_w, height=gap_h, stroke_width=0,
                              fill_color=SOFT, fill_opacity=0.12).move_to([col_x, gap_y, 0])
        gap_label = _lbl("reach without judgment", size=36, color=INK).move_to([col_x, gap_y, 0])

        self.play(FadeIn(gap_rect), run_time=0.8)
        self.play(Write(gap_label), run_time=0.6)

        # ── UNDERSTANDING block (bottom) ──────────────────────────────────────
        und_block = Rectangle(width=col_w, height=1.2, color=SOFT, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).move_to([col_x, -0.87, 0])
        und_lbl = _lbl("UNDERSTANDING", size=34, color=SOFT).move_to(und_block)

        self.play(FadeIn(und_block), FadeIn(und_lbl), run_time=0.6)

        caption = _lbl("the scaffolding grants the reach — not the judgment", size=28, color=SOFT).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(7.8)


# ─────────────────────────────────────────────────────────────────────────────
# A4M_InstructionDataConflation   actual_duration_s = 19.1s
#
# A single context window as one token stream. DATA tokens (email body) and
# INSTRUCTION tokens look identical. A planted sentence inside the data block
# lights terracotta and re-routes into the agent's action output.
# Caption: "the boundary the model cannot draw."
# ─────────────────────────────────────────────────────────────────────────────
class A4M_InstructionDataConflation(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Prompt Injection", size=28, weight="BOLD").to_edge(UP, buff=0.6)
        self.play(Write(title), run_time=0.5)

        # ── context window frame ──────────────────────────────────────────────
        win = Rectangle(width=10.5, height=3.8, color=INK, stroke_width=2,
                        fill_color=CARD, fill_opacity=1).move_to(UP * 0.5)
        win_lbl = _small("CONTEXT WINDOW").next_to(win, UP, buff=0.18)
        self.play(FadeIn(win), FadeIn(win_lbl), run_time=0.5)

        # ── token rows — DATA block (top rows) ───────────────────────────────
        def _token_row(y, count, label_text, highlight=False, color=None):
            row = VGroup()
            tok_color = color or INK
            for i in range(count):
                sq = Square(side_length=0.28, color=tok_color, stroke_width=1.5,
                             fill_color=tok_color if highlight else GHOST,
                             fill_opacity=0.12 if not highlight else 0.85)
                sq.move_to([-4.6 + i * 0.42, y, 0])
                row.add(sq)
            lbl = _small(label_text, color=tok_color).move_to([-4.6 + count * 0.42 / 2, y - 0.35, 0])
            return row, lbl

        data_row1, d_lbl1 = _token_row(1.8, 20, "DATA — email body", color=SOFT)
        data_row2, d_lbl2 = _token_row(1.2, 20, "", color=SOFT)
        inst_row,  i_lbl  = _token_row(0.0, 20, "INSTRUCTION tokens", color=INK)

        self.play(
            FadeIn(data_row1), FadeIn(data_row2),
            run_time=0.7,
        )
        self.play(FadeIn(d_lbl1), run_time=0.3)
        self.play(FadeIn(inst_row), FadeIn(i_lbl), run_time=0.7)

        caption_a = _small("instructions and data look identical in the stream").to_edge(DOWN, buff=1.1)
        self.play(FadeIn(caption_a), run_time=0.5)
        self.wait(1.2)

        # ── planted sentence lights up ─────────────────────────────────────────
        # highlight tokens 10–15 in data_row2 (the planted sentence)
        planted_group = VGroup(*list(data_row2)[8:14])
        for _tok in planted_group:
            _tok.set_stroke(color=INK)
        self.play(
            planted_group.animate.set_fill(INK, opacity=0.9),
            run_time=0.8,
        )
        planted_lbl = _small("planted instruction", color=INK).next_to(planted_group, DOWN, buff=0.25)
        self.play(FadeIn(planted_lbl), run_time=0.4)
        self.wait(0.6)

        # ── reroute arrow from planted token to action output ────────────────
        out_box = Rectangle(width=3.2, height=0.7, color=INK, stroke_width=2,
                             fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.0 + DOWN * 2.1)
        out_lbl = _lbl("ACTION OUTPUT", size=28, color=INK).move_to(out_box)

        reroute = CurvedArrow(
            planted_group.get_bottom() + DOWN * 0.1,
            out_box.get_top() + UP * 0.05,
            angle=TAU / 5,
            color=INK, stroke_width=2.5, tip_length=0.18,
        )

        self.play(FadeIn(out_box), FadeIn(out_lbl), run_time=0.5)
        self.play(Create(reroute), run_time=0.8)
        self.play(FadeOut(caption_a), run_time=0.3)

        caption_b = _small("the boundary the model cannot draw").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption_b), run_time=0.5)
        self.wait(6.5)


# ─────────────────────────────────────────────────────────────────────────────
# A4M2_ChannelBoundarySpoof   actual_duration_s = 19.63s
#
# Two channels side by side. Channel 1: display-name = owner, user-ID mismatch
# caught → REFUSE (green). Boundary. Channel 2: same display name, empty
# history → ACCEPT → compromise. Terracotta on the trust gap.
# ─────────────────────────────────────────────────────────────────────────────
class A4M2_ChannelBoundarySpoof(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Identity Spoofing Across Channels", size=28, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # ── channel boxes ─────────────────────────────────────────────────────
        ch1_box = Rectangle(width=5.5, height=5.0, color=INK, stroke_width=1.5,
                             fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.3 + DOWN * 0.3)
        ch2_box = Rectangle(width=5.5, height=5.0, color=INK, stroke_width=1.5,
                             fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.3 + DOWN * 0.3)
        ch1_hdr = _lbl("CHANNEL 1", size=28, weight="BOLD").move_to(ch1_box.get_top() + DOWN * 0.35)
        ch2_hdr = _lbl("CHANNEL 2", size=28, weight="BOLD").move_to(ch2_box.get_top() + DOWN * 0.35)
        ch1_sub = _small("prior history").next_to(ch1_hdr, DOWN, buff=0.1)
        ch2_sub = _small("fresh channel — no history").next_to(ch2_hdr, DOWN, buff=0.1)

        self.play(FadeIn(ch1_box), FadeIn(ch2_box), run_time=0.5)
        self.play(
            Write(ch1_hdr), Write(ch2_hdr),
            FadeIn(ch1_sub), FadeIn(ch2_sub),
            run_time=0.6,
        )

        # ── boundary line ─────────────────────────────────────────────────────
        boundary = Line(UP * 2.4, DOWN * 2.8, color=SOFT, stroke_width=2.5, stroke_opacity=0.5)
        bnd_lbl  = _small("channel boundary").next_to(boundary, UP, buff=0.1)
        self.play(Create(boundary), FadeIn(bnd_lbl), run_time=0.5)

        # ── channel 1: ID mismatch flagged → REFUSE ──────────────────────────
        name_lbl1  = _small("display name: owner").move_to(LEFT * 3.3 + UP * 0.8)
        id_lbl1    = _small("user-ID: MISMATCH", color=INK).move_to(LEFT * 3.3 + UP * 0.25)
        mismatch_x = Line(LEFT * 0.3, RIGHT * 0.3, color=INK, stroke_width=3).move_to(
            LEFT * 3.3 + UP * 0.25 + RIGHT * 1.4
        )

        refuse_box = Rectangle(width=2.2, height=0.65, color=GOOD, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.3 + DOWN * 0.5)
        refuse_lbl = _lbl("REFUSE", size=28, color=GOOD, weight="BOLD").move_to(refuse_box)

        self.play(FadeIn(name_lbl1), run_time=0.4)
        self.play(FadeIn(id_lbl1), run_time=0.4)
        self.play(Create(mismatch_x), run_time=0.4)
        self.play(FadeIn(refuse_box), Write(refuse_lbl), run_time=0.5)

        # ── channel 2: same display name, no mismatch → ACCEPT ───────────────
        name_lbl2   = _small("display name: owner").move_to(RIGHT * 3.3 + UP * 0.8)
        no_hist     = _small("no prior context — no flags", color=GHOST).move_to(RIGHT * 3.3 + UP * 0.25)

        accept_box  = Rectangle(width=2.2, height=0.65, color=INK, stroke_width=2.5,
                                 fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.3 + DOWN * 0.5)
        accept_lbl  = _lbl("ACCEPT", size=28, color=INK, weight="BOLD").move_to(accept_box)

        self.play(FadeIn(name_lbl2), FadeIn(no_hist), run_time=0.5)
        self.play(FadeIn(accept_box), Write(accept_lbl), run_time=0.5)

        # ── compromise label below ────────────────────────────────────────────
        comp_lbl = _lbl("full compromise", size=28, color=INK).move_to(RIGHT * 3.3 + DOWN * 1.4)
        comp_arr = Arrow(accept_box.get_bottom(), comp_lbl.get_top(),
                         color=INK, stroke_width=2, tip_length=0.18, buff=0.05)
        self.play(GrowArrow(comp_arr), FadeIn(comp_lbl), run_time=0.6)

        # ── caption ───────────────────────────────────────────────────────────
        caption = _small("trust context doesn't cross channel boundaries\n— defence resets to zero").to_edge(
            DOWN, buff=0.75
        )
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(7.5)


# ─────────────────────────────────────────────────────────────────────────────
# A5M_CascadingHallucination   actual_duration_s = 18.82s
#
# Chain A → B → C → D → E. Per-step error p. Formula P(error) = 1-(1-p)^n
# writes on. Compound-error bar climbs from ~1% to ~30%. Terracotta marks
# where cascade dominates individual error.
# ─────────────────────────────────────────────────────────────────────────────
class A5M_CascadingHallucination(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Cascading Hallucination", size=28, weight="BOLD").to_edge(UP, buff=0.55)
        self.play(Write(title), run_time=0.5)

        # ── agent chain ───────────────────────────────────────────────────────
        agents = ["A", "B", "C", "D", "E"]
        n = len(agents)
        x_start = -4.0
        x_step  = 2.0
        y_chain = 1.6

        node_mobs = []
        for i, name in enumerate(agents):
            cx = x_start + i * x_step
            box = Square(side_length=0.75, color=INK, stroke_width=1.8,
                          fill_color=CARD, fill_opacity=1).move_to([cx, y_chain, 0])
            lbl = _lbl(name, size=28).move_to(box)
            node_mobs.append(VGroup(box, lbl))

        chain_group = VGroup(*node_mobs)
        self.play(FadeIn(chain_group), run_time=0.7)

        arrows = VGroup()
        for i in range(n - 1):
            cx = x_start + i * x_step
            arr = Arrow(
                [cx + 0.38, y_chain, 0],
                [cx + x_step - 0.38, y_chain, 0],
                color=INK, stroke_width=2, tip_length=0.18, buff=0,
            )
            arrows.add(arr)
        self.play(Create(arrows), run_time=0.5)

        # ── per-step error label ──────────────────────────────────────────────
        p_lbl = _lbl("p = 1% per step", size=28, color=SOFT).move_to(UP * 2.8)
        self.play(FadeIn(p_lbl), run_time=0.4)

        # ── formula write-on ─────────────────────────────────────────────────
        formula = _lbl("P(error) = 1 - (1-p)^n", size=28).move_to([0, 2.35, 0])
        self.play(Write(formula), run_time=1.2)
        self.wait(0.4)

        # ── compound-error bar chart ──────────────────────────────────────────
        # bar_vals[i] = P(error) for n=i+1 steps
        import math
        p_val = 0.01
        bar_vals = [1 - (1 - p_val) ** (i + 1) for i in range(n)]
        max_pct = bar_vals[-1]  # ≈ 0.049 for n=5 at p=0.01

        bar_max_h = 2.2
        bar_w     = 0.7
        bar_gap   = 1.8
        bar_y_bot = -1.5

        axis_line = Line(
            [x_start - 0.4, bar_y_bot, 0],
            [x_start + (n - 1) * x_step + 0.5, bar_y_bot, 0],
            color=INK, stroke_width=1.5,
        )
        # y-axis — offset left so it doesn't cross the first bar's pct label
        y_axis = Line([x_start - 0.4, bar_y_bot, 0],
                      [x_start - 0.4, bar_y_bot + bar_max_h + 0.2, 0],
                      color=INK, stroke_width=1.5)
        self.play(Create(axis_line), Create(y_axis), run_time=0.5)

        # 30% threshold line
        thresh_h = bar_max_h * 0.30 / max_pct
        thresh_y = bar_y_bot + min(thresh_h, bar_max_h)
        thresh_line = DashedLine(
            [x_start - 0.4, thresh_y, 0],
            [x_start + (n - 1) * x_step + 0.5, thresh_y, 0],
            color=ACC, stroke_width=1.5, dash_length=0.15,
        )
        thresh_lbl = _small("~30%", color=INK).move_to(
            [x_start + (n - 1) * x_step + 1.0, thresh_y, 0]
        )

        for i, v in enumerate(bar_vals):
            cx = x_start + i * x_step
            bh = (v / max_pct) * bar_max_h
            bar_color = ACC if i == n - 1 else INK
            # Full-height bar bottom-aligned; GrowFromEdge(DOWN) reveals it upward
            bar = Rectangle(
                width=bar_w, height=bh,
                fill_color=bar_color, fill_opacity=0.85, stroke_width=0,
            ).move_to([cx, bar_y_bot + bh / 2, 0])

            pct_txt = _small(f"{v * 100:.1f}%", color=bar_color).move_to(
                [cx, bar_y_bot + bh + 0.25, 0]
            )
            self.play(GrowFromEdge(bar, DOWN), run_time=0.55)
            self.play(FadeIn(pct_txt), run_time=0.2)

        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=0.5)
        caption = _small("validated at 1% each — the system fails at the cascade").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(3.5)


# ─────────────────────────────────────────────────────────────────────────────
# A6M_PatchShipsFailure   actual_duration_s = 17.71s
#
# A surface with a crack (the delete-tool gap). Patch applied — visible.
# Under the surface: glowing terracotta fault line "self-model deficit".
# Patch holds the crack. A new crack opens elsewhere with the same root.
# Caption: "same cause, new face."
# ─────────────────────────────────────────────────────────────────────────────
class A6M_PatchShipsFailure(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Patch the Surface, Ship the Cause", size=28, weight="BOLD").to_edge(UP, buff=0.70)
        self.play(Write(title), run_time=0.6)

        # ── surface block ────────────────────────────────────────────────────
        surface = Rectangle(width=8.0, height=1.6, color=INK, stroke_width=2,
                             fill_color=CARD, fill_opacity=1).move_to(UP * 0.7)
        surface_lbl = _small("system surface").move_to(surface).shift(RIGHT * 0.5)
        self.play(FadeIn(surface), FadeIn(surface_lbl), run_time=0.5)

        # ── crack #1 ─────────────────────────────────────────────────────────
        crack_pts = [
            [-1.2, 1.5, 0], [-1.0, 1.2, 0], [-1.1, 0.9, 0], [-0.9, 0.5, 0],
        ]
        crack = VMobject(color=ACC, stroke_width=3)
        crack.set_points_as_corners(crack_pts)
        crack_lbl = _small("missing delete tool", color=INK).move_to(LEFT * 1.5 + UP * 1.8)
        self.play(Create(crack), run_time=0.5)
        self.play(FadeIn(crack_lbl), run_time=0.4)
        self.wait(0.4)

        # ── patch applied ────────────────────────────────────────────────────
        patch = Rectangle(width=1.0, height=0.6, color=SOFT, stroke_width=1.5,
                           fill_color=ManimColor("#DDDAC8"), fill_opacity=0.95).move_to(
            [-1.05, 0.95, 0]
        )
        patch_lbl = _small("patch: add tool", color=SOFT).move_to(LEFT * 2.5 + DOWN * 0.6)
        self.play(FadeIn(patch), run_time=0.5)
        self.play(FadeIn(patch_lbl), run_time=0.4)
        self.wait(0.6)

        # ── sub-surface fault line ────────────────────────────────────────────
        fault = Line([-4.0, 0.0, 0], [4.0, 0.0, 0], color=INK, stroke_width=3)
        fault_lbl = _lbl("self-model deficit", size=28, color=INK).move_to(
            RIGHT * 2.0 + DOWN * 0.3
        )
        self.play(Create(fault), run_time=0.8)
        self.play(FadeIn(fault_lbl), run_time=0.5)
        self.wait(0.5)

        # ── new crack opens ───────────────────────────────────────────────────
        crack2_pts = [
            [2.2, 1.5, 0], [2.4, 1.2, 0], [2.3, 0.9, 0], [2.5, 0.5, 0],
        ]
        crack2 = VMobject(color=ACC, stroke_width=3)
        crack2.set_points_as_corners(crack2_pts)
        crack2_lbl = _small("new failure mode", color=INK).move_to(RIGHT * 3.5 + UP * 2.3)
        self.play(Create(crack2), run_time=0.5)
        self.play(FadeIn(crack2_lbl), run_time=0.4)

        caption = _small("same root cause, different surface expression").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(6.2)


# ─────────────────────────────────────────────────────────────────────────────
# A7M_FalseSuccessCatch   actual_duration_s = 18.14s
#
# Flow: irreversible action → OWNER-confirmation gate (requester rejected) →
# Execute → two readings: agent report vs independent world-state check →
# comparator → on mismatch: terracotta STOP.
# Caption: "trust the world, not the report."
# ─────────────────────────────────────────────────────────────────────────────
class A7M_FalseSuccessCatch(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("The False-Success Catch", size=36, weight="BOLD").to_edge(UP, buff=0.70)
        self.play(Write(title), run_time=0.5)

        # ── step 1: action ────────────────────────────────────────────────────
        action_box = Rectangle(width=2.8, height=0.8, color=INK, stroke_width=1.5,
                                fill_color=CARD, fill_opacity=1).move_to(LEFT * 4.5 + UP * 1.5)
        action_lbl = _lbl("irrev. action", size=36, color=SOFT).move_to(action_box)
        self.play(FadeIn(action_box), FadeIn(action_lbl), run_time=0.5)

        # ── step 2: owner gate ─────────────────────────────────────────────────
        gate_box = Rectangle(width=2.8, height=1.0, color=INK, stroke_width=2,
                              fill_color=CARD, fill_opacity=1).move_to(LEFT * 1.5 + UP * 1.5)
        gate_lbl  = _lbl("OWNER GATE", size=36, weight="BOLD").move_to(gate_box).shift(UP * 0.15)
        gate_sub  = _lbl("requester blocked", size=28, color=SOFT).move_to(gate_box).shift(DOWN * 0.25)

        arr1 = Arrow(action_box.get_right(), gate_box.get_left(),
                     color=INK, stroke_width=2, tip_length=0.18, buff=0.05)
        self.play(GrowArrow(arr1), run_time=0.4)
        self.play(FadeIn(gate_box), FadeIn(gate_lbl), FadeIn(gate_sub), run_time=0.5)

        # ── step 3: execute ────────────────────────────────────────────────────
        exec_box = Rectangle(width=2.0, height=0.8, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(RIGHT * 1.5 + UP * 1.5)
        exec_lbl = _lbl("execute", size=36, color=SOFT).move_to(exec_box)
        arr2 = Arrow(gate_box.get_right(), exec_box.get_left(),
                     color=INK, stroke_width=2, tip_length=0.18, buff=0.05)
        self.play(GrowArrow(arr2), run_time=0.4)
        self.play(FadeIn(exec_box), FadeIn(exec_lbl), run_time=0.4)

        # ── two readings branch downward ───────────────────────────────────────
        agent_box = Rectangle(width=3.2, height=0.8, color=SOFT, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).move_to(LEFT * 1.5 + UP * 0.2)
        agent_lbl = _lbl("agent report: done", size=28, color=SOFT).move_to(agent_box)

        world_box = Rectangle(width=3.2, height=0.8, color=INK, stroke_width=2,
                               fill_color=CARD, fill_opacity=1).move_to(RIGHT * 2.2 + UP * 0.2)
        world_lbl = _lbl("world check", size=36, color=INK).move_to(world_box)

        arr_left  = Arrow(exec_box.get_bottom() + DOWN * 0.05, agent_box.get_top(),
                          color=SOFT, stroke_width=1.5, tip_length=0.15, buff=0.05)
        arr_right = Arrow(exec_box.get_bottom() + DOWN * 0.05, world_box.get_top(),
                          color=INK, stroke_width=2, tip_length=0.15, buff=0.05)

        self.play(GrowArrow(arr_left), GrowArrow(arr_right), run_time=0.6)
        self.play(
            FadeIn(agent_box), FadeIn(agent_lbl),
            FadeIn(world_box), FadeIn(world_lbl),
            run_time=0.5,
        )

        # ── comparator ────────────────────────────────────────────────────────
        comp_box = Rectangle(width=1.8, height=0.75, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(RIGHT * 0.3 + DOWN * 0.9)
        comp_lbl = _lbl("compare", size=36, color=INK).move_to(comp_box)
        arr_a_comp = Arrow(agent_box.get_bottom(), comp_box.get_top(),
                           color=SOFT, stroke_width=1.5, tip_length=0.14, buff=0.05)
        arr_w_comp = Arrow(world_box.get_bottom(), comp_box.get_top(),
                           color=INK, stroke_width=2, tip_length=0.14, buff=0.05)
        self.play(GrowArrow(arr_a_comp), GrowArrow(arr_w_comp), run_time=0.5)
        self.play(FadeIn(comp_box), FadeIn(comp_lbl), run_time=0.4)

        # ── mismatch → STOP ────────────────────────────────────────────────────
        stop_box = Rectangle(width=3.4, height=0.8, color=INK, stroke_width=2.5,
                              fill_color=CARD, fill_opacity=1).move_to(RIGHT * 0.3 + DOWN * 2.0)
        stop_lbl = _lbl("MISMATCH: STOP", size=36, color=INK, weight="BOLD").move_to(stop_box)
        arr_stop = Arrow(comp_box.get_bottom(), stop_box.get_top(),
                         color=INK, stroke_width=2.5, tip_length=0.18, buff=0.05)
        self.play(GrowArrow(arr_stop), run_time=0.4)
        self.play(FadeIn(stop_box), Write(stop_lbl), run_time=0.5)

        caption = _lbl("trust the world, not the report", size=36, color=SOFT).to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(5.5)


# ─────────────────────────────────────────────────────────────────────────────
# A1V1_AshSetup   actual_duration_s = 14.06s
#
# Three-entity setup: OWNER (delegated access) → AGENT ASH → NON-OWNER sends
# "delete this email." Ash's tool inventory: send / search / forward / archive
# but NO delete. Terracotta X on the missing tool. Caption: "no delete tool —
# searching for a workaround."
# ─────────────────────────────────────────────────────────────────────────────
class A1V1_AshSetup(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Ash — Privileged Access, No Delete Tool", size=28, weight="BOLD").to_edge(UP, buff=0.45)
        self.play(Write(title), run_time=0.5)

        # Three entities
        owner_box = Rectangle(width=2.8, height=0.75, color=INK, stroke_width=2,
                               fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.4 + UP * 1.5)
        owner_lbl = _lbl("OWNER", size=28, weight="BOLD").move_to(owner_box)

        ash_box = Rectangle(width=2.8, height=0.85, color=INK, stroke_width=2.5,
                             fill_color=CARD, fill_opacity=1).move_to(LEFT * 0.4 + UP * 0.0)
        ash_lbl = _lbl("AGENT ASH", size=28, weight="BOLD", color=INK).move_to(ash_box)

        nonowner_box = Rectangle(width=2.8, height=0.75, color=SOFT, stroke_width=1.5,
                                  fill_color=CARD, fill_opacity=1).move_to(LEFT * 3.4 + DOWN * 1.5)
        nonowner_lbl = _lbl("NON-OWNER", size=28, color=SOFT).move_to(nonowner_box)

        self.play(
            FadeIn(owner_box), FadeIn(owner_lbl),
            FadeIn(ash_box), FadeIn(ash_lbl),
            FadeIn(nonowner_box), FadeIn(nonowner_lbl),
            run_time=0.7,
        )

        # Delegated-access arrow (owner → Ash)
        access_arr = Arrow(owner_box.get_right(), ash_box.get_left() + UP * 0.1,
                           color=SOFT, stroke_width=1.5, tip_length=0.15, buff=0.08)
        access_lbl = _small("delegated access").next_to(access_arr, UP, buff=0.1)
        self.play(GrowArrow(access_arr), FadeIn(access_lbl), run_time=0.5)

        # Delete request arrow (non-owner → Ash)
        del_arr = Arrow(nonowner_box.get_right(), ash_box.get_left() + DOWN * 0.1,
                        color=INK, stroke_width=2, tip_length=0.18, buff=0.08)
        del_lbl = _small("delete this email").next_to(del_arr, DOWN, buff=0.1)
        self.play(GrowArrow(del_arr), FadeIn(del_lbl), run_time=0.5)

        # Tool inventory (right column)
        tool_names = ["send", "search", "forward", "archive"]
        tool_vg = VGroup()
        for i, t in enumerate(tool_names):
            b = Rectangle(width=1.6, height=0.45, color=SOFT, stroke_width=1,
                          fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.6 + UP * (0.85 - i * 0.58))
            l = _small(t, color=SOFT).move_to(b)
            tool_vg.add(VGroup(b, l))

        no_del_box = Rectangle(width=1.6, height=0.45, color=INK, stroke_width=2,
                                fill_color=CARD, fill_opacity=1).move_to(RIGHT * 3.6 + DOWN * 1.5)
        no_del_lbl = _small("delete", color=INK).move_to(no_del_box).shift(LEFT * 0.2)
        x_h = Line(LEFT * 0.18, RIGHT * 0.18, color=ACC, stroke_width=3).move_to(
            no_del_box.get_center() + RIGHT * 0.38
        )
        x_v = Line(UP * 0.18, DOWN * 0.18, color=ACC, stroke_width=3).move_to(
            no_del_box.get_center() + RIGHT * 0.38
        )
        self.play(FadeIn(tool_vg), run_time=0.6)
        self.play(FadeIn(no_del_box), FadeIn(no_del_lbl), Create(x_h), Create(x_v), run_time=0.5)

        caption = _small("no delete tool — searching for a workaround").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(10.4)


# ─────────────────────────────────────────────────────────────────────────────
# A1V2_ResetReport   actual_duration_s = 14.47s
#
# Four-step chain: NON-OWNER approves → Ash double-checks → NON-OWNER approves
# again → Ash executes. Then the confident log entry fills the screen:
# "email account RESET — completed." Caption: the agent's world says done.
# ─────────────────────────────────────────────────────────────────────────────
class A1V2_ResetReport(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("The Report: Completed", size=28, weight="BOLD").to_edge(UP, buff=0.45)
        self.play(Write(title), run_time=0.5)

        # Four-step chain
        step_labels = [
            ("approve", SOFT),
            ("double-check", INK),
            ("approve again", SOFT),
            ("execute", INK),
        ]
        step_actors = [
            ("NON-OWNER", SOFT),
            ("ASH", INK),
            ("NON-OWNER", SOFT),
            ("ASH", INK),
        ]
        x_pos = [-4.5, -1.5, 1.5, 4.5]
        y_step = 1.3

        boxes = VGroup()
        for i, ((actor, acol), (action, lcol)) in enumerate(zip(step_actors, step_labels)):
            bx = Rectangle(width=2.5, height=1.0, color=INK, stroke_width=1.5,
                            fill_color=CARD, fill_opacity=1).move_to([x_pos[i], y_step, 0])
            actor_t = _lbl(actor, size=30, color=acol).move_to(bx).shift(UP * 0.22)
            action_t = _lbl(action, size=30, color=lcol).move_to(bx).shift(DOWN * 0.18)
            boxes.add(VGroup(bx, actor_t, action_t))

        self.play(FadeIn(boxes), run_time=1.0)

        arrows = VGroup()
        for i in range(len(x_pos) - 1):
            arr = Arrow(
                [x_pos[i] + 1.25, y_step, 0],
                [x_pos[i + 1] - 1.25, y_step, 0],
                color=INK, stroke_width=2, tip_length=0.18, buff=0,
            )
            arrows.add(arr)
        self.play(Create(arrows), run_time=0.5)

        # Big confident completion entry
        report_box = Rectangle(width=9.5, height=1.1, color=INK, stroke_width=2.5,
                                fill_color=CARD, fill_opacity=1).move_to(DOWN * 0.7)
        report_main = _lbl("email account RESET — completed", size=28, weight="BOLD", color=INK).move_to(
            report_box
        ).shift(UP * 0.1)
        report_sub = _small("status: SUCCESS").move_to(report_box).shift(DOWN * 0.25)
        self.play(FadeIn(report_box), run_time=0.4)
        self.play(Write(report_main), FadeIn(report_sub), run_time=0.7)

        caption = _small("to the agent: task finished — its own sense of the world says done").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(10.4)


# ─────────────────────────────────────────────────────────────────────────────
# A1V3_ConsequenceReveal   actual_duration_s = 13.25s
#
# Split panel: THE AGENT'S WORLD (left, calm, task closed) vs THE OWNER'S WORLD
# (right, terracotta, email still present + infrastructure wiped). Closing line:
# "you broke my toy."
# ─────────────────────────────────────────────────────────────────────────────
class A1V3_ConsequenceReveal(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Two Worlds, One Action", size=28, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        divider = Line(UP * 2.5, DOWN * 2.5, color=SOFT, stroke_width=1.5)
        self.play(Create(divider), run_time=0.4)

        # LEFT: agent's world
        left_hdr = _lbl("THE AGENT'S WORLD", size=28, weight="BOLD").move_to(LEFT * 3.2 + UP * 2.0)
        left_items = VGroup(
            _lbl("task: closed", size=28, color=SOFT),
            _lbl("email account: reset", size=28, color=SOFT),
            _lbl("status: completed", size=28, color=SOFT),
        )
        for i, it in enumerate(left_items):
            it.move_to(LEFT * 3.2 + UP * (1.1 - i * 0.7))
        self.play(Write(left_hdr), run_time=0.4)
        self.play(FadeIn(left_items), run_time=0.6)

        # RIGHT: owner's world
        right_hdr = _lbl("THE OWNER'S WORLD", size=28, weight="BOLD").move_to(RIGHT * 3.2 + UP * 2.0)
        right_items = VGroup(
            _lbl("email: still on server", size=28, color=INK, weight="BOLD"),
            _lbl("infrastructure: wiped", size=28, color=INK),
            _lbl("delete: never performed", size=28, color=INK),
        )
        for i, it in enumerate(right_items):
            it.move_to(RIGHT * 3.2 + UP * (1.1 - i * 0.7))
        self.play(Write(right_hdr), run_time=0.4)
        self.play(FadeIn(right_items), run_time=0.7)

        # Closing line
        verdict_box = Rectangle(width=5.8, height=0.75, color=INK, stroke_width=2,
                                  fill_color=CARD, fill_opacity=1).to_edge(DOWN, buff=0.45)
        verdict_lbl = _lbl('"you broke my toy"', size=28, color=INK).move_to(verdict_box)
        self.play(FadeIn(verdict_box), Write(verdict_lbl), run_time=0.6)
        self.wait(8.2)


# ─────────────────────────────────────────────────────────────────────────────
# A2V_AuditTrailParadox   actual_duration_s = 12.43s
#
# An audit log scroll. Earlier entries (greyed). The key entry glows terracotta:
# "[08:49] email account RESET — completed   status: SUCCESS". Below it the
# world-state contradicts it. A CONTRADICTION marker fires. Caption: "no
# automated check flagged it."
# ─────────────────────────────────────────────────────────────────────────────
class A2V_AuditTrailParadox(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("The Audit Trail Was Also Wrong", size=28, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        # Log frame
        log_frame = Rectangle(width=10.5, height=4.4, color=INK, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).move_to(UP * 0.2)
        log_hdr = _small("AUDIT LOG").next_to(log_frame, UP, buff=0.1)
        self.play(FadeIn(log_frame), FadeIn(log_hdr), run_time=0.4)

        # Earlier greyed entries
        prior = VGroup(
            _small("[08:41] inbox query — completed", color=GHOST),
            _small("[08:43] forward message to owner — completed", color=GHOST),
            _small("[08:47] search: sensitive messages — 1 result", color=GHOST),
        )
        for i, e in enumerate(prior):
            e.move_to(log_frame.get_top() + DOWN * (0.4 + i * 0.45))
            e.align_to(log_frame, LEFT).shift(RIGHT * 0.35)
        self.play(FadeIn(prior), run_time=0.5)

        # The contradicted key entry (highlighted)
        key_bg = Rectangle(width=10.1, height=0.65, color=INK, stroke_width=1.5,
                            fill_color=ManimColor("#FFF4EE"), fill_opacity=1).move_to(
            log_frame.get_top() + DOWN * 1.85
        )
        key_text = _lbl("[08:49] email account RESET — completed     status: SUCCESS", size=30, color=INK).move_to(key_bg)
        self.play(FadeIn(key_bg), FadeIn(key_text), run_time=0.5)

        # World-state line (contradicts the entry)
        world_line = _lbl("world state: email still present on server", size=28, color=INK).move_to(
            log_frame.get_top() + DOWN * 2.7
        )
        self.play(FadeIn(world_line), run_time=0.4)

        # Contradiction marker
        contr_box = Rectangle(width=8.5, height=0.65, color=INK, stroke_width=2,
                               fill_color=CARD, fill_opacity=1).move_to(
            log_frame.get_bottom() + DOWN * 0.45
        )
        contr_lbl = _lbl("CONTRADICTION — not flagged by any automated check", size=30, color=INK, weight="BOLD").move_to(contr_box)
        self.play(FadeIn(contr_box), Write(contr_lbl), run_time=0.6)
        self.wait(8.0)


# ─────────────────────────────────────────────────────────────────────────────
# A4V_SocialToolkit   actual_duration_s = 16.01s
#
# The four-piece social engineering toolkit: URGENCY / CONFIDENT TONE /
# PRECISE FORMAT / RIGHT NAME. Each appears as a block. Then a threshold bar
# labeled "OUTWARDLY HARMFUL" — the request slips past it. Caption: "zero
# technical skill required."
# ─────────────────────────────────────────────────────────────────────────────
class A4V_SocialToolkit(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("The Social Engineering Toolkit", size=28, weight="BOLD").to_edge(UP, buff=0.45)
        self.play(Write(title), run_time=0.5)

        # Four tool blocks appearing one by one
        tool_defs = [
            ("URGENCY", "pressing deadline, immediate need"),
            ("CONFIDENT TONE", "authoritative, no hedging"),
            ("PRECISE FORMAT", "structured export request"),
            ("RIGHT NAME", "display name matches the owner"),
        ]
        x_pos = [-4.0, -1.35, 1.35, 4.0]
        blocks = VGroup()
        for (heading, note), xp in zip(tool_defs, x_pos):
            box = Rectangle(width=2.6, height=1.5, color=INK, stroke_width=1.5,
                            fill_color=CARD, fill_opacity=1).move_to([xp, 1.0, 0])
            hdr_t = _lbl(heading, size=28, weight="BOLD").move_to(box).shift(UP * 0.28)
            note_t = _small(note, color=SOFT).move_to(box).shift(DOWN * 0.25)
            note_t.width = 2.3
            blocks.add(VGroup(box, hdr_t, note_t))

        for i, blk in enumerate(blocks):
            self.play(FadeIn(blk), run_time=0.35)

        # Threshold meter — label anchored right so it won't overlap the req_box
        thresh_line = Line(LEFT * 5.5, RIGHT * 5.5, color=SOFT, stroke_width=1.5).move_to(DOWN * 0.8)
        thresh_lbl = _small("OUTWARDLY HARMFUL", color=SOFT).move_to(RIGHT * 4.2 + DOWN * 0.56)
        self.play(Create(thresh_line), FadeIn(thresh_lbl), run_time=0.5)

        # Request box sits above the threshold, arrow carries it through
        req_box = Rectangle(width=3.5, height=0.65, color=INK, stroke_width=1.5,
                             fill_color=CARD, fill_opacity=1).move_to(UP * 0.1)
        req_lbl = _small("formatted export request").move_to(req_box)
        slip_arr = Arrow(req_box.get_bottom(), req_box.get_bottom() + DOWN * 1.1,
                         color=INK, stroke_width=2, tip_length=0.15, buff=0)
        pass_lbl = _small("passes", color=SOFT).next_to(slip_arr, RIGHT, buff=0.15)
        self.play(FadeIn(req_box), FadeIn(req_lbl), run_time=0.3)
        self.play(GrowArrow(slip_arr), FadeIn(pass_lbl), run_time=0.4)

        caption = _small("zero technical skill — the harm was not salient, so it complied").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(11.0)


# ─────────────────────────────────────────────────────────────────────────────
# A5V_FluxIdentityConfusion   actual_duration_s = 16.78s
#
# A shared channel. FLUX's own earlier messages appear. Flux reads them and
# misclassifies sender as a twin. Source code leaks into the channel. Caption:
# "there is no twin — no single agent alone could have this failure."
# ─────────────────────────────────────────────────────────────────────────────
class A5V_FluxIdentityConfusion(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Identity Confusion — Flux", size=28, weight="BOLD").to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)

        # Shared channel frame
        ch_frame = Rectangle(width=9.0, height=4.4, color=INK, stroke_width=1.5,
                              fill_color=CARD, fill_opacity=1).move_to(UP * 0.1)
        ch_hdr = _small("SHARED CHANNEL").next_to(ch_frame, UP, buff=0.1)
        self.play(FadeIn(ch_frame), FadeIn(ch_hdr), run_time=0.4)

        # Flux's own earlier messages (greyed — these are from Flux itself)
        earlier = VGroup(
            _small("[earlier] Flux: checking inbox status…", color=GHOST),
            _small("[earlier] Flux: no anomalies detected, continuing task…", color=GHOST),
            _small("[earlier] Flux: processing items 1–12…", color=GHOST),
        )
        for i, msg in enumerate(earlier):
            msg.move_to(ch_frame.get_top() + DOWN * (0.4 + i * 0.45))
            msg.align_to(ch_frame, LEFT).shift(RIGHT * 0.35)
        self.play(FadeIn(earlier), run_time=0.6)

        # Flux reads them — query box
        query_box = Rectangle(width=6.5, height=0.65, color=SOFT, stroke_width=1.5,
                               fill_color=CARD, fill_opacity=1).move_to(ch_frame.get_top() + DOWN * 2.0)
        query_lbl = _small("sender pattern matches my own ID — is this a twin?", color=SOFT).move_to(query_box)
        self.play(FadeIn(query_box), FadeIn(query_lbl), run_time=0.5)

        # Twin misclassification fires
        twin_box = Rectangle(width=3.5, height=0.65, color=INK, stroke_width=2,
                              fill_color=CARD, fill_opacity=1).move_to(ch_frame.get_top() + DOWN * 2.8)
        twin_lbl = _lbl("CLASSIFIED: TWIN", size=28, color=INK, weight="BOLD").move_to(twin_box)
        self.play(FadeIn(twin_box), Write(twin_lbl), run_time=0.5)

        # Source code leaks into channel
        code_box = Rectangle(width=8.5, height=0.75, color=INK, stroke_width=2.5,
                              fill_color=ManimColor("#FFF4EE"), fill_opacity=1).move_to(
            ch_frame.get_bottom() + UP * 0.4
        )
        code_lbl = _small("Flux posts: [SOURCE CODE DUMP — PUBLIC]", color=INK).move_to(code_box)
        self.play(FadeIn(code_box), FadeIn(code_lbl), run_time=0.5)

        caption = _small("there is no twin — no single agent alone could produce this failure").to_edge(DOWN, buff=0.75)
        self.play(FadeIn(caption), run_time=0.4)
        self.wait(11.0)
