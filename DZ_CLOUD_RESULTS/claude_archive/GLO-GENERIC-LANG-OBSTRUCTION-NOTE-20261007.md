# Even ρ, structured branch, target GLS₀: the generic Lang twist exists iff a rational Lang equation over L = F_q(X) is solvable (Theorem RLE). Solutions are classified exactly by a finite obstruction map (Theorem OB). For a₂ = 1, GLS₁ is the single identity Δ·Ω₁ ≡ 0. There is a valuation obstruction (VO), and an explicit pair (C, D) passes every §4A(iii) test of PTH but has NO generic twist (Example NG). So GLS₀ is not a consequence of the generic relation. (Owner note v1, cloud session, 7 Oct 2026, 21:41Z.)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac; no mailbox access).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS.** v1, **NOT AUDITED. HOLD.** Needs the independent agent audit (arranged by the coordinator) before any packet. It is **not** in the outbox.
**Scope.** This note addresses HANDBACK-20261007T2124Z §3, item 2 (GLS₀/GLS₁: the generic Lang twist). Item 1 (mailbox/ACK hygiene) needs the device and is untouched. **GLS₀ for the arc family remains OPEN.** This note does not prove it. It gives an exact reformulation, new necessary conditions and a proof that arc input is unavoidable. **G1 and the linear-gap conjecture are not claimed.**

## 0. Setting and notation
- **Fields and maps.**
  - m is even, Q = 2^{m/2}, q = Q².
  - L = F_q(X), K ∈ {L^sep, L̄}, and G = Gal(L^sep/L).
  - K{τ} is the ring of 2-linearised polynomials (τc = c²τ), and K{{τ}} is the ring of skew power series.
  - φ(Σa_kτ^k) := Σa_k^Qτ^k, so φ(A) = A^{(Q)} in PTH's notation. φ is an injective ring endomorphism, and the identity on F_Q{{τ}}.
- **The equation (as in PTH §4).**
  - C = Σ_{i≤a₂}c_iτ^i and D = Σ_{i≤a₂}d_iτ^i lie in L{τ}, with P = C + Dτ^{m/2}.
  - The Lang operator is **Λ(A) := C·A + D·φ(A)** (characteristic 2).
  - Coefficientwise: Λ(A)_k = Σ_i (c_i a_{k−i}^{2^i} + d_i a_{k−i}^{Q2^i}).
  - Sol := {A ∈ K{τ} : Λ(A) = 0}, and Sol_{≤n} is its degree-≤ n part.
  - **GLS₀** ⟺ Sol ≠ 0 over L^sep. **GLS₁** additionally asks for deg A ≤ a₂ (PTH §4).
- **Right linearity.** Λ(AE) = Λ(A)E for every E ∈ F_Q{{τ}}, because φ(E) = E. So Sol is a right F_Q{τ}-module.
- **Normalisation (N0).** c₀d₀c_{a₂}d_{a₂} ≠ 0. Put y₀ := c₀/d₀ and Δ₁ := c₁d₀² + d₁c₀² (with c₁ = d₁ = 0 allowed when a₂ = 0).
- **Remark R0 (when (N0) holds).**
  - **[P]** If deg C ≠ deg D, or exactly one of c₀, d₀ is zero, then Sol = 0 (PTH §4A, Lemma ML). So (N0) loses nothing except the case c₀ = d₀ = 0, which this note does not treat.
  - **[COND (B1a⁺), (B1b), HFD §1 [A]]** For the arc's generic relation, (N0) holds if some nonfocus α has a(V_α) = a₂ and (C_α, D_α) ≠ 0 after content removal. There the specialisation is a multiple of a real relation (C′, κC̄′), and HFD §1 gives c′₀c′_{a₂} ≠ 0. The input-step degree bound of PTH §4 makes such α plentiful.
- **Theorems with no condition attached are [P] for every C, D over L satisfying (N0).**

