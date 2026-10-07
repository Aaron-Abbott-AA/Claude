# AUDIT — HYP M>=2, round 20 (owner v1): F_E-subline, constant twists in (𝒦), line-restriction bound, re-count of (R2)

7 October 2026. Independent adversarial referee audit of `src/HYP_M2_ROUND20_owner_v1.md` (sha256 361c9291…cbf2c3, unchanged during the audit; `src/` verified against `checks/src_SHA256SUMS.txt` at the end).

Rules kept: only `src/` was read and only `checks/` plus this file were written. No file whose name contains "DZ" was opened. Owner scripts were copied to `checks/owner_copy/` and run there with `python3 -I`, one process at a time, each under 1 min. All referee scripts are new, use exact arithmetic (`fractions.Fraction`, `galois`, `sympy`), and were run with `python3 -I`.

---

## §0 Verdict

**PASS-with-fixes.**

All three headline claims survive.
- **Prop. 3.1 / Cor. 3.2** ((𝒦) with constant twist forces a>=d', hence it is impossible at n=256 for every D) is correct and really is a two-line argument. The inequality a_max<d' at n=256 holds for every r>=4, Q and S by exact algebra, not only on the grid. It is genuinely new: at n=256 one has 2a_max/d'≈1.40, so R18-T Prop. 4.2 does not apply.
- **Lemmas 4.1–4.3 and Thm 5.1 ((4.1′))** are correct as proved, conditional on the cited inputs. Lemma 4.3 needs a 2-unit correction when g=0 (FIX-4), which changes no number.
- **Every threshold in the table** was re-derived by an independent exact implementation written from the printed formulas.
  - 216 parameter rows: r∈{4,8,16}, Q∈{128,…,16384} *including* Q=8192 (which the owner grid omits), S∈{64,256}, every dyadic n with 256<=n<=2Q (up to 32768), and all 7 values of d'.
  - There are 0 mismatches with the printed R20 patterns and 0 with R19 Cor. 4.2 (mode "R19"). Every closed 𝔮-set is upward closed.

There are two substantive fixes. Neither touches a headline claim.
- **Lemma 2.1(iii) is false** (FIX-1). It is labelled PROVED, but it is not used in any later proof.
- **Example 2.4's COMPUTED clusters are all degenerate points** on a contracted line of e (g=0), which are excluded from every count (FIX-2). The qualitative conclusion is still true: the referee locates genuine clusters at points with g≠0 over GF(2^21).

The remaining fixes are label and over-claim corrections (FIX-3), small statement repairs (FIX-4..7) and provenance items (FIX-8).

---

## Item table

| item | note's label | referee verdict |
|---|---|---|
| (1.1) V_u(z(v))=κ_u p(v)Ξ(u,v) | PROVED | **OK**. Uses 𝒞 formed with z (R19 FIX-1 respected). |
| Lemma 2.1(i) reduction mod P_u | PROVED | **OK** (`ref_misc` (e): 0 violations in 150 random tests). |
| Lemma 2.1(ii) Hasse-sparsity criterion | PROVED | **OK** (0 mismatches). |
| Lemma 2.1(iii) projective invariance of sparsity | PROVED | **FALSE** (FIX-1). Explicit counterexample; 72/200 random Möbius maps violate it. |
| Prop. 2.2 (reduction = vanishing order, E<=a<2E) | PROVED | **OK** with wording and off-by-one fixes (FIX-5). |
| Prop. 2.3(i) pointwise vacuity | PROVED | OK (a remark). |
| Prop. 2.3(ii) "E-cap: no more can be forced" | PROVED/COMPUTED | **Over-claim**: toy evidence for generic forms only, so HEURISTIC (FIX-3). |
| Prop. 2.3(iii) method bound attained (toy) | COMPUTED | OK (owner output reproduced byte for byte). |
| Prop. 2.3(iv) / Example 2.4 clustering | PROVED identity, COMPUTED | Identity **OK**. COMPUTED evidence sits at degenerate g=0 points (FIX-2). Relevance to (𝒦) is HEURISTIC. |
| Cor. 2.5 (H_po) | CONDITIONAL | OK as conditional. Small gap at Z(μ)∪Pole(μ) (FIX-7). |
| **Prop. 3.1** (constant T in (𝒦) ⇒ a>=d') | PROVED (FNAM2) | **CORRECT**, valid for every D. |
| **Cor. 3.2** (n=256 closed for constant T, every D) | PROVED + COMPUTED | **CORRECT**. Exact-algebra proof for all r>=4, Q, S. The max ratio 0.7007 is grid-specific; the supremum is 0.7009 (FIX-8b). |
| Remark 3.3 | PROVED | The identities are OK. "Therefore not closed by Prop. 3.1-type algebra" is HEURISTIC (FIX-3). |
| Lemma 4.1 (order transfer) | PROVED | **OK**. Uses only I(ℓ_u,branch)>=E, proved in all cases (R19 FIX-2 respected). |
| **Lemma 4.2** (N_Ξ(u)<=a−m+mb(u)) | PROVED | **OK**. |
| **Lemma 4.3** (\|𝔅\|<=B_𝔅) | PROVED | **OK except at g=0** (off by 2; FIX-4). No numeric effect. |
| Remark 4.4 | — | "without the factor deg ψ" is wrong (FIX-6). |
| **Thm 5.1 (4.1′)** | PROVED | **OK**. Every exceptional set is charged; checked term by term against R19 (4.1). |
| Prop. 5.2 (N4 in (4.1)) | PROVED in R19 | **OK**. The inequality is R19 Thm 4.1 Step 4 [N4]. The margin example −0.0039 → −0.31 is reproduced. |
| **Cor. 5.3 threshold table** | COMPUTED | **REPRODUCED**: 216 rows, 0 mismatches, extended to Q=8192 and n=2Q<=32768. |
| (6.1)/(6.2), Prop. 6.2 | PROVED | OK. Prop. 6.2 should state its homogeneity assumption (N6). |
| §6 three-term obstruction | HEURISTIC | OK as labelled. |

---

## Detailed audit

### A. Setting and (1.1)
- (1.1) is R19 Lemma 3.1 (𝒞_c=p⊗(Bc)^⊥ on Γ̃, formed with the morphism z) combined with c^[Q]=κ_uB(u)c at a good u.
- In characteristic 2, (Bc)^⊥·w=det(Bc,w) holds. Checked.
- **Pitfall "𝒞 must be formed with z":** respected. The Z(λ) charge (R19 FIX-1) is kept in Thm 5.1.

### B. §2 Frobenius reduction (negative results)
- **Lemma 2.1(i).**
  - At a finite root with A_2(t_i)≠0, t_i^E=A_1/A_2, so ξ(t_i)=R(t_i)/A_2(t_i)^K. Correct.
  - Coprimality of A_1 and A_2 means every finite root has A_2≠0.
  - A residual root at t=∞ (A_2 constant) is not counted. This is harmless (FIX-5).
- **Lemma 2.1(ii).** The Lucas/Leibniz argument is correct, and the decomposition is unique since deg D^{(j)}ξ_k<E. Confirmed by random tests.
- **Lemma 2.1(iii)** is false; see FIX-1.
  - Take E=8, a=8 and the binary form ξ=t·w^7, which has level s=1.
  - The swap t↔w gives t^7·w, which has level 7. The lemma predicts at most s+(a mod E)=1.
  - The proof's denominator count (γt+δ)^a=(γt+δ)^{a mod E}((γt+δ)^E)^K forgets that clearing ξ_k(M(t)) needs (γt+δ)^{deg ξ_k}, and deg ξ_k may exceed a mod E.
  - Affine changes (γ=0) do preserve the level: 0/200 violations.
- **Prop. 2.2.**
  - With t^E|ξ and E<=a<2E: ξ_0=0, R=ξ_1A_1, and roots of A_1 are not residual (A_1(0)≠0 when j(u)=E). So the bound is deg ξ_1<=a−E. Correct.
  - "Exactly deg ξ_1=a−E" in §0 should read "<=".
  - In the general sentence, the "unless" condition should be s<=a−m−K−1, not s<=a−m−K (at equality the two bounds coincide).
- **Prop. 2.2's scope.** It settles only the m=E case.
  - For m=ρ𝔮<E, which is exactly the remaining gap at n=256, the subline reduction *could* beat a−m if V_u were E-sparse along ℓ_u.
  - The note's evidence that it is not (Prop. 2.3(ii)) is a toy with generic forms. ξ=ω^tV_u is not generic: it is κ_u(ω·p)σ_u^{ρ𝔮} on Γ'.
  - So "≈a/E: no" is a HEURISTIC statement about these mechanisms, not a theorem (FIX-3).
- **Prop. 2.3(iii).** The toy reproduces the method bound: owner output reproduced byte for byte, `checks/owner_copy/toy_line_order.out`.
- **Example 2.4.**
  - The identity M(v_ζ)=M(u)^[8] is correct: (ζ_iu_i^8)^7=u_i^56 because ζ_i∈F_8^*. So Ξ(u,v_ζ) does not depend on ζ.
  - The owner count {0:4214, 6:7} is reproduced twice: the owner copy byte for byte, and `ref_fermat_cluster.py` by an independent code path, which also checks that the six v_ζ are distinct and ≠u.
  - **However, all 7 cluster points have U_1=0** (`ref_fermat_cluster.out`), and this matters:
    - These points lie on the contracted line {U_1=0} of e=σ1, so e(u)=(0:1:0)∈Bs(f), g=U_0U_1U_2=0 there, and ℓ_u∩Bs(f)≠∅.
    - So they are non-good points (FIX-N1). They also lie outside Prop. 1.2's hypothesis.
    - There M(u)∈M_2(F_2), so Ξ=det(M(u)c,M(u)c)=0 for a trivial reason.
  - The referee computed Ξ on the curve symbolically (`ref_fermat_mu49.py`): **Ξ=x^14(1+x^49)**.
    - Genuine clusters at points with g≠0 therefore exist exactly at x∈μ_49∖μ_7.
    - There are 294 such affine points, defined over GF(2^21) and not over GF(2^12).
    - All six Ξ vanish at 5 sampled points with g(u)≠0.
  - The qualitative claim (iv) therefore survives, but the COMPUTED statement as printed is misleading (FIX-2).

### C. §3 Constant twists (Prop. 3.1, Cor. 3.2): the attempt to break them
- **Proof.**
  - [T] constant means B=λB_0 with B_0∈GL_2(k) and λ∈K^*.
  - (𝒦) (𝒞_cBc=0 in K² for all c∈k²) then gives C_c(z)B_0c≡0 on Γ̃.
  - W(c,Y):=C_c(Y)B_0c is bihomogeneous of degree (2,a). Each of its three c-coefficients is a vector of degree-a forms that vanishes on z(Γ̃)=Γ', so F divides it.
  - If a<d', then W≡0. For every c∈k²∖0, the vector B_0c∈k²∖0 lies in ker C_c(Y) over k(Y), so Δ(c,Y)=0 for all c∈k². Since k is infinite, Δ≡0 in k[c,Y], contradicting FNAM2.
  - The step is right.
- **What it does not use.** It uses no count, no D, no good point and no reduction (if a_orig<d' no form of degree a is divisible by F, and the reduced a is smaller anyway).
- **FNAP §4 consistency.** The D=1 and D=2 counterexamples (C̃=z_1Ω and C̃=[[0,z_2],[z_1,0]]) have C̃z≠0, so they are not (𝒦)-type. They do not conflict with Prop. 3.1.
- **Inequality.**
  - a=M'+X−ρ−d', and a<d' ⟺ M−1+T−Q<4d'. With d'>=2E−2 this follows from M<8E−T+Q−7. Checked.
- **n=256.**
  - a_max<d' for all d'>=2E−2 ⟺ (2048/625)E+E/(2r)−Q/2<4E−4.
  - The left coefficient is <=3.4018<4 for r>=4, and E>=2^15. So the claim holds for **every** r>=4, Q and S, not just on the grid.
  - Exact maximum of a_max/d' over r<=64, Q<=2^14, S<=2^12 and all d': 0.700886, which is above the printed 0.7007 (grid S∈{64,256}). The supremum is 0.7009.
  - At n=512, min a_max/d'=2.28, so Prop. 3.1 does not reach n>=512, as the note says.
- **Novelty check.** At n=256, 2a_max/d'=1.40>1, so R18-T Prop. 4.2 (2a<d') does not apply. Prop. 3.1 is a genuine gain.
- **Verdict: survives.** (R2) with constant T is closed at n=256 for every D, inside (𝒦). Outside (𝒦), constant T with D∈{1,2} remains in (R3), and the note does not claim otherwise.

### D. §4 Line restriction
- **Lemma 4.1.**
  - In coordinates ℓ_u={Y_2=0}, A(z)=z_0^{deg A}A|_ℓ(t)+z_2·(…).
  - ord z_2=j(u)>=E. This is R19 Lemma 1.1(i)'s "in all cases" part, which holds without the m(w)<E restriction.
  - At a non-cuspidal place, ord t=1 (only non-cuspidality is needed, not "tangent is ℓ_u").
  - The bound is in fact min(N,j(u)). Correct.
  - **Pitfall "tangent limits at singular branches"** is avoided: no tangent-limit argument is used, and cuspidal u are excluded and charged.
- **Lemma 4.2.**
  - The order of ω^tV_u(z(y)) at y=u is ord(ω·p)+ρ𝔮·ord_uσ_u>=ρ𝔮, using p=λp' regular, σ_u(u)=0 and σ_u a section of 𝓣.
  - Lemma 4.1 then gives order >=m on ℓ_u, so ξ has at most a−m distinct zeros on ℓ_u∖{z(u)}.
  - Ξ-zero residual places map to zeros of ξ. Places sharing a point, or lying over z(u)∖{u}, add at most Σ_P(k_P−1)=mb(u).
  - It holds even when σ_u≡0, so the Lemma 3.5(ii) set need not be excluded. Correct.
- **Lemma 4.3.**
  - Step 1 (Δ^{(k)}(c(u),·) vanishes on ℓ_u, so Φ_u has order >=j(u)>=E at every place) is correct.
  - Step 2: φ²=Φ_u(u)². The degree 2deg ψ+2N_kd' is correct.
  - Step 3: from φ≡0, √ψ∉K gives δ_1=0 and δ_0=ψδ_2, and δ_2≢0 by the maximality of k. The bracket β̃(u)α̃(y)+α̃(u)β̃(y) vanishes to order e_ψ(u). The case split is correct. In fact either e_ψ(u)>=E or Δ_2∘z(u)=0.
  - Riemann–Hurwitz for separable ψ (ψ∉K² by R14.1): the number of ramified places is <=2g−2+2deg ψ, and wild ramification does no harm.
  - **Gap:** the final "both cases <=B_𝔅" fails by 2 when g=0 and k=1 (FIX-4).
- **Pitfalls.**
  - Bs(f)∩Γ' (R18-T Lemma 2.1A): points of high multiplicity with many branches are covered through δ_P>=k_P−1 in Σmb(u).
  - Prop. 1.2 (which needs ℓ_u∩Bs(f)=∅) is not used in §4–§5.

### E. §5 The count (4.1′) and N4
- **Term-by-term comparison with R19 v2.1 (4.1).**
  - The coefficient d'−E−τ_0+1 becomes D_1=d'−E−(a−m).
  - The Lemma 3.5(ii) exceptional set 2deg ψ is replaced by B_𝔅 plus the cuspidal places (2d'+2g−2, R19 Lemma 1.5). Lemma 4.1 needs non-cuspidal u, so this is required and present.
  - Σ_u mb(u)<=d·Σ_Pδ_P<=d(d'−1)(d'−2)/2 is added. Places u with P∈ℓ_u lie on the line (P^{[1/E]})^⊥, so there are <=d of them. δ_P>=k_P−1, and Σδ_P=p_a(Γ')−g, using that z is birational.
  - The FIX-1 Z(λ) charge, the FIX-2 cusp-tangent term (d'−E)⌊(2d'+2g−2)/(E−1)⌋, and the Σ(j−E), Σκ and W charges are all present.
  - The p-term uses R19's proved N4 inequality deg𝓟+#Z(λ)<=ad'−ρ deg[T] and d<=2r(d−1).
  - **No exceptional set is missing.** The only new exclusions are 𝔅 and the cusps, and both are charged with multiplicity one per place.
- **Applicability.** D_1>0 needs m>a−(d'−E): 0.400E, 0.338E and 0.308E for r=4, 8 and 16 at n=256. At m=E, D_1/E is 0.600, 0.662 and 0.692. At n=512, D_1/E is about −2.6 for every m<=E. So (4.1′) is an n=256 tool, as claimed.
- **Prop. 5.2.** The margin example (r=16, Q=128, n=256, 𝔮=E/16) gives −0.00386 at τ_0=1 and −0.30862 at τ_hi=85692, with no unclosed τ in between (concave check).

### F. Thresholds (independent exact recomputation)
`checks/ref_thresholds.py` was written from the printed formulas only:
- (4.1) [v2.1, including the FIX-2 term], (4.1)+N4 and (4.1′);
- the normalisation of R19 Cor. 4.2: d=E+2, 2g−2<=d(d−3), a=8h/625−d'+X−ρ, N=16h/625, deg ψ<=(E+1)d, d_def=q/1000, threshold 1551/4000;
- τ_hi=⌊min(ad'/(ρ𝔮),(Nd/ρ+d)/𝔮)⌋, with (4.1) restricted to τ<=d'−E.

The unclosed τ-sets are found by exact integer binary search: (4.1) is concave quadratic in τ and (4.1′) is linear. Results over 216 rows (r∈{4,8,16}, all Q∈{2^7..2^14}, S∈{64,256}, all n∈[256,2Q], all 7 d'):

| r | n | R19 mode | R20 ("all") | printed | match |
|---|---|---|---|---|---|
| 4 | 256 | 8E/Q | 2E/Q (via (4.1′)) | 2E/Q | yes, all Q |
| 4 | 512…2Q (to 32768) | nE/(8Q) | nE/(16Q) (via N4) | nE/(16Q) | yes; E/8 at n=2Q also at Q=2^15, 2^17, 2^19 |
| 8 | 256 | 16E/Q | 2E/Q (N4 alone 8E/Q) | 2E/Q | yes |
| 8 | 512 | 128E/Q | 32E/Q | 32E/Q | yes |
| 8 | 1024 | none | 64E/Q (Q>=512) | 64E/Q | yes |
| 8 | >=2048 | none | none | none | yes |
| 16 | 256 | 512E/Q (Q>=512), none at Q<=256 | 8E/Q (all Q>=128) | 8E/Q | yes |
| 16 | >=512 | none | none | none | yes |

- **R19 Cor. 4.2.** Mode "R19" reproduces every entry, including r=16: E at Q=512, E/2, E/4, E/8 and E/16 at Q=8192, E/32 at 16384.
- **Upward closure.** Every mode is upward closed in 𝔮 (0 exceptions).
- **Owner script.** It omits Q=8192 from its grid. The referee's grid includes it and every claim holds there.

---

## FIX list (substantive first)

**FIX-1 (substantive: a PROVED statement is false). Lemma 2.1(iii).**
- **Counterexample.** E=8, a=8: ξ=t·w^7 (level 1) becomes t^7·w (level 7) under t↔w, whereas the claim gives <=1. 72 of 200 random Möbius maps violate the claim (`ref_misc.out` (d)).
- **Correct statement.** The level is preserved by affine changes. Under a general Möbius change it is preserved, as level <=a mod E, only when s<=a mod E. Otherwise it can rise to E−1.
- **Impact.** (iii) is not used in Prop. 2.2–Thm 5.1. Remove it from the PROVED lists (§0 item 1, §9) or replace it with the corrected statement. Re-examine §7 step 2, where "F|_{ℓ_u} is E-sparse" is parameter-dependent.

**FIX-2 (substantive: misattributed computational evidence). Example 2.4 / Prop. 2.3(iv).**
- **The problem.** All 7 COMPUTED full clusters have U_1=0. They lie on the contracted line of e=σ1, where g=0 and e(u)∈Bs(f), so they are non-good. There M(u) has F_2-entries and Ξ vanishes trivially.
- **The rewrite.** State that on the curve Ξ=x^14(1+x^49) (independent of ζ). Then:
  - non-degenerate full clusters occur exactly at x∈μ_49∖μ_7, which are 294 points over GF(2^21);
  - over GF(2^12) only the degenerate x=0 points occur.
  - (Referee: `ref_fermat_mu49.out`.)
- **Labels.** Keep "PROVED" only for the toy identity. Label the inference for genuine (𝒦)-pencils HEURISTIC.

**FIX-3 (labels and over-claims).**
- **(a) Prop. 2.3(ii) / §0 item 2(ii).** "No more can be forced from Γ' data" is supported only by generic forms in a toy. ξ=ω^tV_u carries the (𝒦) structure (a ρ𝔮-th power on Γ'). Relabel HEURISTIC, with COMPUTED evidence.
- **(b) §0 "Answer" and "What failed".** '"≈a/E": no' should read "not obtainable by the subline reduction or by local data at z(u) alone (HEURISTIC beyond m=E)". Prop. 2.2 proves the m=E case only.
- **(c) Remark 3.3.** The identities are PROVED. The conclusion "not closed by Prop. 3.1-type algebra" is HEURISTIC.

**FIX-4 (Lemma 4.3 constant).**
- In the case φ≢0 the bound is 2deg ψ+2N_kd', which exceeds B_𝔅 by 2 when g=0 (k=1).
- Fix: define B_𝔅:=2deg ψ+2(2a−d')d'+max(2g−2,0).
- No number changes: the numerics use 2g−2<=d(d−3), which is >=0.

**FIX-5 (Prop. 2.2 precision).**
- "Unless deg ξ_k<=a−m−K" should be "unless max deg ξ_k<=a−m−K−1".
- §0's "exactly deg ξ_1=a−E" should be "deg ξ_1<=a−E".
- Add the residual parameter t=∞ when A_2 is constant. It is harmless, since ξ_1 is then a binary form of degree a−E.

**FIX-6 (Remark 4.4).**
- "Re-bounds that set without the factor deg ψ" is wrong: B_𝔅 contains 2deg ψ, the same size as Lemma 3.5(ii)'s bound.
- The second bullet should count distinct points and include mb(u).

**FIX-7 (Cor. 2.5, CONDITIONAL).**
- σ̃_u(z(u))=0 follows from σ_u(u)=0 only if μ(u)∈k^*.
- Add u∈Z(μ)∪Pole(μ) to the unbounded exceptional set, and Res(u)∩Pole(μ) to the count.

**FIX-8 (provenance and reporting).**
- (a) The owner grid omits Q=8192 although the note says Q∈{128,…,16384}. The referee filled the gap and all claims hold.
- (b) "Maximum a_max/d'=0.7007" is specific to S∈{64,256}. The supremum is (2048/625+1/8−2)/2≈0.7009, which is still <1.
- (c) Stale script headers:
  - `fermat_cluster.py` says "Example 5.2";
  - `toy_line_order.py` says "Lemma 3.5′";
  - `numerics_R20.py` has a comment "(C) R20 Thm 3.1 … N_good<=2degpsi+…" that matches neither the note nor the code (the code checks only a_max<d').
- (d) `env_lib.py` is described as an R19 helper. It is headed "helpers for NOTE_ENVELOPE_RIGIDITY" and imports a module `ps` that is not supplied. Correct the description.
- (e) §8 refers to `scripts/`, but the files are delivered in `owner_scripts/`.

---

## Minor notes

- **N1.** In Prop. 3.1, say explicitly that "Δ(c,Y)=0 for all c∈k²" implies Δ≡0 because k is infinite.
- **N2.** In Lemma 4.1, only non-cuspidality is needed for ord t=1. The order bound is actually min(N,j(u)).
- **N3.** In Thm 5.1 Step 3, say explicitly that the Lemma 3.5(ii) set (2deg ψ) is no longer removed, because Lemma 4.2 does not need σ_u≢0. It is replaced by B_𝔅 and the cusps.
- **N4.** For Σmb(u), mention that the points of Bs(f)∩Γ' (multiplicity >=E−3, R18-T Lemma 2.1A) are covered by δ_P.
- **N5.** Prop. 2.3(i) uses d'−E<=E+1 (R19 Remark 1.7), while the numerics conservatively scan d' up to 2E+4. This is consistent but worth one sentence.
- **N6.** Prop. 6.2: state the assumption that p̃⊗b̃_i^⊥ is homogeneous of degree a.
- **N7.** The owner's interval solver locates roots in Decimal and then verifies every segment by exact sign evaluation (assert). This is acceptable. The referee's solver is exact throughout, and its results agree.
- **N8.** `numerics_K.py` and `env_lib.py` were copied but not run. They have no output file to compare against, and env_lib needs the missing `ps` module.

---

## Files in `checks/`

| file | content |
|---|---|
| `src_SHA256SUMS.txt` | pre-existing checksums of `src/`, verified OK at the end of the audit |
| `owner_copy/{numerics_R20,fermat_cluster,toy_line_order}.py` + `.out` | owner scripts copied and re-run with `python3 -I`; all three outputs are **byte-identical** to `src/owner_scripts/*.out` (`cmp`) |
| `owner_copy/{env_lib,numerics_K}.py` | copied, not run (N8) |
| `ref_thresholds.py` / `.out` | independent exact (4.1), (4.1)+N4 and (4.1′) threshold computation: 216 rows, 0 mismatches, upward closed |
| `ref_misc.py` / `.out` | (a) Prop. 3.1/Cor. 3.2 ratios and exact algebra; (b) D_1; (c) the Prop. 5.2 margin; (d) the Lemma 2.1(iii) counterexample; (e) random tests of Lemma 2.1(i),(ii) and Prop. 2.2; (f) r=4, n=2Q up to Q=2^19 |
| `ref_fermat_cluster.py` / `.out` | independent recount of Example 2.4; locates the 7 clusters at U_1=0 |
| `ref_fermat_mu49.py` / `.out` | symbolic Ξ=x^14(1+x^49) on the toy curve; genuine (g≠0) clusters over GF(2^21) |
| `checks_SHA256SUMS.txt` | SHA-256 of every file above |
