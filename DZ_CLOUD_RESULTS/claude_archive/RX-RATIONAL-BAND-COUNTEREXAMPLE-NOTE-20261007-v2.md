# GLO's FIX-1 [OPEN] question, answered negatively as posed: W = F₂[X]_{≤2a} (rational, G-stable, dim 2a+1 ≤ (m−6)/3, unique (N0) relation of degree a) has NO generic Lang twist, although its specialisations are of real type at more than 63q/64 points α [v2: FIX-1]. The cause is a Kummer-divisibility obstruction for G-fixed radicals (Lemma RW). The even-band range dim W ≥ 2a₂+2 remains OPEN. (Owner note **v2**, cloud session, 7 Oct 2026, 22:31Z; v1 22:17Z.)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac; no mailbox access).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- v1 (sha256 ff4da8dd5631fc79bcf20e946ef822d3b3fcaaa33181e46538509517942d76c7) was independently audited in AUDIT-RX-RATIONAL-BAND-COUNTEREXAMPLE-20261007.md (sha256 7cfed798…59b0a8). Verdict: **PASS-with-fixes** (1 substantive FIX-1, 8 minor m1–m8). The explicit example was independently VERIFIED.
- **This v2** applies FIX-1 and m1–m8. Each change is marked [v2: FIX-1] or [v2: m-n], and the change log is §8.
- FIX-1 adopts the referee's proof of real type, credited as [P, referee].
- **STATUS: v2 — PENDING DIFF-CHECK.** Packet EL is prepared in the outbox, marked PENDING DIFF-CHECK (NOT READY).

**Scope.** HANDBACK-20261007T2211Z §2 lists the targets:
- item 1: device steps, impossible here;
- item 2: questions to Codex, which need the mailbox;
- item 3: the FIX-1 [OPEN] item of GLO v2 (§5 "Scope of NG", §6(f)). **This note takes item 3.**

**What is not claimed.** GLS₀ for the arc family, G1 and the linear-gap conjecture are not claimed. RX is an **abstract** example; no arc is claimed to realise it.

## 0. Setting
- Notation is as in GLO v2 (sha256 9b1d48be…faf40f; audit PASS-with-fixes; diff check PASS) and PTH v2.2.
  - L = F_q(X), q = Q², Q = 2^{m/2}, G = Gal(L^sep/L).
  - C, D ∈ L{τ} of degree a₂, P = C + Dτ^{m/2}, R_P = ker P.
  - φ is the Q-power on coefficients, and Λ(A) = CA + Dφ(A).
  - GLS₀ means Λ(A) = 0 has a nonzero solution in L^sep{τ}.
  - (N0) means c₀d₀c_{a₂}d_{a₂} ≠ 0, and y₀ = c₀/d₀.
- **The question (GLO v2 §6(f), FIX-1).** Does GLS₀ follow from the generic relation, for a G-stable W ⊂ R_P with 2a₂ < dim W ≤ (m−6)/3 and a unique (N0) relation line?

## 1. Lemma RW (G-fixed radicals force a trivial Kummer character) [P]
**Statement.** Assume (N0). Let W ⊂ R_P be an F₂-subspace, and put W^G := W ∩ L. If dim W^G > a₂ and GLS₀ holds, then:
- χ is trivial;
- the minimal twist A lies in L{τ};
- **y₀ = c₀/d₀ ∈ L^{*(Q−1)}**.

*Proof.*
1. **Setup.** Let A be a minimal solution. By PTH §4A (ML, valid over L^sep and L̄; GLO v2 R0) the minimal solutions form one F_Q-line, a₀ ≠ 0, and g(A) = Aχ(g) for g ∈ G, with χ(g) = g(a₀)/a₀.
2. **Intersection.** By MI (PTH §2, over L^sep), A(F_Q) ⊂ R_P has dimension m/2. Also dim R_P ≤ deg_τ P ≤ m/2 + a₂. So dim(W^G ∩ A(F_Q)) ≥ dim W^G − a₂ > 0.
3. **χ is trivial.** Pick 0 ≠ w = A(x) in that intersection. Then w = g(w) = A(χ(g)x), and A is injective on F_Q, so χ(g) = 1.
4. **Conclusion.** Hence a₀ ∈ L, and the τ⁰-equation c₀a₀ = d₀a₀^Q gives y₀ = a₀^{Q−1}. By GLO Theorem RLE, A = B·a₀ with B ∈ L{τ}. ∎

