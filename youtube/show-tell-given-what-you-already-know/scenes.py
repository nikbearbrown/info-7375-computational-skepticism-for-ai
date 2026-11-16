from manim import *
import json,os
BG='#F2F0E9';INK='#3D3929';ACC='#8F3F27';K='#C7AE86';P='#F3E9D8';D='#26221F';config.background_color=BG
try:S=json.load(open(os.path.join(os.path.dirname(__file__),'beat_sheet.json')));T={b['beat_id']:float(b.get('actual_duration_s')or b.get('estimated_duration_s',9)) for b in S['beats']}
except:T={}
def text(x,p,z=42):return Text(x,font='EB Garamond',font_size=z,color=INK).move_to([*p,0])
def block(p,w=1.2,h=.7,c=K):return Rectangle(width=w,height=h,fill_color=c,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([*p,0])
def peg(p):return VGroup(block((p[0],p[1]-.25),.55,.8,K),Circle(.23,fill_color=P,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([p[0],p[1]+.35,0]))
def finish(s):
 bid=type(s).__name__.split('_')[0];s.wait(max(.05,T.get(bid,9)-float(s.renderer.time)-.15))
def draw(s,i):
 y=((i%3)-1)*.25; left=block((-3,y),1.7,1.0,K); right=block((3,-y),1.7,1.0,P); mid=RoundedRectangle(width=2.2,height=.65,corner_radius=.18,fill_color=ACC,fill_opacity=1,stroke_color=INK,stroke_width=4).move_to([0,0,0]);
 s.play(FadeIn(left),FadeIn(right),run_time=.45);s.play(FadeIn(mid),run_time=.4)
 labels=['symmetry → number','trials → limit','7 / 20','9 / 60 → 1 / 6','this case now','prior → evidence → posterior','partial information','P(A | B) = P(A ∩ B) / P(B)','Ω shrinks to B','{4,5,6} → {4,6}','report + context','0.30 / 0.76 ≈ 0.395','45% → 39.5%','0.08 / 0.40 = 0.20','same axioms · smaller world']
 lab=text(labels[i],(0,1.65),46);s.play(FadeIn(lab),run_time=.45)
 if i in (1,2,3):
  dots=VGroup(*[Dot([-2.5+k*.5,-1.8,0],radius=.1,color=INK) for k in range(10)]);s.play(FadeIn(dots),run_time=.4)
 elif i in (7,8,9):
  tray=RoundedRectangle(width=5.3,height=1.0,corner_radius=.2,stroke_color=INK,stroke_width=5).move_to([0,-1.8,0]);s.play(Create(tray),run_time=.4)
 elif i in (10,11,12,13):s.play(FadeIn(peg((0,-1.8))),run_time=.4)
 else:s.play(Create(Line([-2,-1.7,0],[2,-1.7,0],color=INK,stroke_width=6)),run_time=.4)
 ring=Circle(.8,color=INK,stroke_width=5).move_to([0,0,0]);s.play(GrowFromCenter(ring),run_time=.25);s.play(FadeOut(ring),run_time=.25);finish(s)
class B00_TwoWays(Scene):
 def construct(self):draw(self,0)
class B01_Classical(Scene):
 def construct(self):draw(self,1)
class B02_Frequentist(Scene):
 def construct(self):draw(self,2)
class B03_DieFrequency(Scene):
 def construct(self):draw(self,3)
class B04_OneOff(Scene):
 def construct(self):draw(self,4)
class B05_Bayesian(Scene):
 def construct(self):draw(self,5)
class B06_Engine(Scene):
 def construct(self):draw(self,6)
class B07_Definition(Scene):
 def construct(self):draw(self,7)
class B08_Shrink(Scene):
 def construct(self):draw(self,8)
class B09_DieConditional(Scene):
 def construct(self):draw(self,9)
class B10_Deployment(Scene):
 def construct(self):draw(self,10)
class B11_Triage(Scene):
 def construct(self):draw(self,11)
class B12_Signal(Scene):
 def construct(self):draw(self,12)
class B13_Spam(Scene):
 def construct(self):draw(self,13)
class B14_SmallerWorld(Scene):
 def construct(self):draw(self,14)
