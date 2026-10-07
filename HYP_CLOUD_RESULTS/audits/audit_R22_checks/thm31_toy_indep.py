# thm31_toy_indep.py -- referee R22: independent exact toy for Prop. 2.3 (*) and Thm 3.1, written from scratch
# with the `galois` package (the owner's gf2k helper and toy are NOT used).
#
# Difference from the owner's toy: the second layer S is a COMPLETELY GENERAL 3x3 matrix of power series in t
# (owner: S = J^[X] C'' J^[rho],t + f^[X] (x) xi), the TSY matrix C is recovered by solving H=[f^[X]]_x S =
# J^[X] C J^[rho],t from 2x2 unit minors (and the full factorisation is verified), and alignment
# S f^[rho] = a' f^[X] is imposed as a linear condition.  Everything lives on one line Y(t)=z+tV, mod t^K.
#   P_c^t = f^[X] (x) kappa_c + F S,  kappa_c = lam * c^t A(t) J(Y)^[rho],t  (first layer, CMIX form),
#   A(t) = A0 + t^nu A1 (nu=None: constant), with the slope equation c^t A0 c^[Q] = 0,
#   z = e(u), g u = f(z), omega = (f(z+tV)+g u)/t, b = J(Y)^t omega (TSYC: constant), c = sqrt(b).
# Checks:
#  (1) TSYC: b constant; Lemma 2.1(ii) f x v = J Omega J^t v (kappa_0=1).
#  (2) identity (*) mod t^K for random S satisfying alignment only (no FN), for constant AND non-constant A;
#  (3) the remark after Prop 2.3: (*).u^[X] is identically 0 on both sides; (*).omega^[X] = t^rho F b^[X]^t C b^[rho];
#  (4) FN imposed (mod t^(K+e)) together with alignment: solvability vs. the prediction ord s >= e-X;
#      for every sampled solution: ord C_c b^[rho] >= min(X-rho, X+ord s-e), the congruence (ii) mod t^X,
#      sharpness (order attained), and the referee's EXACT form
#        C_c b^[rho] = (t^(X-rho) mu^ + t^X s/F) Omega b^[X]   (mod t^(K-rho)),
#      where S u^[rho] = theta omega^[X] + mu u^[X], mu^ = g^(rho-X) mu, and mu^ = a' mod t^rho.
# Run: python3 -I thm31_toy_indep.py
import sys
import numpy as np
import galois

GF = galois.GF(2 ** 8)
RNG = np.random.default_rng(7)


def rnd(nz=False):
    while True:
        x = GF(int(RNG.integers(256)))
        if x != 0 or not nz:
            return x


# ---------- power series mod t^K as GF arrays of length K ----------
class Ser:
    K = 40


def Z():
    return GF.Zeros(Ser.K)


def const(x):
    s = Z(); s[0] = x; return s


def mono(k, x=1):
    s = Z()
    if k < Ser.K:
        s[k] = x
    return s


def mul(a, b):
    c = np.convolve(a, b)
    return c[:Ser.K] if len(c) >= Ser.K else np.concatenate([c, GF.Zeros(Ser.K - len(c))])


def frob(a, p):
    out = Z()
    for i in range(Ser.K):
        if i * p < Ser.K and a[i] != 0:
            out[i * p] = a[i] ** p
    return out


def ordr(a):
    nz = np.nonzero(np.asarray(a))[0]
    return int(nz[0]) if len(nz) else 10 ** 9


def inv_unit(a):
    assert a[0] != 0
    r = Z(); r[0] = GF(1) / a[0]
    for k in range(1, Ser.K):
        acc = GF(0)
        for i in range(1, k + 1):
            acc = acc + a[i] * r[k - i]
        r[k] = acc * r[0]
    return r


def shift(a, k):  # multiply by t^k (k may be negative if divisible)
    if k >= 0:
        return np.concatenate([GF.Zeros(k), a[:Ser.K - k]]) if k < Ser.K else Z()
    assert ordr(a) >= -k, "not divisible"
    return np.concatenate([a[-k:], GF.Zeros(-k)])


def vcross(a, b):
    return [mul(a[1], b[2]) + mul(a[2], b[1]), mul(a[2], b[0]) + mul(a[0], b[2]), mul(a[0], b[1]) + mul(a[1], b[0])]


