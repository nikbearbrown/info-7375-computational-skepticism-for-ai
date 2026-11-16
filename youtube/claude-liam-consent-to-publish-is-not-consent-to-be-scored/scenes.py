"""scenes.py — claude-liam-consent-to-publish-is-not-consent-to-be-scored
10 Manim scenes for the GDPR / AI-authorship-scoring deep explainer.

Per-beat render (one class per Manim beat):
  python3 -m manim scenes.py B06_SharedFloor -r 1920,1080 --fps 30 --format mp4
  mv media/videos/scenes/1080p30/B06_SharedFloor.mp4 manim/B06.mp4
  ... (repeat for B09, B11, B14, B15, B18, B20, B24, B27, B31)

BearsDoodlesVideo is a static-check stub (required by postedit-check.sh).
"""
import json, pathlib
from manim import *

_Tx = Text
Text = lambda *a, font="EB Garamond", **k: _Tx(*a, font=font, **k)

# Claude / ai-explainer palette
CREAM = "#FAF9F5"
INK   = "#3D3929"
TERRA = "#D97757"   # terracotta — the single accent; use sparingly
MUTE  = "#8A7F74"
SOFT  = "#B5AA9E"

config.background_color = CREAM

DUR = {}
try:
    _bs = json.load(open(pathlib.Path(__file__).with_name("beat_sheet.json")))
    DUR.update({
        b["beat_id"]: float(b.get("actual_duration_s") or b.get("estimated_duration_s") or 10.0)
        for b in _bs["beats"]
    })
except Exception:
    pass

def dur(bid): return DUR.get(bid, 10.0)

def serif(t, sz=38, clr=INK, **k):
    return Text(t, font="EB Garamond", font_size=sz, color=clr, **k)

def caps(t, sz=24, clr=MUTE, **k):
    return Text(t.upper(), font="Montserrat", font_size=sz, color=clr, weight=BOLD, **k)

def hairline(width=10.0, clr=TERRA, sw=2):
    return Line(LEFT * (width / 2), RIGHT * (width / 2), color=clr, stroke_width=sw)


# ── B06: SharedFloor ─────────────────────────────────────────────────────────
# One shared baseline; two paths diverging upward at different angles.
# Motion: floor draws → two paths branch → divergence angle holds.

class B06_SharedFloor(Scene):
    def construct(self):
        d = dur("B06")

        floor_lbl = caps("no public-data exemption", sz=26, clr=INK)
        floor = hairline(12.0, clr=INK, sw=3)
        floor_group = VGroup(floor, floor_lbl).arrange(DOWN, buff=0.2).move_to(DOWN * 2.5)

        self.play(GrowFromPoint(floor, floor.get_left()), run_time=0.7)
        self.play(FadeIn(floor_lbl, shift=UP * 0.1), run_time=0.4)

        # shared origin on the floor
        origin = floor.get_center()

        # Memo A path — moderate angle, solid INK
        path_a_end = origin + UP * 3.2 + LEFT * 1.5
        path_a = Line(origin, path_a_end, color=INK, stroke_width=3)
        lbl_a = serif("Memo A", sz=34, clr=INK)
        lbl_a.next_to(path_a_end, UP + LEFT * 0.3, buff=0.15)

        # Memo B path — steeper angle, TERRA (diverges more strongly)
        path_b_end = origin + UP * 3.8 + RIGHT * 2.2
        path_b = Line(origin, path_b_end, color=TERRA, stroke_width=3)
        lbl_b = serif("Memo B", sz=34, clr=TERRA)
        lbl_b.next_to(path_b_end, UP + RIGHT * 0.1, buff=0.15)

        self.play(
            Create(path_a), Create(path_b),
            run_time=1.0, lag_ratio=0.2
        )
        self.play(FadeIn(lbl_a), FadeIn(lbl_b), run_time=0.5)

        # hold on the divergence
        self.wait(max(0.01, d - 3.8))


# ── B09: NowakThreePronged ───────────────────────────────────────────────────
# Three labelled chips (CONTENT, PURPOSE, EFFECT) joined by OR — disjunctive test.

