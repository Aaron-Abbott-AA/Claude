# Even ρ, structured branch, gate-failing cells: if (GT) fails under GLS₁, the twisted subfamily is a B-twisted Kummer–binomial family W′ = B(ηF_{2^{m/4}}), with η an integral Kummer element of height ≤ u that is F_q-valued on all of N; counting alone does not exclude it [COND on GLS₁, (B1a⁺), (B1b)] (owner note, cloud session, 7 Oct 2026, 20:59Z)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS: NOT YET AUDITED.** The coordinator will arrange an independent audit. Do not send to Codex before an audit PASS.

## 0. Setting and inputs
- **PTH v2.2** (reviewed). Used:
  - MI and ML;
  - GO(a)–(c), with L = F_q(X), G = Gal(L^sep/L), W the root space of the WG family B1 (weight u = R/4), the generic relation (C, D) of degree a₂ ≤ a* ≤ ρ/2 − 2, and P = C + Dτ^{m/2} ⊇ W.
- **GX v2.1** (reviewed). Used: the failure pattern [P, referee; adopted]. The sufficient gate fails ⟺ g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2, and then the offending dimension is ρ′ = m/4.
- **(GLS₁)**: a solution A ∈ L^sep{τ} of C·A = D·A^{(Q)}, with deg A ≤ a₂.
- **(B1a⁺)**: B1 is monic over F_q[X], and its roots have pole order ≤ u above ∞.
- **(B1b)**: W(α) is ρ-dimensional and a Frobenius twist of V_α ⊂ F_q at every α ∈ N. In particular B1 is totally split at α.
- **Notation.** T := (4/3)2^{ρ/2} − 1 is the WG threshold [A]. s := 2^{m/4}. N′ := s − 1.

## 1. Proposition KB (structure when (GT) fails) [P under GLS₁, (B1a⁺), (B1b)]
Suppose |χ(G)| ≥ T. Then:
- **(i) Cell.** ρ′ := dim U′ = m/4. U′ = λF_s for some λ ∈ F_Q^*, and F₂(χ(G)) = F_s. The cell is gate-failing: g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2.
- **(ii) Factorisation.** A = B·a₀, meaning A(x) = B(a₀x). Here:
  - B ∈ L{τ} has b₀ = 1 and deg B = deg A ≤ a₂;
  - a₀^{Q−1} = y ∈ L.

  With η := a₀λ:
  - W′ = W ∩ A(F_Q) = B(ηF_s), of dimension m/4;
  - g(η) = ηχ(g) for g ∈ G;
  - h := η^{N′} ∈ L.
- **(iii) Integrality.** η is an F_s-linear combination of elements of W′. Hence η is integral over F_q[X] with pole order ≤ u above ∞, h ∈ F_q[X], and deg h ≤ N′u.
- **(iv) Values on N.** For every α ∈ N and every place above α, η takes a value in F_q. Hence h(α) ∈ {0} ∪ (F_q^*)^{N′} for all α ∈ N.
- **(v) Orbit.** The orbit of η (and of every nonzero element of W′) has size e := |χ(G)|, with T ≤ e and e | N′. η generates a cyclic Kummer extension of L of degree e that is totally split at every α ∈ N (except possibly zeros of h).

*Proof.*
1. **(i).** GO(c) and the failure of (GT) give t > ρ/2. Since t | dim U′ ≤ ρ < 2t, we get t = ρ′ := dim U′ ∈ [ρ−a₂, ρ] ⊂ [ρ−a*, ρ], and t | m/2. GX's failure pattern then gives ρ′ = m/4. U′ is a one-dimensional F_s-space, i.e. U′ = λF_s. The image χ(G) lies in no proper subfield.
2. **(ii).** By ML, a₀ ≠ 0. Put b_i := a_i/a₀^{2^i}.
   - From g(A) = Aχ(g), comparing coefficients gives g(a_i) = a_iχ(g)^{2^i}. Hence g(b_i) = b_i, so B ∈ L{τ}.
   - W′ = A(λF_s) = B(a₀λF_s) = B(ηF_s), and g(η) = g(a₀)λ = ηχ(g).
   - χ(g) ∈ F_s^*, so χ(g)^{N′} = 1, h is G-fixed, and h ∈ L.
3. **(iii).** Pick an F₂-basis t₁, …, t_{m/4} of F_s, and put w_j := B(ηt_j) = Σ_{i≤d} b_iη^{2^i}t_j^{2^i} ∈ W′.
   - The matrix M := [t_j^{2^i}] (m/4 × (d+1)) has full column rank d+1 by Moore, since d+1 ≤ a₂+1 ≤ ρ−a₂ ≤ m/4.
   - A left inverse M⁺ with entries in F_s gives X_i := b_iη^{2^i} = Σ_j M⁺_{ij}w_j. In particular η = X₀, since b₀ = 1.
   - The w_j are roots of B1, so they are integral with pole order ≤ u by (B1a⁺), and F_s-combinations keep both properties.
   - So h = η^{N′} is integral and in L. Hence h ∈ F_q[X], with deg h ≤ N′u.
