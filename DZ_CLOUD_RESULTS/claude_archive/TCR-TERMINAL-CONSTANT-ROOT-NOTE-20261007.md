# Even ρ, gap G5 and the orbit gap: the rational-branch descent ends in a CONSTANT root, which Prop 216.3 forbids. So G5 is not an extra input, and G1′ weakens to "a (2a*+4)-dimensional rational part" (owner note, cloud session, 7 Oct 2026, 19:20Z)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS: NOT YET AUDITED.** An independent audit is to be arranged by the coordinator. This note must not be sent to Codex before that audit passes.

## 0. Inputs
- **RBL v2.1** (RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md: audit PASS-with-fixes, revision check PASS). Used:
  - TSZ;
  - RB(i)–(iii);
  - RD(a), (b) and (d);
  - the invariant in RD(c);
  - the B1 identification conditions (B1a) and (B1b), as defined in RBL v2.1 §4.
  - For this note, (B1b) is read with a **fixed** twist exponent s: W(α) = V_α^{2^s} for every α ∈ N.
- **RR [A]**, via the IDEAS §305 summary reading: "derivative rank ≤ 2 for rational root subspaces".
- **Prop 216.3 [A]**, statement only, via STATE §5: "a nonzero b lies in at most n−1 radicals". Its proof is in the full IDEAS memo (§216), which is not in the handoff.
  - **(I216)** identifies its "radicals" Rad_μ (μ a nonfocus) with the original radicals V_α of the near-diagonal notes. This identification is [A]-pending.
- **Notation.**
  - n = q/2 − d is the arc size, and v = |N| is the number of original nonfoci.
  - v > Q²/2 = q/2 > n − 1. Only the inequality v > n − 1 is used.

## 1. Lemma HF (the descent is a filtration of W; G2 in Hasse form) [P]
**Setting.** Let W ⊂ F_q[X] be an F₂-space. Put W_k := W ∩ F_q[X^{2^k}] for k ≥ 0. Then:
- (i) W = W₀ ⊇ W₁ ⊇ W₂ ⊇ …;
- (ii) the k-th square-root descendant of RBL §5 is exactly W^{(k)} = W_k^{1/2^k};
- (iii) for w = s^{2^k} ∈ W_k, the Hasse derivative satisfies D^{(2^k)}w = (s′)^{2^k}, and w ∈ W_{k+1} ⟺ s′ = 0.

Hence **RR for the descendant W^{(k)} is equivalent to RR_k:**
  dim W_k − dim W_{k+1} ≤ 2, i.e. the F₂-rank of D^{(2^k)} on W_k is ≤ 2.

*Proof.*
1. **(ii), by induction.** W^{(k)} = √(W^{(k−1)} ∩ F_q[X²]). For s ∈ F_q[X], s ∈ W^{(k)} ⟺ s² ∈ W^{(k−1)} ⟺ s^{2^k} ∈ W. Here F_q is perfect, so square roots of polynomials in F_q[X²] are polynomials, and s^{2^k} ∈ F_q[X^{2^k}] automatically.
2. **(iii)** This is the standard char-2 identity D^{(2n)}(f²) = (D^{(n)}f)², iterated.
3. **The equivalence.** w ∈ F_q[X^{2^{k+1}}] ⟺ s ∈ F_q[X²] ⟺ s′ = 0. ∎

**[C]** hassecheck.py (own code, `python3 -I`) checked (iii) and the equivalence for 700 random s over F_{2^8} and F_{2^12}, with k ≤ 3: 0 failures.

**Consequence: G2 restated on the actual family [P].** G2 (RR for every square-root descendant) is exactly the family of rank conditions RR_k (k ≥ 0) for the Hasse derivatives D^{(2^k)} on W_k ⊂ W. These are statements about the actual root space W itself, not about auxiliary families. RR₀ is RR.

## 2. Lemma CD (the descent keeps a large constant part) [P mod RR_k]
**Setting.**
- W ⊂ F_q[X] is a ρ′-dimensional F₂-space of polynomials of degree ≤ u.
- W has an ι-real bivariate relation of minimal degree a₂ ≤ ρ′/2 − 2, as given by RB.
- RR_k holds for all k with 2^k ≤ u.

