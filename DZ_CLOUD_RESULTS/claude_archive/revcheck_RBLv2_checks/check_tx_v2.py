"""Referee check (RBL v2 revision): FIX-4 exact pointwise defects of TX and
FIX-1 stalling constant family. Own code; run with python3 -I.

Usage: python3 -I check_tx_v2.py m rho n_offfield seed
Defect a(V) := min a with rank_Fq [v^(2^e) | vbar^(2^e)]_{e<=a} < 2a+2
(pair-relation form; equals the real-relation defect by HFD sec.1)."""
import sys, random
import numpy as np
import galois

m, rho, n_off, seed = (int(s) for s in sys.argv[1:5])
random.seed(seed)
q = 2 ** m
Q = 2 ** (m // 2)
GF = galois.GF(2 ** m)
g = GF.primitive_element


def frob(x, k):
    """x^(2^k), k may be negative (mod m)."""
    return x ** (2 ** (k % m))


def bar(x):
    return x ** Q


FQ = [GF(0)] + [g ** (((q - 1) // (Q - 1)) * i) for i in range(Q - 1)]
assert all(bar(x) == x for x in FQ)


def span(basis):
    s = {0}
    for b in basis:
        bi = int(b)
        s |= {x ^ bi for x in s}
    return s


def rand_subspace(pool, r):
    while True:
        B = random.sample(pool, r)
        if len(span(B)) == 2 ** r:
            return B


def defect(V):
    """V: list of field elements (an F2-basis)."""
    for a in range(0, len(V)):
        if 2 * a + 2 > len(V):
            return a  # rank automatically < 2a+2
        M = GF([[int(frob(v, e)) for e in range(a + 1)] +
                [int(frob(bar(v), e)) for e in range(a + 1)] for v in V])
        if np.linalg.matrix_rank(M) < 2 * a + 2:
            return a
    return None


U = rand_subspace(FQ[1:], rho)
Uset = span(U)


def Valpha(al):
    return [u * u + al * u for u in U]


def classify(al):
    V = Valpha(al)
    if len(span(V)) < 2 ** rho:
        return "deg"
    return defect(V)


out = []
# (A) all alpha in F_Q (exhaustive)
cnt = {}
bad = 0
for al in FQ:
    c = classify(al)
    inU = int(al) in Uset
    key = ("U\\0" if (inU and int(al) != 0) else ("0" if int(al) == 0 else "FQ\\U"), c)
    cnt[key] = cnt.get(key, 0) + 1
    # predictions: alpha in U\0 -> degenerate; alpha in FQ\U or 0 -> defect 0
    pred = "deg" if (inU and int(al) != 0) else 0
    if c != pred:
        bad += 1
out.append(f"(A) alpha in F_Q, exhaustive ({len(FQ)}): counts {sorted(cnt.items(), key=str)}; mismatches {bad}")

# (B) alpha not in F_Q
FQset = {int(x) for x in FQ}
if n_off == 0:
    offs = [GF(x) for x in range(q) if x not in FQset]
    tag = "exhaustive"
else:
    offs = []
    while len(offs) < n_off:
        x = random.randrange(q)
        if x not in FQset:
            offs.append(GF(x))
    tag = f"random {n_off}"
cntB = {}
for al in offs:
    c = classify(al)
    cntB[c] = cntB.get(c, 0) + 1
out.append(f"(B) alpha not in F_Q, {tag}: defect counts {cntB}; prediction all = 1")

# (C) TX composition identity Gamma(tau+al) = Delta(tau+albar) on random field elems
fail = 0
for _ in range(50):
    al = GF(random.randrange(q))
    ab = bar(al)
    x = GF(random.randrange(q))
    lhs_in = x * x + al * x
    lhs = lhs_in * lhs_in + ab * (al + ab) * lhs_in
    rhs_in = x * x + ab * x
    rhs = rhs_in * rhs_in + al * (al + ab) * rhs_in
    if lhs != rhs:
        fail += 1
out.append(f"(C) Gamma(tau+al)=Delta(tau+albar) on 50 random (al,x): failures {fail}")

# (D) FIX-1 stalling constant family W={u^2+beta u}, beta notin F_Q
beta = offs[0]
W = [u * u + beta * u for u in U]
rows = []
okform = True
for k in range(0, m + 1):
    Wk = [frob(w, -k) for w in W]  # k-fold square root of constant family
    # W_k should equal {s^2 + beta^(1/2^k) s : s in U^(1/2^k)}
    bk = frob(beta, -k)
    alt = [frob(u, -k) ** 2 + bk * frob(u, -k) for u in U]
    if span(Wk) != span(alt):
        okform = False
    d = defect(Wk) if len(span(Wk)) == 2 ** rho else "deg"
    rows.append(d)
out.append(f"(D) constant family, beta notin F_Q: defect at sqrt-steps k=0..{m}: {rows}; "
           f"form {{s^2+beta^(1/2^k)s}} matches: {okform}; dims all rho: {all(r != 'deg' for r in rows)}")

print(f"m={m} rho={rho} seed={seed} |U|={len(Uset)} |F_Q\\U|={Q-len(Uset)}")
for line in out:
    print(line)
