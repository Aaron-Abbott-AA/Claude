#!/usr/bin/env python3
"""Referee check (GLO audit): Theorem OB, Lemma TB, Corollary OB1(a)(b)(c) in finite-field toys.
Independent code (galois library arithmetic).  Run:  nice -n 19 python3 -I glo_ob.py <seed>

Lang operator  Lam(A)_k = sum_i c_i a_{k-i}^{2^i} + d_i a_{k-i}^{Q 2^i}   over F = GF(2^N), F_Q subset F.
For each instance (C, D of degree a2 with c0 d0 c_a2 d_a2 != 0):
  S  := exhaustive set of A in F^{n+1} with Lam(A) = 0 (all k), found layer by layer;
  A0 := a formal solution alpha_0..alpha_n inside F (instance skipped if a root is missing in F);
  OBcount := #{E in F_Q^{n+1} : Lam((A0 E)_{<=n})_k = 0 for k = n+1..n+a2}.
Checks:  |S| == OBcount  (Theorem OB, bijection);  {(A0E)_{<=n}} for those E equals S as a set;
         TB identity Ob_n(E) == lambda(top_n(A0E)) for n >= a2-1 (all E);
         a2 = 1:  S nonzero  <=>  a_top in span_FQ(alpha_0..alpha_n)  (OB1(a), a_top found by search in F
                  if present) ; n = 0: <=> Delta = 0 ; n = 1: <=> Delta*Omega1 = 0  (OB1(b),(c)).
Instance mix (tries mod 4): 0 planted (A of degree <= min(n,a2), kernel of the linear system in (C,D));
1 'kummer' (y0 forced to be a (Q-1)-th power); 2 random; 3 planted FORMAL solution up to tau^n only
(only the equations k <= n imposed), which yields many negative instances with alpha's inside F."""
import sys, random, itertools
import numpy as np
import galois

