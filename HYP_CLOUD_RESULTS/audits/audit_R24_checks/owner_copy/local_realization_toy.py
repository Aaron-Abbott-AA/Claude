#!/usr/bin/env python3
"""R24 COMPUTED toy for Prop. 4.1/4.2 (own-line content of FN; local realisability of F^2|a).
On ONE own line Y(t)=z+tV, over GF(2^8)[[t]] truncated mod t^K:
  random L,N -> J=[L^tY,N^tY], f=j1 x j2 (kappa0=1); g:=1, u:=f(z); omega=(f(Y)-f(z))/t; b=J(Y)^t omega (constant, TSYC).
  'F' is a power series of exact order e (stand-in for F(Y(t)); e > X).
  C (2x2 series) is built to satisfy (alpha): C b^[rho] = gammaC * Omega b^[X], ord gammaC >= X (the (K)-situation).
  first layer kappa = J^[rho] v with s~ = v.b^[rho] of order >= e (nu_u >= e_u).
  Gt: 3x2 with J^[X,t] Gt = I.  P^t = f^[X] (x) kappa + F (Gt Omega C J^[rho,t] + f^[X] (x) sigma).
Checks:
 (A) FN (W=P^t u^[rho] parallel to u^[X]) holds iff alpha_2=0, where
     alpha_2 = kappa.u^[rho] + F sigma.u^[rho] + F t^rho gammaC (t^-X + zeta),  Gt b^[X] = omega^[X] + zeta f^[X];
     tested on random sigma (FN fails, alpha_2 != 0) and on the constructed sigma (both hold).
 (B) constructed sigma: sigma.u^[rho] = phi (prescribed), sigma.f^[rho] = 0 exactly along the line, hence the
     local alignment coefficient a = F sigma.f^[rho] vanishes to order >= 2e on the line (F^2|a-compatible jet).
 (C) control: if ord s~ = e-1 (nu_u < e_u) then t^-rho phi has a pole, so no regular sigma solves the two equations
     (the necessary condition nu_u >= e_u of R23 Cor 2.2(iii)); computed, not assumed.
Run: python3 -I local_realization_toy.py
"""
import random
import numpy as np
import galois

GF = galois.GF(2**8)
random.seed(24)
K = 96

def ser(lst):
    a = GF.Zeros(K)
    for i, c in enumerate(lst[:K]):
        a[i] = c
    return a

def rs(lo=0):
    a = GF.Zeros(K)
    for i in range(lo, K):
        a[i] = random.randrange(256)
    return a

def unit():
    a = rs(0)
    a[0] = random.randrange(1, 256)
    return a

def mul(a, b):
    return np.convolve(a, b)[:K]

def inv(a):
    assert a[0] != 0
    r = GF.Zeros(K)
    r[0] = a[0] ** -1
    for n in range(1, K):
        s = GF(0)
        for i in range(1, n + 1):
            s = s + a[i] * r[n - i]
        r[n] = -(s) * r[0]
    return r

def frob(a, k):
    # a(t)^k for k a power of 2 (Frobenius on series): coefficients^k at t^(ik)
    r = GF.Zeros(K)
    for i in range(K):
        if i * k < K:
            r[i * k] = a[i] ** k
    return r

def shift(a, m):  # multiply by t^m (m>=0)
    r = GF.Zeros(K)
    if m < K:
        r[m:] = a[:K - m]
    return r

def unshift(a, m):  # divide by t^m, requires a = O(t^m)
    assert np.all(a[:m] == 0), "pole"
    r = GF.Zeros(K)
    r[:K - m] = a[m:]
    return r

def order(a):
    nz = np.nonzero(np.array(a))[0]
    return int(nz[0]) if len(nz) else 10**9

def dot(v, w):
    return sum((mul(v[i], w[i]) for i in range(len(v))), GF.Zeros(K))

def cross(a, b):
    return [mul(a[1], b[2]) + mul(a[2], b[1]), mul(a[2], b[0]) + mul(a[0], b[2]), mul(a[0], b[1]) + mul(a[1], b[0])]

def const(c):
    return ser([c])

