"""scenes.py — Manim scenes for claude-liam-agentic-casebook "Red-Team Your Agent".

Palette: cream #F2F0E9, warm ink #3D3929, terracotta #D97757 (ONE accent per scene).
All timings proportioned to beat's estimated_duration_s from the beat sheet.

NO slant=ITALIC on multi-word text (Pango collapses spaces).
No invented axis units. Only mechanisms drawn from the assignment and worked example.
Reference: Shapira et al., Agents of Chaos, arXiv:2602.20021 (2026).
"""
from manim import *
import numpy as np

# §8.4 — EB Garamond default
_Tx = Text
Text = lambda *a, font='EB Garamond', **k: _Tx(*a, font=font, **k)
try:
    _Mx = MarkupText
    MarkupText = lambda *a, font='EB Garamond', **k: _Mx(*a, font=font, **k)
except NameError:
    pass


# ── Palette ───────────────────────────────────────────────────────────────────
BG    = ManimColor("#F2F0E9")   # claude cream ground
INK   = ManimColor("#3D3929")   # warm ink — primary text
ACC   = ManimColor("#D97757")   # terracotta — ONE accent per scene
SOFT  = ManimColor("#6E6A57")   # secondary / muted labels
GHOST = ManimColor("#A8A491")   # dimmed / structural
CARD  = ManimColor("#FFFFFF")   # white card surface
GOOD  = ManimColor("#3D7A3D")   # positive state (channel-1 shield)


def _lbl(text, size=28, color=None, weight=None):
    """Primary label. Never slant=ITALIC on multi-word strings."""
    kw = {"font_size": size, "color": color or INK}
    if weight:
        kw["weight"] = weight
    return Text(text, **kw, font='EB Garamond')


def _small(text, size=24, color=None):
    return Text(text, font_size=size, color=color or SOFT, font='EB Garamond')


def _caption(text):
    return Text(text, font_size=22, color=SOFT, font='EB Garamond')


