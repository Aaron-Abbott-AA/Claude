#!/usr/bin/env python3
"""Revision-check (PTH v2) referee code. Independent of owner and v1-audit code. Reads no files.
Pointwise (K = F_q) tests of Lemma ML (v2 §4A) for the twisted Lang equation  C*A = D*A^{(Q)}  in F_q{tau}.
Modes (python3 -I rc_ml.py MODE m seed n):
  conj   : random C (c0 != 0), D = C^{(Q)}                        [the PTH situation]
  conj0  : random C with c0 = 0 (C = C1*tau), D = C^{(Q)}          [tests ML's 'd0 != 0' clause]
  gen    : random A0, then (C, D) of minimal degree with C*A0 = D*A0^{(Q)} (general D, not conjugate type)
  gen0   : as gen, then (C, D) -> (C*tau, D*tau)                   [c0 = d0 = 0, general D]
  sharp  : C = R o lambda^{-1} (R = subspace poly of K < F_Q, dim a), V = (rho-a)-dim subspace of lambda F_Q
           + a random vectors of Vtilde_C; reports a(V), k, e, deg A_min, dim(V cap A(F_Q)).
For each solvable (C, D): F2-solution space of deg <= N, minimal degree d, F2-dim of {deg <= d} (line <=> = m/2),
deg D == deg C, a0 != 0, d0 != 0, top Kummer identity, generalised bottom identity at lowest index i with c_i != 0.
"""
import sys, random

PRIM = {8: 0x11D, 12: 0x1053, 16: 0x1002D}   # primitive trinomial/pentanomials (checked below)

class GF:
    def __init__(s, m):
        s.m, s.q = m, 1 << m
        f = PRIM[m]; s.exp = [0] * (2 * s.q); s.log = [0] * s.q; x = 1
        for i in range(s.q - 1):
            s.exp[i] = x; s.log[x] = i; x <<= 1
            if x >> m: x ^= f
        assert len(set(s.exp[:s.q - 1])) == s.q - 1, "not primitive"
        for i in range(s.q - 1, 2 * s.q): s.exp[i] = s.exp[i - (s.q - 1)]
    def mul(s, a, b):
        return 0 if a == 0 or b == 0 else s.exp[s.log[a] + s.log[b]]
    def inv(s, a): return s.exp[(s.q - 1 - s.log[a]) % (s.q - 1)]
    def pw(s, a, e):
        if a == 0: return 0 if e else 1
        return s.exp[(s.log[a] * e) % (s.q - 1)]
    def p2(s, a, k): return s.pw(a, pow(2, k % s.m, s.q - 1) if s.q > 2 else 1)

def tmul(F, C, A):
    out = [0] * (len(C) + len(A) - 1)
    for i, c in enumerate(C):
        if c:
            for j, x in enumerate(A):
                if x: out[i + j] ^= F.mul(c, F.p2(x, i))
    return out
def tev(F, C, z):
    r = 0
    for e, c in enumerate(C):
        if c: r ^= F.mul(c, F.p2(z, e))
    return r
