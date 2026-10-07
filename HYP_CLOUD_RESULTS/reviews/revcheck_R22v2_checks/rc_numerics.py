# rc_numerics.py -- revision check of R22 v2 numbers (independent of numerics_R22.py; formulas re-typed from
# the printed statements of Cor 4.1, Cor 4.2, Thm 5.3(i),(ii), Prop 5.5 (pencil, classical dim 4/3) in v2).
# Exact Fractions. Checks: corner values, FIX-6 round-ups >= exact, Cor 5.4 thresholds, grid max + monotonicity.
from fractions import Fraction as Fr
import itertools
T = Fr(1551, 4000)

def bounds(r, Q, S, n, qq=128):
    E = r*Q*S; q = n*E*E; h = n*E
    d = E + 2; dp = 2*E + 4
    N = Fr(16*h, 625); a = Fr(8*h, 625); Mp = Fr(8*h, 625)      # N<16h/625, a,M'<8h/625
    rho = Fr(Q, 2); X = Fr(Q*S, 2)
    Ex = Fr(3, 2)*d*d + Fr(7, 2)*d + 1
    bnd = 6*Fr(q, 1000) + 7                                      # boundary 6 d_def + 7
    psi = (E+1)*d                                                # deg psi
    degT = N*d/rho + d                                           # R18 §5
    rdegT = N*d + rho*d                                          # rho deg[T]
    g22 = d*d - 3*d                                              # 2g-2
    tau0 = degT/qq
    c41 = N*d + Ex + 2*psi + (Q+1)*a*dp/(X-rho) + bnd
    c42 = N*d + Ex + psi + (Q+1)*Mp*dp/rho + bnd                 # M'+Q-T-d' < M'
    ch = N*d + 2*degT/qq + Ex + bnd
    t53i = ch + (2*psi + 2*a*dp + 2*rdegT)                       # deg dd^2
    t53ii = ch + psi + a*dp + rdegT + g22 + 2*psi
    pen = ch + 2*psi + (1*g22 + 2*tau0)/1                        # eps=(0,1), N0-1>=1
    cl4 = ch + 2*psi + (6*g22 + 4*tau0)/1                        # eps=(0,1,2,3), N0-3>=1
    cl3 = ch + 2*psi + (3*g22 + 3*tau0)/2                        # eps=(0,1,2), N0-2>=2
    return [x/q for x in (c41, c42, t53i, t53ii, cl4, pen, cl3)]

names = ["Cor4.1", "Cor4.2", "Thm5.3(i)", "Thm5.3(ii)", "Prop5.5 classical(dim4)", "Prop5.5 pencil", "Prop5.5 classical(dim3)"]
printed_v2 = [Fr("0.046095"), Fr("0.092972"), Fr("0.147704"), Fr("0.104306"), Fr("0.068733"), Fr("0.049195"), None]
printed_v1 = [Fr("0.046095"), Fr("0.092972"), Fr("0.147703"), Fr("0.104305"), Fr("0.068732"), Fr("0.049194"), None]
owner_exact = ["33259609702489/721554505728000", "3194487655227/34359738368000", "32480243592761/219902325555200",
               "114684856407837/1099511627776000", "75571916082327/1099511627776000", "27044774933549/549755813888000", None]
c = bounds(4, 128, 64, 256)
print("== corner (r,Q,S,n)=(4,128,64,256) ==")
for i, nm in enumerate(names):
    line = f"{nm}: exact={c[i]} = {float(c[i]):.10f}"
    if owner_exact[i]:
        line += f" | owner fraction match: {c[i] == Fr(owner_exact[i])}"
    if printed_v2[i] is not None:
        line += f" | v2 printed {float(printed_v2[i])} >= exact: {printed_v2[i] >= c[i]} | v1 printed {float(printed_v1[i])} >= exact: {printed_v1[i] >= c[i]}"
    print(line)
print("0.046094 (Sec0 COMPUTED line / Sec7 truncation) >= exact Cor4.1:", Fr("0.046094") >= c[0])
print("== Cor 5.4 thresholds ==")
for i, lab, pr in ((2, "(R1)", "0.240047"), (3, "(K_psi)\\(K)", "0.283445")):
    th = T - c[i]
    print(f"{lab}: exact threshold 1551/4000 - max = {float(th):.10f}; printed {pr} <= exact: {Fr(pr) <= th}; "
          f"formula with 6-8 digit rounded-up max gives {float(T - Fr(['0.14770305','0.10430527'][i-2])):.10f} <= exact: {T - Fr(['0.14770305','0.10430527'][i-2]) <= th}")
print("== grid: r in 4..128, Q in 2^7..2^14, S in 2^6..2^13, dyadic n in [256,4Q) ==")
grid = {}
for r in (4, 8, 16, 32, 64, 128):
    for Q in [1 << v for v in range(7, 15)]:
        for S in [1 << s for s in range(6, 14)]:
            n = 256
            while n < 4*Q:
                grid[(r, Q, S, n)] = bounds(r, Q, S, n)
                n *= 2
mx = [max(v[i] for v in grid.values()) for i in range(7)]
arg = [[k for k, v in grid.items() if v[i] == mx[i]] for i in range(7)]
print("rows:", len(grid))
for i in range(7):
    print(f"{names[i]}: max={float(mx[i]):.10f} at {arg[i]}; equals corner: {mx[i] == c[i]}; < 1551/4000: {mx[i] < T}")
viol = 0; comps = 0
for k, v in grid.items():
    r, Q, S, n = k
    for k2 in ((2*r, Q, S, n), (r, 2*Q, S, n), (r, Q, 2*S, n), (r, Q, S, 2*n)):
        if k2 in grid:
            for i in range(7):
                comps += 1
                if grid[k2][i] > v[i]:
                    viol += 1
print("monotonicity under doubling: comparisons", comps, "violations", viol)
# Prop 5.5 / closure: with qq maximal, qq<=S implies N0=ceil((2r-1)S/qq)>=2r-1>=7
print("closure dichotomy: for qq<=S, N0 >= 2r-1 >= 7 >= 2 for every r>=4:", all((2*r-1) >= 2 for r in (4, 8, 16, 32, 64, 128)))
