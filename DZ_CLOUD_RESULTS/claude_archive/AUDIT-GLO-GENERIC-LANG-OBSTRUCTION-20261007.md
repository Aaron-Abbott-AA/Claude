# AUDIT — GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007.md (independent referee, cloud session, 7 Oct 2026, 21:47–22:05Z)

Referee: a fresh, isolated, adversarial subagent for the DZ line (project "Wan's numbers of PPs"). It had no contact with the owner session or with Codex, and it read no files outside the DZ scope (§6).

**Note audited:** `src/GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007.md` (owner note v1, 21:41Z), sha256 `3a8a7dbb7d1d1c9cddbe73d41f9204ff09edfe55eaf6ac5e2f7c8bb331136cf2`. The copy in `claude_archive/` has the same sha256.

**Owner scripts:** `glocheck.py` and `glovo.py`. Their sha256 values match the note's §9 table, and the copies in `src/owner_scripts/` and `claude_archive/scripts/` are identical. The referee copied them to `checks/owner_copy/` and reran them there with `nice -n 19 python3 -I`:
- `glocheck.py 1`, `glocheck.py 7` and `glovo.py` reproduce the owner logs byte for byte;
- the seed-1 run takes 1.2 s.

**Labels** follow the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN] open problem. Anything the referee proves is marked [P, referee].

## 0. Verdict: **PASS-with-fixes**

**Every [P] statement in the note is correct as a mathematical statement.** The referee checked each proof step by hand:
- FS (a), (b);
- GR and Corollary AC;
- Theorem OB and Lemma TB, including the index bookkeeping and why n ≥ a₂−1 is needed;
- Theorem RLE, including uniqueness;
- Lemma RD and Corollary N1;
- Corollary OB1 (a), (b), (c), including the squaring step, the case split on Δ, and "Δ = 0 ⇒ Ω₁ ≠ 0";
- Proposition PV;
- the Hermitian remark;
- Proposition TH, including the degree count and homogeneity of degree 4Q+4;
- Proposition VO: the Newton polygon, ties, θ < 0, zero coefficients and r_k = 0 all work;
- Corollary DO;
- Example NG: Sol = 0 over L̄, a(W) = 1 and uniqueness of the relation, for m ≥ 4.

The referee's own code found 0 failures (§5):
- exhaustive OB/TB/OB1 checks with a₂ ≤ 3 and n ≤ 3, in fields with and without F_{Q²}, over 404 instances with a balanced mix of positive and negative cases;
- an exact test of OB1 over the algebraic closure, 3101 instances, including all 2401 cases with Q = 8 over F₈;
- PV exhaustively for Q = 4 and Q = 8;
- a symbolic check of the OB1(c) algebra for general Q;
- a check of AC tower collapse in a finite-field model, 162 solvable instances (the test also separates the unsolvable ones);
- a non-triggering test of VO on 22 planted solvable families over F₂(X), at 184 places;
- agreement of DO and VO on 89 random pairs;
- NG and the RLE controls.

**Two claims overreach and must be restated before any packet. No proof needs to change.**
- **FIX-1 (scope of Example NG).**
  - NG's W is the *full* root space R_P = ker P, of dimension m/2 + a₂ = m/2 + 1.
  - In the band, dim W = ρ ≤ (m−6)/3 < m/2. So W is a proper G-stable subspace of R_P, of codimension ≥ ρ/2 + 3 + a₂.
  - NG's specialisations are of real type only at α = 1. This is incompatible with the arc's real-type specialisation at more than q/2 nonfoci (TH with δ = 1).
  - So NG shows only that (C, D), PTH's tests and "dim W > 2a₂" with W = R_P do not imply GLS₀.
  - It does **not** show that the generic relation on a G-stable W with 2a₂ < dim W ≤ (m−6)/3 fails to imply GLS₀. That question is [OPEN].
  - The following claims therefore overstate what is proved: the title's "So GLS₀ is not a consequence of the generic relation", §5's "message", and §6(a)'s "arc input … is now **necessary**".
- **FIX-2 ("exactly computable" / "finite obstruction").**
  - Theorem OB decides Sol_{≤n} for each fixed n. No bound on the degree of a minimal solution is proved, and none is evident: the minimal B in RLE (ii) has unconstrained degree a priori.
  - So "GLS₀ ⟺ ∃n: ker Ob_n ≠ 0" is a semi-decision. Failure is certified only by tools such as VO, or by a layer leaving L(α₀) (Corollary AC).
  - §6(a)'s "Its obstruction is exactly computable" and the title's "classified exactly by a finite obstruction map" must say this.

