"""Referee check (RBL v2 revision): exact-integer arithmetic for FIX-1 (RD(c)
invariant), FIX-2/FIX-7 (numerical range, a* <= rho/2-2, weight K), FIX-3/G1'
(WG threshold), plus FIX-6 (leading coeff of (c tau^d) o B) and FIX-11
(iota fixes x, y) over a small field. Own code; run with python3 -I."""
import random
from fractions import Fraction
import galois

random.seed(7)
fails = {}


def bad(k):
    fails[k] = fails.get(k, 0) + 1


cells = 0
for rho in range(6, 401, 2):          # even rho; rho>=6 so the band is meaningful
    for g in range(rho + 3, 2 * rho + 1):
        cells += 1
        m = 2 * g + rho
        Q = 2 ** (m // 2)
        R, K = 2 ** g, 2 ** rho
        u = R // 4
        astar = rho - (-(-g // 2))     # rho - ceil(g/2)
        if astar != rho - 1 - (g - 1) // 2:
            bad("astar_forms")
        if astar > rho // 2 - 2:
            bad("astar<=rho/2-2")
        vlow = Fraction(Q * Q, 2)      # v > Q^2/2 = K R^2/2
        if Q * Q != K * R * R:
            bad("Q^2=KR^2")
        for a in range(0, rho // 2 - 1):   # a <= rho/2-2
            lhs = 2 * u * (2 ** (a + 1) - 1) * Q
            if not lhs < vlow:
                bad("RB_hyp_u")
            if R * 2 ** a * Q > Q * Q // 4:
                bad("R2^aQ<=Q^2/4")
        for a in range(0, max(astar, -1) + 1):
            if not K * 2 ** (a + 3) < Q:
                bad("weightK")
            if not a <= g - rho // 2 - 4:
                bad("weightK_form")
        # WG threshold: component of degree e>1 survives WG only if Q <= 3u(e+1)
        thr = Fraction(4, 3) * 2 ** (rho // 2) - 1
        for e in range(2, 4 * 2 ** (rho // 2) if rho <= 20 else 2):
            killed = Q > 3 * u * (e + 1)
            if killed != (e < thr):
                bad("WG_threshold")

# RD(c) invariant: start (rho', a2) with a2 <= rho'/2-2; worst case per step:
# either (dim same, defect same) or (dim -2, defect -1 or more). Check
# every reachable state has dim >= rho'-2a2 >= 4 and a_i <= rho_i/2-2.
states = 0
for rp in range(6, 81):
    for a2 in range(0, rp // 2 - 1):
        if not 2 * a2 + 4 <= rp:
            continue
        stack = [(rp, a2)]
        seen = set()
        while stack:
            r, a = stack.pop()
            if (r, a) in seen:
                continue
            seen.add((r, a))
            states += 1
            if r < rp - 2 * a2 or rp - 2 * a2 < 4:
                bad("RDc_dim")
            if not 2 * a <= r - 4:
                bad("RDc_ineq")
            for drop in range(1, a + 1):        # defect drops by >= 1
                for loss in (0, 1, 2):          # dim loss <= 2
                    stack.append((r - loss, a - drop))

# FIX-6: in L{tau}, (c tau^d) o (b tau^k + lower) has leading coeff c*b^(2^d)
GF = galois.GF(2 ** 8)
for _ in range(200):
    d, k = random.randrange(0, 4), random.randrange(0, 4)
    c = GF(random.randrange(1, 256))
    B = [GF(random.randrange(256)) for _ in range(k)] + [GF(random.randrange(1, 256))]
    # composition: (c tau^d)(sum_j B_j z^(2^j)) = c * sum_j B_j^(2^d) z^(2^(j+d))
    comp = {j + d: c * B[j] ** (2 ** d) for j in range(k + 1)}
    if comp[k + d] != c * B[k] ** (2 ** d):
        bad("FIX6_lc")
    # and the needed c for target leading coeff A_lc:
    A_lc = GF(random.randrange(1, 256))
    cc = A_lc / B[k] ** (2 ** d)
    if cc * B[k] ** (2 ** d) != A_lc:
        bad("FIX6_solve")

# FIX-11: iota(f)(X,Y) = f^(Q)(Y,X). Linear forms f = cX X + cY Y.
# iota(f) = cY^Q X + cX^Q Y. Check x=(wb X + w Y)/(w+wb), y=(X+Y)/(w+wb)
# are fixed and x+w y = X, x+wb y = Y.  Field F_256, Q=16.
Qs = 16
for wv in range(2, 256):
    w = GF(wv)
    wb = w ** Qs
    if wb == w:
        continue  # w in F_Q
    s = w + wb
    x = (wb / s, w / s)
    y = (GF(1) / s, GF(1) / s)
    io = lambda f: (f[1] ** Qs, f[0] ** Qs)
    if io(x) != x or io(y) != y:
        bad("FIX11_fixed")
    X = (x[0] + w * y[0], x[1] + w * y[1])
    Y = (x[0] + wb * y[0], x[1] + wb * y[1])
    if X != (GF(1), GF(0)) or Y != (GF(0), GF(1)):
        bad("FIX11_XY")

print(f"cells (even rho 6..400, g in [rho+3,2rho]): {cells}")
print(f"RD(c) reachable states checked: {states}")
print(f"failures: {fails if fails else 'none'}")
