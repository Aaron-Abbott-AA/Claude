# COMPUTED: residual correspondence for a random paired centre e(U)=sigma1(BU) (Gamma: U^[E].e(U)=0, d=E+2 generically).
# Own conic C_u = {V: u^[E].sigma1(BV)=0}; with a=u^[E] and W=BV it is a0W1W2+a1W0W2+a2W0W1=0,
# parametrised W(t)=(a0 t+a1, t(a0 t+a1), a2 t).  Residual = roots of G(B^{-1}W(t)) after removing the
# base points of e (t=0, a0 t+a1=0, t=inf) and the contact root t_u with its multiplicity.
import sys, random, collections, galois
import numpy as np
E = int(sys.argv[1]); m = int(sys.argv[2]); NU = int(sys.argv[3]); seed = int(sys.argv[4]) if len(sys.argv) > 4 else 3
GF = galois.GF(2**m); P = galois.Poly; rng = random.Random(seed)
while True:
    B = GF([[rng.randrange(2**m) for _ in range(3)] for _ in range(3)])
    if np.linalg.det(B) != 0: break
Bi = np.linalg.inv(B)
def s1(W): return [W[1]*W[2], W[0]*W[2], W[0]*W[1]]
def Gpoly_in_t(a):   # G(V)=V^[E].sigma1(BV) on V=B^{-1}W(t), as Poly in t
    t = P([1, 0], field=GF); one = P([1], field=GF)
    W = [P([int(a[0]), int(a[1])], field=GF), t*P([int(a[0]), int(a[1])], field=GF), P([int(a[2]), 0], field=GF)]
    c = lambda x: P([int(x)], field=GF)
    V = [W[0]*c(Bi[i, 0]) + W[1]*c(Bi[i, 1]) + W[2]*c(Bi[i, 2]) for i in range(3)]
    e = s1(W)
    return sum((V[i]**E * e[i] for i in range(1, 3)), V[0]**E * e[0])
def point():
    while True:
        x1 = GF(rng.randrange(2**m)); y = P([1, 0], field=GF)
        U = [P([1], field=GF), P([int(x1)], field=GF), y]
        c = lambda x: P([int(x)], field=GF)
        W = [U[0]*c(B[i, 0]) + U[1]*c(B[i, 1]) + U[2]*c(B[i, 2]) for i in range(3)]
        e = s1(W); G = sum((U[i]**E * e[i] for i in range(1, 3)), U[0]**E * e[0])
        r = G.roots()
        if len(r): return [GF(1), x1, r[0]]
stats = collections.Counter(); shape = collections.Counter(); cont = collections.Counter(); deg_res = collections.Counter(); sqf = 0
for _ in range(NU):
    u = point(); a = [x**E for x in u]
    G = Gpoly_in_t(a)
    Wu = B @ GF(u)               # u = B^{-1}W(t_u): W(t_u) ∝ Bu  -> t_u = W1/W0
    tu = Wu[1]/Wu[0]
    for lin in [P([1, 0], field=GF), P([int(a[0]), int(a[1])], field=GF)]:
        while G.degree > 0 and G % lin == 0: G = G // lin
    lt = P([1, int(tu)], field=GF); k = 0
    while G % lt == 0: G = G // lt; k += 1
    cont[k] += 1; deg_res[G.degree] += 1
    if k == 0: print("DEGENERATE u=", u, "Bu=", Wu, "a0*tu+a1=", a[0]*tu+a[1], "tu=", tu)
    if galois.gcd(G, G.derivative()).degree == 0: sqf += 1
    G = G // P([int(G.coeffs[0])], field=GF)
    shape[tuple(G.nonzero_degrees.tolist())] += 1
    fs, ds = G.distinct_degree_factors()
    stats[tuple((dd, ff.degree//dd) for ff, dd in zip(fs, ds))] += 1
print(f"random sigma1(BU), E={E}, GF(2^{m}), {NU} points; contact multiplicities {dict(cont)}; residual degrees {dict(deg_res)}; squarefree {sqf}/{NU}")
print("support of residual poly:", dict(shape))
print("distinct-degree patterns (top 6):", dict(stats.most_common(6)), "#patterns", len(stats), "; irreducible:", stats[((E+1,1),)])