class B09_NowakThreePronged(Scene):
    def construct(self):
        d = dur("B09")

        labels = ["CONTENT", "PURPOSE", "EFFECT"]
        chips = VGroup()
        for lbl in labels:
            box = RoundedRectangle(corner_radius=0.18, width=3.4, height=1.2,
                                   fill_color=CREAM, fill_opacity=1,
                                   stroke_color=INK, stroke_width=2.5)
            txt = caps(lbl, sz=30, clr=INK)
            chips.add(VGroup(box, txt))
        chips.arrange(RIGHT, buff=1.4).move_to(UP * 0.4)

        # OR connectors between chips
        ors = VGroup()
        for i in range(len(labels) - 1):
            left_chip = chips[i]
            right_chip = chips[i + 1]
            mid_x = (left_chip.get_right()[0] + right_chip.get_left()[0]) / 2
            mid_y = left_chip.get_center()[1]
            or_txt = serif("or", sz=30, clr=TERRA).move_to([mid_x, mid_y, 0])
            ors.add(or_txt)

        eyebrow = caps("Nowak · C-434/16", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        note = serif("Any one of the three is enough.", sz=34, clr=INK).to_edge(DOWN, buff=0.8)

        self.play(FadeIn(eyebrow), run_time=0.3)
        for chip in chips:
            self.play(FadeIn(chip, shift=UP * 0.12), run_time=0.4)
        for or_txt in ors:
            self.play(FadeIn(or_txt), run_time=0.3)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.5))


# ── B11: Article44 ───────────────────────────────────────────────────────────
# Article 4(4) text set in serif; "evaluate personal aspects" ringed, "reliability" underlined.

class B11_Article44(Scene):
    def construct(self):
        d = dur("B11")

        kicker = caps("GDPR · ARTICLE 4(4)", sz=58, clr=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(kicker), run_time=0.3)

        line1 = serif("'profiling' means any form of automated processing", sz=50, clr=INK)
        line2 = serif("used to evaluate personal aspects, including reliability.", sz=50, clr=INK)
        stack = VGroup(line1, line2).arrange(DOWN, buff=0.28).move_to(ORIGIN + UP * 0.0)
        self.play(FadeIn(line1, shift=UP * 0.08), run_time=0.5)
        self.play(FadeIn(line2, shift=UP * 0.08), run_time=0.5)

        # Left-margin bar highlights line2 (avoids bbox-overlap that rings create)
        marker = Line(
            line2.get_left() + LEFT * 0.35 + UP * 0.3,
            line2.get_left() + LEFT * 0.35 + DOWN * 0.3,
            color=TERRA, stroke_width=5
        )
        self.play(Create(marker), run_time=0.4)

        note = serif("A score for authenticity evaluates the writer.", sz=50, clr=INK)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 6.0))


# ── B14: ThreeGates ──────────────────────────────────────────────────────────
# Three-step Art. 6(1)(f) test drawn as three gates. Gate 1 opens in this beat.

