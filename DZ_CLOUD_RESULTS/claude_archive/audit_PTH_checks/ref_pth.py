#!/usr/bin/env python3
"""Referee check for PTH note (independent code; reads no files).
GF(2^m) via log/exp tables with a primitive polynomial searched from the TOP (differs from owner's).
Modes:
  rand    m rho a trials seed : random C (deg a, c0,ca!=0), V random rho-dim in Vt_C = C^{-1}(F_Q)
  partial m rho a trials seed : C = R o lambda^{-1}, R = subspace poly of a-dim K in F_Q (so k=e=a, A_min = lambda);
                                V = (rho-a)-dim part of lambda F_Q + a random vectors of Vt_C
  twist   m rho d trials seed : V = A0(U), A0 random deg d (a0,ad != 0), U random rho-dim in F_Q
  lsonly  m a trials seed     : S_C dims for random C (no V)
  stab    h trials seed       : stabiliser fields of random subspaces of F_{2^h}
For every V with a(V) = a < rho/2 we take the real relation C (deg a, C(V) in F_Q) and check
 LS: dim_F2 S_C >= m/2 ; MI: minimal A injective on F_Q ;
 PTH(i): A(F_Q) in Vt_C, e := dim Vt_C - m/2 in [0,k] ; (ii) dim(V cap A(F_Q)) >= rho - e ;
 (iii) e = 0 => V subset A(F_Q) and deg A = a ; converse: a(V) <= deg A + codim_V(V cap A(F_Q)) ;
 top-coefficient Kummer relation (a_s^{Q-1})^{2^a} = c_a / cbar_a for minimal A of degree s.
Usage: python3 -I ref_pth.py MODE args...
"""
import sys, random

