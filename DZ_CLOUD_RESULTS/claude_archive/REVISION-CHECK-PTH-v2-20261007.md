# REVISION CHECK — PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.md (independent referee, cloud session, 7 Oct 2026, 20:18–20:35Z)

Referee: a fresh, isolated subagent for the DZ line (project "Wan's numbers of PPs"). I had no contact with the owner session, with Codex, or with the v1 auditor.

Labels follow the handoff: [P] proof, [C] computation, [H] heuristic, [A] reading of a source. "[P, RC]" marks a proof given by this referee.

**Documents checked**

| Role | File | sha256 |
|---|---|---|
| Under check | `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.md` | `478ffaf98bd7108f3b8b4b3cce1dbb9da999e76b7fa0896c5ebd19ebe5dfea87` |
| Baseline (v1) | `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007.md` | `3e17d28c056982a35834fcadf94aa81ba28cac9d2dd1724615bd9165c2680a03` |
| v1 audit | `AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md` | `b3c01e587f0a4e315cf82c501a90fefbefecef2e885640ef1b86b3e3d2ce4e58` |

The `src/` copies and the `claude_archive/` copies of all three files are byte-identical.

## 0. Verdict: **PASS-with-fixes**

**Status of the audit's fixes**
- FIX-2 and all ten minor items (m1–m10) are ADDRESSED.
- FIX-1 is PARTIAL. Its mathematical substance is fully in place: W is defined, the input step for the generic relation is stated and correct, and the inputs are named in the header, in §5 and in the "reduces to" sentence. Two small items remain:
  - the label on GO(d) does not list (B1a⁺) and (B1b);
  - the symbol `v` in the input step is never defined.
  - Both are cosmetic (RC-7, RC-8).
- Both substantive fixes were re-derived independently (§2). They are correct.

**The adopted strengthening GO-S (§4A): PASS-with-fix.**
- **Correct:**
  - the "line" clause of Lemma ML;
  - deg D = deg C;
  - a₀ ≠ 0;
  - the top Kummer identity;
  - GLS₀ ⟹ line clause, and GO's independence from any degree bound on A;
  - χ(g) = g(a₀)/a₀;
  - the necessary test c_{a₂}/d_{a₂} ∈ F_q(X^{2^{a₂}}).
- **One clause of Lemma ML is false as stated: "d₀ ≠ 0".**
  - Counterexample: K = F_q and C = D = τ. Then A = 1 solves C·A = D·A^{(Q)}, yet d₀ = 0.
  - In general c₀a₀ = d₀a₀^Q only gives c₀ = 0 ⟺ d₀ = 0.
  - v2 removed the c₀ ≢ 0 hypothesis (m5) and adopted ML in the same revision. As a result, Consequence (ii) ("Kummer character of c₀/d₀"), (iii) ("d₀ ≢ 0" is necessary) and §6(a) now rest on a hypothesis the note no longer has.
  - The repair is one line and loses nothing; see RC-1.
- **Consequence (iv) needs the hypothesis deg A < m/2** (RC-4).

**New issues**
- **4 must-fix (RC-1 to RC-4).** Each is a one-line restatement; no proof needs to be rewritten.
- **8 cosmetic (RC-5 to RC-12).**
- No mathematical error was found in LS, MI, PTH (i)–(iii), the two-sided Consequence, or GO (a)–(e).

**Outbox:** not as is. A small owner edit (RC-1 to RC-4, about 6 lines) is needed. After that edit, PTH v2.1 can go to the outbox without another full check: the edits are restatements, and a diff check suffices.

## 1. Fix-by-fix table

