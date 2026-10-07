# indep_recount_R20_R23.py -- referee's independent re-implementation of R20 Cor 5.3 and R23 Cor 3.3.
# Run: python3 -I indep_recount_R20_R23.py
# Written from the formulas in R19 v2.1 Thm 4.1 (4.1) (+ R20 Prop 5.2 N4 form) and R20 v2.1 Thm 5.1 (4.1'),
# NOT from the owner's script.  Exact arithmetic (Fraction + integer isqrt root bracketing, then exact
# verification at the boundary integers).  For each (r,Q,S,n,qq,d') the set of integer tau0 in [1,tau_hi]
# failing BOTH tests is computed as an explicit integer interval set; the case closes iff it is empty.
# Modes:
#   R20      : m=min(rho*qq,E),  N1=1
#   R23      : m=E,              N1=max(1,ceil(E/(rho*qq)))        (R23 Prop 2.1(ii): nu_u>=E)
#   R22only  : nu_min=rho*qq*max(1,ceil((E-X)/(rho*qq))), m=min(nu_min,E), N1=nu_min/(rho*qq)
#              (only R22 Cor 3.2 nu_u>=E-X plus divisibility; no R23 bootstrap) -- robustness test
from fractions import Fraction as Fr
from math import isqrt, floor, ceil
import sys

THR = Fr(1551, 4000)

