#!/usr/bin/env python3
"""PTH checks (Claude DZ cloud, 7 Oct 2026); also k = dim ker(C) on F_q and the sharper bound dim(V cap A(F_Q)) >= rho - k. Own code; reads no files.
For random real C (deg a, c0,ca != 0) and random rho-dim V inside C^{-1}(F_Q) (so C(V) in F_Q):
  (1) compute a(V) exactly (rank test on F^e, chiF^e);
  (2) when a(V) = a: compute the F2-space of Lang solutions A (deg <= a) of  C*A = (C*A)^{(Q)}
      [kappa = 1 since the real relation is (C, Cbar)], take a minimal-degree nonzero A,
      check: A injective on F_Q, A(F_Q) inside the root space of P = C + Cbar tau^{m/2},
      and dim(V cap A(F_Q)) >= rho - a(V).
Usage: python3 -I pthcheck.py m rho a trials seed
"""
import sys, random

def find_irred(m):
    for low in range(1, 1 << m, 2):
        f = (1 << m) | low
        if is_irred(f, m):
            return f
def pmod(a, f):
    d = f.bit_length() - 1
    while a and a.bit_length() - 1 >= d:
        a ^= f << (a.bit_length() - 1 - d)
    return a
def pmulmod(a, b, f):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
    return pmod(r, f)
def pgcd(a, b):
    while b: a, b = b, pmod(a, b)
    return a