4. **(iv).** By (B1b), B1 is totally split at α ∈ N with all roots in F_q. So w_j(P) ∈ F_q at every place P above α, and η(P) = Σ M⁺_{0j}w_j(P) ∈ F_q, since F_s ⊂ F_q.
5. **(v).** The orbit of η is ηχ(G). Totally split at α ∈ N: the Frobenius at P | α fixes the w_j, hence η. ∎

**Subcase at the inner resonance (g = 3ρ/2, so m/4 = ρ).**
- Then W′ = W, and W = B(ηF_{2^ρ}).
- If moreover deg B = 0 (B = 1), the radicals are V_α ∝ η(α)F_{2^ρ}: the **globally binomial (E) family**, with ρ | 2g. That is exactly the family treated by Codex's binomial machinery (MH/BC/EWF1 [A]).
- Whether EWF1's "globally binomial resonant g ≥ ρ+2" covers g = 3ρ/2 is a reading question for Codex [A-pending]. If it does, this subcase is closed.

## 2. Why counting does not exclude KB [H; arithmetic P]
- **Weil / character sums for the Kummer cover η^{N′} = h.**
  - Ramified zeros of h have multiplicity ≥ N′/e_P. So h has r ≤ e·u distinct zeros.
  - The Weil bound for the degree-e cyclic cover, totally split over ≈ q/2 places, needs only r ≳ Q/2. That is consistent as soon as e ≳ 2^{ρ/2+1}, and e can reach N′ = 2^{m/4} − 1 ≥ 2^{ρ/2+2}.
  - This is the same threshold as WG, so no contradiction.
- **Norm to F_s.** The condition h(α) ∈ (F_q^*)^{N′} is N_{F_q/F_s}(h(α)) ∈ {0, 1}. A Weil-restriction Schwartz–Zippel argument over F_s⁴ would need deg h < s/8, but deg h can be ≈ (s−1)u.
- **So KB needs arc-specific input**, presumably the binomial/BC machinery generalised to B-twisted binomials. This parallels HFA's treatment of (H) at its inner resonance g = 3ρ/2 [A, NDX §4(a) correction].

## 3. Updated picture (adds a reduction) [COND]
- **Under GLS₁:**
  - (GT) holds, and then GX excludes the structured branch [COND as in GX v2.1]; or
  - (GT) fails, and then the cell is gate-failing (g ≡ ρ/2 mod 2, g ≤ 3ρ/2) and W contains the B-twisted Kummer–binomial family KB of dimension m/4.
- **OPEN:**
  - the exclusion of KB, in particular B-twisted binomials with deg B ≥ 1, and the deg B = 0 inner-resonance subcase pending EWF1's scope;
  - GLS₀/GLS₁ itself.

## 4. Questions for Codex (for a later packet, after audit)
- **(a)** Does EWF1 (or MH/BC) exclude the globally binomial (E) family at g = 3ρ/2 (ρ | 2g, ρ ∤ g)?
- **(b)** Can the binomial machinery handle a B-twisted binomial subfamily W′ = B(ηF_{2^{m/4}}) ⊂ W, with B ∈ L{τ} of degree ≤ a₂, dim W′ = m/4, and η integral of height ≤ u, h = η^{2^{m/4}−1} ∈ F_q[X], η F_q-valued on N?

## 5. Owner self-check (NOT an independent audit)
- **(i)** The stabiliser field of U′ is F_{2^t}, so t | dim U′. Also t > ρ/2 ≥ dim U′/2 forces dim U′ = t. GX's pattern gives the unique offending dimension m/4.
- **(ii)** The relation g(a_i) = a_iχ(g)^{2^i} comes from (Aζ)_i = a_iζ^{2^i}. a₀ ≠ 0 by ML.
- **(iii)** d + 1 ≤ m/4: d ≤ a₂ and m/4 = ρ′ ≥ ρ − a₂ ≥ a₂ + 4. F_s-coefficients preserve integrality and pole bounds.
- **(iv)** F_s ⊂ F_q because m/4 | m.
- **Points to audit.**
  - (1) The use of GX's failure pattern: it needs ρ′ ∈ [ρ−a*, ρ], which holds since a₂ ≤ a*.
  - (2) Whether (B1b)'s Frobenius twist preserves "totally split with roots in F_q". It does, since twisting is a bijection of F_q.
  - (3) The [H] status of §2.
