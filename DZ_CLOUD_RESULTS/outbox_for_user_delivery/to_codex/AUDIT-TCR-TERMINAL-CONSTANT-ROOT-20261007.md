# AUDIT — TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007.md (independent referee, cloud session, 7 Oct 2026, 19:22–19:40Z)

Referee: fresh, isolated subagent for the DZ line ("Wan's numbers of PPs"). No contact with the owner session or with Codex. No files outside the DZ scope were read (list in §7).
Note audited: `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007.md`, sha256 `bfb63eda267a614a23d6c149a768651ceb8a00081598f26bb6543818bbc07a85` (identical copy in `claude_archive/`).
Labels as in the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN].

## 0. Verdict: **PASS-with-fixes**

- The new mathematics is correct. That is Lemma HF [P] and Lemma CD [P mod RR_k, given the audited RD(b)], together with the conditional implications TC and RS(a).
  - I found no counterexample and no gap in any proof step.
  - My own [C] stress test of CD found 0 failures (§5).
- The terminal step is weaker than the note presents it. It rests on (I216) and Prop 216.3, and both are stated too loosely to carry it.
  - Prop 216.3 depends on the coordinate frame. It holds when the comparison direction is a nonfocus. It fails when that direction is a focus and the arc has a translation symmetry along it. The referee proved this and checked it by computation (C3).
  - So (I216) must fix the frame, the scale and the twist. A bare identification "radical = V_α" is not enough.
- The headline claims too much. "G5 is not an extra input" really means that G5 is *traded* for three [A]-pending inputs:
  - a precise (I216);
  - Prop 216.3, an unaudited earlier owner statement whose proof is not in the handoff;
  - a *strengthened* (B1b), with a fixed twist s.
- The fixes are about wording, labels and the statement of the inputs. No proof needs to be rewritten. **Owner revision is required before this note is sent to Codex.**

FIX count: **3 substantive, 8 minor.**

## 1. Item table

| # | Item | Claimed label | Referee finding | Status |
|---|---|---|---|---|
| 1 | §0 Inputs: RBL v2.1 (TSZ, RB, RD(a,b,d), B1a/B1b) | [A] | Matches RBL v2.1. (B1b) is *strengthened* here to a fixed s; RBL v2.1's (B1b) has no fixedness. | FIX-3 |
| 2 | §0 RR via IDEAS §305 | [A] | Citation accurate (IDEAS-PROJECT-TRIM line 18: "derivative rank ≤2 for rational root subspaces"). | OK |
| 3 | §0 Prop 216.3 via STATE §5 | [A] | Citation accurate (STATE line 208). The source is an *unlabelled tool bullet in the Plan section*, so it has no review status. The statement depends on the frame (C3). | FIX-1, FIX-2 |
| 4 | §0 (I216) | [A]-pending | Needed, but stated too loosely: it must fix the frame, a common scale, the twist and an injective index map. | FIX-1 |
| 5 | §1 Lemma HF (i)–(iii) | [P] | Correct. (ii) by induction; (iii) by Lucas, C(i·2^k, 2^k) ≡ i (mod 2). | PASS |
| 6 | §1 RR(W^{(k)}) ⟺ RR_k | [P] | Correct: rank = dim W_k − dim W_{k+1}, and Frobenius is injective and additive. | PASS |
| 7 | §1 "G2 restated on the actual family" | [P] | A correct *reformulation*. It does not reduce G2, and the rhetoric overstates that. | minor m2 |
| 8 | §1 [C] hassecheck | [C] | Reproduced byte for byte (m = 8, 12) and also at m = 16. Seeds are not logged, and the H2 test discriminates weakly. Referee re-test with structured s: 0 failures. | minor m6 |
| 9 | §2 Lemma CD, steps 1–5 | [P mod RR_k] | Correct. Steps 1, 2, 4 and 5 were checked line by line. Step 3 is correct but redundant, and its ordering relative to the induction is implicit. | PASS (m5) |
| 10 | §2 Remark (stalling family) | — | Correct. | OK |
| 11 | §3 Theorem TC, steps 1–3 | [COND] | Steps 1–3 are correct given RB, the numerical range, CD and fixed-s (B1b). | PASS |
| 12 | §3 Theorem TC, step 4 | [COND I216 + 216.3] | Valid only in a frame where Prop 216.3 holds, and only if α ↦ radical is injective. | FIX-1 |
| 13 | §3 "What changed" and the title | — | Overstated: G5 is traded, not removed. | FIX-2 |
| 14 | §4 Corollary RS(a), steps 1–5 | [COND] | Correct. Step 2's justification is unnecessary but harmless. RR_k on W^rat should be stated directly. | PASS (m3, m7) |
| 15 | §4 RS(b): G1″ weaker than G1′; WG threshold | [OPEN]/[COND] | Correct: e_w ≥ (4/3)2^{ρ/2} − 1 follows from √q = R·2^{ρ/2} ≤ 3(R/4)(e_w+1). G1′ ⇒ G1″ via WG + G4. | PASS |
| 16 | §4 Size of the requirement 2a*+4 | arithmetic | Correct: 6 at g = 2ρ−2, and ρ at g = ρ+3 and ρ+4. Checked over 870 cells (C4). | PASS |
| 17 | §5 reduction line | [COND] | G4 is not used by RS(a), so it is superfluous in the line "G1 ⇐ …". | minor m1 |
| 18 | §6 Questions for Codex | — | Appropriate. Question (c) should ask for the frame/scale data of FIX-1, not only whether "radical means V_α". | FIX-1 |
| 19 | §7 Owner self-check | — | Correct as far as it goes. v > n−1 is fine, with margin 2d+2 or more. Audit point (2) is exactly where the frame issue sits. | see FIX-1 |

