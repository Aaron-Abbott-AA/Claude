# Referee check c1 (independent of owner code): exact Fraction evaluation of R19 bound (4.1).
#   N_good*(d'-E-tau+1) <= (d'-E)degpsi + 2r(d-1)a d' + [(E+1)(2g-2)+3d'] + d(2d'+2g-2) + 2 d tau
#                          + (d'-E-tau+1)*[N d + 2tau + (1.5d^2+3.5d+1) + 3d + 2degpsi + 6d_def + 7]
# with d=E+2, 2g-2<=d(d-3), degpsi<=(E+1)d, a<=8h/625-d'+X-rho, N<16h/625, d_def<=q/1000.
# Variant 'fix': adds the cusp-tangent excess CX=(d'-E)*floor((2d'+2g-2)/(E-1)) (referee FIX-2).
# Exclusion criterion as owner: bound/q < 1551/4000 (stricter than G9's N_good>1551q/4000+1).
# d' scanned over EVERY integer in [2E-2, 2E+4] (owner used only 2E-2, 2E, 2E+4).
from fractions import Fraction as Fr
import sys
G9 = Fr(1551, 4000)

def parts(r, Q, S, n, dp):
    E = r*Q*S; h = n*E; q = E*h; d = E+2; rho = Q//2; X = Q*S//2
    a = Fr(8*h, 625) - dp + X - rho; N = Fr(16*h, 625); dpsi = (E+1)*d; g2 = d*(d-3)
    return E, h, q, d, rho, X, a, N, dpsi, g2

def bound(r, Q, S, n, dp, tau, fix=False):
    E, h, q, d, rho, X, a, N, dpsi, g2 = parts(r, Q, S, n, dp)
    den = dp - E - tau + 1
    if den <= 0: return None
    num = (dp-E)*dpsi + 2*r*(d-1)*a*dp + ((E+1)*g2 + 3*dp) + d*(2*dp + g2) + 2*d*tau
    if fix: num += (dp-E)*((2*dp+g2)//(E-1))
    exc = N*d + 2*tau + Fr(3, 2)*d*d + Fr(7, 2)*d + 1 + 3*d + 2*dpsi + Fr(6*q, 1000) + 7
    return (Fr(num, den) + exc)/q

def taumax(r, Q, S, n, dp, fix=False):
    E = r*Q*S
    b = bound(r, Q, S, n, dp, 1, fix)
    if b is None or b >= G9: return 0
    lo, hi = 1, dp - E
    while lo < hi:
        mid = (lo+hi+1)//2; b = bound(r, Q, S, n, dp, mid, fix)
        if b is not None and b < G9: lo = mid
        else: hi = mid-1
    return lo

def least_qq_owner(r, Q, S, n, tm):
    # owner's conservative test: tau <= aK*dpm/(rho qq) with aK at d'=2E-2, dpm=2E+4; qq dyadic <= E
    E = r*Q*S; h = n*E; rho = Q//2
    aK = Fr(8*h, 625) - (2*E-2) + Q*S//2 - rho; dpm = 2*E+4
    qq = 1
    while qq <= E and aK*dpm/(rho*qq) > tm: qq *= 2
    return qq if qq <= E else None

def least_qq_exact(r, Q, S, n, fix=False):
    # per-d' test: need for EVERY admissible d' in [2E-2,2E+1]: a(d') d'/(rho qq) <= taumax(d')
    E = r*Q*S; h = n*E; rho = Q//2
    tms = {dp: taumax(r, Q, S, n, dp, fix) for dp in range(2*E-2, 2*E+2)}
    qq = 1
    while qq <= E:
        if all((Fr(8*h, 625) - dp + Q*S//2 - rho)*dp/(rho*qq) <= tms[dp] for dp in tms): return qq, tms
        qq *= 2
    return None, tms

def fmt(x, E): return "none<=E" if x is None else f"E/{E//x}" if x < E else "E"

if __name__ == "__main__":
    print("# Part A: tau_max/E (min over all d' in [2E-2,2E+4]); owner grid values vs scan")
    print("r Q S n | taumax/E(3 owner d') taumax/E(all d') argmin d'-2E | taumax/E with FIX-2 | owner-least-qq | exact-least-qq (d'<=2E+1) | with FIX-2")
    rows = []
    for r in [4, 8, 16, 32]:
        for Q in [128, 256, 512, 1024, 2048, 4096, 16384]:
            for S in [64, 256]:
                E = r*Q*S
                n = 256
                while n < 4*Q:
                    if n > 8192 and Q < 16384: break
                    t3 = min(taumax(r, Q, S, n, dp) for dp in [2*E-2, 2*E, 2*E+4])
                    alls = {dp: taumax(r, Q, S, n, dp) for dp in range(2*E-2, 2*E+5)}
                    tall = min(alls.values()); arg = min(alls, key=alls.get) - 2*E
                    tfix = min(taumax(r, Q, S, n, dp, True) for dp in range(2*E-2, 2*E+5))
                    qo = least_qq_owner(r, Q, S, n, t3) if t3 > 0 else None
                    qe, _ = least_qq_exact(r, Q, S, n)
                    qf, _ = least_qq_exact(r, Q, S, n, True)
                    print(f"{r} {Q} {S} {n} | {t3/E:.4f} {tall/E:.4f} {arg:+d} | {tfix/E:.4f} | {fmt(qo,E)} | {fmt(qe,E)} | {fmt(qf,E)}", flush=True)
                    rows.append((r, Q, S, n, t3, tall, tfix, qo, qe, qf))
                    n *= 2
    # Part B: the r=4 claim "qq>=E/4 suffices throughout the strip" and "nE/(8Q) for n>=512"
    print("\n# Part B: r=4 claims")
    badB = 0; badC = 0; tot = 0
    for (r, Q, S, n, t3, tall, tfix, qo, qe, qf) in rows:
        if r != 4: continue
        E = r*Q*S; tot += 1
        ok_quarter = (qf is not None and qf <= E//4)
        if not ok_quarter: badB += 1; print("  E/4 FAILS at", (Q, S, n), fmt(qf, E))
        if n >= 512:
            need = n*E//(8*Q)
            if qf is None or qf > need: badC += 1; print("  nE/(8Q) FAILS at", (Q, S, n), fmt(qf, E), "need <=", fmt(need, E))
    print(f"r=4 rows {tot}: E/4 claim failures {badB}; nE/(8Q) (n>=512) failures {badC}")
    # Part C: asymptotics r=4, n=2Q, qq=E/4 : compare K-height a d'/(rho qq)/E with taumax/E
    print("\n# Part C: r=4, S=64, n=2Q, qq=E/4: K-height/E vs taumax/E (with FIX-2), large Q")
    for Q in [2**k for k in range(7, 21, 2)]:
        r, S, n = 4, 64, 2*Q; E = r*Q*S; h = n*E; rho = Q//2
        tm = min(taumax(r, Q, S, n, dp, True) for dp in range(2*E-2, 2*E+2))
        kh = max((Fr(8*h, 625) - dp + Q*S//2 - rho)*dp/(rho*Fr(E, 4)) for dp in range(2*E-2, 2*E+2))
        print(f"Q=2^{Q.bit_length()-1}: Kheight/E={float(kh/E):.5f}  taumax/E={tm/E:.5f}  ok={kh<=tm}")
    print("limit: K-height/E -> 256/625 = %.5f ; taumax/E -> 1 - 0.2048/(1551/4000-0.0256-0.006) = %.5f" % (256/625, 1 - 0.2048/(1551/4000 - 0.0256 - 0.006)))
