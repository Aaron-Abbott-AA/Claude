# AUDIT — HYP M>=2, round 23 (owner v1)

Independent adversarial referee audit of `src/HYP_M2_ROUND23_owner_v1.md`. Date: 7 October 2026.

**Scope and rules followed.**
- I read only files under `src/`, and I wrote only under `checks/` and to this file.
- No file whose name contains "DZ" was opened.
- The source checksums (`checks/src_SHA256SUMS.txt`) verify 24/24, and the owner `SHA256SUMS.txt` verifies 2/2.
- I copied the owner script to `checks/owner_copy/` and re-ran it with `python3 -I` (6.2 s). Its output is **byte-identical** to `src/owner_scripts/numerics_R23.out` (SHA256 9044abc9…edf).
- All my own scripts are independent, exact (Fraction, isqrt, sympy, galois), and run with `python3 -I`, one process at a time. The longest run was 68 s.

---

## §0 Verdict

**PASS-with-fixes.**

I found no mathematical error in any headline result:
- Prop 2.1, including step (ii), the divisibility lift;
- Cor 2.2 and Prop 2.3;
- Thm 3.1;
- Prop 3.2 and Cor 3.3;
- Prop 4.1 and Cor 4.2;
- Lemma 4.3, Prop 4.4 and Cor 4.5.

Every printed bound and threshold was recomputed independently and agrees.

There are two substantive fixes:
- **FIX-1.** A COMPUTED diagnostic claim is false. At r=16, n=256 the miss at 𝔮=4E/Q is about 58 000 values of τ_0, not "a single value". The text of Cor 3.3, "What remains" and §6 next step 2 rest on that misreading.
- **FIX-2.** Cor 3.3 is mis-attributed. Its whole gain already follows from R22 Cor 3.2 (ν_u>=E−X) fed into R20's order step. The bootstrap of Prop 2.1(ii) is not needed for it. This makes Cor 3.3 more robust, but the summary's account of the new input is wrong.

There are also three wording, label and novelty fixes (FIX-3 to FIX-5) and minor notes. No closure has to be withdrawn.

---

## Item table

| item | note's label | referee finding |
|---|---|---|
| Prop 2.1(i) factorisation; order >= min(ν_u, e_u) | PROVED | **Correct.** The pointwise form of R19 Lemma 3.1 is valid at good u. The graph argument is used at a smooth point of Γ' (see A.1). |
| Prop 2.1(ii) ν_u>=E in (𝒦) | PROVED | **Correct.** The divisibility (1.1) holds at every good u and for every admissible 𝔮, constant or not. Any 𝔮>=2 would do; 128 is not needed (toy B). |
| Prop 2.1(iii) ord ε>=X−1 | PROVED | Correct. |
| Cor 2.2 | PROVED | Correct. |
| Prop 2.3 (exact W identity) | PROVED | Correct. Re-derived. |
| Thm 3.1 (F²∤a excluded, any twist) | PROVED; <=0.0925781q COMPUTED | **Correct.** The ψ∉K² device is valid and every exceptional set is charged. The corner value is reproduced exactly, and monotonicity is checked symbolically. |
| Prop 3.2 | PROVED | Correct. It does not need Prop 2.1(ii) for any number in Cor 3.3 (FIX-2). |
| Cor 3.3 (r∈{4,8}, n=256 closed for all 𝔮>=128) | COMPUTED | **Reproduced independently.** 112/112 cases, and the R20 table rows. The diagnostic text is false (FIX-1), and "none rows close only vacuously" is false (FIX-4). |
| Remark 3.4 | PROVED; consequence OPEN | Correct. |
| Prop 4.1 (𝔅_0={𝔡≠0}) | PROVED | Correct. The hypothesis S>=128 is superfluous (N1). |
| Cor 4.2 ((𝒦_ψ)∖(𝒦) closed for every 𝔮; \|𝔅_0\|>0.240046q) | PROVED | Correct. Numbers reproduced. |
| Lemma 4.3 (p-adic orders) | PROVED from CITED SV Cor 1.9 | Correct. The hypotheses of SV hold (A.6). Enumeration reproduced; brute force up to 160 matches the structural list. |
| Prop 4.4 (𝔅_0⊂W(V), weight >=γ) | PROVED (CITED SV Thm 1.5) | Correct. |
| Cor 4.5 ((R1) excluded if Σε_i<=Σ*, Σ*>=0.238γn) | PROVED; Σ* COMPUTED | Correct, with numbers reproduced. "Makes R22 Prop 5.5's (R1) part unconditional" is an overclaim, and two "newly closed" items are not new (FIX-3). |
| Prop 5.1, Cor 5.2 | PROVED (negative) | Prop 5.1 is correct. Cor 5.2's "already excluded" cites the wrong source for its edge case (FIX-5). |
| Remark 5.3 | statement PROVED, use HEURISTIC | Statement re-derived. Correct. |
| COMPUTED (Parts A–D, B2, diagnostics) | COMPUTED | Re-run byte-identical. Independently reproduced, except the diagnostics' interpretation (FIX-1). |

