#!/usr/bin/env python3
"""Referee check (GX audit, 7 Oct 2026). Numerical tests of GX Lemma DZ / Lemma LD over F_q[X], q = 2^m.
A = sum_i a_i(X) tau^i with a_i in F_q[X]; U' an F_2-subspace of F_Q (Q = 2^{m/2}); W' = A(U').
Tests:
 T1 (DZ contrapositive, random): A' != 0 and dim U' >= d+3  ==>  F_2-rank of u -> (A(u))' is >= 3.
 T2 (DZ sharpness/adversarial): A = X*S_K + E (S_K = subspace poly of K in F_Q, dim K = d, E constant),
     so A' = S_K. With U' ⊃ K: rank = dim U' - d, i.e. 3 at dim U' = d+3 and 2 at dim U' = d+2.
 T3 (DZ (ii)): a_i in F_q[X^2]  ==>  every w in W' lies in F_q[X^2] and sqrt(w) = A_half(sqrt u).
 T4 (LD statement, injectivity): A = tau + 1 kills 1; U' ∋ 1 of dim >= 3: W' consists of constants
     but dim W' = dim U' - 1, so the clause 'dim W' = dim U'' needs injectivity of A on U'.
 T5 (LD chain): a_i in F_q[X^{2^K}] with deg <= u: the Hasse filtration W'_k is lossless and W'_K = constants;
     and for random A with one coefficient not a square, level 0 has rank >= 3 (fails RR) when dim U' >= d+3.
Usage: python3 -I dz_ld_check.py <m> <samples> <seed>"""
import sys, random
import galois