**FIX count: 2 substantive, 12 minor (m1–m12).** Owner revision is required: wording and scope only. A diff check is enough after that; a full re-audit is not needed.

## 1. Item table

| # | Item | Claimed label | Referee finding | Status |
|---|---|---|---|---|
| 1 | Title / abstract | — | "Not a consequence of the generic relation" overreaches (FIX-1). "Classified exactly by a finite obstruction map" needs the per-n qualifier (FIX-2). | FIX-1, FIX-2 |
| 2 | §0 setting: Λ, φ an injective endomorphism, right F_Q{{τ}}-linearity | [P] | Correct. φ(AB) = φ(A)φ(B) coefficientwise, and φ(E) = E on F_Q{{τ}}. | PASS |
| 3 | R0, [P] part (deg C ≠ deg D, or exactly one of c₀, d₀ zero ⇒ Sol = 0) | [P] | Correct by PTH v2.2 ML. ML is stated for K = F_q or L^sep, but its proof is valid over L̄, and FS(b) also reduces to L^sep. | PASS; m12 |
| 4 | R0, [COND] part ((N0) for the arc relation) | [COND (B1a⁺), (B1b), HFD §1 [A]] | Logic correct. "Plentiful" is asserted without its one-line reason. Not used by any [P] statement, as the note says. | PASS; m7 |
| 5 | Lemma FS (a), (b) | [P] | Correct: ℓ₀ is separable (derivative c₀), its kernel is α₀F_Q, there is a recursive construction, completeness follows from the τ^k-equation of B, and the least-index argument gives uniqueness. (b) needs only (N0). It does strengthen PTH §4A(iv). | PASS |
| 6 | Prop. GR | [P] | Correct. g fixes F_Q ⊂ L, so g(A₀E_h) = g(A₀)E_h. The constant-term map is multiplicative. Conjugation under change of A₀ is right. | PASS |
| 7 | Cor. AC (tower collapse) | [P] | Correct. Under GLS₀, ker ρ₀ = ker χ (the constant term of Uχ(g)U^{−1} is χ(g)), so L_∞ = L(α₀). This does not depend on the choice of A₀. [C, referee] `glo_ac`: 162/162 solvable instances collapse; 67/78 unsolvable ones leave L(α₀). | PASS |
| 8 | Thm. OB (bijection ker Ob_n → Sol_{≤n}; F_Q-compatibility; dim bound; GLS₀ ⟺ ∃n) | [P] | Correct. Ob_n is F₂-linear; Λ(T)_k depends on t_{≤k}; (A₀E)_{≤n} depends on E_{≤n}. [C, referee] `glo_ob`: the set {(A₀E)_{≤n} : E ∈ ker Ob_n} equals the exhaustive Sol_{≤n} in 404/404 instances. "Exact" is per n only. | PASS; FIX-2 |
| 9 | Lemma TB (Ob_n = λ∘top_n for n ≥ a₂−1; triangular; \|ker λ\| = Q^{a₂}) | [P] | Correct. The index substitution j = a₂+k−i reproduces the formula exactly, and n ≥ a₂−1 is exactly the condition that all indices are ≥ 0. [C, referee] `glo_ob`: 15 728 (E, instance) identity checks over both seeds, 0 failures. "Truncated formal solution at ∞" is informal. | PASS; m5 |
| 10 | Thm. RLE ((i) ⟺ (ii); uniqueness of minimal B; minimal A = B a₀ζ) | [P] | Correct. b_k = a_k/a₀^{2^k} is G-fixed; A = B·a₀; cancellation of the unit a₀; minimal degrees of (i) and (ii) coincide, so uniqueness follows from ML. [C, referee] `glo_vo` (1): 22 planted twisted families over F₂(X), with y₀ = y recovered and (ii) re-verified. | PASS |
| 11 | Lemma RD (affine L-root set is ∅, a point, or a Q-coset) | [P] | Correct. However, "coset of size Q **iff** y₀^{2^k−1} ∈ L^{*(Q−1)}" is true only for a *nonempty* root set. | PASS; m3 |
| 12 | Cor. N1 | [P] | Correct: k = 1 equation divided by c₀ = d₀y₀ gives (c₁ + y₀²d₁)/c₀ = Δ₁/(c₀d₀²). [C, referee]: b₁ of every planted family satisfies N1. | PASS |
| 13 | §3 [C] glovo (TX-like RLE, negative control) | [C] | The positive part reproduces. The negative control is attributed to `glovo.py` in §3, but §9 says it ran "ad hoc in scratch", and it is not in the script. The referee reproduced it in `glo_vo` (4) as [True, False, False]. | m10 |
| 14 | Cor. OB1(a) (span criterion) | [P] | Correct. The (⇒) direction correctly handles solutions of degree < n via V_d ⊂ V_n. [C, referee] `glo_ob`: a₂ = 1, n ≤ 2, 0 mismatches. | PASS |
| 15 | Cor. OB1(b) (n = 0 ⟺ Δ = 0) | [P] | Correct. [C, referee] `glo_ob1_closure`: exact over F̄ in 3101 instances. | PASS |
| 16 | Cor. OB1(c) (GLS₁ ⟺ Δ·Ω₁ = 0) | [P] | Correct, re-derived by hand. [C, referee] symbolic check for general Q (`glo_pv_alg` (b)). Exact test over the algebraic closure, 3101 instances: 0 mismatches, 447 of them on the Δ ≠ 0 = Ω₁ branch. The phrase "a Kummer condition in L" is a misnomer; it is an explicit identity. | PASS; m4 |
| 17 | Prop. PV | [P] | Correct: δ′^Q = κ^Qδ′ uses x^q = x, then Δ^{Q−1} = κ^{2Q−1}, then κ^{4Q}/κ^{3Q−1} = κ^{Q+1} = 1. [C, referee]: exhaustive for Q = 4 (1280 cases) and Q = 8 (36 864), plus 25 000 samples for Q = 16, 32; 0 failures. | PASS |
| 18 | Hermitian remark; "no generic analogue over L" | [P]/[A]/[H] | The Hermitian facts are correct (Tr_{F_q/F_Q} is onto with fibres of size Q; the curve is irreducible of genus Q(Q−1)/2). The sentence "It has no generic analogue over L" carries no label. | PASS; m8 |
| 19 | Prop. TH (deg Δ·Ω₁ ≤ (4Q+4)δ; at most that many real-type α) | [P] (+[H] scale) | Correct: degrees 3δ + (4Q+1)δ, homogeneity of degree 4Q+4, evaluation commutes. [C, referee]: worst ratio 1.000 (the bound is attained). The threshold should be stated with v (the number of α where the specialisation is of real type). Real type is guaranteed only where a(V_α) = a₂. | PASS; m9 |
| 20 | Prop. VO | [P] | Correct. The induction is valid for any sign of θ (2^i, Q2^i > 0). The Newton polygon gives one root of value v(r_k) − v(c₀) ≥ θ and Q−1 roots of value θ; r_k = 0 and ties are harmless. The top equation gives v(a_n) = θ_top. [C, referee]: no trigger on solvable families (hypothesis (ii) held at 84 of 184 places, so the test is not vacuous). | PASS |
| 21 | Cor. DO | [P] | A correct transcription of VO at v_∞ (`glo_vo` (2): 89/89 agree). The hypothesis deg d₀ > deg c₀ is unnecessary. | PASS; m6 |
| 22 | Example NG: (N0), PTH tests, VO at ∞ ⇒ Sol = 0 over L̄ | [P] | Correct: θ = 1/(Q−1) > θ_top = 0. Consistent with OB1: Δ = X²+1 and Δ·Ω₁ ≢ 0 (`glo_vo` (3)). | PASS |
| 23 | Example NG: a(W) = 1, uniqueness, "any even m" | [P] | Correct for **m ≥ 4**. For m = 2, dim W = 2 = 2a₂ and the τ-degree ranges [0,1] and [m/2, m/2+1] overlap. Also: "has dimension m/2" should be "≤ m/2"; generic a(W) is not defined; G-stability of W is not stated. | PASS; m1, m2 |
| 24 | NG "Scope" / message; §6(a) "necessary, not just likely" | [P] claimed | Overreach: NG has W = R_P, with dim = m/2 + 1, whereas the band has ρ ≤ (m−6)/3; NG is also real type at only one α. | **FIX-1** |
| 25 | §6(a) "obstruction is exactly computable" | [P] claimed | No degree bound, so only a semi-decision. | **FIX-2** |
| 26 | §6(b)–(f), §7 | [P]/[OPEN] | Correct. N1, AC, ¬VO and Δ·Ω₁ ≡ 0 are genuine necessary conditions. §7(a)'s "GO/GX route closed for that family if VO triggers" is right, because GO/GX are [COND] on GLS₀/GLS₁. | PASS |
| 27 | §2/§4 [C] glocheck T1/T2/T3; §9 hashes | [C] | Hashes verified; reruns identical. T1 is planted 50/50 as claimed. T3's "half with a planted solution" is not recorded by the script; the logs show 29/32 and 30/32 positives (only 5 negatives in total), caused by selection bias. | m11 |

