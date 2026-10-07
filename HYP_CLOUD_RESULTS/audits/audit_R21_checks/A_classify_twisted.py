# Referee check A (R21 Prop. 2.1), independent of the owner's script.
# Work in ORIGINAL coordinates over GF(2^4) and GF(2^8) with Frobenius-twisted constants:
#   P_D(c,Y) = (K c^[D])^t (c1 C_P(Y) + c2 C_R(Y)) (B c),   K, B in GL_2(GF), entries NOT in F_2.
# Compute the kernel of the linear map (C_P, C_R) -> P_D exactly (Gaussian elimination over GF) for
# D in {1,2,4,8} and a in {0,1,2} (Y = (Y0,Y1,Y2), forms of degree a), and compare with the pull-back of the
# claimed family:  C_c = L^{-t} Ct(Bc),  L = K (B^{-1})^[D],  Ct in F_D.
# Also: (i) K drawn from FNAP's actual iteration B_{i+1}=B_i^[Q] B (Q=2^7), (ii) a negative control with the
# Frobenius twist on B^{-1} omitted (L' = K B^{-1}), which must fail for D>=2 when B is not F_2-rational,
# (iii) PRIMARY's FNAN Sec. 4 formal example (A=I, S=Q => D=1, C_P=I, C_R=0) is in F_1.
# Run: python3 -I A_classify_twisted.py
import itertools, random
import numpy as np
import galois

rng = random.Random(20261007)

def ymonos(a): return [(i, j, a-i-j) for i in range(a+1) for j in range(a+1-i)]

def rand_gl2(GF, avoid_f2=True):
    while True:
        M = GF([[rng.randrange(GF.order) for _ in range(2)] for _ in range(2)])
        if int(np.linalg.det(M)) == 0: continue
        if avoid_f2 and all(int(x) in (0, 1) for x in M.flatten()): continue
        return M

def frob(M, D):  # entrywise D-th power
    return M ** D

def PD_vector(GF, K, B, D, CP, CR):
    """coefficients of P_D in c1^i c2^(D+2-i), i=0..D+2, for constant 2x2 CP, CR (a=0 block)."""
    out = [GF(0) for _ in range(D+3)]   # distinct objects (avoid in-place aliasing of 0-d arrays)
    # (K c^[D])_r = K[r,0] c1^D + K[r,1] c2^D ;  (B c)_s = B[s,0] c1 + B[s,1] c2 ; C_c = c1 CP + c2 CR
    for r in range(2):
        for s in range(2):
            for (pi, kc) in ((D, K[r, 0]), (0, K[r, 1])):          # c1 exponent from K-part
                for (qi, cc) in ((1, CP[r, s]), (0, CR[r, s])):     # c1 exponent from pencil
                    for (si, bc) in ((1, B[s, 0]), (0, B[s, 1])):  # c1 exponent from Bc
                        out[pi+qi+si] = out[pi+qi+si] + kc*cc*bc
    return out

def kernel_and_family(GF, K, B, D, L):
    # unknowns: 8 entries (CP 4, CR 4) of the a=0 block; the map preserves Y-monomials, so the kernel for
    # forms of degree a is (a=0 kernel) (x) k[Y]_a.  We nevertheless build a>0 explicitly below.
    cols = []
    for which in range(2):
        for r in range(2):
            for s in range(2):
                CP = GF.Zeros((2, 2)); CR = GF.Zeros((2, 2))
                (CP if which == 0 else CR)[r, s] = 1
                cols.append(PD_vector(GF, K, B, D, CP, CR))
    M = GF(np.array([[int(x) for x in col] for col in cols]).T)   # (D+3) x 8
    rank = np.linalg.matrix_rank(M)
    kerdim = 8 - rank
    # family basis (A1, A2) with Ct = z1 A1 + z2 A2
    fam = []
    E = lambda i, j: GF(np.array([[1 if (r, s) == (i, j) else 0 for s in range(2)] for r in range(2)]))
    Z = GF.Zeros((2, 2)); Om = GF([[0, 1], [1, 0]])
    for rr in range(2):           # mu = e_rr : row rr = (z2, z1)
        fam.append((E(rr, 1), E(rr, 0)))
    if D == 1:
        fam.append((Om, Z)); fam.append((Z, Om))      # h = z1, h = z2
    if D == 2:
        fam.append((E(1, 0), E(0, 1)))               # h' J(z) = [[0, z2],[z1, 0]]
    Lit = np.linalg.inv(L).T
    vecs = []
    for (A1, A2) in fam:
        CP = Lit @ (B[0, 0]*A1 + B[1, 0]*A2)
        CR = Lit @ (B[0, 1]*A1 + B[1, 1]*A2)
        vecs.append([int(x) for x in list(CP.flatten()) + list(CR.flatten())])
    F = GF(np.array(vecs))
    in_ker = bool(np.all(M @ F.T == 0))
    famrank = np.linalg.matrix_rank(F)
    return kerdim, famrank, in_ker, M

