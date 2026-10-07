# GLS₀ is a property of the radical alone: the generic twist exists (with degree < ρ − 2a₂) iff W contains a twisted half-field A(U) with dim U > a₂ + deg A (Theorem SH). So the even-band GLS₁ question (when ρ > 3a₂), and more generally GLS₀ with a twist of degree < ρ − 2a₂, is exactly "PTH (ii) holds generically" [v2: m1]. Minimal relations are unique when a₂ = a(W) and ρ ≥ 2a₂+1 (Claim U, referee) [v2: FIX-1]. For a = 1, the RX polynomial has G-fixed (rational) kernel exactly W, for every m (Proposition RK) [v2: FIX-2]. (Owner note **v2**, cloud session, 7 Oct 2026, 23:01Z; v1 22:40Z.)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac; no mailbox access).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- v1 (sha256 6fe44b3aa532917279ff06cf69568075fbb97986e36ca3a7ce13c15972668e2e) was independently audited in AUDIT-SH-SUBHALFFIELD-CRITERION-20261007.md (sha256 18f00635…96b68c). Verdict: **PASS-with-fixes** (2 substantive FIX-1, FIX-2; 9 minor m1–m9). The RK example was VERIFIED.
- **This v2** applies all of them. Each change is marked [v2: FIX-n] or [v2: m-n], and the change log is §8.
- FIX-1 adopts the referee's Claim U with credit, as [P, referee; adopted].
- **STATUS: v2 — PENDING DIFF-CHECK.** Packet EM is prepared in the outbox, marked PENDING DIFF-CHECK (NOT READY).

**Scope.** HANDBACK-20261007T2235Z §2 lists the targets:
- item 1: device steps, impossible here;
- item 2: questions to Codex, which need the mailbox;
- item 3: the even-band GLS₀ question. **This note takes item 3.**

**What is not claimed.** The note does **not** settle the even-band question. It reduces it to a clean structural statement and closes one construction route completely. GLS₀ for the arc family, G1 and the linear-gap conjecture are not claimed.

## 0. Setting
Notation is as in GLO v2 (9b1d48be…; review chain complete) and RX v2 (fcecc2c7…; review chain complete).
- L = F_q(X), Q = 2^{m/2}, G = Gal(L^sep/L).
- C, D ∈ L{τ} of degree a₂, P = C + Dτ^{m/2}, R_P = ker P.
- Λ(A) := C·A + D·φ(A), where φ is the Q-power on coefficients.
- GLS₀ means Λ has a nonzero solution in L^sep{τ}.
- (N0) means c₀d₀c_{a₂}d_{a₂} ≠ 0.
- W ⊂ R_P is an F₂-subspace of dimension ρ, and "twisted half-field" means A(U) with A ∈ L̄{τ} and U ⊂ F_Q an F₂-subspace.

**Even band.** EBR (a* = ρ − ⌈g/2⌉, g ≥ ρ+3) gives a₂ ≤ a* ≤ ρ/2 − 2, i.e. **ρ ≥ 2a₂ + 4** (RX v2 §3, m2).

## 1. Theorem SH (sub-half-field criterion) [P]
Assume (N0).
- **(a) Sufficiency.** Suppose A ∈ L̄{τ}∖0 and U ⊂ F_Q satisfy A(U) ⊂ R_P (for instance A(U) ⊂ W) and **dim U > a₂ + deg A**. Then Λ(A) = 0. So GLS₀ holds, with A ∈ L^sep{τ} by GLO FS(b).
- **(b) Necessity.** If GLS₀ holds and A is a minimal twist, then U′ := A^{−1}(W) ∩ F_Q has dim U′ ≥ ρ − a₂, and A(U′) = W ∩ A(F_Q) ⊂ W.
- **(c) Equivalence.** For every d with **d < ρ − 2a₂**, the following are equivalent:
  - GLS₀ holds with a minimal twist of degree ≤ d;
  - W contains a twisted half-field A(U) with deg A ≤ d and dim U > a₂ + deg A.

