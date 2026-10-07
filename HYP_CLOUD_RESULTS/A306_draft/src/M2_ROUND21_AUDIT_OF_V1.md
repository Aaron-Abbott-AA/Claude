# Audit of HYP M>=2 round 21 (owner v1): constant twists with D∈{1,2}, the families 𝔉_1/𝔉_2, and the own-point defect

7 October 2026. Independent adversarial referee audit of `src/HYP_M2_ROUND21_owner_v1.md` (sha256 `1088d185…5de`).

Rules kept:
- Only `src/` was read. Only `checks/` and this file were written.
- No file whose name contains "DZ" was opened.
- Owner scripts were copied to `checks/owner_copy/` and run with `python3 -I`, one process at a time. The referee's own scripts were also run with `python3 -I`; each took under 30 s.
- All 26 `src/` checksums in `checks/src_SHA256SUMS.txt` verify OK, and so do the owner's `SHA256SUMS.txt` entries.

---

## §0. Verdict: **PASS-with-fixes**

- **Prop. 2.1 survives in full.**
  - The classification "P_D≡0 ⟺ C̃∈𝔉_D" is correct over **any** field of characteristic 2 and for **every** a. "Exactly" is justified.
  - The hand proof (a UFD argument in k[z,Y]) never uses the size of a or any property of k beyond characteristic 2.
  - No pencil outside 𝔉_1/𝔉_2 with P_D≡0 exists. This was confirmed independently in original coordinates with Frobenius-twisted constants over GF(2^4) and GF(2^8) (check A).
- **Cor. 2.2 survives.**
  - The FNAO/FNAP count needs D>2 only for P_D≢0. Every other hypothesis holds in the constant D∈{1,2} lane.
  - The numbers are exact: 0.0433718q (D=1) and 0.0472784q (D=2), against 0.38775q.
  - One gap: "at every strip scale" rests on a finite grid. A one-line monotonicity argument closes it (FIX-2), and the referee verified that argument.
