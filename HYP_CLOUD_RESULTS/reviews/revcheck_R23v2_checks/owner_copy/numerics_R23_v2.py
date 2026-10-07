# numerics_R23_v2.py -- Claude HYP(2) owner, round 23, v2 copy (audit FIX-1, FIX-2, FIX-4).
#   Run: python3 -I numerics_R23_v2.py
#   v2 changes: (FIX-1) the diagnostics print the EXACT failing integer sets of tau0, not only failing
#   test points; (FIX-2) a third mode 'R22only' (m=min(rho*qq*ceil((E-X)/(rho*qq)),E), N1=1), i.e. R22 Cor 3.2
#   fed into R20's order step; (FIX-4) for each row the tau_hi at the least closing qq is printed.
#   Parts A, C, D, B2 are unchanged.
# Exact rational arithmetic only (fractions.Fraction, integer isqrt-free sign checks).
#
# Part A: Thm 3.1 of R23 (kernel-aligned (K), any twist, F^2 does not divide a_P or a_R):
#   N_good <= Nd + 2deg[T]/qq + (1.5d^2+3.5d+1) + 6d_def + 7 + deg psi + 2(M'+Q-T-d')d'
#   normalisation: N<16h/625, M'<8h/625, d=E+2, d'<=2E+4, deg psi<=(E+1)d,
#   deg[T]<=Nd/rho+d, qq>=128, d_def<=q/1000, q=nE^2, E=rQS.
#   Upper bound used for the whole strip (drops the negative part Q-T-d'<0):
#   UB/q = (16/625)(1+2/E) + 2(16/625)(1+2/E)/(128 rho) + 2(E+2)/(128 q)
#        + (1.5d^2+3.5d+1)/q + 6/1000 + 7/q + (E+1)(E+2)/q + (32/625)(1+2/E)
#   each term non-increasing in r,Q,S,n.  Also the exact (d'-maximised) bound on the 1260-row grid.
#
# Part B: re-implementation of R20 Cor 5.3 (bounds (4.1)-N4 of R19/R20 and (4.1') of R20 Thm 5.1)
#   mode "R20": m=min(rho*qq,E), N1=1           (must reproduce the R20 v2.1 table)
#   mode "R23": m=E,             N1=ceil(E/(rho*qq))  (R23 Prop 2.1: nu_u>=E in (K))
#   For each (r,Q,S,n) and dyadic qq>=128 (up to the first qq with tau_hi<1), and every
#   d' in [2E-2,2E+4], the model is excluded for qq iff every integer tau0 in [1,tau_hi]
#   satisfies (4.1)-N4 (tau0 <= d'-E+N1-1) or (4.1').  Prints the least dyadic qq from which
#   all larger qq close, per (r,n,Q,S).
#
# Part C: order sequences (0<e1<e2<e3) of a linear system of dim<=4 closed under the
#   p-adic criterion for p=2 (Stoehr-Voloch Cor 1.9, CITED): every binary sub-integer of an order is
#   an order.  Enumerates all such sequences with entries <= 2^12 and checks that
#   N0=(2r-1)2^k is never an order (r>=4), and computes gamma = N0 - max{eps<N0} (with e1=1).
#
# Part B2: R23 mode at n=256 for r in {4,8}, all Q in 2^7..2^14, S in 2^6..2^12 (112 cases).
#
# Part D: (R1), 128<=qq<=S.  R22 Thm 5.3(i) bound B (reproduces R22's corner value exactly);
#   Sigma* = largest integer Sigma with Sigma*(d^2-3d) + 4*tau_hi < gamma*(1551q/4000 - B),
#   gamma=(r-1)S/qq-1, tau_hi=floor((Nd/rho+d)/qq).  R23 Cor 4.5: excluded if sum(eps_i)<=Sigma*.
#
# Diagnostics: R23 mode, r=16, n=256, Q=128, S=64, qq in {128,1024,4096}.
from fractions import Fraction as Fr
import math

THR = Fr(1551, 4000)

