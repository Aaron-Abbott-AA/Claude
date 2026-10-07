# AUDIT — SH-SUBHALFFIELD-CRITERION-NOTE-20261007.md (owner note v1)

Independent referee audit by a fresh, isolated referee agent (DZ lane), 7 Oct 2026, written 22:58Z (`date -u` checked).
- **Note audited:** `SH-SUBHALFFIELD-CRITERION-NOTE-20261007.md`, sha256 `6fe44b3aa532917279ff06cf69568075fbb97986e36ca3a7ce13c15972668e2e`.
  - The working copy and the `claude_archive/` copy are byte-identical.
  - The hash matches HANDBACK-20261007T2240Z.
- **Owner scripts:** `slcheck.py` (bc74772c…4934) and `slcheck.log` (a060fbd3…260a). Both match the hashes in note §7.
- **Labels** are as in the handoff: [P] proof; [C] computation; [H] heuristic; [A] reading of a reviewed source; [COND]; [OPEN].
- **Isolation.**
  - No incoming scripts were executed. The owner script was re-run only from `checks/owner_copy/`, with `python3 -I`.
  - No git was used. No HYP/3PP directories, uploads or other scratchpads were read.

## Verdict: **PASS-with-fixes**

**The central mathematics is correct.**
- Theorem SH (a), (b), (c) is correct as [P].
- Corollaries SH2 and SH3 are correct.
- The "Consistency with RX" paragraph is correct.
- Proposition RK (a = 1: ker P ∩ L = W for every even m ≥ 4) is correct as [P].
  - Every valuation, degree and leading-coefficient step was re-derived by hand.
  - The F₄ branch is right.

**The explicit object is VERIFIED.** Referee code using different algorithms (§5) confirmed:
- RX's a = 1 cofactors equal the Vandermonde products;
- the degrees and the valuations at X and X+1;
- the cofactor identity;
- the F₄-branch identity A₁ = M₁X + M₄X^{2Q} = M₂X² + M₃X^Q, of degree 5Q+1;
- ker P ∩ L = W on all rational functions with small denominators:
  - every monic denominator of degree ≤ 3 (m = 4), ≤ 2 (m = 6) and ≤ 1 (m = 8, 10, 12);
  - random denominators of one degree higher;
  - 16 104 denominators in all;
  - a positive control that does detect roots with finite poles.

**FIX count: 2 substantive, 9 minor (m1–m9).** Both substantive items are **false-as-stated side clauses carrying a [P] label**. Neither touches the proofs of SH or RK.
- **FIX-1.** SH1's parenthetical says "under (N0) [the relation] is determined by W up to scalar". This is false when a₂ > a(W): for W = λF_Q there are two independent (N0) relations of degree 1 [P + C]. It is also unproved in the intended case.
  - The referee supplies a short proof (Claim U) of the correct version: if a₂ = a(W) and dim W ≥ 2a₂+1, the minimal relations form one line.
  - The bound is sharp.
- **FIX-2.** RK's "in particular RX cannot be extended to an even-dimensional radical inside the same P" and §3's "any band-dimensional counterexample … must use a different P" go beyond RK.
  - RK excludes only **G-fixed** (rational) extensions.
  - For m/2 odd, R_P itself is a G-stable, even-dimensional (m/2+1) subspace of R_P that contains W.
  - In general, **any G-stable W″ with W ⊂ W″ ⊂ R_P inherits RX's unique (N0) relation and its GLS₀ failure** (RX v2 (i), (iv)). Whether such W″ exist in band dimension is not decided by RK.

**Owner revision is needed** (wording, plus adoption or deletion of the supplied Claim U). A referee **diff check suffices**; a full re-audit is not needed.

## 1. Item table

