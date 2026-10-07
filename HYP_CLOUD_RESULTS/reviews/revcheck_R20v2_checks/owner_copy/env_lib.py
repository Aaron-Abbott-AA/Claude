# helpers for NOTE_ENVELOPE_RIGIDITY: Hasse derivatives, vectors of power series, branches
import random
from ps import *
MOD = 2**19 - 1

def hasse(p, k):                      # D_s^{(k)} on a truncated series (s = x - x(u))
    N = p.N; c = [GF(0)]*N
    for j in range(k, N):
        if (j & k) == k: c[j-k] = p.c[j]   # Lucas: C(j,k) odd
    return PS(c, N)
def vh(v, k): return [hasse(a, k) for a in v]
def vadd(a, b): return [a[i]+b[i] for i in range(3)]
def vsc(c, a): return [a[i]*c for i in range(3)]
def frob(v, r): return [vi**r for vi in v]
def cst(v, N): return [PS([GF(x)], N) for x in v]
def at0(v): return [GF(x.c[0]) for x in v]
def word(a, b): return min(c.ord() for c in cross(a, b))      # order of a x b
def matvec(A, v): return [sum((v[j]*A[i][j] for j in range(1, 3)), v[0]*A[i][0]) for i in range(3)]
def mT(A): return [[A[j][i] for j in range(3)] for i in range(3)]
def adj3(A):  # adjugate of 3x3 matrix with PS or GF entries (char 2: no signs)
    c = lambda i, j: A[(i+1)%3][(j+1)%3]*A[(i+2)%3][(j+2)%3] + A[(i+1)%3][(j+2)%3]*A[(i+2)%3][(j+1)%3]
    return [[c(j, i) for j in range(3)] for i in range(3)]
def det3(a, b, c): return dot(a, cross(b, c))
def ratio(a, b): return a*b.inv()

# ---- sigma1 data: e = (U1U2, U0U2, U0U1) = (L0 U) x (N0 U)
L0 = [[1,0,0],[0,1,0],[0,0,0]]; N0 = [[0,0,0],[0,1,0],[0,0,1]]
def sig1(V): return [V[1]*V[2], V[0]*V[2], V[0]*V[1]]

def fermat_branch(n, N, rng):
    """branch of U0^n+U1^n+U2^n=0 at a random point, Y=[1,x,y2], x=x0+s."""
    x = PS([GF(rng.randrange(1, 2**19)), GF(1)], N); rhs = 1 + x**n
    y2 = PS([rhs.c[0]**pow(n, -1, MOD)], N)
    for _ in range(10):
        y2 = y2 + (y2**n + rhs)*(y2**(n-1)).inv()
    assert (y2**n + rhs).ord() >= N
    return [PS([GF(1)], N), x, y2]

class Model:
    """e(U)=sigma1(B U); ell=L U, m=N U with L=L0 B, N=N0 B; Gamma: U^[E].e(U)=0."""
    def __init__(s, E, B):
        s.E = E; s.B = [[GF(b) for b in row] for row in B]
        s.L = [[sum((GF(L0[i][k])*s.B[k][j] for k in range(3)), GF(0)) for j in range(3)] for i in range(3)]
        s.N = [[sum((GF(N0[i][k])*s.B[k][j] for k in range(3)), GF(0)) for j in range(3)] for i in range(3)]
    def e(s, Y): return sig1(matvec(s.B, Y))

def model_branch(M, N, rng, tries=40):
    """branch of Gamma_M at a random point with U0=1, x=U1 local parameter."""
    E = M.E; P = galois.Poly
    for _ in range(tries):
        x0 = GF(rng.randrange(1, 2**19))
        Ypol = [P([1], field=GF), P([x0], field=GF), P([1, 0], field=GF)]
        V = [sum((Ypol[j]*M.B[i][j] for j in range(1, 3)), Ypol[0]*M.B[i][0]) for i in range(3)]
        e = sig1(V)
        G = e[0] + e[1]*(x0**E) + e[2]*(Ypol[2]**E)
        rts = G.roots()
        for y0 in rts:
            Y = [PS([GF(1)], N), PS([x0, GF(1)], N), PS([y0], N)]
            for _ in range(12):
                V = matvec(M.B, Y); ee = sig1(V)
                Gv = dot(frob(Y, E), ee)
                w = [M.B[i][2] for i in range(3)]
                Je = [V[1]*w[2] + V[2]*w[1], V[0]*w[2] + V[2]*w[0], V[0]*w[1] + V[1]*w[0]]
                Gy = dot(frob(Y, E), Je)
                if Gy.c[0] == 0: break
                Y[2] = Y[2] + Gv*Gy.inv()
            Gv = dot(frob(Y, E), sig1(matvec(M.B, Y)))
            if Gv.ord() >= N: return Y
    raise RuntimeError("no smooth unramified point found")
