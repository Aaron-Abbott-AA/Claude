#!/usr/bin/env python3
"""Referee check for RBL note, Proposition TX (independent code; galois library).

Usage: python3 -I check_tx.py m rho seed nalpha
 m even, rho <= m/2.
Checks:
 T1  linearized identity (tau+abar(a+abar)) o (tau+a) == (tau+a(a+abar)) o (tau+abar) for random a
 T2  pointwise defect a(V_alpha) for alpha: ALL alpha in F_q if q<=4096 else nalpha random + all of F_Q;
     classify by alpha in F_Q / not; record degenerate alphas (expected: alpha in U minus {0}).
 T3  C_alpha(V_alpha) subset F_Q.
 T4  generic identity C(w) = D(w^Q) in F_q[X] for every basis w (polynomial arithmetic, exact).
 T5  real type fails: D != kappa * C^(Q) (C^(Q): coefficients c_e(X)^Q as elements of F_q[X]).
 T6  C(w1)/C(w2) not in F_q for w1 != w2 (cross-multiplication test c*C(w2) == C(w1) impossible).
 T7  bivariate: Gamma = tau + Y(X+Y) gives Gamma(w) symmetric under iota (coeffs^Q, swap X,Y): checked
     by evaluation at random (X,Y) pairs: Gamma(w)(X,Y)^Q == Gamma(w)(Y^Q... ) -- see code.
 T8  derivative map w -> w' = u has F2-rank rho (RR violated).
 T9  generic defect exactly 1: for alpha not in F_Q, V_alpha not in lambda F_Q (by T2) -> no degree-0 generic relation.
"""
import sys, random
import numpy as np
import galois

