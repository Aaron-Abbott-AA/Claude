# HYP M>=2, round 24 (owner v1): (R1) is closed by a partial Wronskian; G5 is exactly FNAM2 plus nonzero alignment, which closes 𝔇_16 at n=256; the condition F²|a is invisible to every single-point own-line argument

7 October 2026. Claude HYP(2) owner research note (R24), following R23 v2.1.

**Version.** v1, owner draft. It has not been audited. Every PROVED label below is the owner's claim, pending an independent audit.

**Targets (coordinator):**
- (a) study F²|a_P, F²|a_R directly: what global alignment with F²|a implies for P, a second-order lift, the layer identity at order F², the transverse layer, and combinations with (★)/Thm 3.1 at order 2X or with G5;
- (b) (R1): bound 𝔅_0 or Σε_i for non-classical V;
- (c) precise negative results or toy constructions where (a), (b) stall.

I did (b) first, then (a), then (c).

**Inputs (read, not re-proved; copies in `inputs/`):**
- R23 v2.1. Used: §1 (good u, (1.1)), Prop 2.1, Cor 2.2(iii), Thm 3.1, Remark 3.4, Prop 4.1, Cor 4.2, Lemma 4.3, Prop 4.4 (statement and the facts used in its proof), Cor 4.5's case split, §6 residual list.
- R22 v2.1. Used: §1, Lemma 2.1, Prop 2.3 (★), Lemma 2.4, Thm 3.1 (and Step 4), Remark 4.4, Prop 4.3, Lemma 5.1, Thm 5.3 and its numerical normalisation (corner value of B_{5.3(i)}).
- R21 v2.1 (𝔉_D, Prop 2.3), R20 v2.1 (Prop 3.1, Cor 3.2/3.3 table, Lemma 4.3's k), R19 v2.1 (Lemma 3.5(i): Ξ(u,·)=σ_u^{ρ𝔮}, σ_u∈V), R18-T v2.1 (Lemma 1.1, Lemma 2.1(i),(ii), Prop 2.4, Prop 4.1(ii), Prop 4.2), R16 v2.1 (§1: A^hom, G5, PRIM, M<16h/625; R16.1), R17/R18 as cited there.
- PRIMARY FNAL, TSY, TSYC, FNAM (FNAM1 κ_0, J; FNAM2), as reviewed. All PRIMARY results remain PRIMARY's. FNAM2 (G5 ⇒ Δ≢0) is PRIMARY's; §2 adds the exact factorisation behind it.
- Stöhr–Voloch, *Weierstrass points and curves over finite fields*, Proc. LMS 52 (1986): §1 (Hasse derivatives, orders, Thm 1.5: j_i(P)>=ε_i) and Cor 1.9 (p-adic criterion). CITED, as in R23. The partial-Wronskian Lemma 3.1 is proved here in full. It is the truncated-flag version of the proof of SV Thm 1.5 and is standard in spirit (associated curves).

**Labels (as in R18-T–R23):**
- PROVED: complete proof here, conditional only on the named inputs.
- CONDITIONAL: proved under a named hypothesis that is not established.
- COMPUTED: exact computation; it proves only where an exact bound is evaluated.
- HEURISTIC / OPEN / CITED: as stated.

**Rules followed.**
- No file whose name contains "DZ" was opened. (The PRIMARY TSY/TSYC copies mention DZ only in credit lines.)
- No PRIMARY/Codex script was executed; only `.md` files were read.
- Own scripts only, `python3 -I`, one process at a time, each under 1 minute (the longest took 57 s).
- Each script prints exact failing sets, not only sample points.

**Notation** is that of R22/R23:
- q=Eh, E=rQS, ρ=Q/2, X=T/2=ρS, n=h/E; d=deg Γ<=E+2; d'=deg Γ'∈[2E−2,2E+4]; M'=(M−1)/2<8h/625; a=deg C_•=M'+X−ρ−d'; deg a_•=M'+Q−T.
- P^tf^[ρ]=a_Pf^[X], R^tf^[ρ]=a_Rf^[X] (global alignment); a_•=F·a'_• (zero top).
- J=[j_1,j_2], f=κ_0 j_1×j_2 (FNAM1); Ω=[[0,1],[1,0]]; R18-T Lemma 2.1(ii): J^{[X],t}P^t=κ_0^{−X}FΩC_PJ^{[ρ],t} (global).
- A=A^hom=(ℓ(U)·Y)P^[2]+(m(U)·Y)R^[2], with ℓ(U)=LU, m(U)=NU, so ℓ(U)·Y=U·j_1(Y) and m(U)·Y=U·j_2(Y). G5: det A≢0 (R16 §1).
- Δ(v,Y)=det(v_1C_P+v_2C_R)=v_1²Δ_0+v_1v_2Δ_1+v_2²Δ_2 (FNAM2); k_Δ:=min_i ord_F Δ_i (R20 Lemma 4.3's k).
- Good u, c=c(u), Y(t)=z+tV, ω, b=gD·c^[2], s̃_u, e_u, ν_u, 𝔅_0, (𝒦), V=span(t̂_ij) for 𝔮_max, ε_i, j_i(u), N_0=(2r−1)S/𝔮_max, γ=(r−1)S/𝔮_max−1: as in R23.
- **New:**
  - 𝒞_A:=(ℓ(U)·Y)C_P^[2]+(m(U)·Y)C_R^[2] (2×2) and λ_A:=(ℓ(U)·Y)a_P²+(m(U)·Y)a_R² (§2).
  - The transverse layer σ_• (Lemma 2.1).
  - x:=S/𝔮_max; s:=#{i: ε_i<N_0}; Σ':=Σ_{ε_i<N_0}ε_i; γ':=N_0−max{ε_i: ε_i<N_0} (§3).

---

## 0. Summary

**PROVED.**
1. **(R1) is closed (Thm 3.3).** Every non-constant twist outside (𝒦) in 𝔇_16 is excluded, for every r, n, 𝔮_max, at every strip scale:
      N_good <= B_{5.3(i)} + (s/γ')τ_hi + (Σ'/γ')(d²−3d) <= 0.167242q < 1551q/4000.
   - **The new input** is a partial Wronskian (Lemma 3.1). For each s, the s×s minors of the Hasse rows ε_0,…,ε_{s−1} define an effective divisor R_s with
         deg R_s <= sτ_0 + (Σ_{i<s}ε_i)(2g−2)   and   v_P(R_s) >= Σ_{i<s}(j_i(P)−ε_i).
   - **Applied with s=#{ε_i<N_0}.** At u∈𝔅_0, the non-order N_0 (R23 Lemma 4.3(ii)) is a vanishing order (R23 Prop 4.4). So some j_i(u)=N_0 with ε_i<N_0, i.e. i<s. Hence u has weight >=γ' in R_s, not only in the full R_V.
   - **Why this suffices.** Only the orders **below** N_0 enter the degree. By the p-adic structure (R23 Lemma 4.3) their sum is <=2(rx+1), and Σ'/γ'<=5 and s/γ'<=2 on the whole strip. So |𝔅_0|<=5(d²−3d)+2τ_hi≈0.0195q. R23 needed Σ_all ε_i<=0.238γn, which fails when ε_top is large. Large ε_top no longer matters, and no Frobenius non-classical structure is needed.
2. **The exact determinant of A (Prop 2.2).** In 𝔇_16 (global alignment, FNAL/TSY/FNAM1), as polynomials in (U,Y):
      det A = κ_0^{−(Q+T)} · F⁴ · det 𝒞_A · λ_A.
3. **G5 is exactly FNAM2 plus nonzero alignment (Cor 2.3).**
   - G5 ⟺ Δ≢0 and (a_P,a_R)≢(0,0).
   - ord_F det A = 4 + 2k_Δ + 2·min(ord_F a_P, ord_F a_R).
   - In particular F⁶|det A in 𝔇_16, and F^{10}|det A in (𝒦)∧F²|a.
4. **F²|a forces a high top degree (Cor 2.4).** If F²|a_P and F²|a_R, then (G5) M'+Q−T>=2d', i.e. a>=d'+3(X−ρ). In the strip this is impossible at n=256 for every r, Q, S. In general it forces n>=512.
5. **𝔇_16 is excluded at n=256 (Cor 2.5).** Assembling R20 Cor 3.2, R22 Cor 4.1/4.2, R23 Thm 3.1, Thm 3.3 and Cor 2.4: every model of 𝔇_16 (standing hypotheses) with h=256E is excluded. This answers R23 Remark 3.4's OPEN question ("zero alignment" a_P=a_R≡0 contradicts G5). It closes (R2) at n=256 for every r>=16, including r=16 below 8E/Q.
6. **The transverse layer carries F²|a (Lemma 2.1).** Locally at z∈Γ' with f(z)≠0:
      P^t = f^[X]⊗κ̃_P + F·(G̃κ_0^{−X}ΩC_PJ^{[ρ],t} + f^[X]⊗σ_P),   a'_P = σ_P·f^[ρ].
   So F²|a_P ⟺ σ_P|_{Γ'} is a syzygy of f^[ρ] ⟺ there is a "second-order lift": P^t≡f^[X]⊗κ̂_P+F·G̃κ_0^{−X}ΩC_PJ^{[ρ],t} (mod F²) with κ̂_P∈Syz(f^[ρ]).

**PROVED negative results (target (c)).**
7. **FN on an own line never sees a beyond order ρ (Prop 4.1).** At a good u, granting TSYC (α), FN along ℓ_u is equivalent to one scalar identity, g^ρσ_c·u^[ρ]=φ_u(t), with φ_u determined by (C, twist, gauge). The alignment coefficient enters only through a'_c=g^ρσ_c·u^[ρ]+t^ρσ_c·ω^[ρ]. So FN fixes a'_c along ℓ_u exactly modulo t^ρ (R22 Thm 3.1(ii)) and **nothing beyond**.
8. **Local realisability of (𝒦)∧F²|a (Prop 4.2).** Let u be good, with (𝒦), (α) at u and ν_u>=e_u (automatic for a constant twist; necessary by R23 Cor 2.2(iii)). Then there is a matrix germ P at z(u) with:
   - the given first layer and second layer C;
   - local alignment with F²|a;
   - FN along ℓ_u identically in t.

   Hence no argument at a single good point, at any own-line order (in particular (★)/Thm 3.1 at order 2X), can exclude (𝒦)∧F²|a. An exclusion must use global (polynomial, degree) information on P's transverse layer, as Cor 2.4 does.

**COMPUTED** (`scripts/`, exact):
- `numerics_R24.out`:
  - all 120 p-adic-closed order sequences with ε_1=1 (brute-force cross-check on entries <=64: 27=27); exact failing set for "N_0 is an order / γ'<γ / Σ'/γ'>(2rx+2)/γ" is empty; global max Σ'/γ'=5, s/γ'=2, both at r=4, x=1, ε=(0,1,4,5);
  - the R22 corner B_{5.3(i)}=32480243592761/219902325555200 is reproduced exactly;
  - the (R1) bound on 3780 grid cases (r,Q,S,n,𝔮_max<=S): exact failing set empty, grid max 0.167228; whole-strip upper bound 91941792089517/549755813888000≈0.1672411;
  - Cor 2.4: the set of rows where F²|a is degree-feasible at n=256 is empty; the least feasible n is 512 on all 280 (r,Q,S).
- `det_identity_check.out`: Prop 2.2, at random points over GF(2^16): 150/150, with (X,ρ) ranging from (4,2) to (4096,64). The negative control (F³ in place of F⁴) fails 150/150, and a_P=a_R=0 gives det A=0 in 150/150.
- `partial_wronskian_check.out`: Lemma 3.1 on P^1 over GF(2^8), V with orders (0,1,4,8). Both inequalities hold at all 256 points for s=1..4 (exact failing sets empty). At the two points where the non-order 5 is a vanishing order, v_P(R_3)=1. At a Weierstrass point with j=(0,1,4,9), v_P(R_3)=0, which illustrates the gain.
- `local_realization_toy.out`: Prop 4.1/4.2 on one own line over GF(2^8)[[t]], 15 cases, all pass.
  - Random σ violates FN.
  - The constructed σ gives FN together with σ·f^[ρ]≡0 along the line.
  - The control ord s̃=e−1 produces the predicted pole.

**What failed.**
- (a) (𝒦)∧F²|a_P∧F²|a_R is **not** excluded for n>=512, constant or not. G5 contributes exactly (a_P,a_R)≠0 (Cor 2.3), hence the degree bound of Cor 2.4. The second-order lift (Lemma 2.1) and (★) at order 2X contribute nothing at a single point (Props 4.1–4.2).
- The suggested Frobenius non-classical structure (Hefez–Voloch) was not needed for (b) and was not used.
- Nothing new for (R2) from Lemma 3.1 (Remark 3.5): there N_1=2rS/𝔮_max is a power of 2, and only a lower bound for ord σ_u is known.

**Newly closed (PROVED; numbers COMPUTED; v1 not yet audited):**
- (R1) entirely: every non-constant twist outside (𝒦), every r, n, 𝔮_max.
- 𝔇_16 at n=256 entirely, including (R2) at n=256 for r>=16 (r=16 below 8E/Q and r>=32).
- (𝒦)∧F²|a at n=256 for every twist, and every model with a_P=a_R≡0 (all n).

**Residual of 𝔇_16 after R24.** Only (𝒦)∧F²|a_P∧F²|a_R remains (§5), with n>=512 and M'+Q−T>=2d':
- constant twists: D∈{1,2} on 𝔉_D∩{F|h}∩{F²|a}; D>=4 lanes with n<4D, now only D>=256;
- (R2) rows left open by R20/R23: r=4 below R20's thresholds at n>=512; r=8 below them at n∈{512,1024}, and all of n>=2048; r=16 and r>=32 at all n>=512 (r>=32 wherever R20 does not apply).

---

## 1. Setting

The standing hypotheses are those of R22/R23 §1: 𝔇_16, global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮_max>=128, all original gates including G5 and PRIM. Good points, the charges (boundary 6d_def+7 ⊃ Bs(e); 𝔈<=1.5d²+3.5d+1 ⊃ {g=0}; {λ'=0}<=Nd; {det T̂=0}<=2deg[T]/𝔮) and the 𝔮_max conventions are as there.

Γ' contains every base point of f (R18-T Lemma 2.1A). §2's determinant identity is a global polynomial identity and uses no local splitting. Lemma 2.1 and §4 work only at points z∈Γ' with f(z)≠0, in particular at z(u) for good u (f(z(u))=g(u)u≠0).

---

## 2. Target (a): the condition F²|a

**Lemma 2.1 (the transverse layer and the second-order lift; PROVED from R22 Lemma 2.4(i), R18-T Lemma 2.1(ii), FNAM1).** Let z∈Γ' with f(z)≠0, and O:=O_{P²,z}.
- Take the syzygy lift κ̃_P=λ̃(𝒜̃_11j_1^[ρ]+𝒜̃_12j_2^[ρ]) of R22 §1, so κ̃_P·f^[ρ]=0 exactly.
- Take any G̃∈M_{3×2}(O) with J^{[X],t}G̃=I_2. It exists because J^{[X],t}(z) has rank 2.

Then:
- **(i) Unique decomposition.** There is a unique σ_P∈O³ with
      P^t = f^[X]⊗κ̃_P + F·(G̃κ_0^{−X}ΩC_PJ^{[ρ],t} + f^[X]⊗σ_P),   and then   a'_P = σ_P·f^[ρ].
- **(ii) Gauge.** Replacing κ̃_P by κ̃_P+Fη (η∈Syz_O(f^[ρ])), or G̃ by G̃+f^[X]⊗θ, changes σ_P by a vector orthogonal to f^[ρ]. So a'_P=σ_P·f^[ρ] is gauge-invariant. The modification of R22 Prop 4.3, P^t↦P^t+F·f^[X]⊗ξ, is σ_P↦σ_P+ξ.
- **(iii) The equivalences.** These are equivalent:
  - F²|a_P;
  - σ_P·f^[ρ]∈FO;
  - σ_P mod F is a syzygy of f^[ρ] mod F;
  - (second-order lift) there is κ̂_P∈Syz_O(f^[ρ]) with κ̂_P≡κ̃_P mod F and
          P^t ≡ f^[X]⊗κ̂_P + F·G̃κ_0^{−X}ΩC_PJ^{[ρ],t}   (mod F²).

The same holds for R, and for P_c=c_1P+c_2R with σ_c=c_1σ_P+c_2σ_R.

*Proof.*
- **(i) The second layer.** By R22 Lemma 2.4(i), P^t−f^[X]⊗κ̃_P=F·S_P with S_P∈M_3(O).
- **(i) Its J-part.** Apply J^{[X],t} and use J^{[X],t}f^[X]=(J^tf)^[X]=0 and R18-T Lemma 2.1(ii). F is a nonzerodivisor, so J^{[X],t}S_P=κ_0^{−X}ΩC_PJ^{[ρ],t}. Hence every column of S_P−G̃κ_0^{−X}ΩC_PJ^{[ρ],t} lies in ker(J^{[X],t}:O³→O²).
- **(i) The kernel.** J^{[X],t}(z) is onto, so this kernel is free of rank 1. It contains f^[X], which is unimodular since f(z)≠0. So the kernel is O·f^[X], which gives σ_P. Uniqueness: f^[X] is unimodular.
- **(i) Alignment.** Multiply by f^[ρ]. Here κ̃_P·f^[ρ]=0 and J^{[ρ],t}f^[ρ]=0. So P^tf^[ρ]=F(σ_P·f^[ρ])f^[X]. Comparing with a_Pf^[X] (f^[X] unimodular) gives a_P=Fσ_P·f^[ρ].
- **(ii)** The first change sends σ_P↦σ_P−η, with η·f^[ρ]=0. The second sends σ_P↦σ_P−κ_0^{−X}(θΩC_PJ^{[ρ],t}), whose dot product with f^[ρ] is 0. The last claim is the definition.
- **(iii) First two.** F is prime and z∈Γ', so F|a'_P in S iff F|a'_P in O.
- **(iii) Lifting syzygies.** Since f^[ρ](z)≠0, pick e'∈O³ with e'·f^[ρ]=1. Every v∈O³ splits as v=(v·f^[ρ])e'+(v−(v·f^[ρ])e'), and the second summand is a syzygy. So v·f^[ρ]∈FO iff v∈FO³+Syz_O(f^[ρ]).
- **(iii) The lift.** If σ_P=Fτ+η with η a syzygy, put κ̂_P:=κ̃_P+Fη. Then P^t=f^[X]⊗κ̂_P+F·G̃(…)+F²f^[X]⊗τ. Conversely, κ̂_P−κ̃_P=Fη' with η' a syzygy (both are syzygies, F a nonzerodivisor), and the displayed congruence gives σ_P−η'∈FO³. ∎

*Remark.* Lemma 2.1 says that a' is the transverse layer σ contracted with f^[ρ]. FN, by contrast, contracts the same σ with u^[ρ] along ℓ_u (Prop 4.1). At t=0, f(z)^[ρ]=g^ρu^[ρ], so the two contractions agree to order ρ and are unrelated beyond it. This is the whole content of §4.

**Proposition 2.2 (exact determinant of A; PROVED from global alignment, R18-T Lemma 2.1(ii), FNAM1; COMPUTED `det_identity_check.out`).** As polynomials in k[U,Y],
      det A = κ_0^{−(Q+T)} · F⁴ · det 𝒞_A · λ_A,
      𝒞_A=(U·j_1)C_P^[2]+(U·j_2)C_R^[2],   λ_A=(U·j_1)a_P²+(U·j_2)a_R².

*Proof.*
- **Two global identities.** Square R18-T Lemma 2.1(ii) entrywise; Frobenius commutes with products and Ω is a 0/1 matrix:
      J^{[T],t}(P^t)^[2] = κ_0^{−T}F²ΩC_P^[2]J^{[Q],t}.
  Hence
      J^{[T],t}A^t = κ_0^{−T}F²Ω𝒞_AJ^{[Q],t}.          (2.1)
  Squaring global alignment gives (P^t)^[2]f^[Q]=a_P²f^[T]. Hence
      A^tf^[Q] = λ_Af^[T].          (2.2)
- **Block-triangularise.** Let e be a standard basis vector with e·f^[T]≢0. Put L_e:=[J^{[T],t}; e^t] and R_Q:=[J^[Q] | f^[Q]] (3×3). By (2.1) and (2.2), and since J^{[T],t}f^[T]=(J^tf)^[T]=0,
      L_eA^tR_Q = [[κ_0^{−T}F²Ω𝒞_A(J^tJ)^[Q], 0],[e^tA^tJ^[Q], λ_A(e·f^[T])]].
- **Determinants.**
  - det L_e=e·(j_1×j_2)^[T]=κ_0^{−T}(e·f^[T]).
  - det R_Q=(j_1×j_2)^[Q]·f^[Q]=κ_0^{−Q}(f·f)^Q.
  - det(J^tJ)=|j_1×j_2|²=κ_0^{−2}(f·f), by the Cauchy–Binet (Lagrange) identity over any commutative ring.
  - det Ω=1 in characteristic 2.
- **Combine.** Taking determinants,
      κ_0^{−T}(e·f^[T])·det A·κ_0^{−Q}(f·f)^Q = κ_0^{−2T}F⁴det𝒞_A·κ_0^{−2Q}(f·f)^Q·λ_A(e·f^[T]).
  Here f·f=(f_0+f_1+f_2)²≢0, because the components of the birational quadratic map f are linearly independent. Cancelling gives the claim.
- **Degree check.** The Y-degree of the right side is 4d'+2(1+2a)+(1+2(M'+Q−T))=6M'+3=deg_Y det A. ∎

**Corollary 2.3 (G5 decoded; PROVED).**
- (i) **G5 ⟺ FNAM2 ∧ (a_P,a_R)≢(0,0).** That is, det A≢0 iff Δ≢0 and not both alignment coefficients vanish identically.
- (ii) **The F-adic order.** ord_F det A=4+2k_Δ+2·min(ord_F a_P, ord_F a_R). Consequences:
  - in 𝔇_16 (zero top), F⁶|det A;
  - in (𝒦) (k_Δ>=1, R18-T Prop 4.1(ii)), F⁸|det A;
  - in (𝒦)∧F²|a, F^{10}|det A.

*Proof.*
- **The two factors.** Squaring is additive in characteristic 2, so
      det 𝒞_A = Δ(v,Y)² with v_1²=U·j_1, v_2²=U·j_2, i.e. det 𝒞_A = (U·j_1)²Δ_0² + (U·j_1)(U·j_2)Δ_1² + (U·j_2)²Δ_2².
  Likewise λ_A=(U·j_1)a_P²+(U·j_2)a_R².
- **Independence over k(Y).** j_1, j_2 are independent over k(Y) (FNAM1). So the linear forms U·j_1, U·j_2 in U are independent, and the three quadratic monomials in them are k(Y)-independent polynomials in U.
- **(i)** Hence det𝒞_A≢0 iff some Δ_i≢0, i.e. Δ≢0; and λ_A≢0 iff (a_P,a_R)≢0. Then apply Prop 2.2 (k[U,Y] is a domain).
- **(ii) Independence on Γ'.** The same independence holds over k(Γ'), since J has rank 2 at the generic point of Γ' (its minors are κ_0^{−1}f, and f|_{Γ'}≢0).
- **(ii) The orders.** So, after removing F^{2k_Δ} (resp. F^{2min ord}), the bracket is not divisible by F. Its restriction to Γ', as a polynomial in U, is nonzero. Hence ord_F det𝒞_A=2k_Δ and ord_F λ_A=2min(ord_F a_P, ord_F a_R). ∎

