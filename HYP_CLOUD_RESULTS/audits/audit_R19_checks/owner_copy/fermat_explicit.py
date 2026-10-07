# COMPUTED: on Fermat sigma1 with n=E-1, the residual points of l_u are v_zeta = diag(1,zeta,zeta/(1+zeta)) u^[E],
# zeta in F_E \ {0,1}  (E-2 of them).  Check: v_zeta in Gamma, u^[E].e(v_zeta)=0, v_zeta distinct, != u.
import random, galois
for E, m in [(8, 12), (16, 12), (32, 15), (64, 12)]:
    n = E-1; GF = galois.GF(2**m); rng = random.Random(E)
    k = E.bit_length()-1
    FE = [x for x in GF.elements if x**E == x and x not in (0, 1)] if m % k == 0 else None
    if FE is None: print(f"E={E}: F_E not in GF(2^{m}); skipped"); continue
    ok = 0; tot = 0; bad = 0
    for _ in range(20):
        while True:
            u1 = GF(rng.randrange(1, 2**m)); r = galois.Poly([1]+[0]*(n-1)+[int(GF(1)+u1**n)], field=GF).roots()
            if len(r): u = [GF(1), u1, r[0]]; break
        vs = []
        for z in FE:
            D = [GF(1), z, z/(GF(1)+z)]; v = [D[i]*u[i]**E for i in range(3)]
            onG = (v[0]**n + v[1]**n + v[2]**n) == 0
            ev = [v[1]*v[2], v[0]*v[2], v[0]*v[1]]
            inc = (u[0]**E*ev[0] + u[1]**E*ev[1] + u[2]**E*ev[2]) == 0
            vs.append(tuple(int(x/v[0]) for x in v)); ok += onG and inc; tot += 1
        bad += not (len(set(vs)) == E-2 and tuple(int(x) for x in u) not in vs)
    print(f"E={E}: {ok}/{tot} (u,zeta) pairs satisfy v in Gamma and u^[E].e(v)=0; E-2 distinct residuals != u except at {bad}/20 sampled u")
