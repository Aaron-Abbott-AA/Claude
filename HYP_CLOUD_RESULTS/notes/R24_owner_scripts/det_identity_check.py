#!/usr/bin/env python3
"""R24 COMPUTED check of the determinant identity (Prop. 2.2):
   det A = kappa0^{-(Q+T)} F^4 det(C_A) lambda_A,
   A = (l(U).Y) P^[2] + (m(U).Y) R^[2],  C_A = (l.Y) C_P^[2] + (m.Y) C_R^[2],
   lambda_A = (l.Y) a_P^2 + (m.Y) a_R^2,
for P^t = F K_P J^[rho,t] + f^[X] (x) eta_P (the general shape with J^[X,t]P^t = kappa0^{-X} F Omega C_P J^[rho,t],
C_P = kappa0^X Omega J^[X,t] K_P, a_P = eta_P . f^[rho]).  All steps of the proof are pointwise algebra, so
random evaluation over GF(2^16) is a valid test of the identity (probabilistic, COMPUTED).
Also: eta_P = eta_R = 0 (a_P=a_R=0) gives det A = 0 (the G5 consequence), and the layer/alignment identities.
Run: python3 -I det_identity_check.py
"""
import random
import galois
import numpy as np

GF = galois.GF(2**16)
random.seed(20261007)

def rnd(shape=None):
    if shape is None:
        return GF(random.randrange(1, 2**16))
    return GF(np.array([random.randrange(0, 2**16) for _ in range(int(np.prod(shape)))]).reshape(shape))

def cross(a, b):
    return GF([a[1]*b[2] + a[2]*b[1], a[2]*b[0] + a[0]*b[2], a[0]*b[1] + a[1]*b[0]])

def frob(M, k):
    return M ** k

Omega = GF([[0, 1], [1, 0]])
ok = 0
tot = 0
zero_ok = 0
nonzero = 0
ctrl_fail = 0
layer_ok = 0
for (X, rho) in [(4, 2), (8, 2), (8, 4), (64, 32), (128, 64), (4096, 64)]:
    Q, T = 2 * rho, 2 * X
    for trial in range(25):
        L = rnd((3, 3)); N = rnd((3, 3))
        Y = rnd((3,)); U = rnd((3,))
        k0 = rnd()
        j1 = L.T @ Y; j2 = N.T @ Y
        f = k0 * cross(j1, j2)
        J = GF(np.stack([j1, j2], axis=1))         # 3x2
        assert np.all(J.T @ f == 0)
        Fv = rnd()
        KP = rnd((3, 2)); KR = rnd((3, 2))
        eP = rnd((3,)); eR = rnd((3,))
        def Pt(K, e):
            return Fv * (K @ frob(J, rho).T) + np.outer(frob(f, X), e)
        PtP = Pt(KP, eP); PtR = Pt(KR, eR)
        CP = (k0 ** X) * (Omega @ (frob(J, X).T @ KP))
        CR = (k0 ** X) * (Omega @ (frob(J, X).T @ KR))
        # layer identity and alignment
        lhs = frob(J, X).T @ PtP
        rhs = (k0 ** X) ** -1 * Fv * (Omega @ CP @ frob(J, rho).T)
        aP = eP @ frob(f, rho); aR = eR @ frob(f, rho)
        if np.all(lhs == rhs) and np.all(PtP @ frob(f, rho) == aP * frob(f, X)):
            layer_ok += 1
        lY = (L @ U) @ Y; mY = (N @ U) @ Y
        A = lY * frob(PtP.T, 2) + mY * frob(PtR.T, 2)
        CA = lY * frob(CP, 2) + mY * frob(CR, 2)
        lam = lY * aP ** 2 + mY * aR ** 2
        detA = np.linalg.det(A)
        detCA = np.linalg.det(CA)
        pred = (k0 ** (Q + T)) ** -1 * Fv ** 4 * detCA * lam
        tot += 1
        if detA == pred:
            ok += 1
        if detA != 0:
            nonzero += 1
        # negative control: wrong power of F must fail whenever det A != 0
        if detA != 0 and detA != (k0 ** (Q + T)) ** -1 * Fv ** 3 * detCA * lam:
            ctrl_fail += 1
        # zero alignment
        A0 = lY * frob(Pt(KP, GF.Zeros(3)).T, 2) + mY * frob(Pt(KR, GF.Zeros(3)).T, 2)
        if np.linalg.det(A0) == 0:
            zero_ok += 1
    print("(X,rho)=(%d,%d): cumulative identity ok %d/%d" % (X, rho, ok, tot))
print("det identity: %d/%d; failing count %d" % (ok, tot, tot - ok))
print("layer identity + alignment: %d/%d" % (layer_ok, tot))
print("a_P=a_R=0 gives det A=0: %d/%d" % (zero_ok, tot))
print("det A nonzero in %d/%d samples; negative control (F^3 in place of F^4) fails in %d/%d of those" % (nonzero, tot, ctrl_fail, nonzero))