*Proof.*
1. **(a)** P·A = CA + Dτ^{m/2}A = CA + Dφ(A)τ^{m/2}. For u ∈ U ⊂ F_Q, τ^{m/2}(u) = u^Q = u, so 0 = P(A(u)) = Λ(A)(u).
   - Thus the linearised polynomial Λ(A), of τ-degree ≤ a₂ + deg A, vanishes on U.
   - A nonzero linearised polynomial of τ-degree n has an F₂-kernel of dimension ≤ n. Hence Λ(A) = 0.
   - No injectivity of A is needed.
2. **(b)** By MI (PTH §2), A(F_Q) ⊂ R_P has dimension m/2. Also dim R_P ≤ m/2 + a₂, so dim(W ∩ A(F_Q)) ≥ ρ − a₂. A is injective on F_Q, so W ∩ A(F_Q) = A(U′).
3. **(c), forward.** Let the minimal twist have degree d′ ≤ d. Then (b) gives dim U′ ≥ ρ − a₂ > a₂ + d ≥ a₂ + d′.
4. **(c), backward.** (a) gives Λ(A) = 0, so a minimal twist has degree ≤ deg A ≤ d. ∎

**Corollary SH1 (intrinsic form) [P].**
- GLS₀ (with a twist of degree < ρ − 2a₂) depends only on W and a₂, by SH(c).
- [v2: FIX-1] **On uniqueness of the relation.** v1's parenthetical ("under (N0) it is determined by W up to scalar") is **false** when a₂ > a(W).
  - Example [P + C, referee]: for W = λF_Q with λ ∉ F_Q, the relations of degree ≤ 1 form a 2-dimensional space containing two independent (N0) relations. Both admit the twist λ, consistently with SH3.
  - The correct statement follows. If a₂ = a(W) (the generic defect, GLO v2 §0) and ρ ≥ 2a₂+1, then the relations of degree ≤ a₂ form one line (**Claim U** below). This is automatic in the even band.
  - If a₂ > a(W), the relation need not be unique, but SH(c) shows that GLS₀ in degree < ρ−2a₂ is the same for every (N0) relation of degree a₂.
- In the even band (ρ ≥ 2a₂+4), SH(c) characterises:
  - all twists of degree ≤ 3;
  - GLS₁ (degree ≤ a₂), whenever ρ > 3a₂.

**Claim U (uniqueness of minimal relations) [P, referee; adopted]** [v2: FIX-1].
*Statement.* Let K be a field of characteristic 2 (for example L̄). Let W ⊂ K be an F₂-subspace with a := a(W), the minimal degree of a nonzero relation (C, D), C(w) = D(w^Q). If dim W ≥ 2a+1, then the relations of degree ≤ a form one K-line.

*Proof (referee).*
1. **Top map.** The K-linear map (C, D) ↦ (c_a, d_a) on Rel_{≤a} is injective, since its kernel is Rel_{≤a−1} = 0. So dim Rel_{≤a} ≤ 2.
2. **A normalised pair.** Suppose dim Rel_{≤a} = 2. Then there are relations (C₁, D₁) with (c_a, d_a) = (1, 0) and (C₂, D₂) with (c_a, d_a) = (0, 1).
   - D₁ ≠ 0; otherwise W ⊂ ker C₁ would have dimension ≤ a. Put b := deg D₁ ≤ a−1.
   - For a = 0 the relation (1, 0) would force W = 0, so a ≥ 1.
3. **Common left multiple.** A K-linear count (a+b+2 unknowns, a+b+1 equations) gives H₁ (deg ≤ a) and H₂ (deg ≤ b), not both zero, with H₁D₁ = H₂D₂.
   - Both are then nonzero, since K{τ} is a domain.
   - Comparing degrees, deg H₁ = deg H₂ + (a−b).