def vdot(a, b):
    return mul(a[0], b[0]) + mul(a[1], b[1]) + mul(a[2], b[2])


def mvec(M, v):
    return [sum((mul(M[i][j], v[j]) for j in range(len(v))), start=Z()) for i in range(len(M))]


def ccross(a, b):
    return GF([int(a[1] * b[2] + a[2] * b[1]), int(a[2] * b[0] + a[0] * b[2]), int(a[0] * b[1] + a[1] * b[0])])


def setup(rho, X):
    while True:
        L = GF.Random((3, 3), seed=int(RNG.integers(1 << 30)))
        N = GF.Random((3, 3), seed=int(RNG.integers(1 << 30)))
        if np.linalg.det(L) != 0 and np.linalg.det(N) != 0:
            break
    while True:
        u = GF.Random(3, seed=int(RNG.integers(1 << 30)))
        z = ccross(L @ u, N @ u)
        fz = ccross(L.T @ z, N.T @ z)
        k = int(np.nonzero(np.asarray(u))[0][0])
        g = fz[k] / u[k]
        if g != 0 and np.all(np.asarray(fz + g * u) == 0):
            break
    V = GF.Random(3, seed=int(RNG.integers(1 << 30)))
    Y = [const(z[i]) + mono(1, V[i]) for i in range(3)]
    j1 = [sum((mul(const(L.T[i, j]), Y[j]) for j in range(3)), start=Z()) for i in range(3)]
    j2 = [sum((mul(const(N.T[i, j]), Y[j]) for j in range(3)), start=Z()) for i in range(3)]
    f = vcross(j1, j2)
    om = [shift(f[i] + const(g * u[i]), -1) for i in range(3)]
    b0 = vdot(j1, om)
    b1 = vdot(j2, om)
    tsyc = ordr(shift(b0, 0) + const(b0[0])) >= Ser.K and ordr(b1 + const(b1[0])) >= Ser.K
    b = GF([int(b0[0]), int(b1[0])])
    c = GF([int(np.sqrt(b[0])), int(np.sqrt(b[1]))])
    assert np.all(np.asarray(c ** 2 + b) == 0)
    # Lemma 2.1(ii) (R18-T 2.1(i), exponent 1): f x v = J Omega J^t v for a random constant v
    v = [const(rnd()) for _ in range(3)]
    lhs = vcross(f, v)
    Jtv = [vdot(j1, v), vdot(j2, v)]
    rhs = [mul(j1[i], Jtv[1]) + mul(j2[i], Jtv[0]) for i in range(3)]
    lem21 = all(ordr(lhs[i] + rhs[i]) >= Ser.K for i in range(3))
    return dict(L=L, N=N, u=u, z=z, g=g, V=V, Y=Y, j1=j1, j2=j2, f=f, om=om, b=b, c=c, tsyc=tsyc, lem21=lem21)


def first_layer(D, rho, nu):
    Q = 2 * rho
    c = D['c']
    cQ = c ** Q
    while True:
        A0 = GF.Random((2, 2), seed=int(RNG.integers(1 << 30)))
        if cQ[1] != 0 and c[1] != 0:
            s = c[0] * (A0[0, 0] * cQ[0] + A0[0, 1] * cQ[1]) + c[1] * A0[1, 0] * cQ[0]
            A0[1, 1] = s / (c[1] * cQ[1])
        if np.linalg.det(A0) != 0 and (c @ A0 @ cQ) == 0:
            break
    A = [[const(A0[i, j]) for j in range(2)] for i in range(2)]
    if nu is not None:
        while True:
            A1 = GF.Random((2, 2), seed=int(RNG.integers(1 << 30)))
            if (c @ A1 @ cQ) != 0:
                break
        A = [[A[i][j] + mono(nu, A1[i, j]) for j in range(2)] for i in range(2)]
    lam = rnd(nz=True)
    row = [mul(const(c[0]), A[0][k]) + mul(const(c[1]), A[1][k]) for k in range(2)]   # c^t A(t)
    j1r = [frob(x, rho) for x in D['j1']]
    j2r = [frob(x, rho) for x in D['j2']]
    kap = [mul(const(lam), mul(row[0], j1r[i]) + mul(row[1], j2r[i])) for i in range(3)]
    br = D['b'] ** rho
    s_t = mul(const(lam), mul(row[0], const(br[0])) + mul(row[1], const(br[1])))   # s~ = kappa_c . omega^[rho]
    return kap, s_t


