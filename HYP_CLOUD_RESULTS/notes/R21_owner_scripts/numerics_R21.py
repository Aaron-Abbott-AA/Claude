# R21 exact (Fraction) numerics.  Run: python3 -I numerics_R21.py
# (1) Cor. 1.2: PRIMARY's FNAO/FNAP count  N_good <= N d + (D+2)(E+1)d + (Q+1)a + 6 d_def + 7  (valid whenever the
#     reduced slope polynomial P_D is not identically zero; FNAP's D>2 hypothesis is used ONLY for P_D != 0) evaluated
#     for D in {1,2}, with the R19/FNAP normalisation N<16h/625, a<8h/625, d=E+2, d_def<=q/1000.  Exclusion iff < 1551/4000.
# (2) Lemma 2.3: degree of the own-point defect section kappa^2,  2 deg psi + 2 a d' + 2 rho deg[T],
#     with deg[T] <= N d/rho + d (R18 a priori), deg psi <= (E+1)d, d'<=2E+4, as a fraction of q.
from fractions import Fraction as Fr
THR = Fr(1551, 4000)
worst = {1: Fr(0), 2: Fr(0)}; worst_k = Fr(0); rows = 0
for r in [4, 8, 16, 32, 64]:
    for Q in [2**v for v in range(7, 15)]:
        for S in [2**s for s in range(6, 13)]:
            E = r*Q*S; d = E+2; rho = Q//2
            n = 256
            while n < 4*Q:
                h = n*E; q = E*h; N = Fr(16*h, 625); a = Fr(8*h, 625)
                for D in [1, 2]:
                    b = (N*d + (D+2)*(E+1)*d + (Q+1)*a + Fr(6*q, 1000) + 7)/q
                    worst[D] = max(worst[D], b)
                dp = 2*E+4; degT = N*d/rho + d
                k = (2*(E+1)*d + 2*a*dp + 2*rho*degT)/q
                worst_k = max(worst_k, k); rows += 1
                n *= 2
print(f"grid rows: {rows} (r<=64, 2^7<=Q<=2^14, 2^6<=S<=2^12, all dyadic 256<=n<4Q)")
for D in [1, 2]:
    print(f"(1) D={D}: max FNAP-count bound/q = {float(worst[D]):.6f}  (< 1551/4000 = 0.38775: {worst[D] < THR})")
print(f"(2) max deg(kappa^2)/q = {float(worst_k):.6f}")
