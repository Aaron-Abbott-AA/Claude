# AUDIT of HYP M>=2 round 24 (owner v1), 7 October 2026

Independent adversarial referee audit of `src/HYP_M2_ROUND24_owner_v1.md` (sha256 `111cced0…1edd`; all 31 `src/` files match `checks/src_SHA256SUMS.txt`).

**Rules kept.**
- No file whose name contains "DZ" was opened.
- Only `src/` was read.
- Writes went only to `checks/` and to this file. One debug snippet was first written to the scratchpad parent directory by mistake. It was moved into `checks/debug_sympy_iszero.py` and nothing else was left outside.
- Owner scripts were copied to `checks/owner_copy/` and run with `python3 -I`, one process at a time, each under one minute.
- My own scripts are exact (Fractions, sympy over GF(2), hand-rolled GF(2^8)) and also run with `python3 -I`.

## §0 Verdict

**PASS-with-fixes (minor).**

No mathematical error was found in any headline result. All four items the coordinator singled out survive:

- **Lemma 3.1 (partial Wronskian divisor R_s): SURVIVES (PROVED).**
  - The truncated minors are well defined up to a common factor h^s(D_t x)^{Σ'} under a change of frame and parameter.
  - The degree bound (a) and the weight bound (b) are correct in every characteristic, including 2.
  - An independent exact test was run on genus 1 and genus 2 Artin–Schreier curves, with deg R_s computed exactly over the algebraic closure. It gave no failure, and (a) holds with equality at s=r+1, as SV requires.
- **Thm 3.3 ((R1) closed outright): SURVIVES (PROVED, conditional on the inputs it names).**
  - Every link was re-derived.
  - Every case is covered: 𝔮_max>S, or 𝔮_max<=S with dim V∈{2,3,4} and every p-adic-closed order sequence (brute force without the popcount assumption).
  - The numbers were recomputed exactly: the corner value 91941792089517/549755813888000≈0.1672411 is reproduced, and the exact failing set over 17 820 grid cases is empty.
- **Prop 2.2 (det A=κ_0^{−(Q+T)}F⁴det𝒞_Aλ_A): SURVIVES (PROVED).**
  - The proof was re-derived line by line.
  - It was checked as an exact polynomial identity over GF(2)[U,Y], not only at random points, in 8 configurations.
  - The F-adic order formula of Cor 2.3(ii) was verified in 6 configurations, with k_Δ∈{0,2} and min ord_F a∈{1,2}.
  - "G5 ⟺ Δ≢0 ∧ (a_P,a_R)≢0" follows, and both degenerate directions were exhibited.
- **Cor 2.5 (𝔇_16 excluded at n=256): SURVIVES (PROVED as an assembly).**
  - The case split is exhaustive.
  - Every cited result holds on the whole strip, or at n=256 for all (r,Q,S).
  - The zero-alignment exclusion needs only identity (2.2).

The fixes are of scope and labelling only: Lemma 2.1's base point of construction, "regular" versus formal germs in Prop 4.2, an overclaim about R22 Remark 4.4, and the label of Remark 3.5. Several minor notes follow.

## §1 Item table

| item | owner label | referee finding | referee label |
|---|---|---|---|
| Lemma 2.1 (transverse layer σ, a'=σ·f^[ρ], second-order lift) | PROVED | algebra correct; the cited κ̃ (R22 §1) exists only at z(u), u good, while the statement claims every z∈Γ' with f(z)≠0 (FIX-1) | PROVED at z=z(u), u good (all that is used); general z after FIX-1 |
| Prop 2.2 (exact det A) | PROVED; COMPUTED | correct; exact polynomial identity verified (`prop22_symbolic.out`) | PROVED; COMPUTED |
| Cor 2.3(i) (G5 ⟺ Δ≢0 ∧ (a_P,a_R)≢0) | PROVED | correct; "FNAM2" should read "Δ≢0" (N3) | PROVED |
| Cor 2.3(ii) (ord_F det A=4+2k_Δ+2 min ord_F a) | PROVED | correct; verified in 6 configurations | PROVED; COMPUTED |
| Cor 2.4 (F²\|a ⇒ M'+Q−T>=2d'; impossible at n=256) | PROVED; COMPUTED | correct for all r>=4, Q>=128, S>=64 by exact algebra (threshold E>625/113); grid of 2310 (r,Q,S) has an empty failing set | PROVED |
| Cor 2.5 (𝔇_16 excluded at n=256) | PROVED (assembly) | chain verified, all scopes cover n=256 (§2.5) | PROVED (assembly, standing hypotheses) |
| Lemma 3.1 (partial Wronskian) | PROVED; COMPUTED | correct; independent exact test on positive genus (`lemma31_indep.out`) | PROVED; COMPUTED |
| Lemma 3.2 (Σ'/γ'<=5, s/γ'<=2) | PROVED; COMPUTED | correct; brute force without the popcount assumption | PROVED; COMPUTED |
| Thm 3.3 ((R1) excluded) | PROVED | correct; every case covered; numbers reproduced exactly | PROVED (inputs as listed); numbers COMPUTED |
| Remark 3.4 | PROVED comparison | correct | PROVED |
| Remark 3.5 ("Lemma 3.1 yields nothing" in (R2)) | PROVED (negative) | the observation is correct, but "yields nothing" is informal (FIX-3) | PROVED observation; the "nothing" claim is HEURISTIC |
| Prop 4.1 (FN on ℓ_u ⟺ (α)∧(4.1)) | PROVED | correct (basis argument and α_2 recomputed) | PROVED |
| Prop 4.2 (local realisability) | PROVED; COMPUTED | correct for formal germs in Ô, not "regular functions"; the toy checks (B) only along ℓ_u (FIX-2) | PROVED (formal germs) |
| Cor 4.3 (negative) | PROVED | correct in the stated germ sense; the claim that R22 Remark 4.4's HEURISTIC "becomes PROVED" overclaims (FIX-2) | PROVED (local, germ sense) |
| Remark 4.5, §5 next steps | HEURISTIC/OPEN | fine; "Bs(f) has three points" is imprecise (N7) | HEURISTIC/OPEN |
| residual list §5 | — | correct; can be sharpened to Q>=256 (N4) | — |

## §2 Detailed audit

### 2.1 Lemma 3.1, the partial Wronskian (coordinator item 1)

**Well-definedness.**
- Orders are defined greedily, so row_m lies in span_K{row_{ε_j}: ε_j<=m}. This is SV's lexicographic-minimal sequence.
- Two rules are used:
  - the Hasse chain rule, D_t^{(l)}=Σ_{k<=l}c_{l,k}D_x^{(k)} with c_{l,l}=(D_t x)^l;
  - Leibniz for h·ξ.
- Together they make the t-rows of y=hξ at the orders ε_0..ε_{s−1} equal to ΛW_s. Here Λ is lower triangular with diagonal h(D_t x)^{ε_i}. The coefficient of row_{ε_i} in D_t^{(ε_i)}(hξ) comes only from l=k=ε_i. Every other term involves x-rows of index <ε_i, which lie in the span of earlier selected rows.
- Hence w^P_J=h^s(D_t x)^{Σ_{i<s}ε_i}w_J for all J simultaneously, and v_P:=min_J ord_P w^P_J is well defined. Nothing here uses p≠2.

**(a) the degree bound.**
- deg R_s=sτ+Σ'(2g−2)+Σ_P min_J ord_P w_J, and Σ_P min_J ord_P w_J<=Σ_P ord_P w_{J_0}=0.
- The deficit is the degree of the (s−1)-st associated curve. The inequality is therefore usually strict for s<r+1, and it is an equality at s=r+1.

**(b) the weight bound.**
- Take an adapted basis with ord_P y_k=j_k(P). Then ord_P D_t^{(ε_i)}y_k>=max(0,j_k−ε_i).
- Each Leibniz term of a minor with columns k_0<…<k_{s−1} therefore has order >=Σ_l j_{k_l}−Σ_{i<s}ε_i>=Σ_{i<s}(j_i−ε_i), since k_l>=l.
- A constant change of basis multiplies (w_J) by ∧^sA, which preserves min_J ord. Correct.

**Independent test (`checks/lemma31_indep.py`, 11 s).**
- Curves: y²+y=x³ (g=1) and y²+y=x⁵ (g=2), over GF(2^8).
- Twelve linear systems in L(kP_∞). They include the non-classical sequences (0,1,2,8), (0,1,4,5), (0,1,2,4) and (0,1,2), as well as classical ones.
- Orders were computed **exactly** in the coordinate ring A, via nonzero minors.
- The affine part of deg R_s was computed **exactly over the algebraic closure**: A is Dedekind, so dim_k A/(w_J)=Σ_P min_J ord_P w_J. This equals the degree of the gcd of the 2×2 minors of the k[x]-module generated by w_J and y·w_J.
- v_∞ was computed **directly** from Laurent expansions at P_∞, independently of the lemma's change-of-frame formula. It agreed with the formula in every case.
- Results:
  - (a) holds in all 46 (V,s) cases, with equality at s=r+1 in all 12 systems.
  - (b) holds at every affine GF(2^8)-point; the exact failing sets are empty.
  - The local Hasse minors and the global minors give identical v_P, with an empty inconsistency set.
- The Thm 3.3 mechanism was tested on its own:
  - With ε=(0,1,2,8) and j(P)=(0,1,7,8), at N=7, s=3, the result is v_P(R_3)=5=γ' exactly (sharp).
  - With ε=(0,1,2) and j=(0,1,7), the result is likewise 5.
  - With N=14 and j=(0,1,2,14), the result is 10 or 12, at least γ'.
  - All other hits also satisfy the bound.
- The owner's check (P¹ only, finite part only, no v_∞) is reproduced byte for byte. My run supplies the point at infinity and positive genus.

### 2.2 Thm 3.3, (R1) closed (coordinator item 2)

**Chain re-derived.**
1. **𝔮_max>S.** R22 Thm 5.3 applies with 𝔮=𝔮_max. In case (i) (𝔡≢0) the bound is <=0.147704q. In case (ii), via R23 Cor 4.2(i), it is (𝒦) or <=0.104306q. The note cites only 0.147704 (N1).
2. **𝔮_max<=S.** So S>=𝔮_max>=128.
   - If 𝔡≡0, R23 Cor 4.2(i) gives (𝒦) or exclusion.
   - If 𝔡≢0, the good points not in 𝔅_0 lie in Z(𝔡) by R23 Prop 4.1, with at most deg 𝔡² of them.
   - So N_good<=B_{5.3(i)}+|𝔅_0|. Here B_{5.3(i)}=charges+deg 𝔡², and the charges are {λ'=0}, {det T̂=0}, 𝔈 and the boundary (⊃Bs(e)). They are all charged.
3. **u∈𝔅_0.**
   - ν_u=E−X is finite, so σ_u∈V∖0 (R19 Lemma 3.5(i)).
   - ord_uσ_u=ν_u/(ρ𝔮_max)=(2r−1)x=N_0, so N_0=j_{i_0}(u) for some i_0.
   - SV gives ε_{i_0}<=N_0, and N_0 is not an order: it has at least 3 binary ones and dim V<=4, by R23 Lemma 4.3(ii) and SV Cor 1.9. Hence ε_{i_0}<N_0, i.e. i_0<s.
   - Lemma 3.1(b), with all summands >=0 by SV, gives v_u(R_s)>=N_0−ε_{i_0}>=γ'.
   - No exceptional set is needed on 𝔅_0, because σ_u≢0 there.
4. **Count.** 𝓛=𝓣 for 𝔮_max, with τ_0=deg[T]/𝔮_max<=τ_hi (R18 §5) and 2g−2<=d²−3d. With Σ'>=0 this gives |𝔅_0|<=[sτ_hi+Σ'(d²−3d)]/γ'.
5. **Lemma 3.2.**
   - Initial segments of closed sequences are closed.
   - The four forms give Σ'<=2·max{ε<N_0}<=2(rx+1).
   - 2m/(N_0−m) is increasing in m, so Σ'/γ'<=2(rx+1)/((r−1)x−1)<=5 ⟺ 3rx−5x−7>=0, which holds for r>=4, x>=1.
   - s/γ'<=4/γ<=2.

**Coverage.**
- dim V=1 is impossible (σ_u(u)=0 against base-point-freeness), and dim V=2 is included.
- Separability at 𝔮_max gives ε_1=1.
- Brute force over all {0,1,a}, {0,1,a,b} with entries <=2^10, closed under binary sub-integers and **without** assuming popcount<=2, finds 65 sequences, exactly 1+L+C(L,2)+(L−1). All are of the three forms.
- Over r∈{2^2..2^12}, x∈{2^0..2^12} with the structural list to 2^30:
  - N_0 is never an order;
  - γ'>=γ;
  - sup Σ'/γ'=5 and sup s/γ'=2, both at r=4, x=1, ε=(0,1,4,5);
  - the exact failing set is empty.

**Numbers (`checks/numerics_indep.py`, coded from R22's text).**
- B_{5.3(i)} corner = 32480243592761/219902325555200 (reproduced).
- Whole-strip upper bound B+2τ_hi+5(d²−3d) = **91941792089517/549755813888000≈0.16724115** (identical to the owner's). Its pieces are B=0.1477030, 2τ_hi/q=6.3e−6 and 5(d²−3d)/q=0.0195318.
- On 17 820 grid cases (r<=1024, Q<=2^16, S<=2^14, 256<=n<4Q, 128<=𝔮_max<=S), using the joint per-sequence worst case:
  - the maximum is 0.167228 at (4,128,128,256,128);
  - the exact failing set against 1551/4000 is empty;
  - no case exceeds the corner bound;
  - an exact check of the monotonicity of each term along each axis finds no violation.

**Conclusion.**
- Thm 3.3 is correct. The gain over R23 Cor 4.5 is real: orders at or above N_0 add degree to R_V and no weight at 𝔅_0, and truncation removes them.
- Remark 3.4's explanation is accurate.
- The proof is conditional on the cited inputs: R23 Prop 4.1, Cor 4.2, Lemma 4.3 and Prop 4.4's order facts; R22 Thm 5.3; R19 Lemma 3.5(i); R18 §5; and SV Thm 1.5 and Cor 1.9 (CITED). All of these are audited or classical.

### 2.3 Prop 2.2 and Cor 2.3 (coordinator item 3)

**Re-derivation.**
- Squaring R18-T Lemma 2.1(ii) gives (2.1). Squaring alignment gives (2.2).
- With L_e=[J^{[T],t};e^t] and R_Q=[J^{[Q]}|f^{[Q]}], the product L_eA^tR_Q is block lower-triangular. The top-right block is λ_AJ^{[T],t}f^{[T]}=0.
- The determinants:
  - det L_e=e·(j_1×j_2)^{[T]}=κ_0^{−T}(e·f^{[T]}), since Frobenius commutes with ×;
  - det R_Q=κ_0^{−Q}(f·f)^Q;
  - det(J^tJ)=|j_1×j_2|² (Lagrange), so the top-left determinant is κ_0^{−2T}F⁴·1·det𝒞_A·κ_0^{−2Q}(f·f)^Q.
- Cancelling e·f^{[T]}≢0 and (f·f)^Q≢0 is valid because f·f=(Σf_i)² and the f_i are independent. The identity follows.
- The degree check 6M'+3 was confirmed.

**Exact verification (`checks/prop22_symbolic.py`).**
- Setting: GF(2)[U,Y], X=2, ρ=1, κ_0=1, F a smooth conic. P^t is the general solution of both identities, including a random syzygy part J^{[ρ]}w in η.
- Both input identities are themselves verified as polynomial identities.
- (I), the identity of Prop 2.2, holds in all 8 configurations.
- (III), det𝒞_A=(U·j_1)²Δ_0²+(U·j_1)(U·j_2)Δ_1²+(U·j_2)²Δ_2², holds in all 8.
- (II), ord_F det A=4+2k_Δ+2min ord_F a, holds in all 6 nondegenerate configurations: (k_Δ, min ord a) = (0,1), (2,1), (0,1), (0,2), (2,2), (0,1), with ord_F det A = 6, 10, 6, 8, 12, 6.
- Degenerate directions of Cor 2.3(i):
  - a_P=a_R=0 gives det A≡0;
  - a rank-one C pencil with a common kernel gives Δ≡0 and det A≡0 although a≠0. This confirms that both conditions are needed.
- *Script note:* the first run reported (III) as false. That was a sympy artefact: `Poly.is_zero` returned False on an unnormalised zero over GF(2) (`checks/debug_sympy_iszero.out` shows the difference printing as 0). All zero tests now go through `expand(as_expr())==0`. Identity (I) was True in both runs.
- The owner's random-point check is reproduced byte for byte. Its family P^t=FK_PJ^{[ρ],t}+f^[X]⊗η_P is the general pointwise solution: K may absorb f^[X]v^t, which is the syzygy part of η.

**Cor 2.3(ii).**
- The independence of the U-monomials over k(Γ') needs J of rank 2 at the generic point of Γ'. This holds since f|_{Γ'}≢0, because f(z(u))=g(u)u≠0.
- The additivity of ord_F uses that F is prime in k[U,Y]. Correct.
- k_Δ>=1 in (𝒦) is R18-T Prop 4.1(ii), whose proof works for every twist.

### 2.4 Cor 2.4 at n=256 (coordinator item 4)

**The degree step.**
- deg a_•=M'+Q−T, since a_•f^[X]=P^tf^[ρ].
- G5 gives some a_•≢0, which is divisible by F², so M'+Q−T>=2d'.
- Equivalence with a>=d'+3(X−ρ) was checked symbolically: the difference is 0.

**At n=256.**
- M'+Q−T<2048E/625+Q−QS<2048E/625<=4E−4<=2d' whenever E>=625/113≈5.53, while E>=2^15. So the conclusion holds for **all** r>=4, Q>=128, S>=64.
- The grid of 2310 (r,Q,S) with r<=2^12, Q<=2^20, S<=2^20 has an empty failing set.
- The constant, (𝒦) and non-(𝒦) cases do not matter here: the argument is purely degree-theoretic.

**Robustness (N8).** At n=256, F²|a forces a_P=a_R≡0 (R23 Remark 3.4). Then (2.2) alone gives A^tf^{[Q]}=0, so det A≡0, contrary to G5. Neither (2.1) nor the full Prop 2.2 is needed.

### 2.5 Cor 2.5, 𝔇_16 at n=256: the chain and the scope of each link

| case | result used | scope check |
|---|---|---|
| constant twist, not (𝒦) | R22 Cor 4.1 | all D, whole strip (monotone corner 0.046095) ✓ |
| constant twist, (𝒦), F²∤a | R23 Thm 3.1 (any twist, any D; or R22 Cor 4.2) | whole strip (corner 0.0925781) ✓ |
| constant twist, (𝒦), F²\|a | Cor 2.4 + Cor 2.3(i)/(2.2) + G5; also R20 Cor 3.2 (redundant) | n=256, all r,Q,S by exact algebra ✓ |
| non-constant, not (𝒦) ((R1)) | Thm 3.3 (with R22 Thm 5.3, R23 Prop 4.1, Cor 4.2, Lemma 4.3, Prop 4.4, R19 Lemma 3.5(i), SV) | whole strip, every 𝔮_max>=128 ✓ |
| non-constant, (𝒦), F²∤a | R23 Thm 3.1 | whole strip ✓ |
| non-constant, (𝒦), F²\|a ((R2) residual) | Cor 2.4 + G5 | n=256, all r,Q,S ✓ |

- The split constant/non-constant × (𝒦)/not × F²|a_P∧F²|a_R or not is exhaustive.
- Every link covers n=256 for all r>=4, Q>=128, S>=64.
- None of the links is a grid-only result. In particular R23 Cor 3.3's grid computation is **not** needed.
- So Cor 2.5 also upgrades R23's grid-COMPUTED closure of non-constant (𝒦) at n=256, r∈{4,8}, to the whole strip (N9).
- The statement holds under the standing hypotheses of 𝔇_16: global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮_max>=128, and all original gates. The note says so in §1 and in the dependencies paragraph. The §0 "Newly closed" line should carry the qualifier (N2).

### 2.6 Lemma 2.1 and Props 4.1–4.3 (coordinator item 5)

**Lemma 2.1.**
- The algebra is correct:
  - the J-part, using that J^{[X],t}(z) is onto when f(z)≠0;
  - the kernel O·f^[X], since f^[X] is unimodular;
  - a_P=Fσ_P·f^[ρ];
  - the gauge, the syzygy lifting via e' with e'·f^[ρ]=1, and both directions of the second-order lift.
- Gap (FIX-1): the proof takes κ̃_P from R22 §1 and P^t≡f^[X]⊗κ̃_P mod F from R22 Lemma 2.4(i). Both are established only at z(u) for good u (R16.2's local first layer, λ^Y regular).
- The statement claims every z∈Γ' with f(z)≠0. That includes singular points of Γ' and points over {λ'=0} or {det T̂=0}.
- The repair is easy. At such z, common image and f(z)≠0 give P^t|_{Γ'}=f^[X]⊗κ with κ=(row i of P^t)/f_i^X regular, for some i with f_i(z)≠0. Zero top gives κ·f^[ρ]∈FO. Correct κ by the syzygy-lifting step of (iii).
- Only z=z(u) is used in §4, so nothing downstream is affected.

**Prop 4.1.**
- The basis u^[X], f^[X], e_3 is valid.
- J^{[X],t}W_u is computed correctly, so (α)⟺α_3=0.
- α_2 was recomputed: W_u=f^[X](κ̃_c·u^[ρ])+F[κ_0^{−X}(t/g)^ργ_C(ω^[X]+ζf^[X])+f^[X](σ_c·u^[ρ])], with ω^[X]=t^{−X}(g^Xu^[X]+f^[X]) and g^ρκ̃_c·u^[ρ]=t^ρs̃_u. This gives (4.1).
- Also a'_c=g^ρσ_c·u^[ρ]+t^ρσ_c·ω^[ρ]. Correct.

**Prop 4.2.**
- The construction is correct:
  - the 2×2 unit minor of the rows u^[ρ], ω^[ρ];
  - A·f^[ρ](t,0)=φ_u+φ_u=0;
  - β=−(A·Φ)/(γ(v·Φ)) is regular because A·Φ∈γk[[x]];
  - t^{−ρ}φ_u is regular, by ord γ_C>=e_u>X and ord s̃_u>=e_u.
- However, σ is a **formal** germ (A∈k[[t]]³, σ∈k[[x]][y]), not a germ of regular functions (FIX-2).
- The owner's toy checks σ·f^[ρ]=0 only along ℓ_u. It does not check the off-line extension that gives (B) on Γ' (N5).

**Cor 4.3.**
- It is correct in the germ sense it states.
- The sentence "R22's Remark 4.4 'HEURISTIC non-determination' becomes PROVED in this local sense" overclaims (FIX-2). R22's heuristic concerns fixed global (C, a, first layer), with only polynomial syzygy freedom ξ∈Syz(f^[ρ]). Prop 4.2 lets the local σ, and with it the local a, vary freely in Ô.
- The local fact that is proved is this: for fixed a'_c, FN on one line is exactly a'_c≡φ_u mod t^ρ.

**Pitfalls checked.**
- Γ'⊃Bs(f): Lemma 2.1 and §4 require f(z)≠0, and Prop 2.2 is global. ✓
- Bs(e)∩Γ̃: charged in the boundary inside B_{5.3(i)}. ✓
- Singular branches: Prop 4.2 uses smoothness of Γ' at z(u) (R23 §1 N2), and Thm 3.3 works with places of Γ̃. ✓
- 𝒞 formed with z, and Z(λ') charged (Nd, in B_{5.3(i)}). ✓ The new name 𝒞_A collides with 𝒞_c=C_c(z) (N6).
- 𝔮_max conventions: V, N_0, x and τ_hi use 𝔮_max, and the charges use 𝔮>=128. ✓

### 2.7 Owner scripts (copied to `checks/owner_copy/`, run with `python3 -I`)

| script | rerun | byte-identical | remarks |
|---|---|---|---|
| numerics_R24.py | 0.2 s | yes | Part A says "entries <=2^14" but includes (0,1,2^14,2^14+1), so 120 instead of 119 (harmless, N10). Part C ignores n<4Q (N4) |
| det_identity_check.py | 43 s (note says 13 s) | yes | the family is the general pointwise solution |
| partial_wronskian_check.py | 53 s | yes | P¹ only; finite part only (v_∞ not computed) |
| local_realization_toy.py | 17 s | yes | one line only; (B) off the line not tested |

## §3 Fixes (substantive first; none changes a closure or a headline number)

- **FIX-1 (Lemma 2.1, scope of the construction).** Either restrict the statement to z=z(u), u good, which is all §4 uses, or replace the citation of R22 §1 / Lemma 2.4(i) by the general construction:
  - κ:=(row i of P^t)/f_i^X on Γ' near z, for some i with f_i(z)≠0;
  - zero top gives κ·f^[ρ]∈FO;
  - correct κ to an exact syzygy by the lifting step of (iii).
- **FIX-2 (Prop 4.2 / Cor 4.3 wording).**
  - Replace "matrix germ … of regular functions" by "formal matrix germ (entries in Ô_{P²,z(u)})". Optionally add that any finite jet is realised by polynomials.
  - Delete or qualify "R22's Remark 4.4 'HEURISTIC non-determination' becomes PROVED in this local sense". R22's statement, for fixed global (C,a) with polynomial-syzygy freedom only, remains HEURISTIC.
  - Proved is the local version: with σ free in Ô and a'_c fixed, FN on one line is exactly a'_c≡φ_u (mod t^ρ).
- **FIX-3 (Remark 3.5 label).** Keep as PROVED the observation that, if some ε_i>=N_1, "ord_uσ_u>=N_1" holds at every non-Weierstrass point. Relabel "Lemma 3.1 yields nothing for (R2)" as HEURISTIC: Lemma 3.1 does not apply in the way Thm 3.3 uses it.

## §4 Minor notes

- **N1.** Thm 3.3, case 𝔮_max>S: cite R22 Thm 5.3(i) and (ii) with R23 Cor 4.2(i). The bound is max(0.147704, 0.104306)q, or (𝒦).
- **N2.** In §0 "Newly closed" and in the title, add "under the standing hypotheses of 𝔇_16 (global alignment, Q>=128, 𝔮_max>=128, …)". §1 and the final paragraph already say this.
- **N3.** Cor 2.3(i): "G5 ⟺ FNAM2 ∧ …" should read "G5 ⟺ Δ≢0 ∧ (a_P,a_R)≢0 (given (2.1), (2.2))". FNAM2 is the name of an implication.
- **N4.** Cor 2.4 and §5: since n<4Q in the strip, n>=512 forces Q>=256. The residual (𝒦)∧F²|a therefore lives only at Q>=256 (and D>=256 with D<Q gives Q>=512 on the D-lanes). Part C's "least feasible n=512 on all 280 (r,Q,S)" ignores this, though harmlessly.
- **N5.** `local_realization_toy.py` does not test the off-line extension σ=A+yβv, i.e. (B) on Γ'. The hand proof is correct.
- **N6.** The symbol 𝒞_A clashes with the (𝒦)-notation 𝒞_c=C_c(z) of R20 and R23. Suggest C_A^hom or 𝒞^A. In Lemma 3.1 the letter r means dim V−1, which clashes with the strip r. Suggest r_V.
- **N7.** Next step 1: "Bs(f) has three points" should read "at most three proper base points" (infinitely near base points are possible).
- **N8.** The zero-alignment exclusion (R23 Remark 3.4's OPEN question) needs only (2.2): A^tf^{[Q]}=0. Worth stating, since it makes Cor 2.5 independent of the F⁴ bookkeeping.
- **N9.** Cor 2.5 also makes R23 Cor 3.3's grid-only n=256 closure of non-constant (𝒦) for r∈{4,8} a whole-strip PROVED statement. This could be recorded.
- **N10.** numerics_R24 Part A header and count (120 rather than 119), and the timing figure for det_identity_check.
- **N11.** Lemma 3.1 is classical in substance: the ramification divisor of the (s−1)-st associated or osculating map. Its deficit from equality is the degree of that associated curve. The proof given is complete. The "standard in spirit" remark is fair.

## §5 Files in `checks/` (checksums in `checks/checks_SHA256SUMS.txt`)

| file | content | result |
|---|---|---|
| `owner_copy/*` (+ `*.rerun.out`) | owner scripts and outputs, rerun | 4/4 byte-identical |
| `lemma31_indep.py` → `.out` (11 s) | Lemma 3.1 on y²+y=x³, x⁵; exact deg R_s over k̄ (module colength + direct Laurent v_∞); (b) at all affine GF(2^8)-points; Thm 3.3 mechanism | all 12 systems pass; exact failing sets empty; equality at s=r+1 |
| `numerics_indep.py` → `.out` (8 s) | Lemma 3.2 brute force (no popcount assumption); Thm 3.3 corner and 17 820-case grid; monotonicity; Cor 2.4 for 2310 (r,Q,S); symbolic equivalence | all reproduced; failing sets empty |
| `prop22_symbolic.py` → `.out` (43 s) | Prop 2.2 and Cor 2.3 as exact polynomial identities over GF(2)[U,Y] | 8/8 configurations pass |
| `debug_sympy_iszero.py` → `.out` | documents the sympy `Poly.is_zero` artefact behind the first (III) run | — |
| `src_SHA256SUMS.txt` | pre-supplied; 31/31 src files verified | OK |
