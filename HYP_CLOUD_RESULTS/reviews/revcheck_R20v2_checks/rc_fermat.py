# Revision-check (R20 v2) of the Example 2.4 adjudication (audit FIX-2 vs owner addendum).
# Toy: Fermat sigma1, E=8, Gamma: U0^7+U1^7+U2^7=0, e(U)=(U1U2,U0U2,U0U1), own line l_u={Y: u^[8].Y=0},
# residual points v_zeta=diag(1,zeta,zeta/(1+zeta))u^[8], zeta in F_8\{0,1};  M(U)=[[U0^7,U1^7],[U2^7,U0^7+U1^7]],
# c(u)=(sqrt(U2^7), sqrt(U0^7)),  Xi(u,v)=det(M(v)c, M(u)c).
# Independent code path (does not reuse owner code):
#  (1) symbolic derivation over F_2 of Xi on the affine chart u=(1,x,y): Xi = b^2(1+b^7), b=x^7 (=x^14(1+x^49));
#  (2) EXHAUSTIVE over all affine points of Gamma(GF(2^21)) with U0=1, U2!=0 (vectorised): Xi at the six v_zeta
#      from the matrix definition; zeta-independence; formula; zero set;
#  (3) j(u) := ord_u of e^*(l_u) = multiplicity of x_u as root of P(X)=(1+X^7)(X+x^8)^7 + y^56 X^7 (conic G=0 is a graph
#      over x; all 14 intersection points are affine), via Hasse derivatives; compared with the zero set of Xi;
#  (4) collision v_zeta = u (projectively) and zeta = x^-7 at every full-fibre point with g != 0.
# Run: python3 -I rc_fermat.py
import numpy as np
import sympy as sp
import galois, time

t0 = time.time()
# ---------- (1) symbolic
b, s = sp.symbols('b s')
# with u=(1,x,y): U0^7=1, U1^7=b, U2^7=1+b; c=(s,1) with s^2=1+b;  v_zeta^7 = (1, b^8, (1+b)^8)
def M(a0, a1, a2): return sp.Matrix([[a0, a1], [a2, a0 + a1]])
c = sp.Matrix([s, 1])
Mu = M(1, b, 1 + b); Mv = M(1, b**8, (1 + b)**8)
w1 = Mv*c; w2 = Mu*c
Xi = sp.expand(w1[0]*w2[1] + w1[1]*w2[0])
Xi_red = sp.Poly(sp.rem(sp.Poly(Xi, s, b, modulus=2).as_expr(), s**2 - (1 + b), s), s, b, modulus=2)
target = sp.Poly(b**2*(1 + b**7), s, b, modulus=2)
print("(1) symbolic over F_2: Xi(u,v_zeta) mod (s^2-(1+b)) =", Xi_red.as_expr(), "; equals b^2(1+b^7):", Xi_red == target)

