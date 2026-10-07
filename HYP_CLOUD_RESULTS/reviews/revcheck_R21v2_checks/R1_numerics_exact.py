# Revision check R21 v2: FIX-2 / FIX-4 numerics, exact Fractions + sympy monotonicity.
# Run: python3 -I R1_numerics_exact.py
# Normalisation (R19/R20/FNAP, as in the note): E=rQS, h=nE, q=Eh=nE^2, rho=Q/2, d=E+2,
#   N=16h/625, a=8h/625 (suprema of the strict bounds), d_def=q/1000, deg psi<=(E+1)d, d'<=2E+4, deg[T]<=Nd/rho+d.
from fractions import Fraction as Fr
import random
import sympy as sp

THR = Fr(1551, 4000)

def raw_count(r, Q, S, n, D):
    E = r*Q*S; h = n*E; q = E*h; d = E+2
    N = Fr(16*h, 625); a = Fr(8*h, 625)
    return (N*d + (D+2)*(E+1)*d + (Q+1)*a + Fr(6, 1000)*q + 7) / q

def termwise_count(r, Q, S, n, D):  # the note's FIX-2 display
    E = Fr(r*Q*S); q = n*E*E
    return (Fr(16, 625)*(1+2/E) + Fr(D+2, 1)/n*(1+1/E)*(1+2/E)
            + Fr(8*(Q+1), 625*r*Q*S) + Fr(6, 1000) + 7/q)

def raw_kappa(r, Q, S, n, dp_shift=4):
    E = r*Q*S; h = n*E; q = E*h; d = E+2; rho = Fr(Q, 2)
    N = Fr(16*h, 625); a = Fr(8*h, 625); dp = 2*E+dp_shift
    degT = N*d/rho + d
    return (2*(E+1)*d + 2*a*dp + 2*rho*degT) / q

ok = True
def chk(name, cond):
    global ok
    ok &= bool(cond)
    print(f"[{'OK' if cond else 'FAIL'}] {name}")

# 1. Corner values, exact
c1 = raw_count(4, 128, 64, 256, 1); c2 = raw_count(4, 128, 64, 256, 2)
print("corner D=1:", c1, float(c1)); print("corner D=2:", c2, float(c2))
chk("D=1 corner == audit 7451214389181/171798691840000", c1 == Fr(7451214389181, 171798691840000))
chk("D=2 corner == audit 8122364470431/171798691840000", c2 == Fr(8122364470431, 171798691840000))
chk("D=1 corner rounds to 0.0433718", round(float(c1), 7) == 0.0433718)
chk("D=2 corner rounds to 0.0472784", round(float(c2), 7) == 0.0472784)
chk("corners <= note's 0.04338 / 0.04728", c1 <= Fr(4338, 100000) and c2 <= Fr(4728, 100000))
chk("corners < 1551/4000 = 0.38775 (margin > 0.34)", c1 < THR and c2 < THR and THR - c2 > Fr(34, 100))
# D-lane: S=Q^j*D with j>=1, so the smallest S is Q*D (S=128 for D=1, S=256 for D=2 at Q=128)
l1 = raw_count(4, 128, 128, 256, 1); l2 = raw_count(4, 128, 256, 256, 2)
print("D-lane corners (S=QD):", float(l1), float(l2), " [D=2 at S=Q=128 would be", float(raw_count(4, 128, 128, 256, 2)), "]")
chk("D-lane D=1 corner rounds to 0.0433453", round(float(l1), 7) == 0.0433453)
chk("D-lane D=2 corner: nearest 7-digit value is 0.0472383 (note/audit print 0.0472384, a valid upper bound)",
    round(float(l2), 7) == 0.0472383 and l2 < Fr(472384, 10**7))

# 2. The note's term-by-term display equals the raw bound
random.seed(1)
pts = [(4, 128, 64, 256)] + [(random.choice([4, 5, 7, 8, 13, 64, 1000]), random.choice([128, 200, 2**10, 2**20]),
        random.choice([64, 97, 128, 2**12]), random.choice([256, 300, 511, 4096, 10**6])) for _ in range(200)]
chk("FIX-2 termwise formula == raw (N d+(D+2)(E+1)d+(Q+1)a+6d_def+7)/q at 201 points, D=1,2",
    all(termwise_count(*p, D) == raw_count(*p, D) for p in pts for D in (1, 2)))

