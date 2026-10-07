# R20 v2, Example 2.4 [v2: FIX-2, FIX-8c].  (Header corrected: this is Example 2.4 of the R20 note.)
# Fermat sigma1, E=8: Gamma: U0^7+U1^7+U2^7=0; residual points of l_u: v_zeta=diag(1,z,z/(1+z))u^[8], z in F_8\{0,1}
# (R19 Ex. 1.6).  Invariant twist M(U)=[[U0^7,U1^7],[U2^7,U0^7+U1^7]], so M(v_zeta)=M(u)^[8];
# c(u)=(sqrt(beta):sqrt(alpha)), alpha=U0^7, beta=U2^7;  Xi(u,v)=det(M(v)c, M(u)c), independent of zeta.
# Part A: recount over GF(2^12) (as v1) and report U1 and g=U0U1U2 at the full clusters (audit FIX-2: all degenerate).
# Part B: check Xi(u,v_zeta) = x^14 (1+x^49) on u=(1,x,y) (referee's symbolic formula) at random points of GF(2^21),
#         and examine the full clusters at x in mu_49 \ mu_7 (g(u)!=0): there one residual point coincides with u.
# Toy only: no (K)-pencil, no FN condition.  Run: python3 -I fermat_cluster_v2.py
import random
import galois

def setup(m):
    GF = galois.GF(2**m)
    F8 = [g for g in (GF.primitive_element**((2**m-1)//7*i) for i in range(7))]   # F_8^* inside GF(2^m) (3|m)
    F8 = [g for g in F8 if g != 1]
    return GF, F8

def data(GF, F8, u, m):
    sq = lambda x: x**(2**(m-1))
    c = [sq(u[2]**7), sq(u[0]**7)]
    def M(w):
        a, b, cc = w[0]**7, w[1]**7, w[2]**7
        return [[a, b], [cc, a+b]]
    def Xi(v):
        Mu, Mv = M(u), M(v)
        w1 = [Mv[0][0]*c[0]+Mv[0][1]*c[1], Mv[1][0]*c[0]+Mv[1][1]*c[1]]
        w2 = [Mu[0][0]*c[0]+Mu[0][1]*c[1], Mu[1][0]*c[0]+Mu[1][1]*c[1]]
        return w1[0]*w2[1] + w1[1]*w2[0]
    ue = [t**8 for t in u]
    vs = [[ue[0], z*ue[1], z/(GF(1)+z)*ue[2]] for z in F8]
    for v in vs:
        assert sum((t**7 for t in v), GF(0)) == 0
        ev = [v[1]*v[2], v[0]*v[2], v[0]*v[1]]
        assert sum((ue[i]*ev[i] for i in range(3)), GF(0)) == 0
    return vs, [Xi(v) for v in vs]

def proj_eq(a, b):
    return all(a[i]*b[j] == a[j]*b[i] for i in range(3) for j in range(3))

# ---- Part A
GF, F8 = setup(12)
roots7 = {}
for y in GF.elements: roots7.setdefault(int(y**7), []).append(y)
hist = {}; clusters = []
for x in GF.elements:
    for y in roots7.get(int(GF(1)+x**7), []):
        if y == 0: continue
        u = [GF(1), x, y]
        vs, vals = data(GF, F8, u, 12)
        assert all(t == vals[0] for t in vals)
        nz = sum(1 for t in vals if t == 0); hist[nz] = hist.get(nz, 0) + 1
        if nz == 6: clusters.append((int(x), int(u[0]*u[1]*u[2])))
print("Part A, GF(2^12): histogram of N_Xi(u):", dict(sorted(hist.items())))
print("  full clusters (U1, g=U0U1U2) as integers:", clusters)
print("  all full clusters degenerate (U1=0, g=0):", all(a == 0 and b == 0 for a, b in clusters))

# ---- Part B
GF, F8 = setup(21); rng = random.Random(21)
def point_with_x(x):
    rts = galois.Poly([1, 0, 0, 0, 0, 0, 0, GF(1)+x**7], field=GF).roots()
    return [GF(1), x, rts[0]] if len(rts) and rts[0] != 0 else None
ok = 0; tried = 0
while tried < 20:
    x = GF(rng.randrange(2, 2**21)); u = point_with_x(x)
    if u is None: continue
    tried += 1
    vs, vals = data(GF, F8, u, 21)
    ok += all(t == x**14*(GF(1)+x**49) for t in vals)
print(f"Part B, GF(2^21): Xi(u,v_zeta) == x^14(1+x^49) for all zeta at {ok}/{tried} random points")
g49 = GF.primitive_element**((2**21-1)//49)
xs = [g49**i for i in range(49) if (g49**i)**7 != 1]
# NOTE (owner, v2): at x in mu_49\mu_7 one residual point coincides with u (zeta=x^-7 gives v_zeta=u projectively,
# since y^7=1+x^7=(1+zeta)/zeta), so Xi(u,u)=0 forces the whole zeta-independent fibre to vanish and j(u)>E there.
npts = 0; g_nz = 0; coll = 0; allzero = 0; expl = 0
for x in xs:
    u = point_with_x(x)
    if u is None: continue
    npts += 1
    vs, vals = data(GF, F8, u, 21)
    g_nz += (u[0]*u[1]*u[2] != 0)
    hit = [i for i, v in enumerate(vs) if proj_eq(v, u)]
    coll += (len(hit) == 1)
    expl += (len(hit) == 1 and F8[hit[0]] == x**(-7))
    allzero += all(t == 0 for t in vals)
print(f"  x in mu_49\\mu_7 (|.|={len(xs)}), one point u per x: {npts} points; g(u)!=0: {g_nz}; all six Xi=0: {allzero}")
print(f"  exactly one residual v_zeta equal to u (so j(u)>E): {coll}/{npts}; with zeta=x^-7: {expl}/{npts}")
print("  => in this toy every full cluster is degenerate: g=0 (Part A) or a residual point collides with u (Part B).")
