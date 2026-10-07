#!/usr/bin/env python3
"""SL checks (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I slcheck.py
RX family, a = 1: W = F_2[X]_{<=2}, E = (1, 2, Q, 2Q), cofactors M_1..M_4 = (c0, c1, d0, d1).
V  The cofactors equal the Vandermonde products prod_{pairs not containing l} (X^e + X^e') (exact, F_2[X] as ints);
   degrees (5Q, 5Q, 4Q+2, 2Q+2); valuations at X and at X+1 equal (Q+4, Q+2, 4, 4).
R  F_2-dimension of ker P on F_q[X]_{<=3} (F_q coefficients) for m = 16, 18, 20: expected 3 (= W), i.e. no
   rational root outside W of degree <= 3 (Proposition RK proves degree <= 2 and no finite poles).
"""
import itertools

def pmul(a, b):  # carry-less multiply of F_2[X] polynomials encoded as ints
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r

def sparse_det(ks, exps):
    cnt = {}
    for perm in itertools.permutations(range(len(exps))):
        s = sum(k * exps[p] for k, p in zip(ks, perm))
        cnt[s] = cnt.get(s, 0) ^ 1
    return sum(1 << s for s, v in cnt.items() if v)

def val_at(poly, pi):  # multiplicity of irreducible pi in poly (F_2[X] ints)
    def pdivmod(a, b):
        q = 0; db = b.bit_length()
        while a and a.bit_length() >= db:
            sh = a.bit_length() - db; q ^= 1 << sh; a ^= b << sh
        return q, a
    v = 0
    while poly:
        q, r = pdivmod(poly, pi)
        if r: break
        poly = q; v += 1
    return v

def partV(m):
    Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    M = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    ok_prod = True
    for l in range(4):
        rest = E[:l] + E[l + 1:]
        p = 1
        for e, f in itertools.combinations(rest, 2): p = pmul(p, (1 << e) ^ (1 << f))
        ok_prod &= (p == M[l])
    degs = [x.bit_length() - 1 for x in M]
    vX = [val_at(x, 0b10) for x in M]; v1 = [val_at(x, 0b11) for x in M]
    return dict(m=m, vandermonde_product=ok_prod, degs=degs, expected=[5 * Q, 5 * Q, 4 * Q + 2, 2 * Q + 2],
                v_X=vX, v_Xp1=v1, expected_v=[Q + 4, Q + 2, 4, 4])

PRIM = {16: 0x1100B, 18: 0x40081, 20: 0x100009}
class GF:
    def __init__(self, N):
        n = 1 << N; self.n = n; poly = PRIM[N]
        self.exp = [0] * (2 * n); self.log = [0] * n; x = 1
        for i in range(n - 1):
            self.exp[i] = x; self.log[x] = i; x <<= 1
            if x & n: x ^= poly
        assert x == 1
        seen = bytearray(n)
        for i in range(n - 1): seen[self.exp[i]] = 1
        assert sum(seen) == n - 1, "not primitive"
        for i in range(n - 1, 2 * n): self.exp[i] = self.exp[i - (n - 1)]
    def pw(self, a, e): return (0 if e else 1) if a == 0 else self.exp[(self.log[a] * e) % (self.n - 1)]

def partR(m, dmax=3):
    N = m; Q = 1 << (m // 2); F = GF(N); E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    M = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    supp = [[s for s in range(x.bit_length()) if (x >> s) & 1] for x in M]
    basis = {}; kernel = 0; nvec = 0
    for k in range(dmax + 1):
        for bit in range(N):
            beta = 1 << bit
            coef = {}
            for l, e in enumerate(E):
                be = F.pw(beta, e)
                for s in supp[l]:
                    coef[s + k * e] = coef.get(s + k * e, 0) ^ be
            v = 0
            for s, c in coef.items():
                if c: v |= c << (N * s)
            nvec += 1
            while v:
                p = v.bit_length() - 1
                if p in basis: v ^= basis[p]
                else: basis[p] = v; break
            if v == 0: kernel += 1
    return dict(m=m, dmax=dmax, F2_vectors=nvec, kernel_dim=kernel)

if __name__ == "__main__":
    for m in (8, 10, 16, 18, 20):
        print("V", partV(m))
    for m in (16, 18, 20):
        print("R", partR(m))