**Corollary RW′ (Kummer-divisibility test) [P].** Assume (N0) and dim W^G > a₂. If v_π(c₀/d₀) ≢ 0 (mod Q−1) at some place π of L (including ∞), then GLS₀ fails.

## 2. Theorem RX (a rational counterexample in the dimension range 2a₂ < dim W ≤ (m−6)/3 posed by GLO FIX-1) [P]
[v2: m7] dim W = 2a+1 is odd, so W is never an even-band ρ.
Let a ≥ 1, let m be even with a+1 ≤ m/2, and put **W := F₂[X]_{≤2a} = span_{F₂}(1, X, …, X^{2a})**, so ρ := dim W = 2a+1. Write E = (e₁ < … < e_{2a+2}) = (1, 2, …, 2^a, Q, 2Q, …, 2^aQ). Let M_l ∈ F₂[X] be the maximal minor of the ρ×(2a+2) matrix (X^{k·e_l})_{k=0..2a, l} with column l deleted. Put c_i := M_{i+1} and d_i := M_{a+2+i}, for i = 0..a.

**Statements.**
- **(i)** The relations of degree ≤ a on W over L (equivalently over L̄) form exactly the line L·(C, D). Every one of the 2a+2 coefficients is nonzero; in particular (N0) holds. The generic defect is a(W) = a.
- **(ii)** W is G-fixed (W ⊂ L), so it is G-stable, and W(α) ⊂ F_q for every α ∈ F_q.
- **(iii)** v_∞(y₀) = −Σ_{j=1}^{a}(j−1)2^{j−1} − a(Q − 2^a) ≡ 2^{a+1} − a − 2 (mod Q−1). Also 0 < 2^{a+1} − a − 2 < Q−1, so **y₀ ∉ L^{*(Q−1)}**.
- **(iv)** **GLS₀ fails:** no nonzero A ∈ L̄{τ} solves C·A = D·φ(A). Under (N0), every solution over L̄ lies over L^sep by GLO v2 Lemma FS(b), so RW′ covers L̄ [v2: m1]. In particular GLS₁ fails, and so Δ·Ω₁ ≢ 0 when a = 1 (GLO OB1). [C, referee] confirmed this independently of RW: Δ·Ω₁(β) ≠ 0 at random β ∈ GF(2^61), for m = 16, 18, 20.
- **(v) Dimension range** [v2: m7]. If m ≥ 6a+9, then 2a < dim W = 2a+1 ≤ (m−6)/3.
- **(vi) Pointwise real type, with density** [P, referee; adopted] [v2: FIX-1]. Let Z := {α ∈ F_q : M_l(α) = 0 for all l} be the common zero set of the cofactors.
  - **(vi-a)** For every α ∉ Z: dim W(α) = 2a+1, the F_q-relations of degree ≤ a on W(α) form the line spanned by (C_α, D_α) ≠ 0, and d_i(α) = κc_i(α)^Q with κ^{Q+1} = 1. That is, the specialisation is of real type. This uses no HFD input and no hypothesis on a(W(α)).
  - **(vi-b)** |Z| ≤ deg M_{2a+2} = Q[(2a−1)2^a − a + 1] + (a−1)2^{a+1} + 2 < 2a·2^a·Q. If m ≥ 6a+9, then |Z|/q < a·2^{−2a−4} ≤ 1/64, so real type holds at **more than 63q/64** points α ∈ F_q.
  - [C] For a = 1 and m = 16: 300/300 random α are of real type (owner).
  - [C, referee] An exhaustive check found real type at **every** α ∉ Z for (a, m) = (1,12), (1,16), (2,12). For a = 1, Z = F_Q exactly.
  - [C, referee] Samples: (2,22) 1500/1500; (3,28) 300/300.
  - v1's version of (vi) rested on HFD §1 [A]. HFD is stated for even ρ ≥ 4, which is outside this odd-dimensional setting, and v1 gave no density argument. It is replaced.

*Proof.*
1. **Generalised Vandermonde [P].** Take distinct integers k₁ < … < k_r and distinct positive integers f₁ < … < f_r. Then det(X^{k_j f_l}) over F₂ equals Σ_π X^{Σ_j k_j f_{π(j)}} reduced mod 2.
   - The sorted pairing (π = id) is the **unique** maximiser of Σ_j k_j f_{π(j)}. If π has j < j′ with f_{π(j)} > f_{π(j′)}, swapping the two values changes the sum by (k_{j′} − k_j)(f_{π(j)} − f_{π(j′)}) > 0.
   - Likewise the reversed pairing is the unique minimiser.
   - So the determinant is nonzero, with degree Σ k_j f_j and X-adic order Σ k_j f_{r+1−j}.
