# Even ρ, structured branch: pointwise, every radical of defect a IS (up to codimension e ≤ a, typically 0) a twisted half-field A(U) with deg A ≤ a. Generically, a Lang solution with an F_Q-line of minimal solutions would give a Kummer orbit bound and hence G1″ in the range a* ≤ (ρ−4)/3 (owner note, cloud session, 7 Oct 2026, 19:58Z)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS: NOT YET AUDITED.** The coordinator will arrange an independent audit. Do not send to Codex before an audit PASS.

## 0. Setting and inputs
- m is even, Q = 2^{m/2}, and x̄ = x^Q. F_q{τ} is the ring of 2-linearised polynomials (τ is squaring, τc = c²τ). For B = Σb_iτ^i, B^{(Q)} := Σ b_i^Q τ^i; this is a ring automorphism of F_q{τ}, and τ^{m/2}B = B^{(Q)}τ^{m/2}.
- **HFD §1 [A, audited].** If a(V) = a < ρ/2, the relations of degree ≤ a form a χ-stable line containing a real relation (C, C̄). Here C = Σ_{e≤a} c_eτ^e with c₀ ≠ 0 and c_a ≠ 0, and C(V) ⊂ F_Q.
- **RBL v2.1 / TCR v2.1** (audited; revision checks PASS): RB, RS(a), the WG threshold T := (4/3)2^{ρ/2} − 1, and G4.
- **What this note does.**
  - It settles the pointwise "Lang-type" claim that RBL v2.1 §6 left unverified [H].
  - It proves the pointwise classification of the structured branch (α) of HFD.

## 1. Lemma LS (pointwise Lang solvability) [P]
**Statement.** Let C ∈ F_q{τ} have degree a. Put
  S_C := {A ∈ F_q{τ}_{≤a} : C·A ∈ F_Q{τ}}.

Then S_C is a right F_Q-vector space (A ↦ Aζ, ζ ∈ F_Q) with dim_{F₂} S_C ≥ m/2, i.e. S_C ≠ 0.

*Proof.*
1. **Closure under right multiplication.** If CA ∈ F_Q{τ} and ζ ∈ F_Q, then C(Aζ) = (CA)ζ = Σ b_iζ^{2^i}τ^i, which lies in F_Q{τ}.
2. **F₂-dimension count.** The map A ↦ CA is F₂-linear and injective (F_q{τ} is a domain). Its image I ⊂ F_q{τ}_{≤2a} has F₂-dimension m(a+1).
   - F_Q{τ}_{≤2a} has F₂-dimension (m/2)(2a+1).
   - The ambient space has F₂-dimension m(2a+1).
   - So dim_{F₂}(I ∩ F_Q{τ}_{≤2a}) ≥ m(a+1) + (m/2)(2a+1) − m(2a+1) = m/2. ∎

**Remark.** This confirms the pointwise half of the Lang-type route in RBL v2.1 §6, which was [H] and unverified there. With C(V) ⊂ F_Q the normalisation is κ = 1. A general real-type relation D = κC̄ with N(κ) = 1 reduces to this case by rescaling C.

## 2. Lemma MI (minimal solutions are injective on F_Q) [P]
**Statement.** If A ∈ S_C∖{0} has minimal degree, then A is injective on F_Q.

*Proof.*
1. **Factor out the kernel.** Let K₀ := ker A ∩ F_Q, and suppose K₀ ≠ 0. Its subspace polynomial S has coefficients in F_Q, and A = A′S with deg A′ = deg A − dim K₀ (right division).
2. **A′ is also a solution.** Since S^{(Q)} = S and (CA)^{(Q)} = CA, we get ((CA′)^{(Q)} − CA′)S = 0. So CA′ ∈ F_Q{τ}.
3. **Contradiction.** Then A′ ∈ S_C∖{0} has smaller degree than A. ∎

## 3. Theorem PTH (pointwise twisted half-field structure of the structured branch) [P; C]
**Setting.**
- V ⊂ F_q has F₂-dimension ρ and a := a(V) < ρ/2.
- C is the real relation with C(V) ⊂ F_Q.
- Ṽ_C := C^{−1}(F_Q) ∩ F_q.
- k := dim_{F₂}(ker C ∩ F_q) ≤ a.
- A ∈ S_C is nonzero of minimal degree.

**Statement.**
- (i) A(F_Q) ⊆ Ṽ_C, with dim A(F_Q) = m/2. Hence e := dim Ṽ_C − m/2 ∈ [0, k].
- (ii) dim(V ∩ A(F_Q)) ≥ ρ − e ≥ ρ − k ≥ ρ − a.
- (iii) **If e = 0 (in particular if k = 0), then V = A(U) with U := A^{−1}(V) ∩ F_Q ⊂ F_Q, dim U = ρ, and deg A = a.** So V is a twisted half-field radical in the sense of HFD §1.