| Fix | Audit requirement (short) | Location in v2 | Status | Notes |
|---|---|---|---|---|
| FIX-1 | Define W as B1's root space. State the generic-relation input step [COND (B1a⁺),(B1b)]. Note that dim W = ρ uses (B1b). Add (B1a⁺), (B1b), WG [A] to the GO header, the GO(d) label, the §5 line and the "reduces to" sentence. | §0 l.19–21; §4 header l.79; Setting l.82–88; (d) l.98; l.116; §5 l.148 | **PARTIAL** | Substance complete and re-derived (§2.1). (d) carries only "(GT), G4, WG [A]" (RC-7). `v` is undefined (RC-8). |
| FIX-2 | Replace the false "Consequence" with a two-sided statement. Delete "exactly" and "deg A = a(V)". Optionally record the e = a family. | §3 l.59–68 | **ADDRESSED** | (→) and (←) re-derived (§2.2). The sharp-family bullet leaves V unspecified and labels a [C] fact as [P] (RC-5). |
| m1 | 435 samples, 434/435; runtimes | §3 l.71–74 | **ADDRESSED** | Owner scripts re-run byte for byte (§5). |
| m2 | Drop "typically"; [C, sampler]; e > 0 cases are not only partial half-fields | Title; l.74–76 | **ADDRESSED** | |
| m3 | LS gives existence only; dim_{F_Q} S_C can be a+1; the line is for minimal solutions | §1 Remark l.30 | **ADDRESSED** | |
| m4 | Endomorphism, not automorphism, on L^sep{τ} | l.16, l.40, l.162 | **ADDRESSED** | |
| m5 | Remove or complete c₀ ≢ 0 | l.88, l.165 | **ADDRESSED** | The removal interacts with ML's "d₀ ≠ 0" (RC-1). |
| m6 | Define G; orbit size exactly \|χ(G)\| | l.81, l.97, l.106 | **ADDRESSED** | |
| m7 | Title: the gate and the conditional inputs | Title | **ADDRESSED** | Wording nit in RC-9. |
| m8 | Optionally adopt GO-S / GLS₀, marked as needing audit | §4A; l.91; l.164 | **ADDRESSED** | Adopted. Audited in §3 below. |
| m9 | Script paths; `nice -n 19` | l.70, l.188–192 | **ADDRESSED** | `scripts/pthcheck.py`, `scripts/gocells.py` and `audit_PTH_checks/` all exist in `claude_archive/`. |
| m10 | Carry WG's [A] status | §0 l.19 | **ADDRESSED** | |

**Counts:** ADDRESSED 11, PARTIAL 1, NOT ADDRESSED 0.

On the number of minor items: v2's "10 minor items m1–m10" is correct. The audit's headline "9 minor" was the audit's own miscount, since its list runs m1–m10. No action needed.

## 2. Re-derivation of the substantive fixes

### 2.1 FIX-1: the input step for the generic relation (v2 l.83–87) [P, RC] — correct

**Integrality.**
- Let w₁, …, w_ρ be an F₂-basis of W ⊂ L^sep. Each test determinant D_{B1}(S_j ∪ T) is a ρ×ρ Moore determinant.
- A change of basis multiplies it by det g = 1, since g ∈ GL_ρ(F₂). G permutes W. So the determinant lies in L.
- The roots are integral over F_q[X], because B1 is monic over F_q[X] (B1a⁺). F_q[X] is integrally closed, so the determinant lies in F_q[X].
- Each term of the expansion is a product of entries w^{exponent}, one per row. Its pole order is ≤ u·Σ(row exponents) = u[(2^{j+1}−1)(Q+1) + Σ_T 2^e].

**Size of the degree bound [C, RC] `rc_go.py`.**
- Recomputed in all 380 cells (even ρ ∈ [4,40], g ∈ [ρ+3, 2ρ]), taking the worst admissible T ⊂ [j+1, ρ−1] with |T| = ρ−2j−2.
- Result: ≤ Q²/2 everywhere, with worst ratio deg/(Q²/2) = 0.25, at (ρ,g) = (40,43). This matches the audit and v2.
- Also checked: j = a* = ρ−⌈g/2⌉ = ρ−1−⌊(g−1)/2⌋ ≤ ρ/2−2 in every cell.
- **The restriction to ρ ≤ 40 is unnecessary [P, RC].** Since j ≤ ρ/2−2:
  deg < 2^{g−2}(2^{ρ/2−1}·2^{g+ρ/2} + 2^ρ) = 2^{2g+ρ−3} + 2^{g+ρ−2} ≤ 2^{2g+ρ−2} = Q²/4.
  This holds for every cell of the band (optional, RC-12).

**Q²/2 < v.**
- Q² = R²K, so this is EBR's v > KR²/2, where v is the number of original nonfoci (EBR Lemma G, [A]).
- v2 never defines v (RC-8).

