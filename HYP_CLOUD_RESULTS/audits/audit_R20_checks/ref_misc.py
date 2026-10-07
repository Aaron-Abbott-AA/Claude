# Referee R20: miscellaneous independent checks.  Run: python3 -I ref_misc.py
#  (a) Prop 3.1 / Cor 3.2: exact a_max/d' at n=256 and n=512; exact-algebra sufficient condition.
#  (b) D1/E at m=E (Thm 5.1 applicability), n=256/512.
#  (c) Prop 5.2 "margin" example r=16,Q=128,n=256,qq=E/16.
#  (d) Lemma 2.1(iii) (projective invariance of E-sparsity) -- explicit counterexample + random tests.
#  (e) Lemma 2.1(i),(ii) and Prop 2.2 random finite-field tests.
#  (f) r=4, n=2Q beyond the grid (Q up to 2^19): does qq=E/8 close? (uses ref_thresholds by path)
import sys, os, random
from fractions import Fraction as Fr
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ref_thresholds as RT
import galois

print('== (a) Prop 3.1/Cor 3.2: a_max(d\')/d\' with a_max=8h/625-d\'+X-rho ==')
worst256 = Fr(0); best512 = None; viol = []
for r in [4, 8, 16, 32, 64]:
    for Q in [2**k for k in range(7, 15)]:
        for S in [2**k for k in range(6, 13)]:
            E = r*Q*S
            for n in [256, 512]:
                h = n*E
                for dp in range(2*E-2, 2*E+5):
                    a = Fr(8*h, 625) - dp + Q*S//2 - Q//2
                    rat = a/dp
                    if n == 256:
                        worst256 = max(worst256, rat)
                        if rat >= 1: viol.append((r, Q, S, dp))
                    else:
                        best512 = rat if best512 is None else min(best512, rat)
print(f'  n=256: max a_max/d\' over r<=64,Q<=2^14,S<=2^12, all 7 d\' = {float(worst256):.6f} (exact {worst256.limit_denominator(10**6)}); violations: {len(viol)}')
print(f'  n=512: min a_max/d\' = {float(best512):.4f}  (>1 means constant-T (K) not excluded by Prop 3.1)')
# exact-algebra: at n=256, a_max<d' for all d'>=2E-2  <=>  2048E/625 + E/(2r) - Q/2 < 4E-4 ; check sup over r>=4 is r=4
r_ok = all(Fr(2048, 625) + Fr(1, 2*r) < 4 for r in [4, 8, 16, 32])
print(f'  coefficient 2048/625+1/(2r) < 4 for r>=4: {r_ok}; at r=4: {float(Fr(2048,625)+Fr(1,8)):.4f}E vs 4E-4 (E>=2^15)')
# also: 2a<d' (R18-T Prop 4.2) at n=256?  (shows Prop 3.1 is genuinely stronger)
E = 4*128*64; h = 256*E
print(f'  for comparison 2a_max/d\' at r=4,Q=128,S=64,n=256,d\'=2E-2: {float(2*(Fr(8*h,625)-(2*E-2)+E//8-64)/(2*E-2)):.4f} (>=1, so R18-T Prop 4.2 does not apply)')

print('\n== (b) D1 = d\'-E-(a-m) at m=E, d\'=2E-2, Q=128, S=64 ==')
for r in [4, 8, 16]:
    for n in [256, 512]:
        E = r*128*64; h = n*E; dp = 2*E-2
        a = Fr(8*h, 625) - dp + E//(2*r) - 64
        print(f'  r={r:<2} n={n}: D1/E = {float((dp - a)/E):.4f}')
# where does D1>0 require m?  m > a-(d'-E)
for r in [4, 8, 16]:
    E = r*128*64; h = 256*E; dp = 2*E-2
    a = Fr(8*h, 625) - dp + E//(2*r) - 64
    print(f'  r={r:<2} n=256: D1>0 needs m > {float((a-(dp-E))/E):.4f}E, i.e. rho*qq > that')

print('\n== (c) Prop 5.2 example: r=16, Q=128, n=256, qq=E/16, (4.1)+N4 margin = bound/q - 1551/4000 ==')
for S in [64, 256]:
    r, Q, n = 16, 128, 256; E = r*Q*S; qq = E//16
    for dp in [2*E-2, 2*E+4]:
        th = RT.tau_hi(r, Q, S, n, dp, qq)
        q = E*n*E
        def margin(t):
            coef = dp - E - t + 1
            return (RT.g41(r, Q, S, n, dp, qq, t, True)/coef)/q
        f = lambda t: RT.g41(r, Q, S, n, dp, qq, t, True)
        iv = RT.nonneg_interval_concave(f, 1, min(th, dp-E))
        print(f'  S={S} d\'={dp-2*E:+d}+2E: tau_hi={th} (<=d\'-E: {th <= dp-E}); margin(1)={float(margin(1)):.5f}, '
              f'margin(tau_hi)={float(margin(th)):.5f}; non-closed tau-interval: {iv}')

print('\n== (d) Lemma 2.1(iii): projective invariance of E-sparsity level ==')
GF = galois.GF(2**10)
def level(coeffs, E):
    """coeffs: list c[i] of t^i (degree<=a). level s = max_k deg xi_k (xi = sum xi_k t^{kE}, deg xi_k<E)."""
    s = -1
    for i, c in enumerate(coeffs):
        if c != 0: s = max(s, i % E)
    return s
