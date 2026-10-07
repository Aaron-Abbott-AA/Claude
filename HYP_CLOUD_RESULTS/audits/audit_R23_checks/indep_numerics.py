# indep_numerics.py -- referee's independent checks of R23 Thm 3.1 numerics, Lemma 4.3 (p-adic orders),
# Cor 4.2 / Cor 4.5 numbers.  Exact Fractions.  Run: python3 -I indep_numerics.py
from fractions import Fraction as Fr
from itertools import combinations
from math import floor
import sympy as sp

THR = Fr(1551, 4000)

# ---------- A. Thm 3.1 ----------
print("== A. Thm 3.1 ==")
def thm31_terms(r, Q, S, n, qq=128, dp=None, keep_negative=False):
    E = r*Q*S; rho = Fr(Q, 2); T = Q*S; h = n*E; q = n*E*E; d = E+2
    N = Fr(16*h, 625); Mp = Fr(8*h, 625)
    degT = N*d/rho + d
    terms = dict(
        lam = N*d,
        detT = 2*degT/qq,
        frakE = Fr(3, 2)*d*d + Fr(7, 2)*d + 1,
        bdry = 6*Fr(q, 1000) + 7,
        psi = (E+1)*d,
    )
    if dp is None:
        terms['a_sec'] = 2*Mp*(2*E+4)          # drops (Q-T-d')d' <0, d'<=2E+4
    else:
        terms['a_sec'] = 2*(Mp + Q - T - dp)*dp
    return {k: Fr(v)/q for k, v in terms.items()}

corner = sum(thm31_terms(4, 128, 64, 256).values())
print(" corner UB:", corner, float(corner), " equals note's 101790647887837/1099511627776000:",
      corner == Fr(101790647887837, 1099511627776000), " < 1551/4000:", corner < THR)
# monotonicity: symbolic in continuous variables E (>=2^15), n (>=256), rho (>=64)
Es, ns, rhos = sp.symbols('E n rho', positive=True)
d = Es + 2; q = ns*Es**2; h = ns*Es
N = sp.Rational(16, 625)*h; Mp = sp.Rational(8, 625)*h
UB = (N*d + 2*(N*d/rhos + d)/128 + sp.Rational(3, 2)*d**2 + sp.Rational(7, 2)*d + 1 + 6*q/1000 + 7
      + (Es+1)*d + 2*Mp*(2*Es+4))/q
for var in (Es, ns, rhos):
    der = sp.simplify(sp.diff(UB, var))
    # check sign: numerator should be <=0 for E,n,rho>0
    num, den = sp.fraction(sp.together(der))
    print(" d(UB)/d%s numerator (should be <=0 for positive vars):" % var, sp.factor(num), "| den:", sp.factor(den))
# grid: exact bound maximised over d'
mx = None
for r in (4, 8, 16, 32, 64):
    for Q in [2**i for i in range(7, 15)]:
        for S in [2**i for i in range(6, 13)]:
            n = 256
            while n < 4*Q:
                v = max(sum(thm31_terms(r, Q, S, n, dp=dp).values()) for dp in range(2*r*Q*S-2, 2*r*Q*S+5))
                u = sum(thm31_terms(r, Q, S, n).values())
                assert v <= u
                if mx is None or v > mx[0]: mx = (v, (r, Q, S, n))
                n *= 2
print(" grid max exact bound/q:", float(mx[0]), "at", mx[1])
# R22 Cor 4.2 comparison value
print(" R22 Cor 4.2 corner (for comparison):", float(Fr(3194487655227, 34359738368000)))

# ---------- C. Lemma 4.3 ----------
print("== C. Lemma 4.3: order sequences closed under binary sub-integers, <=4 orders ==")
def subs(x):
    bits = [1 << i for i in range(x.bit_length()) if (x >> i) & 1]
    out = set()
    for k in range(len(bits)+1):
        for c in combinations(bits, k):
            out.add(sum(c))
    return out
def closed(S):
    S = set(S) | {0}
    return all(subs(x) <= S for x in S)
# brute force over ALL integers up to B (no popcount pre-filter) for small B
B = 160
brute = set()
for k in range(1, 4):
    for c in combinations(range(1, B+1), k):
        if closed(c): brute.add(c)
# structural prediction
def predicted(Bnd):
    P = [1 << i for i in range(Bnd.bit_length()) if (1 << i) <= Bnd]
    out = set()
    for a in P: out.add((a,))
    for a in P:
        for b in P:
            if a < b: out.add((a, b))
    for a in P:
        for b in P:
            for c in P:
                if a < b < c: out.add((a, b, c))
            if a < b and a+b <= Bnd: out.add((a, b, a+b))
    return out
print(" brute force (all integers <=%d): %d sequences; equals structural list (powers of 2, eps3=eps1+eps2): %s"
      % (B, len(brute), brute == predicted(B)))
