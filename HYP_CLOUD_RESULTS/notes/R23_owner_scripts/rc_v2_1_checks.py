# rc_v2_1_checks.py -- Claude HYP(2) owner, R23 v2.1 (RC-1, RC-4). Run: python3 -I rc_v2_1_checks.py
# Part RC-1: max of sum(eps)/(N1-eps_top) over p-adic-closed sequences (eps_1=1, dim<=4) with eps_top<N1=2^j,
#   and the R22 Prop 5.5 classical-type corner value charges+2deg psi+6(2g-2)+4tau0 at (4,128,64,256).
# Part RC-4: Cor 5.2 edge case a=E-1, d'=2E-2: B_B + cusps + standing charges, max over the 1260-row grid.
print('=== RC-1 ===')
from fractions import Fraction as F
# order sequences (eps_1=1) closed under binary sub-integers, dim<=4: (0,1),(0,1,2^a),(0,1,2^a,2^b),(0,1,2^a,2^a+1)
def seqs(L=2**14):
    out=[(0,1)]; p=[2**i for i in range(1,15)]
    for a in p:
        out.append((0,1,a)); out.append((0,1,a,a+1))
        for b in p:
            if b>a: out.append((0,1,a,b))
    return out
worst={}
for j in range(1,14):
    N1=2**j
    r=[F(sum(s),N1-s[-1]) for s in seqs() if s[-1]<N1]
    w=[F(1,N1-s[-1]) for s in seqs() if s[-1]<N1]
    worst[N1]=(max(r),max(w))
print({k:(str(v[0]),str(v[1])) for k,v in worst.items()})
# corner value of charges + 2 deg psi + 6(2g-2) + 4 tau0 at (4,128,64,256), qq>=128
r,Q,S,n=4,128,64,256; E=r*Q*S; rho=Q//2; h=n*E; q=n*E*E; d=E+2
N=F(16*h,625); degT=N*d/rho+d; tau=degT/128
b = N*d + 2*degT/128 + F(3*d*d+7*d+2,2) + F(6*q,1000)+7 + 2*(E+1)*d + 6*(d*d-3*d) + 4*tau
print(b/q, float(b/q))
print('=== RC-4 ===')
from fractions import Fraction as F
# edge case a=E-1, d'=2E-2: N_good <= |B| + cusps + Nd + 2deg[T]/qq + E-set + boundary
# |B| <= B_B = 2deg psi + 2(2a-d')d' + max(2g-2,0) ; cusps <= 2d'+2g-2 ; 2g-2<=d^2-3d
worst=None
for r in (4,8,16,32,64):
  for Q in [2**i for i in range(7,15)]:
    for S in [2**i for i in range(6,13)]:
      n=256
      while n<4*Q:
        E=r*Q*S; rho=Q//2; h=n*E; q=n*E*E; d=E+2; a=E-1; dp=2*E-2; g22=d*d-3*d
        N=F(16*h,625); degT=N*d/rho+d
        b=(2*(E+1)*d + 2*(2*a-dp)*dp + g22) + (2*dp+g22) + N*d + 2*degT/128 + F(3*d*d+7*d+2,2) + F(6*q,1000)+7
        v=b/q
        if worst is None or v>worst[0]: worst=(v,(r,Q,S,n))
        n*=2
print(worst[0], float(worst[0]), worst[1])
