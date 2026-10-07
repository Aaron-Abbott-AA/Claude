#!/usr/bin/env python3
"""Positive control for sh_ref_rk_kernel.py (referee code).  Run from checks/: nice -n 19 python3 -I sh_ref_rk_control.py
Build the degree-1 relation P' of W'' = span(1, X, 1/(X+1)) (3x4 cofactors; third row scaled by (X+1)^(2Q)).
Then ker P' ∩ L ⊇ W'' has a pole at X = 1, so kernel_dim must give 2 for g = 1 and 3 for g = X+1.
This shows the kernel routine detects rational roots with finite poles.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sympy import Poly, symbols, Matrix, expand
import sh_ref_rk_kernel as R

X = symbols('X')
for m in (4, 6, 8):
    Q = 2 ** (m // 2); E = [1, 2, Q, 2 * Q]
    rows = [[1, 1, 1, 1], [X ** e for e in E], [(X + 1) ** (2 * Q - e) for e in E]]
    M = []
    for l in range(4):
        cols = [j for j in range(4) if j != l]
        d = Poly(expand(Matrix(3, 3, lambda i, j: rows[i][cols[j]]).det(method='berkowitz')), X, modulus=2)
        M.append([int(c) % 2 for c in reversed(d.all_coeffs())])
    K = R.F(m)
    k1 = R.kernel_dim(K, Q, M, [1], 6)
    kg = R.kernel_dim(K, Q, M, [1, 1], 6)
    print(dict(m=m, kernel_g1=k1, kernel_gXp1=kg, expected=(2, 3), ok=(k1, kg) == (2, 3)), flush=True)
