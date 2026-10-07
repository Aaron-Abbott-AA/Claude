# Even ρ, structured branch: pointwise, every radical of defect a contains a twisted half-field A(F_Q) ∩ V of codimension e ≤ a, and equals A(U) when e = 0. Generically, a Lang solution gives a Kummer orbit bound, and hence G1″ for a* ≤ (ρ−4)/3 where the gate (GT) holds [COND on GLS₀, (GT), G4, WG [A], (B1a⁺), (B1b)] (owner note v2, cloud session, 7 Oct 2026, 20:18Z; v1 19:58Z) [v2: m7, m2]

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- v1 (sha256 3e17d28c…680a03) was independently audited in AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md. Verdict: **PASS-with-fixes** (2 substantive, 10 minor items m1–m10).
- This v2 applies FIX-1, FIX-2 and m1–m10. Each change is marked [v2: FIX-n] or [v2: m-n].
- The optional strengthening GO-S (Lemma ML, GLS₀ and the Kummer character) is ADOPTED in §4A, credited to the referee. It needs audit.
- **v2 has NOT been revision-checked. HOLD: do not send to Codex until it has been.**

## 0. Setting and inputs
- **Notation.**
  - m is even, Q = 2^{m/2}, and x̄ = x^Q.
  - F_q{τ} is the ring of 2-linearised polynomials (τc = c²τ).
  - For B = Σb_iτ^i, put B^{(Q)} := Σb_i^Qτ^i. This is a ring automorphism of F_q{τ}, and an injective ring **endomorphism** of L^sep{τ} [v2: m4]. τ^{m/2}B = B^{(Q)}τ^{m/2}.
- **HFD §1 [A, audited].** If a(V) = a < ρ/2, the relations of degree ≤ a form a χ-stable line containing a real relation (C, C̄), with c₀ ≠ 0, c_a ≠ 0 and C(V) ⊂ F_Q. C is unique up to F_Q^*.
- **RBL v2.1 / TCR v2.1** (audited; revision checks PASS): RB, RS(a), T := (4/3)2^{ρ/2} − 1, G4.
- **WG [A]** is a summary reading only (IDEAS §305 / HFD §3), as in RBL v2.1. [v2: m10]
- **(B1a⁺)** [v2: FIX-1]: B1 (the WG family, weight u = R/4) is monic over F_q[X], and its roots have pole order ≤ u at the places above ∞. In the rational branch this is RBL's (B1a).
- **(B1b)** (RBL v2.1): at every α ∈ N, W(α) is ρ-dimensional and is a Frobenius twist of V_α.

## 1. Lemma LS (pointwise Lang solvability) [P]
**Statement.** Let C ∈ F_q{τ} have degree a, and put S_C := {A ∈ F_q{τ}_{≤a} : C·A ∈ F_Q{τ}}. Then S_C is a right F_Q-vector space with dim_{F₂} S_C ≥ m/2. In particular S_C ≠ 0.

*Proof.*
1. **Right F_Q-closure.** C(Aζ) = (CA)ζ = Σb_iζ^{2^i}τ^i lies in F_Q{τ} for ζ ∈ F_Q.
2. **Count.** A ↦ CA is F₂-linear and injective. Its image has F₂-dimension m(a+1), F_Q{τ}_{≤2a} has (m/2)(2a+1), and the ambient space has m(2a+1). So the intersection has F₂-dimension ≥ m(a+1) + (m/2)(2a+1) − m(2a+1) = m/2. ∎

**Remark** [v2: m3]. LS gives **existence** only (dim_{F_Q} S_C ≥ 1). S_C itself can have F_Q-dimension up to a+1; the referee found exactly a+1 for C = R∘λ^{−1}. The "line" of RBL §6 is correct for the **minimal-degree** solutions; see Lemma ML in §4A. A general real-type relation D = κC̄ with N(κ) = 1 reduces to κ = 1 by rescaling C.

## 2. Lemma MI (minimal solutions are injective on F_Q) [P]
**Statement.** If A ∈ S_C∖{0} has minimal degree, then A is injective on F_Q. The same holds over L^sep, for solutions of C·A = D·A^{(Q)}.

