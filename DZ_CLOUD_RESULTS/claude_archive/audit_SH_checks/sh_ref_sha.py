#!/usr/bin/env python3
"""Referee checks (SH audit) in a finite model K = GF(2^N) ⊃ F_Q, Q = 2^h, h | N, N != 2h
(so the Q-power is not an involution on K, as on L).  Referee code; uses galois for linear algebra.
Run: nice -n 19 python3 -I sh_ref_sha.py

T1  Theorem SH(a) threshold.  Random A in K{tau} of exact degree d, random F_2-subspace U ⊂ F_Q of dim r.
    Phi_U : (c,d) -> (P(A(u_j)))_j  and  Psi : (c,d) -> coefficients of Lambda(A) = C A + D phi(A).
    Always ker Psi ⊆ ker Phi_U.  SH(a) predicts equality when r > a2 + d.  For r <= a2 + d we record how often
    ker Phi_U is strictly larger (sharpness of the threshold).
T2  SH1's parenthetical ("under (N0) the relation is determined by W up to scalar") when a2 > a(W):
    W = lambda F_Q (dim h).  Relation spaces of degree <= 0 and <= 1 have dims 1 and 2; two independent
    (N0) degree-1 relations exist, and both admit the degree-0 twist lambda (Lambda(lambda) = 0), as SH3 says.
T3  Referee's Claim U (minimal relations form a line when dim W >= 2a+1, a = a(W)):
    (i)  W = A(U), deg A = a, dim U in [2a+1, h]: dim Rel_{<=a-1} = 0 and dim Rel_{<=a} = 1;
    (ii) random W of dim 2a+1: same;  (iii) random W of dim 2a: dim Rel_{<=a} = 2 (bound is sharp).
    Deviations are listed as (case, a, F_2-dim W, dim Rel_{<=a-1}, dim Rel_{<=a}); a Claim U counterexample would be
    dim Rel_{<=a-1} = 0, dim Rel_{<=a} >= 2 with F_2-dim W >= 2a+1 (counted separately; expected 0).
"""
import random
import numpy as np
import galois

