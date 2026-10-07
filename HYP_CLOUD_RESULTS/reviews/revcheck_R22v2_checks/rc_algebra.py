# rc_algebra.py -- revision check of the v2 algebra on one own line, exact over GF(2^8) (galois), polynomials in t.
# Independent of the owner's gf2k helper. Random data: j1=L Y, j2=N Y, Y(t)=z+tV, f=k0 j1 x j2, gu=f(z),
# omega=(f(z)+f(Y(t)))/t.  Checks:
#  L21i   J^t u = (t/g) b, b constant = g J(V)^t u               (Lemma 2.1(i), TSYC on a line)
#  L21ii  f x v = k0 J Omega J^t v for random v; f x omega = k0 J Omega b
#  CROSS  [f^[X]]_x M = k0^X J^[X] Omega J^[X],t M  (random M)  => J^[X],t(P^t)/F = k0^-X Omega C J^[rho],t
#  FIX1   u-component of (gamma) is automatic: for random y with J-part w:=J^[X],t y and C b^[rho]:=k0^X Omega w,
#         t^(rho+X) u^[X].(omega^[X] x y) == u^[X].J^[X] m,  m = k0^X t^X a' Omega b^[X] + t^rho C b^[rho]  (random a')
#         and kernel of b^t Omega is span(b) (b^t Omega b = 0, b != 0)
#  FIX3   with W = s f^[X] + F y (random s, F, y; C b^[rho] := k0^X Omega J^[X],t y):
#         RHS(*) . u^[X] == 0 and RHS(*) . omega^[X] == t^rho F b^[X],t C b^[rho]  (not t^(rho+X) ...)
#  FIX2   P^t -> P^t + F f^[X] (x) xi : alignment coefficient shifts by F (xi . f^[rho]); [f^[X]]_x-image unchanged;
#         y_u shifts by f^[X](xi . omega^[rho])
import random
import galois
GF = galois.GF(2**8)
random.seed(20261007)
def rnd(): return GF(random.randrange(256))
def rndnz():
    while True:
        x = rnd()
        if x != 0: return x
P = galois.Poly
def poly(c): return P(list(reversed(c)), field=GF) if isinstance(c, list) else P([c], field=GF)
ZERO = P([0], field=GF); ONE = P([1], field=GF); tt = P([1, 0], field=GF)
def rpoly(deg): return P([rnd() for _ in range(deg + 1)], field=GF)
def cross(a, b): return [a[1]*b[2] + a[2]*b[1], a[2]*b[0] + a[0]*b[2], a[0]*b[1] + a[1]*b[0]]
def dot(a, b):
    s = ZERO
    for x, y in zip(a, b): s = s + x*y
    return s
def frob(v, k): return [x**k for x in v]          # coordinatewise k-th power (k a power of 2)
def matvec(M, v): return [dot(row, v) for row in M]
def lin(Mat, vec): return [sum((Mat[i][j]*vec[j] for j in range(3)), ZERO) for i in range(3)]
results = []
def chk(name, ok):
    results.append((name, bool(ok)))
