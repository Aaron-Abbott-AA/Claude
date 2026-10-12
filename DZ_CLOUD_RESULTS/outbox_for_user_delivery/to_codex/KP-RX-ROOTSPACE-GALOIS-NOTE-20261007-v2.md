# The ker P̃ question of SH v2, answered negatively for m = 24, …, 44: the RX root space R_P has NO G-stable subspace of band dimension [6, (m−6)/3]. For m ≡ 0 (mod 4) with m = 24, …, 44, G acts irreducibly on R_P/W. For m ≡ 2 (mod 4) with m = 26, …, 42, only hyperplanes (and, untested for m ≥ 26, lines) can be G-stable. Lines are excluded for m = 10, 14, 18, the m searched [v2: m4]. Method: Frobenius characteristic polynomials at places of degree 2, computed through the σ-module. (Owner note **v2**, cloud session, 12 Oct 2026, 00:05Z; v1 7 Oct 2026, 23:30Z.)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac; no mailbox access).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- v1 (sha256 87430b2398f7858c53fcc92ad5d87b395eeefd382af2c90d0354985a89256ffd) was independently audited in AUDIT-KP-RX-ROOTSPACE-GALOIS-20261007.md (sha256 7639a0ae…b4ee7b). Verdict: **PASS-with-fixes** (2 substantive FIX-1, FIX-2; 6 minor m1–m6; wording and records only). The computations were VERIFIED.
- **This v2** applies all of them. Each change is marked [v2: FIX-n] or [v2: m-n], and the change log is §10.
- **STATUS: v2 — PENDING DIFF-CHECK.** Packet EN is prepared in the outbox, marked PENDING DIFF-CHECK (NOT READY).

**Scope.** HANDBACK-20261007T2303Z §2 lists the targets:
- item 1: device steps, impossible here;
- item 2: questions to Codex, which need the mailbox;
- item 3: the ker P̃ question. **This note takes item 3.**

**What is not claimed.** GLS₀ for the arc family, the even-band question for general W, G1 and the linear-gap conjecture are not claimed. The results are for **RX's polynomial** (a = 1) and for the listed m only.

## 0. Setting
- **RX (a = 1).** W = F₂[X]_{≤2}. P = c₀ + c₁τ + d₀τ^h + d₁τ^{h+1}, with h = m/2 and (c₀, c₁, d₀, d₁) the Vandermonde cofactors (RX v2 §2; SH v2 RK step 1).
- **The quotient.** P = P̃·M_W, where M_W is the subspace polynomial of W (monic, F₂[X] coefficients). P̃ ∈ F₂[X]{τ} has τ-degree n := h − 2.
- **The map.** M_W maps R_P G-equivariantly onto ker P̃, with kernel W [P, referee, SH audit §2.4].
- **The question (SH v2 §3, §5(c), FIX-2).** Are there G-stable W″ with W ⊂ W″ ⊂ R_P and 6 ≤ dim W″ ≤ (m−6)/3? Any such W″ would inherit RX's unique (N0) relation and its GLS₀ failure.

## 1. Lemma FR (Frobenius characteristic polynomial through the σ-module) [P]
**Statement.** Let k = F_{q^r} = F_{2^N} (N = mr), and let P̃ ∈ k{τ} be separable of τ-degree n, with nonzero constant and leading coefficients. Let V := ker P̃ ⊂ k̄ (an n-dimensional F₂-space) and let Fr: x ↦ x^{2^N}. Put M := k{τ}/k{τ}·P̃, with left multiplication by τ. Then:
- τ^N acts k-linearly on M;
- its characteristic polynomial equals the characteristic polynomial of Fr on V, and in particular lies in F₂[T].

*Proof.*
1. **Linearity.** τ^N c = c^{2^N}τ^N = cτ^N for c ∈ k.
2. **An isomorphism** [v2: m1]. Let M̄ := k̄{τ}/k̄{τ}P̃ = k̄ ⊗_k M, via λ ⊗ f ↦ λf. The map Φ: λ ⊗ f ↦ (v ↦ λf(v)) is k̄-linear and sends M̄ to Hom_{F₂}(V, k̄).
   - It is well defined, because P̃ vanishes on V.
   - It is injective: a nonzero f of degree < n has fewer than 2^n roots.
   - Both sides have dimension n over k̄.
