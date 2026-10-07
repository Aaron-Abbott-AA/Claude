# Revision-check (R20 v2): headline numbers (Cor. 3.2, D_1, Prop. 5.2 margin) and Lemma 2.1(iii)/Prop. 2.2 spot tests.
# Exact Fractions / galois.  Run: python3 -I rc_misc.py
from fractions import Fraction as Fr
import math, random, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rc_thresholds as T

print("(a) Cor. 3.2: max a_max/d' at n=256 over owner grid (Q without 8192, S in {64,256}), and with Q=8192")
for grid_name, Qs in (("owner grid", (128, 256, 512, 1024, 2048, 4096, 16384)), ("with 8192", (128, 256, 512, 1024, 2048, 4096, 8192, 16384))):
    best = Fr(0); worst512 = None
    for r in (4, 8, 16):
        for Q in Qs:
            for S in (64, 256):
                E = r*Q*S
                for dp in range(2*E-2, 2*E+5):
                    P = T.params(r, Q, S, 256, dp); best = max(best, P['a']/dp)
                    P5 = T.params(r, Q, S, 512, dp); v = P5['a']/dp
                    worst512 = v if worst512 is None else min(worst512, v)
    print(f"   {grid_name}: max a_max/d' (n=256) = {float(best):.6f} (<1: {best < 1});  min a_max/d' (n=512) = {float(worst512):.4f}")
sup = (Fr(2048, 625) + Fr(1, 8) - 2)/2
print(f"   printed supremum (2048/625+1/8-2)/2 = {float(sup):.6f}")
# exact-algebra claim: (2048/625)E + E/(2r) - Q/2 < 4E-4 for r>=4, E>=2^15
ok = all(Fr(2048, 625)*E + Fr(E, 2*r) - Fr(Q, 2) < 4*E-4
         for r in (4, 8, 16, 32, 64) for Q in (128, 2**10, 2**14) for S in (1, 64, 4096) for E in [r*Q*S] if E >= 2**15)
print(f"   exact inequality 3.2768E+E/(2r)-Q/2<4E-4 on test set: {ok}")

print("(b) D_1/E at n=256 with m=E (Q=1024,S=64, d'=2E-2) and at n=512")
for r in (4, 8, 16):
    Q, S = 1024, 64; E = r*Q*S; dp = 2*E-2
    for n in (256, 512):
        P = T.params(r, Q, S, n, dp); D1 = dp - E - (P['a'] - E)
        print(f"   r={r} n={n}: D_1/E = {float(D1/E):.4f}")

print("(c) Prop. 5.2 margin, r=16, Q=128, n=256, qq=E/16, S=64: (4.1)+N4 bound/q - 1551/4000")
r, Q, S, n = 16, 128, 64, 256; E = r*Q*S; qq = E//16
worst = {}
for dp in range(2*E-2, 2*E+5):
    P = T.params(r, Q, S, n, dp)
    thi = math.floor(min(P['a']*dp/(P['rho']*qq), (P['N']*P['d']/P['rho'] + P['d'])/qq))
    lim = min(thi, dp-E)
    def marg(t):
        return T.f41(P, qq, t, True)/(P['q']*(dp-E-t+1))
    worst[dp] = (thi, lim, float(marg(1)), float(marg(lim)))
for dp, v in worst.items():
    print(f"   d'=2E{dp-2*E:+d}: tau_hi={v[0]} lim={v[1]} margin(1)={v[2]:.5f} margin(lim)={v[3]:.5f}")

print("(d) Lemma 2.1(iii) v2: affine invariance of the level s; Mobius counterexample t*w^7")
import galois
GF = galois.GF(2**8)
rng = random.Random(7)
def level(coeffs, E):  # coeffs[i] = coeff of t^i
    s = -1
    for i, c in enumerate(coeffs):
        if c != 0: s = max(s, i % E)
    return s
def poly_compose_affine(coeffs, lam, mu):
    # xi(lam t + mu)
    res = [GF(0)]*len(coeffs)
    powk = [GF(1)]  # (lam t + mu)^k
    for k, c in enumerate(coeffs):
        if k > 0:
            new = [GF(0)]*(len(powk)+1)
            for i, p in enumerate(powk):
                new[i] = new[i] + p*mu; new[i+1] = new[i+1] + p*lam
            powk = new
        for i, p in enumerate(powk):
            res[i] = res[i] + c*p
    return res
viol = 0; tests = 0
for trial in range(300):
    E = 8; a = rng.choice([8, 12, 15, 16, 20]); s0 = rng.randrange(0, E)
    coeffs = [GF(0)]*(a+1)
    for i in range(a+1):
        if i % E <= s0 and rng.random() < 0.7: coeffs[i] = GF(rng.randrange(256))
    lam = GF(rng.randrange(1, 256)); mu = GF(rng.randrange(256))
    s1 = level(coeffs, E); s2 = level(poly_compose_affine(coeffs, lam, mu), E)
    tests += 1; viol += (s2 > s1)
print(f"   affine changes: {viol}/{tests} raise the level (expected 0)")
print(f"   counterexample: level(t)= {level([GF(0),GF(1)],8)}, level(t^7)= {level([GF(0)]*7+[GF(1)],8)}")

print("(e) Prop. 2.2 FIX-5 wording: a-m <= s+K  <=>  s >= a-m-K (so reduction strictly better iff s <= a-m-K-1)")
bad = 0
for E in (8, 16):
    for a in range(E, 2*E):
        for m in range(1, E+1):
            K = a//E
            for s in range(0, E):
                if ((a-m) <= s+K) != (s >= a-m-K): bad += 1
print(f"   {bad} counterexamples")
