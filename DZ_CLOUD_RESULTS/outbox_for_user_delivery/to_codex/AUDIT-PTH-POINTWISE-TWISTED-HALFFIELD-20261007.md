# AUDIT — PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007.md (independent referee, cloud session, 7 Oct 2026, 19:59–20:20Z)

Referee: fresh, isolated, adversarial subagent for the DZ line (project "Wan's numbers of PPs"). No contact with the owner session or with Codex. No files outside the DZ scope were read (list in §7).
Note audited: `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007.md`, sha256 `3e17d28c056982a35834fcadf94aa81ba28cac9d2dd1724615bd9165c2680a03`. The copy in `claude_archive/` is identical.
Labels follow the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN]. Where the referee proves something, it is marked "[P, referee]".

## 0. Verdict: **PASS-with-fixes**

- **The pointwise mathematics is correct.** This covers Lemma LS, Lemma MI and Theorem PTH (i)–(iii).
  - Every proof step was checked by hand.
  - Independent code (different field polynomial, different linear algebra) ran 626 radicals with 0 failures (§5).
  - The referee also searched adversarially for e > 0 cases and found 130 of them (128 constructed, 2 random). All satisfy (i)–(iii); in every one, (ii) is sharp.
- **The "Consequence (pointwise classification)" after PTH is false as written.** It is labelled [P].
  - "deg A = a(V)" fails whenever e > 0. Counterexamples: the owner's own exceptional sample, the referee's 128 constructed cases, and 2 random cases, one of them with deg A = 2 < a(V) = 3.
  - "Consists exactly" is not a characterisation. The converse with codimension e gives only a(V) ≤ deg A + e.
  - A correct two-sided statement is given in FIX-2.
- **Proposition GO is logically sound given its hypotheses, but it does not name all of them.**
  - Steps (a)–(e) were each checked. The gate arithmetic and the coverage count (78 cells, 51 passing the gate) were reproduced exactly.
  - However, W is never defined in GO. The *generic* relation C(w) = D(w^Q) on the root space of the WG family B1 is assumed, not derived. EBR Lemma G gives it only for the weight-K CM2 family, and WG is applied to B1.
  - The missing input is (B1a)+(B1b), plus a Lemma-G-type count for B1. The referee checked that count's arithmetic in all 380 band cells.
  - It must be named in GO's [COND] label and in the §5 reduction line (FIX-1).
- **Positive finding [P, referee]: GLS₁ is stronger than GO needs.**
  - The "F_Q-line" clause of GLS₁ is *automatic*: whenever a nonzero solution exists, the minimal-degree solutions form exactly one F_Q-line.
  - The degree bound deg A ≤ a₂ is never used.
  - The character χ is the Kummer character of c₀/d₀ ∈ L, so (GT) is a property of the generic relation alone.
  - Details are in §3, item GO-S. The owner may adopt this; if adopted, it needs audit.
- **Owner revision is required before the note goes to Codex.** The fixes are restatements and labels; no proof needs to be rewritten.

FIX count: **2 substantive, 9 minor.**

## 1. Item table