## 1. Formal solutions and the τ-adic Galois representation
### Lemma FS (formal solutions) [P]
Assume (N0).
- **(a)** There is a formal solution A₀ = Σα_kτ^k ∈ L^sep{{τ}} with α₀ ≠ 0. The formal solutions in L̄{{τ}} are exactly A₀·F_Q{{τ}}, and A₀E = 0 only for E = 0.
- **(b)** Every polynomial solution over L̄ has coefficients in L^sep. No degree bound is needed. This strengthens PTH §4A(iv), which needed deg A < m/2.

*Proof.*
1. **The equations.** The equation Λ(A)_k = 0 reads ℓ₀(a_k) = r_k(a₀,…,a_{k−1}), where ℓ₀(a) := d₀a^Q + c₀a and r_k := Σ_{i≥1}(c_i a_{k−i}^{2^i} + d_i a_{k−i}^{Q2^i}).
2. **Kernel and separability.** ℓ₀ is F₂-linear and separable (its derivative is c₀ ≠ 0), so ℓ₀(T) − r is separable for every r. Its kernel is α₀F_Q, where α₀^{Q−1} = y₀; this has Q−1 separable roots, as Q−1 is odd.
3. **Construction.** Choose α₀, then α_k ∈ L^sep(r_k) recursively. This gives A₀ over L^sep.
4. **Completeness.** Let A be any formal solution. Suppose E^{(k)} ∈ F_Q[τ]_{<k} has been chosen with B := A − A₀E^{(k)} ≡ 0 mod τ^k.
   - B is a solution by right linearity. Its τ^k-equation is ℓ₀(b_k) = 0, so b_k = α₀e_k with e_k ∈ F_Q.
   - The τ^k-coefficient of A₀e_kτ^k is α₀e_k.
   - Put E^{(k+1)} := E^{(k)} + e_kτ^k, and pass to the τ-adic limit.
5. **Uniqueness.** If E ≠ 0 has least nonzero index i, then (A₀E)_i = α₀e_i ≠ 0.
6. **(b)** Every polynomial solution is a formal solution A₀E with E ∈ F_Q{{τ}}. ∎

### Proposition GR (τ-adic Galois representation) [P]
- For g ∈ G, g(A₀) = A₀E_g for a unique unit E_g ∈ F_Q{{τ}}^×. The map ρ₀: g ↦ E_g is a group homomorphism.
- Its constant term is the Kummer character χ₀(g) = g(α₀)/α₀ of y₀. Replacing A₀ by A₀U conjugates ρ₀ by U.
- **Corollary AC (tower collapse).** GLS₀ ⇒ ρ₀(G) = U·χ(G)·U^{−1}, a cyclic group of order |χ(G)| dividing Q−1.
  - So the field L_∞ := L(α₀, α₁, …) equals L(α₀), with [L(α₀):L] = |χ(G)|.
  - The F_Q-Artin–Schreier layers of the formal-solution tower must all be trivial.

*Proof.*
1. **Homomorphism.** g commutes with Λ (C, D are over L) and g(α₀) ≠ 0, so FS(a) gives g(A₀) = A₀E_g. Then gh(A₀) = g(A₀E_h) = A₀E_gE_h.
2. **Conjugation under GLS₀.** Let A be a minimal polynomial solution. PTH §4A (ML) gives a₀ ≠ 0 and g(A) = Aχ(g). Write A = A₀U with U a unit; then U^{−1}E_gU = χ(g).
3. **The tower.** ker ρ₀ is the subgroup fixing every α_k, so Gal(L_∞/L) ≅ ρ₀(G). ∎

## 2. Theorem OB (the exact finite obstruction) [P]
**Definition.** Assume (N0) and fix A₀ as in FS. For n ≥ 0 define the F₂-linear map
Ob_n : F_Q[τ]_{≤n} → K^{a₂}, Ob_n(E) := ( Λ((A₀E)_{≤n})_k )_{k=n+1}^{n+a₂}.
Here (·)_{≤n} is truncation.

**Theorem OB.** E ↦ (A₀E)_{≤n} is an F₂-linear bijection ker Ob_n → Sol_{≤n}. It is compatible with right multiplication by F_Q. In particular dim_{F₂} Sol_{≤n} ≤ (n+1)m/2, and GLS₀ ⟺ ∃n: ker Ob_n ≠ 0.