def is_primitive(f, m):
    # check x has order 2^m-1 modulo f (f degree m)
    q1 = (1 << m) - 1
    def mulmod(a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1; a <<= 1
            if a >> m & 1: a ^= f
        return r
    def powx(e):
        r, b = 1, 2
        while e:
            if e & 1: r = mulmod(r, b)
            b = mulmod(b, b); e >>= 1
        return r
    if powx(q1) != 1: return False
    ps = [p for p in range(2, q1 + 1) if q1 % p == 0 and all(p % d for d in range(2, int(p ** .5) + 1))] if q1 < 10 ** 7 else None
    # factor q1 by trial division
    n, ps = q1, []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ps.append(d)
            while n % d == 0: n //= d
        d += 1
    if n > 1: ps.append(n)
    return all(powx(q1 // p) != 1 for p in ps)

class GF:
    def __init__(s, m):
        s.m, s.q = m, 1 << m
        for low in range((1 << m) - 1, 0, -2):  # search from the top
            f = (1 << m) | low
            if is_primitive(f, m): break
        s.f = f
        s.exp = [0] * (2 * s.q); s.log = [0] * s.q
        x = 1
        for i in range(s.q - 1):
            s.exp[i] = x; s.log[x] = i
            x <<= 1
            if x >> m & 1: x ^= f
        for i in range(s.q - 1, 2 * s.q): s.exp[i] = s.exp[i - (s.q - 1)]
    def mul(s, a, b):
        if a == 0 or b == 0: return 0
        return s.exp[s.log[a] + s.log[b]]
    def inv(s, a): return s.exp[(s.q - 1 - s.log[a]) % (s.q - 1)]
    def pw(s, a, e):
        if a == 0: return 0 if e else 1
        return s.exp[(s.log[a] * e) % (s.q - 1)]

# ---------- F2 linear algebra on int bitvectors ----------
class F2Space:
    def __init__(s): s.piv = {}  # leading bit -> vector
    def reduce(s, v):
        while v:
            h = v.bit_length() - 1
            if h in s.piv: v ^= s.piv[h]
            else: return v
        return 0
    def add(s, v):
        v = s.reduce(v)
        if v: s.piv[v.bit_length() - 1] = v; return True
        return False
    def dim(s): return len(s.piv)
    def basis(s): return list(s.piv.values())

def span_dim(vecs):
    S = F2Space()
    for v in vecs: S.add(v)
    return S.dim()

def f2_kernel(images):
    """images[j] = image (int) of j-th basis vector; returns kernel basis as int masks over j."""
    piv = {}  # lead bit -> (vec, combo)
    ker = []
    for j, v in enumerate(images):
        c = 1 << j
        while v:
            h = v.bit_length() - 1
            if h in piv:
                v ^= piv[h][0]; c ^= piv[h][1]
            else:
                break
        if v: piv[v.bit_length() - 1] = (v, c)
        else: ker.append(c)
    return ker

def rank_Fq(F, rows):
    M = [list(r) for r in rows]; rk = 0
    ncol = len(M[0]) if M else 0
    for c in range(ncol):
        p = next((i for i in range(rk, len(M)) if M[i][c]), None)
        if p is None: continue
        M[rk], M[p] = M[p], M[rk]
        iv = F.inv(M[rk][c]); M[rk] = [F.mul(iv, x) for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c]:
                t = M[i][c]; M[i] = [x ^ F.mul(t, y) for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk

class Ctx:
    def __init__(s, m):
        s.F = F = GF(m); s.m = m; s.h = m // 2; s.Q = 1 << s.h
        s.fr = lambda x, e: F.pw(x, 1 << (e % m)) if x else 0
        s.cj = lambda x: s.fr(x, s.h)
        # F_Q basis: kernel of x -> x + x^Q
        ker = f2_kernel([(1 << i) ^ s.cj(1 << i) for i in range(m)])
        s.FQ = ker  # masks over standard basis = elements themselves
        assert span_dim(s.FQ) == s.h and all(s.cj(x) == x for x in s.FQ)
    def ap(s, C, z):
        r = 0
        for e, c in enumerate(C):
            if c and z: r ^= s.F.mul(c, s.fr(z, e))
        return r
    def comp(s, C, A):
        out = [0] * (len(C) + len(A) - 1)
        for i, c in enumerate(C):
            if c:
                for j, x in enumerate(A):
                    if x: out[i + j] ^= s.F.mul(c, s.fr(x, i))
        return out
    def defect(s, V, rho):
        for j in range(0, rho // 2 + 1):
            rows = [[s.fr(v, e) for e in range(j + 1)] + [s.fr(v, s.h + e) for e in range(j + 1)] for v in V]
            if rank_Fq(s.F, rows) < 2 * j + 2: return j
        return rho // 2
    def real_relation(s, V, a):
        """return real C (deg a) with C(V) in F_Q, via F2-kernel of C -> (C(v)+C(v)^Q)_v over coefficient space."""
        m = s.m
        imgs = []
        for e in range(a + 1):
            for i in range(m):
                c = 1 << i
                vec = 0
                for t, v in enumerate(V):
                    y = s.F.mul(c, s.fr(v, e)); vec |= (y ^ s.cj(y)) << (m * t)
                imgs.append(vec)
        ker = f2_kernel(imgs)
        Sp = F2Space()
        for comb in ker:
            Sp.add(comb)
        # pick element with nonzero top coefficient (degree a)
        for comb in Sp.basis():
            C = [0] * (a + 1)
            for j in range(m * (a + 1)):
                if comb >> j & 1: C[j // m] ^= 1 << (j % m)
            if C[a]: return C, len(ker)
        return None, len(ker)
    def lang(s, C, dmax):
        """F2-basis of {A deg<=dmax : CA in F_Q{tau}} as coefficient lists."""
        m = s.m; imgs = []
        for k in range(dmax + 1):
            for i in range(m):
                A = [0] * (dmax + 1); A[k] = 1 << i
                B = s.comp(C, A); vec = 0
                for t, b in enumerate(B): vec |= (b ^ s.cj(b)) << (m * t)
                imgs.append(vec)
        out = []
        for comb in f2_kernel(imgs):
            A = [0] * (dmax + 1)
            for j in range(m * (dmax + 1)):
                if comb >> j & 1: A[j // m] ^= 1 << (j % m)
            out.append(A)
        return out
    def Vtilde(s, C):
        m = s.m
        imgs = [s.ap(C, 1 << i) for i in range(m)]
        kerC = len(f2_kernel(imgs))
        Vt = f2_kernel([y ^ s.cj(y) for y in imgs])
        return Vt, kerC

def analyse(cx, V, rho, stats, expect_a=None):
    F, m, h = cx.F, cx.m, cx.h
    aV = cx.defect(V, rho)
    stats['aV_hist'][aV] = stats['aV_hist'].get(aV, 0) + 1
    if expect_a is not None and aV != expect_a: stats['aV_ne_expected'] += 1
    if aV >= rho / 2: stats['skip_generic'] += 1; return
    C, nrel = cx.real_relation(V, aV)
    stats['n'] += 1
    if nrel != h: stats['fail_realline'] += 1  # real relations of deg<=a form an F_Q-line: F2-dim h
    if C is None or not C[0]: stats['fail_c0'] += 1; return
    if any(cx.cj(cx.ap(C, v)) != cx.ap(C, v) for v in V): stats['fail_CV'] += 1
    a = aV
    sols = cx.lang(C, a)
    if len(sols) < h: stats['fail_LS'] += 1
    stats['SC_FQdim'][len(sols) / h] = stats['SC_FQdim'].get(len(sols) / h, 0) + 1
    # min degree
    dmin = None
    for d in range(a + 1):
        sd = [A for A in sols if all(x == 0 for x in A[d + 1:])]
        dimd = span_dim([sum(x << (m * i) for i, x in enumerate(A)) for A in sd])
        if dimd > 0: dmin = d; break
    # recompute properly: solutions of degree <= d via lang(C, d)
    for d in range(a + 1):
        sd = cx.lang(C, d)
        if sd: dmin = d; break
    stats['dmin_hist'][dmin] = stats['dmin_hist'].get(dmin, 0) + 1
    stats['mindeg_FQdim'][len(sd) / h] = stats['mindeg_FQdim'].get(len(sd) / h, 0) + 1
    A = next(A for A in sd if A[dmin])
    imgA = [cx.ap(A, x) for x in cx.FQ]
    if span_dim(imgA) != h: stats['fail_MI'] += 1
    Vt, k = cx.Vtilde(C)
    if k > a: stats['fail_k'] += 1
    stats['k_hist'][k] = stats['k_hist'].get(k, 0) + 1
    e = len(Vt) - h
    stats['e_hist'][e] = stats['e_hist'].get(e, 0) + 1
    if not (0 <= e <= k): stats['fail_e'] += 1
    VtS = F2Space()
    for z in Vt: VtS.add(z)
    if any(VtS.reduce(z) for z in imgA): stats['fail_i'] += 1
    inter = rho + h - span_dim(list(V) + imgA)
    if inter < rho - e: stats['fail_ii'] += 1
    if inter == rho - e and e > 0: stats['ii_sharp_e_pos'] += 1
    if e == 0:
        if inter != rho: stats['fail_iii_V'] += 1
        if dmin != a: stats['fail_iii_deg'] += 1
    if dmin < aV: stats['degA_lt_aV'] += 1
    if aV > dmin + (rho - inter): stats['fail_converse'] += 1
    # top coefficient Kummer relation
    s = dmin; lhs = F.pw(F.pw(A[s], cx.Q - 1), 1 << a); rhs = F.mul(C[a], F.inv(cx.cj(C[a])))
    if lhs != rhs: stats['fail_top'] += 1
    # bottom: a0^{Q-1} = c0/cbar0
    if A[0] == 0 or F.pw(A[0], cx.Q - 1) != F.mul(C[0], F.inv(cx.cj(C[0]))): stats['fail_bottom'] += 1

def rand_subspace(pool, dim, rng, maxtries=10000):
    S = F2Space(); out = []
    for _ in range(maxtries):
        z = 0
        for b in pool:
            if rng.random() < 0.5: z ^= b
        if z and S.add(z): out.append(z)
        if len(out) == dim: return out
    return None

def newstats():
    keys = ['n', 'skip_generic', 'aV_ne_expected', 'fail_realline', 'fail_c0', 'fail_CV', 'fail_LS', 'fail_MI', 'fail_k', 'fail_e', 'fail_i',
            'fail_ii', 'ii_sharp_e_pos', 'fail_iii_V', 'fail_iii_deg', 'degA_lt_aV', 'fail_converse', 'fail_top', 'fail_bottom']
    st = {k: 0 for k in keys}
    for k in ['aV_hist', 'SC_FQdim', 'dmin_hist', 'mindeg_FQdim', 'k_hist', 'e_hist']: st[k] = {}
    return st

def main():
    mode = sys.argv[1]
    if mode == 'stab':
        hh, trials, seed = map(int, sys.argv[2:5]); rng = random.Random(seed); F = GF(hh)
        bad = 0; tdist = {}
        allel = [1 << i for i in range(hh)]
        for _ in range(trials):
            dim = rng.randrange(1, hh + 1)
            if rng.random() < 0.4:
                # adversarial: subspace of lam * F_{2^t} (possibly all of it)
                divs = [t for t in range(1, hh + 1) if hh % t == 0]
                t0 = rng.choice(divs)
                sub = [x for x in range(1, F.q) if F.pw(x, 1 << t0) == x]
                lam = rng.randrange(1, F.q)
                Sp = F2Space(); [Sp.add(F.mul(lam, x)) for x in sub]
                full = Sp.basis()
                U = full if rng.random() < 0.5 else rand_subspace(full, rng.randrange(1, t0 + 1), rng)
            else:
                U = rand_subspace(allel, dim, rng)
            S = F2Space(); [S.add(u) for u in U]; d = S.dim()
            elems = [x for x in range(1, F.q) if all(S.reduce(F.mul(x, u)) == 0 for u in U)]
            st = elems + [0]
            # field check: closed under + and *, size 2^t
            n = len(st); t = n.bit_length() - 1
            sset = set(st)
            ok = (n == 1 << t) and hh % t == 0 and d % t == 0
            ok = ok and all((x ^ y) in sset and F.mul(x, y) in sset for x in st for y in st)
            if t > d / 2 and t != d: ok = False  # t | d and t > d/2 forces d = t (U = lam F_{2^t})
            if not ok: bad += 1
            tdist[(d, t)] = tdist.get((d, t), 0) + 1
        print(f"cmd: python3 -I ref_pth.py stab {hh} {trials} {seed} | bad={bad} (dim,t) hist={dict(sorted(tdist.items()))}")
        return
    if mode == 'lsonly':
        m, a, trials, seed = map(int, sys.argv[2:6]); rng = random.Random(seed); cx = Ctx(m); h = cx.h
        hist = {}; mhist = {}; dmh = {}; bad = 0
        for _ in range(trials):
            C = [rng.randrange(1, cx.F.q)] + [rng.randrange(cx.F.q) for _ in range(a - 1)] + [rng.randrange(1, cx.F.q)]
            sols = cx.lang(C, a)
            if len(sols) < h: bad += 1
            hist[len(sols) / h] = hist.get(len(sols) / h, 0) + 1
            for d in range(a + 1):
                sd = cx.lang(C, d)
                if sd: break
            dmh[d] = dmh.get(d, 0) + 1; mhist[len(sd) / h] = mhist.get(len(sd) / h, 0) + 1
        print(f"cmd: python3 -I ref_pth.py lsonly {m} {a} {trials} {seed} | field poly {bin(cx.F.f)} | LS fails={bad} | dim_FQ S_C hist={hist} | min deg hist={dmh} | dim_FQ min-deg space hist={mhist}")
        return
    m, rho, a, trials, seed = map(int, sys.argv[2:7]); rng = random.Random(seed); cx = Ctx(m); F, h = cx.F, cx.h
    st = newstats()
    for _ in range(trials):
        if mode == 'rand':
            C = [rng.randrange(1, F.q)] + [rng.randrange(F.q) for _ in range(a - 1)] + [rng.randrange(1, F.q)]
            Vt, k = cx.Vtilde(C)
            V = rand_subspace(Vt, rho, rng)
            if V is None: continue
            analyse(cx, V, rho, st, expect_a=a)
        elif mode == 'partial':
            # R = subspace polynomial of a-dim K in F_Q, times random F_Q unit on the left
            K = rand_subspace(cx.FQ, a, rng)
            R = [1]
            for kk in K:
                # R <- (tau - R(kk)^{1}... ) : S_{K'+<k>} = (tau + S(k)) o S
                sk = cx.ap(R, kk)
                R = cx.comp([sk, 1], R)  # S_{K+<k>} = (tau + S_K(k)) o S_K
            # verify R kills K and has coefficients in F_Q
            assert all(cx.ap(R, kk) == 0 for kk in K), 'R kernel'
            assert all(cx.cj(c) == c for c in R), 'R in F_Q'
            lam = rng.randrange(1, F.q)
            while cx.cj(lam) == lam: lam = rng.randrange(1, F.q)
            li = F.inv(lam)
            C = [F.mul(c, F.pw(li, 1 << e)) for e, c in enumerate(R)]  # C(z) = R(z/lam)
            Vt, k = cx.Vtilde(C)
            part = rand_subspace([F.mul(lam, x) for x in cx.FQ], rho - a, rng)
            S = F2Space(); [S.add(z) for z in part]
            for z in [F.mul(lam, x) for x in cx.FQ]: S.add(z)  # S = lam F_Q
            extra = []
            W = F2Space(); [W.add(z) for z in part]
            tries = 0
            while len(extra) < a and tries < 1000:
                tries += 1
                z = 0
                for b in Vt:
                    if rng.random() < 0.5: z ^= b
                # want z outside lam F_Q + span(extra) and independent of V so far
                T = F2Space(); [T.add(y) for y in S.basis() + extra]
                if z and T.reduce(z) and W.add(z): extra.append(z)
            if len(extra) < a: continue
            V = part + extra
            analyse(cx, V, rho, st, expect_a=a)
        elif mode == 'twist':
            d = a
            A0 = [rng.randrange(1, F.q)] + [rng.randrange(F.q) for _ in range(d - 1)] + ([rng.randrange(1, F.q)] if d >= 1 else [])
            A0 = A0[:d + 1]
            U = rand_subspace(cx.FQ, rho, rng)
            V = [cx.ap(A0, u) for u in U]
            if span_dim(V) < rho: continue
            analyse(cx, V, rho, st, expect_a=None)
    print(f"cmd: python3 -I ref_pth.py {mode} {m} {rho} {a} {trials} {seed} | poly {bin(cx.F.f)} | {st}")

if __name__ == '__main__':
    main()
