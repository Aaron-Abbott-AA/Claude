#!/usr/bin/env python3
"""TXR checks (Claude DZ cloud session, 7 Oct 2026). Own code; reads no external files.

GF(2^m) arithmetic with ints.  Checks for the toy family W = A(U), A = Z^2 + X Z,
U a random rho-dim F2-subspace of F_Q (Q = 2^{m/2}):
  (C1) pointwise defect a(V_alpha) for alpha in a sample of F_q;
  (C2) the pointwise real relation C_alpha = Z^2 + abar(alpha+abar) Z maps V_alpha into F_Q;
  (C3) bivariate rank: [w(X)^{2^e}, w^{(Q)}(Y)^{2^e}]_{e<=1} at independent random (X,Y);
  (C4) control: random rational family W (polys of degree <= u) -> generic defect rho/2,
       both at twisted points (alpha, alpha^Q) and at independent (X,Y).
Usage: python3 -I toycheck.py m rho trials seed
"""
import sys, random

def find_irred(m):
    # smallest-weight search for an irreducible polynomial of degree m (Rabin-style test via x^(2^m) = x and gcds skipped: use order test)
    for low in range(1, 1 << m, 2):
        f = (1 << m) | low
        if is_irred(f, m):
            return f
    raise ValueError

def pmod(a, f):
    df = f.bit_length() - 1
    while a and a.bit_length() - 1 >= df:
        a ^= f << (a.bit_length() - 1 - df)
    return a

def pmulmod(a, b, f):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
    return pmod(r, f)

def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a

def is_irred(f, m):
    # f irreducible iff x^(2^m) == x mod f and gcd(x^(2^(m/p)) - x, f) == 1 for primes p | m
    x = 2
    def frob_pow(k):
        y = x
        for _ in range(k):
            y = pmulmod(y, y, f)
        return y
    if frob_pow(m) != x:
        return False
    ps = [p for p in range(2, m + 1) if m % p == 0 and all(p % d for d in range(2, p))]
    for p in ps:
        if pgcd(f, frob_pow(m // p) ^ x) != 1:
            return False
    return True

class GF:
    def __init__(self, m):
        self.m = m
        self.f = find_irred(m)
        self.q = 1 << m
    def mul(self, a, b):
        return pmulmod(a, b, self.f)
    def pw2(self, a, k):
        for _ in range(k % self.m):
            a = self.mul(a, a)
        return a
    def inv(self, a):
        # a^(q-2)
        r, e, b = 1, self.q - 2, a
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

def rank(F, rows):
    M = [list(r) for r in rows]
    rk, ncol = 0, len(M[0]) if M else 0
    for c in range(ncol):
        piv = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        iv = F.inv(M[rk][c])
        M[rk] = [F.mul(iv, x) for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                t = M[i][c]
                M[i] = [x ^ F.mul(t, y) for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk

def span_basis(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
    return basis

def defect(F, V, h):
    """a(V) = min j with {v^{2^e}, vbar^{2^e}}_{e<=j} dependent (as columns over the rho elements of a basis)."""
    rho = len(V)
    for j in range(0, rho // 2 + 1):
        cols = [[F.pw2(v, e) for v in V] for e in range(j + 1)] + [[F.pw2(v, h + e) for v in V] for e in range(j + 1)]
        # matrix rho x (2j+2): rows = basis elements
        rows = [[cols[c][i] for c in range(len(cols))] for i in range(rho)]
        if rank(F, rows) < 2 * j + 2:
            return j
    return rho // 2

def main():
    m, rho, trials, seed = map(int, sys.argv[1:5])
    assert m % 2 == 0 and rho <= m // 2
    random.seed(seed)
    F = GF(m)
    h = m // 2
    conj = lambda x: F.pw2(x, h)
    FQ = [x for x in range(F.q) if conj(x) == x] if F.q <= 1 << 16 else None
    def rand_FQ():
        while True:
            x = random.randrange(F.q)
            y = F.mul(x, conj(x))  # norm lands in F_Q; norms cover F_Q^*
            if y:
                return y
    # random rho-dim U inside F_Q
    U = []
    while len(span_basis(U)) < rho:
        U = span_basis(U + [rand_FQ()])
    U = span_basis(U)[:rho]
    # (C1),(C2)
    hist = {}
    bad2 = 0
    for _ in range(trials):
        al = random.randrange(F.q)
        V = [F.pw2(u, 1) ^ F.mul(al, u) for u in U]
        if len(span_basis(V)) < rho:
            hist['degenerate'] = hist.get('degenerate', 0) + 1
            continue
        a = defect(F, V, h)
        hist[a] = hist.get(a, 0) + 1
        ab = conj(al)
        c0 = F.mul(ab, al ^ ab)
        for v in V:
            Cv = F.pw2(v, 1) ^ F.mul(c0, v)
            if conj(Cv) != Cv:
                bad2 += 1
    print(f"m={m} rho={rho} field poly={bin(F.f)}")
    print(f"(C1) toy pointwise defect histogram over {trials} random alpha: {hist}")
    print(f"(C2) C_alpha(v) not in F_Q: {bad2} cases")
    # (C3) bivariate at independent (X,Y): w(X) = u^2 + X u ; w^{(Q)}(Y) = u^2 + Y u  (u in F_Q)
    r3 = {}
    for _ in range(trials):
        X, Y = random.randrange(F.q), random.randrange(F.q)
        rows = []
        for u in U:
            wX = F.pw2(u, 1) ^ F.mul(X, u)
            wY = F.pw2(u, 1) ^ F.mul(Y, u)
            rows.append([wX, F.pw2(wX, 1), wY, F.pw2(wY, 1)])
        rk = rank(F, rows)
        r3[rk] = r3.get(rk, 0) + 1
    print(f"(C3) toy bivariate rank of [w(X), w(X)^2, w^(Q)(Y), w^(Q)(Y)^2] at independent (X,Y): {r3}  (<=3 means a bivariate degree-1 relation)")
    # (C4) control: random polynomials of degree <= u_deg with F_q coefficients
    u_deg = 3
    polys = [[random.randrange(F.q) for _ in range(u_deg + 1)] for _ in range(rho)]
    def ev(p, x):
        r = 0
        for c in reversed(p):
            r = F.mul(r, x) ^ c
        return r
    def evQ(p, y):
        return ev([conj(c) for c in p], y)
    tw, ind = {}, {}
    for _ in range(trials):
        al = random.randrange(F.q)
        V = [ev(p, al) for p in polys]
        if len(span_basis(V)) == rho:
            a = defect(F, V, h)
            tw[a] = tw.get(a, 0) + 1
        X, Y = random.randrange(F.q), random.randrange(F.q)
        j = 1
        rows = []
        for p in polys:
            wX, wY = ev(p, X), evQ(p, Y)
            rows.append([F.pw2(wX, e) for e in range(j + 1)] + [F.pw2(wY, e) for e in range(j + 1)])
        rk = rank(F, rows)
        ind[rk] = ind.get(rk, 0) + 1
    print(f"(C4) control random rational family (deg<={u_deg}): pointwise defect hist {tw}; bivariate rank (j=1) hist {ind}")

if __name__ == '__main__':
    main()
