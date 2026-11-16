"""world.py — the constructed table behind tldr-missing-is-not-one-thing.

The chapter states ONE number for this case: `income` is 18% missing (exercise 8),
with the blanks co-occurring with the `age < 25` subgroup (the MAR reading) — and,
in its MNAR example, "high earners suppress their income". Everything else here is
a CONSTRUCTED illustration (captioned as such on screen): 50 rows, 9 blanks
(= 18% exactly), a deterministic age/income table, and three worlds that each
blank exactly 9 cells. No dollar figures are spoken or shown; the film shows only
DIRECTION (where a mean-fill lands relative to the truth), which is the chapter's
claim: "standard imputation produces bias in exactly the direction I cannot measure".
Every relation the film shows is asserted below at import.
"""
import random

N = 50
K = 9
assert K / N == 0.18                                  # the chapter's 18%, exactly
YOUNG = 25                                            # exercise 8: age < 25

_rng = random.Random(20260923)
_ages_young = [19, 20, 21, 22, 22, 23, 23, 24, 24, 21, 20, 23]          # 12 rows under 25
_ages_old = [_rng.randint(25, 64) for _ in range(N - len(_ages_young))]  # 38 rows 25–64
AGES = _ages_young + _ages_old
_rng.shuffle(AGES)                                    # file order is arbitrary — the matrix draws rows as the table has them
assert len(AGES) == N and sum(a < YOUNG for a in AGES) == 12

def _income(age, r):
    # a plausible shape: rises gently with age, plus a high-earner tail that is NOT an age effect
    # (so the top earners are spread across the age order — sorting by age cannot line them up)
    base = 28 + 0.9 * (age - 18) + r.gauss(0, 8)
    if r.random() < 0.20: base *= r.uniform(2.0, 2.8)            # the high-earner tail
    return max(18.0, min(160.0, base))                            # thousands, clamped

_r2 = random.Random(118)
INCOME = [_income(a, _r2) for a in AGES]
TRUE_MEAN = sum(INCOME) / N

def _mean(xs): return sum(xs) / len(xs)

# ── the three worlds: which 9 rows are blank in `income` ─────────────────────
# seeds are chosen so one draw's sampling noise stays below a hair on the drawn axis;
# the DIRECTION claims are checked over 2,000 fresh random draws further down (not seed luck)
MCAR = sorted(random.Random(28).sample(range(N), K))                # nine cells wiped at random (a coin flip per page)
MCAR2 = sorted(random.Random(30).sample(range(N), K))               # a second random wipe — the "vary, replay" instance
MAR = sorted(random.Random(9).sample([i for i in range(N) if AGES[i] < YOUNG], K))   # 9 of the 12 under-25 rows, at random within the band
_by_income = sorted(range(N), key=lambda i: -INCOME[i])
MNAR = sorted(_by_income[:K])                                       # the 9 highest earners left it blank
WORLDS = {"mcar": MCAR, "mcar2": MCAR2, "mar": MAR, "mnar": MNAR}
for w in WORLDS.values(): assert len(w) == K and len(set(w)) == K
assert all(AGES[i] < YOUNG for i in MAR)
assert min(INCOME[i] for i in MNAR) > max(INCOME[i] for i in range(N) if i not in MNAR)

# ── fills ────────────────────────────────────────────────────────────────────
def observed(blank): return [i for i in range(N) if i not in blank]

def fill_column_mean(blank):
    """fill every blank with the mean of the rows you can see; return the filled column's mean."""
    m = _mean([INCOME[i] for i in observed(blank)])
    return _mean([m if i in blank else INCOME[i] for i in range(N)])

def fill_band_mean(blank):
    """fill each blank with the mean of the VISIBLE rows in its age band (<25 / ≥25)."""
    obs = observed(blank)
    band = {True: [INCOME[i] for i in obs if AGES[i] < YOUNG], False: [INCOME[i] for i in obs if AGES[i] >= YOUNG]}
    m = {k: _mean(v) for k, v in band.items()}
    return _mean([m[AGES[i] < YOUNG] if i in blank else INCOME[i] for i in range(N)])

FILL = {
    ("mcar", "column"): fill_column_mean(MCAR),
    ("mcar2", "column"): fill_column_mean(MCAR2),
    ("mar", "column"): fill_column_mean(MAR),
    ("mar", "band"): fill_band_mean(MAR),
    ("mnar", "column"): fill_column_mean(MNAR),
    ("mnar", "band"): fill_band_mean(MNAR),
}
GAP = {k: v - TRUE_MEAN for k, v in FILL.items()}

