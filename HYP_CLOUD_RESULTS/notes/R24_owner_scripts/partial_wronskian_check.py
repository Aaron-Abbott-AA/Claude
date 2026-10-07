#!/usr/bin/env python3
"""R24 COMPUTED check of Lemma 3.1 (partial Wronskian) on P^1 over GF(2^8).
V=span(1, t, g, h) in H^0(O(tau0)), g with exponents = 0,1,4,5 mod 8, with the t^4 coefficient tuned so that D^(4)g(7)=0 (so D^(2),D^(3),D^(6),D^(7) g = 0),
h with exponents = 0,1 mod 8.  For s=1..4: R_s = gcd of the s x s minors of the rows eps_0..eps_{s-1}
(Hasse derivatives in t).  Checks:
 (1) deg(finite part of R_s) <= s*tau0 + (sum_{i<s} eps_i)(2g-2) with g=0 (the point at infinity has v>=0);
 (2) at every P in GF(2^8): min_J ord_P(w_J) >= sum_{i<s} (j_i(P) - eps_i);
 (3) at every P where the non-order N=5 is a vanishing order (here N_0-analogue; s=#{eps<5}=3):
     v_P(R_3) >= 5 - max{eps<5} = 1.  The exact set of such P is printed.
Generic orders are computed as the rank jumps of the Hasse rows, maximised over all 256 points
(valid since every minor has degree < 256).
Run: python3 -I partial_wronskian_check.py
"""
import random
from itertools import combinations
from math import comb
import galois

GF = galois.GF(2**8)
random.seed(7)
Z = GF(0); O = GF(1)
# NOTE: never use in-place += on list entries: galois 0-d arrays are mutable and [Z]*n shares one object
TAU = 24

def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p

def padd(a, b):
    n = max(len(a), len(b))
    return trim([(a[i] if i < len(a) else Z) + (b[i] if i < len(b) else Z) for i in range(n)])

def pmul(a, b):
    r = [Z] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0:
            continue
        for j, y in enumerate(b):
            r[i + j] = r[i + j] + x * y
    return trim(r)

def hasse(p, m):
    r = [Z] * max(1, len(p) - m)
    for n in range(m, len(p)):
        if comb(n, m) % 2:
            r[n - m] = r[n - m] + p[n]
    return trim(r)

def ev(p, x):
    s = Z
    for c in reversed(p):
        s = s * x + c
    return s

def pdivmod(a, b):
    a = trim(a); b = trim(b)
    if len(a) < len(b):
        return [Z], a
    q = [Z] * (len(a) - len(b) + 1)
    a = a[:]
    inv = b[-1] ** -1
    for i in range(len(a) - len(b), -1, -1):
        c = a[i + len(b) - 1] * inv
        q[i] = c
        for j in range(len(b)):
            a[i + j] = a[i + j] + c * b[j]
    return trim(q), trim(a[:len(b) - 1] if len(b) > 1 else [Z])

def iszero(p):
    return all(c == 0 for c in p)

def pgcd(a, b):
    while not iszero(b):
        _, r = pdivmod(a, b)
        a, b = b, r
    if iszero(a):
        return a
    inv = trim(a)[-1] ** -1
    return [c * inv for c in trim(a)]

def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    tot = [Z]
    for j in range(n):
        minor = [row[:j] + row[j + 1:] for row in M[1:]]
        tot = padd(tot, pmul(M[0][j], det(minor)))  # char 2: no signs
    return tot

def ordP(p, x):
    if iszero(p):
        return 10**9
    k = 0
    lin = [x, O]  # t + x = t - x
    while True:
        q, r = pdivmod(p, lin)
        if not iszero(r):
            return k
        p = q
        k += 1

def mono(n):
    return [Z] * n + [O]

def rc():
    return GF(random.randrange(1, 256))

g = padd(mono(4), mono(5))
for n in [8, 9, 12, 13, 16, 17, 20, 21]:
    g = padd(g, [Z] * n + [rc()])
# force a point P0 where the non-order 5 is a vanishing order: make D^(4)g(P0)=0
P0 = GF(7)
val = ev(hasse(g, 4), P0)
g = padd(g, [Z] * 4 + [val])
print("forced D^(4)g(P0)=0 at P0=7: D4g(P0)=%d, D5g(P0)=%d" % (int(ev(hasse(g, 4), P0)), int(ev(hasse(g, 5), P0))))
h = mono(8)
for n in [9, 16, 17, 24]:
    h = padd(h, [Z] * n + [rc()])
basis = [[O], mono(1), g, h]
pts = [GF(i) for i in range(256)]

def taylor(P):
    return [[ev(hasse(b, m), P) for m in range(TAU + 1)] for b in basis]

def rank(rows):
    M = galois.GF(2**8)(rows) if rows else None
    return 0 if M is None else int(__import__('numpy').linalg.matrix_rank(M))

def vanishing_orders(P):
    T = taylor(P)
    js = []
    prev = 0
    for m in range(TAU + 1):
        cols = [[T[k][mm] for mm in range(m + 1)] for k in range(4)]
        rk = rank(cols)
        if rk > prev:
            js.append(m)
            prev = rk
    return js

# generic orders: rank jumps of Hasse rows, maximised over points
best = None
for P in pts:
    js = vanishing_orders(P)
    if best is None or js < best:   # generic = lexicographically smallest sequence
        best = js
eps = best
print("tau0 =", TAU, " generic orders eps =", eps)
rows_poly = {m: [hasse(b, m) for b in basis] for m in range(TAU + 1)}
allok = True
for s in range(1, 5):
    rows = [rows_poly[e] for e in eps[:s]]
    minors = []
    for J in combinations(range(4), s):
        M = [[rows[i][j] for j in J] for i in range(s)]
        minors.append(det(M))
    G = [Z]
    for w in minors:
        G = pgcd(G, w) if not iszero(G) else ([c * trim(w)[-1] ** -1 for c in trim(w)] if not iszero(w) else G)
    degG = len(trim(G)) - 1
    bound = s * TAU - 2 * sum(eps[:s])
    print("s=%d: rows %s, deg(finite R_s) = %d, bound s*tau0 + (sum eps)(2g-2) = %d, ok=%s"
          % (s, eps[:s], degG, bound, degG <= bound))
    allok &= degG <= bound
    bad = []
    weier = []
    for P in pts:
        js = vanishing_orders(P)
        need = sum(js[i] - eps[i] for i in range(s))
        v = min(ordP(w, P) for w in minors)
        if v < need:
            bad.append((int(P), js, v, need))
        if js != eps:
            weier.append((int(P), js, v))
    print("   exact failing set for v_P(R_s) >= sum_{i<s}(j_i-eps_i):", bad)
    allok &= not bad
    if s == 3:
        five = [w for w in weier if 5 in w[1]]
        print("   points with 5 (non-order) as vanishing order, (P, j(P), v_P(R_3)):", five)
        allok &= all(v >= 1 for (_, _, v) in five)
        print("   all Weierstrass points of V in GF(2^8) with v_P(R_3) (P, j(P), v_P(R_3)):", weier)
    if s == 4:
        print("   Weierstrass points of V in GF(2^8) (P, j(P), v_P(R_4)):", weier)
print("ALL CHECKS PASS:", allok)
