#!/usr/bin/env python3
"""Referee checks for TCR (independent code; reads no files).

Usage: python3 -I tcr_referee_checks.py {hasse|cd|p216|arith} [seed] [count]

hasse : Hasse identity D^{(2^k)}(s^{2^k}) = (s')^{2^k}, filtration equivalence with
        STRUCTURED s (half in F_q[X^2]), and Lemma HF(ii) (iterated sqrt-descendant
        equals W_k^{1/2^k}) on random F_2-spaces W of polynomials.
cd    : stress test of Lemma CD on random rational families W subset F_q[X]
        (q = 2^24, Q = 2^12; generic point taken in F_{2^48}).
        Checks: (P1) a(k) non-increasing; (P2) lossy level with dim W_{k+1} >= 2a(k)+2
        => a(k+1) <= a(k)-1; (P3) all RR_k (rank <= 2) and a(0) <= rho'/2-2
        => dim(W cap F_q) >= rho' - 2a(0).  Also cross-checks rank D^{(2^k)} = dim W_k - dim W_{k+1}.
p216  : frame dependence of Prop 216.3 on parabola-subspace hyperfocused arcs.
arith : numerical range / bookkeeping of TCR section 4 and the v > n-1 inequality.
"""
import sys, random

# ---------------- GF(2^48) with primitive modulus ----------------
MBIG = 48
MOD = (1 << 48) | 0b10110111  # x^48 + x^7 + x^5 + x^4 + x^2 + x + 1

def gmul(a, b):
    r = 0
    while b:
        if b & 1:
            r ^= a
        b >>= 1
        a <<= 1
        if a >> MBIG:
            a ^= MOD
    return r

def gpow(a, e):
    r = 1
    while e:
        if e & 1:
            r = gmul(r, a)
        a = gmul(a, a)
        e >>= 1
    return r

def ginv(a):
    assert a
    return gpow(a, (1 << MBIG) - 2)

def frob(a, k):
    for _ in range(k):
        a = gmul(a, a)
    return a

ORDER = (1 << MBIG) - 1
GEN = 2  # x is primitive (checked in main via galois)

