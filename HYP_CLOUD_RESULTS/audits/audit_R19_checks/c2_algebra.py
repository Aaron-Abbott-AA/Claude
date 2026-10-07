# Referee check c2 (independent): algebraic spot checks for R19 §§1-3.
import itertools, random, collections
import galois, numpy as np
import sympy as sp

print("== (a) Lemma 1.1(i) proof: in char 2 the limit of generic tangents need NOT be the branch tangent")
t = sp.symbols('t')
z = sp.Matrix([1, t**2, t**3])
# Hasse derivative D^(1) = ordinary derivative; reduce coefficients mod 2
dz = sp.Matrix([sp.Poly(sp.diff(c, t), t, modulus=2).as_expr() for c in z])
cr = z.cross(dz); cr = sp.Matrix([sp.Poly(c, t, modulus=2).as_expr() for c in cr])
import functools
g = functools.reduce(lambda A, B: A.gcd(B), [sp.Poly(c, t, modulus=2) for c in cr if c != 0])
lim = sp.Matrix([sp.Poly(c, t, modulus=2).quo(g).as_expr().subs(t, 0) if c != 0 else 0 for c in cr])
print("  branch z(t)=(1,t^2,t^3); z x z' =", list(cr), "-> limit line", list(lim))
for name, L in [("limit line", lim), ("true tangent (0,0,1)", sp.Matrix([0, 0, 1]))]:
    val = sp.Poly(sum(L[i]*z[i] for i in range(3)), t, modulus=2)
    print(f"  intersection multiplicity of {name} with the branch:", min(m[0] for m in val.monoms()))

print("== (b) Prop 1.2: roots of (a t+b)t^E+(c t+d) form a Moebius image of P^1(F_E): cross-ratios in F_E")
for E, m in [(4, 8), (8, 12), (16, 16)]:
    GF = galois.GF(2**m); rng = random.Random(E); P = galois.Poly
    found = 0; ok = 0; tries = 0
    while found < 5 and tries < 3000:
        tries += 1
        a, b, c, d = [GF(rng.randrange(2**m)) for _ in range(4)]
        if a == 0 or a*d == b*c: continue
        coeffs = [0]*(E+2); coeffs[0] = int(a); coeffs[1] = int(b); coeffs[E] = int(c); coeffs[E+1] = int(d)
        poly = P(coeffs, field=GF)            # degree E+1 (descending coefficients)
        r = poly.roots()
        if len(r) < 4: continue
        found += 1
        good = True
        for x1, x2, x3, x4 in itertools.combinations(list(r), 4):
            cr_ = ((x1+x3)*(x2+x4))/((x1+x4)*(x2+x3))
            good &= (cr_**E == cr_)
        ok += good
        if found == 1: print(f"  E={E}: sample with {len(r)} rational roots over GF(2^{m}); all cross-ratios in F_E: {good}")
    print(f"  E={E}: {ok}/{found} split samples have all 4-point cross-ratios in F_E (Bluher root counts seen OK)")

print("== (c) char-2 matrix identities used in Cor 2.2(ii) and Lemma 3.5(ii), exhaustive over GF(4)")
GF = galois.GF(4); els = list(GF.elements)
Om = GF([[0, 1], [1, 0]])
mats = [GF([[a, b], [c, d]]) for a in els for b in els for c in els for d in els]
inv = [M for M in mats if np.linalg.det(M) != 0]
id1 = all(np.array_equal(M.T @ Om @ M, np.linalg.det(M)*Om) for M in mats)
print("  B^t Omega B = det(B) Omega for all 256 matrices:", id1)
# Lemma 3.5(ii): det(A c, B c) == 0 for all c in P^1(GF(16)) (17 points > degree 2) => B proportional to A
# fast integer GF(16) arithmetic (tables from galois); GF(4) embedded in GF(16)
GF16 = galois.GF(16)
MUL = [[int(GF16(a)*GF16(b)) for b in range(16)] for a in range(16)]
w16 = [int(x) for x in GF16.elements if x != 0 and x != 1 and x**3 == 1][0]
g4 = [x for x in els if x not in (0, 1)][0]
emb = {0: 0, 1: 1, int(g4): w16, int(g4*g4): MUL[w16][w16]}
def e16(M): return [[emb[int(M[i, j])] for j in range(2)] for i in range(2)]
def mv(M, c): return [MUL[M[0][0]][c[0]] ^ MUL[M[0][1]][c[1]], MUL[M[1][0]][c[0]] ^ MUL[M[1][1]][c[1]]]
def d2(x, y): return MUL[x[0]][y[1]] ^ MUL[x[1]][y[0]]
cs = [[1, x] for x in range(16)] + [[0, 1]]
inv16 = [e16(M) for M in inv]; all16 = [e16(M) for M in mats]
viol = 0; hits = 0
for A in inv16:
    for B in all16:
        if all(d2(mv(A, c), mv(B, c)) == 0 for c in cs):
            hits += 1
            prop = any(all(B[i][j] == MUL[lam][A[i][j]] for i in range(2) for j in range(2)) for lam in range(16))
            viol += (not prop)