## 2. Detailed audit

### 2.1 §0, R0
- **Algebra.** Λ(A)_k = Σ_i(c_i a_{k−i}^{2^i} + d_i a_{k−i}^{Q2^i}) is the coefficient of C·A + D·φ(A). φ is multiplicative: (AB)_k^Q = Σ a_i^Q b_j^{Q2^i}. Right linearity uses only φ(E) = E. All correct.
- **R0 [P].** This is ML's contrapositive. PTH v2.2 states ML for K ∈ {F_q, L^sep}; the proof is field-independent. This is cosmetic (m12).
- **R0 [COND].** The specialisation of (C, D) at a nonfocus α with a(V_α) = a₂ is a relation of W(α) of degree ≤ a₂. By HFD §1 [A] it is a nonzero multiple of (C′, κC̄′) with c′₀c′_{a₂} ≠ 0. Hence c₀(α), d₀(α), c_{a₂}(α), d_{a₂}(α) are all nonzero, and so are the generic coefficients.
- **R0, missing justifications (m7).**
  - Why such α are plentiful: a nonzero degree-(a₂−1) Moore determinant has degree below the input-step bound, which is < v, so a(V_α) = a₂ off its zero set.
  - After content removal, (C_α, D_α) ≠ 0 at every α automatically.
  - a(·) is invariant under the Frobenius twist of (B1b).

