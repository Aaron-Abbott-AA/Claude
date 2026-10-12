"""Re-derive, with referee code (kpref_lib), the owner's IRREDUCIBLE Frobenius samples for m = 24..44, m = 0 mod 4.
Only the owner's sampling is replicated (galois modulus for GF(2^{2m}), random.Random(m).randrange(2, 2^N), same skips);
all algebra (cofactors, M_W, Pt, Frobenius matrix, char poly, factorisation) is the referee's.
usage: python3 -I kp_ref_ownersamples.py"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
import galois

GF2 = galois.GF(2)
for m in (24, 28, 32, 36, 40, 44):
    h = m // 2; n = h - 2; N = 2 * m; q = 1 << m
    F = Field(N, mod=int(galois.irreducible_poly(2, N)))
    rng = random.Random(m); done = 0; found = None
    while done < 40:
        al = rng.randrange(2, 1 << N)
        if F.pw(al, q) == al: continue
        c0, c1, d0, d1 = rx_cofactors(F, al, m)
        if not (c0 and d1): continue
        MW = subspace_poly(F, [1, al, F.mul(al, al)])
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(F, P, MW); assert not any(res)
        cp = f2poly_from_coeffs(charpoly_hessenberg(F, frob_matrix(F, Pt, N)))
        done += 1
        co = [(cp >> i) & 1 for i in range(cp.bit_length())][::-1]
        if galois.Poly(co, field=GF2).is_irreducible():
            found = (done, hex(cp)); break
    print(f"m={m}: owner-sampled alpha #{found[0] if found else None} gives IRREDUCIBLE char poly of degree {n}: {found[1] if found else None}")