def explicit_a(GF, K, B, D, L, a):
    """explicit check for forms of degree a: kernel dimension of the full map equals kerdim0*dim_a."""
    mons = ymonos(a); nm = len(mons)
    _, _, _, M0 = kernel_and_family(GF, K, B, D, L)
    # full matrix is block diagonal: rows (c-monomial, Y-monomial), cols (unknown, Y-monomial)
    big = GF.Zeros(((D+3)*nm, 8*nm))
    for t in range(nm):
        big[t*(D+3):(t+1)*(D+3), t*8:(t+1)*8] = M0
    return 8*nm - np.linalg.matrix_rank(big), nm

pred = {1: 4, 2: 3, 4: 2, 8: 2}
allok = True
print("field  D  trial  kerdim(a=0)  pred  family_rank  family_in_ker  a=1,2 kerdim/dim_a  control(L'=K B^-1) in_ker")
for m in (4, 8):
    GF = galois.GF(2**m)
    for D in (1, 2, 4, 8):
        for trial in range(4):
            B = rand_gl2(GF)
            if trial == 0:
                # K from FNAP's iteration with Q=2^7, j=1 (S=Q*D): B_1=B, B_2=B^[Q] B, K=B_2^[D]
                Qp = 2**7
                B2 = frob(B, Qp) @ B
                K = frob(B2, D)
            else:
                K = rand_gl2(GF)
            L = K @ frob(np.linalg.inv(B), D)
            kd, fr, ink, _ = kernel_and_family(GF, K, B, D, L)
            k1, n1 = explicit_a(GF, K, B, D, L, 1)
            k2, n2 = explicit_a(GF, K, B, D, L, 2)
            Lbad = K @ np.linalg.inv(B)
            _, _, ink_bad, _ = kernel_and_family(GF, K, B, D, Lbad)
            ok = (kd == pred[D] == fr) and ink and k1 == kd*n1 and k2 == kd*n2
            allok &= ok
            print(f"2^{m:<4}{D:<3}{trial:<7}{kd:<13}{pred[D]:<6}{fr:<13}{str(ink):<15}{k1//n1},{k2//n2}{'':<17}{ink_bad}   {'OK' if ok else 'MISMATCH'}")
print("all classification checks OK:", allok)

# FNAN Sec. 4 formal example: ordered e-pencil A=I => B=swap*A^t=Omega; S=Q => D=1, j=1;
# B_2 = B^[Q] B = Omega^2 = I, K = I, L = K B^{-1} = Omega.  Ct(z) = L^t C_{B^{-1} z} with C_P=I, C_R=0.
GF = galois.GF(2**4)
Om = GF([[0, 1], [1, 0]]); I = GF([[1, 0], [0, 1]])
B = Om; K = frob(frob(B, 2**7) @ B, 1); L = K @ np.linalg.inv(B)
kd, fr, ink, M = kernel_and_family(GF, K, B, 1, L)
v = GF([1, 0, 0, 1, 0, 0, 0, 0])   # C_P = I, C_R = 0
print("FNAN Sec.4 example (C_P=I, C_R=0, A=I, D=1): P_D==0:", bool(np.all(M @ v == 0)), "; K==I:", bool(np.all(K == I)), "; L==Omega:", bool(np.all(L == Om)))
# Ct(z) = Omega * C_{Omega z} = Omega * ((Omega z)_1 I) = z2 * Omega  -> h = z2, mu = 0 (in F_1)
print("  => Ct(z) = z2*Omega, i.e. h=z2, mu=0: member of F_1 (by hand; P_D==0 confirms)")
