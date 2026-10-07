# AUDIT — RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007.md (owner note v1)

Independent referee audit (fresh isolated referee agent, DZ lane), 7 Oct 2026, written 22:28Z (`date -u` checked).
- Note audited: `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007.md`, sha256 `ff4da8dd5631fc79bcf20e946ef822d3b3fcaaa33181e46538509517942d76c7`. The working copy and the `claude_archive/` copy are identical.
- Owner scripts: `rxcheck.py` (a53dcda9…f047) and `rxcheck.log` (16a5315f…ae53). Both match the hashes recorded in PROGRESS.md.
- Labels as in the handoff: [P] proof, [C] computation, [H] heuristic, [A] reading of a reviewed source, [OPEN].

## Verdict: **PASS-with-fixes**

- **The central claim is correct.** Lemma RW, Corollary RW′ and Theorem RX (i)–(v) are correct as [P].
- **The explicit object was VERIFIED independently.** W = F₂[X]_{≤2a} with the cofactor relation (C, D) was checked with referee code that uses different algorithms (§5):
  - exact cofactors, all nonzero, with the predicted degrees and orders;
  - the cofactor identity, so W ⊂ ker P;
  - no relation of degree ≤ a−1;
  - the valuation formula, with residue 2^{a+1}−a−2 mod Q−1;
  - Δ·Ω₁ ≢ 0 for a = 1;
  - pointwise real type.
- **So the FIX-1 question of GLO v2, as posed, is answered negatively, and correctly.**
- **FIX count: 1 substantive, 8 minor (m1–m8).**
  - FIX-1: the "real type at almost every α" property is labelled [P] in the title and §4(a), but no proof is given. It also cites HFD §1 outside HFD's stated setting. The referee supplies a short, self-contained repair (§3).
  - No proof needs to change. Owner revision is needed, but only for wording and for adding the supplied argument. A diff check is enough after that; a full re-audit is not needed.

## 1. Item table

