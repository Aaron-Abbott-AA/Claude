#!/usr/bin/env python3
"""GLO checks (Claude DZ cloud owner, 7 Oct 2026).  Own code; run as
    nice -n 19 python3 -I glocheck.py <seed>
Pure-python GF(2^N) arithmetic (log tables).  Q = 2^h plays the role of 2^{m/2}.
Lang operator: Lam(A)_k = sum_i c_i a_{k-i}^{2^i} + d_i a_{k-i}^{Q 2^i}   (char 2).

T1  a2 = 1, n <= 1, fields NOT containing F_{Q^2} (non-pointwise) plus controls:
    exhaustive layered search for nonzero solutions of degree <= 1  <=>  Delta*Omega1 == 0
    <=>  a_top in F_Q alpha_0 + F_Q alpha_1;  and #solutions == #{E in F_Q^2 : (A0 E)_1 in a_top F_Q}.
T2  pointwise identity PV: over F_{Q^2}, D = kappa*Cbar with kappa^{Q+1} = 1  =>  Delta*Omega1 == 0.
T3  a2 = 2, n = 1, 2: exhaustive layered search count == count of truncations (A0 E)_{<=n}
    (E in F_Q[tau]_{<=n}) whose top block satisfies the a2 top equations  (Theorem OB).
"""
import sys, random

PRIM = {4: 0b10011, 6: 0b1000011, 8: 0b100011101, 9: 0b1000010001, 10: 0b10000001001,
        12: 0b1000001010011}

class GF:
    def __init__(self, N):
        self.N = N; self.size = 1 << N; poly = PRIM[N]
        self.exp = [0] * (2 * self.size); self.log = [0] * self.size
        x = 1
        for i in range(self.size - 1):
            self.exp[i] = x; self.log[x] = i
            x <<= 1
            if x & self.size: x ^= poly
        assert x == 1, "not primitive"
        # primitivity: order of generator is exactly 2^N-1
        assert len(set(self.exp[:self.size - 1])) == self.size - 1
        for i in range(self.size - 1, 2 * self.size): self.exp[i] = self.exp[i - (self.size - 1)]
    def mul(self, a, b):
        if a == 0 or b == 0: return 0
        return self.exp[self.log[a] + self.log[b]]
    def inv(self, a):
        assert a
        return self.exp[(self.size - 1 - self.log[a]) % (self.size - 1)]
    def pw(self, a, e):
        if a == 0: return 0 if e > 0 else 1
        return self.exp[(self.log[a] * e) % (self.size - 1)]
    def rnz(self, rng): return rng.randrange(1, self.size)

def lam_coef(F, C, D, A, k, Q):
    """coefficient k of C*A + D*phi(A); C, D lists (index i), A list."""
    s = 0
    for i in range(len(C)):
        j = k - i
        if 0 <= j < len(A):
            s ^= F.mul(C[i], F.pw(A[j], 1 << i)) ^ F.mul(D[i], F.pw(A[j], Q << i))
    return s

def layered_solutions(F, C, D, n, Q):
    """all A=(a_0..a_n) in F^{n+1} with Lam(A)=0 (all coefficients 0..n+a2); exhaustive per layer."""
    a2 = len(C) - 1
    partial = [[]]
    for k in range(n + 1):
        new = []
        for P in partial:
            for x in range(F.size):
                A = P + [x]
                if lam_coef(F, C, D, A, k, Q) == 0:
                    new.append(A)
        partial = new
    out = []
    for A in partial:
        if all(lam_coef(F, C, D, A, k, Q) == 0 for k in range(n + 1, n + a2 + 1)):
            out.append(A)
    return out

def subfield(F, Q):
    return [x for x in range(F.size) if F.pw(x, Q) == x]

def roots_lang(F, d0, c0, r, Q):
    return [x for x in range(F.size) if F.mul(d0, F.pw(x, Q)) ^ F.mul(c0, x) == r]

