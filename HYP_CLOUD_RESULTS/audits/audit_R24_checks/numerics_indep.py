#!/usr/bin/env python3
"""Referee R24: independent exact numerics (Fractions).  Run: python3 -I numerics_indep.py

Part 1 (Lemma 3.2 / R23 Lemma 4.3): brute force, WITHOUT assuming the popcount structure, all subsets
  {0,1,a} and {0,1,a,b} (1<a<b<=2^LIMB) closed under binary sub-integers; confirm they are exactly
  (0,1,2^i), (0,1,2^i,2^j), (0,1,2^i,2^i+1).  Then, with the structural list up to 2^30, compute for
  r=2^2..2^12, x=2^0..2^12 the exact sup of Sigma'/gamma' and s/gamma', gamma'>=gamma, N_0 never an
  order, and the extremal sequences.  Exact failing sets printed.
Part 2 (Thm 3.3): R22 Thm 5.3(i) bound B coded from R22's text; whole-strip bound
  B + 2 tau_hi + 5(d^2-3d) at the corner; per-case bound with exact per-(r,x) worst (s,Sigma',gamma')
  (worst taken jointly per sequence, not ratio-by-ratio) on a grid r<=1024, Q<=2^16, S<=2^14, n in strip,
  q_max in [128,S]; monotonicity of every term checked on the grid (exact).
Part 3 (Cor 2.4 / R23 Remark 3.4): at n=256, M'+Q-T < 2d' for all (r,Q,S) on a big grid (exact, with
  M'<8h/625 and d'>=2E-2); feasibility at n=512 and the strip constraint n<4Q (so Q>=256 is forced).
  Symbolic: M'+Q-T>=2d'  <=>  a>=d'+3(X-rho)  (a=M'+X-rho-d', Q=2rho, T=2X).
"""
from fractions import Fraction as Fr
from itertools import combinations
import sympy as sp

def closed(s):
    S = set(s)
    for e in s:
        sub = e
        while True:
            if sub not in S:
                return False
            if sub == 0:
                break
            sub = (sub - 1) & e
    return True

print("Part 1")
LIMB = 10
lim = 2 ** LIMB
found = []
for a in range(2, lim + 1):
    if closed((0, 1, a)):
        found.append((0, 1, a))
for a in range(2, lim + 1):
    # quick prune: a itself must be closed in {0,1,a,b} => every sub-integer of a is in {0,1,a,b}
    for b in range(a + 1, lim + 1):
        if closed((0, 1, a, b)):
            found.append((0, 1, a, b))
found.append((0, 1))
def ispow2(v):
    return v > 0 and v & (v - 1) == 0
def form(s):
    if s == (0, 1):
        return True
    if len(s) == 3:
        return ispow2(s[2])
    a, b = s[2], s[3]
    return ispow2(a) and (ispow2(b) or b == a + 1)
nonform = [s for s in found if not form(s)]
print("  brute-force closed sequences with eps_1=1, entries<=2^%d: %d; not of the 3 forms: %s" % (LIMB, len(found), nonform))
expected = 1 + LIMB + LIMB * (LIMB - 1) // 2 + (LIMB - 1)  # (0,1); (0,1,2^i) i=1..L; pairs; (0,1,2^i,2^i+1) i=1..L-1
print("  expected count 1+L+C(L,2)+(L-1) =", expected, " match:", expected == len(found))

# structural list up to 2^30
P = [2 ** i for i in range(1, 31)]
seqs = [(0, 1)] + [(0, 1, a) for a in P] + [(0, 1, a, b) for a, b in combinations(P, 2)] + [(0, 1, a, a + 1) for a in P]
fail1 = []
sup_ratio = (Fr(0), None)
sup_sg = (Fr(0), None)
worst_joint = {}
for lr in range(2, 13):
    r = 2 ** lr
    for lx in range(0, 13):
        x = 2 ** lx
        N0 = (2 * r - 1) * x
        gam = (r - 1) * x - 1
        cases = set()
        for s in seqs:
            if N0 in s:
                fail1.append(("N0 order", r, x, s))
                continue
            below = [e for e in s if e < N0]
            gp = N0 - max(below)
            if gp < gam:
                fail1.append(("gamma'<gamma", r, x, s))
            cases.add((len(below), sum(below), gp))
            rat = Fr(sum(below), gp); sg = Fr(len(below), gp)
            if rat > sup_ratio[0]:
                sup_ratio = (rat, (r, x, s))
            if sg > sup_sg[0]:
                sup_sg = (sg, (r, x, s))
            if rat > 5 or sg > 2:
                fail1.append(("ratio", r, x, s, rat, sg))
            if Fr(sum(below), gp) > Fr(2 * (r * x + 1), gam):
                fail1.append(("ratio>2(rx+1)/gamma", r, x, s))
        worst_joint[(r, x)] = cases
print("  exact failing set (N_0 an order / gamma'<gamma / Sigma'/gamma'>5 / s/gamma'>2 / >2(rx+1)/gamma):", fail1)
print("  sup Sigma'/gamma' =", sup_ratio[0], "at", sup_ratio[1], "; sup s/gamma' =", sup_sg[0], "at", sup_sg[1])
# algebraic: 2(rx+1) <= 5((r-1)x-1)  <=> x(3r-5) >= 7
rr, xx = sp.symbols('r x', positive=True)
print("  5((r-1)x-1) - 2(rx+1) =", sp.expand(5 * ((rr - 1) * xx - 1) - 2 * (rr * xx + 1)), "(>=0 for r>=4,x>=1: 7x-7>=0 at r=4, increasing in r)")

print("Part 2")
LIMIT = Fr(1551, 4000)

