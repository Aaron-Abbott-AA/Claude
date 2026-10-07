#!/usr/bin/env python3
"""Referee R24: exact POLYNOMIAL check (not random points) of Prop 2.2 and Cor 2.3 over GF(2)[U,Y].
Run: python3 -I prop22_symbolic.py

Setting (kappa_0=1, X=2, rho=1, i.e. Q=2, T=4; affine chart Y2=1, which preserves identities between
forms of equal degree and F-adic orders since F is not a multiple of Y2):
  j1=L^tY, j2=N^tY (L,N random over GF(2)), f=j1 x j2, F an absolutely irreducible conic, F does not divide f_i.
  P^t = F^kP K_P J^[rho,t] + f^[X] (x) eta_P,  eta_P = F^mP eta0_P + J^[rho] w_P  (w_P random: a syzygy part).
  Then (layer identity) J^[X,t]P^t = F * Omega C_P J^[rho,t] with C_P = F^(kP-1) Omega J^[X,t] K_P,
  and (alignment) P^t f^[rho] = a_P f^[X] with a_P = F^mP (eta0_P . f^[rho]).  Both are VERIFIED as polynomial identities.
  A = (U.j1) P^[2] + (U.j2) R^[2].
Checks per configuration:
  (I)  det A == F^4 det(C_A) lambda_A exactly, C_A=(U.j1)C_P^[2]+(U.j2)C_R^[2], lambda_A=(U.j1)a_P^2+(U.j2)a_R^2;
  (II) ord_F det A == 4 + 2 k_Delta + 2 min(ord_F a_P, ord_F a_R)  (k_Delta, ord_F a computed directly);
  (III) det C_A == (U.j1)^2 D0^2 + (U.j1)(U.j2) D1^2 + (U.j2)^2 D2^2 where Delta(v)=v1^2 D0+v1v2 D1+v2^2 D2;
  plus the two degenerate directions of Cor 2.3(i): a_P=a_R=0 => det A=0; Delta==0 (rank-one C pencil with common
  kernel) => det A=0 even with a != 0.
"""
import random
import sympy as sp

random.seed(2410)
Y0, Y1, U0, U1, U2, v1, v2 = sp.symbols("Y0 Y1 U0 U1 U2 v1 v2")
GENS = (Y0, Y1, U0, U1, U2, v1, v2)
def P_(e):
    return sp.Poly(sp.expand(e), *GENS, modulus=2)
Y = [P_(Y0), P_(Y1), P_(1)]
U = [P_(U0), P_(U1), P_(U2)]
ZERO = P_(0); ONE = P_(1)
X, rho = 2, 1

def isz(p):
    # robust zero test (sympy's Poly zero flag can be False for an unnormalised zero rep over GF(2))
    return sp.expand(p.as_expr()) == 0

def rnd_const():
    return P_(random.randrange(2))

def rnd_form(deg):
    # random polynomial in Y0,Y1 of total degree <= deg (affine chart of a form of degree deg)
    e = 0
    for i in range(deg + 1):
        for j in range(deg + 1 - i):
            if random.randrange(2):
                e += Y0 ** i * Y1 ** j
    return P_(e)

def dot(a, b):
    s = ZERO
    for x, y in zip(a, b):
        s = s + x * y
    return s

def cross(a, b):
    return [a[1] * b[2] + a[2] * b[1], a[2] * b[0] + a[0] * b[2], a[0] * b[1] + a[1] * b[0]]

def matmul(A, B):
    return [[dot(A[i], [B[k][j] for k in range(len(B))]) for j in range(len(B[0]))] for i in range(len(A))]

def transpose(A):
    return [list(r) for r in zip(*A)]

def mpow(A, k):
    return [[x ** k for x in row] for row in A]

def det2(M):
    return M[0][0] * M[1][1] + M[0][1] * M[1][0]

def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] + M[1][2] * M[2][1])
            + M[0][1] * (M[1][0] * M[2][2] + M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] + M[1][1] * M[2][0]))

def ordF(g, F):
    if isz(g):
        return None
    k = 0
    while True:
        q, r = sp.div(g, F)
        if not isz(r):
            return k
        g = q
        k += 1

Om = [[ZERO, ONE], [ONE, ZERO]]
while True:
    L = [[random.randrange(2) for _ in range(3)] for _ in range(3)]
    N = [[random.randrange(2) for _ in range(3)] for _ in range(3)]
    j1 = [dot([P_(L[k][i]) for k in range(3)], Y) for i in range(3)]
    j2 = [dot([P_(N[k][i]) for k in range(3)], Y) for i in range(3)]
    f = cross(j1, j2)
    ff = dot(f, f)
    if any(isz(c) for c in f) or isz(ff):
        continue
    # components linearly independent over GF(2)?
    import itertools
    indep = all(not isz(a * f[0] + b * f[1] + c * f[2]) for a, b, c in itertools.product([ONE, ZERO], repeat=3) if not (isz(a) and isz(b) and isz(c)))
    if indep:
        break
F = P_(Y0 * 1 + Y1 ** 2)  # affine chart of Y0*Y2+Y1^2 (smooth conic, absolutely irreducible)
assert all(ordF(fi, F) == 0 for fi in f)
J = [[j1[i], j2[i]] for i in range(3)]
Jr = mpow(J, rho); JX = mpow(J, X)
fr = [x ** rho for x in f]; fX = [x ** X for x in f]
print("L =", L, " N =", N)
print("f =", [str(c.as_expr()) for c in f])
uj1 = dot(U, j1); uj2 = dot(U, j2)

