# R20 v2 exact (Fraction) numerics [v2: FIX-8c: header comments corrected; computation identical to numerics_R20.py].  Run: python3 -I numerics_R20_v2.py
# Normalisation exactly as R19 Cor. 4.2 / numerics_K.py:
#   E=rQS, h=nE, q=E h, d=E+2, rho=Q/2, X=QS/2, a<=8h/625-d'+X-rho, N<16h/625,
#   deg psi<=(E+1)d, 2g-2<=d(d-3), d_def<=q/1000, d' in [2E-2,2E+4] (all 7 values scanned),
#   excluded iff bound/q < 1551/4000.
# (A) R19 (4.1) [with the FIX-2 cusp-tangent term], optionally with the N4 refinement (R20 Prop. 5.2)
#     2r(d-1)a d'  ->  2r(d-1)(a d' - rho*qq*tau)          (R19 Thm 4.1 Step 4, "not used" there)
#     valid for 1<=tau<=d'-E.
# (B) R20 Thm 5.1, (4.1'):  N_good*D1 <= NUM' + D1*EXC',  D1 = d'-E-(a-m), m=min(rho*qq,E),
#     NUM' = (d'-E)degpsi + 2r(d-1)(a d'-rho qq tau) + SV + KAP + CUSPT + 2d tau + d(d'-1)(d'-2)/2
#     EXC' = N d + 2tau + (1.5d^2+3.5d+1) + 3d + 6d_def + 7 + Bfrak + (2d'+2g-2),
#     Bfrak = 2degpsi + 2(2a-d')d' + max(2g-2,0)  [v2: FIX-4; the code uses 2g-2<=d(d-3)>=0].   Valid for every tau>=1, needs D1>0.
# (C) R20 Prop. 3.1 / Cor. 3.2 (constant T in (K) forces a>=d'): the code only checks a_max(d')<d' (no count is needed).
# Grid note [v2: FIX-8a]: Q runs over {128,256,512,1024,2048,4096,16384}; Q=8192 is omitted here (covered by the audit's ref_thresholds).
# tau ranges over 1..tau_hi, tau_hi=floor(min(a d'/(rho qq), (N d/rho + d)/qq))  (Prop 3.3 / R18 a priori).
from fractions import Fraction as Fr
from decimal import Decimal, getcontext
import math
getcontext().prec = 60
THR = Fr(1551, 4000)