### 2.2 §1 FS, GR, AC
- **FS.** The τ^k-equation is ℓ₀(a_k) = r_k(a_{<k}). ℓ₀ is separable because c₀ ≠ 0, and ker ℓ₀ = α₀F_Q with α₀^{Q−1} = y₀; μ_{Q−1} = F_Q^* ⊂ L.
  - Completeness: if B ≡ 0 mod τ^k, the τ^k-equation of B is ℓ₀(b_k) = 0, and (A₀e_kτ^k)_k = α₀e_k.
  - Uniqueness: least index.
  - (b) follows because the coefficients of A₀E are polynomials in α_j and e_i ∈ F_Q ⊂ L.
  - Correct.
- **GR.** g(A₀) is a formal solution with nonzero constant term, so g(A₀) = A₀E_g with E_g a unit. Then gh(A₀) = g(A₀)E_h, since g fixes E_h ∈ F_Q{{τ}}. Correct.
- **AC.** With a minimal polynomial solution A = A₀U (u₀ = a₀/α₀ ≠ 0), the injectivity of E ↦ A₀E gives E_gU = Uχ(g).
  - The constant term is multiplicative, so ker ρ₀ = ker χ, and χ = χ₀ is the Kummer character of α₀.
  - So the fixer of L_∞ equals the fixer of L(α₀). Correct.
- **Referee remark [P, referee].** AC gives finite **certificates of failure**: if some layer α_k (for any choice) lies outside L(α₀), then GLS₀ fails. This complements FIX-2.

### 2.3 §2 OB, TB
- **OB step 1.** For k ≤ n, Λ((A₀E)_{≤n})_k = Λ(A₀E)_k = (Λ(A₀)E)_k = 0. For k > n+a₂ it vanishes by degree.
- **Surjectivity.** (A₀E_∞)_{≤n} depends only on (E_∞)_{≤n}.
- **Injectivity.** Least index.
- **F_Q-compatibility.** Ob_n(Eζ)_k = Ob_n(E)_k ζ^{2^k}.
- **TB.** With t_j ↔ t_{n−a₂+j}, Λ(T)_{n+k} = Σ_{i=k}^{a₂} c_i t_{n+k−i}^{2^i} + … becomes Σ_{j=k}^{a₂} c_{a₂+k−j} t_j^{2^{a₂+k−j}} + …, as stated.
  - Indices stay ≥ 0 iff n+1−a₂ ≥ 0.
  - Each triangular step is c_{a₂}s + d_{a₂}s^Q = r with s = t^{2^{a₂}}. This has Q roots s, separable because c_{a₂} ≠ 0, and the 2^{a₂}-th root is unique over the perfect field L̄. So |ker λ| = Q^{a₂}.
