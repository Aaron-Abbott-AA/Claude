# Referee check B (R21): symbolic identities over F_2[indeterminates] (sympy, modulus=2).
# (1) Prop 2.1 Step 1/3/4/5/6: hand-proof algebra with generic h, mu (indeterminates standing for elements of k[Y]):
#     q = Ct z for the families; z^[D] . q == 0; det formulas; uniqueness (diagonal entries).
# (2) Prop 2.1 Step 1 (D=1,2) as a generic solve: for a GENERIC pencil Ct = z1 A1 + z2 A2 with 8 indeterminate
#     entries (a=0 block over F_2(params)), the coefficient equations of P_D==0 define a linear space; compare dims.
# (3) Lemma 3.1, Lemma 3.2 (i) (kappa parallel (alpha^X,beta^X)), (ii) squaring, Remark 3.4 identity.
# (4) Identity used by the referee: (L z)^perp == det(L) L^{-t} z^perp in char 2 (so (K c^[D])^perp-type
#     directions and L^{-t}(Bc)^perp agree for D=1, consistent with P_D==0 on F_1).
# Run: python3 -I B_symbolic_identities.py
import sympy as sp
P2 = lambda e, *g: sp.Poly(sp.expand(e), *g, modulus=2)
z1, z2, h1, h2, hp, m1, m2 = sp.symbols('z1 z2 h1 h2 hp m1 m2')
G = (z1, z2, h1, h2, hp, m1, m2)
iszero = lambda e: P2(e, *G).is_zero
Om = sp.Matrix([[0, 1], [1, 0]])
z = sp.Matrix([z1, z2]); zp = sp.Matrix([z2, z1])
mu = sp.Matrix([m1, m2])
h = h1*z1 + h2*z2
res = {}
# D=1 family
C1 = h*Om + mu*zp.T
res['D1: z^t C z == 0'] = iszero((z.T*C1*z)[0])
res['D1: det == h(h+mu.z)'] = iszero(C1.det() - h*(h + m1*z1 + m2*z2))
res['D1: diag entries == (mu1 z2, mu2 z1)'] = iszero(C1[0, 0] - m1*z2) and iszero(C1[1, 1] - m2*z1)
# D=2 family
J = sp.Matrix([[0, z2], [z1, 0]])
C2 = hp*J + mu*zp.T
z2v = sp.Matrix([z1**2, z2**2])
res['D2: C z == hp*(z2^2,z1^2) + mu*(2 z1 z2)'] = iszero((C2*z)[0] - hp*z2**2) and iszero((C2*z)[1] - hp*z1**2)
res['D2: z^[2]t C z == 0'] = iszero((z2v.T*C2*z)[0])
res['D2: det == hp(hp z1 z2 + mu1 z1^2 + mu2 z2^2)'] = iszero(C2.det() - hp*(hp*z1*z2 + m1*z1**2 + m2*z2**2))
res['D2: diag entries == (mu1 z2, mu2 z1)'] = iszero(C2[0, 0] - m1*z2) and iszero(C2[1, 1] - m2*z1)
# D=4,8: rank one
for D in (4, 8):
    zD = sp.Matrix([z1**D, z2**D]); C4 = mu*zp.T
    res[f'D{D}: z^[D]t (mu x zperp) z == 0 and det == 0'] = iszero((zD.T*C4*z)[0]) and iszero(C4.det())

# (2) generic solve over F_2: unknown entries a_{ijk} (C = z1 A1 + z2 A2), coefficient equations of P_D
a = sp.symbols('a0:8')
A1 = sp.Matrix([[a[0], a[1]], [a[2], a[3]]]); A2 = sp.Matrix([[a[4], a[5]], [a[6], a[7]]])
Cg = z1*A1 + z2*A2
for D, pred in ((1, 4), (2, 3), (4, 2), (8, 2), (3, 2), (5, 2)):
    zD = sp.Matrix([z1**D, z2**D])
    PD = sp.Poly(sp.expand((zD.T*Cg*z)[0]), z1, z2)   # coefficients in Z[a], linear in a
    eqs = [sp.Poly(c, *a) for c in PD.coeffs()]
    Mx = sp.Matrix([[e.coeff_monomial(v) for v in a] for e in eqs]) if eqs else sp.zeros(0, 8)
    # rank over F_2
    rows = [int(''.join(str(int(x) % 2) for x in Mx.row(i)), 2) for i in range(Mx.rows)]
    basis = {}
    for v in rows:
        while v:
            p = v.bit_length()-1
            if p in basis: v ^= basis[p]
            else: basis[p] = v; break
    kd = 8 - len(basis)
    res[f'generic a=0 block, D={D}: kernel dim {kd} (pred {pred})'] = (kd == pred)

