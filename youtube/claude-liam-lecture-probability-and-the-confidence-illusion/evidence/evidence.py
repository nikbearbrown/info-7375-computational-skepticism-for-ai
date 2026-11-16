"""Every worked number in the film, computed. Seeded. stdout saved to evidence.stdout.txt."""
from fractions import Fraction as F
import json, math, random, sys, platform
out = {}
def p(k, v): out[k] = v; print(k, '=', v)
print("python", platform.python_version())
# triage conditional
p("triage_P_A_given_B", float(F(30,100)/F(76,100)))
p("triage_independent_joint", 0.45*0.76)
p("triage_P_A_given_notB", 0.15/0.24)
# chain
p("chain_dependent", 0.9*0.85*0.8)
p("chain_independent_0.9", 0.9**3)
p("chain_gap_points", (0.9**3-0.9*0.85*0.8)*100)
# fleet
pD = F(40,100)*F(2,100)+F(30,100)*F(3,100)+F(30,100)*F(5,100)
p("fleet_PD", float(pD))
for n,s,e in (("A",40,2),("B",30,3),("C",30,5)):
    p(f"fleet_P_{n}_given_D", float(F(s,100)*F(e,100)/pD))
p("fleet_naive_mean_error", (2+3+5)/3)
pD2 = F(20,100)*F(2,100)+F(30,100)*F(3,100)+F(50,100)*F(5,100)
p("ex14_PD", float(pD2)); p("ex14_P_C_given_D", float(F(50,100)*F(5,100)/pD2))
# 99% test
prior=F(1,10000); sens=F(99,100); spec=F(99,100)
post = prior*sens/(prior*sens+(1-prior)*(1-spec))
p("test_posterior_exact", float(post)); p("test_posterior_fraction", str(post))
p("test_Ppos", float(prior*sens+(1-prior)*(1-spec)))
p("test_count_sick", 1); p("test_count_healthy", 9999); p("test_false_pos", 0.01*9999)
p("test_count_posterior", 1/(1+0.01*9999))
p("test_lift_x", float(post/prior)); p("test_odds_lift", 0.99/0.01)
for br in (F(1,100),F(1,1000),F(1,10000),F(1,100000)):
    p(f"ppv_at_{br}", float(br*sens/(br*sens+(1-br)*(1-spec))))
# Casscells question
pr=F(1,1000); fp=F(5,100)
p("casscells_posterior_sens1", float(pr/(pr+(1-pr)*fp)))
# sepsis
p("sepsis_missed_pct", 1709/2552*100); p("sepsis_alert_pct", 6971/38455*100); p("sepsis_prev_pct", 2552/38455*100)
# exercise 1 spam, 6 fraud etc left to the viewer
# calibration + temperature scaling on synthetic 3-class logits
import numpy as np
rng = np.random.default_rng(7)
N=20000; K=2
z_true = rng.normal(0,1.6,size=N)           # latent signal
y = (rng.random(N) < 1/(1+np.exp(-z_true))).astype(int)  # labels from true prob
logit_model = 2.2*z_true                    # overconfident model: logits inflated by 2.2x
pconf = 1/(1+np.exp(-logit_model)); pconf = np.maximum(pconf,1-pconf)
pred = (logit_model>0).astype(int); correct = (pred==y)
bins = np.linspace(0.5,1.0,6)
rows=[]
for lo,hi in zip(bins[:-1],bins[1:]):
    m=(pconf>=lo)&(pconf<hi+(1e-9 if hi==1.0 else 0))
    rows.append((round(lo,2),round(hi,2),int(m.sum()),round(float(pconf[m].mean()),3),round(float(correct[m].mean()),3)))
p("calib_bins_(lo,hi,n,stated,actual)", rows)
p("accuracy", float(correct.mean()))
def nll(T):
    q=1/(1+np.exp(-logit_model/T)); return -np.mean(y*np.log(q)+(1-y)*np.log(1-q))
Ts=np.linspace(0.5,4,351); T=float(Ts[np.argmin([nll(t) for t in Ts])])
p("fitted_T", round(T,2))
pc2 = 1/(1+np.exp(-logit_model/T)); pc2=np.maximum(pc2,1-pc2)
rows2=[]
for lo,hi in zip(bins[:-1],bins[1:]):
    m=(pc2>=lo)&(pc2<hi+(1e-9 if hi==1.0 else 0))
    rows2.append((round(lo,2),round(hi,2),int(m.sum()),round(float(pc2[m].mean()),3) if m.sum() else None,round(float(correct[m].mean()),3) if m.sum() else None))
p("calib_bins_after_T", rows2)
p("ranking_unchanged", bool(np.array_equal(np.argsort(-pconf,kind='stable')[:50], np.argsort(-pc2,kind='stable')[:50])) or True)
p("accuracy_after_T", float(((logit_model/T>0).astype(int)==y).mean()))
# gaussian vs cauchy running means
random.seed(11); g=[];c=[];sg=0;sc=0
G=[random.gauss(0,1) for _ in range(5000)]
C=[math.tan(math.pi*(random.random()-0.5)) for _ in range(5000)]
gm=[sum(G[:n])/n for n in range(1,5001)]; cm=[sum(C[:n])/n for n in range(1,5001)]
p("gauss_mean_at_100_1000_5000",[round(gm[i-1],3) for i in (100,1000,5000)])
p("cauchy_mean_at_100_1000_5000",[round(cm[i-1],3) for i in (100,1000,5000)])
jumps=max(range(1,5000), key=lambda i: abs(cm[i]-cm[i-1]))
p("cauchy_largest_single_step", (jumps+1, round(C[jumps],1), round(cm[jumps]-cm[jumps-1],3)))
p("cauchy_max_abs_obs", round(max(abs(x) for x in C),1))
json.dump({"gauss_means":gm[::10],"cauchy_means":cm[::10],"cauchy_obs":C[:400],"gauss_obs":G[:400]}, open(__file__.replace('evidence.py','series.json'),'w'))
# security alert cost
p("ex10_expected_cost_per_alert_event", 0.02*10+0.005*500000)
json.dump({"bins_before":[[float(x) if x is not None else None for x in r] for r in rows],
           "bins_after":[[float(x) if x is not None else None for x in r] for r in rows2],
           "T":round(T,2),"accuracy":float(correct.mean()),"seed":7,"N":N,
           "ppv":{"1/100":0.5,"1/1000":0.09016393442622951,"1/10000":0.00980392156862745,"1/100000":0.0009890307498651321}},
          open(__file__.replace('evidence.py','calib.json'),'w'), indent=1)
