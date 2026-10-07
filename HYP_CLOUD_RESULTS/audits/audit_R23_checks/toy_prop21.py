# toy_prop21.py -- referee toys for R23 Prop 2.1 (exact, GF(2^8) via galois).  Run: python3 -I toy_prop21.py
# Toy A: (1.1) for a genuinely NON-CONSTANT twist on the affine line: with c(u) solving the slope
#        equation c^t A(u) c^[Q]=0, the order at v=u of v -> c^t A(v) c^[Q] is a positive multiple of rho*qq.
# Toy B: the scalar congruence (2.1)  t^{X-rho} a'(t) + t^X s(t)/F(t) == 0 mod t^X  with ord F=e, ord s=nu,
#        solved as a linear system for a' over GF(2^8): solvable iff nu >= e-rho.  Combined with
#        nu in rho*qq*Z and Cor 3.2 (nu>=E-X) the surviving nu are >= E for qq>=2; control qq=1 shows
#        Step 5 (divisibility) is what lifts E-rho to E.
import random
import numpy as np
import galois

GF = galois.GF(2**8)
random.seed(7)

def rand_poly(deg):
    return galois.Poly([random.randrange(256) for _ in range(deg + 1)], field=GF)

def frob_poly(p, k):
    """p(x)^k for k a power of 2 (Frobenius on coefficients and x)"""
    return p ** k

print("== Toy A: non-constant twist, divisibility of nu_u ==")
for (rho, Q, qq) in [(2, 4, 4), (4, 8, 2), (2, 4, 8)]:
    k = rho * qq
    tested = 0; ok = 0; orders = {}
    for trial in range(40):
        that = [[rand_poly(2), rand_poly(2)], [rand_poly(2), rand_poly(2)]]
        # A = (T^t)^[rho], T = That^[qq]  => A_ij = that_ji^(rho*qq)
        A = [[frob_poly(that[j][i], k) for j in range(2)] for i in range(2)]
        if all(A[i][j].degree == 0 for i in range(2) for j in range(2)):
            continue
        for _ in range(6):
            u = GF(random.randrange(256))
            a11, a12, a21, a22 = A[0][0](u), A[0][1](u), A[1][0](u), A[1][1](u)
            # c=(1,y): a11 + a12 y^Q + a21 y + a22 y^{Q+1} = 0
            # NB: build distinct elements and assign (in-place += on a shared 0-d GF array would alias)
            coeffs = [GF(0) for _ in range(Q + 2)]
            coeffs[0] = coeffs[0] + a11; coeffs[Q] = coeffs[Q] + a12
            coeffs[1] = coeffs[1] + a21; coeffs[Q + 1] = coeffs[Q + 1] + a22
            assert all(galois.Poly(coeffs[::-1], field=GF)(yy) == a11 + a12 * yy ** Q + a21 * yy + a22 * yy ** (Q + 1)
                       for yy in (GF(3), GF(77)))
            P = galois.Poly(coeffs[::-1], field=GF)
            if P == 0: continue
            roots = P.roots()
            for y in roots:
                c1, c2 = GF(1), y
                Xi = (A[0][0] * (c1 * c1 ** Q) + A[0][1] * (c1 * c2 ** Q) + A[1][0] * (c2 * c1 ** Q) + A[1][1] * (c2 * c2 ** Q))
                if Xi == 0:
                    continue
                # order at x=u
                lin = galois.Poly([1, u], field=GF)  # x - u = x + u
                m = 0; R = Xi
                while R % lin == 0:
                    R = R // lin; m += 1
                tested += 1
                orders[m] = orders.get(m, 0) + 1
                if m >= 1 and m % k == 0: ok += 1
    print("  rho=%d Q=%d qq=%d: %d (u,c(u)) tested, nu_u a positive multiple of rho*qq=%d in %d; order histogram %s"
          % (rho, Q, qq, tested, k, ok, dict(sorted(orders.items()))))

print("== Toy B: congruence (2.1) solvability and the divisibility lift ==")
def solvable(X, rho, e, nu, trials=3):
    """random F=t^e*unit, s=t^nu*unit; is there a' (deg<X) with t^{X-rho}a' + t^X s/F == 0 mod t^X ?"""
    res = set()
    for _ in range(trials):
        # power series mod t^(2X+e+5)
        L = X + 2   # only w[0..X-1] is ever used
        Fu = [GF(random.randrange(1, 256))] + [GF(random.randrange(256)) for _ in range(L)]
        Su = [GF(random.randrange(1, 256))] + [GF(random.randrange(256)) for _ in range(L)]
        # w = Su/Fu as power series
        inv = [GF(0)] * L; inv[0] = GF(1) / Fu[0]
        for i in range(1, L):
            acc = GF(0)
            for j in range(1, i + 1):
                acc += Fu[j] * inv[i - j]
            inv[i] = -acc / Fu[0]
        w = [GF(0)] * L
        for i in range(L):
            acc = GF(0)
            for j in range(i + 1):
                acc += Su[j] * inv[i - j]
            w[i] = acc
        # eps = t^X * t^nu * w / t^e = t^(X+nu-e) w ; need nu+X-e >= 0 for eps in k[[t]] (Thm 3.1(i))
        sh = X + nu - e
        if sh < 0:
            res.add(False); continue
        eps = [GF(0)] * X
        for i in range(X):
            if 0 <= i - sh < L: eps[i] = w[i - sh]
        # unknown a'_0..a'_{X-1}; coefficient i of t^{X-rho} a' is a'_{i-(X-rho)}
        # equations i=0..X-1 : [i>=X-rho] a'_{i-X+rho} + eps_i = 0
        okk = all(eps[i] == 0 for i in range(X - rho))
        res.add(okk)
    assert len(res) == 1
    return res.pop()

for (rho, S, r) in [(2, 4, 4), (4, 4, 4), (2, 8, 4), (4, 2, 8)]:
    X = rho * S; E = 2 * r * X
    for e in (E, E + 1):
        sol = [nu for nu in range(E - X, e) if solvable(X, rho, e, nu)]
        pred = [nu for nu in range(E - X, e) if nu >= e - rho]
        line = "  rho=%d S=%d r=%d X=%d E=%d e=%d: nu<e solvable = %s (pred nu>=e-rho: %s)" % (rho, S, r, X, E, e, sol == pred, sol[:3])
        for qq in (1, 2, S):
            surv = [nu for nu in sol if nu % (rho * qq) == 0]
            line += " | qq=%d min surviving nu<e: %s" % (qq, (min(surv) - E) if surv else None)
        print(line + "  (values relative to E)")
