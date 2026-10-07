import sympy as sp, random
random.seed(1)
Y0,Y1,U0,v1,v2=sp.symbols('Y0 Y1 U0 v1 v2'); G=(Y0,Y1,U0,v1,v2)
P=lambda e: sp.Poly(e,*G,modulus=2)
def rf():
    return P(sum(Y0**i*Y1**j for i in range(3) for j in range(3-i) if random.randrange(2)))
CP=[[rf(),rf()],[rf(),rf()]]; CR=[[rf(),rf()],[rf(),rf()]]
s1=P(U0*Y0+Y1); s2=P(U0+Y0)
det2=lambda M: M[0][0]*M[1][1]+M[0][1]*M[1][0]
CA=[[s1*CP[i][j]**2+s2*CR[i][j]**2 for j in range(2)] for i in range(2)]
Dv=det2([[P(v1)*CP[i][j]+P(v2)*CR[i][j] for j in range(2)] for i in range(2)])
e=Dv.as_expr()
D=[P(e.coeff(v1,2).coeff(v2,0)),P(e.coeff(v1,1).coeff(v2,1)),P(e.coeff(v1,0).coeff(v2,2))]
print((det2(CA)-(s1**2*D[0]**2+s1*s2*D[1]**2+s2**2*D[2]**2)).is_zero)
print((D[0]-det2(CP)).is_zero, (D[2]-det2(CR)).is_zero)
x=P(e.coeff(v1,1).coeff(v2,1)); print(x)
print(P(e).as_expr()==e)
print("diff D2:", (D[2]-det2(CR)).as_expr())
print("coeff v1,0:", sp.Poly(e, v1).coeff_monomial(1) if False else None)
pe=sp.Poly(e, v1, v2)
print("via Poly(v1,v2):", [(m, ) for m in pe.monoms()])
D2b=P(pe.coeff_monomial(v2**2)); print((D2b-det2(CR)).is_zero)
