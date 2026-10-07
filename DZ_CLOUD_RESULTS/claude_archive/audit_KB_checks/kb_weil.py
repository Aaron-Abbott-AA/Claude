#!/usr/bin/env python3
"""Referee check of KB sec. 2 counting heuristics (exact integer arithmetic). Usage: python3 -I kb_weil.py [rhomax]
Setting per KB cell (even rho, rho+3 <= g <= 2rho, m/4 integer in [rho - a*, rho]):
  u = 2^{g-2}, Q = 2^{g+rho/2}, q = Q^2, s = 2^{m/4}, v >= q/2 + 1 (v > Q^2/2, EBR Lemma G [A]).
Kummer cover y^e = k(X), k := eta^e in F_q[X], deg k <= e*u (KB (iii) sharpened), e odd.
Riemann-Hurwitz (tame, e odd): 2*genus <= (r0 - 1)(e - 1), r0 = #distinct zeros of k <= e*u.
Hasse-Weil: e*v <= #C(F_q) <= q + 1 + (e*u - 1)(e - 1)*Q.  Contradiction ('Kummer-Weil' excludes e) iff
  e*(q/2 + 1) > q + 1 + (e*u - 1)(e - 1)*Q.
WG (RBL v2.1 [A]): excludes 1 < e < T with T = (4/3)2^{rho/2} - 1 (sqrt q > 3u(e+1)).
Reports: largest e excluded by Kummer-Weil vs T and 2^{rho/2+1}; admissible e (e | s-1, e >= T, e not dividing 2^r - 1
for proper r | m/4) that escape Kummer-Weil (smallest such); Schwartz-Zippel arithmetic 4*D*s^3 < s^4/2 iff D < s/8.
"""
import sys
from fractions import Fraction as Fr
from sympy import divisors

rhomax = int(sys.argv[1]) if len(sys.argv) > 1 else 40
rows = []
viol = 0
for rho in range(10, rhomax + 1, 2):
    T = Fr(4, 3) * 2 ** (rho // 2) - 1
    for g in range(rho + 3, 2 * rho + 1):
        m = 2 * g + rho
        astar = rho - (g + 1) // 2
        if astar < 1 or m % 4 or not (rho - astar <= m // 4 <= rho):
            continue
        u = 2 ** (g - 2); Q = 2 ** (g + rho // 2); q = Q * Q
        s4 = m // 4; s = 2 ** s4
        assert Q * Q == 2 ** m and Q == 4 * u * 2 ** (rho // 2)
        excl = lambda e: e * (q // 2 + 1) > q + 1 + (e * u - 1) * (e - 1) * Q
        # largest odd e >= 3 excluded by Kummer-Weil (monotone window [3, emax])
        e = 3; emax = None
        while excl(e):
            emax = e; e += 2
        # confirm nothing excluded beyond emax up to s-1 (sample check: quadratic in e, so one window)
        for e2 in (e, e + 2, s - 1):
            if e2 <= s - 1 and excl(e2):
                viol += 1; print("non-window", rho, g, e2)
        proper = [r for r in range(1, s4) if s4 % r == 0]
        adm = [d for d in divisors(s - 1) if d >= T and all((2 ** r - 1) % d != 0 for r in proper)]
        esc = [d for d in adm if not excl(d)]
        rows.append((rho, g, s4, float(T), emax, 2 ** (rho // 2 + 1), min(adm) if adm else None,
                     min(esc) if esc else None, len(adm), len(esc)))
        if not esc:
            viol += 1
# Schwartz-Zippel arithmetic
for s in (2 ** k for k in range(4, 40)):
    for D in (s // 8 - 1, s // 8, s // 8 + 1):
        if (4 * D * s ** 3 < s ** 4 // 2) != (D < Fr(s, 8)):
            viol += 1; print("SZ", s, D)
print("rho g m/4 | T | largest e excluded by Kummer-Weil | 2^{rho/2+1} | min admissible e>=T | min admissible e escaping KW | #adm #esc")
for r in rows:
    print(r)
ratio = [r[4] / r[3] for r in rows if r[4]]
print(f"cells: {len(rows)}; ratio (KW max excluded e)/T in [{min(ratio):.3f}, {max(ratio):.3f}]; "
      f"cells where KW excludes some admissible e >= T: {sum(1 for r in rows if r[6] is not None and r[4] and r[6] <= r[4])}; "
      f"cells with no admissible e escaping KW (KB excluded by counting): {sum(1 for r in rows if r[9] == 0)}; violations {viol}")