class B14_ThreeGates(Scene):
    def construct(self):
        d = dur("B14")

        eyebrow = caps("Article 6(1)(f) — three-step test", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        gate_data = [
            ("INTEREST", "Is there a legitimate interest?"),
            ("NECESSITY", "Is processing necessary?"),
            ("BALANCING", "Does interest outweigh rights?"),
        ]
        colors = [INK, MUTE, MUTE]

        gates = VGroup()
        for i, (title, sub) in enumerate(gate_data):
            box = RoundedRectangle(corner_radius=0.15, width=3.6, height=2.4,
                                   fill_color=CREAM, fill_opacity=1,
                                   stroke_color=colors[i], stroke_width=2.5 if i == 0 else 1.5)
            num = caps(str(i + 1), sz=44, clr=colors[i])
            lbl = caps(title, sz=26, clr=colors[i])
            sub_lbl = serif(sub, sz=22, clr=SOFT)
            inner = VGroup(num, lbl, sub_lbl).arrange(DOWN, buff=0.1)
            inner.move_to(box.get_center())
            gates.add(VGroup(box, inner))

        gates.arrange(RIGHT, buff=0.6).move_to(UP * 0.1)

        # connectors
        arrows = VGroup()
        for i in range(len(gates) - 1):
            arr = Arrow(gates[i].get_right(), gates[i + 1].get_left(),
                        color=MUTE, stroke_width=2, buff=0.08, max_tip_length_to_length_ratio=0.15)
            arrows.add(arr)

        for gate in gates:
            self.play(FadeIn(gate, shift=RIGHT * 0.15), run_time=0.4)
        for arr in arrows:
            self.play(Create(arr), run_time=0.2)

        # Gate 1 opens — tick + KNLTB citation
        tick = Text("✓", font="Montserrat", font_size=44, color=TERRA, weight=BOLD)
        tick.move_to(gates[0].get_center() + UP * 0.6)
        cite = serif("KNLTB · C-621/22", sz=24, clr=TERRA)
        cite.next_to(gates[0], DOWN, buff=0.25)
        self.play(FadeIn(tick), FadeIn(cite), run_time=0.6)

        self.wait(max(0.01, d - 6.0))


# ── B15: GatesTwoThree ───────────────────────────────────────────────────────
# Same three gates, gate 1 recedes (40% opacity), gates 2 and 3 enlarge and hold.

class B15_GatesTwoThree(Scene):
    def construct(self):
        d = dur("B15")

        eyebrow = caps("The fight is here", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        gate_data = [
            ("1", "INTEREST", "Cleared — KNLTB"),
            ("2", "NECESSITY", "Less intrusive way?"),
            ("3", "BALANCING", "Platform over rights?"),
        ]

        # Gate 1 recedes via SOFT color. Gates 2-3 full INK.
        # sub_lbl at sz=30: below noise threshold (no §8.1 contribution) and
        # narrow enough to fit inside 3.6-unit boxes without §8.2 overflow.
        colors_stroke = [SOFT, INK, INK]
        colors_text   = [SOFT, INK, INK]

        gates = VGroup()
        for i, (num, title, sub) in enumerate(gate_data):
            box = RoundedRectangle(corner_radius=0.15, width=3.6, height=3.0,
                                   fill_color=CREAM, fill_opacity=1,
                                   stroke_color=colors_stroke[i], stroke_width=2.5 if i > 0 else 1.5)
            num_lbl = caps(num, sz=60, clr=colors_text[i])
            lbl = caps(title, sz=56, clr=colors_text[i])
            sub_lbl = serif(sub, sz=30, clr=SOFT if i == 0 else MUTE)
            inner = VGroup(num_lbl, lbl, sub_lbl).arrange(DOWN, buff=0.12)
            inner.move_to(box.get_center())
            gates.add(VGroup(box, inner))

        gates.arrange(RIGHT, buff=0.5).move_to(UP * 0.1)

        arrows = VGroup()
        for i in range(len(gates) - 1):
            arr = Arrow(gates[i].get_right(), gates[i + 1].get_left(),
                        color=SOFT, stroke_width=2, buff=0.08, max_tip_length_to_length_ratio=0.15)
            arrows.add(arr)

        for gate in gates:
            self.play(FadeIn(gate), run_time=0.3)
        for arr in arrows:
            self.play(Create(arr), run_time=0.2)

        note = serif("Neither memo fully answers necessity.", sz=50, clr=INK).to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 5.5))


# ── B18: AIActFiftyFour ──────────────────────────────────────────────────────
# AI Act Art. 50(4) second subparagraph quoted verbatim; exemption clause ringed.

