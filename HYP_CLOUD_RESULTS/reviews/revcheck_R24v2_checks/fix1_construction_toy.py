# Exact check of R24 v2 Lemma 2.1 step (o) [FIX-1] and of (i)-(iii) built on it,
# as polynomial identities over GF(2)[y0,y1,y2] (char 2), on a toy with
#   f = standard Cremona (y1y2, y0y2, y0y1), J = [(y0,y1,0),(y0,0,y2)], kappa_0 = 1,
#   F = an absolutely irreducible NODAL cubic through Bs(f) (node at (1:1:1), f(node) != 0),
#   rho = 2, X = 4, P^t = f^[X] (x) k0' + F (B J^[rho],t + f^[X] (x) s0)  (common image, global alignment, F|a).
# Rational vectors are (numerator, denominator) with denominators powers of f_i, which are
# coprime to the prime F; so "divisible by F as a polynomial" <=> "in F*O_z for every z in Gamma'
# with f_i(z)!=0", i.e. each check is uniform over the whole open set {f_i != 0} of Gamma',
# singular points included.
import itertools, random, sys
from sympy import symbols, Poly, GF
y0, y1, y2 = Y = symbols('y0 y1 y2')
def P_(e): return Poly(e, *Y, modulus=2)
ZERO = P_(0); ONE = P_(1)
random.seed(20261011)
rho, X = 2, 4
f = [P_(y1*y2), P_(y0*y2), P_(y0*y1)]
J = [[P_(y0), P_(y0)], [P_(y1), P_(0)], [P_(0), P_(y2)]]   # 3x2, columns j1, j2
def frob(p, k): return p**k                                  # char 2, k power of 2: Frobenius twist on coefficients is trivial over GF(2)
fX = [frob(c, X) for c in f]; fr = [frob(c, rho) for c in f]
JX = [[frob(J[i][j], X) for j in range(2)] for i in range(3)]
Jr = [[frob(J[i][j], rho) for j in range(2)] for i in range(3)]
def dot(u, v): 
    s = ZERO
    for a, b in zip(u, v): s = s + a*b
    return s
def iszero(p): return p.is_zero or p.as_expr() == 0
def divisible(p, F):
    q, r = p.div(F); return iszero(r)
out = []
def rep(s): out.append(s); print(s); sys.stdout.flush()
# sanity: J^t f = 0, j1 x j2 = f
assert all(iszero(dot([J[i][j] for i in range(3)], f)) for j in range(2))
# --- choose F: cubic in the ideal of Bs(f), singular at (1,1,1), irreducible over GF(2), multiplicity 2 there
mons = [y0**2*y1, y0**2*y2, y1**2*y0, y1**2*y2, y2**2*y0, y2**2*y1, y0*y1*y2]
from sympy import diff, expand
cands = []
for bits in itertools.product([0,1], repeat=7):
    if not any(bits): continue
    Fe = sum(b*m for b, m in zip(bits, mons))
    Fp = P_(Fe)
    pt = {y0:1, y1:1, y2:1}
    if Fp.eval(pt) % 2: continue
    if any(P_(diff(Fe, v)).eval(pt) % 2 for v in Y): continue
    # irreducible over GF(2) <=> no GF(2)-rational linear factor (a cubic)
    lins = [P_(a*y0+b*y1+c*y2) for a, b, c in itertools.product([0,1], repeat=3) if (a, b, c) != (0, 0, 0)]
    if any(divisible(Fp, L) for L in lins): continue
    # multiplicity at (1,1,1): quadratic part of F(1+v) nonzero
    a, b, c = symbols('a b c')
    sh = Poly(expand(Fe.subs({y0:1+a, y1:1+b, y2:1+c}, simultaneous=True)), a, b, c, modulus=2)
    quad = [m for m, co in sh.terms() if sum(m) == 2 and co % 2]
    if not quad: continue
    cands.append(Fe)
rep("cubics through Bs(f), irreducible over GF(2), node (mult 2) at (1:1:1): %d" % len(cands))
Fe = cands[0]; F = P_(Fe)
rep("F = %s  (GF(2)-irreducible + GF(2)-rational double point => absolutely irreducible)" % Fe)
# kappa_0 vector with k0 . f = F
k0 = [ZERO, ZERO, ZERO]
for m, co in P_(Fe).terms():
    e = dict(zip(range(3), m))
    for i, (a_, b_) in enumerate([(1,2),(0,2),(0,1)]):
        if e[a_] >= 1 and e[b_] >= 1:
            ee = list(m); ee[a_] -= 1; ee[b_] -= 1
            k0[i] = k0[i] + P_(y0**ee[0]*y1**ee[1]*y2**ee[2]); break
assert iszero(dot(k0, f) - F)
def rpoly(deg):
    s = ZERO
    for m in itertools.product(range(deg+1), repeat=3):
        if sum(m) == deg and random.random() < 0.5:
            s = s + P_(y0**m[0]*y1**m[1]*y2**m[2])
    return s
