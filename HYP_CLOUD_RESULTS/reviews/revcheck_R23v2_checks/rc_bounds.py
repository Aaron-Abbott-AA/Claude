# Referee's own exact implementation of R19 (4.1) [N4 form, R20 Prop 5.2; R23 Prop 3.2(iii) N_1]
# and R20 Thm 5.1 (4.1'), with R20 Cor 5.3 normalisation.  Written from the note texts only.
# Polynomials in tau are built with exact Fractions and cleared to integer coefficients.
from fractions import Fraction as F
from math import isqrt

LAM = F(1551, 4000)

def cdiv(a, b): return -((-a)//b)

def setup(r, Q, S, n, dp, qq, mode):
    E = r*Q*S; rho = Q//2; X = rho*S; q = n*E*E; h = n*E
    d = E + 2; g22 = d*d - 3*d                 # 2g-2 <= d^2-3d
    a = F(8*h, 625) - dp + X - rho             # a_max (exact upper bound, not floored)
    N = F(16*h, 625); ddef = F(q, 1000); dpsi = (E+1)*d
    rq = rho*qq
    if mode == "R20":   m, N1 = min(rq, E), 1
    elif mode == "R23": m, N1 = E, max(1, cdiv(E, rq))
    elif mode == "R22ceil": m, N1 = min(rq*cdiv(E-X, rq), E), 1      # R22 Cor 3.2 as stated (ceiling form)
    elif mode == "EXplain": m, N1 = E - X, 1                          # literal 'm>=E-X', nothing else
    elif mode == "EXmax":   m, N1 = max(min(rq, E), E - X), 1         # R20's own m together with E-X
    else: raise ValueError(mode)
    tau_hi = (min(a*dp/rq, (N*d/rho + d)/qq)).__floor__()
    return dict(E=E, rho=rho, X=X, q=q, d=d, g22=g22, a=a, N=N, ddef=ddef, dpsi=dpsi, rq=rq,
                m=m, N1=N1, tau_hi=tau_hi, dp=dp, r=r)

def polys(P):
    """Return (pN4, cN4max, p41p or None): integer coefficient lists [c0,c1,c2] such that
       N4 holds at tau iff tau<=cN4max and pN4(tau)>0 ; (4.1') holds iff p41p(tau)>0."""
    E,rho,q,d,g22,a,N,ddef,dpsi,rq,m,N1,dp,r = (P[k] for k in
        "E rho q d g22 a N ddef dpsi rq m N1 dp r".split())
    cusp = (dp - E)*((2*dp + g22)//(E - 1))
    const_common = (dp - E)*dpsi + ((E+1)*g22 + 3*dp) + d*(2*dp + g22) + cusp
    # --- N4: L*(c - t) - [const + 2r(d-1)(a dp - rq t) + 2d t + (c - t)(Br0 + 2t)] > 0, c = dp-E+N1
    c = dp - E + N1
    Br0 = N*d + F(3*d*d + 7*d + 2, 2) + 3*d + 2*dpsi + 6*ddef + 7
    A0 = const_common + 2*r*(d-1)*a*dp
    # RHS(t) = A0 - 2r(d-1)rq t + 2d t + (c - t)(Br0 + 2t)
    #        = A0 + c*Br0 + t*(-2r(d-1)rq + 2d + 2c - Br0) + t^2*(-2)
    R0 = A0 + c*Br0; R1 = -2*r*(d-1)*rq + 2*d + 2*c - Br0; R2 = F(-2)
    L = LAM*q
    pN4 = [L*c - R0, -L - R1, -R2]
    # --- (4.1'): D1 = dp - E - (a - m) ; need D1>0
    D1 = dp - E - (a - m)
    p41 = None
    if D1 > 0:
        Bb = 2*dpsi + 2*(2*a - dp)*dp + max(g22, 0)
        Br1 = N*d + F(3*d*d + 7*d + 2, 2) + 3*d + 6*ddef + 7 + Bb + (2*dp + g22)
        S0 = const_common + 2*r*(d-1)*a*dp + d*(dp-1)*(dp-2)/F(2) + D1*Br1
        S1 = -2*r*(d-1)*rq + 2*d + 2*D1
        p41 = [L*D1 - S0, -S1, F(0)]
    def toint(p):
        den = 1
        for x in p: den = den*F(x).denominator//__import__('math').gcd(den, F(x).denominator)
        return [int(F(x)*den) for x in p]
    return toint(pN4), c - 1, (toint(p41) if p41 is not None else None)

def ev(p, t): return (p[2]*t + p[1])*t + p[0]

def pos_set(p, lo, hi):
    """Exact integer set {t in [lo,hi]: p(t)>0} as list of intervals (p degree<=2, integer coeffs)."""
    if lo > hi: return []
    crit = {lo, hi}
    c0, c1, c2 = p
    if c2 != 0:
        disc = c1*c1 - 4*c2*c0
        for sgn in (1, -1):
            if disc >= 0:
                s = isqrt(disc)
                for ss in (s, s+1):
                    num = -c1 + sgn*ss; den = 2*c2
                    x = num//den
                    for y in (x-1, x, x+1, x+2): crit.add(y)
        v = (-c1)//(2*c2)
        for y in (v-1, v, v+1, v+2): crit.add(y)
    elif c1 != 0:
        x = (-c0)//c1
        for y in (x-1, x, x+1, x+2): crit.add(y)
    pts = sorted(t for t in crit if lo <= t <= hi)
    out = []
    def add(a_, b_):
        if out and out[-1][1] == a_ - 1: out[-1] = (out[-1][0], b_)
        else: out.append((a_, b_))
    for i, t in enumerate(pts):
        if ev(p, t) > 0: add(t, t)
        if i + 1 < len(pts) and pts[i+1] > t + 1:
            a_, b_ = t + 1, pts[i+1] - 1
            mid = (a_ + b_)//2
            sa, sb, sm = ev(p, a_) > 0, ev(p, b_) > 0, ev(p, mid) > 0
            assert sa == sb == sm, ("non-constant sign in gap", a_, b_)
            if sa: add(a_, b_)
    return out

def subtract(intervals_all, goods):
    lo, hi = intervals_all
    res = [(lo, hi)]
    for (ga, gb) in goods:
        new = []
        for (x, y) in res:
            if gb < x or ga > y: new.append((x, y)); continue
            if x < ga: new.append((x, ga - 1))
            if gb < y: new.append((gb + 1, y))
        res = new
    return res

def failing(r, Q, S, n, dp, qq, mode):
    P = setup(r, Q, S, n, dp, qq, mode)
    th = P["tau_hi"]
    if th < 1: return [], P
    pN4, cmax, p41 = polys(P)
    goods = pos_set(pN4, 1, min(th, cmax))
    if p41 is not None: goods += pos_set(p41, 1, th)
    return subtract((1, th), goods), P