print("  det(Ac,Bc)==0 identically (A invertible): %d pairs; B not prop. to A: %d violations" % (hits, viol))
# Cor 2.2(ii): B(u)^t Omega B(v) = m Omega, B(v) invertible => B(u) = (m/det B(v)) B(v)
viol = 0
for Bu in inv:
    for Bv in inv:
        M = Bu.T @ Om @ Bv
        if M[0, 0] == 0 and M[1, 1] == 0 and M[0, 1] == M[1, 0]:
            lam = M[0, 1]/np.linalg.det(Bv)
            viol += not np.array_equal(Bu, lam*Bv)
print("  M=m*Omega => B(u)=(m/detB(v))B(v):", viol, "violations")

print("== (d) Thm 4.1 Step 3 gap (FIX-1): at v with p(v)=0, Pi_1(u,v)=0 for every u but pi(u,y)!=0")
GF = galois.GF(2**16); rng = random.Random(7); R = lambda: GF(rng.randrange(1, 2**16))
rr, X, Q = 4, 4, 8; T = 2*X
cnt = 0
for _ in range(50):
    lam = GF(0); p1, p2 = R(), R()                 # p = lam * p', lam(v)=0, p'(v)=(p1,p2)!=0
    b1, b2 = GF([R(), R()]), GF([R(), R()])        # columns of B(v)
    alpha, beta = R(), R(); c = GF([beta, alpha])**(2**15)   # c=(sqrt beta, sqrt alpha)
    p = GF([lam*p1, lam*p2]); perp = lambda x: GF([x[1], x[0]])
    Cc = np.outer(p, perp(c[0]*b1 + c[1]*b2))
    G = (c**T) @ Cc @ (c**Q)
    Pi1 = (c**T) @ p
    # pi with y-side the 2r-th power of an E-th root of p'(v): use p'^(sigma) := p'^(1/E) with E=2rX
    E = 2*rr*X; root = lambda x: x**pow(E, -1, 2**16-1)
    pi = beta*root(p1)**(2*rr) + alpha*root(p2)**(2*rr)
    cnt += (G == 0 and Pi1 == 0 and pi != 0)
print(f"  {cnt}/50 random instances: G_c(z(v))=0 and Pi_1=0 automatically while pi(u,y)!=0")

print("== (e) arithmetic-monodromy transitivity from observed cycle types (corr_random.out)")
def orbit_partitions_consistent(N, types):
    # all multisets of orbit sizes (partitions of N, >=2 parts) such that every observed cycle type
    # can be distributed into the orbits (each orbit size = sum of a sub-multiset of the cycle lengths)
    def parts(n, mx):
        if n == 0: yield []; return
        for k in range(min(n, mx), 0, -1):
            for rest in parts(n-k, k): yield [k]+rest
    def fits(orbs, cyc):
        def rec(i, rem):
            if i == len(cyc): return all(x == 0 for x in rem)
            seen = set()
            for j in range(len(rem)):
                if rem[j] >= cyc[i] and rem[j] not in seen:
                    seen.add(rem[j]); rem[j] -= cyc[i]
                    if rec(i+1, rem): rem[j] += cyc[i]; return True
                    rem[j] += cyc[i]
            return False
        return rec(0, list(orbs))
    out = []
    for pt in parts(N, N):
        if len(pt) < 2: continue
        if all(fits(pt, sorted(cy, reverse=True)) for cy in types): out.append(pt)
    return out
obs = {8: [[1, 2, 6], [9], [1, 1, 1, 3, 3]],
       16: [[1, 8, 8], [2, 3, 12], [1, 1, 1, 2, 4, 4, 4]],
       32: [[1, 2, 10, 10, 10], [3, 15, 15], [1, 1, 1] + [5]*6]}
for E, types in obs.items():
    bad = orbit_partitions_consistent(E+1, types)
    print(f"  E={E}: intransitive orbit partitions compatible with all observed cycle types: {bad[:6]}{' ...' if len(bad) > 6 else ''} ({len(bad)})")
