#!/usr/bin/env python3
"""Referee check (GLO audit): Corollary AC (tower collapse) in a finite-field model.
Run:  nice -n 19 python3 -I glo_ac.py <seed>

GR/AC are pure Galois theory over any base field L of char 2 containing F_Q, so a finite base F0 is a valid model:
if a nonzero polynomial solution exists over the closure, then every coefficient alpha_k of a formal solution
lies in F0(alpha_0).  Model: Q = 4, F0 = GF(2^6), big field GF(2^18) (contains all cube roots of F0^*).
a2 = 1; existence over the closure decided EXACTLY as in glo_ob1_closure.py (degree <= 1 candidates), or by
planting.  For instances with a solution: compute alpha_1..alpha_3 by solving d0 x^Q + c0 x = r_k inside
F0(alpha_0) (= GF(2^6) or GF(2^18)); AC predicts a root always exists there.  For instances without a degree-<=1
solution we only record how often the tower leaves F0(alpha_0) (shows the test discriminates)."""
import sys, random
import numpy as np
import galois

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261007
    rng = random.Random(seed)
    Q, Nb, NB = 4, 6, 18
    F = galois.GF(2 ** NB)
    g = F.primitive_element
    kb = (2 ** NB - 1) // (2 ** Nb - 1)
    base = [g ** (kb * i) for i in range(2 ** Nb - 1)]
    kq = (2 ** NB - 1) // (Q - 1)
    FQs = [g ** (kq * i) for i in range(Q - 1)]
    allF = F.elements
    small = allF[(allF ** (2 ** Nb)) == allF]          # GF(2^6) inside GF(2^18)
    def kroot(y, e):
        L = int(y.log()); N = 2 ** NB - 1
        from math import gcd
        d = gcd(e, N); assert L % d == 0
        t = (L // d) * pow(e // d, -1, N // d) % (N // d)
        return g ** t
    st = dict(sol_inst=0, ac_ok=0, ac_fail=0, nosol_inst=0, nosol_leaves=0, a0_in_base=0)
    for t in range(240):
        c0, d0, d1 = (rng.choice(base) for _ in range(3))
        c1 = rng.choice(base) if t % 2 else d1 * c0 ** 2 / d0 ** 2   # half with Delta = 0 (degree-0 solution)
        if t % 4 == 1:
            # try to force Delta != 0, Omega1 = 0
            cands = [c for c in base if (c * d0 ** 2 + d1 * c0 ** 2) != 0 and
                     c0 ** 4 * d1 ** Q * (c * d0 ** 2 + d1 * c0 ** 2) ** (Q - 1) + c * d0 ** (4 * Q) == 0]
            if cands: c1 = rng.choice(cands)
        r0 = kroot(c0 / d0, Q - 1); r1 = kroot(c1 / d1, 2 * (Q - 1))
        sol = False
        for a0 in [F(0)] + [r0 * z for z in FQs]:
            for a1 in [F(0)] + [r1 * z for z in FQs]:
                if a0 == 0 and a1 == 0: continue
                if c0 * a1 + c1 * a0 ** 2 + d0 * a1 ** Q + d1 * a0 ** (2 * Q) == 0: sol = True
        al0 = r0
        inbase = bool(al0 ** (2 ** Nb) == al0)
        dom = small if inbase else allF
        ell = d0 * dom ** Q + c0 * dom
        al = [al0]; leaves = False
        for k in range(1, 4):
            j = k - 1
            r = c1 * al[j] ** 2 + d1 * al[j] ** (2 * Q)
            idx = np.nonzero(ell == r)[0]
            if len(idx) == 0: leaves = True; break
            al.append(dom[int(rng.choice(list(idx)))])
        if sol:
            st['sol_inst'] += 1; st['a0_in_base'] += inbase
            if leaves: st['ac_fail'] += 1; print("  AC FAIL", c0, c1, d0, d1)
            else: st['ac_ok'] += 1
        else:
            st['nosol_inst'] += 1; st['nosol_leaves'] += leaves
    print(f"glo_ac seed={seed}: {st}")

main()
