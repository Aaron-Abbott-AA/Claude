# R20 toy checks on the Fermat sigma1 model (E=8): Gamma: U0^7+U1^7+U2^7=0, e=sigma1, d'=14.
# (1) contact of the own line l_u=u^[E] with Gamma' at z(u)=e(u) is exactly E.
# (2) Lemma 3.5' mechanism: a form A of degree a with A(z(y)) = O(s^N) along Gamma at u
#     restricts to l_u with a zero of order >= min(N,E) at z(u); for N>E generically exactly E (cap is sharp).
# (3) sharpness of the method bound a-m: impose in addition A(z(v_i))=0 at k residual points
#     v_i = diag(1,zeta,zeta/(1+zeta)) u^[E]; for k<=a-E there are A with A|l_u != 0, for k>a-E
#     every solution has A|l_u == 0 (the B-alternative of Lemma 3.5').
# Run: python3 -I toy_line_order.py
import random, itertools
import numpy as np
import galois
GF = galois.GF(2**12)
E = 8; L = 40
rng = random.Random(20261007)

def smul(a, b): return np.convolve(a, b)[:L]
def sinv(a):
    out = GF.Zeros(L); out[0] = a[0]**-1
    # Newton-free recursive inverse
    for k in range(1, L):
        acc = GF(0)
        for j in range(1, k+1): acc += a[j]*out[k-j]
        out[k] = -acc*out[0]
    return out
def spow(a, e):
    r = GF.Zeros(L); r[0] = 1
    for _ in range(e): r = smul(r, a)
    return r
def order(a):
    nz = np.nonzero(a)[0]
    return int(nz[0]) if len(nz) else L

def fermat_point():
    while True:
        x0 = GF(rng.randrange(2, 2**12))
        w = GF(1) + x0**7
        if w == 0: continue
        rts = galois.Poly([1, 0, 0, 0, 0, 0, 0, w], field=GF).roots()
        if len(rts): return x0, rts[0]

def branch(x0, y0):
    x = GF.Zeros(L); x[0] = x0; x[1] = 1
    rhs = spow(x, 7); rhs[0] += GF(1)                     # y^7 = 1 + x^7
    y = GF.Zeros(L); y[0] = y0
    for _ in range(8):                                 # Newton: y <- y + (y^7+rhs)/(7 y^6) (7=1 in char 2)
        y = y + smul(spow(y, 7) + rhs, sinv(spow(y, 6)))
    assert order(spow(y, 7) + rhs) >= L
    one = GF.Zeros(L); one[0] = 1
    return [one, x, y]

def sigma1(V): return [smul(V[1], V[2]), smul(V[0], V[2]), smul(V[0], V[1])]
def monos(a): return [(i, j, a-i-j) for i in range(a+1) for j in range(a+1-i)]

def run(a, N, k, trials=3):
    res = []
    for _ in range(trials):
        x0, y0 = fermat_point()
        U = branch(x0, y0); z = sigma1(U)
        u = [GF(1), x0, y0]; lu = [c**E for c in u]
        con = sum((lu[i]*z[i] for i in range(3)), GF.Zeros(L))
        cont = order(con)
        zu = [zi[0] for zi in z]
        # residual points v_zeta = D_zeta u^[E]
        F8 = [g for g in GF.elements if g != 0 and g != 1 and g**8 == g]
        resid = []
        for zeta in F8:
            v = [lu[0], zeta*lu[1], zeta/(GF(1)+zeta)*lu[2]]
            ev = [v[1]*v[2], v[0]*v[2], v[0]*v[1]]
            assert sum((lu[i]*ev[i] for i in range(3)), GF(0)) == 0
            resid.append(ev)
        M = monos(a)
        zp = [[spow(z[c], e) for e in range(a+1)] for c in range(3)]
        cols = []
        for (i, j, l) in M:
            ser = smul(smul(zp[0][i], zp[1][j]), zp[2][l])[:N]
            pts = [r[0]**i * r[1]**j * r[2]**l for r in resid[:k]]
            cols.append(list(ser) + pts)
        A = GF(np.array(cols, dtype=int).T if False else np.array([[int(c) for c in col] for col in cols]).T)
        ns = A.null_space()
        # restriction to l_u: P(t)=z(u)+tW, W = l_u x c0 (a point of l_u)
        c0 = [GF(rng.randrange(1, 2**12)) for _ in range(3)]
        W = [lu[1]*c0[2]+lu[2]*c0[1], lu[0]*c0[2]+lu[2]*c0[0], lu[0]*c0[1]+lu[1]*c0[0]]
        P = [galois.Poly([W[c], zu[c]], field=GF) for c in range(3)]
        Pp = [[P[c]**e for e in range(a+1)] for c in range(3)]
        mono_t = [Pp[0][i]*Pp[1][j]*Pp[2][l] for (i, j, l) in M]
        def restrict(coef):
            poly = galois.Poly([0], field=GF)
            for cf, mt in zip(coef, mono_t):
                if cf != 0: poly = poly + mt*cf
            return poly
        # generic element of the solution space
        best = None; allzero = True
        for _ in range(4):
            comb = GF([rng.randrange(0, 2**12) for _ in range(ns.shape[0])])
            coef = comb @ ns
            rp = restrict(coef)
            if rp != 0:
                allzero = False
                cs = rp.coeffs[::-1]
                o = int(np.nonzero(cs)[0][0])
                best = o if best is None else min(best, o)
        res.append((cont, ns.shape[0], allzero, best))
    return res

if __name__ == "__main__":
    print("E=8 Fermat sigma1, GF(2^12), d'=14, residual points per u: 6")
    for (a, N, k) in [(10, 4, 0), (10, 8, 0), (12, 8, 0), (12, 16, 0), (12, 24, 0), (13, 16, 0),
                      (12, 8, 4), (12, 8, 5), (12, 8, 6), (13, 8, 5), (13, 8, 6), (12, 16, 4), (12, 16, 5)]:
        out = run(a, N, k)
        print(f"a={a:<3} N={N:<3} k={k}: (contact, dim sol, A|l_u==0 for all sampled, min order of A|l_u at z(u)) per trial:", out,
              f"| prediction: order>={min(N,E)}, A|l_u==0 iff k>a-min(N,E)={a-min(N,E)}")