| # | Item | Claimed label | Referee finding | Status |
|---|---|---|---|---|
| 1 | §0: B ↦ B^{(Q)} is a ring automorphism of F_q{τ}; τ^{m/2}B = B^{(Q)}τ^{m/2} | — | Correct. | OK |
| 2 | §0: HFD §1 input (real line, c₀, c_a ≠ 0, C(V) ⊂ F_Q) | [A] | Matches HFD §1 ("Minimal relation is real and nondegenerate"), which was audited PASS. | OK |
| 3 | §0: RBL v2.1 / TCR v2.1 inputs (RB, RS(a), T, G4) | [A] | Accurate. WG's own [A] status (summary reading only) is not carried over. | m10 |
| 4 | §1 Lemma LS | [P] | Correct: right F_Q-closure, injectivity, F₂-count m/2. | PASS |
| 5 | §1 Remark: "confirms the pointwise half of RBL §6" | — | Confirms existence only. S_C can have F_Q-dimension up to a+1. The "line" holds for minimal-degree solutions (referee proof, §3). | m3 |
| 6 | §1 Remark: κ-rescaling | — | Correct (Hilbert 90, λ̄/λ = κ). | OK |
| 7 | §2 Lemma MI | [P] | Correct: subspace polynomial over F_Q, right division, right cancellation. | PASS |
| 8 | §3 PTH (i) | [P] | Correct. | PASS |
| 9 | §3 PTH (ii) | [P] | Correct and sharp (130 constructed cases with equality at e > 0). | PASS |
| 10 | §3 PTH (iii) | [P] | Correct. deg A = a uses HFD's twisted bound. | PASS |
| 11 | §3 "Consequence (pointwise classification)" | [P] | **False as written:** "deg A = a(V)" fails for e > 0, and "exactly" is not a characterisation. | **FIX-2** |
| 12 | §3 [C] pthcheck | [C] | Re-run byte for byte, but the log shows **435** samples (434/435 fully twisted), not 470 (469/470). m = 20 runs take about 38 s, not about 1 s. "Typically e = 0" describes the random-C sampler. | m1, m2 |
| 13 | §4 GO Setting | [COND] | W is undefined. The generic relation on the WG family's root space is assumed without source. dim W = ρ needs (B1b). | **FIX-1** |
| 14 | §4 GO "c₀ ≢ 0" | — | The justification is incomplete, but the hypothesis is not needed. | m5 |
| 15 | §4 GO (a) character | [COND GLS₁] | Correct. The line clause is automatic (§3, GO-S). | PASS (m8) |
| 16 | §4 GO (b) dimension | [COND] | Correct, given dim W = ρ. | PASS (FIX-1) |
| 17 | §4 GO (c) orbits and gate | [COND] | Correct. The stabiliser is a field, t divides dim U′, and t > ρ/2 forces U′ = λF_{2^{ρ′}}. The sufficient gate equals the exact stabiliser obstruction in all 78 cells. | PASS |
| 18 | §4 GO (d) WG ⇒ rational | [COND G4, WG] | Correct: 2^t − 1 ≤ 2^{ρ/2} − 1 < T. | PASS |
| 19 | §4 GO (e) ⇒ G1″ ⇒ RS(a) | [COND] | Correct: ρ − a* ≥ 2a*+4 ⟺ a* ≤ (ρ−4)/3. The TCR v2.1 input list is quoted correctly. | PASS |
| 20 | §4 Coverage [C] gocells | [C] | Reproduced byte for byte and recounted independently: 78 / 51 / 27, with the listed failures confirmed. | PASS |
| 21 | §4 Consistency with TX | [P] | Verified: CA = DA^{(Q)} as polynomials for m = 8, 12, 16, 20. The minimal solutions are exactly (τ+X)F_Q (hand derivation, §3). | PASS |
| 22 | §5 Heuristics and updated reduction | [H] | The first reduction line lacks WG and the B1 inputs (FIX-1). Otherwise labelled correctly. | FIX-1 |
| 23 | Title | — | Omits the gate (GT) and the conditional inputs. | m7 |
| 24 | §7 self-check | — | "Q-power is an automorphism of L^sep{τ}" is false (it is an injective endomorphism, which suffices). The GO(a) rationale for the line clause is moot. | m4, m8 |

## 2. Detailed audit: pointwise part (§§0–3)

**§0.**
- (Σb_iτ^i)(Σc_jτ^j) = Σ b_i c_j^{2^i} τ^{i+j}. Raising coefficients to the Q-th power commutes with this product, and it is bijective on F_q. So B ↦ B^{(Q)} is a ring automorphism of F_q{τ}.
- τ^{m/2}b = b^Qτ^{m/2}, which gives the commutation rule.
- The HFD §1 citation is accurate. For a < ρ/2 the degree-≤ a relations form a χ-stable F_q-line, by the profile count (a+1−d₁)₊ + (a+1−d₂)₊ = 1 with d₂ = ρ−a ≥ a+1.
- The real member Σα_eF^e + ᾱ_eχF^e says exactly C(v) + \overline{C(v)} = 0. C is unique up to F_Q^*, so Ṽ_C, k and e are well defined.

**LS [P]. PASS.**
- Right F_Q-closure: C(Aζ) = (CA)ζ = Σb_iζ^{2^i}τ^i ∈ F_Q{τ}.
- Count: m(a+1) + (m/2)(2a+1) − m(2a+1) = m/2. No hypothesis on C is needed.
- [C] referee: 120 random C (lsonly; m = 12–20, a = 1–4) and all 626 analysed radicals have dim_{F₂}S_C ≥ m/2.

