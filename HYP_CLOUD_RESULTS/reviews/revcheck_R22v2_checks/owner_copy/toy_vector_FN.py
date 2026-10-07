# toy_vector_FN.py -- R22 owner (Claude HYP(2)) exact GF(2^8) check of the vector own-line identity
# (Prop. 2.3 = (*)) and of Theorem 3.1 (constant first layer => C_c b^[rho] = O(t^(X-rho)), with the exact
# congruence C_c b^[rho] == t^(X-rho) a'_c Omega b^[X]  mod t^X), on a single own line.
#
# Everything is restricted to the line Y(t)=z+tV, z=e(u). P is built in the most general shape allowed
# by the structural identities used in the note (common image, global alignment, TSY factorisation):
#   P_b^t = f^[X] (x) kappa_b + F * S_b,   S_b = J^[X] C''_b J^[rho],t + f^[X] (x) xi_b ,
# with kappa_b the CONSTANT-TWIST first layer A_b1 j1^[rho] + A_b2 j2^[rho] (lambda=1, kappa_0=1).
# Unknowns: entries of C''_P, C''_R (polys in t of degree <= dC) and xi_P, xi_R (degree <= dX).
# The full own-line condition FN (R16.1): (c1 P^t + c2 R^t) u^[rho] x u^[X] == 0 in k[t] is imposed
# as a linear system; every solution is then tested against Theorem 3.1.
# Controls: (i) the identity (*) for random (non-FN) data, constant or non-constant-slope A;
#           (ii) a first layer that violates the slope equation c^t A c^[Q]=0.
# Run: python3 -I toy_vector_FN.py   (single process, a few seconds)
import os
import sys
import random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gf2k import *  # noqa

random.seed(20261007)


def rmat3():
    while True:
        A = [[rnd() for _ in range(3)] for _ in range(3)]
        # det over char 2
        d = (mul(A[0][0], mul(A[1][1], A[2][2]) ^ mul(A[1][2], A[2][1]))
             ^ mul(A[0][1], mul(A[1][0], A[2][2]) ^ mul(A[1][2], A[2][0]))
             ^ mul(A[0][2], mul(A[1][0], A[2][1]) ^ mul(A[1][1], A[2][0])))
        if d:
            return A


def mv(A, v):
    return [mul(A[i][0], v[0]) ^ mul(A[i][1], v[1]) ^ mul(A[i][2], v[2]) for i in range(3)]


def tr(A):
    return [[A[j][i] for j in range(3)] for i in range(3)]


def cross_c(a, b):
    return [mul(a[1], b[2]) ^ mul(a[2], b[1]), mul(a[2], b[0]) ^ mul(a[0], b[2]), mul(a[0], b[1]) ^ mul(a[1], b[0])]


def proportional(a, b):
    return all(x == 0 for x in cross_c(a, b))


def setup(rho, X):
    Q = 2 * rho
    L, N = rmat3(), rmat3()
    LT, NT = tr(L), tr(N)

    def e(U):
        return cross_c(mv(L, U), mv(N, U))

    def f(Y):
        return cross_c(mv(LT, Y), mv(NT, Y))
    # sanity: e(f(Y)) ~ Y and f(e(U)) ~ U
    for _ in range(5):
        Y = [rnd() for _ in range(3)]
        assert proportional(e(f(Y)), Y)
        assert proportional(f(e(Y)), Y)
    while True:
        u = [rnd() for _ in range(3)]
        z = e(u)
        fz = f(z)
        k = next(i for i in range(3) if u[i])
        g = mul(fz[k], inv(u[k]))
        if g and all(fz[i] == mul(g, u[i]) for i in range(3)):
            break
    V = [rnd() for _ in range(3)]
    Yt = [ptrim([z[i], V[i]]) for i in range(3)]
    j1 = [ptrim([mv(LT, z)[i], mv(LT, V)[i]]) for i in range(3)]
    j2 = [ptrim([mv(NT, z)[i], mv(NT, V)[i]]) for i in range(3)]
    ft = vcross(j1, j2)
    assert all(ptrim(ft[i][:1]) == ptrim([mul(g, u[i])]) for i in range(3))
    om = [ptrim((padd(ft[i], const(mul(g, u[i]))))[1:]) for i in range(3)]  # (f(t)+g u)/t
    b = [vdot(j1, om), vdot(j2, om)]
    assert all(len(x) <= 1 for x in b), "TSYC: b must be constant"
    b = [x[0] if x else 0 for x in b]
    b0 = [vdot([const(x) for x in mv(LT, V)], [const(x) for x in u]), vdot([const(x) for x in mv(NT, V)], [const(x) for x in u])]
    b0 = [x[0] if x else 0 for x in b0]
    assert b == [mul(g, b0[0]), mul(g, b0[1])], "TSYC: b = g J(V)^t u"
    c = [sqrt(b[0]), sqrt(b[1])]
    return dict(Q=Q, L=L, N=N, u=u, z=z, g=g, V=V, j1=j1, j2=j2, ft=ft, om=om, b=b, c=c)


