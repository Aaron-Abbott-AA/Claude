#!/usr/bin/env python3
"""Referee check (GLO audit): Proposition PV exhaustively, OB1(c) step-4 algebra symbolically, TH degree bound.
Run:  nice -n 19 python3 -I glo_pv_alg.py"""
import random, itertools
import galois, sympy as sp

print(f"glo_pv_alg galois {galois.__version__} sympy {sp.__version__}")
# (a) PV: c_i in F_q, d_i = kappa c_i^Q, kappa^{Q+1} = 1  =>  Delta*Omega1 = 0   (including zeros of c_i)
for Q, N, mode in [(4, 4, 'all'), (8, 6, 'all'), (16, 8, 20000), (32, 10, 5000)]:
    F = galois.GF(2 ** N)
    els = list(F.elements)
    kap = [x for x in els if x != 0 and x ** (Q + 1) == 1]
    assert len(kap) == Q + 1
    rng = random.Random(Q)
    pairs = itertools.product(els, repeat=2) if mode == 'all' else ((rng.choice(els), rng.choice(els)) for _ in range(mode))
    bad = tot = 0; dpow_bad = 0
    for c0, c1 in pairs:
        for k in (kap if mode == 'all' else [rng.choice(kap)]):
            d0, d1 = k * c0 ** Q, k * c1 ** Q
            Dl = c1 * d0 ** 2 + d1 * c0 ** 2
            Om = c0 ** 4 * d1 ** Q * Dl ** (Q - 1) + c1 * d0 ** (4 * Q)
            tot += 1
            if Dl * Om != 0: bad += 1
            if Dl != 0 and Dl ** (Q - 1) != k ** (2 * Q - 1): dpow_bad += 1
    print(f"(a) PV Q={Q} over GF(2^{N}) [{mode}]: {tot} pairs, Delta*Omega1 != 0 in {bad}; Delta^(Q-1) != kappa^(2Q-1) in {dpow_bad}")

# (b) OB1(c) step 4, symbolic in Q: w^2 ((w+1)^2)^{Q-1} == s^{2(Q-1)}  <=>  c1 d0^{4Q} == c0^4 d1^Q Delta^{Q-1}
c0, c1, d0, d1, Dl, Q = sp.symbols('c0 c1 d0 d1 Delta Q', positive=True)
y0 = c0 / d0
w2 = c1 * d0 ** 2 / (d1 * c0 ** 2)
wp12 = Dl / (d1 * c0 ** 2)
sQ1 = y0 * Dl ** (Q - 1) / (c0 * d0 ** 2) ** (Q - 1)        # s^{Q-1}
lhs = w2 * wp12 ** (Q - 1)
rhs = sQ1 ** 2
ratio = sp.simplify(sp.expand_log(sp.log(lhs / rhs), force=True) - sp.expand_log(sp.log(c1 * d0 ** (4 * Q) / (c0 ** 4 * d1 ** Q * Dl ** (Q - 1))), force=True))
print(f"(b) OB1(c) algebra: log(LHS/RHS) - log(c1 d0^4Q / (c0^4 d1^Q Delta^(Q-1))) simplifies to: {ratio}")
# also w^2 and (w+1)^2 identities and s formula from the tau^1 equation (pure algebra in char 2 verified in GF)
F = galois.GF(2 ** 9); rng = random.Random(5); bad = 0
Qn = 8
for _ in range(300):
    a0 = F(rng.randrange(1, 512)); d0n = F(rng.randrange(1, 512)); c1n = F(rng.randrange(1, 512)); d1n = F(rng.randrange(1, 512))
    c0n = d0n * a0 ** (Qn - 1)      # alpha0 = a0 in F
    Dn = c1n * d0n ** 2 + d1n * c0n ** 2
    r1 = c1n * a0 ** 2 + d1n * a0 ** (2 * Qn)
    s = Dn * a0 / (c0n * d0n ** 2)
    if r1 / (c0n * a0) != s: bad += 1   # beta^Q + beta = r1/(c0 alpha0) must equal s
print(f"(b') s = alpha0*Delta/(c0 d0^2) from the tau^1 equation: {bad} failures / 300 (GF(2^9), Q=8)")

# (c) TH degree bound deg(Delta*Omega1) <= (4Q+4) delta, and homogeneity of degree 4Q+4
X = sp.symbols('X')
def P(e): return sp.Poly(e, X, modulus=2)
rng = random.Random(11); worst = 0; bad = 0
for Qn in (4, 8):
    for _ in range(30):
        dl = rng.randint(1, 4)
        cs = [P(sum(rng.randint(0, 1) * X ** i for i in range(dl + 1)) + X ** rng.randint(0, dl)) for _ in range(4)]
        if any(c.is_zero for c in cs): continue
        c0p, c1p, d0p, d1p = cs
        delta = max(c.degree() for c in cs)
        Dp = c1p * d0p ** 2 + d1p * c0p ** 2
        Op = c0p ** 4 * d1p ** Qn * Dp ** (Qn - 1) + c1p * d0p ** (4 * Qn)
        prod = Dp * Op
        if not prod.is_zero:
            worst = max(worst, prod.degree() / ((4 * Qn + 4) * delta))
            if prod.degree() > (4 * Qn + 4) * delta: bad += 1
print(f"(c) TH: deg(Delta*Omega1) > (4Q+4)delta in {bad} random cases; worst ratio {worst:.3f}")
