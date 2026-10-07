# HYP M>=2, round 23 (owner v2): in (𝒦) the twist vanishes to order E at its own point — F²∤a is excluded for every twist; 𝔅_0 is the support of 𝔡 and lies in the Weierstrass locus of the twist

7 October 2026. Claude HYP(2) owner research note (R23), following R22 v2.1.

**Version history.**
- v1: owner draft (`HYP_M2_ROUND23_owner_v1.md`, kept unchanged).
- v1 independently audited (`AUDIT_HYP_M2_ROUND23_20261007.md`): **PASS-with-fixes**. No mathematical error was found in any headline result (Prop 2.1 including the divisibility lift (ii), Cor 2.2, Prop 2.3, Thm 3.1, Prop 3.2, Cor 3.3, Prop 4.1, Cor 4.2, Lemma 4.3, Prop 4.4, Cor 4.5). Fixes FIX-1..5 and minor notes N1–N6 were raised.
- **v2 (this file)** applies FIX-1..5 and N1–N6, marked "[v2: FIX-n]" / "[v2: Nn]". No closure is withdrawn and no headline number changes.
  - FIX-1 corrects a false COMPUTED reading of the r=16, n=256 diagnostics: the two bounds fail on τ_0-intervals of length ~58 000, not on one value. The r=16 threshold 8E/Q is unchanged.
  - FIX-2 re-attributes Cor 3.3: its gain already follows from R22 Cor 3.2 fed into R20's order step; the bootstrap Prop 2.1(ii) is needed for Thm 3.1 (and for Cor 5.2's edge case), not for Cor 3.3.
  - FIX-3 withdraws the overclaim "makes R22 Prop 5.5's (R1) part unconditional" and marks the classical / dim V=2 closures as already in R22.
  - FIX-4 corrects "the R20 'none' rows close only vacuously".
  - FIX-5 corrects the citation for Cor 5.2's edge case.
  - The script is fixed in a new copy `scripts/numerics_R23_v2.py` → `numerics_R23_v2.out` (exact failing sets; mode "R22only"; τ_hi at the least closing 𝔮). Its Parts A, C, D are byte-identical to v1's output; v1's script and output are kept.

**Targets (coordinator):**
- (a) use R22's identity (★) and Thm 3.1 beyond order X against 𝔉_D∩{F|h}∩{F²|a} and the constant D>=4 (𝒦)-lanes with n<4D;
- (b) apply (★)/Thm 3.1 to non-constant twists in (𝒦), i.e. (R2);
- (c) shrink 𝔅_0 in (R1);
- (d) precise negative results where stuck.

I took (b) first, then (c), then (a).

**Inputs (read, not re-proved; copies in `inputs/`):**
- R22 v2.1. Used: §1 (good u, local first layer), Lemma 2.1, Lemma 2.2 (e_u∈{E,E+1}), Lemma 2.4, Thm 3.1 (i)–(iii) and its Step 4, Cor 3.2, Cor 4.2, Lemma 5.1, Lemma 5.2, Thm 5.3, Cor 5.4, Prop 5.5, and the 𝔮 conventions (statements hold for every admissible 𝔮; Prop 5.5 needs 𝔮_max).
- R21 v2.1. Used: Lemma 3.1 (V_u|_{ℓ_u}=η_u(c^[T])^⊥), Lemma 3.2 (𝔡, (𝒦_ψ), deg 𝔡²), Cor 3.3 (V_u(z(u))=κ_u𝔡(u)), Remark 3.4.
- R20 v2.1. Used: Lemma 4.1 (order transfer), Lemma 4.2, Lemma 4.3 (𝔅), Thm 5.1 ((4.1′)), Prop 5.2 (N4), Cor 5.3 (normalisation and table), Prop 3.1.
- R19 v2.1. Used: Lemma 3.0, Lemma 3.1, Lemma 3.5(i),(iii), Thm 4.1 / (4.1).
- R18-T v2.1. Used: §1 (normalisation T=T̂^[𝔮]), Lemma 1.2, Lemma 2.1(ii), Prop 4.1(iii), Prop 4.2.
- R16 v2.1. Used: R16.1 (FN on the whole own line), R14.1 (ψ∉K²), the standing count N_good>(1551/4000)q+1.
- PRIMARY FNAL, TSY, TSYC, FNAM (FNAM1/2/3), as reviewed. All PRIMARY results remain PRIMARY's.
- Stöhr–Voloch, *Weierstrass points and curves over finite fields*, Proc. LMS 52 (1986): Thm 1.5 (j_i(P)>=ε_i; v_P(R)>=Σ(j_i(P)−ε_i); deg R=(Σε_i)(2g−2)+(r+1)deg 𝒟) and Cor 1.9 (p-adic criterion: if ε is an order and binom(ε,μ)≢0 mod p, then μ is an order). CITED.

**Labels (as in R18-T–R22):**
- PROVED: complete proof here, conditional only on the named inputs.
- CONDITIONAL: proved under a named hypothesis that is not established.
- COMPUTED: exact computation; it proves only where an exact bound is evaluated.
- HEURISTIC / OPEN / CITED: as stated.

**Rules followed.**
- No file whose name contains "DZ" was opened. (The PRIMARY TSY/TSYC copies mention DZ only in credit lines.)
- No PRIMARY/Codex script was executed; only `.md` files were read.
- Own scripts only: `scripts/numerics_R23.py` (v1, 6 s) and its corrected copy `scripts/numerics_R23_v2.py` (v2, 10 s), run with `python3 -I`, single process.

**Notation** is that of R22 (and R18-T–R21):
- q=Eh, E=rQS, ρ=Q/2, X=T/2=ρS, n=h/E; d=deg Γ<=E+2; d'=deg Γ'∈[2E−2,2E+4]; a=deg C_•=M'+X−ρ−d'; a'_•=a_•/F of degree M'+Q−T−d'.
- r, Q, S, 𝔮 are powers of 2 with r>=4, Q>=128, S>=64, 𝔮_max>=128.
- Good u, c=c(u)=(√β:√α)(u), b=gD·c^[2] (so b^[ρ]=(gD)^ρc^[Q]), Y(t)=z+tV, V_u(Y)=C_{c(u)}(Y)c(u)^[Q], e_u=ord_tF(Y(t)), ν_u=ord_{v=u}c(u)^t𝒜(v)c(u)^[Q], s̃_u, 𝔅_0={good u: e_u=E, ν_u=E−X}: all as in R22.
- (𝒦): 𝒞_cB c=0 in K² for every c∈k², with 𝒞_c=C_c(z) formed with the morphism z (R20). If F|(C_P,C_R) this holds for the unreduced pencil whenever it holds for the reduced one; everything below uses only the unreduced statement.
- **New:**
  - ε(t):=t^X s̃_u(t)/F(Y(t))∈k[[t]] (R22 Thm 3.1(i)), the "singular term" of Thm 3.1(ii).
  - W_u(Y):=P_{c(u)}(Y)^t u^[ρ], a vector of forms of degree M'. FN (R16.1) says W_u(Y(t))=μ'_u(t)·u^[X] with μ'_u∈k[t].
  - V:=span(t̂_ij)⊂H⁰(𝓣) for 𝔮=𝔮_max, of dimension r_V+1<=4, base-point-free, with orders ε_0<…<ε_{r_V}; R_V its Stöhr–Voloch ramification divisor; W(V):={P: (j_i(P))≠(ε_i)} its Weierstrass points.
  - N_0:=(2r−1)S/𝔮_max (an integer when 𝔮_max<=S), γ:=(r−1)S/𝔮_max−1, N_1:=⌈E/(ρ𝔮)⌉.

---

## 0. Summary

