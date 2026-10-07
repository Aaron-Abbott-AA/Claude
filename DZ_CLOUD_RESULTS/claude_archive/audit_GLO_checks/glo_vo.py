#!/usr/bin/env python3
"""Referee check (GLO audit): Proposition VO / Corollary DO / Theorem RLE / Corollary N1 / Example NG over L = F_2(X)
(F_2(X) is a subfield of F_q(X); every identity below is over F_2(X)).  Run:  nice -n 19 python3 -I glo_vo.py <seed>

(1) Planted twisted families: random B in F_2(X){tau} with b0 = 1 and random y in F_2(X)^*; solve the linear system
    C*B = D*phi(B)*y  (Theorem RLE (ii)) for (C, D) of degree a2; clear denominators.  Then A = B a0 (a0^{Q-1} = y)
    is a nonzero solution over L^sep, so VO must NOT trigger at any place.  Places tested: infinity, X, X+1 and
    every irreducible factor of the c_i, d_i, y and of numerators/denominators of the b_k.
    Also checked: y0 = c0/d0 equals y; b1 is a root of N1: y0 b^Q + b = Delta1/(c0 d0^2).
(2) DO == VO at infinity for random polynomial pairs with deg d0 > deg c0.
(3) Example NG: (N0); PTH 4A(iii) tests; VO at infinity triggers; Delta*Omega1 != 0 (GLS_1 fails, consistent).
(4) RLE negative controls on the TX-like family (the owner's ad hoc controls, reproduced)."""
import sys, random
from fractions import Fraction as Fr
import sympy as sp
from sympy.polys.matrices import DomainMatrix

X = sp.symbols('X')
K = sp.FF(2).frac_field(X)
def kc(e): return K.convert(e)
def poly(e): return sp.Poly(e, X, modulus=2)

def num_den(f):
    e = sp.together(K.to_sympy(f))
    n, d = sp.fraction(e)
    return poly(n), poly(d)

def vplace(f, pi):
    """valuation of f in K at place pi (a Poly irreducible) or 'inf'."""
    if f == K.zero: return None
    n, d = num_den(f)
    if pi == 'inf': return d.degree() - n.degree()
    def mult(p):
        m = 0
        while True:
            q, r = sp.div(p, pi)
            if not r.is_zero: return m
            p = q; m += 1
    return mult(n) - mult(d)

def vo(C, D, Q, pi):
    a2 = len(C) - 1
    v = lambda f: vplace(f, pi)
    th = Fr(v(C[0]) - v(D[0]), Q - 1)
    ok2 = True
    for i in range(1, a2 + 1):
        if C[i] != K.zero and not (v(C[i]) + (2 ** i) * th >= v(C[0]) + th): ok2 = False
        if D[i] != K.zero and not (v(D[i]) + Q * (2 ** i) * th >= v(C[0]) + th): ok2 = False
    thtop = Fr(v(C[a2]) - v(D[a2]), (Q - 1) * 2 ** a2)
    HYP.append(ok2)
    return ok2 and thtop < th

HYP = []   # records whether VO hypothesis (ii) held, to show the planted test is not vacuous

def rand_poly(rng, dmax, nonzero=True):
    while True:
        e = sum(rng.randint(0, 1) * X ** i for i in range(dmax + 1))
        if e != 0 or not nonzero: return e

