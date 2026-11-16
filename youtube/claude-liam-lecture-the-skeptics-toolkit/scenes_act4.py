"""GROUP 4 · Act VI "The slice you can see" (B28-B33) and Act VII "Cheap to make, dear to check" (B34-B37).

Cast, Act VI: the ARTIFACT/WORLD pair drawn as outlines, dashed ghosts for what is never seen, and the lit SLICE of a disk.
Cast, Act VII: effort bars, candidate circles, a stack of boxes with the same hole, a clipboard for the human check.
No people anywhere; the patient is a clot, a tube and a gurney.
"""


def a4_label(s, x, y, size=36, color=INK):
    return T(s, size, color).move_to([x, y, 0])


def a4_x(x, y, s=0.2, color=INK, w=7):
    return VGroup(Line([x - s, y - s, 0], [x + s, y + s, 0], color=color, stroke_width=w),
                  Line([x - s, y + s, 0], [x + s, y - s, 0], color=color, stroke_width=w))


def a4_ghost(center, r, dashes=18):
    return DashedVMobject(Circle(radius=r, color=DIM, stroke_width=5).move_to(center), num_dashes=dashes)


# ── B28 · you never see the cause ────────────────────────────────────────────────────────────────────────
class B28_Unseen(Scene):
    def construct(self):
        ground = Line([-5.6, -2.3, 0], [-2.2, -2.3, 0], color=INK, stroke_width=7)
        apple = VGroup(Circle(radius=0.32, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5),
                       Line([0, 0.32, 0], [0.06, 0.58, 0], color=INK, stroke_width=5)).move_to([-3.9, 2.2, 0])
        oc = np.array([3.4, 0.1, 0.0])
        orbit = Circle(radius=2.0, color=DIM, stroke_width=6).move_to(oc)
        sun = Circle(radius=0.38, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to(oc)
        body = Dot(oc + np.array([-2.0 * 0.5, 2.0 * 0.866, 0]), radius=0.17, color=INK)
        self.add(ground, apple, orbit, sun, body)
        until(self, "You never see causation", lead=0.3)
        ghost = a4_ghost([0, 0.3, 0], 0.65)
        l1 = DashedLine([-0.65, 0.3, 0], [-3.3, 0.3, 0], color=DIM, stroke_width=5)
        l2 = DashedLine([0.65, 0.3, 0], [1.4, 0.3, 0], color=DIM, stroke_width=5)
        cause = a4_label("cause", 0, -0.75)
        self.play(Create(ghost), Create(l1), Create(l2), FadeIn(cause), run_time=0.7)
        until(self, "Nobody has seen gravity", lead=0.2)
        self.play(Indicate(VGroup(ghost, cause), scale_factor=1.12, color=INK), run_time=0.6)
        until(self, "an apple falling", lead=0.6)
        lab_a = a4_label("apple falling", -3.9, -2.85)
        hit = Dot([-3.25, -2.3, 0], radius=0.13, color=TERRA)
        self.play(apple.animate.move_to([-3.9, -1.95, 0]), FadeIn(lab_a), run_time=0.7, rate_func=ease_in)
        self.play(GrowFromCenter(hit), run_time=0.2)
        until(self, "an orbit bending", lead=1.2)
        lab_o = a4_label("orbit bending", 3.4, -2.85)
        arc = Arc(radius=2.0, start_angle=2 * PI / 3, angle=-PI * 0.55, arc_center=oc)
        body.move_to(arc.get_start())
        self.play(MoveAlongPath(body, arc), FadeIn(lab_o), run_time=0.9)
        done(self)


# ── B29 · the lit slice and the outside ───────────────────────────────────────────────────────────────────
class B29_Slice(Scene):
    def construct(self):
        c = np.array([-1.5, 0.2, 0.0])
        disk = Circle(radius=2.2, fill_color=GHOST, fill_opacity=0.45, stroke_color=DIM, stroke_width=6).move_to(c)
        sl = Sector(radius=2.2, start_angle=20 * DEGREES, angle=60 * DEGREES, arc_center=c, fill_color=BOX_L, fill_opacity=1,
                    stroke_color=INK, stroke_width=5)
        out_l = a4_label("outside", -1.5, -2.75)
        sl_l = a4_label("slice", 1.0, 1.95)
        self.add(disk, sl, out_l, sl_l)
        kant = a4_label("Kant", 4.3, 1.9, 40)
        until(self, "Kant said better instruments", lead=0.2)
        tele = VGroup(Rectangle(width=1.5, height=0.4, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5),
                      Line([-0.75, 0, 0], [-0.95, 0.0, 0], color=INK, stroke_width=8)).rotate(133 * DEGREES).move_to([1.7, -0.25, 0])
        self.play(FadeIn(kant), FadeIn(tele), run_time=0.5)
        ticks = VGroup(*[Line(c + np.array([0.7 * np.cos(a * DEGREES), 0.7 * np.sin(a * DEGREES), 0]),
                              c + np.array([2.05 * np.cos(a * DEGREES), 2.05 * np.sin(a * DEGREES), 0]), color=DIM, stroke_width=3)
                         for a in (28, 40, 52, 64, 74)])
        self.play(LaggedStart(*[Create(t) for t in ticks], lag_ratio=0.25), run_time=1.2)
        until(self, "never close that gap", lead=0.1)
        self.play(Indicate(out_l, scale_factor=1.15, color=INK), run_time=0.5)
        until(self, "weaker view", lead=0.2)
        wide = Sector(radius=2.2, start_angle=4 * DEGREES, angle=92 * DEGREES, arc_center=c, fill_opacity=0, stroke_color=INK, stroke_width=5)
        wk = a4_label("weaker view", 4.3, 0.15, 40)
        wk2 = a4_label("the course author's", 4.3, -0.55, 32)
        self.play(Create(wide), FadeIn(wk), FadeIn(wk2), run_time=0.8)
        until(self, "approaching without arriving", lead=0.3)
        reach = Dot(c + np.array([2.2 * np.cos(4 * DEGREES), 2.2 * np.sin(4 * DEGREES), 0]), radius=0.15, color=TERRA)
        self.add(reach)
        self.play(MoveAlongPath(reach, Arc(radius=2.2, start_angle=4 * DEGREES, angle=-80 * DEGREES, arc_center=c)), run_time=1.6)
        until(self, "we see a slice", lead=0.2)
        self.play(Indicate(sl, scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "there is an outside", lead=0.2)
        self.play(Indicate(VGroup(out_l), scale_factor=1.2, color=INK), run_time=0.6)
        done(self)


# ── B30 · artifact | ? | world ────────────────────────────────────────────────────────────────────────────
class B30_ThreeQuestions(Scene):
    def construct(self):
        ab = RoundedRectangle(width=2.6, height=2.2, corner_radius=0.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-3.9, 0.3, 0])
        lines = VGroup(*[Line([-4.7, y, 0], [-3.1, y, 0], color=DIM, stroke_width=5) for y in (0.8, 0.3, -0.2)])
        wb = RoundedRectangle(width=2.6, height=2.2, corner_radius=0.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([3.9, 0.3, 0])
        rings = VGroup(*[Circle(radius=r, color=DIM, stroke_width=5).move_to([3.9, 0.3, 0]) for r in (0.35, 0.75)])
        link = DashedLine([-2.4, 0.3, 0], [2.4, 0.3, 0], color=DIM, stroke_width=5)
        self.add(ab, lines, wb, rings, link)
        until(self, "What is the artifact?", lead=0.2)
        l1 = a4_label("artifact", -3.9, -1.3)
        d1 = Dot([-3.9, -1.85, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(l1), FadeIn(d1), Indicate(VGroup(ab, lines), scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "What is the world?", lead=0.2)
        l2 = a4_label("world", 3.9, -1.3)
        d2 = Dot([3.9, -1.85, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(l2), FadeIn(d2), Indicate(VGroup(wb, rings), scale_factor=1.06, color=INK), run_time=0.6)
        until(self, "the relationship between them", lead=0.3)
        arr = dim_arrow([-2.45, 0.3, 0], [2.45, 0.3, 0], w=7, tip=0.22)
        q = a4_label("?", 0, 1.15, 80)
        l3 = a4_label("relationship", 0, -0.5)
        self.play(FadeOut(link), Create(arr), FadeIn(q), FadeIn(l3), run_time=0.7)
        until(self, "when the output is fluent", lead=0.2)
        d3 = Dot([0, -1.05, 0], radius=0.14, color=TERRA)
        self.play(FadeIn(d3), run_time=0.3)
        done(self)


# ── B31 · everything checked on one side, the clot on the other ─────────────────────────────────────────
class B31_Gurney(Scene):
    def construct(self):
        div = Line([0.1, 2.9, 0], [0.1, -2.7, 0], color=GHOST, stroke_width=5)
        h1 = a4_label("artifact", -3.9, 2.5, 40)
        h2 = a4_label("world", 3.6, 2.5, 40)
        self.add(div, h1, h2)
        rows = [("score", 1.3, "The triage system produced a score"), ("model", 0.3, "the model"), ("metrics", -0.7, "the metrics")]
        labs, cks = [], []
        for name, y, _ in rows:
            labs.append(a4_label(name, -4.5, y))
            cks.append(check(-2.4, y - 0.05, 0.2, INK, 8))
        until(self, "The triage system produced a score", lead=0.1)
        self.play(FadeIn(labs[0]), Create(cks[0]), run_time=0.5)
        until(self, "The patient had a clot", lead=0.1)
        tube = VGroup(Line([1.9, 1.62, 0], [5.4, 1.62, 0], color=DIM, stroke_width=6), Line([1.9, 1.0, 0], [5.4, 1.0, 0], color=DIM, stroke_width=6))
        clot = Dot([3.6, 1.31, 0], radius=0.24, color=TERRA)
        box = Square(side_length=0.5, color=DIM, stroke_width=5).move_to([1.0, 1.31, 0])
        cl = a4_label("clot", 3.6, 0.4)
        self.play(Create(tube), GrowFromCenter(clot), Create(box), FadeIn(cl), run_time=0.7)
        until(self, "reviewed the score", lead=0.1)
        self.play(FadeIn(labs[1]), Create(cks[1]), run_time=0.4)
        self.play(FadeIn(labs[2]), Create(cks[2]), run_time=0.4)
        until(self, "gurney", lead=0.2)
        bed = Rectangle(width=3.4, height=0.32, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([3.6, -1.1, 0])
        legs = VGroup(Line([2.2, -1.26, 0], [2.2, -1.85, 0], color=INK, stroke_width=5), Line([5.0, -1.26, 0], [5.0, -1.85, 0], color=INK, stroke_width=5))
        wheels = VGroup(Circle(radius=0.17, color=INK, stroke_width=5).move_to([2.2, -2.0, 0]), Circle(radius=0.17, color=INK, stroke_width=5).move_to([5.0, -2.0, 0]))
        comp = a4_label("composite case", 3.6, -2.85, 32, DIM)
        self.play(Create(bed), Create(legs), Create(wheels), FadeIn(comp), run_time=0.7)
        done(self)


# ── B32 · the ring lands on the corner marker ───────────────────────────────────────────────────────────
class B32_Xray(Scene):
    def construct(self):
        plate = Rectangle(width=4.2, height=4.8, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=6).move_to([-3.6, -0.1, 0])
        lungs = VGroup(Ellipse(width=1.5, height=2.4, color=DIM, stroke_width=6).move_to([-4.3, -0.1, 0]),
                       Ellipse(width=1.5, height=2.4, color=DIM, stroke_width=6).move_to([-2.9, -0.1, 0]))
        spine = Line([-3.6, 1.6, 0], [-3.6, -1.7, 0], color=GHOST, stroke_width=6)
        marker = VGroup(Rectangle(width=0.55, height=0.36, color=INK, stroke_width=5), Line([-0.15, 0, 0], [0.15, 0, 0], color=DIM, stroke_width=4)).move_to([-5.0, 1.9, 0])
        self.add(plate, lungs, spine, marker)
        until(self, "detect COVID", lead=0.3)
        ring = Circle(radius=1.55, color=TERRA, stroke_width=8).move_to([-3.6, -0.1, 0])
        self.play(Create(ring), run_time=0.8)
        until(self, "DeGrave", lead=0.3)
        who = VGroup(a4_label("DeGrave, Janizek", 3.4, 0.55, 34), a4_label("& Lee, 2021", 3.4, 0.0, 34))
        self.play(FadeIn(who), run_time=0.4)
        until(self, "confounding factors", lead=0.3)
        self.play(ring.animate.scale(0.3).move_to([-5.0, 1.9, 0]), run_time=1.0)
        until(self, "accurate-looking", lead=0.3)
        q = T("“appear accurate, but\nfail when tested in\nnew hospitals”", 38).move_to([3.4, 2.0, 0])
        self.play(FadeIn(q), run_time=0.5)
        def hosp(x):
            return VGroup(Rectangle(width=0.9, height=0.9, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5),
                          Line([-0.2, 0, 0], [0.2, 0, 0], color=DIM, stroke_width=5), Line([0, -0.2, 0], [0, 0.2, 0], color=DIM, stroke_width=5)).move_to([x, -1.2, 0])
        h1, h2 = hosp(1.7), hosp(4.6)
        t1, t2 = a4_label("known", 1.7, -2.25, 32), a4_label("new", 4.6, -2.25, 32)
        self.play(FadeIn(h1), FadeIn(t1), Create(check(2.75, -1.25, 0.2, INK, 8)), run_time=0.5)
        self.play(FadeIn(h2), FadeIn(t2), Create(a4_x(5.65, -1.2)), run_time=0.5)
        done(self)


# ── B33 · artifact / world / relationship for a recidivism score ───────────────────────────────────────
class B33_Score(Scene):
    def construct(self):
        r1, r2, r3 = 2.2, 0.9, -1.1
        l1 = a4_label("artifact", -4.9, r1)
        l2 = a4_label("world", -4.9, r2)
        l3 = a4_label("relationship", -4.9, r3)
        self.add(l1)
        until(self, "A recidivism score", lead=0.2)
        bar = RoundedRectangle(width=4.6, height=0.5, corner_radius=0.25, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([0.6, r1, 0])
        pt = Dot([1.6, r1, 0], radius=0.2, color=INK)
        self.play(Create(bar), GrowFromCenter(pt), run_time=0.6)
        until(self, "A person's future conduct", lead=0.2)
        far = DashedLine([-1.2, r2, 0], [4.8, r2, 0], color=DIM, stroke_width=6)
        tip = Arrow([4.0, r2, 0], [5.3, r2, 0], buff=0, color=DIM, stroke_width=6, tip_length=0.25)
        self.play(FadeIn(l2), Create(far), Create(tip), run_time=0.6)
        until(self, "Between them sit arrest records", lead=0.2)
        c1 = Circle(radius=0.3, color=INK, stroke_width=5).move_to([-1.7, -0.45, 0])
        c2 = Circle(radius=0.3, color=INK, stroke_width=5).move_to([-1.7, -1.95, 0])
        n1, n2 = a4_label("policing", -1.7, 0.1, 34), a4_label("behavior", -1.7, -2.55, 34)
        rec = Rectangle(width=1.0, height=1.3, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([1.2, r3, 0])
        rl = VGroup(*[Line([0.9, r3 + dy, 0], [1.5, r3 + dy, 0], color=DIM, stroke_width=4) for dy in (0.3, 0.0, -0.3)])
        a1 = Arrow([-1.35, -0.55, 0], [0.65, -1.0, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        a2 = Arrow([-1.35, -1.85, 0], [0.65, -1.3, 0], buff=0, color=INK, stroke_width=5, tip_length=0.2)
        rn = a4_label("arrest records", 4.2, r3, 36)
        self.play(FadeIn(l3), Create(c1), Create(c2), FadeIn(n1), FadeIn(n2), run_time=0.6)
        self.play(Create(a1), Create(a2), Create(rec), Create(rl), FadeIn(rn), run_time=0.7)
        until(self, "ProPublica", lead=0.3)
        pp = a4_label("ProPublica, 2016", 4.4, -2.7, 34)
        self.play(FadeIn(pp), run_time=0.4)
        done(self)


# ── B34 · checking is cheap, finding is dear ────────────────────────────────────────────────────────────
class B34_Factors(Scene):
    def construct(self):
        div = Line([0.1, 2.7, 0], [0.1, -2.7, 0], color=GHOST, stroke_width=5)
        lc = a4_label("check", -3.2, 2.5, 40)
        lf = a4_label("find", 3.3, 2.5, 40)
        target = Rectangle(width=3.0, height=2.0, color=DIM, stroke_width=6).move_to([-3.2, 0.0, 0])
        cells = VGroup(*[Circle(radius=0.2, color=INK, stroke_width=4).move_to([1.15 + 0.7 * i, 1.2 - 0.7 * j, 0])
                         for j in range(4) for i in range(6)])
        self.add(div, lc, lf, target, cells)
        until(self, "Hand me the factors", lead=0.2)
        fw = Line([-4.7, -1.4, 0], [-1.7, -1.4, 0], color=INK, stroke_width=8)
        fh = Line([-5.1, -1.0, 0], [-5.1, 1.0, 0], color=INK, stroke_width=8)
        self.play(Create(fw), Create(fh), run_time=0.6)
        until(self, "multiply them", lead=0.3)
        fill = Rectangle(width=3.0, height=2.0, fill_color=BAR2, fill_opacity=1, stroke_color=INK, stroke_width=6).move_to([-3.2, 0.0, 0])
        self.play(FadeIn(fill), Create(check(-3.2, 0.0, 0.35, INK, 12)), run_time=0.6)
        until(self, "Finding them is hard", lead=0.2)
        hop = Dot(cells[0].get_center(), radius=0.14, color=TERRA)
        self.add(hop)
        path = [0, 1, 2, 3, 4, 5, 11, 10, 9, 8, 7, 6, 12]
        step = 1 / 15
        for k in path[1:]:
            self.play(hop.animate.move_to(cells[k].get_center()), run_time=step, rate_func=linear)
        done(self)


# ── B35 · the asymmetry runs backwards ───────────────────────────────────────────────────────────────────
class B35_Backwards(Scene):
    def construct(self):
        lp = a4_label("produce", -5.0, 1.1)
        lv = a4_label("verify", -5.0, -0.5)
        axis = Line([-3.7, 1.9, 0], [-3.7, -1.3, 0], color=DIM, stroke_width=5)
        tag = a4_label("schematic", 4.9, 2.9, 32, DIM)
        self.add(lp, lv, axis, tag)
        until(self, "Producing an output is cheap", lead=0.2)
        pb = Rectangle(width=0.3, height=0.5, fill_color=BAR1, fill_opacity=1, stroke_width=0).move_to([-3.55, 1.1, 0])
        pd = Dot([-3.0, 1.1, 0], radius=0.12, color=TERRA)
        self.play(FadeIn(pb), GrowFromCenter(pd), run_time=0.4)
        until(self, "Verifying it can take", lead=0.2)
        vb = Rectangle(width=6.6, height=0.5, fill_color=BAR2, fill_opacity=1, stroke_color=DIM, stroke_width=3).move_to([-0.4, -0.5, 0])
        vd = Dot([3.1, -0.5, 0], radius=0.12, color=TERRA)
        self.play(GrowFromEdge(vb, LEFT), run_time=2.2, rate_func=linear)
        self.play(GrowFromCenter(vd), run_time=0.3)
        until(self, "compare kinds of work", lead=0.3)
        cap = T("compares kinds of work,\nnot measured costs", 36).move_to([0, -2.4, 0])
        self.play(FadeIn(cap), run_time=0.5)
        done(self)


# ── B36 · the stream, the few checks, the one that was wrong ──────────────────────────────────────────────
class B36_Stream(Scene):
    def construct(self):
        def cell(i, j):
            return np.array([-4.4 + 1.1 * i, 1.8 - 1.15 * j, 0.0])
        circ = [[Circle(radius=0.33, color=DIM, stroke_width=5).move_to(cell(i, j)) for i in range(9)] for j in range(3)]
        until(self, "If you do not budget", lead=0.0)
        self.play(LaggedStart(*[GrowFromCenter(c) for c in circ[0]], lag_ratio=0.2), run_time=1.4)
        until(self, "Outputs pour out", lead=0.2)
        self.play(LaggedStart(*[GrowFromCenter(c) for row in circ[1:] for c in row], lag_ratio=0.06), run_time=1.6)
        until(self, "checks do not", lead=0.2)
        marks = [check(*cell(i, j)[:2], 0.17, INK, 8) for (i, j) in ((1, 0), (5, 1), (7, 2))]
        self.play(*[Create(m) for m in marks], run_time=0.5)
        lg_c = check(-2.6, -2.55, 0.17, INK, 8)
        lg_t = a4_label("checked", -1.5, -2.55, 34)
        lg_o = Circle(radius=0.22, color=DIM, stroke_width=5).move_to([0.6, -2.55, 0])
        lg_u = a4_label("unchecked", 1.9, -2.55, 34)
        self.play(FadeIn(lg_c), FadeIn(lg_t), FadeIn(lg_o), FadeIn(lg_u), run_time=0.4)
        until(self, "until one is the patient", lead=0.2)
        p = cell(4, 2)
        wr = a4_x(p[0], p[1], 0.18, INK, 9)
        wd = Dot(p, radius=0.12, color=TERRA)
        self.play(Create(wr), GrowFromCenter(wd), run_time=0.5)
        lg_x = a4_x(3.9, -2.55, 0.17)
        lg_w = a4_label("wrong", 4.9, -2.55, 34)
        self.play(FadeIn(lg_x), FadeIn(lg_w), run_time=0.4)
        until(self, "the email never deleted", lead=0.3)
        self.play(Indicate(VGroup(wr, wd), scale_factor=1.5, color=INK), run_time=0.6)
        done(self)


# ── B37 · model checking model, the same hole ────────────────────────────────────────────────────────────
class B37_SameHole(Scene):
    def construct(self):
        lo = Rectangle(width=3.0, height=1.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-2.6, -1.0, 0])
        hl = DashedVMobject(Circle(radius=0.3, color=INK, stroke_width=5).move_to([-2.6, -1.0, 0]), num_dashes=12)
        l_lo = a4_label("model", 0.2, -1.0)
        self.add(lo, hl, l_lo)
        until(self, "another model, one layer up", lead=0.5)
        up = Rectangle(width=3.0, height=1.2, fill_color=BOX_TOP, fill_opacity=1, stroke_color=INK, stroke_width=5).move_to([-2.6, 1.4, 0])
        hu = DashedVMobject(Circle(radius=0.3, color=INK, stroke_width=5).move_to([-2.6, 1.4, 0]), num_dashes=12)
        l_up = a4_label("model", 0.2, 1.4)
        arr = Arrow([-2.6, -0.35, 0], [-2.6, 0.75, 0], buff=0, color=DIM, stroke_width=5, tip_length=0.2)
        self.play(Create(up), Create(hu), FadeIn(l_up), Create(arr), run_time=0.8)
        until(self, "with the same problem", lead=0.3)
        guide = DashedLine([-2.6, -2.9, 0], [-2.6, 3.0, 0], color=GHOST, stroke_width=5)
        err = Dot([-2.6, -2.8, 0], radius=0.17, color=TERRA)
        self.add(guide, err)
        self.play(err.animate.move_to([-2.6, 2.9, 0]), run_time=1.0, rate_func=linear)
        until(self, "a human can do", lead=0.4)
        clip = VGroup(RoundedRectangle(width=2.0, height=2.6, corner_radius=0.15, fill_color=CARD, fill_opacity=1, stroke_color=INK, stroke_width=5),
                      Rectangle(width=0.8, height=0.3, fill_color=BOX_L, fill_opacity=1, stroke_color=INK, stroke_width=4).shift(UP * 1.3)).move_to([4.0, 0.2, 0])
        ck = VGroup(*[check(3.5, y, 0.14, INK, 7) for y in (0.8, 0.2, -0.4)])
        ln = VGroup(*[Line([3.75, y, 0], [4.6, y, 0], color=DIM, stroke_width=4) for y in (0.8, 0.2, -0.4)])
        l_h = a4_label("human check", 4.0, -1.6, 34)
        self.play(FadeIn(clip), Create(ck), Create(ln), FadeIn(l_h), run_time=0.8)
        done(self)
