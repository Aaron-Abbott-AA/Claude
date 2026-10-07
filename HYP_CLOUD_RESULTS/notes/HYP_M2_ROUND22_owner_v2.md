# HYP M>=2, round 22 (owner v2): the forgotten span(f^[X]) component — a vector own-line identity, exclusion of every constant twist outside (𝒦), and of (R1) at 𝔮>S

7 October 2026. Claude HYP(2) owner research note (R22), following R21 v2.1.

**Version history.**
- v1: owner draft.
- v1 independently audited (`AUDIT_HYP_M2_ROUND22_20261007.md`): **PASS-with-fixes**. No mathematical error was found in any headline result (Prop. 2.3, Lemma 2.2, Thm 3.1, Cor. 4.1, Cor. 4.2, Thm 5.3). Fixes FIX-1..8 and minor notes N1–N8 were raised.
- **v2 (this file)** applies FIX-1..8, marked "[v2: FIX-n]", and some of the minor notes, marked "[v2: Nn]". The only numbers changed are the FIX-6 round-ups of printed upper bounds. No closure changes. v2 has not been revision-checked.
- Script headers are corrected in a new copy `scripts/toy_vector_FN_v2.py` (FIX-8). Its output `toy_vector_FN_v2.out` is byte-identical to `toy_vector_FN.out`, and the v1 files are kept.

