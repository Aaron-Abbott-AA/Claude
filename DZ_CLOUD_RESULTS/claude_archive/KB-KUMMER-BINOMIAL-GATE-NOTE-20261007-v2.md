# Even ρ, structured branch, gate-failing cells: if (GT) fails under GLS₁, the twisted subfamily is a B-twisted Kummer–binomial family W′ = B(ηF_{2^{m/4}}), with η an integral Kummer element of height ≤ u that is F_q-valued on N, and orbit e ≥ 2^{ρ/2+1} − 1. The B = 1 subcases are half-field and go to HFA. Counting alone does not exclude the rest [H] [COND on GLS₁, (B1a⁺), (B1b)] (owner note v2, cloud session, 7 Oct 2026, 21:10Z; v1 20:59Z) [v2: m1, FIX-1, FIX-2]

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- KB v1 (sha256 d6b60aa1…f124d7) was independently audited in AUDIT-KB-KUMMER-BINOMIAL-GATE-20261007.md. Verdict: **PASS-with-fixes** (2 substantive, 9 minor).
- This **v2** applies FIX-1, FIX-2 and m1–m9. Changes are marked [v2: FIX-n] or [v2: mn].
- **v2 HOLD:** v2 has not been revision-checked. Do not send to Codex until it has been.

## 0. Setting and inputs
**Standing setting** [v2: m6].
- ρ is even, ρ+3 ≤ g ≤ 2ρ, and a(V_α) ≤ a* at every original nonfocus α ∈ N, with a* ≥ 1.
- GO's input step (EBR Lemma G-type count for B1 [A]; PTH v2.2 §4) gives the generic relation (C, D) on W of degree a₂ ≤ a* ≤ ρ/2 − 2.
- L = F_q(X) and G = Gal(L^sep/L). W is the root space of the WG family B1 (weight u = R/4), and P = C + Dτ^{m/2} with R_P ⊇ W.

**Inputs.**
- **PTH v2.2 and GX v2.1** (DZ-internal notes, audited and revision-checked [v2: m8]):
  - MI, ML and GO(a)–(c) from PTH;
  - from GX, the failure pattern [P, referee; adopted]: the sufficient gate fails ⟺ g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2, and the offending dimension is then m/4.
- **(GLS₁)** [v2: m2]: a **nonzero** solution of C·A = D·A^{(Q)} exists in L^sep{τ} with deg A ≤ a₂.
  - In KB, A denotes the **minimal-degree** solution, unique up to F_Q^* (ML), as in GO(a).
  - Only deg A ≤ m/4 − 1 is used, in (iii). So GLS₀ plus that bound suffices.
- **(B1a⁺)**: B1 is monic over F_q[X] of T-degree 2^ρ, and its roots have pole order ≤ u above ∞.
- **(B1b)**: W(α) is ρ-dimensional and is a Frobenius twist of V_α ⊂ F_q at every α ∈ N.
- **Notation.**
  - T := (4/3)2^{ρ/2} − 1, the WG threshold [A].
  - s := 2^{m/4} and N′ := s − 1.
  - d := deg B = deg A [v2: m9].

## 1. Proposition KB (structure when (GT) fails) [P under GLS₁, (B1a⁺), (B1b)]
Suppose |χ(G)| ≥ T. Then:

- **(i) Cell and field.** ρ′ := dim U′ = m/4 and U′ = λF_s for some λ ∈ F_Q^*. The cell is gate-failing: g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2. Moreover F₂(χ(G)) = F_s.
  - χ(G) lies in no proper subfield of F_s, because any proper subfield has order ≤ 2^{m/8}, and 2^{m/8} − 1 ≤ 2^{ρ/2} − 1 < T [v2: m3].
  - Since dim W′ = m/4 ≥ ρ − a₂, the generic defect satisfies a₂ ≥ ρ − m/4 = (3ρ − 2g)/4 [v2: m6].
- **(ii) Factorisation.** A(x) = B(a₀x), with:
  - B ∈ L{τ}, b₀ = 1, and deg B = d ≤ a₂;
  - a₀^{Q−1} = y ∈ L.

  With η := a₀λ:
  - W′ = W ∩ A(F_Q) = B(ηF_s), of dimension m/4;
  - g(η) = ηχ(g) for g ∈ G;
  - h := η^{N′} ∈ L, and y = η^{Q−1} = h^{s+1} [v2: m5].
- **(iii) Integrality.** η is an F_s-linear combination of elements of W′. Hence:
  - η is integral over F_q[X], with pole order ≤ u above ∞;
  - h ∈ F_q[X] with deg h ≤ N′u;
  - k := η^e ∈ F_q[X] with deg k ≤ eu, where e := |χ(G)| [v2: m5].
- **(iv) Values on N.** For every α ∈ N and every place P above α, η(P) ∈ F_q. Hence h(α) ∈ {0} ∪ (F_q^*)^{N′}.
  - By (B1a⁺) (monic, T-degree 2^ρ) and (B1b), B1(α, ·) is separable with all roots in F_q. So every place above α is unramified with trivial decomposition group [v2: m4].
