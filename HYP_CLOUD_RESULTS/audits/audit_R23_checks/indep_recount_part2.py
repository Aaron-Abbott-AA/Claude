# indep_recount_part2.py -- referee: B2 grid (112 cases), r=16 diagnostics, vacuity of "none" rows,
# and the m=E-X ("R22only") robustness test.  Imports the referee's own solver.
# Run: python3 -I indep_recount_part2.py   (from the checks/ directory, so the import resolves)
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from indep_recount_R20_R23 import case, least_qq, mode_params
from fractions import Fraction as Fr
from math import floor

def B2(mode):
    bad = []; cnt = 0
    for r in (4, 8):
        for Q in [2 ** i for i in range(7, 15)]:
            for S in [2 ** i for i in range(6, 13)]:
                l, lnv, bits, _ = least_qq(r, Q, S, 256, mode)
                cnt += 1
                if l != 128: bad.append((r, Q, S, bits))
    return cnt, bad

print("== B2: n=256, r in {4,8}, Q=2^7..2^14, S=2^6..2^12 ==")
for mode in ("R23", "R22only"):
    cnt, bad = B2(mode)
    print(mode, "cases", cnt, "all qq>=128 closed:", not bad, bad[:3])
sys.stdout.flush()

print("== r=16, n=256, Q=128, S=64 diagnostics (fail sets of integer tau0) ==")
for mode in ("R23", "R22only", "R20"):
    for qq in (128, 1024, 2048, 4096, 8192):
        for dp_off in (-2, 4):
            E = 16 * 128 * 64
            ok, how, fails = case(16, 128, 64, 256, qq, 2 * E + dp_off, mode)
            print(" %-7s qq=%5d d'=2E%+d closed=%s fails=%s %s" % (mode, qq, dp_off, ok, fails[:3], how))
sys.stdout.flush()

print("== vacuity of the 'none' rows: at the least closing qq, tau_hi per d' ==")
for (r, n, Q, S) in [(16, 512, 256, 64), (16, 512, 16384, 256), (8, 2048, 1024, 64), (16, 8192, 16384, 256), (8, 8192, 16384, 64)]:
    E = r * Q * S; rho = Q // 2; h = n * E; d = E + 2; N = Fr(16 * h, 625)
    l, lnv, bits, res = least_qq(r, Q, S, n, "R20")
    th = []
    for dp in range(2 * E - 2, 2 * E + 5):
        a = Fr(8 * h, 625) - dp + (Q * S) // 2 - rho
        th.append(floor(min(a * dp / (rho * l), (N * d / rho + d) / l)))
    # also the qq just below
    th2 = []
    for dp in range(2 * E - 2, 2 * E + 5):
        a = Fr(8 * h, 625) - dp + (Q * S) // 2 - rho
        th2.append(floor(min(a * dp / (rho * l // 2), (N * d / rho + d) / (l // 2))))
    ok_below = [case(r, Q, S, n, l // 2, dp, "R20") for dp in range(2 * E - 2, 2 * E + 5)]
    print(" r=%d n=%d Q=%d S=%d least closing qq=%d (=%s E/Q); tau_hi there per d'=%s; at qq/2 tau_hi=%s, fails e.g. %s"
          % (r, n, Q, S, l, Fr(l * Q, E), th, th2, [x[2][:1] for x in ok_below][:2]))