*Proof.*
1. **Truncations solve the low equations.** Λ(T)_k depends only on t₀,…,t_k. So for T = (A₀E)_{≤n}, Λ(T)_k = Λ(A₀E)_k = 0 for k ≤ n. Also Λ(T)_k = 0 for k > n+a₂ by degree. Hence T ∈ Sol ⟺ Ob_n(E) = 0.
2. **Surjectivity.** A ∈ Sol_{≤n} is a formal solution, so A = A₀E_∞ (FS). Then A = (A₀E_∞)_{≤n} = (A₀E)_{≤n} with E := (E_∞)_{≤n}.
3. **Injectivity.** This is FS(a)'s least-index argument. ∎

**Lemma TB (solutions at ∞) [P].** For n ≥ a₂−1, Ob_n(E) = λ(top_n(A₀E)).
- top_n(T) := (t_{n−a₂+1}, …, t_n).
- λ is the fixed, upper-triangular map with λ(t)_k = Σ_{j=k}^{a₂}(c_{a₂+k−j}t_j^{2^{a₂+k−j}} + d_{a₂+k−j}t_j^{Q2^{a₂+k−j}}), for k = 1..a₂.
- Over L̄, |ker λ| = Q^{a₂}. Solve top-down: each step is c_{a₂}s + d_{a₂}s^Q = r in s = t^{2^{a₂}}.
- So polynomial solutions are exactly the formal solutions at 0 whose top block is a truncated formal solution at ∞.

**[C] glocheck.py T3.** a₂ = 2, n ∈ {1, 2}, Q = 4, F = GF(2⁶). Note F_{16} ⊄ F, so the q-Frobenius is not the identity on F.
- Exhaustive layered search of Sol_{≤n} over F was compared with the count from Theorem OB.
- 32 instances per seed (half with a planted solution), seeds 1 and 7: **0 mismatches**.

## 3. Theorem RLE (GLS₀ is a rational problem over L) [P]
Assume (N0). The following are equivalent:
- **(i) GLS₀:** some A ∈ L^sep{τ}∖0 has C·A = D·φ(A).
- **(ii)** Some B ∈ L{τ} with b₀ = 1 satisfies **C·B = D·φ(B)·y₀**, where y₀ = c₀/d₀ is right multiplication by a scalar.
  - Coefficientwise: Σ_i c_i b_{k−i}^{2^i} = y₀^{2^k} Σ_i d_i b_{k−i}^{Q2^i} for all k.

Moreover:
- the minimal-degree B in (ii) is **unique**;
- the minimal solutions in (i) are exactly B·a₀·ζ, with a₀^{Q−1} = y₀ and ζ ∈ F_Q^*;
- χ is the Kummer character of y₀, as in PTH §4A(ii).

*Proof.*
1. **(i)⇒(ii).** Take A minimal. ML gives a₀ ≠ 0, the line property, and g(A) = Aχ(g).
   - So g(a_k) = a_kχ(g)^{2^k} = a_k·g(a₀^{2^k})/a₀^{2^k}, and b_k := a_k/a₀^{2^k} ∈ (L^sep)^G = L.
   - Then A = B·a₀, since τ^k a₀ = a₀^{2^k}τ^k. The τ⁰-equation gives a₀^{Q−1} = y₀.
   - So C·B·a₀ = D·φ(B)·a₀^Q = (D·φ(B)·y₀)·a₀. Cancel the unit a₀ on the right.
2. **(ii)⇒(i).** A := B·a₀ gives C·A = D·φ(B)·y₀a₀ = D·φ(B)·a₀^Q = D·φ(A).
3. **Uniqueness.** Two minimal normalised B give minimal A, A′ with A′ = Aζ. Comparing constant terms gives ζ = 1. ∎

