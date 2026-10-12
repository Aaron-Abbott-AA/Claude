#!/usr/bin/env python3
"""KP checks (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I kpcheck.py <m> <r> <nsamp> <seed>
RX family a = 1: W = F_2[X]_{<=2}, P = c0 + c1 tau + d0 tau^h + d1 tau^{h+1} (h = m/2, cofactors M_1..M_4),
P = Pt * M_W with M_W the subspace polynomial of W.  For random places X = alpha of degree r over F_q
(alpha in F_{q^r}, alpha^q != alpha), compute the characteristic polynomial over F_2 of the Frobenius element
(q^r-power) acting on ker Pt (n = h - 2), via the F_{q^r}-linear map tau^{m r} on M = F_{q^r}{tau}/F_{q^r}{tau}Pt
(char poly of tau^{mr} on M = char poly of Frob on the roots).  Output: factor degrees and the set of subset sums
(possible dimensions of a Frobenius-stable subspace). Stops early once the intersection is {0, n}.  Sanity: the same computation on P itself (n = h+1) must
show the factor (T+1)^3 (W is G-fixed) -- reported as 'P_has_(T+1)^3'.
"""
import sys, random, itertools
import sympy as sp

def irreducible(N):
    import galois
    f = int(galois.irreducible_poly(2, N))
    assert f >> N == 1
    return f