| # | Item | Label | Finding | Result |
|---|---|---|---|---|
| 1 | Header, scope, "what is not claimed" | — | Accurate. Nothing about arcs, GLS₀ for the arc family, G1 or the conjecture is claimed. | PASS |
| 2 | §0 setting and citations (GLO v2 sha256 9b1d48be…faf40f; PTH v2.2) | [A] | The hash matches the archive copy. The notation (Λ, φ, GLS₀, (N0), y₀) matches GLO v2 §0. | PASS |
| 3 | Lemma RW (G-fixed radicals ⇒ χ trivial, A ∈ L{τ}, y₀ ∈ L^{*(Q−1)}) | [P] | Correct. Each step checked: ML/GO(a) give the line and the χ-equivariance; MI gives dim A(F_Q) = m/2; dim R_P = m/2 + a₂; the intersection is > 0; g fixes w; A is injective on F_Q; a₀ ∈ L. | PASS |
| 4 | Corollary RW′ (Kummer-divisibility test) | [P] | Correct: y ∈ L^{*(Q−1)} ⇒ v_π(y) ≡ 0 mod Q−1 at every place, including ∞. | PASS |
| 5 | RX(i): generalised Vandermonde, cofactor line, all 2a+2 coefficients ≠ 0, (N0) | [P] | Correct. Strict rearrangement holds because the k_j and the e_l are distinct (2^a < Q). The kernel of a rank-ρ ρ×(ρ+1) matrix is spanned by the cofactors. [C, referee] E1/E2: exact, 14 (a, m) cases. | PASS |
| 6 | RX(i): a(W) = a (no relation of degree ≤ a−1) | [P] | Correct. [C, referee] Two different 2a×2a minors are nonzero, and the rank at random points of GF(2^61) is 2a. | PASS |
| 7 | RX(ii): W ⊂ L, G-fixed, W(α) ⊂ F_q | [P] | Trivially correct. | PASS |
| 8 | RX(iii): v_∞(y₀) formula; residue 2^{a+1}−a−2 ∈ (0, Q−1) | [P] | Correct. The sum identity, the reduction mod Q−1 and the bound ≤ Q−3 were all re-derived. [C, referee] exact for a = 1..4. | PASS |
| 9 | RX(iv): GLS₀ fails; GLS₁ fails; Δ·Ω₁ ≢ 0 (a = 1) | [P] | Correct over L^sep, via RW′ at ∞. The extension to L̄ needs GLO FS(b), which is not cited. [C, referee] F1: Δ·Ω₁(β) ≠ 0 at random β ∈ GF(2^61), for m = 16, 18, 20. | PASS; m1 |
| 10 | RX(v): band inequality for m ≥ 6a+9 | [P] | Correct arithmetic. | PASS |
| 11 | RX(vi), first clause: pointwise real type via HFD §1 [A] | [P via A] | The conclusion is true. But HFD's setting is "ρ even ≥ 4", whereas W(α) has odd dimension 2a+1 (3 when a = 1). The per-α hypotheses are also stronger than needed. A direct proof exists (FIX-1). | **FIX-1** |
| 12 | RX(vi) [C] 300/300 (a = 1, m = 16) | [C] | Reproduced. The referee also checked **exhaustively** (F2): all 65 280 α ∈ F_q with rank-3 evaluation are of real type, and the 256 exceptions are exactly F_Q. | PASS |
| 13 | Title and §4(a): "real type at almost every α" in a [P] list | [P] claimed | No density proof is given. §6 itself says that "only the [C] sample checks how often" the hypotheses hold. | **FIX-1** |
| 14 | §3: why RX misses the even band (ρ ≥ 2a₂+2) | [P] | Correct. The sharper bound in the band is ρ ≥ 2a₂+4 (see m2). | PASS; m2 |
| 15 | §3: monomial W cannot reach dim 2a+2 | [P] | Correct, given a < m/2, which is unstated but automatic in the band. | PASS; m3 |
| 16 | §3 [C]: no extra rational roots in the tested ranges | [C] | Reproduced, and also by referee code (K2, K3). The tested polynomial range is in fact **complete** for polynomial roots (Newton bound K1). Roots with poles at finite places ≠ 0 are untested. | PASS; m4 |
| 17 | §3 [H] mechanism; §3 refined [OPEN] | [H]/[OPEN] | Properly labelled. | PASS |
| 18 | §4(a) non-implication | [P] | Correct once FIX-1 is applied. | PASS after FIX-1 |
| 19 | §4(b) RW′ as a new necessary test | [P] | Correct. | PASS |
| 20 | §4(c): "logically independent inputs" | [H] | Overstated: RW itself links the two inputs (rational W of dimension > a₂, together with GLS₀, forces χ = 1). RX shows only that rationality does not imply GLS₀. | m5 |
| 21 | §4(d), §5 questions | — | Correct and appropriately scoped. | PASS |
| 22 | §2/§7 [C] rxcheck.py; hashes | [C] | Hashes verified. Re-run with `python3 -I` from `checks/owner_copy/` gives an identical log. The docstring omits part D, and `partD` is defined after the first `__main__` block. | m6 |
| 23 | Theorem RX heading, "of band dimension" | — | dim W = 2a+1 is odd, so it is never an even-band ρ. The wording should be "of the dimension range posed in GLO FIX-1". | m7 |
| 24 | §6 self-check, (vi) bullet | — | Superseded by FIX-1: no condition on a(W(α)) is needed. | m8 |

## 2. Detailed audit

### 2.1 Lemma RW and Corollary RW′
- **Setup.** GLS₀ gives a nonzero solution over L^sep. By PTH v2.2 §4A ML (K = L^sep), the minimal solutions form one right F_Q-line, a₀ ≠ 0, and (N0) gives c₀ ≠ 0, so d₀ ≠ 0.
  - Each g ∈ G maps a minimal solution to a minimal solution, so g(A) = Aχ(g) with χ(g) ∈ F_Q^*.
  - Comparing τ⁰-coefficients gives χ(g) = g(a₀)/a₀ (PTH §4A Consequence (ii)).
- **A(F_Q) ⊂ R_P.** P·A = CA + D·A^{(Q)}τ^{m/2}, and x^Q = x on F_Q. So P(A(x)) = (CA + DA^{(Q)})(x) = 0.
- **Dimensions.**
  - MI (PTH §2, over L^sep) gives dim_{F₂} A(F_Q) = m/2.
  - Under (N0), P is separable (constant term c₀ ≠ 0) and has τ-degree m/2 + a₂ (leading coefficient d_{a₂} ≠ 0). So dim R_P = m/2 + a₂ exactly.
  - Hence dim(W^G ∩ A(F_Q)) ≥ dim W^G − a₂ > 0. W itself plays no role beyond W^G ⊂ R_P ∩ L.