| # | Item | Label | Finding | Result |
|---|---|---|---|---|
| 1 | Header, audit status, scope, "what is not claimed" | — | Accurate: HOLD, not in the outbox. GLS₀ for arcs, G1 and the conjecture are not claimed. | PASS |
| 2 | Title: "So the even-band GLS₀ question is exactly 'PTH (ii) holds generically'" | — | The body (SH2, SH1) proves this only for twists of degree < ρ−2a₂, i.e. GLS₁ when ρ > 3a₂. The title should say GLS₁ / low degree. | m1 |
| 3 | §0 setting, citations (GLO v2 9b1d48be…, RX v2 fcecc2c7…), even band ρ ≥ 2a₂+4 | [A] | Hashes match the archive. The band bound is re-derived: ⌈g/2⌉ ≥ ρ/2+2 for g ≥ ρ+3 with ρ even. | PASS |
| 4 | SH(a) sufficiency | [P] | Correct. P·A = CA + Dφ(A)τ^{m/2}. On U ⊂ F_Q, P(A(u)) = Λ(A)(u). deg_τ Λ(A) ≤ a₂ + deg A. A nonzero 2-polynomial of τ-degree n has at most 2^n roots. No injectivity or (N0) is needed for Λ(A) = 0; FS(b) (needs (N0)) gives L^sep. [C] T1: 385 trials above the threshold, 0 failures; the threshold is sharp (379 of 415 trials at or below it are strict). | PASS |
| 5 | SH(b) necessity | [P] | Correct. A(F_Q) ⊂ R_P; MI gives dim m/2; dim R_P ≤ m/2 + a₂; injectivity of A on F_Q gives W ∩ A(F_Q) = A(U′). (N0) is not needed. | PASS |
| 6 | SH(c) equivalence for d < ρ−2a₂ | [P] | Correct in both directions. (The backward direction does not need d < ρ−2a₂.) | PASS |
| 7 | SH1, first sentence and the degree ranges (≤ 3 in the band; GLS₁ when ρ > 3a₂) | [P] | Correct consequences of SH(c), given a₂. | PASS |
| 8 | SH1 parenthetical: "under (N0) it is determined by W up to scalar" | [P] | **False as stated** if a₂ > a(W): for W = λF_Q, Rel_{≤1} is 2-dimensional with two independent (N0) relations [P + C T2]. **Unproved** if a₂ = a(W). Referee proof of the corrected statement in §2.2. | **FIX-1** |
| 9 | SH2 (pointwise analogue; GLS₁ ⟺ generic PTH (ii) when ρ > 3a₂) | [P, A] | Correct. Two wording points: (i) "(when e = 0 …)" is attached to deg A ≤ a, which holds for every e (A ∈ S_C has degree ≤ a); (ii) "dim U > 2a₂" equals SH(c)'s "dim U > a₂ + deg A" only via SH(b) when ρ > 3a₂, and the note does not say so. | m2 |
| 10 | SH3 (constant twists) | [P] | Correct. The "in particular … (H) shape ηU" clause drops the hypothesis dim U > a₂. | m3 |
| 11 | Consistency with RX | [P] | Correct. An independent elementary check: a ratio of two distinct nonzero elements of F₂[X]_{≤2} is never in F_Q. | PASS |
| 12 | RK step 1 (Vandermonde, factor table, degrees, valuations, monic) | [P]+[C] | Correct; the 3×3 Vandermonde is standard [P]. "v_π(M₄) ≤ 3" is true, and in fact ≤ 2, because gcd(1+X^{Q−1}, 1+X^{Q/2−1}) = 1+X. [C] E1–E3, m = 4..16. | PASS; m7 |
| 13 | RK step 2 (no finite poles) | [P] | Correct. Both inequality chains were re-derived; they need Q ≥ 4. Also confirmed by the referee's denominator search (item 18). | PASS |
| 14 | RK step 3 (degree ≤ 2) | [P] | Correct: 2Qk−3Q+2−2k > 0 for k ≥ 3. | PASS |
| 15 | RK step 4 (β₂, β₁, β₀ ∈ F₂; the F₄ branch) | [P] | Correct. gcd(m/2−1, m) = gcd(m/2−1, 2). In the F₄ branch, M₂X² and M₃X^Q (both of degree 5Q+2) cancel, so deg A₁ = 5Q+1 [C E5/E6]; P(β₁X) = (β₁+β₁²)A₁ = A₁. | PASS |
| 16 | RK [C] slcheck V / R | [C] | Owner script re-run from `checks/owner_copy/`: byte-identical log. | PASS |
| 17 | RK "In particular RX cannot be extended to an even-dimensional radical inside the same P" | [P] | **Overclaim.** It holds for **rational (G-fixed)** extensions only. For m/2 odd, R_P (dim m/2+1, G-stable) is a counterexample to the literal statement. G-stable W″ ⊃ W are governed by R_P/W ≅ ker P̃ (§2.4). | **FIX-2** |
| 18 | §3 "[P] Two constructions are now closed … must use a different P" | [P] | "Non-monomial" follows (RX v2 §3, an [A] citation). "**Must use a different P**" does not: RK does not exclude G-stable non-rational W″ with W ⊂ W″ ⊂ R_P, and any such W″ of band dimension would be a counterexample with the same P (§2.4). | **FIX-2**; m4 |
| 19 | §3 [OPEN] premise "satisfies pointwise PTH (ii) at every nonfocus" | [A] | Passing from V_α to W(α) needs (B1b), and PTH applies with a(V_α) ≤ a* (not with a₂). Label [COND (B1b)]. | m8 |
| 20 | §3 [H] items (pigeonhole, heights, expectation) | [H] | Properly labelled. The expectation agrees with GLO v2's referee count. | PASS |
| 21 | §4(a) "needs no Lang equation, no (C, D) …" | [P] | Overstated. SH still needs a₂ and an (N0) relation, for L^sep-rationality via FS(b). With FIX-1's Claim U both are intrinsic to W in the band, which supports the intended statement. | m5 |
| 22 | §4(b), §4(c), §5 questions | — | Correct and scoped. | PASS |
| 23 | §6 self-check | — | Accurate apart from the FIX-1 and FIX-2 issues. "Vandermonde factorisation is [C]-checked" could be [P] (standard). | m6 |
| 24 | §7 scripts and hashes | [C] | Verified. | PASS |
| 25 | Optional: "unique (N0) relation" hypotheses in GLO FIX-1 / RX §3 | — | By Claim U, uniqueness is **automatic** once a₂ = a(W) and dim W ≥ 2a₂+1. So it is not an extra hypothesis in the band. | m9 (suggestion) |