def build(mode):
    h = rpoly(4); w = [rpoly(4), rpoly(4)]
    k0p = [h*frob(k0[i], rho) + Jr[i][0]*w[0] + Jr[i][1]*w[1] for i in range(3)]
    B = [[rpoly(9) for _ in range(2)] for _ in range(3)]
    if mode == 'F2|a':   # s0 = syzygy + F*(something): then F | s0.f^[rho]
        c = [rpoly(1), rpoly(1)]
        s0 = [Jr[i][0]*c[0] + Jr[i][1]*c[1] + F*rpoly(0) for i in range(3)]
    else:
        s0 = [rpoly(3) for _ in range(3)]
    if mode == 'ctrl-no-zero-top':      # first layer with k0'.f^rho not divisible by F
        k0p[0] = k0p[0] + rpoly(6)
    # P^t[i][j]
    Pt = [[fX[i]*k0p[j] + F*(B[i][0]*Jr[j][0] + B[i][1]*Jr[j][1] + fX[i]*s0[j]) for j in range(3)] for i in range(3)]
    if mode == 'ctrl-no-common-image':  # add B' J^{rho,t} WITHOUT the factor F: alignment kept, common image broken
        Bp = [[rpoly(12) for _ in range(2)] for _ in range(3)]
        Pt = [[Pt[i][j] + Bp[i][0]*Jr[j][0] + Bp[i][1]*Jr[j][1] for j in range(3)] for i in range(3)]
    # C_P := Omega J^{[X],t} B  (kappa_0=1), so J^{[X],t} P^t = F Omega C_P J^{[rho],t}
    JtB = [[sum((JX[k][a]*B[k][b] for k in range(3)), ZERO) for b in range(2)] for a in range(2)]
    CP = [JtB[1], JtB[0]]
    return Pt, CP
