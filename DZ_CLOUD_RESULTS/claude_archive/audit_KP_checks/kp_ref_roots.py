"""Referee validation of Lemma FR against ACTUAL roots (no sigma-module on the root side).
usage: python3 -I kp_ref_roots.py <m> <L> <nsamp> <seed>
Big field B = GF(2^{N L}), N = 2m, sparse modulus (taken from galois 'min' list, re-verified here by Rabin's test).
alpha := Tr_{B/F_{2^N}}(x) for random x, with alpha in F_{2^N} \\ F_{2^m}, c0 d1 != 0.
 SIGMA side: char poly of tau^N on F{tau}/F{tau}Pt (kpref_lib), and nullity of (tau^{N L} - 1).
 ROOT side : the F_2-kernel V_B of x -> Pt(x) on B (an NL x NL F_2 system) and the matrix of Fr: x -> x^{2^N} on V_B.
Checks: dim V_B == nullity(tau^{NL} - 1) [FR at level L]; and when dim V_B = n (splitting inside B):
         char poly over F_2 of Fr on V_B == sigma-side char poly.
"""
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kpref_lib import *
import sympy as sp

SPARSE = {140: [140, 6, 4, 1, 0], 240: [240, 8, 5, 3, 0], 288: [288, 8, 7, 6, 4, 2, 0], 336: [336, 7, 4, 1, 0],
          420: [420, 7, 0], 432: [432, 7, 6, 5, 3, 1, 0], 480: [480, 7, 6, 4, 3, 2, 0]}

def primes(n):
    out = []; p = 2
    while n > 1:
        if n % p == 0:
            out.append(p)
            while n % p == 0: n //= p
        p += 1
    return out

def rabin_irreducible(f):
    d = f.bit_length() - 1
    def x2k(k):
        y = 2
        for _ in range(k): y = pmod(psq(y), f)
        return y
    if x2k(d) != 2: return False
    for p in primes(d):
        if pgcd(x2k(d // p) ^ 2, f) != 1: return False
    return True

class SparseField(Field):
    def __init__(self, degs):
        N = degs[0]; mod = sum(1 << e for e in degs)
        super().__init__(N, mod=mod)
        self.tail = [e for e in degs[1:]]
    def reduce(self, a):
        N = self.N
        while a >> N:
            hi = a >> N; a &= (1 << N) - 1
            for e in self.tail: a ^= hi << e
        return a

def f2_kernel(cols, nbits):
    """cols[b] = image (int) of basis vector b. Return list of kernel vectors (ints over basis indices)."""
    piv = {}  # pivot bit -> (vec, combo)
    ker = []
    for b, v in enumerate(cols):
        combo = 1 << b
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]; v ^= pv; combo ^= pc
            else:
                piv[p] = (v, combo); break
        if v == 0: ker.append(combo)
    return ker

def f2_charpoly(Mx):
    n = len(Mx)
    S = sp.Matrix(n, n, lambda i, j: Mx[i][j])
    T = sp.symbols('T')
    cp = sp.Poly((T * sp.eye(n) - S).det(method='berkowitz'), T, modulus=2)
    co = cp.all_coeffs()[::-1]
    return sum((int(c) % 2) << i for i, c in enumerate(co))

def mat_nullity(F, A):
    n = len(A); M = [r[:] for r in A]; rank = 0
    for c in range(n):
        p = next((i for i in range(rank, n) if M[i][c]), None)
        if p is None: continue
        M[rank], M[p] = M[p], M[rank]; iv = F.inv(M[rank][c])
        for i in range(n):
            if i != rank and M[i][c]:
                f = F.mul(M[i][c], iv); M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[rank])]
        rank += 1
    return n - rank

def main(m, L, nsamp, seed):
    h = m // 2; n = h - 2; N = 2 * m; NL = N * L
    B = SparseField(SPARSE[NL]); assert rabin_irreducible(B.mod), "modulus not irreducible"
    rng = random.Random(seed); done = 0; full = 0
    while done < nsamp:
        x = rng.getrandbits(NL); al = 0; y = x
        for _ in range(L): al ^= y; y = B.pw2(y, N)
        if B.pw2(al, N) != al or B.pw2(al, m) == al: continue
        c0, c1, d0, d1 = rx_cofactors(B, al, m)
        if not (c0 and d1): continue
        Wb = [1, al, B.mul(al, al)]
        MW = subspace_poly(B, Wb)
        P = [c0, c1] + [0] * (h - 2) + [d0, d1]
        Pt, res = quotient_top_down(B, P, MW); assert not any(res)
        assert all(B.pw2(c, N) == c for c in Pt), "Pt not over F_{2^N}"
        cp = f2poly_from_coeffs(charpoly_hessenberg(B, frob_matrix(B, Pt, N)))
        TL = frob_matrix(B, Pt, NL)
        nul = mat_nullity(B, [[TL[i][j] ^ (1 if i == j else 0) for j in range(n)] for i in range(n)])
        # root side
        cols = []
        for b in range(NL):
            xb = 1 << b; s = 0; z = xb
            for i, c in enumerate(Pt):
                if c: s ^= B.mul(c, z)
                z = B.sq(z)
            cols.append(s)
        ker = f2_kernel(cols, NL)
        # turn kernel combos into field elements
        V = []
        for combo in ker:
            e = 0; b = 0; cc = combo
            while cc:
                if cc & 1: e ^= 1 << b
                cc >>= 1; b += 1
            assert lin_eval(B, Pt, e) == 0
            V.append(e)
        dimV = len(V)
        line = f"  sample {done+1}: sigma cp={bin(cp)} nullity(tau^NL-1)={nul} dim V_B={dimV}"
        assert dimV == nul, line + "  MISMATCH"
        if dimV == n:
            full += 1
            # Fr on V: coordinates via elimination on V basis
            piv = {}
            for idx, v in enumerate(V):
                c = 1 << idx; w = v
                while w:
                    p = w.bit_length() - 1
                    if p in piv: w ^= piv[p][0]; c ^= piv[p][1]
                    else: piv[p] = (w, c); break
                assert w
            def coords(w):
                c = 0
                while w:
                    p = w.bit_length() - 1
                    assert p in piv, "Fr(V) not in V"
                    w ^= piv[p][0]; c ^= piv[p][1]
                return c
            Mx = [[0] * n for _ in range(n)]
            for j, v in enumerate(V):
                c = coords(B.pw2(v, N))
                for i in range(n): Mx[i][j] = (c >> i) & 1
            cpr = f2_charpoly(Mx)
            line += f"  root-side cp={bin(cpr)}  " + ("MATCH" if cpr == cp else "MISMATCH")
            assert cpr == cp, line
        print(line); done += 1
    print(f"m={m} L={L} NL={NL} samples={done}: all nullity checks agree; full splitting in B for {full} samples, all char polys MATCH")

if __name__ == "__main__":
    main(*(int(a) for a in sys.argv[1:5]))
