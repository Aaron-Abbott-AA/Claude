"""Diagnostic: per-sample factor degrees for the owner's sampling at m=24 and m=36, referee algebra.
Also re-computes c0,d1 by the owner's sparse-permutation route to compare the skip logic."""
import sys, os, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
import galois, sympy as sp
GF2 = galois.GF(2)
for m in (24, 36):
    h = m // 2; n = h - 2; N = 2 * m; q = 1 << m
    F = Field(N, mod=int(galois.irreducible_poly(2, N)))
    rng = random.Random(m); done = 0; draws = 0
    while done < 4:
        al = rng.randrange(2, 1 << N); draws += 1
        if F.pw(al, q) == al: continue
        c0, c1, d0, d1 = rx_cofactors(F, al, m)
        if not (c0 and d1): continue
        MW = subspace_poly(F, [1, al, F.mul(al, al)])
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(F, P, MW)
        cp = f2poly_from_coeffs(charpoly_hessenberg(F, frob_matrix(F, Pt, N)))
        co = [(cp >> i) & 1 for i in range(cp.bit_length())][::-1]
        fac, mult = galois.Poly(co, field=GF2).factors()
        done += 1
        print(m, 'draw', draws, 'sample', done, sorted(sum([[f.degree]*k for f, k in zip(fac, mult)], [])))