**Vanishing.**
- Let α ∈ N. Under (B1b), B1(α) has the ρ-dimensional root space W(α), which is a Frobenius twist of V_α. So the generic determinant specialises to the Moore determinant of W(α).
- Defect is Frobenius-invariant: if C(V) ⊂ F_Q, then C^{(2^s)}(V^{2^s}) ⊂ F_Q. So a(W(α)) = a(V_α) ≤ a*, and the 2j+2 forms on S_j are dependent on W(α).
- Hence every test determinant vanishes at more than deg-many points, so it vanishes identically.

**Steinitz and descent.**
- Suppose the forms on S_j were independent on W over L^sep. The Moore rows F^0, …, F^{ρ−1} have rank ρ on W. Steinitz exchange would give T ⊂ [j+1, ρ−1] with D(S_j ∪ T) ≢ 0, a contradiction. So the relation space over L^sep is nonzero.
- That space is G-stable (G permutes W) and is defined over a finite Galois extension. Galois descent (Speiser) gives a basis over L, so there is a nonzero (C, D) over L with deg ≤ a*.
- Neither C nor D can be 0. Otherwise a nonzero linearised polynomial of degree ≤ a* < ρ would kill W or W^Q, which have dimension ρ.

**Conclusion.** The step is correct as stated, [COND (B1a⁺), (B1b)], with EBR's v-bound as [A].

**GO (a)–(e) under GLS₀ were re-checked line by line. All PASS.**
- (a): P·A = CA(1+τ^{m/2}). g(A) is again minimal, ML gives the line, and χ is a homomorphism because χ(h) ∈ F_Q is G-fixed.
- (b): MI holds over L^sep, and dim R_P ≤ deg_τ P = m/2 + deg D.
- (c): the stabiliser is a field. The orbit of A(x) is {A(χ(g)x)}, of size exactly |χ(G)|.
- (d): if t > ρ/2, then t | ρ′ and ρ′ < 2t force t = ρ′ | m/2.
- (e): ρ − a* ≥ 2a* + 4 ⟺ a* ≤ (ρ−4)/3.
- Gate recount [C, RC]: 78 / 51 / 27 cells, with the five listed failures present. The sufficient gate coincides with the exact stabiliser obstruction ("some admissible U′ has 2^t − 1 ≥ T") in all 78 cells (0 mismatches).

### 2.2 FIX-2: the two-sided Consequence (v2 l.59–68) [P, RC] — correct

**(→)** This is PTH (i)–(iii) restated. It is valid for a(V) = a < ρ/2.

**(←)** Let d := deg A and V′ := V ∩ A(F_Q) = A(U′), U′ ⊂ F_Q.
- The left-Lang count gives a nonzero C′ ∈ F_q{τ}_{≤d} with C′A ∈ F_Q{τ}. The F₂-count is m(d+1) + (m/2)(2d+1) − m(2d+1) = m/2 > 0. So C′(V′) ⊂ F_Q, which is HFD's twisted bound.
- The pairs (EC′, EC̄′), with E ∈ F_q{τ}_{≤j−d}, are F_q-independent relations of degree ≤ j on V′. They span dimension j−d+1.
- Each of the c extra basis vectors of V imposes one F_q-linear condition on a pair (C, D).
- So for j ≥ d + c a nonzero relation survives on V. The relation space is χ-stable, so it contains a nonzero real relation, and a(V) ≤ d + c. ✓

**The sandwich {a(V) ≤ a} ⊆ TH(a, a) ⊆ {a(V) ≤ 2a}** is correct for a < ρ/2.

**Sharp family: precision issue (RC-5).**
- The bullet takes C := R∘λ^{−1} and concludes "k = e = a, minimal A = λ, (ii) with equality" without saying which V.
- For C to be *the* real relation of V, PTH needs a(V) = a. Some V ⊂ Ṽ_C fail this: any ρ-subspace of λF_Q lies in Ṽ_C but has a(V) = 0 (`rc_ml.py sharp`).
- [C, RC]: I placed (ρ−a) vectors in λF_Q and added a random vectors of Ṽ_C, 75 cases at (m,ρ,a) = (12,6,1), (12,6,2), (16,8,2), (16,8,3).
  - k = e = a and deg A_min = 0 always.
  - a(V) = a occurred in exactly 40 of the 75 cases.
  - Equality dim(V ∩ λF_Q) = ρ − e also held in exactly 40 cases. Each run's equality count equals its a(V) = a count; I did not log the per-case pairing.
  - (ii) failed in 0 cases.