def formal_solution(F, C, D, n, Q, rng):
    """alpha_0..alpha_n of a formal solution with alpha_0 != 0, inside F; None if a root is missing."""
    c0, d0 = C[0], D[0]
    r0 = [x for x in range(1, F.size) if F.mul(d0, F.pw(x, Q)) == F.mul(c0, x)]
    if not r0: return None
    al = [rng.choice(r0)]
    for k in range(1, n + 1):
        r = 0
        for i in range(1, len(C)):
            j = k - i
            if j >= 0:
                r ^= F.mul(C[i], F.pw(al[j], 1 << i)) ^ F.mul(D[i], F.pw(al[j], Q << i))
        rts = roots_lang(F, d0, c0, r, Q)
        if not rts: return None
        al.append(rng.choice(rts))
    return al

def times_E(F, al, E, n):
    """(A0 * E)_{<= n} with E in F_Q[tau]: coefficient k = sum_i al_{k-i} e_i^{2^{k-i}}."""
    return [__import__('functools').reduce(lambda u, v: u ^ v,
            [F.mul(al[k - i], F.pw(E[i], 1 << (k - i))) for i in range(min(k, len(E) - 1) + 1)], 0)
            for k in range(n + 1)]

def delta_omega(F, C, D, Q):
    c0, c1 = C; d0, d1 = D
    Dl = F.mul(c1, F.mul(d0, d0)) ^ F.mul(d1, F.mul(c0, c0))
    Om = F.mul(F.pw(c0, 4), F.mul(F.pw(d1, Q), F.pw(Dl, Q - 1))) ^ F.mul(c1, F.pw(d0, 4 * Q))
    return Dl, Om

def T1(rng, Q, N, ninst):
    F = GF(N); FQ = subfield(F, Q); assert len(FQ) == Q
    stats = dict(inst=0, pos=0, neg=0, bad=0, planted=0)
    tries = 0
    while stats['inst'] < ninst and tries < 50 * ninst:
        tries += 1
        planted = (stats['inst'] % 2 == 0)
        if planted:
            a0, a1 = F.rnz(rng), F.rnz(rng); d1 = F.rnz(rng)
            c1 = F.mul(d1, F.pw(a1, 2 * (Q - 1)))
            den = F.mul(F.pw(a0, Q - 1), a1) ^ F.pw(a1, Q)
            num = F.mul(d1, F.mul(F.pw(a1, 2 * (Q - 1)), F.mul(a0, a0)) ^ F.pw(a0, 2 * Q))
            if den == 0 or num == 0: continue
            d0 = F.mul(num, F.inv(den)); c0 = F.mul(d0, F.pw(a0, Q - 1))
            atop = a1
        else:
            al0, atop = F.rnz(rng), F.rnz(rng); d0, d1 = F.rnz(rng), F.rnz(rng)
            c0 = F.mul(d0, F.pw(al0, Q - 1)); c1 = F.mul(d1, F.pw(atop, 2 * (Q - 1)))
        C, D = [c0, c1], [d0, d1]
        al = formal_solution(F, C, D, 1, Q, rng)
        if al is None: continue
        sols = layered_solutions(F, C, D, 1, Q)
        nz = [A for A in sols if any(A)]
        Dl, Om = delta_omega(F, C, D, Q)
        crit = (F.mul(Dl, Om) == 0)
        span = set()
        for x in FQ:
            for y in FQ: span.add(F.mul(al[0], x) ^ F.mul(al[1], y))
        atopFQ = set(F.mul(atop, z) for z in FQ)
        spancrit = atop in span
        cntE = sum(1 for e0 in FQ for e1 in FQ if times_E(F, al, [e0, e1], 1)[1] in atopFQ)
        ok = (bool(nz) == crit == spancrit) and (cntE == len(sols))
        if planted and not nz: ok = False
        stats['inst'] += 1; stats['planted'] += planted
        stats['pos' if nz else 'neg'] += 1
        if not ok:
            stats['bad'] += 1
            print("  MISMATCH", Q, N, C, D, len(nz), crit, spancrit, cntE, len(sols))
    return stats