for trial in range(12):
    rho, X = random.choice([(1, 4), (2, 4), (2, 8), (4, 8), (4, 16)])
    k0 = poly(rndnz()); g = poly(rndnz())
    Lm = [[poly(rnd()) for _ in range(3)] for _ in range(3)]
    Nm = [[poly(rnd()) for _ in range(3)] for _ in range(3)]
    z = [poly(rnd()) for _ in range(3)]; V = [poly(rnd()) for _ in range(3)]
    Y = [z[i] + tt*V[i] for i in range(3)]
    j1 = lin(Lm, Y); j2 = lin(Nm, Y)
    f = [k0*x for x in cross(j1, j2)]
    fz = [poly(x.coeffs[-1]) if x.degree >= 0 else ZERO for x in f]   # f at t=0
    fz = [P([x(GF(0))], field=GF) for x in f]
    if all(x == ZERO for x in fz): continue
    ginv = poly(GF(1) / g.coeffs[0])
    u = [ginv*x for x in fz]
    om = [(fz[i] + f[i]) // tt for i in range(3)]
    chk("omega exact division", all(((fz[i] + f[i]) % tt) == ZERO for i in range(3)))
    J = [[j1[i], j2[i]] for i in range(3)]                        # 3x2
    Jt = lambda v: [dot(j1, v), dot(j2, v)]
    b = Jt(om)
    chk("L21i b constant", all(x.degree <= 0 for x in b))
    j1V = lin(Lm, V); j2V = lin(Nm, V)
    chk("L21i b = g J(V)^t u", b == [g*dot(j1V, u), g*dot(j2V, u)])
    chk("L21i J^t u = (t/g) b", Jt(u) == [tt*ginv*x for x in b])
    Om = lambda w: [w[1], w[0]]
    Jv = lambda M, w: [M[i][0]*w[0] + M[i][1]*w[1] for i in range(3)]
    vr = [rpoly(2) for _ in range(3)]
    chk("L21ii f x v = k0 J Om J^t v", cross(f, vr) == [k0*x for x in Jv(J, Om(Jt(vr)))])
    chk("L21ii f x omega = k0 J Om b", cross(f, om) == [k0*x for x in Jv(J, Om(b))])
    # Frobenius versions
    fX = frob(f, X); uX = frob(u, X); omX = frob(om, X); bX = frob(b, X); brho = frob(b, rho)
    JX = [[j1[i]**X, j2[i]**X] for i in range(3)]
    JXt = lambda v: [dot([JX[i][0] for i in range(3)], v), dot([JX[i][1] for i in range(3)], v)]
    k0X = k0**X; gX = g**X
    chk("expand g^X u^[X] = f^[X] + t^X om^[X]", [gX*x for x in uX] == [fX[i] + tt**X*omX[i] for i in range(3)])
    Mcol = [rpoly(1) for _ in range(3)]
    chk("CROSS f^[X] x m = k0^X J^[X] Om J^[X],t m", cross(fX, Mcol) == [k0X*x for x in Jv(JX, Om(JXt(Mcol)))])
    # unit 2x2 minor of J^[X] at t=0
    minors = [JX[i][0]*JX[j][1] + JX[i][1]*JX[j][0] for (i, j) in ((0, 1), (0, 2), (1, 2))]
    chk("J^[X] has a unit 2x2 minor", any(mn(GF(0)) != 0 for mn in minors))
    # FIX-1: u-component of (gamma) automatic
    y = [rpoly(3) for _ in range(3)]
    w = JXt(y)
    Cb = [k0X*x for x in Om(w)]                                     # C b^[rho] := k0^X Omega J^[X],t y
    ap = rpoly(2)
    m = [k0X*tt**X*ap*x + tt**rho*cb for x, cb in zip(Om(bX), Cb)]
    lhs = tt**(rho + X) * dot(uX, cross(omX, y))
    rhs = dot(uX, Jv(JX, m))
    chk("FIX1 u-component of (gamma) automatic", lhs == rhs)
    chk("FIX1 dot form: g^X u^[X].(om^[X] x y) = k0^X b^[X]t Om J^[X]t y",
        gX*dot(uX, cross(omX, y)) == k0X*dot(bX, Om(JXt(y))))
    chk("FIX1 dot form RHS: g^X u^[X].J^[X]m = t^(rho+X) b^[X]t C b^[rho]", gX*rhs == tt**(rho + X)*dot(bX, Cb))
    chk("FIX1 b^t Om b = 0 and b != 0", dot(bX, Om(bX)) == ZERO and any(x != ZERO for x in b))
    # FIX-3: dots of RHS(*)
    s = rpoly(2); F = rpoly(3); ac = F*ap
    W = [s*fX[i] + F*y[i] for i in range(3)]
    rhsstar_J = Jv(JX, [k0X*tt**X*ac*x + tt**rho*F*cb for x, cb in zip(Om(bX), Cb)])
    WxomX = cross(W, omX)
    rhsstar = [rhsstar_J[i] + tt**(rho + X)*WxomX[i] for i in range(3)]
    chk("FIX3 RHS(*).u^[X] == 0", dot(rhsstar, uX) == ZERO)
    chk("FIX3 RHS(*).om^[X] == t^rho F b^[X]t C b^[rho]", dot(rhsstar, omX) == tt**rho*F*dot(bX, Cb))
    chk("FIX3 v1 form t^(rho+X) F b C b is NOT it (when bCb != 0)",
        dot(bX, Cb) == ZERO or dot(rhsstar, omX) != tt**(rho + X)*F*dot(bX, Cb))
    # FIX-2: modification by F f^[X] (x) xi  (on the line)
    xi = [rpoly(2) for _ in range(3)]
    frho = frob(f, rho); omrho = frob(om, rho)
    add_on = lambda v: [F*fX[i]*dot(xi, v) for i in range(3)]       # (F f^[X] (x) xi) v
    chk("FIX2 alignment shift a -> a + F(xi.f^[rho])", add_on(frho) == [F*dot(xi, frho)*x for x in fX])
    chk("FIX2 f^[X] x (added term) == 0 (H, C unchanged)", cross(fX, add_on(vr)) == [ZERO]*3)
    chk("FIX2 y_u shift = f^[X](xi.om^[rho])", [x // F for x in add_on(omrho)] == [fX[i]*dot(xi, omrho) for i in range(3)])
n = len(results); bad = [r for r in results if not r[1]]
from collections import Counter
cnt = Counter(name for name, _ in results); okc = Counter(name for name, ok in results if ok)
for k in cnt: print(f"{k}: {okc[k]}/{cnt[k]}")
print("TOTAL", n, "checks;", len(bad), "failures")
