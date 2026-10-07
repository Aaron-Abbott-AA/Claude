# Revision check R19 v2: independent exact-Fraction evaluation of (4.1) AS PRINTED IN v2,
# with the normalisation of Cor. 4.2 (v2).  Written from the v2 text only; no src/ script used.
#
# (4.1): N_good*(d'-E-tau+1) <= (d'-E)degpsi + 2r(d-1) a d' + [(E+1)(2g-2)+3d'] + d(2d'+2g-2) + 2 d tau
#                               + (d'-E) floor((2d'+2g-2)/(E-1))                       [FIX-2 term]
#                               + (d'-E-tau+1)[N d + 2 tau + (1.5d^2+3.5d+1) + 3d + 2 degpsi + 6 d_def + 7]
# Normalisation: d=E+2; d' in [2E-2,2E+4]; 2g-2 = d(d-3) (g=(d-1)(d-2)/2); a = 8h/625 - d' + X - rho;
#   N = 16h/625; d_def = q/1000; degpsi = (E+1)d. Excluded iff bound/q < 1551/4000.
# Height: tau_0 <= min(a d'/(rho qq), (N d/rho + d)/qq)  (Prop 3.3 / a-priori).
from fractions import Fraction as F
import sys

LIM = F(1551, 4000)

def params(r, Q, S, n):
    E = r * Q * S
    T = Q * S
    X = T // 2
    rho = Q // 2
    h = n * E
    q = E * h
    d = E + 2
    return E, T, X, rho, h, q, d