*Proof.*
1. **(i).** A has F_q-coefficients, so A(F_Q) ⊂ F_q. For x ∈ F_Q, C(A(x)) = (CA)(x) ∈ F_Q because CA ∈ F_Q{τ}. So A(F_Q) ⊂ Ṽ_C.
   - dim A(F_Q) = m/2 by MI.
   - dim Ṽ_C = k + dim(F_Q ∩ C(F_q)) ≤ k + m/2.
2. **(ii).** V ⊂ Ṽ_C, and A(F_Q) has codimension e in Ṽ_C.
3. **(iii).** V ⊂ A(F_Q) = Ṽ_C, and A is injective on F_Q.
   - HFD's twisted bound gives a(V) ≤ deg A ≤ a, so deg A = a.
   - If k = 0, then C is bijective on F_q, so F_Q ⊂ C(F_q) and dim Ṽ_C = m/2. ∎

**Consequence (pointwise classification) [P].** HFD's branch (α) (a(V) ≤ c−1) consists exactly of the radicals that, up to codimension e ≤ k ≤ a, are twisted half-fields A(U) with deg A = a(V) and U ⊂ F_Q. HFD §1 already gave the converse: A(U) has a ≤ deg A.

**[C] pthcheck.py** (own code, `python3 -I`, nice 19, about 1 s per run; seeds and commands are in pthcheck.log).
- **Construction.** Random C of degree a, then random ρ-dimensional V ⊂ Ṽ_C, so that C(V) ⊂ F_Q.
- **Range.** 470 samples over (m,ρ,a) ∈ {(12,6,1), (12,6,2), (16,6,1), (16,6,2), (16,8,1), (16,8,2), (16,8,3), (20,10,2), (20,10,3), (20,10,4)}.
- **Checks.** a(V) = a held in every sample, so the relation line is (C, C̄). Then:
  - minimal A injective on F_Q: 0 failures;
  - A(F_Q) inside the root space of P = C + C̄τ^{m/2}: 0 failures;
  - dim(V ∩ A(F_Q)) ≥ ρ − k: 0 failures.
- **Distribution.** V ⊂ A(F_Q) (fully twisted half-field) in 469/470 samples. k took the values 0, 1, 2 and 3. deg A = a in 469/470; the exception had deg A = 0 (a partial half-field V ∩ λF_Q of codimension 1).

## 4. Proposition GO (generic Lang solvability ⟹ Kummer orbit bound ⟹ G1″ in a range) [COND]
**Setting (generic).**
- L = F_q(X). The generic minimal relation is C(w) = D(w^Q) of degree a₂ ≤ a*, with C, D ∈ L{τ} and c₀ ≢ 0 (real type at nonfoci forces c₀(α) ≠ 0). Put P := C + Dτ^{m/2}; its root space R_P has F₂-dimension ≤ m/2 + a₂, and W ⊂ R_P.
- **(GLS₁) [OPEN]:** some nonzero A ∈ L^sep{τ}_{≤a₂} satisfies C·A = D·A^{(Q)}, and the minimal-degree solutions form one right F_Q-line {Aζ : ζ ∈ F_Q}.
- **(GT) gate:** the character χ below has image of order < T.
  - A sufficient condition: no ρ′ ∈ [ρ−a*, ρ] divides g + ρ/2.

**Statement.**
- **(a)** Under GLS₁, the space A(F_Q) ⊂ R_P is G-stable, and G acts on it through a character χ: G → F_Q^*, by g(A(x)) = A(χ(g)x).
- **(b)** W′ := W ∩ A(F_Q) is G-stable, with dim W′ ≥ ρ − a₂.
- **(c)** The orbit of every w ∈ W′ has size dividing |χ(G)| ≤ 2^t − 1. Here F_{2^t} is the stabiliser field of U′ := A^{−1}(W′) ∩ F_Q.
- **(d)** Under (GT) and G4, WG makes W′ rational. So dim W^rat ≥ ρ − a*.
- **(e)** **If moreover a* ≤ (ρ−4)/3, then G1″ holds**, and TCR v2.1 RS(a) excludes the configuration. That step is [COND on G2, (B1a), (I216′) incl. (B1b-fix), Prop 216.3, as in TCR v2.1].

*Proof.*
1. **A(F_Q) ⊂ R_P.** Since τ^{m/2}A = A^{(Q)}τ^{m/2},
   P·A = CA + D·A^{(Q)}τ^{m/2} = CA·(1 + τ^{m/2}).
   So P kills A(F_Q).
2. **(a) The character.** The minimal degree is preserved by G, and G fixes C, D and F_Q, so g(A) is again a minimal-degree solution. By the line hypothesis g(A) = Aχ(g), and χ is a homomorphism. For x ∈ F_Q (fixed by G), g(A(x)) = (Aχ(g))(x) = A(χ(g)x).
3. **(b) Dimension.** The argument of MI works over L^sep: S has F_Q-coefficients and G fixes them. So A is injective on F_Q, and dim A(F_Q) = m/2. Both W and A(F_Q) lie in R_P, so dim W′ ≥ ρ + m/2 − (m/2 + a₂).
4. **(c) Orbits.** G-stability of W′ and injectivity of A on F_Q give χ(g)U′ = U′. The multiplicative stabiliser of an F₂-subspace of F_Q, together with 0, is a subfield F_{2^t} with t | dim U′. So |χ(G)| divides 2^t − 1.
   - Under the sufficient form of (GT): if t > ρ/2, then t | ρ′ := dim U′ ≤ ρ < 2t forces ρ′ = t, and t | m/2. That is excluded. So t ≤ ρ/2, and 2^t − 1 < T.
