#!/usr/bin/env python3
"""Referee revision-check scripts for TCR v2 (independent code; reads no files).
Usage: python3 -I tcrv2_referee_checks.py MODE [args]
  frame SEED      FIX-1: frame dependence of Prop 216.3 / pair uniqueness on parabola-subspace
                  hyperfocused arcs R={(a,a^2): a in A0}, q=64,256, n=4,8,16.
  hasse SEED N    HF re-check with galois: (H1),(H2) and rank(D^(2^k)|W_k) = dim W_k - dim W_{k+1}.
  cdind           m5: CD induction invariant over all abstract level paths, rho' <= 24.
  arith           2a*+4 table, a* <= rho/2-2, v-n margin, pair-count bounds (sympy).
"""
import sys, random, itertools
import numpy as np

def frame(seed):
    import galois
    rnd = random.Random(seed)
    out = []
    for m in (6, 8):
        F = galois.GF(2 ** m)
        q = 2 ** m
        for k in (2, 3, 4):
            n = 2 ** k
            # random k-dim F2-subspace A0
            while True:
                gens = [rnd.randrange(1, q) for _ in range(k)]
                A0 = {0}
                for g in gens:
                    A0 |= {a ^ g for a in A0}
                if len(A0) == n:
                    break
            A0 = sorted(A0)
            R0 = [(F(a), F(a) ** 2) for a in A0]

            def transform(R, M, c):
                (m11, m12), (m21, m22) = M
                return [(m11 * x + m12 * y + c[0], m21 * x + m22 * y + c[1]) for x, y in R]

            def analyse(R, tag):
                # slopes of secants
                slopes = {}
                for P, P2 in itertools.combinations(R, 2):
                    dx, dy = P[0] + P2[0], P[1] + P2[1]
                    s = 'inf' if int(dx) == 0 else int(dy / dx)
                    slopes.setdefault(s, []).append((P, P2))
                hyper = len(slopes) == n - 1 and all(len(v) == n // 2 for v in slopes.values())
                inf_focus = 'inf' in slopes
                fin_nonfoci = [mu for mu in range(q) if mu not in slopes]

                def proj(mu):
                    if mu == 'inf':
                        return [int(x) for x, y in R]
                    M_ = F(mu)
                    return [int(y + M_ * x) for x, y in R]

                def rad(img):
                    S = set(img)
                    assert len(S) == n  # nonfocus => injective
                    u0 = img[0]
                    cand = [u ^ u0 for u in img if u != u0]
                    r = {b for b in cand if all((u ^ b) in S for u in img)}
                    # two-level autocorrelation check: A(b)=n exactly on r
                    ac = {}
                    for u in img:
                        for w in img:
                            if u != w:
                                ac[u ^ w] = ac.get(u ^ w, 0) + 1
                    assert {b for b, c in ac.items() if c == n} == r
                    return r
                cnt_fin, cnt_all = {}, {}
                rads = {}
                for mu in fin_nonfoci:
                    rads[mu] = rad(proj(mu))
                    for b in rads[mu]:
                        cnt_fin[b] = cnt_fin.get(b, 0) + 1
                        cnt_all[b] = cnt_all.get(b, 0) + 1
                if not inf_focus:
                    rinf = rad(proj('inf'))
                    for b in rinf:
                        cnt_all[b] = cnt_all.get(b, 0) + 1
                # pair uniqueness among finite nonfoci
                pu_fin = True
                pu_all = True
                for P, P2 in itertools.combinations(R, 2):
                    dx, dy = P[0] + P2[0], P[1] + P2[1]
                    vals = [int(dy + F(mu) * dx) for mu in fin_nonfoci]
                    if len(set(vals)) < len(vals):
                        pu_fin = False
                    if not inf_focus:
                        if int(dx) in vals:
                            pu_all = False
                mx_fin = max(cnt_fin.values()) if cnt_fin else 0
                mx_all = max(cnt_all.values()) if cnt_all else 0
                out.append(f"q={q} n={n} {tag}: hyperfocused={hyper} inf_focus={inf_focus} "
                           f"#fin_nonfoci={len(fin_nonfoci)} pair_uniq_fin={pu_fin} "
                           f"pair_uniq_incl_inf={'n/a' if inf_focus else pu_all} "
                           f"max#fin_radicals_per_b={mx_fin} (n-1={n-1}) "
                           f"max#all_nonfocus_radicals_per_b={mx_all} (n={n})")
                return slopes, fin_nonfoci, rads, mx_fin, mx_all, inf_focus, pu_fin

            res = analyse(R0, "original")
            assert res[3] <= n - 1 and res[4] <= n
            # random frames with vertical a nonfocus
            for t in range(3):
                while True:
                    M = [[F(rnd.randrange(q)) for _ in range(2)] for _ in range(2)]
                    if int(M[0][0] * M[1][1] + M[0][1] * M[1][0]) == 0:
                        continue
                    c = (F(rnd.randrange(q)), F(rnd.randrange(q)))
                    R = transform(R0, M, c)
                    if all(int(P[0] + P2[0]) != 0 for P, P2 in itertools.combinations(R, 2)):
                        break
                res = analyse(R, f"randframe{t}(vert nonfocus)")
                assert res[6] and res[3] <= n - 1 and res[4] <= n
            # focus-vertical frame: (X,Y) = (t0 x + y, x) maps (1,t0) to (0,1)
            t0 = F(A0[1])
            M = [[t0, F(1)], [F(1), F(0)]]
            c = (F(rnd.randrange(q)), F(rnd.randrange(q)))
            R = transform(R0, M, c)
            slopes, finnf, rads, mxf, mxa, inff, puf = analyse(R, "focus-vertical")
            allhave = all(int(t0) in r for r in rads.values())
            out.append(f"   focus-vertical: b=t0 lies in all {len(finnf)} finite nonfocus radicals: {allhave}; "
                       f"pair_uniq_fin={puf}")
            assert inff and allhave and mxf == len(finnf)
    print("\n".join(out))
    print("frame: all assertions passed")

def hasse(seed, N):
    import galois
    rnd = random.Random(seed)
    m = 10
    F = galois.GF(2 ** m)
    q = 2 ** m
    def P(coefs):  # ascending
        return list(coefs)
    def pmul(a, b):
        r = [F(0)] * (len(a) + len(b) - 1)
        for i, x in enumerate(a):
            if int(x):
                for j, y in enumerate(b):
                    r[i + j] = r[i + j] + x * y
        return r
    def frob(a, k):
        for _ in range(k):
            a = pmul(a, a)
        return a
    def hd(a, e):
        return [a[i] if (i & e) == e else F(0) for i in range(e, len(a))] or [F(0)]
    def trim(a):
        a = list(a)
        while len(a) > 1 and int(a[-1]) == 0:
            a.pop()
        return [int(x) for x in a]
    bad1 = bad2 = bad3 = 0
    nz = 0
    for t in range(N):
        k = rnd.randrange(4)
        deg = rnd.randrange(7)
        s = [F(rnd.randrange(q)) for _ in range(deg + 1)]
        if rnd.random() < 0.5:
            s = [x if i % 2 == 0 else F(0) for i, x in enumerate(s)]
        w = frob(s, k)
        lhs = trim(hd(w, 1 << k))
        rhs = trim(frob(hd(s, 1), k))
        bad1 += lhs != rhs
        sz = all(int(x) == 0 for x in hd(s, 1))
        nz += sz
        win = all(int(x) == 0 for i, x in enumerate(w) if i % (1 << (k + 1)))
        bad2 += sz != win
    # rank equivalence on random F2-spaces W_k = span{s_i^{2^k}}
    def bits(vec, L):
        v = 0
        for i in range(L):
            x = int(vec[i]) if i < len(vec) else 0
            v |= x << (m * i)
        return v
    def f2rank(vs):
        basis = []
        for v in vs:
            for b in basis:
                v = min(v, v ^ b)
            if v:
                basis.append(v)
        return len(basis)
    trials3 = max(1, N // 5)
    for t in range(trials3):
        k = rnd.randrange(3)
        dimgen = rnd.randrange(2, 8)
        gens = []
        for i in range(dimgen):
            deg = rnd.randrange(1, 6)
            s = [F(rnd.randrange(q)) for _ in range(deg + 1)]
            if rnd.random() < 0.5:
                s = [x if j % 2 == 0 else F(0) for j, x in enumerate(s)]
            gens.append(s)
        ws = [frob(s, k) for s in gens]
        L = max(len(w) for w in ws) + 1
        dimW = f2rank([bits(w, L) for w in ws])
        Dw = [hd(w, 1 << k) for w in ws]
        rkD = f2rank([bits(d, L) for d in Dw])
        # dim W_{k+1} = dim W_k - rank(projection to exponents not divisible by 2^{k+1})
        proj = [[x if i % (1 << (k + 1)) else F(0) for i, x in enumerate(w)] for w in ws]
        rkP = f2rank([bits(p, L) for p in proj])
        bad3 += rkD != rkP
    print(f"hasse (galois GF(2^{m}), seed {seed}): {N} samples, s'=0 cases {nz}; (H1) failures {bad1}; "
          f"(H2) failures {bad2}; rank(D^(2^k)|W_k)=dimW_k-dimW_(k+1) on {trials3} random spaces: failures {bad3}")

def cdind():
    bad = 0
    states_total = 0
    for rp in range(4, 25):
        for a2 in range(0, rp // 2 - 1):
            if a2 > rp / 2 - 2:
                continue
            start = (rp, a2)
            seen = {start}
            stack = [start]
            while stack:
                d, a = stack.pop()
                # invariant + derived bound
                if not (d >= rp - 2 * (a2 - a) and a <= d / 2 - 2 and d >= rp - 2 * a2 >= 4):
                    bad += 1
                # lossless: a' <= a ; lossy (only allowed with dim drop 1..2 and a' <= a-1, a' >= 0)
                nxt = [(d, a2_) for a2_ in range(0, a + 1)]
                if a >= 1:
                    nxt += [(d - dd, a_) for dd in (1, 2) for a_ in range(0, a)]
                for s in nxt:
                    if s not in seen:
                        seen.add(s)
                        stack.append(s)
            states_total += len(seen)
    print(f"cdind: rho' in [4,24], all a2 <= rho'/2-2, {states_total} reachable (dim,defect) states; invariant failures {bad}")

def arith():
    import sympy as sp
    bad = 0
    cells = 0
    for rho in range(4, 62, 2):
        for g in range(rho + 3, 2 * rho + 1):
            cells += 1
            astar = rho - (g + 1) // 2
            req = 2 * astar + 4
            if req != 2 * rho - 2 * ((g + 1) // 2) + 4: bad += 1
            if not (astar <= rho / 2 - 2): bad += 1
            if g == 2 * rho - 2 and req != 6: bad += 1
            if g in (rho + 3, rho + 4) and req != rho: bad += 1
            if req > rho: bad += 1
    q, d = sp.symbols('q d', positive=True)
    n = q / 2 - d
    foci = n - 1                      # STATE §1: exactly n-1 secant slopes
    nonfoci_all = (q + 1) - foci
    nonfoci_fin = nonfoci_all - 1     # if the comparison direction is a nonfocus
    m_all = sp.simplify(nonfoci_all - n)
    m_fin = sp.simplify(nonfoci_fin - n)
    # pair counting: n(n-1)/2 unordered pairs, each mu with b in Rad_mu uses n/2 pairs
    nn = sp.symbols('n', positive=True)
    bound = sp.simplify((nn * (nn - 1) / 2) / (nn / 2))
    print(f"arith: {cells} even cells rho<=60, failures {bad}; v-n margins: all nonfoci {m_all}, finite nonfoci {m_fin}; "
          f"pair-count bound #mu <= {bound} (+1 if the comparison projection is included)")

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'frame': frame(int(sys.argv[2]))
    elif mode == 'hasse': hasse(int(sys.argv[2]), int(sys.argv[3]))
    elif mode == 'cdind': cdind()
    elif mode == 'arith': arith()
