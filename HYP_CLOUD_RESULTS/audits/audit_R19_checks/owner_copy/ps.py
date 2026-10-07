# truncated power series over GF(2^m) using galois; minimal helpers
import galois, numpy as np
GF = galois.GF(2**19)
class PS:
    def __init__(s, c, N): 
        c = list(c)[:N]; c += [GF(0)]*(N-len(c)); s.c = GF(c); s.N = N
    def __add__(a, b):
        b = b if isinstance(b, PS) else PS([GF(b)], a.N); return PS(a.c+b.c, a.N)
    __radd__ = __add__
    def __mul__(a, b):
        if not isinstance(b, PS): return PS(a.c*GF(b), a.N)
        N=a.N; out = GF.Zeros(N)
        nz = [i for i in range(N) if a.c[i]!=0]
        for i in nz: out[i:] += a.c[i]*b.c[:N-i]
        return PS(out, N)
    __rmul__ = __mul__
    def inv(a):
        N=a.N; a0=a.c[0]; assert a0!=0
        out=GF.Zeros(N); out[0]=GF(1)/a0
        for k in range(1,N):
            acc=GF(0)
            for i in range(1,k+1): acc += a.c[i]*out[k-i]
            out[k] = acc/a0  # char 2: minus = plus
        return PS(out,N)
    def __pow__(a, e):
        r = PS([GF(1)], a.N); b=a
        while e:
            if e&1: r=r*b
            b=b*b; e>>=1
        return r
    def ord(a):
        for i in range(a.N):
            if a.c[i]!=0: return i
        return a.N
def dot(a,b):
    s=a[0]*b[0]
    for i in (1,2): s = s + a[i]*b[i]
    return s
def cross(a,b):
    return [a[1]*b[2]+a[2]*b[1], a[2]*b[0]+a[0]*b[2], a[0]*b[1]+a[1]*b[0]]