4. **An annihilator of low degree.** Put E := H₁C₁ + H₂C₂. Then E(w) = (H₁D₁ + H₂D₂)(w^Q) = 0 on W.
   - deg(H₂C₂) ≤ deg H₂ + a − 1 < deg H₁ + a = deg(H₁C₁).
   - So E ≠ 0 and deg E = deg H₁ + a ≤ 2a.
5. **Contradiction.** Hence dim W ≤ 2a. ∎

*Sharpness.* A random W of dimension 2a has a 2-dimensional Rel_{≤a} ([C, referee] T3). Owner check of the proof: step 3's equations are K-linear in the coefficients of H_i, and in step 4 char 2 gives H₁D₁ + H₂D₂ = 0.

[v2: m9] **Consequence.** The hypothesis "unique (N0) relation line" in GLO v2 (FIX-1 [OPEN]) and RX v2 §3 is **automatic** for G-stable W with a₂ = a(W) and dim W ≥ 2a₂+1. Only (N0) itself remains a hypothesis.

**Corollary SH2 (the pointwise analogue) [P, with PTH [A, audited]].** PTH (ii) says pointwise that a radical V ⊂ F_q of defect a contains A_α(U_α) with dim U_α ≥ ρ − e ≥ ρ − a and deg A_α ≤ a. The degree bound holds for every e, since A_α ∈ S_C has degree ≤ a. When e = 0, V = A_α(U_α) with deg A_α = a (PTH (iii)) [v2: m2].
- When ρ > 3a, this gives dim U_α > a + deg A_α. So the pointwise twist satisfies SH(a) pointwise.
- **Hence the even-band GLS₁ question (ρ > 3a₂) is exactly whether PTH (ii) holds generically:** does the generic radical W contain a twisted half-field A(U) with deg A ≤ a₂ and dim U > 2a₂?
- [v2: m2] With ρ > 3a₂, "∃A(U) ⊂ W with deg A ≤ a₂ and dim U > 2a₂" ⟺ "∃A(U) ⊂ W with deg A ≤ a₂ and dim U > a₂ + deg A". The direction ⇒ is trivial. For ⇐, apply SH(a) to get a twist, then SH(b) to the minimal twist A′ (deg A′ ≤ deg A ≤ a₂). This gives dim U′ ≥ ρ − a₂ > 2a₂.

**Corollary SH3 (constant twists) [P].** If W contains λU with λ ∈ L̄^* and dim U > a₂, then GLS₀ holds with the twist A = λ, of degree 0. In particular this holds if W contains a sub-radical of the global (H) shape ηU **with dim U > a₂** [v2: m3].

**Consistency with RX [P].** RX's W = F₂[X]_{≤2a} has no twist (RX v2), so by SH(a) it contains no A(U) with dim U > a + deg A. For instance, no two-dimensional λU with λ ∈ L̄^* exists inside W when a = 1.

## 2. Proposition RK (the RX polynomial has rational kernel exactly W; a = 1, all even m ≥ 4) [P]
Let a = 1, W = F₂[X]_{≤2}, E = (1, 2, Q, 2Q), and let (c₀, c₁, d₀, d₁) = (M₁, M₂, M₃, M₄) be the cofactors (RX v2 §2). Then **ker P ∩ L = W**.

This upgrades RX v2 §3's [C] statement, for a = 1, to [P] for all m. In particular RX cannot be extended by a **rational (G-fixed)** root inside the same P.