def is_irred(f, m):
    x = 2
    def fr(k):
        y = x
        for _ in range(k): y = pmulmod(y, y, f)
        return y
    if fr(m) != x: return False
    for p in [p for p in range(2, m + 1) if m % p == 0 and all(p % d for d in range(2, p))]:
        if pgcd(f, fr(m // p) ^ x) != 1: return False
    return True

class GF:
    def __init__(s, m):
        s.m, s.f, s.q = m, find_irred(m), 1 << m
    def mul(s, a, b): return pmulmod(a, b, s.f)
    def pw2(s, a, k):
        for _ in range(k % s.m): a = s.mul(a, a)
        return a
    def inv(s, a):
        r, e, b = 1, s.q - 2, a
        while e:
            if e & 1: r = s.mul(r, b)
            b = s.mul(b, b); e >>= 1
        return r

def rank_Fq(F, rows):
    M = [list(r) for r in rows]; rk = 0
    for c in range(len(M[0]) if M else 0):
        piv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if piv is None: continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = F.inv(M[rk][c]); M[rk] = [F.mul(iv, x) for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                t = M[i][c]; M[i] = [x ^ F.mul(t, y) for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk

def f2_basis(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v: basis.append(v)
    return basis

def f2_kernel(cols, ncols):
    """cols: list of ints (column vectors as bitmasks over rows). Return basis of kernel as bitmasks over columns."""
    # Gaussian elimination tracking combinations
    rows = []  # (vec, combo)
    kernel = []
    for j, c in enumerate(cols):
        v, comb = c, 1 << j
        for (bv, bc) in rows:
            if v ^ bv < v:
                v ^= bv; comb ^= bc
        if v: rows.append((v, comb)); rows.sort(key=lambda t: -t[0])
        else: kernel.append(comb)
    return kernel

def main():
    m, rho, a, trials, seed = map(int, sys.argv[1:6])
    random.seed(seed); F = GF(m); h = m // 2
    conj = lambda x: F.pw2(x, h)
    def tau_apply(C, z):  # C = list of coeffs c_e (e = 0..), C(z) = sum c_e z^{2^e}
        r = 0
        for e, c in enumerate(C):
            if c: r ^= F.mul(c, F.pw2(z, e))
        return r
    def tau_mul(C, A):  # composition C o A in F_q{tau}
        out = [0] * (len(C) + len(A) - 1)
        for i, c in enumerate(C):
            if c:
                for j, x in enumerate(A):
                    if x: out[i + j] ^= F.mul(c, F.pw2(x, i))
        return out
    FQ_basis = f2_basis([F.mul(x, conj(x)) for x in range(1, F.q)][:4 * h])  # norms span F_Q
    assert len(FQ_basis) == h
    def defect(V):
        for j in range(0, rho // 2 + 1):
            rows = [[F.pw2(v, e) for e in range(j + 1)] + [F.pw2(v, h + e) for e in range(j + 1)] for v in V]
            if rank_Fq(F, rows) < 2 * j + 2: return j
        return rho // 2
    stats = {'trials': 0, 'aV_eq_a': 0, 'fail_inj': 0, 'fail_root': 0, 'fail_dim': 0, 'min_slack': None, 'min_slack_k': None, 'k_hist': {}, 'full_twisted': 0, 'degA_hist': {}}
    for _ in range(trials):
        C = [random.randrange(1, F.q)] + [random.randrange(F.q) for _ in range(a - 1)] + [random.randrange(1, F.q)] if a >= 1 else [random.randrange(1, F.q)]
        # preimage of F_Q under C (F2-linear map on F_q), then random rho-dim subspace
        imgs = [tau_apply(C, 1 << i) for i in range(m)]
        # solve C(z) in F_Q: z with conj(C(z)) + C(z) = 0
        cols = [conj(y) ^ y for y in imgs]
        ker = f2_kernel(cols, m)  # combos over basis bits = elements z
        pre = ker  # elements z (bitmask = z itself since basis is 1<<i)
        if len(pre) < rho: continue
        V = []
        while len(f2_basis(V)) < rho:
            z = 0
            for b in pre:
                if random.random() < 0.5: z ^= b
            V = f2_basis(V + [z]) if z else V
        V = f2_basis(V)[:rho]
        stats['trials'] += 1
        aV = defect(V)
        if aV != a: continue
        stats['aV_eq_a'] += 1
        # Lang solutions A (deg <= a): map A -> CA + (CA)^{(Q)} is F2-linear on F_q^{a+1}
        ncols = m * (a + 1)
        colsL = []
        for k in range(a + 1):
            for i in range(m):
                A = [0] * (a + 1); A[k] = 1 << i
                B = tau_mul(C, A)
                vec = 0
                for t, bcoef in enumerate(B):
                    vec |= (bcoef ^ conj(bcoef)) << (m * t)
                colsL.append(vec)
        kerL = f2_kernel(colsL, ncols)
        sols = []
        for comb in kerL:
            A = [0] * (a + 1)
            for j in range(ncols):
                if comb >> j & 1: A[j // m] ^= 1 << (j % m)
            sols.append(A)
        def degA(A):
            return max((i for i, x in enumerate(A) if x), default=-1)
        # minimal degree nonzero element of the F2-span: reduce by echelon on top degree
        span = f2_basis([sum(x << (m * i) for i, x in enumerate(A)) for A in sols])
        best = min(span, key=lambda v: v.bit_length())
        A = [(best >> (m * i)) & ((1 << m) - 1) for i in range(a + 1)]
        dA = degA(A)
        stats['degA_hist'][dA] = stats['degA_hist'].get(dA, 0) + 1
        imgA = [tau_apply(A, x) for x in FQ_basis]
        if len(f2_basis(imgA)) != h: stats['fail_inj'] += 1
        Cbar = [conj(c) for c in C]
        for z in imgA:
            if tau_apply(C, z) ^ tau_apply(Cbar, conj(z)): stats['fail_root'] += 1; break
        dV, dAF = len(f2_basis(V)), len(f2_basis(imgA))
        dsum = len(f2_basis(V + imgA))
        inter = dV + dAF - dsum
        slack = inter - (rho - aV)
        kC = len(f2_kernel(imgs, m))  # dim ker C on F_q
        stats['k_hist'][kC] = stats['k_hist'].get(kC, 0) + 1
        sk = inter - (rho - kC)
        if sk < 0: stats['fail_dim'] += 1
        stats['min_slack_k'] = sk if stats['min_slack_k'] is None else min(stats['min_slack_k'], sk)
        if inter == rho: stats['full_twisted'] += 1
        if slack < 0: stats['fail_dim'] += 1
        stats['min_slack'] = slack if stats['min_slack'] is None else min(stats['min_slack'], slack)
    print(f"cmd: python3 -I pthcheck.py {m} {rho} {a} {trials} {seed} | {stats}")

if __name__ == '__main__':
    main()