def first_layer(S, rho, slope_ok=True, nu=None, nudeg=2):
    """first-layer matrix A(t)=A0 + t^nu A1 (A1 random polys of degree<=nudeg); A0 solves the slope
    equation c^t A0 c^[Q]=0 (unless slope_ok=False). nu=None: constant A (A1=0)."""
    c = S['c']
    Q = 2 * rho
    cQ = [pw(c[0], Q), pw(c[1], Q)]
    A = [[rnd(), rnd()], [rnd(), 0]]
    s = mul(c[0], mul(A[0][0], cQ[0]) ^ mul(A[0][1], cQ[1])) ^ mul(c[1], mul(A[1][0], cQ[0]))
    coef = mul(c[1], cQ[1])
    A[1][1] = mul(s, inv(coef))
    if not slope_ok:
        A[1][1] ^= 1
    At = [[const(A[i][j]) for j in range(2)] for i in range(2)]
    if nu is not None:
        for i in range(2):
            for j in range(2):
                At[i][j] = padd(At[i][j], [0] * nu + [rnd() for _ in range(nudeg + 1)])
    j1r, j2r = vfrob(S['j1'], rho), vfrob(S['j2'], rho)
    kP = vadd([pmul(At[0][0], x) for x in j1r], [pmul(At[0][1], x) for x in j2r])
    kR = vadd([pmul(At[1][0], x) for x in j1r], [pmul(At[1][1], x) for x in j2r])
    slope = mul(c[0], mul(A[0][0], cQ[0]) ^ mul(A[0][1], cQ[1])) ^ mul(c[1], mul(A[1][0], cQ[0]) ^ mul(A[1][1], cQ[1]))
    return At, kP, kR, slope


def series_inv(p, n):
    """inverse of p (p[0]!=0) modulo t^n"""
    assert p and p[0]
    r = [inv(p[0])]
    for k in range(1, n):
        acc = 0
        for i in range(1, min(k, len(p) - 1) + 1):
            acc ^= mul(p[i], r[k - i])
        r.append(mul(acc, r[0]))
    return r


def build_P(S, rho, X, kP, kR, Ft, CPP, CRR, xiP, xiR):
    """returns P^t, R^t (3x3 matrices of polys) and C_P, C_R (TSY, kappa_0=1), a'_P, a'_R"""
    JX = [[pfrob(S['j1'][i], X), pfrob(S['j2'][i], X)] for i in range(3)]      # 3x2
    Jr = [[pfrob(S['j1'][i], rho), pfrob(S['j2'][i], rho)] for i in range(3)]  # 3x2
    fX = vfrob(S['ft'], X)
    fr = vfrob(S['ft'], rho)
    out = []
    for kap, Cpp, xi in ((kP, CPP, xiP), (kR, CRR, xiR)):
        Sm = madd(mmul(mmul(JX, Cpp), mT(Jr)), outer(fX, xi))
        Pt = madd(outer(fX, kap), mscal(Ft, Sm))
        # TSY C:  [f^[X]]x (F S) = F J^[X] Omega (J^t J)^[X] C'' J^[rho],t  => C = Omega (J^tJ)^[X] C''
        JtJ = mmul(mT(JX), JX)
        Om = [[[], [1]], [[1], []]]
        C = mmul(mmul(Om, JtJ), Cpp)
        ap = vdot(xi, fr)
        out.append((Pt, C, ap))
    return out