3. **Frobenius.** For f ∈ M (coefficients in k), (τ^N f)(v) = f(v)^{2^N} = f(v^{2^N}) = f(Fr v). So τ^N ⊗ 1 on k̄ ⊗_k M corresponds to precomposition with Fr, the transpose of Fr ⊗ 1. This is **not** left multiplication by τ^N on M̄, which is only 2^N-semilinear over k̄ [v2: m1]. Transposes have the same characteristic polynomial. ∎

**Matrix form.** In the basis 1, τ, …, τ^{n−1}, τ acts as v ↦ A·σ(v), where σ squares entries and A is the companion matrix of p̃_n^{−1}P̃. Hence τ^N = A·σ(A)·…·σ^{N−1}(A).

## 2. Lemma GS (G-stable subspaces from Frobenius elements) [P; standard Galois theory [A]]
**Statement.** Let 𝔭 be a place of L = F_q(X) of degree r, X ↦ α ∈ F_{q^r}, with d₁(α)c₀(α) ≠ 0 and dim W(α) = 3. Then:
- P̃_α is separable of degree n;
- the roots of P̃ reduce bijectively onto ker P̃_α;
- a Frobenius element Fr_𝔭 ∈ G acts on ker P̃ with the characteristic polynomial of Lemma FR (with k = F_{q^r}).

**Consequences.**
- If U ⊂ ker P̃ is G-stable with dim U = k, then for every such 𝔭, k is a sum of irreducible-factor degrees (with multiplicity) of that characteristic polynomial, since the restriction to U has a characteristic polynomial dividing it.
- In particular, G acts irreducibly on ker P̃ if the **intersection** of the subset-sum sets over the sampled 𝔭 is {0, n}. This holds a fortiori if some Fr_𝔭 has an irreducible characteristic polynomial of degree n [v2: FIX-1].
- [v2: m2] **Which group.** G here is the arithmetic Galois group Gal(L^sep/L), L = F_q(X), as in SH v2's question. Subspaces stable only under the geometric subgroup Gal(L^sep/F̄_qL) are not addressed.

*Proof.*
1. **Integrality.** P̃ has F₂[X] coefficients and leading coefficient d₁ (M_W is monic). So d₁^{−1}P̃ is monic over the local ring at 𝔭, and its roots are integral there.
2. **Separability.** The constant term is c₀/(M_W)₀, which is nonzero at α because W(α) has dimension 3. So the reduction is separable of full degree, and distinct roots reduce to distinct roots.
3. **Frobenius.** The decomposition group's Frobenius acts on residues as the q^r-power. The final statement is linear algebra. ∎

**Remark [A, SH audit §2.4; P via PTH].** Places of degree 1 with α ∉ Z = F_Q (Z from RX v2 (vi); Z = F_Q for a = 1) [v2: m6] are uninformative. There, pointwise real type makes P̃_α have ≥ n−1 roots in F_q, so Frobenius is nearly trivial. [C, referee F5] confirmed dim(ker P̃_α ∩ F_q) ≥ n−1 at 210/210 such α, for m = 10..26. Degree-2 places are used instead.

## 3. Theorem KP (no band-dimensional G-stable subspace of R_P) [P given the computations in §5]
**Statement.** Let a = 1 and let RX's P be as above.
- **(i) m ∈ {24, 28, 32, 36, 40, 44}.** The intersection of the subset-sum sets of the sampled degree-2 Frobenius elements is **{0, n}**. Hence, by GS, G acts irreducibly on R_P/W [v2: FIX-1].
  - [v2: FIX-1] v1 stated instead that "some degree-2 Frobenius has an irreducible characteristic polynomial". **None of the owner's 36 logged samples for these m is irreducible.** The script's message "irreducible Frobenius found" fires when the intersection reaches {0, n}; it is a mislabel. The script is left unchanged, to keep its hash.
  - The literal v1 statement is nevertheless true, by [C, referee F3/F1]: genuinely irreducible degree-2 Frobenius elements exist for every m listed. For example, owner-sequence sample #8 for m = 24, and referee samples for m = 44.
  - Hence every G-stable S ⊂ R_P satisfies S ⊂ W, or S + W = R_P, in which case dim S ≥ m/2 − 2.