# (3) Lemma 3.1: on l_u, G = c^[T].V ; with c1 c2 != 0 constants, G == 0 iff V = eta*(c2^T, c1^T)
c1, c2, V1, V2, eta, T = sp.symbols('c1 c2 V1 V2 eta T')
G3 = (c1, c2, V1, V2, eta)
res['Lemma 3.1: V=eta*(c^[T])^perp => c^[T].V == 0 (T=8 sample)'] = P2((c1**8)*(eta*c2**8) + (c2**8)*(eta*c1**8), *G3).is_zero
# Lemma 3.2(i): c=(sqrt(beta),sqrt(alpha)), T=2X: c^[T]=(beta^X,alpha^X); kappa || (alpha^X,beta^X) => c^[T].kappa=0
al, be, s = sp.symbols('al be s')
X = 4
res['Lemma 3.2(i): (beta^X,alpha^X).(s*alpha^X, s*beta^X) == 0'] = P2(be**X*s*al**X + al**X*s*be**X, al, be, s).is_zero
# Lemma 3.2(ii): kappa = beta k11 + sqrt(alpha beta) k12 + alpha k22 ; kappa^2 = beta^2 k11^2 + alpha beta k12^2 + alpha^2 k22^2
ra, rb, k11, k12, k22 = sp.symbols('ra rb k11 k12 k22')  # ra^2=alpha, rb^2=beta
kap = rb**2*k11 + ra*rb*k12 + ra**2*k22
res['Lemma 3.2(ii): kappa^2 == beta^2 k11^2 + alpha beta k12^2 + alpha^2 k22^2'] = P2(kap**2 - (rb**4*k11**2 + ra**2*rb**2*k12**2 + ra**4*k22**2), ra, rb, k11, k12, k22).is_zero
# Lemma 3.2: kappa formula from k_c = c1^2 k11 + c1 c2 k12 + c2^2 k22 with k11=C_P b1, k22=C_R b2, k12=C_P b2 + C_R b1
p = sp.symbols('p0:4'); r_ = sp.symbols('r0:4'); b = sp.symbols('b0:4'); cc1, cc2 = sp.symbols('cc1 cc2')
CP = sp.Matrix([[p[0], p[1]], [p[2], p[3]]]); CR = sp.Matrix([[r_[0], r_[1]], [r_[2], r_[3]]]); B = sp.Matrix([[b[0], b[1]], [b[2], b[3]]])
b1 = B[:, 0]; b2 = B[:, 1]
kc = (cc1*CP + cc2*CR)*(B*sp.Matrix([cc1, cc2]))
expn = cc1**2*(CP*b1) + cc1*cc2*(CP*b2 + CR*b1) + cc2**2*(CR*b2)
GG = (*p, *r_, *b, cc1, cc2)
res['k_c == c1^2 k11 + c1c2 k12 + c2^2 k22 (k11=C_P b1, k22=C_R b2, k12=C_P b2+C_R b1)'] = all(P2(kc[i]-expn[i], *GG).is_zero for i in range(2))
# Remark 3.4: in (K_psi): k12=0, k11=psi_v k22 ; k_{c(u)}(v) = beta_u k11 + alpha_u k22, alpha_u = psi_u beta_u
bu, psu, psv, k22v = sp.symbols('bu psu psv k22v')
res['Remark 3.4: beta_u psi_v k22 + psi_u beta_u k22 == beta_u (psi_v+psi_u) k22'] = P2(bu*psv*k22v + psu*bu*k22v - bu*(psv+psu)*k22v, bu, psu, psv, k22v).is_zero
# Remark 3.4 second display: Cc(v) Bu c == Cc(v) Bv c + Cc(v)(Bu+Bv) c  (char 2) -- trivial linearity
# (4) (L z)^perp == det(L) L^{-t} z^perp in char 2, i.e. Omega L == L^{-t}... check  L^t Omega L == det(L) Omega
l = sp.symbols('l0:4'); Lm = sp.Matrix([[l[0], l[1]], [l[2], l[3]]])
res['L^t Omega L == det(L) Omega (char 2)'] = all(P2(e, *l).is_zero for e in (Lm.T*Om*Lm - Lm.det()*Om))
w = 0
for k_, v_ in res.items():
    print(f"{'OK ' if v_ else 'FAIL'}  {k_}")
    w = w or (not v_)
print("all symbolic identities OK:", not w)
