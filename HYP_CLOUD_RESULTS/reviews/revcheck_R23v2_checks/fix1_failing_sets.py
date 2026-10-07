# FIX-1: exact failing tau_0 sets, R23 mode, r=16, n=256, Q=128, S=64 (and S=256 for comparison).
# (1) interval solver (exact integer polynomials), (2) brute-force integer scan over every tau_0,
# (3) direct Fraction evaluation of the printed formulas at the interval ends +-1.
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rc_bounds import *

def direct(P, t):
    """Direct evaluation of the two bounds over q at tau_0=t (Fractions), from the printed formulas."""
    E,rho,q,d,g22,a,N,ddef,dpsi,rq,m,N1,dp,r = (P[k] for k in
        "E rho q d g22 a N ddef dpsi rq m N1 dp r".split())
    cusp = (dp - E)*((2*dp + g22)//(E - 1))
    fac = dp - E - t + N1
    n4 = None
    if t <= dp - E + N1 - 1:
        rhs = ((dp-E)*dpsi + 2*r*(d-1)*(a*dp - rq*t) + ((E+1)*g22 + 3*dp) + d*(2*dp+g22) + 2*d*t
               + cusp + fac*(N*d + 2*t + F(3*d*d+7*d+2,2) + 3*d + 2*dpsi + 6*ddef + 7))
        n4 = rhs/fac/q
    D1 = dp - E - (a - m); p41 = None
    if D1 > 0:
        Bb = 2*dpsi + 2*(2*a - dp)*dp + max(g22, 0)
        rhs = ((dp-E)*dpsi + 2*r*(d-1)*(a*dp - rq*t) + ((E+1)*g22 + 3*dp) + d*(2*dp+g22) + cusp
               + 2*d*t + d*(dp-1)*(dp-2)/F(2)
               + D1*(N*d + 2*t + F(3*d*d+7*d+2,2) + 3*d + 6*ddef + 7 + Bb + (2*dp+g22)))
        p41 = rhs/D1/q
    return n4, p41

def ok_direct(P, t):
    n4, p = direct(P, t)
    return (n4 is not None and n4 < LAM) or (p is not None and p < LAM)

r, Q, n = 16, 128, 256
for S in (64,):
    E = r*Q*S
    print(f"=== r={r} n={n} Q={Q} S={S} E={E}  4E/Q={4*E//Q}  8E/Q={8*E//Q} ===")
    for qq in (128, 1024, 4096, 8192):
        for dp in range(2*E-2, 2*E+5):
            fs, P = failing(r, Q, S, n, dp, qq, "R23")
            pN4, cmax, p41 = polys(P)
            n4good = pos_set(pN4, 1, min(P['tau_hi'], cmax))
            p41good = pos_set(p41, 1, P['tau_hi']) if p41 else None
            print(f"qq={qq:5d} d'=2E{dp-2*E:+d}: tau_hi={P['tau_hi']} N1={P['N1']} N4-domain<= {cmax}"
                  f" N4 holds on {n4good}; (4.1') holds on {p41good}; FAILING {fs}")
            # direct spot checks at ends of every failing interval and neighbours
            for (x, y) in fs:
                for t in (x-1, x, y, y+1):
                    if 1 <= t <= P['tau_hi']:
                        inside = x <= t <= y
                        assert ok_direct(P, t) == (not inside), ("direct mismatch", qq, dp, t)
    print("direct-formula spot checks at all failing-interval ends +-1: OK")

# brute-force integer scan (independent of the root solver) for the two quoted d'
print("=== brute-force scan of every integer tau_0 in [1,tau_hi] (d'=2E-2, 2E+4) ===")
S = 64; E = r*Q*S
for qq in (4096, 1024, 128):
    for dp in (2*E-2, 2*E+4):
        t0 = time.time()
        P = setup(r, Q, S, n, dp, qq, "R23")
        pN4, cmax, p41 = polys(P)
        th = P['tau_hi']
        runs = []; cur = None
        a0, a1, a2 = pN4
        b0, b1 = (p41[0], p41[1]) if p41 else (None, None)
        for t in range(1, th+1):
            ok = (t <= cmax and (a2*t + a1)*t + a0 > 0) or (p41 is not None and b1*t + b0 > 0)
            if not ok:
                if cur is not None and cur[1] == t-1: cur[1] = t
                else:
                    cur = [t, t]; runs.append(cur)
        fs, _ = failing(r, Q, S, n, dp, qq, "R23")
        print(f"qq={qq} d'=2E{dp-2*E:+d}: scan failing runs={[tuple(x) for x in runs]}  solver={fs}  "
              f"agree={[tuple(x) for x in runs]==fs}  len={sum(y-x+1 for x,y in fs)}  ({time.time()-t0:.1f}s)")