[v2: FIX-2] **What RK does not exclude.** RK does not exclude G-stable non-rational extensions W ⊂ W″ ⊂ R_P.
- [P, referee] Let M_W be the subspace polynomial of W. Then P = P̃·M_W, and M_W maps R_P G-equivariantly onto ker P̃ with kernel W. So the G-stable W″ ⊃ W correspond to the G-stable subspaces of ker P̃.
- Every such W″ inherits RX's unique relation of degree ≤ 1 and its GLS₀ failure (RX v2 (i), (iv)).
- For m/2 odd, R_P itself (dim m/2+1, even, G-stable) contains W. This lies outside the band.
- Whether band-dimensional G-stable W″ exist is [OPEN] (§3).
- [C, referee] P̃ has no polynomial roots for m = 8..16, and the search is complete for polynomial roots.

*Proof.*
1. **Vandermonde form.** The rows of the matrix are (z_l^k)_l, with z_l = X^{e_l} and k = 0, 1, 2. So M_l = Π_{pairs {e,e′} ∌ e_l} (X^e + X^{e′}) (Vandermonde cofactor; characteristic 2). [C] slcheck V confirms this exactly for m ∈ {8, 10, 16, 18, 20}.
   - Since X^e + X^{e′} = X^e(1 + X^{e′−e}), the factors are as follows:
     - (1,2): X(1+X);
     - (1,Q): X(1+X^{Q−1});
     - (1,2Q): X(1+X^{2Q−1});
     - (2,Q): X²(1+X^{Q/2−1})²;
     - (2,2Q): X²(1+X^{Q−1})²;
     - (Q,2Q): X^Q(1+X)^Q.
   - Here Q−1, 2Q−1 and Q/2−1 are odd, so the bracketed polynomials are separable.
   - Hence:
     - deg (M₁, …, M₄) = (5Q, 5Q, 4Q+2, 2Q+2);
     - v_X = v_{X+1} = (Q+4, Q+2, 4, 4);
     - for an irreducible π ∤ X(X+1), v_π(M₄) ≤ 3 (in fact ≤ 2, since gcd(1+X^{Q−1}, 1+X^{Q/2−1}) = 1+X [v2: m7]);
     - all leading coefficients are 1.
2. **No finite poles.** Suppose w ∈ R_P ∩ L and v_π(w) = −k < 0 at a finite place π. The four terms M_l w^{e_l} have valuations μ_l − e_l k, where μ_l = v_π(M_l).
   - The d₁ term has value μ₄ − 2Qk.
   - At π = X or X+1 this is 4 − 2Qk, which is below d₀'s value 4 − Qk and below the c-terms' values ≥ Q+2−2k.
   - At other π it is ≤ 3 − 2Qk, which is below −Qk ≤ d₀'s value and below the c-terms' values ≥ −2k.
   - So the minimum is attained once, which is impossible. Hence w is a polynomial.
3. **Degree ≤ 2.** For deg w = k, the term degrees are 5Q+k, 5Q+2k, 4Q+2+Qk and 2Q+2+2Qk. For k ≥ 3 the last one is strictly largest, since Q ≥ 4. So deg w ≤ 2.
4. **The coefficients lie in F₂.** Write w = β₀ + β₁X + β₂X² with β_i ∈ F_q.
   - **X^{6Q+2}.** Only the d₀ and d₁ terms reach this degree. Its coefficient is β₂^Q + β₂^{2Q} = 0, so β₂^Q ∈ F₂, hence **β₂ ∈ F₂**. Subtract β₂X² ∈ W.
   - **X^{5Q+2}**, once deg w ≤ 1. Only c₁·w² and d₀·w^Q reach this degree. The coefficient gives β₁² = β₁^Q, i.e. β₁ ∈ F_{2^{gcd(m/2−1, m)}} ⊂ F₄.
     - If β₁ ∈ F₂, subtract β₁X.
     - If β₁ ∈ F₄∖F₂, then gcd = 2, so m/2 is odd and β^Q = β², β^{2Q} = β on F₄. The cofactor identity at k = 1 gives M₁X + M₄X^{2Q} = M₂X² + M₃X^Q =: A₁, of degree 5Q+1. Then P(β₁X) = (β₁ + β₁²)A₁ = A₁. But P(β₀) has degree ≤ 5Q < 5Q+1, so P(w) ≠ 0. Contradiction.
   - **X^{5Q}**, for constants. M₁ and M₂ have degree 5Q with leading coefficient 1, and deg M₃, M₄ < 5Q. The coefficient gives β₀ + β₀² = 0, so **β₀ ∈ F₂**. ∎

