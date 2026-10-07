# COMPUTED checks of the own-line correspondence Z on the Fermat model of sigma1 (NOTE_CORRESPONDENCE_ROUTE §1).
# Gamma: U0^n+U1^n+U2^n=0, n=E-1, e=sigma1=(U1U2,U0U2,U0U1). For u in Gamma(F), residual points v of
# l_u = {Y: u^[E].Y=0} on Gamma'=e(Gamma) are the v in Gamma with u^[E].e(v)=0, v!=u.
# Chart v0=1: v2 = u2^E v1/(u0^E v1+u1^E); residual poly R(v1) = (u0^E v1+u1^E)^n (1+v1^n) + u2^(En) v1^n.
import sys, random, collections
import galois
E = int(sys.argv[1]) if len(sys.argv) > 1 else 8
m = int(sys.argv[2]) if len(sys.argv) > 2 else 13
NU = int(sys.argv[3]) if len(sys.argv) > 3 else 60
n = E - 1
GF = galois.GF(2**m); P = galois.Poly
rng = random.Random(1)
def pts(k):
    out = []
    while len(out) < k:
        u1 = GF(rng.randrange(1, 2**m)); rhs = GF(1) + u1**n
        if rhs == 0: continue
        # all n-th roots of rhs in GF (may be none)
        r = P([1] + [0]*(n-1) + [int(rhs)], field=GF).roots()
        for u2 in r:
            if u2 != 0: out.append((GF(1), u1, u2)); break
    return out
stats = collections.Counter(); mults = collections.Counter(); sqf = 0; sym_tests = 0; sym_true = 0; lin_tot = 0
for u in pts(NU):
    u0, u1, u2 = u
    A = P([int(u0**E), int(u1**E)], field=GF)          # u0^E v1 + u1^E
    R = A**n * P([1] + [0]*(n-1) + [1], field=GF) + P([int(u2**(E*n))] + [0]*n, field=GF)
    lin = P([1, int(u1)], field=GF)
    k = 0; Rq = R
    while Rq % lin == 0: Rq = Rq // lin; k += 1
    mults[k] += 1
    if Rq.degree == E - 2 and galois.gcd(Rq, Rq.derivative()).degree == 0: sqf += 1
    fs, ds = Rq.distinct_degree_factors() if Rq.degree > 0 else ([], [])
    stats[tuple((dd, ff.degree//dd) for ff, dd in zip(fs, ds))] += 1
    fac = Rq.factors()[0] if (1 in ds) else []
    # symmetry test on rational residual points
    for f in fac:
        if f.degree == 1:
            v1 = f.roots()[0]
            v2 = u2**E * v1 / (u0**E * v1 + u1**E); v = (GF(1), v1, v2)
            assert GF(1) + v1**n + v2**n == 0
            ev = (v[1]*v[2], v[0]*v[2], v[0]*v[1]); eu = (u1*u2, u0*u2, u0*u1)
            assert sum(u[i]**E * ev[i] for i in range(3)) == 0
            sym_tests += 1; sym_true += int(sum(v[i]**E * eu[i] for i in range(3)) == 0)
print(f"E={E}, GF(2^{m}), {NU} points u on Gamma (d={n}, d'={2*n})")
print("multiplicity of the root v=u in R (= contact of l_u with Gamma' at e(u)):", dict(mults))
print(f"residual polynomial of degree d'-E={E-2} and squarefree: {sqf}/{NU}")
print("distinct-degree patterns (deg, #factors) of the residual polynomial over GF(2^m):", dict(stats))
print(f"symmetry v^[E].e(u)=0 at rational residual points: {sym_true}/{sym_tests}")
