# Revision-check KB v2: arithmetic of KB(i) a2-bound, KB(iii) Moore bound, KB(vi) Kummer-Weil window,
# and the "37 of 88" / "e = N' survives" claims of section 2. Exact integer arithmetic only.
from fractions import Fraction
from math import ceil

from sympy import divisors

def ordmod2(e):
    if e == 1: return 1
    k, x = 1, 2 % e
    while x != 1:
        x = (2 * x) % e; k += 1
    return k

def contradiction(e, rho, g):
    # Weil with v >= q/2+1 places totally split into e degree-1 places, genus 2g' <= (eu-1)(e-1)
    m = 2 * g + rho; q = 2 ** m; Q = 2 ** (m // 2); u = 2 ** (g - 2)
    v = q // 2 + 1
    return e * v > q + 1 + (e * u - 1) * (e - 1) * Q

viol = []
# (A) general even rho <= 200, all band cells: closed-form window [3, 2K-3] exact, Q = 4u 2^{rho/2}
nbig = 0
for rho in range(6, 201, 2):
    K = 2 ** (rho // 2)
    for g in range(rho + 3, 2 * rho + 1):
        m = 2 * g + rho; Q = 2 ** (m // 2); u = 2 ** (g - 2)
        if Q != 4 * u * K: viol.append(("Q", rho, g))
        astar = rho - ceil(g / 2)
        if astar > rho // 2 - 2: viol.append(("astar", rho, g))
        if m % 4: continue
        if not (m // 4 <= rho and m // 4 >= rho - astar): continue   # KB-admitting gate-failing
        nbig += 1
        # concavity: test endpoints and just outside
        if not (contradiction(3, rho, g) and contradiction(2 * K - 3, rho, g)): viol.append(("win-in", rho, g))
        if contradiction(2 * K - 1, rho, g): viol.append(("win-out", rho, g))
        s = 2 ** (m // 4); Np = s - 1
        if contradiction(Np, rho, g): viol.append(("Nprime", rho, g))
        if Np < 2 ** (rho // 2 + 2): viol.append(("Np>=", rho, g))
        for a2 in range(0, astar + 1):
            if m // 4 >= rho - a2:
                if a2 < Fraction(3 * rho - 2 * g, 4): viol.append(("a2bound", rho, g, a2))
                if a2 + 1 > m // 4 - 3: viol.append(("moore+3", rho, g, a2))
                if Fraction(3 * rho - 2 * g, 4) < 0: viol.append(("neg", rho, g))
        # subfield bound
        if 2 ** (m // 8) - 1 >= Fraction(4, 3) * K - 1: viol.append(("subfield", rho, g))
print("general cells rho<=200 admitting KB:", nbig, "violations:", len(viol), viol[:5])

# (B) GX census: rho in [10,40], rho+3 <= g <= min(2rho, ceil(3rho/2)+2), a* >= 1, gate fails
cells = []; hit = 0; rows = []
for rho in range(10, 41, 2):
    K = 2 ** (rho // 2); T = Fraction(4, 3) * K - 1
    for g in range(rho + 3, min(2 * rho, ceil(3 * rho / 2) + 2) + 1):
        astar = rho - ceil(g / 2)
        if astar < 1: continue
        m = 2 * g + rho; N = m // 2
        fails = any(N % r == 0 for r in range(rho - astar, rho + 1))
        if not fails: continue
        cells.append((rho, g))
        mq = m // 4; s = 2 ** mq
        adm = [e for e in divisors(s - 1) if e >= T and ordmod2(e) == mq]
        exc = [e for e in adm if contradiction(e, rho, g)]
        # exact window among odd e in [1, 4K]: f is concave in e, so the contradiction set is an interval;
        # locate its ends by bisection-free scan of the boundary near 1 and near 2K
        lo = 3 if contradiction(3, rho, g) and not contradiction(1, rho, g) else None
        hi = None
        if lo:
            a, b = 3, 4 * K + 1   # contradiction at a, not at b (b odd)
            if contradiction(b, rho, g): hi = 'beyond'
            else:
                while b - a > 2:
                    c = (a + b) // 2
                    if c % 2 == 0: c += 1
                    if c >= b: c -= 2
                    if contradiction(c, rho, g): a = c
                    else: b = c
                hi = a
        if (lo, hi) != (3, 2 * K - 3): viol.append(("window", rho, g, lo, hi))
        if not adm or (s - 1) not in adm or (s - 1) in exc: viol.append(("Nsurv", rho, g))
        if exc: hit += 1
        rows.append((rho, g, mq, float(T), 2 * K - 3, len(adm), exc))
print("gate-failing cells:", len(cells), " cells with some admissible e excluded:", hit)
print("ratio (2K-1)/T range:", min((2*2**(r//2)-1)/(4/3*2**(r//2)-1) for r in range(10,41,2)),
      max((2*2**(r//2)-1)/(4/3*2**(r//2)-1) for r in range(10,41,2)))
for r in rows[:12]: print(r)
print("total violations:", len(viol), viol[:5])