results = []
for (X, rho, e) in [(4, 2, 9), (8, 2, 17), (8, 4, 17), (16, 4, 33), (16, 8, 33)]:
    for trial in range(3):
        L = [[random.randrange(256) for _ in range(3)] for _ in range(3)]
        N = [[random.randrange(256) for _ in range(3)] for _ in range(3)]
        z = [random.randrange(256) for _ in range(3)]
        V = [random.randrange(256) for _ in range(3)]
        Y = [ser([z[i], V[i]]) for i in range(3)]
        j1 = [sum((mul(const(L[k][i]), Y[k]) for k in range(3)), GF.Zeros(K)) for i in range(3)]
        j2 = [sum((mul(const(N[k][i]), Y[k]) for k in range(3)), GF.Zeros(K)) for i in range(3)]
        f = cross(j1, j2)
        u = [const(f[i][0]) for i in range(3)]       # g := 1, u := f(z)
        if all(c[0] == 0 for c in u):
            continue
        omega = [unshift(f[i] + u[i], 1) for i in range(3)]
        b = [dot([j1[i] for i in range(3)], omega), dot([j2[i] for i in range(3)], omega)]
        assert all(np.all(b[k][1:] == 0) for k in range(2)), "b not constant"
        if b[0][0] == 0 or b[1][0] == 0:
            continue
        bX = [frob(b[k], X) for k in range(2)]
        brho = [frob(b[k], rho) for k in range(2)]
        OmbX = [bX[1], bX[0]]
        JX = [[frob(j1[i], X), frob(j2[i], X)] for i in range(3)]      # 3x2
        Jr = [[frob(j1[i], rho), frob(j2[i], rho)] for i in range(3)]
        fX = [frob(f[i], X) for i in range(3)]
        fr = [frob(f[i], rho) for i in range(3)]
        uX = [frob(u[i], X) for i in range(3)]
        ur = [frob(u[i], rho) for i in range(3)]
        omX = [frob(omega[i], X) for i in range(3)]
        omr = [frob(omega[i], rho) for i in range(3)]
        Fs = shift(unit(), e)
        # C with C b^[rho] = gammaC Omega b^[X], ord gammaC >= X:  C = Omega b^[X] (x) r + M,  r.b^[rho]=gammaC, M b^[rho]=0
        gammaC = shift(unit(), X + random.randrange(0, 3))
        # r = gammaC * (1/brho0, 0)
        r = [mul(gammaC, const(brho[0][0] ** -1)), GF.Zeros(K)]
        m1 = rs(); m2 = rs()
        # rows of M orthogonal to b^[rho]: (m * brho1, m * brho0) (char 2)
        M = [[mul(m1, brho[1]), mul(m1, brho[0])], [mul(m2, brho[1]), mul(m2, brho[0])]]
        C = [[mul(OmbX[i], r[j]) + M[i][j] for j in range(2)] for i in range(2)]
        Cb = [dot(C[i], brho) for i in range(2)]
        assert all(np.all(Cb[i] == mul(gammaC, OmbX[i])) for i in range(2))
        # first layer kappa = J^[rho] v, s~ = v.b^[rho] of order >= e
        stil = shift(unit(), e + random.randrange(0, 3))
        vv = [mul(stil, const(brho[0][0] ** -1)), GF.Zeros(K)]
        kap = [dot(Jr[i], vv) for i in range(3)]
        assert np.all(dot(kap, fr) == 0) and np.all(dot(kap, omr) == stil)
        # Gt with J^[X,t] Gt = I: pick two rows (i1,i2) of JX with unit 2x2 minor at t=0
        best = None
        for (i1, i2) in [(0, 1), (0, 2), (1, 2)]:
            dm = mul(JX[i1][0], JX[i2][1]) + mul(JX[i1][1], JX[i2][0])
            if dm[0] != 0:
                best = (i1, i2, dm)
                break
        i1, i2, dm = best
        di = inv(dm)
        # J^[X,t] restricted to rows i1,i2 is the 2x2 matrix Mt = [[JX[i1][0], JX[i2][0]],[JX[i1][1], JX[i2][1]]]
        Gt = [[GF.Zeros(K), GF.Zeros(K)] for _ in range(3)]
        Gt[i1][0] = mul(JX[i2][1], di); Gt[i1][1] = mul(JX[i2][0], di)
        Gt[i2][0] = mul(JX[i1][1], di); Gt[i2][1] = mul(JX[i1][0], di)
        for a_ in range(2):
            for c_ in range(2):
                val = sum((mul(JX[i][a_], Gt[i][c_]) for i in range(3)), GF.Zeros(K))
                assert np.all(val == (const(1) if a_ == c_ else GF.Zeros(K)))
        # zeta: Gt b^[X] - omega^[X] = zeta f^[X]
        Gb = [dot(Gt[i], bX) for i in range(3)]
        diff = [Gb[i] + omX[i] for i in range(3)]
        k0 = [i for i in range(3) if fX[i][0] != 0][0]
        zeta = mul(diff[k0], inv(fX[k0]))
        assert all(np.all(diff[i] == mul(zeta, fX[i])) for i in range(3))
        # S0 = Gt Omega C J^[rho,t]   (kappa0 = 1)
        OmC = [C[1], C[0]]
        GOC = [[sum((mul(Gt[i][k], OmC[k][j]) for k in range(2)), GF.Zeros(K)) for j in range(2)] for i in range(3)]
        S0 = [[sum((mul(GOC[i][k], Jr[jj][k]) for k in range(2)), GF.Zeros(K)) for jj in range(3)] for i in range(3)]

        def build(sigma):
            Pt = [[mul(fX[i], kap[jj]) + mul(Fs, S0[i][jj] + mul(fX[i], sigma[jj])) for jj in range(3)] for i in range(3)]
            W = [dot(Pt[i], ur) for i in range(3)]
            return Pt, W

        def alpha2(sigma):
            core = mul(gammaC, zeta) + unshift(gammaC, X)   # gammaC (t^-X + zeta)
            return dot(kap, ur) + mul(Fs, dot(sigma, ur)) + mul(Fs, shift(core, rho))

        # (A) random sigma
        sig_r = [rs(), rs(), rs()]
        _, W = build(sig_r)
        fn_r = all(order(c) >= K - X - 2 * rho for c in cross(W, uX))
        a2_r = order(alpha2(sig_r)) >= K - X - 2 * rho
        # constructed sigma: phi = t^rho [ s~/F + gammaC (t^-X + zeta) ]  (g=1)
        sF = mul(unshift(stil, e), inv(unshift(Fs, e)))    # s~/F regular since ord s~ >= e
        phi = shift(sF + mul(gammaC, zeta) + unshift(gammaC, X), rho)
        # solve A.u^[rho] = phi, A.omega^[rho] = t^-rho phi (char 2), third coordinate free = 0
        rhs2 = unshift(phi, rho)
        best = None
        for (p1, p2) in [(0, 1), (0, 2), (1, 2)]:
            dm2 = mul(ur[p1], omr[p2]) + mul(ur[p2], omr[p1])
            if dm2[0] != 0:
                best = (p1, p2, dm2); break
        p1, p2, dm2 = best
        d2 = inv(dm2)
        A = [GF.Zeros(K), GF.Zeros(K), GF.Zeros(K)]
        A[p1] = mul(mul(phi, omr[p2]) + mul(rhs2, ur[p2]), d2)
        A[p2] = mul(mul(phi, omr[p1]) + mul(rhs2, ur[p1]), d2)
        assert np.all(dot(A, ur) == phi) and np.all(dot(A, omr) == rhs2)
        Pt, W = build(A)
        fn_c = all(order(c) >= K - X - 2 * rho for c in cross(W, uX))
        a2_c = order(alpha2(A)) >= K - X - 2 * rho
        sf = order(dot(A, fr))
        aloc = mul(Fs, dot(A, fr))
        # also alignment of the constructed local P: P^t f^[rho] = (F sigma.f^[rho]) f^[X]
        al = [dot(Pt[i], fr) + mul(aloc, fX[i]) for i in range(3)]
        al_ok = all(order(c) >= K - 2 * X for c in al)
        # (C) control: ord s~ < e
        stil_bad = shift(unit(), e - 1)
        # s~/F has a simple pole; phi_bad = t^rho [s~/F + gammaC(t^-X+zeta)]; the second equation needs t^-rho phi_bad
        # to be a power series.  Compute t^rho * (that bracket) * t (to stay in k[[t]]) and test divisibility by t^(rho+1).
        sF_t = mul(unshift(stil_bad, e - 1), inv(unshift(Fs, e)))        # = t * s~/F
        phi_bad_t = shift(sF_t + shift(mul(gammaC, zeta) + unshift(gammaC, X), 1), rho)   # = t * phi_bad
        try:
            unshift(phi_bad_t, rho + 1)    # would be t^-rho phi_bad
            ctrl_pole = False
        except AssertionError:
            ctrl_pole = True
        results.append((X, rho, e, trial, fn_r, a2_r, fn_c, a2_c, sf, order(aloc), al_ok, ctrl_pole))
        print("X=%d rho=%d e=%d trial=%d | random sigma: FN %s, alpha2=0 %s | constructed sigma: FN %s, alpha2=0 %s, "
              "ord(sigma.f^[rho]) %s (>=K means 0 mod t^K), ord(local a) %s, alignment %s | control ord s~<e gives pole: %s"
              % (X, rho, e, trial, fn_r, a2_r, fn_c, a2_c, sf if sf < 10**9 else "inf", order(aloc) if order(aloc) < 10**9 else "inf", al_ok, ctrl_pole))
ok = all((not r[4]) and (not r[5]) and r[6] and r[7] and r[10] and r[11] for r in results)
print("cases:", len(results), " exact failing set:", [r[:4] for r in results if not ((not r[4]) and (not r[5]) and r[6] and r[7] and r[10] and r[11])])
print("ALL CHECKS PASS:", ok)
