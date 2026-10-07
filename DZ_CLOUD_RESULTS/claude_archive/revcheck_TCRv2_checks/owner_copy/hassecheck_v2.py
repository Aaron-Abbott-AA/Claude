#!/usr/bin/env python3
"""TCR check v2 (half of the samples forced into F_q[X^2]; seeds and commands logged).
TCR check (Claude DZ cloud, 7 Oct 2026). Own code; reads no files.
(H1) Hasse identity in char 2: D^{(2^k)}(s^{2^k}) = (s')^{2^k} for random s in F_{2^m}[X].
(H2) Filtration identity: for w in F_q[X^{2^k}], w = s^{2^k}, and s' = 0 iff w in F_q[X^{2^{k+1}}].
Usage: python3 -I hassecheck.py m trials seed
"""
import sys, random

def mk(m):
    for low in range(1, 1 << m, 2):
        f = (1 << m) | low
        if irred(f, m):
            return f
def pmod(a, f):
    d = f.bit_length() - 1
    while a and a.bit_length() - 1 >= d:
        a ^= f << (a.bit_length() - 1 - d)
    return a
def pm(a, b, f):
    r = 0
    while b:
        if b & 1: r ^= a
        b >>= 1; a <<= 1
    return pmod(r, f)
def gcd(a, b):
    while b: a, b = b, pmod(a, b)
    return a
def irred(f, m):
    x = 2
    def fr(k):
        y = x
        for _ in range(k): y = pm(y, y, f)
        return y
    if fr(m) != x: return False
    for p in [p for p in range(2, m + 1) if m % p == 0 and all(p % d for d in range(2, p))]:
        if gcd(f, fr(m // p) ^ x) != 1: return False
    return True

def main():
    m, trials, seed = map(int, sys.argv[1:4])
    random.seed(seed); f = mk(m)
    mul = lambda a, b: pm(a, b, f)
    def polymul(P, R):
        out = [0] * (len(P) + len(R) - 1)
        for i, a in enumerate(P):
            if a:
                for j, b in enumerate(R):
                    if b: out[i + j] ^= mul(a, b)
        return out
    def polypow2(P, k):
        for _ in range(k): P = polymul(P, P)
        return P
    def binom_odd(n, r):  # C(n,r) mod 2 via Lucas
        return (n & r) == r
    def hasse(P, n):
        return [P[i] if binom_odd(i, n) else 0 for i in range(n, len(P))] or [0]
    def deriv(P):
        return hasse(P, 1)
    def trim(P):
        P = list(P)
        while len(P) > 1 and P[-1] == 0: P.pop()
        return P
    bad1 = bad2 = 0
    nzero = 0
    for _ in range(trials):
        k = random.randrange(0, 4)
        deg = random.randrange(0, 7)
        s = [random.randrange(1 << m) for _ in range(deg + 1)]
        if random.random() < 0.5:  # force s into F_q[X^2] so that s' = 0
            s = [c if i % 2 == 0 else 0 for i, c in enumerate(s)]
        w = polypow2(s, k)
        lhs = trim(hasse(w, 1 << k))
        rhs = trim(polypow2(deriv(s), k))
        if lhs != rhs: bad1 += 1
        # (H2): s' == 0 iff w supported on exponents divisible by 2^{k+1}
        sprime_zero = all(c == 0 for c in deriv(s))
        nzero += sprime_zero
        w_in = all(c == 0 for i, c in enumerate(w) if i % (1 << (k + 1)))
        if sprime_zero != w_in: bad2 += 1
    print(f"cmd: python3 -I hassecheck_v2.py {m} {trials} {seed} | m={m} trials={trials} (s'=0 cases: {nzero}): (H1) Hasse-identity failures {bad1}; (H2) filtration-equivalence failures {bad2}")

if __name__ == '__main__':
    main()