def params(r, Q, S, n):
    E = r*Q*S; rho = Q//2; T = Q*S; X = T//2
    h = n*E; q = n*E*E; d = E+2
    return E, rho, T, X, h, q, d

# ---------------- Part A ----------------
def thmB_exact(r, Q, S, n):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h, 625); Mp = Fr(8*h, 625)
    degpsi = (E+1)*d
    degT = N*d/rho + d
    base = N*d + 2*degT/128 + Fr(3*d*d+7*d+2, 2) + Fr(6*q, 1000) + 7 + degpsi
    best = None
    for dp in range(2*E-2, 2*E+5):
        val = base + 2*(Mp+Q-T-dp)*dp
        if best is None or val > best: best = val
    return best/q

def thmB_UB(r, Q, S, n):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    return (Fr(16,625)*(1+Fr(2,E)) + 2*Fr(16,625)*(1+Fr(2,E))/(128*rho) + Fr(2*(E+2),128*q)
            + Fr(3*d*d+7*d+2, 2*q) + Fr(6,1000) + Fr(7,q) + Fr((E+1)*(E+2), q)
            + Fr(32,625)*(1+Fr(2,E)))

def grid1260():
    for r in (4,8,16,32,64):
        for Q in [2**i for i in range(7,15)]:
            for S in [2**i for i in range(6,13)]:
                n = 256
                while n < 4*Q:
                    yield r,Q,S,n
                    n *= 2

def partA():
    print("=== Part A: R23 Thm 3.1 (K with F^2 not dividing a) ===")
    rows = 0; mx = None; arg = None; mxub = None
    for (r,Q,S,n) in grid1260():
        v = thmB_exact(r,Q,S,n); u = thmB_UB(r,Q,S,n)
        assert v <= u, (r,Q,S,n)
        rows += 1
        if mx is None or v > mx: mx, arg = v, (r,Q,S,n)
        if mxub is None or u > mxub: mxub = u
    c = thmB_UB(4,128,64,256)
    print("rows", rows, " max exact bound/q =", float(mx), "at", arg)
    print("whole-strip sup (corner UB) =", c, "=", float(c), " < 1551/4000:", c < THR)
    print("max UB on grid equals corner UB:", mxub == c)

