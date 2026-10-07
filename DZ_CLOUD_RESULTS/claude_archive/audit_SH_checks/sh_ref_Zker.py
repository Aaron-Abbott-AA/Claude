#!/usr/bin/env python3
"""Referee check (SH audit): rational roots of Ptilde := P / M_W (right quotient) for RX's a = 1 polynomial P.
Referee code.  Run: nice -n 19 python3 -I sh_ref_Zker.py [m ...]
Z := ker Ptilde ∩ F_q[X]_{<=D}  (F_2-dimension, exact linear algebra over GF(2^m)).
Every z ∈ Z is G-fixed, so for every F_2-subspace Z0 ⊂ Z the set W'' := {w ∈ R_P : M_W(w) ∈ Z0} is a G-stable
subspace of R_P with W ⊂ W'' and dim W'' = 3 + dim Z0 (M_W : R_P -> ker Ptilde is onto with kernel W).
W'' then has the RX relation (C, D) as its unique relation of degree <= 1 and no relation of degree 0
(it contains W; RX v2 (i)), and GLS0 fails for (C, D) (RX v2 (iv)).
For each m we print dim Z, the degrees of the found roots, and an exact re-verification Ptilde(z) = 0 of a basis.
Positive control (control_on_P=True): the same routine applied to P must return dim 3 (= W, by RK).
NOTE: specialisations of Ptilde at x0 ∈ F_q always have >= m/2-3 roots in F_q (sh_ref_quotient.py); this is
explained pointwise by PTH (A_alpha(F_Q) ⊂ R_{P_alpha} ∩ F_q has dim m/2) and says nothing about rational roots.
"""
import sys, itertools
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import sh_ref_quotient as Qm

def spread(p, N):  # F_2[X] int -> int with bit s moved to position N*s
    r = 0; s = 0
    while p:
        if p & 1: r |= 1 << (N * s)
        p >>= 1; s += 1
    return r

def run(m, D=16, control=False):
    N = m
    Mc = Qm.cofactors(m)
    P = [0] * (m // 2 + 2)
    P[0], P[1], P[m // 2], P[m // 2 + 1] = Mc
    MW = Qm.subspace_poly([1, 0b10, 0b100])
    Pt, R = Qm.right_divide(P, MW)
    assert all(r == 0 for r in R)
    if control: Pt = P  # positive control: the same routine applied to P itself must return W (dim 3)
    K = Qm.GF(m)
    sp = [spread(c, N) for c in Pt]
    def frob(b, j):
        for _ in range(j): b = K.sq(b)
        return b
    vecs = []; labels = []
    for k in range(D + 1):
        for bit in range(N):
            beta = 1 << bit; v = 0
            for j, s in enumerate(sp):
                if s:
                    c = frob(beta, j)
                    # multiply each N-bit slot (all equal to 1) by c: no carries across slots since c < 2^N
                    v ^= (s * c) << (N * k * (1 << j))
            vecs.append(v); labels.append((k, bit))
    # kernel via elimination tracking combinations
    basis = {}; kern = []
    for idx, v in enumerate(vecs):
        comb = 1 << idx
        while v:
            p = v.bit_length() - 1
            if p in basis:
                bv, bc = basis[p]; v ^= bv; comb ^= bc
            else:
                basis[p] = (v, comb); break
        if v == 0: kern.append(comb)
    # decode kernel vectors into polynomials z = sum_k z_k X^k (z_k in GF(2^m) as ints)
    roots = []
    for comb in kern:
        z = [0] * (D + 1)
        for idx in range(len(vecs)):
            if (comb >> idx) & 1:
                k, bit = labels[idx]; z[k] ^= 1 << bit
        roots.append(z)
    # independent re-verification: evaluate Ptilde(z) = sum_j p_j z^(2^j) with dense GF polynomial arithmetic
    def pmul(a, b):
        r = [0] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if x:
                for jj, y in enumerate(b):
                    if y: r[i + jj] ^= K.mul(x, y)
        return r
    def frob_poly(z, j):  # z(X)^(2^j) = sum z_k^(2^j) X^(k 2^j)
        r = [0] * ((len(z) - 1) * (1 << j) + 1)
        for k, c in enumerate(z):
            if c: r[k << j] = frob(c, j)
        return r
    verified = 0
    for z in roots[:4]:
        tot = {}
        for j, c in enumerate(Pt):
            cp = [(c >> s) & 1 for s in range(c.bit_length())]
            t = pmul(cp, frob_poly(z, j))
            for i, x in enumerate(t):
                if x: tot[i] = tot.get(i, 0) ^ x
        verified += all(v == 0 for v in tot.values())
    degs = sorted(max((k for k, c in enumerate(z) if c), default=-1) for z in roots)
    return dict(m=m, D=D, control_on_P=control, Ptilde_deg_p=[c.bit_length() - 1 for c in Pt], dimZ_poly_le_D=len(roots),
                pointwise_specialised_kernel_lower_bound=m // 2 - 3, root_degrees=degs, reverified_first=verified,
                support_of_first=[k for k, c in enumerate(roots[0]) if c] if roots else None)

if __name__ == "__main__":
    ms = [int(a) for a in sys.argv[1:]] or [8, 10, 12, 14, 16]
    for m in ms:
        print(run(m, control=True), flush=True)
        print(run(m), flush=True)
