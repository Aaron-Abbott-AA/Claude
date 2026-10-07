# Referee check D (R21 Cor. 2.2 and Lemma 3.2(iii) numerics), exact Fractions, written independently.
# FNAP count (2) with D in {1,2}:  N_good <= N d + (D+2)(E+1)d + (Q+1)a + 6 d_def + 7,
#   normalisation (FNAN Sec. 3): N < 16h/625, a < 8h/625, d <= E+2, d_def <= q/1000, q = E h, h = nE, E = rQS.
# Each term /q is non-increasing in r, Q, S, n (shown term-by-term below), so the supremum over the whole
# strip (r>=4, Q>=128, S>=64, n>=256) is the value at (r,Q,S,n)=(4,128,64,256).  In the D in {1,2} lane S=Q^j D
# with j>=1, so S>=Q>=128; the lane supremum is at (4,128,128,256) for D=1 and (4,128,256,256) for D=2.
# Lemma 3.2(iii): deg kappa^2 = 2 deg psi + 2 a d' + 2 rho deg[T] <= 2(E+1)d + 2 a d' + 2(N d + rho d),
#   d' <= 2E+4 (owner; R19 Remark 1.7 gives d' <= 2E+1).
# Run: python3 -I D_numerics_exact.py
from fractions import Fraction as Fr

def count_bound(r, Q, S, n, D):
    E = r*Q*S; h = n*E; q = E*h; d = E+2
    N = Fr(16*h, 625); a = Fr(8*h, 625)
    return (N*d + (D+2)*(E+1)*d + (Q+1)*a + Fr(6, 1000)*q + 7)/q

def kappa_bound(r, Q, S, n, dp_extra=4):
    E = r*Q*S; h = n*E; q = E*h; d = E+2; rho = Q//2
    N = Fr(16*h, 625); a = Fr(8*h, 625); dp = 2*E+dp_extra
    return (2*(E+1)*d + 2*a*dp + 2*(N*d + rho*d))/q

THR = Fr(1551, 4000)
# (1) reproduce the owner grid maxima
worst = {1: Fr(0), 2: Fr(0)}; wk = Fr(0); rows = 0; arg = {}
for r in [4, 8, 16, 32, 64]:
    for Q in [2**v for v in range(7, 15)]:
        for S in [2**s for s in range(6, 13)]:
            n = 256
            while n < 4*Q:
                for D in (1, 2):
                    b = count_bound(r, Q, S, n, D)
                    if b > worst[D]: worst[D] = b; arg[D] = (r, Q, S, n)
                k = kappa_bound(r, Q, S, n)
                if k > wk: wk = k; arg['k'] = (r, Q, S, n)
                rows += 1; n *= 2
print("owner grid rows:", rows)
for D in (1, 2):
    print(f"D={D}: grid max bound/q = {float(worst[D]):.8f} at (r,Q,S,n)={arg[D]}; exact = {worst[D]}; < 1551/4000: {worst[D] < THR}")
print(f"kappa^2: grid max deg/q = {float(wk):.8f} at {arg['k']}; exact = {wk}")
print(f"   <= 0.1102 ? {wk <= Fr(1102, 10000)}   <= 0.11 ? {wk <= Fr(11, 100)}   <= 0.1103 ? {wk <= Fr(1103, 10000)}")
# (2) monotonicity: compare each corner value with neighbours in every direction (sampled far beyond the grid)
import itertools
mono_ok = True
for (r, Q, S, n) in itertools.product([4, 5, 8, 64, 1024], [128, 2**10, 2**20], [64, 128, 2**15], [256, 300, 2**12]):
    if n >= 4*Q: continue
    for D in (1, 2):
        b = count_bound(r, Q, S, n, D)
        for (r2, Q2, S2, n2) in [(r+1, Q, S, n), (r, 2*Q, S, n), (r, Q, 2*S, n), (r, Q, S, n+1)]:
            if count_bound(r2, Q2, S2, n2, D) > b: mono_ok = False
    k = kappa_bound(r, Q, S, n)
    for (r2, Q2, S2, n2) in [(r+1, Q, S, n), (r, 2*Q, S, n), (r, Q, 2*S, n), (r, Q, S, n+1)]:
        if kappa_bound(r2, Q2, S2, n2) > k: mono_ok = False
print("monotone non-increasing in r, Q, S, n on sampled points (incl. non-dyadic r, n):", mono_ok)
# (3) whole-strip supremum and D-lane supremum
for D in (1, 2):
    sup_all = count_bound(4, 128, 64, 256, D)
    sup_lane = count_bound(4, 128, 128*D, 256, D)
    print(f"D={D}: sup over whole strip (S>=64) = {float(sup_all):.8f}; over the D-lane (S=Q^j D>=Q) = {float(sup_lane):.8f}; margin to 1551/4000 = {float(THR - sup_all):.6f}")
# closed form at the corner: (16/625)(1+2/E) + (D+2)/n (1+1/E)(1+2/E) + 8(Q+1)/(625 E) + 6/1000 + 7/q
E = 4*128*64; n = 256
for D in (1, 2):
    cf = Fr(16, 625)*(1+Fr(2, E)) + Fr(D+2, n)*(1+Fr(1, E))*(1+Fr(2, E)) + Fr(8*129, 625*E) + Fr(6, 1000) + Fr(7, E*n*E)
    print(f"D={D}: closed form at corner equals computed value: {cf == count_bound(4, 128, 64, 256, D)}")
print(f"kappa^2 sup (whole strip, d'<=2E+4) = {float(kappa_bound(4,128,64,256)):.8f}; with d'<=2E+1: {float(kappa_bound(4,128,64,256,1)):.8f}")
