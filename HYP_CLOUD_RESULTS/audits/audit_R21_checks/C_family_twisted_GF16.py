# Referee check C (R21 Prop. 2.3), independent of the owner's family_check.py.
# Over GF(2^4) with B, L having entries outside F_2 (so B^[D] != B for D=2: the Frobenius twist is exercised;
# the owner's toy used B, L over GF(2) only, where B^[D]=B).  Original coordinates:
#   C_c(Y) = L^{-t} Ct(Bc),  Ct = h*Omega + mu (x) z^perp (D=1) or h'*J(z) + mu (x) z^perp (D=2),
#   K = L B^[D] (FNAP: L = K (B^{-1})^[D]),  P_D = (K c^[D])^t C_c(Y) (B c).
# F = conic Y1^2+Y0Y2 (d'=2) or Fermat cubic Y2^3+Y0^3+Y1^3 (d'=3); h = F*h1 (so (K) should hold).
# Checks: (1) P_D == 0; (2) (K): C_c(Y)Bc == 0 mod F; (3) Delta != 0 and F | Delta; (4) F does not divide all of C_P,C_R;
#         (5) normal form C_c == L^{-t}mu (x) (Bc)^perp mod F; (6) C_c Bc == L^{-t} h (Bc)^perp exactly (D=1),
#         == L^{-t} h' (Bc)^{perp[2]} (D=2)  [this is Prop 2.3(vii)'s formula; F|W_c iff F^2|h then follows by hand].
# Controls: (a) h with F not dividing h: (K) fails, P_D==0 persists; (b) wrong twist K'=L*B for D=2: P_D != 0;
#           (c) a random pencil (not in F_D): P_D != 0.
# Run: python3 -I C_family_twisted_GF16.py   (imports the referee helper gfpoly.py from this directory)
import random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
import galois
from gfpoly import Ring, mat_mul

GF = galois.GF(2**4)
R = Ring(GF, 5)            # variables: c1, c2, Y0, Y1, Y2
c1, c2, Y0, Y1, Y2 = (R.var(i) for i in range(5))
rng = random.Random(2110_1007)
add, mul, scal = R.add, R.mul, R.scal

def rand_form(deg):
    p = {}
    for i in range(deg+1):
        for j in range(deg+1-i):
            v = rng.randrange(16)
            if v: p[(0, 0, i, j, deg-i-j)] = v
    return p if p else {(0, 0, deg, 0, 0): 1}

def rand_gl2():
    while True:
        M = GF([[rng.randrange(16) for _ in range(2)] for _ in range(2)])
        if int(np.linalg.det(M)) and any(int(x) > 1 for x in M.flatten()): return M

CURVES = {
    'conic Y1^2+Y0Y2': (add(mul(Y1, Y1), mul(Y0, Y2)), 3, 2, mul(Y0, Y2), 2),
    'Fermat Y0^3+Y1^3+Y2^3': (add(add(R.powr(Y0, 3), R.powr(Y1, 3)), R.powr(Y2, 3)), 4, 3, add(R.powr(Y0, 3), R.powr(Y1, 3)), 3),
}
def modF(p, cv):
    F, var, deg, repl, _ = cv
    return R.reduce_monic(p, var, deg, repl)
def divF(p, cv): return R.iszero(modF(p, cv))

def build(D, cv, a, Kmode='right', hmode='F'):
    F, _, _, _, dF = cv
    B = rand_gl2(); L = rand_gl2()
    Lit = np.linalg.inv(L).T
    z = [add(scal(B[0, 0], c1), scal(B[0, 1], c2)), add(scal(B[1, 0], c1), scal(B[1, 1], c2))]
    zp = [z[1], z[0]]
    while True:
        mu = [rand_form(a), rand_form(a)]
        if not (divF(mu[0], cv) and divF(mu[1], cv)): break
    if D == 1:
        if hmode == 'F': h = mul(F, add(mul(rand_form(a-dF), z[0]), mul(rand_form(a-dF), z[1])))
        else:            h = add(mul(rand_form(a), z[0]), mul(rand_form(a), z[1]))
        Ct = [[mul(mu[0], zp[0]), add(h, mul(mu[0], zp[1]))], [add(h, mul(mu[1], zp[0])), mul(mu[1], zp[1])]]
    elif D == 2:
        h = mul(F, rand_form(a-dF)) if hmode == 'F' else rand_form(a)
        Ct = [[mul(mu[0], zp[0]), add(mul(h, z[1]), mul(mu[0], zp[1]))], [add(mul(h, z[0]), mul(mu[1], zp[0])), mul(mu[1], zp[1])]]
    else:  # 'random' pencil: arbitrary z-linear entries
        Ct = [[add(mul(rand_form(a), z[0]), mul(rand_form(a), z[1])) for _ in range(2)] for _ in range(2)]
        h = None; D = 2
    Litp = [[R.const(Lit[i, j]) for j in range(2)] for i in range(2)]
    C = mat_mul(R, Litp, Ct)
    BD = B ** D
    K = (L @ BD) if Kmode == 'right' else (L @ B)
    cD = [R.powr(c1, D), R.powr(c2, D)]
    Kc = [add(scal(K[i, 0], cD[0]), scal(K[i, 1], cD[1])) for i in range(2)]
    Cz = [add(mul(C[i][0], z[0]), mul(C[i][1], z[1])) for i in range(2)]
    PD = add(mul(Kc[0], Cz[0]), mul(Kc[1], Cz[1]))
    return dict(B=B, L=L, Lit=Lit, z=z, zp=zp, mu=mu, h=h, C=C, Cz=Cz, PD=PD, D=D)

