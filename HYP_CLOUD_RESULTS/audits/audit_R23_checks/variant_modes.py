# variant_modes.py -- referee: which ingredient drives Cor 3.3?  Monkey-patches the referee solver's mode table.
# Run: python3 -I variant_modes.py
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import indep_recount_R20_R23 as M
from fractions import Fraction as Fr
orig = M.mode_params
def cdiv(a, b): return -((-a)//b)
def patched(mode, E, X, rq):
    if mode == "m_only_EX":      # R22 Cor 3.2 inserted into R20 Lemma 4.2 only (m), residual count unchanged
        k = max(1, cdiv(E - X, rq)); return min(rq*k, E), 1
    if mode == "N1_only_N0":     # R22 Remark 5.6 only (tau0-N_0), m as in R20
        return min(rq, E), max(1, cdiv(E - X, rq))
    if mode == "m_only_E":       # R23 m=E without N1
        return E, 1
    return orig(mode, E, X, rq)
M.mode_params = patched
for mode in ("m_only_EX", "N1_only_N0", "m_only_E"):
    res = {}
    for r in (4, 8, 16):
        for Q in (128, 1024, 16384):
            for S in (64, 256, 4096):
                l, lnv, bits, _ = M.least_qq(r, Q, S, 256, mode)
                res.setdefault(r, set()).add(M.label(l, lnv, r*Q*S, Q) + ("" if l != 128 else "[all]"))
    print(mode, {r: sorted(v) for r, v in res.items()})
