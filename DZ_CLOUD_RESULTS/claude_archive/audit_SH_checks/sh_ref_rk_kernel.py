#!/usr/bin/env python3
"""Referee check (SH audit): rational kernel of the RX polynomial, a = 1 (Proposition RK).  Referee code.
Run: nice -n 19 python3 -I sh_ref_rk_kernel.py
P(w) = M1 w + M2 w^2 + M3 w^Q + M4 w^(2Q), M_l the Vandermonde products (F_2[X]), Q = 2^(m/2), q = Q^2.
For a monic denominator g in F_q[X], w = f/g lies in ker P iff
   N_g(f) := M1 f g^(2Q-1) + M2 f^2 g^(2Q-2) + M3 f^Q g^Q + M4 f^(2Q) = 0,
which is F_2-linear in f.  We compute dim_F2 ker N_g on F_q[X]_{<= deg g + 4}.
Every w in ker P ∩ L with denominator dividing g and v_inf(w) >= -(4) appears; W*g always gives dimension 3.
RK predicts dimension exactly 3 for every g.  Also: polynomial kernel (g = 1) on F_q[X]_{<= 8}.
Field: GF(2^m) by log tables with a primitive polynomial found by search (referee's own).
"""
import itertools, random, sys

def find_prim(N):
    for poly in range((1 << N) + 1, 1 << (N + 1), 2):
        x = 1; ok = True
        for i in range((1 << N) - 1):
            x <<= 1
            if x >> N: x ^= poly
            if x == 1 and i < (1 << N) - 2: ok = False; break
        if ok and x == 1: return poly
    raise ValueError

class F:
    def __init__(self, N):
        self.N = N; self.n = 1 << N; poly = find_prim(N)
        self.exp = [0] * (2 * self.n); self.log = [0] * self.n; x = 1
        for i in range(self.n - 1):
            self.exp[i] = x; self.log[x] = i; x <<= 1
            if x >> N: x ^= poly
        for i in range(self.n - 1, 2 * self.n): self.exp[i] = self.exp[i - (self.n - 1)]
    def mul(self, a, b):
        return 0 if a == 0 or b == 0 else self.exp[self.log[a] + self.log[b]]
    def pw(self, a, e):
        if a == 0: return 0 if e else 1
        return self.exp[(self.log[a] * e) % (self.n - 1)]

def pmul(K, a, b):
    if not a or not b: return []
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                if y: r[i + j] ^= K.mul(x, y)
    return r

def ppow(K, a, e):
    r = [1]; b = a
    while e:
        if e & 1: r = pmul(K, r, b)
        b = pmul(K, b, b); e >>= 1
    return r

def cofactors(Q):
    E = [1, 2, Q, 2 * Q]; M = []
    for l in range(4):
        rest = E[:l] + E[l + 1:]; p = 1
        for e, f in itertools.combinations(rest, 2):
            fac = (1 << e) ^ (1 << f); r = 0; b = fac; a = p
            while b:
                if b & 1: r ^= a
                a <<= 1; b >>= 1
            p = r
        M.append([(p >> s) & 1 for s in range(p.bit_length())])
    return M

def kernel_dim(K, Q, M, g, fdeg):
    G = [pmul(K, M[0], ppow(K, g, 2 * Q - 1)), pmul(K, M[1], ppow(K, g, 2 * Q - 2)),
         pmul(K, M[2], ppow(K, g, Q)), M[3]]
    E = [1, 2, Q, 2 * Q]; N = K.N
    basis = {}; ker = 0
    for j in range(fdeg + 1):
        for bit in range(N):
            beta = 1 << bit
            coef = {}
            for l in range(4):
                be = K.pw(beta, E[l]); sh = j * E[l]
                for s, c in enumerate(G[l]):
                    if c:
                        coef[s + sh] = coef.get(s + sh, 0) ^ K.mul(be, c)
            v = 0
            for s, c in coef.items():
                if c: v |= c << (N * s)
            while v:
                p = v.bit_length() - 1
                if p in basis: v ^= basis[p]
                else: basis[p] = v; break
            if v == 0: ker += 1
    return ker

def monic_polys(K, d):
    for coeffs in itertools.product(range(K.n), repeat=d):
        yield list(coeffs) + [1]

if __name__ == "__main__":
    random.seed(20261007)
    plan = [(4, 3, 300), (6, 2, 500), (8, 1, 1000), (10, 1, 300), (12, 1, 100)]
    for m, dg, nrand in plan:
        Q = 1 << (m // 2); K = F(m); M = cofactors(Q)
        polyker = kernel_dim(K, Q, M, [1], 8)
        tested = 0; bad = []; hist = {}
        for d in range(1, dg + 1):
            for g in monic_polys(K, d):
                k = kernel_dim(K, Q, M, g, d + 4); tested += 1
                hist[k] = hist.get(k, 0) + 1
                if k != 3: bad.append(g)
        if nrand:
            for _ in range(nrand):
                g = [random.randrange(K.n) for _ in range(dg + 1)] + [1]
                k = kernel_dim(K, Q, M, g, dg + 1 + 4); tested += 1
                hist[k] = hist.get(k, 0) + 1
                if k != 3: bad.append(g)
        print(dict(m=m, poly_kernel_deg8=polyker, all_monic_g_deg_le=dg,
                   random_extra=(nrand or 0), random_deg=(dg + 1 if nrand else None),
                   denominators_tested=tested, kernel_dim_histogram=hist, bad=bad[:5]), flush=True)
