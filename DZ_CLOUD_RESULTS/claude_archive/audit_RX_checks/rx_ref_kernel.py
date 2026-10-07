#!/usr/bin/env python3
"""Referee check for RX, part K (independent of the owner's code).  Run: python3 -I rx_ref_kernel.py

K1  Newton-polygon bound at infinity: a polynomial root f (any coefficients) of P = sum_l M_l T^{e_l} of
    degree n needs max_l (deg M_l + n e_l) attained twice.  Lists all such n (for n >= 0) and, at X = 0,
    all pole orders e >= 1 with min_l (ord M_l - e e_l) attained twice.
K2  F_2-dimension of ker P on F_2[X]_{<=dmax}  (a=1: m = 16, 18, 20; a=2: m = 22) -- exact bit-int polys.
K3  F_2-dimension of ker P on F_q[X]_{<=dmax}  (a=1, m = 16, dmax = 6 and 10), own GF(2^16), modulus
    x^16+x^5+x^3+x^2+1 (different from the owner's).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # own checks dir only
from rx_ref_exact import E2, deg, ordx
from rx_ref_fields import GF, MODS

def K1(a, m):
    _, M = E2(a, m); Q = 1 << (m // 2)
    E = [1 << i for i in range(a + 1)] + [Q << i for i in range(a + 1)]
    D = [deg(x) for x in M]; O = [ordx(x) for x in M]
    tie_n = []
    for n in range(0, 64):
        vals = [D[l] + n * E[l] for l in range(len(E))]
        if vals.count(max(vals)) >= 2: tie_n.append(n)
    # for n beyond 63 the top-slope term is strictly largest (checked analytically: slopes distinct,
    # last crossing is below 64 in all cases tested; assert it)
    big = 10 ** 6
    vals = [D[l] + big * E[l] for l in range(len(E))]
    assert vals.count(max(vals)) == 1
    tie_pole0 = []
    for e in range(1, 64):
        vals = [O[l] - e * E[l] for l in range(len(E))]
        if vals.count(min(vals)) >= 2: tie_pole0.append(e)
    return dict(a=a, m=m, poly_root_degree_candidates=tie_n, pole_order_at_0_candidates=tie_pole0)

def rank_insert(basis, v):
    while v:
        p = v.bit_length() - 1
        if p in basis: v ^= basis[p]
        else:
            basis[p] = v; return True
    return False

def K2(a, m, dmax):
    _, M = E2(a, m); Q = 1 << (m // 2)
    E = [1 << i for i in range(a + 1)] + [Q << i for i in range(a + 1)]
    basis = {}; ker = 0
    for k in range(dmax + 1):
        img = 0
        for l, e in enumerate(E): img ^= M[l] << (k * e)
        if not rank_insert(basis, img): ker += 1
    return dict(a=a, m=m, dmax=dmax, F2_kernel_dim=ker)

def K3(m, dmax):
    a = 1; F = GF(m, MODS[m]); Q = 1 << (m // 2)
    _, M = E2(a, m)
    E = [1, 2, Q, 2 * Q]
    terms = [[i for i in range(x.bit_length()) if (x >> i) & 1] for x in M]
    basis = {}; ker = 0
    for k in range(dmax + 1):
        for j in range(m):
            beta = 1 << j
            coef = {}
            for l, e in enumerate(E):
                be = F.frob(beta, e.bit_length() - 1)
                for s in terms[l]:
                    coef[s + k * e] = coef.get(s + k * e, 0) ^ be
            v = 0
            for s, c in coef.items(): v ^= c << (m * s)
            if not rank_insert(basis, v): ker += 1
    return dict(a=a, m=m, dmax=dmax, F2_kernel_dim_on_FqX=ker)

if __name__ == "__main__":
    for (a, m) in [(1, 16), (1, 18), (1, 20), (2, 22), (3, 28)]:
        print("K1", K1(a, m)); sys.stdout.flush()
    for (a, m, d) in [(1, 16, 48), (1, 18, 48), (1, 20, 64), (2, 22, 40)]:
        print("K2", K2(a, m, d)); sys.stdout.flush()
    for d in (6, 10):
        print("K3", K3(16, d)); sys.stdout.flush()