2. **(i) The relation line.** All M_l are such determinants (k = 0..2a), so all are nonzero. The ρ×(ρ+1) matrix therefore has rank ρ over L.
   - Its kernel is the line spanned by the cofactor vector (M_l)_l, by Laplace expansion of the matrix with a repeated row; there are no signs in characteristic 2.
   - A relation (C′, D′) of degree ≤ a is exactly a kernel vector, because Σ_i c′_i w^{2^i} + d′_i w^{Q2^i} = 0 on the basis X^k.
3. **(i) a(W) = a.** A relation of degree ≤ a−1 is a kernel vector of the ρ×2a matrix with exponents E′ = (1, …, 2^{a−1}, Q, …, 2^{a−1}Q). Its 2a×2a minor on rows k = 0..2a−1 is nonzero by step 1, so the kernel is 0. Over L̄ the kernel dimension is the same.
4. **(iii) The valuation.** c₀ = M₁ omits e₁ = 1, and d₀ = M_{a+2} omits e_{a+2} = Q. Pair k_j = j−1 with the sorted remaining exponents:
   - deg c₀ − deg d₀ = Σ_{j=1}^{a+1} (j−1)(e_{j+1} − e_j) = Σ_{j=1}^{a}(j−1)2^{j−1} + a(Q − 2^a);
   - the columns after position a+2 pair identically and cancel.
   - Modulo Q−1 (where Q ≡ 1), this is ((a−2)2^a + 2) + a(1 − 2^a) = −(2^{a+1} − a − 2).
   - So v_∞(y₀) = deg d₀ − deg c₀ ≡ 2^{a+1} − a − 2. This is ≥ 1 for a ≥ 1, and < 2^{a+1} ≤ Q, hence < Q−1 unless 2^{a+1} − a − 2 = Q−1. That is impossible: 2^{a+1} ≤ Q gives 2^{a+1} − a − 2 ≤ Q − 3.
5. **(iv)** W ⊂ R_P and W^G = W has dimension 2a+1 > a. Corollary RW′ at π = ∞ applies.
6. **(v)** is arithmetic.
7. **(vi)** [P, referee; adopted] [v2: FIX-1].
   - **(vi-a), rank.** Evaluation F₂[X] → F_q at α is a ring map, so the minors of N(α) := ((α^k)^{e_l})_{k,l} are the values M_l(α). For α ∉ Z, N(α) has rank 2a+1.
   - **(vi-a), independence.** w ↦ (w^{e_l})_l is F₂-linear. So an F₂-dependence among 1, α, …, α^{2a} would give a dependence among the rows of N(α). Hence dim W(α) = 2a+1.
   - **(vi-a), the relation line.** An F_q-relation of degree ≤ a on W(α) is a vector in ker N(α), by testing on the basis. ker N(α) is a line spanned by the evaluated cofactors (C_α, D_α) ≠ 0.
   - **(vi-a), real type.** The map σ(c, d) := (d̄, c̄), with x̄ = x^Q, preserves ker N(α): raise a relation to the Q-th power and use w^{Q²} = w on F_q.
     - σ is Q-semilinear with σ² = id. So σ(v) = μv with μ^{Q+1} = 1.
     - By Hilbert 90, some λ ∈ F_q^* has λv = (C′, C̄′) σ-fixed.
     - Then d_i(α) = λ^{Q−1}c_i(α)^Q, with κ := λ^{Q−1} satisfying κ^{Q+1} = 1.
   - **(vi-b), degree.** Z lies in the zero set of the nonzero polynomial M_{2a+2} (delete the largest exponent 2^aQ). By step 1 its degree is Σ_{j=0}^{a} j2^j + Q·Σ_{i=0}^{a−1}(a+1+i)2^i = (a−1)2^{a+1} + 2 + Q[(2a−1)2^a − a + 1]. This is < 2a·2^a·Q, since Q ≥ 2^{a+1}.
   - **(vi-b), density.** m ≥ 6a+9 with m even gives m ≥ 6a+10, so Q ≥ 2^{3a+5}. Then |Z|/q < 2a·2^a/Q ≤ a·2^{−2a−4} ≤ 1/64. ∎

