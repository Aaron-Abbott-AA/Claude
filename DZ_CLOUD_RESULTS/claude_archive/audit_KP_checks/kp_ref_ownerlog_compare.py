"""Sample-by-sample comparison with the owner's kpcheck.log: replicate only the owner's sampling
(galois modulus, random.Random(seed=m).randrange(2, 2^N), same skips), recompute every char poly with referee
algebra (kpref_lib), and compare the factor-degree lists with the logged ones.  Also flags which samples are
genuinely irreducible.
usage: python3 -I kp_ref_ownerlog_compare.py <owner kpcheck.log> m1 m2 ..."""
import sys, os, random, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
import galois
GF2 = galois.GF(2)

log = open(sys.argv[1]).read()
for m in (int(a) for a in sys.argv[2:]):
    block = re.search(r"### kpcheck\.py %d 2 40 %d\n(.*?)(?=###|\Z)" % (m, m), log, re.S).group(1)
    logged = [eval(x) for x in re.findall(r"Pt factor degrees (\[[0-9, ]*\])", block)]
    h = m // 2; n = h - 2; N = 2 * m; q = 1 << m
    F = Field(N, mod=int(galois.irreducible_poly(2, N)))
    rng = random.Random(m); mine = []
    while len(mine) < len(logged):
        al = rng.randrange(2, 1 << N)
        if F.pw(al, q) == al: continue
        c0, c1, d0, d1 = rx_cofactors(F, al, m)
        if not (c0 and d1): continue
        MW = subspace_poly(F, [1, al, F.mul(al, al)])
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(F, P, MW); assert not any(res)
        cp = f2poly_from_coeffs(charpoly_hessenberg(F, frob_matrix(F, Pt, N)))
        co = [(cp >> i) & 1 for i in range(cp.bit_length())][::-1]
        fac, mult = galois.Poly(co, field=GF2).factors()
        mine.append(sorted(sum([[f.degree] * k for f, k in zip(fac, mult)], [])))
    agree = sum(a == b for a, b in zip(mine, logged))
    nirr = sum(d == [n] for d in mine)
    print(f"m={m}: {len(logged)} logged samples; referee factor degrees agree on {agree}/{len(logged)}; genuinely irreducible among them: {nirr}")