*Remarks.*
- FNAM2 (PRIMARY) is the implication G5⇒Δ≢0, proved there by a rank argument. Cor 2.3(i) is the exact two-sided statement. Its only new content is the alignment factor λ_A.
- [HEURISTIC/OPEN] If an original gate bounded the F-multiplicity of det A (for example ord_F det A<10), Cor 2.3(ii) would exclude all of (𝒦)∧F²|a. No such gate is in R16's list (G5 is only det A≢0). This is a question for PRIMARY.

**Corollary 2.4 (F²|a forces a high top degree; PROVED; COMPUTED Part C).** Assume F²|a_P and F²|a_R. Then:
- M'+Q−T>=2d', equivalently a>=d'+3(X−ρ). This is stronger than R20 Prop 3.1's a>=d' by 3(X−ρ).
- In the strip this fails for n=256, for every r>=4, Q>=128, S>=64. So F²|a forces n>=512.

*Proof.*
- **The degree bound.** By Cor 2.3(i), one of a_P, a_R, say a_•, is a nonzero form. It is divisible by F², so deg a_•=M'+Q−T>=2d'.
- **At n=256.** M'<8h/625=8nE/625 and d'>=2E−2. So M'+Q−T<(2048/625)E+Q−T<4E−4, because (4−2048/625)E=(452/625)E>4 and Q<T.
- **Check.** Part C finds no feasible row at n=256 and least feasible n=512 on all 280 (r,Q,S). ∎

