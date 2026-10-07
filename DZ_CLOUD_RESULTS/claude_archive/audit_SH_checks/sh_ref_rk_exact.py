#!/usr/bin/env python3
"""Referee check (SH audit), exact F_2[X] part of Proposition RK.  Referee code; uses sympy Poly over GF(2).
Run: nice -n 19 python3 -I sh_ref_rk_exact.py
For m in a range of even m >= 4, Q = 2^(m/2), E = (1, 2, Q, 2Q):
 E1  cofactors M_l = 3x3 determinants det(X^(k*e))_{k=0..2, e in E minus e_l} computed by sympy Matrix.det over GF(2)
     equal the Vandermonde products prod_{pairs}(X^e + X^e')
 E2  degrees (5Q,5Q,4Q+2,2Q+2), monic, v_X and v_{X+1} = (Q+4,Q+2,4,4)
 E3  max multiplicity of an irreducible pi not in {X, X+1} in M_4 (note claims <= 3; referee expects <= 2), via factor_list
 E4  cofactor identity sum_l M_l X^(k e_l) = 0 for k = 0,1,2
 E5  A_1 := M_1 X + M_4 X^(2Q) equals M_2 X^2 + M_3 X^Q and has degree 5Q+1 (used in the F_4 case)
 E6  leading-coefficient bookkeeping of step 4: deg M_2 X^2 = deg M_3 X^Q = 5Q+2 (they cancel in A_1), etc.
"""
import itertools, sympy
from sympy import Poly, symbols, Matrix, GF

X = symbols('X')
def P2(expr): return Poly(expr, X, modulus=2)

def val(p, pi):
    v = 0
    while not p.is_zero:
        q, r = p.div(pi)
        if not r.is_zero: break
        p = q; v += 1
    return v

def run(m, do_factor):
    Q = 2 ** (m // 2); E = [1, 2, Q, 2 * Q]
    M = []
    for l in range(4):
        rest = E[:l] + E[l + 1:]
        mat = Matrix(3, 3, lambda k, j: X ** (k * rest[j]))
        det = P2(sympy.expand(mat.det(method='berkowitz')))
        prod = P2(1)
        for e, f in itertools.combinations(rest, 2): prod = prod * P2(X ** e + X ** f)
        M.append((det, det == prod))
    Ms = [d for d, _ in M]
    out = dict(m=m, E1=all(ok for _, ok in M))
    out['E2_degs'] = [p.degree() for p in Ms] == [5 * Q, 5 * Q, 4 * Q + 2, 2 * Q + 2]
    out['E2_monic'] = all(p.LC() % 2 == 1 for p in Ms)
    x, x1 = P2(X), P2(X + 1)
    out['E2_vX'] = [val(p, x) for p in Ms] == [Q + 4, Q + 2, 4, 4]
    out['E2_vX1'] = [val(p, x1) for p in Ms] == [Q + 4, Q + 2, 4, 4]
    if do_factor:
        fl = Ms[3].factor_list()[1]
        others = [mult for f, mult in fl if f not in (x, x1)]
        out['E3_maxmult_other'] = max(others) if others else 0
    g = P2(1 + X ** (Q - 1)).gcd(P2(1 + X ** (Q // 2 - 1)))
    out['E3_gcd_is_X+1'] = (g == x1)
    out['E4'] = all((sum((Ms[l] * P2(X ** (k * E[l])) for l in range(4)), P2(0))).is_zero for k in range(3))
    A1 = Ms[0] * P2(X) + Ms[3] * P2(X ** (2 * Q)); A1b = Ms[1] * P2(X ** 2) + Ms[2] * P2(X ** Q)
    out['E5'] = (A1 == A1b) and A1.degree() == 5 * Q + 1
    out['E6'] = ((Ms[1] * P2(X ** 2)).degree() == 5 * Q + 2 and (Ms[2] * P2(X ** Q)).degree() == 5 * Q + 2
                 and (Ms[3] * P2(X ** (2 * Q))).degree() == 4 * Q + 2)
    return out

if __name__ == "__main__":
    for m in (4, 6, 8, 10, 12):
        print(run(m, do_factor=True), flush=True)
    for m in (14, 16):
        print(run(m, do_factor=False), flush=True)