def subfield_gen(m):
    return gpow(GEN, ORDER // ((1 << m) - 1))

def rand_sub(m, rng):
    h = subfield_gen(m)
    r = rng.randrange(0, 1 << m)
    return 0 if r == 0 else gpow(h, r)

# ---------------- polynomials over GF(2^48): list of coeffs ----------------
def ptrim(P):
    P = list(P)
    while len(P) > 1 and P[-1] == 0:
        P.pop()
    return P

def padd(P, R):
    n = max(len(P), len(R))
    return ptrim([(P[i] if i < len(P) else 0) ^ (R[i] if i < len(R) else 0) for i in range(n)])

def pscale(P, c):
    return ptrim([gmul(c, x) for x in P])

def pmulp(P, R):
    out = [0] * (len(P) + len(R) - 1)
    for i, a in enumerate(P):
        if a:
            for j, b in enumerate(R):
                if b:
                    out[i + j] ^= gmul(a, b)
    return ptrim(out)

def pfrob(P, k):  # P^{2^k}
    out = [0] * ((len(P) - 1) * (1 << k) + 1)
    for i, a in enumerate(P):
        out[i << k] = frob(a, k)
    return ptrim(out)

def hasse(P, n):
    if len(P) <= n:
        return [0]
    return ptrim([P[i] if (i & n) == n else 0 for i in range(n, len(P))])

def deriv(P):
    return hasse(P, 1)

def peval(P, x):
    r = 0
    for a in reversed(P):
        r = gmul(r, x) ^ a
    return r

def pconjcoef(P, mhalf):  # coefficients raised to Q = 2^{m/2}
    return [frob(a, mhalf) for a in P]

def proot2k(P, k):  # P in F_q[X^{2^k}], q = 2^m subfield: s with s^{2^k} = P
    assert all(c == 0 for i, c in enumerate(P) if i % (1 << k))
    s = [P[i] for i in range(0, len(P), 1 << k)]
    # inverse Frobenius on GF(2^48): a^{2^{48-k}}
    return ptrim([frob(c, MBIG - k) for c in s])

# ---------------- F_2-linear algebra on polynomial lists ----------------
def tobits(P, L):
    v = 0
    for i in range(L):
        c = P[i] if i < len(P) else 0
        v |= c << (MBIG * i)
    return v

def f2_kernel(images):
    """images: list of ints (bitvectors). Returns basis of kernel as list of masks over input index."""
    rows = []  # (vec, mask)
    kern = []
    for idx, v in enumerate(images):
        mask = 1 << idx
        for (rv, rm) in rows:
            if v ^ rv < v:  # leading bit of rv is set in v
                v ^= rv
                mask ^= rm
        if v == 0:
            kern.append(mask)
        else:
            rows.append((v, mask))
            rows.sort(key=lambda t: -t[0])
    return kern

def f2_rank(vecs):
    basis = []
    for v in vecs:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    return len(basis)

def combine(basis, mask):
    P = [0]
    i = 0
    while mask:
        if mask & 1:
            P = padd(P, basis[i])
        mask >>= 1
        i += 1
    return P

def subspace_filter(basis, k, L):
    """W cap F_q[X^{2^k}]: kernel of the map to coefficients at exponents not divisible by 2^k."""
    imgs = []
    for P in basis:
        Q = [P[i] if (i < len(P) and i % (1 << k)) else 0 for i in range(L)]
        imgs.append(tobits(Q, L))
    kern = f2_kernel(imgs)
    return [combine(basis, msk) for msk in kern]

def f2_dim(basis, L):
    return f2_rank([tobits(P, L) for P in basis])

# ---------------- rank over GF(2^48) ----------------
def grank(M):
    M = [list(r) for r in M]
    rk = 0
    ncol = len(M[0]) if M else 0
    for c in range(ncol):
        piv = None
        for r in range(rk, len(M)):
            if M[r][c]:
                piv = r
                break
        if piv is None:
            continue
        M[rk], M[piv] = M[piv], M[rk]
        inv = ginv(M[rk][c])
        M[rk] = [gmul(inv, x) for x in M[rk]]
        for r in range(len(M)):
            if r != rk and M[r][c]:
                f = M[r][c]
                M[r] = [x ^ gmul(f, y) for x, y in zip(M[r], M[rk])]
        rk += 1
    return rk

def bivariate_defect(basis, mhalf, pts):
    """min a with rank[w(x)^{2^e} | w^{(Q)}(y)^{2^e}]_{e<=a} < 2a+2 (max rank over pts)."""
    r = len(basis)
    if r == 0:
        return None
    a = 0
    while True:
        if 2 * a + 2 > r:
            return a
        best = 0
        for (x, y) in pts:
            M = []
            for P in basis:
                wx = peval(P, x)
                wy = peval(pconjcoef(P, mhalf), y)
                M.append([frob(wx, e) for e in range(a + 1)] + [frob(wy, e) for e in range(a + 1)])
            best = max(best, grank(M))
        if best < 2 * a + 2:
            return a
        a += 1

# ---------------- checks ----------------
def check_hasse(seed, count):
    rng = random.Random(seed)
    m = 24
    bad1 = bad2 = 0
    nzero = 0
    for _ in range(count):
        k = rng.randrange(0, 4)
        deg = rng.randrange(0, 9)
        s = [rand_sub(m, rng) for _ in range(deg + 1)]
        if rng.random() < 0.5:  # force s in F_q[X^2]
            s = [c if i % 2 == 0 else 0 for i, c in enumerate(s)]
        s = ptrim(s)
        w = pfrob(s, k)
        if hasse(w, 1 << k) != pfrob(deriv(s), k):
            bad1 += 1
        sp0 = all(c == 0 for c in deriv(s))
        nzero += sp0
        win = all(c == 0 for i, c in enumerate(w) if i % (1 << (k + 1)))
        if sp0 != win:
            bad2 += 1
    # HF(ii): iterated descendant vs W_k^{1/2^k}
    bad3 = 0
    tests3 = 0
    for _ in range(max(1, count // 20)):
        L = 33
        basis = []
        for _ in range(rng.randrange(3, 8)):
            # mixtures: constants, squares, 4th powers, generic
            t = rng.randrange(4)
            s = ptrim([rand_sub(m, rng) for _ in range(rng.randrange(1, 5))])
            basis.append(ptrim(pfrob(s, t)[:L]))
        # independent subset
        indep = []
        for P in basis:
            if f2_dim(indep + [P], L) == len(indep) + 1:
                indep.append(P)
        cur = indep
        for k in range(1, 6):
            # descendant step: sqrt(cur cap F_q[X^2])
            cur0 = subspace_filter(cur, 1, L)
            cur = [proot2k(P, 1) for P in cur0]
            Wk = subspace_filter(indep, k, L)
            Wk_root = [proot2k(P, k) for P in Wk]
            tests3 += 1
            d1, d2 = f2_dim(cur, L), f2_dim(Wk_root, L)
            dj = f2_dim(cur + Wk_root, L)
            if not (d1 == d2 == dj):
                bad3 += 1
    print(f"hasse seed={seed} count={count}: (H1) Hasse identity failures {bad1}; "
          f"(H2) filtration-equivalence failures {bad2} (s'=0 cases: {nzero}); "
          f"(HF-ii) descendant=W_k^(1/2^k) failures {bad3}/{tests3}")

def rand_F2_subspace_FQ(mhalf, dim, rng):
    while True:
        B = [rand_sub(mhalf, rng) for _ in range(dim)]
        if f2_rank(B) == dim:
            return B

def trace_FQ(u, mhalf):
    t = 0
    for _ in range(mhalf):
        t ^= u
        u = gmul(u, u)
    return t  # in F_2 = {0,1}

def gen_family(rng, m, mhalf, rho, umax):
    U = rand_F2_subspace_FQ(mhalf, rho, rng)
    typ = rng.randrange(9)
    def lin(deg):
        cs = [rand_sub(m, rng) for _ in range(deg + 1)]
        return lambda u: _lin(cs, u)
    def lowrank(r, into_FQ):
        th = [rand_sub(mhalf, rng) for _ in range(r)]
        ds = [(rand_sub(mhalf, rng) if into_FQ else rand_sub(m, rng)) for _ in range(r)]
        return lambda u: _lowrank(th, ds, u, mhalf)
    terms = []  # (exponent, map)
    if typ == 0:   # twisted constant part + low-rank X-terms (RR-friendly)
        terms.append((0, lin(rng.randrange(1, 3))))
        for _ in range(rng.randrange(1, 4)):
            e = rng.choice([1, 2, 3, 4, 6, 8, 12])
            terms.append((e, lowrank(rng.randrange(1, 3), rng.random() < 0.5)))
    elif typ == 1:  # A(U) with polynomial coefficients in F_q[X^{2^j}]
        j = rng.randrange(0, 4)
        terms.append((0, lin(1)))
        terms.append((1 << j, lin(rng.randrange(0, 2))))
    elif typ == 2:  # eta * U0 * twist (defect-0 type)
        e = rng.choice([0, 1, 2, 4, 8])
        terms.append((e, lin(0)))
    elif typ == 3:  # stalling constant family u^2 + beta u plus level-structured low-rank terms
        terms.append((0, lin(1)))
        terms.append((rng.choice([1, 3, 5]), lowrank(2, True)))
        terms.append((rng.choice([2, 6, 10]), lowrank(2, True)))
        terms.append((rng.choice([4, 12]), lowrank(2, True)))
    elif typ == 4:  # generic-ish linearized degree 2 with X-coefficients
        for e in rng.sample([0, 1, 2, 3, 4, 8], 3):
            terms.append((e, lin(rng.randrange(0, 3))))
    elif typ == 5:  # partial half-field: U1 + X^e * lowrank
        terms.append((0, lin(0)))
        terms.append((rng.choice([1, 2, 4]), lowrank(rng.randrange(1, 4), True)))
    else:  # types 6-8: defect-1 constant part (u^2+beta u) on rho-2t dims, plus t lossy levels of 2 random polys
        t = typ - 5
        if rho - 2 * t < 2:
            t = 1
        A = lin(1)
        U1 = U[:rho - 2 * t]
        basis = [ptrim([A(u)]) for u in U1]
        for lev in range(t):
            for _ in range(2):
                s = [rand_sub(m, rng) for _ in range((umax >> lev) + 1)]
                if len(s) > 1 and s[1] == 0:
                    s[1] = 1  # ensure s' != 0 generically
                basis.append(ptrim(pfrob(ptrim(s), lev)[:umax + 1]))
        return typ, basis
    basis = []
    for u in U:
        P = [0] * (umax + 1)
        for (e, f) in terms:
            P[e] ^= f(u)
        basis.append(ptrim(P))
    return typ, basis

def _lin(cs, u):
    r = 0
    v = u
    for c in cs:
        r ^= gmul(c, v)
        v = gmul(v, v)
    return r

def _lowrank(th, ds, u, mhalf):
    r = 0
    for t, d in zip(th, ds):
        if trace_FQ(gmul(t, u), mhalf):
            r ^= d
    return r

def check_cd(seed, count):
    rng = random.Random(seed)
    m, mhalf = 24, 12
    umax = 16
    L = umax + 1
    stats = dict(fam=0, P1=0, P1bad=0, P2=0, P2bad=0, P3=0, P3bad=0, rrfail=0, hassebad=0)
    bytype = {}
    for _ in range(count):
        rho = rng.choice([6, 7, 8, 9, 10])
        typ, basis = gen_family(rng, m, mhalf, rho, umax)
        if f2_dim(basis, L) != rho:
            continue
        stats['fam'] += 1
        pts = [(rng.randrange(1, 1 << MBIG), rng.randrange(1, 1 << MBIG)) for _ in range(3)]
        levels = []
        k = 0
        while True:
            Wk = subspace_filter(basis, k, L)
            dk = len(Wk)
            ak = bivariate_defect(Wk, mhalf, pts) if dk else None
            levels.append((k, dk, ak, Wk))
            if (1 << k) > umax:
                break
            k += 1
        # Hasse-rank cross-check and RR
        allRR = True
        for (k, dk, ak, Wk) in levels[:-1]:
            imgs = [tobits(hasse(P, 1 << k), L) for P in Wk]
            rk = f2_rank(imgs)
            if rk != dk - levels[k + 1][1]:
                stats['hassebad'] += 1
            if rk > 2:
                allRR = False
        if not allRR:
            stats['rrfail'] += 1
        for i in range(len(levels) - 1):
            k, dk, ak, _ = levels[i]
            _, dk1, ak1, _ = levels[i + 1]
            if dk1 and ak is not None:
                stats['P1'] += 1
                if ak1 > ak:
                    stats['P1bad'] += 1
                if dk1 < dk and dk1 >= 2 * ak + 2:
                    stats['P2'] += 1
                    if not ak1 <= ak - 1:
                        stats['P2bad'] += 1
        a0 = levels[0][2]
        const = levels[-1][1]
        # direct constants count
        const_direct = len([1]) and f2_dim([P for P in subspace_filter(basis, 5, L)], L)
        assert const == const_direct
        hyp = allRR and a0 <= rho / 2 - 2
        if hyp:
            stats['P3'] += 1
            if const < rho - 2 * a0:
                stats['P3bad'] += 1
        bt = bytype.setdefault(typ, [0, 0, 0, 0, {}])
        bt[0] += 1
        bt[1] += allRR
        bt[2] += hyp
        nloss = sum(1 for i in range(len(levels) - 1) if levels[i + 1][1] < levels[i][1])
        if hyp and const < rho:
            bt[3] += 1
            stats['slack'] = min(stats.get('slack', 99), const - (rho - 2 * a0))
        if allRR:
            key = (rho, a0, nloss, const)
            bt[4][key] = bt[4].get(key, 0) + 1
    print(f"cd seed={seed} count={count}: families {stats['fam']}; "
          f"RR_k failed somewhere in {stats['rrfail']}; Hasse-rank cross-check failures {stats['hassebad']}")
    print(f"  (P1) monotone defect: {stats['P1']} level pairs, {stats['P1bad']} failures")
    print(f"  (P2) lossy & dim W_(k+1) >= 2a(k)+2 => defect drop: {stats['P2']} instances, {stats['P2bad']} failures")
    print(f"  (P3) CD conclusion under its hypotheses: {stats['P3']} families, {stats['P3bad']} failures")
    print(f"  min slack const-(rho'-2a0) over nontrivial CD-hypothesis families: {stats.get('slack')}")
    for t, bt in sorted(bytype.items()):
        print(f"  type {t}: n={bt[0]} all-RR={bt[1]} CD-hyp={bt[2]} CD-hyp&nonconstant={bt[3]}; all-RR (rho,a0,#lossy,const): {dict(sorted(bt[4].items()))}")

# ---------------- Prop 216.3 frame dependence ----------------
def check_p216(seed, count):
    rng = random.Random(seed)
    for m in (6, 8):
        h = subfield_gen(m)
        F = [0] + [gpow(h, r) for r in range(1, 1 << m)]
        for kdim in (2, 3, 4):
            # A0: random F2-subspace of F_q of dim kdim
            while True:
                B = [F[rng.randrange(1, 1 << m)] for _ in range(kdim)]
                if f2_rank(B) == kdim:
                    break
            A0 = [0]
            for b in B:
                A0 = A0 + [a ^ b for a in A0]
            n = len(A0)
            R = [(a, gmul(a, a)) for a in A0]   # parabola points over a subspace
            for frame in ("orig", "focus-vertical"):
                if frame == "orig":
                    Rf = R
                else:
                    f = A0[1]   # a focus slope (secant slope a+a' lies in A0\0)
                    Rf = [(y ^ gmul(f, x), x) for (x, y) in R]   # T(1,f) = (0,1)
                slopes = set()
                vertical = False
                for i in range(n):
                    for j in range(i + 1, n):
                        dx = Rf[i][0] ^ Rf[j][0]
                        dy = Rf[i][1] ^ Rf[j][1]
                        if dx == 0:
                            vertical = True
                        else:
                            slopes.add(gmul(dy, ginv(dx)))
                nfoc = len(slopes) + (1 if vertical else 0)
                # hyperfocused: n-1 slopes, each a perfect matching
                hyper = (nfoc == n - 1)
                nonfoci = [mu for mu in F if mu not in slopes]
                cnt = {}
                for mu in nonfoci:
                    U = set(y ^ gmul(mu, x) for (x, y) in Rf)
                    assert len(U) == n
                    for b in F[1:]:
                        if all((t ^ b) in U for t in U):
                            cnt[b] = cnt.get(b, 0) + 1
                mx = max(cnt.values()) if cnt else 0
                print(f"p216 m={m} n={n} frame={frame}: hyperfocused={hyper} inf_is_focus={vertical} "
                      f"finite nonfoci={len(nonfoci)} max#radicals containing one b={mx} vs n-1={n-1} "
                      f"-> {'OK' if mx <= n-1 else 'EXCEEDS n-1'}")

def check_arith():
    bad = 0
    cells = 0
    for rho in range(4, 61, 2):
        for g in range(rho + 3, 2 * rho + 1):
            cells += 1
            m = 2 * g + rho
            a_star = rho - (g + 1) // 2
            j = m - 1 - g
            d = 1 << j
            q = 1 << m
            n = q // 2 - d
            v_lb = q // 2 + 1
            ok = (a_star <= rho // 2 - 2) and (2 * a_star + 4 == 2 * rho - 2 * ((g + 1) // 2) + 4) \
                and (2 * a_star + 4 <= rho) and (v_lb > n - 1) and (rho - 1 - (g - 1) // 2 == a_star)
            # RB numerical range: 2u(2^{a+1}-1)Q < v with u=R/4, R=2^g, Q=2^{g+rho/2}
            R = 1 << g
            Q = 1 << (g + rho // 2)
            ok = ok and (2 * (R // 4) * ((1 << (a_star + 1)) - 1) * Q < q // 2)
            if not ok:
                bad += 1
    print(f"arith: {cells} even cells (rho 4..60, rho+3<=g<=2rho): failures {bad}")
    print("arith: endpoints  g=2rho-2 -> 2a*+4 =", [2 * (r - (2 * r - 2 + 1) // 2) + 4 for r in (8, 10, 12)],
          "; g=rho+3 -> ", [(2 * (r - (r + 3 + 1) // 2) + 4, r) for r in (8, 10, 12)],
          "; g=rho+4 -> ", [(2 * (r - (r + 4 + 1) // 2) + 4, r) for r in (8, 10, 12)])
    # WG threshold: sqrt q <= 3u(e+1), u = R/4, sqrt q = R 2^{rho/2}  =>  e >= (4/3)2^{rho/2} - 1
    from fractions import Fraction as Fr
    okw = all(Fr(4, 3) * 2 ** (r // 2) - 1 == Fr(4 * 2 ** (r // 2), 3) - 1 for r in range(4, 40, 2))
    print("arith: WG threshold algebra consistent:", okw)

def main():
    try:
        import galois
        assert galois.Poly.Int(MOD, field=galois.GF(2)).is_primitive()
    except ImportError:
        pass
    cmd = sys.argv[1]
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    count = int(sys.argv[3]) if len(sys.argv) > 3 else 100
    if cmd == 'hasse':
        check_hasse(seed, count)
    elif cmd == 'cd':
        check_cd(seed, count)
    elif cmd == 'p216':
        check_p216(seed, count)
    elif cmd == 'arith':
        check_arith()

if __name__ == '__main__':
    main()
