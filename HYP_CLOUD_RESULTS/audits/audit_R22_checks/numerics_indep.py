# numerics_indep.py -- referee R22 (independent of the owner's numerics_R22.py).
# Exact Fraction evaluation of the six printed counts of HYP_M2_ROUND22_owner_v1.md:
#   Cor 4.1, Cor 4.2, Thm 5.3(i), Thm 5.3(ii), Prop 5.5 classical (r_V=3, N0-eps_top=1), Prop 5.5 pencil.
# Normalisation (R16-R21): N < 16h/625, M' < 8h/625, a = M'+X-rho-d' (<= 8h/625+X-rho-d'), d = E+2,
# d' in [2E-2, 2E+4], d_def <= q/1000, deg psi <= (E+1)d, 2g-2 <= d^2-3d, rho*deg[T] <= Nd+rho*d, qq >= 128.
# Two variants: (V1) the owner's conservative a < 8h/625, d' = 2E+4; (V2) exact a = 8h/625+X-rho-d' scanned over
# every d' in [2E-2,2E+4] (worst case reported).  Grid: r in {4..128}, Q in {2^7..2^14} (incl. 8192),
# S in {2^6..2^13}, dyadic n in [256, 2Q]  (2Q = largest dyadic n < 4Q).
# Also: term-by-term monotonicity check along every grid edge, and the Cor 5.4 thresholds.
# Run: python3 -I numerics_indep.py
from fractions import Fraction as F

TARGET = F(1551, 4000)


def counts(r, Q, S, n, dp=None, exact_a=False):
    E = r * Q * S
    h = n * E
    q = n * E * E
    d = E + 2
    if dp is None:
        dp = 2 * E + 4
    rho = F(Q, 2)
    X = F(Q * S, 2)
    T = Q * S
    N = F(16 * h, 625)
    Mp = F(8 * h, 625)
    a = (Mp + X - rho - dp) if exact_a else Mp
    a = max(a, F(0))
    Exc = F(3, 2) * d * d + F(7, 2) * d + 1
    bnd = 6 * F(q, 1000) + 7
    psi = (E + 1) * d
    rho_degT = N * d + rho * d
    degT = rho_degT / rho
    g2 = d * d - 3 * d
    charges = N * d + 2 * degT / 128 + Exc + bnd
    tau0 = degT / 128
    aprime = max(Mp + Q - T - dp, F(0)) if exact_a else Mp
    terms = {}
    terms['4.1'] = [N * d, Exc, 2 * psi, (Q + 1) * a * dp / (X - rho), bnd]
    terms['4.2'] = [N * d, Exc, psi, (Q + 1) * aprime * dp / rho, bnd]
    terms['5.3i'] = [charges, 2 * psi + 2 * a * dp + 2 * rho_degT]
    terms['5.3ii'] = [charges, psi, a * dp, rho_degT, g2, 2 * psi]
    terms['5.5cl'] = [charges, 2 * psi, 6 * g2, 4 * tau0]
    terms['5.5pe'] = [charges, 2 * psi, g2, 2 * tau0]
    return {k: [F(x) / q for x in v] for k, v in terms.items()}


KEYS = ['4.1', '4.2', '5.3i', '5.3ii', '5.5cl', '5.5pe']
PRINTED = {'4.1': F(33259609702489, 721554505728000), '4.2': F(3194487655227, 34359738368000),
           '5.3i': F(32480243592761, 219902325555200), '5.3ii': F(114684856407837, 1099511627776000),
           '5.5cl': F(75571916082327, 1099511627776000), '5.5pe': F(27044774933549, 549755813888000)}
PRINTED_DEC = {'4.1': '0.046095 (Cor 4.1 text) / 0.046094 (table)', '4.2': '0.092972', '5.3i': '0.147703',
               '5.3ii': '0.104305', '5.5cl': '0.068732', '5.5pe': '0.049194'}


def grid():
    for r in (4, 8, 16, 32, 64, 128):
        for v in range(7, 15):
            Q = 1 << v
            for s in range(6, 14):
                S = 1 << s
                n = 256
                while n <= 2 * Q:
                    yield (r, Q, S, n)
                    n *= 2


def main():
    print("referee numerics_indep: exact Fractions; target 1551/4000 =", float(TARGET))
    for variant, exact_a in (("V1 (owner normalisation: a<8h/625, d'=2E+4)", False),
                             ("V2 (a=8h/625+X-rho-d', worst d' in [2E-2,2E+4])", True)):
        mx = {k: (F(0), None) for k in KEYS}
        rows = 0
        for (r, Q, S, n) in grid():
            E = r * Q * S
            dps = [2 * E + 4] if not exact_a else list(range(2 * E - 2, 2 * E + 5))
            for dp in dps:
                c = counts(r, Q, S, n, dp, exact_a)
                rows += 1
                for k in KEYS:
                    val = sum(c[k])
                    if val > mx[k][0]:
                        mx[k] = (val, (r, Q, S, n, dp - 2 * E))
        print(f"== {variant}: rows={rows}")
        for k in KEYS:
            v, arg = mx[k]
            print(f"  {k:6s} max={float(v):.8f} at (r,Q,S,n,d'-2E)={arg}  <1551/4000: {v < TARGET}  margin={float(TARGET - v):.6f}")
    # corner exact values vs owner's printed fractions
    c = counts(4, 128, 64, 256)
    print("== corner (4,128,64,256), V1:")
    for k in KEYS:
        v = sum(c[k])
        print(f"  {k:6s} {v} = {float(v):.10f}; owner fraction equal: {v == PRINTED[k]}; printed decimal {PRINTED_DEC[k]}")
    # monotonicity: each TERM non-increasing when any one of r,Q,S,n doubles (V1), on the whole grid
    bad = 0
    checked = 0
    pts = set(grid())
    for (r, Q, S, n) in pts:
        base = counts(r, Q, S, n)
        for nb in ((2 * r, Q, S, n), (r, 2 * Q, S, n), (r, Q, 2 * S, n), (r, Q, S, 2 * n)):
            if nb not in pts:
                continue
            cn = counts(*nb)
            for k in KEYS:
                for i, (x, y) in enumerate(zip(base[k], cn[k])):
                    checked += 1
                    if y > x:
                        bad += 1
                        if bad <= 5:
                            print("  monotonicity violation", k, i, (r, Q, S, n), nb, float(x), float(y))
    print(f"== term-wise monotonicity along grid edges: {checked} comparisons, violations: {bad}")
    # Cor 5.4 thresholds
    m1 = sum(counts(4, 128, 64, 256)['5.3i'])
    m2 = sum(counts(4, 128, 64, 256)['5.3ii'])
    print(f"== Cor 5.4 thresholds: 1551/4000 - max(5.3i) = {float(TARGET - m1):.6f}; 1551/4000 - max(5.3ii) = {float(TARGET - m2):.6f}")
    # Cor 4.1: size of the (Q+1)ad'/(X-rho) term vs the FNAO line-factor term (Q+1)a, corner
    E = 4 * 128 * 64
    print(f"== Cor 4.1 slope term / FNAO line term at corner: d'/(X-rho) = {float(F(2*E+4)/(F(128*64,2)-64)):.4f} (~4r)")


if __name__ == '__main__':
    main()