def setup(h, N):
    K = galois.GF(2 ** N)
    Q = 2 ** h
    gen = K.primitive_element
    z = gen ** ((2 ** N - 1) // (Q - 1))  # generator of F_Q^*
    FQ = [K(0)] + [z ** j for j in range(Q - 1)]
    return K, Q, FQ

def ev(A, x):  # A = list of K coefficients, A(x) = sum a_k x^(2^k)
    s = x * 0
    for k, a in enumerate(A): s = s + a * x ** (2 ** k)
    return s

def rand_subspace(K, elems, r):
    while True:
        B = random.sample(elems[1:], r)
        span = {0}
        ok = True
        for b in B:
            bi = int(b)
            if bi in span: ok = False; break
            span |= {s ^ bi for s in span}
        if ok: return B

def rand_nonzero(K):
    while True:
        x = K(random.randrange(1, K.order))
        if x != 0: return x

def nullity(K, rows, ncols):
    if not rows: return ncols, None
    Mx = K(np.array([[int(v) for v in row] for row in rows], dtype=int).reshape(len(rows), ncols))
    ns = Mx.null_space()
    return ns.shape[0], ns

def rel_rows(W, a, Q):  # unknowns (c_0..c_a, d_0..d_a): sum c_i w^(2^i) + d_i w^(Q 2^i) = 0
    return [[w ** (2 ** i) for i in range(a + 1)] + [w ** (Q * 2 ** i) for i in range(a + 1)] for w in W]

def T1(K, Q, FQ, h, trials):
    res = {}
    for _ in range(trials):
        a2 = random.randint(0, 2); d = random.randint(0, 2); r = random.randint(1, h)
        A = [K(random.randrange(K.order)) for _ in range(d)] + [rand_nonzero(K)]
        U = rand_subspace(K, FQ, r)
        n = 2 * a2 + 2
        phi_rows = [[ev(A, u) ** (2 ** i) for i in range(a2 + 1)] + [ev(A, u) ** (Q * 2 ** i) for i in range(a2 + 1)] for u in U]
        psi_rows = []
        for k in range(a2 + d + 1):
            row = []
            for i in range(a2 + 1):
                row.append(A[k - i] ** (2 ** i) if 0 <= k - i <= d else K(0))
            for i in range(a2 + 1):
                row.append(A[k - i] ** (Q * 2 ** i) if 0 <= k - i <= d else K(0))
            psi_rows.append(row)
        kphi, nsphi = nullity(K, phi_rows, n)
        kpsi, nspsi = nullity(K, psi_rows, n)
        # containment ker Psi ⊆ ker Phi_U
        if kpsi:
            Phi = K(np.array([[int(v) for v in row] for row in phi_rows], dtype=int))
            contained = bool(np.all(Phi @ nspsi.T == 0))
        else:
            contained = True
        above = r > a2 + d
        key = 'above' if above else 'at_or_below'
        st = res.setdefault(key, dict(n=0, equal=0, strict=0, containment_fail=0))
        st['n'] += 1
        st['equal' if kphi == kpsi else 'strict'] += 1
        if not contained: st['containment_fail'] += 1
    return res

def T2(K, Q, FQ, h):
    lam = rand_nonzero(K)
    while lam ** Q == lam: lam = rand_nonzero(K)
    W = [lam * u for u in FQ[1:]]
    k0, _ = nullity(K, rel_rows(W, 0, Q), 2)
    k1, ns1 = nullity(K, rel_rows(W, 1, Q), 4)
    # find two independent (N0) relations in Rel_{<=1}
    found = []
    for _ in range(200):
        coeffs = K([random.randrange(K.order) for _ in range(ns1.shape[0])])
        v = coeffs @ ns1
        c0, c1, d0, d1 = v
        if c0 != 0 and c1 != 0 and d0 != 0 and d1 != 0:
            if not found or np.linalg.matrix_rank(K(np.vstack([np.array([int(x) for x in found[0]]), np.array([int(x) for x in v])]))) == 2:
                found.append(v)
        if len(found) == 2: break
    # twist lambda: Lambda(lambda)_i = c_i lam^(2^i) + d_i lam^(Q 2^i) = 0 for i = 0, 1
    twist_ok = all(all(v[i] * lam ** (2 ** i) + v[2 + i] * lam ** (Q * 2 ** i) == 0 for i in range(2)) for v in found)
    return dict(dimW=h, rel_deg0=k0, rel_deg_le1=k1, two_indep_N0=len(found) == 2, twist_lambda_ok=twist_ok)

def T3(K, Q, FQ, h, trials):
    out = dict(i_ok=0, i_n=0, ii_ok=0, ii_n=0, iii_two=0, iii_n=0, other=[], claimU_counterexamples=0)
    def f2dim(W):
        span = {0}
        for w in W:
            wi = int(w)
            if wi not in span: span |= {s ^ wi for s in span}
        return len(span).bit_length() - 1
    def note(tag, W, a, km, ka):
        out['other'].append((tag, a, f2dim(W), km, ka))
        if km == 0 and ka >= 2 and f2dim(W) >= 2 * a + 1: out['claimU_counterexamples'] += 1
    for _ in range(trials):
        a = random.randint(1, 2)
        if 2 * a + 1 <= h:
            r = random.randint(2 * a + 1, h)
            A = [K(random.randrange(K.order)) for _ in range(a)] + [rand_nonzero(K)]
            U = rand_subspace(K, FQ, r)
            W = [ev(A, u) for u in U]
            km, _ = nullity(K, rel_rows(W, a - 1, Q), 2 * a)
            ka, _ = nullity(K, rel_rows(W, a, Q), 2 * a + 2)
            out['i_n'] += 1; out['i_ok'] += (km == 0 and ka == 1)
            if not (km == 0 and ka == 1): note('i', W, a, km, ka)
        Wr = [rand_nonzero(K) for _ in range(2 * a + 1)]
        km, _ = nullity(K, rel_rows(Wr, a - 1, Q), 2 * a)
        ka, _ = nullity(K, rel_rows(Wr, a, Q), 2 * a + 2)
        out['ii_n'] += 1; out['ii_ok'] += (km == 0 and ka == 1)
        if not (km == 0 and ka == 1): note('ii', Wr, a, km, ka)
        Ws = Wr[:2 * a]
        km, _ = nullity(K, rel_rows(Ws, a - 1, Q), 2 * a)
        ka, _ = nullity(K, rel_rows(Ws, a, Q), 2 * a + 2)
        out['iii_n'] += 1; out['iii_two'] += (km == 0 and ka == 2)
        if not (km == 0 and ka == 2): note('iii', Ws, a, km, ka)
    return out

if __name__ == "__main__":
    for seed, (h, N), trials in ((1, (4, 12), 300), (2, (6, 18), 200), (3, (3, 9), 300)):
        random.seed(seed)
        K, Q, FQ = setup(h, N)
        print(dict(seed=seed, h=h, N=N, T1=T1(K, Q, FQ, h, trials)), flush=True)
        print(dict(seed=seed, h=h, N=N, T2=T2(K, Q, FQ, h)), flush=True)
        print(dict(seed=seed, h=h, N=N, T3=T3(K, Q, FQ, h, trials // 2)), flush=True)