**The idea.** R22 proved two facts at every good point: Ξ(u,·) vanishes at u to order >=E−X (Cor 3.2), and the second layer obeys the congruence C_cb^[ρ]≡κ_0^X(t^{X−ρ}a'_c+ε)Ωb^[X] (mod t^X) (Thm 3.1(ii)). In the kernel-aligned case (𝒦) the second layer factors through Ξ along Γ: V_u(z(y))=p(y)·det(B(y)c,c^[Q]). So the first fact makes the left side of the congruence vanish mod t^X. Then the singular term ε, whose order is X+ν_u−e_u, must be absorbed by t^{X−ρ}a'_c. This forces ν_u>=e_u−ρ, and divisibility of ν_u by ρ𝔮 lifts it to ν_u>=E. This bootstrap is what Thm 3.1 needs (through Cor 2.2(i)). [v2: FIX-2] The (R2) gain of Cor 3.3 does not need it: it already follows from R22 Cor 3.2 (ν_u>=E−X) fed into R20 Lemma 4.2's order step, which gives m>=E−X for every 𝔮. R22 §6 item 3 compared only Thm 3.1(iii)'s bound with R20's m, and R22 Remark 5.6 applied Cor 3.2 only to the residual count ("not recomputed"); so that input was missed.

**PROVED.**
1. **The twist vanishes to order E at its own point in (𝒦) (Prop 2.1).** In (𝒦), for every twist and every good u, ν_u>=E. Equivalently, ord_uσ_u>=E/(ρ𝔮) for every admissible 𝔮<=2rS. Moreover ord_tε>=X−1, and ord_tε>=X when e_u=E.
2. **a' vanishes at every own point in (𝒦) (Cor 2.2).** In (𝒦), for every twist and every good u, a'_{c(u)} vanishes along ℓ_u at z(u) to order >=ρ−1 (>=ρ if e_u=E). If moreover F²|a_P and F²|a_R, then ν_u>=e_u.
3. **Exact own-line identity for W (Prop 2.3).** At every good u, any twist, μ'_u(t)b^[X]=κ_0^{−X}g^{X−ρ}t^{ρ−X}F(Y(t))ΩC_c(Y(t))b^[ρ] identically in t. Hence ord_tμ'_u=e_u+ρ−X+ord_t(V_u|_{ℓ_u}).
4. **(𝒦) with F²∤a is excluded for every twist (Thm 3.1).** For any twist, constant or not, any D and 𝔮, at every strip scale: if (𝒦) holds and F²∤a_P or F²∤a_R, then
      N_good <= Nd + 2deg[T]/𝔮 + (1.5d²+3.5d+1) + 6d_def + 7 + deg ψ + 2(M'+Q−T−d')d' <= 0.092579q.
   - So **(R2) reduces to (𝒦)∧F²|a_P∧F²|a_R**, the same condition that R22 Cor 4.2 left for constant twists. This holds for every r, n and 𝔮, including r=16 with n>=512 and r=8 with n>=2048.
5. **R20/R19 with m=E (Prop 3.2, Cor 3.3).** In (𝒦), R20 Lemma 4.2 and Thm 5.1 hold with m=E for every 𝔮, and R19 Lemma 3.5(iii) holds with τ_0−N_1. [v2: FIX-2] For every number in Cor 3.3, m>=E−X (R22 Cor 3.2) already suffices; the mode "R22only" reproduces the same closures on all 162 rows and 112/112 B2 cases.
   - Recount (COMPUTED, exact): non-constant (𝒦) at **n=256 is excluded for r∈{4,8} and every 𝔮>=128**. This was checked on 112 (r,Q,S) cases, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12}.
   - All other R20 thresholds are unchanged. The re-implementation reproduces the R20 v2.1 table exactly in R20 mode.
