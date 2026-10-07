# HYP M>=2, round 18-T (v2.1): the non-constant twist in 𝔇_16 — a reduced second-layer cover, the kernel-aligned case, and the decoupling of the two layers

7 October 2026. Claude HYP(2) research note for session_012ij7YN37LGpSS88rmUGQ7E, written as the R18 §8 follow-up ("does rigidity force constant mixing?"). Scripts: this directory (`numerics_twist.py`, `toy_checks.py`, outputs `.out`). No file whose name contains "DZ" was opened. Nothing under any `src/` or `zips/` directory was executed (the PRIMARY `.md` sources were read only).

**Version history.**
- v1: owner draft.
- v1 audited by an independent referee (`AUDIT_HYP_M2_ROUND18T_20261007.md`): PASS-with-fixes, one substantive fix (FIX-1) and six wording, bookkeeping or citation fixes (FIX-2..7).
- **v2** applies FIX-1..7 and the minor notes N1, N3–N8 and N10. The changes, by fix:
  - **FIX-1.** (H_bs) never holds in 𝔇_16, because Γ' passes through every proper base point of f. It is replaced by the polynomial-lift hypothesis (H_lift), which is OPEN. The "(PROVED) identities cannot force constancy" claim is relabelled CONDITIONAL/HEURISTIC.
  - **No change to §§3–4 statements, proofs or numbers.** Theorem 3.4, Cor. 3.5 and §4 do not depend on §2. The only edits there are wording: FIX-3, FIX-5, and the N4 remark after Prop. 4.2.
  - **Changes are marked.** Each change is marked "[v2: FIX-n]".
- v2 revision-checked by a fresh referee (`REVISION_CHECK_HYP_M2_ROUND18T_V2_20261007.md`): PASS-with-fixes. FIX-1..7 are all ADDRESSED; seven revision items RC-1..7 were raised.
- **v2.1 (this file)** applies RC-1..7, marked "[v2.1: RC-n]":
  - Lemma 2.1A now has a self-contained proof (RC-1).
  - N2 is applied in Lemma 1.2 (RC-3).
  - N9 concerns script comments only and is deferred: the scripts are unchanged (RC-3).
  - No statement, label or number changes.

Inputs (read, not re-proved; review status updated in v2 [v2: FIX-4]):
- R16 v2.1, R17 v2.1, R18 v2.1 (`HYP_M2_ROUND18_v2_1.md`: audited PASS-with-fixes, revision-checked, fixes applied).
- PRIMARY FNAK, FNAL, TSY, TSYC, FNAM, FNAN, FNAO, FNAP (owner hand proofs), as reviewed in `CLAUDE_REVIEW_PRIMARY_FNAK_FNAL_FNAM_FNAN_FNAO_FNAP_20261007.md`:
  - FNAK, TSY, TSYC, FNAM: PASS;
  - FNAL, FNAN, FNAO, FNAP: PASS-with-fixes (FIX-L1–L4, FIX-N1).

Notation warning [v2: N1]:
- T denotes both the twist matrix and the integer QS. The integer appears only in exponents and in X=T/2, Q−1+T−D and (T−D)/(Q−1).
- a denotes deg C_•, except in 𝔮=2^a.
- D denotes the reduced exponent 2^t. The R16/FNAM3 function c·e(u) is written D only where it is cited.
- [v2.1: RC-6] S denotes both the integer in E=rQS and the polynomial ring k[Y_0,Y_1,Y_2] (§2).
- [v2.1: RC-6] g denotes the function with f(e(U))=g·U (FNAN §1), the degree-(m−ρ𝔮) form in Cor. 2.3, and the polynomial g(w) in Lemma 3.2. Context disambiguates.

Labels:
- **PROVED**: full proof given here (owner proof; v1 independently audited, v2 revision-checked). A PROVED statement is conditional on the inputs it names.
- **CONDITIONAL**: proved under a named hypothesis that is not established.
- **COMPUTED**: exact finite-field or exact-rational computation. It illustrates; it proves only where an exact rational bound is evaluated.
- **HEURISTIC / OPEN**: as stated.

---

## 0. Summary

**Setting.** 𝔇_16 in the R16 setting (global top alignment, common source image on Γ', zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE), so that FNAL/TSY/FNAM apply. By R18 Thm 4.2(iv) the source rows are a K^𝔮-twist of the e-pencil, 𝔮>=128. Write S=Q^jD with D=2^t<Q (FNAP's reduced exponent).

**What is proved.**

1. **Non-constant CMIX normal form (PROVED, §1).** On Γ, (ϰ_P,ϰ_R)^t=λ·𝒜·(E_P^[ρ],E_R^[ρ])^t with 𝒜=(T^t)^[ρ]∈GL_2(K^{ρ𝔮}). PRIMARY's slope equation c^t𝒜(u)c^[Q]=0 holds pointwise at good points and equals R18's 𝔉(u)^ρ=0. Equivalently c(u)^[Q]∥B(u)c(u), B:=swap·𝒜^t.

2. **Layer identity (PROVED, §2).**
   - [f^[X]]_×=κ_0^X J^[X]ΩJ^[X,t], hence J^[X,t]P^t=κ_0^{−X}F·ΩC_PJ^[ρ,t].
   - The first layer (the twist) and the second layer (C_P,C_R) are **formally decoupled** (Prop. 2.4, PROVED). For any polynomial syzygy η of f^[ρ], the change P^t↦P^t+f^[X]⊗η preserves global alignment, common image, zero top, H_P, C_P, G_c and FNAM2, and it adds η to the first-layer row.
   - [v2: FIX-1] Whether this can turn a constant twist into a non-constant one depends on (H_lift) below, which is OPEN. So the v1 claim "no argument using only these identities can force T constant" is downgraded to CONDITIONAL on (H_lift), and HEURISTIC as a methodological statement (Remark 2.5).

3. **Polynomial origin (option (1), CONDITIONAL on (H_lift), negative).** [v2: FIX-1]
   - Suppose ϰ_P lifts to a polynomial syzygy: (H_lift), which is OPEN.
   - The v1 sufficient condition (H_bs) **never holds**, since Γ' passes through every proper base point of f. Also, (H_lift) forces P(q)=R(q)=0 at those base points.
   - Under (H_lift), [T^ρ] is cut out on Γ' by four forms of degree m=M'−2X−ρ, which gives ρ·deg[T]<=m·d'<Nd.
   - That is the R18 §5 height bound again (used in R18 §8.1), and it does not force constancy: non-constant ρ𝔮-th-power ratios of degree-m forms exist on every plane curve once ρ𝔮<=m (Cor. 2.3).

4. **A reduced second-layer cover for every twist (option (2), PROVED, §3).**
   - Substituting the first layer pointwise into FNAM's G_c(Y) and restricting to the own line gives sections 𝔊_k (k>=0) of explicit degree. Each vanishes at every good point off the exceptional set of Lemma 3.1 [v2: N7].
   - **Dichotomy (Prop. 3.3).** Either some 𝔊_k≢0 with k<D, or the source pencil is **kernel-aligned** (𝒦): C_c(e(U))·B·c=0 in K² for every c∈k².
   - **Generic own-line non-divisibility (Prop. 3.3(b)).** Some 𝔊_k with k<D⌈(a+1)/D⌉ is always ≢0, for every twist, constant or not, when D>=4. The proof is a K^D-linear-independence argument for powers of γ=ψ^{1/2} at the generic point, followed by FNAP's disjoint-support algebra over k[t] and FNAM2.