## 2. Detailed audit

### 2.1 Theorem SH
- **(a)** In L̄{τ} (any field of characteristic 2 containing F_Q), τ^{m/2}A = φ(A)τ^{m/2}, so P·A = CA + Dφ(A)τ^{m/2}.
  - For u ∈ F_Q, τ^{m/2}(u) = u. So (P·A)(u) = Λ(A)(u), and P(A(u)) = 0 because A(u) ∈ R_P.
  - Λ(A) has τ-degree ≤ a₂ + deg A. Viewed as an ordinary polynomial of degree ≤ 2^{a₂+deg A}, a nonzero Λ(A) has at most 2^{a₂+deg A} roots. But it vanishes on U, with |U| = 2^{dim U} > 2^{a₂+deg A}. So Λ(A) = 0.
  - Injectivity of A is not needed. If A killed part of U, then dim(ker A ∩ U) ≤ deg A anyway.
  - Under (N0), FS(b) of GLO v2 puts A in L^sep{τ}.
  - [C] T1 (finite model K = GF(2^N) ⊃ F_Q with N ≠ 2h, so the Q-power is not an involution, as on L): ker Ψ ⊆ ker Φ_U always, and equality held in all 385 trials with dim U > a₂ + d. At or below the threshold, 379/415 trials were strictly larger, so the threshold cannot be lowered in general.
- **(b)** A(F_Q) ⊂ R_P by the same identity with Λ(A) = 0.
  - MI (PTH v2.2 §2, over L^sep) makes A injective on F_Q, so dim A(F_Q) = m/2.
  - dim R_P ≤ deg_τ P = m/2 + a₂. So dim(W ∩ A(F_Q)) ≥ ρ − a₂.
  - Injectivity gives W ∩ A(F_Q) = A(U′).
  - (N0) is not used; ML is not needed either.
- **(c)**
  - Forward: d′ ≤ d < ρ−2a₂ ⇒ ρ − a₂ > a₂ + d ≥ a₂ + d′.
  - Backward: (a) gives a solution of degree ≤ deg A ≤ d, and minimal solutions have one common degree (ML).
  - Both directions are correct.

