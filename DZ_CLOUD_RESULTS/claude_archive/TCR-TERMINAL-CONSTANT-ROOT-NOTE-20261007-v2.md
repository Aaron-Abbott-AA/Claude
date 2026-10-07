# Even ρ, gap G5 and the orbit gap: the rational-branch descent ends in a CONSTANT root. Under a precise radical-frame identification (I216′) and Prop 216.3 this is impossible, so G5 is REPLACED by (I216′) + Prop 216.3, and G1′ weakens to "a rational part of dimension 2a*+4" (owner note v2, cloud session, 7 Oct 2026, 19:38Z; v1 19:20Z) [v2: FIX-2]

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- v1 (sha256 bfb63eda…c07a85) was independently audited in AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md (19:22–19:40Z). Verdict: **PASS-with-fixes** (3 substantive, 8 minor).
- This v2 applies FIX-1–FIX-3 and m1–m8. Each change is marked [v2: FIX-n] or [v2: m-n].
- **The v2 revision has NOT yet been re-checked by a referee. HOLD: do not send to Codex until it has been.**

## 0. Inputs
- **RBL v2.1** (audit PASS-with-fixes; revision check PASS). Used: TSZ, RB(i)–(iii), RD(a), (b), (d), the RD(c) invariant, and (B1a). RBL v2.1's (B1b) is the version **without** fixedness of the twist.
- **(B1b-fix)** [v2: FIX-3]: W(α) = V_α^{2^s} for every α ∈ N, **with s independent of α**.
  - This STRENGTHENS RBL v2.1's (B1b), so a confirmation of the weaker (B1b) does not suffice.
  - It is folded into (I216′) below, as part of the single identification φ.
- **RR [A]**, via the IDEAS §305 summary reading: "derivative rank ≤ 2 for rational root subspaces".
- **Prop 216.3 [A], status explicit** [v2: FIX-2]. The text "a nonzero b lies in at most n−1 radicals" is our OWN earlier owner statement, read from an *unlabelled tool bullet* in STATE §5 (Plan).
  - It is unaudited, with no review recorded. Its proof (memo §216) is not in the handoff.
  - **It depends on the coordinate frame** (see FIX-1 and (I216′)).
  - It must be re-read from the device archive, with its frame hypotheses, before TC is cited as anything more than [COND].