**Remark after LS (m3).**
- LS proves only F_Q-dim S_C ≥ 1. RBL v2.1 §6 said "a nonzero F_Q-line of solutions".
- S_C itself need **not** be a line. For C = R∘λ^{−1} with R ∈ F_Q{τ}, every λB with B ∈ F_Q{τ}_{≤a} lies in S_C, so dim_{F_Q}S_C ≥ a+1.
  - [C] referee "partial" mode: dim_{F_Q}S_C = a+1 exactly (2, 3, 4, 5) in all 128 cases.
- The correct "line" statement is for the minimal-degree solutions. It is a short theorem (Lemma ML below), and it held in all 746 C tested.

**MI [P]. PASS.**
- K₀ ⊂ F_Q, so its subspace polynomial S has F_Q-coefficients and is monic. Right division A = A′S + R′ with deg R′ < dim K₀, and R′ vanishes on K₀, so R′ = 0.
- (CA′)^{(Q)}S = (CA)^{(Q)} = CA = CA′S. Right cancellation (domain) gives CA′ ∈ F_Q{τ}.
- A′ ≠ 0, and deg A′ < deg A contradicts minimality.
- [C] 0 failures out of 626.

**PTH (i)–(iii) [P]. PASS.**
- (i): C(A(x)) = (CA)(x) ∈ F_Q for x ∈ F_Q. Also dim Ṽ_C = dim ker C|_{F_q} + dim(F_Q ∩ C(F_q)). Together with dim A(F_Q) = m/2 (MI), this gives 0 ≤ e ≤ k ≤ a.
  - k ≤ a because C is separable of τ-degree a.
- (ii): V ⊂ Ṽ_C and codim_{Ṽ_C} A(F_Q) = e.
- (iii): e = 0 gives V ⊂ A(F_Q), and U := A^{−1}(V) ∩ F_Q has dimension ρ. HFD's twisted bound gives a = a(V) ≤ deg A ≤ a.
  - k = 0 ⇒ e = 0 is correct.
- [C] referee, 0 failures in 626:
  - (i): A(F_Q) ⊂ Ṽ_C and e ∈ [0,k];
  - (ii);
  - (iii): both V ⊂ A(F_Q) and deg A = a whenever e = 0;
  - the bottom and top Kummer identities a₀^{Q−1} = c₀/c̄₀ and (a_s^{Q−1})^{2^a} = c_a/c̄_a.

**"Consequence (pointwise classification)" — FIX-2 (substantive).** The sentence makes three claims. Each is checked below.
1. **"with deg A = a(V)": false when e > 0.**
   - Explicit family [P, referee]. Take λ ∉ F_Q, K ⊂ F_Q of dimension a, and R ∈ F_Q{τ} the subspace polynomial of K. Put C := R∘λ^{−1}, so C(z) = R(z/λ).
   - Then Ṽ_C = λ{z : z + z̄ ∈ K}, of dimension m/2 + a. So k = e = a.
   - The constant λ lies in S_C, since Cλ = R ∈ F_Q{τ}. So the minimal A has deg A = 0.
   - Take V = (a (ρ−a)-dimensional subspace of λF_Q) ⊕ (a further vectors of Ṽ_C). Then a(V) = a (128/128 cases at (m,ρ,a) = (12,6,1), (12,6,2), (16,6,2), (16,8,3), (20,10,4)), while deg A = 0 and dim(V ∩ A(F_Q)) = ρ − e exactly.
   - A random C also produces deg A ∈ (0, a(V)): rand (16,8,3), seed 107, gave deg A = 2, a(V) = 3, e = 1.
   - So PTH's minimal twist A has degree ≤ a(V), with equality guaranteed only when e = 0.
