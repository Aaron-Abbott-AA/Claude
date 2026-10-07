#!/usr/bin/env python3
"""Referee check for RX, part F (independent of the owner's code).  Run: python3 -I rx_ref_fields.py

Own GF(2^n) arithmetic (carry-less multiply + reduction); the moduli were confirmed irreducible with
galois (see log).  Cofactors at a point are computed as determinants OF THE EVALUATED MATRIX
(Gaussian elimination in the field), i.e. without the exact polynomials (evaluation is a ring map).

F1  (a=1, m in {16,18,20}) GLS_1 obstruction of GLO OB1(c): Delta*Omega_1 evaluated at random beta in
    GF(2^61) is nonzero  =>  Delta*Omega_1 != 0 in F_2[X].  Also checks evaluated dets against the
    exact sparse cofactors from rx_ref_exact (for a=1 they have 6 terms).
F2  Pointwise real type, EXHAUSTIVE over all alpha in F_q for (a,m) = (1,12), (1,16), (2,12):
    at every alpha where the evaluated rho x (2a+2) matrix has rank rho, the cofactor vector (c,d) satisfies
    d_i = kappa c_i^Q for one kappa with kappa^{Q+1} = 1 (zero pattern respected).  Counts the alpha
    with rank < rho and compares with the bound min_l deg M_l.
F3  Same, random samples, for (2,22) and (3,28) (band cases).
"""
import random, sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))  # own checks dir only (python3 -I drops it)

class GF:
    def __init__(self, n, modulus):
        self.n = n; self.mod = modulus; self.size = 1 << n
    def mul(self, a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
            if a >> self.n: a ^= self.mod
        return r
    def sq(self, a): return self.mul(a, a)
    def pw(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def frob(self, a, t):  # a^(2^t)
        for _ in range(t): a = self.mul(a, a)
        return a
    def inv(self, a):
        assert a
        return self.pw(a, self.size - 2)

def det(F, M):
    M = [row[:] for row in M]; r = len(M); d = 1
    for c in range(r):
        p = next((i for i in range(c, r) if M[i][c]), None)
        if p is None: return 0
        M[c], M[p] = M[p], M[c]
        d = F.mul(d, M[c][c]); iv = F.inv(M[c][c])
        for i in range(c + 1, r):
            if M[i][c]:
                f = F.mul(M[i][c], iv)
                M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[c])]
    return d

def rank(F, M):
    M = [row[:] for row in M]; rows = len(M); cols = len(M[0]); rk = 0
    for c in range(cols):
        p = next((i for i in range(rk, rows) if M[i][c]), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]; iv = F.inv(M[rk][c])
        for i in range(rows):
            if i != rk and M[i][c]:
                f = F.mul(M[i][c], iv)
                M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk

def evaluated_matrix(F, beta, a, Q, exps=None):
    rho = 2 * a + 1
    E = exps if exps is not None else [1 << i for i in range(a + 1)] + [Q << i for i in range(a + 1)]
    rows = []
    for k in range(rho):
        w = F.pw(beta, k)
        rows.append([F.frob(w, e.bit_length() - 1) for e in E])  # every exponent is a power of 2
    return rows, E

def cofactors(F, Mv):
    cols = len(Mv[0])
    return [det(F, [row[:l] + row[l + 1:] for row in Mv]) for l in range(cols)]

MODS = {12: 4179, 16: 65581, 22: 4194307, 28: 268435465, 61: 2305843009213693991}

def F1(seed=7061):
    from rx_ref_exact import E2
    F = GF(61, MODS[61]); rng = random.Random(seed); out = []
    for m in (16, 18, 20):
        a = 1; Q = 1 << (m // 2)
        _, Mex = E2(a, m)
        for _ in range(3):
            beta = rng.randrange(2, F.size)
            Mv, E = evaluated_matrix(F, beta, a, Q)
            cof = cofactors(F, Mv)
            # compare with exact sparse polynomials evaluated at beta
            ex = []
            for p in Mex:
                s = 0; i = 0; x = p
                while x:
                    if x & 1: s ^= F.pw(beta, i)
                    x >>= 1; i += 1
                ex.append(s)
            c0, c1, d0, d1 = cof
            Delta = F.mul(c1, F.sq(d0)) ^ F.mul(d1, F.sq(c0))
            Om = F.mul(F.mul(F.pw(c0, 4), F.pw(d1, Q)), F.pw(Delta, Q - 1)) ^ F.mul(c1, F.pw(d0, 4 * Q))
            # rank of the E' matrix (degree <= a-1 relations) at beta: must be 2a
            Mp, _ = evaluated_matrix(F, beta, a, Q, exps=[1 << i for i in range(a)] + [Q << i for i in range(a)])
            out.append(dict(m=m, eval_det_eq_exact=(cof == ex), Delta_nonzero=bool(Delta),
                            DeltaOmega_nonzero=bool(F.mul(Delta, Om)), rank_full=rank(F, Mv) == 3,
                            rank_Eprime=rank(F, Mp)))
    return out

def realtype_at(F, Q, h, cof, a):
    c = cof[:a + 1]; d = cof[a + 1:]
    kap = None
    for ci, di in zip(c, d):
        cq = F.frob(ci, h)
        if ci == 0:
            if di != 0: return False
            continue
        k = F.mul(di, F.inv(cq))
        if kap is None: kap = k
        elif k != kap: return False
    if kap is None: return False
    return F.pw(kap, Q + 1) == 1

def pointwise(a, m, alphas):
    F = GF(m, MODS[m]); Q = 1 << (m // 2); h = m // 2; rho = 2 * a + 1
    full = real = lowrank = 0; c0zero_fullrank = 0
    for al in alphas:
        Mv, E = evaluated_matrix(F, al, a, Q)
        cof = cofactors(F, Mv)
        if any(cof):
            full += 1
            real += realtype_at(F, Q, h, cof, a)
            if cof[0] == 0: c0zero_fullrank += 1
        else:
            lowrank += 1
    return dict(a=a, m=m, tested=len(alphas), rank_rho=full, real_type=real, rank_deficient=lowrank,
                rank_rho_but_c0_zero=c0zero_fullrank)

if __name__ == "__main__":
    import galois
    for n, p in MODS.items():
        print("modulus", n, p, "irreducible:", galois.Poly.Int(p).is_irreducible())
    for r in F1(): print("F1", r)
    sys.stdout.flush()
    for (a, m) in [(1, 12), (2, 12), (1, 16)]:
        print("F2 exhaustive", pointwise(a, m, range(0, 1 << m))); sys.stdout.flush()
    rng = random.Random(1007)
    print("F3 sample", pointwise(2, 22, [rng.randrange(1 << 22) for _ in range(1500)])); sys.stdout.flush()
    print("F3 sample", pointwise(3, 28, [rng.randrange(1 << 28) for _ in range(300)])); sys.stdout.flush()
