# HYP M>=2, round 19 (v2.1): the own-line correspondence — structure, invariance forces constancy, and a count for the kernel-aligned case

7 October 2026. Claude HYP(2) research note for session_012ij7YN37LGpSS88rmUGQ7E. This is the R18-T §6 follow-up: develop the "residual intersection / correspondence" route.

**Version history.**
- v1: owner draft.
- v1 independently audited (`AUDIT_HYP_M2_ROUND19_20261007.md`): **PASS-with-fixes**. No headline claim breaks and all Cor. 4.2 thresholds stand. There are two substantive proof repairs (FIX-1, FIX-2), neither of which changes a printed number, plus label, statement and wording fixes (FIX-3..8) and minor notes N1–N8.
- v2 applies FIX-1..8 and N1–N8. Changes are marked "[v2: FIX-n]" or "[v2: Nn]".
- v2 revision-checked by a fresh referee (`REVISION_CHECK_HYP_M2_ROUND19_V2_20261007.md`): **PASS-with-fixes**. FIX-1 and FIX-2 were re-derived. All Cor. 4.2 numbers were recomputed from v2's (4.1) and are unchanged. Eight minor items RC-1..8 were raised.
- **v2.1 (this file)** applies RC-1..8, marked "[v2.1: RC-n]". No statement, proof step or number changes. RC-5 adds two table entries that were missing from v1's table. Scripts and outputs are in this directory. No file whose name contains "DZ" was opened. Nothing under any `src/` directory was executed (the PRIMARY `.md` sources were read only).

Inputs (read, not re-proved):
- R18-T v2.1 (`R18T_TWIST_NOTE_v2_1.md`): audited PASS-with-fixes, revision-checked, fixes applied [v2: FIX-7]. Used: Lemma 1.1, Lemma 1.2 (first layer), Lemma 2.1A (Γ'⊃Bs(f)), Prop. 4.1, Prop. 4.2.
- R18 v2.1 (audited). Used: Thm 4.2, §5 degree inputs, Lemma 5.3 normalisation of T.
- R17 v2.1 and R16 v2.1. Used: R16 §1 facts, R16 Lemma 1.1, R16.2, R16.4, R14.1 (ψ is not a square in K).
- PRIMARY FNAK, FNAL, TSY, TSYC, FNAM, FNAN, FNAO, FNAP (referee review PASS / PASS-with-fixes, including FIX-N1).

Labels:
- **PROVED**: full proof given here (owner proof; v1 independently audited, v2 revision-checked). It is conditional on the inputs it names.
- **CONDITIONAL**: proved under a named hypothesis that is not established [v2.1: RC-6].
- **COMPUTED**: exact finite-field or exact-rational computation. It illustrates, and it proves only where an exact rational bound is evaluated.
- **HEURISTIC / OPEN**: as stated.

Notation is that of R18-T §1:
- q=Eh, E=rQS=rT, ρ=Q/2, X=T/2, n=h/E.
- d=deg Γ<=E+2, d'=deg Γ'>=2E−2, a=deg C_•.
- c(u)=(√β:√α)(u)=(1:γ) with γ=√ψ(u), ψ=α/β.
- T=T̂^[𝔮], where the entries t̂_ij are sections of 𝓣 without common zero; τ_0:=deg 𝓣=deg[T]/𝔮.
- B=swap·(T^t)^[ρ]. Its entries are b̂^{ρ𝔮}, where b̂ ranges over the t̂_ij.
- 𝒞_•:=C_•(z), formed with the **morphism** z:Γ̃→Γ' (the normalised e), i.e. sections of z^*O(a), of degree a·d'. Not formed with the raw polynomial e(U): that would vanish at every point of Bs(e)∩Γ̃, which can be nonempty (it is in the audit's E=32 sample) [v2: FIX-1; v2.1: RC-2].
- For x=(x_1,x_2) put x^⊥:=(x_2,x_1). In characteristic two, x^⊥·y=det[x y]=x^tΩy with Ω=[[0,1],[1,0]].

---

## 0. Summary

**The correspondence.** 𝒵:={(u,v)∈Γ×Γ : u^[E]·e(v)=0}. Its non-diagonal part 𝒵^res consists of the pairs (u,v), v≠u, such that e(v) is a residual point of the own line ℓ_u on Γ'. It is best studied in the untwisted model
      𝒵':={(u,y)∈Γ×Γ'^{(1/E)} : u·y=0},   y=e(v)^{[1/E]},
which is a plain point–line incidence.

**PROVED.**
1. **Structure of 𝒵 (§1).**
   - The generic contact of ℓ_u with Γ' at e(u) is exactly E (FNAK applied to Γ'). Hence 𝒵'^res has degree d'−E over Γ_u.
   - Over Γ_v, the set-fibres of 𝒵'^res have at most d−1 points (they are line sections of Γ).
   - In the conic parameter of C_u=f(ℓ_u), the intersection with C_orig is cut out by a **projective polynomial** (αt+β)t^E+(γt+δ). By Lang's theorem, its root set is a Möbius image of P¹(F_E) (Prop. 1.2).
   - **Separability lemma (Lemma 1.4).** Every non-diagonal component of 𝒵' is separable over Γ_u. Every non-diagonal component of 𝒵⊂Γ×Γ is inseparable over Γ_v; in 𝒵', the v-functions are E-th powers. The proof is a one-line derivation argument: the tangent of Γ'^{(1/E)} at y=e(v)^{[1/E]} is the point v.
   - **Transversality (Lemma 1.5).** Residual intersections are transversal except at cuspidal branches of Γ'. [v2: FIX-2] One exception: the branch tangent at a cusp w of multiplicity m(w)>=E is not determined (at most one u per such w), and it is charged separately in (4.1).
2. **Invariance forces constancy (Thm 2.1, Cor. 2.2).**
   - A rational function g on Γ with g(u)=g(v) on any non-diagonal component of 𝒵 is constant. Irreducibility of 𝒵 is **not** needed. This matters, because 𝒵^res is reducible in the main toy (below).
   - Hence [T̂](u)=[T̂](v) on such a component forces T constant.
   - So does the weaker identity B(u)c(u)∥B(v)c(u) (equivalently 𝔉_v(s_M(u))=0) holding identically on such a component.
   - This answers question (c) positively.