class Model:
    def __init__(self, rho, X, e, nu, K):
        Ser.K = K
        self.rho, self.X, self.e, self.nu = rho, X, e, nu
        self.D = setup(rho, X)
        D = self.D
        self.kap, self.s = first_layer(D, rho, nu)
        self.F = mono(e, 1) + mono(e + 1, rnd()) + mono(e + 3, rnd())    # F = t^e * unit
        self.fX = [frob(x, X) for x in D['f']]
        self.fr = [frob(x, rho) for x in D['f']]
        self.uX = [const(x ** X) for x in D['u']]
        self.ur = [const(x ** rho) for x in D['u']]
        self.omX = [frob(x, X) for x in D['om']]
        self.omr = [frob(x, rho) for x in D['om']]
        self.JX = [[frob(D['j1'][i], X), frob(D['j2'][i], X)] for i in range(3)]
        self.Jr = [[frob(D['j1'][i], rho), frob(D['j2'][i], rho)] for i in range(3)]
        b = D['b']
        self.bX = b ** X
        self.br = b ** rho
        self.OmbX = [const(self.bX[1]), const(self.bX[0])]
        self.nU = 9 * K
        self.prepare_fixed()

    def S_of(self, x):
        K = Ser.K
        S = [[Z() for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                S[i][j] = GF(x[(3 * i + j) * K:(3 * i + j + 1) * K])
        return S

    def Pt(self, S):
        return [[mul(self.fX[i], self.kap[j]) + mul(self.F, S[i][j]) for j in range(3)] for i in range(3)]

    def residuals(self, x):
        """alignment S f^[rho] x f^[X] (mod t^K) and FN divided by F in k((t)):
           (sigma/F) f^[X] x u^[X] + (S u^[rho]) x u^[X]  (mod t^K),  sigma = kappa_c . u^[rho].
           If (sigma/F) f^[X] x u^[X] has a pole, FN is unsolvable for regular S (flag self.pole)."""
        S = self.S_of(x)
        al = vcross(mvec(S, self.fr), self.fX)
        Su = vcross(mvec(S, self.ur), self.uX)
        fn = [y_ + z_ for y_, z_ in zip(Su, self.fixed_fn)]
        return al, fn

    def prepare_fixed(self):
        # all inputs are polynomials of degree < K, so zero-padding to precision K+e+4 is exact
        K0 = Ser.K
        Kx = K0 + self.e + 4
        pad = lambda a: np.concatenate([a, GF.Zeros(Kx - len(a))])
        kap = [pad(x) for x in self.kap]
        ur = [pad(x) for x in self.ur]
        fX = [pad(x) for x in self.fX]
        uX = [pad(x) for x in self.uX]
        F = pad(self.F)
        Ser.K = Kx
        sigma = vdot(kap, ur)
        v = [mul(sigma, x_) for x_ in vcross(fX, uX)]
        F1inv = inv_unit(shift(F, -self.e))
        self.pole = False
        out = []
        for comp in v:
            cmp_ = mul(comp, F1inv)
            if ordr(cmp_) < self.e:
                self.pole = True
                out.append(GF.Zeros(K0))
            else:
                out.append(shift(cmp_, -self.e)[:K0])
        Ser.K = K0
        self.fixed_fn = out
        self.ord_sigma = ordr(sigma)
        self.Finv_ext = None

    def linear_system(self):
        K = Ser.K
        zero = GF.Zeros(self.nU)
        al0, fn0 = self.residuals(zero)
        cols = []
        for k in range(self.nU):
            x = GF.Zeros(self.nU); x[k] = 1
            al, fn = self.residuals(x)
            cols.append(np.concatenate([a + a0 for a, a0 in zip(al, al0)] + [f_ + f0 for f_, f0 in zip(fn, fn0)]))
        A = GF(np.stack([np.asarray(c_) for c_ in cols], axis=1))
        rhs = np.concatenate(al0 + fn0)
        return A, GF(np.asarray(rhs))


def solve(A, rhs):
    aug = np.concatenate([A, rhs.reshape(-1, 1)], axis=1)
    R = aug.row_reduce()
    nvar = A.shape[1]
    # consistency: no row [0..0 | nonzero]
    for r in R:
        if np.all(np.asarray(r[:nvar]) == 0) and r[nvar] != 0:
            return None, None
    part = GF.Zeros(nvar)
    piv_cols = []
    for r in R:
        nz = np.nonzero(np.asarray(r[:nvar]))[0]
        if len(nz):
            part[nz[0]] = r[nvar] / r[nz[0]]
            piv_cols.append(nz[0])
    assert np.all(np.asarray(A @ part + rhs) == 0)
    Nsp = A.null_space()
    return part, Nsp


def recover_C(m, S):
    """H=[f^[X]]_x S = J^[X] C J^[rho],t ; C from unit 2x2 minors, then verify full factorisation."""
    H = [[None] * 3 for _ in range(3)]
    for j in range(3):
        col = vcross(m.fX, [S[0][j], S[1][j], S[2][j]])
        for i in range(3):
            H[i][j] = col[i]
    JX, Jr = m.JX, m.Jr

    def minor2(M, r0, r1):
        return mul(M[r0][0], M[r1][1]) + mul(M[r0][1], M[r1][0])
    rows = next((p for p in ((0, 1), (0, 2), (1, 2)) if minor2(JX, *p)[0] != 0))
    colsr = next((p for p in ((0, 1), (0, 2), (1, 2)) if minor2(Jr, *p)[0] != 0))
    d1 = inv_unit(minor2(JX, *rows))
    d2 = inv_unit(minor2(Jr, *colsr))
    a, b_ = rows
    M1inv = [[mul(d1, JX[b_][1]), mul(d1, JX[a][1])], [mul(d1, JX[b_][0]), mul(d1, JX[a][0])]]  # char 2 adjugate
    c0, c1 = colsr
    # J^[rho],t restricted to columns c0,c1 is the 2x2 matrix [[Jr[c0][0], Jr[c1][0]],[Jr[c0][1], Jr[c1][1]]]
    Mt = [[Jr[c0][0], Jr[c1][0]], [Jr[c0][1], Jr[c1][1]]]
    M2inv = [[mul(d2, Mt[1][1]), mul(d2, Mt[0][1])], [mul(d2, Mt[1][0]), mul(d2, Mt[0][0])]]
    Hs = [[H[a][c0], H[a][c1]], [H[b_][c0], H[b_][c1]]]
    T1 = [[sum((mul(M1inv[i][k], Hs[k][j]) for k in range(2)), start=Z()) for j in range(2)] for i in range(2)]
    C = [[sum((mul(T1[i][k], M2inv[k][j]) for k in range(2)), start=Z()) for j in range(2)] for i in range(2)]
    # verify H = J^[X] C J^[rho],t
    ok = True
    for i in range(3):
        for j in range(3):
            val = Z()
            for k in range(2):
                for l in range(2):
                    val = val + mul(mul(JX[i][k], C[k][l]), Jr[j][l])
            ok &= ordr(val + H[i][j]) >= Ser.K
    return C, ok


def analyse(m, x, check_star=True):
    D = m.D
    rho, X, e = m.rho, m.X, m.e
    K = Ser.K
    S = m.S_of(x)
    C, tsy_ok = recover_C(m, S)
    Sf = mvec(S, m.fr)
    k = int(np.nonzero(np.asarray([m.fX[i][0] for i in range(3)]))[0][0])
    ap = mul(Sf[k], inv_unit(m.fX[k]))                                  # a' (S f^[rho] = a' f^[X])
    al_ok = all(ordr(Sf[i] + mul(ap, m.fX[i])) >= K for i in range(3))
    Cb = [mul(C[i][0], const(m.br[0])) + mul(C[i][1], const(m.br[1])) for i in range(2)]
    out = dict(tsy=tsy_ok, align=al_ok)
    Pt = m.Pt(S)
    if check_star:
        g = D['g']
        lhs = [mul(const(g ** (rho + X)), y) for y in vcross(mvec(Pt, m.ur), m.uX)]
        ac = mul(m.F, ap)
        inner = [mul(shift(ac, X), m.OmbX[i]) + mul(shift(m.F, rho), Cb[i]) for i in range(2)]
        t1 = [mul(m.JX[i][0], inner[0]) + mul(m.JX[i][1], inner[1]) for i in range(3)]
        t3 = [shift(y, rho + X) for y in vcross(mvec(Pt, m.omr), m.omX)]
        rhs = [t1[i] + t3[i] for i in range(3)]
        out['star'] = all(ordr(lhs[i] + rhs[i]) >= K for i in range(3))
        # remark after Prop 2.3
        out['dot_uX_rhs_zero'] = ordr(vdot(rhs, m.uX)) >= K
        dom = vdot(rhs, m.omX)
        bCb = mul(const(m.bX[0]), Cb[0]) + mul(const(m.bX[1]), Cb[1])
        out['dot_omX_is_t^rho_F_bCb'] = ordr(dom + shift(mul(m.F, bCb), rho)) >= K
        out['dot_omX_is_t^(rho+X)_F_bCb'] = ordr(dom + shift(mul(m.F, bCb), rho + X)) >= K
        out['bCb_zero(TSYC)'] = ordr(bCb) >= K - rho
    out['ord_Cb'] = min(ordr(Cb[0]), ordr(Cb[1]))
    out['Cb'] = Cb
    out['ap'] = ap
    out['S'] = S
    return out


def run(rho, X, e, nu, K, nsamp=6, label=""):
    m = Model(rho, X, e, nu, K)
    D = m.D
    res = dict(label=label, rho=rho, X=X, e=e, nu=nu, K=K, tsyc=bool(D['tsyc']), lem21=bool(D['lem21']),
               ord_s=ordr(m.s))
    # (2),(3): random S satisfying alignment only
    Aal = []
    zero = GF.Zeros(m.nU)
    al0, _ = m.residuals(zero)
    cols = []
    for kk in range(m.nU):
        xx = GF.Zeros(m.nU); xx[kk] = 1
        al, _ = m.residuals(xx)
        cols.append(np.concatenate([a + a0 for a, a0 in zip(al, al0)]))
    Aal = GF(np.stack([np.asarray(c_) for c_ in cols], axis=1))
    Nal = Aal.null_space()
    star = []
    for _ in range(2):
        coef = GF.Random(Nal.shape[0], seed=int(RNG.integers(1 << 30)))
        x = coef @ Nal
        a_ = analyse(m, x)
        star.append({k_: a_[k_] for k_ in ('tsy', 'align', 'star', 'dot_uX_rhs_zero', 'dot_omX_is_t^rho_F_bCb',
                                            'dot_omX_is_t^(rho+X)_F_bCb')})
    res['random_aligned_S'] = star
    # (4): FN + alignment
    A, rhs = m.linear_system()
    part, Nsp = (None, None) if m.pole else solve(A, rhs)
    res['FN_pole_(trivially_unsolvable)'] = m.pole
    pred_solv = (nu is None) or (ordr(m.s) >= e - X)
    res['FN_solvable'] = part is not None
    res['pred_solvable'] = pred_solv
    if part is None:
        print(res); sys.stdout.flush()
        return res
    lb = X - rho if nu is None else min(X - rho, X + ordr(m.s) - e)
    orders, cong, exact, muap, star_ok = [], True, True, True, True
    g = D['g']
    Finv_e = inv_unit(shift(m.F, -e))
    for it in range(nsamp):
        coef = GF.Random(Nsp.shape[0], seed=int(RNG.integers(1 << 30)))
        x = part + coef @ Nsp
        a_ = analyse(m, x)
        star_ok &= bool(a_['star']) and bool(a_['tsy']) and bool(a_['align'])
        Cb, ap, S = a_['Cb'], a_['ap'], a_['S']
        orders.append(a_['ord_Cb'])
        # t^X s/F  as a series (needs ord s >= e-X)
        sF = shift(mul(m.s, Finv_e), X - e) if m.s.any() else Z()
        pred = [mul(shift(ap, X - rho), m.OmbX[i]) + mul(sF, m.OmbX[i]) for i in range(2)]
        cong &= all(ordr(Cb[i] + pred[i]) >= X for i in range(2))
        # exact form: S u^[rho] = theta omega^[X] + mu u^[X]
        Su = mvec(S, m.ur)
        kk = int(np.nonzero(np.asarray(D['u']))[0][0])
        # solve with two coordinates: Su = theta*omX + mu*uX ; use cross with uX to get theta
        cr = vcross(Su, m.uX)
        crw = vcross(m.omX, m.uX)
        i0 = next(i for i in range(3) if crw[i][0] != 0)
        theta = mul(cr[i0], inv_unit(crw[i0]))
        mu_ = mul(Su[kk] + mul(theta, m.omX[kk]), const(GF(1) / m.uX[kk][0]))
        resid = [Su[i] + mul(theta, m.omX[i]) + mul(mu_, m.uX[i]) for i in range(3)]
        okdec = all(ordr(r) >= K - 2 for r in resid)
        muh = mul(const(g ** rho / g ** X), mu_)
        exact_pred = [mul(shift(muh, X - rho), m.OmbX[i]) + mul(sF, m.OmbX[i]) for i in range(2)]
        exact &= okdec and all(ordr(Cb[i] + exact_pred[i]) >= K - rho - 2 for i in range(2))
        muap &= ordr(muh + ap) >= rho
    res.update(dim_solutions=int(Nsp.shape[0]), sample_ord_Cb=orders, predicted_lower_bound=lb,
               bound_ok=all(o >= lb for o in orders), attained=(min(orders) == lb),
               congruence_mod_tX=cong, exact_form=exact, mu_hat_eq_aprime_mod_t_rho=muap, star_on_FN_solutions=star_ok)
    print(res)
    sys.stdout.flush()
    return res


def main():
    print("referee thm31_toy_indep: GF(2^8), general S, C recovered from H; seed 7")
    print("=== constant first layer (Thm 3.1(iv)) ===")
    for (rho, X, e) in ((1, 4, 6), (2, 4, 6), (2, 8, 11), (4, 8, 11), (4, 16, 19), (8, 16, 19)):
        run(rho, X, e, None, X + rho + 8, label="constant")
    print("=== non-constant first layer A0 + t^nu A1 (Thm 3.1(i)-(iii)) ===")
    for (rho, X, e, nu) in ((1, 4, 6, 1), (1, 4, 6, 2), (1, 4, 6, 3), (2, 4, 7, 1), (2, 4, 7, 3), (2, 8, 11, 2),
                            (2, 8, 11, 3), (2, 8, 11, 5), (4, 8, 13, 4), (4, 8, 13, 5), (4, 8, 13, 7)):
        run(rho, X, e, nu, X + rho + e + 4, label="non-constant")


def run_no_alignment(rho, X, e, nu, K):
    """Control for FIX-4: drop the alignment constraint and impose FN only.  Then FN alone should be
    solvable exactly when ord s >= e-X-rho (the R16.2-level bound), i.e. alignment supplies the extra rho."""
    m = Model(rho, X, e, nu, K)
    zero = GF.Zeros(m.nU)
    _, fn0 = m.residuals(zero)
    cols = []
    for kk in range(m.nU):
        xx = GF.Zeros(m.nU); xx[kk] = 1
        _, fn = m.residuals(xx)
        cols.append(np.concatenate([f_ + f0 for f_, f0 in zip(fn, fn0)]))
    A = GF(np.stack([np.asarray(c_) for c_ in cols], axis=1))
    rhs = GF(np.asarray(np.concatenate(fn0)))
    part, _ = (None, None) if m.pole else solve(A, rhs)
    res = dict(rho=rho, X=X, e=e, nu=nu, ord_s=ordr(m.s), FN_only_solvable=part is not None,
               pred_FN_only=(ordr(m.s) >= e - X - rho), pred_with_alignment=(ordr(m.s) >= e - X))
    print(res)
    sys.stdout.flush()
    return res


def main2():
    print("=== control: FN WITHOUT alignment (gap cases e-X-rho <= ord s < e-X become solvable) ===")
    for (rho, X, e, nu) in ((1, 4, 6, 1), (2, 4, 7, 1), (2, 8, 11, 1), (2, 8, 11, 2), (4, 8, 13, 1), (4, 8, 13, 4),
                            (4, 8, 13, 0)):
        run_no_alignment(rho, X, e, nu, X + rho + e + 4)


if __name__ == '__main__':
    main()
    main2()