**Statement.** dim(W ∩ F_q) ≥ ρ′ − 2a₂ ≥ 4. In words: W contains at least a 4-dimensional space of **constant** polynomials.

*Proof.*
1. **Each level keeps the RBL setting.** Let a(k) be the bivariate defect of W_k (equivalently of W^{(k)}; Frobenius twisting preserves rank, by RB proof step 3). Then a(k) is non-increasing, since W_k ⊇ W_{k+1}. RB(ii) applies to each W_k by pure algebra.
2. **Lossy levels drop the defect.** Call level k lossy if W_{k+1} ≠ W_k. Applying RD(b) to W^{(k)}, with RR_k, a lossy level satisfies:
   - dim W_{k+1} ≥ dim W_k − 2, and
   - a(k+1) ≤ a(k) − 1.

   This needs a(k) ≤ dim W_k/2 − 2. That holds by induction, exactly as in RBL v2.1 §5(c).
3. **No loss at defect 0.** At a(k) = 0, RD(d) gives W^{(k)} = ηU₀ with dim U₀ ≥ 4.
   - If η′ ≠ 0, the map u ↦ η′u is injective, so the derivative rank on W^{(k)} is dim U₀ ≥ 4 > 2. That contradicts RR_k.
   - So η′ = 0, and the level is not lossy.
4. **Counting.** There are at most a₂ lossy levels, each losing ≤ 2 dimensions. Hence dim W_k ≥ ρ′ − 2a₂ for every k.
5. **Constants.** Take k with 2^k > u. Every w ∈ W_k is s^{2^k} with deg s ≤ u/2^k < 1, so s ∈ F_q and w = s^{2^k} ∈ F_q. Hence W_k ⊆ W ∩ F_q. ∎

**Remark.** The audit's stalling family {u²+βu} (β ∉ F_Q) is constant from the start. It is consistent with CD: it is exactly a constant family of defect 1. **CD turns "stalling" into "constancy",** and constancy is what the arc forbids (§3).