def T2(rng, Q, N, ninst):
    F = GF(N); assert F.size == Q * Q
    kap = [x for x in range(1, F.size) if F.pw(x, Q + 1) == 1]
    bad = 0
    for _ in range(ninst):
        c0, c1 = F.rnz(rng), F.rnz(rng); k = rng.choice(kap)
        C = [c0, c1]; D = [F.mul(k, F.pw(c0, Q)), F.mul(k, F.pw(c1, Q))]
        Dl, Om = delta_omega(F, C, D, Q)
        if F.mul(Dl, Om) != 0: bad += 1
    return bad

def T3(rng, Q, N, ninst, n):
    F = GF(N); FQ = subfield(F, Q); a2 = 2
    done = bad = pos = 0; tries = 0
    while done < ninst and tries < 200 * ninst:
        tries += 1
        if tries % 2 == 0:
            # plant a solution of degree n: solve the linear system C*A = D*phi(A) for (C, D)
            A = [F.rnz(rng) for _ in range(n + 1)]
            # unknowns c0,c1,c2,d0,d1,d2 ; equations k = 0..n+2 ; brute small search for a kernel vector
            rows = []
            for k in range(n + a2 + 1):
                row = []
                for i in range(a2 + 1):
                    j = k - i
                    row.append(F.pw(A[j], 1 << i) if 0 <= j <= n else 0)
                for i in range(a2 + 1):
                    j = k - i
                    row.append(F.pw(A[j], Q << i) if 0 <= j <= n else 0)
                rows.append(row)
            ker = kernel(F, rows, 2 * (a2 + 1))
            if not ker: continue
            v = [0] * (2 * (a2 + 1))
            for kv in ker:
                cf = F.rnz(rng)
                v = [x ^ F.mul(cf, y) for x, y in zip(v, kv)]
            C, D = v[:a2 + 1], v[a2 + 1:]
        else:
            C = [F.rnz(rng) for _ in range(a2 + 1)]; D = [F.rnz(rng) for _ in range(a2 + 1)]
        if not (C[0] and D[0] and C[a2] and D[a2]): continue
        al = formal_solution(F, C, D, n, Q, rng)
        if al is None: continue
        sols = layered_solutions(F, C, D, n, Q)
        cnt = 0
        import itertools
        for E in itertools.product(FQ, repeat=n + 1):
            T = times_E(F, al, list(E), n)
            if all(lam_coef(F, C, D, T, k, Q) == 0 for k in range(n + 1, n + a2 + 1)):
                cnt += 1
        done += 1
        if any(any(s) for s in sols): pos += 1
        if cnt != len(sols):
            bad += 1; print("  T3 MISMATCH", C, D, cnt, len(sols))
    return done, pos, bad

def kernel(F, rows, ncols):
    M = [r[:] for r in rows]; piv = []; r = 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if M[i][c]), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        iv = F.inv(M[r][c]); M[r] = [F.mul(iv, x) for x in M[r]]
        for i in range(len(M)):
            if i != r and M[i][c]:
                f = M[i][c]; M[i] = [x ^ F.mul(f, y) for x, y in zip(M[i], M[r])]
        piv.append(c); r += 1
    free = [c for c in range(ncols) if c not in piv]
    out = []
    for fc in free:
        v = [0] * ncols; v[fc] = 1
        for i, pc in enumerate(piv): v[pc] = M[i][fc]
        out.append(v)
    return out

if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = random.Random(seed)
    print(f"glocheck seed={seed}")
    for (Q, N, k) in [(4, 6, 40), (8, 9, 30), (4, 10, 20), (8, 12, 10)]:
        tag = "F_{Q^2} subset F" if N % (2 * (Q.bit_length() - 1)) == 0 else "F_{Q^2} NOT subset F"
        s = T1(rng, Q, N, k)
        print(f"T1 Q={Q} N={N} ({tag}): {s}")
    for (Q, N) in [(4, 4), (8, 6), (16, 8), (32, 10)]:
        print(f"T2 PV Q={Q} F_{{Q^2}}=GF(2^{N}): failures {T2(rng, Q, N, 300)}/300")
    for n in (1, 2):
        d, p, b = T3(rng, 4, 6, 12 if n == 2 else 20, n)
        print(f"T3 a2=2 n={n} Q=4 N=6: instances {d}, with nonzero solution {p}, count mismatches {b}")