# ---------------- Part B ----------------
def ceil_div(a, b):
    return -((-a)//b)

def case_closed(r, Q, S, n, qq, dp, mode):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h, 625)
    a = Fr(8*h, 625) - dp + X - rho
    g22 = d*d - 3*d                       # 2g-2 upper bound (also max(2g-2,0))
    degpsi = (E+1)*d
    ddef = Fr(q, 1000)
    rq = rho*qq
    if mode == "R20":
        m = min(rq, E); N1 = 1
    elif mode == "R22only":
        m = min(rq*ceil_div(E - X, rq), E); N1 = 1
    else:
        m = E; N1 = max(1, ceil_div(E, rq))
    tau_hi = math.floor(min(a*dp/rq, (N*d/rho + d)/qq))
    if tau_hi < 1:
        return True, "vacuous"
    thr = THR*q
    fl = (2*dp + g22)//(E-1)
    common = ((dp-E)*degpsi + ((E+1)*g22 + 3*dp) + d*(2*dp+g22) + (dp-E)*fl)
    # (4.1') : linear in tau
    D1 = dp - E - (a - m)
    def b41p(t):
        num = common + 2*r*(d-1)*(a*dp - rq*t) + 2*d*t + Fr(d*(dp-1)*(dp-2), 2)
        Bb = 2*degpsi + 2*(2*a-dp)*dp + g22
        br = N*d + 2*t + Fr(3*d*d+7*d+2,2) + 3*d + 6*ddef + 7 + Bb + (2*dp+g22)
        return num/D1 + br
    t1 = None
    if D1 > 0:
        # b41p is affine in t; find least integer t>=1 with b41p(t) < thr
        v1 = b41p(1); v2 = b41p(2); sl = v2 - v1
        if v1 < thr:
            t1 = 1
        elif sl < 0:
            t = (thr - v1)/sl + 1          # b41p(t) = v1 + sl*(t-1) < thr  <=> t > (thr-v1)/sl + 1
            t1 = math.floor(t) + 1
            while b41p(t1-1) < thr and t1 > 1: t1 -= 1
            assert b41p(t1) < thr
        # if sl>=0 and v1>=thr: never
    # (4.1)-N4 on [1, R] with R = min(tau_hi, t1-1)
    R = tau_hi if t1 is None else min(tau_hi, t1-1)
    if R < 1:
        return True, "41p"
    den0 = dp - E + N1          # denominator dp-E-tau+N1 > 0 needed
    if R > den0 - 1:
        return False, f"N4-range: tau_hi={tau_hi}, (4.1') needs tau0>={t1}, N4 needs tau0<={den0-1}"
    def qN4(t):
        A = common + 2*r*(d-1)*(a*dp - rq*t) + 2*d*t
        Bv = N*d + 2*t + Fr(3*d*d+7*d+2,2) + 3*d + 2*degpsi + 6*ddef + 7
        return A + (Bv - thr)*(den0 - t)       # <0  <=> bound < thr
    # qN4 is a concave quadratic in t (leading coeff -2): check endpoints and vertex
    pts = {1, R}
    # vertex: qN4(t) = -2 t^2 + b t + c ; get b from three values
    f0 = qN4(0); f1 = qN4(1); f2 = qN4(2)
    lead = (f2 - 2*f1 + f0)/2
    b = f1 - f0 - lead
    assert lead == -2
    tv = b/(-2*lead)
    for t in (math.floor(tv), math.floor(tv)+1):
        if 1 <= t <= R: pts.add(t)
    bad = sorted(t for t in pts if not qN4(t) < 0)
    ok = not bad
    return ok, ("N4+41p" if t1 is not None else "N4") + ("" if ok else f" fails at tau0 in {bad[:3]}, (4.1') from {t1}")