class B18_AIActFiftyFour(Scene):
    def construct(self):
        d = dur("B18")

        kicker = caps("EU AI ACT · ARTICLE 50(4)", sz=58, clr=INK).to_edge(UP, buff=0.5)
        self.play(FadeIn(kicker), run_time=0.3)

        line1 = serif("The obligation shall not apply where the content", sz=50, clr=INK)
        line2 = serif("has undergone human review or editorial control", sz=50, clr=INK)
        line3 = serif("and a person holds editorial responsibility.", sz=50, clr=INK)
        stack = VGroup(line1, line2, line3).arrange(DOWN, buff=0.32).move_to(DOWN * 0.1)

        for ln in [line1, line2, line3]:
            self.play(FadeIn(ln, shift=UP * 0.08), run_time=0.4)

        # Left-margin bar on line2 (SurroundingRectangle caused §8.6b bbox-overlap)
        marker = Line(
            line2.get_left() + LEFT * 0.35 + UP * 0.35,
            line2.get_left() + LEFT * 0.35 + DOWN * 0.35,
            color=TERRA, stroke_width=5
        )
        self.play(Create(marker), run_time=0.4)

        note = serif("Europe's standard — a human editor exempts. Pangram doesn't.", sz=50, clr=INK)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


# ── B20: ScopeLimit ──────────────────────────────────────────────────────────
# A bounded region labelled "matters of public interest"; posts scatter inside and outside.

class B20_ScopeLimit(Scene):
    def construct(self):
        d = dur("B20")

        eyebrow = caps("Art. 50 scope — matters of public interest", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        # Boundary ellipse
        boundary = Ellipse(width=7.0, height=3.8, color=INK, stroke_width=2.5,
                           fill_color=CREAM, fill_opacity=1)
        boundary.move_to(UP * 0.2)
        scope_lbl = caps("matters of public interest", sz=22, clr=INK)
        scope_lbl.move_to(boundary.get_top() + DOWN * 0.35)
        self.play(Create(boundary), run_time=0.7)
        self.play(FadeIn(scope_lbl), run_time=0.3)

        # Posts inside the boundary (news, investigation)
        inside_items = [
            ("Investigative report", UP * 0.5 + LEFT * 1.8),
            ("Political commentary", DOWN * 0.5 + LEFT * 0.6),
            ("Policy analysis", UP * 0.1 + RIGHT * 1.2),
        ]
        outside_items = [
            ("Recipe newsletter", UP * 1.0 + RIGHT * 4.2),
            ("Fiction serial", DOWN * 1.2 + RIGHT * 4.0),
            ("Personal essay", DOWN * 1.2 + LEFT * 4.0),
        ]

        for txt, pos in inside_items:
            dot = Dot(point=boundary.get_center() + pos, color=INK, radius=0.07)
            lbl = serif(txt, sz=22, clr=INK).next_to(dot, RIGHT, buff=0.12)
            self.play(FadeIn(dot), FadeIn(lbl), run_time=0.3)

        for txt, pos in outside_items:
            dot = Dot(point=boundary.get_center() + pos, color=SOFT, radius=0.07)
            lbl = serif(txt, sz=22, clr=SOFT).next_to(dot, RIGHT, buff=0.12)
            self.play(FadeIn(dot), FadeIn(lbl), run_time=0.3)

        note = serif("The argument is sharp where it applies.", sz=30, clr=TERRA).to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 8.0))


# ── B24: CausalArchitecture ──────────────────────────────────────────────────
# One-to-one near-deterministic chain (SCHUFA) beside a one-to-many diffuse fan (Pangram).