def bound_over_q(r, Q, S, n, dp, tau, fix2=True):
    E, T, X, rho, h, q, d = params(r, Q, S, n)
    tg = d * (d - 3)                       # 2g-2
    a = F(8 * h, 625) - dp + X - rho
    N = F(16 * h, 625)
    ddef = F(q, 1000)
    dpsi = (E + 1) * d
    m = dp - E - tau + 1
    assert m >= 1
    rhs = ((dp - E) * dpsi + 2 * r * (d - 1) * a * dp + ((E + 1) * tg + 3 * dp)
           + d * (2 * dp + tg) + 2 * d * tau)
    if fix2:
        rhs += (dp - E) * ((2 * dp + tg) // (E - 1))
    rhs += m * (N * d + 2 * tau + (F(3, 2) * d * d + F(7, 2) * d + 1) + 3 * d + 2 * dpsi + 6 * ddef + 7)
    return rhs / m / q

def tau_max(r, Q, S, n, dp, fix2=True):
    E = r * Q * S
    lo, hi = 0, dp - E          # tau in [0, d'-E] (hypothesis tau_0<=d'-E)
    if bound_over_q(r, Q, S, n, dp, 0, fix2) >= LIM:
        return -1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if bound_over_q(r, Q, S, n, dp, mid, fix2) < LIM:
            lo = mid
        else:
            hi = mid - 1
    return lo

def height(r, Q, S, n, dp, qq):
    E, T, X, rho, h, q, d = params(r, Q, S, n)
    a = F(8 * h, 625) - dp + X - rho
    N = F(16 * h, 625)
    return min(a * dp / (rho * qq), (N * d / rho + d) / qq)

def dyadics(lo, hi):
    x = lo
    while x <= hi:
        yield x
        x *= 2

def least_qq(r, Q, S, n, fix2=True, mode="cons"):
    """least dyadic qq in [128,E] that excludes the model; None if none."""
    E = r * Q * S
    dps = list(range(2 * E - 2, 2 * E + 5))
    tm = {dp: tau_max(r, Q, S, n, dp, fix2) for dp in dps}
    for qq in dyadics(128, E):
        if mode == "cons":     # max height over d' in [2E-2,2E+4] vs min tau_max
            H = max(height(r, Q, S, n, dp, qq) for dp in dps)
            ok = H <= min(tm.values())
        else:                  # per-d' exact, admissible d' <= 2E+1
            ok = all(height(r, Q, S, n, dp, qq) <= tm[dp] for dp in dps if dp <= 2 * E + 1)
        if ok:
            return qq, tm
    return None, tm

def frac_E(qq, E):
    if qq is None:
        return "none"
    f = F(qq, E)
    return "E" if f == 1 else ("E/%d" % (1 / f) if f.numerator == 1 else str(f))

out = []
P = lambda *s: out.append(" ".join(str(x) for x in s))

# ---- Part A: tau_max/E (d'=2E-2 and min over the d' scan), with and without FIX-2 ----
P("== Part A: tau_max/E (S=64), least admissible Q with n<=2Q; argmin d' over [2E-2,2E+4] ==")
for r, ns in [(4, [256, 512, 1024, 2048, 4096, 8192]), (8, [256, 512, 1024, 2048]), (16, [256, 512])]:
    for n in ns:
        Q = max(128, n // 2)
        S = 64
        E = r * Q * S
        tms = {dp: tau_max(r, Q, S, n, dp, True) for dp in range(2 * E - 2, 2 * E + 5)}
        tms0 = {dp: tau_max(r, Q, S, n, dp, False) for dp in range(2 * E - 2, 2 * E + 5)}
        argmin = min(tms, key=lambda k: tms[k]) - 2 * E
        tm = min(tms.values())
        tm0 = min(tms0.values())
        P("r=%d n=%d Q=%d: tau_max/E=%.5f (no FIX-2: %.5f, diff %d) argmin d'=2E%+d" %
          (r, n, Q, tm / E, tm0 / E, tm0 - tm, argmin))

# ---- Part B: r=4 thresholds ----
P("")
P("== Part B: r=4 least dyadic qq (S=64 and S=256), cons / per-d' / no-FIX-2 ==")
for Q in [128, 256, 512, 1024, 2048, 4096, 16384]:
    for S in [64, 256]:
        if S == 256 and Q > 4096:
            continue
        n = 256
        while n <= 2 * Q:
            E = 4 * Q * S
            c, _ = least_qq(4, Q, S, n, True, "cons")
            p, _ = least_qq(4, Q, S, n, True, "perdp")
            c0, _ = least_qq(4, Q, S, n, False, "cons")
            claim = F(n, 8 * Q)
            okE4 = c is not None and F(c, E) <= F(1, 4)
            okn8 = (n == 256) or (c is not None and F(c, E) <= claim)
            P("r=4 Q=%d S=%d n=%d: cons=%s perdp=%s noFIX2=%s | <=E/4:%s <=nE/(8Q)=%s:%s" %
              (Q, S, n, frac_E(c, E), frac_E(p, E), frac_E(c0, E), okE4, frac_E(int(claim * E), E), okn8))
            n *= 2

# ---- Part C: r=16 n=256 ----
P("")
P("== Part C: r=16, n=256 (and n=512) least dyadic qq; claim 512E/Q for Q>=512 ==")
for Q in [128, 256, 512, 1024, 2048, 4096, 8192, 16384]:
    S = 64
    E = 16 * Q * S
    for n in [256, 512]:
        if n > 2 * Q:
            continue
        c, tm = least_qq(16, Q, S, n, True, "cons")
        p, _ = least_qq(16, Q, S, n, True, "perdp")
        c0, _ = least_qq(16, Q, S, n, False, "cons")
        claim = "E*512/Q=" + (frac_E(512 * E // Q, E) if Q >= 512 else "n/a(>E)")
        P("r=16 Q=%d n=%d: tau_max/E=%.5f cons=%s perdp=%s noFIX2=%s  [%s]" %
          (Q, n, min(tm.values()) / E, frac_E(c, E), frac_E(p, E), frac_E(c0, E), claim))

# ---- Part D: r=8 table rows ----
P("")
P("== Part D: r=8 rows (S=64) ==")
for Q in [128, 256, 1024, 4096]:
    for n in [256, 512, 1024]:
        if n > 2 * Q:
            continue
        S = 64
        E = 8 * Q * S
        c, tm = least_qq(8, Q, S, n, True, "cons")
        P("r=8 Q=%d n=%d: tau_max/E=%.5f least qq=%s" % (Q, n, min(tm.values()) / E, frac_E(c, E)))

# ---- Part E: asymptotic margin r=4, n=2Q, qq=E/4 ----
P("")
P("== Part E: r=4, n=2Q, qq=E/4: Prop3.3 height/E vs tau_max/E (d'=2E-2) ==")
for Q in [1024, 16384, 2 ** 19]:
    S = 64
    n = 2 * Q
    E = 4 * Q * S
    dp = 2 * E - 2
    H = height(4, Q, S, n, dp, E // 4)
    tm = tau_max(4, Q, S, n, dp, True)
    P("Q=%d: height/E=%.5f tau_max/E=%.5f margin/E=%.5f" % (Q, float(H / E), tm / E, tm / E - float(H / E)))

print("\n".join(out))
