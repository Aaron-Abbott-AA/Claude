#!/usr/bin/env python3
"""RX checks (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I rxcheck.py
W = F_2[X]_{<=2a} = span(1, X, ..., X^{2a}),  rho = 2a+1,  exponents E = (1,2,..,2^a, Q,..,Q 2^a).
Relation (C, D) of degree <= a on W = kernel of the rho x (2a+2) matrix (X^{k e}); coefficient for column l is
the maximal minor with column l deleted (char 2, no signs).  Minors are computed EXACTLY as sparse F_2[X]
polynomials (sum over permutations of monomials, mod 2).
A  For (a, m): all 2a+2 minors nonzero ((N0) and more); deg / ord_0 equal the rearrangement predictions;
   v_inf(y0) = deg d0 - deg c0 equals 2^{a+1} - a - 2 and is not divisible by Q-1; the cofactor identity
   sum_l M_l (X^k)^{e_l} = 0 holds for every basis monomial; and a 2a x 2a minor for exponents E' (degree a-1)
   is nonzero (so a(W) = a).
B  Pointwise (a=1, m=16, GF(2^16)): at random alpha with dim W(alpha) = 3, the specialisation (C_alpha, D_alpha)
   is real type: d_i = kappa c_i^Q with kappa^{Q+1} = 1.
C  Extra rational roots: dim_F2 of ker P on F_2[X]_{<=dmax} (a = 1; m = 16, 18).
"""
import itertools, random

def sparse_det(rows_k, exps):
    """det over F_2 of (X^{k_j * e_l}) as a set of exponents with odd multiplicity."""
    cnt = {}
    for perm in itertools.permutations(range(len(exps))):
        s = sum(k * exps[p] for k, p in zip(rows_k, perm))
        cnt[s] = cnt.get(s, 0) ^ 1
    return frozenset(s for s, v in cnt.items() if v)

def partA(a, m):
    Q = 1 << (m // 2); rho = 2 * a + 1
    E = [1 << i for i in range(a + 1)] + [Q << i for i in range(a + 1)]
    ks = list(range(rho))
    minors = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(len(E))]
    nonzero = all(minors)
    # predictions (rearrangement): deg = sorted pairing, ord0 = reverse pairing
    pred_ok = True
    for l in range(len(E)):
        es = sorted(E[:l] + E[l + 1:])
        dg = sum(k * e for k, e in zip(ks, es)); o0 = sum(k * e for k, e in zip(ks, es[::-1]))
        pred_ok &= (max(minors[l]) == dg and min(minors[l]) == o0)
    c0, d0 = minors[0], minors[a + 1]
    vinf = max(d0) - max(c0)
    form = (1 << (a + 1)) - a - 2
    # cofactor identity: sum_l M_l * X^{k e_l} == 0 for each k in ks
    ident = True
    for k in ks:
        cnt = {}
        for l, e in enumerate(E):
            for s in minors[l]:
                cnt[s + k * e] = cnt.get(s + k * e, 0) ^ 1
        ident &= not any(cnt.values())
    Ep = [1 << i for i in range(a)] + [Q << i for i in range(a)]
    lower = bool(sparse_det(ks[:2 * a], Ep)) if a >= 1 else True
    return dict(a=a, m=m, Q=Q, rho=rho, band=(rho <= (m - 6) / 3), all_minors_nonzero=nonzero,
                deg_ord0_predicted=pred_ok, vinf_y0=vinf, formula=form, vinf_mod_Qm1=vinf % (Q - 1),
                cofactor_identity=ident, no_deg_a_minus_1_relation=lower, terms=[len(x) for x in minors])

