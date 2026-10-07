# Independent audit: HYP M>=2 round 18-T (non-constant twist in 𝔇_16), owner note v1

7 October 2026. Claude, independent adversarial referee, for session_012ij7YN37LGpSS88rmUGQ7E.

**Audited file:** `src/HYP_M2_ROUND18T_TWIST_NOTE_v1.md` (SHA-256 in `checks/src_SHA256SUMS.txt`).

**Rules followed.**
- I read only files in `src/` and wrote only in `checks/` and this file.
- I opened no file whose name contains "DZ".
- Owner scripts were copied to `checks/owner_copy/` and re-run with `python3 -I`. Both outputs are byte-identical to the shipped `.out` files.
- All other checks are my own scripts (`checks/r1_numerics.py`, `checks/r2_algebra.py`; galois 0.4.11, exact arithmetic).

**Scale:** PASS / PASS-with-fixes / FAIL.

---

## 0. Verdict

**PASS-with-fixes.**

**What holds.** The technical core of the note is correct as stated, conditional on its cited inputs:
- Lemmas 1.1 and 1.2 (one wording fix).
- Lemma 2.1.
- Prop. 2.4(i)–(v).
- Def. 3.0 and the degree formula (3.0).
- Lemma 3.1, with every exceptional set charged.
- Lemma 3.2: the field-theoretic descent, the F_0-frame, binary-form splitting, and the FNAP algebra over k[t]/(t^{K_0}).
- Prop. 3.3(a),(b).
- Thm. 3.4 and bound (3.2).
- Cor. 3.5: every number recomputed exactly.
- Props. 4.1 and 4.2, and Example 4.3.

**One substantive fix (FIX-1).**
- The hypothesis (H_bs) of Prop. 2.2 ("no base point of f lies on Γ'") **never holds** in 𝔇_16. Every proper base point of f lies on Γ', with multiplicity >=E−3.
- So Prop. 2.2, Cor. 2.3 and the non-constant-twist construction in Prop. 2.4 are vacuous as stated.
- The **"(PROVED)"** obstruction in Remark 2.5, which reappears in Summary items 2–3 and §5.1, is therefore not established.
- The fix is to replace (H_bs) by the genuine hypothesis "polynomial lift" (H_lift), which is OPEN, and to relabel the obstruction as conditional/HEURISTIC.
- No result of §§3–4 depends on §2, so Thm 3.4, Cor 3.5 and §4 stand unchanged.

The other fixes are wording, bookkeeping or citation updates. No threshold changes.

---

## 1. Parameter constraints used

- q=Eh, E=rQS, T=QS, X=QS/2=ρS, ρ=Q/2. Here r>=4, Q>=128 (strip), S>=64, all dyadic.
- S=Q^jD with D=2^t<Q.
- Strip: 256E<=h<4QE, with n=h/E dyadic.
- N=M−1−X<M<16h/625 and M'=(M−1)/2. Also a=deg C_•=M'+X−ρ−d'<M'<8h/625.
- d<=E+2, d'=deg F>=2E−2, d_def<=q/1000, and the boundary charge is 6d_def+7.
- 𝔮>=128 (R18 v2.1 Cor. 5.5).
- G9: N_good>1551q/4000+1.
- deg ψ<=(E+1)d.
- |𝔈∖boundary|<=1.5d²+3.5d+1 (R16.4). This **includes** {g=0} (<=3d) and {D=0}.

---

## 2. Item table