**[C] rxcheck.py** (own code; `nice -n 19 python3 -I`; about 0.3 s):
- **(A)** Exact sparse F₂[X] minors for (a, m) ∈ {(1,16), (1,18), (1,20), (2,22), (2,24), (2,26), (3,28), (3,30)}. Every case confirms:
  - all minors are nonzero;
  - degree and order match step 1;
  - v_∞(y₀) equals the exact formula (−254, −510, −1022, −4090, −8186, −16378, −49138, −98290), with residues 1, 1, 1, 4, 4, 4, 11, 11 mod Q−1;
  - the cofactor identity holds;
  - there is no degree-(a−1) relation;
  - the band flag holds.
- **(B)** Pointwise real type, 300/300 (a = 1, m = 16, GF(2¹⁶)). For the referee's exhaustive version, see (vi).
- **(C), (D)** Searches for extra rational roots of P (a = 1): see §3.
- [v2: m6] Cosmetic: the script's docstring does not mention part D, and `partD` with its second `__main__` block comes after the first block. The output is correct and reproducible; the referee's rerun is byte-identical. The script is left unchanged, to keep its recorded hash.

## 3. The even band remains OPEN; partial evidence
- **Why RX does not reach the even band.** In the even band, a₂ ≤ a* < ρ/2 forces **ρ ≥ 2a₂ + 2**. [v2: m2] More sharply: EBR's a* = ρ − ⌈g/2⌉ with g ≥ ρ+3 gives a₂ ≤ a* ≤ ρ/2 − 2, so **ρ ≥ 2a₂ + 4**. That equals TCR's G1″ threshold 2a*+4. RX has ρ = 2a₂ + 1, where a relation of degree a₂ exists by counting alone (2a₂+2 unknowns, 2a₂+1 equations).
- **The refined question [OPEN].** Does GLS₀ follow for a G-stable W with 2a₂+2 ≤ dim W ≤ (m−6)/3 and a unique (N0) relation? The band-relevant case is 2a₂+4 ≤ dim W; dim W = 2a₂+2 and 2a₂+3 are intermediate [v2: m2]. Here the existence of the relation is itself a codimension-(ρ−2a₂−1) coincidence (GLO audit, [H] parameter count).
- **[P] Monomial W cannot reach the even band.** Assume a < m/2, so that the exponents in E are distinct [v2: m3]. If W is spanned by 2a+2 distinct monomials X^{k_j} (or by F_q-scaled monomials λ_jX^{k_j}, whose extreme term has coefficient Π_jλ_j^{e_{π(j)}} ≠ 0 [P, referee] [v2: m3]), then W has **no** relation of degree ≤ a: the square generalised Vandermonde determinant is nonzero by step 1. So monomial constructions stop at ρ = 2a+1.
- **[C] Extending RX by one rational root fails in the tested range.** RX would extend to ρ = 2a+2 by adding a rational root of the same P. For a = 1:
  - the F₂-kernel of P on F₂[X]_{≤48} has dimension exactly 3 (that is, W itself), for m = 16 and m = 18;
  - the F₂-kernel on F_q[X]_{≤6} (q = 2¹⁶) also has dimension 3.
  - So no such extension exists in these ranges.
  - [v2: m4] [C, referee K1] The Newton polygon at ∞ shows that any polynomial root of P has degree ≤ 2a. So these searches are **complete for polynomial roots** in F₂[X] and F_q[X]. There is no rational root with a pole at X = 0. Rational roots with poles at other finite places are **untested**.
  - [C, referee K2/K3] Further kernels: m = 20 on ≤64 and (a=2, m=22) on ≤40 (dimensions 3 and 5, i.e. W); F_q[X]_{≤10} (dimension 3).
- **[H] A possible mechanism.** In the even band the relation is a genuine coincidence. It might come with the twisted-half-field structure that GLS₀ asserts, which is what PTH (iii) gives pointwise when e = 0. No proof.

## 4. Consequences
- **(a) [P] The FIX-1 question as posed is answered negatively.** GLS₀ is not implied by the combination of:
  - the generic relation;
  - G-stability;
  - a unique (N0) relation line;
  - 2a₂ < dim W ≤ (m−6)/3;
  - rational specialisation W(α) ⊂ F_q;
  - real-type specialisation at more than 63q/64 points α (RX(vi), proved in v2) [v2: FIX-1].

  This holds even though W is G-fixed. Together with GLO's NG (W = R_P), there are now two abstract non-implications. Neither lies in the even band.
