#!/usr/bin/env python3
"""Referee check (SH audit): G-stable extensions of RX's W inside the same P (a = 1).  Referee code.
Run: nice -n 19 python3 -I sh_ref_quotient.py
W = F_2[X]_{<=2} ⊂ R_P, P = M1 + M2 tau + M3 tau^(m/2) + M4 tau^(m/2+1) (RX cofactors).
M_W = subspace polynomial of W (monic, tau-degree 3, coefficients in F_2[X]), built recursively:
      M_{V+<v>} = (tau + M_V(v)) M_V.
Right division P = Ptilde * M_W in F_2(X){tau}; since M_W is monic, Ptilde ∈ F_2[X]{tau} (checked: remainder 0).
R_P / W ≅ ker Ptilde G-equivariantly (via w -> M_W(w)).  A G-stable W' ⊃ W with dim W' = dim W + 1
exists iff G fixes a nonzero vector of ker Ptilde, i.e. iff Ptilde has a nonzero root z in L = F_q(X).
 m = 6 : Ptilde has tau-degree 1, its nonzero root p0/p1 lies in L: R_P (dim 4) is a G-stable,
         even-dimensional extension of W inside the same P (not G-fixed, consistent with RK).
 m = 8, 10, 12 : if z ∈ L were a nonzero root, then at every x0 ∈ F_q with p_top(x0) != 0, z(x0) ∈ F_q would be
         a nonzero root of the specialised Ptilde (a pole of z at x0 forces p_top(x0) = 0).  We count the x0 ∈ F_q
         (all of them for m <= 10, a sample for m = 12) whose specialised Ptilde has only the root 0 in F_q.
         One such x0 proves: no nonzero rational root, hence no G-stable W' ⊃ W of dimension 4.
RESULT (see log): no such x0 exists for m = 8, 10, 12; the specialised kernels always have dim >= m/2 - 3.
This is explained pointwise (PTH: A_alpha(F_Q) ⊂ R_{P_alpha} ∩ F_q has dim m/2, and W(alpha) has dim 3), so the
specialisation test is INCONCLUSIVE here and says nothing about rational roots.  See sh_ref_Zker.py for a direct
(polynomial) rational-root search.
Polynomials over F_2 are Python ints (bit i = coefficient of X^i).
"""
import itertools, random

def cl_mul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r

def cl_sq(a, times=1):
    for _ in range(times): a = cl_mul(a, a)
    return a

def cl_divmod(a, b):
    q = 0; db = b.bit_length()
    while a and a.bit_length() >= db:
        s = a.bit_length() - db; q ^= 1 << s; a ^= b << s
    return q, a

def lin_eval(L, v):  # L = list of F_2[X] coeffs (tau-degree i), v ∈ F_2[X]; returns sum L_i v^(2^i)
    r = 0
    for i, c in enumerate(L):
        if c: r ^= cl_mul(c, cl_sq(v, i))
    return r

def tau_mul(A, B):  # (A*B) in F_2[X]{tau}: tau^i b = b^(2^i) tau^i
    r = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if not a: continue
        for j, b in enumerate(B):
            if b: r[i + j] ^= cl_mul(a, cl_sq(b, i))
    return r

def subspace_poly(basis):
    M = [1]  # identity
    for v in basis:
        c = lin_eval(M, v)
        M = tau_mul([c, 1], M)
    return M

def cofactors(m):
    Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]; M = []
    for l in range(4):
        rest = E[:l] + E[l + 1:]; p = 1
        for e, f in itertools.combinations(rest, 2): p = cl_mul(p, (1 << e) ^ (1 << f))
        M.append(p)
    return M

def right_divide(P, D):  # P = Qt*D + R with deg R < deg D; D monic; exact over F_2[X] since D monic
    P = P[:]; dD = len(D) - 1; Qt = [0] * max(1, len(P) - dD)
    for k in range(len(P) - 1, dD - 1, -1):
        c = P[k]
        if not c: continue
        j = k - dD
        Qt[j] = c  # c tau^j * D has top coefficient c * 1^(2^j) = c
        term = tau_mul([0] * j + [c], D)
        for i, t in enumerate(term): P[i] ^= t
    return Qt, P[:dD]

class GF:
    def __init__(self, N):
        self.N = N; self.n = 1 << N
        for poly in range(self.n + 1, 2 * self.n, 2):
            x = 1; order = 0
            while True:
                x <<= 1
                if x >> N: x ^= poly
                order += 1
                if x == 1 or order > self.n: break
            if x == 1 and order == self.n - 1: break
        self.poly = poly
    def mul(self, a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            a <<= 1; b >>= 1
            if a >> self.N: a ^= self.poly
        return r
    def ev(self, f, x0):  # f ∈ F_2[X] as int
        r = 0
        for i in range(f.bit_length() - 1, -1, -1):
            r = self.mul(r, x0) ^ ((f >> i) & 1)
        return r
    def sq(self, a): return self.mul(a, a)

def kernel_dim_spec(K, coeffs):  # dim_F2 of roots in F_q of sum c_i Z^(2^i), c_i ∈ F_q
    N = K.N; rows = []
    for bit in range(N):
        z = 1 << bit; v = 0; zp = z
        for c in coeffs:
            if c: v ^= K.mul(c, zp)
            zp = K.sq(zp)
        rows.append(v)
    # rank of N vectors in F_2^N
    basis = {}; rank = 0
    for v in rows:
        while v:
            p = v.bit_length() - 1
            if p in basis: v ^= basis[p]
            else: basis[p] = v; rank += 1; break
    return N - rank

def run(m, sample=None):
    Q = 1 << (m // 2)
    Mc = cofactors(m)
    P = [0] * (m // 2 + 2)
    P[0], P[1], P[m // 2], P[m // 2 + 1] = Mc
    MW = subspace_poly([1, 0b10, 0b100])
    # sanity: M_W kills W and has F_2-kernel exactly W on F_2[X]_{<=2}
    killsW = all(lin_eval(MW, v) == 0 for v in range(8))
    Pt, R = right_divide(P, MW)
    exact = all(r == 0 for r in R)
    check = tau_mul(Pt, MW); recon = all((check[i] if i < len(check) else 0) == P[i] for i in range(len(P))) and len(check) == len(P)
    out = dict(m=m, MW_kills_W=killsW, division_exact=exact, reconstruct=recon, Ptilde_tau_degree=len(Pt) - 1,
               deg_p=[c.bit_length() - 1 for c in Pt])
    if len(Pt) - 1 == 1:
        out['note'] = 'Ptilde = p0 + p1 tau: nonzero root p0/p1 ∈ F_2(X) ⊂ L, so R_P (dim m/2+1 = 4) is G-stable'
        return out
    K = GF(m)
    xs = range(K.n) if sample is None else random.sample(range(K.n), sample)
    tested = 0; zero_kernel = 0; hist = {}
    for x0 in xs:
        top = K.ev(Pt[-1], x0)
        if top == 0: continue
        cs = [K.ev(c, x0) for c in Pt]
        k = kernel_dim_spec(K, cs); tested += 1
        hist[k] = hist.get(k, 0) + 1
        if k == 0: zero_kernel += 1
    out.update(points_tested=tested, kernel_dim_histogram=hist, points_with_only_root_0=zero_kernel,
               conclusion=('no nonzero rational root of Ptilde: no G-stable W\' ⊃ W of dim 4' if zero_kernel else 'inconclusive'))
    return out

if __name__ == "__main__":
    random.seed(5)
    print(run(6), flush=True)
    print(run(8), flush=True)
    print(run(10), flush=True)
    print(run(12, sample=400), flush=True)