- **Caveat.** "Exact" holds per n, but nothing bounds n (FIX-2).

### 2.4 §3 RLE, RD, N1
- **RLE.** All steps verified (see item 10). The equivalence needs y₀ = c₀/d₀ only through a₀^{Q−1} = y₀, which the τ⁰-equation forces.
- **RD.** Subtract two roots: y₀^{2^k−1}b^Q + b = 0, so b = 0 or b^{Q−1} = y₀^{−(2^k−1)}. The nonzero solutions in L are ∅ or a μ_{Q−1}-coset. The "iff" needs "nonempty" (m3).
- **N1.** Verified symbolically by hand and on planted families.

### 2.5 §4 OB1, PV, TH
- **OB1(c).** With α₁ = α₀β, the τ¹-equation gives β^Q + β = s = α₀Δ/(c₀d₀²). This used d₀α₀^Q = c₀α₀ and α₀^{2Q} = α₀²y₀² (checked numerically in GF(2⁹), 300/300).
  - w² = c₁d₀²/(d₁c₀²) and (w+1)² = Δ/(d₁c₀²).
  - If Δ ≠ 0: w ≠ 1, so γ ∉ F_Q. Then γ ∈ F_Q + βF_Q ⟺ ℘(γ) ∈ sF_Q^*, because ℘ is F_Q-linear with kernel F_Q. And ℘(γ) = γ(w+1).
  - Raising to the power Q−1 and squaring (both injective here) gives the stated identity. The symbolic check confirms log-equality for general Q.
  - If Δ = 0, then Ω₁ = c₁d₀^{4Q} ≠ 0 because Q−1 ≥ 1.
- **The closure test** (`glo_ob1_closure`) is fully independent of the derivation.
  - The τ⁰- and τ²-equations force a₀ ∈ {0} ∪ r₀F_Q^* and a₁ ∈ {0} ∪ r₁F_Q^*. All Kummer roots lie in the chosen big field: GF(2¹⁸), GF(2¹²) and GF(2²¹) for the three bases.
  - So enumerating these candidates decides existence over F̄ exactly. There were 0 mismatches against Δ·Ω₁ = 0 and Δ = 0.
- **PV.** See item 17.
  - The statement does not need (N0).
  - PV is consistent with LS (PTH §1): pointwise solvability is known independently.
- **TH.** The statement is correct.
  - "Counting yields GLS₁ only when δ < q/(4Q+4)" is a correct upper bound for this argument, since there are at most q values α.
  - The guaranteed count is v′ := #{α ∈ N : a(V_α) = a₂, specialisation nonzero}. That gives δ < v′/(4Q+4), and v′ ≤ v.
  - Real type at α is guaranteed by HFD §1 only when a(V_α) = a₂ (m9).
  - The [H] scale u·3(Q+1) = (3/4)R(Q+1) and the factor 3R are arithmetically right.

### 2.6 §5 VO, DO, NG
- **VO.** See item 20. The hypotheses are exactly what the induction v(r_k) ≥ v(c₀)+θ needs. The base case k = 0 is the r = 0 Newton polygon.
- **DO.** This is VO at v_∞ = −deg. The extra hypothesis deg d₀ > deg c₀ (θ > 0) is never used (m6).
- **NG, VO.** θ = (0−(−1))/(Q−1) = 1/(Q−1). Hypothesis (ii): v(c₁) + 2θ = 2/(Q−1) ≥ 1/(Q−1), and v(d₁) + 2Qθ ≥ 1/(Q−1). θ_top = 0. So Sol = 0 over L̄ in every degree. Correct.
- **NG, ker P.** P = 1 + τ + Xτ^{m/2} + τ^{m/2+1} is separable (constant term 1). W = ker P has F₂-dimension m/2+1 and is G-stable.
- **NG, no degree-0 relation.** Such a relation would put W inside a kernel of dimension ≤ m/2.
- **NG, uniqueness.** Right division by P, plus |W| = 2^{m/2+1} > 2^{deg R}, gives P′ = eP. Since deg C′, D′ ≤ 1 < m/2, the decomposition P′ = C′ + D′τ^{m/2} is unique, so (C′, D′) = e(C, D). This needs m ≥ 4 (m1).
- **NG, pointwise behaviour.** (1+τ, α+τ) is of real type (D = κC̄ with κ^{Q+1} = 1) iff κ = 1 = α. So NG is of real type only at α = 1 [P, referee]. Consistently, TH with δ = 1 bounds the real-type α by 4Q+4, and Δ·Ω₁ ≢ 0.

