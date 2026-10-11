# Exact recomputation of the v2 residual sharpening (N4):
#  (1) Cor 2.4 at n=256 infeasible for all r>=4,Q>=128,S>=64 (powers of 2): exact algebra + grid;
#  (2) with the strip condition n<4Q (n=h/E, all powers of 2), the least degree-feasible n is 512 and this needs Q>=256;
#      Q=128 has NO feasible strip scale;
#  (3) D-lanes: D=2^(s mod v) (Q=2^v, S=2^s, PRIMARY FNAP), D>=4, residual needs 512<=n<4D  =>  D>=256 => Q>=512 (D<Q),
#      and also S>=D>=256.
# Feasibility of F^2|a (Cor 2.4): exists integer M' with M' < 8h/625 = 8nE/625 and d' >= 2E-2 with M'+Q-T >= 2d', T=QS.
from fractions import Fraction as Fr
import math
def Mmax(n, E):            # largest integer M' < 8nE/625
    v = Fr(8*n*E, 625)
    return math.ceil(v) - 1
def feasible(r, Q, S, n):
    E = r*Q*S; T = Q*S
    return Mmax(n, E) + Q - T >= 2*(2*E - 2)
P2 = lambda a, b: [2**k for k in range(a, b+1)]
rs, Qs, Ss = P2(2, 12), P2(7, 20), P2(6, 20)
fail256 = [(r, Q, S) for r in rs for Q in Qs for S in Ss if feasible(r, Q, S, 256)]
print("grid |(r,Q,S)| =", len(rs)*len(Qs)*len(Ss), "; feasible at n=256 (exact set):", fail256)
# exact algebra: at n=256, M'+Q-T < 2048E/625 + Q - QS <= 2048E/625 < 4E-4 iff E > 625*4/452 = 625/113
print("threshold E > 625/113 =", Fr(625, 113), "; min E in strip = 4*128*64 =", 4*128*64)
least_ignoring = {}; least_strip = {}; Q128_strip = []; viol = []
for r in rs:
    for Q in Qs:
        for S in Ss:
            ns = P2(8, 40)
            fe = [n for n in ns if feasible(r, Q, S, n)]
            least_ignoring[(r, Q, S)] = min(fe) if fe else None
            fs = [n for n in ns if n < 4*Q and feasible(r, Q, S, n)]
            least_strip[(r, Q, S)] = min(fs) if fs else None
            if Q == 128 and fs: Q128_strip.append((r, Q, S, fs))
            if fs and Q < 256: viol.append((r, Q, S))
print("least feasible n ignoring n<4Q, distinct values:", sorted(set(least_ignoring.values()), key=lambda v: (v is None, v)))
print("least feasible n inside strip (n<4Q), distinct values:", sorted(set(least_strip.values()), key=lambda v: (v is None, v)))
print("Q=128 rows with a feasible strip scale (exact set):", Q128_strip)
print("rows with a feasible strip scale and Q<256 (exact set):", viol)
print("rows with Q>=256 and no feasible strip scale:", [k for k, v in least_strip.items() if k[1] >= 256 and v is None][:5])
# D-lanes
dl_viol = []; dl_rows = 0; dl_open = 0
for r in rs:
    for v in range(7, 21):
        for s in range(6, 21):
            Q, S = 2**v, 2**s; D = 2**(s % v)
            assert D < Q
            if D < 4: continue
            dl_rows += 1
            ns = [n for n in P2(8, 40) if n < 4*D and n < 4*Q and feasible(r, Q, S, n)]
            if ns:
                dl_open += 1
                if not (D >= 256 and Q >= 512 and S >= 256 and min(ns) >= 512): dl_viol.append((r, Q, S, D, ns[:3]))
print("D-lane rows (D>=4):", dl_rows, "; with a degree-feasible n<4D:", dl_open, "; violating D>=256, Q>=512, S>=256 (exact set):", dl_viol)
# purely arithmetic form: n power of 2, 512<=n<4D, D<Q powers of 2
ar = [(n, D, Q) for n in P2(9, 30) for D in P2(2, 30) for Q in P2(7, 31) if n < 4*D and D < Q and not (D >= 256 and Q >= 512)]
print("arithmetic: (n,D,Q) with 512<=n<4D, D<Q and not (D>=256,Q>=512):", ar)
ar2 = [(n, Q) for n in P2(9, 30) for Q in P2(7, 31) if n < 4*Q and Q < 256]
print("arithmetic: (n,Q) with n>=512, n<4Q, Q<256:", ar2)