**Targets (coordinator), in priority order:**
- (a) exclude 𝔉_1/𝔉_2 using original-data structure (FNAL's construction, the R18-T layer identity, the F·S layer at own-line orders >=E, G5), or give a partial obstruction or an exact characterisation of the liftable members;
- (b) study (𝒦_ψ): does it force (𝒦), or does it give a count?
- (c) if both stall, give precise negative results.

**Inputs (read, not re-proved; copies in `inputs/`):**
- R21 v2.1. Used: Prop. 2.1 (𝔉_D), Prop. 2.3, Cor. 2.2, Lemma 3.2 (𝔡, (𝒦_ψ), deg 𝔡²), Cor. 3.3, Remark 3.4 (PROVED identity).
- R20 v2.1. Used: Prop. 3.1 ((𝒦) with constant T forces a>=d'), Cor. 3.2, (1.1), Lemma 4.1 (for comparison only).
- R19 v2.1. Used: §3 "good u", Lemma 3.0, Lemma 3.5(i),(ii) (Ξ(u,v)=σ_u(v)^{ρ𝔮}; σ_u≡0 for <=2deg ψ good u), Lemma 1.5 / §1 (generic contact E).
- R18-T v2.1. Used: §1 standing hypotheses and normalisation T=T̂^[𝔮], Lemma 1.1 (first layer), Lemma 1.2 (slope equation), Lemma 2.1(i),(ii) (layer identity), Thm 3.4 exceptional-set list. [v2: FIX-5] Prop. 2.2 Step 3 is no longer cited; F|a_P, F|a_R is proved locally in Lemma 2.4(iv).
- R16 v2.1. Used: §1 (model, (FN), U^[E]=αℓ+βm, deg ψ<=(E+1)d), R16.1 (FN along the whole own line), R16.2 proof Step 1 (contact >=E), R16.4 (exceptional set 𝔈, <=1.5d²+3.5d+1), §5 item 1 (the F·S layer, which is what this note makes precise).
- R18 §5 (deg[T]<=Nd/ρ+d) and Cor. 5.5 (𝔮>=128), as cited in R18-T/R21.
- PRIMARY FNAL (H_P, two-sided kernels, FNAL §4 "the determinant forgets a component in span(f^[X])"), TSY, TSYC (b constant), FNAM (FNAM1 J, κ_0; FNAM3 b=gD(β,α)), FNAN §1 (λ'-zeros <=Nd; ψ-fibres <=(E+1)d), FNAO §2 (at most Q+1 slopes; c^[Q]∥Bc), as reviewed (PASS / PASS-with-fixes). All PRIMARY results remain PRIMARY's.

**Labels (as in R18-T–R21):**
- PROVED: complete proof here, conditional only on the named inputs.
- CONDITIONAL: proved under a named hypothesis that is not established.
- COMPUTED: exact computation; it proves only where an exact bound is evaluated.
- HEURISTIC / OPEN / CITED: as stated.

**Rules followed.**
- No file whose name contains "DZ" was opened. (The TSY/TSYC copies in `inputs/` are PRIMARY_* files; they mention DZ only in credit lines.)
- No PRIMARY/Codex script was executed; only `.md` files were read.
- Own scripts only, run with `python3 -I`, one process at a time, each < 1 min (the longest is 19 s).

**Notation** is that of R18-T §1, R19 and R21:
- q=Eh, E=rQS, ρ=Q/2, X=T/2=ρS, n=h/E; d=deg Γ<=E+2; d'=deg Γ'∈[2E−2,2E+4]; a=deg C_•=M'+X−ρ−d'.
- J=[j_1,j_2], j_1=L^tY, j_2=N^tY; f=κ_0 j_1×j_2 (FNAM1); Ω=[[0,1],[1,0]]; [v]_× is z↦v×z.
- 𝒜=(T^t)^[ρ], B=swap·𝒜^t, T=T̂^[𝔮] with t̂_ij sections of 𝓣 without common zero, τ_0=deg 𝓣=deg[T]/𝔮. "Constant twist" means [T] constant. All statements about 𝔮 hold for any admissible 𝔮 (T∈GL_2(K^𝔮) projectively); a larger 𝔮 only strengthens them. A constant twist behaves as 𝔮=∞.
- Alignment coefficients: P^tf^[ρ]=a_Pf^[X], R^tf^[ρ]=a_Rf^[X] (global alignment). Zero top gives F|a_P, F|a_R (Lemma 2.4(iv), local proof) [v2: FIX-5]. Put a'_•:=a_•/F, a polynomial of degree M'+Q−T−d', and a_c:=c_1a_P+c_2a_R, a'_c likewise.
- For a good u: z=e(u), g=g(u), V=u^[E]×c_0 (generic c_0, D:=c_0·e(u)≠0), Y(t)=z+tV, f(Y(t))=gu+tω(t), ω(t)=w+tw_2. TSYC: b:=J(Y(t))^tω(t)=gJ(V)^tu is constant, and FNAM3: b=gD(β,α)=gD·c^[2], c=c(u)=(√β:√α)(u). So b^[ρ]=(gD)^ρc^[Q] and b^[X]=(gD)^Xc^[T].
- P_c:=c_1P+c_2R, C_c:=c_1C_P+c_2C_R, V_u(Y):=C_{c(u)}(Y)c(u)^[Q] (R20 notation).
- **New:**
  - e_u:=ord_tF(Y(t))=I(ℓ_u,Γ';z(u)), the own-line contact. It is >=E (R16.2).
  - ν_u:=ord_{v=u} of v↦c(u)^t𝒜(v)c(u)^[Q] on Γ̃, in a local frame of 𝓣^{ρ𝔮}. Since c^t𝒜(v)x=det(B(v)c,x), this is ord_{v=u}Ξ(u,v)=ρ𝔮·ord_uσ_u (R19 Lemma 3.5(i)). For a constant twist ν_u=∞.
  - δ_u:=X+min(ν_u,e_u)−e_u.
  - 𝔅_0:={good u: e_u=E and ν_u=E−X}.

---

## 0. Summary

**The idea.** FNAL takes the determinant of R16.1's vector own-line identity with f^[X], and FNAL §4 records that this forgets a component. This note keeps the whole vector identity. Writing it with the first layer of R18-T Lemma 1.1, the layer identity of R18-T Lemma 2.1 and the TSYC constant b gives an exact identity (★) on every own line (Prop. 2.3). That identity contains one piece of information beyond TSYC/FNAM3. The F·S layer of R16 §5 sees the second layer through J^{[X],t}, which carries a factor t^ρ, while the own point u^[X] is seen with t^X. The mismatch t^{X−ρ} forces C_c(Y)c^[Q] to vanish to high order along the own line, at the own point.

**PROVED.**
1. **Vector own-line identity (Prop. 2.3).** At every good u, as polynomials in t, the full FN of R16.1 reads
      g^{ρ+X}·(P_c^tu^[ρ])×u^[X] = J^{[X]}[κ_0^X t^X a_c Ωb^[X] + t^ρ F C_c b^[ρ]] + t^{ρ+X}(P_c^tω^[ρ])×ω^[X].
   This identity is exact; it needs only global alignment, FNAL/TSY, Lemma 2.1(i) of R18-T and TSYC. FN at u says the left side is 0.
2. **Contact (Lemma 2.2).** At every good u, e_u∈{E,E+1}, and e_u=E+1 iff y_1(u)^[E]·e(u)=0.
3. **Main theorem (Thm 3.1).** At every good u (any twist), with s̃_u:=κ̃_c·ω^[ρ] the first-layer scalar on ℓ_u:
   - (i) ord_t s̃_u>=e_u−X, hence ν_u>=e_u−X whenever ν_u<e_u;
   - (ii) C_c(Y(t))b^[ρ] ≡ κ_0^X(t^{X−ρ}a'_c+t^X s̃_u/F)Ωb^[X] (mod t^X);
   - (iii) ord_{z(u)}(V_u|_{ℓ_u})>=min(X−ρ, δ_u), with δ_u>=0.
   - For a constant twist s̃_u≡0. Hence **V_u vanishes to order >=X−ρ=ρ(S−1) along ℓ_u at z(u)**, with the exact congruence C_cb^[ρ]≡κ_0^Xt^{X−ρ}a'_cΩb^[X] (mod t^X) [v2: N4: v1 said "exact leading term"; t^{X−ρ}a'_c leads only when a'_c(z(u))≠0].
4. **Ξ vanishes to high order at its own point (Cor. 3.2).** For every twist and every good u with σ_u≢0: ord_{v=u}Ξ(u,v)>=E−X, i.e. ord_uσ_u>=⌈(2r−1)S/𝔮⌉. [v2: FIX-4] v1 called this new beyond σ_u(u)=0. In fact this bound already follows from R16.2, which with TSYC gives ν_u>=E−X−ρ, together with ν_u∈ρ𝔮Z. What is new is the extra +ρ, used only at e_u=E+1, and above all the C-layer order of Thm 3.1(ii)–(iv), on which Thm 5.3 depends.
5. **Constant twists outside (𝒦) are excluded, for every D, at every strip scale (Cor. 4.1).** The count is
      N_good <= Nd + (1.5d²+3.5d+1) + 2(E+1)d + (Q+1)ad'/(X−ρ) + 6d_def+7 <= 0.046095q.
   This needs neither P_D, nor FNAM2, nor FNAP. In particular **𝔉_D∩{F∤h} (D∈{1,2}) is excluded**, which is target (a) outside (𝒦).
6. **Constant twists inside (𝒦) (Cor. 4.2).** Such a model is excluded unless **F²|a_P and F²|a_R**, i.e. the alignment coefficients vanish to second order along Γ'. The count otherwise is <=0.092972q.
   - For 𝔉_D∩{F|h} this is an exact necessary lifting condition. It lives on the alignment coefficients and is not implied by C̃: the modification P^t↦P^t+F·f^[X]⊗ξ keeps C and the first layer and changes a'↦a'+ξ·f^[ρ] (Prop. 4.3) [v2: FIX-2].
7. **(R1) at 𝔮>S is excluded; (𝒦_ψ) collapses to (𝒦) there (Lemma 5.1, Lemma 5.2, Thm 5.3).**
   - If 𝔮>S, every good u has V_u(z(u))=0, so 𝔡≡0 and (𝒦_ψ) holds (R21 Lemma 3.2).
   - The higher own-line order then forces k_22≡0, i.e. (𝒦).
   - Since 𝔮>=128>64, this excludes (R1) **entirely whenever S=64**, and in general on {𝔮>S}.
   - Answer to (b): for 𝔮>S, (𝒦_ψ)∖(𝒦) is excluded by an explicit count (<=0.104306q [v2: FIX-6]). For 𝔮<=S the same holds unless more than 0.24q good points lie in 𝔅_0 (Cor. 5.4).

**CONDITIONAL.**
8. **(Prop. 5.5)** For a non-constant twist, inside or outside (𝒦), let V:=span(t̂_ij)⊂H⁰(𝓣), with order sequence ε_0<…<ε_top. If ε_top<N_0:=⌈(2r−1)S/𝔮⌉ and the explicit count holds, the model is excluded. The count is <=0.068733q when V is classical with N_0>=4 [v2: FIX-6].
   - This is unconditional when dim V=2: then ε=(0,1), and N_0>=2 holds for 𝔮<(2r−1)S. [v2: FIX-7] Since Cor. 3.2 holds for every twist, this pencil case is PROVED in (R1) and in (R2) alike. Together with Thm 5.3 it closes (R1) with dim V=2 entirely.
   - The open condition is Frobenius non-classicality of the twist's linear system.

**COMPUTED.**
- `toy_vector_FN.out`, exact over GF(2^8). The identity (★) is checked on random data. FN along a line is imposed as a linear system on a family of P realising C=Ω(J^{[X],t}J^[X])C'' (not the most general P [v2: FIX-8]), and every solution satisfies Thm 3.1. The order X−ρ is **attained** (sharp) in all five (ρ,X) cases, and the exact congruence (ii) holds.
  - Controls behave as predicted. If the slope equation fails, FN is unsolvable. A non-constant layer gives order exactly min(X−ρ, X+ord s̃−e) in the solvable cases. [v2: FIX-8] The only unsolvable non-constant control is the trivial pole case ord s̃+X<e. The non-trivial gap cases e−X−ρ<=ord s̃<e−X were tested by the audit (`thm31_toy_indep`, general S): unsolvable with alignment, solvable without it.
- `contact_check.out`, Fermat σ1 model over GF(2^8) and GF(2^12). Every Hensel-checked point has e_u∈{E,E+1}, and E+1 occurs exactly when predicted (450 points for E=16 over GF(2^12)).
- `numerics_R22.out`, exact Fractions, 1260 rows. All six new counts are below 1551/4000. Each is maximal at the corner (4,128,64,256): 0.046094 (4.1), 0.092972 (4.2), 0.147704 and 0.104306 (5.3), 0.068733 and 0.049195 (5.5) [v2: FIX-6: rounded up].

**What failed / what remains.**
- 𝔉_D∩{F|h} with F²|a_P, a_R (a>=d', n>=512) is **not** excluded. The same holds for the constant D>=4 lanes inside (𝒦) with n<4D. Beyond order X, the identity involves y=P_c^tω^[ρ]/F, which (C,a) do not determine (Remarks 4.4, 4.5). G5 was not used (Remark 4.6).
- (R1) with 𝔮<=S is open on 𝔅_0 (points where Ξ(u,·) has the minimal order E−X and the contact is exactly E). (R2) is improved only by the pencil case of Prop. 5.5 (dim V=2, 𝔮<(2r−1)S; PROVED [v2: FIX-7]), conditionally by its classical case, and by a small per-point gain (Remark 5.6).

**Newly closed (PROVED; numbers COMPUTED; v1 audited PASS-with-fixes, no closure changed):**
- every constant twist outside (𝒦) (all D, all n), including 𝔉_D∩{F∤h} and the constant D>=4 lanes with n<4D outside (𝒦);
- constant twists in (𝒦) with F²∤a_P or F²∤a_R;
- (R1) for 𝔮>S, hence all of (R1) when S=64;
- (𝒦_ψ)∖(𝒦) for 𝔮>S;
- [v2: FIX-7] every non-constant twist (in or outside (𝒦)) with dim span(t̂_ij)=2 and 𝔮<(2r−1)S; hence (R1) with dim V=2 entirely.

---

## 1. Setting and good points

The standing hypotheses are those of R18-T §1 / R19 §3: 𝔇_16, global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮>=128.

**Good u.** A good u is a good point off the following sets:
- the original boundary (6d_def+7; this contains Bs(e));
- 𝔈 (R16.4, <=1.5d²+3.5d+1; this contains {g=0});
- {λ'=0} (<=Nd, R18-T Lemma 1.1);
- {det T̂=0} (<=2deg[T]/𝔮; empty for a constant twist).

The constant c_0 is chosen generic, so D(u)≠0 at all of the finitely many good points (FNAM3). At a good u:
- Γ is smooth at u, and e is a local isomorphism Γ→Γ' at u (FNAN §1);
- ℓ_u is the tangent of Γ' at z(u) (R16 §1);
- c(u)^[Q]=κ_uB(u)c(u) with κ_u≠0 (R18-T Lemma 1.2);
- J(z) has rank 2, since its minors are κ_0^{−1}f(z)=κ_0^{−1}gu≠0.

**Local first layer.** By R16.2 and R18-T Lemma 1.1, on Γ' near z(u),
      P(Y)^t = f(Y)^[X]⊗κ^Y_P(Y),   κ^Y_P=λ^Y(𝒜_11 j_1^[ρ]+𝒜_12 j_2^[ρ]),   κ^Y_R=λ^Y(𝒜_21 j_1^[ρ]+𝒜_22 j_2^[ρ]).
- Here λ^Y=g^{−X}λ'∘e^{−1} is regular and nonzero at z(u).
- The entries 𝒜_ij=t̂_ji^{ρ𝔮} are regular in a local frame of 𝓣^{ρ𝔮}.
- Choose lifts λ̃, 𝒜̃_ij∈O_{P²,z(u)} of these functions on Γ' (possible since O_{Γ',z}=O_{P²,z}/(F)), and put κ̃_P, κ̃_R by the same formulas.
- For a constant twist, take 𝒜̃=𝒜 constant (the scalar part of T is absorbed into λ').

---

## 2. The vector own-line identity

**Lemma 2.1 (three elementary identities on ℓ_u; PROVED from FNAM1, TSYC, R18-T Lemma 2.1(i)).** On Y(t)=z+tV:
- (i) J(Y(t))^tu=tJ(V)^tu=(t/g)b.
- (ii) f(Y(t))×ω(t)=κ_0J(Y(t))Ωb. Hence (f×ω)^[X]=κ_0^XJ^{[X]}Ωb^[X].
- (iii) [f^[X]]_×P^t=F·J^{[X]}C_PJ^{[ρ],t} (FNAL+TSY/FNAM), and the same for R.

*Proof.*
- **(i)** J is linear, and J(z)^tu=g^{−1}J(z)^tf(z)=0.
- **(ii)** R18-T Lemma 2.1(i) with exponent 1 gives f×v=κ_0JΩJ^tv. Take v=ω and use J^tω=b (TSYC). Frobenius commutes with × coordinatewise.
- **(iii)** This is FNAL's definition F·H_P=[f^[X]]_×P^t together with H_P=J^[X]C_PJ^[ρ,t]. ∎

**Lemma 2.2 (the own-line contact is E or E+1; PROVED; COMPUTED `contact_check.out`).** At every good u, e_u∈{E,E+1}. Moreover e_u=E+1 iff y_1(u)^[E]·e(u)=0, where v(s)=u+sy_1+s²y_2+… is the branch of Γ at u in a uniformizer s, in an affine lift (so y_1∦u) [v2: N1]. The criterion does not depend on the lift: y_1↦ay_1+bu multiplies it by a^E.

*Proof.*
- **Reduction to Γ.** e is a local isomorphism at u, so e_u=ord_s(u^[E]·e(v(s))).
- **Expand.** On Γ, v^[E]·e(v)=0, since Γ⊂C_orig. In characteristic two, u^[E]·e(v)=(u+v)^[E]·e(v). Frobenius is additive, so (u+v(s))^[E]=Σ_{k>=1}s^{kE}y_k^[E]. Hence
      u^[E]·e(v(s)) = s^E·Λ(e(v(s))) + O(s^{2E}),   Λ(Y):=y_1^[E]·Y.
- **The line Λ.** Since u is smooth, y_1∦u, so y_1^[E]∦u^[E] and the line {Λ=0} is not ℓ_u. If Λ(z(u))≠0, then ord_sΛ(e(v(s)))=0. Otherwise {Λ=0} is a line through the smooth point z(u) other than its tangent ℓ_u, so it meets Γ' there with multiplicity exactly 1.
- **Conclusion.** ord_s(u^[E]·e(v(s)))∈{E,E+1}, since E+1<2E. ∎

*Remark.* [v2: N1] The audit gives a shorter proof that needs no smoothness of Γ: with w=df_z(V), C_f(z+tV)=t^E(z·w^[E])+t^{E+1}(V·w^[E])+O(t^{2E}), and both coefficients cannot vanish by projective étaleness of f; its criterion z·w^[E]=0 agrees with y_1^[E]·e(u)=0 (29 705/29 705 points in the audit). It is consistent with R19 Prop. 1.1, which bounds the total excess Σ(j(u)−E). This sharpens "generic contact exactly E" (R19 §1) to a pointwise statement at all good points. It agrees with the R20 v2.1 observation j(u)=E+1 on the special clusters.

**Proposition 2.3 (the full own-line FN as an exact identity; PROVED from R16.1, global alignment, FNAL/TSY, FNAM1 (J, κ_0) [v2: N7], R18-T Lemma 2.1(i) and TSYC; COMPUTED `toy_vector_FN.out` (A)–(C), "identity (*)").** For every good u and every c∈k², as polynomials in t,
      g^{ρ+X}(P_c^tu^[ρ])×u^[X] = J^{[X]}[ κ_0^X t^X a_c Ωb^[X] + t^ρ F C_c b^[ρ] ] + t^{ρ+X}(P_c^tω^[ρ])×ω^[X],   (★)
with every function evaluated at Y(t). For c=c(u), R16.1 says that the left side vanishes identically. So FN along ℓ_u is equivalent to the vanishing of the right side.

*Proof.*
- **Expand the own point.** gu=f(Y)+tω (characteristic two), so g^ρu^[ρ]=f^[ρ]+t^ρω^[ρ] and g^Xu^[X]=f^[X]+t^Xω^[X].
- **Use global alignment.** P_c^tf^[ρ]=a_cf^[X]. Hence g^ρP_c^tu^[ρ]=a_cf^[X]+t^ρP_c^tω^[ρ].
- **Multiply out.**
      g^{ρ+X}P_c^tu^[ρ]×u^[X] = (a_cf^[X]+t^ρP_c^tω^[ρ])×(f^[X]+t^Xω^[X])
                            = t^Xa_c(f×ω)^[X] + t^ρ f^[X]×P_c^tω^[ρ] + t^{ρ+X}P_c^tω^[ρ]×ω^[X],
  using f^[X]×f^[X]=0 and the commutativity of × in characteristic two.
- **Substitute.** Insert Lemma 2.1(ii) and (iii). ∎

*What (★) adds to FNAL/TSYC.*
- [v2: FIX-3; v1 was wrong here] Dotting (★) with u^[X] gives nothing: both sides are identically ⊥u^[X] (two equal terms cancel on the right). Dotting with ω^[X] gives t^ρ·F·b^{[X],t}C_cb^[ρ] (v1 wrote t^{ρ+X}). This is exactly FNAL2/TSYC: J^{[X],t} sees only the second layer. (COMPUTED by the audit, `thm31_toy_indep.out`.)
- The remaining scalar of (★) is the span(f^[X]) component that FNAL §4 says is forgotten. Sections 3–5 use it.

**Lemma 2.4 (local splitting of P along ℓ_u; PROVED).** At a good u, with κ̃ as in §1 and c=c(u):
- (i) P^t−f^[X]⊗κ̃_P∈F·M_3(O_{P²,z}), and likewise for R.
- (ii) Hence, in k[[t]]³,
      P_c(Y(t))^tω(t)^[ρ] = s̃_u(t)·f(Y(t))^[X] + F(Y(t))·y_u(t),   y_u∈k[[t]]³,
  where
      s̃_u(t):=κ̃_c(Y(t))·ω(t)^[ρ]=λ̃(Y(t))(gD)^ρ·c^t𝒜̃(Y(t))c^[Q].
- (iii) s̃_u(0)=0. For a constant twist s̃_u≡0.
- (iv) a_c=F·a'_c (zero top; local proof below) [v2: FIX-5].

*Proof.*
- **(i)** The difference vanishes on Γ' near z(u) (§1). F is prime in S, so FO_{P²,z} is prime and is the ideal of Γ' at z.
- **(ii)** Write κ̃_c=λ̃J^[ρ]𝒜̃^tc. Then κ̃_c·ω^[ρ]=λ̃c^t𝒜̃(J^tω)^[ρ]=λ̃c^t𝒜̃b^[ρ], and b^[ρ]=(gD)^ρc^[Q].
- **(iii)** At t=0, c^t𝒜(u)c^[Q]=0 (R18-T Lemma 1.2). For constant 𝒜 this scalar is independent of t.
- **(iv)** [v2: FIX-5: v1 cited R18-T Prop. 2.2 Step 3, a step of a CONDITIONAL proposition.] On Γ' off Bs(f), P^t=f^[X]⊗κ_P with κ_P·f^[ρ]=g^{ρ−X}ϰ_P·U^[ρ]=0 by zero top. So a_Pf^[X]=P^tf^[ρ]=f^[X](κ_P·f^[ρ])=0 on Γ'. Some f_i^X is not divisible by the prime F, hence F|a_P; likewise F|a_R. ∎

---

## 3. The main theorem

**Theorem 3.1 (own-line order of the second layer; PROVED, conditional on R16.1, R18-T Lemmas 1.1, 1.2, 2.1, Lemma 2.4(iv) here [v2: FIX-5], FNAL/TSY/TSYC/FNAM; COMPUTED `toy_vector_FN.out`).** Let u be good and c=c(u). Then:
- (i) **Regularity.** ord_t s̃_u>=e_u−X. Consequently ν_u>=e_u−X whenever ν_u<e_u.
- (ii) **Exact congruence.** In k[[t]]²,
      C_c(Y(t))b^[ρ] ≡ κ_0^X·( t^{X−ρ}a'_c(Y(t)) + t^X s̃_u(t)/F(Y(t)) )·Ωb^[X]   (mod t^X).
- (iii) **Order.** ord_{z(u)}(V_u|_{ℓ_u})>=min(X−ρ, δ_u), where δ_u=X+min(ν_u,e_u)−e_u>=0.
- (iv) **Constant twist.** C_c(Y(t))b^[ρ]≡κ_0^Xt^{X−ρ}a'_c(Y(t))Ωb^[X] (mod t^X) (an exact congruence; t^{X−ρ}a'_c is the leading term only if a'_c(z(u))≠0 [v2: N3]). In particular V_u vanishes to order >=X−ρ=ρ(S−1) at z(u) along ℓ_u, and 𝔡(u)=V_u(z(u))/κ_u=0.

*Proof.*
- **Step 1: divide (★) by F.** By Lemma 2.4(ii), and since f^[X]×ω^[X]=κ_0^XJ^{[X]}Ωb^[X],
      (P_c^tω^[ρ])×ω^[X] = s̃_u·κ_0^XJ^{[X]}Ωb^[X] + F·(y_u×ω^[X]).
  Insert this and a_c=Fa'_c into (★), whose left side is 0 by R16.1. F(Y(t))≢0, because the irreducible nonlinear Γ' contains no line (FNAL §2). Dividing by F in k((t)) gives
      J^{[X]}·m = t^{ρ+X}(ω^[X]×y_u),   m:=κ_0^X(t^Xa'_c+t^{ρ+X}s̃_u/F)Ωb^[X] + t^ρC_cb^[ρ] ∈ k((t))².
- **Step 2: m∈t^{ρ+X}k[[t]]².** J(z) has rank 2, so some 2×2 minor of J^{[X]}(Y(t)) is a unit of k[[t]]. Cramer's rule on those two rows gives m∈t^{ρ+X}k[[t]]².
- **Step 3: (i) and (ii).** Divide by t^ρ:
      C_cb^[ρ] = t^{−ρ}m − κ_0^X(t^{X−ρ}a'_c+t^Xs̃_u/F)Ωb^[X].
  - The left side, t^{−ρ}m∈t^Xk[[t]]² and t^{X−ρ}a'_c lie in k[[t]], and Ωb^[X]≠0 (b≠0). Hence t^Xs̃_u/F∈k[[t]], i.e. ord s̃_u>=e_u−X. That is (i) for s̃_u, and the display is (ii).
- **Step 4: ord s̃_u versus ν_u.** λ̃ is a unit at z. φ:=c^t𝒜̃c^[Q]∈O_{P²,z} restricts on Γ' to the function whose order at z is ν_u.
  - In local coordinates with ℓ_u={y=0} and Γ'={y=γ(x)}, ord γ=e_u (Γ' is smooth at z and tangent to ℓ_u). Write φ(x,0)=φ(x,γ(x))+γ(x)·(…).
  - So ord_tφ(Y(t))=ν_u if ν_u<e_u, and ord_tφ(Y(t))>=e_u otherwise.
  - Hence ord s̃_u>=min(ν_u,e_u), with equality when ν_u<e_u. Together with Step 3 this gives the second half of (i).
- **Step 5: (iii).** b^[ρ]=(gD)^ρκ_uB(u)c, so V_u∝C_cb^[ρ] up to a nonzero constant. In (ii), the first term has order >=X−ρ, and the second has order X+ord s̃_u−e_u>=δ_u (Step 4). Also δ_u>=0 by (i).
- **Step 6: (iv).** s̃_u≡0 by Lemma 2.4(iii). At t=0, V_u(z(u))=κ_u𝔡(u) (R21 Cor. 3.3 proof), and X−ρ>=1. ∎

*Remarks.*
- **The mechanism.** J^{[X],t} applied to the S-layer gives κ_0^{−X}ΩC_c(J^tu)^[ρ]=O(t^ρ) (R18-T Lemma 2.1(ii) and Lemma 2.1(i) here). The own point gives J^{[X],t}u^[X]=O(t^X). FN says the S-layer image is a multiple of u^[X] with a *regular* coefficient. This is where regularity of the local S (Lemma 2.4) enters: the t^{X−ρ} cannot be absorbed.
- **Sharpness.** In `toy_vector_FN.out` (A), the order X−ρ is attained in every case (ρ,X)∈{(1,4),(2,4),(1,8),(2,8),(4,8)}, with 8/8 nonzero samples each. So (iv) is optimal from the (C,a)-level data.
- **The hypotheses are used.** In the controls:
  - (B) without the slope equation, FN is unsolvable;
  - (C) with a non-constant layer, the order is exactly min(X−ρ, X+ord s̃−e), and FN is solvable iff ord s̃>=e−X, as (i) predicts.

- [v2: N2] **Exact form (audit).** The audit's second proof gives, exactly and not only mod t^X, C_c(Y(t))b^[ρ]=κ_0^X(t^{X−ρ}μ̂+t^Xs̃_u/F)Ωb^[X] with μ̂≡a'_c (mod t^ρ). So V_u|_{ℓ_u} is everywhere a multiple of the constant vector Ωb^[X]∝(c^[T])^⊥. The same proof shows where the +ρ of (i) comes from: FN and common image alone give only ord s̃_u>=e_u−X−ρ, and global alignment supplies the rest.

**Corollary 3.2 (Ξ(u,·) vanishes to order >=E−X at u; PROVED).**
- For every twist and every good u with σ_u≢0:
      ord_{v=u}Ξ(u,v) = ν_u >= E−X,   i.e.   ord_uσ_u >= N_0 := ⌈(2r−1)S/𝔮⌉.
- If e_u=E+1, then ord_uσ_u>=⌈((2r−1)ρS+1)/(ρ𝔮)⌉.

*Proof.*
- If ν_u<e_u, Thm 3.1(i) gives ν_u>=e_u−X>=E−X. Otherwise ν_u>=e_u>=E.
- ν_u=ρ𝔮·ord_uσ_u, since Ξ(u,·)=σ_u^{ρ𝔮} (R19 Lemma 3.5(i)) and c^t𝒜(v)c^[Q]=det(B(v)c,c^[Q])=κ_uΞ(u,v). ∎

[v2: FIX-4] v1 said: "This is new information on the twist itself: R19 had only σ_u(u)=0." That overstates it. R16.2 with TSYC's J(Y(t))^tu=(t/g)b, transported to Γ by the graph argument, already gives ν_u+ρ>=E−X. Since ν_u∈ρ𝔮Z, this already yields ν_u>=E−X for 𝔮<=S and ν_u>=E for 𝔮>S. So the first bullet, and with it Prop. 5.5 and Remark 5.6, were derivable from R16.2 and R19 Lemma 3.5. Genuinely new are the extra +ρ, which matters only for the e_u=E+1 refinements (second bullet; Lemma 5.1(b)), and the C-layer order of Thm 3.1(ii)–(iv), which Thm 5.3 needs.

---

## 4. Constant twists

**Corollary 4.1 (constant twists outside (𝒦) are excluded; PROVED, conditional on Thm 3.1 and FNAO §2 / FNAN §1; numbers COMPUTED `numerics_R22.out`).** Assume a constant twist (any D) in 𝔇_16, and not (𝒦), i.e. the quadratic form c↦C_c(Y)Bc mod F is not identically zero. Then
      N_good <= Nd + (1.5d²+3.5d+1) + 2(E+1)d + (Q+1)·a·d'/(X−ρ) + 6d_def + 7,
whose value over q is <=0.046095 on the whole strip. So the model is excluded.

*Proof.*
- **Slopes.** Every good slope lies in the set of <=Q+1 projective roots of c^tAc^[Q]=0, and c^[Q]∝Bc there (FNAO §2). So for an allowed slope c, the vector of forms 𝒱_c(Y):=C_c(Y)c^[Q] of degree a is fixed up to a scalar.
- **Exceptional slopes.** Call c exceptional if F divides both components of 𝒱_c, equivalently F|C_c(Y)Bc. Outside (𝒦), c↦C_cBc mod F is a nonzero binary quadratic form with coefficients in (S/F)², so at most 2 projective c are exceptional.
  - The good u of a fixed slope c have ψ(u)=c_2²/c_1² (0 and ∞ included), so they lie in a single ψ-fibre, of at most (E+1)d points (FNAN §1).
- **Non-exceptional slopes.** Fix a component G of 𝒱_c with F∤G. For each good u with c(u)=c, Thm 3.1(iv) gives ord_{z(u)}(G|_{ℓ_u})>=X−ρ.
  - Γ' is smooth at z(u) with contact e_u>=E>X−ρ with ℓ_u, so ord_{z(u)}(G|_{Γ'})>=min(X−ρ,e_u)=X−ρ. This is the graph argument of Thm 3.1 Step 4.
  - Distinct good u give distinct smooth points of Γ' and distinct places of Γ̃. The places are counted via the morphism z, and z is a local isomorphism at good u.
  - Hence #{u: c(u)=c}·(X−ρ) <= deg(z^*G) = a·d'.
  - Summing over <=Q+1 slopes gives (Q+1)ad'/(X−ρ).
- **Exceptional sets.** {λ'=0} <=Nd; 𝔈 <=1.5d²+3.5d+1; the boundary <=6d_def+7.
- **Numerics.** With N<16h/625, a<8h/625, d=E+2, d'<=2E+4, d_def<=q/1000, q=nE², E=rQS and X−ρ=Q(S−1)/2, the bound over q is
      (16/625)(1+2/E) + (1.5d²+3.5d+1)/(nE²) + 2(E+1)(E+2)/(nE²) + 32(Q+1)(1+2/E)/(625Q(S−1)) + 6/1000 + 7/q.
  - Each term is non-increasing in r, Q, S, n, so the supremum is the corner (4,128,64,256): 33259609702489/721554505728000≈0.0460944<1551/4000.
  - The grid of 1260 rows confirms the maximum there. ∎

*Remarks on scope.*
- (1) This supersedes R21 Cor. 2.2 outside (𝒦) and needs no P_D≢0. It covers 𝔉_D∩{F∤h} for D∈{1,2}: by R21 Prop. 2.3(i), (𝒦)⟺F|h on 𝔉_D.
- (2) It covers every constant D>=4 lane outside (𝒦), including n<4D, which FNAP does not reach, and D>n/16, which R18-T Thm 3.4 does not reach.
- (3) It uses neither FNAM2 nor G5. On 𝔉_D outside (𝒦) it says that h(Bc,Y) vanishes to order >=X−ρ along ℓ_u at z(u) for every good u of slope c. A nonzero form of degree a can do this at no more than ad'/(X−ρ) points of Γ'.

**Corollary 4.2 (constant twists in (𝒦): the alignment coefficients must vanish doubly; PROVED; numbers COMPUTED).** Assume a constant twist and (𝒦). If F²∤a_P or F²∤a_R, then
      N_good <= Nd + (1.5d²+3.5d+1) + (E+1)d + (Q+1)·(M'+Q−T−d')·d'/ρ + 6d_def + 7 <= 0.092972q,
and the model is excluded. So every surviving constant (𝒦)-model has F²|a_P and F²|a_R.

*Proof.*
- **a' vanishes at each own point.** In (𝒦), F|C_c(Y)Bc for all c, so C_c(Y(t))b^[ρ]=O(t^{e_u}) with e_u>=E>X. By Thm 3.1(iv), t^{X−ρ}a'_c(Y(t))≡0 (mod t^X). Hence a'_{c(u)} vanishes to order >=ρ along ℓ_u at z(u), and so to order >=min(ρ,e_u)=ρ on Γ' at z(u).
- **Exceptional slopes.** a'_c=c_1a'_P+c_2a'_R is linear in c. Unless F|a'_P and F|a'_R, at most one projective c has F|a'_c. That slope costs one ψ-fibre, <=(E+1)d.
- **Other slopes.** For every other allowed slope, the form a'_c (degree M'+Q−T−d'<M'<8h/625) vanishes to order >=ρ at each of its good points. So that slope carries <=(M'+Q−T−d')d'/ρ good points.
- **Numerics.** The bound over q is <=(16/625)(1+2/E)+…+32(Q+1)(1+2/E)/(625Q)+…, monotone as before. The corner value is 3194487655227/34359738368000≈0.0929718. ∎

**Proposition 4.3 (what a liftable member of 𝔉_D must satisfy; PROVED: a list of necessary conditions, not a characterisation).** Let D∈{1,2} and suppose an original constant-twist model in 𝔇_16 survives with C̃∈𝔉_D. Then:
- (i) (𝒦) holds, i.e. F|h (resp. F|h'). This is Cor. 4.1 with R21 Prop. 2.3(i).
- (ii) a>=d', so n>=512 (R20 Prop. 3.1 / Cor. 3.2).
- (iii) F²|a_P and F²|a_R (Cor. 4.2).
- (iv) In particular, if 2d'−X+ρ<=M'<2d'+T−Q, then a_P=a_R=0 identically. Indeed deg a_• = M'+Q−T<2d', while (𝒦) forces M'>=2d'−X+ρ (R20 Prop. 3.1).

Conditions (iii) and (iv) concern the alignment coefficients and are not implied by C̃ [v2: FIX-2]:
- the modification P^t↦P^t+F·f^[X]⊗ξ (Remark 4.6) keeps H, C, the first layer and zero top, and changes a'↦a'+ξ·f^[ρ]; so F²|a can be destroyed without changing C̃;
- the converse is not shown: achieving F²|a for a given C̃ would need a'∈(F)+I_ρ.
- [v2: FIX-2] v1 justified this with "P^t↦P^t+f^[X]⊗η, η arbitrary (not a syzygy), R18-T Prop. 2.4". That was wrong: for non-syzygy η the change breaks zero top unless F|η·f^[ρ], and it changes the first layer unless η|_{Γ'}=0. R18-T Prop. 2.4 concerns syzygies only.

This answers target (a) as follows:
- 𝔉_D∩{F∤h} does not lift;
- for 𝔉_D∩{F|h}, Thm 3.1 and Cor. 4.2 impose no condition on C̃ beyond those of R21; the new necessary condition is on the top a of P [v2: FIX-2: v1 said "every C̃ is still possible at the C-level"];
- whether the members with F²|a lift is OPEN.

**Remark 4.4 (the exact content of FN at a good u, constant twist; PROVED decomposition, HEURISTIC non-determination [v2: FIX-1]).** By Step 1 of Thm 3.1, FN along ℓ_u is equivalent to the conjunction of:
- (α) TSYC, b^{[X],t}C_c(Y)b^[ρ]≡0 on ℓ_u;
- (β) the congruence of Thm 3.1(iv) modulo t^X;
- (γ) ω^[X]×y_u = t^{−ρ−X}J^{[X]}m, with m as in Step 1.

(α) and (β) involve only the canonical data (C, a). (γ) prescribes y_u=P_c^tω^[ρ]/F modulo ω^[X], in terms of (C, a).
- **PROVED [v2: FIX-1].** (γ) is solvable for y_u∈k[[t]]³ iff (α) and (β) hold, and the J-part of the solution is automatically consistent. Proof: dotting t^X·(γ) with u^[X] gives b^{[X],t}ΩJ^{[X],t}y_u=κ_0^{−X}b^{[X],t}C_cb^[ρ], and J^{[X],t}y_u=κ_0^{−X}ΩC_cb^[ρ] by Lemma 2.1(iii); the functional b^{[X],t}Ω has kernel spanned by b^[X]. Hence FN at u ⟺ (α)∧(β)∧(one scalar condition per t-order on the f^[X]-component of y_u).
- **HEURISTIC [v2: FIX-1; v1 labelled this PROVED].** That this f^[X]-component carries no further (C,a)-information, i.e. that (β) is the full (C,a)-content of FN modulo t^X. With (C, a, first layer) fixed, the only freedom is P^t↦P^t+F·f^[X]⊗ξ with F|ξ·f^[ρ]. This changes y_u by f^[X](ξ·ω^[ρ]), a restricted family, so non-determination is not proved.
- [v2: FIX-1] v1 also said that any further exclusion "must use (γ)". This is true but tautological, since FN ⟺ (γ).

**Remark 4.5 (what FN forces on the transverse layer in (𝒦)∧F²|a; PROVED statement, use HEURISTIC).** Assume a constant twist, (𝒦) and F²|a_P, F²|a_R, and write C_cBc=FW_c.
- FN gives W=P_c^tu^[ρ]=μu^[X]. Applying J^{[X],t} and Lemma 2.1(i) gives μ=F²t^{ρ−X}·(unit factor times the coefficient of ΩW_c on Ωb^[X]).
- From g^ρW=a_cf^[X]+t^ρFy_u it follows that y_u=P_c^tω^[ρ]/F=O(t^{e_u−X}) along ℓ_u. Equivalently, P_c(Y(t))^tω(t)^[ρ] vanishes to order >=2e_u−X at every good u.
- This is a statement about P's transverse layer, not about (C,a). Turning it into a count needs a new invariant of that layer (HEURISTIC; compare R16 §5's "recursion of depth <=M'/(2E−2)").

**Remark 4.6 (G5).**
- (PROVED) G5 is used nowhere in this note.
- (PROVED) The modification P^t↦P^t+F·f^[X]⊗ξ keeps H_P, C_P, the Γ'-data and the slope set. It changes a_P by F·(ξ·f^[ρ]); so F²|a_P is kept iff F|ξ·f^[ρ]. It changes W along ℓ_u by F·f^[X](ξ·u^[ρ]), i.e. it enters (γ).
- (HEURISTIC) G5 is a Zariski-open condition on (P,R), and the transverse freedom above is large. So G5 is unlikely to obstruct 𝔉_D∩{F|h, F²|a} by itself. This was not checked against (γ).

---

## 5. Non-constant twists: (R1) and (𝒦_ψ)

**Lemma 5.1 (the own-line order in terms of 𝔮; PROVED).** Let u be good, with a non-constant twist.
- (a) If 𝔮>S, then δ_u>=X−1. Hence ord_{z(u)}(V_u|_{ℓ_u})>=X−ρ, and V_u(z(u))=0, so 𝔡(u)=0.
- (b) If 𝔮<=S and u∉𝔅_0, then δ_u>=min(ρ𝔮−1, X). Hence ord_{z(u)}(V_u|_{ℓ_u})>=min(X−ρ, ρ𝔮−1)>=2.
- (c) If 𝔮<=S and u∈𝔅_0, then only δ_u>=0 holds.

*Proof.* Use E−X=(2r−1)X=(2r−1)ρS, ν_u∈ρ𝔮·Z_{>=1}∪{∞}, e_u∈{E,E+1} (Lemma 2.2) and ν_u>=e_u−X if ν_u<e_u (Thm 3.1(i)).
- **(a)** ρ𝔮 is a multiple of 2ρS=2X, and E−X is an odd multiple of X. So the least multiple of ρ𝔮 that is >=E−X is >=2rX=E. Hence min(ν_u,e_u)>=E. So δ_u>=X if e_u=E, and δ_u>=X−1 if e_u=E+1. Also X−ρ<=X−1.
- **(b)** Here ρ𝔮 | E−X.
  - If e_u=E+1, then ν_u>=E−X+1, so ν_u>=E−X+ρ𝔮 and δ_u>=min(ρ𝔮−1, X).
  - If e_u=E and u∉𝔅_0, then ν_u≠E−X, so ν_u>=E−X+ρ𝔮 (or ν_u>=E) and δ_u>=min(ρ𝔮, X).
- **(c)** Immediate. ∎

**Lemma 5.2 ((𝒦_ψ) with k_22≢0 is counted by the own-line order; PROVED, conditional on R21 Remark 3.4).** Assume (𝒦_ψ). Let 𝔊 be a set of good u with β(u)≠0 and m'_u:=min(ord_{z(u)}(V_u|_{ℓ_u}), e_u, ρ𝔮)>=2 for u∈𝔊. If k_22≢0, then
      |𝔊| <= a·d' + ρ·deg[T] + 2g−2 + 2deg ψ.

*Proof.*
- **The identity.** R21 Remark 3.4 gives, in a local frame of 𝓣^{ρ𝔮} at u,
      V_u(z(v)) = κ_u[ β(u)(ψ(v)+ψ(u))k_22(v) + 𝒞_c(v)(B(u)+B(v))c ],   c=c(u).
- **Orders.** As a function of v∈Γ̃ near u:
  - the left side has order >=min(ord(V_u|_{ℓ_u}), e_u). This is the graph argument of Thm 3.1 Step 4: z is a local isomorphism at u and Γ' is smooth there with contact e_u.
  - the B-term has order >=ρ𝔮, since B(v)−B(u)=(B̂(v)−B̂(u))^{[ρ𝔮]} in the frame.
  - Hence ord_u[(ψ−ψ(u))k_22]>=m'_u. ψ is regular at u because β(u)≠0, and ψ−ψ(u) has order e_ψ(u) (the ramification index; ψ is separable since ψ∉K², R14.1). So ord_uk_22>=m'_u−e_ψ(u)>=2−e_ψ(u).
- **Summation.** Sum over u∈𝔊, taking a nonzero component of k_22 (a section of z^*O(a)⊗𝓣^{ρ𝔮}, of degree ad'+ρ·deg[T]):
      Σ_{u∈𝔊}(2−e_ψ(u)) <= ad'+ρ·deg[T].
  Riemann–Hurwitz gives Σ_u(e_ψ(u)−1)<=deg Diff=2g−2+2deg ψ. ∎

**Theorem 5.3 ((R1) is excluded when 𝔮>S; (𝒦_ψ)∖(𝒦) likewise; PROVED, conditional on Thm 3.1, Lemma 5.1, Lemma 5.2, R21 Lemma 3.2 and R18 §5; numbers COMPUTED).** Assume a non-constant twist in 𝔇_16 with 𝔮>S. Then:
- (i) 𝔡≡0, i.e. (𝒦_ψ) holds. Otherwise
      N_good <= charges + deg 𝔡² <= 0.147704q [v2: FIX-6].
- (ii) In (𝒦_ψ), k_22≡0, i.e. (𝒦) holds. Otherwise
      N_good <= charges + deg ψ + ad' + ρ·deg[T] + 2g−2 + 2deg ψ <= 0.104306q [v2: FIX-6].
- Here charges = Nd + 2deg[T]/𝔮 + (1.5d²+3.5d+1) + 6d_def + 7, and ρ·deg[T]<=Nd+ρd (R18 §5).

Consequences:
- Every non-constant twist outside (𝒦) with 𝔮>S is excluded. That is (R1)∩{𝔮>S}.
- Since 𝔮>=128 in 𝔇_16, **all of (R1) is excluded when S=64.**
- Every (𝒦_ψ)∖(𝒦) model with 𝔮>S is excluded.

*Proof.*
- **(i)** By Lemma 5.1(a), 𝔡(u)=0 at every good u. If 𝔡≢0, R21 Lemma 3.2(iii) allows at most deg 𝔡²=2deg ψ+2ad'+2ρ·deg[T] such u.
- **(ii)** By Lemma 5.1(a), m'_u>=min(X−ρ, E, ρ𝔮)>=2 at every good u. Apply Lemma 5.2 to the good u with β(u)≠0; the zeros of β̃ number <=deg ψ. If k_22≡0, then (𝒦_ψ) gives k_11=ψk_22=0 and k_12=0, i.e. (𝒦) (R21 Lemma 3.2(iv)).
- **Numerics.** Use deg ψ<=(E+1)d, 2g−2<=d²−3d, deg[T]<=Nd/ρ+d, 𝔮>=128, and the normalisation of Cor. 4.1. Every term over q is non-increasing in r, Q, S, n. The corner values are 32480243592761/219902325555200≈0.147703 and 114684856407837/1099511627776000≈0.104305, both <1551/4000. ∎

**Corollary 5.4 ((R1) and (𝒦_ψ) for 𝔮<=S; PROVED).** For a non-constant twist with 𝔮<=S, the conclusions of Thm 5.3 hold unless
      |𝔅_0| > (1551/4000 − 0.14770305)q ≈ 0.240047q [v2: N6].
For (𝒦_ψ)∖(𝒦) alone, the threshold is |𝔅_0| > (1551/4000−0.10430527)q≈0.283445q [v2: N6].

*Proof.* By Lemma 5.1(b), good u∉𝔅_0 have own-line order >=2. Run Thm 5.3 with 𝔅_0 added to the charges. ∎

So the open part of (R1) after this note is **𝔮<=S with a positive proportion of good points in 𝔅_0**. At such points:
- the contact is exactly E;
- Ξ(u,·) vanishes at u to the minimal allowed order E−X exactly, i.e. ord_uσ_u=(2r−1)S/𝔮.

**Proposition 5.5 (non-constant twists via the osculation of V=span(t̂_ij); CONDITIONAL on the order sequence, PROVED otherwise; numbers COMPUTED).** Let T be a non-constant twist, inside or outside (𝒦). Let V:=span(t̂_ij)⊂H⁰(𝓣), base-point free, of dimension r_V+1∈{2,3,4}, with order sequence ε_0=0<ε_1<…<ε_{r_V}. Take 𝔮 maximal, so the map [t̂_ij] is separable and ε_1=1. If ε_{r_V}<N_0=⌈(2r−1)S/𝔮⌉, then
      N_good <= charges + 2deg ψ + [ (Σ_iε_i)(2g−2) + (r_V+1)τ_0 ] / (N_0−ε_{r_V}).
- **Pencil case (unconditional).** If dim V=2, then ε=(0,1). The hypothesis is N_0>=2, i.e. 𝔮<(2r−1)S, and the bound over q is <=0.049195 [v2: FIX-6].
- **Classical case.** If V is classical (ε_i=i) and N_0>=4, i.e. 𝔮<(2r−1)S/3, the bound over q is <=0.068733 [v2: FIX-6].
- In both cases the model is excluded.

*Proof.*
- **σ_u is a member of V.** By R19 Lemma 3.5(i), σ_u=Σ_{ij}ŵ_iĉ_jb̂_ij∈V. By Lemma 3.5(ii), σ_u≢0 except at <=2deg ψ good points.
- **Contact at each good point.** By Cor. 3.2, ord_uσ_u>=N_0, so the top vanishing order satisfies j_{r_V}(u)>=N_0.
- **Weierstrass count.** By Stöhr–Voloch (CITED: j_i(P)>=ε_i at every P, and deg R=(Σε_i)(2g−2)+(r_V+1)deg 𝓣), each such u contributes v_u(R)>=j_{r_V}(u)−ε_{r_V}>=N_0−ε_{r_V}>=1.
- **Separability.** If all ratios t̂_ij/t̂_kl were squares, then T would be a 2𝔮-th power projectively, contradicting maximality. So the map is separable, and for r_V=1 this gives ε=(0,1).
- **Numerics.** τ_0<=(Nd/ρ+d)/128, and the remaining terms are as in Thm 5.3. ∎

*Remarks.*
- Prop. 5.5 is CONDITIONAL in general, because the twist's linear system may be Frobenius non-classical, with ε_{r_V} a large power of 2. In characteristic 2 this is the expected obstacle, so the general case is OPEN.
- It reduces every non-constant twist with 𝔮<(2r−1)S/3, in (𝒦) or not, to that non-classical situation.

**Remark 5.6 (per-point gain in R19/R20; PROVED statement, impact HEURISTIC).**
- deg σ_u=τ_0, and σ_u has a zero of order >=N_0 at u. So the residual count of R19 Lemma 3.5 improves from τ_0−1 to N_Ξ(u)<=τ_0−N_0 (σ_u≢0).
- Since N_0<=(2r−1)S/128≪E, this does not move any threshold of the R20 table. Not recomputed.

---

## 6. What remains, and next steps

**Residual after R22** (inside 𝔇_16, global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128; v2, after the v1 audit):
- **Constant twist.** Only (𝒦) with a>=d' (n>=512) and F²|a_P, F²|a_R remains. That is:
  - D∈{1,2}: 𝔉_D∩{F|h}∩{F²|a};
  - D>=4: n<4D, (𝒦), F²|a.

  Everything outside (𝒦) is closed (Cor. 4.1).
- **(R1)** (non-constant, outside (𝒦)): only 𝔮<=S with |𝔅_0|>0.240q remains (S>=128 necessarily). [v2: FIX-7] (R1) with dim V=2 is closed entirely: 𝔮>S by Thm 5.3, and 𝔮<=S<(2r−1)S by the unconditional pencil case of Prop. 5.5. Conditionally on a classical V (with N_0>=4), only the Frobenius non-classical V with ε_top>=N_0 remain.
- **(R2)** (non-constant in (𝒦)): as in R20 v2.1 Cor. 5.3, except that [v2: FIX-7] every twist with dim V=2 and 𝔮<(2r−1)S is now excluded (Prop. 5.5, pencil case, PROVED). The classical case of Prop. 5.5 is CONDITIONAL. Remark 5.6 also applies.
- **(𝒦_ψ)∖(𝒦):** closed for 𝔮>S. For 𝔮<=S, open only with |𝔅_0|>0.283q.

**Next steps (HEURISTIC).**
1. **Constant (𝒦)∧F²|a.** Exploit (γ) of Remark 4.4. It fixes the f^[X]-component of the transverse layer y_u=P_c^tω^[ρ]/F at every good u, and there are >0.388q of them. If that component is shown to be the restriction of a section of bounded degree, these pointwise equalities become an identity on Γ'. That would start the S-layer recursion with an explicit invariant: zero top of S, i.e. F²|a, is its first step.
2. **𝔅_0.** At u∈𝔅_0 the slope function c(u)^t𝒜(v)c(u)^[Q] vanishes to exactly order E−X. Combined with Cor. 3.2 at *all* good points, this is a strong osculation condition on the curve [t̂_ij]. The tool is Stöhr–Voloch with the Frobenius-twisted hyperplanes H_u (coefficients ŵ⊗ĉ depend on c(u) only). It should handle the non-classical case, because H_u is constrained to the rank-one locus ŵ⊗ĉ.
3. **No gain for R20 Lemma 4.2 inside (𝒦) (PROVED comparison).** Off 𝔅_0, Lemma 5.1 gives own-line order >=min(X−ρ, ρ𝔮−1), and R20 Lemma 4.1 already gives min(ρ𝔮,E). For 𝔮<=S, min(X−ρ,ρ𝔮−1)<=ρ𝔮=min(ρ𝔮,E). For 𝔮>S, R20's m=min(ρ𝔮,E)>=X−ρ. So Thm 3.1 does not raise R20's m; (R2) needs a different input.

---

## 7. Computations (`scripts/`; all `python3 -I`, single process, each < 20 s)

| script → output | content | result |
|---|---|---|
| `gf2k.py` | helper: exact GF(2^m) (m=8 and 12, primitive moduli asserted), polynomials in t, nullspace over GF(2^m) | — |
| `toy_vector_FN.py` → `.out` | (★) on random data. FN along one own line imposed as a GF(2^8)-linear system on P^t=f^[X]⊗κ̃+F(J^[X]C''J^{[ρ],t}+f^[X]⊗ξ), a family satisfying common image, alignment and TSY but realising only C=Ω(J^{[X],t}J^[X])C'' (not the most general P [v2: FIX-8]). The first layer κ̃ is constant (A), slope-violating (B) or non-constant (C). Header-corrected copy `toy_vector_FN_v2.py` → `toy_vector_FN_v2.out`, byte-identical to v1's output | (★) holds in every case. (A) 5/5 cases: every sampled solution has ord C_cb^[ρ]=X−ρ exactly, the bound is attained, and the congruence (ii) holds. (B) FN unsolvable. (C) observed order = predicted min(X−ρ, X+ord s̃−e) in 3/3 solvable cases; the one unsolvable case is the trivial pole case ord s̃+X<e [v2: FIX-8] |
| `contact_check.py` → `.out` | Fermat σ1 model (e=standard Cremona, Γ: U_0^{E−1}+U_1^{E−1}+U_2^{E−1}=0). Hensel branches at all points predicted to have e_u=E+1, plus a sample of the others | E∈{8,32} over GF(2^8), E∈{8,16} over GF(2^12): every checked point has e_u∈{E,E+1}, with E+1 iff y_1^[E]·e(u)=0. For E=16 over GF(2^12): 450 points with E+1, 61 sampled with E. (E=16 has no points with x_0y_0≠0 over GF(2^8)) |
| `numerics_R22.py` → `.out` | exact Fractions over r∈{4,…,64}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12}, dyadic 256<=n<4Q (1260 rows): bounds of Cor. 4.1, Cor. 4.2, Thm 5.3 (i),(ii), Prop. 5.5 (classical, pencil) | max/q = 0.046094, 0.092972, 0.147703, 0.104305, 0.068732, 0.049194 (6-decimal truncations as printed by the script; rounded-up bounds 0.046095, 0.092972, 0.147704, 0.104306, 0.068733, 0.049195 [v2: FIX-6]), all at (4,128,64,256), all <0.38775 |

Checksums: `scripts/SHA256SUMS.txt` (delivered to the audit as `owner_scripts/` [v2: N8]).

*Caveat on the toy.* `toy_vector_FN.py` works on one line with polynomial P. In control (C) it uses F(t)=t^e, so that a polynomial S is the local S of Lemma 2.4. With residual zeros of F on the line, a polynomial S cannot absorb a non-constant layer; this is a toy artefact, as the first run showed. Case (A) uses F with residual zeros and e_F=3<X, which is harmless since F cancels for a constant layer (s̃≡0) [v2: FIX-8]. In (C), the only unsolvable case is the trivial pole case ord s̃+X<e; the non-trivial gap cases e−X−ρ<=ord s̃<e−X are covered by the audit's independent toy with a general second layer S (unsolvable with alignment, solvable without) [v2: FIX-8]. The toy checks the algebra of Prop. 2.3 and Thm 3.1 on a restricted family of P. It is not an original model and says nothing about existence.

---

## 8. Status

| item | status |
|---|---|
| Lemma 2.1 (identities on ℓ_u) | PROVED (from FNAM1, TSYC, R18-T Lemma 2.1) |
| Lemma 2.2 (e_u∈{E,E+1} at good points) | PROVED; COMPUTED (Fermat σ1, GF(2^8), GF(2^12)) |
| Prop. 2.3 (vector own-line identity (★)) | PROVED; COMPUTED. Remark after it corrected [v2: FIX-3] |
| Lemma 2.4 (local splitting along ℓ_u; (iv) local proof of F\|a) | PROVED [v2: FIX-5] |
| Thm 3.1 (regularity ord s̃_u>=e_u−X; exact congruence mod t^X; order >=min(X−ρ,δ_u); constant twist: >=X−ρ) | PROVED (R16.1, R18-T 1.1/1.2/2.1, Lemma 2.4(iv), FNAL/TSY/TSYC/FNAM); COMPUTED (sharp in toy; independent audit toy) |
| Cor. 3.2 (ord_{v=u}Ξ(u,v)>=E−X; ord_uσ_u>=⌈(2r−1)S/𝔮⌉) | PROVED; first bullet already derivable from R16.2 + R19 Lemma 3.5 [v2: FIX-4] |
| Cor. 4.1 (constant twist outside (𝒦) excluded, all D, all n; includes 𝔉_D∩{F∤h}) | PROVED; bound <=0.046095q COMPUTED, whole strip by monotonicity |
| Cor. 4.2 (constant (𝒦): F²∤a ⇒ excluded) | PROVED; <=0.092972q COMPUTED |
| Prop. 4.3 (necessary conditions for liftable 𝔉_D; F²\|a not implied by C̃) | PROVED (necessary only); sufficiency OPEN [v2: FIX-2] |
| Remark 4.4 (exact content of FN at u: (α),(β),(γ)) | decomposition PROVED; "(β) is all (C,a)-level content mod t^X" HEURISTIC [v2: FIX-1] |
| Remark 4.5 (in (𝒦)∧F²\|a: P_c^tω^[ρ]=O(t^{2e_u−X}) along ℓ_u) | PROVED; use HEURISTIC |
| Remark 4.6 (G5 not used; transverse freedom) | PROVED parts as marked; "unlikely to obstruct" HEURISTIC |
| Lemma 5.1 (own-line order vs 𝔮; 𝔅_0) | PROVED |
| Lemma 5.2 ((𝒦_ψ)-count via own-line order) | PROVED (R21 Remark 3.4, Riemann–Hurwitz) |
| Thm 5.3 ((R1) and (𝒦_ψ)∖(𝒦) excluded for 𝔮>S; all (R1) at S=64) | PROVED; <=0.147704q / <=0.104306q COMPUTED [v2: FIX-6] |
| Cor. 5.4 (𝔮<=S: excluded unless \|𝔅_0\|>0.240047q, resp. 0.283445q) | PROVED |
| Prop. 5.5 (osculation of V; pencil case unconditional, in (R1) and (R2)) | CONDITIONAL on ε_top(V)<N_0; PROVED for dim V=2 [v2: FIX-7]; numbers COMPUTED [v2: FIX-6] |
| Remark 5.6 (N_Ξ(u)<=τ_0−N_0) | PROVED; impact HEURISTIC |
| constant (𝒦)∧a>=d'∧F²\|a (incl. 𝔉_D∩{F\|h}); (R1) on 𝔅_0 for 𝔮<=S with dim V>=3; (R2) with dim V>=3 or 𝔮>=(2r−1)S | OPEN |

Dependencies: R21, R20, R19, R18-T, R16 (all v2.1, audited and revision-checked); PRIMARY FNAL/TSY/TSYC/FNAM/FNAN/FNAO (reviewed). The PRIMARY results remain PRIMARY's. The idea of keeping FNAL's forgotten span(f^[X]) component is FNAL §4's own pointer. The F·S layer is R16 §5 item 1. v1 was independently audited (PASS-with-fixes); this v2 applies FIX-1..8 and N1–N4, N6–N8, and has not been revision-checked. No manuscript was edited. The classification of hyperovals is not claimed complete.