**Corollary 2.5 (𝔇_16 is excluded at n=256; PROVED, assembling the cited results).** Every model of 𝔇_16 with h=256E (standing hypotheses of §1) is excluded.

*Proof.* The case split is exhaustive:
- **Constant twist outside (𝒦):** R22 Cor 4.1, all n.
- **Constant twist in (𝒦):** R20 Cor 3.2 already closes n=256. Independently, R22 Cor 4.2 covers F²∤a, and Cor 2.4 covers F²|a.
- **Non-constant twist outside (𝒦), i.e. (R1):** Thm 3.3 below, all n.
- **Non-constant twist in (𝒦), i.e. (R2):** R23 Thm 3.1 covers F²∤a, all n; Cor 2.4 covers F²|a at n=256. ∎

*What is new in Cor 2.5.* R23 Remark 3.4 left "a_P=a_R≡0" OPEN at n=256. Cor 2.3(i) excludes it by G5. Before this note, (R2) at n=256 was open for r=16 below 8E/Q (R20/R23 tables) and for r>=32 where R20 does not apply. Both are now closed.

---

## 3. Target (b): (R1) via a partial Wronskian

**Lemma 3.1 (partial Wronskian divisor; PROVED; COMPUTED `partial_wronskian_check.out`).** Let 𝒳 be a smooth projective curve of genus g over an algebraically closed field of characteristic p, 𝓛 a line bundle of degree τ, and V⊂H⁰(𝓛) of dimension r+1, with orders ε_0<…<ε_r (SV §1). For 1<=s<=r+1 there is an effective divisor R_s with:
- (a) deg R_s <= sτ + (Σ_{i<s}ε_i)(2g−2);
- (b) v_P(R_s) >= Σ_{i<s}(j_i(P)−ε_i) at every point P, where j_0(P)<…<j_r(P) are the vanishing orders of V at P.