---

## Detailed audit

### A.1 Prop 2.1 — the bootstrap

**Step 1 (factorisation).** This holds for frozen c=c(u). (𝒦) is an identity in K² for each constant c, so 𝒞_c(y)B(y)c=0 near u.
- β(u)=B(u)c≠0 because det T̂(u)≠0, and good points avoid {det T̂=0}.
- In characteristic two, m·β=0 gives m=p·Ωβ with p regular near u.
- Then V_u(z(y))=p(y)·det(B(y)c,c^[Q])=p(y)·c^t𝒜(y)c^[Q] (R19 Lemma 3.0).
- If F | (C_P,C_R), the unreduced 𝒞 is identically zero. The conclusion still holds, with p=0, and the order is >= e_u.

**Step 2 (to ℓ_u).** The graph argument needs Γ' to be smooth at z(u). The note asserts this, inheriting it from R22 §1, without proof. It is true, for the following reason:
- f∘z and the normalisation map Γ̃→Γ agree off z^{-1}(Bs f).
- z(u)∉Bs f, since f(z(u))=g(u)u≠0.
- So z(v)=z(u) forces v↦u in Γ. Γ is smooth at u, so v=u.
- Hence z^{-1}(z(u))={u}, and z is unramified there (non-cuspidal).

So the pitfall "tangent limits at singular branches" does not arise. I suggest adding this sentence (N2).

**Step 3.** By R22 Cor 3.2, ν_u>=E−X=(2r−1)X>=X. Also e_u>=E. So V_u|_{ℓ_u}≡0 (mod t^X). Thm 3.1(ii) then gives (2.1), because Ωb^[X] is a nonzero constant vector. Correct.

**Step 4.** This is correct. If ν_u<e_u, then ord s̃_u=ν_u exactly (R22 Thm 3.1 Step 4, the graph argument at a smooth point). So ord ε=X+ν_u−e_u, and (2.1) forces ord ε>=X−ρ.

**Step 5 (divisibility) — scrutinised as asked.**
- **Source.** R19 Lemma 3.5(i): Ξ(u,·)=c^t𝒜(·)c^[Q]=σ_u^{ρ𝔮}, because the entries of 𝒜 are t̂^{ρ𝔮} and k is perfect.
- **Every good u.** It holds at every good u. If σ_u≡0, then ν_u=∞ and the claim is empty.
- **Non-constant twists.** It holds for non-constant twists; that is precisely the case where ν_u is finite.
- **Admissibility.** 𝔮=128 is admissible because 𝔮_max>=128 and T∈GL_2(K^{𝔮_max})⊂GL_2(K^{128}). This is consistent with the R22 v2.1 𝔮-conventions; Prop 2.1 is not a 𝔮_max statement.
- **The lift.** E=2rρS is a multiple of ρ𝔮 whenever 𝔮 | 2rS. So [E−ρ,E) contains no multiple of ρ𝔮 for any 𝔮>=2.

**Toys** (`toy_prop21.out`, GF(2^8)):
- **Toy A**, a genuinely non-constant twist on the affine line, with c(u) solving the slope equation. In 683/683 cases ν_u is a positive multiple of ρ𝔮; three (ρ,Q,𝔮) settings were tested.
- **Toy B**, (2.1) as a linear system for a'. It is solvable iff ν>=e−ρ, in 8/8 settings.
  - With 𝔮=1 (no divisibility), ν=E−ρ survives.
  - With 𝔮>=2 the only surviving ν<e is ν=E at e=E+1.
  - This is exactly Prop 2.1(ii)–(iii). It also shows that Step 5 is essential, and that it works with any 𝔮>=2.

