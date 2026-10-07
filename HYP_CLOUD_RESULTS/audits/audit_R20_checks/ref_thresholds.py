# Referee R20: independent exact (Fraction) evaluation of R19 (4.1), (4.1)+N4 (R20 Prop 5.2) and
# R20 (4.1') (Thm 5.1), written from the PRINTED formulas of R19 v2.1 Thm 4.1 / R20 Thm 5.1 and the
# normalisation of R19 Cor 4.2 / R20 Cor 5.3.  Does NOT import or copy the owner code.
# Run: python3 -I ref_thresholds.py [mode]
# Method: for each (r,Q,S,n,d',qq) the set of integer tau in [1,tau_hi] NOT closed by a bound is computed
# exactly: (4.1)-type g(tau) is a concave quadratic (leading coeff -2), (4.1') is linear; integer
# boundaries are located by exact binary search on the sign of g (no floating point).
import sys
from fractions import Fraction as Fr

THR = Fr(1551, 4000)

def base(r, Q, S, n, dp):
    E = r*Q*S; h = n*E; q = E*h; d = E + 2; rho = Q//2; X = Q*S//2
    a = Fr(8*h, 625) - dp + X - rho          # a <= 8h/625 - d' + X - rho  (worst case, used everywhere)
    N = Fr(16*h, 625)                         # N < 16h/625
    dpsi = (E+1)*d                            # deg psi <= (E+1)d
    G2 = d*(d-3)                              # 2g-2 <= d(d-3)
    ddef = Fr(q, 1000)
    Ecal = Fr(3, 2)*d*d + Fr(7, 2)*d + 1
    return E, h, q, d, rho, X, a, N, dpsi, G2, ddef, Ecal

