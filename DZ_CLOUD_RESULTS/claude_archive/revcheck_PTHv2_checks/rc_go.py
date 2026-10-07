#!/usr/bin/env python3
"""Revision-check (PTH v2) referee arithmetic for GO's input step and gate. Reads no files. python3 -I rc_go.py
(1) Input step (v2 §4 Setting): for even rho in [4,40], g in [rho+3, 2rho] (380 cells), j = a* = rho - ceil(g/2),
    u = R/4 = 2^{g-2}, Q = 2^{g+rho/2}: max over T in [j+1, rho-1], |T| = rho-2j-2, of
    u[(2^{j+1}-1)(Q+1) + sum_T 2^e]  versus  Q^2/2 = K R^2 / 2 (EBR's lower bound for v).
(2) Gate: recount 78/51/27 over even rho in [10,40], g in [rho+3, min(2rho, ceil(3rho/2)+2)], a* <= (rho-4)/3;
    sufficient gate <=> no admissible U' (dim rho' in [rho-a*, rho]) has stabiliser field F_{2^t} with 2^t - 1 >= T.
"""
import math
from fractions import Fraction as Fr
cells = 0; worst = Fr(0); worst_cell = None; bad = 0; jbad = 0
for rho in range(4, 41, 2):
    for g in range(rho + 3, 2 * rho + 1):
        cells += 1
        j = rho - math.ceil(g / 2)
        assert j == rho - 1 - (g - 1) // 2
        if not (0 <= j <= rho // 2 - 2): jbad += 1
        u = 2 ** (g - 2); Q = 2 ** (g + rho // 2); K = 2 ** rho; R = 2 ** g
        assert Q * Q == K * R * R
        nT = rho - 2 * j - 2
        topT = sum(2 ** e for e in range(rho - nT, rho))       # largest admissible T
        assert rho - nT >= j + 1
        d = u * ((2 ** (j + 1) - 1) * (Q + 1) + topT)
        r = Fr(d, Q * Q // 2)
        if r > worst: worst, worst_cell = r, (rho, g, j)
        if not d <= Q * Q // 2: bad += 1
print(f"(1) cells={cells}  j-range violations={jbad}  bound>Q^2/2 violations={bad}  worst deg/(Q^2/2)={float(worst):.6f} at (rho,g,a*)={worst_cell}")
n = ok = 0; mism = 0; fails = []
for rho in range(10, 41, 2):
    T = Fr(4, 3) * 2 ** (rho // 2) - 1
    for g in range(rho + 3, min(2 * rho, math.ceil(3 * rho / 2) + 2) + 1):
        a = rho - math.ceil(g / 2)
        if 3 * a > rho - 4: continue
        n += 1; h = g + rho // 2
        suff = not any(h % rp == 0 for rp in range(rho - a, rho + 1))
        # exact: exists rho' in range and t | rho', t | h with 2^t - 1 >= T  (U' = F_{2^t}-space of dim rho')
        exact_bad = any(rp % t == 0 and h % t == 0 and 2 ** t - 1 >= T
                        for rp in range(rho - a, rho + 1) for t in range(1, rp + 1))
        if suff == exact_bad: mism += 1
        if suff: ok += 1
        else: fails.append((rho, g))
print(f"(2) range cells={n} gate-pass={ok} gate-fail={n-ok} sufficient-vs-stabiliser mismatches={mism}")
print(f"    first gate failures: {fails[:8]}")
print(f"    listed in v2 present: {[c in fails for c in [(10,15),(14,21),(16,24),(18,27),(20,30)]]}")