**Lemma RD (rigidity of the rational recursion) [P].** At step k ≥ 1, (ii) asks for b_k ∈ L with y₀^{2^k−1}b_k^Q + b_k = s_k, where s_k ∈ L is determined by b₀,…,b_{k−1}.
- The L-roots form an empty set, a single point, or a coset of size Q.
- They form a coset of size Q iff y₀^{2^k−1} ∈ L^{*(Q−1)}.

*Proof.* The difference of two roots solves y₀^{2^k−1}b^{Q−1} = 1. ∎

**Corollary N1 (first-step necessary condition, any a₂ ≥ 1) [P].**
GLS₀ ⇒ **y₀b^Q + b = Δ₁/(c₀d₀²) has a root b ∈ L.**
- This is the k = 1 equation, divided by c₀ = d₀y₀; only i ≤ 1 enters it.
- If B = 1 (degree 0), then Δ₁ = 0 and b = 0.

**[C] glovo.py.** For the TX-like family A = X + τ:
- C = X^{Q+1}(1+X^{Q−1}) + τ and D = X²(1+X^{Q−1}) + τ give C·A = D·φ(A).
- B = 1 + X^{−2}τ ∈ L{τ} satisfies (ii) with y₀ = X^{Q−1}, for Q = 4, 8, 16.
- A negative control (B = 1 + X^{−3}τ, 1 + (1 + X^{−2})τ) correctly fails.

## 4. The case a₂ = 1: explicit obstruction [P]
Assume (N0) with a₂ = 1, and let a_top satisfy a_top^{2(Q−1)} = c₁/d₁. Then Ker λ = a_topF_Q.

**Corollary OB1.**
- **(a) Span criterion.** For every n, Sol_{≤n} ≠ 0 ⟺ **a_top ∈ span_{F_Q}(α₀, …, α_n)**, where K is an F_Q-space by multiplication. So GLS₀ ⟺ a_top ∈ Σ_{j≥0} α_jF_Q.
- **(b) n = 0:** ⟺ Δ := Δ₁ = c₁d₀² + d₁c₀² = 0.
- **(c) GLS₁ (n = 1):** ⟺ **Δ·Ω₁ = 0**, where Ω₁ := c₀⁴d₁^QΔ^{Q−1} + c₁d₀^{4Q}.
  - Equivalently: Δ = 0, or Δ ≠ 0 and (d₁Δ/d₀⁴)^{Q−1} = c₁d₀⁴/(d₁c₀⁴), a Kummer condition in L.

*Proof.*
1. **(a)**
   - (A₀E)_n = Σ_{i≤n} α_{n−i}e_i^{2^{n−i}}. As E varies, this ranges over V_n := Σ_{j≤n} α_jF_Q, since e ↦ e^{2^{n−i}} permutes F_Q. V_n is F_Q-stable.
   - Ob_n(E) = c₁t² + d₁t^{2Q} with t = (A₀E)_n, and its kernel is a_topF_Q.
   - (⇐) Take E with t(E) = a_top.
   - (⇒) A nonzero solution of exact degree d ≤ n has top coefficient a_d ∈ a_topF_Q^*, by its τ^{d+1}-equation. Theorem OB gives a_d ∈ V_d ⊂ V_n.
2. **(b)** a_top ∈ F_Qα₀ ⟺ (a_top/α₀)^{2(Q−1)} = 1 ⟺ c₁/d₁ = y₀².
3. **(c), the reduction.** Write α₁ = α₀β. Using d₀α₀^Q = c₀α₀, the τ¹-equation becomes β^Q + β = s := α₀Δ/(c₀d₀²).
   - Put γ := a_top/α₀ and w := γ^{Q−1}. Then w² = c₁d₀²/(d₁c₀²) and (w+1)² = Δ/(d₁c₀²).
   - If Δ = 0, (b) applies.
   - If Δ ≠ 0, then s ≠ 0 and γ ∉ F_Q. So a_top ∈ V₁ ⟺ γ = x + x′β with x ∈ F_Q, x′ ∈ F_Q^*. Applying T ↦ T^Q + T, this holds ⟺ (γ^Q+γ)/s ∈ F_Q^*. That is ⟺ (γ(w+1)/s)^{Q−1} = 1.