2. **"exactly": not a characterisation.**
   - The true converse is a(V) ≤ deg A + c, where c := codim_V(V ∩ A(F_Q)) [P, referee].
   - Proof: V′ := V ∩ A(F_Q) = A(U′) has a(V′) ≤ deg A =: d. The profile gives ≥ j+1−d independent relations of degree ≤ j on V′ (window length j+1). Extending to V imposes c F_q-linear conditions. So a relation of degree ≤ j exists on V once j ≥ d + c.
   - [C] referee: 0 violations of a(V) ≤ deg A + c in 626 cases. Equality occurs in the partial family (a = 0 + a).
   - So the class "twisted half-field of degree ≤ a up to codimension ≤ a" lies between {a(V) ≤ a} and {a(V) ≤ 2a}. It is not equal to {a(V) ≤ a}.
3. **"HFD §1 already gave the converse"**: true only for e = 0 (codimension 0).

## 3. Detailed audit: Proposition GO (§4) and §5

**GO Setting — FIX-1 (substantive).**
- **W is never defined in §4.** WG is applied in (d) to "components" with the threshold T = (4/3)2^{ρ/2} − 1, which is the threshold for the WG family B1 of weight u = R/4. So W must be B1's root space over L.
- **The generic relation of degree a₂ ≤ a* on that W is assumed, not derived.** Its only stated source is EBR Lemma G(a), which concerns the weight-K CM2 family. RBL/TCR obtain a relation on B1's roots only in the *rational* branch, via TSZ. GO is about the non-rational branch.
- **What is needed, and suffices:**
  - (B1a⁺): B1 is monic over F_q[X] and its roots have pole order ≤ u at the places above ∞. In the rational branch this is RBL's (B1a).
  - (B1b): W(α) is ρ-dimensional and is a Frobenius twist of V_α at every α ∈ N. This is also what makes dim W = ρ in GO(b).
  - A Lemma-G-type count for B1. The GL_ρ(F₂)-invariant Moore determinants D_{B1}(S_j ∪ T) are then in F_q[X]. Their degree is ≤ u[(2^{j+1}−1)(Q+1) + Σ_T 2^e].
  - [C] referee, ref_go.py (3): this is ≤ Q²/2 < v in all 380 cells (even ρ ∈ [4,40], g ∈ [ρ+3,2ρ], j = a*). The worst ratio is 0.25.
  - So all of them vanish identically. By Steinitz and Galois descent of the G-stable relation space, a relation over L of degree ≤ a* exists on W.
- **Required change.** State this as an input step in GO's Setting, labelled [COND (B1a⁺), (B1b)]. Add (B1a⁺), (B1b) and WG [A] to GO's header label. Add them to the §5 line "G1″ ⇐ GLS₁ + (GT) + G4".
  - In the chain to G1, (B1b) is already implied by (I216′)'s (B1b-fix). The standalone implication G1″ ⇐ … is incomplete without them.

**GO (a)–(e): logic PASS.**
- **(a).** τ^{m/2}A = A^{(Q)}τ^{m/2} in L^sep{τ}, so P·A = CA(1+τ^{m/2}), which kills F_Q.
  - For g ∈ G = Gal(L^sep/L): C·g(A) = g(CA) = D·g(A)^{(Q)}, so g(A) is again a minimal solution. The line gives g(A) = Aχ(g).
  - g(Aζ) = g(A)ζ for ζ ∈ F_Q, so χ is a homomorphism, and g(A(x)) = A(χ(g)x).
- **(b).** MI over L^sep needs only the injective endomorphism property of Q-power (m4).
  - dim R_P ≤ deg_τ P ≤ m/2 + a₂ holds for ANY nonzero linearized P. So "c₀ ≢ 0" is not needed (m5).
  - dim W′ ≥ ρ + m/2 − (m/2 + a₂), given dim W = ρ (FIX-1).
- **(c).** The set {ζ ∈ F_Q : ζU′ ⊆ U′} is a finite subring of a field, hence a field F_{2^t}. Then t | dim U′ and t | m/2.
  - The orbit of w ≠ 0 in W′ has size exactly |χ(G)| (m6).
  - If t > ρ/2, then ρ′ = t, so U′ = λF_{2^{ρ′}}.
  - [C] referee stab mode: 750 subspaces (h = 6, 8, 10), including adversarial λF_{2^t}-subspaces; 0 failures.
- **(d).** WG needs √q ≤ 3u(e_w+1), with √q = 4u·2^{ρ/2}. So 1 < e_w < T is impossible, and 2^t − 1 ≤ 2^{ρ/2} − 1 < T.
- **(e).** ρ − a* ≥ 2a*+4 ⟺ a* ≤ (ρ−4)/3. G1″ is TCR's dim W^rat ≥ 2a*+4. RS(a)'s conditional inputs are quoted correctly from TCR v2.1 §5.