def planted(rng, Q, nb, a2):
    b = [K.one] + [kc(rand_poly(rng, 2)) / kc(rand_poly(rng, 2)) for _ in range(nb)]
    y = kc(rand_poly(rng, 2)) / kc(rand_poly(rng, 2))
    rows = []
    for k in range(nb + a2 + 1):
        row = []
        for i in range(a2 + 1):
            j = k - i
            row.append(b[j] ** (2 ** i) if 0 <= j <= nb else K.zero)
        for i in range(a2 + 1):
            j = k - i
            row.append(y ** (2 ** k) * b[j] ** (Q * 2 ** i) if 0 <= j <= nb else K.zero)
        rows.append(row)
    M = DomainMatrix(rows, (len(rows), 2 * a2 + 2), K)
    ns = M.nullspace().to_Matrix()
    if ns.rows == 0: return None
    vec = [K.zero] * (2 * a2 + 2)
    for r in range(ns.rows):
        if rng.randint(0, 1) or r == 0:
            vec = [vec[t] + kc(ns[r, t]) for t in range(2 * a2 + 2)]
    # clear denominators
    dens = [num_den(x)[1] for x in vec if x != K.zero]
    l = dens[0]
    for d in dens[1:]: l = sp.lcm(l, d)
    vec = [x * kc(l.as_expr()) for x in vec]
    C, D = vec[:a2 + 1], vec[a2 + 1:]
    return b, y, C, D

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261007
    rng = random.Random(seed)
    print(f"glo_vo seed={seed} sympy {sp.__version__}")
    # (1)
    for Q in (4, 8):
        st = dict(inst=0, places=0, vo_triggered=0, y0_mismatch=0, n1_fail=0, rle_fail=0)
        tries = 0
        while st['inst'] < (14 if Q == 4 else 8) and tries < 200:
            tries += 1
            nb = rng.choice([1, 2]); a2 = nb + rng.choice([0, 1])
            r = planted(rng, Q, nb, a2)
            if r is None: continue
            b, y, C, D = r
            if any(x == K.zero for x in (C[0], D[0], C[a2], D[a2])): continue
            st['inst'] += 1
            y0 = C[0] / D[0]
            if y0 != y: st['y0_mismatch'] += 1
            # RLE (ii) identity re-verified coefficientwise
            for k in range(nb + a2 + 1):
                lhs = sum((C[i] * b[k - i] ** (2 ** i) for i in range(a2 + 1) if 0 <= k - i <= nb), K.zero)
                rhs = y0 ** (2 ** k) * sum((D[i] * b[k - i] ** (Q * 2 ** i) for i in range(a2 + 1) if 0 <= k - i <= nb), K.zero)
                if lhs != rhs: st['rle_fail'] += 1
            D1 = C[1] * D[0] ** 2 + D[1] * C[0] ** 2
            if y0 * b[1] ** Q + b[1] != D1 / (C[0] * D[0] ** 2): st['n1_fail'] += 1
            places = {'inf'}
            for x in list(C) + list(D) + [y] + b:
                if x == K.zero: continue
                for p in num_den(x):
                    for fac, _ in p.factor_list()[1]:
                        places.add(fac)
            places.add(poly(X)); places.add(poly(X + 1))
            for pi in places:
                st['places'] += 1
                if vo(C, D, Q, pi):
                    st['vo_triggered'] += 1
                    print("  VO TRIGGERED ON A SOLVABLE FAMILY:", Q, pi, C, D)
        st['hyp_ii_held'] = sum(HYP); HYP.clear()
        print(f"(1) planted twisted families Q={Q}: {st}")
    # (2) DO == VO at infinity
    agree = dis = 0
    for _ in range(300):
        Q = rng.choice([4, 8]); a2 = rng.choice([1, 2])
        C = [kc(rand_poly(rng, 5)) for _ in range(a2 + 1)]; D = [kc(rand_poly(rng, 5)) for _ in range(a2 + 1)]
        dg = lambda f: num_den(f)[0].degree()
        if not dg(D[0]) > dg(C[0]): continue
        th = Fr(dg(D[0]) - dg(C[0]), Q - 1)
        do = all(dg(C[i]) <= dg(C[0]) + (2 ** i - 1) * th and dg(D[i]) <= dg(C[0]) + (Q * 2 ** i - 1) * th for i in range(1, a2 + 1)) \
            and (dg(D[a2]) - dg(C[a2]) < 2 ** a2 * (dg(D[0]) - dg(C[0])))
        if do == vo(C, D, Q, 'inf'): agree += 1
        else: dis += 1
    print(f"(2) DO vs VO at infinity: agree {agree}, disagree {dis}")
    # (3) NG
    for Q in (4, 8, 16):
        C = [K.one, K.one]; D = [kc(X), K.one]
        tests = (C[0] != K.zero and D[0] != K.zero and C[1] != K.zero and D[1] != K.zero)
        D1 = C[1] * D[0] ** 2 + D[1] * C[0] ** 2
        Om = C[0] ** 4 * D[1] ** Q * D1 ** (Q - 1) + C[1] * D[0] ** (4 * Q)
        print(f"(3) NG Q={Q}: N0 {tests}; VO@inf {vo(C, D, Q, 'inf')}; VO@X {vo(C, D, Q, poly(X))}; "
              f"Delta = {K.to_sympy(D1)}; Delta*Omega1 == 0: {D1 * Om == K.zero}")
    # (4) RLE negative controls (TX-like, y0 = X^{Q-1})
    for Q in (4, 8, 16):
        C = [kc(X ** (Q + 1) * (1 + X ** (Q - 1))), K.one]; D = [kc(X ** 2 * (1 + X ** (Q - 1))), K.one]
        y0 = C[0] / D[0]
        res = []
        for b1 in (kc(1) / kc(X ** 2), kc(1) / kc(X ** 3), K.one + kc(1) / kc(X ** 2)):
            b = [K.one, b1]
            ok = True
            for k in range(3):
                lhs = sum((C[i] * b[k - i] ** (2 ** i) for i in range(2) if 0 <= k - i <= 1), K.zero)
                rhs = y0 ** (2 ** k) * sum((D[i] * b[k - i] ** (Q * 2 ** i) for i in range(2) if 0 <= k - i <= 1), K.zero)
                ok = ok and lhs == rhs
            res.append(ok)
        print(f"(4) TX-like Q={Q}: RLE(ii) holds for B = 1+X^-2 tau, 1+X^-3 tau, 1+(1+X^-2) tau : {res}")

main()