def failing_set(r, Q, S, n, qq, dp, mode="R23"):
    """exact set of integers tau0 in [1,tau_hi] satisfying neither (4.1)-N4 nor (4.1'), as intervals"""
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h, 625)
    a = Fr(8*h, 625) - dp + X - rho
    g22 = d*d - 3*d; degpsi = (E+1)*d; ddef = Fr(q, 1000); rq = rho*qq
    if mode == "R20": m = min(rq, E); N1 = 1
    elif mode == "R22only": m = min(rq*ceil_div(E - X, rq), E); N1 = 1
    else: m = E; N1 = max(1, ceil_div(E, rq))
    tau_hi = math.floor(min(a*dp/rq, (N*d/rho + d)/qq))
    thr = THR*q; fl = (2*dp + g22)//(E-1)
    common = ((dp-E)*degpsi + ((E+1)*g22 + 3*dp) + d*(2*dp+g22) + (dp-E)*fl)
    D1 = dp - E - (a - m)
    def ok41p(t):
        if D1 <= 0: return False
        num = common + 2*r*(d-1)*(a*dp - rq*t) + 2*d*t + Fr(d*(dp-1)*(dp-2), 2)
        Bb = 2*degpsi + 2*(2*a-dp)*dp + g22
        br = N*d + 2*t + Fr(3*d*d+7*d+2,2) + 3*d + 6*ddef + 7 + Bb + (2*dp+g22)
        return num/D1 + br < thr
    den0 = dp - E + N1
    def qN4(t):
        A = common + 2*r*(d-1)*(a*dp - rq*t) + 2*d*t
        Bv = N*d + 2*t + Fr(3*d*d+7*d+2,2) + 3*d + 2*degpsi + 6*ddef + 7
        return A + (Bv - thr)*(den0 - t)
    def okN4(t):
        return t <= den0 - 1 and qN4(t) < 0
    # okN4 on [1, den0-1] is the complement of an interval {qN4>=0} (concave quadratic);
    # ok41p is upward closed (affine, slope<0) -- checked below.
    # Generic exact scan over breakpoints: find all boundaries by bisection.
    def bisect_change(f, lo, hi):
        # f(lo) != f(hi); return smallest t in (lo,hi] with f(t)==f(hi)
        flo = f(lo)
        while hi - lo > 1:
            mid = (lo + hi)//2
            if f(mid) == flo: lo = mid
            else: hi = mid
        return hi
    good = lambda t: okN4(t) or ok41p(t)
    # candidate breakpoints: vertex of qN4, den0, threshold of 41p; build sorted points and bisect between
    f0 = qN4(0); f1 = qN4(1); f2 = qN4(2); lead = (f2 - 2*f1 + f0)/2; b = f1 - f0 - lead
    tv = math.floor(b/(-2*lead))
    pts = sorted({1, tau_hi, max(1, min(tau_hi, tv)), max(1, min(tau_hi, tv+1)),
                  max(1, min(tau_hi, den0-1)), max(1, min(tau_hi, den0))})
    # within each segment between consecutive pts each of okN4, ok41p changes at most once
    fails = []
    cur = None
    def add(lo, hi):
        if fails and fails[-1][1] >= lo - 1: fails[-1] = (fails[-1][0], max(hi, fails[-1][1]))
        else: fails.append((lo, hi))
    for i in range(len(pts)-1 if len(pts)>1 else 1):
        lo = pts[i]; hi = pts[i+1] if len(pts)>1 else pts[0]
        # split [lo,hi] by changes of okN4 and ok41p
        cuts = {lo, hi+1}
        for f in (okN4, ok41p):
            if lo < hi and f(lo) != f(hi): cuts.add(bisect_change(f, lo, hi))
        cuts = sorted(cuts)
        for j in range(len(cuts)-1):
            a0, a1 = cuts[j], cuts[j+1]-1
            if a0 > a1: continue
            if not good(a0):
                assert not good(a1)
                add(a0, a1)
    # verify by spot checks
    for (lo, hi) in fails:
        for t in {lo, hi, (lo+hi)//2}:
            assert not good(t)
        if lo > 1: assert good(lo-1)
        if hi < tau_hi: assert good(hi+1)
    return tau_hi, fails

def least_qq(r, Q, S, n, mode):
    """least dyadic qq>=128 such that every dyadic qq'>=qq closes (all d')."""
    E = r*Q*S
    res = []
    qq = 128
    while True:
        closed = all(case_closed(r,Q,S,n,qq,dp,mode)[0] for dp in range(2*E-2, 2*E+5))
        res.append((qq, closed))
        E_, rho, T, X, h, q, d = params(r,Q,S,n)
        N = Fr(16*h,625)
        if (N*d/rho + d)/qq < 1:   # tau_hi<1 for all larger qq
            break
        qq *= 2
    least = None
    for qq_, c in reversed(res):
        if c: least = qq_
        else: break
    bits = "".join("1" if c else "0" for _, c in res)
    return least, bits

def tau_hi_at(r, Q, S, n, qq):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h, 625); vals = []
    for dp in range(2*E-2, 2*E+5):
        a = Fr(8*h, 625) - dp + X - rho
        vals.append(math.floor(min(a*dp/(rho*qq), (N*d/rho + d)/qq)))
    return max(vals)

def qq_vac(r, Q, S, n):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h, 625); qq = 128
    while (N*d/rho + d)/qq >= 1: qq *= 2
    return qq

def fmt(least, E, Q, vac):
    if least is None: return "none"
    fr = Fr(least*Q, E)
    return f"{least} (= {fr} E/Q)"

def diag(r, Q, S, n, qq, mode="R23"):
    """print, per d', which tau0 fail"""
    E = r*Q*S
    for dp in (2*E-2, 2*E+4):
        ok, how = case_closed(r,Q,S,n,qq,dp,mode)
        print(f"   diag r={r} Q={Q} S={S} n={n} qq={qq} d'={dp-2*E:+d}+2E: closed={ok} ({how})")