### 2.2 SH1 and FIX-1 (uniqueness of the relation)
- **The counterexample when a₂ > a(W) [P + C].** Take W = λF_Q (or λU), with λ ∉ F_Q.
  - A pair (C, D) of degree ≤ a₂ < dim U is a relation on λU iff Cλ = Dλ^Q, i.e. d_i = c_iλ^{2^i(1−Q)} for every i. Here the degree is below the size of U, so the vanishing on U is an identity.
  - So Rel_{≤a₂} has dimension a₂+1, and every C with c₀c_{a₂} ≠ 0 gives an (N0) relation.
  - For a₂ = 1 there are two independent (N0) relations. Both admit the twist λ, consistently with SH3.
  - [C] T2 reproduced this for (h, N) = (4,12), (6,18), (3,9): dim Rel₀ = 1, dim Rel_{≤1} = 2, two independent (N0) relations, and Λ(λ) = 0 for both.
- **Claim U (the correct version) [P, referee].** Let K be a field of characteristic 2 (for example L̄). Let W ⊂ K be an F₂-subspace with a := a(W), the minimal degree of a nonzero relation, and suppose dim W ≥ 2a+1. Then the relations of degree ≤ a form one K-line.
  - *Proof.*
    1. **Top map.** The K-linear map Rel_{≤a} → K², (C, D) ↦ (c_a, d_a), is injective. Its kernel is Rel_{≤a−1} = 0.
    2. **Normalised pair.** Suppose dim Rel_{≤a} = 2. Then there are relations (C₁, D₁) with (c_a, d_a) = (1, 0) and (C₂, D₂) with (c_a, d_a) = (0, 1).
       - D₁ ≠ 0, since otherwise W ⊂ ker C₁ would have dimension ≤ a. Put b := deg D₁ ≤ a−1.
       - (For a = 0, the relation (1, 0) would force W = 0.)
    3. **Common left multiple.** A linear count (a+b+2 unknowns, a+b+1 equations, K-linear in the coefficients of H_i) gives nonzero H₁ (deg ≤ a) and H₂ (deg ≤ b) with H₁D₁ = H₂D₂. Then deg H₁ = deg H₂ + (a−b).
    4. **An annihilator of low degree.** Put E := H₁C₁ + H₂C₂. Then E(w) = (H₁D₁ + H₂D₂)(w^Q) = 0 on W.
       - deg(H₂C₂) ≤ deg H₂ + a − 1 < deg H₁ + a = deg(H₁C₁).
       - So E ≠ 0 and deg E = deg H₁ + a ≤ 2a.
    5. **Contradiction.** Hence dim W ≤ 2a, against dim W ≥ 2a+1. ∎
  - **Sharpness.** A random W of dimension 2a has a 2-dimensional Rel_{≤a} and no relation of lower degree ([C] T3(iii): 395/400; every deviation is a sample whose F₂-dimension dropped).
  - [C] T3(i)/(ii): W = A(U) with dim U ≥ 2a+1, and random W of dimension 2a+1. The line property held in every sample with the intended dimension. **0 counterexamples** to Claim U.
- **Repair.** Replace the parenthetical with:

  > "if a₂ = a(W) (the generic defect, GLO v2 §0) and ρ ≥ 2a₂+1 — automatic in the even band — the relations of degree ≤ a₂ form one line (Claim U, [P, referee]); for a₂ > a(W) the relation need not be unique (W = λF_Q), but SH(c) shows that GLS₀ in degree < ρ−2a₂ is the same for every (N0) relation of degree a₂."

  Alternatively, simply delete the parenthetical, since SH1's main sentence follows from SH(c) alone.

