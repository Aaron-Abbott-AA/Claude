# COMPUTED checks of the algebra of §3 (random values over GF(2^16)):
# (1) with T=That^[qq], B=swap.(T^t)^[rho], c=(1,s^rho), s a root of F_u(s)=T22 s^{Q+1}+T21 s^Q+T12 s+T11:
#     c^[Q] || B(u)c ;  det(B(v)c, c^[Q]) = F_v(s)^rho ;  det(B(v)c, B(u)c) = kappa * F_v(s)^rho, kappa!=0.
# (2) det(B(v)c,B(u)c) = sigma_u(v)^(rho*qq) with sigma_u linear in the entries of That(v).
# (3) normal form: C_P=p(x)b1perp, C_R=p(x)b2perp  =>  c^[T]^t C_c c^[Q] = (c^[T].p) * det(Bc, c^[Q]) for free c.
import random, galois, numpy as np
GF = galois.GF(2**16); rng = random.Random(5); R = lambda: GF(rng.randrange(1, 2**16))
det = lambda x, y: x[0]*y[1] + x[1]*y[0]
perp = lambda x: GF([x[1], x[0]])
ok = [0, 0, 0]; N = 0
for rho, qq in [(2, 4), (4, 8), (8, 16), (64, 128)]:
    Q = 2*rho
    for _ in range(25):
        N += 1
        s = R(); Thu = GF([[R(), R()], [R(), R()]]); Tu = Thu**qq
        Tu[0, 0] = Tu[1, 1]*s**(Q+1) + Tu[1, 0]*s**Q + Tu[0, 1]*s          # force F_u(s)=0
        Thv = GF([[R(), R()], [R(), R()]]); Tv = Thv**qq
        Bm = lambda T: GF([[T[1, 0]**rho, T[1, 1]**rho], [T[0, 0]**rho, T[0, 1]**rho]])
        Bu, Bv = Bm(Tu), Bm(Tv)
        c = GF([1, s**rho]); cQ = c**Q
        Fv = Tv[1, 1]*s**(Q+1) + Tv[1, 0]*s**Q + Tv[0, 1]*s + Tv[0, 0]
        a1 = det(cQ, Bu @ c) == 0
        a2 = det(Bv @ c, cQ) == Fv**rho
        kap = (Bu @ c)[0]/cQ[0]
        a3 = det(Bv @ c, Bu @ c) == kap*Fv**rho and kap != 0
        ok[0] += a1 and a2 and a3
        # (2): entries of Bv are (That entries)^(rho*qq); sigma = sum w_i^(1/rq) c_j^(1/rq) Bhat_ij
        rq = rho*qq; inv = lambda x: x**pow(rq, -1, GF.order-1) if x != 0 else x
        Bh = GF([[Thv[1, 0], Thv[1, 1]], [Thv[0, 0], Thv[0, 1]]])
        w = perp(Bu @ c)
        sig = sum((inv(w[i])*inv(c[j])*Bh[i, j] for i in range(2) for j in range(2)), GF(0))
        ok[1] += det(Bv @ c, Bu @ c) == sig**rq
        # (3): free c, random p, b1, b2
        Tt = 2*Q*rho                     # any power of 2 for the identity
        p = GF([R(), R()]); b1 = GF([R(), R()]); b2 = GF([R(), R()]); cf = GF([R(), R()])
        CP = np.outer(p, perp(b1)); CR = np.outer(p, perp(b2)); Cc = cf[0]*CP + cf[1]*CR
        Bc = cf[0]*b1 + cf[1]*b2
        ok[2] += (cf**Tt) @ Cc @ (cf**Q) == ((cf**Tt) @ p) * det(Bc, cf**Q)
print(f"(1) slope/eigen identities {ok[0]}/{N}; (2) Xi = sigma_u(v)^(rho qq) {ok[1]}/{N}; (3) K-normal-form factorisation {ok[2]}/{N}")