**[C] slcheck.py R.** The F₂-dimension of ker P on F_q[X]_{≤3} (F_q coefficients) is **3** for m = 16, 18 and 20. m = 18 is the odd-m/2 (F₄) case.

## 3. The even band after SH: status and the remaining gap
- **[OPEN] Generic PTH (ii).** In the even band, W (G-stable, dim ρ ≥ 2a₂+4, unique (N0) relation) satisfies pointwise PTH (ii) at every nonfocus. This premise is **[COND (B1b)] / [A]**: it uses (B1b) to pass from V_α to W(α), and holds with a(V_α) ≤ a* [v2: m8]. The question is whether it contains a generic twisted half-field A(U) with dim U > a₂ + deg A (SH).
- **Two constructions are now closed.**
  - **[A]** (RX v2 §3, reviewed) Monomial or F_q-scaled-monomial W cannot have ρ ≥ 2a₂+2 [v2: m4].
  - **[P]** The RX polynomial has no further **rational** roots (RK, a = 1).
  - Therefore any band-dimensional counterexample must be non-monomial. For a = 1 it cannot be a G-fixed extension of RX's W inside the same P.
  - [v2: FIX-2] **[OPEN]** A G-stable non-rational W″ ⊃ W inside RX's P would be a band counterexample with the **same** P, if one exists with 6 ≤ dim W″ ≤ (m−6)/3 (possible only for m ≥ 24). Equivalently: does ker P̃ have G-stable subspaces of dimension 3..(m−15)/3?
- **[H] Why a lifting proof is hard.** Pointwise, the twisted half-field A_α(U_α) ⊂ W(α) singles out a subspace W″_α ⊂ W of dimension ≥ ρ − a₂.
  - W has finitely many subspaces, so by pigeonhole a fixed W″ is a pointwise twisted half-field at ≥ v′/#Gr(ρ − a₂, W) nonfoci.
  - Lifting "W″(α) = A_α(U_α)" to a generic A meets GLO's Q-power obstruction again: A_α depends on the conjugates C̄_α.
  - A lift would follow if the heights of W″ were < Q/c (TH-type counting). The arc's B1 roots have height ≤ u = R/4 ((B1a⁺)), but the twist coefficients are not controlled by that.
- **[H] Expectation.** GLO's referee parameter count (right factors of dimension ≈ 2a+1 versus twisted half-fields of dimension ≈ a+1) suggests that band-dimensional W without a generic twisted half-field exist abstractly. If so, any proof of GLS₀ must use arc structure through SH, i.e. produce A(U) ⊂ W directly.

## 4. Consequences
- **(a) [P] A cleaner target for GLS₀.** It suffices to find, inside the generic radical W, a twisted half-field A(U) with dim U > a₂ + deg A (SH(a)). This needs no Lang equation and no Galois descent, and it is exactly the generic form of PTH (ii) (SH2). SH still uses a₂ and an (N0) relation (for L^sep-rationality via FS(b)), but by Claim U both are intrinsic to W in the band [v2: m5].
- **(b) [P] For GO.** GO's W′ = W ∩ A(F_Q) is precisely the SH sub-half-field. GO + (GT) + WG turn it into rational structure.
- **(c) Unchanged.** GO/GX/KB remain [COND] on GLS₀/GLS₁. The G1 reduction table is unchanged.