class GF16:
    N = 16; poly = 0x1100B
    def __init__(self):
        n = 1 << self.N; self.n = n
        self.exp = [0] * (2 * n); self.log = [0] * n; x = 1
        for i in range(n - 1):
            self.exp[i] = x; self.log[x] = i; x <<= 1
            if x & n: x ^= self.poly
        assert x == 1 and len(set(self.exp[:n - 1])) == n - 1
        for i in range(n - 1, 2 * n): self.exp[i] = self.exp[i - (n - 1)]
    def mul(self, a, b): return 0 if a == 0 or b == 0 else self.exp[self.log[a] + self.log[b]]
    def pw(self, a, e): return (0 if e else 1) if a == 0 else self.exp[(self.log[a] * e) % (self.n - 1)]
    def inv(self, a): return self.exp[(self.n - 1 - self.log[a]) % (self.n - 1)]

def partB(nsamp=300, seed=20261007):
    a, m = 1, 16; Q = 256; F = GF16(); rng = random.Random(seed)
    E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    minors = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    def ev(sp, al):
        s = 0
        for e in sp: s ^= F.pw(al, e)
        return s
    tested = real = skipped = 0
    for _ in range(nsamp):
        al = rng.randrange(2, F.n)
        if F.pw(al, 4) == al:  # alpha in F_4: 1, alpha, alpha^2 dependent
            skipped += 1; continue
        c0, c1, d0, d1 = (ev(x, al) for x in minors)
        if c0 == 0 or c1 == 0:
            skipped += 1; continue
        k0 = F.mul(d0, F.inv(F.pw(c0, Q))); k1 = F.mul(d1, F.inv(F.pw(c1, Q)))
        tested += 1
        if k0 == k1 and F.pw(k0, Q + 1) == 1: real += 1
    return dict(tested=tested, real_type=real, skipped=skipped)

def partC(m, dmax):
    a = 1; Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    minors = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    vecs = []
    for k in range(dmax + 1):
        v = 0
        for l, e in enumerate(E):
            for s in minors[l]: v ^= 1 << (s + k * e)
        vecs.append(v)
    # F_2 kernel dimension of k -> vecs[k]
    basis = {}  # pivot -> (vector, combo)
    kernel = 0
    for k, v in enumerate(vecs):
        combo = 1 << k
        while v:
            p = v.bit_length() - 1
            if p in basis:
                bv, bc = basis[p]; v ^= bv; combo ^= bc
            else:
                basis[p] = (v, combo); break
        if v == 0: kernel += 1
    return dict(m=m, dmax=dmax, kernel_dim_on_F2X=kernel)

if __name__ == "__main__":
    for (a, m) in [(1, 16), (1, 18), (1, 20), (2, 22), (2, 24), (2, 26), (3, 28), (3, 30)]:
        print("A", partA(a, m))
    print("B a=1 m=16", partB())
    for m in (16, 18):
        print("C", partC(m, 48))

def partD(dmax=6):
    """a=1, m=16: F_2-dimension of ker P on F_q[X]_{<=dmax} (F_q = GF(2^16) coefficients)."""
    a, m = 1, 16; Q = 256; F = GF16(); E = [1, 2, Q, 2 * Q]; ks = [0, 1, 2]
    minors = [sparse_det(ks, E[:l] + E[l + 1:]) for l in range(4)]
    basis = {}; kernel = 0; nvec = 0
    for k in range(dmax + 1):
        for bit in range(16):
            beta = 1 << bit
            coef = {}
            for l, e in enumerate(E):
                be = F.pw(beta, e)
                for s in minors[l]:
                    coef[s + k * e] = coef.get(s + k * e, 0) ^ be
            v = 0
            for s, c in coef.items():
                if c: v |= c << (16 * s)
            nvec += 1
            while v:
                p = v.bit_length() - 1
                if p in basis: v ^= basis[p]
                else: basis[p] = v; break
            if v == 0: kernel += 1
    return dict(m=m, dmax=dmax, F2_vectors=nvec, kernel_dim_on_FqX=kernel, expected_from_W_tensor="3 (W itself)")

if __name__ == "__main__":
    print("D", partD(6))