- **(v) Orbit.** The orbit of η, and of every nonzero element of W′, has size e = |χ(G)|, with T ≤ e and e | N′. η generates a cyclic Kummer extension L(η) = L(k^{1/e}) of degree e, totally split at every α ∈ N [v2: m4].
- **(vi) Kummer–Weil bound** [P, referee; adopted; under the same inputs plus EBR Lemma G [A]] [v2: FIX-2]. **e ≥ 2^{ρ/2+1} − 1.**

*Proof.*
1. **(i).** GO(c) and the failure of (GT) give t > ρ/2. Since t | dim U′ ≤ ρ < 2t, we get t = ρ′ = dim U′ ∈ [ρ−a₂, ρ] ⊂ [ρ−a*, ρ], with t | m/2.
   - GX's failure pattern then gives ρ′ = m/4.
   - U′ is a one-dimensional F_s-space.
   - The subfield claim and the bound on a₂ are as stated.
2. **(ii).** By ML, a₀ ≠ 0. Put b_i := a_i/a₀^{2^i}.
   - From g(A) = Aχ(g): g(a_i) = a_iχ(g)^{2^i}, so g(b_i) = b_i.
   - W′ = A(λF_s) = B(ηF_s), and g(η) = ηχ(g).
   - Since χ(g)^{N′} = 1, h ∈ L.
   - Also (Q−1) = N′(s+1), so y = h^{s+1}.
3. **(iii).** Take an F₂-basis t₁, …, t_{m/4} of F_s, and put w_j := B(ηt_j) = Σ_{i≤d} b_iη^{2^i}t_j^{2^i} ∈ W′.
   - M := [t_j^{2^i}] has full column rank d+1 (Moore), since d+1 ≤ a₂+1 ≤ ρ−a₂ ≤ m/4.
   - A left inverse M⁺ over F_s gives b_iη^{2^i} = Σ_j M⁺_{ij}w_j, and in particular η = Σ_j M⁺_{0j}w_j.
   - Integrality and the pole bound pass to F_s-combinations. h = η^{N′} and k = η^e are G-fixed (χ(g)^e = 1) and integral, so they lie in F_q[X].
4. **(iv)–(v).** w_j(P) ∈ F_q because B1 is totally split at α. So η(P) ∈ F_q, and the decomposition group of P in L(η)/L is trivial. The orbit of η is ηχ(G).
5. **(vi), from the referee.**
   - The curve y^e = k is a tame cyclic cover (e is odd). k has r₀ ≤ deg k ≤ eu distinct zeros, and Riemann–Hurwitz gives 2·genus ≤ (r₀−1)(e−1) ≤ (eu−1)(e−1).
   - The v > q/2 places of N split totally, which forces the constant field to be F_q. Weil then gives e·v ≤ q + 1 + (eu−1)(e−1)Q.
   - With Q = 4u·2^{ρ/2}, this is contradictory for every odd e ∈ [3, 2^{ρ/2+1} − 3]. Hence e ≥ 2^{ρ/2+1} − 1.
   - [C, referee] kb_weil: exact in the 88 gate-failing cells with ρ ≤ 40.
   - This is stronger than WG's T, by a factor of about 1.5. ∎