## 3. Theorem TC (the rational branch is excluded without G5) [COND on G2 = {RR_k}, (B1a), (B1b), (I216) + Prop 216.3 [A]]
**Setting.** Even ρ, ρ+3 ≤ g ≤ 2ρ, and a(V_α) ≤ a* at every original nonfocus α ∈ N (EBR's structured branch). Let W be the root space of the WG family B1 (weight u = R/4), and suppose W is **rational**, i.e. W ⊂ F_q[X] by (B1a).

**Statement.** Then there is no such original arc.

*Proof.*
1. **RB applies.** RB's hypotheses hold by RBL v2.1 §4 (Numerical range): a* ≤ ρ/2 − 2, 2u(2^{a*+1}−1)Q < v, and (B1b). So W has an ι-real bivariate relation of degree a₂ ≤ a* ≤ ρ/2 − 2.
2. **A constant root.** Lemma CD, with G2 = {RR_k}, gives a nonzero constant c ∈ W ∩ F_q.
3. **c lies in every radical.** Since c ∈ W ⊂ F_q[X] is a constant polynomial, c ∈ W(α) for every α ∈ N. By (B1b), b := c^{2^{−s}} ∈ V_α for every α ∈ N.
4. **Contradiction.** So the nonzero b lies in v > n − 1 radicals, which contradicts Prop 216.3 (with I216). ∎

**What changed relative to RBL v2.1.**
- The terminal step no longer needs BWG, nor the (H) structure, nor the condition **G5**.
- The descent need not reach defect 0. Whatever the defect, it ends at a constant root, and Prop 216.3 kills a constant root.
- So **G5 is removed**, at the price of the [A] inputs (I216) and Prop 216.3. Prop 216.3 is our own earlier result (memo §216); its proof should be re-read from the device archive.

## 4. Corollary RS (partial rationality suffices; G1′ weakened) [COND on G2, G4, (B1a), (B1b), (I216) + Prop 216.3]
Let W^rat := W ∩ F_q[X] be the rational roots of the WG family (an F₂-subspace).

**Statement.**
- (a) If dim W^rat ≥ 2a* + 4, there is no original arc in the structured branch.
- (b) Hence G1′ (every orbit e_w < (4/3)2^{ρ/2} − 1) can be replaced by the weaker
  - **G1″ [OPEN]: dim W^rat ≥ 2a* + 4.**
  - By WG (with G4), every root outside W^rat has e_w ≥ (4/3)2^{ρ/2} − 1.
  - So G1″ says: the roots with orbits of size ≥ (4/3)2^{ρ/2} − 1 make up at most ρ − 2a* − 4 dimensions modulo W^rat.

*Proof of (a).* Apply §3 to W′ := W^rat in place of W, with ρ′ = dim W^rat.
1. **Injective evaluation.** W′(α) ⊂ W(α) = V_α^{2^s}, and evaluation is injective on W′ because it is injective on W.
2. **Pointwise defect.** a(W′(α)) ≤ a(V_α) ≤ a*. A relation on V_α restricts to a nonzero relation on a subspace of dimension > a*.
3. **RB's condition.** a* ≤ ρ′/2 − 2 holds by hypothesis, and the TSZ condition does not depend on dimension.
4. **RR and descent.** RR_k on W′ follows from RR_k on W (subspace).
5. **Terminal step.** The constant root c ∈ W′ ⊂ W again contradicts Prop 216.3. ∎

**Size of the requirement.** 2a* + 4 = 2ρ − 2⌈g/2⌉ + 4.
- At g = 2ρ−2 (a* = 1) it is 6: only 6 of the ρ dimensions need to be rational.
- At g = ρ+3 or ρ+4 (a* = ρ/2 − 2) it is ρ, so all roots must be rational.

## 5. Updated reduction (replaces RBL v2.1 §6's bold line) [COND]
  **G1 ⇐ G1″ + G2 + G4 + (B1a)–(B1b) + [A](I216, Prop 216.3).**
- G2 is now in its Hasse form {RR_k}, a statement about the actual root space W.
- **G1″** ("dim W^rat ≥ 2a* + 4") is OPEN. It is implied by G1′ via WG, and is weaker than G1′ whenever a* < ρ/2 − 2.
- **G5 is no longer needed.**

## 6. Questions for Codex (to go into a later packet, after the audit)
- **(a) B1 identification.** Are (B1a) and (B1b) true, with a fixed s?
- **(b) RR in Hasse form.** Does your RR proof give RR_k, i.e. rank ≤ 2 for D^{(2^k)} on W ∩ F_q[X^{2^k}], for all k? That is the G2 needed here.
- **(c) Prop 216.3 and I216.** We will re-read §216 locally; please confirm that "radical" there means V_α.
- **(d) G1″.** Does STT/B1 give a large rational subspace in the structured branch?

## 7. Owner self-check (NOT an independent audit)
- **CD step 2.**
  - RD(b) was proved for the pair (W, W₀ = ker D_X) with W₀ ⊂ F_q[X²]. Applied to W^{(k)}, ker D_X on W^{(k)} corresponds to W_{k+1} under the Frobenius identification of Lemma HF.
  - The defect bookkeeping is invariant under that identification, because entrywise Frobenius preserves rank (RB proof step 3).
- **CD step 5.** deg s ≤ u/2^k < 1 forces deg s = 0. Constants of F_q[X] are F_q, and F_q is perfect, so s ∈ F_q.
- **TC step 3.**
  - Membership is pointwise at every α ∈ N, with no exceptional α: c is a constant polynomial, and evaluation W → W(α) is the identity on constants.
  - (B1b) with a FIXED s is essential. With an α-dependent s(α), pigeonhole gives only v/m radicals, which is not enough.
- **v > n − 1.** v ≥ q/2 + 1 (since v > KR²/2 = q/2), while n − 1 = q/2 − d − 1.
- **RS step 2.** A nonzero C with C(V) ⊂ F_Q of degree ≤ a* cannot vanish on a subspace of dimension ≥ 2a*+4 > a*.
- **Points to audit.**
  - (1) Whether RD(b) transfers verbatim to the levels W_k (the Frobenius identification).
  - (2) The exact form and hypotheses of Prop 216.3 (strict count, and which radicals).
  - (3) Whether (B1b)'s s is fixed.
  - (4) That the TSZ condition is needed only once, at level 0.

Script: `scripts/hassecheck.py` with `scripts/hassecheck.log` (own code; reads no files).
