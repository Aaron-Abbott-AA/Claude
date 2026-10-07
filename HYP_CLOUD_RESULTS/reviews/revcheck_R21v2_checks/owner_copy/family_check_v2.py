# R21 Prop. 2.3 check [v2: N1 header fixed; computation identical to family_check.py; B, L in GL_2(F_2), so the Frobenius twist K=LB^[D] is not exercised here (audit N3, see the audit check C over GF(16))]: the D in {1,2} normal-form families satisfy the C-level identities of the constant-twist (K) setting.
# Over GF(2), F = Fermat cubic Y0^3+Y1^3+Y2^3 (irreducible, d'=3) and the conic Y0Y2+Y1^2 (d'=2).
# Original coordinates: C_c(Y) = L^{-t} Ct(Bc),  Ct(z) = h*Omega + mu (x) z^perp  (D=1)  or  h'*J(z) + mu (x) z^perp (D=2),
# with random invertible constant B, L over GF(2), h = F*h1 (so that (K) holds), mu random with F not dividing mu.
# FNAP's K = L B^[D] (since L = K (B^{-1})^[D]).  Checks:
#  (1) P_D(c,Y) = (K c^[D])^t C_c(Y) (B c) == 0 identically            (own-line divisibility vacuous)
#  (2) C_c(Y) B c == 0 mod F for all c (both entries, as polynomials)     ((K) for constant T)
#  (3) Delta(c,Y)=det C_c(Y) != 0 (FNAM2) and F | Delta                    (R18-T Prop. 4.1(ii))
#  (4) F does not divide all entries of C_P, C_R                           (R19 reduction)
#  (5) on F=0: C_c == p (x) (Bc)^perp with p = L^{-t} mu                  (R19 Lemma 3.1 normal form)
#  (6) a >= d'  (R20 Prop. 3.1)
# Run: python3 -I family_check_v2.py
import random
import sympy as sp
c1, c2, Y0, Y1, Y2 = sp.symbols('c1 c2 Y0 Y1 Y2')
GENS = (c1, c2, Y0, Y1, Y2)
rng = random.Random(2110)
P = lambda e: sp.Poly(e, *GENS, modulus=2)

def rand_form(deg):
    mons = [Y0**i*Y1**j*Y2**(deg-i-j) for i in range(deg+1) for j in range(deg+1-i)]
    while True:
        f = sum(m for m in mons if rng.random() < 0.5)
        if f != 0: return sp.expand(f)
def rand_GL2():
    while True:
        M = sp.Matrix(2, 2, [rng.randrange(2) for _ in range(4)])
        if M.det() % 2 == 1: return M
def mod2(M): return M.applyfunc(lambda e: P(e).as_expr())
def inv2(M):  # inverse over GF(2) of a 2x2 matrix with det=1
    return sp.Matrix([[M[1, 1], M[0, 1]], [M[1, 0], M[0, 0]]])
def divF(e, F):
    e = sp.expand(e)
    if e == 0: return True
    _, r = sp.reduced(e, [F], Y0, Y1, Y2, c1, c2, modulus=2)
    return P(r).is_zero

def check(D, F, dF, a, control=False):
    B, L = rand_GL2(), rand_GL2()
    Linv_t = inv2(L).T
    z = B*sp.Matrix([c1, c2]); zp = sp.Matrix([z[1], z[0]])
    mu = sp.Matrix([rand_form(a), rand_form(a)])
    while divF(mu[0], F) and divF(mu[1], F): mu = sp.Matrix([rand_form(a), rand_form(a)])
    if D == 1:
        h = sp.expand(F*(rand_form(a-dF)*z[0] + rand_form(a-dF)*z[1])) if not control else sp.expand(rand_form(a)*z[0] + rand_form(a)*z[1])
        Ct = sp.Matrix([[0, h], [h, 0]]) + mu*zp.T
    else:
        hp = sp.expand(F*rand_form(a-dF))
        Ct = sp.Matrix([[0, hp*z[1]], [hp*z[0], 0]]) + mu*zp.T
    C = mod2(sp.expand(Linv_t*Ct))
    K = L*B.applyfunc(lambda e: e**D)
    cD = sp.Matrix([c1**D, c2**D])
    PD = sp.expand(((K*cD).T*C*z)[0])
    r1 = P(PD).is_zero
    Kv = sp.expand(C*z)
    r2 = divF(Kv[0], F) and divF(Kv[1], F)
    Delta = sp.expand(C.det())
    r3 = (not P(Delta).is_zero) and divF(Delta, F)
    CP = C.subs({c1: 1, c2: 0}); CR = C.subs({c1: 0, c2: 1})
    r4 = not all(divF(sp.expand(e), F) for e in list(CP)+list(CR))
    p = mod2(sp.expand(Linv_t*mu)); diff = sp.expand(C - p*zp.T)
    r5 = all(divF(e, F) for e in diff)
    return r1, r2, r3, r4, r5, a >= dF

for (Fname, F, dF) in [("conic Y0Y2+Y1^2", Y0*Y2+Y1**2, 2), ("Fermat cubic", Y0**3+Y1**3+Y2**3, 3)]:
    for D in [1, 2]:
        for a in [dF, dF+1, dF+2]:
            res = [check(D, F, dF, a) for _ in range(3)]
            print(f"{Fname:<17} D={D} a={a}: (P_D==0, (K), FNAM2 & F|Delta, F not| C, normal form, a>=d') ->",
                  "all True" if all(all(r) for r in res) else res)

# negative control: h not divisible by F (outside (K)): expect P_D==0 still True but (K) False
ctl = [check(1, Y0**3+Y1**3+Y2**3, 3, 4, control=True) for _ in range(3)]
print("control (D=1, h random, F=Fermat cubic, a=4): (K) holds in", sum(r[1] for r in ctl), "of 3; P_D==0 in", sum(r[0] for r in ctl), "of 3")