def g41(r, Q, S, n, dp, qq, tau, n4):
    """R19 (4.1) [v2.1, incl. FIX-2 cusp-tangent term]; n4=True: p-term 2r(d-1)(a d' - rho*qq*tau).
       Returns RHS - THR*q*coef  (closed iff < 0).  Valid only for 1<=tau<=d'-E."""
    E, h, q, d, rho, X, a, N, dpsi, G2, ddef, Ecal = base(r, Q, S, n, dp)
    coef = dp - E - tau + 1
    P = a*dp - (rho*qq*tau if n4 else 0)
    num = ((dp-E)*dpsi + 2*r*(d-1)*P + ((E+1)*G2 + 3*dp) + d*(2*dp + G2) + 2*d*tau
           + (dp-E)*((2*dp + G2)//(E-1)))
    exc = N*d + 2*tau + Ecal + 3*d + 2*dpsi + 6*ddef + 7
    return num + coef*exc - THR*q*coef

def g41p(r, Q, S, n, dp, qq, tau):
    """R20 (4.1'): N_good*D1 <= NUM' + D1*EXC'. Returns NUM' + D1*EXC' - THR*q*D1, or None if D1<=0."""
    E, h, q, d, rho, X, a, N, dpsi, G2, ddef, Ecal = base(r, Q, S, n, dp)
    m = min(rho*qq, E)
    D1 = dp - E - (a - m)
    if D1 <= 0: return None
    num = ((dp-E)*dpsi + 2*r*(d-1)*(a*dp - rho*qq*tau) + ((E+1)*G2 + 3*dp) + d*(2*dp + G2)
           + (dp-E)*((2*dp + G2)//(E-1)) + 2*d*tau + Fr(d*(dp-1)*(dp-2), 2))
    Bfr = 2*dpsi + 2*(2*a - dp)*dp + G2
    exc = N*d + 2*tau + Ecal + 3*d + 6*ddef + 7 + Bfr + (2*dp + G2)
    return num + D1*exc - THR*q*D1

def tau_hi(r, Q, S, n, dp, qq):
    E, h, q, d, rho, X, a, N, dpsi, G2, ddef, Ecal = base(r, Q, S, n, dp)
    v = min(a*dp/(rho*qq), (N*d/rho + d)/qq)
    return v.numerator // v.denominator

def nonneg_interval_concave(f, lo, hi):
    """f concave on integers [lo,hi]; return (x,y) integer interval where f>=0 (or None)."""
    if lo > hi: return None
    # ternary-free: find the integer maximiser by binary search on f(t+1)-f(t) (decreasing for concave)
    L, R = lo, hi
    while L < R:
        mid = (L + R)//2
        if f(mid+1) > f(mid): L = mid + 1
        else: R = mid
    t0 = L
    if f(t0) < 0: return None
    # left boundary: smallest t in [lo,t0] with f(t)>=0 (f nondecreasing there)
    L, R = lo, t0
    while L < R:
        mid = (L + R)//2
        if f(mid) >= 0: R = mid
        else: L = mid + 1
    x = L
    L, R = t0, hi
    while L < R:
        mid = (L + R + 1)//2
        if f(mid) >= 0: L = mid
        else: R = mid - 1
    return (x, L)

def closed(r, Q, S, n, qq, mode):
    """mode: 'R19' (4.1) only; 'N4' (4.1)+N4 only; 'new' (4.1') only; 'all' = N4 or (4.1')."""
    E = r*Q*S
    for dp in range(2*E-2, 2*E+5):
        th = tau_hi(r, Q, S, n, dp, qq)
        if th < 1: continue
        # uncovered pieces by the old bound
        unc = []
        if mode in ('R19', 'N4', 'all'):
            top = min(th, dp - E)
            iv = nonneg_interval_concave(lambda t: g41(r, Q, S, n, dp, qq, t, mode != 'R19'), 1, top)
            if iv: unc.append(iv)
            if th > top: unc.append((top+1, th))
        else:
            unc.append((1, th))
        if not unc: continue
        if mode in ('new', 'all'):
            if g41p(r, Q, S, n, dp, qq, 1) is None: return False
            f = lambda t: g41p(r, Q, S, n, dp, qq, t)   # linear: closed set is an interval
            for (x, y) in unc:
                if not (f(x) < 0 and f(y) < 0): return False
        else:
            return False
    return True

def qq_list(E):
    out = []; x = 128
    while x <= E: out.append(x); x *= 2
    return out

def threshold(r, Q, S, n, mode):
    E = r*Q*S; qs = qq_list(E); st = [closed(r, Q, S, n, x, mode) for x in qs]
    least = None
    for i in range(len(qs)-1, -1, -1):
        if st[i]: least = qs[i]
        else: break
    upward = all(st[i] <= st[i+1] for i in range(len(st)-1))
    return least, upward, ''.join('1' if b else '0' for b in st)

def fmt(x, E):
    if x is None: return 'none'
    return 'E' if x == E else f'E/{E//x}'

def predicted(r, Q, n):
    """R20 Cor 5.3 printed claims (as multiples c with qq0 = c*E/Q); None = 'none'."""
    if r == 4:
        return 2 if n == 256 else Fr(n, 16)
    if r == 8:
        return {256: 2, 512: 32, 1024: 64}.get(n)
    if r == 16:
        return 8 if n == 256 else None

def predicted_R19(r, Q, n):
    if r == 4: return 8 if n == 256 else Fr(n, 8)
    if r == 8: return {256: 16, 512: 128}.get(n)
    if r == 16: return (512 if Q >= 512 else None) if n == 256 else None

if __name__ == '__main__':
    import time
    t0 = time.time()
    Qs = [128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    bad = 0; rows = 0; nonup = 0
    print('r  Q      S    n      R19     N4      new     all     | pred_R20  pred_R19  | all-mode bits')
    for r in [4, 8, 16]:
        for Q in Qs:
            for S in [64, 256]:
                n = 256
                while n < 4*Q:
                    E = r*Q*S
                    res = {m: threshold(r, Q, S, n, m) for m in ['R19', 'N4', 'new', 'all']}
                    pr = predicted(r, Q, n); p19 = predicted_R19(r, Q, n)
                    def pq(c):
                        if c is None: return None
                        v = c*E/Q
                        return int(v) if v <= E else None
                    okA = (res['all'][0] == pq(pr)) if pr is not None else (res['all'][0] is None)
                    okR = (res['R19'][0] == pq(p19)) if p19 is not None else (res['R19'][0] is None)
                    # if the predicted qq exceeds E the printed claim is vacuous; flag separately
                    flag = '' if (okA and okR) else '  <-- MISMATCH'
                    bad += (not okA) + (not okR); rows += 1
                    nonup += sum(not res[m][1] for m in res)
                    print(f'{r:<3}{Q:<7}{S:<5}{n:<7}' + ''.join(f'{fmt(res[m][0],E):<8}' for m in ['R19','N4','new','all'])
                          + f'| {str(pr):<9} {str(p19):<9} | {res["all"][2]}{flag}')
                    n *= 2
    print(f'rows={rows}  mismatches vs printed R20/R19 patterns={bad}  non-upward-closed (any mode)={nonup}')
    print(f'time {time.time()-t0:.1f}s')