For s=r+1 this is SV Thm 1.5, where (a) is an equality.

*Proof.*
- **Setup.** Fix a basis x_0..x_r of V, a nonzero section s_0∈H⁰(𝓛), and a separating variable x∈K=k(𝒳). Put ξ_j:=x_j/s_0∈K, and let D^{(m)} be Hasse derivatives with respect to x. Let row_m:=(D^{(m)}ξ_j)_j∈K^{r+1}.
- **Orders.** By definition, ε_i is the i-th m at which row_m is not in the K-span of row_0..row_{m−1}. So for every m, row_m lies in span_K{row_{ε_j}: ε_j<=m}.
- **The minors.** Let W_s be the s×(r+1) matrix with rows row_{ε_0},…,row_{ε_{s−1}}. Its rows are K-independent, so some s×s minor w_J (J an s-subset of columns) is ≢0.
- **Change of frame and parameter.** Fix P, a local parameter t at P and a local frame e_P of 𝓛 at P. Put y_j:=x_j/e_P=hξ_j with h:=s_0/e_P, and let row^P_m be the Hasse rows of (y_j) with respect to t.
  - Leibniz for Hasse derivatives: D_t^{(m)}(hξ)=Σ_{l<=m}D_t^{(m−l)}h·D_t^{(l)}ξ.
  - Chain rule: D_t^{(l)}=Σ_{k<=l}c_{l,k}D_x^{(k)} with c_{l,k}∈K and c_{l,l}=(D_t^{(1)}x)^l.
  - Combined with the span property, these give W_s^P=ΛW_s with Λ lower triangular in M_s(K) and diagonal entries h·(D_t^{(1)}x)^{ε_i}. Only these diagonal entries matter.
  - Hence, as elements of K, w^P_J=h^s(D_t^{(1)}x)^{Σ_{i<s}ε_i}w_J for every J.