- **χ is trivial.** For 0 ≠ w = A(x) ∈ L: g(w) = g(A)(x), since x ∈ F_Q ⊂ L. This equals A(χ(g)x). Injectivity on F_Q gives χ(g) = 1.
- **Conclusion.** a₀ ∈ L^G = L. (In fact g(A) = A for all g, so A ∈ L{τ} directly, without RLE.) The τ⁰-equation gives y₀ = a₀^{Q−1}.
- **RW′.** This is the contrapositive at any place. **No gap.**

### 2.2 Theorem RX (i)–(v)
- **Generalised Vandermonde.** Over F₂ the determinant equals the permanent Σ_π X^{Σ k_j f_{π(j)}} reduced mod 2.
  - Strict rearrangement (distinct k_j, distinct f_l) makes the sorted pairing the unique maximiser and the reversed pairing the unique minimiser. So the extreme monomials survive.
  - Distinctness of E needs 2^a < Q, which follows from a+1 ≤ m/2.
- **Relation line.** A relation of degree ≤ a is an F₂-linear condition in w, so it suffices to test it on the basis X^k. All maximal minors are nonzero, so the rank is ρ over L and over L̄, and the kernel is the cofactor line.
  - Index bookkeeping: c_i = M_{i+1} (column 2^i) and d_i = M_{a+2+i} (column 2^iQ). Correct.