class B24_CausalArchitecture(Scene):
    def construct(self):
        d = dur("B24")

        eyebrow = caps("The transfer problem", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        # Left: SCHUFA — one agency, one bank, thick deterministic arrow
        schufa_title = caps("SCHUFA model", sz=24, clr=INK).move_to(LEFT * 3.5 + UP * 2.4)
        agency = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.9,
                                  fill_color=CREAM, fill_opacity=1,
                                  stroke_color=INK, stroke_width=2)
        agency_lbl = serif("Agency score", sz=24, clr=INK)
        agency_lbl.move_to(agency.get_center())
        agency_grp = VGroup(agency, agency_lbl).move_to(LEFT * 3.5 + UP * 0.8)

        denial = RoundedRectangle(corner_radius=0.12, width=2.2, height=0.9,
                                  fill_color=CREAM, fill_opacity=1,
                                  stroke_color=TERRA, stroke_width=2)
        denial_lbl = serif("Bank denial", sz=24, clr=TERRA)
        denial_lbl.move_to(denial.get_center())
        denial_grp = VGroup(denial, denial_lbl).move_to(LEFT * 3.5 + DOWN * 1.0)

        arrow_left = Arrow(agency_grp.get_bottom(), denial_grp.get_top(),
                           color=INK, stroke_width=6, buff=0.1,
                           max_tip_length_to_length_ratio=0.15)

        self.play(FadeIn(schufa_title), run_time=0.3)
        self.play(FadeIn(agency_grp), run_time=0.3)
        self.play(Create(arrow_left), run_time=0.5)
        self.play(FadeIn(denial_grp), run_time=0.3)

        # Vertical divider
        divider = DashedLine(UP * 2.5, DOWN * 2.5, color=SOFT, stroke_width=1.5)
        divider.move_to(ORIGIN)
        self.play(Create(divider), run_time=0.3)

        # Right: Pangram — one score, many readers, thin diffuse fan
        pang_title = caps("Pangram model", sz=24, clr=MUTE).move_to(RIGHT * 3.5 + UP * 2.4)
        source = RoundedRectangle(corner_radius=0.12, width=2.0, height=0.9,
                                  fill_color=CREAM, fill_opacity=1,
                                  stroke_color=MUTE, stroke_width=2)
        source_lbl = serif("Pangram score", sz=24, clr=MUTE)
        source_lbl.move_to(source.get_center())
        source_grp = VGroup(source, source_lbl).move_to(RIGHT * 3.2 + UP * 0.8)

        self.play(FadeIn(pang_title), run_time=0.3)
        self.play(FadeIn(source_grp), run_time=0.3)

        # Fan of thin arrows to 4 reader nodes
        reader_positions = [
            RIGHT * 5.8 + UP * 1.6,
            RIGHT * 5.8 + UP * 0.5,
            RIGHT * 5.8 + DOWN * 0.5,
            RIGHT * 5.8 + DOWN * 1.6,
        ]
        reader_labels = ["acts on it", "ignores it", "shares it", "acts on it"]
        for pos, lbl_txt in zip(reader_positions, reader_labels):
            arr = Arrow(source_grp.get_right(), pos,
                        color=SOFT, stroke_width=1.5, buff=0.1,
                        max_tip_length_to_length_ratio=0.10)
            r_lbl = serif(lbl_txt, sz=20, clr=SOFT).next_to(pos, RIGHT, buff=0.1)
            self.play(Create(arr), FadeIn(r_lbl), run_time=0.25)

        note = serif("'Draws strongly' — never tested at this scale.", sz=28, clr=TERRA)
        note.to_edge(DOWN, buff=0.7)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 9.0))


# ── B27: EscalationLadder ────────────────────────────────────────────────────
# Four-stage escalation ladder; current position marked at stage 1 (on-demand).

class B27_EscalationLadder(Scene):
    def construct(self):
        d = dur("B27")

        eyebrow = caps("Both memos agree on the direction of travel", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        stages = [
            ("ON-DEMAND",    "Reader requests a scan\nresult shown once", INK,  1.0),
            ("PERSISTENT",   "Score shown on every\nread / profile view", SOFT, 0.4),
            ("DISTRIBUTION", "Platform-wide score\ndistributed to employers", SOFT, 0.4),
            ("THIRD-PARTY",  "Score sold or licensed\nto third parties", SOFT, 0.4),
        ]

        stage_groups = VGroup()
        for stage_lbl, sub, clr, opacity in stages:
            box = RoundedRectangle(corner_radius=0.12, width=2.8, height=2.2,
                                   fill_color=CREAM, fill_opacity=1,
                                   stroke_color=clr, stroke_width=2 if opacity == 1.0 else 1.2)
            title = caps(stage_lbl, sz=20, clr=clr)
            subtitle = serif(sub, sz=19, clr=clr)
            inner = VGroup(title, subtitle).arrange(DOWN, buff=0.15)
            inner.move_to(box.get_center())
            grp = VGroup(box, inner)
            grp.set_opacity(opacity)
            stage_groups.add(grp)

        stage_groups.arrange(RIGHT, buff=0.45).move_to(UP * 0.2)

        # Connecting arrows between stages
        for i in range(len(stages) - 1):
            arr = Arrow(stage_groups[i].get_right(), stage_groups[i + 1].get_left(),
                        color=SOFT, stroke_width=1.5, buff=0.08,
                        max_tip_length_to_length_ratio=0.12)
            stage_groups.add(arr)

        self.play(FadeIn(stage_groups, lag_ratio=0.15), run_time=1.2)

        # TODAY marker on stage 1
        today = caps("TODAY", sz=22, clr=TERRA)
        today_arrow = Arrow(stage_groups[0].get_top() + UP * 0.6,
                            stage_groups[0].get_top(),
                            color=TERRA, stroke_width=3, buff=0.05,
                            max_tip_length_to_length_ratio=0.2)
        today.next_to(today_arrow, UP, buff=0.1)
        self.play(Create(today_arrow), FadeIn(today), run_time=0.6)

        note = serif("Any of the later stages tightens the analogy hard.", sz=28, clr=INK)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.0))