| item | verdict | notes |
|---|---|---|
| Lemma 1.1 (non-constant CMIX) | PASS-with-fix (FIX-3) | Identity and Nd bound are correct; independence of E_P(u),E_R(u) needs g(u)≠0 |
| Lemma 1.2 (slope eq. = 𝔉^ρ; B=swap·𝒜^t) | PASS | Kernel and 𝔉 identities checked (r2 c); note N2 (c_1=0; identification with s_M(u)) |
| Lemma 2.1 (cross factorisation; layer identity) | PASS | r2 a, b (160 points, exact) |
| Prop. 2.2 (polynomial lift under (H_bs)) | PASS as a conditional implication; **hypothesis never satisfied** (FIX-1) | Steps 1–6 correct; Step 4 CM/nonzerodivisor argument correct; Step 3 needs no (H_bs) (N3) |
| Cor. 2.3 | PASS conditional; vacuous under (H_bs) (FIX-1) | Bound correct under (H_lift); actually m·d'<Nd (N5) |
| Prop. 2.4 (i)–(v) (decoupling) | PASS (unconditional) | "In particular" example needs (H_bs)/(H_lift) (FIX-1) |
| Remark 2.5 | **Overclaim** (FIX-1, FIX-2) | "(PROVED) no identity-only argument forces T constant" is not established; "Γ-local structure" is not invariant |
| Def. 3.0, degree formula (3.0) | PASS | Exponent (T−D)/(Q−1) is an integer; bidegree (D+2,a); 2ρ𝔮 deg𝓣=Q deg[T] (r2 d) |
| Lemma 3.1 | PASS | All exceptional sets charged: boundary, 𝔈 ⊇ {g=0} (FIX-N1 satisfied), {λ'=0} replaces R18's Z_λ, {det T̂=0} |
| Lemma 3.2 | PASS | All seven steps verified; Step 5 also tested by exact GF(2) linear algebra (r2 e), Step 7 exhaustively over GF(2)[t]/(t²) (r2 f) |
| Prop. 3.3 (a),(b) | PASS | |
| Thm 3.4, bound (3.2) | PASS | Exceptional sets complete; degree bound correct |
| Cor. 3.5 numerics | PASS-with-fix (FIX-5) | All values exact; D-windows understated beyond n=1024 |
| Prop. 4.1 (i)–(iv) | PASS | |
| Prop. 4.2 | PASS | Algebra 2a<d' ⟺ M−1+T−Q<3d' checked |
| Example 4.3 | PASS (formal, as labelled) | Owner check re-run |
| §5 items 3, 5 | wording (FIX-6, FIX-7) | |
| Labels and status table §8 | PASS-with-fixes (FIX-1, FIX-4) | |

---

## 3. Detailed audit

### §1. Lemma 1.1

**The identity.** It follows from R18 v2.1 Thm 4.2(iv) and purity ϰ_•=λ_ϰM_•^[ρ]:

      ϰ_P = λ_ϰλ^ρ(T_11^ρE_P^[ρ]+T_21^ρE_R^[ρ]).

So 𝒜 has rows (T_11^ρ,T_21^ρ) and (T_12^ρ,T_22^ρ), i.e. 𝒜=(T^t)^[ρ]. Correct.

**Regularity of λ'.** Write ϰ_P(u) in the basis E_P(u)^[ρ], E_R(u)^[ρ].
- Frobenius preserves k-independence, since k is perfect.
- By Cramer with a nonvanishing minor, the coefficients λ'·t̂^{ρ𝔮} are regular.
- Some t̂_ij(u)≠0, so λ' is regular at u.
- **Caveat (FIX-3).** The independence of E_P(u), E_R(u) is FNAN §1's "maximal minors of J(e(u)) = const·g(u)u". It needs g(u)≠0 and e(u)≠0. "At a good point" must read "at a good point off {g=0} (and off Bs(e))". This is exactly FIX-N1 of the Claude PRIMARY review.

**Zeros.** If λ'(u)=0, then ϰ_P(u)=ϰ_R(u)=0. So there are <=Nd such points, from one fixed nonzero entry, a section of O(N). Correct.

**R18's Z_λ.** The note never uses the M-normalised rows, only ϰ=λ'𝒜E^[ρ]. So only λ'(u)≠0 is needed, and Z_λ is correctly replaced by {λ'=0}.

### §1. Lemma 1.2

**Order-ρ coefficient.** Take a smooth good point u off 𝔈 (so g(u)≠0 and R16.2 applies). Then:
- (E_•(y)·u)^ρ = s^ρ(E_•(u)·w)^ρ + O(s^{2ρ}).
- (E_P·w, E_R·w) = κ·(β,α) = κc^[2], because n=αE_P+βE_R kills w.
- So the s^ρ-coefficient is λ'(u)κ^ρ·c^t𝒜(u)c^[Q]. It vanishes because E−X>ρ.

**Kernel.** The row r=c^t𝒜 has kernel spanned by (r_2,r_1)=[[𝒜_12,𝒜_22],[𝒜_11,𝒜_21]]c=swap·𝒜^t·c. With the entries of 𝒜 this gives B=[[T_21^ρ,T_22^ρ],[T_11^ρ,T_12^ρ]], which is correct.

**Relation to 𝔉.** c^t𝒜c^[Q] at c=(1,s^ρ) equals (T_11+sT_12+s^QT_21+s^{Q+1}T_22)^ρ=𝔉(s)^ρ. Checked exactly for ρ=2,4,8,64 (r2 c).

**N2 (optional).**
- (i) At points with β(u)=0, c=(0:1) is not of the form (1:s^ρ). Use the homogenised 𝔉 (s=∞).
- (ii) The identification with R18's 𝔉(u):=𝔉(s_M(u)) deserves one line. The slope equation is W(s)=s^{−Q}=β/α(u) for s=(α/β)^{1/Q}(u). W is injective at u (det T(u)≠0), and W(s_M)=β/α (R18 Thm 4.2(iv)). Hence s=s_M(u). I verified (𝔉(s)=0 ⟺ W(s)=s^{−Q}) numerically (r2 c).

### §2. Lemma 2.1

