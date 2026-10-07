# GLO's FIX-1 [OPEN] question, answered negatively as posed: W = F₂[X]_{≤2a} (rational, G-stable, dim 2a+1 ≤ (m−6)/3, unique (N0) relation of degree a, real type at almost every α) has NO generic Lang twist. The cause is a Kummer-divisibility obstruction for G-fixed radicals (Lemma RW). The even-band range dim W ≥ 2a₂+2 remains OPEN. (Owner note v1, cloud session, 7 Oct 2026, 22:17Z.)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac; no mailbox access).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS.** v1, **NOT AUDITED. HOLD.** Needs the independent agent audit (arranged by the coordinator) before any packet. It is **not** in the outbox.

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

## 2. Theorem RX (a rational counterexample of band dimension) [P]
Let a ≥ 1, let m be even with a+1 ≤ m/2, and put **W := F₂[X]_{≤2a} = span_{F₂}(1, X, …, X^{2a})**, so ρ := dim W = 2a+1. Write E = (e₁ < … < e_{2a+2}) = (1, 2, …, 2^a, Q, 2Q, …, 2^aQ). Let M_l ∈ F₂[X] be the maximal minor of the ρ×(2a+2) matrix (X^{k·e_l})_{k=0..2a, l} with column l deleted. Put c_i := M_{i+1} and d_i := M_{a+2+i}, for i = 0..a.

**Statements.**
- **(i)** The relations of degree ≤ a on W over L (equivalently over L̄) form exactly the line L·(C, D). Every one of the 2a+2 coefficients is nonzero; in particular (N0) holds. The generic defect is a(W) = a.
- **(ii)** W is G-fixed (W ⊂ L), so it is G-stable, and W(α) ⊂ F_q for every α ∈ F_q.
- **(iii)** v_∞(y₀) = −Σ_{j=1}^{a}(j−1)2^{j−1} − a(Q − 2^a) ≡ 2^{a+1} − a − 2 (mod Q−1). Also 0 < 2^{a+1} − a − 2 < Q−1, so **y₀ ∉ L^{*(Q−1)}**.
- **(iv)** **GLS₀ fails:** no nonzero A ∈ L̄{τ} solves C·A = D·φ(A). In particular GLS₁ fails, and so Δ·Ω₁ ≢ 0 when a = 1 (GLO OB1).
- **(v) Band dimension.** If m ≥ 6a+9, then 2a < dim W = 2a+1 ≤ (m−6)/3.
- **(vi) Pointwise real type** [P via HFD §1 [A]; C].
  - At every α ∈ F_q with dim W(α) = 2a+1, a(W(α)) = a and (C_α, D_α) ≠ 0, the specialisation is a nonzero multiple of a real relation (C′, κC̄′). This holds because the relation space of degree ≤ a on W(α) is a line containing a real relation, as a < ρ/2.
  - [C] For a = 1 and m = 16: **300/300** random α are of real type, with d_i(α) = κc_i(α)^Q and κ^{Q+1} = 1.

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
7. **(vi), first clause.** This is HFD §1 [A] applied to W(α), with a(W(α)) = a < (2a+1)/2. The specialised (C_α, D_α) is a nonzero relation of degree ≤ a, so it lies on the real line. ∎

**[C] rxcheck.py** (own code; `nice -n 19 python3 -I`; about 0.3 s):
- **(A)** Exact sparse F₂[X] minors for (a, m) ∈ {(1,16), (1,18), (1,20), (2,22), (2,24), (2,26), (3,28), (3,30)}. Every case confirms:
  - all minors are nonzero;
  - degree and order match step 1;
  - v_∞(y₀) equals the exact formula (−254, −510, −1022, −4090, −8186, −16378, −49138, −98290), with residues 1, 1, 1, 4, 4, 4, 11, 11 mod Q−1;
  - the cofactor identity holds;
  - there is no degree-(a−1) relation;
  - the band flag holds.
- **(B)** Pointwise real type, 300/300 (a = 1, m = 16, GF(2¹⁶)).
- **(C), (D)** Searches for extra rational roots of P (a = 1): see §3.