- **(ii) m ∈ {26, 30, 34, 38, 42}.** Over 40 degree-2 Frobenius elements, the intersection of the subset-sum sets is **{0, 1, n−1, n}**.
  - Hence every G-stable S ⊂ R_P has dim((S+W)/W) ∈ {0, 1, n−1, n}. So dim S ≤ 4, or dim S ≥ n−1 = m/2 − 3.
- **(iii) Conclusion.** In both cases R_P has **no** G-stable subspace S with 5 ≤ dim S ≤ m/2 − 4. In particular there is none of band dimension 6 ≤ dim S ≤ (m−6)/3, since (m−6)/3 ≤ m/2 − 4 for m ≥ 12.
  - So **RX's polynomial yields no band-dimensional counterexample** for these m, whether or not the subspace contains W.
  - This answers the SH v2 §5(c) / FIX-2 question negatively in the tested range.

*Proof.*
1. **(i), (ii).** Combine Lemma GS with the computed characteristic polynomials (§5).
2. **Reduction to ker P̃.** For any G-stable S, S ∩ W and (S+W)/W ⊂ R_P/W ≅ ker P̃ are G-stable. Also dim S = dim(S+W) − 3 + dim(S ∩ W).
3. **(i).** If (S+W)/W = 0, then S ⊂ W. Otherwise S + W = R_P, so dim S ≥ m/2 + 1 − 3.
4. **(ii).** If dim((S+W)/W) ≤ 1, then dim S ≤ 4. Otherwise dim S ≥ dim((S+W)/W) ≥ n − 1.
5. **(iii).** m/2 − 3 > (m−6)/3 ⟺ m > 6. ∎

## 4. Proposition KL (no G-stable line in ker P̃ for m = 10, 14, 18) [P given the exact search]
**Statement.** For m ∈ {10, 14, 18} (m/2 odd), P̃ has **no** nonzero root in L = F_q(X). So ker P̃ has no G-stable line. Combined with the Frobenius patterns ({0, 1, 2, 3}, {0, 1, 4, 5}, {0, 1, 6, 7}), the only possible proper G-stable subspaces of ker P̃ are hyperplanes.

In particular there is no G-stable W″ ⊃ W in R_P of the intermediate dimension 4 = 2a₂ + 2. For m = 18 this dimension lies within (m−6)/3 = 4.

*Proof.*
1. **Lines are rational roots.** A G-stable F₂-line is pointwise fixed (GL₁(F₂) = 1), so it is spanned by a root lying in L.
2. **Exact search** (`kprat.py`).
   - P̃ is computed exactly over F₂[X].
   - At every irreducible π dividing a coefficient, and at ∞, the Newton polygon of Σ p̃_i T^{2^i} limits the root valuations. No finite pole is possible, and the degree is ≤ 12.
   - [v2: m5] kprat's output lists entries "(π, 0)". These are the places whose Newton polygons have positive slopes, all **fractional** (at most 1/2, 1/8, 1/32 for m = 10, 14, 18). So no integer pole order exists, and the floor is 0. At ∞ there is a single segment of slope 12, so deg t = 12 exactly [C, referee F6].
   - The F₂-kernel of u ↦ Σ p̃_i u^{2^i} on F_q[X]_{≤12} is **0**.
3. **Positive control.** The same search on P returns exactly W (F₂-dimension 3), in agreement with SH v2 RK. ∎

**[C/OPEN].** For m ≥ 26 with m/2 odd, the line case was not searched (kprat is too slow there). Whether the (T+1) factor reflects a G-stable hyperplane is **[H]**.

