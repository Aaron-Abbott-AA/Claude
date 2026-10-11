#!/usr/bin/env python3
"""R24 owner numerics (exact Fractions).  Run: python3 -I numerics_R24.py

Part A: p-adic-closed order sequences (eps_0=0, eps_1=1, length 2..4, entries <= 2^14).
        For r in {4,...,64}, x=S/q_max in {1,...,64}: N_0=(2r-1)x.  Report exact failing
        sets (sequences containing N_0: expected none), s=#{eps<N_0}, Sigma'=sum{eps<N_0},
        gamma'=N_0-max{eps<N_0}, and the maxima of Sigma'/gamma' and s/gamma'.
Part B: R22 Thm 5.3(i) bound B (reproduce corner 32480243592761/219902325555200),
        and the R24 (R1) bound  B + [s*tau_hi + Sigma'*(d^2-3d)]/gamma'  on the 1260-row grid
        (q_max ranging over dyadic 128..S), plus the monotone whole-strip upper bound.
        Exact failing rows (bound >= 1551/4000) are listed (expected: none).
Part C: F^2|a with (a_P,a_R)!=0 needs M'+Q-T >= 2d' >= 4E-4; with M'<8h/625 this fails at
        n=256 for all rows.  Report rows where it is feasible at n=256 (expected none) and
        the least dyadic n at which it is feasible, per (r,Q,S).
"""
from fractions import Fraction as Fr
from itertools import combinations

LIM = 2**14
pw = [2**k for k in range(0, 15)]

def closed(seq):
    s = set(seq)
    for e in seq:
        # every binary sub-integer of e must be in s
        m = e
        sub = m
        while True:
            if sub not in s:
                return False
            if sub == 0:
                break
            sub = (sub - 1) & m
    return True

# enumerate candidate sets: 0,1 and up to two more elements; elements must be
# 0, power of two, or sum of two distinct powers of two already present (else closure fails)
cands = set()
cands.add((0, 1))
P2 = [p for p in pw if p >= 2]
for a in P2:
    cands.add((0, 1, a))
for a, b in combinations(P2, 2):
    cands.add((0, 1, a, b))
for a in P2:
    cands.add((0, 1, a, a + 1))
seqs = sorted(s for s in cands if closed(s))
# sanity: brute force over small range that nothing else is closed (entries <= 64)
brute = []
for k in range(0, 3):
    for extra in combinations(range(2, 65), k):
        s = tuple(sorted((0, 1) + extra))
        if closed(s):
            brute.append(s)
small = sorted(s for s in seqs if max(s) <= 64)
print("Part A")
print("  closed sequences enumerated:", len(seqs))
print("  brute-force check (entries<=64): brute=%d, enumerated=%d, equal=%s"
      % (len(brute), len(small), sorted(brute) == small))

rs = [4, 8, 16, 32, 64]
xs = [1, 2, 4, 8, 16, 32, 64]
fail_order = []
worst = {}
glob_ratio = (Fr(0), None)
glob_sg = (Fr(0), None)
for r in rs:
    for x in xs:
        N0 = (2 * r - 1) * x
        gamma = (r - 1) * x - 1
        wr = (Fr(0), None)
        ws = (Fr(0), None)
        for s in seqs:
            if N0 in s:
                fail_order.append((r, x, s))
                continue
            below = [e for e in s if e < N0]
            gp = N0 - max(below)
            if gp < gamma:
                fail_order.append(("gamma", r, x, s))
            sig = sum(below)
            rat = Fr(sig, gp)
            sg = Fr(len(below), gp)
            if rat > wr[0]:
                wr = (rat, s)
            if sg > ws[0]:
                ws = (sg, s)
        ub = Fr(2 * r * x + 2, gamma)
        worst[(r, x)] = (wr, ws, ub)
        if wr[0] > glob_ratio[0]:
            glob_ratio = (wr[0], (r, x, wr[1]))
        if ws[0] > glob_sg[0]:
            glob_sg = (ws[0], (r, x, ws[1]))
        if wr[0] > ub:
            fail_order.append(("ub", r, x, wr))
print("  exact failing set (N0 an order, or gamma'<gamma, or ratio>(2rx+2)/gamma):", fail_order)
for (r, x) in [(4, 1), (4, 2), (8, 1), (16, 1), (64, 64)]:
    wr, ws, ub = worst[(r, x)]
    print("  r=%d x=%d: max Sigma'/gamma' = %s (seq %s), max s/gamma' = %s, (2rx+2)/gamma = %s"
          % (r, x, str(wr[0]), str(wr[1]), str(ws[0]), str(ub)))