5. **(d)** WG (with G4) excludes components with 1 < e_w < T, so every w ∈ W′ is rational.
6. **(e)** ρ − a* ≥ 2a* + 4 ⟺ a* ≤ (ρ−4)/3. Then G1″ holds, and RS(a) applies. ∎

**Coverage [C] (gocells.py).** Among even ρ ∈ [10, 40] and the cells ρ+3 ≤ g ≤ min(2ρ, ⌈3ρ/2⌉+2) not covered by NWF:
- 78 cells satisfy a* ≤ (ρ−4)/3;
- 51 of these also pass the sufficient gate;
- the gate fails, for example, at (10,15), (14,21), (16,24), (18,27) and (20,30), where ρ′ = ρ divides g + ρ/2.

Whether other closed-cell results (C1, R6U, EDA) also cover these cells is not rechecked here. In these cells, GO reduces the structured branch to GLS₁ plus the inputs of TCR v2.1.

**Consistency with TX.** In RBL's toy family, A = τ + X ∈ L{τ} solves C·A = D·A^{(Q)}. So GLS₁ holds there with χ trivial and A(F_Q) rational, consistent with TX being rational.

## 5. What remains, and why GLS₁ is the right target [H]
- **GLS₁ is the generic counterpart of LS/PTH.**
  - Pointwise, LS gives solutions at every α ∈ N, and PTH shows that radicals ARE twisted half-fields.
  - GLS₁ asks for this structure to be generic, with the twist A defined over a Kummer extension.
  - Proving GLS₁ from its pointwise truth meets the same obstruction as G1. The pointwise solution A_α depends on C̄_α, whose coefficients have degree about Q in α, so TSZ-type lifting fails.
- **GLS₁ may fail generically** (the Lang system is overdetermined: 2a+1 equations in a+1 unknowns). Then R_P has no G-stable A(F_Q) at all, the structure is "pointwise only", and an arc-specific input (STT/B1) is needed.
- **Updated reduction (adds a route; replaces nothing):**
  - G1″ ⇐ GLS₁ + (GT) + G4, in the range a* ≤ (ρ−4)/3;
  - G1 ⇐ G1″ + G2 + (B1a) + (I216′)[incl. (B1b-fix)] + [A] Prop 216.3 (TCR v2.1).
- **OPEN:**
  - GLS₁;
  - the gate-failing cells;
  - the range a* > (ρ−4)/3, i.e. g < about (4ρ+8)/3.

## 6. Questions for Codex (for a later packet, after audit)
- **(a)** Does your B1/STT structure give a twist A ∈ L^sep{τ} with C·A = D·A^{(Q)} (GLS₁), i.e. a generic twisted half-field form W ∩ A(ηF_Q)?
- **(b)** Do your moving-radical results (MRL/MT, "L = S²+tS") identify the radicals of the structured branch as twisted half-fields with a globally defined twist?

## 7. Owner self-check (NOT an independent audit)
- **LS count.** F₂-dimensions: m(a+1) + (m/2)(2a+1) − m(2a+1) = m/2 > 0. No F_q-structure is needed for the count; the right F_Q-structure is used only for closure.
- **MI.** Subspace polynomials of F_Q-subspaces have F_Q-coefficients. Coefficientwise Q-power is a ring automorphism of F_q{τ} and of L^sep{τ}. Right cancellation holds in a domain.
- **PTH(iii).** e = 0 forces V ⊂ A(F_Q). deg A ≤ a, and deg A ≥ a(V) = a by HFD's twisted bound.
- **GO(a).** The character property needs the minimal-degree solutions to form a single F_Q-line. If they formed a larger F_Q-space, G would act through GL_s(F_Q) and no scalar bound follows. That is why GLS₁ has the line clause.
- **GO(b).** dim R_P ≤ m/2 + a₂ uses P separable (c₀ ≢ 0). Both W and A(F_Q) lie in R_P.
- **GO(c).** The stabiliser of an F₂-subspace under F_Q^*-multiplication is a subgroup whose union with {0} is closed under addition (it is the set {ζ : ζU′ ⊆ U′}), hence a subfield.
- **Points to audit.**
  - (1) Whether the gate condition is stated correctly. The bad case is exactly U′ = λF_{2^{ρ′}} with ρ′ | m/2.
  - (2) Whether c₀ ≢ 0 generically. It follows from c₀(α) ≠ 0 at real-type nonfoci (HFD: α₀ ≠ 0).
  - (3) The "open cells" list relies on NWF only.

Scripts:
- `scripts/pthcheck.py` and `.log` (own code; reads no files).
- `scripts/gocells.py` and `.log` (arithmetic).