def partB():
    print("=== Part B: R20 Cor 5.3 re-implementation; modes R20 and R23 ===")
    for r in (4, 8, 16):
        for n in (256, 512, 1024, 2048, 4096, 8192):
            for Q in (128, 256, 512, 1024, 2048, 4096, 16384):
                if n >= 4*Q: continue
                for S in (64, 256):
                    E = r*Q*S
                    vac = qq_vac(r,Q,S,n)
                    l20, b20 = least_qq(r,Q,S,n,"R20")
                    l22, b22 = least_qq(r,Q,S,n,"R22only")
                    l23, b23 = least_qq(r,Q,S,n,"R23")
                    th = tau_hi_at(r,Q,S,n,l23) if l23 is not None else None
                    same = (l22 == l23 and b22 == b23)
                    print(f"r={r:2d} n={n:5d} Q={Q:5d} S={S:3d} | R20: {fmt(l20,E,Q,vac):22s} | R23: {fmt(l23,E,Q,vac):22s} | tau_hi at least R23 qq: {th} | R22only==R23: {same} | bits R20 {b20} R23 {b23}")

# ---------------- Part C ----------------
def subints(x):
    bits = [1<<i for i in range(x.bit_length()) if x>>i & 1]
    out = set()
    for mask in range(1<<len(bits)):
        out.add(sum(b for j,b in enumerate(bits) if mask>>j & 1))
    return out

def partC():
    print("=== Part C: p-adic closed order sequences (p=2), dim<=4 ===")
    L = 1<<12
    pw = [1<<i for i in range(13)]
    cands = sorted(set(pw) | {a+b for a in pw for b in pw if a<b})
    seqs = []
    for e1 in cands:
        if e1 > L: continue
        if not subints(e1) <= {0,e1}: continue
        seqs.append((0,e1))
        for e2 in cands:
            if e2 <= e1 or e2 > L: continue
            if not subints(e2) <= {0,e1,e2}: continue
            seqs.append((0,e1,e2))
            for e3 in cands:
                if e3 <= e2 or e3 > L: continue
                if not subints(e3) <= {0,e1,e2,e3}: continue
                seqs.append((0,e1,e2,e3))
    # completeness check: any integer up to L closed must be a power of 2 or sum of two
    for x in range(1, 600):
        s = subints(x) - {0}
        if len(s) <= 3:
            assert x in cands, x
    print("closed sequences enumerated:", len(seqs))
    bad = 0; worst = {}
    for r in (4,8,16,32,64):
        for k in range(0,7):
            N0 = (2*r-1)<<k
            assert len(subints(N0)) == 2*r
            for s in seqs:
                if N0 in s: bad += 1
            # gamma with e1=1
            g = None
            for s in seqs:
                if len(s)>1 and s[1]==1:
                    below = [e for e in s if e < N0]
                    gg = N0 - max(below)
                    if g is None or gg < g: g = gg
            worst[(r,k)] = g
            assert g >= (r-1)*(1<<k) - 1, (r,k,g)
    print("sequences containing some N0=(2r-1)2^k (r>=4):", bad)
    for (r,k),g in sorted(worst.items()):
        if k in (0,1,3,6):
            print(f"  r={r:2d} k={k}: N0={(2*r-1)<<k:5d}  min gamma (e1=1) = {g:4d}  bound (r-1)2^k-1 = {(r-1)*(1<<k)-1}")

# ---------------- Part D ----------------
# R22 Thm 5.3(i): charges + deg d^2, charges = Nd + 2deg[T]/qq + (1.5d^2+3.5d+1) + 6d_def + 7,
# deg d^2 = 2deg psi + 2 a d' + 2 rho deg[T]; R21/R22 normalisation: a < 8h/625, d'<=2E+4,
# rho deg[T] <= Nd + rho d, deg psi <= (E+1)d, deg[T] <= Nd/rho + d, qq>=128.
def B53i(r, Q, S, n):
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h,625); degT = N*d/rho + d; a = Fr(8*h,625); dp = 2*E+4
    return (N*d + 2*degT/128 + Fr(3*d*d+7*d+2,2) + Fr(6*q,1000) + 7
            + 2*(E+1)*d + 2*a*dp + 2*(N*d + rho*d))
