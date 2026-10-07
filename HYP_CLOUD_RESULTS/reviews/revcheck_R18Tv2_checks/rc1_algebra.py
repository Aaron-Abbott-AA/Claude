# Independent checks (revision check of R18T v2), all over GF(2), exact.
# (A) Lemma 2.1A ingredients: f(e(U)) = g U; C_f := sum Z_i f_i^E is nonzero of degree 2E+1;
#     C_f(e(U)) = g^E * C_orig(U) with C_orig = U^[E].e(U) (so C_f vanishes on Gamma' = e(Gamma));
#     every proper base point q of f has mult_q C_f >= E.
# (B) sigma model: C_f = Z0Z1Z2 * F, deg F = 2E-2, mult_(1:0:0) F = E-1.
# (C) (N10): ker J^[X,t] = S * f^[X] degree by degree (GF(2) linear algebra).
import random, itertools
import numpy as np
import galois
random.seed(20261007)
GF2 = galois.GF(2)

# polynomials in 3 variables over GF(2): set of exponent tuples (coefficient 1)
def add(a, b): return a ^ b
def mul(a, b):
    r = set()
    for m in a:
        for n in b:
            r ^= {(m[0]+n[0], m[1]+n[1], m[2]+n[2])}
    return r
def pw(a, k):
    r = {(0, 0, 0)}; base = a
    while k:
        if k & 1: r = mul(r, base)
        base = mul(base, base); k >>= 1
    return r
VAR = [{(1, 0, 0)}, {(0, 1, 0)}, {(0, 0, 1)}]
def lin(M, v):
    out = []
    for i in range(3):
        s = set()
        for j in range(3):
            if M[i][j]: s = add(s, v[j])
        out.append(s)
    return out
def sig(W): return [mul(W[1], W[2]), mul(W[0], W[2]), mul(W[0], W[1])]
def comp(p, sub):
    acc = set(); cache = {}
    for m in p:
        t = {(0, 0, 0)}
        for i, k in enumerate(m):
            if k:
                if (i, k) not in cache: cache[(i, k)] = pw(sub[i], k)
                t = mul(t, cache[(i, k)])
        acc = add(acc, t)
    return acc
def deg(p): return max(sum(m) for m in p) if p else None
def mult_at(p, pt):
    # translate a GF(2)-point to (chart k) origin and take lowest degree
    k = [i for i in range(3) if pt[i] == 1][0]
    sub = []
    for i in range(3):
        if i == k: sub.append({(0, 0, 0)})
        else: sub.append(add(VAR[i], {(0, 0, 0)}) if pt[i] else VAR[i])
    q = comp(p, sub)
    return min(sum(m) for m in q) if q else None
def rand_inv():
    while True:
        M = GF2([[random.randint(0, 1) for _ in range(3)] for _ in range(3)])
        if np.linalg.det(M) == 1: return M
out = []
for E in [4, 8, 16]:
    for trial in range(3):
        A = rand_inv(); B = rand_inv(); Ai = np.linalg.inv(A); Bi = np.linalg.inv(B)
        A_, B_, Ai_, Bi_ = [x.tolist() for x in (A, B, Ai, Bi)]
        BU = lin(B_, VAR)
        e = lin(A_, sig(BU))
        f = lin(Bi_, sig(lin(Ai_, VAR)))
        g = mul(mul(BU[0], BU[1]), BU[2])
        fe = [comp(fi, e) for fi in f]
        ok_fe = all(fe[i] == mul(g, VAR[i]) for i in range(3))
        Cf = set()
        for i in range(3): Cf = add(Cf, mul(VAR[i], pw(f[i], E)))
        Corig = set()
        for i in range(3): Corig = add(Corig, mul(pw(VAR[i], E), e[i]))
        ok_pull = comp(Cf, e) == mul(pw(g, E), Corig)
        bps = [[int(A_[i][k]) for i in range(3)] for k in range(3)]  # A * coordinate points
        fvan = all(mult_at(fi, bp) >= 1 for fi in f for bp in bps)
        mults = [mult_at(Cf, bp) for bp in bps]
        out.append(f"E={E} t={trial}: Cf!=0:{bool(Cf)} deg={deg(Cf)} (2E+1={2*E+1}) f(e(U))=gU:{ok_fe} "
                   f"Cf(e(U))=g^E*Corig:{ok_pull} f(bp)=0:{fvan} mult_bp(Cf)={mults} (>=E:{all(m>=E for m in mults)})")
out.append("support argument: monomials of Z_i*f_i^E have exponent vector = e_i mod E; pairwise disjoint => Cf=0 iff f=0")
for E in [4, 8, 16]:
    s = sig(VAR)
    Cf = set(); F = set()
    for i in range(3):
        Cf = add(Cf, mul(VAR[i], pw(s[i], E))); F = add(F, pw(s[i], E - 1))
    ok = Cf == mul(mul(mul(VAR[0], VAR[1]), VAR[2]), F)
    out.append(f"sigma E={E}: Cf=Z0Z1Z2*F:{ok} degF={deg(F)} mult_(1:0:0)F={mult_at(F,[1,0,0])} (E-1={E-1}); "
               f"cofactor mult={mult_at(mul(mul(VAR[0],VAR[1]),VAR[2]),[1,0,0])}, total mult Cf={mult_at(Cf,[1,0,0])}")
out.append("mu=1: F^2 | C_f would need 2d' <= 2E+1, impossible with d' >= 2E-2 and E >= 3")
# (C) N10
def monos(dg): return [m for m in itertools.product(range(dg + 1), repeat=3) if sum(m) == dg]
def cross(a, b): return [add(mul(a[1], b[2]), mul(a[2], b[1])), add(mul(a[2], b[0]), mul(a[0], b[2])), add(mul(a[0], b[1]), mul(a[1], b[0]))]
for X in [2, 4]:
    for trial in range(3):
        while True:
            L = rand_inv().tolist(); N = rand_inv().tolist()
            Lt = [[L[j][i] for j in range(3)] for i in range(3)]; Nt = [[N[j][i] for j in range(3)] for i in range(3)]
            j1 = lin(Lt, VAR); j2 = lin(Nt, VAR)
            f = cross(j1, j2)
            if all(f):  # require all three quadrics nonzero
                break
        j1X = [pw(x, X) for x in j1]; j2X = [pw(x, X) for x in j2]
        res = []
        for dl in range(0, 2 * X + 3):
            src = monos(dl); tgt = monos(dl + X); ti = {t: k for k, t in enumerate(tgt)}
            cols = []
            for comp_ in range(3):
                for m in src:
                    col = [0] * (2 * len(tgt))
                    for r, jr in enumerate((j1X, j2X)):
                        for t in mul(jr[comp_], {m}): col[r * len(tgt) + ti[t]] ^= 1
                    cols.append(col)
            Mx = GF2(np.array(cols, dtype=int).T)
            kd = len(cols) - int(np.linalg.matrix_rank(Mx))
            # common factor check of f: compare with expected
            ex = len(monos(dl - 2 * X)) if dl >= 2 * X else 0
            res.append(f"{dl}:{kd}/{ex}{'' if kd==ex else '!'}")
        out.append(f"N10 X={X} t={trial}: deg v: dimker/dim S_(deg-2X) -> " + " ".join(res))
print("\n".join(out))
