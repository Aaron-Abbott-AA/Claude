# Referee check c3: Prop 3.3 "Comparison" numbers and the dominant-term remark of Cor 4.2 (exact Fractions).
from fractions import Fraction as Fr
for r in [4, 8, 16]:
    for (Q, S) in [(128, 64), (1024, 256)]:
        for n in [256, 512, 1024]:
            if n >= 4*Q: continue
            E = r*Q*S; h = n*E; d = E+2; rho = Q//2; X = Q*S//2; dp = 2*E-2
            a = Fr(8*h, 625) - dp + X - rho; N = Fr(16*h, 625); Mp = Fr(8*h, 625)
            ratio = (a*dp/rho) / (N*d/rho + d)
            ratio2 = (a*(2*E+1)/rho) / (N*d/rho + d)
            dom = 2*r*(d-1)*a*dp/(dp-E) / (E*h)
            print(f"r={r} Q={Q} S={S} n={n}: a/E={float(a/E):.4f} M'/E={float(Mp/E):.4f} "
                  f"(K-height)/(a priori) at d'=2E-2: {float(ratio):.4f}, at d'=2E+1: {float(ratio2):.4f}; "
                  f"p-term/q={float(dom):.4f} vs 0.0512r={0.0512*r:.4f}")
