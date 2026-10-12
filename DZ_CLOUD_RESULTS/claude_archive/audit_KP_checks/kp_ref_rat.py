"""Referee re-check of Proposition KL: rational roots of Pt in L = F_q(X) (independent code).
usage: python3 -I kp_ref_rat.py <m> <D> [control]
 - cofactors by explicit 3x3 determinant expansion (not the Vandermonde product);
 - M_W from the ordinary product prod_{w in W}(x + w) (coefficients outside x^{2^i} asserted zero);
 - Pt by top-down solving over F_2[X]; P == Pt o M_W verified exactly;
 - Newton polygons at every F_2-irreducible factor of every coefficient and at infinity (factorisation re-multiplied);
 - F_2-kernel of u -> Pt(u) on F_q[X]_{<=D} with an own modulus for F_q (D chosen >= the Newton bound).
"""
import sys, os, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import pmul, psq, pmod, own_irreducible, Field
from fractions import Fraction
import sympy as sp

def pw2(a, i):
    for _ in range(i): a = psq(a)
    return a
def pdivmod(a, b):
    q = 0; db = b.bit_length()
    while a and a.bit_length() >= db:
        s = a.bit_length() - db; q ^= 1 << s; a ^= b << s
    return q, a

def cofactors(m):
    Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]; out = []
    for l in range(4):
        z1, z2, z3 = [1 << E[i] for i in range(4) if i != l]
        s = 0
        for a, b in ((z2, z3), (z3, z2), (z1, z3), (z3, z1), (z1, z2), (z2, z1)):
            s ^= pmul(a, psq(b))
        out.append(s)
    return out

def subspace_poly_FX():
    W = []
    for bits in range(8):
        W.append((bits & 1) | (((bits >> 1) & 1) << 1) | (((bits >> 2) & 1) << 2))  # 0,1,X,X+1,X^2,...
    poly = [1]  # coefficients in x (index = x-degree), entries in F_2[X]
    for w in W:
        new = [0] * (len(poly) + 1)
        for i, c in enumerate(poly):
            new[i + 1] ^= c; new[i] ^= pmul(c, w)
        poly = new
    for i, c in enumerate(poly):
        if i not in (1, 2, 4, 8): assert c == 0, i
    return [poly[1], poly[2], poly[4], poly[8]]

def compose(A, B):
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a:
            for j, b in enumerate(B):
                if b: out[i + j] ^= pmul(a, pw2(b, i))
    return out

def quotient(P, M):
    k = len(M) - 1; n = len(P) - 1 - k; Pt = [0] * (n + 1)
    for d in range(n, -1, -1):
        s = P[d + k]
        for i in range(d + 1, n + 1):
            j = d + k - i
            if 0 <= j <= k and Pt[i] and M[j]: s ^= pmul(Pt[i], pw2(M[j], i))
        Pt[d] = s
    assert compose(Pt, M) == P, "P != Pt o M_W"
    return Pt

def val(a, pi):
    v = 0
    while True:
        q, r = pdivmod(a, pi)
        if r: return v
        a = q; v += 1

def lower_hull_slopes(pts):
    pts = sorted(pts); hull = []
    for p in pts:
        while len(hull) >= 2 and (hull[-1][1] - hull[-2][1]) * (p[0] - hull[-2][0]) >= (p[1] - hull[-2][1]) * (hull[-1][0] - hull[-2][0]):
            hull.pop()
        hull.append(p)
    return [Fraction(y2 - y1, x2 - x1) for (x1, y1), (x2, y2) in zip(hull, hull[1:])]

def main(m, D, control):
    h = m // 2; c0, c1, d0, d1 = cofactors(m)
    P = [c0, c1] + [0] * (h - 2) + [d0, d1]
    MW = subspace_poly_FX(); assert MW[-1] == 1
    Pt = quotient(P, MW)
    target = P if control else Pt
    n = len(target) - 1
    X = sp.symbols('X'); facs = set()
    for c in target:
        if not c: continue
        poly = sp.Poly(sum(X ** i for i in range(c.bit_length()) if (c >> i) & 1), X, modulus=2)
        lc, fl = poly.factor_list(); prod = 1
        for f, k in fl:
            fi = int(''.join(str(int(b) % 2) for b in f.all_coeffs()), 2)
            facs.add(fi)
            for _ in range(k): prod = pmul(prod, fi)
        assert prod == c, "factorisation does not re-multiply"
    maxpole = 0; intpole = 0
    for pi in facs:
        sl = lower_hull_slopes([(1 << i, val(c, pi)) for i, c in enumerate(target) if c])
        # root valuations are -slope; a pole means -slope < 0, i.e. slope > 0
        for s in sl:
            if s > 0: maxpole = max(maxpole, s)
            if s > 0 and s.denominator == 1: intpole = max(intpole, int(s))
    sl_inf = lower_hull_slopes([(1 << i, -(c.bit_length() - 1)) for i, c in enumerate(target) if c])
    degbound = max([s for s in sl_inf] + [0])   # root valuation at inf = -slope -> degree = slope
    print(f"m={m} {'CONTROL (P)' if control else 'Pt'} n={n} coef degrees={[c.bit_length()-1 if c else None for c in target]}")
    print(f"  #irreducible factors={len(facs)}; max positive slope at finite places={maxpole} (max INTEGER positive slope={intpole}; root valuations in L are integers); slopes at inf={sorted(set(sl_inf))}; degree bound={degbound}; D={D}")
    assert intpole == 0, "finite pole possible"
    assert D >= degbound
    F = Field(m, seed=4242 + m)
    cols = []
    for k in range(D + 1):
        for bit in range(m):
            beta = 1 << bit; coef = {}
            for i, c in enumerate(target):
                if not c: continue
                be = F.pw(beta, 1 << i); sh = k << i; s = 0; a = c
                while a:
                    if a & 1: coef[s + sh] = coef.get(s + sh, 0) ^ be
                    a >>= 1; s += 1
            v = 0
            for e, cf in coef.items():
                if cf: v |= cf << (m * e)
            cols.append(v)
    piv = {}; ker = 0
    for v in cols:
        while v:
            p = v.bit_length() - 1
            if p in piv: v ^= piv[p]
            else: piv[p] = v; break
        if v == 0: ker += 1
    print(f"  F_2-dim of roots in F_q[X]_(<= {D}) (own modulus {hex(F.mod)}): {ker}")

if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), len(sys.argv) > 3 and sys.argv[3] == 'control')
