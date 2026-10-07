#!/usr/bin/env python3
"""Referee check of RB 'Numerical range' and the WG threshold arithmetic (exact integer arithmetic).

For even rho in [4, 400], g in [rho+3, 2rho]: m = 2g+rho, Q = 2^{m/2}, K = 2^rho, R = 2^g, v_lb = K R^2 / 2 (v > v_lb).
 a* = rho - ceil(g/2) (note's form) ; EBR form rho-1-floor((g-1)/2) ; check equal and a* <= rho/2-2.
 (R1) u = R/4: 2u(2^{a+1}-1)Q < v_lb for all 0<=a<=rho/2-2 ; and the note's chain R 2^a Q = 2^{a-rho/2}Q^2 <= Q^2/4.
 (R2) u = K: 2K(2^{a+1}-1)Q < v_lb for all a <= a* ; note's condition a <= g - rho/2 - 4.
 (R3) WG threshold: Q <= 3u(e+1) with u=R/4  <=>  e >= (4/3)2^{rho/2} - 1 ; check smallest killed/unkilled e.
 (R4) RD: rho' - 2 a2 >= 4 whenever a2 <= rho'/2 - 2.
"""
from fractions import Fraction

def main():
    fails = {k: 0 for k in ('aform', 'astar', 'R1', 'R1chain', 'R2', 'R2cond', 'R3')}
    cells = 0
    for rho in range(4, 401, 2):
        for g in range(rho + 3, 2 * rho + 1):
            cells += 1
            m = 2 * g + rho; Q = 2 ** (m // 2); K = 2 ** rho; R = 2 ** g
            assert Q * Q == K * R * R
            vlb = Fraction(K * R * R, 2)
            a_note = rho - (g + 1) // 2
            a_ebr = rho - 1 - (g - 1) // 2
            if a_note != a_ebr: fails['aform'] += 1
            if a_note > rho // 2 - 2: fails['astar'] += 1
            u = R // 4
            for a in range(0, rho // 2 - 1):
                if not (2 * u * (2 ** (a + 1) - 1) * Q < vlb): fails['R1'] += 1
                if not (R * 2 ** a * Q == Fraction(2 ** a, 2 ** (rho // 2)) * Q * Q and R * 2 ** a * Q <= Fraction(Q * Q, 4)):
                    fails['R1chain'] += 1
            for a in range(0, a_note + 1):
                if not (2 * K * (2 ** (a + 1) - 1) * Q < vlb): fails['R2'] += 1
                if not (a <= g - rho // 2 - 4): fails['R2cond'] += 1
            # WG: killed iff Q > 3u(e+1)
            thr = Fraction(4, 3) * 2 ** (rho // 2) - 1
            for e in (int(thr) - 1, int(thr), int(thr) + 1, int(thr) + 2):
                if e < 2: continue
                killed = Q > 3 * u * (e + 1)
                if killed != (e < thr): fails['R3'] += 1
    print(f"cells checked (even rho<=400, rho+3<=g<=2rho): {cells}")
    print(f"failures: {fails}")
    # R4
    bad = sum(1 for rp in range(4, 200) for a2 in range(0, rp // 2 - 1) if rp - 2 * a2 < 4)
    print(f"R4 rho'-2a2>=4 failures: {bad}")

if __name__ == '__main__':
    main()
