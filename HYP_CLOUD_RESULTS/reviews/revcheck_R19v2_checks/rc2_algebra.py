# Revision check R19 v2: local algebra checks for FIX-1 / FIX-2 (char 2), own code.
#  (a) v1-continuity counterexample (1,t^2,t^3): limit of z x z' vs true branch tangent.
#  (b) Lemma 1.1(i) v2 argument: for random v(t), z(t)=v(t)^[E] x y(t) (so v^[E].z==0),
#      ord_t(w^[E].z) >= E, and when the branch multiplicity m<E, l_w is the branch tangent.
#  (c) local toy showing the incidence argument alone cannot decide m(w)>=E:
#      v=(1,t,0), z=(t^E,1,b0+t^(E+1)) has m=E and l_w is NOT the branch tangent.
#  (d) FIX-1 Frobenius identity: c^[T].(lam*p'^[E]) = lam*(beta p1^{2r}+alpha p2^{2r})^X, E=2rX, T=2X,
#      c=(sqrt beta, sqrt alpha), checked as polynomials over GF(2).
#  (e) FIX-1 regularity: if C = P (x) w with w coprime polynomial entries and C polynomial,
#      then P is polynomial; and deg(gcd(P)) + deg(P/gcd) = deg C - deg w.
import random
from sympy import symbols, Poly, GF
t = symbols('t')
random.seed(19)
D = GF(2)

def P_(c):  # poly from coefficient list low->high
    return Poly(list(reversed(c)) if c else [0], t, domain=D)

def rnd(deg, const=None):
    c = [random.randint(0, 1) for _ in range(deg + 1)]
    if const is not None:
        c[0] = const
    return P_(c)

def ordt(p):
    if p.is_zero:
        return 10 ** 9
    terms = p.terms()
    return min(m[0] for m, _ in terms)

def frob(p, E):
    return p ** E   # char 2: p(t)^E (coefficients in GF(2))

def cross(a, b):
    return [a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0]]

def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]

def deriv(p):
    return p.diff(t)

out = []
# (a)
z = [P_([1]), P_([0, 0, 1]), P_([0, 0, 0, 1])]
zp = [deriv(x) for x in z]
zz = cross(z, zp)
k = min(ordt(x) for x in zz)
lim = [x.coeff_monomial(t ** k) for x in zz]
I_lim = ordt(dot([P_([c]) for c in lim], z))
true_tan = [0, 0, 1]
I_true = ordt(dot([P_([c]) for c in true_tan], z))
out.append("(a) z=(1,t^2,t^3): lim z x z' = %s, meets with mult %d; true tangent (0,0,1) mult %d" % (lim, I_lim, I_true))

# (b)
def mult_and_tangent(z, N=60):
    # normalise so that some coordinate of z(0) is 1 (z(0) != 0 assumed after removing t-power)
    k = min(ordt(x) for x in z)
    z = [Poly((x.as_expr() / t ** k).expand(), t, domain=D) for x in z]
    z0 = [x.coeff_monomial(1) for x in z]
    # transverse order: smallest i with z_i not parallel to z0
    for i in range(1, N):
        zi = [x.coeff_monomial(t ** i) for x in z]
        cr = cross([P_([c]) for c in z0], [P_([c]) for c in zi])
        if any(not c.is_zero for c in cr):
            tang = [c.coeff_monomial(1) for c in cr]   # line through z0 and z_i
            return i, tang, z
    return None, None, z

