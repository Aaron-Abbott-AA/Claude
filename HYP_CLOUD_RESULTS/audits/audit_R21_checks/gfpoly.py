# Referee helper (R21 audit): sparse multivariate polynomials over GF(2^m), exact.
# Coefficients are ints in the galois field GF; monomials are exponent tuples.
import galois

class Ring:
    def __init__(self, GF, nvars):
        self.GF = GF; self.n = nvars
    def const(self, a):
        a = int(a)
        return {} if a == 0 else {(0,)*self.n: a}
    def var(self, i):
        e = [0]*self.n; e[i] = 1
        return {tuple(e): 1}
    def add(self, p, q):
        r = dict(p)
        for m, c in q.items():
            v = int(self.GF(r.get(m, 0)) + self.GF(c))
            if v: r[m] = v
            else: r.pop(m, None)
        return r
    def scal(self, a, p):
        a = self.GF(int(a))
        if int(a) == 0: return {}
        return {m: int(a*self.GF(c)) for m, c in p.items()}
    def mul(self, p, q):
        r = {}
        for m1, c1 in p.items():
            g1 = self.GF(c1)
            for m2, c2 in q.items():
                m = tuple(x+y for x, y in zip(m1, m2))
                v = int(self.GF(r.get(m, 0)) + g1*self.GF(c2))
                if v: r[m] = v
                else: r.pop(m, None)
        return r
    def powr(self, p, k):
        r = self.const(1)
        for _ in range(k): r = self.mul(r, p)
        return r
    def iszero(self, p): return len(p) == 0
    def reduce_monic(self, p, var, deg, repl):
        """reduce p modulo F = var^deg + repl (repl free of var^deg terms), char 2: var^deg -> repl"""
        p = dict(p)
        while True:
            bad = [m for m in p if m[var] >= deg]
            if not bad: return p
            m = max(bad); c = p.pop(m)
            e = list(m); e[var] -= deg
            p = self.add(p, self.mul({tuple(e): c}, repl))

def mat_mul(R, A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[{} for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            acc = {}
            for t in range(k): acc = R.add(acc, R.mul(A[i][t], B[t][j]))
            out[i][j] = acc
    return out