# ---------- (2) exhaustive over GF(2^21)
m = 21
GF = galois.GF(2**m)
allel = GF.Range(0, 2**m)
p7 = (allel**7).view(np.ndarray).astype(np.int64)
root7 = np.full(2**m, -1, dtype=np.int64); root7[p7] = np.arange(2**m, dtype=np.int64)  # one 7th root per 7th power
isH = root7 >= 0
g7 = GF.primitive_element**((2**m - 1)//7)
mu7 = [g7**i for i in range(7)]                     # mu_7 = F_8^*
zetas = [z for z in mu7 if z != 1]                  # F_8 \ {0,1}
bs = np.nonzero(isH)[0]                             # b in H u {0}
ok = isH[bs ^ 1] & ((bs ^ 1) != 0)                  # 1+b also a nonzero 7th power (y != 0); char 2: 1+b = b xor 1
bs = bs[ok]
x0 = GF(root7[bs]); y0 = GF(root7[bs ^ 1])
# all points: x = x0*w^i (or x=0 once if b=0), y = y0*w^j
X_list = []; Y_list = []
for i in range(7):
    for j in range(7):
        X_list.append(x0*mu7[i]); Y_list.append(y0*mu7[j])
X = np.concatenate(X_list).view(GF); Y = np.concatenate(Y_list).view(GF)
# remove duplicates from x=0 (b=0): keep unique (x,y)
key = X.view(np.ndarray).astype(np.int64)*(2**m) + Y.view(np.ndarray).astype(np.int64)
_, uniq = np.unique(key, return_index=True)
X = X[uniq]; Y = Y[uniq]
npts = len(X)
one = GF(1)
assert np.all(one + X**7 + Y**7 == 0)
print(f"(2) affine points of Gamma(GF(2^21)) with U0=1, U2!=0: {npts}  [{time.time()-t0:.1f}s]")
sq = lambda z: z**(2**(m - 1))
U0 = GF(np.ones(npts, dtype=np.int64)); U1 = X; U2 = Y
c0 = sq(U2**7); c1 = sq(U0**7)
def Mrows(a0, a1, a2): return (a0, a1, a2, a0 + a1)
m00, m01, m10, m11 = Mrows(U0**7, U1**7, U2**7)
w2a = m00*c0 + m01*c1; w2b = m10*c0 + m11*c1
ue = (U0**8, U1**8, U2**8)
xis = []; coll = []
for z in zetas:
    v = (ue[0], z*ue[1], (z/(one + z))*ue[2])
    assert np.all(v[0]**7 + v[1]**7 + v[2]**7 == 0)                       # v on Gamma
    ev = (v[1]*v[2], v[0]*v[2], v[0]*v[1])
    assert np.all(ue[0]*ev[0] + ue[1]*ev[1] + ue[2]*ev[2] == 0)            # e(v) on l_u
    n00, n01, n10, n11 = Mrows(v[0]**7, v[1]**7, v[2]**7)
    w1a = n00*c0 + n01*c1; w1b = n10*c0 + n11*c1
    xis.append(w1a*w2b + w1b*w2a)
    # projective equality v == u  (u=(1,x,y), v0=1)
    coll.append((v[1] == U1) & (v[2] == U2))
xis = np.stack([np.asarray(t) for t in xis]); coll = np.stack(coll)
same = np.all(xis == xis[0], axis=0)
formula = (X**14*(one + X**49)).view(np.ndarray)
print(f"    Xi independent of zeta at all points: {bool(np.all(same))};  Xi == x^14(1+x^49) at all points: {bool(np.all(xis[0] == formula))}")
zero = xis[0] == 0
g = (U0*U1*U2).view(np.ndarray) != 0
print(f"    full fibres (all six Xi=0): {int(zero.sum())};  with g=0: {int((zero & ~g).sum())};  with g!=0: {int((zero & g).sum())}")
Xn = X.view(np.ndarray)
x49 = (X**49 == one); x7 = (X**7 == one)
print(f"    full fibres with g!=0 have x in mu_49\\mu_7: {bool(np.all(x49[zero & g] & ~x7[zero & g]))};  "
      f"#points with x in mu_49\\mu_7: {int((x49 & ~x7).sum())}")

# ---------- (4) collisions
ncoll = coll.sum(axis=0)
zinv = X**(-1) if False else None
zz = np.full(npts, -1, dtype=np.int64)
for k, z in enumerate(zetas):
    zz[coll[k]] = int(z)
Xg = X[g]; target_z = (Xg**7)**-1
print(f"(4) points with some v_zeta == u: {int((ncoll > 0).sum())}; with exactly one: {int((ncoll == 1).sum())}; "
      f"coincide with full fibres with g!=0: {bool(np.array_equal(ncoll > 0, zero & g))}")
sel = (ncoll == 1)
print(f"    colliding zeta equals x^-7 at all collision points: "
      f"{bool(np.all(zz[sel] == ((X[sel]**7)**-1).view(np.ndarray)))}")

# ---------- (3) j(u) via Hasse derivatives of P at x_u
# P(T) = sum_{i=0..7} T^i w^{7-i} + sum_{i=0..7} T^{i+7} w^{7-i} + cc T^7,  w = x^8, cc = y^56 (binom(7,i) all odd)
w = X**8; cc = Y**56
coef = []
for jdeg in range(15):
    if jdeg < 7: coef.append(w**(7 - jdeg))
    elif jdeg == 7: coef.append(one + w**7 + cc)
    else: coef.append(w**(14 - jdeg))
def hasse(k):
    tot = GF(np.zeros(npts, dtype=np.int64))
    for jdeg in range(k, 15):
        if sp.binomial(jdeg, k) % 2:
            tot = tot + coef[jdeg]*X**(jdeg - k)
    return tot
mult = np.full(npts, -1)
for k in range(0, 15):
    hk = hasse(k).view(np.ndarray)
    newly = (mult < 0) & (hk != 0)
    mult[newly] = k
hist = {int(k): int(v) for k, v in zip(*np.unique(mult, return_counts=True))}
print(f"(3) histogram of j(u)=ord_u e^*(l_u) over all {npts} points: {hist}")
jgt = (mult > 8) & g     # restricted to g!=0: at x=0 (g=0) the conic G contains the contracted line {U1=0},
                          # so P = T^14 and the x-projection does not compute j(u) there
print(f"    on g!=0: j(u) values {sorted(set(mult[g].tolist()))};  {{g!=0, j(u)>E}} == {{some v_zeta=u}}: {bool(np.array_equal(jgt, ncoll > 0))};  "
      f"{{g!=0, j(u)>E}} == {{g!=0 and full fibre}}: {bool(np.array_equal(jgt, zero & g))};  j(u)=E+1 there: {bool(np.all(mult[jgt] == 9))}")
print(f"    among g!=0 points with j(u)=E: full fibres = {int((zero & g & (mult == 8)).sum())}")
print(f"    (g=0 points x=0: P=T^14 because G contains the line U1=0 -- not a j(u) computation; value {sorted(set(mult[zero & ~g].tolist()))})")
print(f"done [{time.time()-t0:.1f}s]")