### 2.7 FIX-1 in detail (scope of NG)
- **What the band requires.** EBR's band ρ+3 ≤ g ≤ 2ρ gives m/2 = g + ρ/2 ≥ 3ρ/2 + 3. So dim W = ρ ≤ (m−6)/3, and W has codimension ≥ m/2 + a₂ − ρ ≥ ρ/2 + 3 + a₂ in R_P.
- **What NG has.** W = R_P, of dimension m/2 + 1.
- **Why the arc's W cannot be all of R_P.** Over L, a G-stable W of the band's dimension is a strictly smaller object. Any degree-ρ right factor S ∈ L{τ} of P with ker S = W must be special: a generic P has no such factor.
- **What NG does and does not establish.**
  - Its hypotheses include dim W = m/2 + a₂, which is never the band's situation.
  - Nothing in the note excludes a proof of GLS₀ that uses only: the generic relation, G-stability of W, dim W = ρ ≤ (m−6)/3, and uniqueness of the relation line.
  - Those inputs are not "arc input" in the sense of STT/MRL.
  - Moreover TH shows that, at a₂ = 1, the elementary pointwise real-type specialisation already forces GLS₁ once δ is small. That is an elementary piece of arc data which NG violates.
- **Status of the open question.** It is [OPEN] whether a G-stable W with 2a₂ < dim W < m/2, a unique (N0) relation and Sol = 0 exists.
  - [H, referee] A parameter count suggests that it does. Degree-ρ right factors S of some C + Dτ^{m/2} with deg C, D ≤ a form a family of dimension about 2a+1 (ρ unknowns minus ρ−2a−1 rank conditions). Twisted half-fields A(U) form a family of dimension about a+1.
  - [P, referee] The simplest candidates, W = ηF_{2^ρ} with F_{2^ρ} ⊄ F_Q, always violate (N0). By Artin independence of the embeddings u ↦ u^{2^e}, (N0) forces s := m/2 mod ρ to satisfy s ≡ i ≡ −j with i, j ≤ a₂ < ρ/2, hence s ≡ 0.
- **Required restatement.** In the title, §5 "Scope/message" and §6(a), say that NG shows non-implication only for W = R_P (dim W = m/2 + a₂, outside the band). Delete "now necessary". Record the band-dimension version as [OPEN]. Add "dim W = ρ ≤ (m−6)/3" and "real type at > q/2 nonfoci (TH)" to NG's list of arc data it does not model.

### 2.8 FIX-2 in detail
- Ob_n is a finite F₂-linear problem over L(α₀, …, α_n) for each n, and OB is exact at each n.
- GLS₀ ⟺ ∃n ker Ob_n ≠ 0 has no proved bound on n.
- The PTH §4A(iv) degree bound (< m/2) does not help. Solutions of degree ≥ m/2 exist in general, for example A(τ^{m/2}+1), and nothing proves that the minimal one has degree < m/2. MI only gives injectivity on F_Q.
- Restate as follows: OB/RLE give an exact criterion degree by degree, which is a semi-decision for GLS₀. Non-existence is certified by VO, or by AC (a layer outside L(α₀)).

## 3. FIX items (substantive first)
- **FIX-1 (substantive; restatement).** Restrict NG's message to W = R_P (dim m/2 + a₂). State that the band has dim W = ρ ≤ (m−6)/3 < m/2, and that NG is of real type at only one α.
  - Replace §6(a)'s "now necessary, not just likely" and the title's "So GLS₀ is not a consequence of the generic relation" with the qualified statement.
  - Add an [OPEN] item: GLS₀ for G-stable W with 2a₂ < dim W ≤ (m−6)/3 and a unique (N0) relation.
  - Optionally cite the referee's [H] parameter count and the [P, referee] remark on W = ηF_{2^ρ}.
  - "PTH §4A(iii)'s tests are necessary but not sufficient" (§6(c)) is unaffected and correct.
