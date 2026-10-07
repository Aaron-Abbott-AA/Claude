#!/usr/bin/env python3
"""Referee arithmetic for GO (independent code; reads no files). Usage: python3 -I ref_go.py
(1) Recount GO coverage: even rho in [10,40], g in [rho+3, min(2rho, ceil(3rho/2)+2)], a* = rho-1-floor((g-1)/2)
    (EBR form; compared with rho - ceil(g/2)); range a* <= (rho-4)/3; gate: no r in [rho-a*, rho] with r | g+rho/2.
    Also recompute the gate in its EXACT form from GO(c): the bad case needs t | gcd(rho', m/2) with t > rho/2,
    i.e. t = rho' > rho/2, rho' | m/2 (same as sufficient form since rho' >= rho-a* > rho/2).
(2) Threshold: 2^t - 1 < T = (4/3)2^{rho/2} - 1 for all t <= rho/2.
(3) Lemma-G analogue for the WG family B1 (weight u = R/4): for j = a*,
    u * [ (2^{j+1}-1)(Q+1) + max_T sum_{e in T} 2^e ] <= Q^2/2 < v, all even rho in [4,40], g in [rho+3, 2rho].
(4) TX: A = tau + X solves C*A = D*A^{(Q)} over F_2[X] for Q = 2^{m/2}, m in {8,12,16,20}
    (C = tau + X^Q(X+X^Q), D = tau + X(X+X^Q)); and top-coefficient necessary condition c_1/d_1 = 1 in L^2.
"""
import math

# ---- (1) coverage
n_range = n_gate = 0; mism = 0; fails = []; exact_mism = 0
for rho in range(10, 41, 2):
    for g in range(rho + 3, min(2 * rho, math.ceil(3 * rho / 2) + 2) + 1):
        a1 = rho - 1 - (g - 1) // 2
        a2 = rho - math.ceil(g / 2)
        if a1 != a2: mism += 1
        a = a1
        if 3 * a > rho - 4: continue
        n_range += 1
        half_m = g + rho // 2
        bad = [r for r in range(rho - a, rho + 1) if half_m % r == 0]
        # exact form: exists rho' in [rho-a, rho] and t with t | rho', t | m/2, t > rho/2
        bad_exact = [(rp, t) for rp in range(rho - a, rho + 1) for t in range(rho // 2 + 1, rp + 1) if rp % t == 0 and half_m % t == 0]
        if bool(bad) != bool(bad_exact): exact_mism += 1
        if not bad: n_gate += 1
        else: fails.append((rho, g, bad))
print(f"(1) a* forms mismatch={mism}; cells in range a*<=(rho-4)/3: {n_range}; gate passes: {n_gate}; gate fails: {len(fails)}; sufficient-vs-exact gate mismatch={exact_mism}")
print("    first gate failures:", fails[:8])
for c in [(10, 15), (14, 21), (16, 24), (18, 27), (20, 30)]:
    print("    listed failure", c, "in fails:", any(f[0] == c[0] and f[1] == c[1] and c[0] in f[2] for f in fails))

# ---- (2) threshold
ok2 = all((1 << t) - 1 < (4 / 3) * 2 ** (rho / 2) - 1 for rho in range(4, 81, 2) for t in range(1, rho // 2 + 1))
print(f"(2) 2^t-1 < T for t <= rho/2, even rho <= 80: {ok2}")

# ---- (3) Lemma-G analogue for B1
worst = None; badc = 0; cells = 0
for rho in range(4, 41, 2):
    for g in range(rho + 3, 2 * rho + 1):
        a = rho - 1 - (g - 1) // 2
        if a < 0: continue
        j = min(a, rho // 2 - 2)
        Q = 2 ** (g + rho // 2); u = 2 ** g // 4
        Tmax = sum(2 ** e for e in range(rho - (rho - 2 * j - 2), rho))  # top rho-2j-2 exponents in [j+1, rho-1]
        deg = u * ((2 ** (j + 1) - 1) * (Q + 1) + Tmax)
        cells += 1
        ratio = deg / (Q * Q / 2)
        if not deg <= Q * Q // 2: badc += 1
        if worst is None or ratio > worst[0]: worst = (ratio, rho, g, j)
print(f"(3) cells={cells}; violations of u*sum <= Q^2/2: {badc}; worst ratio deg/(Q^2/2) = {worst[0]:.4f} at (rho,g,j)={worst[1:]}")

# ---- (4) TX over F_2[X], polynomials as ints
def pmul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
    return r
def psub(a, k):  # a(X^k) for k a power of 2: spread bits
    r = 0; i = 0
    while a:
        if a & 1: r |= 1 << (i * k)
        a >>= 1; i += 1
    return r
def tmul(C, A):  # composition in F_2[X]{tau}: tau^i c = c^{2^i} tau^i, c^{2^i}(X) = c(X^{2^i})
    out = [0] * (len(C) + len(A) - 1)
    for i, c in enumerate(C):
        for j, x in enumerate(A):
            out[i + j] ^= pmul(c, psub(x, 1 << i))
    return out
X = 0b10
for m in (8, 12, 16, 20):
    Q = 1 << (m // 2)
    XQ = 1 << Q
    c0 = pmul(XQ, X ^ XQ); d0 = pmul(X, X ^ XQ)
    C = [c0, 1]; D = [d0, 1]; A = [X, 1]; AQ = [psub(x, Q) for x in A]
    lhs = tmul(C, A); rhs = tmul(D, AQ)
    print(f"(4) m={m}: C*A == D*A^(Q): {lhs == rhs}; c1/d1 = 1 (a square): {C[1] == D[1] == 1}")
