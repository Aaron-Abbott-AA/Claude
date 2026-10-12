"""Referee library for the KP audit (independent of the owner's code).
- Own irreducible moduli (Ben-Or test, seeded random candidates), NOT galois.irreducible_poly.
- GF(2^N) arithmetic with a 4-bit windowed carry-less multiply.
- Upper-Hessenberg reduction + Hessenberg recurrence for characteristic polynomials (not Berkowitz).
- Cofactors evaluated as 3x3 Vandermonde products; subspace polynomial by solving a linear system;
  Pt by solving P = Pt o M_W top-down (not by the owner's right_div routine).
- Frobenius matrix by iterating left multiplication by tau N times on each basis vector.
"""
import random

# ---------- F_2[x] as Python ints ----------
def pmul(a, b):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1; b >>= 1
    return r

def pmod(a, f):
    df = f.bit_length() - 1
    while a.bit_length() - 1 >= df:
        a ^= f << (a.bit_length() - 1 - df)
    return a

def pgcd(a, b):
    while b:
        a, b = b, pmod(a, b)
    return a

def psq(a):
    r = 0; i = 0
    while a:
        if a & 1: r |= 1 << (2 * i)
        a >>= 1; i += 1
    return r

def is_irreducible(f):
    """Ben-Or: f irreducible over F_2 iff gcd(x^{2^i} - x, f) = 1 for i = 1..deg/2."""
    d = f.bit_length() - 1
    if d < 1: return False
    x = 2; cur = x
    for i in range(1, d // 2 + 1):
        cur = pmod(psq(cur), f)
        if pgcd(cur ^ x, f) != 1: return False
    return True

def own_irreducible(N, seed):
    rng = random.Random(seed)
    while True:
        f = (1 << N) | (rng.getrandbits(N) | 1)
        if is_irreducible(f): return f

# ---------- GF(2^N) ----------
class Field:
    def __init__(self, N, seed=12345, mod=None):
        self.N = N
        self.mod = mod if mod is not None else own_irreducible(N, seed)
        assert self.mod >> N == 1
        # reduction table for the top 4 bits overflow handled generically in reduce
    def reduce(self, a):
        N = self.N; f = self.mod
        while a >> N:
            a ^= f << (a.bit_length() - 1 - N)
        return a
    def mul(self, a, b):
        if a == 0 or b == 0: return 0
        # 4-bit windowed carry-less multiply, then reduce
        tbl = [0] * 16
        for i in range(1, 16):
            t = 0
            for j in range(4):
                if (i >> j) & 1: t ^= a << j
            tbl[i] = t
        r = 0; sh = 0
        while b:
            nib = b & 15
            if nib: r ^= tbl[nib] << sh
            b >>= 4; sh += 4
        return self.reduce(r)
    def sq(self, a):
        return self.reduce(psq(a))
    def pw2(self, a, k):
        for _ in range(k): a = self.sq(a)
        return a
    def pw(self, a, e):
        r = 1
        while e:
            if e & 1: r = self.mul(r, a)
            a = self.mul(a, a); e >>= 1
        return r
    def inv(self, a):
        assert a
        return self.pw(a, (1 << self.N) - 2)

# ---------- linear algebra over the field ----------
def solve(F, A, b):
    """Solve A x = b (square, nonsingular) over F by Gaussian elimination."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(i for i in range(c, n) if M[i][c])
        M[c], M[p] = M[p], M[c]
        iv = F.inv(M[c][c])
        M[c] = [F.mul(iv, x) for x in M[c]]
        for i in range(n):
            if i != c and M[i][c]:
                f = M[i][c]
                M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[c])]
    return [M[i][n] for i in range(n)]

def det(F, A):
    n = len(A); M = [r[:] for r in A]; d = 1
    for c in range(n):
        p = next((i for i in range(c, n) if M[i][c]), None)
        if p is None: return 0
        M[c], M[p] = M[p], M[c]
        d = F.mul(d, M[c][c]); iv = F.inv(M[c][c])
        for i in range(c + 1, n):
            if M[i][c]:
                f = F.mul(M[i][c], iv)
                M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[c])]
    return d

def charpoly_hessenberg(F, A):
    """Coefficients (low -> high) of det(T I - A), char 2."""
    n = len(A); H = [r[:] for r in A]
    for j in range(n - 2):
        p = next((i for i in range(j + 1, n) if H[i][j]), None)
        if p is None: continue
        if p != j + 1:
            H[p], H[j + 1] = H[j + 1], H[p]
            for r in H: r[p], r[j + 1] = r[j + 1], r[p]
        iv = F.inv(H[j + 1][j])
        for i in range(j + 2, n):
            if H[i][j]:
                f = F.mul(H[i][j], iv)
                H[i] = [x ^ F.mul(f, y) for x, y in zip(H[i], H[j + 1])]   # row_i -= f row_{j+1}
                for r in H: r[j + 1] ^= F.mul(f, r[i])                     # col_{j+1} += f col_i
    p = [[1]]
    def padd(a, b):
        L = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) ^ (b[i] if i < len(b) else 0) for i in range(L)]
    def pscal(c, a): return [F.mul(c, x) for x in a]
    for k in range(1, n + 1):
        prev = p[k - 1]
        cur = padd([0] + prev, pscal(H[k - 1][k - 1], prev))
        prod = 1
        for i in range(1, k):
            prod = F.mul(prod, H[k - i][k - i - 1])
            if prod == 0: break
            c = F.mul(H[k - 1 - i][k - 1], prod)
            if c: cur = padd(cur, pscal(c, p[k - 1 - i]))
        p.append(cur)
    return p[n]

# ---------- RX objects at X = alpha ----------
def rx_cofactors(F, al, m):
    Q = 1 << (m // 2); E = [1, 2, Q, 2 * Q]
    z = [F.pw(al, e) for e in E]
    out = []
    for l in range(4):
        r = [z[i] for i in range(4) if i != l]
        out.append(F.mul(F.mul(r[0] ^ r[1], r[0] ^ r[2]), r[1] ^ r[2]))
    return out  # c0, c1, d0, d1

def lin_eval(F, coeffs, w):
    s = 0; x = w
    for c in coeffs:
        if c: s ^= F.mul(c, x)
        x = F.sq(x)
    return s

def subspace_poly(F, basis):
    """Monic M with M(x) = x^{2^k} + sum_{i<k} s_i x^{2^i}, vanishing on span(basis) (k = len)."""
    k = len(basis)
    A = [[F.pw2(w, i) for i in range(k)] for w in basis]
    b = [F.pw2(w, k) for w in basis]
    s = solve(F, A, b)
    return s + [1]

def compose_coeffs(F, A, B):
    """tau-coefficients of A o B (A applied after B)."""
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        if not a: continue
        for j, b in enumerate(B):
            if b: out[i + j] ^= F.mul(a, F.pw2(b, i))
    return out

def quotient_top_down(F, P, M):
    """Solve P = Pt o M (M monic of tau-degree k) top-down; return Pt and the residual P - Pt o M."""
    k = len(M) - 1; n = len(P) - 1 - k
    Pt = [0] * (n + 1)
    for d in range(n, -1, -1):
        # coefficient of tau^{d+k} in Pt o M: sum_{i+j=d+k} Pt_i M_j^{2^i}; unknown Pt_d enters with M_k = 1
        s = P[d + k]
        for i in range(d + 1, n + 1):
            j = d + k - i
            if 0 <= j <= k and Pt[i] and M[j]: s ^= F.mul(Pt[i], F.pw2(M[j], i))
        Pt[d] = s
    R = compose_coeffs(F, Pt, M)
    resid = [x ^ y for x, y in zip(P, R)]
    return Pt, resid

def frob_matrix(F, Pt, Nsteps):
    """Matrix (columns = images of tau^j) of tau^{Nsteps} acting by left multiplication on F{tau}/F{tau}Pt."""
    n = len(Pt) - 1; il = F.inv(Pt[n]); r = [F.mul(c, il) for c in Pt[:n]]
    cols = []
    for j in range(n):
        v = [0] * n; v[j] = 1
        for _ in range(Nsteps):
            top = F.sq(v[n - 1])
            w = [0] + [F.sq(x) for x in v[:n - 1]]
            if top:
                w = [x ^ F.mul(top, ri) for x, ri in zip(w, r)]
            v = w
        cols.append(v)
    return [[cols[j][i] for j in range(n)] for i in range(n)]

def f2poly_from_coeffs(cp):
    assert all(c in (0, 1) for c in cp), "char poly not over F_2"
    return sum(c << i for i, c in enumerate(cp))
