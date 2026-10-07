#!/usr/bin/env python3
"""Revision check GX v2, FIX-2 statements (referee, 7 Oct 2026). Field F_q = GF(2^12), F_Q = GF(2^6) inside it.
Polynomials in F_q[X] are lists of ints (galois field elements), index = degree.
R1 (SQ step 2 as revised): rank_F2 {A'(u)} on U' == rank_F2 of derivative on W' = A(U'), with A NON-injective
    on U' (A = P o S_K, K subset U'), and rank >= 3 whenever P' != 0 and dim U' >= d+3.
R2 (LD step 1 as revised): A with square coefficients, injective on U' => A_half injective on sqrt(U').
R3 (LD bullet): without injectivity, dim W' >= dim U' - d; sharp for A = P o S_K.
Usage: python3 -I rc_fix2.py"""
import random
import galois

GF = galois.GF(2 ** 12)
M = 12
g0 = GF.primitive_element
z = g0 ** ((2 ** 12 - 1) // (2 ** 6 - 1))      # generator of F_64^*
FQ_basis = [z ** i for i in range(6)]           # F_2-basis candidate of F_Q (check rank below)
rng = random.Random(7)

def padd(a, b):
    n = max(len(a), len(b)); a = a + [GF(0)] * (n - len(a)); b = b + [GF(0)] * (n - len(b))
    return [x + y for x, y in zip(a, b)]

def pscal(a, c):
    return [x * c for x in a]

def pderiv(a):
    return [a[i + 1] if (i + 1) % 2 == 1 else GF(0) for i in range(len(a) - 1)] or [GF(0)]

def to_bits(poly, D):
    poly = poly + [GF(0)] * (D - len(poly))
    v = []
    for c in poly[:D]:
        x = int(c)
        v.extend((x >> j) & 1 for j in range(M))
    return v

def rank2(vecs):
    rows = [int(''.join(map(str, v)), 2) if v else 0 for v in vecs]
    r = 0; piv = []
    for x in rows:
        for p in piv:
            x = min(x, x ^ p)
        if x:
            piv.append(x); r += 1
    return r

def apply_A(A, u):
    # A = list of polynomial coefficients a_i (lists); A(u) = sum a_i u^{2^i}
    out = [GF(0)]
    for i, ai in enumerate(A):
        out = padd(out, pscal(ai, u ** (2 ** i)))
    return out

def rand_poly(deg):
    return [GF(rng.randrange(2 ** 12)) for _ in range(deg + 1)]

def span_basis(vs):
    # F_2-span: enumerate all 2^k combos of a basis (small k)
    return vs

def subspace_poly_coeffs(K):
    # coefficients (in F_q, constants) of S_K(x) = prod_{k in span K}(x - k) as a tau-polynomial
    elems = [GF(0)]
    for b in K:
        elems = elems + [e + b for e in elems]
    # compute S_K(x) via linearised recursion: S_{K+b}(x) = S_K(x)^2 - S_K(b) S_K(x)
    coeffs = [GF(1)]  # S_0(x) = x
    def ev(c, x):
        s = GF(0)
        for i, ci in enumerate(c):
            s = s + ci * x ** (2 ** i)
        return s
    for b in K:
        sb = ev(coeffs, b)
        new = [GF(0)] + [c * c for c in coeffs]   # tau o S_K: square coefficients and shift
        new = [new[i] + (sb * coeffs[i] if i < len(coeffs) else GF(0)) for i in range(len(new))]
        coeffs = new
    return coeffs, elems

def compose_P_S(P, Sc):
    # (P o S)(u) = sum_j p_j S(u)^{2^j}; as tau-poly with polynomial coeffs: coefficient of tau^{i+j} += p_j * s_i^{2^j}
    d = len(P) - 1 + len(Sc) - 1
    A = [[GF(0)] for _ in range(d + 1)]
    for j, pj in enumerate(P):
        for i, si in enumerate(Sc):
            A[i + j] = padd(A[i + j], pscal(pj, si ** (2 ** j)))
    return A

assert rank2([[int(b) for b in to_bits([x], 1)] for x in FQ_basis]) == 6
_Sc, _el = subspace_poly_coeffs([z, z ** 2 + GF(1), z ** 5])
assert all(int(sum((c * e ** (2 ** i) for i, c in enumerate(_Sc)), GF(0))) == 0 for e in _el)
fail = {"R1": 0, "R2": 0, "R3": 0}; cnt = {"R1": 0, "R2": 0, "R3": 0}
for trial in range(40):
    k = rng.choice([1, 2]); dP = rng.choice([0, 1]); d = k + dP
    if d + 3 > 6:
        continue
    dimU = rng.randrange(d + 3, 7)
    # U' = span of dimU elements of F_Q containing K
    while True:
        U = [sum((FQ_basis[j] for j in range(6) if rng.random() < 0.5), GF(0)) for _ in range(dimU)]
        if rank2([to_bits([x], 1) for x in U]) == dimU:
            break
    K = U[:k]
    Sc, _ = subspace_poly_coeffs(K)
    P = [rand_poly(rng.randrange(1, 6)) for _ in range(dP + 1)]
    A = compose_P_S(P, Sc)
    Ad = [pderiv(a) for a in A]
    W = [apply_A(A, u) for u in U]
    D = max(len(w) for w in W) + 1
    Wd = [pderiv(w) for w in W]
    AdU = [apply_A(Ad, u) for u in U]
    rW = rank2([to_bits(w, D) for w in W])
    rd = rank2([to_bits(w, D) for w in Wd]); ra = rank2([to_bits(w, D) for w in AdU])
    Pd_nonzero = any(any(int(c) for c in pderiv(p)) for p in P)
    cnt["R1"] += 1
    if rd != ra or (Pd_nonzero and rd < 3):
        fail["R1"] += 1
    cnt["R3"] += 1
    if not (rW >= dimU - d and rW == dimU - k):
        fail["R3"] += 1
# R2: square coefficients, injective A on U' => A_half injective on sqrt(U')
for trial in range(40):
    d = rng.choice([0, 1, 2, 3]); dimU = rng.randrange(d + 3, 7) if d + 3 <= 6 else None
    if dimU is None:
        continue
    U = [sum((FQ_basis[j] for j in range(6) if rng.random() < 0.5), GF(0)) for _ in range(dimU)]
    if rank2([to_bits([x], 1) for x in U]) != dimU:
        continue
    S = [rand_poly(rng.randrange(0, 4)) for _ in range(d + 1)]           # s_i
    Asq = [padd([GF(0)], [GF(0)] * 0) for _ in S]
    Asq = []
    for s in S:   # a_i = s_i^2 : square coefficients and X -> X^2
        sq = [GF(0)] * (2 * len(s) - 1)
        for e, c in enumerate(s):
            sq[2 * e] = c * c
        Asq.append(sq)
    W = [apply_A(Asq, u) for u in U]
    D = max(len(w) for w in W) + 1
    if rank2([to_bits(w, D) for w in W]) != dimU:
        continue   # A not injective on U'; skip
    cnt["R2"] += 1
    sqU = [u ** (2 ** 11) for u in U]   # sqrt in GF(2^12)
    Wh = [apply_A(S, v) for v in sqU]
    Dh = max(len(w) for w in Wh) + 1
    ok = rank2([to_bits(w, Dh) for w in Wh]) == dimU
    # and A(u) = A_half(sqrt u)^2
    for w, wh in zip(W, Wh):
        sq = [GF(0)] * (2 * len(wh) - 1)
        for e, c in enumerate(wh):
            sq[2 * e] = c * c
        a = w + [GF(0)] * (len(sq) - len(w)); b = sq + [GF(0)] * (len(w) - len(sq))
        if any(int(x) != int(y) for x, y in zip(a, b)):
            ok = False
    if not ok:
        fail["R2"] += 1
for key in ("R1", "R2", "R3"):
    print(f"{key}: cases={cnt[key]} failures={fail[key]}")