def W_of(S, rho, X, Pt_P, Pt_R):
    c = S['c']
    ur = [const(pw(x, rho)) for x in S['u']]
    Pc = madd(mscal(const(c[0]), Pt_P), mscal(const(c[1]), Pt_R))
    return mvec(Pc, ur), Pc


def run_case(rho, X, dC, dX, dF, slope_ok=True, ntests=6, label="", nu=None, eF=3, Fmono=False):
    S = setup(rho, X)
    At, kP, kR, slope = first_layer(S, rho, slope_ok, nu)
    c = S['c']
    kc = vadd([pscal(c[0], x) for x in kP], [pscal(c[1], x) for x in kR])
    ur = [const(pw(x, rho)) for x in S['u']]
    kcu = vdot(kc, ur)
    Ft = ptrim([0] * eF + [rnd(nonzero=True)] + [rnd() for _ in range(dF - eF)])  # F(t)=t^eF*(unit)
    if Fmono:
        Ft = [0] * eF + [1]   # local model: no residual zero of F on the line (S polynomial = S regular)
    uX = [const(pw(x, X)) for x in S['u']]
    # unknown layout
    names = []
    for bb in 'PR':
        for i in range(2):
            for j in range(2):
                for k in range(dC + 1):
                    names.append(('C', bb, i, j, k))
        for i in range(3):
            for k in range(dX + 1):
                names.append(('x', bb, i, k))
    nU = len(names)

    def assemble(xv):
        CPP = [[[], []], [[], []]]
        CRR = [[[], []], [[], []]]
        xiP = [[], [], []]
        xiR = [[], [], []]
        tmpC = {'P': [[[0] * (dC + 1) for _ in range(2)] for _ in range(2)], 'R': [[[0] * (dC + 1) for _ in range(2)] for _ in range(2)]}
        tmpx = {'P': [[0] * (dX + 1) for _ in range(3)], 'R': [[0] * (dX + 1) for _ in range(3)]}
        for val, nm in zip(xv, names):
            if nm[0] == 'C':
                tmpC[nm[1]][nm[2]][nm[3]][nm[4]] = val
            else:
                tmpx[nm[1]][nm[2]][nm[3]] = val
        CPP = [[ptrim(tmpC['P'][i][j]) for j in range(2)] for i in range(2)]
        CRR = [[ptrim(tmpC['R'][i][j]) for j in range(2)] for i in range(2)]
        xiP = [ptrim(tmpx['P'][i]) for i in range(3)]
        xiR = [ptrim(tmpx['R'][i]) for i in range(3)]
        return CPP, CRR, xiP, xiR

    def fn_expr(xv, with_fixed=True):
        CPP, CRR, xiP, xiR = assemble(xv)
        (PtP, CP, aP), (PtR, CR, aR) = build_P(S, rho, X, kP if with_fixed else [[], [], []], kR if with_fixed else [[], [], []], Ft, CPP, CRR, xiP, xiR)
        W, Pc = W_of(S, rho, X, PtP, PtR)
        return vcross(W, uX), (PtP, CP, aP, PtR, CR, aR, W, Pc)

    # ---------- identity (*) check for random data ----------
    g = S['g']
    b = S['b']
    om = S['om']
    JX = [[pfrob(S['j1'][i], X), pfrob(S['j2'][i], X)] for i in range(3)]
    bX = [pw(b[0], X), pw(b[1], X)]
    br = [pw(b[0], rho), pw(b[1], rho)]
    OmbX = [const(bX[1]), const(bX[0])]
    ident_ok = True
    for _ in range(3):
        xv = [rnd() for _ in range(nU)]
        Ex, (PtP, CP, aP, PtR, CR, aR, W, Pc) = fn_expr(xv)
        lhs = [pscal(pw(g, rho + X), comp) for comp in Ex]
        ac = pmul(Ft, padd(pscal(c[0], aP), pscal(c[1], aR)))   # a_c = F a'_c (kappa.f^[rho]=0 identically)
        # check alignment directly: P_c^t f^[rho] = a_c f^[X]
        frv = vfrob(S['ft'], rho)
        fXv = vfrob(S['ft'], X)
        al = mvec(Pc, frv)
        assert all(ptrim(al[i]) == ptrim(pmul(ac, fXv[i])) for i in range(3)), "global alignment"
        Cc = madd(mscal(const(c[0]), CP), mscal(const(c[1]), CR))
        Ccb = mvec(Cc, [const(br[0]), const(br[1])])
        t = lambda k: [0] * k + [1]
        term1 = vscal(pmul(t(X), ac), mvec(JX, OmbX))
        term2 = vscal(pmul(t(rho), Ft), mvec(JX, Ccb))
        omr = vfrob(om, rho)
        omX = vfrob(om, X)
        term3 = vscal(t(rho + X), vcross(mvec(Pc, omr), omX))
        rhs = vadd(vadd(term1, term2), term3)
        ident_ok &= all(ptrim(lhs[i]) == ptrim(rhs[i]) for i in range(3))
    # ---------- impose FN ----------
    E0, _ = fn_expr([0] * nU)              # fixed part (first layer only)
    E0flat = []
    cols = []
    maxdeg = 0
    for k in range(nU):
        xv = [0] * nU
        xv[k] = 1
        Ek, _ = fn_expr(xv)
        Ek = [padd(a, b_) for a, b_ in zip(Ek, E0)]  # linear part
        cols.append(Ek)
        maxdeg = max([maxdeg] + [len(p) for p in Ek])
    maxdeg = max([maxdeg] + [len(p) for p in E0])
    rows = []
    rhsv = []
    for comp in range(3):
        for dgr in range(maxdeg):
            row = [(cols[k][comp][dgr] if dgr < len(cols[k][comp]) else 0) for k in range(nU)]
            rows.append(row)
            rhsv.append(E0[comp][dgr] if dgr < len(E0[comp]) else 0)
    # augmented nullspace: [rows | rhs] (x,1)
    aug = [r + [v] for r, v in zip(rows, rhsv)]
    basis = nullspace(aug, nU + 1)
    hom = [v[:nU] for v in basis if v[nU] == 0]
    part = [v for v in basis if v[nU] != 0]
    sols = []
    if part:
        p0 = part[0]
        s = inv(p0[nU])
        p0 = [mul(s, x) for x in p0[:nU]]
    else:
        p0 = None
    fn_solvable = (p0 is not None) or all(ptrim(x) == [] for x in E0)
    if not fn_solvable:
        hom = []
    # s(t) = c^t A(t) b^[rho] = kappa_c . omega^[rho]
    br_ = [const(pw(S['b'][0], rho)), const(S['b'][1] and pw(S['b'][1], rho))]
    st = padd(pmul(const(c[0]), padd(pmul(At[0][0], br_[0]), pmul(At[0][1], br_[1]))), pmul(const(c[1]), padd(pmul(At[1][0], br_[0]), pmul(At[1][1], br_[1]))))
    res = dict(label=label, rho=rho, X=X, eF=eF, nu=nu, ord_s=pord(st), fn_solvable=fn_solvable, unknowns=nU, equations=len(rows), slope=slope,
               kappa_c_dot_u_rho_zero=(ptrim(kcu) == []), identity_star=ident_ok,
               dim_hom=len(hom), has_particular=(p0 is not None))
    # sample solutions
    orders = []
    congr_ok = True
    nonzero = 0
    for it in range(ntests):
        if not fn_solvable or (p0 is None and not hom):
            break
        xv = list(p0) if p0 is not None else [0] * nU
        for h in hom:
            cf = rnd()
            xv = [a ^ mul(cf, bb) for a, bb in zip(xv, h)]
        Ex, (PtP, CP, aP, PtR, CR, aR, W, Pc) = fn_expr(xv)
        assert all(ptrim(x) == [] for x in Ex), "FN not satisfied by solution"
        Cc = madd(mscal(const(c[0]), CP), mscal(const(c[1]), CR))
        Ccb = mvec(Cc, [const(br[0]), const(br[1])])
        o = min(pord(x) for x in Ccb)
        orders.append(o)
        if o != float('inf'):
            nonzero += 1
        acp = padd(pscal(c[0], aP), pscal(c[1], aR))
        pred = [pmul([0] * (X - rho) + [1], pmul(acp, OmbX[i])) for i in range(2)]
        # + t^X s/F Omega b^[X]  (Laurent; F=t^eF F1)
        F1 = Ft[eF:]
        sF = pmul(st, series_inv(F1, X + 4))[: X + 4]
        if st:
            sh = X - eF
            if sh >= 0:
                sF = [0] * sh + sF
            else:
                assert all(v == 0 for v in sF[:-sh]), 'regularity of t^X s/F violated'
                sF = sF[-sh:]
            pred = [padd(pred[i], pmul(sF, OmbX[i])) for i in range(2)]
        for i in range(2):
            dlt = padd(Ccb[i], pred[i])
            if pord(dlt) < X:
                congr_ok = False
    res.update(sample_orders_of_Cc_b_rho=orders, nonzero_samples=nonzero, congruence_mod_tX=congr_ok)
    return res


