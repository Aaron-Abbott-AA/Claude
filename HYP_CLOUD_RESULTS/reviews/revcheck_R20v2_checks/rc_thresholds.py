# Revision-check (R20 v2): independent exact-Fraction recomputation of the Cor. 5.3 threshold table,
# written from the PRINTED formulas only:
#   R19 (4.1) [v2.1, incl. FIX-2 cusp-tangent term], optionally with the N4 term (R20 Prop. 5.2):
#     N*(d'-E-t+1) <= (d'-E)degpsi + 2r(d-1)(a d' - [N4] rho*qq*t) + [(E+1)(2g-2)+3d'] + d(2d'+2g-2) + 2d t
#                     + (d'-E)floor((2d'+2g-2)/(E-1)) + (d'-E-t+1)[Nd + 2t + (1.5d^2+3.5d+1) + 3d + 2degpsi + 6ddef + 7]
#     valid only for t <= d'-E.
#   R20 (4.1'):  N*D1 <= (d'-E)degpsi + 2r(d-1)(a d' - rho qq t) + [(E+1)(2g-2)+3d'] + d(2d'+2g-2)
#                     + (d'-E)floor((2d'+2g-2)/(E-1)) + 2d t + d(d'-1)(d'-2)/2
#                     + D1[Nd + 2t + (1.5d^2+3.5d+1) + 3d + 6ddef + 7 + Bfrak + (2d'+2g-2)],
#     D1 = d'-E-(a-m), m=min(rho qq, E), Bfrak = 2degpsi + 2(2a-d')d' + max(2g-2,0); needs D1>0.
# Normalisation (R19 Cor. 4.2): d=E+2, 2g-2=d(d-3), a=8h/625-d'+X-rho, N=16h/625, ddef=q/1000, degpsi=(E+1)d,
#   q=E*h, h=n*E, E=rQS, T=QS, X=T/2, rho=Q/2; excluded iff bound < 1551 q/4000;
#   t in [1, t_hi], t_hi = floor(min(a d'/(rho qq), (Nd/rho + d)/qq)); every d' in [2E-2, 2E+4]; dyadic 128<=qq<=E.
# The N-bound is concave quadratic in t for (4.1) and linear for (4.1'), so the "bad" t-set is found exactly
# by integer binary search on exact Fractions.  Run: python3 -I rc_thresholds.py
from fractions import Fraction as Fr
import math

THR = Fr(1551, 4000)

def params(r, Q, S, n, dp):
    E = r*Q*S; T = Q*S; X = Fr(T, 2); rho = Fr(Q, 2); h = n*E; q = E*h; d = E+2
    tg = d*(d-3)                       # 2g-2
    a = Fr(8*h, 625) - dp + X - rho
    N = Fr(16*h, 625); ddef = Fr(q, 1000); dpsi = (E+1)*d
    return dict(E=E, X=X, rho=rho, h=h, q=q, d=d, tg=tg, a=a, N=N, ddef=ddef, dpsi=dpsi, dp=dp, r=r)

