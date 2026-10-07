# Revision check: HYP M>=2 round 22, owner v2

7 October 2026. This is an independent revision check of `src/HYP_M2_ROUND22_owner_v2.md` (sha256 `0b031fc0…c9c3`). It is checked against `src/inputs/R22_v1.md` and `src/inputs/AUDIT_HYP_M2_ROUND22_20261007.md` (FIX-1..8, N1–N8).

**Rules kept.**
- I read only under `src/` and wrote only under `checks/` and to this file.
- I opened no file whose name contains "DZ".
- `src/` matches the pre-supplied `checks/src_SHA256SUMS.txt` (all OK).
- I copied the owner scripts to `checks/owner_copy/` and ran them with `python3 -I`, one at a time. All four outputs are byte-identical:

  | script | time |
  |---|---|
  | numerics | 0.18 s |
  | toy v2 | 2.6 s |
  | toy v1 | 2.6 s |
  | contact | 15.4 s |

- Below its header, `toy_vector_FN_v2.py` is identical to `toy_vector_FN.py`, as the note claims.
- My own checks use `fractions` and `galois` and do not use the owner's `gf2k`. Each ran under `python3 -I` in under 10 s.

---

## §0 Verdict: **PASS-with-fixes** (text-only fixes; no mathematical error)

- All 8 FIX items are addressed.
- 7 of the 8 minor notes are addressed. N5 was optional and is declared as not applied.
- I found no mathematical error in v2. The headline results, labels and closures are unchanged, apart from the FIX-6 round-ups (each confirmed to be at least the exact value) and the FIX-7 record.
- **The new claim "(R1) with dim V=2 is closed" stands.** I re-proved it in full (§2.1). One precision fix is needed: "𝔮" in the pencil statements must mean the *maximal* 𝔮 (RC-1).
- The other new or rewritten proofs also check out, by hand and exactly over GF(2^8):
  - the local proof of F|a (FIX-5);
  - the J-part consistency (FIX-1);
  - the modification η=Fξ in Prop. 4.3 (FIX-2);
  - the corrected dot products after Prop. 2.3 (FIX-3).
- RC-1..RC-4 are wording, precision and rounding issues. None of them changes a label or a closure.

---

## §1 Fix-by-fix table

Line numbers refer to v2.

