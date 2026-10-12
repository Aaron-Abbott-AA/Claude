"""Referee re-computation of KP's Frobenius characteristic polynomials (independent code; see kpref_lib).
usage: python3 -I kp_ref_frob.py <m> <r> <nsamp> <seed>
For random alpha in F_{q^r} of exact degree r over F_q (r prime), with c0 d1 != 0 and dim W(alpha) = 3:
 (a) checks that (c0,c1,d0,d1) (Vandermonde products) kill 1, alpha, alpha^2;
 (b) computes M_W by solving a linear system and Pt by top-down solving P = Pt o M_W (residual must be 0);
 (c) computes the char poly of tau^{mr} on F{tau}/F{tau}Pt and on F{tau}/F{tau}P (iterated tau; Hessenberg);
 (d) checks both are in F_2[T] and cp(P) == (T+1)^3 cp(Pt) EXACTLY;
 (e) factors cp(Pt) over F_2 with galois AND sympy (must agree); records the subset-sum set.
Does NOT stop early. Prints the intersection of subset-sum sets and how many samples were irreducible.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
import galois, sympy as sp

GF2 = galois.GF(2)
T = sp.symbols('T')

def factor_degs(f):
    co = [(f >> i) & 1 for i in range(f.bit_length())][::-1]
    fac, mult = galois.Poly(co, field=GF2).factors()
    d1 = sorted(sum([[fz.degree] * k for fz, k in zip(fac, mult)], []))
    _, fl = sp.Poly(sum(T ** i for i in range(f.bit_length()) if (f >> i) & 1), T, modulus=2).factor_list()
    d2 = sorted(sum([[g.degree()] * k for g, k in fl], []))
    assert d1 == d2, (d1, d2)
    return d1

def subset_sums(ds):
    s = {0}
    for d in ds: s |= {x + d for x in s}
    return s

def main(m, r, nsamp, seed):
    h = m // 2; n = h - 2; N = m * r; q = 1 << m
    F = Field(N, seed=1000 + N)
    rng = random.Random(seed)
    poss = None; nirr = 0; done = 0; pats = {}
    while done < nsamp:
        al = rng.getrandbits(N)
        if F.pw(al, q) == al: continue
        c0, c1, d0, d1 = rx_cofactors(F, al, m)
        if not (c0 and d1): continue
        Wb = [1, al, F.mul(al, al)]
        for w in Wb:
            v = F.mul(c0, w) ^ F.mul(c1, F.sq(w)) ^ F.mul(d0, F.pw2(w, h)) ^ F.mul(d1, F.pw2(w, h + 1))
            assert v == 0, "cofactor relation fails"
        MW = subspace_poly(F, Wb)
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(F, P, MW)
        assert not any(res), "P != Pt o M_W"
        assert Pt[0] and Pt[n] == d1
        cpt = f2poly_from_coeffs(charpoly_hessenberg(F, frob_matrix(F, Pt, N)))
        cpP = f2poly_from_coeffs(charpoly_hessenberg(F, frob_matrix(F, P, N)))
        assert cpP == pmul(cpt, 0b1111), "cp(P) != (T+1)^3 cp(Pt)"   # (T+1)^3 = T^3+T^2+T+1
        ds = factor_degs(cpt)
        done += 1
        if ds == [n]: nirr += 1
        pats[tuple(ds)] = pats.get(tuple(ds), 0) + 1
        ss = subset_sums(ds); poss = ss if poss is None else poss & ss
    print(f"m={m} r={r} N={N} mod={hex(F.mod)} seed={seed} samples={done} n={n}")
    print(f"  all checks (a)-(e) passed; irreducible cp(Pt): {nirr}/{done}")
    print(f"  intersection of subset-sum sets: {sorted(poss)}")
    print(f"  patterns: {sorted(pats.items(), key=lambda kv: -kv[1])[:12]}")

if __name__ == "__main__":
    main(*(int(x) for x in sys.argv[1:5]))
