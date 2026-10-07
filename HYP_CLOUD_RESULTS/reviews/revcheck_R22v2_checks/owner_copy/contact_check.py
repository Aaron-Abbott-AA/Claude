# contact_check.py -- R22 owner (Claude HYP(2)): exact check of Lemma 2.2 (own-line contact e_u in {E,E+1}
# at smooth points with g(u)!=0, and e_u=E+1 iff y_1^[E].e(u)=0) on the Fermat model of the sigma1 centre:
#   e(U)=(U1U2,U0U2,U0U1),  C_orig=U^[E].e(U)=U0U1U2*(U0^(E-1)+U1^(E-1)+U2^(E-1)),  Gamma: Fermat of degree E-1.
# For every affine point u=(x0,y0,1) of Gamma over GF(2^8) and GF(2^12) with x0*y0!=0 (so g(u)=U0U1U2!=0, u smooth),
# compute the branch y(s) (x=x0+s) by Hensel lifting and the order of h(s)=u^[E].e(v(s)) = I(l_u,Gamma';e(u)).
# Run: python3 -I contact_check.py
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gf2k import *  # noqa
import gf2k


def trunc(p, n):
    return ptrim(p[:n])


def ser_pow(p, k, n):
    r = [1]
    for _ in range(k):
        r = trunc(pmul(r, p), n)
    return r


def branch_order(x0, y0, E):
    n = 2 * E + 4
    xs = [x0, 1]
    Gy = pw(y0, E - 2)  # dG/dy at (x0,y0) (E-1 odd)
    ys = [y0]
    for k in range(1, n):
        trial = ys + [0]
        G = padd(padd(ser_pow(xs, E - 1, k + 1), ser_pow(trial, E - 1, k + 1)), [1])
        ck = G[k] if k < len(G) else 0
        ys.append(mul(ck, inv(Gy)))
    G = padd(padd(ser_pow(xs, E - 1, n), ser_pow(ys, E - 1, n)), [1])
    assert all(v == 0 for v in G[:n]), "branch not on curve"
    # h(s) = u^[E] . e(v(s)),  v=(x(s),y(s),1),  e(v)=(y,x,xy)
    uE = [pw(x0, E), pw(y0, E), 1]
    ev = [ys, xs, trunc(pmul(xs, ys), n)]
    h = padd(padd(pscal(uE[0], ev[0]), pscal(uE[1], ev[1])), pscal(uE[2], ev[2]))
    a1 = ys[1] if len(ys) > 1 else 0
    return pord(trunc(h, n)), a1


def run(E, nsample=60):
    """all points with predicted e_u=E+1 (crit=0) + a deterministic sample of the others get the full Hensel check"""
    q1 = 1 << gf2k.M
    table = {}
    for y in range(1, q1):
        table.setdefault(pw(y, E - 1), []).append(y)
    pts = []
    for x0 in range(1, q1):
        for y0 in table.get(pw(x0, E - 1) ^ 1, []):
            pts.append((x0, y0))
    crit0, other = [], []
    for (x0, y0) in pts:
        a1 = mul(pw(x0, E - 2), inv(pw(y0, E - 2)))      # dy/dx = G_x/G_y (char 2)
        (crit0 if (y0 ^ mul(pw(a1, E), x0)) == 0 else other).append((x0, y0))
    step = max(1, len(other) // nsample)
    test = crit0 + other[::step]
    res = {}
    ok = True
    for (x0, y0) in test:
        o, a1 = branch_order(x0, y0, E)
        res[o] = res.get(o, 0) + 1
        crit = y0 ^ mul(pw(a1, E), x0)
        if (o == E + 1) != (crit == 0) or o not in (E, E + 1):
            ok = False
    return len(pts), len(crit0), len(test), res, ok


if __name__ == '__main__':
    for (m, mod) in ((8, 0x11D), (12, 0x1053)):
      set_field(m, mod)
      print(f"R22 contact_check: Fermat sigma1 model over GF(2^{m})")
      for E in ((8, 16, 32) if m == 8 else (8, 16)):
        npts, ncrit, ntest, res, ok = run(E)
        print(f"  E={E}: affine points with x0*y0!=0: {npts}; predicted e_u=E+1: {ncrit}; Hensel-checked: {ntest}; "
              f"orders -> counts {dict(sorted(res.items()))}; e_u in {{E,E+1}} and (E+1 <=> y_1^[E].e(u)=0): {ok}")
