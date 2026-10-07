# gf2k.py -- small exact GF(2^m) arithmetic and univariate polynomials (R22 owner helper).
# Default field GF(2^8), modulus x^8+x^4+x^3+x^2+1 (0x11D, primitive); set_field() switches field.
# Elements are ints 0..2^m-1. NOTE: other modules must access tables via the module (gf2k.EXP etc.).
import random

M = 8
MOD = 0x11D
ORD = (1 << M) - 1
EXP = []
LOG = []


def set_field(m, mod):
    """(re)initialise GF(2^m) with the given primitive modulus; asserts primitivity."""
    global M, MOD, ORD, EXP, LOG
    M, MOD, ORD = m, mod, (1 << m) - 1
    EXP = [0] * (2 * ORD)
    LOG = [0] * (1 << M)
    x = 1
    seen = set()
    for i in range(ORD):
        EXP[i] = x
        LOG[x] = i
        seen.add(x)
        x <<= 1
        if x & (1 << M):
            x ^= MOD
    assert len(seen) == ORD, "modulus not primitive"
    for i in range(ORD, 2 * ORD):
        EXP[i] = EXP[i - ORD]


set_field(8, 0x11D)


def mul(a, b):
    if a == 0 or b == 0:
        return 0
    return EXP[LOG[a] + LOG[b]]


def inv(a):
    assert a != 0
    return EXP[(ORD - LOG[a]) % ORD]


def pw(a, e):
    if e == 0:
        return 1
    if a == 0:
        return 0
    return EXP[(LOG[a] * e) % ORD]


def sqrt(a):
    # a^(2^(M-1))
    return pw(a, 1 << (M - 1))


def rnd(nonzero=False):
    while True:
        a = random.randrange(1 << M)
        if a or not nonzero:
            return a

# ---------- univariate polynomials in t: list of coefficients, low degree first ----------


def ptrim(p):
    p = list(p)
    while p and p[-1] == 0:
        p.pop()
    return p


def padd(p, q):
    n = max(len(p), len(q))
    r = [0] * n
    for i, a in enumerate(p):
        r[i] ^= a
    for i, a in enumerate(q):
        r[i] ^= a
    return ptrim(r)


def pmul(p, q):
    if not p or not q:
        return []
    r = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        if a == 0:
            continue
        la = LOG[a]
        for j, b in enumerate(q):
            if b:
                r[i + j] ^= EXP[la + LOG[b]]
    return ptrim(r)


def pscal(c, p):
    return ptrim([mul(c, a) for a in p])


def pfrob(p, X):
    # (sum a_i t^i)^X = sum a_i^X t^(iX)   (X a power of 2)
    if not p:
        return []
    r = [0] * ((len(p) - 1) * X + 1)
    for i, a in enumerate(p):
        r[i * X] = pw(a, X)
    return ptrim(r)


def pord(p):
    p = ptrim(p)
    if not p:
        return float('inf')
    for i, a in enumerate(p):
        if a:
            return i


def pshift_down(p, k):
    # divide by t^k, assert exact
    p = ptrim(p)
    assert all(a == 0 for a in p[:k]), "not divisible by t^k"
    return p[k:]

# vectors of polynomials


def vadd(u, v):
    return [padd(a, b) for a, b in zip(u, v)]


def vscal(p, v):
    return [pmul(p, a) for a in v]


def vdot(u, v):
    r = []
    for a, b in zip(u, v):
        r = padd(r, pmul(a, b))
    return r


def vcross(u, v):
    return [padd(pmul(u[1], v[2]), pmul(u[2], v[1])),
            padd(pmul(u[2], v[0]), pmul(u[0], v[2])),
            padd(pmul(u[0], v[1]), pmul(u[1], v[0]))]


def vfrob(v, X):
    return [pfrob(a, X) for a in v]


def const(a):
    return ptrim([a])

# matrices: list of rows, entries polys


def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    return [[ptrim(sum_polys([pmul(A[i][l], B[l][j]) for l in range(k)])) for j in range(m)] for i in range(n)]


def sum_polys(ps):
    r = []
    for p in ps:
        r = padd(r, p)
    return r


def mvec(A, v):
    return [sum_polys([pmul(A[i][l], v[l]) for l in range(len(v))]) for i in range(len(A))]


def mT(A):
    return [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]


def outer(col, row):
    return [[pmul(a, b) for b in row] for a in col]


def madd(A, B):
    return [[padd(a, b) for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mscal(p, A):
    return [[pmul(p, a) for a in r] for r in A]

# ---------- linear algebra over GF(2^8) ----------


def nullspace(rows, ncols):
    """rows: list of lists (length ncols). Returns a basis of the right nullspace."""
    A = [list(r) for r in rows]
    piv_cols = []
    r = 0
    for c in range(ncols):
        p = None
        for i in range(r, len(A)):
            if A[i][c]:
                p = i
                break
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        iv = inv(A[r][c])
        A[r] = [mul(iv, x) for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c]:
                f = A[i][c]
                A[i] = [x ^ mul(f, y) for x, y in zip(A[i], A[r])]
        piv_cols.append(c)
        r += 1
        if r == len(A):
            break
    free = [c for c in range(ncols) if c not in piv_cols]
    basis = []
    for fc in free:
        v = [0] * ncols
        v[fc] = 1
        for i, pc in enumerate(piv_cols):
            v[pc] = A[i][fc]  # char 2: -x = x
        basis.append(v)
    return basis