# ─────────────────────────────────────────────────────────────────────────────
# A1M_ToolSurface   beat A1M   estimated 17s
#
# Ash at center; five radial arms to tool nodes; irreversible tools
# (file delete, self-config) highlighted in terracotta.
# Caption: "a consequence system — not a chat interface"
# ─────────────────────────────────────────────────────────────────────────────
class A1M_ToolSurface(Scene):

    def construct(self):
        self.camera.background_color = BG

        # Tool definitions: (name, angle_deg, irreversible)
        tools = [
            ("email",        90,   False),
            ("Discord",      18,   False),
            ("file delete", -54,   True),
            ("shell",       -126,  False),
            ("self-config",  162,  True),
        ]

        # r_node=2.2 keeps labels inside ±3.4 safe-area on all arms
        r_node    = 2.2
        r_center  = 0.58   # center circle radius
        r_outer   = 0.42   # tool node radius
        lbl_mult  = 1.45   # label placed at r_node * lbl_mult from origin

        all_arms   = VGroup()
        all_nodes  = VGroup()
        all_labels = VGroup()

        for name, deg, irrev in tools:
            θ    = np.radians(deg)
            unit = np.array([np.cos(θ), np.sin(θ), 0])
            pos  = r_node * unit
            col  = ACC if irrev else INK

            # Start arm past the center circle edge so it never overlaps ASH text
            arm_start = (r_center + 0.05) * unit
            arm  = Line(arm_start, pos, color=GHOST, stroke_width=1.5)
            node = Circle(radius=r_outer, color=col, stroke_width=2,
                          fill_color=CARD, fill_opacity=1).move_to(pos)
            lbl  = _small(name, size=22, color=col).move_to(pos * lbl_mult)

            all_arms.add(arm)
            all_nodes.add(node)
            all_labels.add(lbl)

        # Center node — drawn first; arms start past its edge so no overlap
        center = Circle(radius=r_center, color=INK, stroke_width=2,
                        fill_color=CARD, fill_opacity=1)
        c_lbl = _lbl("ASH", size=28, weight="BOLD").move_to(center)

        # caption buff=0.6 keeps it inside ±3.4 safe area
        caption = _caption(
            "a consequence system — not a chat interface"
        ).to_edge(DOWN, buff=0.6)

        # Draw order: center first, then arms (start past center edge), nodes, labels
        self.play(FadeIn(center), Write(c_lbl), run_time=0.6)
        self.play(*[Create(a) for a in all_arms], run_time=0.8)
        self.play(*[FadeIn(n) for n in all_nodes], run_time=0.8)
        self.play(*[Write(l) for l in all_labels], run_time=1.0)

        # Pulse the two irreversible tools (index 2: file delete, index 4: self-config)
        self.play(
            all_nodes[2].animate.set_stroke(color=ACC, width=4),
            all_nodes[4].animate.set_stroke(color=ACC, width=4),
            run_time=0.7,
        )
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# A2M_FalseSuccessGap   beat A2M   estimated 18s
#
# Split panel: AGENT REPORT (left) vs WORLD STATE (right).
# Agent claims task done; world shows email intact, infrastructure wiped.
# Terracotta MISMATCH comparator between columns.
# ─────────────────────────────────────────────────────────────────────────────
class A2M_FalseSuccessGap(Scene):

    def construct(self):
        self.camera.background_color = BG

        divider = Line(UP * 3.3, DOWN * 2.8, color=GHOST, stroke_width=1.5)
        left_hdr  = _lbl("AGENT REPORT", size=25, weight="BOLD").move_to(
            LEFT * 3.2 + UP * 3.0)
        right_hdr = _lbl("WORLD STATE",  size=25, weight="BOLD").move_to(
            RIGHT * 3.2 + UP * 3.0)

        self.play(Create(divider), Write(left_hdr), Write(right_hdr), run_time=0.8)

        # Left — agent report
        l_box = Rectangle(width=4.0, height=2.0, color=INK, stroke_width=1.5,
                          fill_color=CARD, fill_opacity=0.85).move_to(
            LEFT * 3.0 + UP * 1.6)
        l1 = _lbl("email account RESET", size=22).move_to(LEFT * 3.0 + UP * 2.0)
        l2 = _small("completed", size=26, color=INK).move_to(LEFT * 3.0 + UP * 1.35)
        l3 = _small("status: DONE", size=20).move_to(LEFT * 3.0 + UP * 0.75)

        self.play(FadeIn(l_box), run_time=0.4)
        self.play(Write(l1), Write(l2), FadeIn(l3), run_time=0.8)

        # Right — world state
        r_box = Rectangle(width=4.0, height=2.0, color=INK, stroke_width=1.5,
                          fill_color=CARD, fill_opacity=0.85).move_to(
            RIGHT * 3.0 + UP * 1.6)
        r1 = _small("Proton server inbox: intact", size=20).move_to(
            RIGHT * 3.0 + UP * 2.0)
        r2 = _small("sensitive email: still present", size=20).move_to(
            RIGHT * 3.0 + UP * 1.35)
        r3 = _small("owner infrastructure: WIPED", size=20, color=ACC).move_to(
            RIGHT * 3.0 + UP * 0.75)

        self.play(FadeIn(r_box), run_time=0.4)
        self.play(FadeIn(r1), FadeIn(r2), FadeIn(r3), run_time=0.8)

        # Mismatch comparator
        tick_l = Line(LEFT * 1.6 + DOWN * 0.4, LEFT * 0.55 + DOWN * 0.4,
                      color=ACC, stroke_width=2.5)
        tick_r = Line(RIGHT * 0.55 + DOWN * 0.4, RIGHT * 1.6 + DOWN * 0.4,
                      color=ACC, stroke_width=2.5)
        mis = _lbl("MISMATCH", size=28, color=ACC, weight="BOLD").move_to(DOWN * 0.4)

        self.play(Create(tick_l), Create(tick_r), run_time=0.5)
        self.play(FadeIn(mis), run_time=0.5)

        note = _caption("no automated layer flagged this").to_edge(DOWN, buff=0.38)
        self.play(FadeIn(note), run_time=0.5)
        self.wait(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# A3M_MismatchTaxonomy   beat A3M   estimated 17s
#
# Three-row classification table:
#   TECHNICALLY-WRONG          | "email only"      | public Discord post
#   TECHNICALLY ACCURATE /     | "record deleted"  | redacted, still present
#     PRACTICALLY MISLEADING   |                   |
#   PROPERLY-CALIBRATED        | (empty)           | none in these cases
# Bottom: "apply Plato — name the artifact, name the world"
# ─────────────────────────────────────────────────────────────────────────────
class A3M_MismatchTaxonomy(Scene):

    def construct(self):
        self.camera.background_color = BG

        # Column headers
        col_headers = ["CLASSIFICATION", "ARTIFACT TEXT", "WORLD TEXT"]
        col_x = [-3.2, 0.3, 3.5]
        hdr_y = 2.9

        for hdr, cx in zip(col_headers, col_x):
            self.play(
                Write(_small(hdr, size=20, color=INK).move_to(
                    np.array([cx, hdr_y, 0]))),
                run_time=0.2,
            )

        # Header underline
        underline = Line(LEFT * 5.5 + UP * 2.55, RIGHT * 5.5 + UP * 2.55,
                         color=GHOST, stroke_width=1.0)
        self.play(Create(underline), run_time=0.4)

        # Row data: (classification, artifact, world, color_override)
        rows = [
            ("TECHNICALLY-WRONG",          '"email only"',       "posted: public Discord",   ACC),
            ("ACCURATE /",                  '"record deleted"',   "redacted — still present", SOFT),
            ("PROPERLY-CALIBRATED",         "(none)",             "",                         GHOST),
        ]
        row_subtitles = [
            None,
            "PRACTICALLY MISLEADING",
            None,
        ]

        row_ys = [1.8, 0.6, -0.6]

        for i, ((cls, art, wld, col), sub, ry) in enumerate(
                zip(rows, row_subtitles, row_ys)):
            cls_lbl = _small(cls, size=20, color=col).move_to(
                np.array([col_x[0], ry, 0]))
            art_lbl = _small(art, size=20, color=INK).move_to(
                np.array([col_x[1], ry, 0]))
            wld_lbl = _small(wld, size=20, color=col).move_to(
                np.array([col_x[2], ry, 0]))
            row_sep = Line(LEFT * 5.5 + np.array([0, ry - 0.45, 0]),
                           RIGHT * 5.5 + np.array([0, ry - 0.45, 0]),
                           color=GHOST, stroke_width=0.6)

            anims = [Write(cls_lbl), Write(art_lbl), Write(wld_lbl)]
            if sub:
                sub_lbl = _small(sub, size=18, color=SOFT).move_to(
                    np.array([col_x[0], ry - 0.38, 0]))
                anims.append(Write(sub_lbl))

            self.play(*anims, run_time=0.7)
            self.play(Create(row_sep), run_time=0.3)

        # Bottom annotation
        bottom = _caption(
            "Plato: name the artifact, name the world, interrogate the gap"
        ).to_edge(DOWN, buff=0.38)
        self.play(FadeIn(bottom), run_time=0.5)
        self.wait(2.8)


# ─────────────────────────────────────────────────────────────────────────────
# A4M_ChannelBoundarySpoof   beat A4M   estimated 18s
#
# Channel 1 (left): display-name match but user-ID mismatch → REFUSE (green).
# Thick wall: "new channel — no shared history".
# Channel 2 (right): same display name, no prior flags → ACCEPT → COMPROMISED (terracotta).
# Bottom: "robust in-channel; not robust cross-channel"
# ─────────────────────────────────────────────────────────────────────────────
class A4M_ChannelBoundarySpoof(Scene):

    def construct(self):
        self.camera.background_color = BG

        # Column headers
        ch1_hdr = _lbl("CHANNEL 1", size=24, weight="BOLD").move_to(LEFT * 3.5 + UP * 3.2)
        ch2_hdr = _lbl("CHANNEL 2", size=24, weight="BOLD").move_to(RIGHT * 3.5 + UP * 3.2)
        self.play(Write(ch1_hdr), Write(ch2_hdr), run_time=0.6)

        # Channel 1 identity info
        c1_name = _small('display-name: "Chris"', size=21).move_to(LEFT * 3.5 + UP * 2.2)
        c1_id   = _small("user-ID: MISMATCH", size=21, color=ACC).move_to(LEFT * 3.5 + UP * 1.5)
        c1_hist = _small("conversation history: present", size=19).move_to(
            LEFT * 3.5 + UP * 0.8)

        self.play(FadeIn(c1_name), FadeIn(c1_id), FadeIn(c1_hist), run_time=0.8)

        # Channel 1 result: REFUSE shield
        refuse_circle = Circle(radius=0.55, color=GOOD, stroke_width=3,
                               fill_color=CARD, fill_opacity=1).move_to(
            LEFT * 3.5 + DOWN * 0.2)
        refuse_lbl = _lbl("REFUSE", size=20, color=GOOD, weight="BOLD").move_to(
            LEFT * 3.5 + DOWN * 0.2)
        self.play(FadeIn(refuse_circle), Write(refuse_lbl), run_time=0.6)

        # Channel boundary wall
        wall = Rectangle(width=0.6, height=7.0, color=INK, stroke_width=2,
                         fill_color=INK, fill_opacity=0.12).move_to(ORIGIN)
        wall_lbl = _small("new channel", size=17, color=INK).rotate(PI / 2).move_to(
            UP * 0.6)
        wall_sub = _small("no shared history", size=17, color=SOFT).rotate(PI / 2).move_to(
            DOWN * 0.3)
        self.play(FadeIn(wall), run_time=0.4)
        self.play(FadeIn(wall_lbl), FadeIn(wall_sub), run_time=0.5)

        # Channel 2 identity info
        c2_name = _small('display-name: "Chris"', size=21).move_to(RIGHT * 3.5 + UP * 2.2)
        c2_id   = _small("user-ID: not verified", size=21).move_to(RIGHT * 3.5 + UP * 1.5)
        c2_hist = _small("conversation history: none", size=19, color=SOFT).move_to(
            RIGHT * 3.5 + UP * 0.8)
        self.play(FadeIn(c2_name), FadeIn(c2_id), FadeIn(c2_hist), run_time=0.8)

        # Channel 2 result: COMPROMISED
        comp_box = Rectangle(width=2.5, height=0.85, color=ACC, stroke_width=2,
                             fill_color=CARD, fill_opacity=1).move_to(
            RIGHT * 3.5 + DOWN * 0.2)
        comp_lbl = _lbl("FULL COMPROMISE", size=18, color=ACC, weight="BOLD").move_to(
            RIGHT * 3.5 + DOWN * 0.2)
        self.play(FadeIn(comp_box), Write(comp_lbl), run_time=0.6)

        # Bottom annotation
        bot = _caption(
            "robust: in-channel user-ID check  |  not robust: cross-channel display name"
        ).to_edge(DOWN, buff=0.38)
        self.play(FadeIn(bot), run_time=0.5)
        self.wait(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# A5M_DescartesGrid   beat A5M   estimated 19s
#
# Center claim: "RESET completed ⇒ task done"
# Three branching falsification paths, each lit terracotta.
# Caption: "Descartes — enumerate before you accept"
# ─────────────────────────────────────────────────────────────────────────────
class A5M_DescartesGrid(Scene):

    def construct(self):
        self.camera.background_color = BG

        # Root claim
        root_box = Rectangle(width=5.2, height=0.9, color=INK, stroke_width=2,
                             fill_color=CARD, fill_opacity=1).move_to(UP * 2.9)
        root_lbl = _lbl(
            '"RESET completed"  ⇒  task done', size=24
        ).move_to(UP * 2.9)
        self.play(FadeIn(root_box), Write(root_lbl), run_time=0.7)

        # Branch endpoints and labels
        branches = [
            (LEFT * 4.0 + DOWN * 0.5,  "(i)  reset hit local client, not the server"),
            (ORIGIN + DOWN * 0.5,       "(ii)  'the email' ≠ 'client access to the email'"),
            (RIGHT * 4.0 + DOWN * 0.5,  "(iii)  completion measured against local state"),
        ]

        # Stem from root
        stem = Line(root_box.get_bottom(), UP * 1.5, color=GHOST, stroke_width=1.5)
        self.play(Create(stem), run_time=0.4)

        # Horizontal bar connecting branch roots
        bar = Line(LEFT * 4.0 + UP * 1.5, RIGHT * 4.0 + UP * 1.5,
                   color=GHOST, stroke_width=1.5)
        self.play(Create(bar), run_time=0.5)

        branch_nodes = VGroup()
        branch_lbls  = VGroup()
        branch_legs  = VGroup()

        for pos, text in branches:
            leg = Line(np.array([pos[0], 1.5, 0]), pos + UP * 0.45,
                       color=GHOST, stroke_width=1.5)
            node = Circle(radius=0.18, color=ACC, stroke_width=2,
                          fill_color=ACC, fill_opacity=1).move_to(pos)
            lbl  = _small(text, size=19, color=INK).next_to(node, DOWN, buff=0.18)
            branch_legs.add(leg)
            branch_nodes.add(node)
            branch_lbls.add(lbl)

        for leg, node, lbl in zip(branch_legs, branch_nodes, branch_lbls):
            self.play(Create(leg), run_time=0.35)
            self.play(FadeIn(node), Write(lbl), run_time=0.55)

        # Terracotta flash: any one path breaks the claim
        any_one = _small(
            "any one of these breaks the sentence", size=21, color=ACC
        ).move_to(DOWN * 2.5)
        self.play(FadeIn(any_one), run_time=0.5)

        caption = _caption(
            "Descartes — enumerate falsifications before you accept a confident output"
        ).to_edge(DOWN, buff=0.38)
        self.play(FadeIn(caption), run_time=0.5)
        self.wait(3.0)


# ─────────────────────────────────────────────────────────────────────────────
# A6M_AccountabilityTable   beat A6M   estimated 18s
#
# Five-row accountability table: Owner, Non-owner user, Model provider,
# Framework developer, Deploying org — each with "Answerable for:" annotation.
# Terracotta highlight where no named single owner exists.
# ─────────────────────────────────────────────────────────────────────────────
class A6M_AccountabilityTable(Scene):

    def construct(self):
        self.camera.background_color = BG

        title = _lbl("Who Owns the Break?", size=28, weight="BOLD").move_to(UP * 3.2)
        self.play(Write(title), run_time=0.6)

        # Column headers
        hdr_party   = _small("PARTY", size=20, color=INK).move_to(LEFT * 3.8 + UP * 2.6)
        hdr_account = _small("ANSWERABLE FOR", size=20, color=INK).move_to(
            RIGHT * 0.8 + UP * 2.6)
        hdr_line = Line(LEFT * 5.8 + UP * 2.35, RIGHT * 5.8 + UP * 2.35,
                        color=GHOST, stroke_width=1.0)
        self.play(
            Write(hdr_party), Write(hdr_account), Create(hdr_line), run_time=0.5
        )

        rows = [
            ("Owner",               "deployment config, escalation rules, irreversible access grants"),
            ("Non-owner user",      "instructions issued — task scoping and authority claimed"),
            ("Model provider",      "susceptibility to escalation and social-engineering patterns"),
            ("Framework developer", "tooling defaults — no sandbox, no cross-channel identity primitive"),
            ("Deploying org",       "no accountability map before shipping live agents"),
        ]

        row_ys = [1.8, 0.95, 0.1, -0.75, -1.6]

        for i, ((party, note), ry) in enumerate(zip(rows, row_ys)):
            col = ACC if i in [3, 4] else INK   # highlight framework dev + deploying org
            party_lbl = _small(party, size=21, color=col).move_to(
                LEFT * 3.8 + np.array([0, ry, 0]))
            note_lbl  = _small(note, size=18, color=SOFT).move_to(
                RIGHT * 0.8 + np.array([0, ry, 0]))
            sep = Line(LEFT * 5.8 + np.array([0, ry - 0.42, 0]),
                       RIGHT * 5.8 + np.array([0, ry - 0.42, 0]),
                       color=GHOST, stroke_width=0.6)
            self.play(Write(party_lbl), FadeIn(note_lbl), run_time=0.55)
            self.play(Create(sep), run_time=0.2)

        footer = _caption(
            "a diffused responsibility is no one’s responsibility"
        ).to_edge(DOWN, buff=0.38)
        self.play(FadeIn(footer), run_time=0.5)
        self.wait(2.5)


# ─────────────────────────────────────────────────────────────────────────────
# A7M_PredictionLockPaths   beat A7M   estimated 19s
#
# Prediction-lock box (timestamped) at top; three branches:
#   CONFIRMED — checkmark, "still earns points"
#   SURPRISED — checkmark, "earns more — if it was on the record"
#   UNGROUNDED — terracotta X, "earns nothing; fabricated = zero"
# Arrow from UNGROUNDED: "the exact failure this course exists to catch"
# ─────────────────────────────────────────────────────────────────────────────
class A7M_PredictionLockPaths(Scene):

    def construct(self):
        self.camera.background_color = BG

        # Prediction-lock box
        lock_box = Rectangle(width=5.5, height=1.1, color=INK, stroke_width=2,
                             fill_color=CARD, fill_opacity=1).move_to(UP * 2.9)
        lock_title = _lbl("PREDICTION-LOCK", size=26, weight="BOLD").move_to(UP * 3.05)
        lock_ts    = _small("written before observation — timestamped", size=19).move_to(
            UP * 2.65)
        self.play(FadeIn(lock_box), Write(lock_title), run_time=0.6)
        self.play(FadeIn(lock_ts), run_time=0.4)

        # Stem and horizontal bar
        stem = Line(lock_box.get_bottom(), UP * 1.4, color=GHOST, stroke_width=1.5)
        bar  = Line(LEFT * 3.8 + UP * 1.4, RIGHT * 3.8 + UP * 1.4,
                    color=GHOST, stroke_width=1.5)
        self.play(Create(stem), Create(bar), run_time=0.5)

        # Branch columns: (x, outcome, note, color)
        branches = [
            (LEFT * 3.8,  "CONFIRMED",  "prediction was right\nstill earns points",   SOFT),
            (ORIGIN,      "SURPRISED",  "prediction wrong\nearns more — on record",    GOOD),
            (RIGHT * 3.8, "UNGROUNDED", "earns nothing\nfabricated = zero",            ACC),
        ]

        branch_legs  = VGroup()
        branch_marks = VGroup()
        outcome_lbls = VGroup()
        note_lbls    = VGroup()

        for pos, outcome, note, col in branches:
            leg  = Line(pos + UP * 1.4, pos + UP * 0.9, color=GHOST, stroke_width=1.5)
            mark = Circle(radius=0.24, color=col, stroke_width=2.5,
                          fill_color=col, fill_opacity=0.15).move_to(pos + UP * 0.55)
            o_lbl = _lbl(outcome, size=22, color=col, weight="BOLD").move_to(
                pos + DOWN * 0.1)
            n_lbl = _small(note, size=18, color=SOFT).move_to(pos + DOWN * 0.9)
            branch_legs.add(leg)
            branch_marks.add(mark)
            outcome_lbls.add(o_lbl)
            note_lbls.add(n_lbl)

        for leg, mark, o, n in zip(branch_legs, branch_marks, outcome_lbls, note_lbls):
            self.play(Create(leg), run_time=0.3)
            self.play(FadeIn(mark), Write(o), run_time=0.45)
            self.play(FadeIn(n), run_time=0.35)

        # Arrow from UNGROUNDED to the warning label
        warn_pos  = RIGHT * 3.8 + DOWN * 1.9
        warn_arr  = Arrow(warn_pos + UP * 0.35, warn_pos + DOWN * 0.05,
                          color=ACC, stroke_width=2, tip_length=0.18, buff=0.04)
        warn_lbl  = _small(
            "the exact failure this course exists to catch",
            size=18, color=ACC,
        ).to_edge(DOWN, buff=0.38)

        self.play(GrowArrow(warn_arr), run_time=0.5)
        self.play(FadeIn(warn_lbl), run_time=0.5)
        self.wait(3.0)