3. **The kernel-aligned case (§3).**
   - **Normal form (Lemma 3.1).** If (𝒦) holds and F∤(C_P,C_R), then on Γ' one has 𝒞_c=p⊗(Bc)^⊥ with **one** vector p∈K² for both P and R. So R18-T Example 4.3 is the general shape.
   - **Factorisation (Cor. 3.2).** G_c|_{Γ'}=(c^[T]·p)·det(Bc,c^[Q]).
   - **Height (Prop. 3.3).** ρ·deg[T]<=a·d'. This answers question (d) inside (𝒦).
   - **Residual dichotomy (Prop. 3.4).** At a good u and a residual v, either Π_1:=c(u)^[T]·p(v)=0 or Ξ:=det(B(v)c(u),B(u)c(u))=0. Ξ=0 is exactly the B(u)/B(v) comparison asked in (a): c(u) is a slope of the frozen FN equation at v.
   - **Per-point bound (Lemma 3.5).** Unless T is constant, for each u outside <=2 ψ-fibres, at most τ_0−1 residual points satisfy Ξ=0.
4. **A count in (𝒦) (Thm 4.1).**
   - Π_1=λ(v)·π^X, where π is a section on 𝒵' that is cheap on both sides and λ depends on v only (Thm 4.1 Step 1) [v2.1: RC-3]. The reason: c^[T]=(β,α)^[X], v-functions are E-th powers, and E=2rX.
   - Summing over good points (with the v2 repairs FIX-1/FIX-2, which change no number) gives an explicit bound that **excludes (𝒦) with non-constant T** in a range where τ_0=deg[T]/𝔮 is at most ≈0.43E (r=4) or ≈0.16–0.48E (r=8, n<=512). With the (𝒦) height bound, this holds when 𝔮 is at least a fixed fraction of E (Cor. 4.2, exact numerics):
     - r=4: 𝔮>=nE/(8Q) suffices for n>=512 (better at n=256). Since dyadic n<=2Q, **𝔮>=E/4 suffices throughout the strip**. [v2: FIX-5] The margin is uniform: as n=2Q→∞ the (𝒦)-height/E tends to 0.4096 and τ_max/E to 0.42496. This was verified up to Q=16384, and at n=2Q up to Q=2^19 (audit c1).
     - r=8: 𝔮>=nE/(16Q) at n=256, and 𝔮>=nE/(4Q) at n=512.
     - r=16 [v2: FIX-5]: only n=256, with 𝔮>=512E/Q for Q>=512 (E at Q=512, E/2 at 1024, …, E/32 at 16384).
   - The count does not use D. So it also covers the D∈{1,2} lanes of (𝒦) for non-constant T.

**COMPUTED.**
- **Fermat σ1 (n=E−1).** 𝒵^res is the disjoint union of the E−2 graphs of the Frobenius-twisted maps u↦diag(1,ζ,ζ/(1+ζ))·u^[E], ζ∈F_E∖{0,1}. So it is reducible, with bidegree (1,E) per component. This is verified for E=8,…,64 and PROVED by a one-line identity (Example 1.6).
- **Random centres σ1(BU).** The residual polynomial always has the 4-term support {E+1,E,1,0}. Its factorisation patterns over F_{2^m} are those of projective polynomials (e.g. 1+2+6, 9 and 1+1+1+3+3 for E=8). [v2: FIX-3(a)] The arithmetic monodromy is transitive for E=8 (an irreducible specialisation) and for E=16 (cycle-type combinatorics, audit c2(e)). It is not decided for E=32.
- In both families d'−E=d−1.
- The algebraic identities of §3 hold in 300/300 random tests.

**What failed / OPEN.**
- **(R1) (outside 𝒦).** The residual route gives **no** B(u)–B(v) relation (HEURISTIC, Prop. 5.1(i)) [v2.1: RC-1]. Per point u, G_{c(u)}|_{Γ'} has degree a·d'>d'−E, so vanishing at the residual points is never contradictory. On 𝒵', every section encoding the residual vanishing contains the factor c^[Q] or the linear pencil coordinate c. Neither is an E-th power, so the section pays a factor E on the v-side. [v2: FIX-4] The degree counts of §5 are PROVED. The claim that the residual route cannot improve R18-T's X·deg[T] cost there is HEURISTIC.
- **(R2)** remains open for small 𝔮 (τ_0 comparable to E), for r>=16 except n=256, and for r=8 with n>=1024. In these ranges the p-term 2r·a·d' of the count already exceeds the budget.
- **Constant T in (𝒦) with D∈{1,2}** remains as in FNAP §4.

**Most promising next step (HEURISTIC, §6).**
- In (𝒦), improve the per-point bound "τ_0−1 Ξ-zeros". The residual set is a Möbius image of P¹(F_E) (Prop. 1.2), and Ξ(u,·)=σ_u^{ρ𝔮} with σ_u a section of 𝓣. A section of degree τ_0 whose zeros contain many points of an F_E-subline is very constrained.
- In (R1), look for a factorisation of 𝒞_c that isolates the pencil coordinate in a factor that is cheap per point, as the 𝒦 normal form does.

---

## 1. The correspondence 𝒵

**Definition 1.0.**
- 𝒵⊂Γ̃×Γ̃ is the reduced curve {(u,v) : u^[E]·e(v)=0}. It contains the diagonal Δ, because Γ⊂C_orig.
- 𝒵^res is the union of the components other than Δ.
- The Frobenius-root model is Γ'^{(1/E)}, the plane curve whose equation is F with coefficients replaced by their E-th roots. Coordinatewise E-th roots Y↦Y^{[1/E]} give a bijection Γ'→Γ'^{(1/E)} that maps lines to lines and tangents to tangents, since it is the base change by an automorphism of k.
- Put 𝒵':={(u,y)∈Γ̃×Γ̃'^{(1/E)} : u·y=0}, a divisor of type (O(1),O(1)).
- The map (u,y)↦(u,v) with v:=f(y^[E]) (so y=e(v)^{[1/E]} projectively) is a bijection 𝒵'→𝒵 **on points of the normalisations**. Here v=f(y^[E]) means the birational map extended to Γ̃'. It is undefined pointwise at Γ'∩Bs(f), and Γ' passes through every proper base point of f with multiplicity >=E−3 (R18-T v2.1 Lemma 2.1A); several places of Γ̃' lie over such a point. [v2: FIX-6]
- Under it, the **diagonal component** Δ':={(f(y^[E]),y)} corresponds to Δ.

Facts used: on Γ, f(e(U))=gU. At smooth points z=e(u) of Γ' with g(u)≠0, the tangent of Γ' is f(z)^[E]∝u^[E], i.e. the own line ℓ_u (R16 §1).

**Lemma 1.1 (branch tangents; PROVED for m(w)<E, OPEN for m(w)>=E) [v2: FIX-2].**
- (i) Let w be a place of Γ̃ whose branch of Γ' at z(w) has multiplicity m(w)<E. Then the branch tangent is ℓ_w={Y : w^[E]·Y=0}. In all cases, ℓ_w meets the branch with multiplicity >=E.
- (ii) Consequently, for m(v)<E (in particular at generic v), the tangent line of the branch of Γ'^{(1/E)} at y=e(v)^{[1/E]} is the line with coordinates v. That is, it is {Y : v·Y=0}.

*Proof.*
- **(i) [v2: FIX-2; the v1 continuity argument is invalid at singular branches in characteristic 2.]**
  - *Counterexample to v1's argument.* For the branch (1,t²,t³), z×z' tends to the line (0,1,0), which meets the branch with multiplicity 2. The true tangent (0,0,1) meets it with multiplicity 3.
  - *Correct argument.* Let v(t) be the branch of Γ at w, with v(0)=w, and z(t) the corresponding branch of Γ'.
    - On Γ, v(t)^[E]·z(t)=0 identically.
    - Also v(0)^[E]−v(t)^[E]=(v(0)−v(t))^[E] is divisible by t^E.
    - Hence ℓ_w·z(t)=(v(0)^[E]−v(t)^[E])·z(t)=O(t^E), i.e. I_w(ℓ_w)>=E.
    - For a branch of multiplicity m, every line through z(0) other than the branch tangent meets it with multiplicity exactly m. So if m(w)<E, ℓ_w is the branch tangent.
  - For m(w)>=E, whether ℓ_w is the branch tangent is OPEN. The places with m(w)>=E number at most (2d'+2g−2)/(E−1) (Lemma 1.5's count).
- **(ii)** Apply the coordinatewise E-th root to (i). It is used only at the generic place (Lemma 1.4), where m=1. ∎

**Proposition 1.1 (generic contact exactly E; residual degree; PROVED).**
- (i) For all but finitely many u, the branch of Γ' at e(u) meets ℓ_u with multiplicity exactly E. In general, write j(u)>=E for this multiplicity. Then
      Σ_u (j(u)−E) <= (E+1)(2g−2)+3d'.
- (ii) As divisors, 𝒵'=Δ'+𝒵'^res, and Δ' occurs with multiplicity one. The projection 𝒵'^res→Γ̃_u has degree d'−E. The projection 𝒵'^res→Γ̃'^{(1/E)} has degree <=d−1.

*Proof.*
- **(i) The contact is at least E.** For a generic point z of Γ', the curve Γ̃→Γ'⊂P² has generic order sequence (0,1,ε_2), with ε_2>=E because Γ'⊂C_f has contact >=E with its tangent (R16 Lemma 1.1). Moreover ε_2 is a power of 2 (Stöhr–Voloch, p-adic criterion).
- **(i) The contact is at most E.** By FNAK part 1, applied to the point map z:Γ̃→P² (nondegenerate, since Γ' is not a line, with orders (0,1,ε_2), ε_2>=4), the osculating object z×D^{(1)}z, i.e. the tangent line, is projectively defined over K^{ε_2}. The tangent is [u^[E]]. If ε_2>=2E, then [u]∈P²(K^{ε_2/E})⊂P²(K²). So both coordinate ratios U_1/U_0 and U_2/U_0 lie in K², and since they generate K, K⊂K², which is false [v2: N1]. Hence ε_2=E.
  - (FNAK is stated for maps to P²*; its proof is the Hasse-derivative computation, which is symmetric in points and lines.)
- **(i) The sum.** The bound is Stöhr–Voloch: v_u(R)>=Σ_i(j_i(u)−ε_i)>=j(u)−E, with deg R=(ε_0+ε_1+ε_2)(2g−2)+3d'.
- **(ii) Over u.** The fibre of the divisor 𝒵' over u is the divisor of the line u^⊥ on Γ̃'^{(1/E)}, of degree d'. Δ'→Γ̃_u is purely inseparable of degree E, since y↦f(y^[E]) is the E-power Frobenius followed by a birational map. At the place y_u=e(u)^{[1/E]}, the multiplicity of u^⊥ is j(u)=E generically. So Δ' has multiplicity one, and the residual degree is d'−E.
- **(ii) Over y.** The fibre over y is the divisor of the line y^⊥ on Γ̃, of degree d. Δ' contributes at least 1, namely the place v. ∎

**Proposition 1.2 (residual points form an F_E-subline; PROVED, with Lang's theorem cited).** It applies to u with ℓ_u∩Bs(f)=∅, which is all but <=3d points [v2: FIX-6, N2]. Then C_u=f(ℓ_u) is a smooth conic through Bs(e). The degenerate case αδ=βγ is not analysed, and it is not used.
- **The parametrisation.** Let ν_u:P¹→C_u=f(ℓ_u) be a parametrisation of the conic (quadratic in t).
- **The polynomial.** Then C_orig(ν_u(t))=ν_u(t)^[E]·e(ν_u(t)) factors as
      (base-point factors) × (t−t_u)^E × [(αt+β)t^E+(γt+δ)],
  where t_u=ν_u^{−1}(u) and the four coefficients are in K(u).
- **Lang.** When the bracket is not degenerate (αδ≠βγ), its roots form g_u(P¹(F_E)) for some g_u∈PGL_2(k): the fixed points of a Frobenius-semilinear projectivity.
- **Consequence.** The residual places of ℓ_u∩Γ' form a subset of a Möbius image of P¹(F_E). They are the subline minus the points lying on line components of C_orig or at base points.

*Proof.*
- **The linear factor.** e maps C_u birationally onto the line ℓ_u, and the conic passes through the three base points of e. Hence e(ν_u(t))=b(t)·λ(t), where b is cubic (vanishing at the base parameters) and λ(t) is a **linear** parametrisation of ℓ_u.
- **The Frobenius factor.** ν_u(t)^[E]=ν_u^{(E)}(t^E) is quadratic in s:=t^E. So C_orig(ν_u(t))=b(t)·H(t^E,t), with H(s,t)=A_2(t)s²+A_1(t)s+A_0(t) and the A_i linear.
- **Divide out the contact.** C_orig(ν_u(t)) is divisible by (t−t_u)^E=s−s_u, where s_u=t_u^E (Prop. 1.1, contact >=E at the place u). Reducing H modulo s−s_u gives A_2(t)s_u²+A_1(t)s_u+A_0(t), a polynomial of t-degree <=1<E. It must vanish. Hence H=(s−s_u)(A_2(t)(s+s_u)+A_1(t)), and the cofactor has the stated shape.
- **The subline.** If M(t):=(γt+δ)/(αt+β) is invertible, the roots are the fixed points of t↦M^{−1}(t^E). By Lang's theorem (H¹ of a finite field in PGL_2(k̄) is trivial), this semilinear map is conjugate to t↦t^E, whose fixed points are P¹(F_E). ∎

*COMPUTED (`corr_random.out`, `corr_fermat.py`).*
- For random centres e=σ1(BU) with E=8,16,32 over GF(2^13), GF(2^11):
  - the contact root has multiplicity exactly E. The single degenerate sample at E=32 is a point u∈Bs(e)∩Γ (audit c0), so it is evidence that Bs(e)∩Γ≠∅, which is relevant to FIX-1. It is not a counterexample to Prop. 1.2 [v2: FIX-8];
  - the residual polynomial has degree E+1=d−1=d'−E, support exactly {E+1,E,1,0}, and is squarefree;
  - its factorisation patterns are the projective-polynomial patterns (Bluher). For E=8 these are 1+2+6, 9 and 1+1+1+3+3. Pattern 9 occurs, so the arithmetic monodromy on the E+1 roots is transitive there. For E=16 transitivity follows from the observed cycle types; for E=32 it is not decided [v2: FIX-3(a)].
- For Fermat σ1 the residual has E−2 roots. The patterns are (3,3) at E=8 and (2,4,4,4) at E=16: the Frobenius orbits on F_E∖{0,1}. See Example 1.6.

**Lemma 1.4 (separability lemma; PROVED).** Let 𝒵'_1 be a component of 𝒵'^res with function field L=k(u,y), and 𝒵_1 the corresponding component of 𝒵^res.
- (A) L/k(Γ_u) is **separable**.
- (B) k(𝒵_1)/k(Γ_v) is **inseparable**. In 𝒵', every function of v is an E-th power in L.

*Proof.*
- **(A) Set-up.** Suppose L/k(Γ_u) is inseparable. Let L_s be the separable closure of k(Γ_u) in L. Then L/L_s is purely inseparable of degree 2^i>=2. For a one-variable function field over a perfect field this forces L_s=L^{2^i}. So k(Γ_u)⊂L².
- **(A) A derivation.** Choose a nonzero derivation D of L/k. Then D kills L², hence kills the affine coordinates of u. Normalise u=(1,u_1,u_2) and y=(1,y_1,y_2). Then u·y=0 gives u·Dy=0.
  - Dy≠0: L is generated by k(u) and k(y), so a derivation vanishing on both is zero.
  - Dy has first coordinate 0, so y and Dy are independent, and u∥y×Dy.
- **(A) The tangent.** D restricted to k(y) is φ·d/dx_y with φ∈L^*, since the derivations k(y)→L form a one-dimensional L-space. So y×Dy∥y×dy/dx_y, which is the tangent of Γ'^{(1/E)} at y. By Lemma 1.1(ii), this tangent is v=f(y^[E]). Hence u=v and 𝒵'_1⊂Δ'. Contradiction.
- **(B) The E-th powers.** k(Γ_v)⊂k(Γ'^{(1/E)})=k(y)⊂L. The first inclusion is the E-power Frobenius composed with birational maps, so k(Γ_v)=k(y)^E·(constants)=k(y)^E.
- **(B) Directly in 𝒵.** Suppose k(𝒵_1)/k(Γ_v) is separable. Then d/dx_v extends to a derivation δ of k(𝒵_1).
  - δ kills every E-th power, so applying δ to u^[E]·e(v)=0 gives u^[E]·δe(v)=0.
  - Likewise, from v^[E]·e(v)=0 on Γ, v^[E]·δe(v)=0.
  - e(v)×δe(v)≠0: otherwise every coordinate ratio of e(v) would have zero derivative, i.e. lie in K², so k(Γ')⊂K², contradicting birationality of e.
  - Hence u^[E]∥v^[E]∥e(v)×δe(v), so u=v. ∎

**Lemma 1.5 (transversality away from cusps; PROVED, with the cusp-tangent exception) [v2: FIX-2].**
- **Cusps.** Call a place w of Γ̃ *cuspidal* if the branch z_w(t) of Γ' at e(w) has z_w(t)∧z_w(0)=O(t²). Write m(w)>=2 for its multiplicity.
- **Statement.** For u≠w with e(w)∈ℓ_u, the intersection multiplicity of ℓ_u with the branch at w is 1 if w is not cuspidal. It is m(w) if w is cuspidal and ℓ_u is not the branch tangent. The latter can fail only if m(w)>=E (by Lemma 1.1(i), ℓ_w is then possibly not the tangent), and for at most one good u per such w (Frobenius is injective) [v2.1: RC-8]. The excess there is <=d'−E.
- **Count.** Σ_{w cuspidal}(m(w)−1) <= 2d'+2g−2.

*Proof.*
- **Non-cuspidal branches.** For a smooth branch, a line through z_w(0) has multiplicity >=2 iff it is the branch tangent ℓ_w (Lemma 1.1). And ℓ_u=ℓ_w forces u=w, since Frobenius is injective.
- **Cuspidal branches.** For a branch of multiplicity m, a non-tangent line has multiplicity exactly m. If m(w)<E, the tangent is ℓ_w (Lemma 1.1(i)), and ℓ_u=ℓ_w forces u=w. If m(w)>=E, at most one u≠w can have ℓ_u equal to the true tangent.
- **The count.** z×dz is a nonzero section of O_{Γ'}(2)⊗Ω¹ (the map is separable and Γ' is not a line), and ord_w(z×dz)>=m(w)−1. So the number of w with m(w)>=E is <=⌊(2d'+2g−2)/(E−1)⌋. ∎

**Example 1.6 (Fermat σ1: 𝒵^res is a union of E−2 Frobenius graphs; PROVED; COMPUTED in `fermat_explicit.out`).**
- **The model.** Γ: U_0^{E−1}+U_1^{E−1}+U_2^{E−1}=0 and e=σ1. For ζ∈F_E∖{0,1} put D_ζ:=diag(1,ζ,ζ/(1+ζ)) and Φ_ζ(u):=D_ζu^[E].
- **Φ_ζ(u)∈Γ.** The entries of D_ζ lie in F_E^*=μ_{E−1}, so Σ(D_ζu^[E])_i^{E−1}=(Σu_i^{E−1})^E=0.
- **Incidence.** u^[E]·σ1(v)=v_0v_1v_2Σ_iu_i^E/v_i=v_0v_1v_2(1+ζ^{−1}+(1+ζ)ζ^{−1})=0.
- **Conclusion.** These are E−2 residual points (distinct for generic u), which is all of them since d'−E=E−2. So
      𝒵^res=⋃_{ζ∈F_E∖{0,1}} graph(Φ_ζ),
  each component of bidegree (1,E). This illustrates Lemma 1.4: k(Γ_v)=k(Γ_u)^E on each graph.
- **Computation.** 𝒵^res is therefore **reducible** in the principal toy model, which is why §2 avoids irreducibility. COMPUTED: E=8, 16, 32, 64, 20 random u each; all (u,ζ) incidences hold. The residuals are distinct and ≠u except at 4/20 special u for E=16 over GF(2^12).

*Remark 1.7 (bidegree).* In both toy families d'−E=d−1 (COMPUTED). By Prop. 1.2, d'−E<=E+1 always. We use only d'−E (over u) and <=d−1 (over y).

---

## 2. A function invariant under the correspondence is constant

**Theorem 2.1 (PROVED).** Let g∈K=k(Γ) and let 𝒵_1 be a non-diagonal component of 𝒵. If g(u)=g(v) on 𝒵_1, then g is constant.

*Proof.*
- **Reduce to a separating g.** Suppose g is non-constant. Write g=g_0^{2^j} with g_0∉K². This is possible because a non-constant element lies in only finitely many K^{2^j}. Frobenius is injective, so g_0(u)=g_0(v) on 𝒵_1.
- **Separability.** g_0∉K² means g_0 is separating, so k(Γ_u)/k(g_0(u)) and k(Γ_v)/k(g_0(v)) are finite separable. In k(𝒵_1) the two elements g_0(u) and g_0(v) coincide.
- **Compositum.** k(𝒵_1) is the compositum of k(Γ_u) and k(Γ_v), so it is separable over k(g_0), hence over k(Γ_v). This contradicts Lemma 1.4(B). ∎

*Remark.* Irreducibility of 𝒵 is not used. Fermat (Example 1.6) shows it can fail. In Fermat the theorem is transparent: g∘Φ_ζ has degree E·deg g≠deg g. Equivalently, invariance g=g∘Φ_ζ forces g∈K^E, and iterating forces g∈∩_mK^{E^m}=k: purely inseparable composition removes invariants rather than creating them (audit §3.2, counterexample attempt) [v2: audit §3.2; marker added in v2.1: RC-6].

**Corollary 2.2 (PROVED).** Let 𝒵_1 be a non-diagonal component of 𝒵^res.
- (i) If [T̂](u)=[T̂](v) on 𝒵_1, then T is constant (in PGL_2).
- (ii) Suppose Ξ(u,v):=det(B(u)c(u),B(v)c(u)) vanishes identically on 𝒵_1. Then T is constant. Here Ξ(u,v)=0 at a good u is equivalent to 𝔉_v(s_M(u))=0, i.e. s_M(u) solves the frozen FN equation of v (Lemma 3.0).

*Proof.*
- **(i)** Apply Thm 2.1 to each coordinate ratio t̂_ij/t̂_kl.
- **(ii) Set-up.** Put L:=k(𝒵_1) and F_0:=L^{ρ𝔮}. Then B(u),B(v)∈M_2(F_0), and c(u)=(1,γ) with γ²=ψ(u).
  - By Lemma 1.4(A) (which carries over to 𝒵_1, since 𝒵'_1→𝒵_1 is bijective and k(𝒵_1)⊂L' with L'/k(𝒵_1) purely inseparable), ψ(u)∉L².
  - So the least 2^i with γ^{2^i}∈F_0 is 2ρ𝔮>=4, and 1, γ, γ² are F_0-independent.
- **(ii) Solve.** With M:=B(u)^tΩB(v)∈M_2(F_0), we get 0≡Ξ=M_11+γ(M_12+M_21)+γ²M_22. Hence M_11=M_22=0 and M_12=M_21, i.e. M=mΩ.
  - m≠0, since B(u), B(v) are invertible.
  - Using B^tΩB=det(B)·Ω, this gives B(u)^t=(m/det B(v))B(v)^t, so B(u)∝B(v).
- **(ii) Conclude.** The entries of B are the ρ𝔮-th powers of the t̂_ij, so [T̂(u)]=[T̂(v)]. Apply (i). ∎

**Answer to question (c).** Yes: the comparison B(u)c(u)∥B(v)c(u), holding identically on any one non-diagonal component of the correspondence, forces constancy. It does so through the inseparability of 𝒵 over its second factor, not through irreducibility or monodromy. The difficulty is quantitative: the residual vanishing gives this comparison only at finitely many pairs, and only in (𝒦) (see §3–§5).

---
## 3. The kernel-aligned case (𝒦): normal form, height, residual dichotomy

Standing for §3–§4:
- 𝔇_16 as in R18-T §1 (global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮>=128), together with (𝒦): 𝒞_cB c=0 in K² for all c∈k².
- **Reduction.** If F divides all entries of C_P and C_R, replace C_• by C_•/F^k with F∤(C_P,C_R) jointly.
  - This keeps ℓ_u | G_c, because ℓ_u∤F and ℓ_u is prime.
  - It keeps FNAM2, because Δ is divided by F^{2k}.
  - It lowers a to a−kd'.
  - The R18-T dichotomy then applies afresh to the reduced pencil. Below, (𝒦) refers to the reduced pencil, and a<=M'+X−ρ−d' still holds.
- "Good u" means a good point off the exceptional sets of R18-T Lemma 3.1: 𝔈, the boundary, {λ'=0}, {det T̂=0} and {g=0} (FIX-N1). By R18-T Lemma 1.2, c(u)^[Q]=κ_uB(u)c(u) with κ_u≠0.

**Lemma 3.0 (PROVED; COMPUTED (1) in `kappa_identities.out`).** At a good u, with c=c(u)=(1:s^ρ) and s=s_M(u), and any v where T is regular,
      det(B(v)c, c^[Q]) = c^t𝒜(v)c^[Q] = 𝔉_v(s)^ρ,   and   det(B(v)c, B(u)c) = κ_u^{−1}·𝔉_v(s)^ρ,
where 𝔉_v(s):=T_22(v)s^{Q+1}+T_21(v)s^Q+T_12(v)s+T_11(v) is R18's FN form frozen at v.

*Proof.*
- **The first equality.** B(v)c spans the kernel of the row c^t𝒜(v), so B(v)c=(c^t𝒜(v))^⊥. Hence det(B(v)c,w)=c^t𝒜(v)w.
- **The second.** It is R18-T Lemma 1.2's expansion, with T frozen at v.
- **The third.** Substitute c^[Q]=κ_uB(u)c. ∎

**Lemma 3.1 (normal form in (𝒦); PROVED).** Assume (𝒦) and F∤(C_P,C_R). Then 𝒞_P≠0, 𝒞_R≠0, and there is a unique p∈K²∖0 with
      𝒞_P = p⊗b_1^⊥,   𝒞_R = p⊗b_2^⊥,   i.e.   𝒞_c = p⊗(Bc)^⊥  for all c,
where B=[b_1 b_2].

*Proof.*
- **Both are nonzero.** If 𝒞_P=0, then by R18-T Prop. 4.1(i), 𝒞_Rb_1=𝒞_Pb_2=0 and 𝒞_Rb_2=0. Since B is invertible, 𝒞_R=0, i.e. F divides everything. Symmetrically for 𝒞_R.
- **Rank one.** 𝒞_Pb_1=0 with b_1≠0 and 𝒞_P≠0, so 𝒞_P has rank one with kernel Kb_1. Its rows are multiples of b_1^⊥, since b_1^⊥·b_1=0 in characteristic two. So 𝒞_P=p_P⊗b_1^⊥, and likewise 𝒞_R=p_R⊗b_2^⊥.
- **The vectors agree.** The mixed identity 𝒞_Pb_2=𝒞_Rb_1 reads p_P·det B=p_R·det B, and det B≠0. ∎

**Corollary 3.2 (factorisation on Γ'; PROVED; COMPUTED (3)).** For a free c∈k² and Z∈Γ',
      G_c(Z)=c^[T,t]𝒞_c c^[Q]=(c^[T]·p)·det(Bc, c^[Q]).
At a good u and Z=e(v):
      G_{c(u)}(e(v)) = κ_u·Π_1(u,v)·Ξ(u,v),   Π_1:=c(u)^[T]·p(v),   Ξ:=det(B(v)c(u), B(u)c(u)).

*Remark.* This is R18-T Example 4.3 in general: modulo F, the (𝒦)-pencil is p⊗(Bc)^⊥. R18-T Prop. 4.1(iii) (own-line flatness to order min(ρ𝔮,E)) is visible here: det(B(y)c, c^[Q]) vanishes to order ρ𝔮 at u.

**Proposition 3.3 (height in (𝒦); PROVED).** ρ·deg[T]<=a·d'. In particular τ_0=deg[T]/𝔮<=a·d'/(ρ𝔮).

*Proof.*
- **A map given by degree-a forms.** Pick a row i with p_i≠0. By Lemma 3.1, (row_i𝒞_P, row_i𝒞_R)=p_i(b_1^⊥,b_2^⊥)=p_i(T_11^ρ,T_21^ρ,T_12^ρ,T_22^ρ). So the map [T^[ρ]]:Γ̃→P³ is given by four restrictions to Γ' of forms of degree a, i.e. by sections of a bundle of degree a·d'. Removing common zeros only lowers the degree.
- **Frobenius.** deg[T^[ρ]]=ρ·deg[T]. ∎

*Comparison.* This is a (modest) improvement of the a-priori bound deg[T]<=Nd/ρ+d (R18 §5). Using a<=M'+X−ρ−d' and d'<=2d:
- a·d'<=(N+3X−2d')d;
- at h=256E one has a<=1.40E against M'≈3.28E, so the (𝒦) bound is ≈0.43 of the a-priori one;
- the ratio tends to 1 as n grows.

It does not by itself close the height window.

**Proposition 3.4 (residual dichotomy; PROVED).** Let u be good, and let v be a residual place of ℓ_u (i.e. (u,v)∈𝒵^res) with det T̂(v)≠0. (This hypothesis is kept so that B(v) is invertible and Ξ is the B(u)/B(v) comparison of Cor. 2.2. The dichotomy itself holds at every residual v, since p is regular everywhere [v2.1: RC-7].) Then
      Π_1(u,v)=0   or   Ξ(u,v)=0 (equivalently 𝔉_v(s_M(u))=0).

*Proof.*
- **Vanishing.** e(v)∈ℓ_u, and ℓ_u | G_{c(u)} (FNAM3/TSYC). So G_{c(u)}(e(v))=0.
- **Factor.** Apply Cor. 3.2. [v2: FIX-1] With 𝒞 formed by the morphism z, p=λp' is regular everywhere (Thm 4.1, Step 1). The alternative Π_1=0 includes the places with λ(v)=0, i.e. where C_P and C_R both vanish at z(v); these are charged separately in Thm 4.1. ∎

**Answer to question (a).**
- In (𝒦): yes. The residual vanishing forces, at each residual v, either a first-layer-type condition Π_1(u,v)=0 or the B(u)/B(v) comparison Ξ=0, i.e. B(u)c(u)∈ker C_{c(u)}(e(v))=K·B(v)c(u).
- Outside (𝒦): no such relation is found (HEURISTIC, Prop. 5.1(i)) [v2.1: RC-1].

**Lemma 3.5 (few Ξ-coincidences per point; PROVED; COMPUTED (2)).** Assume [T̂] is non-constant. Then:
- (i) For a good u, v↦Ξ(u,v) equals σ_u(v)^{ρ𝔮}, where σ_u:=Σ_{ij}ŵ_iĉ_jb̂_ij∈H⁰(𝓣), with ŵ:=((B(u)c)^⊥)^{[1/ρ𝔮]} and ĉ:=c^{[1/ρ𝔮]}. Also σ_u(u)=0.
- (ii) σ_u≡0 only if c(u) is a root of a fixed nonzero binary quadratic form. So it happens for at most 2·deg ψ<=2(E+1)d good points.
- (iii) Otherwise at most τ_0−1 places v≠u satisfy Ξ(u,v)=0.

*Proof.*
- **(i)** The entries of B(v) are the b̂_ij(v)^{ρ𝔮}. Frobenius is additive, so Ξ(u,·)=Σw_ic_jB_ij(·) is the ρ𝔮-th power of σ_u. Ξ(u,u)=0 trivially.
- **(ii) Expansion.** Write B(v)=Σ_{k<=s}φ_k(v)B_k, with k-linearly independent functions φ_k and constant matrices B_k. Here s>=2, since [T̂] is non-constant.
- **(ii) The condition.** σ_u≡0 iff B_kc∥B(u)c for every k, which forces det(B_kc,B_lc)=0 for all k, l.
- **(ii) Some form is nonzero.** Choose a combination B_* of the B_k that is invertible (e.g. B(v_0) for generic v_0). If det(B_*c,B_kc)≡0 in c for all k, then every vector is an eigenvector of B_*^{−1}B_k. So B_k∝B_*, and s=1, a contradiction. Thus some det(B_*c,B_kc) is a nonzero binary quadratic form.
- **(ii) Count.** c(u)=(√β:√α)(u) lies among its <=2 roots. That fixes ψ(u) in a set of <=2 values, hence <=2 deg ψ points.
- **(iii)** deg 𝓣=τ_0, and one zero is at u. ∎

---

## 4. A count in the kernel-aligned case

**Theorem 4.1 ((𝒦) with non-constant twist; PROVED, conditional on the cited inputs; repaired in v2 [v2: FIX-1, FIX-2]).** Assume §3's standing hypotheses, (𝒦) for the reduced pencil, [T̂] non-constant, and τ_0<=d'−E. Then
      N_good·(d'−E−τ_0+1) <= (d'−E)·deg ψ + 2r(d−1)·a·d' + [(E+1)(2g−2)+3d'] + d(2d'+2g−2) + 2dτ_0
                               + (d'−E)·⌊(2d'+2g−2)/(E−1)⌋
                               + (d'−E−τ_0+1)·[Nd + 2τ_0 + (1.5d²+3.5d+1) + 3d + 2deg ψ + 6d_def+7].        (4.1)
The second line is new in v2 (FIX-2: the cusp-tangent excess). It changes no printed digit of Cor. 4.2 (audit c1, column "with FIX-2"). FIX-1 adds no term: its cost is absorbed by the 2r(d−1)·a·d' term (Step 4).

*Proof.*
- **Step 1: the cheap section π.**
  - c(u)^[T]=(β,α)(u)^[X] projectively.
  - On 𝒵', p(v)=(p^σ(y))^[E], where p^σ is the E-th-root conjugate section on Γ'^{(1/E)} (Lemma 1.4(B)).
  - [v2: FIX-1] Write p=λp', where p' is a section of a bundle 𝓟 without common zeros, and let w:=(t̂_11,t̂_21,t̂_12,t̂_22)^{ρ𝔮}, also without common zeros. Lemma 3.1 gives [𝒞_P|𝒞_R]=λ·p'⊗w. So λ is a **regular** section of z^*O(a)⊗𝓟^{−1}⊗𝓣^{−ρ𝔮}, and
        deg𝓟 + #Z(λ) <= a·d' − ρ·deg[T]   (in particular deg𝓟<=a·d').
    Its zeros Z(λ) are exactly the places where C_P and C_R both vanish at z(v). Since E=2rX,
        Π_1(u,v) = λ(v)·π(u,y)^X,   π := β(u)·p'^σ_1(y)^{2r} + α(u)·p'^σ_2(y)^{2r}.
  - π is a section on 𝒵'^res of degree <=(d'−E)·deg ψ+(d−1)·2r·deg𝓟, by Prop. 1.1(ii), using deg𝓟^σ=deg𝓟.
- **Step 2: π is nonzero on each component.** If π≡0 on a component 𝒵'_1, then ψ(u)=(p'^σ_1/p'^σ_2)^{2r}∈L². [v2: N3] If p'^σ_2≡0, then π=β(u)p'^σ_1(y)^{2r}≢0 [v2.1: RC-4] directly, since p'^σ_1≢0. By Lemma 1.4(A), L/k(Γ_u) is separable, so L²∩k(Γ_u)=k(Γ_u)². That contradicts R14.1.
- **Step 3: zeros above one good u.**
  - Let u be good, outside the exceptional sets bracketed in (4.1).
  - The distinct residual places of ℓ_u number at least d'−j(u)−κ(u), where κ(u):=Σ_{w∈Res(u)}(I_w(ℓ_u)−1). By Lemma 1.5 only cuspidal w contribute to κ(u).
  - Remove the residual places in W:={det T̂=0} (|W|<=2τ_0).
  - Remove at most τ_0−1 places with Ξ=0 (Lemma 3.5(iii); u is outside the <=2 deg ψ points of 3.5(ii)).
  - [v2: FIX-1] Remove the residual places in Z(λ). At every remaining residual place, Π_1=0 (Prop. 3.4) and λ(v)≠0, so π=0.
  - The pairs (u,y) are distinct points of the normalisation of 𝒵'^res.
- **Step 4: sum over u.**
  - Σ_u(j(u)−E)<=(E+1)(2g−2)+3d' (Prop. 1.1(i)).
  - Σ_uκ(u)<=d·Σ_w(m(w)−1)+(d'−E)⌊(2d'+2g−2)/(E−1)⌋<=d(2d'+2g−2)+(d'−E)⌊(2d'+2g−2)/(E−1)⌋. A place w is residual for at most d places u, namely those on the line e(w)^{[1/E]}. The second term is the cusp-tangent exception of Lemma 1.5 [v2: FIX-2].
  - [v2: FIX-1] Σ_u|Res(u)∩Z(λ)|<=d·#Z(λ). Since d<=2r(d−1), 2r(d−1)deg𝓟+d·#Z(λ)<=2r(d−1)(a·d'−ρ·deg[T])<=2r(d−1)·a·d'. So the π-degree term together with the Z(λ) charge is bounded by the printed 2r(d−1)·a·d' term [v2: N4: it even improves by 2r(d−1)ρ·deg[T], which is not used].
  - Σ_u|Res(u)∩W|<=d|W|.
  - Comparing with the degree of π on each component of 𝒵'^res, and adding the exceptional sets (λ'-zeros Nd, det T̂ zeros 2τ_0, 𝔈, FIX-N1's 3d, Lemma 3.5(ii), boundary) gives (4.1). ∎

**Corollary 4.2 (numerics; COMPUTED exactly in `numerics_K.out`, `numerics_K_r4.out`).**
- **Normalisation** (R18-T Cor. 3.5): d=E+2; d'∈[2E−2,2E+4] (worst case taken); g<=(d−1)(d−2)/2; a<=8h/625−d'+X−ρ; N<16h/625; d_def<=q/1000; deg ψ<=(E+1)d. The model is excluded when (4.1)/q<1551/4000.
- **The threshold τ_max.** Let τ_max be the largest τ_0 for which this holds.
  - r=4: τ_max/E≈0.71 (n=256), 0.565 (512), 0.494 (1024), 0.459 (2048), 0.442 (4096), 0.434 (8192).
  - r=8: 0.477 (n=256), 0.157 (n=512); τ_max≈0.0022E at n=1024, where no 𝔮<=E suffices; τ_max=0 from n=2048 [v2: FIX-5, N5].
  - r=16: 0.011 at n=256; fails beyond.
- **Combined with Prop. 3.3** (τ_0<=a d'/(ρ𝔮)) or the a-priori τ_0<=(Nd/ρ+d)/𝔮, (𝒦) with non-constant twist is excluded whenever 𝔮 is at least the value in the table (least dyadic 𝔮<=E):

| r | n | 𝔮 suffices (Q=128 / 256 / 1024 / 4096) |
|---|---|---|
| 4 | 256 | E/16 / E/32 / E/128 / E/512 [v2.1: RC-5] |
| 4 | 512 | — / E/4 / E/16 / E/64 [v2.1: RC-5] |
| 4 | 1024 | — / — / E/8 / E/32 |
| 4 | 2048–8192 | E/4 at n=2Q; nE/(8Q) in general |
| 8 | 256 | E/8 / E/16 / E/64 / E/256 [v2.1: RC-5] |
| 8 | 512 | — / E/2 / E/8 / E/32 [v2.1: RC-5] |
| 16 | 256 | none / none / E/2 (and E at Q=512, E/4 at 2048, E/8 at 4096, E/32 at 16384; i.e. 𝔮>=512E/Q) [v2: FIX-5] |

  - (Here — means n>=4Q, outside the strip. The S-dependence is nil for S∈{64,256}.)
  - **r=4:** since n<=2Q in the strip, 𝔮>=E/4 suffices at every scale. The margin is uniform: the limit is 0.4096<0.42496 (audit c1, verified to Q=2^19).
  - [v2: FIX-5] An independent check (audit c1) scanned **every** d'∈[2E−2,2E+4] and Q up to 16384. The minimum is always at d'=2E−2, and all thresholds are unchanged with the FIX-2 term.
- **D.** Theorem 4.1 does not use D. So these ranges include the D∈{1,2} lanes of (𝒦) with non-constant twist, which R18-T and FNAP leave open.

*Remarks.*
- **The dominant cost.** It is the p-term 2r·a·d'/(d'−E)≈4raE. That is ≈0.0512·r·q at large n, and less at small n because a<=8h/625−d'+X−ρ. Its factor 2r is the price of writing c^[T]·p(v) as an X-th power: E/X=2r. This is why only r<=8 (and r=16 at n=256) close.
- **Why the residual route works here.** Π_1 has no linear dependence on the pencil coordinate c. In the 𝒦 normal form that dependence sits entirely in Ξ, which is handled **per point** (Lemma 3.5), because for fixed u it is a section of 𝓣 in v.

---

## 5. Outside (𝒦): what the residual points cannot give

**Proposition 5.1 (per-point emptiness; (i) HEURISTIC remark that no B(u)/B(v) relation results, (ii) PROVED) [v2: FIX-4; v2.1: RC-1].** Outside (𝒦), let u be good.
- (i) (HEURISTIC) The residual vanishing is the single equation c^[T,t]𝒞_c(v)B(u)c=0 with c=c(u). Since 𝒞_c(v)B(v)c≠0 at generic v, it gives no relation between B(u) and B(v).
- (ii) For fixed u, Y↦G_{c(u)}(Y)|_{Γ'} is a section of O_{Γ'}(a), of degree a·d'>=d'>d'−E. So vanishing at the d'−E residual points is never contradictory point by point.

*Proof.*
- **(i) (heuristic justification)** The equation is not of the form 𝒞_c(v)B(v)c=0, which is the definition of (𝒦). No proof is claimed that no relation can be derived from it [v2.1: RC-1].
- **(ii)** Divisibility ℓ_u | G_{c(u)} gives div(G_{c(u)}|_{Γ'})>=ℓ_u·Γ', of degree d'. This is consistent whenever a>=1. ∎

**Proposition 5.2 (the E-penalty; the degree counts are PROVED, the cost conclusion is HEURISTIC) [v2: FIX-4].**
- **The obstruction.** On 𝒵', a v-function that is not an E-th power must be pulled back through 𝒵'→Γ'^{(1/E)}→Γ_v, whose degree over Γ_v is E·(d−1) (Prop. 1.1, Lemma 1.4(B)).
- **The structure of G.** G_{c(u)}(e(v))=Σ_{i,k,j}c_i^T c_k c_j^Q C_{k,ij}(e(v)). The factors c_i^T=β^X, α^X (E-th powers of (β,α)^{[1/(2r)]}) and C(e(v)) (E-th powers on 𝒵') are compatible with taking E-th roots. The factor c_kc_j^Q, of degree Q+1, is not.
- **Removing it costs.**
  - Squaring gives a genuine section whose v-side height is multiplied by E. The per-point cost is ≈E·a·d'≫q/N_good.
  - Using the first layer c^[T]∝𝒦𝓂(u)c^[D] (R18-T §3) costs X·deg[T] on the u-side, unchanged by passing to residual points.
- **Consequence.** Every section on 𝒵' encoding the residual vanishing outside (𝒦) has per-point cost >=min(X·deg[T], X·deg ψ, E·a·d') up to lower-order terms. (HEURISTIC: no rearrangement avoids this. This is the residual-point analogue of R18-T §5.5.)

*Why (𝒦) escapes.* Lemma 3.1 splits G into Π_1 (no pencil-linear factor; Π_1=λ(v)·π^X with π cheap, λ depending on v only) [v2.1: RC-3] times Ξ (pencil-dependent, but of degree τ_0 in v for fixed u).

**Question (b), degrees/irreducibility, answered.**
- 𝒵'^res has degree d'−E over Γ_u (generic fibre reduced) and <=d−1 over Γ'^{(1/E)}. [v2: FIX-3(b)] 𝒵^res is inseparable over Γ_v (Lemma 1.4(B)). The inseparable degree is E in the Fermat example; in general it is not determined.
- Irreducibility fails in general (Fermat: E−2 components).
- For random centres the arithmetic monodromy on the E+1 residual roots is transitive for E=8 and E=16 (COMPUTED; for E=16 via cycle-type combinatorics). It is not decided for E=32 [v2: FIX-3(a)]. Geometric irreducibility there is OPEN, and not needed.

**Question (d), better height bound.**
- In (𝒦): ρ·deg[T]<=a·d' (Prop. 3.3), a factor ≈0.43 better than a priori at n=256, tending to 1.
- Outside (𝒦): OPEN.

---

## 6. What remains, and next steps

**Residual after this note** (inside 𝔇_16 with global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128):
- (R1) Outside (𝒦): unchanged from R18-T. Non-constant twists with θ_max·rh<deg[T]<=e_M+d. The residual route gives nothing (HEURISTIC, Prop. 5.1(i)) [v2.1: RC-1].
- (R2) (𝒦) with 2a>=d'. Now closed for non-constant T in the ranges of Cor. 4.2, for every D. What remains open:
  - non-constant T with 𝔮 below the Cor. 4.2 thresholds;
  - r>=16, except n=256 with 𝔮>=512E/Q (Q>=512);
  - r=8 with n>=1024;
  - constant T with D∈{1,2} (FNAP §4).
- (R3), (R4): as in R18-T. Cor. 4.2 removes the D∈{1,2} non-constant part of (R3) inside (𝒦) in its ranges.

**Most promising next steps (HEURISTIC).**
1. **Sharpen Lemma 3.5 on the subline.**
   - By Prop. 1.2, the residual set over u lies in g_u(P¹(F_E)), with t^E=M_u(t) in the conic parameter.
   - In the frame of Prop. 3.3, p_i(v)·Ξ(u,v)=Ξ̃_u(e(v)) for a form Ξ̃_u of degree a in Y. So on the residual points it is the restriction of a binary form of degree a on ℓ_u.
   - On Γ' the same function is a ρ𝔮-th power (Lemma 3.5(i)).
   - The residual points are E+1 (or fewer) points of an F_E-subline of C_u, i.e. the roots of t^E=M_u(t). Reducing a polynomial modulo (αt+β)t^E+γt+δ replaces t^E by a Möbius expression, which lowers the degree.
   - If such a Frobenius reduction applies to Ξ̃_u, its zeros on the subline could be bounded by ≈a/E+O(1) instead of τ_0−1. That would remove the τ_0 restriction in Thm 4.1 and close (R2) for non-constant T for r=4 throughout, and for r=8 at n<=512.
   - Whether Ξ̃_u has the needed E-th-power structure along ℓ_u is unverified.
2. **(R1).** Seek a decomposition of 𝒞_c on Γ' that isolates the pencil coordinate, as Lemma 3.1 does in (𝒦). For example, write 𝒞_c=p⊗(Bc)^⊥+(kernel-defect term) and study the defect k_c:=𝒞_cBc (quadratic in c, ≢0 outside (𝒦)) through the own-line expansion of R18-T Lemma 3.2 at **residual** points, where the D-substitution is not needed.
3. **The 2r loss.** The factor 2r in Thm 4.1 comes from E/X. If p is itself a 2r-th power on Γ', for instance in polynomial-origin situations (R18-T v2.1 Prop. 2.2, which is CONDITIONAL on (H_lift), OPEN; its v1 hypothesis (H_bs) never holds) [v2: FIX-7], the factor 2r disappears from the p-term and r=16 would close. Worth testing on R18-T Example 4.3-type data.

---

## 7. Computations (this directory; run with `python3 -I`)

| script → output | content | result |
|---|---|---|
| `corr_fermat.py` (args E m N) | Fermat σ1: multiplicity of the contact root, residual degree, squarefreeness, factor patterns over GF(2^m) | contact exactly E (E=8,16; 60+40 points per field); residual degree E−2, squarefree; patterns (3,3) at E=8 and (2,4,4,4) at E=16 = Frobenius orbits on F_E∖{0,1} |
| `fermat_explicit.py` → `.out` | Example 1.6: v=diag(1,ζ,ζ/(1+ζ))u^[E] | all (u,ζ) incidences hold, E=8,16,32,64 |
| `corr_random.py` → `corr_random.out` | random centres σ1(BU), E=8,16,32 | contact multiplicity exactly E (the one degenerate sample at E=32 is a base point of e on Γ, see FIX-8); residual degree E+1=d−1, support {E+1,E,1,0}, squarefree; projective-polynomial factor patterns (3 per E) |
| `kappa_identities.py` → `.out` | Lemma 3.0, Lemma 3.5(i), Cor. 3.2 | 100/100 each |
| `numerics_K.py`, `numerics_K_r4.py` → `.out` | exact Fraction evaluation of (4.1); τ_max; 𝔮 thresholds | as in Cor. 4.2 |

Helpers `env_lib.py` and `ps.py` were copied from R18 (not needed by these scripts).

[v2: FIX-8, N8] Script notes:
- `corr_fermat.out`'s "symmetry … 0/0" test was **not exercised** and should be ignored.
- Script headers that cite "Theorem 4.4 of NOTE_CORRESPONDENCE_ROUTE.md" or "Prop 4.2" mean Thm 4.1 and Prop. 3.3 of this note.
- The scripts themselves are unchanged from v1. All owner outputs were re-run byte-identical by the auditor.

---

## 8. Status

| item | status |
|---|---|
| Lemma 1.1 | PROVED for m(w)<E (v2 proof); OPEN for m(w)>=E [v2: FIX-2] |
| Prop. 1.1 (contact exactly E via FNAK; degrees of 𝒵') | PROVED (uses FNAK, Stöhr–Voloch, R14.1) |
| Prop. 1.2 (projective-polynomial / F_E-subline structure) | PROVED (Lang's theorem cited); COMPUTED |
| Lemma 1.4 (separable over u, inseparable over v) | PROVED |
| Lemma 1.5 (transversality, with the cusp-tangent exception) | PROVED [v2: FIX-2] |
| arithmetic monodromy transitive (random centres) | COMPUTED for E=8, 16; not decided for E=32 [v2: FIX-3] |
| Example 1.6 (Fermat: E−2 Frobenius graphs) | PROVED; COMPUTED |
| Thm 2.1 (invariant functions are constant), Cor. 2.2 (Ξ≡0 or T̂-invariance ⇒ T constant) | PROVED |
| Lemma 3.0, 3.1 (𝒦 normal form), Cor. 3.2, Prop. 3.3 (ρ deg[T]<=a d'), Prop. 3.4, Lemma 3.5 | PROVED; identities COMPUTED |
| Thm 4.1, Cor. 4.2 ((𝒦), non-constant T, closed for large 𝔮/E, r<=8, and r=16 at n=256) | PROVED with the v2 repairs FIX-1, FIX-2 (no number changes); numbers COMPUTED exactly, independently reproduced |
| Prop. 5.1(ii), the 5.2 degree counts | PROVED |
| Prop. 5.1(i), the 5.2 cost conclusion, "the route cannot improve (R1)" | HEURISTIC [v2: FIX-4] |
| constancy of T in 𝔇_16; (R1); remaining (R2) ranges | OPEN |

Dependencies:
- R18-T v2.1 (audited, revision-checked).
- FNAK/FNAL/TSY/TSYC/FNAM/FNAN/FNAO/FNAP (reviewed PASS / PASS-with-fixes).

v1 of this note was independently audited (PASS-with-fixes). v2 applied FIX-1..8 and was revision-checked (PASS-with-fixes). v2.1 applies RC-1..8. No manuscript was edited.