**(i).** In characteristic 2, (a×b)×v=(a·v)b+(b·v)a. Frobenius commutes with ×. Hence

      f^[X]×v = κ_0^X(j_1^[X]·v j_2^[X] + j_2^[X]·v j_1^[X]) = κ_0^X J^[X]ΩJ^[X,t]v.

Correct (r2 a: X=2,…,16, random centres).

**(ii).**
- FH_P=[f^[X]]_×P^t (FNAL) and H_P=J^[X]C_PJ^[ρ,t] (TSY) give J^[X](κ_0^XΩJ^[X,t]P^t−FC_PJ^[ρ,t])=0.
- J^[X] is injective over Frac(S), so J^[X,t]P^t=κ_0^{−X}FΩC_PJ^[ρ,t].
- C_P is recovered because J^[ρ,t] has full row rank.
- Correct. r2 b builds P^t=f^[X]⊗κ+F·S with [f^[X]]_×S=H pointwise and confirms the displayed identity at 160 points.

### §2. Prop. 2.2: the mathematics, conditional on (H_bs)

**Step 1.** Common image gives r_if_j^X≡r_jf_i^X (mod F); these are the entries of [f^[X]]_×P^t. On the charts {f_k≠0}, κ=r_k/f_k^X is regular and the charts glue. Under (H_bs) they cover Γ'. Correct.

**Step 2.** H¹(P²,O(n))=0 for all n, so restriction is surjective. Correct.

**Step 3.**
- On Γ', ϰ_P=g^X·κ∘e, so κ·f^[ρ]=g^{ρ−X}ϰ_P·U^[ρ]=0. Hence κ̃·f^[ρ]≡0 (mod F). Correct.
- *N3:* (H_bs) is not needed here. F is prime and F∤f_i^X for some i, so F | f_i^X·h for all i already gives F | h.

**Step 4.**
- I=(f_0,f_1,f_2) is the ideal of maximal minors of the 3×2 matrix J (FNAM1).
- The f_i have no common factor, so ht I>=2=the expected codimension. Hence S/I is perfect (Hilbert–Burch).
- Flat Frobenius base change keeps 0→S²→S³→S exact. So pd S/I_ρ=2, depth 1, dim 1, and S/I_ρ is CM. Its associated primes are the minimal primes, i.e. the points of Bs(f).
- F avoids them under (H_bs), so F is a nonzerodivisor. Then Fb∈I_ρ⇒b∈I_ρ, and κ̃'=κ̃−Fη is a syzygy.
- Correct.

**Steps 5–6.** Syz(f^[ρ])=J^[ρ]S² (TSY/FNAM1). The coefficients A_P,B_P have degree M'−2X−ρ=m. The comparison uses ϰ_P=g^Xκ∘e and E_•=j_•(e(U)), with λ''=g^{−X}λ' common to P and R. Correct.

**The defect: (H_bs) is never satisfied (FIX-1).**
- C_f(Z):=Z·f(Z)^[E] vanishes on Γ', and deg C_f=2E+1.
- Let q be a proper base point of f; one exists for every plane quadratic Cremona map. Every f_i vanishes at q, so mult_q C_f>=E.
- The components of {C_f=0} other than Γ' have total degree 2E+1−d'<=3, because d'>=2E−2 is cited by the note itself. Their multiplicity at q is therefore <=3.
- Hence **mult_q Γ'>=E−3>0, so q∈Γ'.**
- *COMPUTED (r2 g1).* On the Fermat σ1 model, the main test model of R16–R18, F=(Y_1Y_2)^n+(Y_0Y_2)^n+(Y_0Y_1)^n with n=E−1 has multiplicity exactly E−1 at the base point (1:0:0) of f.
- *COMPUTED (r2 g2).* For 8 random centres e=LU×NU (E=16), I took the third zero u* of C_orig on the contracted line through two base points of e. It satisfies C_orig(u*)=0 and e(u*)≠0, and f(e(u*))=0, i.e. g(u*)=0. Since deg Γ>=E−1>2, u*∈Γ, so e(u*)∈Γ'∩Bs(f).
- Equivalently: Γ meets every contracted line of e, and e maps those points to base points of f.

**Consequences of FIX-1.**
- Prop. 2.2 and Cor. 2.3 are true implications with a false hypothesis.
- The "Without (H_bs)" paragraph is in fact **the** general case.
- If a polynomial lift exists, then P^t≡f^[X]⊗κ̃' (mod F) forces P(q)=R(q)=0 at every proper base point q of f (since q∈Γ', f(q)=0). So a lift is a genuine, possibly restrictive condition on the original model, not an automatic one.

### §2. Cor. 2.3