4. **(c), the algebra.** Use s^{Q−1} = y₀Δ^{Q−1}/(c₀d₀²)^{Q−1}, square (which is injective), and substitute w² and (w+1)². The result is c₁d₀^{4Q} = c₀⁴d₁^QΔ^{Q−1}, i.e. Ω₁ = 0.
5. **Combining.** If Δ = 0 then Ω₁ = c₁d₀^{4Q} ≠ 0, so the two cases combine as Δ·Ω₁ = 0. ∎

**Proposition PV (why pointwise solvability is automatic) [P].** Suppose c_i ∈ F_q and d_i = κc_i^Q with κ^{Q+1} = 1 (real type, as at a nonfocus with a(V_α) = a₂ by HFD §1). Then Δ·Ω₁ = 0.
*Proof.*
1. Δ = κδ′ with δ′ := κc₁c₀^{2Q} + c₁^Qc₀².
2. Since x^q = x on F_q, δ′^Q = κ^Qδ′. So if Δ ≠ 0, then Δ^{Q−1} = κ^{2Q−1}.
3. Hence Ω₁ = c₀⁴c₁(κ^{3Q−1} + κ^{4Q}) = 0, because κ^{Q+1} = 1. ∎

The pointwise identity is a **q-Frobenius = identity** phenomenon (Δ/κ is F_Q-rational up to κ). It has no generic analogue over L. Its shape is the Hermitian one:
- every x ∈ F_q gives Q solutions b ∈ F_q of b^Q + b = x^{Q+1}, because x^{Q+1} ∈ F_Q = Tr_{F_q/F_Q}(F_q) [P];
- yet x^{Q+1} ∉ ℘_Q(F̄_q(x)), because the Hermitian curve is irreducible of genus Q(Q−1)/2 [A, standard].

The analogy is [H].

**[C] glocheck.py T1/T2.** Seeds 1 and 7.
- **T1 (Corollary OB1).**
  - Fields: (Q, N) = (4, 6), (8, 9), (4, 10), none containing F_{Q²}, plus the control (8, 12).
  - 100 instances per seed (half planted, so both outcomes occur).
  - Checked: exhaustive "nonzero solution of degree ≤ 1 exists" ⟺ Δ·Ω₁ = 0 ⟺ span criterion, and the solution count equals the count from Theorem OB.
  - Result: **0 mismatches**.
- **T2 (PV).** Q = 4, 8, 16, 32 over F_{Q²}, with 300 random real-type pairs each: **0 failures**.

**Proposition TH (the counting threshold, a₂ = 1) [P].**
- **Setup.** Normalise C, D to have coefficients in F_q[X], and let δ := max deg c_i, d_i.
- **Degree bound.** deg_X(Δ·Ω₁) ≤ 3δ + (4Q+1)δ = (4Q+4)δ. Q-th powers commute with evaluation at α ∈ F_q, and Δ·Ω₁ is homogeneous under (C, D) ↦ λ(C, D).
- **Statement.** If Δ·Ω₁ ≢ 0, then at most (4Q+4)δ values α ∈ F_q have (C_α, D_α) a nonzero multiple of a real-type pair (by PV).
- **Consequence.** Counting yields GLS₁ only when δ < q/(4Q+4) < Q/4.
- **[H]** The Moore-minor scale of the PTH §4 input step suggests δ of order u·3(Q+1) ≈ (3/4)RQ for a₂ = 1. That misses the threshold by a factor ≈ 3R. This quantifies the "G1 obstruction" (PTH §5) for a₂ = 1.

## 5. Valuation obstruction and Example NG
### Proposition VO [P]
Assume (N0). Let v be a valuation of L̄ (ℚ-valued, extending one of L). Put θ := (v(c₀) − v(d₀))/(Q−1) and θ_top := (v(c_{a₂}) − v(d_{a₂}))/((Q−1)2^{a₂}). Suppose:
- for every 1 ≤ i ≤ a₂ with c_i ≠ 0: v(c_i) + 2^iθ ≥ v(c₀) + θ;
- for every 1 ≤ i ≤ a₂ with d_i ≠ 0: v(d_i) + Q2^iθ ≥ v(c₀) + θ.