## 2. Detailed audit

### 2.1 Lemma HF [P] — PASS
- **(i) Filtration.** W₀ = W ⊇ W₁ ⊇ … is trivial.
- **(ii) Descendants.** RBL §5(c) iterates W ↦ √(ker D_X|W), and ker D_X|W = W ∩ F_q[X²] in characteristic 2. The induction s ∈ W^{(k)} ⟺ s² ∈ W^{(k−1)} ⟺ s^{2^k} ∈ W is correct; the first ⟺ holds because s² ∈ F_q[X²] automatically.
- **(iii) Hasse identity.** For w = Σ s_i^{2^k}X^{i2^k}, D^{(2^k)} picks up C(i2^k, 2^k) ≡ i (mod 2) by Lucas. This gives (s′)^{2^k}. The kernel of D^{(2^k)} on W_k is W_{k+1}.
- **Equivalence.** RR(W^{(k)}) ⟺ RR_k, because rank(s ↦ s′ on W^{(k)}) = dim W_k − dim W_{k+1}.
- **[C].** The referee re-checked (H1), (H2) and (ii) independently over F_{2^24} (C2): 600 s, of which 332 were forced into F_q[X²], plus 150 descendant comparisons. 0 failures.

### 2.2 Lemma CD [P mod RR_k] — PASS
- **Step 1.** a(k) is non-increasing, because a relation on W_k restricts to W_{k+1}. The defect of W_k equals that of W^{(k)}, because the matrix of W_k is the entrywise 2^k-th power of the matrix of W^{(k)} (both the X-columns and the ι-columns), and this is a field embedding of L₂. RB(ii) (Galois descent; γ₀ ≠ 0 via W²) and RB(iii) are pure algebra for any F₂-space in F_q[X]. TSZ is needed only at level 0 (audit point 4: confirmed).
- **Step 2.** RD(b) applied to W^{(k)}:
  - ℓ = D_X(relation) vanishes on ker D_X and is independent of (γ, ιγ) when the level is lossy.
  - d₂(W_{k+1}) ≥ dim W_{k+1}/2 ≥ a(k)+1 holds once a(k) ≤ dim W_k/2 − 2 and RR_k gives dim W_{k+1} ≥ dim W_k − 2. So d₁ ≤ a(k) − 1.
  - The induction a(k) ≤ dim W_k/2 − 2 is preserved: a lossy level lowers the left side by at least 1 and the right side by at most 1.
  - Audit point 1, the Frobenius identification, is confirmed. The kernel of D_X on W^{(k)} is the 2^{−k}-th root of W_{k+1} (HF), and defects are Frobenius-invariant.
