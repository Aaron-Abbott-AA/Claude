# HYP M>=2, round 21 (owner v2): constant twists with D∈{1,2} reduce to two explicit families; the own-point defect outside (𝒦)

7 October 2026. Claude HYP(2) owner research note (R21), following R20 v2.1 (final, A306 kit).

**Version history.**
- v1: owner draft.
- v1 independently audited (`AUDIT_HYP_M2_ROUND21_20261007.md`): **PASS-with-fixes**.
  - Prop. 2.1 and Cor. 2.2 survive in full. Prop. 2.1 was independently confirmed in original coordinates with Frobenius-twisted constants over GF(2^4) and GF(2^8). The Cor. 2.2 numbers were reproduced exactly.
  - Main fix: Prop. 2.3/Cor. 2.4/summary item 3 overclaimed (FIX-1).
  - Further fixes FIX-2..6 and minor notes N1–N12.
- **v2 (this file)** applies FIX-1..6 and N1–N12, marked "[v2: FIX-n]" / "[v2: Nn]".
  - The only number changed is the one the audit asked for: deg 𝔡²/q <0.1103q (FIX-4).
  - [v2: N6] The own-point defect vector, called κ(u) in v1, is renamed 𝔡(u). This avoids a clash with the scalar κ_u (c^[Q]=κ_uB(u)c) and with R19's count κ(u).
  - Script headers are corrected in new copies `*_v2.py`. The originals are kept, and all v2 outputs are byte-identical to v1's.

**Targets, as set by the coordinator:**
- (a) constant T in (𝒦) with a>=d' (n>=512), especially D∈{1,2};
- (b) (R1), studied through the defect k_c=𝒞_cBc at residual points;
- (c) precise negative results where (a) or (b) stalls.

**Inputs (read, not re-proved; copies in `inputs/`):**
- R20 v2.1 (`HYP_M2_ROUND20_owner_v2_1.md`, audited, revision-checked). Used: Prop. 3.1, Lemma 4.1, Lemma 4.2, (1.1), (6.1).
- R19 v2.1 (`R19_CORRESPONDENCE_ROUTE_v2_1.md`). Used: Lemma 3.1, R14.1 usage, Prop. 1.1.
- R18-T v2.1 (`R18T_TWIST_NOTE_v2_1.md`). Used: Lemma 1.1, Lemma 1.2, Lemma 3.1, Prop. 4.1(ii), §6 residual list.
- PRIMARY FNAO (§2 slope set, §3 count), FNAP (§2 iteration, (1)–(2), §4), FNAM (FNAM2, FNAM3), FNAN, as reviewed (PASS / PASS-with-fixes). [v2: N9] The FNAO/FNAP files still carry "independent review PENDING" headers. Their acceptance is recorded in the PRIMARY 13:01 message and in R18-T §1 (Claude review PASS-with-fixes). All PRIMARY results remain PRIMARY's. In particular, the count used in Cor. 2.2 is PRIMARY's FNAO §3 / FNAP (2), unchanged.

**Labels (as in R18-T/R19/R20):**
- PROVED: complete proof here, conditional only on the named inputs.
- CONDITIONAL.
- COMPUTED: exact computation; it proves only where an exact bound is evaluated.
- HEURISTIC / OPEN / CITED.

**Rules followed.**
- No file whose name contains "DZ" was opened. (FNAO/FNAP mention "DZ" only in their credit lines.)
- No PRIMARY/Codex script was executed.
- Own scripts were run with `python3 -I`, one at a time, each < 10 s.

**Notation** is that of R18-T/R19/R20.
- "Constant twist" means [T] constant, i.e. T=λT_0 with T_0∈GL_2(k). Then B=λ^ρB_0 with B_0∈GL_2(k). By R18-T Lemma 1.1 this is exactly FNAO's CMIX with constant A. Below, B denotes B_0.
- FNAP §2 is used throughout:
  - T=QS, S=Q^jD, D=2^t<Q;
  - K=B_{j+1}^[D]; z:=Bc; L:=K(B^{−1})^[D]∈GL_2(k);
  - C̃(z):=L^t·C_{B^{−1}z}(Y), linear in z, 2×2, entries forms of degree a in Y;
  - the reduced slope polynomial P_D(c,Y)=(Kc^[D])^tC_c(Y)(Bc)=z^{[D],t}C̃(z)z.
- Further notation: Ω=[[0,1],[1,0]], z^⊥=(z_2,z_1)=Ωz, J(z):=[[0,z_2],[z_1,0]], z^{⊥[2]}=(z_2²,z_1²).

---

## 0. Summary