- So the family must specify V: dim(V ∩ λF_Q) = ρ − a and a(V) = a. The fact a(V) = a is [C] (the audit had 128/128 for its construction; this check gave 40/75 for a random completion). It is not [P].

## 3. Audit of the adopted strengthening GO-S (§4A), as new material

### 3.1 Lemma ML, clause by clause [P, RC]

Setup: K is a field of characteristic 2 containing F_Q (here F_q or L^sep), and C, D ∈ K{τ} with C ≠ 0. B ↦ B^{(Q)} is an injective ring endomorphism, so the solution set of C·A = D·A^{(Q)} is an F₂-space. It is closed under A ↦ Aζ for ζ ∈ F_Q, since ζ^{(Q)} = ζ. More generally it is a right F_Q{τ}-module.

| Clause | Check | Verdict |
|---|---|---|
| Nonzero solution ⟹ D ≠ 0 | D = 0 gives CA = 0, so A = 0 (domain). | OK (implicit in v2) |
| deg D = deg C | Top terms: c_{a₂}a_d^{2^{a₂}}τ^{a₂+d} = d_{a₂′}a_d^{Q2^{a₂′}}τ^{a₂′+d}. | **OK** |
| Top Kummer identity (a_d^{Q−1})^{2^{a₂}} = c_{a₂}/d_{a₂} | Same comparison. | **OK** |
| Minimal-degree solutions ∪ {0} form one F_Q-line | r^{(Q−1)2^{a₂}} = 1 ⟹ r^{Q−1} = 1 (Frobenius injective). ζ = r^{2^{−d}} ∈ F_Q. A₂ − A₁ζ is a solution of lower degree, so it is 0. A₁ζ has degree d for ζ ≠ 0. | **OK** |
| a₀ ≠ 0 | If a₀ = 0, then A = A′τ (right factor). Since τ^{(Q)} = τ, right cancellation gives CA′ = DA′^{(Q)} with deg A′ < d. | **OK** |
| d₀ ≠ 0 | The τ⁰-coefficients give c₀a₀ = d₀a₀^Q. With a₀ ≠ 0 this gives only **c₀ = 0 ⟺ d₀ = 0**. | **FALSE as stated** (RC-1) |

**Counterexample to "d₀ ≠ 0" [P, RC].**
- K = F_q, C = D = τ: A = 1 is a minimal solution (degree 0) with a₀ = 1, but d₀ = 0.
- This is even of PTH type, since D = C^{(Q)}.
- More generally, (C₁τ, D₁τ) has the solutions A = A₁^{(1/2)}, where A₁ solves (C₁, D₁), and c₀ = d₀ = 0.
- [C, RC] `rc_ml.py`, modes conj0 and gen0: 540 such pairs at m = 8, 12, 16 and a = 1, 2, 3. All were solvable, all had a₀ ≠ 0, and all had d₀ = 0.

**Where the false clause propagates.**
- The original GO-S assumed c₀ ≢ 0, as v1 §4 did. v2 dropped that assumption on the audit's advice (m5), which was correct for GO(b), but kept the "d₀ ≠ 0" clause.
- Downstream:
  - Consequence (ii): a₀^{Q−1} = c₀/d₀ is meaningless if c₀ = d₀ = 0;
  - Consequence (iii): "d₀ ≢ 0" is listed as necessary;
  - §6(a): "c₀/d₀ a Kummer class".
- **Pointwise there is no problem.** For PTH's C, HFD §1 gives c₀ ≠ 0, so d₀ = c̄₀ ≠ 0.

**Repair, losing nothing [P, RC].**
- Let i be the least index with (c_i, d_i) ≠ (0, 0). The τ^i-coefficients give c_i a₀^{2^i} = d_i a₀^{Q2^i}. With a₀ ≠ 0, both c_i and d_i are nonzero, and (a₀^{Q−1})^{2^i} = c_i/d_i.
- y := a₀^{Q−1} is G-fixed, since g(a₀) = a₀χ(g) and χ(g)^{Q−1} = 1. So y ∈ L, and in particular c_i/d_i ∈ L^{2^i}.
- Hence χ is the Kummer character of y ∈ L. Here y = c₀/d₀ when c₀ ≢ 0, and in general y is the unique 2^i-th root in L of c_i/d_i. (GT) remains a property of the generic relation alone.
- [C, RC]: the generalised bottom identity held in all 1,080 solvable cases, with 0 failures.