- **Step 3.** This step is correct. In RD(d), W^{(k)} = ηU₀, and η′ ≠ 0 would give rank dim U₀.
  - The step is not needed, though. At a(k) = 0, step 2's count would force d₁ ≤ −1 on a lossy level, which is impossible.
  - Its use of dim U₀ ≥ 4 relies on the step-4 bound at level k, so the induction should be made explicit (minor m5).
- **Step 4.** There are at most a₂ lossy levels, each costing at most 2 dimensions. Correct.
- **Step 5.** For 2^k > u, W_k ⊂ F_q. RR_k is needed only for 2^k ≤ u, because constant levels are lossless. Correct.
- **[C] (check C2-cd in §5).** 600 random rational families over F_{2^24}, with the generic point taken in F_{2^48}. The families include adversarial "defect-1 constant core plus t lossy levels" constructions.
  - (P1) monotone defect: 2278 level pairs, 0 failures.
  - (P2) lossy ⇒ defect drop: 65 instances, 0 failures.
  - (P3) CD conclusion under its hypotheses: 68 families, 0 failures, minimum slack 1.
  - Every family built with more lossy levels than its intended defect came out with *generic* defect ⌊ρ′/2⌋, as CD predicts.

### 2.3 Theorem TC — logically valid as a conditional; the inputs need sharper statements
- **Steps 1–2.** RB applies with a₂ ≤ a* ≤ ρ/2 − 2. This was verified over 870 even cells for ρ ≤ 60 (C4), including the TSZ range 2u(2^{a*+1}−1)Q < q/2. CD gives c ∈ W ∩ F_q∖{0}.
- **Step 3.** This is correct *given (B1b) with an α-independent s*. RBL v2.1's (B1b), the audited version, says only "a Frobenius twist of V_α"; fixedness is a new strengthening (FIX-3). The owner's remark that an α-dependent s(α) gives only v/m radicals by pigeonhole is correct, and v/m < n−1.
- **Step 4 (the critical point).** Prop 216.3, "a nonzero b lies in at most n−1 radicals", is not invariant under the choice of coordinates in which radicals of different projections are compared.
  - **The natural proof (referee reconstruction).** Put π_μ(x,y) = y + μx. For each pair {P, P′} ⊂ R and each b, the equation π_μ(P − P′) = b has at most one solution μ, *provided P − P′ is not vertical*. Each μ with b ∈ Rad_μ uses n/2 pairs. Hence #{μ} ≤ n−1. This needs the vertical direction (∞) to be a **nonfocus**.
  - **When ∞ is a focus**, a vertical pair contributes to *every* μ. If R + (0,b) = R, then b lies in Rad_μ for every finite nonfocus μ.
  - **(C3)** Parabola–subspace hyperfocused arcs R = {(a, a²) : a ∈ A₀} with A₀ ≤ F_q of dimension k, at q = 64 and 256 and n = 4, 8, 16.
    - In the original frame (∞ a nonfocus), the maximum number of radicals containing one b is exactly n−1. Prop 216.3 holds and is sharp.
    - After a linear change of frame that makes a focus direction vertical, one b lies in **all** finite nonfocus radicals (62, 58, 50, 254, 250, 242 of them), far above n−1.
  - These small arcs are not in the quadratic regime. They show only that the *statement* depends on the frame and on translation symmetry. That is exactly what (I216) must pin down.
  - **Scaling.** The reviewed same-arc theorem R3AF–AI (IDEAS-RECENT §298, ρ = 3) gives "every radical equals h(a,b)^{1/R}H*". So in a common frame the actual radicals of different projections are *different scalar multiples* λ_μH* of one space.
    - Hence any per-nonfocus normalisation of V_α (scaling, as in several earlier normal forms) destroys the transfer "c ∈ every W(α) ⟹ b ∈ every Rad_μ".
    - The referee found no statement in the handoff that fixes the normalisation of the original radicals V_α relative to Rad_μ.
