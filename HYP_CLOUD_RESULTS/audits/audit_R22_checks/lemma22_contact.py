# lemma22_contact.py -- referee R22: independent test of Lemma 2.2 (own-line contact e_u in {E,E+1} at good
# points, and e_u=E+1 iff y_1^[E].e(u)=0), on RANDOM paired centres e(U)=LU x NU (the R16 model), not only on
# the Fermat sigma1 model used by the owner.  Uses the `galois` package (not the owner's gf2k helper).
#
# For each centre and E, every affine point u=(1,x,y) of C_orig(U)=U^[E].e(U) over GF(2^m) is found by full
# enumeration.  Keep points that are smooth on C_orig, with e(u)!=0 and g(u)!=0 (f(e(u))=g u).  For each kept point:
#   (A) branch method (Hensel): ord_s u^[E].e(v(s)) along the branch v(s) of C_orig at u;
#   (B) line method: ord_t C_f(z+tV), C_f(Y)=Y.f(Y)^[E], z=e(u), V=u^[E] x c0 (c0 random, V not radial);
#       at such z, C_f is smooth (grad = f(z)^[E] = g^E u^[E] != 0), so this equals I_z(l_u, Gamma');
#   (C) owner's criterion y_1^[E].e(u)=0, with y_1=(0,C_2,C_1) the affine tangent;
#   (D) referee's closed form: z.w^[E]=0 with w=df_z(V)  (C_f(z+tV)=t^E z.w^[E]+t^(E+1) V.w^[E]+O(t^(2E))).
# The full per-point computations (A),(B) are run on ALL points with predicted E+1 and on a sample of the others;
# the criteria (C),(D) are evaluated on all kept points.
# Run: python3 -I lemma22_contact.py
import sys
import numpy as np
import galois

RNG = np.random.default_rng(20261007)


def setup_field(m):
    return galois.GF(2 ** m)


def rand_inv3(GF):
    while True:
        A = GF.Random((3, 3), seed=int(RNG.integers(1 << 30)))
        if np.linalg.det(A) != 0:
            return A


def cross(a, b):
    return [a[1] * b[2] + a[2] * b[1], a[2] * b[0] + a[0] * b[2], a[0] * b[1] + a[1] * b[0]]


def matvec(A, U):  # A: 3x3 GF array, U: list of 3 arrays/scalars (broadcast)
    return [A[i, 0] * U[0] + A[i, 1] * U[1] + A[i, 2] * U[2] for i in range(3)]


# ---------------- truncated power series (lists of GF scalars as GF arrays) ----------------
def smul(a, b, n):
    c = np.convolve(a, b)
    if len(c) < n:
        c = np.concatenate([c, type(c).Zeros(n - len(c))])
    return c[:n]


def sfrob(a, E, n):
    GF = type(a)
    out = GF.Zeros(n)
    for i in range(len(a)):
        if i * E < n:
            out[i * E] = a[i] ** E
    return out


def sord(a):
    nz = np.nonzero(np.asarray(a))[0]
    return int(nz[0]) if len(nz) else None


def series_e(L, N, v, n):
    v = [x[:n] for x in v]
    Lv = [sum((L[i, j] * v[j] for j in range(3)), start=type(v[0]).Zeros(n)) for i in range(3)]
    Nv = [sum((N[i, j] * v[j] for j in range(3)), start=type(v[0]).Zeros(n)) for i in range(3)]
    return [smul(Lv[1], Nv[2], n) + smul(Lv[2], Nv[1], n),
            smul(Lv[2], Nv[0], n) + smul(Lv[0], Nv[2], n),
            smul(Lv[0], Nv[1], n) + smul(Lv[1], Nv[0], n)]


def C_series(L, N, E, v, n):
    v = [x[:n] for x in v]
    ev = series_e(L, N, v, n)
    vE = [sfrob(x, E, n) for x in v]
    return smul(vE[0], ev[0], n) + smul(vE[1], ev[1], n) + smul(vE[2], ev[2], n)