- **The divisor.** Put v_P:=min_J ord_P(w^P_J). It is >=0, since the y_j are regular at P and so are their Hasse derivatives in t. Define R_s:=Σ_P v_P·P.
- **(a)** ord_P h=ord_P s_0 and ord_P(D_t^{(1)}x)=ord_P(dx). Fix J_0 with w_{J_0}≢0. Then
      deg R_s = sΣ_P ord_P s_0 + (Σ_{i<s}ε_i)Σ_P ord_P(dx) + Σ_P min_J ord_P w_J <= sτ + (Σ_{i<s}ε_i)(2g−2) + Σ_P ord_P w_{J_0},
  and Σ_P ord_P w_{J_0}=0.
- **(b) Adapted basis.** Changing the basis of V by a constant matrix multiplies the vector (w_J)_J by ∧^sA. This preserves min_J ord_P. So take a basis adapted to P, ord_P y_k=j_k(P). The entries satisfy ord_P D_t^{(ε_i)}y_k>=max(0, j_k(P)−ε_i).
- **(b) Expand.** In the Leibniz expansion of a minor with columns k_0<…<k_{s−1}, each term has order >=Σ_l(j_{k_l}(P)−ε_{π(l)})=Σ_l j_{k_l}(P)−Σ_{i<s}ε_i. Since k_l>=l and j is increasing, this is >=Σ_{i<s}(j_i(P)−ε_i). ∎

**Lemma 3.2 (bookkeeping of the orders below N_0; PROVED from R23 Lemma 4.3; COMPUTED Part A).** Assume 𝔮_max<=S, put x=S/𝔮_max>=1, and let V (for 𝔮_max, ε_1=1) be as in R23. Then:
- N_0=(2r−1)x is not an order;
- s<=4;
- γ':=N_0−max{ε_i<N_0}>=γ=(r−1)x−1>=2;
- Σ'<=2·max{ε_i<N_0}<=2(rx+1);
- consequently Σ'/γ'<=2(rx+1)/((r−1)x−1)<=5 and s/γ'<=2.

*Proof.*
- **First three claims.** R23 Lemma 4.3(ii),(iii).
- **The sum bound.** The orders below N_0 form a set closed under binary sub-integers (by the p-adic criterion, since sub-integers are smaller). R23 Lemma 4.3(iv)'s case list applies to it and gives Σ'<=2·max{ε_i<N_0}. The max is <=rx+1 by Lemma 4.3(iii).
- **The ratio.** 2m/(N_0−m) is increasing in m, which gives the first inequality. Then 2(rx+1)<=5((r−1)x−1) ⟺ x(3r−5)>=7, which holds for r>=4, x>=1.
- **Check.** Part A enumerates all 120 closed sequences and finds max Σ'/γ'=5 and max s/γ'=2, both at r=4, x=1, ε=(0,1,4,5). ∎