# the relations the film shows — DIRECTION only, never a dollar figure
TOL = 0.04 * TRUE_MEAN
assert abs(GAP[("mcar", "column")]) < TOL,          "MCAR: a mean fill lands on the truth (within noise)"
assert abs(GAP[("mcar2", "column")]) < TOL
assert GAP[("mar", "column")] > TOL,                "MAR: a column-mean fill lands HIGH (the missing young earn less)"
assert abs(GAP[("mar", "band")]) < TOL,             "MAR: conditioning on the visible column recovers the truth"
assert GAP[("mnar", "band")] < -3 * TOL,            "MNAR: even the band fill lands LOW — the missing ARE the high earners"
assert GAP[("mnar", "column")] < -3 * TOL
assert abs(GAP[("mnar", "band")]) > 3 * abs(GAP[("mcar", "column")])

# the sorts: under which order do the blanks form one block?
def block_under(order_key, blank):
    """rank positions of the blank rows when rows are sorted by order_key; a block = 9 consecutive ranks."""
    order = sorted(range(N), key=order_key)
    ranks = sorted(order.index(i) for i in blank)
    return ranks[-1] - ranks[0] == K - 1

assert not block_under(lambda i: i, MCAR) and not block_under(lambda i: AGES[i], MCAR)
assert block_under(lambda i: -INCOME[i], MNAR)                       # world 3 lines up ONLY under the hidden sort
assert not block_under(lambda i: i, MNAR) and not block_under(lambda i: AGES[i], MNAR)
assert not block_under(lambda i: i, MAR)
# world 2 under the AGE sort: all 9 blanks sit inside the 12-row under-25 band at the top
_age_order = sorted(range(N), key=lambda i: AGES[i])
assert max(_age_order.index(i) for i in MAR) < 12

# a categorical column with no order of its own (the "city" stripe); a sort by it is just another shuffle
CITY = [random.Random(11 + i).randint(0, 4) for i in range(N)]
ORDERS = {
    "file": list(range(N)),
    "age": sorted(range(N), key=lambda i: (AGES[i], i)),
    "city": sorted(range(N), key=lambda i: (CITY[i], i)),
    "truth": sorted(range(N), key=lambda i: (-INCOME[i], i)),
    "outcome": sorted(range(N), key=lambda i: (0 if i in MNAR else 1, i)),   # the patients reading: the same 9 rows, "died" first
}
def rank_of(order, i): return ORDERS[order].index(i)
def is_block(order, blank):
    ranks = sorted(rank_of(order, i) for i in blank); return ranks[-1] - ranks[0] == K - 1
assert not is_block("city", MNAR) and not is_block("city", MCAR) and not is_block("city", MAR)
assert is_block("truth", MNAR) and is_block("outcome", MNAR)
assert all(rank_of("age", i) < 12 for i in MAR)                     # world 2 lines up under the AGE sort (the under-25 band)
assert not is_block("age", MNAR) and not is_block("age", MCAR)
for w_ in (MCAR, MCAR2, MNAR):
    for o_ in ("file", "age", "city"): assert not is_block(o_, w_)
assert not is_block("truth", MCAR) and not is_block("truth", MCAR2)

# ── robustness: the direction claims hold over fresh random draws, not just these seeds ──
def _robust(trials=2000):
    rr = random.Random(99); young = [i for i in range(N) if AGES[i] < YOUNG]
    mc = [fill_column_mean(rr.sample(range(N), K)) - TRUE_MEAN for _ in range(trials)]
    ma_c = [fill_column_mean(rr.sample(young, K)) - TRUE_MEAN for _ in range(trials)]
    ma_b = [fill_band_mean(rr.sample(young, K)) - TRUE_MEAN for _ in range(trials)]
    return _mean(mc), _mean(ma_c), min(ma_c), _mean(ma_b)
ROBUST = _robust()
assert abs(ROBUST[0]) < 0.5,  "MCAR: across draws the mean fill is unbiased"
assert ROBUST[2] > 0,         "MAR: EVERY random under-25 draw puts the column-mean fill above the truth"
assert abs(ROBUST[3]) < 1.0,  "MAR: across draws the age-band fill is unbiased"

# the drawn income axis: a window, no numbers spoken or shown — the film shows direction only
AX_LO, AX_HI = 40.0, 90.0
assert AX_LO < TRUE_MEAN < AX_HI and all(AX_LO < v < AX_HI for v in FILL.values())

if __name__ == "__main__":
    print(f"N={N} K={K} true mean={TRUE_MEAN:.1f}")
    for k, v in GAP.items(): print(f"  {k}: fill−truth = {v:+.1f}")
    print("MCAR", MCAR); print("MAR ", MAR); print("MNAR", MNAR)
    print("income range", min(INCOME), max(INCOME))
    print("robust (mcar mean gap, mar col mean gap, mar col min gap, mar band mean gap):", [round(x, 2) for x in ROBUST])
