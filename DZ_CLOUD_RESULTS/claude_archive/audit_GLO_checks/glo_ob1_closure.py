#!/usr/bin/env python3
"""Referee check (GLO audit): Corollary OB1(b),(c) over the ALGEBRAIC CLOSURE (not just inside a base field).
Run:  nice -n 19 python3 -I glo_ob1_closure.py <seed>

a2 = 1, A = a0 + a1 tau.  The tau^0 and tau^2 equations force a0 in {0} u r0 F_Q^*  (r0^{Q-1} = y0 = c0/d0) and
a1 in {0} u r1 F_Q^*  (r1^{2(Q-1)} = c1/d1).  All these Kummer roots lie in the big field F listed below
(checked), so enumerating the finite candidate sets decides EXACTLY whether a nonzero solution of degree <= 1
exists over the algebraic closure.  This is compared with  Delta*Omega1 == 0  (OB1(c)) and the degree-0 part
(a1 = 0) with  Delta == 0  (OB1(b)).
Bases:  Q = 4, base GF(2^6) (contains F_4, not F_16), big field GF(2^18);
        Q = 4, base GF(2^4)  (pointwise-type control, contains F_16), big field GF(2^12);
        Q = 8, base GF(2^3)  (= F_8), big field GF(2^21)  -- exhaustive over all (c0,c1,d0,d1) in (F_8^*)^4."""
import sys, random, itertools
import galois

def setup(N_base, N_big, Q):
    Fb = galois.GF(2 ** N_big)
    k = (2 ** N_big - 1) // (2 ** N_base - 1)
    g = Fb.primitive_element
    base = [Fb(0)] + [g ** (k * i) for i in range(2 ** N_base - 1)]   # embedded subfield
    FQs = [x for x in base if x != 0 and x ** Q == x]
    kq = (2 ** N_big - 1) // (Q - 1)
    FQs = [g ** (kq * i) for i in range(Q - 1)]
    return Fb, g, base, FQs

def kroot(Fb, g, y, e):
    """one x with x^e = y (y != 0), via discrete log; asserts existence in Fb."""
    L = int(y.log())
    N = 2 ** Fb.degree - 1
    from math import gcd
    d = gcd(e, N)
    assert L % d == 0, "root not in big field"
    # solve e*t = L mod N
    t = (L // d) * pow(e // d, -1, N // d) % (N // d)
    x = g ** t
    assert x ** e == y
    return x

def test(C, D, Fb, g, FQs, Q):
    c0, c1 = C; d0, d1 = D
    r0 = kroot(Fb, g, c0 / d0, Q - 1)
    r1 = kroot(Fb, g, c1 / d1, 2 * (Q - 1))
    A0s = [Fb(0)] + [r0 * z for z in FQs]
    A1s = [Fb(0)] + [r1 * z for z in FQs]
    sol = deg0 = False
    for a0 in A0s:
        for a1 in A1s:
            if a0 == 0 and a1 == 0: continue
            e0 = c0 * a0 + d0 * a0 ** Q
            e1 = c0 * a1 + c1 * a0 ** 2 + d0 * a1 ** Q + d1 * a0 ** (2 * Q)
            e2 = c1 * a1 ** 2 + d1 * a1 ** (2 * Q)
            if e0 == 0 and e1 == 0 and e2 == 0:
                sol = True
                if a1 == 0: deg0 = True
    Dl = c1 * d0 ** 2 + d1 * c0 ** 2
    Om = c0 ** 4 * d1 ** Q * Dl ** (Q - 1) + c1 * d0 ** (4 * Q)
    return sol, deg0, (Dl * Om == 0), (Dl == 0), (Dl != 0 and Om == 0)

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261007
    rng = random.Random(seed)
    print(f"glo_ob1_closure seed={seed} galois {galois.__version__}")
    for (Q, Nb, NB, nrand) in [(4, 6, 18, 400), (4, 4, 12, 300), (8, 3, 21, None)]:
        Fb, g, base, FQs = setup(Nb, NB, Q)
        nz = [x for x in base if x != 0]
        st = dict(inst=0, sol=0, deg0=0, omega_branch=0, bad=0)
        def one(C, D):
            sol, deg0, crit, crit0, omb = test(C, D, Fb, g, FQs, Q)
            st['inst'] += 1; st['sol'] += sol; st['deg0'] += deg0; st['omega_branch'] += (omb and sol)
            if sol != crit or deg0 != crit0:
                st['bad'] += 1; print("  MISMATCH", Q, Nb, C, D, sol, deg0, crit, crit0)
        if nrand is None:
            for c0, c1, d0, d1 in itertools.product(nz, repeat=4):
                one((c0, c1), (d0, d1))
        else:
            for t in range(nrand):
                c0, d0, d1 = (rng.choice(nz) for _ in range(3))
                if t % 3 == 0:
                    c1 = rng.choice(nz)
                elif t % 3 == 1:
                    c1 = d1 * c0 ** 2 / d0 ** 2          # Delta = 0
                else:
                    # search c1 with Delta != 0, Omega1 = 0
                    cands = []
                    for c in nz:
                        Dl = c * d0 ** 2 + d1 * c0 ** 2
                        if Dl != 0 and c0 ** 4 * d1 ** Q * Dl ** (Q - 1) + c * d0 ** (4 * Q) == 0:
                            cands.append(c)
                    c1 = rng.choice(cands) if cands else rng.choice(nz)
                one((c0, c1), (d0, d1))
        print(f"Q={Q} base GF(2^{Nb}) big GF(2^{NB}): {st}")

main()