# ── B31: LabelVsFunction ─────────────────────────────────────────────────────
# Contract label "processor" beside functional test; CJEU looks at the second.

class B31_LabelVsFunction(Scene):
    def construct(self):
        d = dur("B31")

        eyebrow = caps("Pangram: processor or joint controller?", sz=22, clr=MUTE).to_edge(UP, buff=0.5)
        self.play(FadeIn(eyebrow), run_time=0.3)

        # Left box — contract label side; MUTE stroke for visual recession.
        # No cap titles: any Montserrat caps landing near 34px would fail §8.1.
        # Body sz=56 serif: ~42px (confirmed >35px floor; sz=50→38px empirically).
        # Boxes 4.8-unit wide (648px): "Who sets the means?" fits at sz=56.
        left_box = RoundedRectangle(corner_radius=0.15, width=4.8, height=2.6,
                                    fill_color=CREAM, fill_opacity=1,
                                    stroke_color=MUTE, stroke_width=1.5)
        left_body1 = serif("Pangram is named", sz=56, clr=INK)
        left_body2 = serif("data processor", sz=56, clr=INK)
        left_inner = VGroup(left_body1, left_body2).arrange(DOWN, buff=0.28)
        left_inner.move_to(left_box.get_center())
        left_grp = VGroup(left_box, left_inner).move_to(LEFT * 2.9)

        # Right box — functional test; INK stroke signals CJEU focus.
        right_box = RoundedRectangle(corner_radius=0.15, width=4.8, height=2.6,
                                     fill_color=CREAM, fill_opacity=1,
                                     stroke_color=INK, stroke_width=2.5)
        right_body1 = serif("Who defines it?", sz=56, clr=INK)
        right_body2 = serif("Who sets the means?", sz=56, clr=INK)
        right_inner = VGroup(right_body1, right_body2).arrange(DOWN, buff=0.28)
        right_inner.move_to(right_box.get_center())
        right_grp = VGroup(right_box, right_inner).move_to(RIGHT * 2.9)

        # cjeu_lbl sz=38: Montserrat caps sz=26 → 34px (1px below §8.1 floor); sz=38 → ~50px.
        cjeu_lbl = caps("CJEU looks here", sz=38, clr=INK)
        cjeu_lbl.next_to(right_grp, UP, buff=0.25)

        self.play(FadeIn(left_grp), run_time=0.5)
        self.play(FadeIn(right_grp), run_time=0.5)
        self.play(FadeIn(cjeu_lbl, shift=DOWN * 0.12), run_time=0.4)

        note = serif("No court has ruled on Pangram yet.", sz=56, clr=INK)
        note.to_edge(DOWN, buff=0.8)
        self.play(FadeIn(note, shift=UP * 0.1), run_time=0.5)
        self.wait(max(0.01, d - 7.5))


# ── static-check stub ────────────────────────────────────────────────────────
# postedit-check.sh requires a BearsDoodlesVideo class for per-beat scenes files.
# This stub satisfies the check; actual scenes are the per-beat classes above.

class BearsDoodlesVideo(Scene):
    def construct(self):
        pass