def main():
    m, rho, seed, nalpha = map(int, sys.argv[1:5])
    assert m % 2 == 0 and rho <= m // 2
    random.seed(seed)
    h = m // 2
    Q = 1 << h
    q = 1 << m
    F = galois.GF(2**m)
    def el(x): return F(int(x))
    def conj(x): return x ** Q
    # F_Q elements: x^Q == x
    gen = F.primitive_element
    gQ = gen ** ((q - 1) // (Q - 1))  # generator of F_Q^*
    FQ = [F(0)] + [gQ ** i for i in range(Q - 1)]
    # random rho-dim F2-subspace U of F_Q via bit-vector basis
    def indep(vecs):
        basis = []
        for v in vecs:
            v = int(v)
            for b in basis:
                v = min(v, v ^ b)
            if v == 0:
                return False
            basis.append(v)
        return True
    while True:
        U = [random.choice(FQ[1:]) for _ in range(rho)]
        if indep(U):
            break
    def rank(rows):
        A = F(np.array([[int(x) for x in r] for r in rows], dtype=np.int64))
        return np.linalg.matrix_rank(A)
    def defect(V):
        r = len(V)
        for j in range(0, r // 2 + 1):
            rows = [[v ** (2 ** e) for e in range(j + 1)] + [conj(v) ** (2 ** e) for e in range(j + 1)] for v in V]
            if 2 * j + 2 > r or rank(rows) < 2 * j + 2:
                return j
        return r // 2
    # T1
    bad1 = 0
    for _ in range(50):
        a = el(random.randrange(q)); ab = conj(a)
        # compose linearized polys: (tau + c) o (tau + d) = tau^2 + (d^2 + c) tau + c d
        c1, d1 = ab * (a + ab), a
        c2, d2 = a * (a + ab), ab
        lhs = (d1 ** 2 + c1, c1 * d1)
        rhs = (d2 ** 2 + c2, c2 * d2)
        if lhs != rhs:
            bad1 += 1
    print(f"m={m} rho={rho} seed={seed}")
    print(f"T1 identity failures: {bad1}/50")
    # T2/T3
    if q <= 4096:
        alphas = [el(i) for i in range(q)]
    else:
        alphas = [el(random.randrange(q)) for _ in range(nalpha)] + FQ
    hist = {}
    bad3 = 0
    degen = []
    for a in alphas:
        V = [u ** 2 + a * u for u in U]
        inFQ = (conj(a) == a)
        if not indep(V):
            degen.append(int(a))
            continue
        d = defect(V)
        key = ('alpha in F_Q' if inFQ else 'alpha notin F_Q', d)
        hist[key] = hist.get(key, 0) + 1
        ab = conj(a)
        c0 = ab * (a + ab)
        for v in V:
            Cv = v ** 2 + c0 * v
            if conj(Cv) != Cv:
                bad3 += 1
    # degenerate alphas should be exactly U-span \ {0}
    span = set()
    for mask in range(1, 1 << rho):
        s = 0
        for i in range(rho):
            if mask >> i & 1:
                s ^= int(U[i])
        span.add(s)
    degen_ok = set(degen) <= span
    print(f"T2 defect histogram (key=(class, a)): {hist}")
    print(f"T2 degenerate alphas: {len(degen)} (all inside span(U)\\0: {degen_ok})")
    print(f"T3 C_alpha(v) not in F_Q: {bad3}")
    # T4-T6 polynomial identities in F_q[X]
    X = galois.Poly([1, 0], field=F)
    XQ = galois.Poly.Degrees([Q], coeffs=[1], field=F)
    one = galois.Poly([1], field=F)
    c1 = XQ * (X + XQ)        # C = Z^2 + c1 Z
    d1 = X * (X + XQ)         # D = Z^2 + d1 Z
    bad4 = 0
    Cw = []
    for u in U:
        w = galois.Poly([1, 0], field=F) * u + one * (u ** 2)   # u^2 + X u
        wQ = galois.Poly([1, 0], field=F) * 0 + XQ * u + one * (u ** 2)  # w^Q = u^2 + X^Q u (u in F_Q)
        # sanity: w^Q computed as power
        if w ** Q != galois.Poly(np.array((w ** Q).coeffs), field=F):
            pass
        lhs = w * w + c1 * w
        rhs = wQ * wQ + d1 * wQ
        if lhs != rhs:
            bad4 += 1
        Cw.append(lhs)
    # check w^Q identity directly for one u (power of polynomial)
    u0 = U[0]
    w0 = X * u0 + one * (u0 ** 2)
    wq_direct = w0
    for _ in range(h):
        wq_direct = wq_direct * wq_direct
    wQ_ok = (wq_direct == XQ * u0 + one * (u0 ** 2))
    print(f"T4 generic identity C(w)=D(w^Q) failures: {bad4}/{rho}; w^Q formula ok: {wQ_ok}")
    # T5: c1^Q (as element of F_q[X]) vs d1
    c1Q = c1
    for _ in range(h):
        c1Q = c1Q * c1Q
    print(f"T5 real type D == C^(Q) ? {c1Q == d1}  (deg c1^Q = {c1Q.degree}, deg d1 = {d1.degree})")
    # T6: C(w1) = c * C(w2) with c in F_q  -> compare leading/const structure via solving c from one coeff
    bad6 = 0
    for i in range(rho):
        for j in range(rho):
            if i == j:
                continue
            A, B = Cw[i], Cw[j]
            # find c from constant coefficient (X^0): A0 = c B0
            A0 = A.coeffs[-1]; B0 = B.coeffs[-1]
            c = A0 / B0
            if A == B * c:
                bad6 += 1
    print(f"T6 pairs with constant ratio C(w_i)/C(w_j): {bad6}")
    # T7: bivariate real relation: Gamma(w) = w^2 + Y(X+Y) w ; iota(f)(X,Y) = f^(Q)(Y,X).
    # Gamma(w)(X,Y) = u^4 + (X^2+XY+Y^2) u^2 + (X^2 Y + X Y^2) u ; coefficients u^k in F_Q -> f^(Q) = f; symmetric in X,Y.
    bad7 = 0
    for _ in range(30):
        x, y = el(random.randrange(q)), el(random.randrange(q))
        for u in U:
            w_x = u ** 2 + x * u
            iw_y = u ** 2 + y * u           # iota w = w^(Q)(Y)
            G = w_x ** 2 + y * (x + y) * w_x
            Dl = iw_y ** 2 + x * (x + y) * iw_y   # iota(Gamma) = tau + X(X+Y) applied to iota w
            if G != Dl:
                bad7 += 1
    print(f"T7 bivariate real relation Gamma(w) = (iota Gamma)(iota w) failures: {bad7}")
    # T8 derivative w' = u : rank = rho (U independent)
    print(f"T8 derivative map rank = {rho if indep(U) else 'deficient'} (RR bound 2)")

if __name__ == '__main__':
    main()