print("  global max Sigma'/gamma' =", glob_ratio)
print("  global max s/gamma'      =", glob_sg)

# ---------------- Part B ----------------
print("Part B")
LIMIT = Fr(1551, 4000)

def B53(r, Q, S, n, qq=128):
    E = r * Q * S
    h = n * E
    q = n * E * E
    rho = Q // 2
    d = E + 2
    N = Fr(16 * h, 625)
    a = Fr(8 * h, 625)
    dprime = 2 * E + 4
    degT = N * d / rho + d
    charges = N * d + 2 * degT / qq + (Fr(3, 2) * d * d + Fr(7, 2) * d + 1) + Fr(6 * q, 1000) + 7
    degdd = 2 * (E + 1) * d + 2 * a * dprime + 2 * (N * d + rho * d)
    return (charges + degdd) / q

corner = B53(4, 128, 64, 256)
print("  R22 Thm 5.3(i) corner B/q =", corner, "=", float(corner),
      " reproduces 32480243592761/219902325555200:", corner == Fr(32480243592761, 219902325555200))

def R1bound(r, Q, S, n, qmax, mode="exact"):
    E = r * Q * S
    h = n * E
    q = n * E * E
    rho = Q // 2
    d = E + 2
    N = Fr(16 * h, 625)
    x = S // qmax
    tau_hi = (N * d / rho + d) / qmax  # real upper bound (floor not needed)
    if mode == "exact":
        wr, ws, ub = worst[(r, x)] if (r, x) in worst else (None, None, None)
        rat = wr[0]
        sg = ws[0]
    else:
        rat = Fr(5)
        sg = Fr(2)
    extra = sg * tau_hi + rat * (d * d - 3 * d)
    return B53(r, Q, S, n, 128) + extra / q

rows = 0
fails = []
mx = (Fr(0), None)
for r in rs:
    for Q in [2**k for k in range(7, 15)]:
        for S in [2**k for k in range(6, 13)]:
            n = 256
            while n < 4 * Q:
                for qm in [2**k for k in range(7, 13)]:
                    if qm > S:
                        continue
                    x = S // qm
                    if (r, x) not in worst:
                        continue
                    v = R1bound(r, Q, S, n, qm)
                    rows += 1
                    if v >= LIMIT:
                        fails.append((r, Q, S, n, qm, float(v)))
                    if v > mx[0]:
                        mx = (v, (r, Q, S, n, qm))
                n *= 2
print("  (R1) R24 bound on grid: %d (r,Q,S,n,q_max<=S) cases; exact failing set: %s" % (rows, fails))
print("  grid maximum =", float(mx[0]), "at", mx[1])
# whole-strip monotone upper bound at the corner (ratio 5, s/gamma'<=2, q_max>=128)
E = 4 * 128 * 64
cb = R1bound(4, 128, 64, 256, 128, mode="ub")
print("  whole-strip UB (ratio 5, s/gamma'<=2) at corner (4,128,64,256), q_max=128 (tau_hi largest):", cb, "=", float(cb))
print("  margin to 1551/4000:", float(LIMIT - cb))

# ---------------- Part C ----------------
print("Part C")
feas256 = []
nmin = {}
for r in rs:
    for Q in [2**k for k in range(7, 15)]:
        for S in [2**k for k in range(6, 13)]:
            E = r * Q * S
            T = Q * S
            n = 256
            first = None
            while n < 4 * Q * 4:
                Mp_sup = Fr(8 * n * E, 625)  # M' < 8h/625 (strict)
                feasible = Mp_sup + Q - T > 4 * E - 4  # need M'+Q-T >= 2d' >= 4E-4 with M'<Mp_sup
                if feasible and first is None:
                    first = n
                if n == 256 and feasible:
                    feas256.append((r, Q, S))
                n *= 2
            nmin[(r, Q, S)] = first
print("  rows (r,Q,S) where F^2|a with (a_P,a_R)!=0 is degree-feasible at n=256 (exact set):", feas256)
vals = sorted(set(v for v in nmin.values()))
print("  least dyadic n at which it is degree-feasible, over all 280 (r,Q,S):", vals)
# algebraic statement: 8*256E/625 + Q - T < 4E-4  <=>  (4-2048/625)E - 4 + T - Q > 0
print("  4-2048/625 =", Fr(4) - Fr(2048, 625))