def params(r, Q, S, n, dp):
    E = r*Q*S; h = n*E; q = E*h; d = E+2; rho = Q//2; X = Q*S//2
    a = Fr(8*h, 625) - dp + X - rho; N = Fr(16*h, 625); dpsi = (E+1)*d; g2 = d*(d-3)
    SV = (E+1)*g2 + 3*dp; KAP = d*(2*dp + g2); CUSPT = (dp-E)*((2*dp+g2)//(E-1))
    Ecal = Fr(3, 2)*d*d + Fr(7, 2)*d + 1; ddef = Fr(q, 1000)
    return dict(E=E, h=h, q=q, d=d, rho=rho, X=X, a=a, N=N, dpsi=dpsi, g2=g2, SV=SV, KAP=KAP,
                CUSPT=CUSPT, Ecal=Ecal, ddef=ddef, dp=dp, r=r)

def old_coeffs(P, qq, n4):
    """g(tau)=NUM(tau)+(EXC(tau)-THR q)(D-tau), D=d'-E+1; closed iff g<0 (tau<=D-1). Returns (A2,A1,A0)."""
    E, d, dp, r, rho, q = P['E'], P['d'], P['dp'], P['r'], P['rho'], P['q']
    num0 = (dp-E)*P['dpsi'] + 2*r*(d-1)*P['a']*dp + P['SV'] + P['KAP'] + P['CUSPT']
    s = (2*r*(d-1)*rho*qq if n4 else 0) - 2*d          # NUM(tau)=num0 - s tau
    C = P['N']*d + P['Ecal'] + 3*d + 2*P['dpsi'] + 6*P['ddef'] + 7 - THR*q   # EXC-THRq = C + 2 tau
    D = dp - E + 1
    # (C+2t)(D-t) = -2t^2 + (2D - C)t + C D
    return (Fr(-2), Fr(2*D) - C - s, num0 + C*D)

def new_coeffs(P, qq):
    E, d, dp, r, rho, q, a = P['E'], P['d'], P['dp'], P['r'], P['rho'], P['q'], P['a']
    m = min(rho*qq, E); D1 = dp - E - a + m
    if D1 <= 0: return None
    num0 = (dp-E)*P['dpsi'] + 2*r*(d-1)*a*dp + P['SV'] + P['KAP'] + P['CUSPT'] + Fr(d*(dp-1)*(dp-2), 2)
    s = 2*r*(d-1)*rho*qq - 2*d
    Bfrak = 2*P['dpsi'] + 2*(2*a-dp)*dp + P['g2']
    C = P['N']*d + P['Ecal'] + 3*d + 6*P['ddef'] + 7 + Bfrak + (2*dp + P['g2']) - THR*q
    # NUM0 - s t + D1 (C + 2t)
    return (Fr(0), 2*D1 - s, num0 + D1*C)

def ev(c, t): return (c[0]*t + c[1])*t + c[2]

def neg_set(c, lo, hi):
    """integer t in [lo,hi] with c0 t^2 + c1 t + c2 < 0, as list of closed intervals (exact)."""
    if lo > hi: return []
    A2, A1, A0 = c; bps = {lo, hi+1}
    def addroot(x):
        f = math.floor(x)
        for k in range(f-2, f+3):
            if lo <= k <= hi+1: bps.add(k)
    if A2 == 0:
        if A1 != 0:
            addroot(float(Decimal(-A0.numerator*A1.denominator)/Decimal(A0.denominator*A1.numerator)))
    else:
        disc = A1*A1 - 4*A2*A0
        if disc > 0:
            sd = (Decimal(disc.numerator)/Decimal(disc.denominator)).sqrt()
            a1 = Decimal(A1.numerator)/Decimal(A1.denominator); a2 = Decimal(A2.numerator)/Decimal(A2.denominator)
            for sg in (1, -1):
                addroot(float((-a1 + sg*sd)/(2*a2)))
    b = sorted(bps); out = []
    for i in range(len(b)-1):
        x, y = b[i], b[i+1]-1
        sx, sy = ev(c, x) < 0, ev(c, y) < 0
        assert sx == sy, "sign change inside a segment"
        if sx:
            if out and out[-1][1] == x-1: out[-1] = (out[-1][0], y)
            else: out.append((x, y))
    return out

def covered(intervals, lo, hi):
    cur = lo
    for (x, y) in sorted(intervals):
        if x > cur: break
        cur = max(cur, y+1)
    return cur > hi

def tau_hi(P, qq):
    v = min(P['a']*P['dp']/(P['rho']*qq), (P['N']*P['d']/P['rho'] + P['d'])/qq)
    return math.floor(v)

def status(r, Q, S, n, qq, mode):
    """True iff every d' and every tau in [1,tau_hi] is closed. mode in {'R19','N4','new','all'}."""
    E = r*Q*S
    for dp in range(2*E-2, 2*E+5):
        P = params(r, Q, S, n, dp); th = tau_hi(P, qq)
        if th < 1: continue
        iv = []
        if mode in ('R19', 'N4', 'all'):
            iv += neg_set(old_coeffs(P, qq, mode != 'R19'), 1, min(th, dp-E))
        if mode in ('new', 'all'):
            c = new_coeffs(P, qq)
            if c is not None: iv += neg_set(c, 1, th)
        if not covered(iv, 1, th): return False
    return True

def thresholds(r, Q, S, n, mode):
    E = r*Q*S; qs = []; qq = 128
    while qq <= E: qs.append(qq); qq *= 2
    st = [status(r, Q, S, n, x, mode) for x in qs]
    # least qq0 such that all qq>=qq0 closed
    least = None
    for i in range(len(qs)-1, -1, -1):
        if st[i]: least = qs[i]
        else: break
    return least, st, qs

def fmt(x, E):
    if x is None: return "none"
    return f"E/{E//x}" if x <= E and E % x == 0 and x < E else ("E" if x == E else str(x))

def bound_old(P, qq, t, n4):
    E, d, dp, r, rho, q = P['E'], P['d'], P['dp'], P['r'], P['rho'], P['q']
    num = (dp-E)*P['dpsi'] + 2*r*(d-1)*(P['a']*dp - (rho*qq*t if n4 else 0)) + P['SV'] + P['KAP'] + P['CUSPT'] + 2*d*t
    exc = P['N']*d + 2*t + P['Ecal'] + 3*d + 2*P['dpsi'] + 6*P['ddef'] + 7
    return (num/(dp-E-t+1) + exc)/q

def bound_new(P, qq, t):
    E, d, dp, r, rho, q, a = P['E'], P['d'], P['dp'], P['r'], P['rho'], P['q'], P['a']
    m = min(rho*qq, E); D1 = dp - E - a + m
    num = (dp-E)*P['dpsi'] + 2*r*(d-1)*(a*dp - rho*qq*t) + P['SV'] + P['KAP'] + P['CUSPT'] + 2*d*t + Fr(d*(dp-1)*(dp-2), 2)
    Bf = 2*P['dpsi'] + 2*(2*a-dp)*dp + P['g2']
    exc = P['N']*d + 2*t + P['Ecal'] + 3*d + 6*P['ddef'] + 7 + Bf + (2*dp + P['g2'])
    return (num/D1 + exc)/q

def spot_check(trials=40, per=60):
    rnd = __import__('random').Random(7); bad = 0; tot = 0
    for _ in range(trials):
        r = rnd.choice([4, 8, 16]); Q = rnd.choice([128, 256, 1024]); S = rnd.choice([64, 256])
        n = rnd.choice([n for n in [256, 512, 1024] if n < 4*Q]); E = r*Q*S
        dp = rnd.randrange(2*E-2, 2*E+5); qq = 128*2**rnd.randrange(0, (E//128).bit_length())
        P = params(r, Q, S, n, dp); th = tau_hi(P, qq)
        if th < 1: continue
        n4 = rnd.random() < 0.5
        iv_o = neg_set(old_coeffs(P, qq, n4), 1, min(th, dp-E))
        c = new_coeffs(P, qq); iv_n = neg_set(c, 1, th) if c is not None else []
        ts = {1, th, min(th, dp-E)} | {rnd.randrange(1, th+1) for _ in range(per)}
        for (x, y) in iv_o + iv_n: ts |= {x, y, max(1, x-1), min(th, y+1)}
        for t in ts:
            tot += 1
            ino = any(x <= t <= y for (x, y) in iv_o); inn = any(x <= t <= y for (x, y) in iv_n)
            do = (t <= dp-E) and bound_old(P, qq, t, n4) < THR
            dn = (c is not None) and bound_new(P, qq, t) < THR
            bad += (ino != do) + (inn != dn)
    return bad, tot

if __name__ == "__main__":
    b, t = spot_check()
    print(f"== self-check: interval solver vs direct exact evaluation: {b} mismatches in {t} (tau,case) pairs ==")
    print()
    print("== (C) Prop. 3.1: (K) with constant T needs a>=d'.  Check a_max(d')<d' for all d' in [2E-2,2E+4] at n=256 ==")
    for r in [4, 8, 16]:
        for Q in [128, 256, 1024, 4096, 16384]:
            for S in [64, 256]:
                E = r*Q*S; n = 256
                worst = max(params(r, Q, S, n, dp)['a']/dp for dp in range(2*E-2, 2*E+5))
                print(f"r={r:<2} Q={Q:<5} S={S:<3}  max_d' a_max/d' = {float(worst):.5f}  (<1: constant-T (K) impossible) {worst < 1}")
    for r in [4, 8, 16]:
        E = r*128*64
        nn = [n for n in [256, 512] if all(params(r, 128, 64, n, dp)['a'] < dp for dp in range(2*E-2, 2*E+5))]
        print(f"r={r}: dyadic n in {{256,512}} with a_max<d' (Q=128,S=64): {nn}")
    print()
    print("== D1 = d'-E-(a-m) at m=E (n=256, d'=2E-2): (4.1') applicable only where D1>0 ==")
    for r in [4, 8, 16]:
        for n in [256, 512]:
            Q, S = 128, 64; P = params(r, Q, S, n, 2*r*Q*S-2)
            print(f"r={r:<2} n={n}: (a_max-E)/E={float((P['a']-P['E'])/P['E']):.4f}  D1/E={float((P['dp']-P['a'])/P['E']):.4f}")
    print()
    print("== least dyadic qq (128<=qq<=E) from which ALL larger dyadic qq close, (K) non-constant T ==")
    print("   modes: R19 = (4.1) as in R19 (per-d' exact); N4 = (4.1) with the N4 p-term; all = N4 or (4.1')")
    print(f"{'r':<3}{'Q':<6}{'S':<5}{'n':<6}{'R19':<10}{'N4':<10}{'all':<10} closed-set over qq=128..E (all mode)")
    for r in [4, 8, 16]:
        for Q in [128, 256, 512, 1024, 2048, 4096, 16384]:
            for S in [64, 256]:
                for n in [256, 512, 1024, 2048, 4096, 8192]:
                    if n >= 4*Q: continue
                    E = r*Q*S
                    res = {}
                    for mode in ['R19', 'N4', 'all']:
                        res[mode] = thresholds(r, Q, S, n, mode)
                    st = ''.join('1' if b else '0' for b in res['all'][1])
                    print(f"{r:<3}{Q:<6}{S:<5}{n:<6}{fmt(res['R19'][0],E):<10}{fmt(res['N4'][0],E):<10}{fmt(res['all'][0],E):<10} {st}")