- **The "newly closed" claim survives with rephrasing.** It misstates the prior state: R20 Cor. 3.2 had already closed constant (𝒦) at n=256 for every D (FIX-3). What is new is the exclusion of constant-twist D∈{1,2} models with C̃∉𝔉_D, in (R2) at n>=512 and in (R3) at every n.
- **Main overclaim (FIX-1).**
  - Prop. 2.3, Cor. 2.4 and summary item 3 say that 𝔉_D satisfies "every algebraic identity of FNAL/TSY/TSYC/FNAM". They also say it "cannot be excluded" by those inputs.
  - Only the C-level consequences were checked: FNAM2, ℓ_u|G_c, (𝒦), F|Δ, the R19 normal form and the R19/R20 residual machinery.
  - Whether original P, R exist that realise C̃ (FNAL quotient, TSY factorisation, G5, and the full vector own-line identity that FNAL's determinant forgets) is not addressed. The note's own Remark 2.5 says this lifting might exclude 𝔉_D.

---

## Item table

| item | owner label | referee finding | fix |
|---|---|---|---|
| Prop. 2.1 (classification of P_D≡0) | PROVED; COMPUTED | **correct**, for every field of char 2 and every a; uniqueness and det formulas verified; FNAP §4 examples and FNAN §4's S=Q example lie in 𝔉_1/𝔉_2 | N2 |
| Cor. 2.2 (constant D∈{1,2}, C̃∉𝔉_D excluded) | PROVED cond. on FNAO/FNAP count; COMPUTED | **correct**; count hypotheses hold; numbers reproduced exactly; whole-strip claim needs the monotonicity sentence | FIX-2, N11 |
| Prop. 2.3 (i)–(vii) | PROVED; COMPUTED | each identity correct (checked symbolically and over GF(16) with a genuine twist); title "all available identities" overclaims; (vi)'s reason is imprecise | FIX-1, FIX-6, N7, N10 |
| Cor. 2.4 (negative result for (a)) | PROVED | correct relative to the **C-level** identities; overclaims for FNAL/TSY/TSYC; internally inconsistent with Remark 2.5 | **FIX-1** |
| Remark 2.5 | HEURISTIC | fine | — |
| Lemma 3.1 | PROVED | correct (tautological); hypothesis c_1c_2≠0 unnecessary | N4 |
| Lemma 3.2 (i)–(iv) | PROVED (R14.1, R18-T L1.2); bound COMPUTED | proofs correct; numeric bound misstated (0.110235 > 0.1102); "⊋" unproved; dependency list incomplete | FIX-4, FIX-5, N5 |
| Cor. 3.3 | PROVED (negative) | the order-0 statement is correct; the summary's "cannot produce a per-point bound" generalises beyond the mechanism treated | FIX-5 |
| Remark 3.4 | PROVED identity; usefulness OPEN | identity correct; the "m=1" order claim is generic, i.e. heuristic | N8 |
| Remark 3.5 | HEURISTIC | fine; "<=0.11q" slightly wrong (0.1102347q) | FIX-4 |
| "Newly closed" | PROVED, numbers COMPUTED | substantively correct; prior-state sentence contradicts R20 Cor. 3.2 | **FIX-3** |
| owner scripts | COMPUTED | all three outputs byte-identical on re-run; stale headers; GF(2)-only toy | N1, N3 |

---

## Detailed audit

### 1. Reproduction of the owner computations

The owner scripts were copied to `checks/owner_copy/` and run with `python3 -I`. All three outputs compare byte-identical (`cmp`) to `src/owner_scripts/*.out`:
- `classify_PD.out`: 20/20 OK;
- `family_check.out`: 36/36 plus the control; 5.9 s;
- `numerics_R21.out`: 1260 rows.

What each script actually tests:
- **`classify_PD.py`** works over F_2 in C̃-coordinates. Each unknown maps to a single monomial with coefficient 1, so the kernel dimension is field-independent, as the owner says.
  - It does **not** test the change of coordinates C_c=L^{−t}C̃(Bc) with L=K(B^{−1})^[D]. Check A does.
- **`family_check.py`** uses B, L∈GL_2(F_2). There B^[D]=B, so the Frobenius twist in K=LB^[D] is never exercised. Check C does exercise it (N3).
- **`numerics_R21.py`** is correct (check D reproduces it).

### 2. Prop. 2.1: the classification

**Hand proof, step by step.**
- **Step 1.**
  - D=1: z_1q_1=z_2q_2 in characteristic 2. Since z_1, z_2 are coprime primes of k[z,Y], z_2|q_1. Then q=h·z^⊥ with h z-linear.
  - D=2: z_2²|q_1 with q_1 quadratic in z, so q_1=z_2²h' and q_2=z_1²h'.
  - D>=3: the supports are disjoint, so q≡0. Only D>2 is needed, not D>=4.
- **Step 2.** C̃_0z=hz^⊥, resp. h'z^{⊥[2]}.
- **Step 3.** Every row r of a z-linear M with r·z=0 is λz^⊥, with λ∈k[Y]_a. Hence M=μ⊗z^⊥.
- **Step 4.** The diagonal of hΩ+μ⊗z^⊥ (and of h'J+μ⊗z^⊥) is (μ_1z_2, μ_2z_1). So μ=0, and then h=0. Uniqueness follows.
- **Step 5.** This uses z^⊥·z=2z_1z_2=0.
- **Step 6.** det = h(h+μ·z), resp. h'(h'z_1z_2+μ_1z_1²+μ_2z_2²).

All steps are valid over any field of characteristic 2. The proof uses only that k[z,Y] is a UFD and that z_1, z_2 are primes. The degree a plays no role. So "exactly" and "unique" are justified for every a and every field of characteristic 2. The FNAM2 criterion follows from Step 6 and det L^{−t}≠0.

**Independent checks.**
- **Check A (`A_classify_twisted.py`).** The map (C_P,C_R)↦P_D(c,Y)=(Kc^[D])^tC_c(Y)(Bc) was set up in **original coordinates** over GF(2^4) and GF(2^8), with B∉GL_2(F_2). K was either random or taken from FNAP's actual iteration (B_2=B^[Q]B, Q=2^7, K=B_2^[D]).
  - For D∈{1,2,4,8} the kernel dimension is 4, 3, 2, 2 per Y-monomial.
  - The pulled-back family L^{−t}𝔉_D(Bc) lies in the kernel and spans it, in 32/32 trials. The same holds at a=1, 2.
  - Since the map preserves Y-monomials, the kernel for degree a is (kernel at a=0)⊗k[Y]_a. So the a=0 computation already proves the claim for **all** a (N2).
  - Negative control: with the Frobenius on B^{−1} omitted (L'=KB^{−1}), the family leaves the kernel for D=2 (8/8). For D=1 and for D>=4 the control is vacuous by construction. So the twist in L is essential and correctly placed.
- **Check B (`B_symbolic_identities.py`).** Over F_2 with generic indeterminates, the following all hold: z^{[D]t}C̃z=0 on the families, both determinant formulas, the diagonal (uniqueness) identity, and rank one for D=4, 8. A generic a=0 pencil solve gives kernel dimensions 4, 3, 2, 2, 2, 2 for D=1, 2, 4, 8, 3, 5.

**Attempt to find a pencil outside 𝔉_1/𝔉_2 with P_D≡0.** Kernel dimension equals family rank in every case, so the kernel contains nothing else. The hand proof excludes such pencils in general.

**Sanity check against PRIMARY's examples.**
- FNAP §4's two examples are (h=z_1, μ=0)∈𝔉_1 and (h'=1, μ=0)∈𝔉_2.
- FNAN §4's formal S=Q example (A=I, C_P=I, C_R=0) gives B=Ω, K=I and L=Ω, so C̃=z_2Ω∈𝔉_1. P_D≡0 is confirmed in check A.

So the families exactly generalise PRIMARY's obstructions, and the note treats them as obstructions only: Cor. 2.4 says "not a claim that the models exist". **The FNAP §4 pitfall is respected.**

### 3. Cor. 2.2: what the FNAO/FNAP count needs, and whether it holds here

| requirement of FNAO §2–§4 / FNAP §2–§3 | status for constant T, D∈{1,2} |
|---|---|
| CMIX with constant A∈GL_2(k) and a common scalar λ | holds: R18-T Lemma 1.1 with T=λT_0 gives 𝒜=λ^ρ(T_0^t)^[ρ] |
| original strip (global alignment, common image, zero top, first scalar, Q>=128, 256E<=h<4QE) | holds: these are the note's standing hypotheses (𝔇_16) |
| λ-zeros <=N·d; boundary 6d_def+7 | holds; FNAN §1 and R18-T Lemma 1.1, with FIX-N1 (off {g=0} and Bs(e)) |
| <=Q+1 slopes from c^tAc^[Q]=0 | holds; independent of D |
| c^[T]∥Kc^[D], K=B_{j+1}^[D] | holds; for D∈{1,2}, S=Q^jD>=64 forces j>=1 |
| **P_D≢0** | this is the only place FNAP uses D>2 (FNAP §3); it is exactly the hypothesis C̃∉𝔉_D (Prop. 2.1) |
| <=D+2 exceptional slopes, (E+1)d each (ψ-fibre) | holds; independent of D |
| <=a own lines per other slope; distinct u give distinct lines | holds |
| numerics: FNAP handles only D>=4 | the note recomputes; (D+2)/n<=4/256 |

**Numerics (check D, `D_numerics_exact.py`, exact Fractions).**
- The owner's grid maxima are reproduced exactly at (r,Q,S,n)=(4,128,64,256):
  - D=1: 7451214389181/171798691840000 ≈ 0.04337178;
  - D=2: 8122364470431/171798691840000 ≈ 0.04727838.
- Each term of the bound divided by q is non-increasing in r, Q, S and n:
  - (16/625)(1+2/E);
  - (D+2)/n·(1+1/E)(1+2/E);
  - 8(Q+1)/(625rQS);
  - 6/1000;
  - 7/q.
- This was spot-checked at non-dyadic r and n and far outside the grid. So the whole-strip supremum is the corner value.
- On the actual D-lane (S=Q^jD>=Q) the supremum is slightly smaller: 0.0433453 (D=1) and 0.0472384 (D=2).
- The margin to 1551/4000 is >=0.3404.
- **Gap (FIX-2).** The note's proof states the bound only over the finite grid r<=64, Q<=2^14, S<=2^12, yet claims "at every strip scale". The monotonicity sentence is missing.

**Inside (𝒦).** Here P_D=z^{[D]}·q with F|q, so P_D=F·P_D'. The line count only improves, and the conclusion is consistent.

### 4. Prop. 2.3, Cor. 2.4: the negative result

**(i)–(vii), item by item.**
- **(i)** For constant [T], (𝒦) ⟺ F|L^{−t}q(B_0c,Y) as polynomials in (c,Y), since k is infinite. Then F|h·z_2 and F|h·z_1 force F|h. Correct.
  - "a>=deg h>=d'" should read "a=deg_Y h>=d' (h≢0 by FNAM2)" (N10).
- **(ii)** C̃≡μ⊗z^⊥ mod F when F|h. So F|(C_P,C_R) ⟺ F|μ. Correct. The automatic h≢μ·z argument is correct.
  - Note: R19's reduction divides by F^k. On 𝔉_D with F|h and F|μ the reduced pencil is again in 𝔉_D, so the family is closed under the reduction.
- **(iii)** and **(iv)** are correct.
- **(v)** G_{c(u)}=ν_uP_D(c(u),·)≡0, so own-line divisibility is vacuous. Correct.
- **(vi)** Ξ(u,v)=det(B(v)c,B(u)c)=0 because B is **projectively** constant (B=λ^ρB_0), not constant. The reason given for "the R20 per-point bounds say nothing" is imprecise:
  - Ξ≡0 makes N_Ξ(u) maximal. If a−m were smaller than the number of residual places, Lemma 4.2 would then force u∈𝔅.
  - The bounds are vacuous because a>=d' on 𝔉_D∩(𝒦) (R20: "at n>=512 the line bound is vacuous"). FIX-6.
- **(vii)** W_c=L^{−t}(h/F)(Bc)^⊥ is correct for D=1. The D=2 analogue L^{−t}(h'/F)(Bc)^{⊥[2]} is not stated (N7).

**Independent checks.**
- **Check C (`C_family_twisted_GF16.py`, own sparse-polynomial code over GF(2^4)).** B, L were chosen with entries outside F_2, so the twist K=LB^[D] is genuinely exercised for D=2. F was a conic or the Fermat cubic, with a=d'..d'+2.
  - All of the following hold in 36/36 cases: P_D≡0, (𝒦), Δ≢0 and F|Δ, F∤(C_P,C_R), the normal form, and the exact C_cBc formula.
  - Controls:
    - F∤h: (𝒦) fails 3/3 while P_D≡0 persists 3/3;
    - wrong twist K'=LB: P_D≢0 in 3/3;
    - a random pencil: P_D≢0 in 3/3.
- **Check B** verifies the identity L^tΩL=det(L)Ω, which is used to see that (Kc^[D])^⊥ and L^{−t}(Bc)^⊥ agree projectively for D=1. This is consistent with P_D≡0.

**Overclaim (FIX-1).** Cor. 2.4 and summary item 3 assert two things:
- that 𝔉_D satisfies "every algebraic identity of FNAL/TSY/TSYC/FNAM/FNAM2";
- that (𝒦) with constant T, D∈{1,2}, a>=d' "cannot be excluded by FNAL/TSY/TSYC/FNAM/FNAM2/FNAP…".

What is verified is only that 𝔉_D satisfies the C-level consequences of those inputs: FNAM2 (Δ≢0) and ℓ_u|G_c (FNAL2/TSYC/FNAM3), together with (𝒦), F|Δ, the normal form and R20 Prop. 3.1. What FNAL/TSY themselves assert is not checked, for three reasons:
- FNAL defines H_b=[f^[X]]_×P^t/F from **original** P, R satisfying global alignment.
- TSY then factors H_b=J^[X]C_b(J^[ρ])^t.
- FNAL §4 states that FNAL2 is necessary but not sufficient: "taking a determinant forgets a component in span(f^[X])".

So whether some original (P, R, A) with G5 produces a given C̃∈𝔉_D is open. The note itself proposes in Remark 2.5 that "the rank-one-plus-scalar structure of 𝔉_D … may contradict [G5] after lifting through TSY/FNAL". That is inconsistent with a PROVED claim that FNAL/TSY cannot exclude 𝔉_D.

The last sentence of Cor. 2.4 ("G5, PRIM, the point count and the higher own-line layers are not checked") partly scopes the claim but does not repair it. The label PROVED is right only for the restated, C-level version.

### 5. §3: Lemma 3.1, Lemma 3.2, Cor. 3.3, Remarks 3.4–3.5

**Lemma 3.1.**
- G_c|_{ℓ_u}=c^[T]·V_u|_{ℓ_u} vanishes iff V_u|_{ℓ_u}=η(c^[T])^⊥. Correct.
- With c a constant vector this is immediate, and c_1c_2≠0 is not needed: if c_1=0, take η=V_1/c_2^T (N4).
- Residual v has z(v)∈ℓ_u (R20 §1), so the residual vanishing is implied. Correct.
- "Carry nothing new" is an interpretation; it is accurate relative to ℓ_u|G_c.

**Lemma 3.2.**
- **(i)** Correct.
  - Good u avoid Bs(e) and {g=0}, so z(u)=[e(u)]∈ℓ_u (R18-T Lemma 3.1: u^[E]·e(u)=0).
  - Then G_{c(u)}(z(u))=0 by FNAM3/TSYC, and c^[Q]=κ_uB(u)c gives c^[T]·κ(u)=0.
  - c^[T]=(β^X,α^X) and κ∥(α^X,β^X). Verified in check B.
  - The dependency on FNAM3/TSYC should be listed (N5).
- **(ii)** The squaring formula is verified symbolically (check B). The degree is 2deg ψ+2(ad'+ρ·deg[T]).
  - deg z^*O(1)=d' because 𝒞 is formed with the morphism z and Γ̃→Γ' is birational. The Bs(e)∩Γ̃ pitfall is handled correctly.
  - 𝓣^{ρ𝔮} has degree ρ·deg[T].
- **(iii)** The dichotomy is correct.
  - ψ∉K² (R14.1) gives K-independence of 1 and √ψ.
  - Equivalently, x²+ψy²=0 with x, y∈K² forces x=y=0.
  - κ≡0 ⟺ κ²≡0 by injectivity of Frobenius.
  - Zeros of a nonzero component bound the good u with κ(u)=0. Good points are counted as places, which is conservative. Z(λ') is already outside the good set.
  - **Numeric misstatement (FIX-4).** The exact grid maximum of deg κ²/q is 946909077437/8589934592000 = 0.11023472 (check D). This is **larger** than the stated "<=0.1102q" and larger than Remark 3.5's "<=0.11q".
    - The whole-strip supremum equals this corner value (the same monotonicity applies).
    - It is 0.1102324 with R19's sharper d'<=2E+1.
    - Use "<0.1103q".
- **(iv)** Correct. However, the summary's "(𝒦_ψ) ⊋ (𝒦)" asserts strictness, and nothing shows that (𝒦_ψ)∖(𝒦) is non-empty, even formally. Use ⊇ (FIX-5).

**Cor. 3.3.**
- V_u(z(u))=𝒞_c(u)c^[Q]=κ_uκ(u). Correct.
- Since κ(u)∥(c^[T])^⊥, the exceptional direction is ω∥c^[T], for which ξ^ω_u=G|_{ℓ_u}≡0. Every other ω gives order 0 at z(u). Correct.
- The labels are right for this statement. Summary item 5 ("the residual route therefore cannot produce a per-point bound below the trivial a+mb(u)") and the bullet "no per-point bound of R20 type is available" go beyond what is proved:
  - the proof covers only the order-at-z(u) mechanism of R20 Lemma 4.2, at good u off Z(κ);
  - outside (𝒦), R20's (1.1)/Ξ factorisation does not even exist, so "comparison factor" is undefined there.
  - Restrict the wording (FIX-5).

**Remark 3.4.**
- The identity k_{c(u)}(v)=β(u)(ψ(v)+ψ(u))k_22(v) is verified (check B).
- The split V_u(z(v))=κ_u[k_c(v)+𝒞_c(v)(B(u)+B(v))c] is linear algebra in characteristic 2. B(u)+B(v) needs a common local frame, as in R18-T Prop. 4.1(iii).
- The order statement "generically 1, so m=1" is a generic, heuristic claim. It also needs the following, which the note does not record (N8):
  - β(u)≠0;
  - a non-cuspidal u for the transfer to ℓ_u (R20 Lemma 4.1);
  - the tangent-limit caution at singular branches.

**Remark 3.5.** HEURISTIC, correctly labelled. Apart from 0.11 (FIX-4), no issue.

### 6. The "newly closed" claim

- **Consistency with FNAP.** FNAP §4 says only that FNAP's nonvanishing argument fails for D∈{1,2}. R21 shows the failure locus is exactly 𝔉_D and that FNAP's count applies verbatim off it. This is consistent and does not contradict FNAP §4: no claim is made that 𝔉_D models exist or are excluded.
- **Consistency with R20.** R20 v2.1 Cor. 3.2 already closed "(R2) with constant T at n=256 for every D, including D∈{1,2}". It left open "constant T with a>=d' and D∈{1,2}". The note's sentence "Before this note, the whole D∈{1,2} constant lane was open" is therefore false (FIX-3).
- **What is genuinely new:**
  - (R2) constant T, D∈{1,2}, n>=512 (a>=d'), C̃∉𝔉_D;
  - (R3) constant T, D∈{1,2}, outside (𝒦), every n in the strip, C̃∉𝔉_D.
  - Inside (𝒦) the residual is 𝔉_D∩{F|h}, a>=d' (n>=512). Outside it, 𝔉_D∩{F∤h}.
- **Overclaim check.** "Closed except the two explicit families" is accurate once the phrase is read as "excluded when P_D≢0". The families are parametrised by (L, B), i.e. they depend on the twist. That is fine, but should be said.

### 7. Pitfall checklist

| pitfall | finding |
|---|---|
| Γ' contains all base points of f | not used by R21's new arguments; no violation |
| Bs(e)∩Γ̃ nonempty | handled: good u avoid Bs(e) (R18-T FIX-3); degrees use z^*O(1) with deg d' |
| tangent limits at singular branches (char 2) | only Remark 3.4's order claim is local; it is generic, so N8 |
| 𝒞 formed with z; Z(λ) charged | 𝒞=C(z) throughout; {λ'=0} is outside the good set (Nd charged in FNAP's count) |
| every exceptional set charged | Cor. 2.2 inherits FNAP's full charge list; Lemma 3.2(iii) counts zeros among good u only; Cor. 3.3 is stated off Z(κ) |
| FNAP §4 counterexamples are to the algebraic step only | respected: 𝔉_D is presented as an obstruction (Cor. 2.4 last sentence), not as models |
| conditional on FNAO/FNAP count | the count's only D-dependent input is P_D≢0, which is exactly the hypothesis; the other inputs hold (§3 table); numerics recomputed |

---

## FIX list (substantive first)

**FIX-1 (substantive; overclaim in a PROVED negative result).** Restate Prop. 2.3's title, Cor. 2.4 and summary item 3 as:

> 𝔉_D satisfies the C-level consequences used in R18-T–R20, namely FNAM2 (Δ≢0), own-line divisibility ℓ_u|G_c (the content of FNAL2/TSYC/FNAM3), (𝒦)⟺F|h, F|Δ, the R19 normal form, R20 Prop. 3.1 and the R19/R20 residual machinery. Hence no argument using only these consequences excludes 𝔉_D.

- Delete "every algebraic identity of FNAL/TSY/TSYC/FNAM" and "cannot be excluded by FNAL/TSY/TSYC…".
- State explicitly that it is OPEN whether 𝔉_D lifts to original data. That means original P, R with global alignment and G5 whose FNAL quotient factors through TSY with C=C̃, together with FNAL's forgotten span(f^[X]) component and R16's full vector own-line identity.
- This makes Cor. 2.4 consistent with Remark 2.5.

**FIX-2 (gap in a PROVED proof; easy).** In Cor. 2.2's proof, add the monotonicity argument. Each term of (N d+(D+2)(E+1)d+(Q+1)a+6d_def+7)/q is non-increasing in r, Q, S and n, so the supremum over the whole strip is the value at (4,128,64,256):
- 0.0433718 (D=1) and 0.0472784 (D=2);
- on the true D-lane S>=Q: 0.0433453 and 0.0472384.

Without this, "at every strip scale" rests on the finite grid r<=64, Q<=2^14, S<=2^12 (check D).

**FIX-3 (substantive misstatement of the prior state).** Replace "Before this note, the whole D∈{1,2} constant lane was open" with the following:

> R20 Cor. 3.2 had closed constant (𝒦) at n=256 for every D. New here: constant-twist D∈{1,2} with C̃∉𝔉_D is excluded in (R2) for n>=512 and in (R3) (outside (𝒦)) for every n in the strip.

Make the same correction in §0 "Newly closed" and §4.

**FIX-4 (numeric).**
- Lemma 3.2(iii), summary item 4, Cor. 3.3 and §5: the exact maximum of deg κ²/q is 0.11023472. Replace "<=0.1102q" with "<0.1103q" (or "<=0.110235q").
- Remark 3.5: "<=0.11q" → "<0.1103q".

**FIX-5 (scope).**
- Summary item 4: "(𝒦_ψ) ⊋ (𝒦)" → "(𝒦_ψ) ⊇ (𝒦)". Strictness is not shown.
- Summary item 5 and Cor. 3.3's second consequence: restrict the claim to "the R20 order-at-z(u) mechanism (Lemma 4.1–4.2) yields order 0 for every ω∦c^[T], and nothing for ω∥c^[T], at all good u off Z(κ)".
- Drop "the residual route cannot produce a per-point bound below a+mb(u)", or label it HEURISTIC.

**FIX-6 (imprecise reason).** Prop. 2.3(vi):
- "Since B is constant" → "since [B] is constant (B=λ^ρB_0)".
- Add that the R20 line bound (Lemma 4.2) is vacuous on 𝔉_D∩(𝒦) because a>=d' (so a−m>=d'−E>=#residual), not merely because Ξ≡0.

---

## Minor notes

- **N1.** Script headers use stale numbering: `classify_PD.py` "Prop. 1.1"; `family_check.py` "Prop. 1.3"; `numerics_R21.py` "Cor. 1.2", "Lemma 2.3". The note refers to `scripts/`, but the delivered directory is `owner_scripts/`.
- **N2.** The P_D map preserves Y-monomials, so the a=0 kernel computation already proves the kernel statement for all a. The COMPUTED check can say so; it is then a complete independent proof of Prop. 2.1 for every a.
- **N3.** `family_check.py` draws B, L∈GL_2(F_2), so B^[D]=B and the Frobenius twist in K=LB^[D] is not exercised. Referee check C repeats the test over GF(16) with a genuine twist (36/36, plus a wrong-twist control that fails).
- **N4.** Lemma 3.1: the hypothesis c_1c_2≠0 is unnecessary.
- **N5.** Lemma 3.2's dependency list should add FNAM3/TSYC (for G_{c(u)}(z(u))=0), R18-T Lemma 3.1's u^[E]·e(u)=0, and R18 §5 (deg[T]<=Nd/ρ+d).
- **N6.** Notation: κ_u (a scalar, c^[Q]=κ_uB(u)c) and κ(u) (the defect vector) collide. Rename one of them.
- **N7.** Prop. 2.3(vii): add the D=2 form W_c=L^{−t}(h'/F)(Bc)^{⊥[2]}.
- **N8.** Remark 3.4's "order >=min(ρ𝔮, ord k_22+e_ψ(u)), generically 1" needs β(u)≠0, a common local frame for B(u)+B(y), and non-cuspidality for R20 Lemma 4.1. The "m=1" conclusion is HEURISTIC.
- **N9.** The FNAO/FNAP input files still carry "independent review PENDING" headers. Their acceptance is recorded in the PRIMARY 13:01 message (DZ-reviewed) and in R18-T §1 (Claude PASS-with-fixes). Cite these.
- **N10.** Prop. 2.3(i): "a>=deg h>=d'" → "a=deg_Y h>=d', with h≢0 by FNAM2".
- **N11.** The Cor. 2.2 grid includes S=64 and S<Q. These are not in the D∈{1,2} lane (S=Q^jD>=Q), so the grid is conservative; say so.
- **N12.** Prop. 2.1 Step 1 needs only D>=3. "D>=4" is used only because D is a power of 2.

---

## checks/ files

| file | content | result |
|---|---|---|
| `src_SHA256SUMS.txt` | pre-supplied checksums of `src/` | 26/26 OK |
| `owner_copy/{classify_PD,family_check,numerics_R21}.py` → `.out` | owner scripts re-run with `python3 -I` | all three outputs byte-identical to the owner's |
| `gfpoly.py` | referee helper: sparse multivariate polynomials over GF(2^m) | — |
| `A_classify_twisted.py` → `.out` | Prop. 2.1 in original coordinates with Frobenius-twisted K, B over GF(2^4) and GF(2^8); D∈{1,2,4,8}, a=0,1,2; FNAP iteration K; wrong-twist control; FNAN §4 example | 32/32 OK; D=2 control leaves the kernel 8/8; FNAN example ∈𝔉_1 |
| `B_symbolic_identities.py` → `.out` | symbolic char-2 identities: families, determinants, uniqueness, generic a=0 solve for D=1,2,3,4,5,8; Lemma 3.1, Lemma 3.2(i)(ii), the k_c expansion, Remark 3.4, L^tΩL=det L·Ω | 21/21 OK |
| `C_family_twisted_GF16.py` → `.out` | Prop. 2.3(i)–(v),(vii) over GF(16), conic and Fermat cubic, genuine twist; controls (F∤h; wrong twist; random pencil) | 36/36 all True; controls as expected |
| `D_numerics_exact.py` → `.out` | Cor. 2.2 and Lemma 3.2(iii) numerics, exact; grid reproduction; monotonicity; whole-strip and D-lane suprema | 0.04337178 / 0.04727838 reproduced; κ² maximum 0.11023472 (> 0.1102) |
| `checks_SHA256SUMS.txt` | checksums of all of the above | — |