### 2.3 Proposition RK
- **Step 1.**
  - The rows (z_l^k), k = 0, 1, 2, give 3×3 Vandermonde minors, so M_l = Π over the pairs avoiding l. There are no signs in characteristic 2.
  - The factor table is correct.
  - Multiplicities: Q−1, 2Q−1 and Q/2−1 are odd for Q ≥ 4, and 1+X^{2n} = (1+X^n)². Also gcd(X^{Q−1}+1, X^{Q/2−1}+1) = X^{gcd(Q−1, Q/2−1)}+1 = X+1, so v_π(M₄) ≤ 2 off X(X+1). The note's ≤ 3 is enough. (For m = 4 the maximum is 1.)
  - Degrees (5Q, 5Q, 4Q+2, 2Q+2) and v_X = v_{X+1} = (Q+4, Q+2, 4, 4) were recomputed for M₁…M₄.
  - [C] E1–E3: sympy determinants (Berkowitz) over GF(2) for m = 4, 6, …, 16; factor_list for m ≤ 12.
- **Step 2.**
  - At X (or X+1): 4−2Qk < 4−Qk, and 4−2Qk < Q+2−2k ⟺ 2−Q < 2k(Q−1).
  - Elsewhere: 3−2Qk < −Qk ⟺ Qk > 3, and 3−2Qk < −2k ⟺ 2k(Q−1) > 3.
  - A unique minimum is impossible, so w is a polynomial. Correct.
- **Step 3.** The top degrees are compared correctly.
- **Step 4.**
  - X^{6Q+2}: only M₃w^Q and M₄w^{2Q} reach it. The c₁ term has degree 5Q+4 < 6Q+2. This gives β₂^Q ∈ F₂.
  - X^{5Q+2}: only M₂w² and M₃w^Q reach it. The d₁ term has degree 4Q+2. This gives β₁^Q = β₁², so β₁ ∈ F_{2^{gcd(m/2−1, m)}} ⊂ F₄.
  - In the F₄ branch, β^Q = β² and β^{2Q} = β when m/2 is odd. P(β₁X) = β₁(M₁X + M₄X^{2Q}) + β₁²(M₂X² + M₃X^Q) = (β₁+β₁²)A₁ = A₁, of exact degree 5Q+1, while deg P(β₀) ≤ 5Q.
  - X^{5Q}: β₀ + β₀² = 0, since deg M₃, M₄ < 5Q for Q > 2.
  - All correct. [C] E4–E6 for m = 4..16; the F₄ case occurs at m = 6, 10, 14.
- **[C] referee rational-kernel search** (`sh_ref_rk_kernel.py`, own GF(2^m) tables). For every monic denominator g, it computes the F₂-kernel of f ↦ g^{2Q}P(f/g) on F_q[X]_{≤deg g+4}. W·g always contributes dimension 3. Results:
  - m = 4: all g of degree ≤ 3, plus 300 random of degree 4;
  - m = 6: all g of degree ≤ 2, plus 500 random of degree 3;
  - m = 8: all g of degree ≤ 1, plus 1000 random of degree 2;
  - m = 10: all g of degree ≤ 1, plus 300 random of degree 2;
  - m = 12: all g of degree ≤ 1, plus 100 random of degree 2;
  - in every case the kernel has dimension exactly 3;
  - the polynomial kernel up to degree 8 also has dimension 3 for every m.
- **Positive control** (`sh_ref_rk_control.py`). For the relation of span(1, X, 1/(X+1)), the same routine returns 2 for g = 1 and 3 for g = X+1, at m = 4, 6, 8.
- **Verdict on the example:** VERIFIED.

### 2.4 FIX-2: what RK does and does not exclude
- RK proves ker P ∩ L = W, i.e. R_P^G = W. It says nothing about **G-stable** subspaces of R_P.
- **M_W map.** Let M_W be the subspace polynomial of W (monic, coefficients in F₂[X]). Then P = P̃·M_W with P̃ ∈ F₂[X]{τ} of τ-degree m/2−2 [C, exact division for m = 6..12]. The map M_W: R_P → ker P̃ is G-equivariant and onto, with kernel W.
- **Consequences.**
  - G-stable W″ with W ⊂ W″ ⊂ R_P correspond exactly to G-stable subspaces of ker P̃.
  - Every such W″ contains W. So it has no relation of degree 0, and its unique relation of degree ≤ 1 is RX's (C, D) (RX v2 (i); also Claim U).
  - GLS₀ fails for (C, D) (RX v2 (iv), via RW′ applied to W ⊂ R_P).
  - So **any G-stable W″ ⊃ W in R_P with 2a₂+4 = 6 ≤ dim W″ ≤ (m−6)/3 (possible only for m ≥ 24) would be an even-band-dimensional counterexample with the same P.**