### 3.2 Consequences (i)–(iv)

- **(i) GLS₀ ⟹ line clause; GO uses no degree bound on A.** Correct.
  - GO(a) uses only ML's line clause. GO(b) uses MI and P·A = CA(1+τ^{m/2}), neither of which involves deg A. (c)–(e) do not involve A's degree.
  - Caveat RC-10: v2 calls GLS₁ "as in v1", but restates it *without* v1's bound deg A ≤ a₂. "GLS₁ ⟸ GLS₀" is true only for the restated GLS₁. With v1's GLS₁ the correct relation is GLS₁ ⟹ GLS₀, and GLS₀ already suffices for GO.
- **(ii) χ(g) = g(a₀)/a₀.**
  - Correct: compare the τ⁰-coefficients of g(A) = Aχ(g).
  - The identification with c₀/d₀ needs c₀ ≢ 0 (RC-1).
  - TX check [P, RC] from RBL v2.1 §2: C = τ + X^Q(X+X^Q) and D = τ + X(X+X^Q), so c₀/d₀ = X^{Q−1}. A = τ + X gives CA = DA^{(Q)} = τ² + (X²+X^{Q+1}+X^{2Q})τ + X^{Q+1}(X+X^Q). Then a₀ = X, and χ is trivial. ✓
- **(iii) c_{a₂}/d_{a₂} ∈ L^{2^{a₂}} = F_q(X^{2^{a₂}}).**
  - Correct: y = a_d^{Q−1} ∈ L^sep, and y^{2^{a₂}} ∈ L, so y is separable and purely inseparable over L, hence y ∈ L. Also F_q is perfect.
  - "deg D = deg C" is correctly listed as necessary.
  - "d₀ ≢ 0" is **not** necessary. Replace it with "c₀ ≡ 0 ⟺ d₀ ≡ 0, and c_i/d_i ∈ L^{2^i} at the least such i" (RC-1).
- **(iv) "If P is separable, a solution over L̄ already lies in L^sep{τ}".**
  - The Moore-matrix inversion over F_Q recovers the coefficients of A from its values A(x_j) on an F₂-basis of F_Q **only if deg A < m/2**.
  - For any solution B, B·(τ^{m/2}+1) is again a solution and vanishes on F_Q, since (τ^{m/2}+1)^{(Q)} = τ^{m/2}+1. [C, RC]: this held in all 1,080 cases. So the values do not determine high-degree solutions.
  - Add "of degree < m/2" (RC-4). This is satisfied in GO's setting whenever deg A ≤ a₂ ≤ a* < ρ/2 < m/2.
  - (iv) is not used in GO's logic.
- **[C] "minimal-degree F_Q-dimension 1 in all 746 C".** This is quoted from the audit. Independent confirmation [C, RC] (`rc_ml.py`):
  - 1,080 solvable (C, D) pairs at m = 8, 12, 16 and a = 1–3;
  - four modes, including *general* D not of conjugate type (mode gen, (C, D) solved from a random A₀);
  - results: line clause 0 failures, deg D = deg C 0 failures, top Kummer 0 failures, a₀ ≠ 0 always, MI 0 failures, and c₀ = 0 ⟺ d₀ = 0 always.

**Strengthening verdict: PASS-with-fix.** The core (line clause, GLS₀, χ via a₀, top-coefficient test) is sound. The "d₀ ≠ 0" clause and the consequences built on it need the one-line repair above. (iv) needs a degree hypothesis.

## 4. Diff v1 → v2: unintended changes, overclaims, label errors

The diff has 266 changed lines. All intended changes match the change log (§8 of v2). I found these points that the change log does not record:

1. **(GT) "equivalent to it in all 78 range cells (referee)"** (l.92): this misquotes the audit. The audit showed that the sufficient gate is equivalent to the *stabiliser obstruction* (t ≤ ρ/2 for every admissible U′). It did not show equivalence to (GT) itself, i.e. |χ(G)| < T. (GT) can hold in gate-failing cells; in TX, for example, χ is trivial. This is an overclaim → RC-2.
2. **§6(a) "Equivalently, is c₀/d₀ a Kummer class of small order, with c_{a₂}/d_{a₂} ∈ F_q(X^{2^{a₂}})?"**: GLS₀ is *not* equivalent to these. Small order is (GT), and the second condition is only necessary. This is an overclaim in text meant for Codex → RC-3.
3. **GLS₁ silently redefined.** v2 drops v1's deg A ≤ a₂ while saying "as in v1" (l.90). → RC-10.
4. **ML/m5 interaction.** Removing c₀ ≢ 0 while adopting ML's "d₀ ≠ 0" leaves Consequences (ii)/(iii) and §6(a) without their hypothesis. → RC-1.
5. Harmless omissions:
   - PTH(iii) no longer states dim U = ρ; it follows from MI.
   - The k = 0 ⇒ e = 0 proof line was dropped; it follows from (i), e ∈ [0, k].
   - "k took the values 0–3" was dropped.
   - The approximation "g < about (4ρ+8)/3" was dropped from §5.
   - None of these needs action.
6. Labels:
   - §5 says "ML(iii)", but ML has no item (iii); it means §4A Consequence (iii) (RC-11).
   - The sharp family is labelled [P, referee], but its key fact a(V) = a is [C] (RC-5).
   - The random deg-2 sample (seed 107) sits inside that [P] bullet and should read [C, referee].
7. Not regressions:
   - The v2 header count "10 minor items" is correct.
   - The archive paths in m9 exist.
   - TX is unchanged and re-verified (§3.2).

## 5. RC list

**Must-fix before the outbox.** All four are one-line restatements; no proof changes.
- **RC-1 (ML "d₀ ≠ 0").**
  - Replace "a₀ ≠ 0 and d₀ ≠ 0" by: "a₀ ≠ 0; c₀ = 0 ⟺ d₀ = 0; in particular d₀ ≠ 0 when c₀ ≠ 0 (always the case pointwise, by HFD §1)".
  - Proof step 4: "…gives d₀ ≠ 0 *if c₀ ≠ 0*".
  - Consequence (ii): "χ is the Kummer character of y := a₀^{Q−1} ∈ L, where y^{2^i} = c_i/d_i for the least i with c_i ≠ 0. So y = c₀/d₀ when c₀ ≢ 0."
  - Consequence (iii): replace "d₀ ≢ 0" by "c₀ ≡ 0 ⟺ d₀ ≡ 0, and c_i/d_i ∈ L^{2^i} at the least such i".
  - §6(a): replace c₀/d₀ by y.
  - Counterexample to the current clause: C = D = τ, A = 1.
- **RC-2 ((GT) wording, l.92).** Replace "equivalent to it in all 78 range cells (referee)" by "which in all 78 range cells is equivalent to the stabiliser bound t ≤ ρ/2 holding for every admissible U′ (referee); (GT) itself may still hold in gate-failing cells".
- **RC-3 (§6(a) "Equivalently").** Replace by "In particular (necessary conditions): c_{a₂}/d_{a₂} ∈ F_q(X^{2^{a₂}}), and (GT) asks that y have small order in L^*/L^{*(Q−1)}".
- **RC-4 (§4A (iv)).** Add "of degree < m/2". The Moore inversion needs it, and B(τ^{m/2}+1) shows that high-degree solutions are not determined by their values on F_Q.

**Cosmetic.**
- **RC-5 (sharp family, l.61–63).** Specify V: "V ⊂ Ṽ_C with dim(V ∩ λF_Q) = ρ − a and a(V) = a". Label a(V) = a as [C, referee] (128/128 in the audit's construction; 40/75 for this check's random completion). Label the seed-107 sample [C, referee].
- **RC-6 (title).** "contains a twisted half-field A(F_Q) ∩ V of codimension e ≤ a" should read "of codimension ≤ e ≤ a". Add "a < ρ/2".
- **RC-7 (FIX-1 residual).** Add (B1a⁺) and (B1b) to the GO(d) label (l.98), or write "[COND as in the header]".
- **RC-8 (FIX-1 residual).** Define v at l.85: "v := number of original nonfoci; v > KR²/2 = Q²/2 (EBR, [A])".
- **RC-9 (l.116).** In the 51 gate-passing cells (GT) is *implied* by the sufficient gate. Listing it as a remaining input is redundant; say "(GT) automatic there".
- **RC-10 (l.90).** GLS₁ is restated without v1's deg A ≤ a₂ but called "as in v1". Either restore the bound and write "GLS₁ ⟹ GLS₀, which suffices", or drop "as in v1".
- **RC-11 (§5 l.146).** "ML(iii)" should read "§4A Consequence (iii)".
- **RC-12 (optional, l.85).** The restriction "in all 380 band cells" can be lifted: the bound gives deg < Q²/4 for every cell of the band (§2.1). Also note in §3 that R_P (l.73) is the root space of P = C + C̄τ^{m/2}, since P is defined only in §4. Also note that (B1b) is cited as "(RBL v2.1)", where RBL v2.1 lists it as an [A]-pending identification input.