stats = {"ordge": 0, "tot": 0, "m<E": 0, "tangent_ok": 0}
for E in [4, 8]:
    for trial in range(40):
        v = [P_([1]), rnd(5, 0), rnd(5, 0)]
        y = [rnd(6), rnd(6), rnd(6)]
        vE = [frob(x, E) for x in v]
        z = cross(vE, y)
        if all(x.is_zero for x in z):
            continue
        assert dot(vE, z).is_zero
        w = [x.coeff_monomial(1) for x in v]
        wE = [P_([c]) for c in w]          # w^[E] = w for GF(2) coefficients
        m, tang, zn = mult_and_tangent(z)
        I = ordt(dot(wE, zn))
        stats["tot"] += 1
        stats["ordge"] += (I >= E)
        if m is not None and m < E:
            stats["m<E"] += 1
            # l_w is tangent iff l_w proportional to tang
            cr = cross(wE, [P_([c]) for c in tang])
            stats["tangent_ok"] += all(c.is_zero for c in cr)
out.append("(b) random branches E=4,8: I_w(l_w)>=E in %d/%d; among m<E: l_w = branch tangent in %d/%d"
           % (stats["ordge"], stats["tot"], stats["tangent_ok"], stats["m<E"]))

# (c)
for E in [4, 8]:
    v = [P_([1]), P_([0, 1]), P_([0])]
    z = [P_([0] * E + [1]), P_([1]), P_([1] + [0] * E + [1])]   # (t^E, 1, 1+t^(E+1))
    vE = [frob(x, E) for x in v]
    assert dot(vE, z).is_zero
    wE = [P_([1]), P_([0]), P_([0])]
    m, tang, zn = mult_and_tangent(z)
    I_lw = ordt(dot(wE, zn))
    I_tan = ordt(dot([P_([c]) for c in tang], zn))
    out.append("(c) E=%d toy: v=(1,t,0), z=(t^E,1,1+t^(E+1)): incidence ok; m=%d, I(l_w)=%d, tangent %s has I=%d -> l_w not tangent"
               % (E, m, I_lw, tang, I_tan))

# (d)
ok = 0
for trial in range(20):
    r, X = random.choice([(2, 2), (2, 4), (4, 2)])
    E, T = 2 * r * X, 2 * X
    sb, sa = rnd(3), rnd(3)                 # sqrt(beta), sqrt(alpha)
    beta, alpha = sb ** 2, sa ** 2
    lam, q1, q2 = rnd(2), rnd(3), rnd(3)    # lam(v), p'^sigma_i(y)  (p'(v)=p'^sigma(y)^E)
    lhs = sb ** T * lam * q1 ** E + sa ** T * lam * q2 ** E
    rhs = lam * (beta * q1 ** (2 * r) + alpha * q2 ** (2 * r)) ** X
    ok += (lhs - rhs).is_zero
out.append("(d) Pi_1 = lam * pi^X identity: %d/20" % ok)

# (e)
from sympy import gcd, div
ok = tot = 0
for trial in range(40):
    That = [rnd(3, 1), rnd(3), rnd(3), rnd(3)]
    g = That[0]
    for x in That[1:]:
        g = gcd(g, x)
    if g.degree() > 0:
        continue
    w = [x ** 4 for x in That]                     # w = That^{rho qq}, no common zero
    lam = rnd(2, 0) + P_([0, 0, 0, 1])               # lam(0)=0: Z(lam) nonempty
    p1, p2 = rnd(4, 1), rnd(4)
    gp = gcd(p1, p2)
    p1, p2 = div(p1, gp)[0], div(p2, gp)[0]
    if p2.is_zero:
        continue
    tot += 1
    Cm = [[lam * p1 * wj for wj in w], [lam * p2 * wj for wj in w]]
    rows = []
    for row in Cm:
        gg = row[0]
        for x in row[1:]:
            gg = gcd(gg, x)
        rows.append(gg)                               # = lam*p_i (monic): p is a polynomial (regular)
    allg = gcd(rows[0], rows[1])                      # = lam: common zeros of all entries of C = Z(lam)
    ok += (rows[0] == (lam * p1).monic()) and (rows[1] == (lam * p2).monic()) and (allg == lam.monic())
out.append("(e) row-gcd of [C_P|C_R] = lam*p'_i and gcd of all entries = lam (Z(lam) = common zeros): %d/%d" % (ok, tot))
print("\n".join(out))