def coeff_c1(p, which):   # C is linear in c: extract coefficient of c1 (which=0) or c2 (which=1)
    out = {}
    for m, v in p.items():
        if m[which] == 1 and m[1-which] == 0: out[(0, 0) + m[2:]] = v
    return out

def checks(d, cv):
    C, Cz, z, zp = d['C'], d['Cz'], d['z'], d['zp']
    r1 = R.iszero(d['PD'])
    r2 = divF(Cz[0], cv) and divF(Cz[1], cv)
    Delta = add(mul(C[0][0], C[1][1]), mul(C[0][1], C[1][0]))
    r3 = (not R.iszero(Delta)) and divF(Delta, cv)
    CP = [[coeff_c1(C[i][j], 0) for j in range(2)] for i in range(2)]
    CR = [[coeff_c1(C[i][j], 1) for j in range(2)] for i in range(2)]
    r4 = not all(divF(e, cv) for M in (CP, CR) for row in M for e in row)
    p = [add(scal(d['Lit'][i, 0], d['mu'][0]), scal(d['Lit'][i, 1], d['mu'][1])) for i in range(2)]
    r5 = all(divF(add(C[i][j], mul(p[i], zp[j])), cv) for i in range(2) for j in range(2))
    # (6) exact second layer
    if d['D'] == 1: v = zp
    else: v = [mul(z[1], z[1]), mul(z[0], z[0])]
    tgt = [add(scal(d['Lit'][i, 0], mul(d['h'], v[0])), scal(d['Lit'][i, 1], mul(d['h'], v[1]))) for i in range(2)]
    r6 = all(R.iszero(add(Cz[i], tgt[i])) for i in range(2))
    return r1, r2, r3, r4, r5, r6

allok = True
for name, cv in CURVES.items():
    dF = cv[4]
    for D in (1, 2):
        for a in (dF, dF+1, dF+2):
            res = [checks(build(D, cv, a), cv) for _ in range(3)]
            ok = all(all(r) for r in res); allok &= ok
            print(f"{name:<24} D={D} a={a}: (P_D==0, (K), Delta!=0 & F|Delta, F!|(C_P,C_R), normal form, exact C_cBc) ->",
                  "all True (3/3)" if ok else res)
# controls
ctl_a = [checks(build(1, cv, 4, hmode='free'), cv) for _ in range(3)]
print("control (a) D=1, F not| h, Fermat a=4: (K) holds in", sum(r[1] for r in ctl_a), "/3; P_D==0 in", sum(r[0] for r in ctl_a), "/3")
ctl_b = [build(2, cv, 4, Kmode='wrong') for _ in range(3)]
print("control (b) D=2, wrong twist K'=L*B (no Frobenius on B): P_D==0 in", sum(R.iszero(d['PD']) for d in ctl_b), "/3")
ctl_c = [build('random', cv, 3) for _ in range(3)]
print("control (c) random pencil (D=2): P_D==0 in", sum(R.iszero(d['PD']) for d in ctl_c), "/3")
allok &= sum(r[1] for r in ctl_a) == 0 and all(r[0] for r in ctl_a)
allok &= sum(R.iszero(d['PD']) for d in ctl_b) == 0 and sum(R.iszero(d['PD']) for d in ctl_c) == 0
print("all OK:", allok)