5. **Height-bounded twists are excluded (Thm 3.4, PROVED; numbers COMPUTED exactly).** Outside 𝒦, with D>=4,
       N_good <= Nd + 2deg[T]/𝔮 + |𝔈| + (D+2)(E+1)d + 4ad + 2(D−1)(E−2)d + Q·deg[T]·(Q−1+T−D)/(Q−1) + 6d_def + 7.
   Hence 𝔇_16 is excluded whenever deg[T]<=θ_max·rh. For example:
   - θ_max>=0.2497 for D=4 at every strip scale;
   - [v2: FIX-5] D has a nonempty low-height closing window (θ_max>0) exactly when D<=n/16, for n=h/E=256,…,8192. That is D∈{4,8,16} at n=256, D<=32 at 512, D<=64 at 1024, D<=128 at 2048, D<=256 at 4096 and D<=512 at 8192. These values come from the referee's grid; the v1 owner grid stopped at D=64. For such D only deg[T]<=θ_max·rh is closed, not the whole case.

   Constant T (deg[T]=0) is included. That recovers a FNAP-type exclusion for those D outside 𝒦.

6. **The kernel-aligned case (§4).**
   - 𝒦 forces F | det(v_1C_P+v_2C_R), and it determines the columns of B (hence [T^ρ]) as kernel vectors of C_P(Z), C_R(Z) on Γ'. In 𝒦 the reduced second layer vanishes on the own line to order >=min(ρ𝔮,E) automatically.
   - 𝒦 is **excluded when 2a<d'** (sufficient: M<6E−T+Q−5), by FNAM2 (Prop. 4.2).
   - For 2a>=d', 𝒦 is formally realisable with non-constant T (Example 4.3, COMPUTED). It is OPEN.

**What failed.**
- Constancy of T is not proved.
- [v2: FIX-6] The reduced cover is expensive in deg[T].
  - The half-section 𝔊_k costs ≈X·deg[T]=T·deg[T]/2, from the Frobenius-iterated twist B_{j+1}^[D].
  - The counted section 𝔊_k² carries Q·deg[T](Q−1+T−D)/(Q−1)≈T·deg[T]=2X·deg[T].
  - That is what closes only deg[T]<=~0.25rh.
- The a-priori range is deg[T]<=e_M+d<=Nd/ρ+d≈0.0512·S·rh (R18 §5), with S>=64. So a window 0.25rh<deg[T]<=0.0512S·rh of non-constant twists survives, together with 𝒦 for large M and D∈{1,2} (as in FNAP).
- Polynomial origin, even granted (H_lift), gives no height improvement over R18.
- [v2: FIX-1] The v1 "identities cannot force constancy" obstruction is not established. It rested on (H_bs), which never holds.

**Most promising next step (HEURISTIC, §6).** Exploit the **residual intersection points** of the own line with Γ'. Line divisibility gives Π_u(e(u_i))=0 at the other points e(u_i)∈ℓ_u∩Γ' as well, and in 𝒦 the kernel identity holds at u_i with B(u_i). That compares B(u) with B(u_i) along the correspondence {(u,v): u^[E]·e(v)=0}. If the C-kernels are one-dimensional there, T̂ would be invariant under this correspondence, which should force constancy. Second, attack the height window by bounding deg[T] through the second layer: in 𝒦, B is a kernel of C(Z), which suggests a lower-height description.

---

## 1. Setting and the non-constant CMIX normal form

**Standing hypotheses (CITED).**
- 𝔇_16 as in R16 §6/R17 Def. 6.1, in the R16 setting with **global** top alignment (needed for FNAL), common source image on Γ', zero top, first scalar order ρ, all original gates G0–G11, PRIM, G5.
- Pure: ϰ_•=λ_ϰM_•^[ρ] (R16 Lemma 5.5). Nondegenerate, ε_1=1, ε_2=𝔮=2^a, non-cuspidal, with 𝔮>=128 after R18 Cor. 5.5.
- R18 Thm 4.2(iv): M_P=λ(T_11E_P+T_21E_R), M_R=λ(T_12E_P+T_22E_R), with T∈GL_2(K^𝔮), E_P=L^te(U), E_R=N^te(U).
- Normalise T=T̂^[𝔮], where the entries t̂_ij of T̂ are sections of a line bundle 𝓣 without common zero, and deg[T]=𝔮·deg 𝓣 (R18 Lemma 5.3).
- FNAL, TSY, TSYC, FNAM (with FNAM2: Δ(v,Y):=det(v_1C_P(Y)+v_2C_R(Y))≢0 in k[v,Y]); FNAN/FNAO/FNAP as stated by PRIMARY. [v2: FIX-4] Claude referee review: FNAK, TSY, TSYC, FNAM PASS; FNAL, FNAN, FNAO, FNAP PASS-with-fixes (FIX-L1–L4, FIX-N1).
- Parameters: q=Eh, E=rQS, ρ=Q/2, X=T/2, T=QS, N=M−1−X, M'=(M−1)/2, d<=E+2, d'=deg F>=2E−2, a=deg C_•=M'+X−ρ−d'<M'.
- S=Q^jD, with D=2^t, 0<=t<v (Q=2^v).

**Lemma 1.1 (non-constant CMIX; PROVED).** On Γ,
      (ϰ_P,ϰ_R)^t = λ'·𝒜·(E_P^[ρ],E_R^[ρ])^t,   𝒜:=[[T_11^ρ,T_21^ρ],[T_12^ρ,T_22^ρ]]=(T^t)^[ρ],   λ'=λ_ϰλ^ρ.
With 𝒜's entries the sections t̂_ij^{ρ𝔮} of 𝓣^{ρ𝔮}, λ' is regular at every good point off {g=0} and off Bs(e) [v2: FIX-3], and it vanishes at no more than Nd good points.

*Proof.*
- **The identity.** Raise R18 Thm 4.2(iv) to the ρ-th power coordinatewise, and multiply by λ_ϰ.
- **Regularity of λ'.** Let u be a good point with g(u)≠0 and e(u)≠0 [v2: FIX-3; this is FIX-N1 of the PRIMARY review]. Then E_P(u) and E_R(u) are independent (FNAN §1: the maximal minors of J(e(u)) are a nonzero constant times g(u)u). The ϰ_• are regular sections of O(N) (R16.2). Solving for the coordinates of ϰ_• in the basis E_P^[ρ](u), E_R^[ρ](u) shows that λ'·t̂_ij^{ρ𝔮} is regular at u for all i,j. Some t̂_ij(u)≠0, so λ' is regular at u.
- **Zeros of λ'.** If λ'(u)=0, then ϰ_P(u)=ϰ_R(u)=0, so u is a zero of a fixed nonzero entry of ϰ_P or ϰ_R. That gives at most Nd points (FNAN §1). ∎

**Lemma 1.2 (the slope equation is 𝔉; PROVED; COMPUTED in `toy_checks.out` (2)).**
- **Statement.** Let u be a good point off the original boundary and off 𝔈, with λ'(u)≠0 and det T̂(u)≠0. Then c:=(√β:√α)(u) satisfies
      c^t𝒜(u)c^[Q]=0   ⟺   c^[Q] ∥ B(u)c,   B:=[[T_21^ρ,T_22^ρ],[T_11^ρ,T_12^ρ]]=swap·𝒜^t.
- **Relation to 𝔉.** With c=(1:s^ρ), c^t𝒜c^[Q]=𝔉(s)^ρ, where 𝔉(s)=T_22s^{Q+1}+T_21s^Q+T_12s+T_11 is R18's FN normal form.

