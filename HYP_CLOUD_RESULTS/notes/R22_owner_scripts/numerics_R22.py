# numerics_R22.py -- R22 owner (Claude HYP(2)). Exact-rational evaluation of the three new counts:
#  (4.1) Cor 4.1  constant twist, NOT (K):        Nd + Ex + 2(E+1)d + (Q+1) a d'/(X-rho) + 6 d_def + 7
#  (4.2) Cor 4.2  constant twist, (K), F^2 !| a:  Nd + Ex + (E+1)d + (Q+1) M' d'/rho + 6 d_def + 7
#  (5.3) Thm 5.3  non-constant twist, not (K), qq > S:
#        step 1 (K_psi):  charges + deg(dd^2),  deg dd^2 <= 2(E+1)d + 2ad' + 2(Nd+rho d)        (R21 Lemma 3.2)
#        step 2 (K):      charges + (E+1)d + [a d' + (Nd+rho d) + (d^2-3d) + 2(E+1)d]/(m*-1), m*=2
#        charges = Nd + 2 deg[T]/qq + Ex + 6 d_def + 7, deg[T] <= Nd/rho + d, qq >= 128
#  (5.5) Prop 5.5 (CONDITIONAL on the order sequence of V=span(t_ij)): charges + 2deg psi + deg R/(N0-eps_top),
#        deg R = (sum eps)(2g-2) + dim(V) tau_0, tau_0 = deg[T]/qq; worst cases N0-eps_top = 1.
# Normalisation as in R16-R21: N < M < 16h/625, a < M' < 8h/625, d = E+2, d' <= 2E+4, d_def <= q/1000,
# Ex = 1.5 d^2 + 3.5 d + 1 (R16.4 exceptional set, contains {g=0}), q = nE^2, h = nE, E = rQS, rho=Q/2, X=QS/2.
# Each term divided by q is non-increasing in r, Q, S, n (see the note), so the sup over the strip is the corner
# value (r,Q,S,n)=(4,128,64,256); the grid below confirms it.
from fractions import Fraction as Fr

TARGET = Fr(1551, 4000)


def terms(r, Q, S, n):
    E = r * Q * S
    q = n * E * E
    h = n * E
    d = E + 2
    dp = 2 * E + 4
    N = Fr(16 * h, 625)
    a = Fr(8 * h, 625)
    Mp = Fr(8 * h, 625)
    rho = Fr(Q, 2)
    X = Fr(Q * S, 2)
    Ex = Fr(3, 2) * d * d + Fr(7, 2) * d + 1
    ddef = Fr(q, 1000)
    psi = (E + 1) * d
    degT = N * d / rho + d
    c41 = (N * d + Ex + 2 * psi + (Q + 1) * a * dp / (X - rho) + 6 * ddef + 7) / q
    c42 = (N * d + Ex + psi + (Q + 1) * Mp * dp / rho + 6 * ddef + 7) / q
    charges = N * d + 2 * degT / 128 + Ex + 6 * ddef + 7
    dd2 = 2 * psi + 2 * a * dp + 2 * (N * d + rho * d)
    s1 = (charges + dd2) / q
    s2 = (charges + psi + (a * dp + (N * d + rho * d) + (d * d - 3 * d) + 2 * psi)) / q
    tau0 = degT / 128
    # Prop 5.5 (CONDITIONAL on the order sequence of V=span(t_ij)): charges + 2 deg psi + deg R/(N0-eps_top)
    p55_classical = (charges + 2 * psi + (6 * (d * d - 3 * d) + 4 * tau0)) / q      # eps=(0,1,2,3), N0>=4
    p55_pencil = (charges + 2 * psi + ((d * d - 3 * d) + 2 * tau0)) / q             # dim V=2, eps=(0,1), N0>=2
    return c41, c42, s1, s2, p55_classical, p55_pencil


def main():
    print("R22 numerics (exact Fractions); target 1551/4000 =", float(TARGET))
    rows = 0
    mx = [Fr(0)] * 6
    arg = [None] * 6
    for r in (4, 8, 16, 32, 64):
        for v in range(7, 15):
            Q = 1 << v
            for s in range(6, 13):
                S = 1 << s
                n = 256
                while n < 4 * Q:
                    t = terms(r, Q, S, n)
                    rows += 1
                    for i in range(6):
                        if t[i] > mx[i]:
                            mx[i] = t[i]
                            arg[i] = (r, Q, S, n)
                    n *= 2
    names = ["Cor 4.1 (constant, not K)", "Cor 4.2 (constant, K, F^2 !| a)",
             "Thm 5.3 step 1 (K_psi)", "Thm 5.3 step 2 (K)",
             "Prop 5.5 classical V (eps=0,1,2,3; N0>=4)", "Prop 5.5 pencil V (dim 2; N0>=2)"]
    allok = True
    for i in range(6):
        ok = mx[i] < TARGET
        allok &= ok
        print(f"{names[i]}: max bound/q = {float(mx[i]):.6f} at (r,Q,S,n)={arg[i]}; < 1551/4000: {ok}")
    corner = terms(4, 128, 64, 256)
    print("corner (4,128,64,256):", [f"{float(x):.8f}" for x in corner])
    print("corner exact:", [str(x) for x in corner])
    print("rows:", rows, "| all below target:", allok)


if __name__ == '__main__':
    main()