- **a(W) = a.** The 2a×2a minor on rows 0..2a−1 is nonzero, so the ρ×2a E′-matrix has full column rank.
- **(iii).**
  - Pairing check: c₀ omits e₁ = 1 and d₀ omits e_{a+2} = Q. The sorted lists differ in positions 1..a+1 (shifted by one), so deg c₀ − deg d₀ = Σ_{j=1}^{a+1}(j−1)(e_{j+1} − e_j). This equals Σ_{j=1}^{a}(j−1)2^{j−1} + a(Q − 2^a).
  - Σ_{i=0}^{a−1} i2^i = (a−2)2^a + 2.
  - Mod Q−1 this gives −(2^{a+1} − a − 2).
  - Bounds: 1 ≤ 2^{a+1} − a − 2 ≤ Q − 3 when 2^{a+1} ≤ Q.
  - [C, referee] confirms exactly that v_∞(y₀) = −254, −510, −1022, −4090, −8186, −16378, −49138, −98290 (the note's list), plus (a, m) = (4, 34): −524258, residue 26.
- **(iv).**
  - RW′ at ∞ with W^G = W of dimension 2a+1 > a. This is correct over L^sep.
  - The note says "no nonzero A ∈ L̄{τ}". That needs GLO v2 FS(b): every polynomial solution over L̄ is over L^sep, under (N0). It is not cited (m1).
  - GLS₁ failure follows. For a = 1, OB1(c) ([A], GLO v2) gives Δ·Ω₁ ≢ 0. The referee confirmed this **independently of RW**, by evaluating Δ·Ω₁ at random β ∈ GF(2^61) (F1): nonzero for m = 16, 18, 20.
- **(v).** (m−6)/3 ≥ 2a+1 ⟺ m ≥ 6a+9. Correct.

### 2.3 RX(vi), the title and §4(a): real type (FIX-1)
- **Problem 1: the [A] citation is out of scope.** HFD §1 is stated for "ρ even ≥ 4", whereas W(α) has dimension 2a+1, which is odd (3 when a = 1). The module argument (d₁ + d₂ = ρ) does extend, but that extension is not reviewed.
- **Problem 2: the density is unproved.** The clause needs dim W(α) = 2a+1, a(W(α)) = a and (C_α, D_α) ≠ 0 at α. The note gives no count of such α; §6 concedes that only the [C] sample addresses it. Yet the title ("real type at almost every α") and §4(a)'s [P] list use the density.
- **Referee repair [P, referee].** Let Z := {α ∈ F_q : M_l(α) = 0 for all l} (common zeros of the cofactors).
  - **(a)** For α ∉ Z, the evaluated ρ×(2a+2) matrix N(α) = ((α^k)^{e_l}) has rank ρ = 2a+1. Evaluation F₂[X] → F_q is a ring map, so minors evaluate to minors. Its rows are then F_q-independent, so 1, α, …, α^{2a} are F₂-independent: an F₂-dependence among the α^k would give one among the rows, because w ↦ (w^{e_l})_l is F₂-linear. Hence dim W(α) = 2a+1.
  - **(b)** The F_q-relations of degree ≤ a on W(α) are exactly ker N(α). This is a line, spanned by the evaluated cofactors (C_α, D_α) ≠ 0.
  - **(c)** σ(c, d) := (d̄, c̄) (x̄ = x^Q) preserves ker N(α). To see this, raise each relation to the Q-th power and use x^{Q²} = x on F_q.
    - So σ(v) = μv with N_{F_q/F_Q}(μ) = 1. Hilbert 90 gives a σ-fixed generator λv = (C′, C̄′).
    - Hence d_i(α) = κc_i(α)^Q with κ = λ^{Q−1}, so κ^{Q+1} = 1.
    - No HFD input and no hypothesis on a(W(α)) are needed.
  - **(d)** |Z| ≤ min_l deg M_l = deg M_{2a+2} (delete the largest column 2^aQ) = Q[(2a−1)2^a − a + 1] + (a−1)2^{a+1} + 2 < 2a·2^a·Q.
    - [C, referee] This matches the exact degrees for a = 1..4: 2Q+2, 11Q+10, 38Q+34, ….
    - If m ≥ 6a+9 (so m ≥ 6a+10, Q ≥ 2^{3a+5}), then |Z|/q < 2a·2^a/Q ≤ a·2^{−2a−4} ≤ 1/64.
    - So real type holds at > 63q/64 points: more than the "> q/2" that GLO's audit lists as arc data.
- **[C, referee] F2 (exhaustive).**

  | (a, m) | α with rank ρ | of real type | \|Z\| | Z equals |
  |---|---|---|---|---|
  | (1, 12) | 4032 | 4032 | 64 | F_Q |
  | (1, 16) | 65 280 | 65 280 | 256 | F_Q |
  | (2, 12) | 4020 | 4020 | 76 | \|F_Q ∪ F_16\| |

- **[C, referee] F3 (samples, band cases).** (2, 22): 1500/1500. (3, 28): 300/300.
- **Required change.** See FIX-1 in §3.

### 2.4 §3: the even band remains OPEN
- **Parity.** In the even-ρ lane, dim W = ρ is even, so RX (dim 2a+1) can never be a band W. §3 says so correctly.
- **Sharper threshold.** With EBR's a* = ρ − ⌈g/2⌉ and g ≥ ρ+3, a₂ ≤ a* ≤ ρ/2 − 2, so the band has ρ ≥ 2a₂+4. This coincides with TCR's G1″ threshold 2a*+4. Stating the refined [OPEN] for ≥ 2a₂+2 is more general and not wrong (m2).
- **Monomial bound.** Correct, given a < m/2 so that the exponents are distinct (m3). The same argument also covers F_q-scaled monomials λ_jX^{k_j}: the extreme term has coefficient Πλ_j^{e_{π(j)}} ≠ 0. Optional.
- **[C] extension search.**
  - Reproduced: the F₂-kernel on F₂[X]_{≤48} has dimension 3 for m = 16 and 18. Referee extras: m = 20 on ≤64, and (a = 2, m = 22) on ≤40, kernel dimension 5. The F_q[X]_{≤6} and F_q[X]_{≤10} kernels have dimension 3 (m = 16), computed with a different field modulus.
  - **Newton bound K1.** Any polynomial root has degree ≤ 2a, for every tested (a, m). So these searches are **complete for polynomial roots** in F_q[X]. K1 also shows that no rational root has a pole at X = 0. Poles at other finite places are not covered.
  - The phrase "in these ranges" is honest. The owner may state the stronger polynomial-root completeness (m4).
  - The reasoning "an extension to dimension 2a+2 containing W must use the same P" is right, since W's relation line is unique.

### 2.5 §4: consequences
- (a) is correct after FIX-1.
- (b) is correct.
- (c) [H]: "logically independent" is too strong. RW shows a dependence (rational W with dim > a₂, together with GLS₀, forces trivial χ and y₀ ∈ L^{*(Q−1)}). RX shows only "rational ⇏ GLS₀" (m5). "Not covered by TCR RS" is correct: 2a+1 < 2a+4.
- (d) is correct.

### 2.6 Optional additions (not required)
- **O1 (consistency with GLO TH; sharpness).** For a = 1 and m = 16: δ = max deg = 5Q = 1280, real type holds at q − Q = 65 280 points, and Δ·Ω₁ ≢ 0.
  - This is consistent with TH's bound (4Q+4)δ ≈ 1.3·10⁶.
  - It also shows that a TH-type bound "#real ≤ c·Q·δ" cannot have c below about 1/5. So TH is sharp up to a constant. This is a cheap remark the owner may add, labelled [P]+[C].
- **O2 (second Kummer certificate).** [C, referee] v₀(y₀) = ord c₀ − ord d₀ has the same nonzero residue 2^{a+1}−a−2 mod Q−1 in every tested case (E2). The [P] proof follows from the reversed pairing. Optional.

## 3. FIX entries (substantive first)

- **FIX-1 (substantive; proof addition and relabel).** "Real type at almost every α" is used as [P] in the title and in §4(a), but RX(vi) gives only a per-α conditional through HFD §1, outside HFD's stated setting (ρ even ≥ 4). There is no density argument.
  - **Repair.** Replace the first clause of (vi) with the referee argument in §2.3 (a)–(d):
    - at every α outside the common zero set Z of the cofactors, (C_α, D_α) ≠ 0 spans the σ-stable relation line, so it is of real type by Hilbert 90;
    - |Z| ≤ deg M_{2a+2} < 2a·2^a·Q, so |Z|/q < 1/64 when m ≥ 6a+9.
  - Drop the HFD §1 [A] dependence and the hypothesis a(W(α)) = a. Optionally cite the exhaustive [C] F2 (Z = F_Q for a = 1).
  - Alternatively, relabel "almost every α" as [C] in the title and §4(a).

## 4. Minor notes
- **m1.** RX(iv): cite GLO v2 FS(b) for the passage from L^sep to L̄ ("no nonzero A ∈ L̄{τ}"). Alternatively, state (iv) over L^sep.
- **m2.** §3: within the band, a₂ ≤ a* ≤ ρ/2 − 2, so ρ ≥ 2a₂+4, which equals the G1″ threshold. The refined [OPEN] question may note that 2a₂+4 ≤ dim W is the band-relevant case, and that dim W = 2a₂+2 and 2a₂+3 are intermediate.
- **m3.** §3 monomial [P]: add the hypothesis a < m/2 (distinct exponents). Optionally extend it to F_q-scaled monomials.
- **m4.** §3 [C]: note that the tested ranges are complete for polynomial roots (any polynomial root has degree ≤ 2a, by the Newton polygon at ∞ [C, referee K1]). Rational roots with poles at finite places other than X = 0 are untested.
- **m5.** §4(c): replace "logically independent inputs" with "rationality of W does not imply GLS₀ (RX); conversely, under GLS₀, rationality forces χ = 1 (RW)".
- **m6.** rxcheck.py: the docstring omits part D, and `partD` and the second `__main__` block come after the first. This is cosmetic; the output is correct and reproducible.
- **m7.** Theorem RX heading and §4(a): "of band dimension" should read "in the dimension range 2a₂ < dim W ≤ (m−6)/3 posed by GLO FIX-1 (odd dimension, so never an even-band ρ)".
- **m8.** §6, (vi) bullet: update after FIX-1. No condition on a(W(α)) is needed, and the exceptional set is bounded.

## 5. Checks (referee code; `checks/` in the referee working directory)
All checks were run with `nice -n 19 python3 -I`, one process at a time, in under 75 s each. None reuses owner code.
- **`rx_ref_exact.py` / `.log`** (~9 s): exact cofactors as **permanents mod 2 by subset DP** (the owner enumerates permutations).
  - E1: sympy cross-check on 7 tiny matrices, all equal.
  - E2, for 14 cases (a, m) ∈ {(1,4), (1,6), (2,6), (1,10), (2,12), (1,16), (1,18), (1,20), (2,22), (2,24), (2,26), (3,28), (3,30), (4,34)}: all cofactors nonzero; degree and order equal the predictions; the cofactor identity holds; two E′ minors are nonzero; v_∞(y₀) equals the formula, with residue 2^{a+1}−a−2; the v₀ residue is recorded; the band flag holds. All True.
- **`rx_ref_fields.py` / `.log`** (~73 s): own GF(2^n) arithmetic; moduli checked irreducible with galois. Cofactors are computed as determinants of the **evaluated** matrix.
  - F1: Δ·Ω₁ ≠ 0 at 9 random points of GF(2^61), for m = 16, 18, 20. The evaluated determinants equal the exact polynomials, and the E′ rank is 2a.
  - F2: exhaustive real type for (1,12), (2,12) and (1,16).
  - F3: samples (2,22) 1500/1500 and (3,28) 300/300.
- **`rx_ref_kernel.py` / `.log`** (<1 s):
  - K1: Newton candidates for polynomial-root degrees are ⊂ [0, 2a], and there are no pole orders at 0.
  - K2: F₂-kernels have dimension 3, 3, 3 and 5.
  - K3: F_q[X]_{≤6} and F_q[X]_{≤10} kernels have dimension 3.
- **`owner_copy/rxcheck.py`** and **`owner_copy/rxcheck_rerun.log`**: the owner script copied and re-run with `python3 -I`. The log is byte-identical to the owner's (16a5315f…ae53).
- **`checks_SHA256SUMS.txt`**, sha256 `81ceccebb7bac30d249d4ea749f7e3baad9cd5c56f1b6f72387b5cbb6750bf3e`:

```
66b2adb0ce9a305916b5a21880eef430c97ecc2c7311d0aa934d8db68af5451f  rx_ref_exact.py
59248ee1741b21678ca60de4815d17d393f3d6774da07669c2ecb86d7087806d  rx_ref_exact.log
9f7d87fb40e850b52ad2ba01bbf9d0c985de3c1df3190c728708705a40d23b26  rx_ref_fields.py
500f32e6c854bd7502d80b47e9fe5691158b41b2c17d4b7e666f42a489a1bc1e  rx_ref_fields.log
e288cd35a48517b684253b075379d0a935da40bf85c7e0e278debf7a5db80593  rx_ref_kernel.py
539f3878fd3f2a1db0d5e72a08a333636496622ce59f7e2ed379b11ab016c2f7  rx_ref_kernel.log
a53dcda9d24ca7291f5fa2726cf743405ebfc23cca96d3db61177ced88f9f047  owner_copy/rxcheck.py
16a5315f2bddfb4891b5e264374473559876a676a57d0a650da3eb45abf2ae53  owner_copy/rxcheck_rerun.log
```

The checks live only in the referee working directory (`dz_isolated/referee_RX/checks/`). Per the referee instructions, nothing other than this audit file was added to DZ_CLOUD_RESULTS.

## 6. Files read
- `dz_isolated/work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`. It places no referee-specific read restriction beyond the isolation rules given.
- `dz_isolated/work/DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md` (§1–§2; cited by RX(vi)).
- `referee_RX/src/RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007.md` (the note under audit).
- `referee_RX/src/owner_scripts/rxcheck.py` and `rxcheck.log` (read and re-run only from a copy).
- `DZ_CLOUD_RESULTS/claude_archive/`:
  - GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md (sha256 9b1d48be…faf40f, verified);
  - AUDIT-GLO-GENERIC-LANG-OBSTRUCTION-20261007.md (FIX-1 and §2.7 only, via grep);
  - PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md;
  - TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md (grep for G1″ and 2a*+4);
  - HANDBACK-20261007T2211Z.md, and the head of HANDBACK-20261007T2219Z.md;
  - the directory listing; RX's archive copy and scripts/rxcheck.* (hashes only).
- `DZ_CLOUD_RESULTS/PROGRESS.md` (grep for the RX lines and hashes only).
- Not read: HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads, other scratchpad directories, and git.