**Counts:** 12 RC in total: 4 must-fix (blocking for the outbox, small edit) and 8 cosmetic.

## 6. Files read
- **Handoff (read-only):**
  - `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`, read fully. It contains no referee-specific restriction on which files a referee may read; `grep -ril referee` over the handoff returned nothing. Its labelling and audit rules were followed.
  - `work/DZ-CLOUD-HANDOFF/notes/EBR-EVEN-BAND-REDUCTION-NOTE-20261007.md`, lines 1–80 (Lemma G, the v-bound, test sets).
  - Recursive listing of `work/DZ-CLOUD-HANDOFF/`.
- **Under check (`referee_PTHv2/src/`):** the v2 note, the v1 note, and the v1 audit, all read fully.
- **Archive (`DZ_CLOUD_RESULTS/claude_archive/`, read-only):**
  - directory listings of the archive, `scripts/` and `audit_PTH_checks/` (names only);
  - sha256 of the PTH v1, PTH v2 and AUDIT-PTH copies;
  - `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md`: a grep for B1a/B1b/TX, plus lines 36–70 and 200–212 (Proposition TX, the (B1a)/(B1b) definitions);
  - `scripts/{pthcheck.py, pthcheck.log, gocells.py, gocells.log}`, copied to `checks/owner_copy/` and read.
- Listing of `scratchpad/dz_isolated/`, top level only.
- **Not read:** HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads, any other scratchpad directory, and the v1 auditor's check code. No git was used. Nothing in DZ_CLOUD_RESULTS was modified except adding this file.

## 7. Computations (`checks/`, all `python3 -I`, one process at a time, total under 3 min)
- **`owner_copy/`**: byte copies of `pthcheck.py`, `pthcheck.log`, `gocells.py` and `gocells.log`.
  - Re-runs with the logged arguments (pthcheck under `nice -n 19`): `pthcheck_rerun.log` and `gocells_rerun.log` are **byte-identical** to the owner logs.
  - Totals: 435 samples, a(V) = a in all, 434 fully twisted, deg A = a in 434 (the exception has deg A = 0, at (16,6,1)). This matches v2 §3 exactly.
- **`rc_ml.py` → `rc_ml.log`** (own GF(2^m) log tables with fixed primitive polynomials, and an own F₂/F_q echelon).
  - Modes conj, conj0, gen and gen0, at m = 8, 12, 16 and a = 1, 2, 3: 1,080 solvable (C, D) pairs.
    - Line clause, deg D = deg C, top Kummer, a₀ ≠ 0, MI, generalised bottom identity, and c₀ = 0 ⟺ d₀ = 0: 0 failures.
    - d₀ = 0 in all 540 c₀ = 0 cases: the counterexample to ML's "d₀ ≠ 0".
    - B(τ^{m/2}+1) was a solution vanishing on F_Q in all 1,080 cases (the RC-4 caveat).
  - Mode sharp: 75 cases of C = R∘λ^{−1}, with k = e = a and deg A_min = 0. a(V) = a in 40/75, the (ii) equality count matched the a(V) = a count in each run (pairing not logged), and (ii) failed 0 times. A ρ-subspace of λF_Q lies in Ṽ_C with a(V) = 0 (RC-5).
- **`rc_go.py` → `rc_go.log`**:
  - the input-step degree bound in 380 cells: 0 violations, worst ratio 0.25 at (40,43);
  - the gate recount 78/51/27, with 0 mismatches between the sufficient gate and the exact stabiliser obstruction, and the five listed failures present.
- **Hashes:** `checks/checks_SHA256SUMS.txt`.
