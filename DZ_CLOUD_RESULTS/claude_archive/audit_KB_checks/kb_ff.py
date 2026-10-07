#!/usr/bin/env python3
"""Referee finite-field toys for KB (pointwise analogues of the linear algebra in KB (ii)-(iv), sec. 2, sec. 1 subcase).
Usage: python3 -I kb_ff.py [seed]
F1  (ii)/(iii): host F_{2^32} ⊃ F_q = F_{2^16} ⊃ F_Q = F_{2^8} ⊃ F_s = F_{2^4}. Random A = sum a_i tau^i (d = 0..3, a_0 != 0),
    lambda in F_Q^*, B := sum (a_i / a_0^{2^i}) tau^i, eta := a_0*lambda. Check A(lambda t) = B(eta t) on F_s;
    Moore matrix M = [t_j^{2^i}] (4 x (d+1)) has full column rank; a left inverse with F_s entries recovers
    X_i = b_i eta^{2^i} from w_j, and X_0 = eta; also simulated twist a_i -> a_i chi^{2^i} (chi in F_s^*) maps W' to itself
    with eta -> eta chi and h = eta^{s-1} fixed, y = a_0^{Q-1} = h^{s+1} * lambda-free check.
F2  (iv): (F_q^*)^{s-1} = ker N_{F_q/F_s} for (m) = 8, 16 (exhaustive on F_q^*).
F3  inner resonance g = 3rho/2 (rho = 6, g = 9, m = 24): F_{2^rho} ⊂ F_Q, so V = mu F_{2^rho} satisfies v^Q = mu^{Q-1} v,
    i.e. V ⊂ mu F_Q (half-field, a(V) = 0): the B = 1 subcase is a global (H) family.
"""
import sys, random
import numpy as np
import galois

seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261007
rng = random.Random(seed)
fails = 0

def subfield_gen(GF, M, k):
    a = GF.primitive_element
    return a ** ((2 ** M - 1) // (2 ** k - 1))

def rand_nz(GF, M):
    while True:
        x = GF(rng.randrange(1, 2 ** M))
        if x != 0:
            return x

# ---------- F1 ----------
M = 32
GF = galois.GF(2 ** M)
m = 16; s4 = m // 4; s = 2 ** s4; Q = 2 ** (m // 2)
bs = subfield_gen(GF, M, s4)          # generator of F_s
bQ = subfield_gen(GF, M, m // 2)      # generator of F_Q
Fs = [GF(0)] + [bs ** k for k in range(s - 1)]
tbasis = [bs ** k for k in range(s4)]  # F_2-basis of F_s (degree-4 subfield, power basis)
def frob(x, i):
    return x ** (2 ** i)
ntr = 0
for trial in range(40):
    d = rng.randrange(0, 4)
    a = [rand_nz(GF, M) for _ in range(d + 1)]
    lam = bQ ** rng.randrange(0, Q - 1)
    A = lambda x: sum((a[i] * frob(x, i) for i in range(d + 1)), GF(0))
    b = [a[i] / frob(a[0], i) for i in range(d + 1)]
    eta = a[0] * lam
    B = lambda x: sum((b[i] * frob(x, i) for i in range(d + 1)), GF(0))
    for t in Fs:
        if A(lam * t) != B(eta * t):
            fails += 1; print("F1 A!=B", trial)
    w = [B(eta * t) for t in tbasis]
    Mm = GF([[frob(t, i) for i in range(d + 1)] for t in tbasis])
    if np.linalg.matrix_rank(Mm) != d + 1:
        fails += 1; print("F1 Moore rank", trial)
    # left inverse from the first d+1 rows (Moore square block invertible)
    Msq = Mm[: d + 1, :]
    Minv = np.linalg.inv(Msq)
    for x in Minv.flatten():
        if x ** s != x:
            fails += 1; print("F1 left inverse not in F_s", trial)
    X = Minv @ GF(w[: d + 1])
    for i in range(d + 1):
        if X[i] != b[i] * frob(eta, i):
            fails += 1; print("F1 X_i", trial, i)
    if X[0] != eta:
        fails += 1; print("F1 eta", trial)
    # simulated Galois twist by chi in F_s^*
    chi = bs ** rng.randrange(1, s - 1)
    a2 = [a[i] * frob(chi, i) for i in range(d + 1)]
    A2 = lambda x: sum((a2[i] * frob(x, i) for i in range(d + 1)), GF(0))
    Wp = set(int(A(lam * t)) for t in Fs)
    Wp2 = set(int(A2(lam * t)) for t in Fs)
    if Wp != Wp2:
        fails += 1; print("F1 W' not stable under twist", trial)
    eta2 = a2[0] * lam
    if eta2 != eta * chi or eta2 ** (s - 1) != eta ** (s - 1):
        fails += 1; print("F1 eta twist / h", trial)
    if frob(a[0], 0) ** (Q - 1) != (eta ** (s - 1)) ** (s + 1):
        fails += 1; print("F1 y = h^{s+1}", trial)
    ntr += 1
print(f"F1: {ntr} trials, d in 0..3, fails so far {fails}")

# ---------- F2 ----------
for mm in (8, 16):
    G2 = galois.GF(2 ** mm)
    q = 2 ** mm; ss = 2 ** (mm // 4)
    x = G2.Range(1, q) if hasattr(G2, "Range") else G2(np.arange(1, q))
    pw = set(int(v) for v in (x ** (ss - 1)))
    nm = set(int(v) for v in x if (v ** ((q - 1) // (ss - 1))) == 1)
    ok = (pw == nm)
    if not ok:
        fails += 1
    print(f"F2 m={mm}: |(F_q^*)^(s-1)| = {len(pw)}, |ker N| = {len(nm)}, equal sets: {ok}")

# ---------- F3 ----------
M3 = 24; rho = 6; G3 = galois.GF(2 ** M3); Q3 = 2 ** 12
b6 = subfield_gen(G3, M3, rho)
F64 = [G3(0)] + [b6 ** k for k in range(63)]
bad = 0
for trial in range(20):
    mu = rand_nz(G3, M3)
    for t in F64:
        v = mu * t
        if v ** Q3 != (mu ** (Q3 - 1)) * v:
            bad += 1
        if v != 0 and (v / mu) ** Q3 != v / mu:
            bad += 1
fails += bad
print(f"F3 (rho,g,m)=(6,9,24): 20 random mu, V = mu F_64 inside mu F_Q with v^Q = mu^(Q-1) v: failures {bad}")
print("TOTAL FAILURES:", fails)