def params(r, Q, S, n):
    E = r * Q * S
    h = n * E
    q = n * E * E
    rho = Q // 2
    d = E + 2
    N = Fr(16 * h, 625)
    a = Fr(8 * h, 625)
    dp = 2 * E + 4
    return E, h, q, rho, d, N, a, dp

def B53(r, Q, S, n):
    E, h, q, rho, d, N, a, dp = params(r, Q, S, n)
    degT = N * d / rho + d
    charges = N * d + 2 * degT / 128 + (Fr(3, 2) * d * d + Fr(7, 2) * d + 1) + Fr(6, 1000) * q + 7
    degpsi = (E + 1) * d
    deg_dd2 = 2 * degpsi + 2 * a * dp + 2 * (N * d + rho * d)
    return (charges + deg_dd2) / q

def terms(r, Q, S, n, qmax):
    E, h, q, rho, d, N, a, dp = params(r, Q, S, n)
    tau_hi = (N * d / rho + d) / qmax
    return B53(r, Q, S, n), tau_hi / q, Fr(d * d - 3 * d, q)

c = B53(4, 128, 64, 256)
print("  B_5.3(i) corner =", c, float(c), " equals R22's 32480243592761/219902325555200:", c == Fr(32480243592761, 219902325555200))
b, t, D2 = terms(4, 128, 64, 256, 128)
UB = b + 2 * t + 5 * D2
print("  whole-strip UB B + 2tau_hi + 5(d^2-3d) at corner (4,128,64,256), q_max=128:", UB, float(UB))
print("  equals owner's 91941792089517/549755813888000:", UB == Fr(91941792089517, 549755813888000), "; < 1551/4000:", UB < LIMIT)
print("  pieces: B=%.9f  2tau_hi/q=%.3e  5(d^2-3d)/q=%.9f" % (float(b), float(2 * t), float(5 * D2)))
# grid with joint worst case per (r,x)
grid = 0
fails = []
mx = (Fr(0), None)
mono_fail = []
for lr in range(2, 11):
    r = 2 ** lr
    for lQ in range(7, 17):
        Q = 2 ** lQ
        for lS in range(6, 15):
            S = 2 ** lS
            n = 256
            while n < 4 * Q:
                for lq in range(7, lS + 1):
                    qm = 2 ** lq
                    x = S // qm
                    if (r, x) not in worst_joint:
                        continue
                    b, t, D2 = terms(r, Q, S, n, qm)
                    best = max(Fr(sn * t + sig * D2, gp) for (sn, sig, gp) in worst_joint[(r, x)]) * 1
                    # convert: |B0|/q <= (s*tau_hi + Sigma'(d^2-3d))/(gamma' q)
                    val = b + best
                    grid += 1
                    if val >= LIMIT:
                        fails.append((r, Q, S, n, qm, float(val)))
                    if val > mx[0]:
                        mx = (val, (r, Q, S, n, qm))
                    if val > UB:
                        mono_fail.append((r, Q, S, n, qm))
                n *= 2
print("  grid cases (r<=1024,Q<=2^16,S<=2^14,256<=n<4Q, 128<=q_max<=S):", grid)
print("  exact failing set (bound >= 1551/4000):", fails)
print("  grid max =", float(mx[0]), "at", mx[1], "; exact set of cases exceeding the corner UB:", mono_fail)
# monotonicity of each term along each axis on a sub-grid (exact)
mono = []
for lr in range(2, 10):
    for lQ in range(7, 14):
        for lS in range(7, 13):
            r, Q, S = 2 ** lr, 2 ** lQ, 2 ** lS
            base = terms(r, Q, S, 256, 128)
            for (r2, Q2, S2, n2) in [(2 * r, Q, S, 256), (r, 2 * Q, S, 256), (r, Q, 2 * S, 256), (r, Q, S, 512)]:
                nxt = terms(r2, Q2, S2, n2, 128)
                for i in range(3):
                    if nxt[i] > base[i]:
                        mono.append(((r, Q, S), (r2, Q2, S2, n2), i))
print("  exact set of monotonicity violations (each of B, tau_hi/q, (d^2-3d)/q non-increasing):", mono)

print("Part 3")
fail256 = []
feas512 = []
cnt = 0
for lr in range(2, 13):
    r = 2 ** lr
    for lQ in range(7, 21):
        Q = 2 ** lQ
        for lS in range(6, 21):
            S = 2 ** lS
            E = r * Q * S
            T = Q * S
            cnt += 1
            Msup = Fr(8 * 256 * E, 625)   # M' < 8h/625, h=256E
            if not (Msup + Q - T <= 2 * (2 * E - 2)):
                fail256.append((r, Q, S))
            Msup5 = Fr(8 * 512 * E, 625)
            if Msup5 + Q - T > 2 * (2 * E + 4):
                feas512.append((r, Q, S))
print("  (r,Q,S) tested:", cnt, "; exact set where M'+Q-T<2d' is NOT forced at n=256:", fail256)
print("  n=512 degree-feasible (even against d'=2E+4) on %d/%d; but the strip n<4Q puts n=512 only at Q>=256" % (len(feas512), cnt))
Mp, X, rho, dp = sp.symbols("Mp X rho dp")
a = Mp + X - rho - dp
lhs = (Mp + 2 * rho - 2 * X) - 2 * dp
rhs = a - (dp + 3 * (X - rho))
print("  symbolic: (M'+Q-T-2d') - (a-d'-3(X-rho)) =", sp.simplify(lhs - rhs))
# R23 Remark 3.4 constant: 2048/625
print("  8*256/625 =", Fr(8 * 256, 625), "=", float(Fr(2048, 625)), "< 4: E-threshold for (4-2048/625)E>4:", Fr(4) / (Fr(4) - Fr(2048, 625)))
