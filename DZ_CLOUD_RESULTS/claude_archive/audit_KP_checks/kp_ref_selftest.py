"""Self-tests of kpref_lib: field arithmetic, Hessenberg char poly vs det(tI-A), quotient routine."""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *

rng = random.Random(2026)
for N in (20, 48, 88):
    F = Field(N, seed=N)
    for _ in range(20):
        a, b, c = (rng.getrandbits(N) for _ in range(3))
        assert F.mul(a, b) == F.mul(b, a)
        assert F.mul(a, b ^ c) == F.mul(a, b) ^ F.mul(a, c)
        assert F.pw(a, 1 << N) == a
        if a: assert F.mul(a, F.inv(a)) == 1
        assert F.sq(a) == F.mul(a, a)
    # Hessenberg char poly vs determinant at random points
    for n in (1, 2, 5, 9, 14):
        A = [[rng.getrandbits(N) if rng.random() < 0.7 else 0 for _ in range(n)] for _ in range(n)]
        cp = charpoly_hessenberg(F, A)
        assert len(cp) == n + 1 and cp[-1] == 1
        for _ in range(3):
            t = rng.getrandbits(N)
            val = 0; tp = 1
            for c in cp: val ^= F.mul(c, tp); tp = F.mul(tp, t)
            B = [[(t if i == j else 0) ^ A[i][j] for j in range(n)] for i in range(n)]
            assert val == det(F, B), (N, n)
    # quotient: random Pt, random monic M -> recover
    for _ in range(5):
        M = [rng.getrandbits(N) for _ in range(3)] + [1]
        Pt = [rng.getrandbits(N) for _ in range(6)]
        P = compose_coeffs(F, Pt, M)
        Pt2, res = quotient_top_down(F, P, M)
        assert Pt2 == Pt and not any(res)
    print(f"N={N} mod={bin(F.mod)}: field, charpoly, quotient self-tests OK")
print("ALL SELFTESTS OK")