Then every coefficient of every formal solution has v ≥ θ. Hence **if θ_top < θ, then Sol = 0 over L̄: GLS₀ fails.**

*Proof.*
1. **Induction.** Suppose v(a_j) ≥ θ for all j < k. Then v(r_k) ≥ v(c₀) + θ.
2. **Newton polygon.** The polygon of d₀T^Q + c₀T + r_k has vertices (0, v(r_k)), (1, v(c₀)), (Q, v(d₀)).
   - The last edge has slope −θ, and the first slope is ≤ −θ.
   - So the root valuations are v(r_k) − v(c₀) ≥ θ (one root) and θ (the other Q−1 roots).
3. **Contradiction.** A nonzero polynomial solution of degree n has a_n^{(Q−1)2^{a₂}} = c_{a₂}/d_{a₂}. So v(a_n) = θ_top < θ, a contradiction. ∎

**Corollary DO (degree test at ∞) [P].** Take polynomial coefficients and v = v_∞. GLS₀ fails if all of the following hold:
- deg d₀ > deg c₀;
- deg c_i ≤ deg c₀ + (2^i−1)θ and deg d_i ≤ deg c₀ + (Q2^i−1)θ for 1 ≤ i ≤ a₂, where θ = (deg d₀ − deg c₀)/(Q−1);
- deg d_{a₂} − deg c_{a₂} < 2^{a₂}(deg d₀ − deg c₀).

The same test applies at any finite place π, with v_π in place of −deg.

### Example NG (no generic twist) [P]
Take C = 1 + τ and D = X + τ (any even m), so P = 1 + τ + Xτ^{m/2} + τ^{m/2+1}.

**What NG satisfies.**
- **(N0)** holds.
- **PTH §4A(iii)'s necessary tests all pass.** deg C = deg D = 1; c₀, d₀ ≠ 0; c₀/d₀ = 1/X ∈ L; c₁/d₁ = 1 ∈ L².
- **W := ker P** (dim m/2+1 > 2a₂; P is separable since its constant term is 1) has **a(W) = 1**, and (C, D) is its **unique** relation of degree ≤ 1, up to scalar.
  - A degree-0 relation would force W ⊂ ker(c + dτ^{m/2}), which has dimension m/2.
  - Any relation P′ of degree ≤ m/2+1 that vanishes on ker P is a left multiple eP, with e a scalar.

**Why there is no twist.** VO at v_∞ gives θ = 1/(Q−1) > θ_top = 0; hypothesis (ii) holds trivially. **So Sol = 0 over L̄ in every degree: GLS₀ fails.**

**[C] glovo.py.**
- The VO hypotheses for NG are confirmed for Q = 4, 8, 16.
- On the TX-like family (where a solution exists), VO is correctly not triggered at v_∞ or at v₀.

**Scope of NG.** NG is abstract, like TX in RBL. It does not model the arc inputs: rational specialisation W(α) ⊂ F_q on N, (B1a⁺) pole bounds, STT, MRL. Its message is precise:
- **GLS₀ does not follow from the generic relation C(w) = D(w^Q) on a ρ-space W with ρ > 2a₂, nor from PTH's necessary tests.**
- Any proof of GLS₀ must use arc data beyond the generic relation.

## 6. Consequences for the G1 programme
- **(a) [P] The status of GLS₀ is clarified, not settled.** GLS₀ ⟺ RLE over L (Theorem RLE). Its obstruction is exactly computable (Theorem OB). It is not implied by the generic relation (NG). So the HANDBACK's assessment ("arc input is the likely route") is now **necessary**, not just likely.
- **(b) [P] New necessary conditions for GLS₀**, testable on B1's generic relation once Codex supplies (C, D) or its valuations:
  - **N1:** a root b ∈ L of y₀b^Q + b = Δ₁/(c₀d₀²);
  - **AC:** L(α₀, α₁, …) = L(α₀);
  - **¬VO** at every place, in particular at ∞ and at the poles of B1;
  - for a₂ = 1, **Δ·Ω₁ ≡ 0** (this is GLS₁).