def mobius(coeffs, a, lam, mu, gam, dlt):
    """binary form xi(t,w) of degree a -> xi(lam t+mu w, gam t + dlt w); return dehomogenised coeffs."""
    P = galois.Poly
    num = P([lam, mu][::-1] if False else [lam, mu], field=GF)   # lam*t + mu
    den = P([gam, dlt], field=GF)                                # gam*t + dlt
    tot = P([0], field=GF)
    for i, c in enumerate(coeffs):
        if c != 0:
            tot = tot + GF(c) * num**i * den**(a-i)
    cs = list(tot.coeffs[::-1]) + [GF(0)]*(a+1)
    return [int(x) for x in cs[:a+1]]
E = 8; a = 8
xi = [0, 1] + [0]*7                     # xi = t (as a degree-8 binary form: t*w^7), level 1
sw = mobius(xi, a, GF(0), GF(1), GF(1), GF(0))   # t <-> w swap: t -> w/t, i.e. (lam,mu,gam,dlt)=(0,1,1,0)
print(f'  E=8, a=8: xi=t*w^7 has level {level(xi,E)}; after the swap t<->w it is {sw} -> level {level(sw,E)};'
      f' Lemma 2.1(iii) predicts <= {level(xi,E)} + (a mod E) = {level(xi,E) + a % E}')
rng = random.Random(1)
cnt_bad = 0; cnt_aff_bad = 0; trials = 200
for _ in range(trials):
    E = 8; a = rng.choice([8, 9, 10, 12, 13, 16, 17]); s = rng.randrange(0, 4)
    xi = [0]*(a+1)
    for i in range(a+1):
        if i % E <= s: xi[i] = rng.randrange(0, 2**10)
    s0 = level(xi, E)
    if s0 < 0: continue
    while True:
        lam, mu, gam, dlt = [GF(rng.randrange(0, 2**10)) for _ in range(4)]
        if lam*dlt + mu*gam != 0 and gam != 0: break
    s1 = level(mobius(xi, a, lam, mu, gam, dlt), E)
    cnt_bad += s1 > s0 + a % E
    s2 = level(mobius(xi, a, lam, mu, GF(0), GF(1)), E)   # affine change
    cnt_aff_bad += s2 > s0
print(f'  random: {cnt_bad}/{trials} general Mobius changes violate s->s+(a mod E); affine changes violating s->s: {cnt_aff_bad}/{trials}')

print('\n== (e) Lemma 2.1(i),(ii), Prop 2.2: random tests over GF(2^10), E=8 ==')
P = galois.Poly
rng = random.Random(2); viol_i = 0; viol_22 = 0; viol_ii = 0; ntest = 0
for _ in range(150):
    E = 8
    while True:
        A1 = P([GF(rng.randrange(1, 1024)), GF(rng.randrange(1, 1024))], field=GF)   # A1(0)!=0
        A2 = P([GF(rng.randrange(1, 1024)), GF(rng.randrange(0, 1024))], field=GF)
        if galois.gcd(A1, A2).degree == 0: break
    Pu = A2 * P([1] + [0]*E, field=GF) + A1
    roots = Pu.roots()
    a = rng.choice([8, 10, 12, 15]); K = a // E
    s = rng.randrange(0, E)
    # xi with prescribed level s
    pieces = [P([GF(rng.randrange(0, 1024)) for _ in range(min(s, a - k*E) + 1)], field=GF) for k in range(K+1)]
    xi = sum((pieces[k] * P([1] + [0]*(k*E), field=GF) for k in range(K+1)), P([0], field=GF))
    if xi == 0: continue
    ntest += 1
    R = sum((pieces[k] * A1**k * A2**(K-k) for k in range(K+1)), P([0], field=GF))
    z = sum(1 for t in roots if A2(t) != 0 and xi(t) == 0)
    if R != 0 and z > R.degree: viol_i += 1
    # Prop 2.2: xi = t^E * xi1, E<=a<2E -> residual zeros of xi = zeros of xi1 among residual roots
    if 8 <= a < 16:
        xi1 = P([GF(rng.randrange(0, 1024)) for _ in range(a - E + 1)], field=GF)
        if xi1 != 0:
            xx = xi1 * P([1] + [0]*E, field=GF)
            z2 = sum(1 for t in roots if xx(t) == 0)
            z1 = sum(1 for t in roots if xi1(t) == 0)
            viol_22 += (z2 != z1) or (z2 > xi1.degree)
    # (ii) Hasse criterion: level<=s iff D^(j)xi == 0 for s<j<E
    def hasse(p, j):
        cs = p.coeffs[::-1]; out = [GF(0)]*max(1, len(cs))
        for i in range(j, len(cs)):
            if ((i & j) == j): out[i-j] = cs[i]
        return P(out[::-1], field=GF)
    lv = level([int(c) for c in xi.coeffs[::-1]], E)
    for s0 in range(0, E):
        crit = all(hasse(xi, j) == 0 for j in range(s0+1, E))
        viol_ii += crit != (lv <= s0)
print(f'  tests={ntest}: Lemma 2.1(i) violations {viol_i}; Prop 2.2 violations {viol_22}; Lemma 2.1(ii) criterion mismatches {viol_ii}')

print('\n== (f) r=4, n=2Q beyond the grid: qq=E/8 closed (mode all) and qq=E/16 ==')
for Q in [2**15, 2**17, 2**19]:
    S = 64; r = 4; n = 2*Q; E = r*Q*S
    c8 = RT.closed(r, Q, S, n, E//8, 'all'); c16 = RT.closed(r, Q, S, n, E//16, 'all')
    c4 = RT.closed(r, Q, S, n, E//4, 'all')
    print(f'  Q=2^{Q.bit_length()-1}: qq=E/4 closed {c4}, E/8 closed {c8}, E/16 closed {c16}')
