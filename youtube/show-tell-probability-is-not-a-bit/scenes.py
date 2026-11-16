from manim import *
import json, os, numpy as np
STAGE="#F2F0E9"; INK="#3D3929"; TERRA="#8F3F27"; DIM="#8B8F96"; KRAFT="#C7AE86"; PALE="#F3E9D8"; DARK="#26221F"; SERIF="EB Garamond"
config.background_color=STAGE
try:
 S=json.load(open(os.path.join(os.path.dirname(__file__),"beat_sheet.json")))
 TARGET={b['beat_id']:float(b.get('actual_duration_s') or b.get('estimated_duration_s',8)) for b in S['beats']}
except Exception:
 TARGET={}
def txt(s,p=(0,0),z=42,c=INK): return Text(s,font=SERIF,font_size=z,color=c).move_to([*p,0])
def box(p=(0,0),w=1.5,h=.8,c=KRAFT):
 x,y=p; return VGroup(Rectangle(width=w,height=h,fill_color=c,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([x,y,0]),Line([x-w/2,y+h/2,0],[x-w/2+.22,y+h/2+.16,0],color=INK,stroke_width=3),Line([x+w/2,y+h/2,0],[x+w/2+.22,y+h/2+.16,0],color=INK,stroke_width=3))
def tile(n,p,c=PALE): return VGroup(box(p,.85,.62,c),txt(str(n),p,36))
def peg(p):
 x,y=p; return VGroup(RoundedRectangle(width=.55,height=.85,corner_radius=.15,fill_color=KRAFT,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([x,y-.3,0]),Circle(.24,fill_color=PALE,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([x,y+.43,0]))
def bar(p=(0,0),mark=.5,label="belief"):
 x,y=p; rail=RoundedRectangle(width=4.5,height=.55,corner_radius=.18,stroke_color=INK,stroke_width=4).move_to([x,y,0]); fill=Rectangle(width=max(.08,4.35*mark),height=.4,fill_color=TERRA,fill_opacity=1,stroke_width=0).align_to(rail,LEFT).shift(RIGHT*.08); m=Line([x-2.18+4.35*mark,y-.42,0],[x-2.18+4.35*mark,y+.42,0],color=INK,stroke_width=7); return VGroup(rail,fill,m,txt('0',(x-2.25,y-.65),30),txt('1',(x+2.25,y-.65),30),txt(label,(x,y+.75),34))
def tray(nums,p=(0,0),label='Ω'):
 x,y=p; base=RoundedRectangle(width=5.4,height=1.5,corner_radius=.2,fill_color=PALE,fill_opacity=1,stroke_color=INK,stroke_width=5).move_to([x,y,0]); ts=VGroup(*[tile(n,(x-2.05+i*.82,y),KRAFT) for i,n in enumerate(nums)]); return VGroup(base,ts,txt(label,(x-3.65,y+1.4),52))
def elapsed(s): return float(getattr(getattr(s,'renderer',None),'time',0) or 0)
def finish(s):
 bid=type(s).__name__.split('_')[0]; t=TARGET.get(bid,8); s.wait(max(.05,t-elapsed(s)-.15)); print(f'[pace] {bid} content={elapsed(s):.2f}s target={t:.2f}s')
def pulse(s,p):
 r=Circle(1.0,color=DIM,stroke_width=6).move_to([*p,0]); s.play(GrowFromCenter(r),run_time=.3); s.play(FadeOut(r),run_time=.3)
class B00_Boolean(Scene):
 def construct(self):
  a,b=tile(1,(-2.6,0)),tile(0,(2.6,0)); sw=Line([-1.3,0,0],[1.3,0,0],color=INK,stroke_width=9); dot=Dot([-1.0,0,0],radius=.18,color=TERRA)
  self.play(FadeIn(a),FadeIn(b),Create(sw),FadeIn(dot),run_time=.6); self.play(dot.animate.shift(RIGHT*2),run_time=.7); wob=VGroup(Line([-1,-1.6,0],[1,-1.6,0],color=DIM),Line([-.7,-1.8,0],[.7,-1.4,0],color=DIM)); self.play(Create(wob),run_time=.5); pulse(self,(0,0)); finish(self)
class B01_Degree(Scene):
 def construct(self):
  bit=tile('0 / 1',(0,1.5)); self.play(FadeIn(bit),run_time=.4); b=bar((0,-.2),.68); self.play(Transform(bit,b),run_time=.8); pulse(self,(.8,-.2)); finish(self)
class B02_TwoEngineers(Scene):
 def construct(self):
  ps=VGroup(peg((-4,-.5)),peg((4,-.5))); evidence=box((0,1.3),2.0,1.1,PALE); self.play(FadeIn(ps),FadeIn(evidence),run_time=.5); pri=VGroup(box((-4,-2),1.2,.55,KRAFT),box((4,-2),1.2,.55,KRAFT),txt('prior A',(-4,-1.35),32),txt('prior B',(4,-1.35),32)); self.play(FadeIn(pri),run_time=.5); bs=VGroup(bar((-2.7,.2),.35,'0.35'),bar((2.7,.2),.72,'0.72')).scale(.55); self.play(FadeIn(bs),run_time=.6); pulse(self,(0,1.3)); finish(self)
class B03_ModelWorld(Scene):
 def construct(self):
  m=box((-3,0),2.3,1.5,DARK); w=box((3,0),2.3,1.5,KRAFT); self.play(FadeIn(m),FadeIn(w),FadeIn(txt('model',(-3,1.25))),FadeIn(txt('world',(3,1.25))),run_time=.5); page=box((0,.2),1.0,1.3,PALE); self.play(FadeIn(page),Create(DashedLine([-1.8,0,0],[1.8,0,0],color=DIM)),run_time=.6); self.play(FadeIn(txt('≠',(0,-1.5),72)),run_time=.4); pulse(self,(0,0)); finish(self)
class B04_SampleSpace(Scene):
 def construct(self):
  tr=tray([1,2,3,4,5,6]); [tr[1][i][1].shift(UP*.48) for i in (1,3,5)]; self.play(FadeIn(tr),run_time=.6); ev=VGroup(tr[1][1],tr[1][3],tr[1][5]); self.play(*[x.animate.shift(UP*1.4) for x in ev],run_time=.8); self.play(FadeIn(txt('event: even',(0,2.95),42)),run_time=.4); pulse(self,(0,.6)); finish(self)
class B05_Nonnegative(Scene):
 def construct(self):
  b=bar((0,0),.45,'P(A) ≥ 0'); self.play(FadeIn(b),run_time=.5); stop=Line([-2.18,-.7,0],[-2.18,.7,0],color=TERRA,stroke_width=10); self.play(Create(stop),run_time=.4); arr=Arrow([-1.2,1.9,0],[-2.1,.8,0],color=INK,buff=.1); self.play(GrowArrow(arr),run_time=.5); pulse(self,(-2.18,0)); finish(self)
class B06_Normalization(Scene):
 def construct(self):
  p=peg((-4,0)); frame=Rectangle(width=2,height=4,stroke_color=INK,stroke_width=5).move_to([1,0,0]); sick=Rectangle(width=1.8,height=1.5,fill_color=TERRA,fill_opacity=1,stroke_width=0).align_to(frame,DOWN).shift(UP*.1); healthy=Rectangle(width=1.8,height=2.25,fill_color=KRAFT,fill_opacity=1,stroke_width=0).next_to(sick,UP,buff=0); self.play(FadeIn(p),Create(frame),run_time=.5); self.play(FadeIn(sick),FadeIn(txt('sick',(3, -1.1))),run_time=.4); self.play(FadeIn(healthy),FadeIn(txt('healthy',(3,.9))),run_time=.4); self.play(FadeIn(txt('P(Ω) = 1',(1,2.7),58)),run_time=.4); pulse(self,(1,0)); finish(self)
class B07_Additivity(Scene):
 def construct(self):
  ev=VGroup(tile(2,(-4,1.3)),tile(4,(-3,1.3)),tile(6,(-2,1.3))); five=tile(5,(3,1.3)); self.play(FadeIn(ev),FadeIn(five),run_time=.5); self.play(FadeIn(txt('disjoint',(0,2.3),44)),run_time=.3); a=Rectangle(width=2,height=1.2,fill_color=KRAFT,fill_opacity=1,stroke_color=INK).move_to([-1,-1,0]); b=Rectangle(width=1,height=1.2,fill_color=TERRA,fill_opacity=1,stroke_color=INK).next_to(a,RIGHT,buff=0); self.play(FadeIn(a),FadeIn(b),run_time=.6); self.play(FadeIn(txt('P(A ∪ B) = P(A) + P(B)',(0,-2.4),48)),run_time=.5); pulse(self,(0,-1)); finish(self)
class B08_Foundation(Scene):
 def construct(self):
  pillars=VGroup(*[Rectangle(width=1,height=3,fill_color=KRAFT,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([x,-.6,0]) for x in (-3,0,3)]); labs=VGroup(txt('≥ 0',(-3,-.6)),txt('= 1',(0,-.6)),txt('adds',(3,-.6))); top=Rectangle(width=8.5,height=.5,fill_color=DARK,fill_opacity=1,stroke_color=INK).move_to([0,1.2,0]); self.play(FadeIn(pillars),FadeIn(labs),run_time=.6); self.play(FadeIn(top),run_time=.4); ideas=VGroup(txt('conditional',(-3,2)),txt('Bayes',(0,2)),txt('central limit',(3,2))); self.play(FadeIn(ideas),run_time=.6); pulse(self,(0,1.2)); finish(self)
class B09_Consequences(Scene):
 def construct(self):
  empty=RoundedRectangle(width=2.6,height=1.2,corner_radius=.2,stroke_color=INK,stroke_width=5).move_to([-3,0,0]); self.play(Create(empty),FadeIn(txt('P(∅) = 0',(-3,-1.2),48)),run_time=.5); full=Rectangle(width=4.2,height=.7,stroke_color=INK,stroke_width=4).move_to([2.5,0,0]); a=Rectangle(width=2.6,height=.55,fill_color=TERRA,fill_opacity=1,stroke_width=0).align_to(full,LEFT).shift(RIGHT*.08); c=Rectangle(width=1.35,height=.55,fill_color=KRAFT,fill_opacity=1,stroke_width=0).next_to(a,RIGHT,buff=.08); self.play(FadeIn(full),FadeIn(a),FadeIn(c),run_time=.5); self.play(FadeIn(txt('P(Aᶜ) = 1 − P(A)',(2.5,-1.2),48)),run_time=.4); pulse(self,(2.5,0)); finish(self)
class B10_Complement(Scene):
 def construct(self):
  tr=tray([1,2,3,4,5,6]); [tr[1][i][1].shift(UP*.48) for i in (1,3,5)]; self.play(FadeIn(tr),run_time=.5); self.play(*[tr[1][i].animate.shift(UP*1.35) for i in (1,3,5)],run_time=.7); self.play(FadeIn(txt('A = even',(0,2.95))),FadeIn(txt('Aᶜ = 1, 3, 5',(0,-2.0))),run_time=.5); frame=Rectangle(width=7,height=.22,fill_color=INK,fill_opacity=1,stroke_width=0).move_to([0,-2.8,0]); self.play(FadeIn(frame),run_time=.3); pulse(self,(0,.5)); finish(self)
class B11_Close(Scene):
 def construct(self):
  p=VGroup(peg((-4,-.8)),peg((4,-.8))); self.play(FadeIn(p),run_time=.5); b=bar((0,.2),.38); b2=bar((0,.2),.72); self.play(FadeIn(b),run_time=.5); self.play(Transform(b,b2),run_time=.6); self.play(FadeIn(txt('given what each knows',(0,2.1),48)),run_time=.4); pulse(self,(0,.2)); finish(self)