def check(mode):
    Pt, CP = build(mode)
    ok = {}
    # global hypotheses
    cross = []
    for j in range(3):
        col = [Pt[i][j] for i in range(3)]
        cross += [fX[1]*col[2]-fX[2]*col[1], fX[2]*col[0]-fX[0]*col[2], fX[0]*col[1]-fX[1]*col[0]]
    ok['common image ([f^X]x P^t = 0 mod F)'] = all(divisible(c, F) for c in cross)
    Ptf = [dot(Pt[i], fr) for i in range(3)]
    i0 = 0
    aP_num = Ptf[i0]; aP, r = aP_num.div(fX[i0]); assert iszero(r)
    ok['global alignment (P^t f^rho = a f^X)'] = all(iszero(Ptf[i] - aP*fX[i]) for i in range(3))
    ok['zero top: F | a_P'] = divisible(aP, F)
    if mode.startswith('ctrl'):
        if mode == 'ctrl-no-common-image':
            # layer identity no longer of the stated form; C_P stays as built; skip (i)-(iii), test (o) only
            pass
    F2a = divisible(aP, F*F)
    JXtPt = [[sum((JX[k][a]*Pt[k][j] for k in range(3)), ZERO) for j in range(3)] for a in range(2)]
    OmCJ = [[F*(CP[1-a][0]*Jr[j][0] + CP[1-a][1]*Jr[j][1]) for j in range(3)] for a in range(2)]
    ok['R18-T 2.1(ii) layer identity'] = all(iszero(JXtPt[a][j] - OmCJ[a][j]) for a in range(2) for j in range(3))
    kt = {}
    for i in range(3):   # step (o) on the chart {f_i != 0}, e' = e_i / f_i^rho
        D = fX[i]*fr[i]
        kappa_num = [Pt[i][j]*fr[i] for j in range(3)]           # kappa = row_i/f_i^X, put over D
        kf = dot([Pt[i][j] for j in range(3)], fr)                # (row_i . f^rho), kappa.f^rho = kf/f_i^X
        ok['(o) chart %d: kappa.f^rho in F O' % i] = divisible(kf, F)
        N = [kappa_num[j] - (kf if j == i else ZERO) for j in range(3)]   # kappa~ = N/D
        ok['(o) chart %d: kappa~.f^rho = 0 exactly' % i] = iszero(dot(N, fr))
        ok['(o) chart %d: D P^t - f^X (x) N in F M_3' % i] = all(divisible(D*Pt[a][b] - fX[a]*N[b], F) for a in range(3) for b in range(3))
        kt[i] = (N, D)
        # (i): S = (P^t - f^X(x)kappa~)/F over D; Gtilde via the minor not involving row i: J^{[X],t} rows (k,l) with minor = f_i^X
        S = [[(D*Pt[a][b] - fX[a]*N[b]).div(F)[0] for b in range(3)] for a in range(3)]   # S_true = S/D
        JXtS = [[sum((JX[k][a]*S[k][b] for k in range(3)), ZERO) for b in range(3)] for a in range(2)]
        ok['(i) chart %d: J^{X,t} S = Omega C_P J^{rho,t}' % i] = all(iszero(JXtS[a][b] - D*OmCJ[a][b].div(F)[0]) for a in range(2) for b in range(3))
        # right inverse G (3x2) of J^{[X],t} supported on rows {k,l} = complement of i ; det = f_i^X (char 2)
        k_, l_ = [t for t in range(3) if t != i]
        Mx = [[JX[k_][0], JX[l_][0]], [JX[k_][1], JX[l_][1]]]   # J^{X,t} restricted to columns k_,l_
        det = Mx[0][0]*Mx[1][1] - Mx[0][1]*Mx[1][0]
        assert iszero(det - fX[i])
        adj = [[Mx[1][1], Mx[0][1]], [Mx[1][0], Mx[0][0]]]       # inverse = adj/det in char 2
        G = [[ZERO, ZERO] for _ in range(3)]; G[k_] = adj[0]; G[l_] = adj[1]   # G_true = G/f_i^X
        ok['(i) chart %d: J^{X,t} G = f_i^X I' % i] = all(iszero(sum((JX[k][a]*G[k][b] for k in range(3)), ZERO) - (fX[i] if a == b else ZERO)) for a in range(2) for b in range(2))
        # T := S_true - G_true Omega C_P J^{rho,t}  ; common denominator D*f_i^X
        GO = [[sum((G[a][c]*OmCJ[c][b].div(F)[0] for c in range(2)), ZERO) for b in range(3)] for a in range(3)]
        T = [[S[a][b]*fX[i] - GO[a][b]*D for b in range(3)] for a in range(3)]   # T_true = T/(D f_i^X)
        sig = [T[i][b] for b in range(3)]                                           # sigma_true = sig/(D f_i^{2X})
        ok['(i) chart %d: T = f^X (x) sigma (kernel = O f^X)' % i] = all(iszero(T[a][b]*fX[i] - fX[a]*sig[b]) for a in range(3) for b in range(3))
        den = D*fX[i]*fX[i]
        ok['(i) chart %d: a_P = F sigma.f^rho' % i] = iszero(aP*den - F*dot(sig, fr))
        sf = dot(sig, fr)
        ok['(iii) chart %d: [F^2|a_P] <=> [sigma.f^rho in F O]' % i] = (divisible(sf, F) == F2a)
        if F2a:
            # second-order lift: eta = sigma - (sigma.f^rho) e'  (syzygy); kappa^ = kappa~ + F eta
            # sigma.f^rho = sf/den ; e' = e_i/f_i^rho  ; eta = (sig*f_i^rho - sf e_i)/(den f_i^rho)
            DD = den*fr[i]
            eta = [sig[b]*fr[i] - (sf if b == i else ZERO) for b in range(3)]
            ok['(iii) chart %d: eta syzygy' % i] = iszero(dot(eta, fr))
            # kappa^ = N/D + F*eta/DD ; check P^t - f^X(x)kappa^ - F*G~Omega C J^{rho,t} = 0 mod F^2  (over DD*f_i^X)
            L = DD*fX[i]
            res_ok = True
            for a in range(3):
                for b in range(3):
                    num = Pt[a][b]*L - fX[a]*(N[b]*(L.div(D)[0]) + F*eta[b]*fX[i]) - F*(GO[a][b]*(L.div(fX[i])[0]))
                    if not divisible(num, F*F): res_ok = False
            ok['(iii) chart %d: second-order lift P^t = f^X(x)kappa^ + F G~OmegaC_PJ^rho,t mod F^2' % i] = res_ok
    # gauge (ii): lifts from different charts differ by F*eta with eta a syzygy
    for i, j in [(0,1),(0,2),(1,2)]:
        Ni, Di = kt[i]; Nj, Dj = kt[j]
        diffs = [Ni[b]*Dj - Nj[b]*Di for b in range(3)]
        dv = all(divisible(d_, F) for d_ in diffs)
        q = [d_.div(F)[0] for d_ in diffs]
        ok['(ii) charts %d,%d: kappa~_i - kappa~_j = F eta, eta syzygy' % (i, j)] = dv and iszero(dot(q, fr))
    return ok, F2a
for mode in ['F2|a', 'generic', 'ctrl-no-zero-top', 'ctrl-no-common-image']:
    for trial in range(2 if not mode.startswith('ctrl') else 1):
        ok, F2a = check(mode)
        bad = [k for k, v in ok.items() if not v]
        rep("mode=%-7s trial=%d  F^2|a_P=%s  checks=%d  exact failing set=%s" % (mode, trial, F2a, len(ok), bad))
# point evaluation at the node and at a point of Gamma' with some f_j = 0
node = {y0:1, y1:1, y2:1}
rep("F(node)=%d, grad F(node)=0 checked in selection; f(node)=%s (nonzero)" % (F.eval(node) % 2, [int(c.eval(node)) % 2 for c in f]))
pts = [p for p in itertools.product([0,1], repeat=3) if any(p) and F.eval(dict(zip(Y, p))) % 2 == 0]
rep("GF(2)-points of Gamma': %s ; with f(z)!=0: %s" % (pts, [p for p in pts if any(c.eval(dict(zip(Y, p))) % 2 for c in f)]))