def f41(P, qq, t, n4):
    # returns RHS - THR*q*coef  (negative <=> excluded at this t); requires t <= d'-E
    E, d, dp, tg, a = P['E'], P['d'], P['dp'], P['tg'], P['a']
    coef = dp - E - t + 1
    pterm = 2*P['r']*(d-1)*(a*dp - (P['rho']*qq*t if n4 else 0))
    rhs = ((dp-E)*P['dpsi'] + pterm + ((E+1)*tg + 3*dp) + d*(2*dp+tg) + 2*d*t
           + (dp-E)*((2*dp+tg)//(E-1))
           + coef*(P['N']*d + 2*t + (Fr(3, 2)*d*d + Fr(7, 2)*d + 1) + 3*d + 2*P['dpsi'] + 6*P['ddef'] + 7))
    return rhs - THR*P['q']*coef

def g41p(P, qq, t):
    E, d, dp, tg, a = P['E'], P['d'], P['dp'], P['tg'], P['a']
    m = min(P['rho']*qq, E)
    D1 = dp - E - (a - m)
    if D1 <= 0:
        return None
    Bf = 2*P['dpsi'] + 2*(2*a-dp)*dp + max(tg, 0)
    num = ((dp-E)*P['dpsi'] + 2*P['r']*(d-1)*(a*dp - P['rho']*qq*t) + ((E+1)*tg + 3*dp) + d*(2*dp+tg)
           + (dp-E)*((2*dp+tg)//(E-1)) + 2*d*t + Fr(d*(dp-1)*(dp-2), 2))
    exc = P['N']*d + 2*t + (Fr(3, 2)*d*d + Fr(7, 2)*d + 1) + 3*d + 6*P['ddef'] + 7 + Bf + (2*dp+tg)
    return num + D1*exc - THR*P['q']*D1

def interval_nonneg_concave(fn, lo, hi):
    """integers t in [lo,hi] with fn(t)>=0, fn concave in t -> an interval (or None)."""
    if lo > hi: return None
    # ternary-like search for an integer maximiser
    # concave: forward difference fn(t+1)-fn(t) is nonincreasing; find first t with difference <= 0
    a, b = lo, hi
    while a < b:
        mid = (a+b)//2
        if fn(mid+1) - fn(mid) > 0: a = mid+1
        else: b = mid
    best = a
    if fn(best) < 0: return None
    L, R = lo, best          # leftmost with fn>=0 (fn nondecreasing on [lo,best])
    while L < R:
        mid = (L+R)//2
        if fn(mid) >= 0: R = mid
        else: L = mid+1
    left = L
    L, R = best, hi
    while L < R:
        mid = (L+R+1)//2
        if fn(mid) >= 0: L = mid
        else: R = mid-1
    return (left, L)

def closed(r, Q, S, n, qq, mode):
    """mode: 'R19' (4.1) only; 'N4' (4.1)+N4; 'all' N4 union (4.1')."""
    for dp in range(2*r*Q*S-2, 2*r*Q*S+5):
        P = params(r, Q, S, n, dp)
        E, d = P['E'], P['d']
        a = P['a']
        thi = math.floor(min(a*dp/(P['rho']*qq), (P['N']*d/P['rho'] + d)/qq))
        if thi < 1: continue
        lim = min(thi, dp - E)
        # bad set for (4.1)[-N4]: t in [1,lim] with f>=0, plus (lim, thi] entirely
        n4 = mode in ('N4', 'all')
        I = interval_nonneg_concave(lambda t: f41(P, qq, t, n4), 1, lim)
        bad41 = []
        if I: bad41.append(I)
        if lim < thi: bad41.append((max(lim+1, 1), thi))
        if mode != 'all':
            if bad41: return False
            continue
        # (4.1') linear: bad set {g>=0} (or everything if D1<=0)
        if g41p(P, qq, 1) is None:
            badp = (1, thi)
        else:
            J = interval_nonneg_concave(lambda t: g41p(P, qq, t), 1, thi)
            badp = J
        if badp is None: continue
        for (l1, h1) in bad41:
            if max(l1, badp[0]) <= min(h1, badp[1]):
                return False
    return True

def least_q(r, Q, S, n, mode):
    E = r*Q*S
    qs = [2**k for k in range(7, int(math.log2(E))+1)]
    bits = [closed(r, Q, S, n, qq, mode) for qq in qs]
    # least dyadic qq from which all larger close
    least = None
    for i in range(len(qs)-1, -1, -1):
        if bits[i]: least = qs[i]
        else: break
    upward = all(bits[j] for j in range(len(qs)) if least is not None and qs[j] >= least) and \
             (least is None or all(not b for b, qq in zip(bits, qs) if qq < least) or True)
    # strict upward-closure test: once True, stays True
    first = next((i for i, b in enumerate(bits) if b), None)
    up_closed = first is None or all(bits[first:])
    return least, E, up_closed

def fmt(least, E):
    if least is None: return "none"
    return f"E/{E//least}" if least <= E else "?"

if __name__ == "__main__":
    # expected R20 patterns (printed Cor. 5.3), as least qq in units of E/Q (or E for n-dependent)
    def expected(r, Q, n):
        if r == 4:
            return Fr(2, Q) if n == 256 else Fr(n, 16*Q)
        if r == 8:
            if n == 256: return Fr(2, Q)
            if n == 512: return Fr(32, Q)
            if n == 1024: return Fr(64, Q) if Q >= 512 else None
            return None
        if r == 16:
            return Fr(8, Q) if n == 256 else None
    def expected_R19(r, Q, n):  # R19 Cor. 4.2 table (generic forms)
        if r == 4: return Fr(8, Q) if n == 256 else Fr(n, 8*Q)
        if r == 8:
            if n == 256: return Fr(16, Q)
            if n == 512: return Fr(128, Q)
            return None
        if r == 16:
            return Fr(512, Q) if (n == 256 and Q >= 512) else None
    rows = 0; mism = 0; mismR19 = 0; notup = 0
    import sys
    for r in (4, 8, 16):
        for Q in (128, 256, 512, 1024, 2048, 4096, 8192, 16384):
            for S in (64, 256):
                n = 256
                while n <= 2*Q:
                    E = r*Q*S
                    res = {}
                    for mode in ('R19', 'N4', 'all'):
                        least, _, up = least_q(r, Q, S, n, mode)
                        res[mode] = least; notup += (not up)
                    ex = expected(r, Q, n); exR = expected_R19(r, Q, n)
                    exq = None if ex is None else ex*E
                    exRq = None if exR is None else exR*E
                    # an expected value below 128 or above E is clipped
                    def clip(x):
                        if x is None or x > E: return None
                        return max(x, 128)
                    ok = (res['all'] == clip(exq)); okR = (res['R19'] == clip(exRq))
                    rows += 1; mism += (not ok); mismR19 += (not okR)
                    tag = "" if (ok and okR) else "   <-- MISMATCH"
                    print(f"r={r:2d} Q={Q:5d} S={S:3d} n={n:5d}: R19 {fmt(res['R19'],E):>9s}  N4 {fmt(res['N4'],E):>9s}  "
                          f"R20 {fmt(res['all'],E):>9s}   printed R20 {fmt(clip(exq),E):>9s}, R19 {fmt(clip(exRq),E):>9s}{tag}")
                    sys.stdout.flush()
                    n *= 2
    print(f"rows={rows}  mismatches vs printed R20 table: {mism}; vs R19 Cor 4.2 pattern: {mismR19}; non-upward-closed: {notup}")
