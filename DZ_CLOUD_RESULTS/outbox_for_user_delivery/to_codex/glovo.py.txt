#!/usr/bin/env python3
"""GLO valuation checks (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I glovo.py
Uses sympy polynomials over GF(2) in X.  For Q in (4, 8, 16):
 (1) TX-like planted family: A = X + tau, C = X^{Q+1}(1+X^{Q-1}) + tau, D = X^2(1+X^{Q-1}) + tau
     satisfies C*A = D*phi(A) identically (phi = Q-power on coefficients); evaluate the VO hypotheses
     at v_inf and v_0 (they must NOT both hold, since a solution exists).
 (2) Example NG: C = 1 + tau, D = X + tau: VO hypotheses at v_inf hold with theta = 1/(Q-1) > theta_top = 0.
 (3) RLE check on the TX-like family: B := A a_0^{-1} = 1 + X^{-2} tau lies in L{tau}, b_0 = 1, and
     C*B == D*phi(B)*y_0 with y_0 = c_0/d_0 = X^{Q-1} (right multiplication by the scalar y_0)."""
from fractions import Fraction as Fr
import sympy as sp
X = sp.symbols('X')

def P(e): return sp.Poly(e, X, modulus=2)

def ore_mul(Cc, Ac):
    """(sum c_i tau^i)(sum a_j tau^j) = sum c_i a_j^{2^i} tau^{i+j}; coefficient lists of Polys."""
    out = {}
    for i, c in enumerate(Cc):
        for j, a in enumerate(Ac):
            out[i + j] = out.get(i + j, P(0)) + c * a ** (2 ** i)
    return [out.get(k, P(0)) for k in range(max(out) + 1)]

def v_inf(p): return -p.degree() if not p.is_zero else None
def v_0(p):
    if p.is_zero: return None
    terms = p.terms()
    return min(m[0] for m, _ in terms)

def vo(C, D, Q, v):
    a2 = len(C) - 1
    th = Fr(v(C[0]) - v(D[0]), Q - 1)
    ok2 = all((v(C[i]) is None or v(C[i]) + (2 ** i) * th >= v(C[0]) + th) and
              (v(D[i]) is None or v(D[i]) + Q * (2 ** i) * th >= v(C[0]) + th) for i in range(1, a2 + 1))
    thtop = Fr(v(C[a2]) - v(D[a2]), (Q - 1) * 2 ** a2)
    return th, ok2, thtop, (ok2 and thtop < th)

for Q in (4, 8, 16):
    A = [P(X), P(1)]
    C = [P(X ** (Q + 1) * (1 + X ** (Q - 1))), P(1)]
    D = [P(X ** 2 * (1 + X ** (Q - 1))), P(1)]
    lhs = ore_mul(C, A)
    rhs = ore_mul(D, [a ** Q for a in A])
    ident = all((l - r).is_zero for l, r in zip(lhs, rhs)) and len(lhs) == len(rhs)
    print(f"Q={Q} TX-like: C*A == D*phi(A): {ident};  VO@inf {vo(C, D, Q, v_inf)};  VO@0 {vo(C, D, Q, v_0)}")
    Cn, Dn = [P(1), P(1)], [P(X), P(1)]
    print(f"Q={Q} NG: VO@inf (theta, hyp(ii), theta_top, OBSTRUCTED) = {vo(Cn, Dn, Q, v_inf)}")

def rle_check(Q):
    """coefficientwise over F_2(X): (C*B)_k == y0^{2^k} (D*phi(B))_k, using sympy rational functions."""
    c = [X ** (Q + 1) * (1 + X ** (Q - 1)), sp.Integer(1)]
    d = [X ** 2 * (1 + X ** (Q - 1)), sp.Integer(1)]
    b = [sp.Integer(1), X ** -2]
    y0 = sp.cancel(c[0] / d[0])
    ok = True
    for k in range(3):
        lhs = sum(c[i] * b[k - i] ** (2 ** i) for i in range(2) if 0 <= k - i < 2)
        rhs = y0 ** (2 ** k) * sum(d[i] * b[k - i] ** (Q * 2 ** i) for i in range(2) if 0 <= k - i < 2)
        num = sp.Poly(sp.numer(sp.together(lhs - rhs)), X, modulus=2)
        ok = ok and num.is_zero
    return y0, ok

for Q in (4, 8, 16):
    y0, ok = rle_check(Q)
    print(f"Q={Q} RLE on TX-like: y0 = {y0}; C*B == D*phi(B)*y0 : {ok}")