L = 1 << 12
seqs = predicted(L)
print(" structural sequences with entries <=2^12:", len(seqs), "(owner: 443)")
bad = 0; gfail = 0; sumfail = 0
for r in (4, 8, 16, 32, 64, 128):
    for k in range(0, 12):
        N0 = (2*r-1) << k
        for s in seqs:
            if N0 in s: bad += 1
            if s[0] == 1:
                below = [0] + [e for e in s if e < N0]
                if N0 - max(below) < (r-1)*(1 << k) - 1: gfail += 1
for s in seqs:
    if s[0] == 1 and sum(s) > 2*s[-1]: sumfail += 1
print(" sequences containing (2r-1)2^k (r in 4..128, k<=11):", bad, "; gamma violations:", gfail,
      "; Sigma>2*eps_top violations (eps1=1):", sumfail)

# ---------- D. Cor 4.2 / Cor 4.5 ----------
print("== D. Cor 4.2(ii) and Cor 4.5 ==")
B53 = Fr(32480243592761, 219902325555200)
print(" 1551/4000 - B53(i) corner =", float(THR - B53), " (note: >0.240046)", THR - B53 > Fr(240046, 10**6))
# recompute R22 Thm 5.3(i) corner independently
def B53i(r, Q, S, n):
    E = r*Q*S; rho = Fr(Q, 2); h = n*E; q = n*E*E; d = E+2
    N = Fr(16*h, 625); degT = N*d/rho + d; a = Fr(8*h, 625); dp = 2*E+4
    charges = N*d + 2*degT/128 + Fr(3, 2)*d*d + Fr(7, 2)*d + 1 + 6*Fr(q, 1000) + 7
    dd2 = 2*(E+1)*d + 2*a*dp + 2*rho*degT
    return (charges + dd2)/q
print(" R22 Thm 5.3(i) corner recomputed equals R22's printed fraction:", B53i(4, 128, 64, 256) == B53)
# whole-strip sufficiency claim: Sigma<=0.238 gamma n => excluded
E0 = 4*128*64
c1 = Fr(238, 1000)*(1 + Fr(1, E0))                         # Sigma(E^2+E-2)/ (gamma q) with E>=2^15
h0 = 256*E0; q0 = 256*E0*E0; N0_ = Fr(16*h0, 625); d0 = E0+2
c2 = 4*(N0_*d0/64 + d0)/128/q0                             # (r_V+1) tau_hi / q at the corner (max)
tot_per_gamma = c1 + c2/2                                   # gamma>=2
print(" 0.238(1+1/E) =", float(c1), "; 4 tau_hi/q <=", float(c2), "; total/gamma (gamma>=2) =", float(tot_per_gamma),
      "; note prints <=0.2380137:", tot_per_gamma <= Fr(2380137, 10**7), "; < 0.240046:", tot_per_gamma < Fr(240046, 10**6))
# Sigma* on a grid, independent definition
def sigma_star(r, Q, S, n, qq):
    E = r*Q*S; rho = Fr(Q, 2); h = n*E; q = n*E*E; d = E+2
    N = Fr(16*h, 625)
    tau_hi = floor((N*d/rho + d)/qq)
    gamma = (r-1)*S//qq - 1
    room = gamma*(THR - B53i(r, Q, S, n))*q - 4*tau_hi
    s = room/(d*d - 3*d)
    sig = floor(s)
    if sig == s: sig -= 1
    return sig, gamma
worst = None; viol = 0
for r in (4, 8, 16, 32):
    for Q in [2**i for i in range(7, 15)]:
        for S in [2**i for i in range(7, 13)]:
            n = 256
            while n < 4*Q:
                qq = 128
                while qq <= S:
                    sg, gm = sigma_star(r, Q, S, n, qq)
                    if sg < Fr(238, 1000)*gm*n: viol += 1
                    rat = Fr(sg, n)
                    if worst is None or rat < worst[0]: worst = (rat, (r, Q, S, n, qq), sg, gm)
                    qq *= 2
                n *= 2
print(" Sigma* grid: min Sigma*/n =", float(worst[0]), "at", worst[1], "Sigma*=", worst[2], "gamma=", worst[3],
      "; violations of Sigma*>=0.238 gamma n:", viol)
# eps_top<N0 special case inequality: 2(2r-1)x <= 0.238*256*((r-1)x-1) for r>=4, x>=1 (x=S/qq)
okall = all(2*(2*r-1)*x <= Fr(238, 1000)*256*((r-1)*x-1) for r in (4, 8, 16, 32, 64, 128) for x in (1, 2, 4, 8, 64, 4096))
print(" eps_top<N0 => Sigma<=0.238*gamma*256 on sample (r,x):", okall)
