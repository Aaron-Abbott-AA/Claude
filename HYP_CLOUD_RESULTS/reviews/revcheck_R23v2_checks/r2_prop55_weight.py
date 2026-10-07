# Check of v2 §3 'Residual of (R2)' new sentence: "For eps_top<N_1 the weight N_1-eps_top is >=1, so
# R22 Prop 5.5's count is automatic there as well."  N_1=2rS/qq_max is a power of 2.
# (a) weight>=1 alone: worst term Sigma/(weight) with only Sigma<=2 eps_top, eps_top<=N_1-1.
# (b) with the p-adic structure (Lemma 4.3(i)): max of Sigma eps_i/(N_1-eps_top) over closed sequences.
# (c) the resulting whole-strip bound with R22 Prop 5.5 / Thm 5.3 charges, exact Fractions at the corner,
#     and on a grid (r,Q,S,n,qq_max) with N_1>=2.
from fractions import Fraction as F
from itertools import combinations

def subints(x):
    bits = [1 << i for i in range(x.bit_length()) if x >> i & 1]
    out = set()
    for k in range(len(bits)+1):
        for c in combinations(bits, k): out.add(sum(c))
    return out

CAP = 2**13
# closed sequences of length <=4 containing 0 and 1 (eps_1=1, separable), entries <= CAP
cands = [x for x in range(2, CAP+1) if bin(x).count("1") <= 2]
seqs = [(0, 1)]
for a in cands:
    s = {0, 1, a}
    if all(subints(e) <= s for e in s): seqs.append((0, 1, a))
    for b in cands:
        if b <= a: continue
        s = {0, 1, a, b}
        if all(subints(e) <= s for e in s): seqs.append((0, 1, a, b))
print("closed sequences with eps_1=1, entries<=2^13:", len(seqs))
worst = {}
for j in range(1, 14):
    N1 = 2**j; best = None
    for s in seqs:
        if s[-1] < N1:
            rat = F(sum(s), N1 - s[-1])
            if best is None or rat > best[0]: best = (rat, s)
    worst[N1] = best
    print(f"N_1=2^{j}: max Sigma/(N_1-eps_top) = {best[0]} at {best[1]};  weight>=1-only worst 2(N_1-1) = {2*(N1-1)}")
RAT = max(v[0] for v in worst.values())
print("overall max ratio with p-adic structure:", RAT)

LAM = F(1551, 4000)
def bound_over_q(r, Q, S, n, qqmax, ratio):
    E = r*Q*S; rho = Q//2; q = n*E*E; h = n*E; d = E+2; g22 = d*d - 3*d
    N = F(16*h, 625); dpsi = (E+1)*d; ddef = F(q, 1000)
    tau_hi = (N*d/rho + d)/qqmax
    charges = N*d + 2*tau_hi + F(3*d*d+7*d+2, 2) + 6*ddef + 7
    return (charges + 2*dpsi + ratio*g22 + 4*tau_hi) / q   # weight>=1 on the tau term

c = bound_over_q(4, 128, 64, 256, 128, RAT)
print("corner (4,128,64,256,qq_max=128) bound/q with p-adic ratio:", float(c), "<1551/4000:", c < LAM)
mx = F(0); bad_w1 = 0; tot = 0
for r in (4, 8, 16, 32, 64):
    for Q in [2**k for k in range(7, 15)]:
        for S in [2**k for k in range(6, 13)]:
            n = 256
            while n < 4*Q:
                for qqe in range(7, 40):
                    qq = 2**qqe; N1 = 2*r*S//qq if qq <= 2*r*S else 1
                    if N1 < 2: break
                    tot += 1
                    b = bound_over_q(r, Q, S, n, qq, RAT); mx = max(mx, b)
                    b1 = bound_over_q(r, Q, S, n, qq, 2*(N1-1))
                    if b1 >= LAM: bad_w1 += 1
                n *= 2
print(f"grid cases {tot}: max bound/q with p-adic ratio = {float(mx):.6f} (<0.38775: {mx < LAM});"
      f" cases NOT closed using only 'weight>=1' (ratio 2(N_1-1)): {bad_w1}")