def cdiv(a, b):
    return -((-a) // b)

def mode_params(mode, E, X, rq):
    if mode == "R20":
        return min(rq, E), 1
    if mode == "R23":
        return E, max(1, cdiv(E, rq))
    if mode == "R22only":
        k = max(1, cdiv(E - X, rq))
        nu = rq * k
        return min(nu, E), k
    raise ValueError(mode)

def int_set_lt0_affine(c0, c1, lo, hi):
    """integers t in [lo,hi] with c0+c1*t<0, returned as (a,b) interval or None"""
    if lo > hi: return None
    if c1 == 0:
        return (lo, hi) if c0 < 0 else None
    root = Fr(-c0) / c1
    if c1 < 0:   # holds for t > root
        a = floor(root) + 1
        a = max(a, lo)
        # exact verification
        while a - 1 >= lo and c0 + c1 * (a - 1) < 0: a -= 1
        while a <= hi and not (c0 + c1 * a < 0): a += 1
        return (a, hi) if a <= hi else None
    else:        # holds for t < root
        b = ceil(root) - 1
        b = min(b, hi)
        while b + 1 <= hi and c0 + c1 * (b + 1) < 0: b += 1
        while b >= lo and not (c0 + c1 * b < 0): b -= 1
        return (lo, b) if b >= lo else None

def fail_set_concave(a2, a1, a0, lo, hi):
    """integers t in [lo,hi] with a2 t^2 + a1 t + a0 >= 0, a2<0: an interval or None"""
    assert a2 < 0
    f = lambda t: a2 * t * t + a1 * t + a0
    disc = a1 * a1 - 4 * a2 * a0
    if disc < 0: return None
    # sqrt bracket
    p, qd = disc.numerator, disc.denominator
    s_lo = Fr(isqrt(p * qd), qd)           # <= sqrt(disc)
    s_hi = s_lo + Fr(1, qd)                # >= sqrt(disc)
    # roots: (-a1 -+ s)/(2 a2); a2<0 so smaller root = (-a1 + s)/(2a2)?? compute both and order
    c = 2 * a2
    cand = [(-a1 + s_lo) / c, (-a1 + s_hi) / c, (-a1 - s_lo) / c, (-a1 - s_hi) / c]
    rmin, rmax = min(cand), max(cand)
    A = max(lo, floor(rmin) - 1); B = min(hi, ceil(rmax) + 1)
    if A > B: return None
    # tighten exactly
    while A <= B and f(A) < 0: A += 1
    while B >= A and f(B) < 0: B -= 1
    if A > B: return None
    # sanity: concavity => f>=0 on [A,B]; and f<0 just outside within [lo,hi]
    assert f(A) >= 0 and f(B) >= 0
    if A - 1 >= lo: assert f(A - 1) < 0
    if B + 1 <= hi: assert f(B + 1) < 0
    return (A, B)

def subtract(intv, cut):
    """intv minus cut (both closed integer intervals or None) -> list of intervals"""
    if intv is None: return []
    if cut is None: return [intv]
    a, b = intv; c, d = cut
    out = []
    if c > a: out.append((a, min(b, c - 1)))
    if d < b: out.append((max(a, d + 1), b))
    return [x for x in out if x[0] <= x[1]]

def case(r, Q, S, n, qq, dp, mode):
    E = r * Q * S; rho = Q // 2; T = Q * S; X = T // 2
    h = n * E; q = n * E * E; d = E + 2
    N = Fr(16 * h, 625); a = Fr(8 * h, 625) - dp + X - rho
    G = d * d - 3 * d; degpsi = (E + 1) * d; ddef = Fr(q, 1000)
    Eset = Fr(3 * d * d + 7 * d + 2, 2)
    thr = THR * q
    rq = rho * qq
    m, N1 = mode_params(mode, E, X, rq)
    tau_hi = floor(min(a * dp / rq, (N * d / rho + d) / qq))
    if tau_hi < 1:
        return True, "vacuous", []
    fl = (2 * dp + G) // (E - 1)
    # common constant part (no tau)
    K0 = (dp - E) * degpsi + (E + 1) * G + 3 * dp + d * (2 * dp + G) + (dp - E) * fl
    # ---- N4 form of (4.1): N_good*(K - tau) <= K0 + 2r(d-1)(a dp - rq tau) + 2 d tau + (K - tau)*(B0 + 2 tau)
    K = dp - E + N1
    B0 = N * d + Eset + 3 * d + 2 * degpsi + 6 * ddef + 7
    C0 = K0 + 2 * r * (d - 1) * a * dp
    C1 = -2 * r * (d - 1) * rq + 2 * d
    # Qd(t) = C0 + C1 t + (K - t)(B0 - thr + 2t)  ; pass iff Qd<0 (and K-t>0)
    Bm = B0 - thr
    a2 = Fr(-2); a1 = C1 + 2 * K - Bm; a0 = C0 + K * Bm
    lo, hi = 1, tau_hi
    n4_dom_hi = min(hi, K - 1)
    fail_n4 = []
    if n4_dom_hi >= lo:
        fs = fail_set_concave(a2, a1, a0, lo, n4_dom_hi)
        if fs: fail_n4.append(fs)
    if K - 1 < hi:
        fail_n4.append((max(lo, K), hi))
    # ---- (4.1'): N_good*D1 <= K0 + 2r(d-1)(a dp - rq t) + 2 d t + d(dp-1)(dp-2)/2 + D1*(B1 + 2t)
    D1 = dp - E - (a - m)
    pass41p = None
    if D1 > 0:
        Bb = 2 * degpsi + 2 * (2 * a - dp) * dp + G
        B1 = N * d + Eset + 3 * d + 6 * ddef + 7 + Bb + (2 * dp + G)
        L0 = K0 + 2 * r * (d - 1) * a * dp + Fr(d * (dp - 1) * (dp - 2), 2) + D1 * B1 - thr * D1
        L1 = -2 * r * (d - 1) * rq + 2 * d + 2 * D1
        pass41p = int_set_lt0_affine(L0, L1, lo, hi)
    fails = []
    for iv in fail_n4:
        fails += subtract(iv, pass41p)
    return (len(fails) == 0), ("41p:%s" % (pass41p,)), fails

def least_qq(r, Q, S, n, mode):
    E = r * Q * S; rho = Q // 2
    h = n * E; d = E + 2; N = Fr(16 * h, 625)
    res = []
    qq = 128
    while True:
        st = []
        vac_all = True
        for dp in range(2 * E - 2, 2 * E + 5):
            ok, how, fails = case(r, Q, S, n, qq, dp, mode)
            st.append(ok)
            if how != "vacuous": vac_all = False
        res.append((qq, all(st), vac_all))
        if vac_all and (N * d / rho + d) / qq < 1:
            break
        qq *= 2
    least = None; least_nonvac = None
    for qq_, c, v in reversed(res):
        if c:
            least = qq_
        else:
            break
    # least nonvacuous closure: least qq in the closed tail where some d' was nonvacuous
    if least is not None:
        tail = [x for x in res if x[0] >= least]
        nonvac = [x for x in tail if not x[2]]
        least_nonvac = least if nonvac else None
    return least, least_nonvac, "".join("1" if c else "0" for _, c, _ in res), res

def label(least, least_nonvac, E, Q):
    if least is None: return "never"
    if least_nonvac is None: return "none(vacuous)"
    return str(Fr(least * Q, E)) + "E/Q"

if __name__ == "__main__":
    print("== Part 1: R20 table grid, modes R20 / R23 / R22only ==")
    grid = []
    for r in (4, 8, 16):
        for n in (256, 512, 1024, 2048, 4096, 8192):
            for Q in (128, 256, 512, 1024, 2048, 4096, 8192, 16384):
                if n >= 4 * Q: continue
                for S in (64, 256):
                    grid.append((r, Q, S, n))
    rows = 0
    for (r, Q, S, n) in grid:
        E = r * Q * S
        out = []
        for mode in ("R20", "R23", "R22only"):
            l, lnv, bits, _ = least_qq(r, Q, S, n, mode)
            out.append(label(l, lnv, E, Q))
        rows += 1
        print("r=%2d n=%5d Q=%5d S=%3d | R20 %-14s | R23 %-14s | R22only %-14s" % (r, n, Q, S, out[0], out[1], out[2]))
        sys.stdout.flush()
    print("rows:", rows)
