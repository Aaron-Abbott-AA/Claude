#!/usr/bin/env python3
"""Referee check for KB note (arithmetic, exact integers). Usage: python3 -I kb_arith.py [rhomax]
For every even rho in [6, rhomax] and every band cell rho+3 <= g <= 2rho, with a* = rho - ceil(g/2), checks:
 K1  a* <= rho/2 - 2.
 K2  For every a2 in [0, a*]: the set of t with t | m/2, rho/2 < t <= rho, t >= rho - a2 (KB(i) candidates)
     is empty or {m/4}; it is nonempty iff m/4 is an integer with rho - a2 <= m/4 <= rho.
     Record whether the cell is gate-failing (g = rho/2 mod 2, g <= 3rho/2) and whether every candidate case
     lies in a gate-failing cell.
 K3  In KB cells: every proper subfield F_{2^r} of F_s (r | m/4, r < m/4) has 2^r - 1 < T, T = (4/3)2^{rho/2} - 1
     (so chi(G) generates F_s); also T <= N' = s - 1.
 K4  Moore rank condition d+1 <= m/4 for d <= a2 <= a*; and N' >= 2^{rho/2+2}.
 K5  Implicit constraint: KB needs a2 >= rho - m/4 = (3rho - 2g)/4; report cells where this exceeds 0.
 K6  The (GT)-failure chain needs only T; also check 2^t - 1 >= T  =>  t > rho/2 (i.e. 2^{rho/2} - 1 < T).
"""
import sys
from fractions import Fraction as Fr

rhomax = int(sys.argv[1]) if len(sys.argv) > 1 else 200
cells = kbcells = viol = 0
k5 = []
inner = []
for rho in range(6, rhomax + 1, 2):
    T = Fr(4, 3) * 2 ** (rho // 2) - 1
    # K6
    if not (2 ** (rho // 2) - 1 < T):
        viol += 1; print("K6 viol", rho)
    for g in range(rho + 3, 2 * rho + 1):
        m = 2 * g + rho
        astar = rho - (g + 1) // 2
        cells += 1
        if not astar <= rho // 2 - 2:
            viol += 1; print("K1 viol", rho, g)
        gatefail = (g % 2 == (rho // 2) % 2) and (2 * g <= 3 * rho)
        anykb = False
        for a2 in range(0, max(astar, 0) + 1):
            cand = [t for t in range(rho // 2 + 1, rho + 1) if (m // 2) % t == 0 and t >= rho - a2]
            pred = (m % 4 == 0) and (rho - a2 <= m // 4 <= rho)
            if cand and cand != [m // 4]:
                viol += 1; print("K2 cand viol", rho, g, a2, cand)
            if bool(cand) != pred:
                viol += 1; print("K2 pred viol", rho, g, a2, cand)
            if cand:
                anykb = True
                if not gatefail:
                    viol += 1; print("K2 not gatefail", rho, g, a2)
                s4 = m // 4
                s = 2 ** s4
                for r in range(1, s4):
                    if s4 % r == 0 and not (2 ** r - 1 < T):
                        viol += 1; print("K3 subfield viol", rho, g, r)
                if not T <= s - 1:
                    viol += 1; print("K3 T>N'", rho, g)
                if not a2 + 1 <= s4:
                    viol += 1; print("K4 Moore viol", rho, g, a2)
                if not s - 1 >= 2 ** (rho // 2 + 2):
                    viol += 1; print("K4 N' viol", rho, g)
        if anykb:
            kbcells += 1
            lb = Fr(3 * rho - 2 * g, 4)
            if lb > 0:
                k5.append((rho, g, astar, int(lb)))
            if 2 * g == 3 * rho:
                inner.append((rho, g))
        if gatefail and astar >= 0:
            # GX: gate-failing cells all admit the KB candidate at a2 = a* (m/4 >= ceil(g/2))
            if not ((m % 4 == 0) and (rho - astar <= m // 4 <= rho)):
                viol += 1; print("gatefail but no candidate at a*", rho, g)
print(f"rho in [6,{rhomax}] even: band cells {cells}; cells admitting KB(i) for some a2<=a*: {kbcells}; violations: {viol}")
print("K5: KB cells where KB forces a2 >= (3rho-2g)/4 > 0 (first 12):", k5[:12], "... total", len(k5))
print("inner-resonance KB cells g = 3rho/2 (first 8):", inner[:8], "... total", len(inner))
# list for rho <= 40 with a* >= 1 and g <= ceil(3rho/2)+2, to compare with GX's 88
n88 = 0
for rho in range(10, 41, 2):
    for g in range(rho + 3, min(2 * rho, -(-3 * rho // 2) + 2) + 1):
        astar = rho - (g + 1) // 2
        if astar < 1:
            continue
        m = 2 * g + rho
        if m % 4 == 0 and rho - astar <= m // 4 <= rho:
            n88 += 1
print("gate-failing cells (rho in [10,40], a*>=1, not NWF):", n88)