**Gate (owner audit point 1).** The statement is correct.
- Since ρ′ ≥ ρ − a* > ρ/2, the sufficient gate "no ρ′ ∈ [ρ−a*, ρ] divides m/2" is *equivalent* to "the stabiliser bound gives t ≤ ρ/2" for every possible U′. ref_go.py (1) found 0 mismatches in 78 cells.
- The bad case is exactly U′ = λF_{2^{ρ′}} with ρ′ | m/2.

**Coverage [C].** gocells.py was re-run byte for byte. The referee also recounted independently, using EBR's form a* = ρ−1−⌊(g−1)/2⌋, which agrees with ρ−⌈g/2⌉ in all cells:
- 78 cells in range;
- 51 pass the gate;
- 27 fail it, including the five listed.

The disclaimer about C1, R6U and EDA is noted.

**TX consistency.**
- ref_go.py (4): CA = DA^{(Q)} holds as polynomials over F₂[X] for m = 8, 12, 16, 20.
- Hand derivation of the degree-≤ 1 solutions. a₁² = a₁^{2Q} forces a₁ ∈ F_Q. Then a₀^{Q−1} = c₀/d₀ = X^{Q−1} gives a₀ = Xζ. The τ-coefficient then gives a₁ = ζ². So the minimal solutions are exactly (τ+X)F_Q, and χ is trivial, as the note says.

**GO-S: strengthening offered to the owner (not a FIX; [P, referee], needs audit if adopted).**
- **Lemma ML (the line is automatic).** Let K be F_q or L^sep, and let (C, D) have degree a₂. Suppose the equation C·A = D·A^{(Q)} has a nonzero solution in K{τ}, and let d be the minimal degree of such solutions. Then:
  - deg D = deg C = a₂;
  - a₀ ≠ 0 and d₀ ≠ 0;
  - the minimal-degree solutions together with 0 form exactly one right F_Q-line.

  *Proof.*
  1. Compare top coefficients: c_{a₂}a_d^{2^{a₂}} = d_{a₂′}a_d^{Q2^{a₂′}}. This forces a₂′ = a₂ and (a_d^{Q−1})^{2^{a₂}} = c_{a₂}/d_{a₂}.
  2. For two minimal solutions A₁, A₂, the ratio r = a_{2,d}/a_{1,d} satisfies r^{(Q−1)2^{a₂}} = 1. In characteristic 2 this gives r^{Q−1} = 1, so r ∈ F_Q^*.
  3. Put ζ := r^{2^{−d}} ∈ F_Q. Then A₂ − A₁ζ is a solution of degree < d, so it is 0.
  4. If a₀ = 0, then A = A′τ with A′ a smaller solution, so a₀ ≠ 0. Then c₀a₀ = d₀a₀^Q gives d₀ ≠ 0. ∎

  Pointwise (K = F_q) this is the correct form of RBL §6's "line" claim. [C]: the minimal-degree F_Q-dimension was 1 in all 746 C tested, including the 128 cases where dim_{F_Q}S_C = a+1.
- **Consequences for GO.**
  - (i) GLS₁ can be weakened to GLS₀: "C·A = D·A^{(Q)} has a nonzero solution in L^sep{τ}". GO never uses deg A ≤ a₂: MI and A(F_Q) ⊂ R_P hold for any degree.
  - (ii) The τ⁰-coefficient of g(A) = Aχ(g) gives χ(g) = g(a₀)/a₀ with a₀^{Q−1} = c₀/d₀ ∈ L. So **χ is the Kummer character of c₀/d₀**, and |χ(G)| is the order of c₀/d₀ in L^*/L^{*(Q−1)}.
    - So (GT) is a condition on the generic relation alone.
    - In TX, c₀/d₀ = X^{Q−1}, so χ is trivial.
  - (iii) GLS₀ has cheap necessary conditions. Besides deg D = deg C and d₀ ≢ 0: y := a_d^{Q−1} is separable over L, and y^{2^{a₂}} ∈ L, so y ∈ L. Hence **c_{a₂}/d_{a₂} ∈ L^{2^{a₂}} = F_q(X^{2^{a₂}})**. This gives a concrete test that could refute GLS₀ for a given family.
  - (iv) If P is separable, any solution over the algebraic closure L̄ already lies in L^sep{τ}. Its coefficients are F_Q-combinations of the values A(x_j) ∈ R_P ⊂ L^sep, by inverting a Moore matrix over F_Q. So "sep" costs nothing.