# 3. Monotonicity (symbolic): each term's partial derivative in r, Q, S, n is <= 0 for positive variables
r, Q, S, n = sp.symbols('r Q S n', positive=True)
E = r*Q*S
terms = [sp.Rational(16, 625)*(1+2/E), (sp.Symbol('Dp2', positive=True))/n*(1+1/E)*(1+2/E),
         8*(Q+1)/(625*r*Q*S), sp.Rational(6, 1000), 7/(n*E**2)]
kterms = [2/n*(1+1/E)*(1+2/E), sp.Rational(32, 625)*(1+2/E),            # 2deg psi/q ; 2 a d'/q (d'=2E+4)
          sp.Rational(32, 625)*(1+2/E), (1+2/E)/(n*r*S)]                  # 2Nd/q ; 2 rho d/q (rho=Q/2)
def nonincreasing(t):
    for v in (r, Q, S, n):
        num, den = sp.fraction(sp.together(sp.diff(t, v)))
        num = sp.expand(num); den = sp.expand(den)
        # positive vars: sign determined if all coefficients of num are <=0 and den's are >=0 (or both flipped)
        cn = sp.Poly(num, r, Q, S, n, sp.Symbol('Dp2')).coeffs() if num != 0 else [0]
        cd = sp.Poly(den, r, Q, S, n, sp.Symbol('Dp2')).coeffs()
        if not ((all(c <= 0 for c in cn) and all(c >= 0 for c in cd)) or (all(c >= 0 for c in cn) and all(c <= 0 for c in cd))):
            return False
    return True
chk("count: every term non-increasing in r,Q,S,n (sympy, sign of derivative numerators)", all(nonincreasing(t) for t in terms))
chk("negative control: the sign test rejects increasing terms (n, Q/(rS), E/n)",
    not nonincreasing(n) and not nonincreasing(Q/(r*S)) and not nonincreasing(E/n))
kraw = (2*(E+1)*(E+2) + 2*sp.Rational(8, 625)*n*E*(2*E+4) + 2*(sp.Rational(16, 625)*n*E*(E+2) + Q/2*(E+2)))/(n*E**2)
chk("kappa^2 bound: termwise split equals raw", sp.simplify(kraw - sum(kterms)) == 0)
chk("kappa^2 bound: every term non-increasing in r,Q,S,n", all(nonincreasing(t) for t in kterms))

# 4. Grid reproduction (owner grid) and whole-strip sampling
wg = {1: Fr(0), 2: Fr(0)}; wk = Fr(0); rows = 0
for rr in [4, 8, 16, 32, 64]:
    for QQ in [2**v for v in range(7, 15)]:
        for SS in [2**s for s in range(6, 13)]:
            nn = 256
            while nn < 4*QQ:
                for D in (1, 2):
                    wg[D] = max(wg[D], raw_count(rr, QQ, SS, nn, D))
                wk = max(wk, raw_kappa(rr, QQ, SS, nn)); rows += 1; nn *= 2
chk(f"grid rows = {rows} == 1260", rows == 1260)
chk("grid max == corner (D=1, D=2)", wg[1] == c1 and wg[2] == c2)
ck = raw_kappa(4, 128, 64, 256)
print("kappa^2 corner:", ck, float(ck))
chk("grid kappa^2 max == corner == 946909077437/8589934592000", wk == ck == Fr(946909077437, 8589934592000))
chk("kappa^2 corner > 0.1102 (v1 statement false) and <= 0.110235 < 0.1103", ck > Fr(1102, 10000) and ck <= Fr(110235, 1000000) < Fr(1103, 10000))
ck1 = raw_kappa(4, 128, 64, 256, dp_shift=1)
chk("with d'<=2E+1: 0.1102324", round(float(ck1), 7) == 0.1102324)
random.seed(7); bad = 0
for _ in range(3000):
    rr = random.randint(4, 300); QQ = random.randint(128, 10**5); SS = random.randint(64, 10**4); nn = random.randint(256, 10**6)
    if raw_count(rr, QQ, SS, nn, 1) > c1 or raw_count(rr, QQ, SS, nn, 2) > c2 or raw_kappa(rr, QQ, SS, nn) > ck:
        bad += 1
chk("3000 random non-dyadic strip points: none exceeds the corner values", bad == 0)
print("ALL OK" if ok else "SOME FAIL")
