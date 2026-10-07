# R21 Prop. 2.1 check [v2: N1 header fixed; computation identical to classify_PD.py]: classification of pencils Ct(z) = z1*A1(Y) + z2*A2(Y) (2x2, entries forms of degree a in Y)
# over GF(2) with FNAP's reduced polynomial  P_D(z,Y) = z^[D]^t Ct(z) z  identically zero.
# Claim: D=1: Ct = h(z,Y)*Omega + mu(Y) (x) z^perp   (h linear in z, mu a vector of forms)   dim = 4*dim_a
#        D=2: Ct = h'(Y)*J(z) + mu(Y) (x) z^perp,  J(z)=[[0,z2],[z1,0]]                       dim = 3*dim_a
#        D=4,8: Ct = mu(Y) (x) z^perp only (FNAP disjoint supports; det Ct == 0)                  dim = 2*dim_a
# Method: exact linear algebra over GF(2) (bitset Gaussian elimination).  The nullspace dimension of the
# coefficient map does not depend on the field (the map is defined over F_2 with 0/1 entries, one monomial per unknown).
# We (i) compute dim ker, (ii) check that the claimed family lies in the kernel and spans it.
# Run: python3 -I classify_PD_v2.py
import itertools

def ymonos(a): return [(i, j, a-i-j) for i in range(a+1) for j in range(a+1-i)]

def unknowns(a):   # (row i, col j, z-index k, Y-monomial m): entry (i,j) gets z_k * Y^m
    return [(i, j, k, m) for i in range(2) for j in range(2) for k in range(2) for m in ymonos(a)]

def image(u, D):   # P_D contribution: z_i^D * (z_k Y^m) * z_j  -> monomial (e1,e2,m)
    i, j, k, m = u
    e = [0, 0]; e[i] += D; e[k] += 1; e[j] += 1
    return (e[0], e[1], m)

def rank_gf2(vecs):
    basis = {}
    for v in vecs:
        while v:
            p = v.bit_length()-1
            if p in basis: v ^= basis[p]
            else: basis[p] = v; break
    return len(basis)

def kernel_dim(a, D):
    U = unknowns(a); imgs = {}
    for u in U: imgs.setdefault(image(u, D), 0)
    rank = len(imgs)    # each unknown maps to a single monomial with coefficient 1
    return len(U) - rank, U

def family(a, D):
    """claimed kernel basis, as bit vectors over the unknown index set."""
    U = unknowns(a); idx = {u: n for n, u in enumerate(U)}; vecs = []
    M = ymonos(a)
    def vec(entries):   # entries: list of (i,j,k,m)
        v = 0
        for e in entries: v ^= 1 << idx[e]
        return v
    for m in M:
        for r in range(2):   # mu = e_r * Y^m :  mu (x) z^perp, z^perp=(z2,z1): row r = (z2, z1)
            vecs.append(vec([(r, 0, 1, m), (r, 1, 0, m)]))
        if D == 1:           # h = z_k Y^m : h*Omega = [[0,h],[h,0]]
            for k in range(2): vecs.append(vec([(0, 1, k, m), (1, 0, k, m)]))
        if D == 2:           # h' = Y^m : h'J(z) = [[0, z2 Y^m],[z1 Y^m, 0]]
            vecs.append(vec([(0, 1, 1, m), (1, 0, 0, m)]))
    return vecs

def in_kernel(v, U, D):
    acc = {}
    for n, u in enumerate(U):
        if v >> n & 1:
            key = image(u, D); acc[key] = acc.get(key, 0) ^ 1
    return all(c == 0 for c in acc.values())

pred = {1: 4, 2: 3, 4: 2, 8: 2}
print("D  a  #unknowns  dim ker  predicted  family in ker  family rank")
ok_all = True
for D in [1, 2, 4, 8]:
    for a in range(0, 5):
        kd, U = kernel_dim(a, D); fam = family(a, D)
        fin = all(in_kernel(v, U, D) for v in fam); fr = rank_gf2(fam)
        p = pred[D]*len(ymonos(a))
        ok = (kd == p == fr) and fin; ok_all &= ok
        print(f"{D:<3}{a:<3}{len(U):<11}{kd:<9}{p:<11}{str(fin):<14}{fr}   {'OK' if ok else 'MISMATCH'}")
print("all OK:", ok_all)