**[H].** A natural candidate is a G-equivariant functional R_P → F₂, giving a G-stable hyperplane of dimension m/2 containing W. This is outside the band in any case.

## 5. Computations [C]
All are own code (`nice -n 19 python3 -I`; one process at a time). GF(2^{2m}) uses irreducible moduli from `galois.irreducible_poly`, which is used only for the modulus; the arithmetic is own carry-less code. Characteristic polynomials are computed by Berkowitz and factored over F₂ with sympy.

- **`kpcheck.py <m> 2 40 <seed=m>`.** Random degree-2 places (α ∈ F_{q²}∖F_q), with sanity checks:
  - every characteristic polynomial lies in F₂[T];
  - W(α) ⊂ ker P_α, by exact right division with zero remainder;
  - Frobenius on ker P has the factor (T+1)³ (W is G-fixed).
  - 356 Frobenius elements in all, with no warnings.
- **Results.** In the table, a run stops early once the **intersection of the subset-sum sets equals {0, n}** (not when an irreducible polynomial appears; the script's printed message is a mislabel) [v2: FIX-1]. "Possible stable dims" is that intersection.

  | m | n | samples | possible stable dims | intersection {0, n} reached (early stop) [v2: FIX-1] |
  |---|---|---|---|---|
  | 10 | 3 | 40 | {0,1,2,3} | — |
  | 14 | 5 | 40 | {0,1,4,5} | — |
  | 18 | 7 | 40 | {0,1,6,7} | — |
  | 24 | 10 | 2 | {0,10} | yes |
  | 26 | 11 | 40 | {0,1,10,11} | — |
  | 28 | 12 | 7 | {0,12} | yes |
  | 30 | 13 | 40 | {0,1,12,13} | — |
  | 32 | 14 | 2 | {0,14} | yes |
  | 34 | 15 | 40 | {0,1,14,15} | — |
  | 36 | 16 | 8 | {0,16} | yes |
  | 38 | 17 | 40 | {0,1,16,17} | — |
  | 40 | 18 | 8 | {0,18} | yes |
  | 42 | 19 | 40 | {0,1,18,19} | — |
  | 44 | 20 | 9 | {0,20} | yes |

- **`kprat.py <m>` and `kprat.py <m> control`.** For m = 10, 14, 18: rational roots of P̃ have dimension 0; the control on P returns 3.
- [v2: FIX-1, m4] **Referee verification (audit §5).**
  - All 356 owner samples were recomputed; the factor lists agree.
  - Lemma FR was checked against actual roots: 78/78 nullities, 39/39 characteristic polynomials.
  - Fresh samples reproduce every intersection.
  - For information: m = 12, 16, 20 also give {0, n}, and m = 22 gives {0, 1, 8, 9}.

## 6. Consequences
- **(a) [P + C] The RX construction is exhausted** for a = 1 in the tested range.
  - RK: there is no rational extension (all m).
  - KP: there is no G-stable band-dimensional subspace of R_P at all (m = 24, …, 44).
  - Hence, for a = 1 and m = 24, …, 44, any band-dimensional non-implication must come from a relation (C, D) **not proportional to RX's**: any W with RX's relation lies in R_P.
  - [v2: FIX-2] v1's added "and a non-rational W" is **withdrawn**. Rational band-dimensional W with another (C, D) are not excluded by RK or KP; RX v2 §3 excludes monomial W only. This case is **[OPEN]**. Cases with a ≥ 2 are untouched.
- **(b) [H]** The pattern (intersection {0, n}, i.e. G irreducible on R_P/W, for m ≡ 0 mod 4; intersection {0, 1, n−1, n} for m ≡ 2 mod 4) suggests a general theorem [v2: FIX-1]. Individual Frobenius characteristic polynomials are mostly reducible. That theorem is **[OPEN]**.
- **(c) Unchanged.** The even-band question (generic PTH (ii), SH v2) remains **[OPEN]**. GO/GX/KB remain [COND] on GLS₀/GLS₁.
- **(d) Method [P].** Lemmas FR and GS give a general computational test, usable on B1 once Codex supplies its relation: compute Frobenius characteristic polynomials of P̃ at degree-≥2 places. Irreducibility of R_P/W, or of R_P, excludes G-stable sub-radicals of given dimension. With them it excludes the G-stable subspaces A(F_Q) and W ∩ A(F_Q) = A(U′) (SH(b)) attached to a minimal twist A, whenever their dimensions fall in the excluded range. A general A(U) need not be G-stable. For RX's P with R_P/W irreducible, a G-stable A(F_Q) (dim m/2) is **not** excluded by irreducibility alone [v2: m3].

## 7. Questions for Codex (for a later packet, only after audit)
- **(a)** Can B1's generic relation (C, D) be supplied explicitly for a small band cell, so that the Frobenius test of §6(d) can be run on the arc relation?

## 8. Owner self-check; points for the audit
- **FR:** the duality M̄ ≅ Hom_{F₂}(V, k̄) and τ^N ↔ precomposition with Fr. Transposes share characteristic polynomials.
- **FR, ordering:** in the product A·σ(A)·…, the ordering follows from τ(τ(v)) = Aσ(Aσ(v)) = Aσ(A)σ²(v).
- **GS:** the good-reduction hypotheses (d₁(α) ≠ 0, c₀(α) ≠ 0, dim W(α) = 3) are checked in the script for every sample.
- **KP(iii):** the arithmetic (m−6)/3 ≤ m/2 − 4 ⟺ m ≥ 12, and m/2 − 3 > (m−6)/3.
- **KL:** Newton-polygon pole bounds. The integral part of the largest possible pole order is used, which over-approximates. Root valuations at ∞ give the degree bound.
- **Galois:** the `galois` package is used only to obtain irreducible moduli. All field arithmetic is own code.

## 9. Scripts
In `claude_archive/scripts/`:
- `kpcheck.py` — bb1eb2a4c77fae982df8f832d20ea585ce9e8ef4976796858109f509c96a9a60;
- `kpcheck.log` — cb00f4b0991a4c8eb77f90bdfc0752bf82a3e218bb0ac84600c9be5271138d96;
- `kprat.py` — bde2936239b0fa5274a2969b1aaad92c6c56991877e6ab0dc81db53a653c4e5b;
- `kprat.log` — cc1344dfb38cec31fa146670bb381bf458d31f2257a57cb22aac92bff7627ee9.

## 10. Change log v1 → v2 [v2]
| Item | Where | Change |
|---|---|---|
| FIX-1 | Title, GS, KP(i), §5 text/table/referee summary, §6(b) | Evidence restated: the intersection of subset sums is {0, n} (owner samples contain no irreducible polynomial; the script message is mislabelled). The literal v1 statement is true by [C, referee F3/F1]. The conclusion is unchanged. |
| FIX-2 | §6(a) | "and a non-rational W" withdrawn. Rational W with another (C, D) are [OPEN]; scope a = 1, m = 24..44. (The same correction applies to HANDBACK-20261007T2330Z §2 item 4; it is made in the new HANDBACK.) |
| m1 | FR proof | k̄ ⊗_k M identification made explicit; τ^N ⊗ 1 versus left multiplication on M̄. |
| m2 | GS | The arithmetic Galois group is meant; geometric-only stability is not addressed. |
| m3 | §6(d) | "SH-type twisted half-fields" restricted to the G-stable A(F_Q) and A(U′). A(F_Q) is not excluded by irreducibility. |
| m4 | Title, §5 | Ranges m = 24..44 stated. "Exactly" replaced by "the m searched". Referee information added. |
| m5 | KL proof | The "(π, 0)" output is explained (fractional slopes). |
| m6 | §2 Remark | Qualifier α ∉ Z = F_Q added, with referee F5. |

No proof was changed. Scripts are unchanged (hashes as in §9). The referee's checks are in `audit_KP_checks/`.