## 3. The even band remains OPEN; partial evidence
- **Why RX does not reach the even band.** In the even band, a₂ ≤ a* < ρ/2 forces **ρ ≥ 2a₂ + 2**. RX has ρ = 2a₂ + 1, where a relation of degree a₂ exists by counting alone (2a₂+2 unknowns, 2a₂+1 equations).
- **The refined question [OPEN].** Does GLS₀ follow for a G-stable W with 2a₂+2 ≤ dim W ≤ (m−6)/3 and a unique (N0) relation? Here the existence of the relation is itself a codimension-(ρ−2a₂−1) coincidence (GLO audit, [H] parameter count).
- **[P] Monomial W cannot reach the even band.** If W is spanned by 2a+2 distinct monomials X^{k_j}, then W has **no** relation of degree ≤ a: the square generalised Vandermonde determinant is nonzero by step 1. So monomial constructions stop at ρ = 2a+1.
- **[C] Extending RX by one rational root fails in the tested range.** RX would extend to ρ = 2a+2 by adding a rational root of the same P. For a = 1:
  - the F₂-kernel of P on F₂[X]_{≤48} has dimension exactly 3 (that is, W itself), for m = 16 and m = 18;
  - the F₂-kernel on F_q[X]_{≤6} (q = 2¹⁶) also has dimension 3.
  - So no such extension exists in these ranges.
- **[H] A possible mechanism.** In the even band the relation is a genuine coincidence. It might come with the twisted-half-field structure that GLS₀ asserts, which is what PTH (iii) gives pointwise when e = 0. No proof.

## 4. Consequences
- **(a) [P] The FIX-1 question as posed is answered negatively.** GLS₀ is not implied by the combination of:
  - the generic relation;
  - G-stability;
  - a unique (N0) relation line;
  - 2a₂ < dim W ≤ (m−6)/3;
  - rational specialisation W(α) ⊂ F_q;
  - real-type specialisation at almost every α.

  This holds even though W is G-fixed. Together with GLO's NG (W = R_P), there are now two abstract non-implications. Neither lies in the even band.
- **(b) [P] A new necessary test for GLS₀ (RW′).** Whenever dim W^G > a₂, c₀/d₀ must be a (Q−1)-th power in L, so all valuations must be ≡ 0 mod Q−1. This is a cheap test on B1's relation, complementing GLO's N1, AC, VO and Δ·Ω₁.
- **(c) [H] What this means for the GO route.** GO uses GLS₀ only to manufacture rational structure (W′ ⊂ W^rat). RX shows that rational W need not carry a twist. So "W rational" and "GLS₀" are logically independent inputs, and the programme should not try to derive the former only through the latter.
  - RX itself is not covered by TCR RS: dim W = 2a+1 < 2a+4, the G1″ threshold.
  - Nothing here is claimed about arcs.
- **(d) Status.** GO/GX/KB remain [COND] on GLS₀/GLS₁. The G1 reduction table (HANDBACK-2124Z §2) is unchanged.

## 5. Questions for Codex (for a later packet, only after audit)
- **(a)** In the even band, does B1's W have dim W^G > a₂ (for instance via WG)? If so, does c₀/d₀ pass RW′?
- **(b)** Do the arc data force ρ ≥ 2a₂+2 relations to come from twisted half-fields (the refined [OPEN] question of §3)?

## 6. Owner self-check; points for the audit
- **RW:** uses ML's line and χ-equivariance (PTH §4A, GO(a)), MI over L^sep, and dim R_P ≤ m/2 + a₂. If c₀ = 0, (N0) fails and RW′ is not applied.
- **Step 1 (uniqueness of the maximiser):** strictness needs distinct k_j and distinct f_l. Both hold, since the k_j are 0..2a and E consists of 2a+2 distinct values (2^a < Q).
- **Cofactor kernel:** standard for rank ρ in a ρ×(ρ+1) matrix over a field.
- **(iii) arithmetic:** Σ_{i=0}^{a−1} i·2^i = (a−2)2^a + 2. Checked exactly by [C] for a = 1, 2, 3.
- **(vi):** the clause needs a(W(α)) = a exactly at α. Only the [C] sample checks how often that holds; the theorem does not depend on it.
- **Isolation and process:** own scripts only; no incoming scripts.

## 7. Scripts
`claude_archive/scripts/rxcheck.py` and `rxcheck.log`. Their sha256 values are recorded in PROGRESS.md (session 2, RX section). Run with `nice -n 19 python3 -I rxcheck.py`.
