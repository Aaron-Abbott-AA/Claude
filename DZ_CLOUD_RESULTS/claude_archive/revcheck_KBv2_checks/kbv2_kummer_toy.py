# Sanity toy for KB(vi)'s inputs: for Kummer curves y^e = k(x) over F_q (q = 2^8, 2^12), e odd, e | q-1,
# the number of degree-1 places satisfies N1 <= q + 1 + (deg k - 1)(e - 1) sqrt(q)  (Weil + RH bound 2g <= (r0-1)(e-1)),
# and a degree-1 place x=a with k(a) a nonzero e-th power splits into exactly e rational points.
import random, math
def mk(m, poly):
    def mul(a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
            if a >> m: a ^= poly
        return r
    return mul
def pw(mul, a, n):
    r = 1
    while n:
        if n & 1: r = mul(r, a)
        a = mul(a, a); n >>= 1
    return r
bad = 0; tests = 0
for m, poly in ((8, 0x11d), (12, 0x1053)):
    q = 2 ** m; mul = mk(m, poly); sq = 2 ** (m // 2)
    es = [e for e in range(3, q, 2) if (q - 1) % e == 0 and e <= 65]
    rnd = random.Random(20261007 + m)
    for e in es:
        for trial in range(6):
            dk = rnd.randint(1, 3 * e)
            coeffs = [rnd.randrange(q) for _ in range(dk)] + [rnd.randrange(1, q)]
            def k(x):
                r = 0
                for c in reversed(coeffs): r = mul(r, x) ^ c
                return r
            N1 = 0
            for a in range(q):
                v = k(a)
                if v == 0: N1 += 1
                elif pw(mul, v, (q - 1) // e) == 1: N1 += e   # e-th power: e roots of y^e = v since mu_e in F_q
            # places above infinity: at most e of degree 1
            N1 += e if dk % e == 0 else math.gcd(dk, e)
            tests += 1
            if N1 > q + 1 + max(dk - 1, 0) * (e - 1) * sq: bad += 1
print("Kummer toy: tests", tests, "violations of N1 <= q+1+(deg k-1)(e-1)sqrt(q):", bad)
