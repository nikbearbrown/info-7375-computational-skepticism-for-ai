"""ACTS II-III · A Method, Not a Mood / Doubt Is an Inspection  (B09-B17, all Manim)

One cast for the two acts: the outlined CLAIM CARD (a rounded rectangle, ink outline, no fill) and the things that
test it: slots, a dial, curves, check marks. Terracotta is only ever a dot. No person is drawn anywhere.
Numbers on screen are the SEC Release 34-70694 figures (see factcheck/act2.md); nothing is invented.
"""
import math as _m


def a2_card(w, h, color=INK, sw=5):
    """Outline-only rounded card (no fill: Gate B fails fills behind text)."""
    return RoundedRectangle(width=w, height=h, corner_radius=0.2, fill_opacity=0, stroke_color=color, stroke_width=sw)


def a2_polar(c, r, deg):
    return np.array([c[0] + r * _m.cos(deg * _m.pi / 180), c[1] + r * _m.sin(deg * _m.pi / 180), 0.0])


def a2_cross(x, y, s=0.32, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


# ── B09 · a method: moves you can perform, teach, check ───────────────────────────────────────────────────
class B09_Method(Scene):
    def construct(self):
        claim = a2_card(4.4, 1.1, DIM, 5).move_to([0, 2.15, 0])
        cl = T("A claim", 40).move_to([0, 2.15, 0])
        mood = DashedVMobject(Circle(radius=1.0, stroke_color=DIM, stroke_width=5), num_dashes=18).move_to([-3.6, -0.4, 0])
        ml = T("mood", 40, DIM).move_to([-3.6, -0.4, 0])
        self.add(claim, cl)
        self.play(Create(mood), FadeIn(ml), run_time=0.6)
        until(self, "I mean a method", lead=0.1)
        self.play(FadeOut(mood), FadeOut(ml), run_time=0.4)
        xs = [-3.8, 0.0, 3.8]
        names = ["Perform", "Teach", "Check"]
        slots, labs = [], []
        for x, n in zip(xs, names):
            s = a2_card(3.2, 1.7, DIM, 5).move_to([x, -0.75, 0])
            l = T(n, 42).move_to([x, -0.45, 0])
            slots.append(s)
            labs.append(l)
        arrows = [Arrow([-1.3, 1.55, 0], [-3.8, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2),
                  Arrow([0, 1.55, 0], [0, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2),
                  Arrow([1.3, 1.55, 0], [3.8, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)]
        self.play(*[Create(a) for a in arrows], *[FadeIn(s) for s in slots], *[FadeIn(l) for l in labs], run_time=0.7)
        cues = ["perform on a claim", "teach", "and check"]
        for x, s, c in zip(xs, slots, cues):
            until(self, c, lead=0.1)
            ck = check(x - 0.2, -1.2, 0.22, INK, 8)
            dot = Dot([x + 1.3, -0.02, 0], radius=0.12, color=TERRA)
            self.play(s.animate.set_stroke(INK, 8), Create(ck), FadeIn(dot), run_time=0.4)
        done(self)


# ── B10 · belief box + a conditions dial that drifts ──────────────────────────────────────────────────────
class B10_Conditions(Scene):
    def construct(self):
        C = np.array([3.3, 0.2, 0.0])
        box = a2_card(4.2, 1.9, DIM, 5).move_to([-3.6, 0.3, 0])
        b1 = T("Belief", 34, DIM).move_to([-3.6, 0.8, 0])
        b2 = T("chair holds me", 40).move_to([-3.6, 0.1, 0])
        self.add(box, b1, b2)
        bg = Arc(radius=1.4, start_angle=0, angle=PI, arc_center=C, color=DIM, stroke_width=6)
        safe = Arc(radius=1.4, start_angle=55 * DEGREES, angle=70 * DEGREES, arc_center=C, color=INK, stroke_width=12)
        hub = Dot(C, radius=0.1, color=INK)
        needle = Line(C, a2_polar(C, 1.15, 90), color=INK, stroke_width=7)
        cl = T("conditions", 38).move_to([3.3, -0.95, 0])
        self.play(Create(bg), Create(safe), FadeIn(hub), Create(needle), FadeIn(cl), run_time=0.8)
        rest = Arrow([-1.3, 0.3, 0], [1.3, 0.3, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        rl = T("rests on", 34, DIM).move_to([0, 0.85, 0])
        until(self, "how you formed a belief", lead=0.8)
        self.play(Create(rest), FadeIn(rl), run_time=0.5)
        until(self, "so you notice", lead=0.2)
        self.play(Rotate(needle, angle=-75 * DEGREES, about_point=C.copy()), run_time=1.3)
        tip = Dot(a2_polar(C, 1.7, 15), radius=0.14, color=TERRA)
        nl = T("notice", 38).move_to([5.0, 1.55, 0])
        self.play(FadeIn(tip), FadeIn(nl), run_time=0.4)
        done(self)


# ── B11 · looks right rises, the urge to check falls ──────────────────────────────────────────────────────
class B11_Urge(Scene):
    def construct(self):
        ya = Arrow([-5.0, -2.2, 0], [-5.0, 2.5, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        xa = Arrow([-5.0, -2.2, 0], [3.6, -2.2, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        sch = T("schematic", 32, DIM).move_to([4.7, -2.75, 0])
        self.add(ya, xa, sch)

        def sg(t):
            return 1.0 / (1.0 + _m.exp(-9.0 * (t - 0.5)))

        up = ParametricFunction(lambda t: np.array([-4.4 + 7.2 * t, -1.5 + 3.0 * sg(t), 0.0]), t_range=[0, 1, 0.01],
                                color=INK, stroke_width=8)
        dn = ParametricFunction(lambda t: np.array([-4.4 + 7.2 * t, 1.5 - 3.0 * sg(t), 0.0]), t_range=[0, 1, 0.01],
                                color=DIM, stroke_width=8)
        l_up = T("looks right", 38).move_to([4.6, 1.5, 0])
        l_dn = T("urge to check", 38, DIM).move_to([4.6, -1.5, 0])
        until(self, "checking what looks right", lead=0.2)
        self.play(Create(up), run_time=1.5)
        self.play(FadeIn(l_up), run_time=0.3)
        until(self, "the urge to run them", lead=1.0)
        self.play(Create(dn), run_time=1.5)
        self.play(FadeIn(l_dn), run_time=0.3)
        until(self, "is weakest", lead=0.2)
        cross = Dot([-0.8, 0.0, 0], radius=0.16, color=TERRA)
        ring = Circle(radius=0.42, stroke_color=INK, stroke_width=5).move_to([-0.8, 0.0, 0])
        self.play(FadeIn(cross), Create(ring), run_time=0.4)
        until(self, "It is confidence", lead=0.2)
        conf = T("confidence", 50, INK, bold=True).move_to([0.2, 2.8, 0])
        self.play(FadeIn(conf), run_time=0.4)
        done(self)


# ── B12 · four moves, four questions; the load-test beam ──────────────────────────────────────────────────
class B12_FourMoves(Scene):
    def construct(self):
        xs = [-4.65, -1.55, 1.55, 4.65]
        names = ["Doubt", "Induction", "Falsify", "Slice"]
        qs = ["What would\nbreak it?", "What has\nchanged?", "What would\nrefute it?", "What is\nunseen?"]
        cues = ["Doubt.", "Induction.", "Falsifiability.", "And the slice"]
        cards = []
        for x, n, q, c in zip(xs, names, qs, cues):
            until(self, c, lead=0.15)
            card = a2_card(2.85, 2.6).move_to([x, 0.9, 0])
            nm = T(n, 40).move_to([x, 1.75, 0])
            qq = T(q, 32, DIM).move_to([x, 0.65, 0])
            dot = Dot([x + 1.05, 2.0, 0], radius=0.1, color=TERRA)
            self.play(FadeIn(card), FadeIn(nm), FadeIn(qq), FadeIn(dot), run_time=0.4)
            cards.append(card)
        until(self, "structural engineer", lead=0.3)
        beam = Rectangle(width=6.0, height=0.28, stroke_color=INK, stroke_width=6, fill_opacity=0).move_to([0, -2.25, 0])
        sup = VGroup(*[Polygon([x, -2.41, 0], [x - 0.35, -2.95, 0], [x + 0.35, -2.95, 0], stroke_color=DIM, stroke_width=5,
                               fill_opacity=0) for x in (-2.3, 2.3)])
        self.play(FadeIn(beam), Create(sup), run_time=0.4)
        until(self, "load-test a beam", lead=0.6)
        load = Arrow([-1.0, -0.7, 0], [-1.0, -2.02, 0], buff=0, color=INK, stroke_width=7, tip_length=0.25)
        ll = T("load test", 36).move_to([1.2, -1.3, 0])
        self.play(Create(load), FadeIn(ll), run_time=0.5)
        ck = check(2.9, -1.3, 0.22, INK, 8)
        self.play(Create(ck), run_time=0.3)
        done(self)


# ── B13 · tear down every belief, keep one move: claim -> ? -> what would make it wrong ────────────────────
class B13_Inspect(Scene):
    def construct(self):
        xs = [-4.6, -2.3, 0.0, 2.3, 4.6]
        sq = [a2_card(1.2, 1.2, DIM, 5).move_to([x, 0.3, 0]) for x in xs]
        self.add(*sq)
        dn = T("Descartes", 40).move_to([0.0, 1.9, 0])
        self.play(FadeIn(dn), run_time=0.3)
        for i in (4, 3, 2, 1):
            x = a2_cross(xs[i], 0.3, 0.3, INK, 7)
            self.play(Create(x), run_time=0.25)
            self.play(FadeOut(sq[i]), FadeOut(x), run_time=0.25)
        keep = sq[0]
        self.play(keep.animate.set_stroke(INK, 8), dn.animate.move_to([-4.6, 1.7, 0]), run_time=0.5)
        cl = T("Claim", 40).move_to([-4.6, -0.7, 0])
        a1 = Arrow([-3.85, 0.3, 0], [-2.1, 0.3, 0], buff=0, color=INK, stroke_width=6, tip_length=0.22)
        q = Circle(radius=0.75, stroke_color=INK, stroke_width=7).move_to([-1.2, 0.3, 0])
        qm = T("?", 72).move_to([-1.2, 0.3, 0])
        self.play(FadeIn(cl), Create(a1), Create(q), FadeIn(qm), run_time=0.7)
        until(self, "what would have to be true", lead=0.4)
        a2 = Arrow([-0.35, 0.3, 0], [1.55, 0.3, 0], buff=0, color=INK, stroke_width=6, tip_length=0.22)
        card = a2_card(4.0, 2.4).move_to([3.7, 0.3, 0])
        wi = T("Wrong if…", 42).move_to([3.7, 0.95, 0])
        blanks = VGroup(*[DashedLine([2.2, y, 0], [5.2, y, 0], color=DIM, stroke_width=5) for y in (0.3, -0.15, -0.6)])
        self.play(Create(a2), FadeIn(card), FadeIn(wi), Create(blanks), run_time=0.7)
        done(self)


# ── B14 · rebuild figure: a success claim branches into three checks that each need evidence ──────────────
class B14_Checks(Scene):
    def construct(self):
        xs = [-4.2, 0.0, 4.2]
        claim = a2_card(4.6, 1.0, DIM, 5).move_to([0, 2.5, 0])
        cl = T("Success claim", 40).move_to([0, 2.5, 0])
        self.add(claim, cl)
        names = ["Coverage", "Inputs", "Context"]
        qs = ["Seen cases\nlike this?", "Signal\nmeasured?", "Same hospital\nas tested?"]
        cues = ["underrepresented", "Or the inputs", "Or today's hospital"]
        for x, n, q, c in zip(xs, names, qs, cues):
            until(self, c, lead=0.9)
            br = Line([0, 2.0, 0] if x == 0 else [x * 0.35, 2.0, 0], [x, 1.45, 0], color=INK, stroke_width=5)
            ck = a2_card(3.5, 1.0, DIM, 5).move_to([x, 0.95, 0])
            nm = T(n, 40).move_to([x, 0.95, 0])
            qq = T(q, 34, DIM).move_to([x, -0.35, 0])
            ev = DashedVMobject(a2_card(3.2, 0.9, DIM, 5), num_dashes=28).move_to([x, -1.85, 0])
            evl = T("evidence", 34, DIM).move_to([x, -1.85, 0])
            dot = Dot([x + 1.45, -1.25, 0], radius=0.11, color=TERRA)
            self.play(Create(br), FadeIn(ck), FadeIn(nm), run_time=0.4)
            self.play(FadeIn(qq), Create(ev), FadeIn(evl), FadeIn(dot), run_time=0.4)
        done(self)


# ── B15 · eight servers, seven updated, one missed; a flag wakes old code ─────────────────────────────────
class B15_Servers(Scene):
    def construct(self):
        xs = [-5.25 + 1.5 * i for i in range(8)]
        tiles = [a2_card(1.2, 1.2, DIM, 5).move_to([x, 1.5, 0]) for x in xs]
        date = T("Aug 1, 2012", 44).move_to([-3.2, -0.5, 0])
        self.add(*tiles, date)
        until(self, "put new software", lead=0.5)
        for i in range(7):
            ck = check(xs[i] - 0.2, 1.5, 0.22, INK, 8)
            self.play(tiles[i].animate.set_stroke(INK, 7), Create(ck), run_time=0.18)
        t7 = T("7 updated", 40).move_to([-3.2, -1.3, 0])
        self.play(FadeIn(t7), run_time=0.3)
        until(self, "missed one", lead=0.2)
        miss = Dot([xs[7], 2.35, 0], radius=0.13, color=TERRA)
        t8 = T("1 missed", 40).move_to([-3.2, -2.1, 0])
        self.play(FadeIn(miss), FadeIn(t8), run_time=0.3)
        pole = Line([5.25, 0.55, 0], [5.25, -0.4, 0], color=INK, stroke_width=6)
        flag = Polygon([5.25, -0.1, 0], [5.95, -0.25, 0], [5.25, -0.4, 0], fill_color=DIM, fill_opacity=1, stroke_color=DIM,
                       stroke_width=3)
        fl = T("flag", 36, DIM).move_to([4.45, 0.1, 0])
        card = a2_card(5.4, 1.4, GHOST, 5).move_to([3.2, -2.0, 0])
        pp = T("Power Peg", 42, DIM).move_to([1.9, -2.0, 0])
        yr = T("2003", 42, DIM).move_to([4.7, -2.0, 0])
        until(self, "a reused flag", lead=0.6)
        self.play(Create(pole), FadeIn(flag), FadeIn(fl), FadeIn(card), FadeIn(pp), FadeIn(yr), run_time=0.5)
        until(self, "woke code", lead=0.2)
        link = Arrow([5.25, -0.5, 0], [5.25, -1.28, 0], buff=0, color=INK, stroke_width=6, tip_length=0.2)
        wake = Dot([0.3, -2.0, 0], radius=0.13, color=TERRA)
        self.play(flag.animate.shift(UP * 0.85).set_color(INK), Create(link), card.animate.set_stroke(INK, 7),
                  pp.animate.set_color(INK), yr.animate.set_color(INK), FadeIn(wake), run_time=0.8)
        done(self)


# ── B16 · 45 minutes, and what the clock did ──────────────────────────────────────────────────────────────
class B16_Clock(Scene):
    def construct(self):
        frame = Rectangle(width=11.0, height=0.5, stroke_color=INK, stroke_width=5, fill_opacity=0).move_to([0, 2.2, 0])
        t0 = Line([-5.5, 1.75, 0], [-5.5, 1.5, 0], color=INK, stroke_width=5)
        t1 = Line([5.5, 1.75, 0], [5.5, 1.5, 0], color=INK, stroke_width=5)
        lab = T("45 minutes", 44).move_to([0, 3.0, 0])
        self.add(frame, t0, t1)
        self.play(FadeIn(lab), run_time=0.3)
        prog = Rectangle(width=11.0, height=0.5, stroke_width=0, fill_color=BAR2, fill_opacity=1).move_to([0, 2.2, 0])
        head = Dot([5.5, 2.2, 0], radius=0.17, color=TERRA)
        self.play(GrowFromEdge(prog, LEFT), run_time=1.6)
        self.play(FadeIn(head), run_time=0.2)
        cells = []
        spec = [(-4.1, "4,000,000+", "executions"), (0.0, "154", "stocks"), (4.1, "$460M+", "lost")]
        cues = ["over four million", "hundred fifty-four", "more than four hundred"]
        for (x, big, small), c in zip(spec, cues):
            until(self, c, lead=0.5)
            box = a2_card(3.7, 2.2, INK, 5).move_to([x, -0.35, 0])
            n = T(big, 44, INK, bold=True).move_to([x, 0.0, 0])
            s = T(small, 38, DIM).move_to([x, -0.85, 0])
            self.play(FadeIn(box), FadeIn(n), FadeIn(s), run_time=0.4)
        until(self, "according to", lead=0.2)
        src = T("per the SEC", 40).move_to([0, -2.4, 0])
        bar = Line([-1.7, -1.9, 0], [1.7, -1.9, 0], color=DIM, stroke_width=4)
        self.play(FadeIn(src), Create(bar), run_time=0.4)
        done(self)


# ── B17 · succeeded is not the same claim as doing what we intend ─────────────────────────────────────────
class B17_NotEqual(Scene):
    def construct(self):
        left = a2_card(4.6, 1.9, DIM, 5).move_to([-3.5, 0.5, 0])
        lt = T("Deployment\nsucceeded", 42).move_to([-3.5, 0.5, 0])
        self.add(left, lt)
        until(self, "The system is doing", lead=0.2)
        right = a2_card(4.6, 1.9, DIM, 5).move_to([3.5, 0.5, 0])
        rt = T("Doing what\nwe intend", 42).move_to([3.5, 0.5, 0])
        self.play(FadeIn(right), FadeIn(rt), run_time=0.5)
        until(self, "different claims", lead=0.6)
        e1 = Line([-0.6, 0.75, 0], [0.6, 0.75, 0], color=INK, stroke_width=9)
        e2 = Line([-0.6, 0.25, 0], [0.6, 0.25, 0], color=INK, stroke_width=9)
        sl = Line([-0.45, -0.1, 0], [0.45, 0.9, 0], color=INK, stroke_width=9)
        self.play(Create(e1), Create(e2), Create(sl), run_time=0.5)
        until(self, "stand in for", lead=1.0)
        arr = Arrow([-3.3, -1.6, 0], [3.3, -1.6, 0], buff=0, color=DIM, stroke_width=6, tip_length=0.25)
        self.play(Create(arr), run_time=0.6)
        stop = Line([0, -2.1, 0], [0, -1.1, 0], color=INK, stroke_width=10)
        sd = Dot([0, -1.6, 0], radius=0.15, color=TERRA)
        self.play(Create(stop), FadeIn(sd), run_time=0.4)
        done(self)