- **A counterexample to the literal statement.** For m/2 odd, R_P itself (dim m/2+1, even) is G-stable and contains W. For m = 6, P̃ = p₀ + p₁τ has its root p₀/p₁ in L [C, `sh_ref_quotient.py`]. This lies outside the band.
- **What the referee could not decide.** Whether ker P̃ has G-stable subspaces (for example rational roots) for larger m.
  - A direct search found **no polynomial roots** of P̃ for m = 8..16. The search is complete for polynomial roots, since the Newton polygon of P̃ at ∞ is a single segment of slope 12 for every m = 8..16 (degrees in the log), so every root has degree 12 ≤ 16. For m ≤ 12, the polygons at X and X+1 also force zeros of order 4 there (referee computation). Roots with poles at other finite places are not covered. [C, `sh_ref_Zker.py`, with a positive control on P.]
  - **Caution.** Specialisations P̃_{x₀} with x₀ ∈ F_q always have ≥ m/2−3 roots in F_q (m = 8, 10, 12). This is forced pointwise by PTH (A_α(F_Q) ⊂ R_{P_α} ∩ F_q). It is **not** evidence for rational roots.
- **Repair.**
  - RK's last sentence: "In particular RX cannot be extended by a rational (G-fixed) root inside the same P; G-stable non-rational extensions W ⊂ W″ ⊂ R_P are not excluded."
  - §3: "Any band-dimensional counterexample must be non-monomial [A: RX v2 §3]; for a = 1 it cannot be a G-fixed extension of RX's W inside the same P (RK). G-stable non-rational W″ ⊃ W inside RX's P would be band counterexamples if they exist with 6 ≤ dim W″ ≤ (m−6)/3 [OPEN]."
  - Optionally, add this as a Codex/owner question.

### 2.5 Remaining sections
- §3 [H] and [OPEN] items are properly labelled (m8 concerns the [COND (B1b)] label).
- §4(b): GO's W′ = W ∩ A(F_Q) is exactly A(U′) of SH(b). Correct.
- §4(c), §5: no claims beyond the scope.

## 3. FIX entries (substantive first)
- **FIX-1 (substantive; SH1 parenthetical; title, §4(a) by reference).** "Under (N0) [(C, D)] is determined by W up to scalar" is false when a₂ > a(W) (W = λF_Q has two independent (N0) degree-1 relations) and unproved otherwise.
  - Restate as in §2.2, with the hypotheses a₂ = a(W) and ρ ≥ 2a₂+1, citing Claim U [P, referee] (proof in §2.2, adopt with credit). Or delete the parenthetical.
  - No proof of SH changes.
- **FIX-2 (substantive; RK last sentence of the header paragraph; §3 "[P] Two constructions are now closed", last bullet).** "RX cannot be extended to an even-dimensional radical inside the same P" and "must use a different P" exceed RK, which excludes only G-fixed extensions.
  - The literal statement fails for m/2 odd (R_P itself).
  - Any G-stable W ⊂ W″ ⊂ R_P of band dimension would be a counterexample with the same P.
  - Restate as in §2.4. Optionally add the [OPEN] question about G-stable subspaces of ker P̃.

## 4. Minor notes
- **m1 (title).** "So the even-band GLS₀ question is exactly …": replace GLS₀ with "GLS₁ (when ρ > 3a₂), and more generally GLS₀ with a twist of degree < ρ−2a₂".
- **m2 (SH2).**
  - Move "(when e = 0; see PTH (iii))" so that it qualifies "V = A(U), deg A = a". deg A_α ≤ a holds for every e.
  - Add one line: with ρ > 3a₂, "∃A(U) ⊂ W with deg A ≤ a₂ and dim U > 2a₂" ⟺ "… dim U > a₂ + deg A". The direction ⇐ is via SH(a) then SH(b).
