"""Referee check of the §2 Remark (degree-1 places uninformative): for alpha in F_q \\ F_Q with c0 d1 != 0,
the F_2-dimension of ker Pt_alpha inside F_q equals the nullity of (tau^m - 1) on F{tau}/F{tau}Pt (FR, r = 1).
Report that dimension (claimed >= n-1) and the factor degrees of the q-Frobenius char poly.
usage: python3 -I kp_ref_deg1.py <m> <nsamp> <seed>"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
from kp_ref_roots import mat_nullity
import galois
GF2 = galois.GF(2)

def main(m, nsamp, seed):
    h = m // 2; n = h - 2; F = Field(m, seed=777 + m); rng = random.Random(seed); done = 0; dims = {}
    while done < nsamp:
        al = rng.getrandbits(m)
        if F.pw2(al, h) == al: continue          # alpha in F_Q: excluded (Z = F_Q for a = 1)
        c0, c1, d0, d1 = rx_cofactors(F, al, m)
        if not (c0 and d1): continue
        Wb = [1, al, F.mul(al, al)]
        MW = subspace_poly(F, Wb)
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(F, P, MW); assert not any(res)
        Fm = frob_matrix(F, Pt, m)
        nul = mat_nullity(F, [[Fm[i][j] ^ (1 if i == j else 0) for j in range(n)] for i in range(n)])
        # direct count of roots in F_q: F_2-kernel of Pt on F_q (m x m system)
        piv = {}; ker = 0
        for b in range(m):
            v = lin_eval(F, Pt, 1 << b)
            while v:
                p = v.bit_length() - 1
                if p in piv: v ^= piv[p]
                else: piv[p] = v; break
            if v == 0: ker += 1
        assert ker == nul
        dims[ker] = dims.get(ker, 0) + 1; done += 1
    print(f"m={m} n={n}: dim_F2(ker Pt_alpha cap F_q) distribution over {nsamp} alpha in F_q minus F_Q: {sorted(dims.items())} (claim >= n-1 = {n-1}); direct count == FR nullity in all")

if __name__ == "__main__":
    main(*(int(a) for a in sys.argv[1:4]))