*Proof.*
1. Suppose K₀ := ker A ∩ F_Q ≠ 0. Its subspace polynomial S has F_Q-coefficients, and right division gives A = A′S.
2. Then S^{(Q)} = S. From (CA)^{(Q)} = CA we get ((CA′)^{(Q)} − CA′)S = 0, so CA′ ∈ F_Q{τ}. Over L^sep the same computation gives CA′S = DA′^{(Q)}S.
3. Right cancellation (a domain) shows that A′ is a smaller nonzero solution. Contradiction.

Only the *endomorphism* property of B ↦ B^{(Q)} is used. ∎ [v2: m4]

## 3. Theorem PTH (pointwise twisted half-field structure) [P; C]
**Setting.**
- V ⊂ F_q has dim_{F₂} V = ρ, and a := a(V) < ρ/2.
- C is the real relation with C(V) ⊂ F_Q, and Ṽ_C := C^{−1}(F_Q) ∩ F_q.
- k := dim_{F₂}(ker C ∩ F_q) ≤ a.
- A ∈ S_C∖{0} has minimal degree.

**Statement.**
- **(i)** A(F_Q) ⊆ Ṽ_C and dim A(F_Q) = m/2. Hence e := dim Ṽ_C − m/2 ∈ [0, k].
- **(ii)** dim(V ∩ A(F_Q)) ≥ ρ − e ≥ ρ − k ≥ ρ − a.
- **(iii)** If e = 0 (in particular if k = 0), then V = A(U) with U := A^{−1}(V) ∩ F_Q ⊂ F_Q, and deg A = a.

*Proof.*
1. **(i).** For x ∈ F_Q, C(A(x)) = (CA)(x) ∈ F_Q, and A(F_Q) ⊂ F_q. MI gives dim A(F_Q) = m/2. Also dim Ṽ_C = k + dim(F_Q ∩ C(F_q)) ≤ k + m/2.
2. **(ii).** V ⊂ Ṽ_C.
3. **(iii).** V ⊂ A(F_Q). HFD's twisted bound gives a ≤ deg A ≤ a. ∎

