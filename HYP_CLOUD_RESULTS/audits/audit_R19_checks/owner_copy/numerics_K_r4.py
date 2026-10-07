# Exact evaluation (Fractions) of the kernel-aligned bound, Theorem 4.4 of NOTE_CORRESPONDENCE_ROUTE.md:
#  N_good <= [ (d'-E)degpsi + 2r(d-1)a d' + SV + KAP + 2 d tau ] / (d'-E-tau+1)
#            + N d + 2 tau + (1.5d^2+3.5d+1) + 3d + 2 degpsi + 6 d_def + 7,
#  degpsi<=(E+1)d, SV=(E+1)d(d-3)+3d', KAP=d(2d'+d(d-3)), a<=8h/625-d'+X-rho (a<M'), N<16h/625, d_def<=q/1000.
# Excluded iff bound < 1551 q/4000.  tau=deg T / qq.  Output: tau_max/E, and the least qq for which the
# K-height bound tau<=a d'/(rho qq) (Prop 4.2) or the a-priori bound tau<=(N d/rho+d)/qq gives tau<=tau_max.
from fractions import Fraction as Fr
def bound(r, Q, S, n, dp, tau):
    E = r*Q*S; h = n*E; q = E*h; d = E+2; rho = Q//2; X = Q*S//2
    a = Fr(8*h, 625) - dp + X - rho; N = Fr(16*h, 625); dpsi = (E+1)*d
    if dp - E - tau + 1 <= 0: return None, a
    SV = (E+1)*d*(d-3) + 3*dp; KAP = d*(2*dp + d*(d-3))
    main = Fr((dp-E)*dpsi + 2*r*(d-1)*a*dp + SV + KAP + 2*d*tau, dp-E-tau+1)
    exc = N*d + 2*tau + Fr(3, 2)*d*d + Fr(7, 2)*d + 1 + 3*d + 2*dpsi + Fr(6*q, 1000) + 7
    return (main+exc)/q, a
def tau_max(r, Q, S, n):
    E = r*Q*S; worst = None
    for dp in [2*E-2, 2*E, 2*E+4]:
        lo, hi = 0, dp-E          # largest tau with bound < 1551/4000
        b0, _ = bound(r, Q, S, n, dp, 1)
        if b0 is None or b0 >= Fr(1551, 4000): return 0, b0
        while lo < hi:
            mid = (lo+hi+1)//2; b, _ = bound(r, Q, S, n, dp, mid)
            if b is not None and b < Fr(1551, 4000): lo = mid
            else: hi = mid-1
        worst = lo if worst is None else min(worst, lo)
    return worst, b0
print("r   Q    S    n      bound(tau=1)  tau_max/E   least qq (K-height)  least qq (a priori)   [qq dyadic, <=E]")
for r in [4]:
    for Q in [512, 1024, 4096]:
        for S in [64]:
            E = r*Q*S
            for n in [1024, 2048, 4096, 8192]:
                if n >= 4*Q: continue
                tm, b0 = tau_max(r, Q, S, n)
                if tm == 0:
                    print(f"{r:<3} {Q:<4} {S:<4} {n:<6} {float(b0):.4f}       fails at tau=1"); continue
                h = n*E; rho = Q//2; d = E+2
                aK = max(Fr(8*h, 625) - dp + Q*S//2 - rho for dp in [2*E-2]) ; dpm = 2*E+4
                def least(fn):
                    qq = 1
                    while qq <= E and fn(qq) > tm: qq *= 2
                    return qq if qq <= E else None
                qK = least(lambda qq: aK*dpm/(rho*qq)); qA = least(lambda qq: (Fr(16*h, 625)*d/rho + d)/qq)
                fmt = lambda x: "none<=E" if x is None else f"2^{x.bit_length()-1} (={Fr(x, E)}E)"
                print(f"{r:<3} {Q:<4} {S:<4} {n:<6} {float(b0):.4f}       {tm/E:.4f}      {fmt(qK):<20} {fmt(qA)}")
