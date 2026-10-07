#!/usr/bin/env python3
"""Revision check GX v2 (referee, 7 Oct 2026). Independent arithmetic, no owner code.
C1: 200/112/88 cells (even rho in [10,40], rho+3<=g<=min(2rho,ceil(3rho/2)+2), a*>=1).
C2: GO(e) range cells (a* <= (rho-4)/3): 78, 51 gate-passing; all 51 inside GX's 112; 112-51 = 61 outside range.
C3: v2 [P] failure pattern: offending r = N/2 = m/4, gate fails <=> g = rho/2 mod 2 and g <= 3rho/2
    (cells of the full NWF-uncovered window, even rho in [10,1000]); also a* = rho - ceil(g/2) so rho-a* = ceil(g/2).
C4: kernel bound a* <= rho/2-2 over the whole band rho+3<=g<=2rho, even rho in [4,1000].
C5: v2 m5 chain: in gate-failing cells, any t > rho/2 with t | N and t in [rho-a*, rho] equals m/4 > rho/2,
    and 2^(t') - 1 < T = (4/3)2^(rho/2) - 1 for every proper divisor t' of t.
Usage: python3 -I rc_cells.py"""
import math

def cells(rho):
    for g in range(rho + 3, min(2 * rho, math.ceil(3 * rho / 2) + 2) + 1):
        a = rho - math.ceil(g / 2)
        yield g, a

def offending(rho, g, a):
    N = g + rho // 2
    return [r for r in range(rho - a, rho + 1) if N % r == 0]

# C1, C2
tot = gate = 0; gate_set = set(); go_range = go_gate = 0; go_gate_set = set()
for rho in range(10, 41, 2):
    for g, a in cells(rho):
        if a < 1:
            continue
        tot += 1
        ok = not offending(rho, g, a)
        if ok:
            gate += 1; gate_set.add((rho, g))
        if 3 * a <= rho - 4:
            go_range += 1
            if ok:
                go_gate += 1; go_gate_set.add((rho, g))
print(f"C1 cells={tot} gate_pass={gate} gate_fail={tot-gate}")
print(f"C2 GO(e) range={go_range} range&gate={go_gate} subset_of_GX={go_gate_set <= gate_set} "
      f"gate_pass_outside_range={len(gate_set - go_gate_set)}")
# C3
mism = 0; nonm4 = 0; acheck = 0; ncell = 0; a0 = 0
for rho in range(10, 1001, 2):
    for g, a in cells(rho):
        ncell += 1
        if a < 1:
            a0 += 1
        if rho - a != math.ceil(g / 2):
            acheck += 1
        off = offending(rho, g, a)
        N = g + rho // 2
        pred_fail = (N % 2 == 0) and (N // 2 <= rho)
        if bool(off) != pred_fail:
            mism += 1
        if off and off != [N // 2]:
            nonm4 += 1
print(f"C3 cells={ncell} (a*<1: {a0}) closed-form mismatches={mism} offending!=[m/4]: {nonm4} rho-a*!=ceil(g/2): {acheck}")
# C4
bad = 0; nb = 0
for rho in range(4, 1001, 2):
    for g in range(rho + 3, 2 * rho + 1):
        nb += 1
        a = rho - math.ceil(g / 2)
        if not (a <= rho // 2 - 2 and rho - a - 2 > a):
            bad += 1
print(f"C4 band cells={nb} kernel-bound failures={bad}")
# C5
bad5 = 0; n5 = 0
for rho in range(10, 401, 2):
    T = (4 / 3) * 2 ** (rho / 2) - 1
    for g, a in cells(rho):
        N = g + rho // 2
        for t in range(rho // 2 + 1, rho + 1):
            if N % t == 0 and rho - a <= t:
                n5 += 1
                if not (2 * t == N and t > rho / 2):
                    bad5 += 1
                for tp in range(1, t):
                    if t % tp == 0 and not (2 ** tp - 1 < T):
                        bad5 += 1
        # 2^t - 1 >= T forces t > rho/2:
        if not (2 ** (rho // 2) - 1 < T):
            bad5 += 1
print(f"C5 instances={n5} failures={bad5}")
