# Referee R20: where do the Example 2.4 clusters live?
# (1) sympy over GF(2): with c=(s,1), s^2=y^7 (affine U0=1, U1=x, U2=y), compute
#     Xi(u) = det(M(u)^[8] c, M(u) c) and reduce modulo s^2-y^7 and the curve y^7=1+x^7.
# (2) GF(2^21) check: x a primitive 49th root of unity (x^7 != 1), y^7 = 1+x^7 != 0: all six residual
#     Xi vanish, and g(u)=U0U1U2 != 0 (u is off the contracted lines of sigma1).
# Run: python3 -I ref_fermat_mu49.py
import sympy as sp
x, y, s = sp.symbols('x y s')
M = sp.Matrix([[1, x**7], [y**7, 1 + x**7]])
M8 = M.applyfunc(lambda e: sp.expand(e**8))
c = sp.Matrix([s, 1])
p, q = M8*c, M*c
Xi = sp.expand(p[0]*q[1] + p[1]*q[0])
P = sp.Poly(Xi, s, x, y, modulus=2)
# reduce s^2 -> y^7, then y^7 -> 1 + x^7 (repeatedly)
def red(expr):
    _, r = sp.reduced(expr, [s**2 + y**7, y**7 + 1 + x**7], s, y, x, order='lex', modulus=2)
    return sp.Poly(r, s, y, x, modulus=2)
R = red(Xi)
print('Xi reduced on the curve (mod 2):', sp.factor(R.as_expr(), modulus=2))

import galois
GF = galois.GF(2**21)
g = GF.primitive_element
w = g**((2**21 - 1)//49)            # primitive 49th root of unity
assert w**49 == 1 and w**7 != 1
F8 = [z for z in [GF(0)] + [g**(k*(2**21-1)//7) for k in range(7)] if z != 0 and z != 1 and z**8 == z]
# note: F_8 subset GF(2^21) since 3 | 21
assert len(F8) == 6, len(F8)
def sqrt(t): return t**(2**20)
def Mf(u):
    a_, b_, c_ = u[0]**7, u[1]**7, u[2]**7
    return ((a_, b_), (c_, a_ + b_))
def mv(A, v): return (A[0][0]*v[0] + A[0][1]*v[1], A[1][0]*v[0] + A[1][1]*v[1])
def det(p_, q_): return p_[0]*q_[1] + p_[1]*q_[0]
found = 0; checked = 0
for k in [1, 2, 3, 5, 8]:
    xx = w**k
    if xx**7 == 1: continue
    rhs = GF(1) + xx**7
    # y with y^7 = rhs: y = rhs^(1/7) exists iff rhs is a 7th power; 7 | 2^21-1, try via exponent
    # search a 7th root by exponent arithmetic on the discrete log
    L = int(rhs.log()) if hasattr(rhs, 'log') else None
    if L is None or L % 7: continue
    yy = g**(L//7)
    assert yy**7 == rhs
    u = (GF(1), xx, yy); checked += 1
    c_ = (sqrt(u[2]**7), sqrt(u[0]**7))
    ue = tuple(t**8 for t in u)
    vals = []
    for z in F8:
        v = (ue[0], z*ue[1], z/(GF(1)+z)*ue[2])
        assert v[0]**7 + v[1]**7 + v[2]**7 == 0
        vals.append(det(mv(Mf(v), c_), mv(Mf(u), c_)))
    allzero = all(t == 0 for t in vals)
    found += allzero
    print(f'  x=w^{k}: g(u)=U0U1U2 != 0: {u[0]*u[1]*u[2] != 0}; all six Xi(u,v_zeta)=0: {allzero}')
print(f'checked {checked} points with x in mu_49 \\ mu_7 over GF(2^21); full clusters at {found}')