class GF2N:
    def __init__(self, N):
        self.N = N; self.mod = irreducible(N)
    def mul(self, a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
            if a >> self.N: a ^= self.mod
        return r
    def sq(self, a): return self.mul(a, a)
    def pw(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def inv(self, a): return self.pw(a, (1 << self.N) - 2)

def sparse_det(ks, exps):
    cnt = {}
    for perm in itertools.permutations(range(len(exps))):
        s = sum(k * exps[p] for k, p in zip(ks, perm))
        cnt[s] = cnt.get(s, 0) ^ 1
    return sorted(s for s, v in cnt.items() if v)

def skew_mul(F, A, B):  # (sum a_i tau^i)(sum b_j tau^j) = sum a_i b_j^{2^i} tau^{i+j}
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if a == 0: continue
        for j, b in enumerate(B):
            if b: out[i + j] ^= F.mul(a, F.pw(b, 1 << i))
    return out

def right_div(F, P, M):  # P = Qt * M + R, M monic
    P = P[:]; dm = len(M) - 1; dq = len(P) - 1 - dm
    Qt = [0] * (dq + 1)
    for j in range(dq, -1, -1):
        a = P[j + dm]
        if a == 0: continue
        Qt[j] = a
        for i, mcoef in enumerate(M):
            P[i + j] ^= F.mul(a, F.pw(mcoef, 1 << j))
    return Qt, P[:dm]

def frob_charpoly(F, Pt, nsteps):
    """char poly (coefficient list over F, low->high) of tau^{nsteps} on F{tau}/F{tau}Pt."""
    n = len(Pt) - 1; lc_inv = F.inv(Pt[n])
    r = [F.mul(c, lc_inv) for c in Pt[:n]]
    A = [[0] * n for _ in range(n)]
    for i in range(n - 1): A[i + 1][i] = 1
    for i in range(n): A[i][n - 1] = r[i]
    def matmul(X, Y):
        return [[__import__('functools').reduce(lambda u, v: u ^ v, (F.mul(X[i][k], Y[k][j]) for k in range(n)), 0)
                 for j in range(n)] for i in range(n)]
    def sigma_pow(X, j):
        return [[F.pw(x, 1 << j) if x else 0 for x in row] for row in X]
    # F_j := A sigma(A) ... sigma^{j-1}(A);  F_{a+b} = F_a sigma^a(F_b)
    res, resj = None, 0
    cur, curj = A, 1
    e = nsteps
    while e:
        if e & 1:
            if res is None: res, resj = cur, curj
            else: res, resj = matmul(res, sigma_pow(cur, resj)), resj + curj
        e >>= 1
        if e: cur, curj = matmul(cur, sigma_pow(cur, curj)), 2 * curj
    # Berkowitz-free: char poly via Hessenberg-free Krylov with fallback (use sympy-free Faddeev-like? use Berkowitz)
    return berkowitz(F, res)

def berkowitz(F, Mx):
    n = len(Mx)
    # returns coefficients c_0..c_n of det(T I - M) (char 2: signs irrelevant)
    C = [1]  # char poly of empty
    for k in range(n):
        # leading principal (k+1)x(k+1): a = M[k][k], R = M[k][:k], Cc = column M[:k][k], A = M[:k][:k]
        a = Mx[k][k]; Rr = Mx[k][:k]; Cc = [Mx[i][k] for i in range(k)]; Ak = [row[:k] for row in Mx[:k]]
        # Toeplitz vector: [1, -a, -R C, -R A C, ..., -R A^{k-1} C]
        t = [1, a]
        v = Cc[:]
        for _ in range(k):
            s = 0
            for i in range(k): s ^= F.mul(Rr[i], v[i])
            t.append(s)
            v = [__import__('functools').reduce(lambda u, w: u ^ w, (F.mul(Ak[i][j], v[j]) for j in range(k)), 0) for i in range(k)]
        # new poly (high->low) = Toeplitz(t) * C(high->low)
        Ch = C[::-1]  # high->low, length k+1
        new = []
        for i in range(k + 2):
            s = 0
            for j in range(k + 1):
                if 0 <= i - j < len(t): s ^= F.mul(t[i - j], Ch[j])
            new.append(s)
        C = new[::-1]
    return C  # low->high

def factor_degrees(coefs):
    T = sp.symbols('T')
    poly = sp.Poly(sum(int(c) * T ** i for i, c in enumerate(coefs)), T, modulus=2)
    _, fl = poly.factor_list()
    degs = []
    for f, mult in fl: degs += [f.degree()] * mult
    lin1 = sum(mult for f, mult in fl if f.degree() == 1 and f.eval(1) % 2 == 0)
    return sorted(degs), lin1

def subset_sums(degs):
    s = {0}
    for d in degs: s |= {x + d for x in s}
    return s

def main(m, r, nsamp, seed):
    h = m // 2; Q = 1 << h; N = m * r
    F = GF2N(N); rng = random.Random(seed)
    E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    Ms = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    q = 1 << m
    poss = None; done = 0; tries = 0
    while done < nsamp and tries < 20 * nsamp:
        tries += 1
        al = rng.randrange(2, 1 << N)
        if F.pw(al, q) == al: continue          # want degree r over F_q (r prime)
        c0, c1, d0, d1 = (__import__('functools').reduce(lambda u, v: u ^ v, (F.pw(al, s) for s in sp_), 0) for sp_ in Ms)
        if not (c0 and d1): continue
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        # subspace polynomial of span(1, al, al^2): S <- (tau + S(w)) S
        S = [1]
        for w in (1, al, F.mul(al, al)):
            sw = 0
            for i, c in enumerate(S): sw ^= F.mul(c, F.pw(w, 1 << i))
            if sw == 0: S = None; break
            S = skew_mul(F, [sw, 1], S)
        if S is None: continue
        Pt, rem = right_div(F, P, S)
        assert not any(rem), "W(alpha) not in ker P_alpha"
        cp = frob_charpoly(F, Pt, N)
        if any(c not in (0, 1) for c in cp):
            print("  WARNING: char poly not over F_2", cp[:4]); continue
        degs, _ = factor_degrees(cp)
        ss = subset_sums(degs)
        poss = ss if poss is None else poss & ss
        # sanity on P itself
        cpP = frob_charpoly(F, P, N)
        degsP, lin1 = factor_degrees(cpP)
        done += 1
        print(f"  alpha#{done}: Pt factor degrees {degs}; P_has_(T+1)^3: {lin1 >= 3}")
        if poss == {0, h - 2}:
            print(f"  -> irreducible Frobenius found (char poly irreducible of degree {h - 2}); stopping early")
            break
    n = h - 2
    band = [k for k in range(3, n + 1) if 6 <= 3 + k <= (m - 6) / 3]
    print(f"m={m} r={r} samples={done} n=dim ker Pt={n}; possible stable dims (intersection) = {sorted(poss) if poss else poss}")
    print(f"  band-relevant k (3 <= k, 6 <= 3+k <= (m-6)/3): {band}; surviving: {[k for k in band if poss and k in poss]}")

if __name__ == "__main__":
    m, r, nsamp, seed = (int(x) for x in sys.argv[1:5])
    main(m, r, nsamp, seed)
