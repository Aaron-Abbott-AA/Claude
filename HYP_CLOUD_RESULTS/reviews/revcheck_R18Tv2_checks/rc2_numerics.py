# Independent recomputation of Cor 3.5 numerics (rest, theta_max, D-windows, theta_up).
from fractions import Fraction as Fr
def rest(r,Q,S,D,n):
    E=r*Q*S; h=n*E; q=E*h; d=E+2
    N=Fr(16*h,625); a=Fr(8*h,625)
    tot=N*d+Fr(3,2)*d*d+Fr(7,2)*d+1+(D+2)*(E+1)*d+4*a*d+2*(D-1)*(E-2)*d+6*Fr(q,1000)+7
    return tot/q
def thmax(r,Q,S,D,n,qq=128):
    T=Q*S
    return (Fr(1551,4000)-rest(r,Q,S,D,n))*(Q-1)*S/(Q-1+T-D+Fr(2,qq)*Fr(Q-1,Q))
c=rest(4,128,512,4,256)
print("corner rest =",c, float(c), "matches note:", c==Fr(1490227160815097,10995116277760000))
print("corner theta_max =", float(thmax(4,128,512,4,256)))
Qs=[2**v for v in range(7,13)]
cases=0; win={}; minD4={}; minratio=None
for r in [4,8,16,32]:
  for Q in Qs:
    for j in range(3):
      D=1
      while D<Q:
        S=Q**j*D
        if S>=64 and D>=4:
          n=256
          while n<4*Q:
            cases+=1
            t=thmax(r,Q,S,D,n)
            if t>0: win.setdefault(n,set()).add(D)
            if D==4: minD4[n]=min(minD4.get(n,9),float(t))
            E=r*Q*S; h=n*E; d=E+2; N=Fr(16*h,625)
            tup=(N*d/Fr(Q,2)+d)/(r*h)
            if t>0:
              rt=tup/t; minratio=rt if minratio is None else min(minratio,rt)
            n*=2
        D*=2
print("cases",cases)
for n in sorted(win): print("n=%d maxD=%d n/16=%d  D-set=%s"%(n,max(win[n]),n//16,sorted(win[n])))
print("min theta_max D=4 per n:",{k:round(v,4) for k,v in sorted(minD4.items())})
print("min theta_up/theta_max:",float(minratio))
print("theta_up(S=64) approx 0.0512*64 =",0.0512*64)
# N6 check
print("2m/Q bound at h=256E,Q=128: 16*256/(625*128)=",16*256/(625*128),"; as h->4QE: 64/625=",64/625)