**Consequence (two-sided pointwise statement) [P]** [v2: FIX-2; replaces v1's false "exactly … deg A = a(V)"].
- **(→)** If a(V) = a < ρ/2, then there are A with deg A ≤ a, injective on F_Q, and e ≤ k ≤ a such that dim(V ∩ A(F_Q)) ≥ ρ − e. Moreover deg A = a and V = A(U) when e = 0.
  - **For e > 0, deg A can be < a(V).** Sharp family [P, referee]: take λ ∉ F_Q, K ⊂ F_Q of dimension a, R its subspace polynomial (in F_Q{τ}), and C := R∘λ^{−1}.
  - Then k = e = a, the minimal A is λ (degree 0), and (ii) holds with equality.
  - A random sample also gave deg A = 2 < a(V) = 3 with e = 1, at (16,8,3), seed 107 of the referee.
- **(←)** If dim(V ∩ A(F_Q)) ≥ ρ − c, then a(V) ≤ deg A + c [P, referee].
  - V′ := V ∩ A(F_Q) = A(U′) has a(V′) ≤ deg A.
  - Its profile gives ≥ j+1−deg A relations of degree ≤ j.
  - Extending to V imposes c linear conditions.
- So "twisted half-field of degree ≤ a up to codimension ≤ a" lies between {a(V) ≤ a} and {a(V) ≤ 2a}. **It is not a characterisation.**

**[C] pthcheck.py** [v2: m1, m2, m9]. Own code; `nice -n 19 python3 -I`. Commands and seeds are in pthcheck.log.
- **Samples.** 10 parameter runs, **435** samples in total, over (m,ρ,a) ∈ {(12,6,1), (12,6,2), (16,6,1), (16,6,2), (16,8,1), (16,8,2), (16,8,3), (20,10,2), (20,10,3), (20,10,4)}.
- **Runtime.** About 0.4–2 s per run for m ≤ 16, and about 38 s for m = 20.
- **Results.** 0 failures of a(V) = a, injectivity of A on F_Q, A(F_Q) ⊂ R_P, and the bound ρ − k.
- **[C, sampler]** V ⊂ A(F_Q) in **434/435** samples, and deg A = a in 434/435.
  - These frequencies describe the random-C sampler, in which e > 0 has probability about 1/Q. They say **nothing** about arc radicals.
  - The e > 0 cases are not only partial half-fields; see the referee's deg-2 case above.
- **Independent check.** The referee's code analysed 626 radicals (130 with e > 0) with 0 failures.

## 4. Proposition GO (generic Lang solvability ⟹ Kummer orbit bound ⟹ G1″ in a range) [COND on GLS₀ (or GLS₁), (GT), G4, WG [A], (B1a⁺), (B1b)] [v2: FIX-1]
**Setting.** [v2: FIX-1, m5, m6]
- L = F_q(X) and G := Gal(L^sep/L).
- **W** is the F₂-space of roots over L of the WG family B1 (weight u = R/4). dim W = ρ uses (B1b).
- **Input step: the generic relation on W [COND (B1a⁺), (B1b)].**
  - By (B1a⁺), the GL_ρ(F₂)-invariant Moore determinants D_{B1}(S_j ∪ T) (j = a*, EBR's test sets) are polynomials in F_q[X] of degree ≤ u[(2^{j+1}−1)(Q+1) + Σ_T 2^e].
  - This is ≤ Q²/2 < v in all 380 band cells (even ρ ∈ [4,40], g ∈ [ρ+3,2ρ]); the referee checked this, worst ratio 0.25.
  - By (B1b), they vanish at every α ∈ N, because a(W(α)) = a(V_α) ≤ a*. So they vanish identically.
  - Steinitz exchange and Galois descent of the G-stable relation space then give a nonzero relation C(w) = D(w^Q) over L, with deg ≤ a* (minimal degree a₂).
- **P := C + Dτ^{m/2}** has root space R_P with dim R_P ≤ deg_τ P ≤ m/2 + a₂. This holds for every nonzero linearised P; no hypothesis on c₀ is needed [v2: m5]. W ⊂ R_P.
- **Hypotheses.**
  - **(GLS₁)**, as in v1: a nonzero solution A ∈ L^sep{τ} of C·A = D·A^{(Q)} exists, and the minimal-degree solutions form one right F_Q-line.
  - **(GLS₀)**, weaker, from §4A: a nonzero solution exists. By Lemma ML it implies GLS₁, and no degree bound on A is used.
  - **(GT) gate:** the character χ has image of order < T. A sufficient condition, equivalent to it in all 78 range cells (referee): no ρ′ ∈ [ρ−a*, ρ] divides g + ρ/2.

**Statement.**
- **(a)** A(F_Q) ⊂ R_P is G-stable, and G acts on it through a character χ: G → F_Q^*: g(A(x)) = A(χ(g)x).
- **(b)** W′ := W ∩ A(F_Q) is G-stable, with dim W′ ≥ ρ − a₂.
- **(c)** Every w ∈ W′∖{0} has orbit size **exactly** |χ(G)| [v2: m6]. This divides 2^t − 1, where F_{2^t} is the stabiliser field of U′ := A^{−1}(W′) ∩ F_Q.
- **(d) [COND (GT), G4, WG [A]]** [v2: FIX-1] WG makes W′ rational, so dim W^rat ≥ ρ − a*.
- **(e)** If moreover a* ≤ (ρ−4)/3, then G1″ holds, and TCR v2.1 RS(a) excludes the configuration [COND on G2, (B1a), (I216′) incl. (B1b-fix), Prop 216.3].

*Proof.*
1. **(a)** P·A = CA + DA^{(Q)}τ^{m/2} = CA(1+τ^{m/2}), so P kills A(F_Q).
   - For g ∈ G, g(A) is again a minimal-degree solution, so g(A) = Aχ(g). This makes χ a homomorphism.
   - For x ∈ F_Q, g(A(x)) = A(χ(g)x).
2. **(b)** MI over L^sep gives dim A(F_Q) = m/2. Both W and A(F_Q) lie in R_P.
3. **(c)** χ(g)U′ = U′, and the multiplicative stabiliser of U′ together with 0 is a subfield. The orbit of A(x), x ≠ 0, is {A(χ(g)x)}, of size |χ(G)|.
   - Under the sufficient gate: t > ρ/2 would force t = ρ′ | m/2, which is excluded. So t ≤ ρ/2, and 2^t − 1 < T.
4. **(d)** WG excludes 1 < e_w < T.
5. **(e)** ρ − a* ≥ 2a* + 4 ⟺ a* ≤ (ρ−4)/3. ∎

**Coverage [C] (gocells.py, reproduced by the referee).** Even ρ ∈ [10, 40], cells ρ+3 ≤ g ≤ min(2ρ, ⌈3ρ/2⌉+2) not covered by NWF:
- **78** cells have a* ≤ (ρ−4)/3;
- **51** pass the gate;
- 27 fail it, e.g. (10,15), (14,21), (16,24), (18,27), (20,30).

In those 51 cells, GO reduces the structured branch to: GLS₀, (GT), G4, WG [A], (B1a⁺) and (B1b), plus the TCR v2.1 inputs [v2: FIX-1]. Other closed-cell results (C1, R6U, EDA) were not rechecked.

**Consistency with TX.** A = τ + X solves C·A = D·A^{(Q)}. The minimal solutions are exactly (τ+X)F_Q (referee), and χ is trivial.

## 4A. Adopted strengthening GO-S (from the audit) [P, referee; adopted in v2; NEEDS AUDIT] [v2: m8]
**Lemma ML (the line is automatic).** Let K be F_q or L^sep, and let deg C = a₂. Suppose C·A = D·A^{(Q)} has a nonzero solution in K{τ}, and let d be the minimal degree of a solution. Then:
- deg D = deg C;
- a₀ ≠ 0 and d₀ ≠ 0;
- the minimal-degree solutions, together with 0, form exactly one right F_Q-line.

*Proof (referee).*
1. **Top coefficients.** c_{a₂}a_d^{2^{a₂}} = d_{a₂′}a_d^{Q2^{a₂′}} forces a₂′ = a₂ and (a_d^{Q−1})^{2^{a₂}} = c_{a₂}/d_{a₂}.
2. **Two minimal solutions.** For A₁, A₂, the ratio r of their top coefficients satisfies r^{(Q−1)2^{a₂}} = 1, so r^{Q−1} = 1 in characteristic 2.
3. **They are proportional.** With ζ := r^{2^{−d}} ∈ F_Q, A₂ − A₁ζ is a solution of degree < d, hence 0.
4. **Bottom coefficients.** If a₀ = 0, then A = A′τ with A′ a smaller solution. Then c₀a₀ = d₀a₀^Q gives d₀ ≠ 0. ∎

**Consequences.**
- **(i)** GLS₁ ⟸ GLS₀. GO uses no degree bound on A.
- **(ii) χ is the Kummer character of c₀/d₀ ∈ L.** Comparing τ⁰-coefficients in g(A) = Aχ(g) gives χ(g) = g(a₀)/a₀, with a₀^{Q−1} = c₀/d₀. So (GT) is a condition on the generic relation alone. In TX, c₀/d₀ = X^{Q−1}, so χ is trivial.
- **(iii) Necessary conditions for GLS₀.**
  - deg D = deg C.
  - d₀ ≢ 0.
  - c_{a₂}/d_{a₂} ∈ L^{2^{a₂}} = F_q(X^{2^{a₂}}). Here y = a_d^{Q−1} is separable over L and y^{2^{a₂}} ∈ L.
  - These give a concrete test for a given family.
- **(iv) Algebraic closure.** If P is separable, a solution over L̄ already lies in L^sep{τ}: invert a Moore matrix over F_Q on the values A(x_j) ∈ R_P.

**[C] (referee).** The minimal-degree F_Q-dimension was 1 in all 746 C tested.

## 5. What remains [H]
- **GLS₀ is the generic counterpart of LS/PTH.** Lifting it from its pointwise truth meets the G1 obstruction: A_α depends on C̄_α, whose coefficients have degree about Q in α.
- **GLS₀ may fail generically.** ML(iii) makes this testable: c_{a₂}/d_{a₂} ∈ F_q(X^{2^{a₂}}) is necessary.
- **Updated reduction (adds a route; replaces nothing):** [v2: FIX-1]
  - G1″ ⇐ GLS₀ + (GT) + G4 + WG [A] + (B1a⁺) + (B1b), in the range a* ≤ (ρ−4)/3;
  - G1 ⇐ G1″ + G2 + (B1a) + (I216′)[incl. (B1b-fix)] + [A] Prop 216.3 (TCR v2.1).
- **OPEN:**
  - GLS₀;
  - the 27 gate-failing range cells;
  - the range a* > (ρ−4)/3.

## 6. Questions for Codex (for a later packet, after the revision check)
- **(a)** Does B1/STT give a twist A ∈ L^sep{τ} with C·A = D·A^{(Q)} (GLS₀)? Equivalently, is c₀/d₀ a Kummer class of small order, with c_{a₂}/d_{a₂} ∈ F_q(X^{2^{a₂}})?
- **(b)** Do MRL/MT ("L = S²+tS") identify structured-branch radicals as twisted half-fields with a global twist?
- **(c)** Confirm (B1a⁺) and (B1b) for B1.

## 7. Owner self-check (updated)
- **LS count:** m(a+1) + (m/2)(2a+1) − m(2a+1) = m/2.
- **MI:** uses only the injective-endomorphism property of the Q-twist on L^sep{τ} [v2: m4], plus right cancellation.
- **PTH(iii):** e = 0 ⇒ V ⊂ A(F_Q); deg A = a by HFD's twisted bound. For e > 0 no degree claim is made [v2: FIX-2].
- **GO(a):** the line clause is automatic by ML [v2: m8].
- **GO(b):** dim R_P ≤ deg_τ P for every nonzero P; the c₀ argument has been removed [v2: m5]. dim W = ρ by (B1b) [v2: FIX-1].
- **GO(c):** stabiliser is a field; orbit size is exactly |χ(G)| [v2: m6].
- **Points to audit.**
  - (1) The input step for the generic relation on B1: the degree arithmetic was referee-checked; the invariant-polynomial property needs (B1a⁺).
  - (2) Lemma ML as adopted.
  - (3) The "open cells" list relies on NWF only.

## 8. Change log v1 → v2
| Item | Where | Change |
|---|---|---|
| FIX-1 | §0, §4 header/Setting/(d), §5 | W defined as B1's root space. The generic relation is derived as an input step [COND (B1a⁺), (B1b)] with the referee's degree check. (B1a⁺), (B1b) and WG [A] added to the labels and the reduction. |
| FIX-2 | §3 Consequence | Replaced by the two-sided statement (→)/(←). The sharp e = a family recorded. "Exactly" and "deg A = a(V)" deleted for e > 0. |
| m1 | §3 [C] | 435 samples, 434/435. Runtimes corrected. |
| m2 | Title, §3 [C] | "Typically" dropped. Frequencies labelled [C, sampler]. e > 0 is not only partial half-fields. |
| m3 | §1 Remark | Existence only; S_C can have F_Q-dim a+1; the line is for minimal solutions (ML). |
| m4 | §0, §2, §7 | Endomorphism (not automorphism) of L^sep{τ}. |
| m5 | §4 Setting, §7 | c₀ argument removed: dim R_P ≤ deg_τ P always. |
| m6 | §4 | G defined; orbit size exactly |χ(G)|. |
| m7 | Title | Gate and conditional inputs added. |
| m8 | §4A, §7 | GO-S (Lemma ML, GLS₀, Kummer character, necessary test) adopted with credit; needs audit. |
| m9 | §3, scripts | Script paths and nice -n 19 noted. |
| m10 | §0 | WG [A] status carried. |

Scripts (archive paths under `claude_archive/`; in a packet they may ship as `owner_scripts/`) [v2: m9]:
- `scripts/pthcheck.py` and `.log`;
- `scripts/gocells.py` and `.log`.

Run as `nice -n 19 python3 -I <script> <args>`. The referee's checks are in `audit_PTH_checks/`.