*Proof.*
- **The slope equation.** FNAO §2's derivation is pointwise. The order-ρ coefficient of R16.2's series at u is c_1ϰ_P(u)·w^[ρ]+c_2ϰ_R(u)·w^[ρ]=0, for a nonradial tangent w. Also (E_P(u)·w,E_R(u)·w) is a nonzero multiple of (β,α)(u)=c^[2] (FNAN §1). Insert Lemma 1.1 evaluated at u; λ'(u)≠0.
- **The kernel form.** The row c^t𝒜(u) is nonzero, since 𝒜(u) is invertible. In characteristic two its kernel is spanned by B(u)c (FNAO §2).
- **Relation to 𝔉.** Expand the product. Constancy of 𝒜 is never used: the point u is fixed.
- [v2.1: RC-3/N2] **The case c_1=0.** At points with β(u)=0, c=(0:1) is not of the form (1:s^ρ). There one uses the homogenised 𝔉, i.e. s=∞, and the statement c^t𝒜c^[Q]=0 is unchanged.
- [v2.1: RC-3/N2] **Identification with R18's 𝔉(u):=𝔉(s_M(u)).**
  - Put W(s):=(T_21+sT_22)/(T_11+sT_12), evaluated at u. Then 𝔉(s)=0 ⟺ W(s)=s^{−Q}. The slope equation is this equation at s=(α/β)^{1/Q}(u), where s^{−Q}=β/α(u).
  - W is injective at u, since det T(u)≠0.
  - W(s_M(u))=β/α(u) by R18 Thm 4.2(iv).
  - Hence the root s of the slope equation is s_M(u). (Checked numerically in the v1 audit, r2 c.) ∎

*Remark 1.3.* For non-constant T the slope set {c : c^t𝒜(u)c^[Q]=0} moves with u. This is exactly where FNAN/FNAO's "at most Q+1 slopes" and their single binary form P(c,Y) break down (FNAO §4 says so).

---

## 2. Option (1): polynomial origin, and the decoupling of the two layers

Notation:
- S=k[Y_0,Y_1,Y_2], with j_1:=L^tY, j_2:=N^tY and J=[j_1,j_2] (FNAM1).
- FNAM1 gives f=κ_0·(j_1×j_2) with κ_0∈k^*.
- I_ρ:=(f_0^ρ,f_1^ρ,f_2^ρ)⊂S, and Ω:=[[0,1],[1,0]].

**Lemma 2.1 (cross-product factorisation and the layer identity; PROVED; COMPUTED in `toy_checks.out` (1)).**
- (i) For every v∈S³, f^[X]×v=κ_0^X·J^[X]ΩJ^[X,t]v.
- (ii) Consequently, with FNAL's H_P and TSY/FNAM's C_P,
      J^[X,t]P^t = κ_0^{−X}·F·ΩC_P·J^[ρ,t],   and likewise for R.
  In particular J^[X,t]P^t≡0 mod F, and C_P is determined by J^[X,t]P^t/F, because the 2×3 matrix J^[ρ,t] has rank 2 over Frac(S).

*Proof.*
- **(i)** Frobenius commutes with the cross product coordinatewise, so f^[X]=κ_0^X(j_1^[X]×j_2^[X]). In characteristic two (a×b)×v=(a·v)b+(b·v)a. Hence (j_1^[X]×j_2^[X])×v=(j_1^[X]·v)j_2^[X]+(j_2^[X]·v)j_1^[X]=J^[X]ΩJ^[X,t]v.
- **(ii)** FNAL gives F·H_P=[f^[X]]_×P^t, and TSY/FNAM give H_P=J^[X]C_PJ^[ρ,t]. By (i), J^[X](κ_0^XΩJ^[X,t]P^t−F·C_PJ^[ρ,t])=0.
- J^[X] has rank 2 over Frac(S) (FNAM1, Frobenius), so it is injective on Frac(S)². Since Ω²=I, (ii) follows. ∎

*Remark.* (ii) says that the second layer is literally J^[X,t]P^t/F, i.e. the two Frobenius-syzygy coordinates of P^t divided by the inverse-curve equation. The first layer is P^t mod F, whose image is f^[X]. These are complementary pieces of P^t.