m = int(sys.argv[1]); NS = int(sys.argv[2]); seed = int(sys.argv[3])
random.seed(seed)
GF = galois.GF(2**m)
q = 2**m; Q = 2**(m // 2)
prim = GF.primitive_element
gQ = prim ** ((q - 1) // (Q - 1))          # generator of F_Q^*

def el(x): return GF(int(x))
ZERO = GF(0)

def rand_FQ():
    k = random.randrange(Q)
    return ZERO if k == 0 else gQ ** k

def f2_rank(vecs):
    """vecs: list of python ints (bit vectors). Return F_2 rank."""
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
    return len(basis)

def poly_to_bits(p):
    # p: list of GF elems (coeff of X^j); pack into int, m bits per coefficient
    v = 0
    for j, c in enumerate(p):
        v |= int(c) << (m * j)
    return v

def rand_subspace_FQ(dim, contain=()):
    """random F_2-subspace of F_Q of given dim containing the vectors in contain (assumed independent)."""
    vecs = list(contain)
    while f2_rank([int(x) for x in vecs]) < len(vecs):
        raise ValueError
    while len(vecs) < dim:
        x = rand_FQ()
        if f2_rank([int(y) for y in vecs] + [int(x)]) == len(vecs) + 1:
            vecs.append(x)
    return vecs

def frob(x, i):
    for _ in range(i):
        x = x * x
    return x

def apply_A(A, u):
    """A: list over i of polynomial coefficient lists a_i; returns polynomial A(u) = sum a_i u^{2^i}."""
    L = max(len(a) for a in A)
    out = [ZERO] * L
    for i, a in enumerate(A):
        ui = frob(u, i)
        for j, c in enumerate(a):
            out[j] = out[j] + c * ui
    return out

def deriv(p):
    return [p[j + 1] if (j + 1) % 2 == 1 else ZERO for j in range(len(p) - 1)] or [ZERO]

def is_zero_poly(p): return all(int(c) == 0 for c in p)

def deriv_A(A): return [deriv(a) for a in A]

def rank_of_derivative(A, U):
    return f2_rank([poly_to_bits(deriv(apply_A(A, u))) for u in U])

def subspace_poly(K):
    """subspace polynomial of span(K) as tau-coefficients (constant), degree len(K)."""
    S = [GF(1)]                      # S = tau^0
    for k in K:
        # S <- (tau - S(k)^{1}) * S  i.e. S_new(x) = S(x)^2 - S(k) S(x)
        sk = ZERO
        for i, c in enumerate(S): sk = sk + c * frob(k, i)
        new = [ZERO] * (len(S) + 1)
        for i, c in enumerate(S):
            new[i + 1] = new[i + 1] + c * c
            new[i] = new[i] + sk * c
        S = new
    return S

def rand_poly(deg, sq_level=0):
    """random polynomial of degree <= deg in F_q[X^{2^sq_level}]"""
    step = 2 ** sq_level
    p = [ZERO] * (deg + 1)
    for j in range(0, deg + 1, step):
        p[j] = el(random.randrange(q))
    return p

dmax = m // 2 - 3
fails = {"T1": 0, "T2": 0, "T3": 0, "T4": 0, "T5": 0}
cnt = {"T1": 0, "T1_nonzeroAprime": 0, "T2": 0, "T3": 0, "T4": 0, "T5": 0}
for s in range(NS):
    d = random.randint(0, dmax)
    # T1
    A = [rand_poly(random.randint(0, 5)) for _ in range(d + 1)]
    while is_zero_poly(A[d]): A[d] = rand_poly(3)
    U = rand_subspace_FQ(random.randint(d + 3, m // 2))
    Ap_nonzero = any(not is_zero_poly(deriv(a)) for a in A)
    r = rank_of_derivative(A, U)
    cnt["T1"] += 1
    if Ap_nonzero:
        cnt["T1_nonzeroAprime"] += 1
        if r < 3: fails["T1"] += 1; print("T1 FAIL", d, r)
    # T2: A = X*S_K + E
    K = rand_subspace_FQ(d)
    S = subspace_poly(K)
    E = [el(random.randrange(q)) for _ in range(d + 1)]
    A2 = [[E[i], S[i]] for i in range(d + 1)]
    for extra in (2, 3):
        if d + extra > m // 2: continue
        U2 = rand_subspace_FQ(d + extra, contain=K)
        r2 = rank_of_derivative(A2, U2)
        cnt["T2"] += 1
        if r2 != extra: fails["T2"] += 1; print("T2 FAIL", d, extra, r2)
    # T3: square coefficients
    A3 = [rand_poly(2 * random.randint(0, 3), sq_level=1) for _ in range(d + 1)]
    while is_zero_poly(A3[d]): A3[d] = rand_poly(4, sq_level=1)
    Ahalf = [[c.__pow__(q // 2) for c in a[0::2]] for a in A3]   # sqrt of coefficients, X^2 -> X
    U3 = rand_subspace_FQ(random.randint(d + 3, m // 2))
    for u in U3:
        w = apply_A(A3, u)
        ok = all(int(w[j]) == 0 for j in range(1, len(w), 2))
        su = u ** (q // 2)
        sw = [c ** (q // 2) for c in w[0::2]]
        rhs = apply_A(Ahalf, su)
        L = max(len(sw), len(rhs)); sw += [ZERO] * (L - len(sw)); rhs += [ZERO] * (L - len(rhs))
        ok = ok and all(int(a) == int(b) for a, b in zip(sw, rhs))
        cnt["T3"] += 1
        if not ok: fails["T3"] += 1; print("T3 FAIL")
    # T5: coefficients in F_q[X^{2^K}], deg <= u ; chain lossless, top level constants
    Klev = random.randint(1, 3); u_deg = 2 ** Klev - 1 + 2 ** Klev * random.randint(0, 0)
    A5 = [rand_poly(u_deg, sq_level=Klev) for _ in range(d + 1)]   # only constant term survives since deg < 2^K
    # nontrivial version: degree up to 2^Klev * t, then chain must be lossless for levels < Klev
    t = random.randint(1, 2)
    A5 = [rand_poly(2 ** Klev * t, sq_level=Klev) for _ in range(d + 1)]
    while is_zero_poly(A5[d]): A5[d] = rand_poly(2 ** Klev * t, sq_level=Klev)
    U5 = rand_subspace_FQ(random.randint(d + 3, m // 2))
    Wp = [apply_A(A5, u) for u in U5]
    dimW = f2_rank([poly_to_bits(w) for w in Wp])
    for k in range(Klev + 1):
        # dim W'_k: elements of span lying in F_q[X^{2^k}] -- all of them here by construction
        allk = all(all(int(w[j]) == 0 for j in range(len(w)) if j % (2 ** k)) for w in Wp)
        cnt["T5"] += 1
        if not allk: fails["T5"] += 1; print("T5 FAIL lossy", k)
    # contrapositive: perturb one coefficient by an odd-degree term -> rank >= 3 at level 0
    A5b = [list(a) for a in A5]
    A5b[random.randrange(d + 1)] += [ZERO] * 0
    j = random.randrange(d + 1)
    A5b[j] = A5b[j] + [ZERO] * max(0, 2 - len(A5b[j]))
    A5b[j][1] = A5b[j][1] + el(random.randrange(1, q))
    r5 = rank_of_derivative(A5b, U5)
    cnt["T5"] += 1
    if r5 < 3: fails["T5"] += 1; print("T5 FAIL contrapositive", d, r5)

# T4 deterministic: A = tau + 1, U' ∋ 1
for dimU in range(3, m // 2 + 1):
    U4 = rand_subspace_FQ(dimU, contain=[GF(1)])
    A4 = [[GF(1)], [GF(1)]]
    W4 = [apply_A(A4, u) for u in U4]
    dW = f2_rank([poly_to_bits(w) for w in W4])
    const = all(all(int(c) == 0 for c in w[1:]) for w in W4)
    cnt["T4"] += 1
    print(f"T4 dimU'={dimU}: W' constants={const}, dim W'={dW} (= dimU'-1: {dW == dimU - 1})")
    if not (const and dW == dimU - 1): fails["T4"] += 1

print(f"m={m} Q={Q} samples={NS} seed={seed} dmax={dmax}")
print("counts:", cnt)
print("failures:", fails)
