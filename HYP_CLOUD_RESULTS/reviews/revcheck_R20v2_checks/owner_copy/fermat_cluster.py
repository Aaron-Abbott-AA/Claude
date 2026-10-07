# R20 Example 5.2: Xi-zeros cluster on residual fibres ("all or nothing").
# Fermat sigma1, E=8: Gamma: U0^7+U1^7+U2^7=0, residual points of l_u are v_zeta=diag(1,z,z/(1+z))u^[8], z in F_8\{0,1}
# (R19 Ex. 1.6).  Take a twist whose entries are F_2-forms in U0^7,U1^7,U2^7 (invariant under the diagonal F_8^* action):
#   M(U) = [[U0^7, U1^7], [U2^7, U0^7+U1^7]],  so M(v_zeta) = M(u)^[8] for every zeta.
# With c(u)=(sqrt(beta):sqrt(alpha)), alpha=U0^7, beta=U2^7 (R16 sec. 3 Fermat data), Xi(u,v)=det(M(v)c, M(u)c)
# is the same for all six residual v: N_Xi(u) in {0,6} = {0, d'-E}.  Counted over Gamma(GF(2^12)).
# (Toy only: no (K)-pencil, no FN condition; it illustrates that per-point bounds need an exceptional set.)
# Run: python3 -I fermat_cluster.py
import galois
GF = galois.GF(2**12)
E = 8
roots7 = {}
for y in GF.elements:
    roots7.setdefault(int(y**7), []).append(y)
F8 = [g for g in GF.elements if g != 0 and g != 1 and g**8 == g]
def sq(x): return x**(2**11)
def M(u):
    a, b, c = u[0]**7, u[1]**7, u[2]**7
    return [[a, b], [c, a+b]]
def Xi(u, v, c):
    Mu, Mv = M(u), M(v)
    w1 = [Mv[0][0]*c[0]+Mv[0][1]*c[1], Mv[1][0]*c[0]+Mv[1][1]*c[1]]
    w2 = [Mu[0][0]*c[0]+Mu[0][1]*c[1], Mu[1][0]*c[0]+Mu[1][1]*c[1]]
    return w1[0]*w2[1] + w1[1]*w2[0]
npts = 0; hist = {}; inc_ok = True; same_ok = True
for x in GF.elements:
    w = GF(1) + x**7
    for y in roots7.get(int(w), []):
        if y == 0: continue
        u = [GF(1), x, y]; npts += 1
        c = [sq(u[2]**7), sq(u[0]**7)]
        ue = [t**E for t in u]
        vals = []
        for z in F8:
            v = [ue[0], z*ue[1], z/(GF(1)+z)*ue[2]]
            assert sum((t**7 for t in v), GF(0)) == 0
            ev = [v[1]*v[2], v[0]*v[2], v[0]*v[1]]
            inc_ok &= (sum((ue[i]*ev[i] for i in range(3)), GF(0)) == 0)
            vals.append(Xi(u, v, c))
        same_ok &= all(t == vals[0] for t in vals)
        nz = sum(1 for t in vals if t == 0)
        hist[nz] = hist.get(nz, 0) + 1
print(f"affine points of Gamma(GF(2^12)) with U0=1, U2!=0: {npts}")
print(f"incidence u^[8].e(v_zeta)=0 for all: {inc_ok};  Xi(u,v_zeta) independent of zeta for all u: {same_ok}")
print(f"histogram of N_Xi(u) (number of the 6 residual points with Xi=0): {dict(sorted(hist.items()))}")