**Lemma 2.1A (Γ' contains every base point of f; PROVED) [v2: FIX-1].** Let q be a proper base point of the quadratic Cremona map f. Then q∈Γ', and mult_qΓ'>=E−3.

*Proof.* [v2.1: RC-1: self-contained; the argument is from the v1 audit, with the three steps the revision check asked to be justified.]
- **The form.** Put C_f(Z):=Z·f(Z)^[E]. It is a form of degree 1+2E.
- **C_f vanishes on Γ'.** f(e(U))=g·U (FNAN §1), so C_f(e(U))=e(U)·(g^E U^[E])=g^E·(U^[E]·e(U)). The last factor vanishes on Γ: every point u∈Γ lies on its own line, u^[E]·e(u)=0 (R16 §1; this is the diagonal of the own-line incidence). So C_f∘e vanishes on Γ, i.e. C_f vanishes on Γ'=e(Γ). Hence F|C_f.
- **C_f≢0.** C_f=Σ_i Z_i f_i(Z)^E. The i-th summand is Z_i times an E-th power, so all its monomials have Z_i-exponent ≡1 and the other two exponents ≡0 (mod E). For i=0,1,2 these residue classes differ, so the three summands have disjoint monomial supports. No f_i^E is zero, so C_f≠0.
- **F occurs exactly once.** If F²|C_f, then 2d'<=2E+1. That contradicts d'>=2E−2 once E>=4. So C_f=F·C' with F∤C' and deg C'=2E+1−d'<=3.
- **The multiplicity bound.** Every f_i vanishes at the proper base point q, so mult_q(f_i^E)>=E and mult_qC_f>=E. Multiplicities add over products: mult_qC_f=mult_qF+mult_qC'. Also mult_qC'<=deg C'<=3. Hence mult_qΓ'=mult_qF>=E−3>0. (Note that q∈Γ' alone needs only F|C_f and mult_qC'<mult_qC_f; the exact-once step is used for the bound E−3.) ∎

*COMPUTED (audit r2 g1, g2).*
- On Fermat σ1, mult_{(1:0:0)}Γ'=E−1.
- For 8 random centres (E=16), the third zero u* of C_orig on a contracted line of e satisfies g(u*)=0 and e(u*)∈Γ'∩Bs(f).

**Hypothesis (H_lift) (polynomial lift; OPEN in 𝔇_16) [v2: FIX-1].** There are κ̃'_P, κ̃'_R∈Syz(f^[ρ])_{M'−2X} with
      P^t≡f^[X]⊗κ̃'_P   and   R^t≡f^[X]⊗κ̃'_R   (mod F).
*Remark.* (H_lift) is a genuine condition. At a proper base point q of f (which lies on Γ' by Lemma 2.1A), f(q)=0 forces P(q)=R(q)=0. Nothing in the standing hypotheses is known to imply this.

**Proposition 2.2 (polynomial lift of the first layer; CONDITIONAL on (H_lift)) [v2: FIX-1].**
- **Statement.** Assume (H_lift). Then there are forms A_P, B_P, A_R, B_R∈S of degree m:=M'−2X−ρ with
      P^t ≡ f^[X]⊗(A_Pj_1^[ρ]+B_Pj_2^[ρ]) mod F,   R^t ≡ f^[X]⊗(A_Rj_1^[ρ]+B_Rj_2^[ρ]) mod F.
- **The twist on Γ'.** With λ'' a common rational scalar,
      (A_P,B_P,A_R,B_R)|_{Γ'} = λ''·(T_11^ρ,T_21^ρ,T_12^ρ,T_22^ρ).
- **The general case (this is the actual case in 𝔇_16).** Without (H_bs), the two obstructions to the Steps 1–4 construction of a lift are listed below. They are not obstructions to a lift in general: (H_lift) could still hold by other means. [v2.1: RC-5]
  - (a) local non-freeness of (f^[X])O_{Γ'} at the points of Γ'∩Bs(f);
  - (b) the module (I_ρ:F)/I_ρ=Tor_1^S(S/I_ρ,S/F).
  
  Both are supported on Γ'∩Bs(f). By Lemma 2.1A this set is the full set of proper base points of f, so it is never empty. Whether they vanish is OPEN.
- **Superseded v1 hypothesis.** v1 assumed (H_bs): no base point of f lies on Γ'. Steps 1–4 below prove (H_bs)⇒(H_lift). Steps 5–6 prove the statement from (H_lift). By Lemma 2.1A, (H_bs) **never holds** in 𝔇_16. Steps 1–4 are kept only as the record of where the obstructions (a), (b) arise.

*Proof.*
- **Step 1: a section on the scheme Γ'.** Let r_i be the rows of P^t.
  - Common image on Γ' (equivalently [f^[X]]_×P^t≡0 mod F, from FNAL) gives r_if_j^X≡r_jf_i^X mod F.
  - Under (H_bs), on the chart {f_k≠0} of the scheme Γ'={F=0}, κ:=r_k/f_k^X is regular.
  - These local rows agree on overlaps, so they glue to κ∈H⁰(Γ',O_{Γ'}(M'−2X))³.
- **Step 2: lift to S.** H¹(P²,O(M'−2X−d'))=0, so S_{M'−2X}→H⁰(O_{Γ'}(M'−2X)) is onto. Lift κ to κ̃∈S³_{M'−2X}; then P^t≡f^[X]⊗κ̃ mod F.
- **Step 3: κ̃ is a syzygy modulo F.** Global alignment gives P^tf^[ρ]=a_Pf^[X].
  - Zero top on Γ means a_P≡0 mod F: on Γ', P^tf^[ρ]=f^[X](κ·f^[ρ]), and κ·f^[ρ] is a unit multiple of ϰ_P·U^[ρ]=0.
  - Hence f_i^X(κ̃·f^[ρ])≡0 mod F for all i. F is prime and F∤f_i^X for some i, so κ̃·f^[ρ]=F·b with b∈S. (This step does not need (H_bs) [v2: N3].)
- **Step 4: correct by a multiple of F.** S/I_ρ is Cohen–Macaulay of dimension 1: I_ρ is the Frobenius pull-back of the perfect codimension-2 ideal of maximal minors of J, and Frobenius is flat (TSY). Its associated primes are the points of Bs(f).
  - Under (H_bs), F is a nonzerodivisor on S/I_ρ. Since F·b∈I_ρ, we get b∈I_ρ, say b=η·f^[ρ].
  - Then κ̃':=κ̃−Fη is a syzygy of f^[ρ], with P^t≡f^[X]⊗κ̃' mod F still.
- **Step 5: expand in the free basis.** By TSY/FNAM1 (Frobenius flatness), Syz(f^[ρ])=J^[ρ]S², so κ̃'=A_Pj_1^[ρ]+B_Pj_2^[ρ].
- **Step 6: compare with Lemma 1.1.** In Y-coordinates on Γ', ϰ_P corresponds to λ''(T_11^ρj_1^[ρ]+T_21^ρj_2^[ρ]), because E_P=j_1(e(U)) and E_R=j_2(e(U)). The rows j_1^[ρ], j_2^[ρ] are independent at the generic point of Γ', which gives the last display.
- **Where (H_bs) was used.** Steps 1 and 4 are the only uses of (H_bs). Their failures are exactly (a) and (b). Steps 5–6 use only the conclusion of Step 4, i.e. (H_lift). ∎

**Corollary 2.3 (height from polynomial origin; CONDITIONAL on (H_lift)) [v2: FIX-1].**
- **The bound.** ρ·deg[T]<=m·d'.
- **Comparison with R18.** This is the R18 §5 bound deg[T]<=e_M+d<=Nd/ρ+d [v2: N5]. In fact m·d'<=(M−1−4X−2ρ)d<Nd strictly, since d'<=2d. So deg[T]<Nd/ρ, marginally below R18. Polynomial origin gives **no** real height improvement.
- **It does not force constancy.** Take any plane curve Γ' that is not a line, any independent linear forms α_1, β_1, and any form g of degree m−ρ𝔮 (possible when ρ𝔮<=m). Then the forms A=gα_1^{ρ𝔮}, B=gβ_1^{ρ𝔮} have A/B=(α_1/β_1)^{ρ𝔮}|_{Γ'}, a non-constant ρ𝔮-th power.
- **Size of the 𝔮-range [v2: N6].** In 𝔇_16, ρ𝔮<=m requires 𝔮<=2m/Q. That is 𝔮<64E/625≈0.1E only as h→4QE; at h=256E it is <0.0512E (Q=128).

*Proof.*
- **The bound.** By Prop. 2.2, [T^[ρ]] is the restriction to Γ' of the map [A_P:B_P:A_R:B_R], given by forms of degree m. Its pullback degree on the normalisation, which is birational to Γ̃, is <=m·d'. Also deg[T^[ρ]]=ρ·deg[T].
- **The example** is immediate. ∎

**Proposition 2.4 (decoupling of the layers; PROVED).** Let η_P, η_R∈S³_{M'−2X} be any polynomial syzygies of f^[ρ] (η·f^[ρ]=0), and put
      P_η^t:=P^t+f^[X]⊗η_P,   R_η^t:=R^t+f^[X]⊗η_R.
Then:
- (i) global alignment holds with the same a_P, a_R;
- (ii) common image on Γ' holds;
- (iii) zero top holds;
- (iv) H_P, H_R, C_P, C_R, every FNAM polynomial G_c, and FNAM2's Δ are unchanged;
- (v) the first-layer rows become ϰ_•+η_•|_{Γ'} (in Y-coordinates).

In particular, suppose (H_lift) holds (OPEN; [v2: FIX-1], v1 said (H_bs), which never holds) and the original model is pure with twist T. Then the choice
      η_P=−κ̃'_P+g(α_1^{ρ𝔮}j_1^[ρ]+β_1^{ρ𝔮}j_2^[ρ]),   η_R=−κ̃'_R+g(α_2^{ρ𝔮}j_1^[ρ]+β_2^{ρ𝔮}j_2^[ρ])
(with ρ𝔮<=m) produces first-layer rows of the 𝔇_16 normal form with the **non-constant** twist T'=[[α_1^𝔮,α_2^𝔮],[β_1^𝔮,β_2^𝔮]](e(U)), and an **identical** second layer.

*Proof.*
- **(i)** f^[X](η·f^[ρ])=0.
- **(ii)** The added term has image in span f^[X].
- **(iii)** η·f^[ρ]=0.
- **(iv)** [f^[X]]_×(f^[X]⊗η)=(f^[X]×f^[X])⊗η=0, so FNAL's quotient is unchanged. TSY's C is unique given H.
- **(v)** This is the definition of the first-layer row.
- **The example** follows from Prop. 2.2 (under (H_lift)), Lemma 1.1 and E_•=j_•(e(U)). ∎

*Remark (exactly what the decoupling covers) [v2: N10].* Let P' be any matrix with the same second layer as P and the same alignment coefficients a_P, a_R [v2.1: RC-2].
- Then J^[X,t](P'^t−P^t)=0.
- Also ker J^[X,t]=S·f^[X], because its maximal minors κ_0^X f^[X] have grade 2. So P'^t=P^t+f^[X]⊗η with η∈S³ polynomial.
- The equality of the alignment coefficients gives f^[X](η·f^[ρ])=0, i.e. η·f^[ρ]=0, so η is a syzygy. Zero top alone would give only η·f^[ρ]≡0 mod F.
- Hence "same second layer and same a_P, a_R" is the same as "first-layer change within Syz(f^[ρ])".

*Remark 2.5 (obstruction, option (3); relabelled in v2) [v2: FIX-1, FIX-2].* Prop. 2.4 says the global polynomial identities are invariant under an arbitrary change of the first layer within Syz(f^[ρ]). These identities are alignment, common image, zero top, H, C, G_c and FNAM2's Δ, i.e. those used by FNAL/TSY/TSYC/FNAM.

The Γ-local, good-point conditions are **not** invariant: R16.2, Lemma 1.2, FN and FNAN/FNAO's pointwise inputs all couple the first layer at u.

The twist T is first-layer data. Therefore:
- **(PROVED)** every global identity listed is invariant under P^t↦P^t+f^[X]⊗η, η∈Syz(f^[ρ])_{M'−2X};
- **(CONDITIONAL on (H_lift) and ρ𝔮<=m)** this exchanges a constant twist for a non-constant one, with an identical second layer;
- **(HEURISTIC)** hence an argument from these global identities alone can force constancy only by excluding all lift-admitting data with ρ𝔮<=m. That is, it would have to prove those identities inconsistent for such data, which is not ruled out;
- **(OPEN)** (H_lift) itself. It is nontrivial: it forces P, R to vanish at the base points of f, which lie on Γ' (Lemma 2.1A);
- **(OPEN)** whether the original gates G5, PRIM, "first scalar order ρ", nonclassicality and the point count survive such a change. G5 and PRIM are open (Zariski) conditions on P, R; the count is not;
- **consequence (HEURISTIC):** constancy, if true, most plausibly comes from the **point coupling**: the same c(u), u and own line enter both the first-layer equation 𝔉(u)=0 and the second-layer divisibility ℓ_u | G_{c(u)}. §3 builds the cover that uses this coupling.

---

## 3. Option (2): a reduced second-layer cover for every twist

**Definition 3.0.** Put B_1:=B, B_{i+1}:=B_i^[Q]B (entrywise Q-th power, then matrix product), and 𝒦𝓂:=B_{j+1}^[D]. Since T=QS=Q^{j+1}D, the entries are:
- of B: sections of 𝓣^{ρ𝔮};
- of 𝒦𝓂: sections of 𝓣^{ρ𝔮(T−D)/(Q−1)}. The exponent is an integer, since T−D=D(Q^{j+1}−1).

For a free c∈k² and Y∈k³, put
      𝒫(c,Y) := (𝒦𝓂·c^[D])^t · C_c(Y) · (B·c),   C_c:=c_1C_P+c_2C_R,
a polynomial in (c,Y) of bidegree (D+2,a) with coefficients sections on Γ̃. At a point u where B is regular and invertible, 𝒫 specialises to FNAP's polynomial P_D for the constant matrix B(u) (FNAP §2, eq. (1)).

Let c_gen:=(√β̃,√α̃), where α̃, β̃ are sections without common zero of the bundle 𝓐 of (α:β) (deg 𝓐=deg ψ<=(E+1)d). Let Z:=e(U)∈H⁰(O(2))³ and V:=U^[E]×c_0∈H⁰(O(E))³, with a fixed generic c_0∈k³. Define
      𝔊_k := [t^k] 𝒫(c_gen, Z+tV),   k=0,1,…,a.
Since everything is homogeneous of degree D+2 in c_gen, 𝔊_k² is a genuine section on Γ̃:
      𝔊_k² ∈ H⁰(𝓐^{D+2} ⊗ 𝓣^{Q𝔮(Q−1+T−D)/(Q−1)} ⊗ O(2(2(a−k)+Ek))),
      deg = (D+2)deg ψ + Q·deg[T]·(Q−1+T−D)/(Q−1) + 2(2(a−k)+Ek)d.          (3.0)
(The t^k-coefficient of C(Z+tV) is a sum of products of a−k entries of Z and k entries of V. The middle exponent uses 2ρ𝔮·deg 𝓣=Q·deg[T].)

**Lemma 3.1 (vanishing at good points; PROVED).** Let u be a good point off the original boundary, off 𝔈 (R16.4), off {λ'=0} and off {det T̂=0}. Then 𝔊_k(u)=0 for every k.

*Proof.*
- **Reduce G_c.** By Lemma 1.2 and FNAP §2's induction (pointwise, B(u)∈GL_2(k)), c:=c(u) satisfies c^[Q^i]∥B_i(u)c. Hence c^[T]∥𝒦𝓂(u)c^[D], with nonzero vectors on both sides.
- **Proportionality.** So FNAM's G_c(Y)=c^[T,t]C_c(Y)c^[Q] equals ν·𝒫_u(c,Y) with ν∈k^*, where 𝒫_u is the specialisation at u.
- **Use the own line.** FNAM (with TSYC, and FNAM3 for the identification b=gD(β,α)) says that ℓ_u:=u^[E] divides G_c, or G_c=0. Either way G_c vanishes on {Y : u^[E]·Y=0}.
- **Conclude.** z+tV(u) lies on that line for every t (u^[E]·e(u)=0 and u^[E]·V(u)=0). So 𝒫_u(c(u),z+tV(u))≡0 in t. ∎

**Lemma 3.2 (descent of the vanishing order; PROVED).** Assume D>=4. Let K_0 be a positive multiple of D, and suppose 𝔊_k≡0 on Γ̃ for every 0<=k<K_0. Then for all but finitely many u∈Γ̃ and every c∈k²,
      C_c(e(u)+tV(u))·B(u)c ≡ 0   mod t^{K_0}.          (3.1)

*Proof.*
- **Step 1: fields.** Put F_0:=K^D and γ:=ψ^{1/2}∈K^{1/2}.
  - γ^{2^i}=ψ^{2^{i−1}} lies in K^D iff ψ∈K^{D/2^{i−1}}. ψ∉K² (R14.1), so this needs 2^i>=2D. Hence [F_0(γ):F_0]=2D.
  - Since D+2<2D (D>2), the elements 1, γ, …, γ^{D+2} are F_0-independent and extend to an F_0-basis (e_β) of K^{1/2}.
- **Step 2: coefficients in F_0.** Divide the t̂_ij by one fixed nonzero t̂_{i_0j_0}. Then B, 𝒦𝓂∈M_2(K^{ρ𝔮})⊂M_2(F_0), since D<Q<=ρ𝔮.
  - So 𝒫(c,Y)=Σ_{m=0}^{D+2}c_1^{D+2−m}c_2^mΠ_m(Y) with Π_m∈F_0[Y].
  - Generically c_gen∝(1,γ), so 𝒫(c_gen,Y)∝Σ_mγ^mΠ_m(Y).
- **Step 3: an F_0-rational frame of the own line.** In the affine normalisation U=(1,x,U_2/U_0), the line form λ:=U^[E] lies in (K^E)³⊂F_0³ (D|E).
  - For generic constants w_1, w_2 put P_i:=λ×w_i∈F_0³. These span the line {λ·Y=0} over K.
  - Write Z=σP_1+τP_2 and V=σ'P_1+τ'P_2 with σ,τ,σ',τ'∈K. Here στ'−σ'τ≠0, because V∦Z for generic c_0. Without loss τ≠0.
- **Step 4: a binary-form root.** Put g_m(w):=Π_m(wP_1+P_2)∈F_0[w] and g:=Σ_mγ^mg_m.
  - Π(Z+tV)=(τ+tτ')^a·g(w(t)), with w(t)=(σ+tσ')/(τ+tτ').
  - Also w(t)−w_0 has t-order exactly 1, where w_0:=σ/τ∈K.
  - So the hypothesis says (w−w_0)^{K_0} | g in K^{1/2}[w].
- **Step 5: split along the basis.** (w−w_0)^{K_0}=(w^D−w_0^D)^{K_0/D}∈F_0[w], since w_0^D∈F_0.
  - Write g=(w^D−w_0^D)^{K_0/D}·h with h∈K^{1/2}[w]=⊕_βe_βF_0[w].
  - Comparing e_β-coordinates gives g_m=(w^D−w_0^D)^{K_0/D}h_m with h_m∈F_0[w].
  - So Π_m(Z+tV)≡0 mod t^{K_0} in K[[t]] for every m.
- **Step 6: specialise.** At all but finitely many u all coefficients are regular. So 𝒫_u(c,z+tV(u))≡0 mod t^{K_0} as a polynomial in the free c.
- **Step 7: FNAP's algebra over R:=k[t]/(t^{K_0}).** Put z':=B(u)c and Λ:=𝒦𝓂(u)(B(u)^{−1})^[D]∈GL_2(k). Then
      𝒫_u = z'^[D,t]Λ^tC̃(z')z',   C̃(z'):=C_{B(u)^{−1}z'}(z+tV).
  - Put (q_1,q_2)^t:=Λ^tC̃(z')z'∈R[z']², quadratic in z'. The identity z'^D_1q_1+z'^D_2q_2=0 holds in R[z'].
  - The z'_1-degrees of the monomials of the two summands lie in {D,D+1,D+2} and {0,1,2}. These are disjoint for D>2.
  - So q_1=q_2=0, i.e. C̃(z')z'=0, which is (3.1). ∎

**Proposition 3.3 (dichotomy and generic own-line non-divisibility; PROVED).** Assume D>=4.
- (a) Either some 𝔊_k≢0 with k<D, or the pencil is **kernel-aligned**:
      (𝒦)   C_c(e(U))·B·c = 0 in K² for every c∈k².
- (b) For every twist, constant or not, some 𝔊_k with k<D⌈(a+1)/D⌉ is ≢0.

*Proof.*
- **(a)** Apply Lemma 3.2 with K_0=D and read the t⁰-coefficient of (3.1). It gives C_c(e(u))B(u)c=0 at almost all u, which is an identity in K.
- **(b)** Suppose not, and apply Lemma 3.2 with K_0=D⌈(a+1)/D⌉>a.
  - The left side of (3.1) has t-degree <=a, so it vanishes identically. For generic u, z+tV(u) sweeps the affine part of ℓ_u (V(u)∦z). Hence C_c(Y)B(u)c=0 for Y∈ℓ_u.
  - Since B(u)c≠0 for c≠0, det C_c(Y)=Δ(c,Y)=0 for all c∈k² and Y∈ℓ_u. So ℓ_u divides every c-coefficient Δ_i(Y).
  - By FNAM2 some Δ_i≢0. It has degree 2a, hence at most 2a distinct line factors.
  - But u↦u^[E] is injective on points, so infinitely many u give infinitely many distinct ℓ_u. Contradiction. ∎

*Remark.* (b) answers R18 §8.2/option (2) affirmatively in the weak sense: a cover vanishing at every good point exists for **every** twist, through the FNAP disjoint-support mechanism. It is the generic-point replacement for FNAN/FNAO's "finitely many slopes". What it does **not** give is a small degree; see (3.0) and §5.

**Theorem 3.4 (height-bounded twists are excluded; PROVED, conditional on the cited inputs).** Assume §1, D>=4, and not (𝒦). Then
      N_good <= Nd + 2deg[T]/𝔮 + (1.5d²+3.5d+1) + (D+2)(E+1)d + 4ad + 2(D−1)(E−2)d
                + Q·deg[T]·(Q−1+T−D)/(Q−1) + 6d_def + 7.          (3.2)
Hence the model is excluded whenever the right side is <1551q/4000. In particular it is excluded whenever deg[T]<=θ_max·rh, with θ_max as in Cor. 3.5.

*Proof.*
- **Choose the section.** By Prop. 3.3(a) there is k<D with 𝔊_k≢0, hence 𝔊_k²≢0.
- **Good points are zeros.** By Lemma 3.1 every good point off the listed exceptional sets is a zero of 𝔊_k. Distinct zeros of 𝔊_k are distinct zeros of 𝔊_k², so there are at most deg 𝔊_k² of them, by (3.0).
- **Bound the degree.** Use deg ψ<=(E+1)d and 2(2(a−k)+Ek)d=4ad+2k(E−2)d<=4ad+2(D−1)(E−2)d.
- **Exceptional sets.**
  - {λ'=0}: <=Nd (Lemma 1.1).
  - {det T̂=0}: <=2deg 𝓣=2deg[T]/𝔮.
  - 𝔈∖boundary: <=1.5d²+3.5d+1 (R16.4).
  - The boundary: 6d_def+7.
  - [v2: FIX-3] {g=0} (<=3d) is contained in 𝔈 and charged in 1.5d²+3.5d+1, so FIX-N1 is satisfied. Bs(e) lies in the original boundary. No number changes. ∎

**Corollary 3.5 (numerics; COMPUTED exactly in `numerics_twist.out`).**
- **Normalisation** as in R16–R18: M<16h/625, a<8h/625, d=E+2, d_def<=q/1000, 𝔮>=128. Write deg[T]=θ·rh.
- **The deg[T]-term.** With q=rQS·h, the main deg[T]-term of (3.2)/q equals θ·(Q−1+T−D)/((Q−1)S)≈θ·Q/(Q−1). So (3.2)<1551q/4000 iff θ<θ_max, where
      θ_max = (1551/4000 − rest)·(Q−1)S/(Q−1+T−D+(2/𝔮)(Q−1)/Q)   (exact form in the script),
  and "rest" collects the deg[T]-free terms.
- **Values.**
  - At the worst corner r=4, Q=128, S=512 (D=4), n=h/E=256: rest=1490227160815097/10995116277760000≈0.13554, and θ_max≈0.24978.
  - D=4: θ_max>=0.2497 at every n>=256 (0.2772, 0.2911, 0.2980, 0.3015, 0.3032 at n=512, …, 8192).
  - [v2: FIX-5] Non-empty windows θ_max>0 (r=4, least admissible Q) occur exactly for D<=n/16, at n=256,…,8192 (audit r1 grid, 1260 cases; the same sets over the whole grid). That is D∈{4,8,16} at n=256, D<=32 at 512, D<=64 at 1024, D<=128 at 2048, D<=256 at 4096 and D<=512 at 8192. v1's "D<=64 for n>=1024" was an artefact of the owner grid stopping at D=64. Within a window only deg[T]<=θ_max·rh is closed.
- **The a-priori range.** R18 §5 gives deg[T]<=e_M+d<=Nd/ρ+d, i.e. θ<=θ_up≈0.0512·S (3.28 at S=64). No grid case has θ_max>=θ_up: Theorem 3.4 closes only the low-height part of the twisted residual.
- **Constant twists.** deg[T]=0 always closes when rest<1551/4000, i.e. under the D-windows above. This is weaker than FNAP (which needs only n>=max(256,4D)) but independent of FNAP's line-factor count.
- **Gonality.** If [T] is non-constant, deg[T]>=𝔮·gon(Γ̃) (R18 §8.1). So Theorem 3.4 closes every non-constant twist outside (𝒦) when 𝔮·gon(Γ̃)<=deg[T]<=θ_max·rh. With 𝔮>=128 this is a genuine, non-empty range whenever gon(Γ̃)<=θ_max·rh/𝔮.

---

## 4. The kernel-aligned case (𝒦)

Write B=[b_1 b_2], where b_1=(T_21^ρ,T_11^ρ) and b_2=(T_22^ρ,T_12^ρ) (Lemma 1.2), and 𝒞_•:=C_•(e(U))∈M_2(K).

**Proposition 4.1 (structure of 𝒦; PROVED).** Assume (𝒦).
- (i) 𝒞_Pb_1=0, 𝒞_Rb_2=0 and 𝒞_Pb_2=𝒞_Rb_1. These are the c_1², c_2² and c_1c_2 coefficients.
- (ii) F divides det C_P, det C_R, and every coefficient Δ_i(Y) of Δ(v,Y)=det(v_1C_P+v_2C_R).
- (iii) For generic u, C_c(e(u)+tV(u))B(u)c≡0 mod t^{min(ρ𝔮,E)} for all c. Hence 𝔊_k≡0 for all k<min(ρ𝔮,E): in (𝒦) the reduced second layer carries no information below order min(ρ𝔮,E)>=min(64·𝔮,E) along the own line.
- (iv) If 𝒞_P≠0, then [b_1]=[ker 𝒞_P]. That is, [T_21:T_11]^ρ is the kernel direction, restricted to Γ', of a polynomial 2×2 matrix of degree a. Likewise [b_2]=[ker 𝒞_R] if 𝒞_R≠0.

*Proof.*
- **(i)** Expand C_c(Z)Bc=(c_1𝒞_P+c_2𝒞_R)(c_1b_1+c_2b_2) in c.
- **(ii)** For c≠0, Bc≠0 lies in ker C_c(Z), so Δ(c,Z)=0 for all c. Hence each Δ_i vanishes on Γ'. F is irreducible, so F|Δ_i. Likewise det𝒞_P=0 by (i), since b_1≠0.
- **(iii) Freeze B.** Normalise B∈M_2(K^{ρ𝔮}), regular at generic u. Along the branch y(s) of Γ at u, B(y)=B(u)+O(s^{ρ𝔮}). So C_c(e(y))B(u)c=C_c(e(y))(B(u)−B(y))c=O(s^{ρ𝔮}), using (𝒦) at y.
- **(iii) Pass to the own line.** By R16.2 Step 2, e(y(t))=κ(t)z(t) with κ a unit and z(t)−(z+tV)=O(t^E) (V=u^[E]×c_0, contact >=E). C_c is homogeneous of degree a, so C_c(z+tV)B(u)c=O(t^{min(ρ𝔮,E)}).
- **(iii) The 𝔊_k.** Multiply by (𝒦𝓂(u)c^[D])^t and put c=c_gen(u).
- **(iv)** By (i). ∎

**Proposition 4.2 ((𝒦) is excluded when 2a<d'; PROVED, conditional on FNAM2).** If 2a<d', then (𝒦) is impossible. Since 2a=M−1+T−Q−2d' and d'>=2E−2, a sufficient condition is
      M < 6E − T + Q − 5.

*Proof.* By Prop. 4.1(ii) F|Δ_i with deg Δ_i=2a<d'=deg F, so Δ_i=0 for all i. Then Δ≡0, contradicting FNAM2. ∎

*Remarks.*
- In the strip M ranges up to 16h/625>=6.55E (at h=256E). So Prop. 4.2 closes (𝒦) only for small M; (𝒦) with 2a>=d' is **OPEN**.
- [v2: N4] For D>=4 [v2.1: RC-6], combining Prop. 4.1(iii) with Prop. 3.3(b) excludes (𝒦) whenever a+1<=min(ρ𝔮,E). This adds only the edge case a=E−1, d'=2E−2 (when E<=ρ𝔮), where 2a=d' and Prop. 4.2 does not apply. For a<=E−2, Prop. 4.2 already applies.

**Example 4.3 ((𝒦) is formally non-empty with non-constant T; PROVED algebra, COMPUTED check `toy_checks.out` (4)).**
- **The data.** Let α_i, β_i be linear forms, n_0:=ρ𝔮, b_i:=((β_i·Y)^{n_0},(α_i·Y)^{n_0}), b_i^⊥:=((α_i·Y)^{n_0},(β_i·Y)^{n_0}), and p a vector of forms. Put
      C_P:=p⊗b_1^⊥+F·N_P,   C_R:=p⊗b_2^⊥+F·N_R.
- **The kernel identities.** In characteristic two b_i^⊥·b_i=0, and b_1^⊥·b_2=b_2^⊥·b_1. So (i) of Prop. 4.1 holds on {F=0} for B=[b_1 b_2]. This B corresponds to T_11=(α_1·e(U))^𝔮, T_21=(β_1·e(U))^𝔮, and so on, which is non-constant.
- **Generic invertibility.** For generic N_P, N_R, det(v_1C_P+v_2C_R)≢0. This is COMPUTED on the conic F=Y_0Y_2+Y_1², with n_0=8 and a=9.
- **Scope.** This requires a>=max(deg p+n_0,d'), consistent with Prop. 4.2. It is an algebraic test of the reduced identities only. It is not an original model, and no gate is verified.

---

## 5. Option (3): what the identities cannot do

1. **Decoupling (identities PROVED, Prop. 2.4; consequence CONDITIONAL/HEURISTIC) [v2: FIX-1].**
   - All global identities of FNAL/TSY/TSYC/FNAM/FNAM2 are invariant under P^t↦P^t+f^[X]⊗η with η∈Syz(f^[ρ]). The Γ-local conditions are not.
   - Under (H_lift) (OPEN; (H_bs) never holds) this changes a constant twist into an arbitrary ρ𝔮-th-power twist of polynomial origin with ρ𝔮<=m, keeping the second layer fixed.
   - So, conditionally on (H_lift), constancy of T is not a consequence of the global identities alone, unless they are inconsistent for such data (HEURISTIC).
   - It would then have to come from the point coupling (Lemma 3.1) or from the non-algebraic gates: the count N_good>1551q/4000, and possibly G5/PRIM.
2. **Polynomial origin is no height gain (CONDITIONAL on (H_lift), Cor. 2.3).**
3. **The kernel-aligned sub-case is formally consistent (Example 4.3).**
   - In (𝒦) the own-line expansion of the reduced second layer is automatically flat to order min(ρ𝔮,E).
   - [v2: FIX-7] So no 𝔊_k (k<min(ρ𝔮,E)) is nonzero in (𝒦) (PROVED, Prop. 4.1(iii)).
   - That no own-line cover at z of degree O(D·E·d+X·deg[T]) exists by any other construction is HEURISTIC.
4. **D∈{1,2} (FNAP §4).** FNAP's counterexamples to non-vanishing are pointwise identities in z'. They apply verbatim at every u for non-constant B(u). So the method of Lemma 3.2/Prop. 3.3 needs D>=4 [v2: N8]: the FNAP counterexamples are to the algebraic step only (COMPUTED `toy_checks.out` (3′)).
5. **The cost X·deg[T] (HEURISTIC) [v2: FIX-6].** Any cover obtained by substituting the first layer into G_c must express c^[T] through c^[Q]∥B(u)c. That introduces the Frobenius iterate B_{j+1}^[D]. The half-section 𝔊_k then has height ≈S·ρ·deg[T]=X·deg[T], and the counted section 𝔊_k² has ≈2X·deg[T]=T·deg[T]. The alternative c^[T]=(β:α)^[X] costs X·deg ψ. Either way the cover has degree >=X·min(deg[T],deg ψ), up to lower-order terms. So the method of §3 closes exactly the heights deg[T]≲rh·const (Cor. 3.5), and no rearrangement of the same substitution can do better.
6. **R18 §7 still applies.** The first layer alone (𝔉) has a Θ(QEd) zero set for T=I.

---

## 6. What remains, and the most promising next step

**Residual after this note** (all inside 𝔇_16 with global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128):
- (R1) non-constant twists of height θ_max·rh<deg[T]<=e_M+d (≈0.25rh to ≈0.0512S·rh), outside (𝒦);
- (R2) (𝒦) with 2a>=d' (any height, constant or not; the constant case is closed by FNAP when D>=4 and h>=max(256E,4DE));
- (R3) D∈{1,2} (as in FNAP), and D>=4 with n below the D-window of Cor. 3.5, unless T is constant and FNAP applies;
- (R4) the non-global-alignment variant of 𝔇_16 (FNAL unavailable) and 𝔇_17 (R18 §6);
- [v2: FIX-1] (H_lift), the polynomial lift of the first layer through the base points of f.

**Most promising next step (HEURISTIC).** Use the **residual intersection points of the own line**.
- **The extra vanishing.** At a good u, ℓ_u | G_{c(u)} also gives 𝒫_u(c(u),e(u_i))=0 at the residual points e(u_i)∈ℓ_u∩Γ', u_i≠u. Counted with multiplicity there are d'−I_z(ℓ_u,Γ') of them. Since d'>=2E−2 and I_z>=E, they exist unless the own line meets Γ' only at z; this has to be checked.
- **In (𝒦).** C_{c'}(e(u_i))B(u_i)c'=0 for all c'. When ker C_{c'}(e(u_i)) is one-dimensional, the residual vanishing compares B(u) with B(u_i).
- **Expected conclusion.** This should give T̂(u)=T̂(u_i) along the correspondence 𝒵={(u,v): u^[E]·e(v)=0, v≠u}. An irreducible correspondence of positive degree on both sides with an invariant non-constant function is very restrictive (both projections would factor through T̂). That is a plausible route to **constancy** in (R2), and possibly to a better cover in (R1): evaluate at e(u_i), which has degree 2 in v, instead of along the own line at z.
- **What has to be checked.**
  - (a) Linear disjointness of γ over F_0(e(u_i)), needed to transport Lemma 3.2 to the residual points. This holds if e(u_i) is separable over F_0=K^D. It is unknown.
  - (b) The degree of 𝒵 and of the pulled-back sections.
  - (c) Irreducibility, or at least no T̂-saturated components, of 𝒵.

A second, independent route to (R1) is to bound deg[T] through the second layer. In (𝒦), [b_1]=[ker𝒞_P] (Prop. 4.1(iv)), so the twist has the "height" of a kernel of a degree-a matrix. Outside (𝒦) one would like a similar description from the first non-vanishing 𝔊_k.

---

## 7. Computations (COMPUTED; this directory)

| script → output | content | result |
|---|---|---|
| `numerics_twist.py` → `.out` | exact Fraction evaluation of (3.2): θ_max over r∈{4,8,16}, Q∈{128,…,1024}, S∈{64,…,4096}, strip n∈[256,4Q); D-windows; a-priori θ_up | worst corner rest=0.13554, θ_max=0.24978 (D=4, n=256); D-windows up to D=64 (the owner grid stops there); the full D<=n/16 statement of Cor. 3.5 is from the audit grid (v1 audit r1; v2 revision check, 1764 cases) [v2.1: RC-4]; 0 cases with θ_max>=θ_up |
| `toy_checks.py` → `.out` (1) | [f^[X]]_×=κ_0^XJ^[X]ΩJ^[X,t] (X=2,4,8) and f(e(U))∥U, for a random centre over GF(2^16) | true |
| (2) | c^t(T^t)^[ρ]c^[Q]=𝔉(s)^ρ at c=(1,s^ρ), ρ=2,4,8 | true |
| (3) | reduced P_D^B on a random line ≢0 for random generically invertible degree-3 pencils, D=4,8, Q=4,8, j=0,1 | 8/8 nonzero |
| (3′) | FNAP's D=1,2 counterexamples vanish | true |
| (4) | Example 4.3 on the conic, n_0=8, a=9 | C_c(Z)Bc=0 on {F=0} for all tested c; det pencil ≠0 at a generic point |

Helpers `env_lib.py`, `ps.py` were copied from R18 but are not used by these scripts (no power-series computation was needed). Run with `python3 -I`.

---

## 8. Status

| item | status |
|---|---|
| Lemma 1.1 (non-constant CMIX normal form), Lemma 1.2 (slope equation = 𝔉^ρ) | PROVED (from R18 Thm 4.2, FNAN/FNAO local inputs); COMPUTED check |
| Lemma 2.1 (cross factorisation; J^[X,t]P^t=κ_0^{−X}FΩC_PJ^[ρ,t]) | PROVED (from FNAM1, FNAL, TSY); COMPUTED check |
| Lemma 2.1A (Γ'⊃Bs(f), mult>=E−3) [v2] | PROVED (audit FIX-1); COMPUTED (audit r2 g1, g2) |
| Prop. 2.2 (polynomial lift), Cor. 2.3 (height; no constancy) | CONDITIONAL on (H_lift), which is OPEN [v2: FIX-1]. (H_bs)⇒(H_lift) is proved, but (H_bs) never holds |
| Prop. 2.4 (i)–(v) (decoupling) | PROVED (unconditional) |
| "In particular" example in Prop. 2.4 | CONDITIONAL on (H_lift) |
| Remark 2.5 obstruction | CONDITIONAL/HEURISTIC [v2: FIX-1, FIX-2] |
| Preservation of G5/PRIM/count under decoupling | OPEN |
| Def. 3.0, Lemma 3.1 (𝔊_k vanish at good points) | PROVED |
| Lemma 3.2, Prop. 3.3 (dichotomy; generic own-line non-divisibility), D>=4 | PROVED (uses R14.1, FNAP algebra, FNAM2) |
| Thm 3.4 (height-bounded exclusion outside 𝒦), Cor. 3.5 | PROVED; numbers COMPUTED exactly |
| Prop. 4.1 (structure of 𝒦), Prop. 4.2 (𝒦 excluded if 2a<d') | PROVED |
| Example 4.3 (formal 𝒦 with non-constant T) | PROVED algebra; COMPUTED; not a model |
| constancy of T in 𝔇_16; (R1)–(R4); (H_lift) | OPEN |
| residual-intersection route (§6) | HEURISTIC (developed in `R19_CORRESPONDENCE_ROUTE_owner.md`, an unaudited owner draft; audit in progress) [v2.1: RC-7] |

[v2: FIX-4] Dependencies:
- R18 v2.1: audited and revision-checked.
- PRIMARY FNAL, TSY, TSYC, FNAM (FNAM2 is essential for Props. 3.3(b), 4.2), FNAN, FNAO, FNAP: Claude referee review PASS / PASS-with-fixes as listed in the header.
- v2 applied the audit's FIX-1..7 and was revision-checked (PASS-with-fixes); v2.1 applies RC-1..7.
- No manuscript was edited.