def run(Q, N, a2, n, ninst, rng, out):
    F = galois.GF(2 ** N)
    allF = F.elements
    FQ = [int(x) for x in allF if int(x ** Q) == int(x)]
    assert len(FQ) == Q
    def P(x, e): return F(x) ** e
    def lam_k(C, D, A, k):
        s = F(0)
        for i in range(a2 + 1):
            j = k - i
            if 0 <= j < len(A):
                s += C[i] * A[j] ** (2 ** i) + D[i] * A[j] ** (Q * 2 ** i)
        return s
    stats = dict(inst=0, pos=0, neg=0, bad=0, planted=0, tb_checked=0)
    tries = 0
    while stats['inst'] < ninst and tries < 400 * ninst:
        tries += 1
        mode = tries % 4
        if mode in (0, 3):
            # mode 0: planted polynomial solution of degree <= min(n, a2);
            # mode 3: planted FORMAL solution up to tau^n only (equations k = 0..n), generic top block
            dA = rng.randint(0, min(n, a2)) if mode == 0 else n
            A = [F(rng.randrange(1, 2 ** N)) for _ in range(dA + 1)]
            rows = []
            for k in range(dA + a2 + 1 if mode == 0 else n + 1):
                row = []
                for i in range(a2 + 1):
                    j = k - i
                    row.append(int(A[j] ** (2 ** i)) if 0 <= j <= dA else 0)
                for i in range(a2 + 1):
                    j = k - i
                    row.append(int(A[j] ** (Q * 2 ** i)) if 0 <= j <= dA else 0)
                rows.append(row)
            M = F(rows)
            ns = M.null_space()
            if ns.shape[0] == 0: continue
            v = F.Zeros(2 * (a2 + 1))
            for r in range(ns.shape[0]):
                v = v + F(rng.randrange(1, 2 ** N)) * ns[r]
            C = [v[i] for i in range(a2 + 1)]; D = [v[a2 + 1 + i] for i in range(a2 + 1)]
        else:
            C = [F(rng.randrange(1, 2 ** N)) for _ in range(a2 + 1)]
            D = [F(rng.randrange(1, 2 ** N)) for _ in range(a2 + 1)]
            if mode == 1:
                t = F(rng.randrange(1, 2 ** N)); C[0] = D[0] * t ** (Q - 1)
        if not all(int(x) for x in (C[0], D[0], C[a2], D[a2])): continue
        c0, d0 = C[0], D[0]
        ell = d0 * allF ** Q + c0 * allF       # ell_0 on all of F (vectorised)
        # formal solution inside F
        al = []
        ok = True
        for k in range(n + 1):
            r = F(0)
            for i in range(1, a2 + 1):
                j = k - i
                if j >= 0:
                    r += C[i] * al[j] ** (2 ** i) + D[i] * al[j] ** (Q * 2 ** i)
            idx = np.nonzero(ell == r)[0]
            if k == 0: idx = idx[idx != 0]
            if len(idx) == 0: ok = False; break
            al.append(allF[int(rng.choice(list(idx)))])
        if not ok: continue
        # exhaustive layered search
        partial = [[]]
        for k in range(n + 1):
            new = []
            for Pp in partial:
                r = F(0)
                for i in range(1, a2 + 1):
                    j = k - i
                    if j >= 0:
                        r += C[i] * Pp[j] ** (2 ** i) + D[i] * Pp[j] ** (Q * 2 ** i)
                for x in np.nonzero(ell == r)[0]:
                    new.append(Pp + [allF[int(x)]])
            partial = new
        S = set()
        for A in partial:
            if all(int(lam_k(C, D, A, k)) == 0 for k in range(n + 1, n + a2 + 1)):
                S.add(tuple(int(a) for a in A))
        # Theorem OB count
        def trunc(E):
            return [sum((al[k - i] * F(E[i]) ** (2 ** (k - i)) for i in range(k + 1)), F(0)) for k in range(n + 1)]
        OBset = set(); bad = False
        for E in itertools.product(FQ, repeat=n + 1):
            T = trunc(E)
            ob = [lam_k(C, D, T, k) for k in range(n + 1, n + a2 + 1)]
            if n >= a2 - 1:
                # TB: lambda(top) with top = (t_{n-a2+1}, ..., t_n) indexed j = 1..a2
                top = {j: T[n - a2 + j] for j in range(1, a2 + 1)}
                lam = []
                for kk in range(1, a2 + 1):
                    s = F(0)
                    for j in range(kk, a2 + 1):
                        e = a2 + kk - j
                        s += C[e] * top[j] ** (2 ** e) + D[e] * top[j] ** (Q * 2 ** e)
                    lam.append(s)
                if [int(x) for x in lam] != [int(x) for x in ob]: bad = True
                stats['tb_checked'] += 1
            if all(int(x) == 0 for x in ob):
                OBset.add(tuple(int(t) for t in T))
        if OBset != S: bad = True
        nz = any(any(a) for a in S)
        if a2 == 1:
            c1, d1 = C[1], D[1]
            Dl = c1 * d0 ** 2 + d1 * c0 ** 2
            Om = c0 ** 4 * d1 ** Q * Dl ** (Q - 1) + c1 * d0 ** (4 * Q)
            tops = [x for x in allF if int(x) and int(d1 * x ** (2 * Q)) == int(c1 * x ** 2)]
            if tops:
                span = set()
                for E in itertools.product(FQ, repeat=n + 1):
                    span.add(int(sum((al[j] * F(E[j]) for j in range(n + 1)), F(0))))
                if (int(tops[0]) in span) != nz: bad = True
            if n == 0 and ((int(Dl) == 0) != nz): bad = True
            if n == 1 and ((int(Dl * Om) == 0) != nz): bad = True
        stats['inst'] += 1; stats['planted'] += (mode == 0); stats['formal'] = stats.get('formal', 0) + (mode == 3)
        stats['pos' if nz else 'neg'] += 1
        if bad:
            stats['bad'] += 1
            out.append(f"  MISMATCH Q={Q} N={N} a2={a2} n={n} C={[int(x) for x in C]} D={[int(x) for x in D]}")
    return stats

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 20261007
    rng = random.Random(seed)
    print(f"glo_ob seed={seed} galois {galois.__version__}")
    plan = [(4, 6, 1, 0, 30), (4, 6, 1, 1, 40), (4, 6, 1, 2, 20), (4, 10, 1, 1, 16), (8, 9, 1, 1, 16),
            (4, 8, 1, 1, 16), (4, 6, 2, 1, 20), (4, 6, 2, 2, 12), (4, 6, 3, 2, 8), (4, 6, 3, 3, 6),
            (4, 8, 2, 2, 8), (8, 9, 2, 1, 10)]
    for (Q, N, a2, n, k) in plan:
        out = []
        s = run(Q, N, a2, n, k, rng, out)
        tag = "F_{Q^2} in F" if N % (2 * (Q.bit_length() - 1)) == 0 else "F_{Q^2} not in F"
        print(f"Q={Q} N={N} ({tag}) a2={a2} n={n}: {s}")
        for line in out: print(line)