## 5. Questions for Codex (packet EM, PENDING DIFF-CHECK)
- **(a)** Do STT/MRL ("L = S² + tS") exhibit, inside B1's root space W, a twisted half-field A(U) with A ∈ L^sep{τ} and dim U > a₂ + deg A? By SH this is equivalent to GLS₀ for degree < ρ − 2a₂.
- **(b)** Is there a global (H)-type sub-radical ηU ⊂ W with dim U > a₂? If so, GLS₀ holds by SH3.
- **(c)** [v2: FIX-2] For the RX polynomial (a = 1): do G-stable subspaces of ker P̃ of dimension ≥ 3 exist for m ≥ 24? Any such subspace would give a band-dimensional non-implication with the same P.

## 6. Owner self-check; points for the audit
- **SH(a):** needs only A(U) ⊂ R_P and the kernel-dimension bound for linearised polynomials. It does not need A(U) ⊂ W, injectivity or (N0); (N0) is used only to quote FS(b) for L^sep-rationality.
- **SH(b):** MI and ML over L^sep (PTH, audited), and dim R_P ≤ m/2 + a₂.
- **RK step 1:** the Vandermonde factorisation is a standard [P] identity (3×3 Vandermonde cofactors, characteristic 2); the [C] check is confirmation [v2: m6]. The multiplicities follow because 1 + X^n with n odd is separable, and 1 + X^{2n} = (1 + X^n)².
- **RK step 2:** the competing-term inequalities need Q ≥ 4.
- **RK step 3:** 2Qk − 3Q + 2 − 2k > 0 for k ≥ 3 and Q ≥ 4.
- **RK step 4:** gcd(m/2 − 1, m) ∈ {1, 2}. The F₄ case uses Q ≡ 2 (mod 3) when m/2 is odd.
- **Not covered by RK:** a ≥ 2. RX v2 §3 (referee K1) covers the tested (a, m) only.
- **Process:** own scripts only, `nice -n 19 python3 -I`, about 0.8 s.

## 7. Scripts
`claude_archive/scripts/slcheck.py` (sha256 bc74772ca8374092597dad05693c6979028b4906d54e6dddac1a7f321dbb4934) and `slcheck.log` (a060fbd370f36828145c9bfe10a86e4b1b9daf7e11937b9bba18af6c025d260a).

## 8. Change log v1 → v2 [v2]
| Item | Where | Change |
|---|---|---|
| FIX-1 | Title, SH1, new Claim U, §4(a) | The false parenthetical "(C, D) determined by W" is replaced. Counterexample W = λF_Q noted. Claim U (minimal relations unique if a₂ = a(W), ρ ≥ 2a₂+1) adopted with its proof, credited [P, referee]. |
| FIX-2 | Title, RK header paragraph, §3, §5(c) | "Cannot be extended … same P" and "must use a different P" restricted to rational (G-fixed) extensions. G-stable non-rational W″ ⊃ W in R_P (via ker P̃) added as [OPEN] and as a Codex question. |
| m1 | Title | GLS₀ replaced by "GLS₁ (ρ > 3a₂) / twist degree < ρ−2a₂". |
| m2 | SH2 | Placement of the e = 0 qualifier fixed; equivalence of the two dim U conditions spelled out. |
| m3 | SH3 | "with dim U > a₂" added to the (H)-shape clause. |
| m4 | §3 | Monomial bullet relabelled [A] (citation of RX v2 §3). |
| m5 | §4(a) | "No (C, D)" softened; a₂ and (N0) are intrinsic via Claim U. |
| m6 | §6 | Vandermonde factorisation labelled [P], with [C] as confirmation. |
| m7 | RK step 1 | v_π(M₄) ≤ 2 noted. |
| m8 | §3 | [OPEN] premise labelled [COND (B1b)] / [A]. |
| m9 | after Claim U | The "unique relation" hypothesis of GLO FIX-1 / RX §3 is automatic under a₂ = a(W), dim W ≥ 2a₂+1. |

No proof of SH or RK was changed. Scripts are unchanged. The referee's checks are in `audit_SH_checks/`.