**§5.** The [H] content is correctly labelled. The first reduction line needs FIX-1. "GLS₁ may fail generically" is a fair [H]; GO-S(iii) makes it testable.

## 4. FIX list

### Substantive
- **FIX-1 (GO inputs).**
  - Define W in §4 as the root space over L of the WG family B1 (weight u = R/4).
  - Derive, or cite, the generic degree-≤ a* relation on W as an input step labelled [COND (B1a⁺), (B1b)]. Here (B1a⁺) means: monic over F_q[X], with roots of pole order ≤ u at ∞. The step is the Lemma-G-type invariant-Moore-determinant count; the referee checked its arithmetic in all 380 cells.
  - Note that dim W = ρ uses (B1b).
  - Add (B1a⁺), (B1b) and WG [A] (summary reading only) to:
    - GO's header label;
    - the GO(d) label;
    - the §5 line "G1″ ⇐ GLS₁ + (GT) + G4";
    - the sentence "GO reduces the structured branch to GLS₁ plus the inputs of TCR v2.1", which should also mention (GT), G4 and WG.
- **FIX-2 (Consequence after PTH).** Replace the paragraph by a correct two-sided statement:
  - "If a(V) = a < ρ/2, there are A with deg A ≤ a, injective on F_Q, and e ≤ k ≤ a with dim(V ∩ A(F_Q)) ≥ ρ − e. deg A = a and V = A(U) hold when e = 0.
  - Conversely, if dim(V ∩ A(F_Q)) ≥ ρ − c, then a(V) ≤ deg A + c."
  - Delete "exactly" and "deg A = a(V)" in the general case.
  - Optionally record the explicit e = a family C = R∘λ^{−1} (minimal A = λ of degree 0, sharp (ii)).

### Minor
- **m1.** [C] pthcheck: the log (re-run byte for byte by the referee) has **435** samples, with V ⊂ A(F_Q) in **434/435**; the note says 470 and 469/470. Runtime is about 0.4–2 s for m ≤ 16 and about 38 s for m = 20; the note says "about 1 s per run".
- **m2.** "e typically 0" and "deg A = a in 469/470" describe the random-C sampler, where e > 0 has probability about 1/Q. They say nothing about arc radicals. Label them [C, sampler] and drop "typically" from the title, or qualify it. Also, e > 0 exceptions are not only partial half-fields: see the random case (16,8,3), seed 107, with deg A = 2.
- **m3.** Remark after LS: say that LS confirms *existence* (dim_{F_Q} S_C ≥ 1), and that S_C may have F_Q-dimension a+1. The "line" of RBL §6 holds for the minimal-degree solutions; cite Lemma ML if adopted.
- **m4.** §7: coefficientwise Q-power is an injective ring *endomorphism* of L^sep{τ}, not an automorphism (L^sep is imperfect). MI and GO(a) need only the endomorphism property.
- **m5.** GO Setting and audit point (2): the "c₀ ≢ 0" argument needs some α ∈ N with a(V_α) = a₂ and (C,D)(α) ≠ 0, for instance from a Lemma-G(b)-type count. It is also unnecessary: dim R_P ≤ deg_τ P holds for every nonzero linearized P. Remove it or complete it.
- **m6.** GO: define G = Gal(L^sep/L). In (c), the orbit of w ≠ 0 has size exactly |χ(G)|, not just a divisor of it.
- **m7.** Title: "hence G1″ in the range a* ≤ (ρ−4)/3" omits the gate (GT), which fails in 27 of the 78 cells, and the inputs WG, G4, (B1a⁺) and (B1b). Add "where (GT) holds, [COND …]".
- **m8.** §7 GO(a): "If they formed a larger F_Q-space …" can never happen (Lemma ML). Consider replacing GLS₁ by the weaker GLS₀ and recording χ = the Kummer character of c₀/d₀ (GO-S). This is optional and needs audit if adopted.
- **m9.** Script paths: the note says `scripts/pthcheck.py`, but the files ship as `owner_scripts/`. The log lines omit `nice -n 19`. Cosmetic.
- **m10.** §0: carry WG's [A] status ("summary reading only, IDEAS §305 / HFD §3"), as RBL v2.1 does.