def branch_order(GF, L, N, E, u, C1, C2):
    """Hensel branch of C_orig at smooth affine u=(1,x0,y0); returns ord_s u^[E].e(v(s))."""
    n = 2 * E + 6
    one = GF.Zeros(n); one[0] = 1
    if C2 != 0:   # x = x0 + s free, solve y(s)
        xs = GF.Zeros(n); xs[0] = u[1]; xs[1] = 1
        ys = GF.Zeros(n); ys[0] = u[2]
        piv, free_is_x = C2, True
    else:
        ys = GF.Zeros(n); ys[0] = u[2]; ys[1] = 1
        xs = GF.Zeros(n); xs[0] = u[1]
        piv, free_is_x = C1, False
    for k in range(1, n):
        if (free_is_x and k == 1) or True:
            v = [one, xs, ys]
            c = C_series(L, N, E, v, k + 1)
            ck = c[k]
            if ck != 0:
                if free_is_x:
                    ys[k] = ys[k] + ck / piv
                else:
                    xs[k] = xs[k] + ck / piv
    v = [one, xs, ys]
    assert sord(C_series(L, N, E, v, n)) is None, "Hensel failed"
    ev = series_e(L, N, v, n)
    uE = [u[i] ** E for i in range(3)]
    h = uE[0] * ev[0] + uE[1] * ev[1] + uE[2] * ev[2]
    return sord(h)


def line_order(GF, Lt, Nt, E, z, V, cap):
    """ord_t C_f(z+tV), C_f(Y)=Y.f(Y)^[E], f(Y)=L^tY x N^tY; computed as an exact polynomial in t."""
    n = cap
    Y = []
    for i in range(3):
        s = GF.Zeros(n); s[0] = z[i]; s[1] = V[i]; Y.append(s)
    jY = [sum((Lt[i, j] * Y[j] for j in range(3)), start=GF.Zeros(n)) for i in range(3)]
    kY = [sum((Nt[i, j] * Y[j] for j in range(3)), start=GF.Zeros(n)) for i in range(3)]
    fY = [smul(jY[1], kY[2], n) + smul(jY[2], kY[1], n),
          smul(jY[2], kY[0], n) + smul(jY[0], kY[2], n),
          smul(jY[0], kY[1], n) + smul(jY[1], kY[0], n)]
    fE = [sfrob(x, E, n) for x in fY]
    Cf = smul(Y[0], fE[0], n) + smul(Y[1], fE[1], n) + smul(Y[2], fE[2], n)
    return sord(Cf)


