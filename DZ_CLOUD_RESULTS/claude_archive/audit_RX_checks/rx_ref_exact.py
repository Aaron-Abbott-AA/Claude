#!/usr/bin/env python3
"""Referee check for RX (independent of the owner's rxcheck.py).  Run: python3 -I rx_ref_exact.py

Polynomials over F_2 are Python ints (bit i = coefficient of X^i).
Maximal minors of the monomial matrix (X^{k f_l}) are computed EXACTLY as permanents mod 2
(det = perm in characteristic 2) by a dynamic programme over column subsets (Ryser-free DP),
which is a different algorithm from the owner's permutation enumeration.

E1  sympy cross-check of the DP determinant on tiny cases.
E2  For each (a, m): all 2a+2 cofactors M_l nonzero; deg and X-adic order equal the
    rearrangement prediction; cofactor identity sum_l M_l X^{k e_l} = 0 (k = 0..2a);
    rank of the E' (degree <= a-1) matrix is 2a (some 2a x 2a minor nonzero, tested on two row sets);
    v_inf(y0) = deg d0 - deg c0 vs the closed formula and its residue mod Q-1;
    v_0(y0) = ord c0 - ord d0 and its residue (second, independent Kummer certificate);
    band flag 2a+1 <= (m-6)/3.
"""
import sys, itertools

def det_mono(ks, fs):
    """det over F_2 of (X^{k_j f_l}), rows ks, columns fs, as a bit-int polynomial (subset DP)."""
    r = len(ks); assert r == len(fs)
    dp = {0: 1}
    for j, k in enumerate(ks):
        nd = {}
        for mask, poly in dp.items():
            if not poly:
                continue
            for l in range(r):
                if not (mask >> l) & 1:
                    nm = mask | (1 << l)
                    nd[nm] = nd.get(nm, 0) ^ (poly << (k * fs[l]))
        dp = nd
    return dp.get((1 << r) - 1, 0)

def deg(p): return p.bit_length() - 1
def ordx(p): return (p & -p).bit_length() - 1

def E1_sympy():
    import sympy
    X = sympy.symbols('X')
    out = []
    for (ks, fs) in [((0, 1, 2), (1, 2, 4)), ((0, 1, 2), (2, 4, 8)), ((0, 1, 2), (1, 4, 8)),
                     ((0, 1, 2, 3, 4), (1, 2, 8, 16, 32)), ((0, 1, 2, 3, 4), (2, 4, 8, 16, 32)),
                     ((0, 1, 2, 3), (1, 2, 8, 16)), ((1, 2, 3), (1, 4, 8))]:
        M = sympy.Matrix([[X ** (k * f) for f in fs] for k in ks])
        d = sympy.Poly(sympy.expand(M.det(method='berkowitz')), X, modulus=2)
        bits = 0
        for (e,), c in d.terms():
            if int(c) % 2:
                bits |= 1 << e
        out.append(bits == det_mono(ks, fs))
    return out

def E2(a, m):
    Q = 1 << (m // 2)
    assert a + 1 <= m // 2
    rho = 2 * a + 1
    E = [1 << i for i in range(a + 1)] + [Q << i for i in range(a + 1)]
    assert len(set(E)) == 2 * a + 2
    ks = list(range(rho))
    M = [det_mono(ks, E[:l] + E[l + 1:]) for l in range(2 * a + 2)]
    res = {'a': a, 'm': m, 'Q': Q}
    res['all_nonzero'] = all(M)
    pred = True
    for l in range(2 * a + 2):
        f = sorted(E[:l] + E[l + 1:])
        pred &= deg(M[l]) == sum(k * x for k, x in zip(ks, f))
        pred &= ordx(M[l]) == sum(k * x for k, x in zip(ks, f[::-1]))
    res['deg_ord_pred'] = pred
    ident = True
    for k in ks:
        acc = 0
        for l, e in enumerate(E):
            acc ^= M[l] << (k * e)
        ident &= (acc == 0)
    res['cofactor_identity'] = ident
    Ep = [1 << i for i in range(a)] + [Q << i for i in range(a)]
    n1 = det_mono(list(range(2 * a)), Ep)
    n2 = det_mono(list(range(1, 2 * a + 1)), Ep)
    res['Eprime_minor_rows0..2a-1_nonzero'] = bool(n1)
    res['Eprime_minor_rows1..2a_nonzero'] = bool(n2)
    res['deg_Eprime_minor'] = deg(n1)
    c0, d0 = M[0], M[a + 1]
    vinf = deg(d0) - deg(c0)
    formula = -sum((j - 1) * (1 << (j - 1)) for j in range(1, a + 1)) - a * (Q - (1 << a))
    res['vinf_y0'] = vinf
    res['vinf_eq_formula'] = (vinf == formula)
    res['vinf_mod_Qm1'] = vinf % (Q - 1)
    res['residue_eq_2^(a+1)-a-2'] = (vinf % (Q - 1) == (1 << (a + 1)) - a - 2)
    v0 = ordx(c0) - ordx(d0)
    res['v0_y0'] = v0
    res['v0_mod_Qm1'] = v0 % (Q - 1)
    res['band'] = (rho <= (m - 6) / 3)
    res['m>=6a+9'] = (m >= 6 * a + 9)
    res['degs'] = [deg(x) for x in M]
    res['min_deg_cofactor'] = min(deg(x) for x in M)
    res['nterms'] = [bin(x).count('1') for x in M]
    return res, M

if __name__ == "__main__":
    print("E1 sympy cross-check of DP determinant:", E1_sympy())
    for (a, m) in [(1, 4), (1, 6), (2, 6), (1, 10), (2, 12), (1, 16), (1, 18), (1, 20),
                   (2, 22), (2, 24), (2, 26), (3, 28), (3, 30), (4, 34)]:
        r, _ = E2(a, m)
        print("E2", r)
        sys.stdout.flush()