- **FIX-2 (substantive; restatement).** Qualify "exactly computable" in §6(a) and "classified exactly by a finite obstruction map" in the title as **per degree n**, with no a priori degree bound, so a semi-decision. Mention AC's failure certificate.

## 4. Minor notes
- **m1.** NG: require even m ≥ 4, not "any even m". Change "ker(c + dτ^{m/2}) has dimension m/2" to "≤ m/2". State that W = ker P is G-stable, since P ∈ L{τ}.
- **m2.** Define generic a(W) for W ⊂ L̄: the minimal max(deg C, deg D) of a nonzero pair with C(w) = D(w^Q) on W. The note's §0 has only the pointwise definition via F_Q.
- **m3.** Lemma RD: "a nonempty root set is a coset of size Q iff y₀^{2^k−1} ∈ L^{*(Q−1)}".
- **m4.** OB1(c): "a Kummer condition in L" should read "an explicit identity in L"; nothing is required to be solvable.
- **m5.** TB: replace "truncated formal solution at ∞" with "lies in ker λ", or define the term.
- **m6.** DO: the hypothesis deg d₀ > deg c₀ is unnecessary; VO at ∞ works for any sign of θ.
- **m7.** R0 [COND]: add the one-line reason why α with a(V_α) = a₂ are plentiful, note that (C_α, D_α) ≠ 0 at every α after content removal, and note that (B1b)'s Frobenius twist preserves a(·).
- **m8.** §4: label "It has no generic analogue over L" as [H], or point to NG and TH.
- **m9.** TH: state the threshold with v′ = #{α ∈ N : a(V_α) = a₂, specialisation nonzero}, giving δ < v′/(4Q+4). Real type is guaranteed only at such α. δ < q/(4Q+4) is the best case.
- **m10.** §3 [C]: the RLE negative control is attributed to `glovo.py` but was run ad hoc. Either add it to the script or relabel it as "[C, ad hoc; reproduced by referee `glo_vo` (4)]".
- **m11.** §2 [C] T3: "half with a planted solution" is not recorded by the script, and the logs show 59/64 positives because of selection bias. Restate the claim, or log the planted count. The referee's `glo_ob` gives balanced coverage.
- **m12.** R0 and RLE cite ML (PTH v2.2) over L^sep. Note that ML's proof works over L̄ (or use FS(b)). Also say that GR's Kummer extension is Galois because μ_{Q−1} ⊂ F_Q ⊂ L.

## 5. `checks/` (referee code; `nice -n 19 python3 -I`; galois 0.4.11, sympy 1.14.0; each run under 70 s; one process at a time)
- **`glo_ob.py`**, with `glo_ob.log` (seed 20261007) and `glo_ob_seed7.log` (seed 7). Exhaustive layered search against Theorem OB (as sets), the TB identity, and OB1(a)/(b)/(c).
  - Parameters: (Q, N) ∈ {(4,6), (4,8), (4,10), (8,9)}, a₂ ≤ 3, n ≤ 3.
  - Each seed ran 202 instances with a balanced positive/negative mix: planted polynomial, planted formal-only, Kummer and random.
  - 0 mismatches.
- **`glo_ob1_closure.py` / `.log`.** OB1(b)/(c) decided exactly over F̄ by enumerating the forced candidates.
  - Cases: Q = 4 over GF(2⁶), 400 instances; Q = 4 over GF(2⁴), 300; Q = 8 over F₈, all 2401.
  - 0 mismatches.
- **`glo_pv_alg.py` / `.log`.** Four parts:
  - PV: exhaustive for Q = 4, 8; samples for Q = 16, 32.
  - The OB1(c) step-4 algebra, symbolic in Q.
  - The formula for s.
  - The TH degree bound (attained).
- **`glo_vo.py` / `.log`.** Four parts:
  - (1) 22 planted twisted families over F₂(X) (Q = 4, 8): RLE (ii), y₀ = y and N1 hold; VO never triggers at 184 places, with hypothesis (ii) holding at 84 of them.
  - (2) DO ≡ VO at ∞: 89/89.
  - (3) NG: (N0), VO at ∞, and Δ·Ω₁ ≢ 0.
  - (4) RLE controls on TX-like: [True, False, False].
