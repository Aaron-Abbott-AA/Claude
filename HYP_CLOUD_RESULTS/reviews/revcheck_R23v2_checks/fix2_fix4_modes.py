# FIX-2 / FIX-4 / N5: least closing dyadic qq per (r,n,Q,S) row in five modes, exact.
#  R20     : m=min(rho qq,E), N1=1                       (must reproduce R20 v2.1 table)
#  R23     : m=E, N1=ceil(E/(rho qq))                     (Prop 2.1 bootstrap)
#  R22ceil : m=min(rho qq ceil((E-X)/(rho qq)),E), N1=1   (R22 Cor 3.2 exactly as stated there)
#  EXplain : m=E-X, N1=1                                  (literal 'm>=E-X' of Prop 3.2 weaker form, nothing else)
#  EXmax   : m=max(min(rho qq,E),E-X), N1=1               (R20's own m together with E-X)
import sys, os, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rc_bounds import *

MODES = ["R20", "R23", "R22ceil", "EXplain", "EXmax"]

def closed(r, Q, S, n, qq, mode):
    E = r*Q*S
    for dp in range(2*E-2, 2*E+5):
        fs, P = failing(r, Q, S, n, dp, qq, mode)
        if fs: return False
    return True

def tau_hi_max(r, Q, S, n, qq):
    E = r*Q*S
    return max(setup(r, Q, S, n, dp, qq, "R20")["tau_hi"] for dp in range(2*E-2, 2*E+5))

def profile(r, Q, S, n, mode):
    """closed flags for qq=2^k, k=0.. until tau_hi<1 for all d'; return least qq from which all larger close"""
    flags = []; k = 0
    while True:
        qq = 2**k
        if tau_hi_max(r, Q, S, n, qq) < 1:
            flags.append((qq, True)); break
        flags.append((qq, closed(r, Q, S, n, qq, mode))); k += 1
    least = None
    for qq, c in reversed(flags):
        if c: least = qq
        else: break
    all128 = all(c for qq, c in flags if qq >= 128)
    return least, all128

def fmtq(least, E, Q):
    from fractions import Fraction as F
    return f"{least} (= {F(least*Q, E)}E/Q)"

t0 = time.time()
rows = []
for r in (4, 8, 16):
    for Q in (128, 256, 512, 1024, 2048, 4096, 8192, 16384):
        for S in (64, 256):
            n = 256
            while n < 4*Q and n <= 8192:
                rows.append((r, n, Q, S)); n *= 2
print(f"grid rows: {len(rows)} (incl. Q=8192: {sum(1 for x in rows if x[2]==8192)})")
diffs = {m: 0 for m in MODES}
summary = {}
for (r, n, Q, S) in rows:
    E = r*Q*S
    res = {m: profile(r, Q, S, n, m) for m in MODES}
    summary[(r,n,Q,S)] = res
    line = " ".join(f"{m}:{fmtq(res[m][0],E,Q)}{'*' if res[m][1] else ''}" for m in MODES)
    print(f"r={r:2d} n={n:5d} Q={Q:5d} S={S:3d} | {line}")
print("(* = every dyadic qq>=128 closes)")
for m in ("R22ceil", "EXplain", "EXmax"):
    nd = [k for k in summary if summary[k][m] != summary[k]["R23"]]
    print(f"rows where {m} differs from R23: {len(nd)} {nd[:12]}")
nd = [k for k in summary if summary[k]["R23"] != summary[k]["R20"]]
print(f"rows where R23 differs from R20: {len(nd)}: {sorted(nd)}")
print(f"[grid time {time.time()-t0:.1f}s]")

# B2: 112 cases r in {4,8}, n=256, Q 2^7..2^14, S 2^6..2^12: does every qq>=128 close?
print("=== B2: r in {4,8}, n=256, Q=2^7..2^14, S=2^6..2^12 ===")
for m in ("R23", "R22ceil", "EXplain", "EXmax", "R20"):
    ok = 0; bad = []
    for r in (4, 8):
        for Q in [2**k for k in range(7, 15)]:
            for S in [2**k for k in range(6, 13)]:
                l, a128 = profile(r, Q, S, 256, m)
                if a128: ok += 1
                else: bad.append((r, Q, S, l))
    print(f"mode {m}: every qq>=128 closes in {ok}/112 cases; failures (r,Q,S,least) first 8: {bad[:8]}")
print(f"[total time {time.time()-t0:.1f}s]")

# FIX-4: tau_hi at the least closing qq in the R20 'none' rows (r=8 n>=2048, r=16 n>=512)
print("=== FIX-4: R20 'none' rows: least closing qq and tau_hi there (max over d') ===")
vals = set()
for (r, n, Q, S), res in sorted(summary.items()):
    if (r == 8 and n >= 2048) or (r == 16 and n >= 512):
        l = res["R20"][0]; th = tau_hi_max(r, Q, S, n, l)
        vals.add(th)
        print(f"r={r} n={n} Q={Q} S={S}: least closing qq=2^{l.bit_length()-1}, tau_hi there={th}")
print("set of tau_hi values at least closing qq:", sorted(vals))