6. **𝔅_0 is the support of 𝔡 (Prop 4.1).** For good u [v2: N1: the v1 hypothesis S>=128 is superfluous]: u∈𝔅_0 ⟺ 𝔡(u)≠0. On 𝔅_0, 𝔡(u) has an explicit formula: the ratio of the leading coefficients of s̃_u (order E−X) and F|_{ℓ_u} (order E).
7. **(𝒦_ψ)∖(𝒦) is excluded for every 𝔮 (Cor 4.2).** This removes R22 Cor 5.4's 0.283q threshold. Also, (R1) with 𝔮_max<=S forces 𝔡≢0 and |𝔅_0|>0.240046q.
8. **𝔅_0 lies in the Weierstrass locus of the twist (Lemma 4.3, Prop 4.4; uses CITED Stöhr–Voloch).** By the p-adic criterion, N_0=(2r−1)S/𝔮_max (three or more binary ones, since r>=4) is never an order of V. Hence every u∈𝔅_0 is a Weierstrass point of V with v_u(R_V)>=γ=(r−1)S/𝔮_max−1>=2.
9. **(R1) closes for every V with small order sum (Cor 4.5).** (R1) is excluded unless 𝔮_max<=S and Σε_i(V)>Σ*, where Σ*>=0.238γn. In particular (R1) is excluded:
   - for every classical V and for dim V=2 (already in R22: Prop 5.5's classical/pencil cases with Thm 5.3) [v2: FIX-3];
   - for every V with ε_top<N_0, with no count hypothesis: Lemma 4.3(iii) makes the weight N_0−ε_top>=γ>=2 uniform. [v2: FIX-3] v1 said this "makes R22 Prop 5.5's (R1) part unconditional and removes its 𝔮_max<(2r−1)S/3 restriction". That overclaims: the hypothesis ε_top<N_0 on V remains, and the 𝔮_max restriction is vacuous in (R1) (𝔮_max<=S gives N_0>=7);
   - for every non-classical V with ε_top<=0.119γn.

**Precise negative results (target (a)).**
10. **Prop 2.1 is empty for constant twists, where ν_u=∞.** R22 Cor 4.2 is unchanged, and nothing new is proved for 𝔉_D∩{F|h}∩{F²|a} or for the constant D>=4 lanes with n<4D.
11. **The line-zero count for W_u is vacuous in (𝒦) (Cor 5.2).** Prop 2.3's high-order zero of W_u on ℓ_u (order >=2E+ρ−X in (𝒦)) cannot force W_u|_{ℓ_u}≡0 by counting zeros, even granting a zero at every residual point. That would need a<E, which (𝒦) excludes (R20 Prop 3.1, R18-T Prop 4.2) except at R18-T's edge case.

**COMPUTED** (`scripts/numerics_R23.out`, exact Fractions, 6 s):
- Thm 3.1 bound: the whole-strip supremum is the corner value 101790647887837/1099511627776000≈0.0925781. Each term is monotone; the exact grid maximum over 1260 rows is 0.08263.
- R20 Cor 5.3 re-implemented. Mode "R20" reproduces every entry of the R20 v2.1 table: 162 (r,n,Q,S) rows. [v2: FIX-4] In the "none" rows the least closing 𝔮 is huge, with τ_hi∈{1,2,6,12} there (v1 wrongly said "only vacuously, at τ_hi<1"). Mode "R23" closes n=256 for r∈{4,8} at every 𝔮; mode "R22only" (m>=E−X, N_1=1) gives exactly the same closures [v2: FIX-2].
- p-adic order sequences (dim<=4): 443 sequences enumerated. None contains (2r−1)2^k for r>=4. The minimal γ is >=(r−1)2^k−1 in every case.
- (R1) threshold Σ*: the minimum of Σ*/n over the grid is 0.4766, at r=4, 𝔮_max=S, γ=2.

**What failed / what remains.**
- **(a)** (𝒦)∧F²|a_P∧F²|a_R remains OPEN, for constant twists (𝔉_D∩{F|h}∩{F²|a}, D∈{1,2}; D>=4 with n<4D) and now also as the **only** residual of (R2). Thm 3.1 shows that the two residuals now share this hypothesis.
- **(R2) below R20's thresholds under F²|a.** The m=E recount does not move n>=512, or r=16 at n=256. There 𝔮<8E/Q stays open. [v2: FIX-1] At 𝔮=4E/Q (Q=128, S=64) both bounds fail on τ_0∈[5473,63625] (d'=2E−2; [5501,63607] for d'=2E+4), and at 𝔮=128 on [1528,2036040]. v1's "miss by a single value of τ_0" was a misreading of the script, which printed only failing test points.
- **(R1).** Only non-classical V [v2: N4: v1 said "Frobenius non-classical"; the order sequence ε_i of V is meant] of dimension 3 or 4 with Σε_i>Σ*>=0.238γn remains. That means ε_top>0.119γn>=60 and 𝔮_max<=S, with more than 0.24q Weierstrass points of V among the good points.

**Newly closed (PROVED; numbers COMPUTED; v1 audited PASS-with-fixes, no closure withdrawn):**
- every (𝒦)-model, constant or not, with F²∤a_P or F²∤a_R: all r, n, D, 𝔮. In particular this is all of (R2) outside F²|a, including r=16 with n>=512 and r=8 with n>=2048;
- non-constant (𝒦) at n=256 for r∈{4,8}, all 𝔮>=128 (grid-COMPUTED, as R20's table; [v2: FIX-2] the input is R22 Cor 3.2 fed into R20's order step);
- (𝒦_ψ)∖(𝒦) for every 𝔮;
- (R1) for every twist whose V has ε_top<N_0 (no count hypothesis) or Σε_i<=0.238γn. This includes every V with ε_top<=0.119γn. [v2: FIX-3] Classical V and dim V=2 were already closed in R22.

---

## 1. Setting

The standing hypotheses are those of R22 §1: 𝔇_16, global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮_max>=128. A good u is as in R22 §1. It is off:
- the boundary (6d_def+7; this contains Bs(e));
- 𝔈 (<=1.5d²+3.5d+1; this contains {g=0});
- {λ'=0} (<=Nd);
- {det T̂=0} (<=2deg[T]/𝔮, empty for a constant twist).

At a good u:
- Γ is smooth and z is a local isomorphism onto the smooth point z(u)∈Γ';
- ℓ_u is the tangent there, with contact e_u∈{E,E+1} (R22 Lemma 2.2);
- c^[Q]=κ_uB(u)c with κ_u≠0;
- D(u)≠0 for the generic c_0;
- B(u) is invertible.

The base points of f lie on Γ' (R18-T Lemma 2.1A), but never at z(u) for good u. Nothing below evaluates a local splitting at a base point.

[v2: N2] **Γ' is smooth at z(u).** f∘z equals the normalisation map Γ̃→Γ off z^{−1}(Bs f), and z(u)∉Bs f since f(z(u))=g(u)u≠0. So z(v)=z(u) forces v↦u in Γ, and Γ is smooth at u, so z^{−1}(z(u))={u} and z is unramified there. This is used in Prop 2.1 Step 2 and Cor 2.2(ii); the singular-branch pitfall does not arise.

**Admissible 𝔮.** T∈GL_2(K^{𝔮_max}) projectively, so every dyadic 𝔮<=𝔮_max is admissible, with T̂_𝔮=T̂_{𝔮_max}^{[𝔮_max/𝔮]}. For each admissible 𝔮, Ξ(u,·)=σ_u^{ρ𝔮} with σ_u∈H⁰(𝓣_𝔮) (R19 Lemma 3.5(i)). Hence

      ν_u ∈ ρ𝔮·Z_{>=1} ∪ {∞}   for every admissible 𝔮   (σ_u(u)=0, R18-T Lemma 1.2).     (1.1)

In particular (1.1) holds for 𝔮=128, and 128 | 2rS since r>=4, S>=64. [v2: N1] Any admissible 𝔮>=2 would serve in Prop 2.1 Step 5 (audit toy B); 128 is a choice, not a need.

---

## 2. The kernel-aligned case: the own-point order of the twist

**Proposition 2.1 (in (𝒦), ν_u>=E; PROVED, conditional on R22 Thm 3.1, Cor 3.2 and Lemma 2.2, R20 Lemma 4.1, R19 Lemma 3.0/3.5(i)).** Assume (𝒦), with any twist. Let u be good and c=c(u). Then:
- (i) along Γ near u, V_u(z(y))=p(y)·c^t𝒜(y)c^[Q] with p regular at u. Hence ord_{y=u}V_u(z(y))>=ν_u and ord_t(V_u|_{ℓ_u})>=min(ν_u,e_u);
- (ii) ν_u>=E. Equivalently, ord_uσ_u>=E/(ρ𝔮) for every admissible 𝔮 with 𝔮 | 2rS (σ_u≢0);
- (iii) ord_tε>=X+E−e_u>=X−1, and ε≡0 (mod t^X) when e_u=E.

*Proof.*
- **Step 1: factorisation along Γ.** Work in local frames at u: z^*O(a) for 𝒞_c, and 𝓣^{ρ𝔮} for B.
  - By (𝒦), 𝒞_c(y)β(y)=0 for y near u, where β(y):=B(y)c is regular and β(u)≠0, since B(u) is invertible and c≠0.
  - Each row m(y) of 𝒞_c(y) satisfies m·β=0. In characteristic two this means m=p_i·β^⊥ with β^⊥=Ωβ. If β_1(u)≠0, then p_i=m_2/β_1 is regular near u; symmetrically if β_2(u)≠0.
  - So 𝒞_c(y)=p(y)⊗β(y)^⊥ with p regular at u (possibly p=0). This is the pointwise form of R19 Lemma 3.1; no reduction of (C_P,C_R) is needed.
  - Then V_u(z(y))=𝒞_c(y)c^[Q]=p(y)(β(y)^⊥·c^[Q])=p(y)det(B(y)c,c^[Q])=p(y)c^t𝒜(y)c^[Q] (R19 Lemma 3.0). Its order at y=u is >=ν_u.
- **Step 2: the own line.** z is non-cuspidal at u. R20 Lemma 4.1 (in its sharp form, order >=min(N,j(u)), with j(u)=e_u at a smooth point of Γ') gives ord_t(V_u|_{ℓ_u})>=min(ν_u,e_u) in the linear parameter t of Y(t)=z+tV. This proves (i).
- **Step 3: the congruence becomes homogeneous.** By R22 Cor 3.2, ν_u>=E−X (or ν_u=∞). Also e_u>=E. So min(ν_u,e_u)>=E−X=(2r−1)X>=X, and C_c(Y(t))b^[ρ]=(gD)^ρV_u(Y(t))≡0 (mod t^X). R22 Thm 3.1(ii) gives, since κ_0≠0 and Ωb^[X] is a nonzero constant vector,
      t^{X−ρ}a'_c(Y(t)) + ε(t) ≡ 0   (mod t^X).          (2.1)
- **Step 4: the singular term must be absorbed.** Suppose ν_u<e_u.
  - By R22 Thm 3.1 Step 4, ord_ts̃_u=ν_u. Also ord_tF(Y(t))=e_u, so ord_tε=X+ν_u−e_u<X.
  - The other term of (2.1) has order >=X−ρ, because a'_c(Y(t))∈k[t].
  - So (2.1) forces X+ν_u−e_u>=X−ρ, i.e. ν_u>=e_u−ρ>=E−ρ.
- **Step 5: divisibility.** Take 𝔮=128 in (1.1). Then ν_u is a positive multiple of 128ρ, and 128ρ divides E=2rρS. There is no multiple of 128ρ in [E−ρ,E), since 128ρ>ρ. Hence ν_u>=E.
  - If ν_u>=e_u, then ν_u>=e_u>=E directly. This proves (ii); the 𝔮-form follows from ν_u=ρ𝔮·ord_uσ_u.
- **Step 6: (iii).** R22 Thm 3.1 Step 4 gives ord_ts̃_u>=min(ν_u,e_u)>=E. So ord_tε>=X+E−e_u. This is >=X−1 by Lemma 2.2, and >=X if e_u=E. ∎

*Remarks.*
- **Consistency.** (i) refines R18-T Prop 4.1(iii) (flatness to order min(ρ𝔮,E)) to order min(ν_u,e_u)>=E. It is consistent with R22 Thm 3.1(iii): in (𝒦) the order E>=X−ρ is reached through (i), not through δ_u.
- **What R22 §6 item 3 missed (PROVED comparison).** R22 compared the order bound min(X−ρ,ρ𝔮−1) of Thm 3.1(iii) with R20's m=min(ρ𝔮,E), and that comparison is correct. But in (𝒦), R20's own order step "ord_{y=u}ω^tV_u(z(y))>=ord Ξ(u,·)" combined with R22 Cor 3.2 already gives m>=E−X for every 𝔮. The bootstrap of Steps 3–5 raises this to m>=E. [v2: FIX-2] The miss that matters for (R2) is the E−X input: it alone gives every closure of Cor 3.3 (audit `variant_modes.out`; mode "R22only" of `numerics_R23_v2.out`). The raise to E is used by Thm 3.1 (via Cor 2.2(i)) and by Cor 5.2's edge case, not by Cor 3.3.
- **Not specific to (𝒦).** Steps 3–5 use (𝒦) only through ord_t(V_u|_{ℓ_u})>=X. At any good u where V_u|_{ℓ_u} has order >=X (any twist, any branch), the same argument gives ν_u>=E.

**Corollary 2.2 (a' vanishes at every own point in (𝒦); PROVED).** Assume (𝒦), with any twist, and let u be good, c=c(u).
- (i) a'_c(Y(t))≡0 (mod t^{ρ−1}), and mod t^ρ if e_u=E. In particular a'_{c(u)}(z(u))=0.
- (ii) a'_{c(u)} vanishes on Γ' at z(u) to order >=ρ−1.
- (iii) If F²|a_P and F²|a_R, then ν_u>=e_u.

*Proof.*
- **(i)** By (2.1) and Prop 2.1(iii), t^{X−ρ}a'_c≡−ε≡0 (mod t^{X−1}), and mod t^X if e_u=E. Divide by t^{X−ρ}. Since ρ>=64, ρ−1>=1.
- **(ii)** Graph argument (R22 Thm 3.1 Step 4) with ρ−1<E<=e_u.
- **(iii)** Now a'_c=F·a''_c, so t^{X−ρ}a'_c has order >=X−ρ+e_u>=X, and (2.1) gives ε≡0 (mod t^X). If ν_u<e_u, then ord_tε=X+ν_u−e_u<X, a contradiction. ∎

For a constant twist, (i) is R22 Cor 4.2's first step (there s̃_u≡0). The point of Cor 2.2 is that the non-constant layer s̃_u can no longer obstruct it.

**Proposition 2.3 (exact own-line identity for W_u; PROVED from R16.1, R22 Lemma 2.1(i), R18-T Lemma 2.1(ii)).** At every good u, with any twist and c=c(u), as polynomials (resp. Laurent polynomials) in t:
      μ'_u(t)·b^[X] = κ_0^{−X} g^{X−ρ} t^{ρ−X} F(Y(t))·ΩC_c(Y(t))b^[ρ].          (2.2)
Consequently:
- ΩC_c(Y(t))b^[ρ] is everywhere parallel to the constant vector b^[X];
- ord_tμ'_u=e_u+ρ−X+ord_t(V_u|_{ℓ_u});
- W_u|_{ℓ_u}=μ'_uu^[X] vanishes at z(u) to exactly that order. In (𝒦) this is >=e_u+ρ−X+E>=2E+ρ−X (Prop 2.1(i),(ii)).

*Proof.*
- **FN.** By R16.1, W_u(Y(t))×u^[X]=0. Since u^[X] is a nonzero constant vector and W_u(Y(t)) is a polynomial vector, W_u(Y(t))=μ'_u(t)u^[X] with μ'_u∈k[t].
- **Apply J^{[X],t}(Y(t)) to both sides.**
  - On the right, J^{[X],t}u^[X]=(J(Y(t))^tu)^[X]=(t/g)^Xb^[X] (Frobenius is additive; R22 Lemma 2.1(i)).
  - On the left, R18-T Lemma 2.1(ii) gives J^{[X],t}P_c^t=κ_0^{−X}F·ΩC_cJ^{[ρ],t}. Hence J^{[X],t}W_u=κ_0^{−X}FΩC_c(J^tu)^[ρ]=κ_0^{−X}FΩC_c(t/g)^ρb^[ρ].
- **Compare** and multiply by g^Xt^{−X}. Choose i with b_i≠0 for the order statement. ∎

*Remarks.*
- (2.2) is a one-line form of R22 Remark 4.4's (α)/(β) and of the audit's exact form (R22 N2). It shows that the whole span(f^[X])-component of FN (FNAL §4) is the scalar μ'_u. Its order is fixed by the second layer.
- R22 Remark 4.5 is the special case "(𝒦), constant twist, F²|a".

---

## 3. Consequences for (R2)

**Theorem 3.1 ((𝒦) with F²∤a is excluded for every twist; PROVED, conditional on Cor 2.2, R14.1, R18 §5; numbers COMPUTED).** Assume (𝒦) in 𝔇_16 (strip as in §1), with any twist (constant or not), any D and any 𝔮_max>=128. If F²∤a_P or F²∤a_R, then
      N_good <= Nd + 2deg[T]/𝔮 + (1.5d²+3.5d+1) + 6d_def + 7 + deg ψ + 2(M'+Q−T−d')d',
whose value over q is <=101790647887837/1099511627776000<0.092579 on the whole strip. So the model is excluded.

*Proof.*
- **The section.** Let α̃, β̃ be sections of 𝓐 (deg 𝓐=deg ψ) without common zero, with (α:β)=(α̃:β̃), and put A:=a'_P∘z and B':=a'_R∘z, sections of z^*O(m_a) with m_a:=M'+Q−T−d'. Define
      𝔞 := β̃·A² + α̃·B'² ∈ H⁰(𝓐⊗z^*O(2m_a)),   deg 𝔞 = deg ψ + 2m_a d'.
  (If m_a<0, then a'=0 and F²|a holds trivially.)
- **𝔞 vanishes at every good point.** At a good u, c(u)=(√β̃:√α̃)(u). In characteristic two, 𝔞(u)=(√β̃(u)A(u)+√α̃(u)B'(u))², which is a nonzero constant times a'_{c(u)}(z(u))². This is 0 by Cor 2.2(i). This includes the points with β(u)=0 or α(u)=0, where c=(0:1) or (1:0).
- **Case 𝔞≢0.** The good points are among its zeros, so they number at most deg 𝔞.
- **Case 𝔞≡0.** Divide by β̃ (β̃≢0, since ψ is non-constant): A²+ψB'²=0 in K.
  - If B'≠0, then ψ=(A/B')²∈K², contradicting R14.1. So B'=0, and then A=0.
  - So a'_P and a'_R vanish on Γ', and F|a'_P, F|a'_R (F prime). That is F²|a_P and F²|a_R, contrary to the hypothesis.
- **Exceptional sets.** {λ'=0}<=Nd; {det T̂=0}<=2deg[T]/𝔮 (0 for a constant twist); 𝔈<=1.5d²+3.5d+1; the boundary <=6d_def+7.
- **Numerics.** Use N<16h/625, M'<8h/625, d=E+2, d'<=2E+4, deg ψ<=(E+1)d, deg[T]<=Nd/ρ+d with 𝔮>=128, and d_def<=q/1000. Drop the negative part (Q−T−d')d'<0. Then bound/q is at most
      (16/625)(1+2/E) + (32/625)(1+2/E)/(128ρ) + 2(E+2)/(128q) + (1.5d²+3.5d+1)/q + (E+1)(E+2)/q + (32/625)(1+2/E) + 6/1000 + 7/q.
  - Every term is non-increasing in r, Q, S and n (E=rQS, q=nE², ρ=Q/2). So the supremum over the strip (r>=4, Q>=128, S>=64, n>=256) is the corner value at (4,128,64,256): 101790647887837/1099511627776000≈0.0925781<1551/4000.
  - The exact bound, maximised over d'∈[2E−2,2E+4], was evaluated on the 1260-row grid of R22 (`numerics_R23.out` Part A). Its maximum is 0.08263, and every row lies below the displayed upper bound. ∎

*Remarks on scope.*
- (1) For constant twists, Thm 3.1 re-proves R22 Cor 4.2 by a different count (one section over all slopes instead of one form per slope). The value 0.092578 is slightly below R22's 0.092972.
- (2) For non-constant twists it is new. It uses no τ_0-range, no D, no 𝔮-threshold, no line-restriction bound and no Ξ-residual count. So it covers the R20-"none" rows: r=8 with n>=2048, r=16 with n>=512, and every 𝔮 below R20's thresholds, **unless F²|a_P and F²|a_R**.
- (3) F²|a is not a C-level condition (R22 Prop 4.3, FIX-2): the modification P^t↦P^t+F·f^[X]⊗ξ changes a' by ξ·f^[ρ]. So Thm 3.1 is a genuine condition on original data, not on (C, twist).

**Proposition 3.2 (R19/R20 per-point inputs in (𝒦) with m=E; PROVED, conditional on Prop 2.1 and the cited R19/R20 statements; [v2: FIX-2] the weaker form with m=E−X needs only R22 Cor 3.2 in place of Prop 2.1).** Assume (𝒦) with a non-constant twist (R19's reduced pencil, as in R20). Then:
- (i) R20 Lemma 4.2 holds with m:=E for every 𝔮. For good, non-cuspidal u∉𝔅, N_Ξ(u)<=a−E+mb(u).
- (ii) R20 Thm 5.1 / (4.1′) holds with m=E, i.e. with D_1=d'−a, for every 𝔮.
- (iii) R19 Lemma 3.5(iii) holds with τ_0−N_1 in place of τ_0−1, where N_1=⌈E/(ρ𝔮)⌉ for an admissible 𝔮 (σ_u≢0). So R19 (4.1) (with R20's N4 form) holds with the factor d'−E−τ_0+N_1, for τ_0<=d'−E+N_1−1.

*Proof.*
- **(i)** In R20 Lemma 4.2's "order at z(u)" step, ω^tV_u(z(y))=κ_u(ω·p(y))Ξ(u,y) for the reduced pencil, with p regular. Its order at y=u is >=ord_{y=u}Ξ(u,y)=ν_u>=E (Prop 2.1(ii), applied to the unreduced pencil; ν_u depends only on the twist and c(u)). R20 Lemma 4.1 then gives order >=min(ν_u,j(u))>=E on ℓ_u. The rest of the proof is unchanged.
- **(ii)** R20 Thm 5.1 uses m only through Lemma 4.2.
- **(iii)** deg σ_u=τ_0, and σ_u has a zero of order ν_u/(ρ𝔮)>=E/(ρ𝔮) at u.
- [v2: FIX-2] **Weaker form.** Replacing Prop 2.1(ii) by R22 Cor 3.2 (ν_u>=E−X) in (i) gives m>=E−X for every 𝔮 and D_1>=d'−a−X in (ii). Every closure of Cor 3.3 already holds with this weaker form. ∎

**Corollary 3.3 (recount of R20 Cor 5.3; COMPUTED exactly, `numerics_R23.out` Parts B, B2; failing sets and mode "R22only" in `numerics_R23_v2.out` [v2: FIX-1, FIX-2]).**
- **Normalisation and test.** These are R20 Cor 5.3's: every d'∈[2E−2,2E+4], 2g−2<=d²−3d, a<=8h/625−d'+X−ρ, N<16h/625, d_def<=q/1000, deg ψ<=(E+1)d, and τ_0∈[1,τ_hi] with τ_hi=⌊min(ad'/(ρ𝔮),(Nd/ρ+d)/𝔮)⌋.
  - A 𝔮 closes if every integer τ_0 in [1,τ_hi] satisfies (4.1)-N4 or (4.1′).
  - (4.1′) is affine in τ_0. The N4 test is a concave quadratic in τ_0 after clearing the denominator. It was checked at the endpoints and the vertex, with exact Fractions.
- **Self-check.** Mode "R20" (m=min(ρ𝔮,E), N_1=1) reproduces every entry of the R20 v2.1 table on its grid (r∈{4,8,16}, Q∈{128,…,4096,16384}, S∈{64,256}, n<=8192; 162 rows):
  - 2E/Q (r=4, 8 at n=256);
  - 32E/Q (n=512);
  - nE/(16Q) (r=4, n>=1024);
  - 64E/Q (r=8, n=1024);
  - 8E/Q (r=16, n=256);
  - "none" (r=8, n>=2048; r=16, n>=512). [v2: FIX-4] In these rows only very large 𝔮 close, where τ_hi is O(1)–O(10): at the least closing 𝔮, τ_hi∈{1,2,6,12} (e.g. 12 at (8,2048,1024,64), 2 at (16,512,256,64), 6 at (8,8192,16384,64)). v1 said "only those with τ_hi<1", which is false: these are genuine, if extreme, closures. No claim of this note depends on them.
- **Mode "R23"** (m=E, N_1=⌈E/(ρ𝔮)⌉). [v2: FIX-2] Mode "R22only" (m=min(ρ𝔮⌈(E−X)/(ρ𝔮)⌉,E), N_1=1, i.e. only R22 Cor 3.2) gives identical results on all 162 rows and on the 112 B2 cases (`numerics_R23_v2.out`):
  - **r∈{4,8}, n=256: every dyadic 𝔮>=128 closes.** This holds on the main grid and on 112 further cases (r∈{4,8}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12}; Part B2).
  - All other rows are unchanged.
  - For r=16, n=256 the threshold stays 8E/Q. [v2: FIX-1] At Q=128, S=64 the exact failing τ_0-sets (`numerics_R23_v2.out`, diagnostics v2) are:
    - 𝔮=4E/Q=4096: [5473,63625] for d'=2E−2 and [5501,63607] for d'=2E+4 (τ_hi=171385). N4 holds only up to 5472, (4.1′) from 63626.
    - 𝔮=1024: [1809,254502] (d'=2E−2), [1818,254429] (d'=2E+4).
    - 𝔮=128: [1528,2036040] (d'=2E−2), [1536,2035461] (d'=2E+4). Here 131085 is only the end of N4's domain τ_0<=d'−E+N_1−1; N4 itself holds only up to 1527.
    - v1 said that at 𝔮=4E/Q "the two bounds miss by one value". That was a misreading: v1's script printed only the failing test points (endpoints and vertex), not the failing set.
  - At n>=512, (4.1′) is vacuous (D_1=d'−a<0), and N_1 is negligible against τ_hi.
- **Scope.** These are grid statements, exactly like R20's table. No monotone whole-strip argument is claimed for Cor 3.3.

**Remark 3.4 (F²|a at n=256 forces a=0; PROVED).** deg a_P=M'+Q−T<8h/625. At n=256 this is <3.277E<4E−4<=2d'. So at n=256, F²|a_P forces a_P=0, and likewise a_R=0. Therefore the n=256 residual of (𝒦)∧F²|a, which by Cor 3.3 can only be r>=16, has a_P=a_R≡0, i.e. P^tf^[ρ]=R^tf^[ρ]=0 identically. Whether this "zero alignment" contradicts an original gate was not examined (OPEN).

**Residual of (R2) after this note.** Non-constant (𝒦)∧F²|a_P∧F²|a_R, in the rows that Cor 3.3 leaves open:
- r=4: 𝔮<32E/Q at n=512, 𝔮<nE/(16Q) at n>=1024;
- r=8: 𝔮<32E/Q at n=512, 𝔮<64E/Q at n=1024, all 𝔮 at n>=2048;
- r=16: 𝔮<8E/Q at n=256, all 𝔮 at n>=512;
- r>=32 wherever R20 does not apply, as before.

R22 Prop 5.5 continues to apply there (CONDITIONAL on ε_top<N_1, with N_1 in place of N_0 by Prop 2.1). [v2: N3] Here N_1=2rS/𝔮_max: Prop 5.5 must be applied with 𝔮_max (R22 v2.1 RC-1), and if 𝔮_max>2rS then N_1=1 and the condition is void. [v2: FIX-3, audit's optional observation] For ε_top<N_1 the weight N_1−ε_top is >=1, so R22 Prop 5.5's count is automatic there as well. The p-adic argument of §4 does not apply here, because N_1=2rS/𝔮_max is a power of 2.

---

## 4. (R1): 𝔅_0 is the support of 𝔡 and lies in the Weierstrass locus

**Proposition 4.1 (𝔅_0={𝔡≠0}; PROVED, conditional on R22 Thm 3.1, Lemma 5.1, R21 Cor 3.3).** Assume a non-constant twist, inside or outside (𝒦). [v2: N1: v1 also assumed S>=128; this is superfluous, see the proof.] For every good u:
      u∈𝔅_0  ⟺  𝔡(u)≠0.
For u∈𝔅_0, with λ_u:=[t^0]ε(t)=lc_{E−X}(s̃_u)/lc_E(F(Y(t)))≠0,
      𝔡(u) = κ_u^{−1}κ_0^X(gD)^{X−ρ}·λ_u·(α^X,β^X)(u).          (4.1)

*Proof.*
- [v2: N1] **Case S=64.** Then 𝔮_max>=128>S, so R22 Lemma 5.1(a) gives V_u(z(u))=0 and ν_u>=E at every good u. Hence 𝔅_0=∅ and 𝔡=0 at every good u, and the equivalence holds trivially. Assume S>=128 below.
- **Off 𝔅_0.** Take 𝔮=128<=S in R22 Lemma 5.1(b); it allows any admissible 𝔮<=S, and 128ρ | E−X=(2r−1)ρS because 128 | S. For good u∉𝔅_0 this gives δ_u>=min(128ρ−1,X)>=1. So R22 Thm 3.1(iii) gives ord_t(V_u|_{ℓ_u})>=min(X−ρ,δ_u)>=1, i.e. V_u(z(u))=0. By R21 Cor 3.3, V_u(z(u))=κ_u𝔡(u), so 𝔡(u)=0.
- **On 𝔅_0.** Here ν_u=E−X<E=e_u.
  - So ord_ts̃_u=E−X (R22 Thm 3.1 Step 4) and ord_tε=X+(E−X)−E=0.
  - In R22 Thm 3.1(ii) at t=0, the term t^{X−ρ}a'_c vanishes (X−ρ>=1). This gives C_c(z)b^[ρ]=κ_0^Xλ_uΩb^[X].
  - Now b^[ρ]=(gD)^ρc^[Q], Ωb^[X]=(gD)^XΩc^[T]=(gD)^X(α^X,β^X), and V_u(z(u))=κ_u𝔡(u). These give (4.1), and λ_u≠0. ∎

*Remark.* (4.1) is consistent with R21 Lemma 3.2(i) (𝔡∥(α^X,β^X)). It identifies the open set {𝔡≠0} with the points where the twist osculates its own slope only to the minimal order E−X, and it gives 𝔡 there as the quotient of two leading coefficients.

**Corollary 4.2 ((𝒦_ψ)∖(𝒦) is excluded for every 𝔮; (R1) forces a large 𝔅_0; PROVED; numbers from R22 Thm 5.3).**
- (i) Every non-constant (𝒦_ψ)-model is in (𝒦), or has N_good<=0.104306q and is excluded. This holds for every 𝔮_max.
- (ii) A non-constant model outside (𝒦) (i.e. (R1)) with 𝔮_max<=S has 𝔡≢0 and |𝔅_0|>(1551/4000−0.147704)q>0.240046q.

*Proof.*
- **(i)** If 𝔮_max>S, this is R22 Thm 5.3(ii). Otherwise S>=𝔮_max>=128, and by Prop 4.1, 𝔡≡0 gives 𝔅_0=∅.
  - So by R22 Lemma 5.1(b) (with 𝔮=𝔮_max), every good u has m'_u=min(ord V_u|_{ℓ_u},e_u,ρ𝔮)>=min(X−ρ,ρ𝔮−1)>=2.
  - R22 Lemma 5.2 and the proof of Thm 5.3(ii) apply verbatim, with the same numbers (they use only 𝔮>=128). So k_22≡0, i.e. (𝒦), or N_good<=0.104306q.
- **(ii)** If 𝔡≡0, then (i) puts the model in (𝒦) or excludes it. So 𝔡≢0, and Z(𝔡)∩good has at most deg 𝔡² points (R21 Lemma 3.2(iii)).
  - By Prop 4.1 the remaining good points are exactly 𝔅_0.
  - R22 Thm 5.3(i) bounds charges+deg 𝔡² by 0.147704q, and N_good>(1551/4000)q+1. ∎

So R22 Cor 5.4's second threshold is gone, and its first becomes a **lower** bound: in (R1) with 𝔮_max<=S, more than 0.24q good points lie in 𝔅_0.

**Lemma 4.3 (orders of V; PROVED from CITED Stöhr–Voloch Cor 1.9; COMPUTED check, Part C).** Let V be a base-point-free linear system of dimension <=4 on a smooth curve in characteristic 2, with orders ε_0=0<ε_1<…<ε_{r_V}.
- (i) Every ε_i is 0, a power of 2, or ε_1+ε_2. The last occurs only as ε_3.
- (ii) No integer with three or more binary ones is an order. In particular, if r>=4 and 𝔮<=S, then N_0=(2r−1)S/𝔮 is not an order.
- (iii) If ε_1=1 and 𝔮<=S, then max{ε_i: ε_i<N_0}<=rS/𝔮+1. Hence N_0−max{ε_i<N_0}>=γ:=(r−1)S/𝔮−1>=r−2>=2.
- (iv) If ε_1=1, then Σε_i<=2ε_top.

*Proof.*
- **The criterion.** By Lucas, binom(ε,μ) is odd iff the binary digits of μ are a subset of those of ε. So by the p-adic criterion (CITED), every binary sub-integer of an order is an order.
- **(ii).** An integer with b binary ones has 2^b distinct sub-integers. There are at most 4 orders, so b<=2. N_0=(2r−1)·2^k with 2^k=S/𝔮, and 2r−1 has log_2(2r)>=3 ones.
- **(i).** ε_1 has only the sub-integers 0 and ε_1, so it is a power of 2.
  - If ε_2 had two ones, both one-bit parts would be orders below ε_2, i.e. both equal to ε_1, which is impossible. So ε_2 is a power of 2.
  - ε_3 has b<=2 ones; if b=2, its one-bit parts are ε_1 and ε_2.
- **(iii).** r and 2^k are powers of 2. The largest power of 2 below (2r−1)2^k is r2^k, and ε_1+ε_2=1+ε_2<=r2^k+1 when ε_2<N_0. So max{ε_i<N_0}<=r2^k+1, and N_0−(r2^k+1)=(r−1)2^k−1.
- **(iv).** The possible sequences are (0,1), (0,1,2^a), (0,1,2^a,2^b) and (0,1,2^a,2^a+1). In each case Σε_i<=2ε_top.
- **Check.** `numerics_R23.out` Part C enumerates all 443 closed sequences with entries <=2^12. None contains (2r−1)2^k (r∈{4,…,64}, k<=6), and the minimal γ is >=(r−1)2^k−1 in every case. ∎

**Proposition 4.4 (𝔅_0 lies in the Weierstrass locus of V; PROVED, conditional on Lemma 4.3 and CITED Stöhr–Voloch Thm 1.5).** Assume a non-constant twist with 𝔮_max<=S. Let V=span(t̂_ij) for 𝔮_max. Then every u∈𝔅_0 lies in W(V) and satisfies v_u(R_V)>=γ. Consequently
      |𝔅_0| <= deg R_V/γ = [ (Σε_i)(2g−2) + (r_V+1)τ_0 ] / γ.

*Proof.*
- **σ_u has order exactly N_0.** For u∈𝔅_0, ν_u=E−X is finite, so σ_u∈V∖0 (R19 Lemma 3.5(i): σ_u=Σŵ_iĉ_jb̂_ij, and the b̂_ij are the t̂_kl). Its order at u is ν_u/(ρ𝔮_max)=(2r−1)ρS/(ρ𝔮_max)=N_0.
- **So N_0 is a vanishing order at u.** N_0 belongs to the set {j_0(u),…,j_{r_V}(u)} of vanishing orders of members of V at u, say N_0=j_{i_0}(u).
- **u is a Weierstrass point.** By Stöhr–Voloch, j_i(u)>=ε_i for all i. If j(u)=ε, then N_0 would be an order, contradicting Lemma 4.3(ii). So u∈W(V).
- **The weight.** Moreover ε_{i_0}<=j_{i_0}(u)=N_0 and ε_{i_0}≠N_0, so ε_{i_0}<N_0. Hence v_u(R_V)>=Σ_i(j_i(u)−ε_i)>=N_0−ε_{i_0}>=γ (Lemma 4.3(iii); 𝔮_max makes the map separable, so ε_1=1, as in R22 Prop 5.5).
- **Count.** R_V is effective of the stated degree, and distinct u are distinct points of Γ̃. ∎

**Corollary 4.5 ((R1) is excluded unless V is non-classical with a large order sum [v2: N4]; PROVED; numbers COMPUTED).** A non-constant model outside (𝒦) in 𝔇_16 is excluded unless 𝔮_max<=S and
      Σ_iε_i(V) > Σ* := max{Σ : Σ(d²−3d) + (r_V+1)τ_hi < γ(1551q/4000 − B_{5.3(i)})},
with B_{5.3(i)} the bound of R22 Thm 5.3(i) and τ_hi=⌊(Nd/ρ+d)/𝔮_max⌋. On the whole strip Σ*>=0.238γn. In particular (R1) is excluded whenever:
- V is classical (ε_i=i), or dim V=2 (already in R22 [v2: FIX-3]);
- ε_top<N_0;
- ε_top<=0.119γn.

*Proof.*
- **The case split.** If 𝔮_max>S, use R22 Thm 5.3. Otherwise S>=128, Cor 4.2(ii) gives 𝔡≢0, and Prop 4.1 splits the good points into Z(𝔡) and 𝔅_0. So
      N_good <= B_{5.3(i)} + |𝔅_0| <= B_{5.3(i)} + deg R_V/γ   (Prop 4.4),
  with 2g−2<=d²−3d and τ_0<=τ_hi (R18 §5). This gives the Σ* criterion.
- **Whole strip.** B_{5.3(i)}<=0.147704q (R22, whole strip). Suppose Σε_i<=0.238γn. Then:
  - Σε_i(d²−3d)=Σε_i(E²+E−2)<=0.238γq(1+2^{−15});
  - (r_V+1)τ_hi<=4(Nd/ρ+d)/128<=1.3·10^{−5}q, using ρ>=64 and Nd<(16/625)(1+2/E)q.
  - With γ>=2 the sum is <=0.2380137γq<0.240046γq. So N_good<1551q/4000.
- **The special cases.**
  - Classical V has Σε_i<=6.
  - ε_top<N_0 gives Σε_i<=2ε_top<2(2r−1)S/𝔮_max. This is <=0.238((r−1)S/𝔮_max−1)·256 for all r>=4 and S/𝔮_max>=1, since 60.9(r−1)x−60.9−(4r−2)x>0.
  - Lemma 4.3(iv) gives Σε_i<=2ε_top.
- **Numbers.** The grid values of Σ* are in `numerics_R23.out` Part D. The minimum of Σ*/n is 0.4766, at r=4, 𝔮_max=S (γ=2), n=256, where Σ*=122. ∎

*Remarks.*
- **Relation to R22 Prop 5.5.** [v2: FIX-3] In (R1), Cor 4.5 contains R22 Prop 5.5's pencil and classical cases (both already closed in R22). For V with ε_top<N_0 it gives the exclusion with no count hypothesis, because Lemma 4.3(iii) makes the weight N_0−ε_top>=γ>=2 uniform. The hypothesis ε_top<N_0 on V itself remains; v1's "makes ... unconditional" was an overclaim. v1's "Prop 5.5 needed 𝔮_max<(2r−1)S/3; Cor 4.5 does not" is vacuous in (R1), where 𝔮_max<=S gives N_0>=7.
- **The residual of (R1)** is now: 𝔮_max<=S (so S>=128); dim V∈{3,4}; V non-classical [v2: N4] with ε=(0,1,2^a), (0,1,2^a,2^b) or (0,1,2^a,2^a+1); ε_top>0.119γn (so ε_top>=64 at n=256); and more than 0.24q good points that are Weierstrass points of V, each of weight >=γ.
- **(HEURISTIC) Where the next gain should come from.** At good u∉W(V), σ_u is a member of V of order >=N_0+1 whose coefficient tensor has the rank-one Frobenius form ĉ(u)^[Q]⊗ĉ(u). If no order of V lies strictly between N_0 and ε_top, then σ_u is the osculating hyperplane at u. That hyperplane map is a 2^b-th power (FNAK-type). This rigid coincidence is the natural target. Comparing the two maps naively costs a factor Q𝔮 in degree (compare R21 Remark 3.5), so a different argument is needed.

---

## 5. Target (a): what the new input does and does not give

**Proposition 5.1 (constant twists: no new constraint from §2; PROVED).** For a constant twist, ν_u=∞ and s̃_u≡0 at every good u. Prop 2.1 is then empty, and Cor 2.2(i) is R22 Cor 4.2's first step (order >=ρ). Thm 3.1 re-proves R22 Cor 4.2 with a different count. **No new condition** is obtained on 𝔉_D∩{F|h}∩{F²|a} (D∈{1,2}) or on the constant D>=4 lanes with n<4D. ∎

**Corollary 5.2 (the W_u line-zero count is vacuous in (𝒦); PROVED negative result).** Assume (𝒦). By Prop 2.3, W_u|_{ℓ_u} has a zero of order >=e_u+ρ−X+E at z(u). Suppose, generously, that it also vanished at every one of the d'−e_u residual intersections of ℓ_u with Γ', counted with multiplicity. Then its number of zeros would be >=d'+E+ρ−X. Since deg W_u=M'=a+d'+ρ−X, this forces W_u|_{ℓ_u}≡0 only if a<E. But:
- for a constant twist, (𝒦) forces a>=d'>=2E−2 (R20 Prop 3.1);
- for a non-constant twist, F|Δ forces 2a>=d' (R18-T Prop 4.2), so a<E only at a=E−1, d'=2E−2. [v2: FIX-5] That edge case is excluded by Prop 3.2(i) together with R20 Lemma 4.3: with m=E>a, every good non-cuspidal u has ξ^ω_u≡0, i.e. lies in 𝔅, and |𝔅|<=B_𝔅=O(E²)≪q. This uses the bootstrap Prop 2.1(ii); m=E−X would not suffice. v1 cited R18-T's N4 remark, which is stated for D>=4 and needs E<=ρ𝔮, so it does not cover non-constant twists with ρ𝔮<E.

So this route gives no new range. ∎

*Remark 5.3 (where the remaining information sits; statements PROVED, use HEURISTIC).* By Prop 2.3 and R22 Remark 4.4, FN at u is equivalent to the congruence (2.2) together with the f^[X]-component of the transverse layer y_u=P_c^tω^[ρ]/F. (2.2) is fixed by (C, twist). In (𝒦)∧F²|a with any twist, Cor 2.2(iii) gives ν_u>=e_u. Then Step 1 of R22 Thm 3.1 gives ω^[X]×(y_u−(s̃_u/F)f^[X])≡0, i.e. y_u≡(s̃_u/F)f^[X]+μω^[X] (mod t^{e_u−X}) for some μ∈k[[t]] (using f^[X]×ω^[X]=κ_0^XJ^[X]Ωb^[X]). Comparing the f^[X]- and ω^[X]-coefficients of FN (f(z)×w≠0, so the comparison is unimodular) gives μ≡t^{X−ρ}a'_c≡0 (mod t^{e_u−X}). Hence P_c^tω^[ρ]=s̃_uf^[X]+Fy_u=O(t^{2e_u−X}) along ℓ_u, which is R22 Remark 4.5 now for every twist. Any further exclusion must use P's transverse layer, which (C, a, twist) do not determine (R22 Remark 4.4 / Prop 4.3). This is the common bottleneck of the constant residual and of (R2) after Thm 3.1.

---

## 6. What remains, and next steps

**Residual after R23** (inside 𝔇_16, global alignment, Q>=128, 256E<=h<4QE, 𝔮_max>=128; v1 audited PASS-with-fixes, v2 applies the fixes):
- **(𝒦)∧F²|a_P∧F²|a_R, any twist.** This is now the single common residual of:
  - the constant twists (D∈{1,2}: 𝔉_D∩{F|h}∩{F²|a}; D>=4: n<4D, (𝒦), F²|a);
  - (R2) (non-constant), in the rows of §3 left open by Cor 3.3: r=4 at n>=512 below R20's thresholds, r=8 at n∈{512,1024} below them and all of n>=2048, r=16 at n=256 below 8E/Q and all of n>=512.
  
  At n=256 it forces a_P=a_R≡0 (Remark 3.4).
- **(R1).** Only 𝔮_max<=S with V non-classical [v2: N4], dim V∈{3,4}, Σε_i>Σ*>=0.238γn.
- **(𝒦_ψ)∖(𝒦):** closed.

**Next steps (HEURISTIC).**
1. **(𝒦)∧F²|a.** Since F²|a_P and the S-layer is aligned (R17 §7.3), the second layer S of a local splitting P^t=f^[X]⊗κ̃+F·S satisfies Sf^[ρ]=(a'−κ')f^[X], with a'≡0 mod F. In (𝒦), S_c maps span(f^[ρ],v_c) (J^[ρ,t]v_c=Bc) into span f^[X] on Γ'. This is a partial common-image structure one layer down. If it can be made global (an analogue of FNAL for S, with a degree drop of d'), the R16 §5 recursion of depth <=M'/(2E−2) would start with an explicit invariant. Remark 3.4's "a≡0 at n=256" is its first instance.
2. **r=16, n=256.** [v2: FIX-1] The gap below 8E/Q is wide: at 𝔮=4E/Q both bounds fail on ~58 000 consecutive values of τ_0 ([5473,63625]), and at 𝔮=128 on [1528,2036040]. v1's "a small per-point gain would close that 𝔮" is withdrawn. Closing these rows needs a genuinely new input in the middle τ_0-range, where neither the N4 denominator d'−E−τ_0+N_1 nor the (4.1′) budget ad'−ρ𝔮τ_0 is favourable.
3. **(R1).** Use the rigidity of §4's remark: off W(V), σ_u has rank-one Frobenius coefficients ĉ^[Q]⊗ĉ and order >=N_0+1. When ε_{top−1}<N_0, σ_u is the osculating hyperplane, which is a 2^b-th power map. A comparison at the level of V^* that avoids the Q𝔮 degree factor is needed.

---

## 7. Computations (`scripts/`; `python3 -I`, single process; v1 script 6 s, v2 copy 10 s)

| script → output | content | result |
|---|---|---|
| `numerics_R23.py` → `numerics_R23.out`, Part A | Thm 3.1 bound: exact, maximised over d'∈[2E−2,2E+4], on 1260 rows (r∈{4,…,64}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12}, dyadic 256<=n<4Q); monotone upper bound | grid max 0.0826303 at (64,16384,64,32768); whole-strip sup = corner UB 101790647887837/1099511627776000≈0.0925781<0.38775; the grid max of the UB equals the corner value |
| Part C | all p-adic-closed order sequences of length <=4 with entries <=2^12 (443); test N_0=(2r−1)2^k; minimal γ with ε_1=1 | no sequence contains any N_0 (r∈{4,…,64}, k<=6); min γ>=(r−1)2^k−1 throughout, with equality except at r=64, k=6 (4032 vs 4031; an artefact of the cap 2^12, which excludes the order 4097) |
| Part D | R22 Thm 5.3(i) bound (reproduces R22's corner 32480243592761/219902325555200 exactly); Σ* of Cor 4.5 on a grid of (r,Q,S,n,𝔮_max<=S) | min Σ*/n=0.4766 (r=4, 𝔮_max=S, γ=2, n=256, Σ*=122); e.g. Σ*=860 at r=16, γ=14, n=256 |
| Part B | R20 Cor 5.3 re-implementation, modes "R20" and "R23", 162 (r,n,Q,S) rows, every d', all dyadic 𝔮 up to τ_hi<1 [v2: N5: the audit's independent recount adds Q=8192, 198 rows, all agreeing] | R20 mode reproduces the R20 v2.1 table exactly; R23 mode: n=256, r∈{4,8}: least 𝔮 = 128 (all close); other rows unchanged |
| Part B2 | R23 mode, n=256, r∈{4,8}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12} | 112/112 cases: every 𝔮>=128 closes |
| diagnostics (v1) | R23 mode, r=16, n=256, Q=128, S=64 | [v2: FIX-1] v1's script printed only the failing *test points* (endpoints/vertex), e.g. "fails at τ_0 in [63625]"; v1 misread this as a one-value gap. Superseded by the next rows |
| `numerics_R23_v2.py` → `numerics_R23_v2.out` [v2: FIX-1, FIX-2, FIX-4] | corrected copy: exact failing integer τ_0-sets (bisection on exact sign changes, with spot checks at both ends of every interval); mode "R22only"; τ_hi at the least closing 𝔮 per row. Parts A, C, D byte-identical to v1's | r=16, n=256, Q=128, S=64: 𝔮=4096 fails on [5473,63625] (d'=2E−2), [5501,63607] (d'=2E+4); 𝔮=1024 on [1809,254502], [1818,254429]; 𝔮=128 on [1528,2036040], [1536,2035461] (all agree with the audit). R22only = R23 on 162/162 rows and 112/112 B2 cases. "none" rows: τ_hi at the least closing 𝔮 ∈{1,2,6,12} |

Checksums: `scripts/SHA256SUMS.txt` (v1 and v2 scripts and outputs).

*Caveat.* The new structural results (Prop 2.1, Cor 2.2, Prop 2.3, Prop 4.1, Prop 4.4) are proved by hand from the cited inputs. The owner built no toy model of an original configuration, because R22's `toy_vector_FN.py` is not in this directory and was not re-run. The owner computations check the counts, the reproduction of R20's and R22's numbers, and the combinatorics of Lemma 4.3. [v2: N6] The audit's toys A and B (`toy_prop21.py`, GF(2^8)) check the mechanism: (1.1) for a non-constant twist (683/683), and the congruence (2.1) with the divisibility lift (solvable iff ν>=e−ρ; with 𝔮>=2 the only surviving ν<e is ν=E at e=E+1). They are not original models.

---

## 8. Status

| item | status |
|---|---|
| Prop 2.1 ((𝒦) ⇒ ν_u>=E; ord ε>=X−1) | PROVED (R22 Thm 3.1/Cor 3.2/Lemma 2.2, R20 Lemma 4.1, R19 Lemma 3.0/3.5(i)) |
| Cor 2.2 ((𝒦) ⇒ a'_{c(u)} vanishes to order >=ρ−1 at z(u); F²\|a ⇒ ν_u>=e_u) | PROVED |
| Prop 2.3 (exact identity μ'_ub^[X]=κ_0^{−X}g^{X−ρ}t^{ρ−X}FΩC_cb^[ρ]) | PROVED (R16.1, R22 Lemma 2.1(i), R18-T Lemma 2.1(ii)) |
| Thm 3.1 ((𝒦) with F²∤a excluded, any twist, every scale) | PROVED; <=0.0925781q COMPUTED, whole strip by monotonicity |
| Prop 3.2 (R20 Lemma 4.2/Thm 5.1 with m=E; R19 Lemma 3.5(iii) with τ_0−N_1) | PROVED; [v2: FIX-2] the weaker form m>=E−X needs only R22 Cor 3.2 |
| Cor 3.3 (non-constant (𝒦) at n=256, r∈{4,8}, all 𝔮) | COMPUTED exactly on the grid (exclusion PROVED where evaluated); R20 table reproduced; [v2: FIX-2] input is R22 Cor 3.2 into R20's order step; [v2: FIX-1] r=16 failing sets corrected; [v2: FIX-4] "none" rows not vacuous |
| Remark 3.4 (n=256, F²\|a ⇒ a_P=a_R=0) | PROVED; consequence OPEN |
| Prop 4.1 (𝔅_0={𝔡≠0}; formula (4.1)) | PROVED; [v2: N1] S>=128 not needed |
| Cor 4.2 ((𝒦_ψ)∖(𝒦) excluded for every 𝔮; (R1) ⇒ \|𝔅_0\|>0.240046q) | PROVED; numbers from R22 |
| Lemma 4.3 (p-adic structure of orders; N_0 never an order; γ) | PROVED from CITED SV Cor 1.9; COMPUTED check |
| Prop 4.4 (𝔅_0⊂W(V), v_u(R_V)>=γ) | PROVED (CITED SV Thm 1.5) |
| Cor 4.5 ((R1) excluded if Σε_i<=Σ*, Σ*>=0.238γn; ε_top<N_0 with no count hypothesis; classical V and dim V=2 already in R22) | PROVED; Σ* COMPUTED; [v2: FIX-3] "unconditional" withdrawn |
| Prop 5.1, Cor 5.2 (no gain for constant twists; W-line count vacuous) | PROVED (negative); [v2: FIX-5] edge case via Prop 3.2(i) + R20 Lemma 4.3 |
| Remark 5.3 (P_c^tω^[ρ]=O(t^{2e_u−X}) in (𝒦)∧F²\|a, any twist) | PROVED statement; use HEURISTIC |
| (𝒦)∧F²\|a_P∧F²\|a_R (constant and non-constant, rows of §6); (R1) with non-classical V [v2: N4], Σε_i>Σ* | OPEN |

Dependencies: R22, R21, R20, R19, R18-T, R16 (all v2.1, audited and revision-checked); PRIMARY FNAL/TSY/TSYC/FNAM (reviewed); Stöhr–Voloch (CITED). The PRIMARY results remain PRIMARY's. The bootstrap of Prop 2.1 combines R22's Cor 3.2 and Thm 3.1(ii) with R19's (𝒦) normal form; the count of Thm 3.1 follows R21 Lemma 3.2's ψ∉K² device. v1 was independently audited (PASS-with-fixes); this v2 applies FIX-1..5 and N1–N6. No manuscript was edited. The classification of hyperovals is not claimed complete.
