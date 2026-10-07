#!/usr/bin/env python3
"""Referee checks for RB(iii) (pair-relation module over L2 = F_q(X,Y)) and RD(b),(c).

Generic ranks over L2 are estimated by the MAX rank of M_L(x,y) = [w_i(x)^{2^e} | w_i^{(Q)}(y)^{2^e}]_{e<=L}
over several random (x,y) in F_q^2 (rank at a point <= generic rank; equality w.h.p. for q = 2^16).

 (M1) W = A(U), U in F_Q (dim rho), A = tau^d + sum_{i<d} h_i(X) tau^i, h_i random polys (deg<=2, F_q coeffs), h_0 != 0.
      Expect bivariate defect d1 = d (d < rho/2) and relation counts n(L) = (L+1-d1)_+ + (L+1-d2)_+ with d2 = rho-d1.
 (M2) RD(b) consistency: W = A(U1) + span(p1,p2), A = tau + h, h a SQUARE (h'=0), U1 in F_Q dim r1, p_i random.
      Compute W0 = ker(d/dX) by brute force over F2-combinations; compare bivariate defects a2(W), a2(W0).
 (M3) RD(c) abstract counterexample: CONSTANT family W = {u^2 + beta u : u in U}, beta notin F_Q.
      All derivatives vanish (W0 = W), sqrt(W) is again constant with the same defect 1, forever: the
      descent never reaches bivariate defect 0 by algebra alone.
Usage: python3 -I check_module.py seed
"""
import sys, random
import numpy as np
import galois

m = 16; h = m // 2; Q = 1 << h; q = 1 << m
F = galois.GF(2**m)

def rank(rows):
    return int(np.linalg.matrix_rank(F(np.array(rows, dtype=np.int64))))

def polyQ(p):
    # coefficients raised to Q
    return galois.Poly(p.coeffs ** Q, field=F)

def rel_count(W, L, samples=4):
    """# independent relations of degree <= L over L2 = (2L+2) - generic rank (if rows >= cols)."""
    best = 0
    WQ = [polyQ(w) for w in W]
    for _ in range(samples):
        x = F(random.randrange(q)); y = F(random.randrange(q))
        rows = []
        for w, wq in zip(W, WQ):
            a = w(x); b = wq(y)
            rows.append([int(a ** (2 ** e)) for e in range(L + 1)] + [int(b ** (2 ** e)) for e in range(L + 1)])
        best = max(best, rank(rows))
    return (2 * L + 2) - best

def biv_defect(W):
    r = len(W)
    for L in range(0, r // 2 + 1):
        if rel_count(W, L) > 0:
            return L
    return r // 2

def FQ_elems():
    gQ = F.primitive_element ** ((q - 1) // (Q - 1))
    return [gQ ** i for i in range(Q - 1)]

def rand_U(dim):
    FQs = FQ_elems()
    while True:
        U = [random.choice(FQs) for _ in range(dim)]
        basis = []
        ok = True
        for v in U:
            v = int(v)
            for b in basis:
                v = min(v, v ^ b)
            if not v:
                ok = False; break
            basis.append(v)
        if ok:
            return U

def rand_poly(deg):
    return galois.Poly([random.randrange(q) for _ in range(deg + 1)], field=F)

def apply_lin(A, u):
    # A = list of coefficient polys [h_0, ..., h_d] meaning sum h_i tau^i ; u in F_q (constant)
    out = galois.Poly([0], field=F)
    for i, hi in enumerate(A):
        out = out + hi * (u ** (2 ** i))
    return out

def main():
    seed = int(sys.argv[1]); random.seed(seed)
    one = galois.Poly([1], field=F)
    # (M1)
    print(f"m={m}, Q={Q}")
    for rho in (6, 8):  # dim U <= m/2 = 8
        for d in (1, 2, 3):
            if not d < rho / 2:
                continue
            U = rand_U(rho)
            A = [rand_poly(2) for _ in range(d)] + [one]
            W = [apply_lin(A, u) for u in U]
            d1 = biv_defect(W); d2 = rho - d1
            counts = [rel_count(W, L) for L in range(0, rho)]
            pred = [max(L + 1 - d1, 0) + max(L + 1 - d2, 0) for L in range(0, rho)]
            # pointwise defect at a few alpha (should be <= d)
            print(f"(M1) rho={rho} deg A={d}: bivariate d1={d1}; counts n(L), L=0..{rho-1}: {counts}; predicted {pred}; match={counts == pred}")
    # (M2)
    for r1 in (8,):
        U1 = rand_U(r1)
        s = rand_poly(2)
        hsq = s * s
        A = [hsq, one]
        W1 = [apply_lin(A, u) for u in U1]
        p1, p2 = rand_poly(5), rand_poly(5)
        W = W1 + [p1, p2]
        rho_p = len(W)
        a2 = biv_defect(W)
        # W0 = kernel of derivative, brute force over F2 combos
        W0 = []
        basis_bits = []
        for mask in range(1, 1 << rho_p):
            w = galois.Poly([0], field=F)
            for i in range(rho_p):
                if mask >> i & 1:
                    w = w + W[i]
            if w.derivative() == galois.Poly([0], field=F):
                v = mask
                for b in basis_bits:
                    v = min(v, v ^ b)
                if v:
                    basis_bits.append(v); W0.append(w)
        a0 = biv_defect(W0) if W0 else None
        print(f"(M2) dim W={rho_p}, a2(W)={a2} (hyp a2<=rho'/2-2: {a2 <= rho_p//2 - 2}); dim W0={len(W0)} (>= rho'-2: {len(W0) >= rho_p-2}); a2(W0)={a0}; RD(b) 'a2(W0)<=a2-1' holds: {a0 is not None and a0 <= a2 - 1}")
    # (M3)
    rho = 8
    U = rand_U(rho)
    while True:
        beta = F(random.randrange(q))
        if beta ** Q != beta:
            break
    W = [galois.Poly([int(u ** 2 + beta * u)], field=F) for u in U]
    line = []
    for k in range(6):
        allzero = all(w.derivative() == galois.Poly([0], field=F) for w in W)
        line.append((k, biv_defect(W), allzero))
        # square root of a constant polynomial: c^(1/2) = c^(q/2)
        W = [galois.Poly([int(w.coeffs[-1] ** (q // 2))], field=F) for w in W]
    print(f"(M3) constant family, beta notin F_Q: (step, bivariate defect, all derivatives zero) = {line}")

if __name__ == '__main__':
    main()