- **Conclusion on TC.** TC is a correct implication **once (I216) is the precise statement in FIX-1**. As written, "(I216) identifies Rad_μ with V_α" does not suffice.

### 2.4 Corollary RS — PASS
- (a) W′ = W^rat. Each step checks out:
  - evaluation is injective on W′;
  - a(W′(α)) ≤ a(V_α^{2^s}) = a(V_α);
  - RB's condition holds with ρ′ ≥ 2a*+4;
  - the rank of a restriction is at most the rank, so RR_k passes to W′;
  - a constant in W′ is a constant in W.
- (b) The WG arithmetic is correct. G1′ ⇒ G1″ needs WG + G4. The comparison "strictly weaker iff a* < ρ/2−2" is correct.
- RS(a) itself does **not** use G4 (minor m1).

### 2.5 Labels and status
- The body carries correct [COND] labels.
- The title and §3 "What changed" do not carry them: "which Prop 216.3 forbids", "G5 is not an extra input", "G5 is removed" (FIX-2).
- The [A] label on Prop 216.3 is formally allowed ("earlier sources"). But the source line is an unlabelled tool bullet in STATE §5 (Plan), the proof (memo §216) is absent, and no review is recorded. The note should say so explicitly.

## 3. FIX items (substantive first)

**FIX-1 (substantive): state (I216) precisely; Prop 216.3 depends on the frame.** Replace (I216) by an explicit hypothesis, for example:

> (I216′) There are an F₂-linear bijection φ of F_q that does not depend on α (for instance x ↦ λx^{2^{−s}}), an injective map α ↦ μ(α) from N into the nonfocus directions, and normalised projections π_μ with the following property: for every pair P ≠ P′ in R and every b ≠ 0, the equation π_μ(P − P′) = b has at most one solution among the nonfocus μ. And φ(W(α)) = Rad_{π_{μ(α)}} for every α ∈ N.

Then Prop 216.3 holds in that frame by pair counting, with the constant n−1, or at worst n, which is harmless since v − n ≥ 2d + 1 > 0. TC step 4 follows.
- Record the referee's counterexample to the frame-free reading (C3): when a focus direction is the comparison direction, a translation-symmetric hyperfocused arc puts one b in every radical.
- Record that R3AF–AI shows that radicals in a common frame scale with the direction.
- Redirect question §6(c) to Codex accordingly: ask for the frame and scale in which the V_α are defined, not only whether "radical means V_α".

**FIX-2 (substantive): correct the headline claims and the status of Prop 216.3.**
- **Title, §3 "What changed", §5.** Say that G5 is *replaced* by (I216′) + Prop 216.3 + fixed-s (B1b), not that it is "not an extra input" or "removed".
- **§0.** Prop 216.3 is the owner's earlier statement, unaudited, read from an unlabelled Plan bullet. Its proof (memo §216) must be re-read, and its frame hypotheses checked, before TC is cited as more than [COND].

**FIX-3 (substantive): name the strengthened (B1b).**
- Introduce (B1b-fix) for "W(α) = V_α^{2^s} with s independent of α". This differs from RBL v2.1's audited (B1b), which has no fixedness.
- Use the new name in TC, RS, §5 and §6(a), so that a Codex confirmation of the weaker (B1b) is not taken as sufficient.
- Ideally, merge it into (I216′) (FIX-1), since both are parts of one identification φ.

**m1.** In §5, drop G4 from "G1 ⇐ G1″ + …", or annotate it "(G4 only for G1′ ⇒ G1″)". RS(a) does not use WG.

**m2.** In §1 "Consequence": call it a reformulation of G2 [P]. Do not suggest that G2 has become easier. Whether RR's proof gives Hasse-order ranks is the open question §6(b).

**m3.** In §4 step 4: define RR_k directly on W^rat (W^rat_k := W^rat ∩ F_q[X^{2^k}]). HF's setting assumes W ⊂ F_q[X], which fails for non-rational W.

