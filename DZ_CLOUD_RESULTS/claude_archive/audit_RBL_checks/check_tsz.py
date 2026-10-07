#!/usr/bin/env python3
"""Referee check of Lemma TSZ (twisted Schwartz-Zippel), independent code.

Claim: f in F_q[X,Y], deg_X, deg_Y <= delta, f(a, a^Q) = 0 for > 2*delta*Q values a in F_q  =>  f = 0.
 (A) m=4 (q=16, Q=4), delta=1: EXHAUSTIVE over all 16^4 nonzero f = c00 + c10 X + c01 Y + c11 XY.
     Report max #zeros on the twisted diagonal; bound 2*delta*Q = 8.
 (B) m=6 (q=64, Q=8), delta=1,2: random f plus structured products; bound 2*delta*Q.
 (C) m=8 (q=256, Q=16), delta=1,2,3: random + structured (products of (X+Y+c), (XY+c), (X^Q-ish excluded)).
Usage: python3 -I check_tsz.py
"""
import random, itertools
import numpy as np
import galois

def twisted_values(F, m):
    q = 1 << m; Q = 1 << (m // 2)
    A = F(np.arange(q))
    return A, A ** Q

def count_zeros(F, coeffs, A, AQ, delta):
    # coeffs[i][j] for X^i Y^j
    val = F.Zeros(A.shape)
    Xp = [F.Ones(A.shape)]
    Yp = [F.Ones(A.shape)]
    for _ in range(delta):
        Xp.append(Xp[-1] * A); Yp.append(Yp[-1] * AQ)
    for i in range(delta + 1):
        for j in range(delta + 1):
            c = coeffs[i][j]
            if c:
                val = val + F(c) * Xp[i] * Yp[j]
    return int(np.count_nonzero(val == 0))

def main():
    random.seed(7)
    # (A) exhaustive m=4, delta=1
    m = 4; F = galois.GF(2**m); A, AQ = twisted_values(F, m)
    q = 16; Q = 4
    # vectorised: values matrix for basis monomials 1, X, Y, XY
    mons = [F.Ones(A.shape), A, AQ, A * AQ]
    best = 0; arg = None
    for c in itertools.product(range(q), repeat=4):
        if not any(c):
            continue
        v = F(c[0]) * mons[0] + F(c[1]) * mons[1] + F(c[2]) * mons[2] + F(c[3]) * mons[3]
        z = int(np.count_nonzero(v == 0))
        if z > best:
            best, arg = z, c
    print(f"(A) m=4 delta=1 exhaustive: max zeros = {best} at coeffs(1,X,Y,XY)={arg}; TSZ bound 2*delta*Q = {2*Q}; violation: {best > 2*Q}")
    # (B),(C) random + structured
    for m, deltas in ((6, (1, 2)), (8, (1, 2, 3))):
        F = galois.GF(2**m); A, AQ = twisted_values(F, m); q = 1 << m; Q = 1 << (m // 2)
        for delta in deltas:
            best = 0
            for _ in range(3000):
                co = [[random.randrange(q) if random.random() < 0.5 else 0 for _ in range(delta + 1)] for _ in range(delta + 1)]
                if not any(any(r) for r in co):
                    continue
                best = max(best, count_zeros(F, co, A, AQ, delta))
            # structured: products of delta factors each of bidegree (1,1): (X+Y+c), (XY+c), (X + l Y + c)
            sbest = 0
            for _ in range(2000):
                val = F.Ones(A.shape)
                for _k in range(delta):
                    t = random.randrange(3)
                    c = F(random.randrange(q)); l = F(random.randrange(1, q))
                    if t == 0:
                        fac = A + AQ + c
                    elif t == 1:
                        fac = A * AQ + c
                    else:
                        fac = A + l * AQ + c
                    val = val * fac
                sbest = max(sbest, int(np.count_nonzero(val == 0)))
            print(f"m={m} delta={delta}: random max zeros {best}, structured max zeros {sbest}; TSZ bound 2*delta*Q = {2*delta*Q}; violation: {max(best, sbest) > 2*delta*Q}")

if __name__ == '__main__':
    main()