| item | status | location in v2 | comment |
|---|---|---|---|
| FIX-1 (Remark 4.4 overclaim) | **ADDRESSED** | l. 282–290; table l. 429 | Split into a PROVED decomposition, with the J-part proof added, and a HEURISTIC non-determination. The tautology is noted. Proof verified (§2.3). Small imprecisions: RC-2 |
| FIX-2 (Prop. 4.3 justification) | **ADDRESSED** | l. 70, 272–275, 279; table l. 428 | Uses η=Fξ. "Not implied by C̃" and "converse not shown" are correctly scoped. The wrong v1 sentence is retracted. Verified (§2.4) |
| FIX-3 (false remark after Prop. 2.3) | **ADDRESSED** | l. 163; table l. 422 | ·u^[X]≡0 and ·ω^[X]=t^ρF b^{[X],t}C_cb^[ρ]. Re-verified exactly (`rc_algebra`, 12/12 each) |
| FIX-4 (Cor. 3.2 novelty) | **ADDRESSED** | §0 item 4 (l. 65), l. 226; table l. 425 | Matches the audit, including the 𝔮<=S and 𝔮>S arithmetic, which I re-derived |
| FIX-5 (citation inside a CONDITIONAL proposition) | **ADDRESSED** | l. 20, 40, 173, 179, 185; table l. 423–424 | The local proof is correct and unconditional (§2.2) |
| FIX-6 (round-ups) | **ADDRESSED** | l. 75, 78, 86, 334, 336, 361, 362, 408, 434 | Each round-up is >= the exact value (§3). Cosmetic residue: RC-3(b,c) |
| FIX-7 (§6 consistency, Prop. 5.5 pencil) | **ADDRESSED** | l. 79, 90, 97, 390, 391; table l. 436, 438 | The closure is verified (§2.1). Needs the "𝔮 maximal" qualifier (RC-1), and l. 90 lacks "dim V>=3" (RC-4) |
| FIX-8 (toy wording and coverage) | **ADDRESSED** | l. 83–84, 406, 412; `toy_vector_FN_v2.py` header | Headers corrected; the code is unchanged and the output byte-identical |
| N1 (Lemma 2.2: affine lift, shorter proof) | **ADDRESSED** | l. 138, 147 | |
| N2 (exact form (†)) | **ADDRESSED** | l. 215 | |
| N3 (Thm 3.1(iv) "exact congruence") | **ADDRESSED** | l. 190 | |
| N4 (§0 item 3 wording) | **ADDRESSED** | l. 64 | |
| N5 (m'_u>=X−ρ margin in Lemma 5.2) | **NOT ADDRESSED** (optional; declared at l. 440, "N1–N4, N6–N8") | — | Acceptable; the audit said "not needed" |
| N6 (Cor. 5.4 thresholds) | **ADDRESSED** | l. 350–351, 435 | The printed decimals round a *threshold* upward (RC-3(a)) |
| N7 (FNAM1 in the dependencies of Prop. 2.3) | **ADDRESSED** | l. 149 | |
| N8 (`scripts/` vs `owner_scripts/`) | **ADDRESSED** | l. 410 | |

---

## §2 New claims in v2

### 2.1 FIX-7: the Prop. 5.5 pencil case is unconditional in (R1) and (R2), and "(R1) with dim V=2 is closed"

I re-proved this in full.

**Definition.** (R1) consists of the non-constant twists outside (𝒦) (R18-T §5, R19 §6). Fix such a model with dim V=2, where V=span(t̂_ij).

**Step 1. Choose 𝔮 maximal.**
- 𝔮_max exists and is finite, because a non-constant [T] is not a 2^k-th power for every k.
- Thm 5.3 is stated for any admissible 𝔮, and its proof (Lemma 5.1(a)) only needs 𝔮, S to be powers of 2 with 𝔮>S, i.e. 𝔮>=2S. So it applies with 𝔮=𝔮_max.
- Prop. 5.5 explicitly needs 𝔮=𝔮_max: separability comes from maximality.

**Step 2. Case 𝔮_max>S.** Thm 5.3(i) and (ii) exclude the model, since it lies outside (𝒦). The bounds are <=0.147704q and <=0.104306q. I re-derived Lemma 5.1(a): the least multiple of ρ𝔮 (a multiple of 2X) that is >=(2r−1)X is >=2rX=E.

**Step 3. Case 𝔮_max<=S.** Then 𝔮_max<(2r−1)S, since r>=4, and N_0=⌈(2r−1)S/𝔮_max⌉>=2r−1>=7>=2. The pencil argument goes through:
- **σ_u∈V.** By R19 Lemma 3.5(i), σ_u∈V, and σ_u≢0 off <=2deg ψ good points.
- **Order at each good point.** Cor. 3.2 holds for every twist; it uses only Thm 3.1(i), which assumes no (𝒦) or constancy. It gives ord_uσ_u>=N_0.
- **Separability.** The t̂_ij have no common zero, so V is base-point free and j_0(u)=0. A section of a 2-dimensional V vanishing to order >=N_0 forces j_1(u)>=N_0. If s_1/s_0∈K², then every t̂_ij/t̂_kl∈K², because these are constant-coefficient Möbius images over the perfect field k. So T would be a 2𝔮-th power, which contradicts maximality. Hence [V]: Γ̃→P¹ is separable and ε=(0,1).
- **Ramification count.** Riemann–Hurwitz (Stöhr–Voloch for r_V=1, CITED) gives v_u(R)>=j_1(u)−1>=N_0−1>=1 at each such good u, wild ramification included. Also deg R=2g−2+2τ_0.
- **The bound.** Hence N_good<=charges+2deg ψ+(2g−2+2τ_0), which is <=0.049195q on the whole strip (§3). The model is excluded.

Steps 2 and 3 cover every 𝔮_max, so (R1)∩{dim V=2} is closed. **PROVED.**
- The same argument with Step 3 alone excludes (R2)∩{dim V=2, 𝔮_max<(2r−1)S}.
- The open remainder recorded in the table (l. 438), "(R1) on 𝔅_0, 𝔮<=S, dim V>=3; (R2) with dim V>=3 or 𝔮>=(2r−1)S", is consistent with this.

**Caveat (RC-1).** The statements at l. 79, 97, 391 and 436 say "𝔮<(2r−1)S" without "maximal". The notation rule at l. 39 says "All statements about 𝔮 hold for any admissible 𝔮; a larger 𝔮 only strengthens them". That rule is false for Prop. 5.5's hypothesis, because a larger 𝔮 makes N_0 smaller. For a non-maximal admissible 𝔮'<(2r−1)S with 𝔮_max>=(2r−1)S, the (R2) statement as literally read is not proved.
- The (R1) closure is unaffected, since it is a dichotomy on 𝔮_max.
- Fix: write 𝔮_max (or "𝔮 maximal") in those lines, and add an exception to the l. 39 convention for Prop. 5.5.

*Novelty.* By FIX-4 (l. 226), the pencil case was already derivable from R16.2 and R19 Lemma 3.5. The (R1) closure also uses Thm 5.3, which is genuinely new. So recording it as newly closed is fair.

### 2.2 FIX-5: the local proof of F|a_P (Lemma 2.4(iv))

Correct and unconditional.
- **First layer.** On a dense open set of Γ' (off Bs(f), where e^{-1} is defined), common image gives P^t=f^[X]⊗κ_P with κ_P rational. This is the local first layer of §1, which needs no global lift (unlike R18-T Step 1, which used (H_bs)).
- **Zero top.** Then a_Pf^[X]=P^tf^[ρ]=f^[X](κ_P·f^[ρ]). Also κ_P·f^[ρ] is a unit multiple of ϰ_P·U^[ρ], which is 0 by zero top (a standing hypothesis), since f^[ρ]=g^ρU^[ρ] on Γ'.
- **Divisibility.** Γ' is irreducible and reduced, so a_Pf_i^X≡0 mod F for all i. Some f_i∤F: deg f_i=2<d', and f≢0 on Γ' since f(e(u))=g(u)u. F is prime, so F|a_P.
- **Scope.** This is exactly the first bullet of R18-T Step 3 with the (H_bs)-dependent global κ replaced by a local one. The CONDITIONAL dependency is gone. Thm 3.1's dependency line is updated accordingly (l. 185, 424).

### 2.3 FIX-1: the J-part consistency (Remark 4.4)

Correct. I re-derived it by hand, for a constant twist (s̃_u=0).
- **(γ) is solvable iff (α) and (β) hold.** Write R:=t^{−ρ−X}J^[X]m.
  - ω(0)=w=df_z(V)≠0, so ω^[X] is unimodular, and the image of [ω^[X]]_× on k[[t]]³ is exactly (ω^[X])^⊥.
  - R·ω^[X]=t^{−ρ−X}(J^tω)^[X]·m=t^{−X}b^{[X],t}C_cb^[ρ], using b^{[X],t}Ωb^[X]=2b_1^Xb_2^X=0. So R⊥ω^[X] ⟺ (α).
  - J^[X] has a unit 2×2 minor, so R is regular ⟺ m∈t^{ρ+X}k[[t]]² ⟺ (β).
- **The J-part is automatically consistent.**
  - Use u^[X]×ω^[X]=g^{−X}f^[X]×ω^[X]=g^{−X}κ_0^XJ^[X]Ωb^[X].
  - Dotting (γ) with u^[X] gives κ_0^X b^{[X],t}ΩJ^{[X],t}y=b^{[X],t}C_cb^[ρ] (after cancelling g^{−X}). This is implied by J^{[X],t}y_u=κ_0^{−X}ΩC_cb^[ρ].
  - The kernel of b^{[X],t}Ω=(b_2^X,b_1^X) is span(b^[X]), with b constant and nonzero. So the solution family y_0+φω^[X] meets the prescribed J-part with φ regular.
  - What remains is one scalar condition per order on the f^[X]-component.
- **Exact check.** `rc_algebra.out`, 12 random lines over GF(2^8) with (ρ,X)∈{(1,4),(2,4),(2,8),(4,8),(4,16)}, checks the following, each 12/12:
  - "FIX1 u-component of (gamma) automatic", for random y and a';
  - both dot forms;
  - b^tΩb=0.
- **Precision points (RC-2), not affecting the label.**
  - (a) J^{[X],t}y_u=κ_0^{−X}ΩC_cb^[ρ] is credited to "Lemma 2.1(iii)". It also needs [f^[X]]_×=κ_0^XJ^[X]ΩJ^{[X],t} (Lemma 2.1(ii)/R18-T 2.1(i), verified as "CROSS" 12/12), injectivity of J^[X], and J^{[X],t}f^[X]=0.
  - (b) "dotting t^X·(γ)": the factor t^X is spurious.
  - (c) In the HEURISTIC bullet, "with (C, a, first layer) fixed, the only freedom is … F|ξ·f^[ρ]" is not right. With a fixed exactly, R18-T Prop. 2.4's closing Remark gives η∈Syz(f^[ρ]), and η=Fξ with F prime gives ξ·f^[ρ]=0, i.e. ξ=J^[ρ]η' and y_u↦y_u+f^[X](η'·b^[ρ]). F|ξ·f^[ρ] is the freedom that keeps (C, first layer, F²|a), not a. The family is even more restricted, so the HEURISTIC label stands.

### 2.4 FIX-2: Prop. 4.3 with η=Fξ

Correct.
- P^t↦P^t+F f^[X]⊗ξ adds F f^[X](ξ·f^[ρ]) to P^tf^[ρ]. So a↦a+F(ξ·f^[ρ]), i.e. a'↦a'+ξ·f^[ρ].
- [f^[X]]_×(f^[X]⊗ξ)=0, so H and C are unchanged.
- The added term is ≡0 mod F, so the first layer, common image and zero top are kept.
- One can take ξ with F∤ξ·f^[ρ], e.g. ξ=e_i·(monomial) with f_i^ρ∤F. In the setting of Prop. 4.3, a>=d' gives M'>=2d'−X+ρ, so deg ξ=M'−2X−d'>=d'−3X+ρ>0. Hence F²|a can be destroyed without changing C̃.
- The exact check is `rc_algebra` "FIX2 …", three identities, each 12/12.
- "Converse not shown: would need a'∈(F)+I_ρ" is correctly scoped to this modification.
- Minor point, inherited from v1 and covered by Remark 4.6's HEURISTIC on G5: "not implied by C̃" means "not implied via the global identities". The modified P need not satisfy every original gate.

### 2.5 Other new text

- **FIX-3 (l. 163).** Correct (§1).
- **FIX-4 (l. 226).** Correct. I re-derived it: with ν_u>=E−X−ρ and ν_u∈ρ𝔮Z, one gets E−X for 𝔮<=S, and E for 𝔮>S because 2(r−1)X<(2r−1)X−ρ.
- **N1 remark, N2 exact form.** These are accurate transcriptions of the audit.
- **No new overclaims elsewhere.** The exception is RC-1, which concerns the scope of a new statement.

---

## §3 Numbers (FIX-6) and headline invariance

`checks/rc_numerics.py` is an independent exact-Fraction evaluation of the printed formulas. Corner (r,Q,S,n)=(4,128,64,256):

| count | exact (= owner fraction) | decimal | v2 printed | v2 >= exact | v1 printed | v1 >= exact |
|---|---|---|---|---|---|---|
| Cor. 4.1 | 33259609702489/721554505728000 | 0.0460943829 | 0.046095 | yes | 0.046095 | yes |
| Cor. 4.2 | 3194487655227/34359738368000 | 0.0929718271 | 0.092972 | yes | 0.092972 | yes |
| Thm 5.3(i) | 32480243592761/219902325555200 | 0.1477030473 | **0.147704** | **yes** | 0.147703 | no |
| Thm 5.3(ii) | 114684856407837/1099511627776000 | 0.1043052693 | **0.104306** | **yes** | 0.104305 | no |
| Prop. 5.5 classical | 75571916082327/1099511627776000 | 0.0687322573 | **0.068733** | **yes** | 0.068732 | no |
| Prop. 5.5 pencil | 27044774933549/549755813888000 | 0.0491941590 | **0.049195** | **yes** | 0.049194 | no |

**Grid check.**
- Grid: r∈{4,…,128}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^13}, dyadic n∈[256,4Q), 1728 rows.
- Every maximum is at the corner and below 1551/4000.
- Monotonicity under doubling: 39 480 comparisons, 0 violations.
- The classical dim-3 sub-case is also computed (0.0511458) and lies below the dim-4 value used.

**Headline invariance (diff v1→v2).**
- Every changed line carries a "[v2: …]" tag, apart from the title, the version block and the "v1/v2" status words.
- No headline statement, label or closure changed, except the FIX-7 *record* of the pencil closures, which v1's Prop. 5.5 (pencil, "unconditional") plus Thm 5.3 already implied.
- Labels agree across §0, the body and §8 for every item. The only wording gaps are in RC-1 and RC-4.

---

## §4 RC items

- **RC-1 (precision of a new claim; FIX-7).** In l. 79, 97, 391, 436 and 438, "𝔮<(2r−1)S" must refer to the **maximal** 𝔮 (Prop. 5.5 l. 359 already takes it). Also qualify the l. 39 convention, "a larger 𝔮 only strengthens them", which is false for Prop. 5.5's hypothesis. In §6 (R1), say that the dichotomy 𝔮>S / 𝔮<=S is applied to 𝔮_max (Thm 5.3 allows any admissible 𝔮). The closure of (R1) with dim V=2 is unaffected (§2.1).
- **RC-2 (Remark 4.4 precision; FIX-1).**
  - (a) Cite Lemma 2.1(ii) and (iii), injectivity of J^[X] and J^{[X],t}f^[X]=0 for J^{[X],t}y_u=κ_0^{−X}ΩC_cb^[ρ].
  - (b) Drop the spurious "t^X·" in "dotting t^X·(γ)".
  - (c) With a fixed, the residual freedom is ξ∈Syz(f^[ρ]), not F|ξ·f^[ρ]. The latter keeps F²|a, not a. Then y_u shifts by f^[X](η'·b^[ρ]) with ξ=J^[ρ]η'.
  - The labels stay as they are.
- **RC-3 (rounding, cosmetic).**
  - (a) The Cor. 5.4 thresholds are printed as 0.240047q and 0.283445q (l. 350–351, 435). The exact values are 0.2400469527q and 0.2834447307q. In "excluded unless |𝔅_0|>θq", θ must be rounded *down* (0.240046, 0.283444) or kept in the exact form (1551/4000−0.14770305), which is safe. The l. 75, 390 and 392 values 0.24q and 0.283q are safe.
  - (b) l. 86 lists 0.046094 (a truncation below the exact 0.0460943829) under the tag "[FIX-6: rounded up]". Use 0.046095.
  - (c) The Thm 5.3 proof (l. 347) still prints "≈0.147703 / ≈0.104305". This is harmless as "≈", but could match the statement or give 8 digits.
  - (d) The version block (l. 8) says "The only numbers changed are the FIX-6 round-ups", but N6 also changed the printed Cor. 5.4 thresholds.
- **RC-4 (consistency wording).**
  - (a) l. 8 "No closure changes" and l. 92 "no closure changed" sit next to the new FIX-7 closure item. Say "no closure withdrawn; FIX-7 records closures already implied by v1's Prop. 5.5 pencil case and Thm 5.3".
  - (b) l. 90 "(R1) with 𝔮<=S is open on 𝔅_0" needs "with dim V>=3", as §6 and l. 438 now say.
  - (c) l. 89 "y … which (C,a) do not determine (Remarks 4.4, 4.5)" is true for the vector y_u: the Syz-freedom of RC-2(c) changes it. But Remark 4.4 now labels the relevant non-determination HEURISTIC. Reword to keep the two apart.

---

## §5 Files in `checks/`

| file | content | result |
|---|---|---|
| `src_SHA256SUMS.txt` | pre-supplied hashes of `src/` | all OK |
| `owner_copy/` (+ `rerun/`, `rerun/rerun_log.txt`) | copies of the owner scripts; reruns with `python3 -I` | numerics, toy v1, toy v2, contact: **byte-identical**. v2 toy code = v1 below the header |
| `rc_numerics.py` → `.out` | independent exact Fractions: corner values, FIX-6 round-ups vs exact, v1 values, Cor. 5.4 thresholds, 1728-row grid, monotonicity | §3: all round-ups >= exact; RC-3(a,b) found |
| `rc_algebra.py` → `.out` | exact GF(2^8) (galois) on 12 random own lines: Lemma 2.1(i),(ii), the CROSS identity, the FIX-1 J-part consistency, the FIX-3 dot products, the FIX-2 modification | 228 checks, 0 failures |
| `checks_SHA256SUMS.txt` | hashes of the files above | — |
