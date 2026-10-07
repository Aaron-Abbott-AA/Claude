#!/usr/bin/env python3
"""PTH/GO arithmetic (Claude DZ cloud, 7 Oct 2026). Even rho in [10,40], g in [rho+3, min(2rho, ceil(3rho/2)+2)]
(cells not covered by NWF). Lists cells with a* = rho - ceil(g/2) <= (rho-4)/3 and the sufficient gate
'no rho' in [rho-a*, rho] divides g + rho/2'. Usage: python3 -I gocells.py"""
import math
n_range = n_gate = 0
for rho in range(10, 41, 2):
    out = []
    for g in range(rho + 3, min(2 * rho, math.ceil(3 * rho / 2) + 2) + 1):
        a = rho - math.ceil(g / 2)
        if 3 * a > rho - 4:
            continue
        n_range += 1
        bad = [r for r in range(rho - a, rho + 1) if (g + rho // 2) % r == 0]
        if not bad:
            n_gate += 1
        out.append(f"({g},a*={a},{'gate-ok' if not bad else 'gate-fails:' + ','.join(map(str, bad))})")
    print(f"rho={rho}: " + ' '.join(out))
print(f"cells with a* <= (rho-4)/3: {n_range}; of these passing the sufficient gate: {n_gate}")
