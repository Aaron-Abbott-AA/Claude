#!/usr/bin/env python3
"""KP rational-root search (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I kprat.py <m>
RX family a = 1 (W = F_2[X]_{<=2}).  Exact P in F_2[X]{tau}; M_W = subspace polynomial of W (monic, F_2[X]
coefficients); Pt = P / M_W (exact right division).  A G-stable F_2-line in ker Pt is the same as a nonzero
root t in L = F_q(X) of Pt.  Search: Newton polygons of Pt at every irreducible pi dividing a coefficient (and at
infinity) give the possible pole orders and the degree bound; then the F_2-kernel of u -> v^{2^n} Pt(u/v) on
F_q[X]_{<=D} (F_q coefficients as bit vectors) is computed exactly.  Output: kernel dimension.  'kprat.py <m> control' runs the same search on P itself (expected 3 = W).
"""
import sys, itertools
from fractions import Fraction
import sympy as sp

def pmul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r
def pdivmod(a, b):
    q = 0; db = b.bit_length()
    while a and a.bit_length() >= db:
        sh = a.bit_length() - db; q ^= 1 << sh; a ^= b << sh
    return q, a
def ppow2(a, k):  # a^(2^k) over F_2: spread bits
    for _ in range(k):
        r = 0; i = 0; x = a
        while x:
            if x & 1: r |= 1 << (2 * i)
            x >>= 1; i += 1
        a = r
    return a
def deg(a): return a.bit_length() - 1

def skew_mul(A, B):  # F_2[X]{tau}
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if not a: continue
        for j, b in enumerate(B):
            if b: out[i + j] ^= pmul(a, ppow2(b, i))
    return out
def evalP(S, w):
    s = 0
    for i, c in enumerate(S): s ^= pmul(c, ppow2(w, i))
    return s
def right_div_monic(P, M):
    P = P[:]; dm = len(M) - 1; dq = len(P) - 1 - dm; Qt = [0] * (dq + 1)
    for j in range(dq, -1, -1):
        a = P[j + dm]
        if not a: continue
        Qt[j] = a
        for i, mc in enumerate(M): P[i + j] ^= pmul(a, ppow2(mc, j))
    return Qt, P[:dm]

def vandermonde_cofactors(m):
    Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]; M = []
    for l in range(4):
        rest = E[:l] + E[l + 1:]; p = 1
        for e, f in itertools.combinations(rest, 2): p = pmul(p, (1 << e) ^ (1 << f))
        M.append(p)
    return M

def to_sympy(a, X):
    return sp.Poly(sum(X ** i for i in range(a.bit_length()) if (a >> i) & 1), X, modulus=2)

def val(a, pi):
    v = 0
    while a:
        q, r = pdivmod(a, pi)
        if r: break
        a = q; v += 1
    return v

def newton_root_vals(points):
    """points: list of (x=2^i, y=valuation or None). Return set of root valuations (negatives of slopes)."""
    pts = sorted((x, y) for x, y in points if y is not None)
    hull = []
    for p in pts:
        while len(hull) >= 2:
            (x1, y1), (x2, y2) = hull[-2], hull[-1]
            if (y2 - y1) * (p[0] - x1) >= (p[1] - y1) * (x2 - x1): hull.pop()
            else: break
        hull.append(p)
    return {Fraction(-(y2 - y1), (x2 - x1)) for (x1, y1), (x2, y2) in zip(hull, hull[1:])}

PRIM = {10: 0b10000001001, 14: 0b100000000101011, 18: 0x40081}
def gmul(a, b, N, mod):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
        if a >> N: a ^= mod
    return r
def gpow(a, e, N, mod):
    r = 1
    while e:
        if e & 1: r = gmul(r, a, N, mod)
        a = gmul(a, a, N, mod); e >>= 1
    return r

def main(m):
    X = sp.symbols('X'); h = m // 2; Q = 1 << h
    c0, c1, d0, d1 = vandermonde_cofactors(m)
    P = [c0, c1] + [0] * (h - 2) + [d0, d1]
    S = [1]
    for w in (1, 0b10, 0b100):
        sw = evalP(S, w); S = skew_mul([sw, 1], S)
    assert S[-1] == 1
    Pt, rem = right_div_monic(P, S)
    assert not any(rem)
    if CONTROL:
        Pt = P  # positive control: the rational roots of P itself are exactly W (F_2-dim 3, Proposition RK)
    n = len(Pt) - 1
    # places: irreducible factors of all nonzero coefficients
    facs = set()
    for c in Pt:
        if c:
            for f, _ in to_sympy(c, X).factor_list()[1]:
                facs.add(int(''.join(str(int(b)) for b in f.all_coeffs()), 2))
    poles = {}
    for pi in facs:
        rv = newton_root_vals([(1 << i, val(c, pi) if c else None) for i, c in enumerate(Pt)])
        neg = [-r for r in rv if r < 0]
        if neg: poles[pi] = int(max(neg))  # max pole order (integral part)
    # infinity: v_inf(c) = -deg c
    rv_inf = newton_root_vals([(1 << i, -deg(c) if c else None) for i, c in enumerate(Pt)])
    v = 1
    for pi, k in poles.items():
        for _ in range(k): v = pmul(v, pi)
    # root t = u/v with v_inf(t) >= min root valuation at inf  =>  deg u <= deg v + max(-rv_inf)
    D = deg(v) + int(max([-r for r in rv_inf] + [0]))
    print(f"m={m} n={n} coefficient degrees={[deg(c) if c else None for c in Pt]}")
    print(f"  possible poles (pi, max order): {[(bin(p), k) for p, k in poles.items()]}; inf root vals {sorted(rv_inf)}; D={D}")
    # F_2-kernel of u -> sum_i Pt_i u^{2^i} v^{2^n - 2^i} on F_q[X]_{<=D}
    N = m; mod = PRIM[m]
    vpow = [ppow2(v, 0)]
    vp = {}
    for i in range(n + 1):
        # v^{2^n - 2^i} = prod over bits; compute as product of v^{2^j} for j in [i, n-1]
        t = 1
        for j in range(i, n): t = pmul(t, ppow2(v, j))
        vp[i] = pmul(Pt[i], t) if Pt[i] else 0
    basis = {}; kernel = 0
    for k in range(D + 1):
        for bit in range(N):
            beta = 1 << bit
            coef = {}
            for i in range(n + 1):
                if not vp[i]: continue
                be = gpow(beta, 1 << i, N, mod); sh = k << i
                a = vp[i]; s = 0
                while a:
                    if a & 1: coef[s + sh] = coef.get(s + sh, 0) ^ be
                    a >>= 1; s += 1
            vec = 0
            for s, c in coef.items():
                if c: vec |= c << (N * s)
            while vec:
                p = vec.bit_length() - 1
                if p in basis: vec ^= basis[p]
                else: basis[p] = vec; break
            if vec == 0: kernel += 1
    print(f"  F_2-dim of rational roots of Pt (in F_q(X), denominators | v, deg u <= {D}): {kernel}")

CONTROL = False
if __name__ == "__main__":
    CONTROL = len(sys.argv) > 2 and sys.argv[2] == "control"
    if CONTROL: print("POSITIVE CONTROL: searching rational roots of P itself")
    main(int(sys.argv[1]))