- **(c) [P] PTH §4A(iii)'s tests are necessary but not sufficient** (NG).
- **(d) [P+H] Degree counting cannot supply GLS₁ at a₂ = 1** unless δ < Q/4 (TH). The pointwise truth (PV) is a q-Frobenius/Hermitian-type identity [H for the analogy].
- **(e) Routes that are unaffected.** GO/GX/KB are unchanged; they remain [COND] on GLS₀/GLS₁. The G1 reduction table in HANDBACK §2 is unchanged.
- **(f) [OPEN]**
  - GLS₀/GLS₁ for the arc family;
  - an ∞-side analogue of VO (via the adjoint operator);
  - general-a₂ closed forms beyond Theorem OB.

## 7. Questions for Codex (for a later packet, only after audit)
- **(a)** For B1's generic relation (C, D):
  - What are v_∞ and the pole valuations of c₀, d₀, c_{a₂}, d_{a₂}?
  - Does Corollary DO / Proposition VO trigger? If so, the GO/GX route is closed for that family, and G1 needs another route.
- **(b)** Does STT/MRL ("L = S² + tS") produce B ∈ L{τ} with C·B = D·φ(B)·y₀ (Theorem RLE)? Or at least the first-step root of N1?
- **(c)** For a₂ = 1 cells: is Δ·Ω₁ ≡ 0 for B1's relation?

## 8. Owner self-check; points for the audit
- **FS:** ℓ₀ is separable because c₀ ≠ 0. Completeness uses only right F_Q{{τ}}-linearity, which holds because φ fixes F_Q.
- **OB:** Λ(T)_k depends only on t_{≤k}. Truncation is F₂-linear. Injectivity uses the least-index argument.
- **TB:** λ is independent of n (for n ≥ a₂−1). |ker λ| = Q^{a₂} over L̄, which is perfect.
- **RLE:** uses ML (PTH §4A, audited chain) for a₀ ≠ 0 and the line property. The converse direction is unconditional.
- **OB1(c):** the algebra is re-derived in §4, step 4, and checked by [C] T1.
  - Points to audit: the squaring step, the case split on Δ, and that Δ = 0 ⇒ Ω₁ ≠ 0 under (N0).
- **PV:** uses x^q = x on F_q and κ^{Q+1} = 1.
- **VO:** a standard Newton polygon argument. Points to audit: ties, θ < 0, and zero coefficients.
- **NG:** VO at ∞. a(W) = 1 and uniqueness use the separability of P and right division.
- **R0:** the only [COND] item. It is not used by any [P] statement.

## 9. Scripts and computations
All are own code, in `claude_archive/scripts/`. Run with `nice -n 19 python3 -I`. No incoming scripts were executed.

| File | sha256 | Content |
|---|---|---|
| glocheck.py | e39894a42da9d03bac0ee22d62d45e4b544253225b4d96f7ea9867afe066a9d3 | T1/T2/T3; pure-Python GF(2^N) |
| glocheck.log | 48ed5541addb7530b086d856ec8b523197a4e827f0bd3b77ab8b3f50ca865424 | seed 1 (about 1.2 s) |
| glocheck_seed7.log | 84c310e972da513398392d8afe0e2582471c86085dfc4e9fbbca01dcc6e0534b | seed 7 |
| glovo.py | 413b9fd4fc7faf8b8bbbab05cdf3d98fa7bfd12cb765d789154f4c758a7adf6b | VO hypotheses for NG and the TX-like family; RLE identity (sympy over GF(2)) |
| glovo.log | 1ef8ddc45646fd5c7a67dc76b11d4d08f9dc4f07af3a9f972a6714a89866dd6f | output |

Totals over both seeds: T1 200 instances, T2 2400, T3 64. **0 mismatches and 0 failures.** The RLE negative control was run ad hoc in scratch; it correctly returns False for two wrong B.