if __name__ == '__main__':
    print("R22 toy_vector_FN: GF(2^8), seed 20261007")
    print("=== (A) constant first layer satisfying the slope equation (hypotheses of Thm 3.1) ===")
    cases = [(1, 4, 16, 16, 8), (2, 4, 12, 12, 8), (1, 8, 26, 26, 8), (2, 8, 26, 26, 8), (4, 8, 26, 26, 8)]
    allok = True
    for (rho, X, dC, dX, dF) in cases:
        r = run_case(rho, X, dC, dX, dF, slope_ok=True, label="A: constant layer", ntests=8)
        print(r)
        ok = r['identity_star'] and r['kappa_c_dot_u_rho_zero'] and r['congruence_mod_tX'] and \
            all(o >= X - rho for o in r['sample_orders_of_Cc_b_rho'])
        print("  Thm 3.1 (order >= X-rho and exact congruence mod t^X):", ok, "| X-rho =", X - rho,
              "| min observed order =", min(r['sample_orders_of_Cc_b_rho']) if r['sample_orders_of_Cc_b_rho'] else None,
              "| nonzero C_c b^[rho] samples:", r['nonzero_samples'])
        allok &= ok
    print("ALL (A) cases OK:", allok)
    print("=== (B) control: constant layer violating the slope equation (expect FN unsolvable) ===")
    for (rho, X, dC, dX, dF) in cases[:2]:
        r = run_case(rho, X, dC, dX, dF, slope_ok=False, label="B: slope eq. fails")
        print(r)
        print("  identity (*) holds:", r['identity_star'], "| FN solvable:", r['fn_solvable'])
    print("=== (C) control: NON-constant layer A(t)=A0+t^nu A1 (Thm 3.1 general form) ===")
    print("    F(t)=t^eF (local model, so that a polynomial S is the local S of the note)")
    print("    predicted: solvable only if ord s >= eF-X; then ord C_c b^[rho] >= min(X-rho, X+ord s-eF)")
    for (rho, X, dC, dX, dF, nu, eF) in [(1, 4, 16, 16, 10, 1, 5), (1, 4, 16, 16, 10, 2, 5), (1, 4, 16, 16, 10, 1, 7), (2, 8, 26, 26, 12, 2, 9)]:
        r = run_case(rho, X, dC, dX, dF, slope_ok=True, label="C: non-constant layer", nu=nu, eF=eF, ntests=8, Fmono=True)
        print(r)
        pred = min(X - rho, X + r['ord_s'] - eF)
        obs = min(r['sample_orders_of_Cc_b_rho']) if r['sample_orders_of_Cc_b_rho'] else None
        print("  predicted solvable:", r['ord_s'] >= eF - X, "| solvable:", r['fn_solvable'],
              "| predicted lower bound:", pred, "| min observed:", obs,
              "| general congruence mod t^X:", r['congruence_mod_tX'])