**Subcases with B = 1 (half-field; routed to HFA)** [v2: FIX-1, m7].
- **Inner resonance (g = 3ρ/2, so m/4 = ρ).** Here W′ = W = ηF_{2^ρ}, and ρ | m/2, so F_{2^ρ} ⊂ F_Q. For w = ηt, w^Q = y·w with y ∈ L [P, referee].
  - So the generic radical has a degree-0 relation (a₂ = 0, HFA's hypothesis "Rem ≡ cX").
  - Pointwise, V_α is a Frobenius twist of η(P)F_{2^ρ} ⊂ η(P)F_Q with η(P) ≠ 0, so a(V_α) = 0 at every nonfocus.
  - This is the **global (H) family**. The project ledger records it as closed by IHF/HFA/HFA3 [A]:
    - STATE §3y: "the global half-field branch is closed";
    - IDEAS §321 / packet EB: the inner-resonance correction, then the (H) closure in the near-diagonal;
    - STATE §3z: C1 + HFA3 close (10,15), (14,21) and (24,36).
  - **Status:** closed by HFA [A], pending confirmation that HFA3's statement covers g = 3ρ/2. EWF1 ("globally binomial resonant g ≥ ρ+2" [A]) remains an alternative route.
- **General B = 1 (any gate-failing cell).** W′ = ηF_s ⊂ ηF_Q is a partial half-field sub-radical of dimension m/4 ≥ ρ − a₂. This is HFD §3's narrow partial-half-field sub-case [A].

## 2. Why counting does not exclude KB [H; arithmetic P] [v2: FIX-2]
- **The Kummer–Weil count (KB(vi))** excludes 3 ≤ e ≤ 2^{ρ/2+1} − 3. That is stronger than WG's T ≈ (4/3)2^{ρ/2}; the thresholds differ by about 1.5.
  - It removes some admissible e (those with e | s−1 that generate F_s) in 37 of the 88 gate-failing cells with ρ ≤ 40 [C, referee].
  - But **e = N′ always survives**: the count is consistent for e ≳ 2^{ρ/2+1}, and N′ = 2^{m/4} − 1 ≥ 2^{ρ/2+2}.
- **Norm to F_s.** h(α) ∈ (F_q^*)^{N′} ⟺ N_{F_q/F_s}(h(α)) ∈ {0, 1}. A Weil-restriction Schwartz–Zippel argument over F_s⁴ needs deg h < s/8, while deg h can be about (s−1)u.
- **So KB with B ≠ 1 needs arc-specific input,** presumably the binomial/BC machinery generalised to B-twisted binomials. This parallels HFA's treatment of (H) at its inner resonance g = 3ρ/2 [A, IDEAS §321 and packet EB, correcting NDX §4(a)] [v2: m8].

## 3. Updated picture (adds a reduction) [COND]
- **Under GLS₁:**
  - (GT) holds, and then GX excludes the structured branch [COND as in GX v2.1]; or
  - (GT) fails, and then the cell is gate-failing, e ≥ 2^{ρ/2+1} − 1, and W contains the B-twisted Kummer–binomial family KB of dimension m/4.
- **B = 1 subcases:** half-field, routed to HFA [A]; the inner resonance is pending HFA3's scope [v2: FIX-1].
- **OPEN:**
  - the exclusion of KB with B ≠ 1 (deg B ≥ 1);
  - GLS₀/GLS₁ itself.

## 4. Questions for Codex (for a later packet, after the revision check)
- **(a)** [v2: FIX-1] Does HFA3 (or IHF/HFA) as stated cover the global (H) family at g = 3ρ/2? There ρ | m/2, and the family W = ηF_{2^ρ} ⊂ ηF_Q has a degree-0 generic relation. Does it cover the partial-half-field sub-radicals ηF_{2^{m/4}} of the general gate-failing cells? EWF1 is a possible alternative at g = 3ρ/2.
- **(b)** Can the binomial machinery handle a B-twisted binomial subfamily W′ = B(ηF_{2^{m/4}}) ⊂ W with:
  - B ∈ L{τ} of degree 1 ≤ d ≤ a₂ and dim W′ = m/4;
  - η integral of height ≤ u, F_q-valued on N, with h = η^{2^{m/4}−1} ∈ F_q[X];
  - orbit e ≥ 2^{ρ/2+1} − 1?

## 5. Owner self-check (NOT an independent audit)
- **(i)** The stabiliser field is F_{2^t} with t | dim U′, and t > ρ/2 ≥ dim U′/2 forces equality. GX's pattern then gives m/4. The subfield bound uses m/8 ≤ ρ/2, from m/4 ≤ ρ.
- **(ii)** From (Aζ)_i = a_iζ^{2^i}. a₀ ≠ 0 by ML. Q − 1 = (s−1)(s+1).
- **(iii)** d+1 ≤ m/4 since m/4 ≥ ρ − a₂ ≥ a₂ + 4.
- **(iv)** Separability of B1(α, ·) from (B1a⁺) and (B1b): the roots form the ρ-dimensional space W(α).
- **(vi)** Referee's lemma, adopted with credit. Weil needs the constant field F_q, which total splitting at a degree-1 place guarantees.
- **Points to audit.**
  - (1) Adopted lemma (vi).
  - (2) The routing of the B = 1 subcases to HFA [A].
  - (3) That the bound a₂ ≥ (3ρ−2g)/4 is used only descriptively.

## 6. Change log v1 → v2 [v2]
| Item | Where | Change |
|---|---|---|
| FIX-1 | Title, §1 subcases, §3, §4(a) | B = 1 subcases recognised as half-field (H), routed to HFA [A] (inner resonance pending HFA3's scope); EWF1 is an alternative. The general B = 1 case is a partial half-field. |
| FIX-2 | §1(vi), §2, title | "Same threshold as WG" corrected. Kummer–Weil bound e ≥ 2^{ρ/2+1} − 1 adopted [P, referee]; 37/88 cells partly affected; e = N′ survives. |
| m1 | Title | [H] label on "counting alone". |
| m2 | §0 | "Nonzero" solution; A is the minimal-degree solution; only deg A ≤ m/4 − 1 is used. |
| m3 | §1(i) | Proof that χ(G) lies in no proper subfield. |
| m4 | §1(iv)/(v) | Separability and unramifiedness; decomposition group trivial; superfluous clause removed. |
| m5 | §1(ii)/(iii) | k = η^e ∈ F_q[X] with deg ≤ eu; y = h^{s+1}. |
| m6 | §0, §1(i) | Standing setting stated; a₂ ≥ (3ρ−2g)/4. |
| m7 | §1 subcases | η(P) instead of η(α); Frobenius twist; η(P) ≠ 0. |
| m8 | §0, §2 | "Audited" (DZ-internal), not "reviewed"; inner-resonance citation is IDEAS §321 / EB. |
| m9 | §0 | d := deg B = deg A defined. |