**PROVED.**
1. **Classification of P_D≡0 (Prop. 2.1).** For a constant twist, P_D(c,Y)≡0 holds exactly in the following cases:
   - D=1: C̃(z)=h(z,Y)·Ω+μ(Y)⊗z^⊥, with h linear in z and μ∈k[Y]_a²;
   - D=2: C̃(z)=h'(Y)·J(z)+μ(Y)⊗z^⊥;
   - D>=4: C̃(z)=μ⊗z^⊥ (rank one, excluded by FNAM2; this case is FNAP's).

   The parametrisation is unique. FNAM2 holds iff h≢0 and h≢μ_1z_1+μ_2z_2 (D=1), resp. h'≢0 (D=2).
2. **Reduction of the constant D∈{1,2} lanes (Cor. 2.2).** For a constant twist with D∈{1,2}, inside or outside (𝒦), at every strip scale:
   - if C̃ is **not** in the family of Prop. 2.1, then P_D≢0, and PRIMARY's FNAO/FNAP count (unchanged) excludes the model;
   - the bound/q is <=0.0473 (COMPUTED exactly over 1260 parameter rows). [v2: FIX-2] Each term of bound/q is non-increasing in r, Q, S and n, so the supremum over the whole strip is the corner value at (4,128,64,256). "At every strip scale" is therefore PROVED, not only computed on the grid.

   So the constant-twist parts of (R2) and (R3) with D∈{1,2} reduce to the two explicit families 𝔉_1, 𝔉_2.
3. **The families satisfy the C-level identities used so far (Prop. 2.3; precise negative result for (a), restated in v2) [v2: FIX-1].** On 𝔉_D:
   - (𝒦) ⟺ F|h (resp. F|h');
   - the R19 Lemma 3.1 normal form holds with p=L^{−t}μ;
   - F|Δ holds, and FNAM2 holds;
   - the R19 reduction F∤(C_P,C_R) holds iff F∤μ (FNAM2 then iff h≢0);
   - every own-line divisibility ℓ_u|G_{c(u)} is **vacuous** (G≡0);
   - a>=d' (consistent with R20 Prop. 3.1).

   Answer to "iterate F|W_c": W_c=C_cBc/F=L^{−t}(h/F)(Bc)^⊥, and F|W_c iff F²|h. Nothing forces this.

   So no argument that uses only these **C-level consequences** can exclude (𝒦) with constant T, D∈{1,2}, a>=d' on 𝔉_D. The consequences are FNAM2, own-line divisibility (the content of FNAL2/TSYC/FNAM3), (𝒦), F|Δ, the R19 normal form, R20 Prop. 3.1 and the R19/R20 residual machinery.
   - [v2: FIX-1] Whether 𝔉_D **lifts to original data** is **OPEN**. Lifting means original P, R with global alignment and G5 whose FNAL quotient factors through TSY with C=C̃. It also involves FNAL's forgotten span(f^[X]) component and R16's full vector own-line identity.
   - That lift is where an exclusion may come from (HEURISTIC, Remark 2.5).
4. **Own-point defect outside (𝒦) (Lemma 3.2).** Put 𝔡(u):=k_{c(u)}(u)=𝒞_{c(u)}(u)B(u)c(u).
   - At every good u, 𝔡(u)∥(α^X,β^X)(u) (or 𝔡(u)=0).
   - Either 𝔡≡0, which defines a class (𝒦_ψ) ⊇ (𝒦) [v2: FIX-5: strictness is not shown]: k_12≡0 and k_11=ψk_22. Or 𝔡(u)≠0 at all good u except at most 2deg ψ+2ad'+2ρ·deg[T] (<0.1103q [v2: FIX-4], COMPUTED).
5. **Negative for (b) (Cor. 3.3).** At every good u off Z(𝔡), V_u(z(u))=κ_u𝔡(u)≠0.
   - [v2: FIX-5] So the R20 order-at-z(u) mechanism (Lemmas 4.1–4.2) gives order 0 for every ω∦c^[T], and nothing for ω∥c^[T] (where ξ^ω_u=G|_{ℓ_u}≡0).
   - That a per-point bound below a+mb(u) is unavailable by any residual route is only HEURISTIC.
   - In (𝒦_ψ), the defect at residual points factors through a ψ-comparison: k_{c(u)}(v)=β(u)(ψ(v)+ψ(u))k_22(v) (Remark 3.4, PROVED identity).

**COMPUTED.**
- `classify_PD.out`: the kernel of the P_D coefficient map equals the claimed family exactly (dimensions 4·dim_a, 3·dim_a, 2·dim_a for D=1, 2, 4/8), for a=0..4. [v2: N2] The map preserves Y-monomials, so the a=0 case already proves the kernel statement for every a.
- `family_check.out`: random members over GF(2) on a conic and on the Fermat cubic satisfy all six C-level identities of Prop. 2.3, in 36/36 cases. A negative control (h not divisible by F) fails (𝒦) as expected.
  - [v2: N3] Here B, L∈GL_2(F_2), so the Frobenius twist in K=LB^[D] is not exercised. The audit repeated the test over GF(16) with a genuine twist (36/36, and a wrong-twist control fails).
- `numerics_R21.out`: the FNAP-count bound for D∈{1,2} is <=0.0473 over 1260 rows; deg 𝔡²/q<=0.110235<0.1103 [v2: FIX-4].

**What failed.**
- (a) is not closed for the families 𝔉_1, 𝔉_2. They are consistent with every **C-level** identity used so far (Prop. 2.3); their lift to original data is OPEN [v2: FIX-1]. No count is possible from G, because G≡0.
- (b): no new closed range. The residual data outside (𝒦) carry no per-point information beyond ℓ_u|G_c (Lemma 3.1). The R20 order mechanism fails off Z(𝔡) (Cor. 3.3). Exploiting 𝔡(u)∥(α^X,β^X) costs ≈X·deg ψ (HEURISTIC).

**Newly closed (PROVED, numbers COMPUTED) [v2: FIX-3].**
- **Prior state.** R20 v2.1 Cor. 3.2 had already closed constant (𝒦) at n=256 for every D.
- **New here.** Constant-twist models with D∈{1,2} and C̃∉𝔉_D (equivalently P_D≢0) are excluded:
  - in (R2) for n>=512 (a>=d');
  - in (R3), outside (𝒦), for every n in the strip.
- **What remains.** 𝔉_D∩{F|h} with a>=d' inside (𝒦), and 𝔉_D∩{F∤h} outside it. The families are parametrised by the twist data (L, B).
- FNAP §4 shows that P_D can vanish; Prop. 2.1 classifies exactly when.

**Next step (HEURISTIC, §4).**
- For 𝔉_D: bring in the F·S layer at own-line orders >=E (R16 §5 item 1), which sees C̃ and not only P_D. On 𝔉_D the second layer is degenerate, C_c(Y)Bc=L^{−t}h·(Bc)^⊥, a scalar times a constant direction.
- For (R1): study the intermediate class (𝒦_ψ).

---

## 1. Setting

Standing hypotheses are those of R18-T §1 / R19 §3 (𝔇_16, global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128).
- For a constant twist, the good slopes c(u) lie in the set of at most Q+1 projective roots of c^tAc^[Q]=0 (FNAO §2, PRIMARY).
- At each good u, c(u)^[T]∥Kc(u)^[D] and G_{c(u)}=ν_u·P_D(c(u),·) with ν_u∈k^* (FNAP §2; R18-T Lemma 3.1 proof).
- ℓ_u|G_{c(u)} (FNAM3/TSYC).
- With q(z,Y):=C̃(z)z∈k[z,Y]² (quadratic in z, degree a in Y), P_D=z_1^Dq_1+z_2^Dq_2.

---

## 2. Constant twists with D∈{1,2}

**Proposition 2.1 (classification of P_D≡0; PROVED; COMPUTED check `classify_PD.out`).** Let C̃(z)=z_1A_1(Y)+z_2A_2(Y) with A_i∈M_2(k[Y]_a). Then P_D≡0 iff:
- (D=1) C̃(z)=h(z,Y)Ω+μ(Y)⊗z^⊥, with h=h_1(Y)z_1+h_2(Y)z_2, h_i∈k[Y]_a, μ∈k[Y]_a²;
- (D=2) C̃(z)=h'(Y)J(z)+μ(Y)⊗z^⊥, with h'∈k[Y]_a, μ∈k[Y]_a²;
- (D>=4) C̃(z)=μ(Y)⊗z^⊥. [v2: N12] Step 1 needs only D>=3; D>=4 is written because D is a power of 2.

In each case the parameters are unique. [v2: N2] The statement holds over every field of characteristic 2 and for every a. The proof uses only that k[z,Y] is a UFD. Moreover
      det C̃ = h·(h+μ_1z_1+μ_2z_2)  (D=1),    det C̃ = h'·(h'z_1z_2+μ_1z_1²+μ_2z_2²)  (D=2),    det C̃ = 0  (D>=4).
So FNAM2 (Δ≢0) holds iff h≢0 and h≢μ_1z_1+μ_2z_2 (D=1), resp. iff h'≢0 (D=2). For D>=4 it never holds (FNAP §3).

*Proof.*
- **Step 1: the shape of q.**
  - D>2: the z_1-exponents of z_1^Dq_1 lie in {D,D+1,D+2} and those of z_2^Dq_2 lie in {0,1,2}. So q≡0 (FNAP §3).
  - D=1: z_1q_1=z_2q_2 (characteristic 2). Since k[z,Y] is a UFD and z_1, z_2 are coprime primes, z_2|q_1. Write q_1=z_2h; then q_2=z_1h, with h of z-degree 1. So q=h·z^⊥.
  - D=2: z_1²q_1=z_2²q_2 gives q_1=z_2²h' and q_2=z_1²h' with h' of z-degree 0. So q=h'·z^{⊥[2]}.
- **Step 2: a particular solution.** C̃_0:=hΩ satisfies C̃_0z=hz^⊥ (D=1). C̃_0:=h'J(z) satisfies C̃_0z=h'(z_2²,z_1²) (D=2). C̃_0:=0 serves for D>2.
- **Step 3: the homogeneous solutions.** M:=C̃−C̃_0 is linear in z and Mz≡0. A row (r_1,r_2) of M with r_iz-linear and r_1z_1+r_2z_2=0 has z_2|r_1. Since r_1 is linear in z, r_1=λz_2 and r_2=λz_1 with λ∈k[Y]_a. So M=μ⊗z^⊥.
- **Step 4: uniqueness.** If hΩ+μ⊗z^⊥=0, the diagonal entries give μ_1z_2=μ_2z_1=0, so μ=0 and then h=0. The same argument works for D=2.
- **Step 5: the converse.**
  - z^{[D],t}(μ⊗z^⊥)z=(z^{[D]}·μ)(z^⊥·z) and z^⊥·z=2z_1z_2=0.
  - z^t(hz^⊥)=0.
  - z^{[2],t}(h'z^{⊥[2]})=2h'z_1²z_2²=0.
- **Step 6: determinants.** For D=1, C̃=[[μ_1z_2, h+μ_1z_1],[h+μ_2z_2, μ_2z_1]], so det=μ_1μ_2z_1z_2+(h+μ_1z_1)(h+μ_2z_2)=h²+h(μ_1z_1+μ_2z_2). D=2 is similar. ∎

**Corollary 2.2 (reduction of the constant D∈{1,2} lanes; PROVED, conditional on PRIMARY's FNAO §3 / FNAP (2) count; numbers COMPUTED).** Assume a constant twist with D∈{1,2} in 𝔇_16 (inside or outside (𝒦)), and that C̃ is **not** of the form in Prop. 2.1. Then P_D≢0, and
      N_good <= N·d + (D+2)(E+1)d + (Q+1)a + 6d_def + 7 < 1551q/4000.
So the model is excluded.

*Proof.*
- **The count.** FNAP's count (FNAO §3 with S replaced by D) uses D>2 *only* to show P_D≢0 (FNAP §3 "Thus P_D is nonzero"). The rest of the count is independent of D:
  - at most Q+1 slopes;
  - at most D+2 exceptional slopes, each a ψ-fibre of at most (E+1)d points;
  - at most a own lines per non-exceptional slope, distinct u giving distinct ℓ_u.
  Given P_D≢0, it applies verbatim.
- **Numerics.** With N<16h/625, a<8h/625, d=E+2 and d_def<=q/1000, the right side over q is at most 0.04338 (D=1) and 0.04728 (D=2). This holds over r∈{4,…,64}, Q∈{2^7,…,2^14}, S∈{2^6,…,2^12} and all dyadic 256<=n<4Q (`numerics_R21.out`).
- **[v2: FIX-2] Whole strip.** Write the bound over q term by term:
  (16/625)(1+2/E) + (D+2)/n·(1+1/E)(1+2/E) + 8(Q+1)/(625rQS) + 6/1000 + 7/q.
  Each term is non-increasing in r, Q, S and n (E=rQS, q=nE²). So the supremum over the whole strip (r>=4, Q>=128, S>=64, n>=256) is the value at (4,128,64,256), namely 0.0433718 (D=1) and 0.0472784 (D=2).
  - [v2: N11] The grid includes S<Q, which is not in the D-lane (S=Q^jD>=Q). It is therefore conservative. On the true lane the audit finds 0.0433453 and 0.0472384. ∎

**Proposition 2.3 (the families 𝔉_D satisfy the C-level identities used in R18-T–R20; PROVED; COMPUTED check `family_check.out`) [v2: FIX-1].** Let D∈{1,2} and C_c(Y):=L^{−t}C̃(Bc) with C̃∈𝔉_D. Then:
- (i) **(𝒦) holds iff F|h (resp. F|h').** For a constant twist, (𝒦) is C_c(Z)Bc=0 on Γ', i.e. F|L^{−t}q. Here q=h·z^⊥ (resp. h'·z^{⊥[2]}), whose second factor has coprime entries z_2, z_1 in k[c]. In particular, (𝒦) on 𝔉_D forces a=deg_Y h>=d', with h≢0 by FNAM2 [v2: N10] (R20 Prop. 3.1).
- (ii) **The R19 reduction F∤(C_P,C_R) holds, under F|h, iff F∤μ.** FNAM2 then holds iff h≢0. The second condition of Prop. 2.1, h≢μ·z, is automatic: h=μ_1z_1+μ_2z_2 with F|h would force F|μ.
- (iii) **R18-T Prop. 4.1(ii): F|Δ.** Indeed Δ=det L^{−t}·h(h+μ·z) (resp. h'(…)).
- (iv) **R19 Lemma 3.1 normal form.** On Γ', 𝒞_c=p⊗(Bc)^⊥ with p=L^{−t}μ|_{Γ'}.
- (v) **Own-line divisibility is vacuous.** At every good u, G_{c(u)}=ν_uP_D(c(u),·)≡0. So ℓ_u|G_{c(u)} holds trivially, and FNAP's count gets no non-exceptional slope.
- (vi) **The residual machinery is vacuous.** [v2: FIX-6] Since [B] is constant (B=λ^ρB_0), Ξ(u,v)=det(B(v)c,B(u)c)≡0 (R19 Cor. 3.2: G=κ_uΠ_1Ξ≡0).
  - Ξ≡0 makes N_Ξ(u) maximal, so on its own it would push u into 𝔅 via R20 Lemma 4.2.
  - The R20 line bound is vacuous on 𝔉_D∩(𝒦) because a>=d'. Then a−m>=d'−E>=#residual places, and Lemma 4.2 says nothing.
- (vii) **No iterated divisibility is forced.** W_c:=C_cBc/F=L^{−t}(h/F)(Bc)^⊥ (D=1), and W_c=L^{−t}(h'/F)(Bc)^{⊥[2]} (D=2) [v2: N7]. So F|W_c iff F²|h (resp. F²|h'), and h is free beyond F|h.
  - [v2: audit note] R19's reduction divides by F^k. On 𝔉_D with F|h and F|μ the reduced pencil is again in 𝔉_D, so the family is closed under the reduction.

*Proof.* Each item is immediate from Prop. 2.1 and the cited statements.
- For (i): F|h·z_2 and F|h·z_1 as polynomials in (c,Y) force F|h, since F∈k[Y] is prime and does not divide z_i.
- For (v): FNAP §2 and R18-T Lemma 3.1 give G_c=ν·P_D at good u. ∎

**Corollary 2.4 (answer to target (a); PROVED negative result at the C-level) [v2: FIX-1 restated].** Consider (𝒦) with constant T, D∈{1,2}. Every such model with a>=d' and P_D≢0 is excluded (Cor. 2.2). Every model with P_D≡0 lies in 𝔉_D with F|h. Such C-pencils satisfy the C-level consequences used in R18-T–R20:
- FNAM2 (Δ≢0);
- own-line divisibility ℓ_u|G_c (the content of FNAL2/TSYC/FNAM3);
- (𝒦)⟺F|h, F|Δ and the R19 normal form;
- R20 Prop. 3.1;
- the R19/R20 residual machinery.

Hence no argument using **only these consequences** excludes 𝔉_D.
- **OPEN:** whether 𝔉_D lifts to original data. That means original P, R with global alignment and G5 whose FNAL quotient factors through TSY with C=C̃, together with FNAL's forgotten span(f^[X]) component (FNAL §4: FNAL2 is necessary, not sufficient) and R16's full vector own-line identity.
- This is a statement about the listed C-level identities, not a claim that the models exist. G5, PRIM, the point count and the higher own-line layers are not checked. Remark 2.5 is consistent with this: the lift is the proposed exclusion route.

**Remark 2.5 (what could exclude 𝔉_D; HEURISTIC).**
- On 𝔉_D the second layer is degenerate along every pencil member: C_c(Y)Bc=L^{−t}h(Bc,Y)(Bc)^⊥, a single scalar form times a constant direction (D=1).
- R16 §5 item 1 records that the FN condition at own-line orders >=E involves the F·S layer through an identity in which C enters linearly but not only through P_D. That layer is the natural place to test 𝔉_D.
- A second option is G5 (det A≢0, used in FNAM2's proof). The rank-one-plus-scalar structure of 𝔉_D on Γ' may contradict it after lifting through TSY/FNAL.

---

## 3. (R1): the defect at the own point and at residual points

Outside (𝒦), write k_c:=𝒞_cBc=c_1²k_11+c_1c_2k_12+c_2²k_22, with
      k_11=𝒞_Pb_1,   k_22=𝒞_Rb_2,   k_12=𝒞_Pb_2+𝒞_Rb_1,
sections of z^*O(a)⊗𝓣^{ρ𝔮}, of degree ad'+ρ·deg[T]. (𝒦) ⟺ k_11=k_12=k_22=0.

**Lemma 3.1 (own-line shape; residual data carry nothing new; PROVED).** Let u be good. [v2: N4] The v1 hypothesis c_1c_2≠0 is unnecessary: if c_1=0, take η=V_1/c_2^T, and symmetrically. Then ℓ_u|G_{c(u)} holds iff
      V_u|_{ℓ_u} = η_u·(c^[T])^⊥
for a binary form η_u of degree a. In particular, the residual vanishing G_{c(u)}(z(v))=0 at every residual v is a consequence of ℓ_u|G_{c(u)}.

*Proof.* G_c|_{ℓ_u}=c_1^TV_1+c_2^TV_2. This vanishes identically iff V_1=c_2^Tη and V_2=c_1^Tη (characteristic 2), with η=V_1/c_2^T a polynomial. ∎

So any residual-point gain outside (𝒦) must come from identities in K valid at **all** v, i.e. from the structure of k_c (R20 (6.1)), and not from the vanishing itself.

**Lemma 3.2 (own-point defect; PROVED, conditional on R14.1, R18-T Lemma 1.2, FNAM3/TSYC (for G_{c(u)}(z(u))=0), R18-T Lemma 3.1 (u^[E]·e(u)=0), and R18 §5 (deg[T]<=Nd/ρ+d) [v2: N5]).** Put 𝔡(u):=k_{c(u)}(u)=β(u)k_11(u)+√(αβ)(u)k_12(u)+α(u)k_22(u).
- (i) At every good u, c(u)^[T]·𝔡(u)=0. Equivalently, 𝔡(u)=0 or 𝔡(u)∥(α^X,β^X)(u).
- (ii) The section 𝔡²:=β̃²k_11^{[2]}+α̃β̃k_12^{[2]}+α̃²k_22^{[2]} (componentwise squares; α̃,β̃ as in R20 Lemma 4.3) has degree 2deg ψ+2ad'+2ρ·deg[T].
- (iii) **Dichotomy.** 𝔡≡0 iff (𝒦_ψ): k_12≡0 and k_11=ψ·k_22. Otherwise at most 2deg ψ+2ad'+2ρ·deg[T] good u have 𝔡(u)=0. With ρ·deg[T]<=Nd+ρd (R18 §5), this is <=0.110235q<0.1103q on the grid (`numerics_R21.out`) [v2: FIX-4: v1 said <=0.1102q, but the exact maximum is 0.11023472]. By the same monotonicity as in Cor. 2.2, this is also the whole-strip supremum (audit).
- (iv) (𝒦)⊆(𝒦_ψ), with equality iff k_22≡0. Whether (𝒦_ψ)∖(𝒦) is nonempty, even formally, is not shown [v2: FIX-5].

*Proof.*
- **(i)** z(u)∈ℓ_u, so G_{c(u)}(z(u))=0. With c^[Q]=κ_uB(u)c (good u), G_c(z(u))=κ_uc^[T]·𝒞_c(u)B(u)c=κ_uc^[T]·𝔡(u). Also c^[T]=(β^X,α^X) projectively (c=(√β:√α), T=2X), and in characteristic 2 x·y=0 iff y∥x^⊥.
- **(ii)** Squaring is additive.
- **(iii)** Normalise by a fixed section and divide by β̃: 𝔡/β=k_11+√ψk_12+ψk_22, with k_ij∈K⊕K (vectors over K). Since √ψ∉K (R14.1), 1 and √ψ are K-independent, so 𝔡≡0 iff k_12=0 and k_11=ψk_22. If 𝔡≢0, some component of 𝔡² is a nonzero section, and its zeros contain {𝔡(u)=0}.
- **(iv)** Immediate. ∎

**Corollary 3.3 (the R20 order mechanism fails outside (𝒦_ψ); PROVED negative result, scope restricted in v2) [v2: FIX-5].** Let u be good with 𝔡(u)≠0 (all but <0.1103q good u when 𝔡≢0 [v2: FIX-4]). Then V_u(z(u))=κ_u𝔡(u)≠0. So for every ω∈k² with ω·𝔡(u)≠0 (all ω except one projective direction), ξ^ω_u(z(u))≠0, i.e. ξ^ω_u has order 0 at z(u).

Consequences [v2: FIX-5]:
- The R20 order-at-z(u) mechanism (Lemmas 4.1–4.2) yields order 0 for every ω∦c^[T], and nothing for ω∥c^[T] (there ξ^ω_u=G|_{ℓ_u}≡0), at all good u off Z(𝔡).
- Outside (𝒦), R20's (1.1)/Ξ factorisation does not exist, so no "comparison factor" is defined.
- That **no** per-point residual bound below a+mb(u) exists outside (𝒦_ψ) is HEURISTIC. v1 stated it as part of the PROVED result.

*Proof.* (1.1)-type expansion: V_u(z(y))=𝒞_c(y)c^[Q]=κ_u𝒞_c(y)B(u)c with c=c(u) frozen. At y=u this is κ_uk_{c(u)}(u). ∎

**Remark 3.4 ((𝒦_ψ): the defect factors through a ψ-comparison; PROVED identity).** In (𝒦_ψ), for all u, v,
      k_{c(u)}(v) = β(u)k_11(v)+α(u)k_22(v) = β(u)·(ψ(v)+ψ(u))·k_22(v),
with no square root, since k_12≡0. At a good u and a residual v (R20 (1.1)–(6.1)),
      V_u(z(v)) = κ_u[ β(u)(ψ(v)+ψ(u))k_22(v) + 𝒞_c(v)(B(u)+B(v))c ],   c=c(u).
So in (𝒦_ψ) the residual vector is a sum of a **ψ-comparison** term and the B-comparison term of R19.
- (HEURISTIC) [v2: N8] Along Γ at y=u, V_u(z(y)) has order >=min(ρ𝔮, ord_uk_22+e_ψ(u)), which is generically 1. So the R20 order mechanism yields only m=1 there. This needs β(u)≠0, a common local frame for B(u)+B(y) (as in R18-T Prop. 4.1(iii)) and non-cuspidal u for R20 Lemma 4.1. The m=1 conclusion is a generic claim.
- Whether (𝒦_ψ)∖(𝒦) can be handled as (𝒦) was in R19/R20 is OPEN.

**Remark 3.5 (cost of the own-point identity; HEURISTIC).**
- Lemma 3.2(i) is a cheap section 𝔡 (<0.1103q [v2: FIX-4]) constrained by the expensive relation 𝔡_1β^X=𝔡_2α^X. Its zero count as a section costs ≈X·deg ψ≫q.
- Rewriting x^X=y as y^{q/X}=x on F_q-points costs (q/X)·deg 𝔡, which is worse.
- Replacing c^[T] by 𝒦𝓂(u)c^[D] (R18-T) costs X·deg[T]. That is R18-T Thm 3.4 again (𝔊_0).
- So the own-point defect reproduces R18-T's cost and gives no new range. This is the R21 form of R19 Prop. 5.2's E/X-penalty.

---

## 4. What remains, and next steps

**Residual after this note** (inside 𝔇_16, global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128):
- **Constant twist, D∈{1,2}** [v2: FIX-3]:
  - (R2) at n=256 was already closed by R20 Cor. 3.2.
  - In (R2) with n>=512 (a>=d') and in (R3), only the families 𝔉_1, 𝔉_2 of Prop. 2.1 remain: F|h inside (𝒦), F∤h outside.
  - Their lift to original data is OPEN [v2: FIX-1].
- **Constant twist, D>=4:** as before (FNAP, n>=4D). Prop. 2.1 adds nothing there.
- **Non-constant twists:** (R1) is unchanged. (R2) is as in R20 v2.1 Cor. 5.3. The new intermediate class (𝒦_ψ) (Lemma 3.2(iii)) is open.

**Next steps (HEURISTIC).**
1. **𝔉_D versus the F·S layer.** Write the order->=E own-line identity of R16 §5 for C_c=L^{−t}(hΩ+μ⊗z^⊥)(Bc), in which every pencil member is a scalar times a constant direction plus a rank-one term. Test it on the toys of `family_check.py`, lifted through TSY.
2. **(𝒦_ψ).**
   - k_12=0 is the mixed (𝒦)-identity alone. k_11=ψk_22 ties the two pure defects by ψ.
   - Try R19 Lemma 3.1's rank argument with ψ-twisted kernels: 𝒞_Pb_1=ψ𝒞_Rb_2, 𝒞_Pb_2=𝒞_Rb_1.
   - If it yields a normal form 𝒞_c=p⊗(Bc)^⊥+(ψ-term), Remark 3.4's two-comparison structure may admit an R19-type count, with Ξ and ψ(v)+ψ(u) both handled per point.
3. **(R1) outside (𝒦_ψ).** Cor. 3.3 shows that per-point residual bounds are unavailable. Progress needs either a cheap way to use 𝔡(u)∥(α^X,β^X) at good points (a Frobenius-twisted Stöhr–Voloch count on Γ for the pair (ψ,𝔡_1/𝔡_2)), or input beyond the second layer.

---

## 5. Computations (`scripts/` in the owner directory, delivered to the audit as `owner_scripts/` [v2: N1]; all `python3 -I`, single process, each < 10 s)

| script → output | content | result |
|---|---|---|
| `classify_PD.py` → `.out` | exact GF(2) linear algebra: kernel of C̃↦P_D for D∈{1,2,4,8}, a=0..4, compared with the families of Prop. 2.1 | kernel dimension = 4·dim_a, 3·dim_a, 2·dim_a, 2·dim_a; family ⊂ kernel and spans it; all 20 cases OK |
| `family_check.py` → `.out` | random 𝔉_D members (D=1,2) over GF(2) with random B, L∈GL_2(F_2), F a conic or the Fermat cubic, a=d'..d'+2, F|h; checks P_D≡0, (𝒦), FNAM2 and F|Δ, F∤C, R19 normal form, a>=d'; negative control h∤F | 36/36 all True; control: (𝒦) fails 3/3 while P_D≡0 still holds |
| `numerics_R21.py` → `.out` | exact Fractions: the FNAP count for D∈{1,2} (Cor. 2.2); deg 𝔡²/q (Lemma 3.2) | max bound/q = 0.043372 (D=1), 0.047278 (D=2) < 0.38775 over 1260 rows; max deg 𝔡²/q = 0.110235 (<0.1103) |
| `classify_PD_v2.py`, `family_check_v2.py`, `numerics_R21_v2.py` → `*_v2.out` [v2: N1] | header-corrected copies (section numbers Prop. 2.1/2.3, Cor. 2.2, Lemma 3.2; the GF(2)-only twist caveat) | outputs byte-identical to v1's (`cmp`) |

Checksums: `scripts/SHA256SUMS.txt`.

---

## 6. Status

| item | status |
|---|---|
| Prop. 2.1 (classification of P_D≡0 for a constant twist) | PROVED; COMPUTED (exact GF(2) kernel dimensions) |
| Cor. 2.2 (constant D∈{1,2}: excluded unless C̃∈𝔉_D) | PROVED, conditional on PRIMARY's FNAO/FNAP count; whole strip by monotonicity [v2: FIX-2] |
| Prop. 2.3 (𝔉_D satisfies the C-level identities: (𝒦) iff F\|h, FNAM2, F\|Δ, normal form, vacuous own-line and residual conditions) | PROVED; COMPUTED (36/36 plus control; GF(16) by the audit) [v2: FIX-1, FIX-6] |
| Cor. 2.4 (no exclusion of constant (𝒦), D∈{1,2}, a>=d' from the C-level identities) | PROVED (C-level only) [v2: FIX-1]; lift to original data (FNAL/TSY/G5) OPEN |
| Remark 2.5 (F·S layer or G5 as the exclusion route) | HEURISTIC |
| Lemma 3.1 (own-line shape; residual vanishing implied) | PROVED |
| Lemma 3.2 (own-point defect: 𝔡(u)∥(α^X,β^X); dichotomy (𝒦_ψ)⊇(𝒦) vs few zeros) | PROVED (R14.1, R18-T Lemma 1.2, FNAM3/TSYC, R18 §5); bound <0.1103q COMPUTED [v2: FIX-4, FIX-5, N5] |
| Cor. 3.3 (R20 order-at-z(u) mechanism gives order 0 off Z(𝔡)) | PROVED (negative, for that mechanism only); "no residual per-point bound at all" HEURISTIC [v2: FIX-5] |
| Remark 3.4 ((𝒦_ψ) defect identity) | PROVED identity; the m=1 order claim HEURISTIC [v2: N8]; usefulness OPEN |
| Remark 3.5 (cost ≈X·deg ψ) | HEURISTIC |
| 𝔉_1, 𝔉_2 (constant, D∈{1,2}); (R1); (𝒦_ψ)∖(𝒦); (R2) ranges left by R20 | OPEN |

Dependencies: R20 v2.1, R19 v2.1, R18-T v2.1 (audited, revision-checked); PRIMARY FNAO/FNAP/FNAM/FNAN (reviewed). v1 was independently audited (PASS-with-fixes); v2 applies FIX-1..6 and N1–N12 and has not been revision-checked. No manuscript was edited. The classification of hyperovals is not claimed complete.