- **`glo_ac.py` / `.log`.** AC in the finite model F₀ = GF(2⁶) ⊂ GF(2¹⁸), Q = 4: 162/162 solvable instances collapse; 67/78 unsolvable instances leave F₀(α₀).
- **`owner_copy/`.** Copies of `glocheck.py` and `glovo.py` with rerun logs.
  - `rerun_glocheck_seed1.log` adds the `time` lines; its first 11 lines are identical to the owner's log.
  - The seed-7 and glovo reruns are byte-identical to the owner's logs.
- **`checks_SHA256SUMS.txt`** (sha256 `d586da00eee3acbb768f66e38515231e0d2d77d120c88bd5cb8a10ab3e6c9790`):
  - `75915af9d813516fddae318dd8238d6030b6da9e9bd21b7f4a89075ce00fb1d5  glo_ac.py`
  - `704d7d78ef404307ca56967918f99d2ec7573e27a19c7108b5bb951306d3b5a9  glo_ob.py`
  - `09564172829a319d7136f7c5fc5084cc7703c95df020f8b95617a3dc28df854f  glo_ob1_closure.py`
  - `92a7e20281dc7fd0c8dc45a2116ad071442abd47d0d67402b6a80bc4977578e3  glo_pv_alg.py`
  - `839ba5e02214c8e8a33b9f3070ed30113d2f6aae041b63625b18c3cba970369f  glo_vo.py`
  - `ce30d2dfc29081dd27008023fcf251171363875b244a5c589fea3182bfcb9e98  glo_ac.log`
  - `824a3fad9f732623a362533d9572ca093e6ce5df999b44ebf8256bbbe60f67f4  glo_ob.log`
  - `58d4e757b377b9b78f6f8cc8725c6cbf73b3a56ca82a00b715a4584d2c0fd460  glo_ob1_closure.log`
  - `33ad7556a6b25a340fd19e0d12a5555f051375421e94b14d27adb226ed3b6fa7  glo_ob_seed7.log`
  - `a715fb74a5c15862e4f543db0178af71ca7927af8b2773917897973beff508d0  glo_pv_alg.log`
  - `e72208ef300ca295a2446eea5e55c1718c28689080ff92ba42df645dba4693ce  glo_vo.log`
  - `e39894a42da9d03bac0ee22d62d45e4b544253225b4d96f7ea9867afe066a9d3  owner_copy/glocheck.py`
  - `413b9fd4fc7faf8b8bbbab05cdf3d98fa7bfd12cb765d789154f4c758a7adf6b  owner_copy/glovo.py`
  - `d33ffc0201fc1c502ce7f411b5b46dbfa7bf7edded4e0006d6fab3250b228d05  owner_copy/rerun_glocheck_seed1.log`
  - `84c310e972da513398392d8afe0e2582471c86085dfc4e9fbbca01dcc6e0534b  owner_copy/rerun_glocheck_seed7.log`
  - `1ef8ddc45646fd5c7a67dc76b11d4d08f9dc4f07af3a9f972a6714a89866dd6f  owner_copy/rerun_glovo.log`
- The checks live in `referee_GLO/checks/`. Nothing other than this audit file was written to DZ_CLOUD_RESULTS.

## 6. Files read
- **The note under audit:** `referee_GLO/src/GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007.md` (full). The archive copy was compared by sha256 only.
- **Owner scripts:** `src/owner_scripts/glocheck.py`, `glovo.py` and the three logs (full). The `claude_archive/scripts/glo*` copies were compared by sha256 only.
- **Handoff:**
  - `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md` (full). It contains no referee-specific read restrictions; its labels were followed.
  - Grep of `notes/EBR-EVEN-BAND-REDUCTION-NOTE-20261007.md` for the band definition (lines 1, 10, 48, 52, 60).
- **Archive** (`/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive/`):
  - `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md` (full; cited for ML, GO, the §4A tests and LS);
  - `HANDBACK-20261007T2124Z.md` (full; cited for scope);
  - `AUDIT-KB-KUMMER-BINOMIAL-GATE-20261007.md` (lines 1–60 and the tail, for format);
  - a directory listing.
- **Not read:** RBL, TCR, GX and KB notes. GLO cites them only for context (TX, GO/GX/KB status), and nothing in GLO's proofs depends on them. Also not read: HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, uploads, other scratchpads. Git was not used.