- **(I216′) — precise radical-frame identification** [v2: FIX-1; replaces v1's loose "(I216): Rad_μ = V_α"]. There exist:
  - an F₂-linear bijection φ of F_q, independent of α (for instance x ↦ λx^{2^{−s}}, which absorbs (B1b-fix));
  - an injective map α ↦ μ(α) from N into the nonfocus directions; and
  - normalised projections π_μ, all in ONE common affine frame of the arc R,

  such that:
  - **(pair uniqueness)** for every pair P ≠ P′ in R and every b ≠ 0, the equation π_μ(P − P′) = b has at most one solution among the nonfocus μ; and
  - **(identification)** φ(W(α)) = Rad_{π_{μ(α)}} for every α ∈ N, where Rad is the radical of the quadric projection.

  **Under (I216′), Prop 216.3 holds in that frame** by pair counting, with the constant n−1, or at worst n. Each μ with b ∈ Rad_μ uses n/2 pairs {P, P′}, and each pair serves at most one μ.

  **Why the frame matters (from the audit, [C] C3 of the referee).** Pair uniqueness can fail when a focus direction is the vertical comparison direction. Then a vertical pair contributes to every μ, and a translation-symmetric hyperfocused arc (R + (0,b) = R) puts one b in **every** finite nonfocus radical.
  - The referee's parabola–subspace arcs at q = 64 and 256 show exactly n−1 in the original frame, and "all radicals" after a focus-vertical change of frame.
  - Also, the reviewed same-arc structure (R3AF–AI, ρ = 3) shows that, in a common frame, the radicals of different projections are *different scalar multiples* λ_μH* of one space.
  - So any per-nonfocus normalisation of V_α would break the transfer. (I216′) therefore fixes the frame, the scale, the twist and injectivity together.
- **Notation.** n = q/2 − d is the arc size. v = |N| is the number of original nonfoci; v > q/2 > n − 1, and even v − n ≥ 2d + 1 > 0.

## 1. Lemma HF (the descent is a filtration of W; G2 in Hasse form) [P]
**Setting.** Let W ⊂ F_q[X] be an F₂-space, and put W_k := W ∩ F_q[X^{2^k}].

**Statement.**
- (i) W = W₀ ⊇ W₁ ⊇ ….
- (ii) The k-th square-root descendant of RBL §5 is exactly W^{(k)} = W_k^{1/2^k}.
- (iii) For w = s^{2^k} ∈ W_k we have D^{(2^k)}w = (s′)^{2^k}, and w ∈ W_{k+1} ⟺ s′ = 0.

Hence **RR for W^{(k)} ⟺ RR_k: dim W_k − dim W_{k+1} ≤ 2**, i.e. the F₂-rank of D^{(2^k)} on W_k is ≤ 2.

*Proof.*
1. **(ii).** By induction: s ∈ W^{(k)} ⟺ s² ∈ W^{(k−1)} ⟺ s^{2^k} ∈ W. The first equivalence uses that s² ∈ F_q[X²] automatically, and F_q is perfect.
2. **(iii).** Lucas gives C(i·2^k, 2^k) ≡ i (mod 2), so D^{(2^k)} applied to Σ s_i^{2^k}X^{i2^k} gives (s′)^{2^k}.
3. **The equivalence.** w ∈ F_q[X^{2^{k+1}}] ⟺ s ∈ F_q[X²] ⟺ s′ = 0. ∎

**[C]** [v2: m6]
- hassecheck.py (v1): 700 random s, 0 failures. The audit reproduced it byte for byte and extended it to m = 16.
- hassecheck_v2.py (new): seeds and command lines are logged, and half of the samples are forced into F_q[X²].
  - Runs: m = 8 (400, seed 1), m = 12 (300, seed 2), m = 16 (200, seed 3).
  - 519 of the cases had s′ = 0.
  - (H1) and (H2): 0 failures.
- The referee's independent C2 check over F_{2^24} also gave 0 failures.

**Consequence: a reformulation of G2 [P]** [v2: m2].
- G2 (RR for every square-root descendant) is *equivalent* to the rank conditions RR_k (k ≥ 0) for the Hasse derivatives D^{(2^k)} on W_k ⊂ W.
- This is a reformulation only. It does **not** make G2 easier. Whether the RR proof yields these Hasse-order ranks is open question §6(b).

## 2. Lemma CD (the descent keeps a large constant part) [P mod RR_k]
**Setting.**
- W ⊂ F_q[X] is a ρ′-dimensional F₂-space of polynomials of degree ≤ u.
- W has an ι-real bivariate relation of minimal degree a₂ ≤ ρ′/2 − 2, as in RB.
- RR_k holds for all k with 2^k ≤ u. (Constant levels are lossless, so no RR_k is needed beyond that.)

**Statement.** dim(W ∩ F_q) ≥ ρ′ − 2a₂ ≥ 4.

*Proof.* The induction runs over k. The hypothesis at level k is: dim W_k ≥ ρ′ − 2(a₂ − a(k)), and hence a(k) ≤ dim W_k/2 − 2. [v2: m5]
1. **Defects.** a(k), the bivariate defect of W_k, equals that of W^{(k)}: entrywise Frobenius is a field embedding of L₂ and preserves rank. a(k) is non-increasing in k. RB(ii)–(iii) apply to each level by pure algebra; TSZ is used only at level 0.
2. **A lossy level drops the defect.** Suppose W_{k+1} ≠ W_k. RD(b) applied to W^{(k)} (whose ker D_X is W_{k+1}^{1/2^k} by HF), together with RR_k, gives:
   - dim W_{k+1} ≥ dim W_k − 2, and
   - a(k+1) ≤ a(k) − 1.

   The induction hypothesis is preserved, because a lossy step lowers a(k) by ≥ 1 and dim W_k/2 by ≤ 1.
3. **No loss at defect 0 (redundant).** At a(k) = 0, step 2's count would force d₁ ≤ −1 on a lossy level, which is impossible. So a defect-0 level is lossless. [v2: m5]
   - Equivalently, RD(d) gives W^{(k)} = ηU₀, with dim U₀ = dim W_k ≥ 4 by the induction hypothesis. Then RR_k forces η′ = 0.
4. **Counting.** There are ≤ a₂ lossy levels, each losing ≤ 2 dimensions. So dim W_k ≥ ρ′ − 2a₂ for all k.
5. **Constants.** For 2^k > u, every s ∈ W^{(k)} has deg < 1, so W_k ⊂ F_q. ∎

**Remark.** The stalling family {u²+βu} (β ∉ F_Q) from the RBL audit is constant from the start. CD turns "stalling" into "constancy". [C] Referee C2-cd: 600 families, including adversarial lossy constructions; 0 failures of monotonicity, of the defect drop, or of the conclusion.

## 3. Theorem TC (the rational branch is excluded, with G5 REPLACED by (I216′) + Prop 216.3) [COND on G2 = {RR_k}, (B1a), (I216′) including (B1b-fix), Prop 216.3 [A]] [v2: FIX-1, FIX-2, FIX-3]
**Setting.**
- Even ρ, ρ+3 ≤ g ≤ 2ρ, and a(V_α) ≤ a* at every original nonfocus α ∈ N.
- **Branch hypothesis:** the roots of the WG family B1 (weight u = R/4) are all rational. (B1a) then turns rationality into W ⊂ F_q[X] with deg ≤ u. [v2: m4]

**Statement.** There is no such original arc.

*Proof.*
1. **Bivariate relation.** RB applies: a* ≤ ρ/2 − 2, 2u(2^{a*+1}−1)Q < v, and by (B1b-fix) W(α) = V_α^{2^s}, whose defect is a(V_α) ≤ a*. (The defect is invariant under Frobenius twists and scalings.) So a₂ ≤ a*.
2. **A constant root.** CD gives a nonzero constant c ∈ W ∩ F_q.
3. **c lies in every radical.** As a constant polynomial, c ∈ W(α) for every α ∈ N, with no exceptional α. By (I216′), φ(c) ∈ Rad_{π_{μ(α)}} for every α ∈ N. These are v DISTINCT nonfocus radicals, because α ↦ μ(α) is injective. [v2: m8]
4. **Contradiction.** In the frame of (I216′), Prop 216.3 (pair counting) allows φ(c) ≠ 0 to lie in at most n−1 (or n) of them. But v > n. ∎

**What changed relative to RBL v2.1** [v2: FIX-2].
- The terminal step no longer uses BWG, the (H) structure, or the condition G5.
- **G5 is not eliminated but TRADED.** It is replaced by three [A]-pending inputs:
  - (I216′), a precise frame/scale/twist identification;
  - (B1b-fix), a fixed twist s, folded into (I216′);
  - Prop 216.3, an unaudited earlier owner statement whose frame hypotheses must be re-checked.

## 4. Corollary RS (partial rationality suffices; G1′ weakened) [COND on G2, (B1a), (I216′), Prop 216.3; plus G4 for part (b) only] [v2: m1]
Let W^rat := W ∩ F_q[X] be the rational roots of the WG family.

**Statement.**
- **(a)** If dim W^rat ≥ 2a*+4, there is no original arc in the structured branch.
- **(b)** By WG with G4, every root outside W^rat has e_w ≥ (4/3)2^{ρ/2} − 1. So G1′ (all orbits small) implies
  - **G1″ [OPEN]: dim W^rat ≥ 2a*+4.**

  This is strictly weaker than G1′ when a* < ρ/2 − 2.

*Proof of (a).* Apply §3 to W′ := W^rat, with ρ′ = dim W^rat.
1. **Injective evaluation.** Evaluation is injective on W′, since it is injective on W.
2. **Pointwise defect.** a(W′(α)) ≤ a(V_α) ≤ a*: a relation restricted to a subspace is still a relation in the pair-module sense. [v2: m7]
3. **RB's condition.** a* ≤ ρ′/2 − 2 holds by hypothesis.
4. **Hasse ranks.** RR_k is required directly on W^rat_k := W^rat ∩ F_q[X^{2^k}]. It follows from RR_k on W whenever W is rational; in general it is part of G2 for the rational subspace. [v2: m3]
5. **Terminal step.** A constant c ∈ W′ ⊂ W gives the contradiction of §3, step 4. ∎

**Size of the requirement.** 2a*+4 = 2ρ − 2⌈g/2⌉ + 4. It is 6 at g = 2ρ−2, and ρ at g = ρ+3 and ρ+4. The referee checked this over 870 cells.

## 5. Updated reduction (replaces RBL v2.1 §6's bold line) [COND] [v2: m1, FIX-2]
  **G1 ⇐ G1″ + G2 + (B1a) + (I216′) [including (B1b-fix)] + [A] Prop 216.3.**
- **G4** is needed only for G1′ ⇒ G1″ via WG. RS(a) does not use it.
- G2 is in its Hasse form {RR_k}.
- **G1″ is OPEN.**
- G5 has been traded for (I216′) + Prop 216.3; it has not disappeared.

## 6. Questions for Codex (for a later packet, after the revision check)
- **(a)** B1: is (B1a) true? Is (B1b-fix) true, i.e. W(α) = V_α^{2^s} with s INDEPENDENT of α? [v2: FIX-3]
- **(b)** RR in Hasse form: does your RR proof give rank ≤ 2 for D^{(2^k)} on W ∩ F_q[X^{2^k}], for all k?
- **(c)** Frame and scale of V_α [v2: FIX-1]:
  - In which affine frame of R, and with which normalisation (scale, twist), are the original radicals V_α defined?
  - Is the comparison direction a nonfocus in that frame, so that the pair uniqueness of (I216′) holds?
  - Is the map α ↦ radical injective?

  This replaces v1's question "does radical mean V_α?".
- **(d)** G1″: does STT/B1 give a large rational subspace in the structured branch?

## 7. Owner self-check (updated)
- **CD steps 1–2.** These use only Frobenius invariance of the bivariate defect and RD(b). The audit confirmed both (audit points 1 and 4).
- **TC step 3.** Every α ∈ N, no exception, AND distinct α give distinct radicals (injectivity of α ↦ μ(α) in (I216′)). [v2: m8]
- **TC step 4.** Uses Prop 216.3 only in the (I216′) frame. In a focus-vertical frame it can fail (audit C3).
- **Counting.** v − n ≥ 2d + 1 > 0, so even the weaker constant n suffices.
- **Remaining points to settle locally.**
  - (1) Re-read memo §216: the exact frame hypotheses of Prop 216.3.
  - (2) Settle (I216′) and (B1b-fix) with Codex.

## 8. Change log v1 → v2
| FIX | Where | Change |
|---|---|---|
| FIX-1 | §0, §3 step 3–4, §6(c), §7 | (I216) replaced by the precise (I216′): fixed φ, injective α ↦ μ, common frame, pair uniqueness. The frame-dependence counterexample (audit C3) and the R3AF–AI scaling remark recorded. Question (c) redirected. |
| FIX-2 | Title, §0, §3 "What changed", §5 | "G5 removed / not extra" replaced by "G5 traded for (I216′) + Prop 216.3". Prop 216.3's status (unaudited, unlabelled Plan bullet, proof absent, frame-dependent) made explicit. |
| FIX-3 | §0, §3, §4, §5, §6(a) | Named (B1b-fix), with s independent of α, and folded into (I216′). |
| m1 | §4 header, §5 | G4 only for G1′ ⇒ G1″. |
| m2 | §1 Consequence | Called a reformulation; it does not make G2 easier. |
| m3 | §4 step 4 | RR_k defined directly on W^rat_k. |
| m4 | §3 Setting | Rationality (branch) separated from (B1a) (polynomiality, degree ≤ u). |
| m5 | §2 steps 2–3 | Induction made explicit; step 3 marked redundant. |
| m6 | §1 [C] | hassecheck_v2.py with logged seeds and commands, and forced s′ = 0 samples. |
| m7 | §4 step 2 | Simplified justification. |
| m8 | §3 step 3, §7 | Injectivity of α ↦ radical made explicit. |

Scripts:
- `scripts/hassecheck.py` and `.log` (v1).
- `scripts/hassecheck_v2.py` and `.log` (v2; own code, reads no files).
- The referee's checks are in `audit_TCR_checks/`.