def sigma_star(r, Q, S, n, qq):
    """largest integer Sigma with Sigma*(d^2-3d) + 4*tau_hi < gamma*(1551q/4000 - B53i), gamma=(r-1)S/qq-1"""
    E, rho, T, X, h, q, d = params(r, Q, S, n)
    N = Fr(16*h,625)
    tau_hi = math.floor((N*d/rho + d)/qq)
    gamma = (r-1)*S//qq - 1
    room = gamma*(THR*q - B53i(r,Q,S,n)) - 4*tau_hi
    sig = math.floor(room/(d*d-3*d))
    if sig*(d*d-3*d) == room: sig -= 1
    return sig, gamma, (2*r-1)*S//qq
def partD():
    print("=== Part D: (R1), 128<=qq<=S: Weierstrass bound |B_0| <= deg R_V / gamma ===")
    c = B53i(4,128,64,256)/(256*(4*128*64)**2)
    print("R22 Thm 5.3(i) corner value reproduced:", c, float(c), c == Fr(32480243592761,219902325555200))
    # whole-strip: B53i/q is non-increasing in r,Q,S,n (R22); so sup over S>=128 is <= corner(S=64)
    print(" r     Q     S     n    qq    N0 gamma   Sigma*   Sigma*/n  (excluded if sum of orders <= Sigma*)")
    worst = None
    for r in (4,8,16):
        for Q in (128,1024,16384):
            for S in (128,256,4096):
                for n in (256,512,2048,8192):
                    if n >= 4*Q: continue
                    qq = 128
                    while qq <= S:
                        sg, gm, N0 = sigma_star(r,Q,S,n,qq)
                        ratio = Fr(sg, n)
                        if worst is None or ratio < worst[0]: worst = (ratio, (r,Q,S,n,qq), sg)
                        if qq in (S, 128) and Q in (128,16384) and n in (256,2048):
                            print(f"{r:2d} {Q:5d} {S:5d} {n:5d} {qq:5d} {N0:5d} {gm:5d} {sg:8d}  {float(ratio):8.4f}")
                        qq *= 2
    print("min Sigma*/n over the D-grid:", float(worst[0]), "at (r,Q,S,n,qq) =", worst[1], "Sigma* =", worst[2])

if __name__ == "__main__":
    partA()
    partC()
    partD()
    partB()
    print("=== Part B2: R23 mode, n=256, r in {4,8}, S in 2^6..2^12, all Q: is every dyadic qq>=128 closed? ===")
    allok = True; cnt = 0
    for r in (4,8):
        for Q in [2**i for i in range(7,15)]:
            for S in [2**i for i in range(6,13)]:
                l, b = least_qq(r,Q,S,256,"R23"); cnt += 1
                if l != 128: allok = False; print("  NOT all closed:", r,Q,S,b)
    print("  cases:", cnt, " all qq>=128 closed in every case:", allok)
    print("=== Part B2': R22only mode on the same 112 cases ===")
    allok = True
    for r in (4,8):
        for Q in [2**i for i in range(7,15)]:
            for S in [2**i for i in range(6,13)]:
                l, b = least_qq(r,Q,S,256,"R22only")
                if l != 128: allok = False; print("  NOT all closed:", r,Q,S,b)
    print("  R22only: all qq>=128 closed in every case:", allok)
    print("=== diagnostics v2 (R23 mode), r=16 n=256 below 8E/Q: EXACT failing tau0-sets ===")
    E = 16*128*64
    for qq in (128, 1024, 4096):
        for dp in (2*E-2, 2*E+4):
            th, fails = failing_set(16,128,64,256,qq,dp)
            print(f"   r=16 Q=128 S=64 n=256 qq={qq} d'=2E{dp-2*E:+d}: tau_hi={th}, failing tau0 intervals: {fails}")