- **m3 (SH3).** In "in particular … ηU", add "with dim U > a₂".
- **m4 (§3).** The monomial bullet is a citation of RX v2 §3: label it [A] (reviewed), not [P].
- **m5 (§4(a)).** "No (C, D)" is too strong: SH uses a₂ and an (N0) relation (FS(b)). With Claim U these are intrinsic to W in the band.
- **m6 (§6, RK step 1).** The Vandermonde factorisation is a standard [P] identity. The [C] check is confirmation.
- **m7 (RK step 1).** It may be sharpened to v_π(M₄) ≤ 2 off X(X+1), since gcd(1+X^{Q−1}, 1+X^{Q/2−1}) = 1+X. Cosmetic.
- **m8 (§3 [OPEN] premise).** "Satisfies pointwise PTH (ii) at every nonfocus" uses (B1b) (V_α → W(α)) and holds with a(V_α) ≤ a*. Label it [COND (B1b)] / [A].
- **m9 (suggestion).** Record that, by Claim U, the hypothesis "unique (N0) relation line" in GLO v2 FIX-1 / RX v2 §3 is automatic for G-stable W with a₂ = a(W) and dim W ≥ 2a₂+1. Only (N0) itself remains a hypothesis.

## 5. Checks (referee code; `checks/` in the referee working directory)
All were run with `nice -n 19 python3 -I`, one process at a time, each in under 2 minutes.

| File | Content | Result |
|---|---|---|
| `owner_copy/slcheck.py`, `owner_copy/slcheck_rerun.log` | Copy of the owner script and its re-run | Byte-identical to the owner log (a060fbd3…) |
| `sh_ref_rk_exact.py` / `.log` | E1–E6: sympy 3×3 determinants over GF(2) vs Vandermonde products; degrees; monic; v_X, v_{X+1}; factor_list of M₄; gcd; cofactor identity; F₄ identity A₁ and cancellation at 5Q+2. m = 4..16. | All True. Max multiplicity off X(X+1) is 1 (m = 4) or 2 (m = 6..12). |
| `sh_ref_rk_kernel.py` / `.log` | Rational kernel with denominators (own GF(2^m) tables; F₂-linear in the numerator) | 16 104 denominators over m = 4..12: kernel dimension 3 in every case. Polynomial kernel up to degree 8: 3. |
| `sh_ref_rk_control.py` / `.log` | Positive control: relation of span(1, X, 1/(X+1)) | (2, 3) as expected, m = 4, 6, 8 |
| `sh_ref_sha.py` / `.log` | Finite model GF(2^N) ⊃ F_Q: T1 SH(a) threshold; T2 λF_Q non-uniqueness; T3 Claim U and its sharpness | T1: 385/385 equal above the threshold, 0 containment failures. T2: (1, 2), two (N0) relations, twist λ, for 3 fields. T3: 0 Claim U counterexamples; all deviations are F₂-dimension drops. |
| `sh_ref_quotient.py` / `.log` | P = P̃·M_W (exact); m = 6: R_P G-stable of dim 4; specialised kernels for m = 8, 10, 12 | Division exact. The specialisation test is inconclusive by design (see §2.4). |
| `sh_ref_Zker.py` / `.log` | Polynomial roots of P̃ up to degree 16, m = 8..16, with a positive control on P | P̃: dimension 0 for all m. Control: 3 (= W). |
| `checks_SHA256SUMS.txt` | sha256 of all files above | — |

## 6. Files read
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`.
- `referee_SH/src/SH-SUBHALFFIELD-CRITERION-NOTE-20261007.md`, and `src/owner_scripts/slcheck.py`, `slcheck.log`.
- `claude_archive/`, in full:
  - `GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md` (9b1d48be…);
  - `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md` (9ecf61da…);
  - `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md` (fcecc2c7…);
  - `HANDBACK-20261007T2235Z.md`, `HANDBACK-20261007T2240Z.md`.
- `claude_archive/AUDIT-RX-RATIONAL-BAND-COUNTEREXAMPLE-20261007.md`: first 60 lines and headings, for format only.
- **Not read:** HFD, EBR, OBC, TCR, RBL and the IDEAS/STATE docs. They enter only as [A] citations inside the note, and none of the audited [P] steps depends on them beyond what GLO v2, PTH v2.2 and RX v2 restate.