def build(kP, mP, dK=None, eta0=None, K=None, syz=True):
    degP = 2 * X + 2 * mP
    dK_ = degP - 2 * kP - rho
    assert dK_ >= 0
    if K is None:
        K = [[rnd_form(dK_) for _ in range(2)] for _ in range(3)]
    if eta0 is None:
        eta0 = [rnd_const() for _ in range(3)]
    Fk = F ** kP
    KJ = matmul(K, transpose(Jr))
    eta = [F ** mP * e for e in eta0]
    if syz:
        w = [rnd_form(2 * mP - rho) if 2 * mP - rho >= 0 else ZERO for _ in range(2)]
        eta = [eta[i] + dot(Jr[i], w) for i in range(3)]
    Pt = [[Fk * KJ[i][j] + fX[i] * eta[j] for j in range(3)] for i in range(3)]
    C = [[F ** (kP - 1) * x for x in row] for row in matmul(Om, matmul(transpose(JX), K))]
    a = F ** mP * dot(eta0, fr)
    # verify layer identity and alignment as polynomial identities
    lhs = matmul(transpose(JX), Pt)
    rhs = [[F * x for x in row] for row in matmul(matmul(Om, C), transpose(Jr))]
    assert all(isz(lhs[i][j] - rhs[i][j]) for i in range(2) for j in range(3)), "layer identity"
    al = [dot(Pt[i], fr) - a * fX[i] for i in range(3)]
    assert all(isz(c) for c in al), "alignment"
    return Pt, C, a

results = []
def check(name, cfgP, cfgR, expect_zero=False):
    PtP, CP, aP = build(*cfgP[:2], **cfgP[2]) if len(cfgP) > 2 else build(*cfgP)
    PtR, CR, aR = build(*cfgR[:2], **cfgR[2]) if len(cfgR) > 2 else build(*cfgR)
    PP = transpose(PtP); RR = transpose(PtR)
    A = [[uj1 * PP[i][j] ** 2 + uj2 * RR[i][j] ** 2 for j in range(3)] for i in range(3)]
    CA = [[uj1 * CP[i][j] ** 2 + uj2 * CR[i][j] ** 2 for j in range(2)] for i in range(2)]
    lam = uj1 * aP ** 2 + uj2 * aR ** 2
    dA = det3(A)
    dCA = det2(CA)
    I = isz(dA - F ** 4 * dCA * lam)
    Dv = det2([[P_(v1) * CP[i][j] + P_(v2) * CR[i][j] for j in range(2)] for i in range(2)])
    pv = sp.Poly(sp.expand(Dv.as_expr()), v1, v2)
    D0 = P_(pv.coeff_monomial(v1 ** 2)); D1 = P_(pv.coeff_monomial(v1 * v2)); D2 = P_(pv.coeff_monomial(v2 ** 2))
    assert isz(Dv - (P_(v1 ** 2) * D0 + P_(v1 * v2) * D1 + P_(v2 ** 2) * D2)), "Delta extraction"
    III = isz(dCA - (uj1 ** 2 * D0 ** 2 + uj1 * uj2 * D1 ** 2 + uj2 ** 2 * D2 ** 2))
    Deltazero = isz(D0) and isz(D1) and isz(D2)
    if isz(dA):
        II = None
        line = "%s: det A == 0; identity (I) %s; (III) %s; Delta==0: %s; a_P==0: %s, a_R==0: %s" % (
            name, I, III, Deltazero, isz(aP), isz(aR))
        ok = I and III and expect_zero
    else:
        kD = min(o for o in (ordF(D0, F), ordF(D1, F), ordF(D2, F)) if o is not None)
        ma = min(o for o in (ordF(aP, F), ordF(aR, F)) if o is not None)
        oA = ordF(dA, F)
        II = (oA == 4 + 2 * kD + 2 * ma)
        line = "%s: (I) det A = F^4 detC_A lambda_A: %s; (III): %s; ord_F det A = %d, k_Delta=%d, min ord_F a=%d, 4+2k+2m=%d, (II): %s" % (
            name, I, III, oA, kD, ma, 4 + 2 * kD + 2 * ma, II)
        ok = I and III and II and not expect_zero
    print(line, flush=True)
    results.append((name, ok))

check("generic (kP,kR,mP,mR)=(1,1,1,1)", (1, 1), (1, 1))
check("C_P,C_R divisible by F (2,2,1,1)", (2, 1), (2, 1))
check("only C_P divisible by F (2,1,1,1)", (2, 1), (1, 1))
check("F^2|a_P,a_R (1,1,2,2)", (1, 2), (1, 2))
check("(K)-like k_Delta>=1 and F^2|a (2,2,2,2)", (2, 2), (2, 2))
check("mixed orders of a (1,1,1,2)", (1, 1), (1, 2))
check("zero alignment a_P=a_R=0", (1, 1, {"eta0": [ZERO, ZERO, ZERO]}), (1, 1, {"eta0": [ZERO, ZERO, ZERO]}), expect_zero=True)
# Delta==0: K_P = k (x) w^t, K_R = k' (x) w^t (common row vector w) -> C pencil rank one with common kernel
dK = 2 * X + 2 * 1 - 2 * 1 - rho
wv = [rnd_form(0) + ONE, rnd_form(0)]
kv = [rnd_form(dK) for _ in range(3)]; kv2 = [rnd_form(dK) for _ in range(3)]
KP = [[kv[i] * wv[j] for j in range(2)] for i in range(3)]
KR = [[kv2[i] * wv[j] for j in range(2)] for i in range(3)]
check("Delta==0 (rank-one C pencil, common kernel), a != 0", (1, 1, {"K": KP}), (1, 1, {"K": KR}), expect_zero=True)
print("exact failing set:", [n for n, ok in results if not ok])
print("ALL CHECKS PASS:", all(ok for _, ok in results))