def deg(A): return max((i for i, x in enumerate(A) if x), default=-1)
def trim(A): d = deg(A); return A[:d + 1] if d >= 0 else [0]
def twQ(F, A): return [F.p2(x, F.m // 2) for x in A]

def f2_basis(vs):
    piv = {}                      # leading bit -> vector (proper echelon form, distinct leading bits)
    for v in vs:
        while v:
            t = v.bit_length() - 1
            if t in piv: v ^= piv[t]
            else: piv[t] = v; break
    return list(piv.values())
def f2_kernel(cols):
    rows, ker = [], []
    for j, c in enumerate(cols):
        v, cb = c, 1 << j
        for bv, bc in rows:
            if v ^ bv < v: v ^= bv; cb ^= bc
        if v: rows.append((v, cb)); rows.sort(key=lambda t: -t[0])
        else: ker.append(cb)
    return ker

def lang_solutions(F, C, D, N):
    """F2-basis of {A in F_q{tau}_{<=N} : C A = D A^{(Q)}} as coefficient lists."""
    m = F.m; cols = []
    for k in range(N + 1):
        for i in range(m):
            A = [0] * (N + 1); A[k] = 1 << i
            L = tmul(F, C, A); R = tmul(F, D, twQ(F, A))
            n = max(len(L), len(R)); L += [0] * (n - len(L)); R += [0] * (n - len(R))
            v = 0
            for t in range(n): v |= (L[t] ^ R[t]) << (m * t)
            cols.append(v)
    sols = []
    for cb in f2_kernel(cols):
        A = [0] * (N + 1)
        for j in range((N + 1) * m):
            if cb >> j & 1: A[j // m] ^= 1 << (j % m)
        sols.append(A)
    return sols

def pack(F, A): return sum(x << (F.m * i) for i, x in enumerate(A))

def analyse(F, C, D, N, st):
    m, h = F.m, F.m // 2
    sols = lang_solutions(F, C, D, N)
    if not sols: st['unsolvable'] += 1; return
    st['solvable'] += 1
    dmin = min(deg(A) for A in sols)
    # F2-dim of solutions of degree <= dmin  (all nonzero ones have degree exactly dmin)
    # the kernel basis is not degree-filtered; recompute via echelon on packed vectors with top-degree pivots
    allv = f2_basis([pack(F, A) for A in sols])
    lowdim = sum(1 for v in allv if v.bit_length() <= m * (dmin + 1))
    if lowdim != h: st['line_fail'] += 1
    A = [ (min(allv, key=lambda v: v.bit_length()) >> (m * i)) & (F.q - 1) for i in range(N + 1)]
    a2, a2p = deg(C), deg(D)
    if a2 != a2p: st['degCD_fail'] += 1
    if A[0] == 0: st['a0_zero'] += 1
    if D[0] == 0: st['d0_zero'] += 1
    if (C[0] == 0) != (D[0] == 0): st['c0d0_mismatch'] += 1
    d = deg(A); y = F.pw(A[d], (1 << h) - 1)
    if F.p2(y, a2) != F.mul(C[a2], F.inv(D[a2p])): st['top_kummer_fail'] += 1
    i = min(t for t, c in enumerate(C) if c)
    y0 = F.pw(A[0], (1 << h) - 1)
    if D[i] == 0 or F.p2(y0, i) != F.mul(C[i], F.inv(D[i])): st['bottom_gen_fail'] += 1
    if C[0]:
        if F.mul(C[0], A[0]) != F.mul(D[0], F.p2(A[0], h)) : st['bottom0_fail'] += 1
    # MI: minimal A injective on F_Q
    FQ = f2_basis([F.mul(x, F.p2(x, h)) for x in range(1, F.q)][:4 * h])
    if len(f2_basis([tev(F, A, x) for x in FQ])) != h: st['MI_fail'] += 1
    # A*(tau^{h}+1) is a solution vanishing on F_Q (relevant to ML consequence (iv))
    E = [1] + [0] * (h - 1) + [1]
    AE = tmul(F, A, E)
    L = tmul(F, C, AE); R = tmul(F, D, twQ(F, AE))
    if L != R or any(tev(F, AE, x) for x in FQ): st['iv_demo_fail'] += 1
    st['dmin_hist'][dmin] = st['dmin_hist'].get(dmin, 0) + 1

def solve_CD(F, A0, s):
    """Nonzero (C, D) of degree <= s with C A0 = D A0^{(Q)}: F_q-linear system, unknowns c_0..c_s, d_0..d_s."""
    dA = deg(A0); B = twQ(F, A0); nrow = s + dA + 1; ncol = 2 * (s + 1)
    M = [[0] * ncol for _ in range(nrow)]
    for i in range(s + 1):
        for j in range(dA + 1):
            M[i + j][i] ^= F.p2(A0[j], i)
            M[i + j][s + 1 + i] ^= F.p2(B[j], i)
    # row reduce, find kernel vector
    piv = []; r = 0
    for c in range(ncol):
        p = next((k for k in range(r, nrow) if M[k][c]), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]; iv = F.inv(M[r][c]); M[r] = [F.mul(iv, x) for x in M[r]]
        for k in range(nrow):
            if k != r and M[k][c]:
                t = M[k][c]; M[k] = [x ^ F.mul(t, y) for x, y in zip(M[k], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(ncol) if c not in piv]
    if not free: return None
    fc = free[0]; v = [0] * ncol; v[fc] = 1
    for k, c in enumerate(piv): v[c] = M[k][fc]
    return trim(v[:s + 1]), trim(v[s + 1:])

def defect(F, V, rho):
    h = F.m // 2
    for j in range(rho // 2 + 1):
        rows = [[F.p2(v, e) for e in range(j + 1)] + [F.p2(v, h + e) for e in range(j + 1)] for v in V]
        if rank_Fq(F, rows) < 2 * j + 2: return j
    return rho // 2
def rank_Fq(F, rows):
    M = [list(r) for r in rows]; rk = 0
    for c in range(len(M[0])):
        p = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]; iv = F.inv(M[rk][c]); M[rk] = [F.mul(iv, x) for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                t = M[i][c]; M[i] = [x ^ F.mul(t, y) for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk

def subspace_poly(F, K):
    S = [1]
    for k in K:
        val = tev(F, S, k)
        if val: S = tmul(F, [val, 1], S)      # S_new = S^2 + val*S = (tau + val) o S
    return S

def main():
    mode, m, seed, n = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
    random.seed(seed); F = GF(m); h = m // 2
    st = {'cases': 0, 'solvable': 0, 'unsolvable': 0, 'line_fail': 0, 'degCD_fail': 0, 'a0_zero': 0, 'd0_zero': 0,
          'c0d0_mismatch': 0, 'top_kummer_fail': 0, 'bottom_gen_fail': 0, 'bottom0_fail': 0, 'MI_fail': 0,
          'iv_demo_fail': 0, 'dmin_hist': {}}
    rnz = lambda: random.randrange(1, F.q)
    if mode == 'sharp':
        rho, a = int(sys.argv[5]), int(sys.argv[6])
        out = {'cases': 0, 'aV_hist': {}, 'k': set(), 'e': set(), 'degA': set(), 'inter_eq_rho_minus_e': 0, 'ii_fail': 0}
        FQ = f2_basis([F.mul(x, F.p2(x, h)) for x in range(1, F.q)][:4 * h])
        for _ in range(n):
            lam = rnz()
            while F.p2(lam, h) == lam: lam = rnz()
            K = []
            while len(f2_basis(K)) < a:
                z = 0
                for b in FQ:
                    if random.random() < .5: z ^= b
                if z: K = f2_basis(K + [z])
            R = subspace_poly(F, K)
            assert deg(R) == a and all(tev(F, R, k) == 0 for k in K)
            assert all(F.p2(c, h) == c for c in R)
            il = F.inv(lam); C = [F.mul(c, F.p2(il, e)) for e, c in enumerate(R)]   # C = R o (z/lam)
            imgs = [tev(F, C, 1 << i) for i in range(m)]
            pre = f2_kernel([F.p2(y, h) ^ y for y in imgs])
            kC = len(f2_kernel(imgs)); e = len(pre) - h
            Vb = []
            while len(Vb) < rho - a:
                z = 0
                for b in FQ:
                    if random.random() < .5: z ^= b
                if z: Vb = f2_basis(Vb + [F.mul(lam, z)])
            V = Vb
            while len(V) < rho:
                z = 0
                for b in pre:
                    if random.random() < .5: z ^= b
                if z: V = f2_basis(V + [z])
            aV = defect(F, V, rho)
            sols = lang_solutions(F, C, [F.p2(c, h) for c in C], a)
            allv = f2_basis([pack(F, A) for A in sols])
            best = min(allv, key=lambda v: v.bit_length())
            A = [(best >> (m * i)) & (F.q - 1) for i in range(a + 1)]
            imgA = [tev(F, A, x) for x in FQ]
            inter = len(V) + len(f2_basis(imgA)) - len(f2_basis(V + imgA))
            out['cases'] += 1; out['aV_hist'][aV] = out['aV_hist'].get(aV, 0) + 1
            out['k'].add(kC); out['e'].add(e); out['degA'].add(deg(A))
            if inter == rho - e: out['inter_eq_rho_minus_e'] += 1
            if inter < rho - e: out['ii_fail'] += 1
        # also: V inside lambda F_Q (rho <= h) lies in Vtilde_C but has a(V) = 0  (so V must be specified)
        if rho <= h:
            V0 = f2_basis([F.mul(lam, x) for x in FQ])[:rho]
            out['V_in_lamFQ_defect'] = defect(F, V0, rho)
            out['V_in_lamFQ_inside_Vtilde'] = all(F.p2(tev(F, C, v), h) == tev(F, C, v) for v in V0)
        out = {k: (sorted(v) if isinstance(v, set) else v) for k, v in out.items()}
        print(f"cmd: python3 -I rc_ml.py {' '.join(sys.argv[1:])} | {out}"); return
    a = int(sys.argv[5])
    for _ in range(n):
        st['cases'] += 1
        if mode in ('conj', 'conj0'):
            C = [rnz()] + [random.randrange(F.q) for _ in range(a - 1)] + [rnz()]
            if mode == 'conj0': C = tmul(F, C, [0, 1])            # C*tau : c0 = 0
            D = [F.p2(c, h) for c in C]
            analyse(F, C, D, deg(C) + 1, st)
        else:
            A0 = [rnz()] + [random.randrange(F.q) for _ in range(a - 1)] + [rnz()]
            cd = solve_CD(F, A0, a)
            if cd is None: st['cases'] -= 1; continue
            C, D = cd
            if deg(C) < 0 or deg(D) < 0: st['cases'] -= 1; continue
            if mode == 'gen0': C, D = tmul(F, C, [0, 1]), tmul(F, D, [0, 1])
            analyse(F, C, D, max(deg(A0), deg(C)) + 1, st)
    print(f"cmd: python3 -I rc_ml.py {' '.join(sys.argv[1:])} | {st}")

if __name__ == '__main__':
    main()