- Under a lift, [T^ρ]=[A_P:B_P:A_R:B_R]|_{Γ'}. These are forms of degree m on a curve of degree d', so ρ·deg[T]<=m·d'. Correct.
- *N5.* d'<=2d (e is quadratic), so m·d'<=(M−1−4X−2ρ)d<Nd. Hence deg[T]<Nd/ρ, marginally below R18's Nd/ρ+d. "No height improvement" is fair.
- The example (A/B=(α_1/β_1)^{ρ𝔮}) is immediate.
- Numerics: 2m/Q<64E/625≈0.102E holds only near h→4QE. At h=256E it is <0.0512E (Q=128). That is harmless.

### §2. Prop. 2.4 and Remark 2.5

**(i)–(v): correct and unconditional for η∈Syz(f^[ρ])_{M'−2X}.**
- (i) f^[X](η·f^[ρ])=0.
- (ii) The added term has image in span f^[X].
- (iii) Zero top is unchanged.
- (iv) [f^[X]]_×(f^[X]⊗η)=(f^[X]×f^[X])⊗η=0, so H is unchanged, and so are C (TSY uniqueness), G_c and Δ.
- (v) This is the definition.
- *Remark.* Every P' with the same second layer is of this form. J^[X,t](P'^t−P^t)=0 and ker J^[X,t]=S·f^[X], since the maximal minors are κ_0^X f^[X], which has grade 2. So P'^t=P^t+f^[X]⊗η with η polynomial; the syzygy condition is then the zero-top/alignment requirement.

**"In particular" (non-constant twist T').**
- The computation T'=[[α_1^𝔮,α_2^𝔮],[β_1^𝔮,β_2^𝔮]](e(U)) is correct, given the lift κ̃'.
- Without (H_bs), or (H_lift), the first layer κ cannot be cancelled by a polynomial η.
- Adding g(α^{ρ𝔮}j_1^[ρ]+β^{ρ𝔮}j_2^[ρ]) to λ''T^ρ-rows does not in general give a scalar times a K^{ρ𝔮}-matrix, i.e. it is not a twist normal form.

**Remark 2.5.**
- *FIX-1.* The bullet "(PROVED) no argument that uses only these identities … can force T to be constant" rests on the "In particular" example, hence on (H_bs). It is therefore not proved.
- *Logical caveat.* Even under (H_lift) the correct meta-statement is weaker: "any derivation of constancy from these identities alone would also derive a contradiction from them for the exchanged data, i.e. it would have to exclude all lift-admitting data with ρ𝔮<=m". An identity-only argument that proves the identities inconsistent is not ruled out.
- *FIX-2.* "and by R16–R18's Γ-local structure" is inaccurate. The R16.2 series, the slope equation (Lemma 1.2) and FN at good points involve the first layer at u and are **not** invariant under P^t↦P^t+f^[X]⊗η. Only the global polynomial identities are invariant: alignment, common image, zero top, H, C, G_c, Δ. The next bullet, "without the coupling … at the same good point u", already concedes this. The sentence should be made consistent with it.

### §3. Definition 3.0 and degree (3.0)

**The iteration.** With B_1=B and B_{i+1}=B_i^[Q]B, we get c^[Q^i]∥B_i c. Induction: c^[Q^{i+1}]∥(B_ic)^[Q]=B_i^[Q]c^[Q]∥B_i^[Q]Bc. Then c^[T]=(c^[Q^{j+1}])^[D]∥𝒦𝓂c^[D].

**Degree of the entries.**
- B_i has degree e_i=(Q^i−1)/(Q−1) in units of 𝓣^{ρ𝔮}.
- Hence 𝒦𝓂 has D(Q^{j+1}−1)/(Q−1)=(T−D)/(Q−1), which is an integer.
- r2 d checks the parallelism and the exponent for Q∈{4,8}, j∈{0,1,2}, D∈{1,2,4} (90 cases). It also checks that G_c∝𝒫_u with a constant independent of C.

**Bidegree and (3.0).**
- 𝒫 has bidegree (D+2,a).
- 𝔊_k² carries:
  - 𝓐^{D+2}, from c^[2]=(β̃,α̃);
  - 𝓣^{2ρ𝔮[(T−D)/(Q−1)+1]}=𝓣^{Q𝔮(Q−1+T−D)/(Q−1)}, of degree Q·deg[T]·(Q−1+T−D)/(Q−1);
  - O(2(2(a−k)+Ek)), from a−k entries of Z∈O(2) and k entries of V∈O(E).
- Correct. Dehomogenising multiplies each t^k-coefficient by its own nonzero unit, so "𝔊_k≡0" is unambiguous.

### §3. Lemma 3.1: exceptional sets

**Reduction.** Off {det T̂=0}, B(u)∈GL_2(k). The pointwise iteration gives c^[T]∥𝒦𝓂(u)c^[D] with nonzero sides, so G_c=ν𝒫_u.

**Own line.**
- FNAM (FNAL+TSY+TSYC+FNAM3) needs u to be original good, off the base/contracted boundary, with g(u)≠0, and some nonradial V chosen at u. It does not need the specific V=U^[E]×c_0.
- So ℓ_u | G_{c(u)}, or G_{c(u)}=0.
- z+tV(u)∈ℓ_u for all t, including when V(u) is radial.
- c_gen(u)∝c(u), since α̃,β̃ have no common zero.

**Exceptional sets.**
- Original boundary (6d_def+7).
- 𝔈 (R16.4). It contains {g=0} (<=3d, inside 1.5d²+3.5d+1), so **FIX-N1 is satisfied**, together with Sing Γ, {D=0}, ramification and infinity.
- {λ'=0} (<=Nd; this replaces R18's Z_λ, see §1).
- {det T̂=0} (<=2deg𝓣=2deg[T]/𝔮).

This list is complete. B, 𝒦𝓂, Z, V and c_gen² are sections, so there are no poles.

### §3. Lemma 3.2: line by line

**Step 1.**
- [K:K²]=2, so [K^{1/2}:K^D]=2D.
- γ^{2^i}=ψ^{2^{i−1}}∈K^D forces ψ∈K^{D/2^{i−1}}⊂K² unless 2^{i−1}>=D. So [F_0(γ):F_0]=2D and F_0(γ)=K^{1/2}.
- For D>=3, D+3<=2D, so 1,…,γ^{D+2} are independent. Correct.

**Step 2.**
- Divide by one t̂_{i0j0}. The entries of B, 𝒦𝓂 then lie in K^{ρ𝔮}⊂K^D (D<Q<=ρ𝔮), and C_P,C_R have constant coefficients.
- So Π_m∈F_0[Y], and c_gen∝(1,γ) because γ=√(α/β). Correct.

**Step 3.**
- In the affine normalisation, U^[E]∈(K^E)³⊂F_0³ (D|E). So P_i=λ×w_i∈F_0³, and they span λ^⊥.
- Z,V∈λ^⊥.
- στ'−σ'τ≠0 ⟺ Z∦V ⟺ c_0·e(U)≢0, which holds for generic c_0. Correct.

**Step 4.**
- Homogeneity gives Π(Z+tV)=(τ+tτ')^a g(w(t)) with a unit prefactor.
- w(t)−w_0=t(σ'τ−στ')/(τ(τ+tτ')) has order exactly 1.
- By Hasse–Taylor expansion at w_0∈K, ord_t g(w(t))=min{j: g^{(j)}(w_0)≠0}. So the hypothesis is (w−w_0)^{K_0} | g in K^{1/2}[w]. Correct.

**Step 5.**
- Φ:=(w−w_0)^{K_0}=(w^D−w_0^D)^{K_0/D} is monic in F_0[w].
- Divide each g_m by Φ in F_0[w]. The remainder of g is then Σγ^m r_m, by uniqueness of division in K^{1/2}[w]. It is 0, so all r_m=0 by F_0-independence.
- This is the same as the note's coordinate comparison. Correct.
- *COMPUTED (r2 e).* Over k(y) with γ=y, F_0=k(y^{2D}), w_0=y², I computed exactly over GF(2) the solution space of "(w−w_0)^{K_0} | Σ_m y^m g_m" with g_m∈F_0[w] in a coefficient box, and compared it with the space where every g_m is divisible. The dimensions are equal for (D,K_0)=(4,4),(8,8),(4,4) with larger boxes (28=28, 44=44, 63=63).
- Control D=2 (D+2=2D, independence fails): 38>30, so the joint condition is strictly weaker, as expected.

**Step 6.** The coefficients are in K. Their vanishing is generic, so it holds at all but finitely many u. Correct.

**Step 7.**
- z'=B(u)c and Λ=𝒦𝓂(u)(B(u)^{−1})^[D]. With (Mv)^[D]=M^[D]v^[D] for constant M, 𝒫_u=z'^[D,t]Λ^tC̃(z')z'.
- The z'_1-supports {D,D+1,D+2} and {0,1,2} are disjoint for D>2, over any coefficient ring, in particular R=k[t]/(t^{K_0}).
- So Λ^tC̃z'=0, hence C̃z'=0, which is (3.1). Correct.
- *COMPUTED (r2 f).* Exhaustively over GF(2)[t]/(t²), all 4^8=65536 pencils C̃(z)=z_1A_1+z_2A_2: z^[4,t]C̃z=0 ⇒ C̃z=0, with 0 counterexamples.

### §3. Prop. 3.3

**(a).** Apply Lemma 3.2 with K_0=D and take the t⁰-term. It vanishes at infinitely many u, hence (𝒦) holds in K. Correct.

**(b).**
- Take K_0=D⌈(a+1)/D⌉>a. The polynomial of t-degree <=a then vanishes.
- For generic u, V(u)∦z, so z+tV(u) sweeps ℓ_u minus one point; by homogeneity it covers all of ℓ_u.
- B(u)c≠0 gives Δ(c,Y)=0 on ℓ_u for all c∈k². Since k is infinite, every coefficient Δ_i vanishes on ℓ_u.
- Infinitely many distinct ℓ_u (u↦u^[E] is injective) contradict FNAM2: some Δ_i≢0 has degree 2a.
- Correct. Note that 𝔊_k=0 for k>a, so the nonzero 𝔊_k has k<=a.

### §3. Theorem 3.4 and (3.2)

- Under not-(𝒦), there is k<D with 𝔊_k≢0.
- The good points off the exceptional sets are distinct zeros of the nonzero section 𝔊_k², so their number is <=deg 𝔊_k².
- 2(2(a−k)+Ek)d=4ad+2k(E−2)d<=4ad+2(D−1)(E−2)d, and deg ψ<=(E+1)d.
- The exceptional sets are as in Lemma 3.1.
- (3.2) is correct.
- Exclusion when the right side is <1551q/4000 is conservative relative to G9 (N_good>1551q/4000+1).

### §3. Cor. 3.5: numerics (r1, exact Fractions)

**The worst corner.** At r=4, Q=128, S=512 (D=4), n=256:
- rest=1490227160815097/10995116277760000≈0.135535370720, **identical** to the owner's value.
- θ_max=0.2497753573.

**Grid.** r∈{4,8,16,32}, Q∈{128,…,4096}, S=Q^jD (j<=2, S>=64), dyadic n∈[256,4Q); 1260 cases.
- D=4: min θ_max=0.249775, at the corner above. The claim θ_max>=0.2497 holds everywhere.
- Minima at n=512,1024,2048,4096,8192: 0.2772, 0.2911, 0.2980, 0.3015, 0.3032 (all at r=4, least Q, S=4Q). These match the note.
- No case has θ_max>=θ_up. The minimum ratio is θ_up/θ_max≈11.83.
- θ_up(S=64)=3.2780 (0.0512·64=3.2768). Correct.

**D-windows (θ_max>0), r=4, least admissible Q.**

| n=h/E | 256 | 512 | 1024 | 2048 | 4096 | 8192 |
|---|---|---|---|---|---|---|
| D with nonempty window | 4–16 | 4–32 | 4–64 | 4–**128** | 4–**256** | 4–**512** |

- The same sets come out over the whole grid. Exactly D<=n/16.
- The note's "D<=64 from 1024E on" is an artefact of the owner grid stopping at D=64. See FIX-5. This understates the result and is not an error.

**Owner scripts.** Re-run from `checks/owner_copy/`; the output is identical.

**Parameter use.** Every term is bounded conservatively:
- N, a by 16h/625 and 8h/625;
- d=E+2;
- the 2/𝔮 term with 𝔮=128;
- 6d_def/q<=0.006.

The monotonicity used in "at every strip scale" (θ_max increases with r, Q, S, n) is confirmed on the grid.

### §4. Prop. 4.1, Prop. 4.2, Example 4.3

**4.1(i).** Expanding in c gives the c_1², c_2² and c_1c_2 coefficients. Correct.

**4.1(ii).**
- For every c, Bc≠0 lies in ker C_c(Z), so every Δ_i vanishes on Γ'. F is irreducible, so F|Δ_i.
- det𝒞_P=0 since 𝒞_Pb_1=0 and b_1≠0.
- Correct.

**4.1(iii).**
- B∈M_2(K^{ρ𝔮}) is regular at generic u, so B(y)=B(u)+O(s^{ρ𝔮}).
- (𝒦) holds identically along the branch.
- Transfer to the own line: R16.2 Step 2 gives z(t)=z+tV+O(t^E) with t a uniformizer (V nonradial at generic u), and e(y(t))=unit·z(t).
- Correct.

**4.1(iv).** 𝒞_P≠0 with det 0 has rank 1 and kernel [b_1]=[T_21:T_11]^ρ. Correct.

**4.2.**
- deg Δ_i=2a<d'=deg F with F|Δ_i, so Δ≡0, contrary to FNAM2.
- 2a=M−1+T−Q−2d', and 2a<d' ⟺ M−1+T−Q<3d'. With d'>=2E−2 a sufficient condition is M<6E−T+Q−5. Checked, 0 violations in 20000 random parameter draws (r1).
- 16·256/625=6.5536.
- *N4.* The remark "gives nothing new" overlooks one edge case. Combining 4.1(iii) and 3.3(b) excludes (𝒦) whenever a+1<=min(ρ𝔮,E). That covers a=E−1 with d'=2E−2 (when E<=ρ𝔮), which Prop. 4.2 misses (there 2a=d'). This is trivial.

**Example 4.3.**
- b_i^⊥·b_i=0 and b_1^⊥·b_2=b_2^⊥·b_1 hold in characteristic 2.
- B corresponds to T_11=(α_1·e(U))^𝔮, T_21=(β_1·e(U))^𝔮.
- The scope statement a>=max(deg p+n_0,d') is correct.
- The owner check was re-run. It is formal only, as labelled.

---

## 4. Fixes (numbered, with locations and proposed corrections)

**FIX-1 (substantive; §0 items 2–3, Prop. 2.2, Cor. 2.3, Prop. 2.4 "In particular", Remark 2.5, §5 items 1–2, §8 rows 3–4). (H_bs) is never satisfied.**

The problem:
- Every proper base point q of f lies on Γ', with mult_q Γ'>=E−3. Proof: mult_q(Z·f(Z)^[E])>=E, and the other components of {C_f=0} have total degree <=2E+1−d'<=3.
- This is confirmed on Fermat σ1 (mult=E−1) and on 8 random centres (r2 g1, g2).

Proposed correction:
1. **Prop. 2.2.** Replace (H_bs) by
   - (H_lift): "there are κ̃'_P, κ̃'_R∈Syz(f^[ρ])_{M'−2X} with P^t≡f^[X]⊗κ̃'_P and R^t≡f^[X]⊗κ̃'_R (mod F)."
   
   State:
   - Steps 1–4 prove only (H_bs)⇒(H_lift), and (H_bs) fails in 𝔇_16.
   - Steps 5–6 and Cor. 2.3 hold verbatim under (H_lift).
   - (H_lift) forces P(q)=R(q)=0 at every proper base point q of f.
   - (H_lift) is OPEN in 𝔇_16.
   - Move the "Without (H_bs)" paragraph forward: it is the actual case.
2. **Prop. 2.4.** Keep (i)–(v) as PROVED (unconditional). Restate "In particular" under (H_lift) for the starting model.
3. **Remark 2.5.**
   - Replace "(PROVED) no argument … can force T to be constant" by:
     - "(PROVED) every global identity listed is invariant under P^t↦P^t+f^[X]⊗η, η∈Syz(f^[ρ])_{M'−2X};
     - (CONDITIONAL on (H_lift) and ρ𝔮<=m) this exchanges a constant twist for a non-constant one, with an identical second layer;
     - (HEURISTIC) hence an argument from these identities alone can force constancy only by excluding all such data."
   - Add the caveat that (H_lift) itself is open and nontrivial.
4. **Summary item 2.** Drop "So no argument … can force T constant", or label it CONDITIONAL/HEURISTIC as above.
5. **Summary item 3.** Replace "(always true when Γ' avoids the base points of f …)" by "(under the polynomial-lift hypothesis (H_lift), which is OPEN: the sufficient condition (H_bs) never holds, since Γ' passes through every proper base point of f)".
6. **§5 item 1.** Likewise.
7. **§8 table.** Change to "Prop. 2.2, Cor. 2.3: PROVED under (H_lift) [(H_bs)⇒(H_lift), but (H_bs) never holds]; Remark 2.5 obstruction: CONDITIONAL/HEURISTIC".

**FIX-2 (Remark 2.5, first sentence).** Delete "and by R16–R18's Γ-local structure", or replace it by "(the Γ-local, good-point conditions — R16.2, Lemma 1.2, FN — are not invariant: they couple the first layer at u)".

**FIX-3 (Lemma 1.1, "Regularity of λ'" and the statement).** Replace "at every good point" by "at every good point off {g=0} (and off Bs(e))". The independence of E_P(u),E_R(u) needs g(u)≠0 (FNAN §1; FIX-N1 of the PRIMARY review).

In Lemma 3.1 / Thm 3.4, add one sentence: "{g=0} (<=3d) is contained in 𝔈 and charged in 1.5d²+3.5d+1, so FIX-N1 is satisfied." No number changes.

**FIX-4 (citations and status: header line 5, §1 line 61, §8 last paragraph).**
- R18 v1 "audit pending" → R18 v2.1 (`HYP_M2_ROUND18_v2_1.md`: audited PASS-with-fixes, revision-checked, fixes applied).
- R17 v2 → R17 v2.1.
- PRIMARY statuses → Claude referee review (CLAUDE_REVIEW_PRIMARY_…_20261007.md): FNAK, TSY, TSYC, FNAM PASS; FNAL, FNAN, FNAO, FNAP PASS-with-fixes (FIX-L1–L4, FIX-N1). Replace "FNAN is DZ-reviewed per FNAO" accordingly.
- Remove "Dependencies whose review is pending: R18 v1 …".

**FIX-5 (§0 item 5 third bullet; Cor. 3.5 "Values" third bullet).**
- Replace "D<=64 for n>=1024" by "exactly D<=n/16 for n=256,…,8192 (D<=128 at 2048, <=256 at 4096, <=512 at 8192); the owner grid stopped at D=64".
- Replace "covered" by "has a nonempty low-height closing window (θ_max>0)". For these D only deg[T]<=θ_max·rh is closed, not the whole case.

**FIX-6 (§0 "What failed" bullet 2; §5 item 5).**
- "costs ≈X·deg[T]=T·deg[T]/2" refers to the half-section 𝔊_k.
- The counted section 𝔊_k² carries Q·deg[T](Q−1+T−D)/(Q−1)≈T·deg[T]=2X·deg[T]. That is what makes θ_max≈0.25.
- State both, so the cost and the window agree.

**FIX-7 (§5 item 3, last sentence).** "So no cover of degree O(D·E·d+X·deg[T]) can come from the own line at z alone" is proved only for the family 𝔊_k (Prop. 4.1(iii)). Restrict it to "no 𝔊_k of that degree is nonzero", or label it HEURISTIC.

---

## 5. Minor notes (optional)

- **N1 (notation clashes).**
  - T denotes both the twist matrix and the integer QS (e.g. "Q·deg[T]·(Q−1+T−D)"); X=T/2 uses the integer.
  - a denotes both deg C_• and the exponent in 𝔮=2^a (§1 bullet 2).
  - D denotes 2^t, c·e(u) (R16/FNAM3) and the Hasse operator.
  - Renaming, e.g. 𝒯 for the twist and t_D or 2^t, is recommended.
- **N2.** Lemma 1.2: handle c_1=0 (s=∞), and add the one-line identification s=s_M(u) via injectivity of W at u (§3 above).
- **N3.** Prop. 2.2 Step 3 does not use (H_bs).
- **N4.** Remark after Prop. 4.2: the edge case a=E−1, d'=2E−2.
- **N5.** Cor. 2.3 gives m·d'<Nd (strictly). Summary item 3 cites "R18 §8.1" where Cor. 2.3 cites "R18 §5": harmonise. The bound is R18 §5's; §8.1 uses it.
- **N6.** Cor. 2.3: "𝔮≈0.1E" holds only as h→4QE. At h=256E, 2m/Q<0.0512E.
- **N7.** Summary item 4: "Each vanishes at every good point" should read "… off the exceptional set of Lemma 3.1".
- **N8.** §5 item 4 "genuinely need D>=4" means that the method needs it. The FNAP D∈{1,2} counterexamples are to the algebraic step only.
- **N9.** Cosmetic slips in scripts:
  - `toy_checks.py` says "Example 4.4" (note: 4.3) and "NOTE_TWIST_CONSTANCY.md" (note: the R18T filename).
  - `numerics_twist.py` says "K-case (Prop 4.3)" (note: 4.2).
- **N10.** Prop. 2.4 Remark: every P' with the same second layer is P+f^[X]⊗η with η∈S³ (ker J^[X,t]=S·f^[X]). So "first-layer change within Syz(f^[ρ])" is exactly "same second layer and same alignment". It is worth stating.

---

## 6. Scope

Everything proved in §§3–4 is conditional on the cited inputs, which are used within their scopes:
- **R18 v2.1:** Thm 4.2(iv), Lemma 5.3 normalisation, §5 degree inputs, §8.1 gonality, Cor. 5.5 (𝔮>=128). They require (Γ),(P), which hold in 𝔇_16.
- **R16:** R16.2 and R16.4 (𝔈), §1 (deg ψ, R14.1).
- **FNAL:** requires global top alignment and common image. Both are in the standing hypotheses.
- **TSY, TSYC, FNAM1–3:** FNAM2 uses G5.
- **FNAN §1, FNAO §2 and FNAP §2:** used pointwise. Lemma 3.2 Step 7 uses only the support argument, over k[t]/(t^{K_0}).

The global-alignment hypothesis is used exactly where FNAL is needed. No result claims anything about the non-global variant: (R4) is correctly listed as open.

**Still OPEN, as the note states:**
- constancy of T;
- (R1) the height window θ_max·rh<deg[T]<=e_M+d;
- (R2) (𝒦) with 2a>=d';
- (R3) D∈{1,2} and D>=4 below the window;
- (R4) the non-global-alignment variant of 𝔇_16, and 𝔇_17.

Add (H_lift) to this list (FIX-1). §6 is correctly labelled HEURISTIC.

## 7. Files

- `checks/r1_numerics.py` → `r1_numerics.out`: Cor. 3.5, θ_up, D-windows, Prop. 4.2 algebra.
- `checks/r2_algebra.py` → `r2_algebra.out`:
  - a, b: Lemma 2.1;
  - c: Lemma 1.2;
  - d: Def. 3.0 iteration and proportionality;
  - e: Lemma 3.2 Step 5, plus the D=2 control;
  - f: exhaustive disjoint support over GF(2)[t]/(t²);
  - g1, g2: (H_bs) fails.
  
  All PASS.
- `checks/owner_copy/`: owner scripts re-run; outputs identical.
- `checks/src_SHA256SUMS.txt`, `checks/checks_SHA256SUMS.txt`.
