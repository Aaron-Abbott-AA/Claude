#!/usr/bin/env python3
"""GX coverage arithmetic (Claude DZ cloud, 7 Oct 2026). Even rho in [10,40] (rho = 4,6,8 closed earlier),
cells rho+3 <= g <= min(2rho, ceil(3rho/2)+2) (not covered by NWF), a* = rho - ceil(g/2) >= 1.
Sufficient gate: no rho' in [rho-a*, rho] divides m/2 = g + rho/2.  Also checks rho - a* - 2 > a* (kernel bound)
for every cell.  Usage: python3 -I gxcells.py"""
import math
tot = gate = kern_fail = 0
fails = []
for rho in range(10, 41, 2):
    for g in range(rho + 3, min(2 * rho, math.ceil(3 * rho / 2) + 2) + 1):
        a = rho - math.ceil(g / 2)
        if a < 1:
            continue
        tot += 1
        if not (rho - a - 2 > a):
            kern_fail += 1
        bad = [r for r in range(rho - a, rho + 1) if (g + rho // 2) % r == 0]
        if bad:
            fails.append((rho, g, a, bad))
        else:
            gate += 1
print(f"cells (a*>=1, not NWF): {tot}; sufficient gate passes: {gate}; gate fails: {len(fails)}; kernel-bound failures: {kern_fail}")
print("gate-failing cells (rho,g,a*,rho'):", fails)
