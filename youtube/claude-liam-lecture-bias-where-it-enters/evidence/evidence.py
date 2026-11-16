"""evidence.py — every worked number the lecture shows (EXECUTABLE-EVIDENCE). Seeded, standard library + numpy.
Constructed illustrations, not empirical results: the film labels them so. Writes evidence.json beside this file."""
import json, math, itertools
import numpy as np
from pathlib import Path
HERE = Path(__file__).resolve().parent
rng = np.random.default_rng(7)
out = {}

# A. A biased estimator does not improve with more data (selection depends on the outcome)
p_true, keep1, keep0 = 0.30, 0.40, 0.80
limit = p_true*keep1 / (p_true*keep1 + (1-p_true)*keep0)
rows = []
for n in (10, 100, 1000, 10000):
    ests = []
    for _ in range(2000):
        # draw until n people are KEPT by the filter (keep prob depends on outcome)
        y = rng.random(int(n*6)) < p_true
        k = rng.random(y.size) < np.where(y, keep1, keep0)
        kept = y[k][:n]
        while kept.size < n:
            y = rng.random(n*6) < p_true; k = rng.random(y.size) < np.where(y, keep1, keep0)
            kept = np.concatenate([kept, y[k]])[:n]
        ests.append(kept.mean())
    ests = np.array(ests)
    rows.append({"n": n, "mean": round(float(ests.mean()), 4), "sd": round(float(ests.std()), 4),
                 "samples": [round(float(v), 4) for v in ests[:400]]})
out["A"] = {"true": p_true, "keep_if_outcome": keep1, "keep_if_no_outcome": keep0, "limit": round(limit, 4), "rows": rows}

# B. Inverse probability weighting when the selection variable WAS recorded
n = 20000
y = rng.random(400000) < p_true
keep = rng.random(y.size) < np.where(y, keep1, keep0)
yk = y[keep][:n]; pk = np.where(yk, keep1, keep0)
out["B"] = {"naive": round(float(yk.mean()), 4), "ipw": round(float(np.sum(yk/pk)/np.sum(1/pk)), 4), "true": p_true}

# C. Cohen's kappa, blinded vs unblinded annotators (constructed counts)
def kappa(t):
    a, b, c, d = t[0][0], t[0][1], t[1][0], t[1][1]; N = a+b+c+d
    po = (a+d)/N; pe = ((a+b)*(a+c) + (c+d)*(b+d))/N**2
    return {"counts": t, "po": round(po, 3), "pe": round(pe, 3), "kappa": round((po-pe)/(1-pe), 3)}
out["C"] = {"blinded": kappa([[40, 10], [10, 40]]), "unblinded": kappa([[40, 10], [30, 20]])}

# D. Funnel plot: effect vs precision, with and without publication filtering
rng2 = np.random.default_rng(11)
studies = []
for _ in range(90):
    ni = int(rng2.integers(20, 400)); se = 1/math.sqrt(ni); eff = rng2.normal(0.20, se)
    z = eff/se; sig = z > 1.96
    pub = bool(sig or rng2.random() < 0.12)
    studies.append({"se": round(se, 4), "eff": round(float(eff), 4), "pub": pub})
allm = np.mean([s["eff"] for s in studies]); pubm = np.mean([s["eff"] for s in studies if s["pub"]])
out["D"] = {"true": 0.20, "mean_all": round(float(allm), 3), "mean_published": round(float(pubm), 3),
            "n_all": len(studies), "n_pub": sum(s["pub"] for s in studies), "studies": studies}

# E. Sampling bias: reweight strata by population share over sample share
pop = {"Credentialed": 0.30, "Other office": 0.50, "Other": 0.20}
smp = {"Credentialed": 0.60, "Other office": 0.30, "Other": 0.10}
out["E"] = {"rows": [{"stratum": k, "pop": pop[k], "sample": smp[k], "weight": round(pop[k]/smp[k], 2)} for k in pop]}

# F. The impossibility, as arithmetic: equal PPV v, equal TPR t, base rates p
v, t = 0.60, 0.70
rowsF = []
for name, p in (("Group one", 0.30), ("Group two", 0.50)):
    f = p*t*(1-v)/((1-p)*v)
    ppv_check = p*t/(p*t + (1-p)*f)
    rowsF.append({"group": name, "p": p, "t": t, "f": round(f, 4), "ppv_check": round(ppv_check, 4)})
out["F"] = {"v": v, "t": t, "rows": rowsF}

# G. Leverage on a constructed graph: count the paths from the protected attribute to the outcome
edges = [("A","P"),("A","D"),("A","L"),("A","R"),("A","C"),("P","F"),("P","R"),("P","C"),("D","M"),("L","M"),("F","M"),("M","O"),("O","R"),("O","C"),("R","K"),("C","K")]
names = {"A":"protected attribute","P":"proxies","D":"training sample","L":"labels","F":"features","M":"model","O":"model output","R":"reviewer","C":"threshold and appeals","K":"outcome"}
adj = {}
for a, b in edges: adj.setdefault(a, []).append(b)
paths = []
def dfs(u, path):
    if u == "K": paths.append(path[:]); return
    for w in adj.get(u, []): dfs(w, path+[w])
dfs("A", ["A"])
def blocked(nodes): return sum(1 for p_ in paths if any(n_ in p_[1:-1] for n_ in nodes))
out["G"] = {"edges": edges, "names": names, "paths": ["".join(p_) for p_ in paths], "n_paths": len(paths),
            "blocked": {"model (team one)": blocked(["M"]), "training sample (team two)": blocked(["D"]),
                        "labels": blocked(["L"]), "reviewer (team three)": blocked(["R"]), "threshold and appeals": blocked(["C"]), "proxies": blocked(["P"]),
                        "reviewer and threshold together": blocked(["R","C"])}}
(HERE/"evidence.json").write_text(json.dumps(out, indent=1))

print("A. A biased estimator does not improve with n")
print("   true rate 0.30; keeps 40% of positives, 80% of negatives")
print(f"   the estimate converges to {limit:.4f}, not 0.30")
for r in rows: print(f"   n={r['n']:>6}  mean estimate={r['mean']:.4f}  spread (sd)={r['sd']:.4f}")
print(f"B. IPW: naive={out['B']['naive']:.4f}  weighted={out['B']['ipw']:.4f}  true=0.30")
print(f"C. Cohen's kappa: blinded={out['C']['blinded']['kappa']}  unblinded={out['C']['unblinded']['kappa']}")
print(f"D. Meta-analysis, true effect 0.20: all {out['D']['n_all']} studies mean={out['D']['mean_all']}")
print(f"   published {out['D']['n_pub']} studies mean={out['D']['mean_published']}")
print("E. Weights:", {r['stratum']: r['weight'] for r in out['E']['rows']})
print(f"F. PPV {v} and TPR {t} in both groups, so the FPR is forced:")
for r_ in rowsF: print(f"   {r_['group'].lower()} (base rate {r_['p']:.2f}): FPR {r_['f']:.4f}")
print(f"G. {len(paths)} paths from attribute to outcome; fix -> paths blocked:")
for k_, v_ in out["G"]["blocked"].items(): print(f"   {k_}: {v_}")