- **(b) [P] A new necessary test for GLS₀ (RW′).** Whenever dim W^G > a₂, c₀/d₀ must be a (Q−1)-th power in L, so all valuations must be ≡ 0 mod Q−1. This is a cheap test on B1's relation, complementing GLO's N1, AC, VO and Δ·Ω₁.
- **(c) [H] What this means for the GO route.** GO uses GLS₀ only to manufacture rational structure (W′ ⊂ W^rat). RX shows that rational W need not carry a twist: rationality of W does not imply GLS₀. Conversely, under GLS₀, rationality of W (with dim W^G > a₂) forces χ = 1 (RW) [v2: m5]. So the programme should not try to derive rationality only through GLS₀.
  - RX itself is not covered by TCR RS: dim W = 2a+1 < 2a+4, the G1″ threshold.
  - Nothing here is claimed about arcs.
- **(d) Status.** GO/GX/KB remain [COND] on GLS₀/GLS₁. The G1 reduction table (HANDBACK-2124Z §2) is unchanged.

## 5. Questions for Codex (packet EL, PENDING DIFF-CHECK)
- **(a)** In the even band, does B1's W have dim W^G > a₂ (for instance via WG)? If so, does c₀/d₀ pass RW′?
- **(b)** Do the arc data force ρ ≥ 2a₂+2 relations to come from twisted half-fields (the refined [OPEN] question of §3)?

## 6. Owner self-check; points for the audit
- **RW:** uses ML's line and χ-equivariance (PTH §4A, GO(a)), MI over L^sep, and dim R_P ≤ m/2 + a₂. If c₀ = 0, (N0) fails and RW′ is not applied.
- **Step 1 (uniqueness of the maximiser):** strictness needs distinct k_j and distinct f_l. Both hold, since the k_j are 0..2a and E consists of 2a+2 distinct values (2^a < Q).
- **Cofactor kernel:** standard for rank ρ in a ρ×(ρ+1) matrix over a field.
- **(iii) arithmetic:** Σ_{i=0}^{a−1} i·2^i = (a−2)2^a + 2. Checked exactly by [C] for a = 1, 2, 3.
- **(vi):** [v2: m8] after FIX-1, no condition on a(W(α)) is needed. The exceptional set Z is bounded by deg M_{2a+2}, and real type holds off Z via Hilbert 90 (referee argument, adopted).
- **Isolation and process:** own scripts only; no incoming scripts.

## 7. Scripts
`claude_archive/scripts/rxcheck.py` and `rxcheck.log`. Their sha256 values are recorded in PROGRESS.md (session 2, RX section). Run with `nice -n 19 python3 -I rxcheck.py`.

## 8. Change log v1 → v2 [v2]
| Item | Where | Change |
|---|---|---|
| FIX-1 | Title, RX(vi) + proof step 7, §4(a), §6 | The HFD §1 [A] citation (outside HFD's setting) is replaced by the referee's self-contained proof: real type off Z via σ-stability and Hilbert 90, and \|Z\| ≤ deg M_{2a+2}, giving real type at > 63q/64 points. Credited [P, referee; adopted]. "Almost every" replaced by the proved density. |
| m1 | RX(iv) | Cites GLO v2 FS(b) for the passage from L^sep to L̄; adds the referee's independent Δ·Ω₁ check. |
| m2 | §3 | The band has ρ ≥ 2a₂+4, equal to the G1″ threshold; the intermediate dimensions are noted. |
| m3 | §3 | Adds the hypothesis a < m/2; extends the bound to F_q-scaled monomials (referee). |
| m4 | §3 | The searches are complete for polynomial roots (referee K1); roots with poles at finite places ≠ 0 are untested; referee K2/K3 added. |
| m5 | §4(c) | "Logically independent" replaced by the two directions (RX and RW). |
| m6 | §2 [C] | Cosmetic issues in the script recorded; script unchanged. |
| m7 | §2 heading, RX(v) | "Band dimension" replaced by "the dimension range posed by GLO FIX-1 (odd, never an even-band ρ)". |
| m8 | §6 | The (vi) self-check is updated. |

No other proof was changed. The referee's checks are in `audit_RX_checks/`. Scripts are unchanged.
