# Referee R20: independent recomputation of Example 2.4 (Fermat sigma1, E=8, GF(2^12)).
# Independent code path: points enumerated by y (solving x^7 = 1 + y^7), Xi computed two ways:
#   (I) directly from M(v_zeta) at the six explicit residual points,
#  (II) from the claimed identity M(v_zeta) = M(u)^[8]  (so Xi = det(M(u)^[8] c, M(u) c)).
# Also checks: the six v_zeta are distinct points of Gamma on l_u, and != u.
# Run: python3 -I ref_fermat_cluster.py
import galois
GF = galois.GF(2**12)
E = 8
els = [GF(i) for i in range(2**12)]
seventh = {}
for x in els:
    seventh.setdefault(int(x**7), []).append(x)
F8 = [z for z in els if z**8 == z and z not in (GF(0), GF(1))]
assert len(F8) == 6
def sqrt(x): return x**(2**11)
def M(u):
    a, b, c = u[0]**7, u[1]**7, u[2]**7
    return ((a, b), (c, a + b))
def mv(A, c): return (A[0][0]*c[0] + A[0][1]*c[1], A[1][0]*c[0] + A[1][1]*c[1])
def det(p, q): return p[0]*q[1] + p[1]*q[0]
def proj_eq(p, q):
    return all(p[i]*q[j] == p[j]*q[i] for i in range(3) for j in range(3))
hist = {}; agree = True; npts = 0; distinct_ok = True; special = []
for y in els:
    if y == 0: continue
    for x in seventh.get(int(GF(1) + y**7), []):
        u = (GF(1), x, y); npts += 1
        c = (sqrt(u[2]**7), sqrt(u[0]**7))
        ue = tuple(t**E for t in u)
        Mu = M(u); Mu8 = tuple(tuple(e**8 for e in row) for row in Mu)
        xiII = det(mv(Mu8, c), mv(Mu, c))
        vs = []
        cnt = 0
        for z in F8:
            v = (ue[0], z*ue[1], z/(GF(1) + z)*ue[2])
            assert v[0]**7 + v[1]**7 + v[2]**7 == 0
            ev = (v[1]*v[2], v[0]*v[2], v[0]*v[1])
            assert ue[0]*ev[0] + ue[1]*ev[1] + ue[2]*ev[2] == 0
            vs.append(v)
            xiI = det(mv(M(v), c), mv(Mu, c))
            agree &= (xiI == xiII)
            cnt += (xiI == 0)
        for i in range(6):
            distinct_ok &= not proj_eq(vs[i], u)
            for j in range(i):
                distinct_ok &= not proj_eq(vs[i], vs[j])
        hist[cnt] = hist.get(cnt, 0) + 1
        if cnt: special.append((int(x), int(y)))
print(f'points (U0=1, U2!=0): {npts}')
print(f'Xi via M(v_zeta) equals Xi via M(u)^[8] at all (u,zeta): {agree}')
print(f'six residual points distinct and != u at every u: {distinct_ok}')
print(f'histogram N_Xi: {dict(sorted(hist.items()))}')
print(f'u with N_Xi=6 (x,y as ints): {special}')