**Why R22's audit and revision check did not see it.**
- R22 §6 item 3 compared only Thm 3.1(iii)'s bound min(X−ρ,ρ𝔮−1) with R20's m=min(ρ𝔮,E). As a comparison that is correct.
- R22 Remark 5.6 applied Cor 3.2 only to the residual count τ_0−N_0 ("not recomputed").
- R22 FIX-4 then noted that Cor 3.2 already follows from R16.2.
- Nobody fed Cor 3.2 into R20 Lemma 4.2's order step. That step gives m>=E−X for every 𝔮.
- The miss is real, but it is the miss of the *E−X* input, not of the bootstrap (see FIX-2).

**Verdict on Prop 2.1(ii): survives.**

### A.2 Cor 2.2, Prop 2.3, Remark 5.3

All three re-derived:
- **Cor 2.2(iii).** If F²|a, then ord(t^{X−ρ}a'_c)>=X−ρ+e_u>=X, so ε≡0 (mod t^X), which forces ν_u>=e_u.
- **Prop 2.3.** Apply J^{[X],t} to W_u=μ'_uu^[X], and use R18-T Lemma 2.1(ii) and R22 Lemma 2.1(i).
- **Remark 5.3.** In (𝒦)∧F²|a the orders in m are >=X+e_u, >=ρ+X and >=ρ+e_u. So m≡κ_0^Xt^{ρ+X}(s̃/F)Ωb^[X] (mod t^{ρ+e_u}). The f^[X]/ω^[X] comparison (unimodular since f(z)×w≠0) gives μ=t^{X−ρ}a'_c, and P_c^tω^[ρ]=O(t^{2e_u−X}). Correct.

### A.3 Thm 3.1

**The ψ∉K² device.**
- At a good u, 𝔞(u)=(√β̃A+√α̃B')²(u)∝a'_{c(u)}(z(u))²=0, by Cor 2.2(i), since ρ−1>=1.
- If 𝔞≡0, then A²=ψB'² in K, so B'=0, then A=0. Hence F|a'_P and F|a'_R, i.e. F²|a. Correct.

**Pitfalls.**
- A and B' are pulled back by the morphism z, and deg 𝔞=deg ψ+2m_ad'.
- {λ'=0}, {det T̂=0}, 𝔈 (which contains {g=0}) and the boundary (which contains Bs(e)) are all charged.
- No step evaluates at a base point of f.
- Points with σ_u≡0 need no charge, since ν_u=∞ there.

**Numerics** (`indep_numerics.out` A).
- The corner value is exactly 101790647887837/1099511627776000≈0.0925781<1551/4000.
- Monotonicity was checked with sympy. The partial derivatives of the upper bound in E, n and ρ have numerators −6144Enρ−32En−500625Eρ−1842500ρ, −160E²−801E−1474 and −E−2, all negative.
- The grid maximum of the exact d'-maximised bound is 0.0826303 at (64,16384,64,32768), as printed.

**Verdict: survives.**

### A.4 Prop 3.2 and Cor 3.3 — independent recount

I wrote `indep_recount_R20_R23.py` from the formulas of R19 (4.1) (N4 form, R20 Prop 5.2) and R20 (4.1′), not from the owner's code.
- For each τ_0-interval it computes the **exact failing integer set**: the concave quadratic for N4 is solved by isqrt bracketing with exact verification at the boundary integers; (4.1′) is affine.
- It agrees with direct evaluation of the bounds in **6164/6164** sampled (case, τ_0) pairs, with 0 mismatches (`direct_eval_crosscheck.out`).

**Mode R20** reproduces every finite entry of the R20 v2.1 table, on the grid r∈{4,8,16}, Q∈{128,…,16384} *including Q=8192*, S∈{64,256}, n<=8192 (198 rows):
- 2E/Q for r∈{4,8} at n=256;
- 32E/Q at n=512;
- nE/(16Q) for r=4 at n>=1024;
- 64E/Q for r=8 at n=1024;
- 8E/Q for r=16 at n=256.

**Mode R23** (m=E, N_1=⌈E/(ρ𝔮)⌉):
- r∈{4,8}, n=256: every 𝔮>=128 closes, on all grid rows and on 112/112 B2 cases (`indep_recount_part2.out`).
- All other rows are unchanged.
- r=16, n=256 stays at 8E/Q.

**Cor 3.3 survives.**

The validity of Prop 3.2(i)–(iii) was checked against R20 Lemma 4.1/4.2, Thm 5.1 and R19 Lemma 3.5(iii):
- ν_u depends only on (twist, c(u)), so Prop 2.1 applied to the unreduced pencil feeds R20's reduced-pencil (1.1).
- With m=E, D_1=d'−a.
- The factor d'−E−τ_0+N_1 is correct.

### A.5 Prop 4.1 and Cor 4.2

**Off 𝔅_0.** R22 Lemma 5.1(b) with any admissible 𝔮<=S gives δ_u>=1. Thm 3.1(iii) then gives V_u(z(u))=0, i.e. 𝔡(u)=0.

**On 𝔅_0.**
- ν_u=E−X<E=e_u, so ord s̃_u=E−X and ε(0)=λ_u≠0.
- Thm 3.1(ii) at t=0 gives V_u(z(u))=(gD)^{X−ρ}κ_0^Xλ_uΩc^[T] with Ωc^[T]=(α^X,β^X). This is formula (4.1).
- The point with e_u=E+1 and ν_u=E−X cannot occur (Thm 3.1(i)).

**Cor 4.2(i).** If 𝔡≡0, Prop 4.1 gives 𝔅_0=∅. Then R22 Lemma 5.1(b) with 𝔮_max, Lemma 5.2 and the Thm 5.3(ii) count apply. This is exactly R22 Cor 5.4's second clause with |𝔅_0|=0.

**Cor 4.2(ii).** 1551/4000−32480243592761/219902325555200=0.2400469527>0.240046. I recomputed R22's Thm 5.3(i) corner fraction exactly.

**Verdict: Cor 4.2 survives.**

### A.6 Lemma 4.3, Prop 4.4 and Cor 4.5

**Hypotheses of Stöhr–Voloch.** V=span(t̂_ij) is a base-point-free subsystem of H⁰(𝓣) on the smooth irreducible curve Γ̃. It defines a nondegenerate morphism to P(V^*). That is all SV Thm 1.5 and Cor 1.9 (the p-adic criterion for the generic order sequence) require.
- Via Lucas, the criterion becomes closure of the orders under binary sub-integers.
- ε_1=1 follows from separability at 𝔮_max, as in R22 Prop 5.5. This uses the 𝔮_max convention correctly.

**Lemma 4.3 (i)–(iv)** re-proved by hand.
- Brute force over *all* integers <=160 (no popcount pre-filter) gives exactly the structural list: powers of 2, plus ε_3=ε_1+ε_2. That is 119 sequences.
- With the cap 2^12 there are 443 sequences, as the note says.
- No sequence contains (2r−1)2^k, for r∈{4,…,128} and k<=11.
- There are no γ violations, and no violations of Σ<=2ε_top.

**Prop 4.4.** For u∈𝔅_0, σ_u (for 𝔮_max) is a nonzero member of V of order exactly N_0, so N_0 is some j_{i_0}(u). Then:
- j(u)≠ε, because N_0 is not an order;
- ε_{i_0}<=N_0 and ε_{i_0}≠N_0, so ε_{i_0}<=N_0−γ;
- v_u(R_V)>=γ.

Correct.

**Cor 4.5.** Recomputed:
- 0.238(1+2^{-15})+1.25·10^{-5}/2=0.2380135<0.2380137<0.240046;
- Σ* on a grid (r<=32, Q, S>=128, all n, 𝔮_max<=S): minimum Σ*/n=0.4765625 (Σ*=122, γ=2), with 0 violations of Σ*>=0.238γn;
- the inequality for the ε_top<N_0 case checks.

**Verdict.** Cor 4.5's mathematics survives, but "unconditional" is an overclaim (FIX-3).

---

## FIXES

### Substantive

**FIX-1 (false COMPUTED claim: r=16, n=256 "misses by a single τ_0").**

*Where.* §0 "What failed/what remains" ("at 𝔮=4E/Q … miss by a single value of τ_0"), Cor 3.3 bullet 3, §6 next step 2 ("a single τ_0 value. A small per-point gain would close that 𝔮"), and the §7 diagnostics row.

*What is actually true* (`indep_recount_part2.out`, `direct_eval_crosscheck.out`). At Q=128, S=64, 𝔮=4096, d'=2E−2:
- N4 holds only for τ_0<=5472;
- (4.1′) holds only from 63626;
- **both fail on τ_0∈[5473,63625]**, about 58 000 values. For example, at τ_0=30000, N4/q=0.4102 and (4.1′)/q=0.4804, against 0.38775.

At d'=2E+4 the failing set is [5501,63607].

The note's phrase "at 𝔮=128: N4 up to 131085" is also wrong:
- 131085 is the end of N4's *domain* (τ_0<=d'−E+N_1−1);
- N4 actually holds only up to τ_0=1527;
- the failing set is [1528,2036040].

*Cause.* The owner script's `case_closed` reports only the test points (endpoints and vertex) that fail, not the failing set. The note read "fails at τ0 in [63625]" as a one-value gap.

*Fix.* Replace the text with the failing intervals above. Delete "a small per-point gain would close that 𝔮". The r=16 threshold stays 8E/Q, so no closure is affected.

**FIX-2 (attribution: Cor 3.3 does not use the bootstrap).**

`indep_recount_R20_R23.out` (mode "R22only") and `variant_modes.out` show the following:
- Take only R22 Cor 3.2 (ν_u>=E−X, PROVED in R22 and derivable from R16.2) and insert it into R20 Lemma 4.2's order step, through the (𝒦) normal form (1.1).
- This gives m=min(ν_min,E)>=E−X.
- It reproduces **exactly** the same closures as the note's "R23" mode: all 198 rows and 112/112 B2 cases. This holds even with N_1=1 (mode `m_only_EX`).
- The residual-count improvement N_1 alone (mode `N1_only_N0`) gives nothing.

So:
- (a) The summary's "This bootstrap is the main new input", and the Remark "What R22 §6 item 3 missed … the bootstrap raises this to m>=E", should say that the (R2) gain of Cor 3.3 comes from feeding R22 Cor 3.2 into R20's m. R22 Remark 5.6 applied Cor 3.2 only to the residual count and did not recompute. The bootstrap Prop 2.1(ii) is what Thm 3.1, through Cor 2.2(i), needs; Cor 3.3 does not need it.
- (b) State Prop 3.2 with the weaker dependency (m>=E−X suffices for every Cor 3.3 number). Cor 3.3 then rests only on audited inputs.
- (c) The bootstrap does have one use outside Thm 3.1. At a=E−1 it gives m=E>a, which settles Cor 5.2's edge case (FIX-5).

### Wording, label and novelty

**FIX-3 (overclaim: "makes R22 Prop 5.5's (R1) part unconditional"; "newly closed" list).**

R22 Prop 5.5 is labelled CONDITIONAL on ε_top(V)<N_0, a hypothesis on V. Cor 4.5 does not remove that hypothesis. The accurate statement is: "in (R1), every V with ε_top<N_0 is excluded, with no count hypothesis. Lemma 4.3(iii) makes the weight N_0−ε_top>=γ>=2 uniform."

The "removal of the 𝔮_max<(2r−1)S/3 restriction" is vacuous in (R1):
- if 𝔮_max>S, R22 Thm 5.3 applies;
- if 𝔮_max<=S, then N_0>=7.

The closures of (R1) for classical V and for dim V=2 were already in R22 (Prop 5.5 classical/pencil cases plus Thm 5.3). Remove "for every classical V" from the §0 "Newly closed" list, or mark it "(already R22)".

Optional observation: the same Lemma 4.3(iii) weight makes R22 Prop 5.5's count automatic for ε_top<N_0 in (R2) as well.

**FIX-4 ("none" rows do not close only vacuously).**

Cor 3.3's self-check says that in the R20 "none" rows (r=8 with n>=2048, r=16 with n>=512) "the only closed 𝔮 are those with τ_hi<1". That is false. At the least closing 𝔮, τ_hi>=1; for example:

| (r, n, Q, S) | least closing 𝔮 | τ_hi there |
|---|---|---|
| (16, 512, 256, 64) | 2^31 | 2 |
| (8, 2048, 1024, 64) | 2^31 | 12 |
| (8, 8192, 16384, 64) | 2^38 | 6 |

These are genuine (if extreme) closures. The owner's own output prints finite thresholds there, because its `qq_vac` tests only the a-priori τ bound. No claim of the note depends on this. Reword it to: "only at 𝔮 so large that τ_0<=τ_hi is O(1)–O(10)".

**FIX-5 (Cor 5.2 edge case: wrong citation).**

"a=E−1, d'=2E−2 … already excluded" cites R18-T's N4 remark. That remark is stated for D>=4 and needs E<=ρ𝔮. For non-constant twists with ρ𝔮<E it does not apply.

The edge case *is* excluded, but by this note's Prop 3.2(i) together with R20 Lemma 4.3:
- with m=E>a, every good non-cuspidal u lies in 𝔅;
- |𝔅|<=B_𝔅=O(E²)≪q.

Cite that instead. This is a use of the bootstrap, since m=E−X would not suffice.

---

## Minor notes

- **N1.** Prop 4.1's hypothesis S>=128 is superfluous. For S=64, 𝔮_max>S, so R22 Lemma 5.1(a) gives ν_u>=E. Then 𝔅_0=∅ and 𝔡≡0 on good points, and the equivalence holds trivially. Likewise Step 5 of Prop 2.1 works with any admissible 𝔮>=2 (toy B), so "take 𝔮=128" is a choice, not a need.
- **N2.** Add the one-line justification that Γ' is smooth at z(u) for good u: z^{-1}(z(u))={u}, because f∘z equals the normalisation map off z^{-1}Bs(f) and z(u)∉Bs(f). It is used in Prop 2.1 Step 2 and in Cor 2.2(ii).
- **N3.** §3 "Residual of (R2)": write N_1=2rS/𝔮_max. Prop 5.5 must be applied with 𝔮_max (R22 v2.1 RC-1). If 𝔮_max>2rS, then N_1=1 and the condition is void.
- **N4.** "Frobenius non-classical" (§0 item 9 and Cor 4.5 residual; inherited from R22) is the wrong term. In Stöhr–Voloch that refers to the Frobenius order sequence. For the order sequence ε_i of V the correct term is "non-classical".
- **N5.** §7 Part B says "162 (r,n,Q,S) rows". The referee grid adds Q=8192 (36 more rows), and every one agrees.
- **N6.** The caveat in §7 says no toy was built. The referee toys A and B (`toy_prop21.py`) cover (1.1) for a non-constant twist and the congruence (2.1) with the divisibility lift. They check the mechanism, not an original model.

---

## checks/ files

| file | content |
|---|---|
| `src_SHA256SUMS.txt` | provided; verifies 24/24 source files |
| `owner_copy/numerics_R23.py`, `owner_copy/numerics_R23.rerun.out` | owner script, re-run; output byte-identical to `src/owner_scripts/numerics_R23.out` |
| `indep_recount_R20_R23.py` → `.out` | independent exact re-implementation of R20 Cor 5.3 / R23 Cor 3.3, modes R20, R23 and R22only, on 198 rows |
| `indep_recount_part2.py` → `.out` | B2 112/112 (R23 and R22only); r=16 failing sets; vacuity test of the "none" rows |
| `direct_eval_crosscheck.py` → `.out` | direct bound evaluation at sample τ_0 (FIX-1); solver against direct evaluation, 6164/6164 |
| `variant_modes.py` → `.out` | which ingredient drives Cor 3.3 (FIX-2) |
| `indep_numerics.py` → `.out` | Thm 3.1 corner, symbolic monotonicity and grid; Lemma 4.3 brute force and enumeration; Cor 4.2 and Cor 4.5 numbers |
| `toy_prop21.py` → `.out` | toy A ((1.1), non-constant twist, GF(2^8), 683/683); toy B ((2.1) and the divisibility lift) |
| `checks_SHA256SUMS.txt` | SHA256 of all the above |