def run_centre(GF, L, N, E, label, full_sample=40):
    Lt, Nt = L.T, N.T
    q = GF.order
    elems = GF.elements
    xs_l, ys_l = [], []
    for x0 in elems:   # enumerate affine points (1,x,y), vectorised in y
        X = GF.Ones(q) * x0
        U = [GF.Ones(q), X, elems]
        e = cross(matvec(L, U), matvec(N, U))
        C = U[0] ** E * e[0] + U[1] ** E * e[1] + U[2] ** E * e[2]
        idx = np.nonzero(np.asarray(C) == 0)[0]
        xs_l.extend(int(x0) for _ in idx)
        ys_l.extend(int(elems[i]) for i in idx)
    P = len(xs_l)
    U = [GF.Ones(P), GF(xs_l), GF(ys_l)]
    LU, NU = matvec(L, U), matvec(N, U)
    e = cross(LU, NU)
    uE = [x ** E for x in U]
    part = []
    for j in range(3):
        Lej = [GF.Ones(P) * L[i, j] for i in range(3)]
        Nej = [GF.Ones(P) * N[i, j] for i in range(3)]
        dj = [a + b for a, b in zip(cross(Lej, NU), cross(LU, Nej))]
        part.append(uE[0] * dj[0] + uE[1] * dj[1] + uE[2] * dj[2])
    C1, C2 = part[1], part[2]
    smooth = (np.asarray(C1) != 0) | (np.asarray(C2) != 0)
    enz = (np.asarray(e[0]) != 0) | (np.asarray(e[1]) != 0) | (np.asarray(e[2]) != 0)
    fz = cross(matvec(Lt, e), matvec(Nt, e))
    g = fz[0]
    prop = (np.asarray(fz[1] + g * U[1]) == 0) & (np.asarray(fz[2] + g * U[2]) == 0)
    gnz = (np.asarray(g) != 0) & prop
    c0 = GF.Random(3, seed=int(RNG.integers(1 << 30)))
    V = cross(uE, [GF.Ones(P) * c0[i] for i in range(3)])
    VxE = cross(V, e)
    nonrad = (np.asarray(VxE[0]) != 0) | (np.asarray(VxE[1]) != 0) | (np.asarray(VxE[2]) != 0)
    w = [a + b for a, b in zip(cross(matvec(Lt, V), matvec(Nt, e)), cross(matvec(Lt, e), matvec(Nt, V)))]
    wxu = cross(w, U)
    wrad = (np.asarray(wxu[0]) == 0) & (np.asarray(wxu[1]) == 0) & (np.asarray(wxu[2]) == 0)
    y1 = [GF.Zeros(P), C2, C1]
    critC = (y1[0] ** E) * e[0] + (y1[1] ** E) * e[1] + (y1[2] ** E) * e[2]
    critD = (w[0] ** E) * e[0] + (w[1] ** E) * e[1] + (w[2] ** E) * e[2]
    keep = smooth & enz & gnz & nonrad
    pC = (np.asarray(critC) == 0) & keep
    pD = (np.asarray(critD) == 0) & keep
    stats = dict(points=P, singular=int((~smooth).sum()), g_zero_or_e_zero=int((smooth & ~(enz & gnz)).sum()),
                 kept=int(keep.sum()), w_radial_among_kept=int((wrad & keep).sum()),
                 pred_E1_ownercrit=int(pC.sum()), pred_E1_closedform=int(pD.sum()),
                 crit_agree=int(((pC == pD) & keep).sum()), full_checked=0, full_ok=0, orders={}, bad=[])
    kidx = np.nonzero(keep)[0]
    pidx = [i for i in kidx if pC[i]]
    oidx = [i for i in kidx if not pC[i]]
    step = max(1, len(oidx) // full_sample)
    for i in pidx + oidx[::step]:
        u = GF([1, xs_l[i], ys_l[i]])
        z = GF([int(e[0][i]), int(e[1][i]), int(e[2][i])])
        Vi = GF([int(V[0][i]), int(V[1][i]), int(V[2][i])])
        oA = branch_order(GF, L, N, E, u, C1[i], C2[i])
        oB = line_order(GF, Lt, Nt, E, z, Vi, 2 * E + 4)
        stats['full_checked'] += 1
        stats['orders'][(oA, oB)] = stats['orders'].get((oA, oB), 0) + 1
        ok = (oA == oB) and oA in (E, E + 1) and ((oA == E + 1) == bool(pC[i]))
        stats['full_ok'] += int(ok)
        if not ok:
            stats['bad'].append((xs_l[i], ys_l[i], oA, oB, bool(pC[i])))
    print(f"  {label} E={E}: {stats}")
    sys.stdout.flush()
    return stats


def fermat_centre(GF):
    # sigma1(U)=(U1U2,U0U2,U0U1) = LU x NU with L=diag(1,1,0)?  Use L=[[0,0,0],[0,1,0],[0,0,1]]... find directly:
    # (LU x NU) with L=diag(1,1,0), N=diag(1,0,1): LU=(U0,U1,0), NU=(U0,0,U2) -> cross=(U1U2, U0U2, U0U1). (char 2)
    L = GF([[1, 0, 0], [0, 1, 0], [0, 0, 0]])
    N = GF([[1, 0, 0], [0, 0, 0], [0, 0, 1]])
    return L, N


def main():
    print("referee lemma22_contact: random paired centres e(U)=LU x NU (R16 model) + sigma1 control")
    for m, Es, ncentres in ((8, (8, 16, 32), 3), (10, (8, 16), 2), (12, (8, 16), 2)):
        GF = setup_field(m)
        print(f"GF(2^{m}):")
        L, N = fermat_centre(GF)
        if m == 12:
            run_centre(GF, L, N, 16, "sigma1 (control; owner reports 450 E+1 points)")
        for ci in range(ncentres):
            L, N = rand_inv3(GF), rand_inv3(GF)
            for E in Es:
                run_centre(GF, L, N, E, f"random centre #{ci}")


if __name__ == '__main__':
    main()