**Theorem 3.3 ((R1) is excluded; PROVED, conditional on R23 Prop 4.1, Cor 4.2, Lemma 4.3 and Prop 4.4's order facts, R22 Thm 5.3, R19 Lemma 3.5(i), CITED SV Thm 1.5 and Cor 1.9; numbers COMPUTED).** Every non-constant twist outside (𝒦) in 𝔇_16 is excluded, at every strip scale.
- If 𝔮_max>S, N_good<=0.147704q (R22 Thm 5.3).
- If 𝔮_max<=S, then
      |𝔅_0| <= [sτ_0 + Σ'(d²−3d)]/γ' <= 2τ_hi + 5(d²−3d),
      N_good <= B_{5.3(i)} + 2τ_hi + 5(d²−3d) <= 0.167242q < 1551q/4000,
  with τ_hi=(Nd/ρ+d)/𝔮_max.

*Proof.*
- **𝔮_max>S.** This is R22 Thm 5.3.
- **𝔮_max<=S: split the good points.** If 𝔡≡0, R23 Cor 4.2(i) puts the model in (𝒦), which is not (R1), or gives N_good<=0.104306q. If 𝔡≢0, R23 Cor 4.2(ii) and Prop 4.1 split the good points into Z(𝔡) and 𝔅_0, with N_good<=B_{5.3(i)}+|𝔅_0|. Here B_{5.3(i)} contains every charge: the boundary, 𝔈, {λ'=0}, {det T̂=0} and deg 𝔡².
- **Each u∈𝔅_0 is a zero of R_s.**
  - ν_u=E−X is finite, so σ_u∈V∖0 (R19 Lemma 3.5(i)), and ord_uσ_u=ν_u/(ρ𝔮_max)=N_0.
  - So N_0=j_{i_0}(u) for some i_0. By SV, ε_{i_0}<=j_{i_0}(u)=N_0, and N_0 is not an order (Lemma 3.2). So ε_{i_0}<N_0, i.e. i_0<s with s:=#{ε_i<N_0}.
  - Lemma 3.1(b) with this s, together with j_i(u)>=ε_i (SV), gives v_u(R_s)>=j_{i_0}(u)−ε_{i_0}>=N_0−max{ε_i<N_0}=γ'.
- **Count.** Distinct u∈𝔅_0 are distinct places of Γ̃. Lemma 3.1(a) with 𝓛=𝓣, τ=τ_0<=τ_hi (R18 §5) and 2g−2<=d²−3d gives |𝔅_0|<=deg R_s/γ'<=[sτ_hi+Σ'(d²−3d)]/γ'. Lemma 3.2 bounds this by 2τ_hi+5(d²−3d).
- **Numbers.**
  - B_{5.3(i)}/q is non-increasing in r, Q, S, n (R22), with corner value 0.14770305.
  - 5(d²−3d)/q=5(E²+E−2)/(nE²)<=5(1+2^{−15})/256.
  - 2τ_hi/q<=2((16/625)(1+2/E)/ρ+(E+2)/q)/128.
  - All three are non-increasing, so the whole-strip supremum is at most the corner value 91941792089517/549755813888000≈0.1672411<1551/4000 (Part B). This is a formal upper bound: at S=64, 𝔮_max<=S cannot occur.
  - The exact bound with the per-(r,x) worst ratios has grid maximum 0.167228, with an empty failing set on 3780 cases.
- In every case N_good<1551q/4000+1, a contradiction. ∎

*Remarks.*
- **3.4 (why R23 stopped short; PROVED comparison).** R23 Prop 4.4 used the full ramification divisor R_V=R_{r_V+1}. Its degree carries Σ_all ε_i, and ε_top can be as large as τ_0. But the defect at u∈𝔅_0 is in an order **below** N_0. The orders above N_0 add degree to R_V and nothing to the weight at u. Truncating the flag at s=#{ε_i<N_0} removes them. No structure of non-classical curves (Hefez–Voloch, Frobenius orders) is used. The coordinator's suggested route was not needed.
- **3.5 (no transfer to (R2); PROVED negative).** In (R2), R23 Prop 2.1 gives only ord_uσ_u>=N_1=2rS/𝔮_max at every good u. Exactness is not known. Suppose some order ε_i>=N_1. Then at every non-Weierstrass point the members of V of order >=N_1 form a nonzero subspace. So "ord_uσ_u>=N_1" is not a Weierstrass condition, and Lemma 3.1 yields nothing. If ε_top<N_1, R22 Prop 5.5 already closes it (R23 §3, RC-1).
- **(HEURISTIC)** The remaining (R2) information is that σ_u has the rank-one Frobenius coefficient form (Ωĉ^[Q])⊗ĉ. For example, when exactly one order is >=N_1, the osculating hyperplane at u has this form, with ĉ^{[Q𝔮]}=(β:α)(u). Turning this into a count costs the factor Q𝔮 in degree (R21 Remark 3.5, R23 §4). If it held identically, then ψ=(c'_2/c'_1)^{Q𝔮}∈K², contradicting R14.1. The open problem is the count at finitely many points.

---

## 4. Target (c): F²|a is invisible at every single own line

Throughout §4, u is good, c=c(u), and Lemma 2.1's gauge is fixed at z=z(u). Assume TSYC (α): b^{[X],t}C_c(Y(t))b^[ρ]≡0. This is FNAL2/TSYC, valid for every actual model. Write C_c(Y(t))b^[ρ]=γ_C(t)Ωb^[X] with γ_C∈k[t]. Write G̃b^[X]=ω^[X]+ζf^[X] with ζ∈k[[t]]: since J^{[X],t}ω^[X]=b^[X], the difference lies in O·f^[X] (Lemma 2.1(i)).

**Proposition 4.1 (the own-line content of FN in the transverse frame; PROVED).** Along ℓ_u, FN (R16.1: W_u:=P_c^tu^[ρ]∥u^[X]) is equivalent to
      g^ρ·σ_c(Y(t))·u^[ρ] = φ_u(t) := t^ρ·[ s̃_u/F + κ_0^{−X}γ_C(t^{−X}+ζ) ]   in k((t)).          (4.1)
Moreover a'_c(Y(t))=g^ρσ_c·u^[ρ]+t^ρσ_c·ω^[ρ]. Hence:
- (i) FN determines a'_c along ℓ_u modulo t^ρ. This is R22 Thm 3.1(ii): μ̂≡a'_c mod t^ρ.
- (ii) FN imposes no condition on σ_c·ω^[ρ], hence none on a'_c beyond order ρ. In particular a''_c (when F²|a) and the a-term t^Xa_c=t^XF²a''_c of (★), which has order >=X+2e_u, never enter.

*Proof.*
- **A basis.** Over k((t)), the vectors u^[X], f^[X], e_3 form a basis for any e_3 with J^{[X],t}e_3∦b^[X]. Indeed f^[X]=g^Xu^[X]+t^Xω^[X] and u∦ω.
- **Reduce to one coefficient.** Write W_u=α_1u^[X]+α_2f^[X]+α_3e_3. FN ⟺ α_2=α_3=0. By R22 Lemma 2.1(i) and R18-T Lemma 2.1(ii),
      J^{[X],t}W_u=κ_0^{−X}FΩC_c(t/g)^ρb^[ρ]=α_1(t/g)^Xb^[X]+α_3J^{[X],t}e_3.
  So (α) ⟺ α_3=0, and FN ⟺ (α)∧α_2=0.
- **Compute α_2.** Insert Lemma 2.1(i) and J^{[ρ],t}u^[ρ]=(t/g)^ρb^[ρ]:
      W_u = f^[X](κ̃_c·u^[ρ]) + F·κ_0^{−X}(t/g)^ργ_C(ω^[X]+ζf^[X]) + F·f^[X](σ_c·u^[ρ]).
  - The f^[X]-coefficient of ω^[X]=t^{−X}(g^Xu^[X]+f^[X]) is t^{−X}.
  - g^ρκ̃_c·u^[ρ]=κ̃_c·(f^[ρ]+t^ρω^[ρ])=t^ρs̃_u.
  - So g^ρα_2=t^ρs̃_u+F[g^ρσ_c·u^[ρ]+κ_0^{−X}t^ργ_C(t^{−X}+ζ)].
  - α_2=0 is (4.1), after dividing by F≢0 on ℓ_u (characteristic 2).
- **The alignment coefficient.** a'_c=σ_c·f^[ρ] (Lemma 2.1), and f^[ρ]=g^ρu^[ρ]+t^ρω^[ρ].
- **(i), (ii).** u^[ρ] and ω^[ρ] are k[[t]]-independent, since u(0) and w are independent. So (4.1) constrains only the u^[ρ]-contraction of σ_c. The coefficient a_c appears in neither (α) nor (4.1). ∎

**Proposition 4.2 (local realisability of (𝒦)∧F²|a at one own line; PROVED; COMPUTED `local_realization_toy.out`).** Fix the C-level data (C_P, C_R, twist, first layer κ̃_•). Assume at u: (𝒦), (α), and ν_u>=e_u. The last condition is automatic for a constant twist (s̃_u≡0) and is necessary for F²|a by R23 Cor 2.2(iii). Then there is a matrix germ P^t (and R^t) of regular functions at z(u) with:
- J^{[X],t}P^t=κ_0^{−X}FΩC_PJ^{[ρ],t};
- P^t≡f^[X]⊗κ̃_P mod F;
- P^tf^[ρ]=a_Pf^[X] with F²|a_P in O (and likewise for R);
- FN along ℓ_u identically in t.

*Proof.*
- **The ansatz.** Take P^t, R^t of the form of Lemma 2.1(i), with σ_R:=0 and σ_P:=σ/c_1 (if c_1=0, swap the roles of P and R). The first two properties hold for every regular σ. The third holds with a_P=F·σ_P·f^[ρ]. By Prop 4.1, FN holds iff g^ρσ(Y(t))·u^[ρ]=φ_u. So it suffices to find σ∈O³ with
  - (A) σ(Y(t))·u^[ρ]=g^{−ρ}φ_u(t) on ℓ_u, and
  - (B) σ·f^[ρ]∈FO.
- **φ_u is divisible by t^ρ.** By (𝒦) and R23 Prop 2.1(i), ord_tγ_C>=min(ν_u,e_u)>=e_u>=E>X, so t^{−X}γ_C is regular. By R22 Thm 3.1 Step 4, ord s̃_u>=min(ν_u,e_u)=e_u=ord_tF, so s̃_u/F is regular.
- **Coordinates.** Choose local coordinates (x,y) at z(u) with ℓ_u={y=0}, x|_{ℓ_u}=t, and Γ'={y=γ(x)}, ord γ=e_u (Γ' is smooth at z(u), tangent to ℓ_u).
- **The section on ℓ_u.** Solve A·u^[ρ]=g^{−ρ}φ_u and A·ω^[ρ]=t^{−ρ}φ_u (characteristic 2) for A∈k[[t]]³. This is possible because the right sides are regular and the 2×3 coefficient matrix has a unit 2×2 minor. Then A·f^[ρ](t,0)=φ_u+φ_u=0 exactly.
- **Extend off ℓ_u.** Put Φ(x):=f^[ρ](x,γ(x)). Since Φ−f^[ρ](x,0)∈γ·k[[x]]³, A·Φ=O(x^{e_u}). Choose a constant v with v·Φ(0)≠0 (f(z)≠0), and put
      σ := A(x) + y·β(x)v,   β:=−(A·Φ)/(γ·(v·Φ)),
  which is regular. Then σ(x,γ(x))·Φ(x)=0, i.e. (B), and σ(x,0)=A, i.e. (A). ∎

**Corollary 4.3 (negative result for target (a); PROVED).**
- No argument that uses only the C-level data, the twist and FN along a single own line (as an identity of germs at z(u), at any order in t) can exclude (𝒦)∧F²|a_P∧F²|a_R.
- In particular, (★) and R22 Thm 3.1 at order 2X, or at any order, give no condition on a''. R22's Remark 4.4 "HEURISTIC non-determination" becomes PROVED in this local sense.
- Any exclusion must use **global** information on the transverse layer σ: the polynomiality of P across many own lines, or degrees. Cor 2.4 (via Prop 2.2) is such information, and it is what closes n=256.

*Proof.* Prop 4.2 realises every jet allowed by the C-level data at u, with F²|a locally. Prop 4.1(ii) identifies what FN constrains. ∎

*Remarks.*
- **4.4 (toy, COMPUTED).** The toy checks the following, on one line, with random C satisfying (α) and ord γ_C>=X, a first layer with ord s̃>=e, and G̃ solving J^{[X],t}G̃=I:
  - FN ⟺ α_2=0;
  - a random σ violates FN;
  - the constructed σ satisfies FN and σ·f^[ρ]≡0 along the line, and the local P satisfies alignment with a=Fσ·f^[ρ];
  - with ord s̃=e−1, t^{−ρ}φ_u has a pole, so no regular σ exists.

  It tests the algebra of Props 4.1–4.2 on 15 cases (X up to 16, e up to 33). It is not an original model.
- **4.5 (what a global argument must do; HEURISTIC).**
  - Prop 4.1 fixes σ_c·u^[ρ] along every own line ℓ_u, at >0.388q points.
  - a'_c=σ_c·f^[ρ] is a global form of degree M'+Q−T−d'.
  - In (𝒦)∧F²|a, a'_c≡0 on Γ', and Prop 4.1 then forces σ_c(Y(t))·ω^[ρ]≡−t^{−ρ}φ_u mod t^{e_u−ρ}.
  - A global section interpolating these pointwise jets (for instance a polynomial representative of σ modulo Syz(f^[ρ]), i.e. (H_lift) one layer down) would turn them into a count. Whether one exists is the same obstruction as R18-T's (H_lift), at the second layer: OPEN.

---

## 5. What remains, and next steps

**Residual of 𝔇_16 after R24** (global alignment, Q>=128, 256E<=h<4QE, 𝔮_max>=128):
- **Outside (𝒦): closed.** Constant twists by R22 Cor 4.1; non-constant twists ((R1)) by Thm 3.3.
- **(𝒦) with F²∤a: closed** (R22 Cor 4.2, R23 Thm 3.1).
- **(𝒦) with F²|a_P, F²|a_R:** open only for n>=512 with M'+Q−T>=2d' and (a_P,a_R)≢0 (Cor 2.3, 2.4). That is:
  - constant twists: D∈{1,2} on 𝔉_D∩{F|h}∩{F²|a}; D>=4 with 512<=n<4D, so D>=256;
  - non-constant twists ((R2)): r=4 below R20's thresholds at n>=512 (32E/Q at n=512, nE/(16Q) at n>=1024); r=8 below 32E/Q (n=512) and 64E/Q (n=1024), and all 𝔮 at n>=2048; r=16 and r>=32 at all n>=512 (r>=32 wherever R20 does not apply).
- **At n=256, 𝔇_16 is closed** (Cor 2.5).

**Next steps (HEURISTIC).**
1. **Global transverse layer.** Remark 4.5: a polynomial representative of σ modulo Syz(f^[ρ]), the second-layer analogue of (H_lift), would convert Prop 4.1's pointwise jets into a count. Its obstruction is supported on Bs(f)⊂Γ' (R18-T Lemma 2.1A), and so is (H_lift)'s. Bs(f) has three points, so the obstruction might be chargeable rather than fatal.
2. **ord_F det A.** Cor 2.3(ii) gives F^{10}|det A in (𝒦)∧F²|a. Ask PRIMARY whether any original gate (G0–G11, PRIM) or the hyperoval geometry constrains the multiplicity of the inverse curve Γ' in det A.
3. **(R2), n>=512.** Use Cor 2.4's lower bound a>=d'+3(X−ρ) together with the rank-one osculation of Remark 3.5. The obstacle is the Q𝔮 degree factor.

---

## 6. Computations (`scripts/`; `python3 -I`, single process)

| script → output | content | result |
|---|---|---|
| `numerics_R24.py` → `numerics_R24.out` (0.2 s), Part A | all p-adic-closed order sequences, ε_0=0, ε_1=1, length <=4, entries <=2^14 (120; brute-force cross-check on entries <=64: 27=27); r∈{4,…,64}, x∈{1,…,64}; s, Σ', γ' | exact failing set (N_0 an order, γ'<γ, or Σ'/γ'>(2rx+2)/γ) empty; max Σ'/γ'=5, max s/γ'=2, at r=4, x=1, ε=(0,1,4,5) |
| Part B | R22 Thm 5.3(i) bound; Thm 3.3 bound on 3780 cases (1260 rows × admissible 𝔮_max<=S) with per-(r,x) worst ratios; whole-strip upper bound with ratio 5, s/γ'<=2 | corner B_{5.3(i)}=32480243592761/219902325555200 reproduced exactly; exact failing set empty; grid max 0.167228 at (4,128,128,256,128); whole-strip UB 91941792089517/549755813888000≈0.1672411 |
| Part C | Cor 2.4: M'+Q−T>=4E−4 with M'<8nE/625 | infeasible rows at n=256: exact feasible set empty; least feasible n=512 for all 280 (r,Q,S) |
| `det_identity_check.py` → `.out` (13 s) | Prop 2.2 at random points over GF(2^16), for P^t=FK_PJ^{[ρ],t}+f^[X]⊗η_P (the general shape given C and a); (X,ρ)∈{(4,2),(8,2),(8,4),(64,32),(128,64),(4096,64)} | 150/150; layer identity and alignment 150/150; a_P=a_R=0 ⇒ det A=0 150/150; det A≠0 in 150/150; negative control (F³) fails 150/150 |
| `partial_wronskian_check.py` → `.out` (57 s) | Lemma 3.1 on P^1/GF(2^8), V=span(1,t,g,h), orders (0,1,4,8), τ_0=24, with D^{(4)}g forced to vanish at P=7 | deg R_s (finite part) 0, 0, 17, 33 <= bounds 24, 46, 62, 70; per-point inequality: exact failing sets empty for s=1..4; points with vanishing order 5: P∈{7,16}, v_P(R_3)=1; Weierstrass point 30 with j=(0,1,4,9) has v_P(R_3)=0 |
| `local_realization_toy.py` → `.out` (14 s) | Props 4.1–4.2 on one own line over GF(2^8)[[t]] mod t^96; (X,ρ,e)∈{(4,2,9),(8,2,17),(8,4,17),(16,4,33),(16,8,33)}, 3 trials each | 15/15: random σ violates FN and α_2≠0; constructed σ satisfies FN, α_2=0, σ·f^[ρ]≡0, alignment; control ord s̃=e−1 gives the pole; exact failing set empty |

Checksums: `scripts/SHA256SUMS.txt`.

*Caveats.*
- The toys test the algebra of Prop 2.2, Lemma 3.1 and Props 4.1–4.2 on restricted data. They are not original models and say nothing about existence.
- The proofs are by hand from the cited inputs. Thm 3.3 is a strong claim, the closure of all of (R1). It rests on Lemma 3.1 (proved here), on R23 Prop 4.1 / Cor 4.2 / Lemma 4.3, and on the two order facts behind R23 Prop 4.4: ord_uσ_u=N_0 on 𝔅_0, and SV's j_i>=ε_i. The audit should check these first.
- An earlier draft of `partial_wronskian_check.py` had a bug: in-place `+=` on shared galois 0-d arrays corrupted the zero element. The bug was found and fixed before the recorded run, and is documented in the script.

---

## 7. Status

| item | status |
|---|---|
| Lemma 2.1 (transverse layer σ; a'=σ·f^[ρ]; F²\|a ⟺ second-order lift) | PROVED |
| Prop 2.2 (det A=κ_0^{−(Q+T)}F⁴det𝒞_Aλ_A) | PROVED; COMPUTED (150/150, control fails) |
| Cor 2.3 (G5 ⟺ FNAM2 ∧ (a_P,a_R)≢0; ord_F det A=4+2k_Δ+2min ord_F a) | PROVED |
| Cor 2.4 (F²\|a ⇒ M'+Q−T>=2d' ⇒ n>=512) | PROVED; COMPUTED Part C |
| Cor 2.5 (𝔇_16 excluded at n=256; R23 Remark 3.4 resolved) | PROVED (assembly of R20, R22, R23 and this note) |
| Lemma 3.1 (partial Wronskian divisor) | PROVED; COMPUTED check |
| Lemma 3.2 (Σ'/γ'<=5, s/γ'<=2) | PROVED from R23 Lemma 4.3; COMPUTED Part A |
| Thm 3.3 ((R1) excluded, every 𝔮_max, every scale; <=0.167242q) | PROVED (inputs as listed); numbers COMPUTED, whole strip by monotonicity |
| Remark 3.5 (no transfer to (R2) via Lemma 3.1) | PROVED (negative); rank-one osculation route HEURISTIC |
| Prop 4.1 (FN on ℓ_u ⟺ (α) ∧ (4.1); a enters only mod t^ρ) | PROVED |
| Prop 4.2 (local realisability of (𝒦)∧F²\|a at one own line) | PROVED; COMPUTED toy |
| Cor 4.3 (no single-point argument excludes (𝒦)∧F²\|a) | PROVED (negative) |
| Remark 4.5, §5 next steps (global σ, ord_F det A, (R2) osculation) | HEURISTIC / OPEN |
| (𝒦)∧F²\|a_P∧F²\|a_R at n>=512 (constant and non-constant, rows of §5) | OPEN |

Dependencies: R23, R22, R21, R20, R19, R18-T, R16 (all v2.1, audited and revision-checked); PRIMARY FNAL/TSY/TSYC/FNAM (reviewed); Stöhr–Voloch (CITED). PRIMARY's results remain PRIMARY's. FNAM2's implication G5⇒Δ≢0 is PRIMARY's; Prop 2.2 makes it exact. R23's reduction of (R1) to 𝔅_0 (Prop 4.1, Cor 4.2, Prop 4.4) is the input that Thm 3.3 completes. This v1 is unaudited. No manuscript was edited. The classification of hyperovals is not claimed complete: 𝔇_16 at n>=512 (§5), 𝔇_17, and the non-global-alignment variant remain.
