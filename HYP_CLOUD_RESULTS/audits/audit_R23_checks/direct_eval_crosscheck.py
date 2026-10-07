# direct_eval_crosscheck.py -- referee: evaluate (4.1)-N4 and (4.1') DIRECTLY as bound/q at given tau0
# (no quadratic algebra), to cross-check the interval solver and the r=16 "single value" claim.
# Run: python3 -I direct_eval_crosscheck.py
import sys, os, random
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_recount_R20_R23 import case, mode_params
from fractions import Fraction as Fr
from math import floor

THR = Fr(1551, 4000)

def direct(r, Q, S, n, qq, dp, tau, mode):
    E = r*Q*S; rho = Q//2; T = Q*S; X = T//2; h = n*E; q = n*E*E; d = E+2
    N = Fr(16*h, 625); a = Fr(8*h, 625) - dp + X - rho
    g2 = d*d - 3*d; degpsi = (E+1)*d; ddef = Fr(q, 1000); Eset = Fr(3*d*d+7*d+2, 2)
    m, N1 = mode_params(mode, E, X, rho*qq)
    degT = qq*tau
    # (4.1) with N4 and N1
    den = dp - E - tau + N1
    n4 = None
    if den > 0:
        rhs = ((dp-E)*degpsi + 2*r*(d-1)*(a*dp - rho*degT) + ((E+1)*g2 + 3*dp) + d*(2*dp+g2) + 2*d*tau
               + (dp-E)*((2*dp+g2)//(E-1))
               + den*(N*d + 2*tau + Eset + 3*d + 2*degpsi + 6*ddef + 7))
        n4 = rhs/den/q
    D1 = dp - E - (a - m)
    p41 = None
    if D1 > 0:
        BB = 2*degpsi + 2*(2*a-dp)*dp + g2
        rhs = ((dp-E)*degpsi + 2*r*(d-1)*(a*dp - rho*degT) + ((E+1)*g2 + 3*dp) + d*(2*dp+g2)
               + (dp-E)*((2*dp+g2)//(E-1)) + 2*d*tau + Fr(d*(dp-1)*(dp-2), 2)
               + D1*(N*d + 2*tau + Eset + 3*d + 6*ddef + 7 + BB + (2*dp+g2)))
        p41 = rhs/D1/q
    return n4, p41

E16 = 16*128*64
print("== r=16 n=256 Q=128 S=64 qq=4096 d'=2E-2: direct bound/q at sample tau0 (threshold 0.38775) ==")
for tau in (1, 5472, 5473, 10000, 30000, 63625, 63626, 100000):
    n4, p41 = direct(16, 128, 64, 256, 4096, 2*E16-2, tau, "R23")
    print("  tau0=%6d  N4=%s  (4.1')=%s" % (tau, None if n4 is None else "%.6f" % float(n4), None if p41 is None else "%.6f" % float(p41)))

# random cross-check of the interval solver against direct evaluation
random.seed(20261007)
mism = 0; checks = 0
cases = [(4,128,64,256),(8,256,64,256),(16,128,64,256),(4,1024,256,512),(8,1024,64,1024),(16,512,64,256),(4,4096,64,2048)]
for (r,Q,S,n) in cases:
    E = r*Q*S
    for mode in ("R20","R23"):
        for qq in (128, 512, 2048, 8192, 32768):
            for dp in (2*E-2, 2*E+1, 2*E+4):
                ok, how, fails = case(r,Q,S,n,qq,dp,mode)
                if how == "vacuous": continue
                rho = Q//2; h = n*E; d = E+2; N = Fr(16*h,625); a = Fr(8*h,625)-dp+(Q*S)//2-rho
                tau_hi = floor(min(a*dp/(rho*qq), (N*d/rho+d)/qq))
                failset = set()
                for (x,y) in fails:
                    failset.add(x); failset.add(y)
                samples = set(random.randrange(1, tau_hi+1) for _ in range(25)) | {1, tau_hi} | failset
                for (x,y) in fails:
                    for t in (x-1, y+1):
                        if 1 <= t <= tau_hi: samples.add(t)
                for t in samples:
                    n4, p41 = direct(r,Q,S,n,qq,dp,t,mode)
                    passes = (n4 is not None and n4 < THR) or (p41 is not None and p41 < THR)
                    infail = any(x <= t <= y for (x,y) in fails)
                    checks += 1
                    if passes == infail: mism += 1; print("MISMATCH", r,Q,S,n,mode,qq,dp,t)
print("solver vs direct evaluation: checks", checks, "mismatches", mism)