## 5. Referee computations (`checks/`, all `python3 -I`, one process at a time, each under 1 min)

- **owner_copy/** holds byte copies of `pthcheck.py` and `gocells.py` (sha256 identical to `src/owner_scripts/`). Both were re-run with the logged commands.
  - `pthcheck_rerun.log`: the 10 `cmd:` lines are identical to the owner log. The totals are 435 trials and 434 fully twisted. The elapsed times are recorded.
  - `gocells_rerun.log`: identical.
- **ref_pth.py** (independent code). It uses a log/exp-table GF(2^m) with the primitive polynomial searched from the top, which differs from the owner's polynomial, and its own F₂ and F_q elimination. It has five modes:
  - **rand**: random C, and V ⊂ Ṽ_C; 9 runs, 380 radicals.
  - **partial**: C = R∘λ^{−1}, forcing k = e = a; 5 runs, 128 radicals.
  - **twist**: V = A₀(U); 5 runs, 118 radicals.
  - **lsonly**: 120 random C.
  - **stab**: 750 subspaces.
- **Results** (`ref_pth.log`, `ref_pth_stab.log`):
  - 626 radicals analysed;
  - 0 failures of: the real line, c₀ ≠ 0, C(V) ⊂ F_Q, LS, MI, k ≤ a, e ∈ [0,k], (i), (ii), (iii)-V, (iii)-deg, the converse a(V) ≤ deg A + c, and the top and bottom Kummer identities;
  - 130 cases with e > 0 (128 partial + 2 rand), all of them sharp in (ii) and all with deg A < a(V) (FIX-2);
  - minimal-degree solution space F_Q-dimension 1 in all cases;
  - stab: 0 failures.
- **ref_go.py** (`ref_go.log`):
  - (1) coverage recount 78/51/27, with sufficient gate = exact obstruction;
  - (2) 2^t − 1 < T for even ρ ≤ 80;
  - (3) the B1 Lemma-G count is ≤ Q²/2 in 380 cells (worst ratio 0.25);
  - (4) the TX identity holds for m = 8, 12, 16, 20.
- **Hashes:** `checks/checks_SHA256SUMS.txt`.

## 6. Owner audit points (§7 of the note)
- (1) Gate: correct. It is exactly the stabiliser obstruction (§3).
- (2) c₀ ≢ 0: the argument is incomplete but the hypothesis is unnecessary (m5).
- (3) Open cells rely on NWF only: confirmed and disclosed. The recount agrees.

## 7. Files read
- Handoff (read-only):
  - `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`. It contains no referee restriction on which files may be read; its labels and audit rule were followed.
  - `notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`
  - `notes/EBR-EVEN-BAND-REDUCTION-NOTE-20261007.md`
  - Directory listings of `docs/`, `notes/`, `packets/` and `scripts/`. A grep for "NWF" over the handoff returned matching lines only (STATE, CHECKPOINT, notes, ndz scripts).
- Under audit:
  - `referee_PTH/src/PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007.md`
  - `src/owner_scripts/{pthcheck.py, pthcheck.log, gocells.py, gocells.log}`
- Archive (cited inputs):
  - `claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md` (sha256 f3a2e176…d9453)
  - `claude_archive/TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md` (sha256 4b2d969b…c7428)
  - the first 40 lines of `claude_archive/AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md`, for format only
  - a sha256 comparison of the archive copy of the PTH note
- Not read: HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, uploads, other scratchpad directories. No git was used.

## 8. Written
- `referee_PTH/AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md` (this file), with an identical copy in `DZ_CLOUD_RESULTS/claude_archive/`.
- `referee_PTH/checks/`:
  - `ref_pth.py`, `ref_pth.log`, `ref_pth_stab.log`
  - `ref_go.py`, `ref_go.log`
  - `owner_copy/{pthcheck.py, gocells.py, pthcheck_rerun.log, gocells_rerun.log}`
  - `checks_SHA256SUMS.txt`