**m4.** In the TC setting, "W is rational, i.e. W ⊂ F_q[X] by (B1a)" mixes two things. Rationality is the branch hypothesis; (B1a) converts it into polynomiality with deg ≤ u.

**m5.** In CD step 3, note that it is implied by step 2's count, or make the induction order explicit, since it uses dim W^{(k)} ≥ 4 from step 4.

**m6.** In the hassecheck log, record the seeds and command lines. The (H2) test with unstructured random s rarely hits s′ = 0; force half the samples into F_q[X²], as in the referee's C2.

**m7.** In RS step 2, the "cannot vanish on a subspace of dimension > a*" argument is unnecessary. A restricted relation is still a relation in the pair-module sense. Harmless.

**m8.** In §7, the self-check line "c lies in every radical: no exceptional α" should add "and distinct α give distinct radicals" (injectivity, FIX-1).

## 4. Minor notes (no fix required)
- v > n−1 holds with margin. With ∞ a nonfocus, v counts the finite nonfoci, q/2 + d + 1 of them, against n − 1 = q/2 − d − 1.
- The constant core produced by CD has dimension ≥ ρ′ − 2a₂ ≥ 4. Only one constant is used.
- The stalling family {u²+βu} is consistent with CD and would be killed by TC under (I216′).

## 5. Referee checks (`checks/`, all run with `python3 -I`, one process at a time)

| ID | Command | Result |
|---|---|---|
| C1 | `owner_copy/hassecheck.py 8 400 1`, `12 300 2`, `8 400 7`, `16 200 3` | 0/0 failures. The owner's two log lines are reproduced byte for byte (`owner_copy/rerun.log`). |
| C2 | `tcr_referee_checks.py hasse 11 600` | (H1) 0, (H2) 0 (332 s′ = 0 cases), (HF-ii) 0/150 |
| C2-cd | `tcr_referee_checks.py cd 7 600` | 600 families; (P1) 0/2278, (P2) 0/65, (P3) 0/68; Hasse-rank cross-check 0 failures |
| C3 | `tcr_referee_checks.py p216 5` | Original frame: max = n−1 in 6/6 cases. Focus-vertical frame: one b in all finite nonfocus radicals in 6/6 cases. |
| C4 | `tcr_referee_checks.py arith` | 870 cells, 0 failures (a* ≤ ρ/2−2; 2a*+4 formula and ≤ ρ; TSZ range; v > n−1); WG threshold algebra correct |

Hashes are in `checks/checks_SHA256SUMS.txt`.

## 6. Recommendation
- Apply FIX-1–FIX-3, the wording fixes, which need no new mathematics, and the minors.
- After that, TC and RS are acceptable as **[COND on G2, (I216′) including fixed s, Prop 216.3]**, with Lemmas HF and CD as [P] (CD mod RR_k).
- Before the note is sent to Codex, either re-read Prop 216.3 (memo §216) from the device archive with its frame hypotheses, or forward FIX-1's precise question to Codex.

## 7. Files read
- `dz_isolated/referee_TCR/src/TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007.md` (full)
- `dz_isolated/referee_TCR/src/owner_scripts/hassecheck.py`, `hassecheck.log` (full)
- `dz_isolated/work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md` (full; no referee read-restriction found)
- `DZ-CLOUD-HANDOFF/docs/STATE-PROJECT-TRIM.md` (full)
- `DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md` (full)
- `DZ-CLOUD-HANDOFF/docs/IDEAS-PROJECT-TRIM.md` (grep hits only; line 18, §305)
- `DZ-CLOUD-HANDOFF/docs/IDEAS-DZ-QUADRATIC-REGIME-RECENT.md` (grep hits; lines 868–885 and 1020–1050)
- `DZ-CLOUD-HANDOFF/notes/{EBR,UGP,IT,NDX,OBC,ODD-RHO-GEN-TAUFLAG}*.md` (grep hits only)
- `/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md` (full, as cited)
- `claude_archive/` directory listing (names only); no other archive file was opened.
