# Even ρ, gap G1: generic real type is FALSE in the abstract setting (toy family TX); the rational branch lifts BIVARIATELY (twisted Schwartz–Zippel) and then descends while staying nonzero; G1 reduces, modulo named inputs, to an orbit bound G1′ (owner note v2, cloud session, 7 Oct 2026, 19:06Z; v1 18:27Z) [v2: FIX-1, FIX-3]

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac). Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed sources; [COND] conditional on a named input.

**AUDIT STATUS (v2).**
- v1 (sha256 c5f5b805…a34cfe) was independently audited (AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md, 18:29–19:05Z). Verdict: **PASS-with-fixes** (3 substantive and 8 minor FIX items).
- This v2 applies all eleven. Each change is marked [v2: FIX-n].
- The v2 revision itself has NOT yet been re-checked by a referee. **HOLD**: do not send to Codex until it is.

**Inputs [A].**
- HFD §1: real structure, pair-relation module, Popov degrees.
- EBR: Lemma G, and the generic relation C(w) = D(w^Q) with deg ≤ a*.
- The PHFG sketch (HFD §3), with its steps 2–4 and gaps G1–G4.
- WG, as quoted in HFD §3: "a component of degree e_w > 1 with all nonfoci totally split needs √q ≤ 3u(e_w+1)".
- RR, as quoted in IDEAS §305: "derivative rank ≤ 2 for rational root subspaces".
- **The WG and RR statements are [A] via the HFD/IDEAS summary readings only.** Those documents record that only Codex summaries of WG/RR were read, not the proofs. [v2: FIX-10]

**Notation.**
- m is even, Q = 2^{m/2}, q = Q², and x̄ = x^Q on F_q.
- N is the set of original nonfoci, v = |N| > Q²/2.
- a(V) is the half-field defect.
- For a polynomial f ∈ F_q[X], f^{(Q)} has its coefficients raised to the Q-th power, so f(α)^Q = f^{(Q)}(ᾱ) for α ∈ F_q.

## 1. Lemma AR (real type at rational points is automatic) [P]
**Statement.** Let a := a_gen be the generic defect, i.e. the minimal degree of a generic relation C(w) = D(w^Q), and suppose a < ρ/2. Let α ∈ N with a(V_α) = a, and suppose the primitive generic relation (C, D) does not vanish at α. Then (C_α, D_α) is real type: D_α = κ_α C̄_α.

*Proof.*
1. The specialisation is a nonzero relation of degree ≤ a on V_α.
2. By HFD §1, at a(V_α) = a < ρ/2 the relations of degree ≤ a form a χ-stable line, and a χ-stable line is spanned by a real relation (C_r, C̄_r).
3. Write the specialisation as λ(C_r, C̄_r). Then D_α = (λ/λ̄)C̄_α. ∎

**Consequence [H].** Pointwise realness carries no information beyond "generic identity + V_α ⊂ F_q". Any proof of G1 must take its extra input from the arc (weights, WG, RR, BWG), not from the pointwise real structure. This is an interpretation of the lemma, not a theorem. [v2: FIX-8]

## 2. Proposition TX (a toy family: generic real type fails) [P; C]
**Setting.** Let ρ ≥ 6 be even with ρ ≤ m/2. Let U ⊂ F_Q be a fixed ρ-dimensional F₂-subspace, and A = Z² + XZ. Put
  W := A(U) = {u² + Xu : u ∈ U} ⊂ F_q[X],   V_α = W(α) (α ∈ F_q).

**1. Pointwise defect.** [v2: FIX-4]
- V_α is degenerate (dimension ρ−1) exactly when α ∈ U∖{0}. Otherwise dim V_α = ρ.
- **Defect ≤ 1 at every non-degenerate α.** Take Γ_α = τ + ᾱ(α+ᾱ) and Δ_α = τ + α(α+ᾱ), where τ is squaring.
  - Then Γ_α(τ+α) = Δ_α(τ+ᾱ); both sides equal τ² + (α²+α^{Q+1}+α^{2Q})τ + α^{Q+1}(α+ᾱ).
  - Since u ∈ F_Q gives v̄ = ū² + ᾱū = (τ+ᾱ)(u), we get Γ_α(v) = Δ_α(v̄) = \overline{Γ_α(v)}.
  - So C_α := Γ_α maps V_α into F_Q.
- **Exact values.**
  - For α ∈ F_Q∖U, V_α ⊂ F_Q, so a(V_α) = 0.
  - For α ∉ F_Q, a(V_α) = 1 exactly. Suppose a(V_α) = 0, i.e. V_α ⊂ λF_Q. Then two independent elements satisfy u₁²+αu₁ = r(u₂²+αu₂) with r ∈ F_Q, so α(u₁+ru₂) = u₁²+ru₂². Either α ∈ F_Q, or u₁ = ru₂; the latter gives r² = r, so u₁ = u₂, a contradiction. (Proof from the audit.)

**2. Generic relation, NOT real type.**
- Over L = F_q(X) we have w^Q = u² + X^Q u. The same identity with ᾱ replaced by X^Q gives the generic relation
  C = Z² + X^Q(X+X^Q)Z,   D = Z² + X(X+X^Q)Z,   C(w) = D(w^Q).
- **The generic defect is exactly 1.** [v2: FIX-4] A degree-0 generic relation would specialise to a(V_α) = 0 at all but finitely many α. That contradicts a(V_α) = 1 for all α ∉ F_Q.
- Hence the relations of degree ≤ 1 form a line, by the HFD count with d₁ = 1 < d₂ = ρ−1.
- Real type would need D = κC^{(Q)}. That forces κ = 1 (the leading coefficients are monic) and X²+X^{Q+1} = X^{q+Q}+X^{2q} in F_q[X], which is false.

**3. C(W) is not contained in ηF_Q for any η.**
- C(w) = u⁴ + (X²+X^{Q+1}+X^{2Q})u² + X^{Q+1}(X+X^Q)u.
- Comparing the X⁰- and X²-coefficients, a constant ratio C(w₁)/C(w₂) forces (u₁/u₂)⁴ = (u₁/u₂)², i.e. u₁ = u₂.

**4. The family is rational and violates RR.** All roots are polynomials. w′ = u, so the derivative map W → W′ is injective (rank ρ).

**Meaning.** PHFG step 1 claimed "S_j generically dependent ⟹ C(W) ⊂ F_Q (constants) after rescaling". TX satisfies every hypothesis used at that point:
- a generic family with polynomial roots;
- every α totally split;
- pointwise defect ≤ 1 at every non-degenerate α;
- generic defect 1 ≤ ρ/2 − 2.

Yet the conclusion fails. **So G1, as formulated (lift the real type generically), is not provable from those hypotheses.** TX is not an arc family: RR excludes it (item 4). The correct target must use arc input; see §5–§6.

**[C] toycheck.py** (own code, `python3 -I`; the auditor reproduced it byte for byte with seeds 1, 2, 3).

| m | ρ | random α tested | a(V_α) observed | C_α(v) ∉ F_Q | bivariate rank at independent (X,Y) |
|---|---|---|---|---|---|
| 16 | 6 | 199 | 1 in every sample | 0 | always 3 |
| 20 | 8 | 120 | 1 in every sample | 0 | always 3 |
| 24 | 10 | 60 | 1 in every sample | 0 | always 3 |

- "1 in every sample" is a sampling effect: F_Q has density 1/Q, so random α almost never lies in it, and the defect-0 set α ∈ F_Q∖U was not hit. [v2: FIX-4]
- The auditor's exhaustive check at m = 12 confirmed the exact values in item 1.
- At (16, 6) one further α was degenerate and was skipped.
- The last column shows a bivariate degree-1 relation (§4) in every case.
- **Control.** A random rational family of degree ≤ 3 has pointwise defect ρ/2 *generically*; seed 1 at m = 20 showed one sporadic α with defect ρ/2−1. Its bivariate rank is 4, i.e. there is no degree-1 bivariate relation. [v2: FIX-9]

## 3. Lemma TSZ (twisted Schwartz–Zippel) [P]
**Statement.** Let f ∈ F_q[X,Y] with deg_X f ≤ δ and deg_Y f ≤ δ. Suppose f(α, ᾱ) = 0 for all α in a set N ⊂ F_q with |N| > 2δQ. Then f = 0.

*Proof.*
1. Fix ω ∈ F_q∖F_Q. Every α ∈ F_q is uniquely x+ωy with x, y ∈ F_Q, and then ᾱ = x+ω̄y.
2. Put h(x,y) := f(x+ωy, x+ω̄y). It has total degree ≤ 2δ.
3. Write h = h₁ + ωh₂ with h₁, h₂ ∈ F_Q[x,y]. At F_Q-points both h_i take F_Q-values, so both vanish on the image N′ ⊂ F_Q² of N, and |N′| = |N|.
4. By Schwartz–Zippel, a nonzero polynomial of total degree ≤ 2δ has at most 2δQ zeros in F_Q². Hence h₁ = h₂ = 0, so h = 0.
5. The map (x,y) ↦ (x+ωy, x+ω̄y) is an invertible linear change of variables over F_q, since ω ≠ ω̄. Hence f = 0. ∎

## 4. Theorem RB (rational branch: pointwise defect lifts to a bivariate real relation) [P]
**Setting.**
- L₂ := F_q(X,Y), with the order-2 automorphism ι(f)(X,Y) := f^{(Q)}(Y,X).
- Its fixed field is F := F_Q(x,y), where X = x+ωy and Y = x+ω̄y. Explicitly x = (ω̄X+ωY)/(ω+ω̄) and y = (X+Y)/(ω+ω̄), so ι(x) = x and ι(y) = y. [v2: FIX-11]
- W ⊂ F_q[X] is a ρ′-dimensional F₂-space of polynomials of degree ≤ u.
- For α ∈ N, W(α) is ρ′-dimensional and a(W(α)) ≤ a, where a ≤ ρ′/2 − 2.

**Statement.** If 2u(2^{a+1}−1)Q < |N|, then:
- (i) the pair (W, ιW) has a nonzero relation of degree ≤ a over L₂, i.e. Σ_{e≤a} γ_e w^{2^e} + δ_e(ιw)^{2^e} = 0 for all w ∈ W;
- (ii) one such relation, of minimal degree a₂ ≤ a, can be taken **ι-real** (δ = ιγ) with γ₀ ≠ 0. Equivalently, C := Σγ_eτ^e has C(W) ⊂ F;
- (iii) the relations of degree ≤ a₂ form an L₂-line.

*Proof.*
1. **(i)** Let M(X,Y) = [w_i(X)^{2^e} | w_i^{(Q)}(Y)^{2^e}]_{e≤a}, a ρ′ × (2a+2) matrix.
   - Since ιw = w^{(Q)}(Y) and w(α)^Q = w^{(Q)}(ᾱ), M(α,ᾱ) is exactly the defect matrix of W(α).
   - Each (2a+2)-minor has deg_X, deg_Y ≤ u(2^{a+1}−1) and vanishes at every (α,ᾱ) with α ∈ N.
   - By TSZ every minor is 0, so rank M < 2a+2 over L₂.
2. **(ii) A real relation.** ι(w^{(Q)}(Y)) = w^{(q)}(X) = w(X). So (γ,δ) ↦ (ιδ, ιγ) maps relations to relations; this map is ι-semilinear of order 2.
   - A nonzero ι-stable L₂-space contains a nonzero fixed vector (Galois descent for L₂/F).
   - A fixed vector has δ = ιγ, and γ ≠ 0, since otherwise δ = 0 too.
3. **(ii) γ₀ ≠ 0.** Suppose γ₀ = 0, hence δ₀ = 0.
   - Then the coefficients (γ_{e+1}, δ_{e+1}) give a relation of degree a₂−1 for W² = {w²}.
   - But M(W²) at degree d is the entrywise square of M(W) at degree d. Entrywise squaring is a field embedding, so it preserves rank, and W² has the same minimal degree a₂. Contradiction.
4. **(iii) The pair-relation module over L₂.** HFD §1 transfers verbatim. [v2: FIX-6]
   - Division with remainder A = PB + R (B on the right) exists in L₂{τ}, because the needed leading coefficient lc(A)/lc(B)^{2^{n−k}} always exists (n−k is the degree difference).
   - This gives weak Popov forms, with pivots in distinct columns, for left submodules.
   - Frobenius-twisting a leading row preserves its pivot position, so the predictable-degree property holds. Hence the relations of degree ≤ L have dimension (L+1−d₁)₊ + (L+1−d₂)₊.
   - Moore over L₂ gives d₁+d₂ = ρ′.
   - At d₁ = a₂ ≤ ρ′/2−2 the count is 1 for L = a₂. ∎

**Numerical range (arithmetic) [P].** Take WG's family B1 of weight u = R/4, and |N| = v > Q²/2 = KR²/2.
- Then 2u·2^{a+1}Q = R2^aQ = 2^{a−ρ/2}Q² ≤ Q²/4 < v whenever **a ≤ ρ/2−2**.
- That range **contains** EBR's structured range a ≤ a*, since a* ≤ ρ/2−2. [v2: FIX-7]
- **Application to the arc [COND on (B1a), (B1b)]: the hypothesis of RB holds in every open even cell PROVIDED** [v2: FIX-2]:
  - **(B1a)** B1 is monic over F_q[X], so that in the rational branch its roots are polynomials of degree ≤ u = R/4; and
  - **(B1b)** at every original nonfocus α, B1's root space is ρ-dimensional and a Frobenius twist of V_α, so that its defect is ≤ a(V_α).
  - Both are [A]-pending from Codex. If B1's root space were only a ρ′-dimensional subspace of V_α, RB would need a ≤ ρ′/2−2, which can fail.
- **Weight K.** The condition is K·2^{a+3} < Q, i.e. a ≤ g−ρ/2−4. Given a ≤ a* = ρ−⌈g/2⌉, this holds for every g ≥ ρ+3; at g = ρ+3, a* = ρ/2−2 ≤ ρ/2−1. The auditor checked this over 39,800 cells.

## 5. Proposition RD (descent in the rational branch) [COND on G2 + G5 + (B1a)–(B1b)] [v2: FIX-1, FIX-2]
**Setting.**
- Keep RB's setting, and suppose RR applies to W and to every square-root descendant. This is gap G2 of HFD §3, the same input PHFG and HFA1 use.
- Let D_X = ∂/∂X on L₂, and W₀ := ker(D_X|W) = W ∩ F_q[X²].

**Statement.**
- **(a)** γ₀w′ = ℓ(w) := Σ_e D_X(γ_e)w^{2^e} + D_X(ιγ_e)(ιw)^{2^e} for all w ∈ W.
- **(b)** RR gives dim W₀ ≥ ρ′−2. Moreover, either W₀ = W, or W₀ has bivariate defect ≤ a₂−1.
- **(c) Replaced.** [v2: FIX-1] Iterate W ↦ √W₀. Here √W₀ ⊂ F_q[X] has degree ≤ (current degree)/2 and the same bivariate defect as W₀, and RB(ii) applies to it by pure algebra, with no further TSZ. Each step either:
  - keeps the dimension (W₀ = W) while the degree halves; or
  - loses ≤ 2 dimensions while the defect drops by ≥ 1.

  Hence **every descendant is nonzero, with dimension ≥ ρ′−2a₂ ≥ 4**, and the inequality a_i ≤ ρ_i/2−2 is preserved. **If defect 0 is ever reached, (d) applies.**
  - Nothing in RB, RD or RR forces a defect drop.
  - Abstract example (from the audit): the constant family {u²+βu : u ∈ U} with β ∉ F_Q has degree 0 ≤ u, defect 1 at every α, and RR-rank 0. It is its own square-root descendant up to Frobenius twist, and it never reaches defect 0.
- **(d)** Suppose defect 0 is reached. Then (cw)/(cw₁) ∈ F ∩ F_q(X) = F_Q for all w, so the family is ηU₀ with η ∈ F_q[X] and U₀ ⊂ F_Q. This is HFA1's rational (H) structure.
  - RR then forces η′ = 0 at each further step, since the rank of u ↦ η′u is dim U₀ ≥ 4. The descent continues as in HFA1.
- **(e) Termination: the named condition G5.** [v2: FIX-1]
  - **G5:** HFA1's terminal step (weight bookkeeping + BWG) excludes a nonzero rational descended family at the terminal weight *irrespective of its defect*; or positive-defect terminal families are excluded by other arc input.
  - Without G5, RB+RD give only (c): a nonzero descendant of dimension ≥ 4 persists at every weight.

*Proof.*
1. **(a)** Apply D_X to the real relation. D_X kills (ιw)^{2^e} and w^{2^e} for e ≥ 1, because these are functions of Y or squares.
2. **(b)** [v2: FIX-5] Suppose W₀ ≠ W.
   - Then ℓ does not vanish identically on W; otherwise γ₀w′ ≡ 0, i.e. W₀ = W.
   - The relation (γ,ιγ) does vanish on all of W, so ℓ is not an L₂-multiple of (γ,ιγ).
   - Both vanish on W₀, which therefore carries two independent relations of degree ≤ a₂.
   - With ρ″ = dim W₀ ≥ ρ′−2 and d₂ ≥ ρ″/2 ≥ a₂+1, the count (a₂+1−d₁)₊ + (a₂+1−d₂)₊ ≥ 2 forces d₁ ≤ a₂−1.
   - The minimal relation is again ι-real, by RB(ii) applied to W₀.
3. **(c)** The dimension drops only at defect drops, by ≤ 2 each. So ρ_i ≥ ρ′−2(a₂−a_i) ≥ ρ′−2a₂, and a_i ≤ ρ_i/2−2 is preserved.
4. **(d)** w/w₁ is ι-fixed and lies in F_q(X). Being ι-fixed, it equals its own (Q)-twist in Y, so it is constant and lies in F_Q. ∎

**Status.** [v2: FIX-1, FIX-2]
- RB is [P].
- RD is [COND on G2 + G5 + (B1a)–(B1b)].
- In the rational branch (all roots of the WG family rational), RB+RD reduce the structured branch to the terminal question G5. The bivariate real relation replaces the false "C(W) ⊂ F_Q constants".
- RB+RD do NOT by themselves remove G1 in the rational branch.

## 6. What G1 now is: an orbit bound G1′, modulo named inputs [OPEN; H] [v2: FIX-3]
By TX, generic real type cannot be the target. By RB/RD, the rational branch is reduced to G5 (mod G2, (B1a)–(B1b)). With u = R/4, WG kills components with 1 < e_w < (4/3)2^{ρ/2} − 1. So:

**G1′ (orbit bound).** In an open even cell with a(V_α) ≤ a* at every nonfocus, every root of the WG family has Galois orbit size e_w < (4/3)2^{ρ/2} − 1.

Then WG gives e_w = 1, and RB+RD hand over to G5.

**G1 ⇐ G1′ + G2 + G4 + G5 + [A] B1 identification (B1a)–(B1b).** [v2: FIX-3]
- G4 is the geometric irreducibility needed for WG (HFD §3).

**Why counting does not give G1′ [H].**
- **Base-curve counting fails.**
  - The generic relation's coefficients have degree about K·Q·2^{a+1} (Lemma G).
  - TX suggests that degree about Q is intrinsic, since the coefficients involve X^Q. This is a single example. [H]
  - So every conjugated identity over the α-line has degree ≥ Q·deg > v.
  - TSZ needs bidegree < Q/4; only the ROOTS have that (degree u), not the coefficients.
- **Counting on the cover fails.** On the Galois closure X_W the minors have low bidegree on X_W × X_W^{(Q)}. But the twisted rational points lie on the Frobenius graph, and counting on a curve of genus ≳ |G|u gives nothing.
- **Twisted half-field families.**
  - For the natural families A(ηU₀) with η Kummer, or C^{−1}(ηU₀), one has e_w ≤ 2^a·e with e | 2^t−1.
  - **No family with generic defect a ≥ 1 and large orbits is known.**
  - Constructing one, or proving G1′ from the arc's B1 structure (STT), is the next step.
- **A possible route: the Lang-type equation C·A = D·A^{(Q)}, deg A ≤ a.**
  - Pointwise it has a nonzero F_Q-line of solutions A_α. This rests on a real 2a+1 vs 2a+2 dimension count, which is NOT checked here.
  - Its extreme coefficients satisfy the Kummer equations a_a^{(Q−1)2^a} = c_a/d_a and a₀^{Q−1} = c₀/d₀. The auditor checked these.
  - If a generic solution with small orbits exists, then R_P ⊇ A(ηF_Q), and W ∩ A(ηF_Q) has dim ≥ ρ−a with e_w ≤ e·(orbit of A).
  - [H] only.

## 7. Owner self-check (v1, updated)
- **TX identity Γ(τ+α) = Δ(τ+ᾱ).**
  - The τ-coefficients are α²+α^{Q+1}+α^{2Q} on both sides, and the constants are α^{Q+1}(α+ᾱ) on both sides.
  - Rechecked by hand and confirmed numerically: C2, 0 failures at m = 16, 20, 24. The auditor's T1–T7 also passed.
- **TSZ.** The total degree of h is ≤ deg_X + deg_Y. The F_Q-splitting h = h₁ + ωh₂ is valid because h_i(x,y) ∈ F_Q at F_Q-points.
- **RB(i).** The minors have deg_X ≤ u·Σ_{e≤a}2^e, and the ι-columns have the same Y-degree.
- **RB(iii).** [v2: FIX-6] Weak Popov forms over the non-perfect L₂ use only division with remainder with B on the right. Windows start at 0, so no φ^{−1} is needed (unlike HFD, which used σ^{−1} on F_Q).
- **RD(b).** [v2: FIX-5] ℓ is not an L₂-multiple of (γ,ιγ), because ℓ does not vanish identically on W while (γ,ιγ) does. D_X(ιγ_e) is well defined, since ιγ_e ∈ L₂.
- **Audit points.**
  - (1) TSZ constants against the exact v: PASS (auditor, 39,800 cells).
  - (2) B1 identification: now named (B1a)–(B1b), [A]-pending.
  - (3) RR for subspaces of descendants: G2.
  - (4) F₂-independence over L₂ follows from dimension ρ′ at α ∈ N.

## 8. Change log v1 → v2
| FIX | Where | Change |
|---|---|---|
| FIX-1 | §5(c)–(e), Status, title | RD(c) restated: nonzero descendants with dim ≥ ρ′−2a₂. The abstract stalling example added. New named condition G5. |
| FIX-2 | §4 Numerical range, §5 header and Status | Application conditional on (B1a)–(B1b). Status: G2 + G5 + (B1a)–(B1b). |
| FIX-3 | §6, title | G1 ⇐ G1′ + G2 + G4 + G5 + B1 identification. |
| FIX-4 | §2 items 1–2, table | Degenerate α excluded. Defect 0 on F_Q∖U, exactly 1 off F_Q. Generic defect exactly 1. "Always 1" relabelled as sampling. |
| FIX-5 | §5(b) proof, §7 | Independence wording fixed. |
| FIX-6 | §4(iii), §7 | Division-with-remainder wording, with exponent 2^{n−k}. |
| FIX-7 | §4 Numerical range | "EXACTLY" changed to "contains". |
| FIX-8 | §1 Consequence | Labelled [H]. |
| FIX-9 | §2 control row | "Generically" ρ/2, sporadic ρ/2−1 noted; "no degree-1 bivariate relation". |
| FIX-10 | Inputs | WG/RR marked [A] via summary readings. |
| FIX-11 | §4 Setting | Y = x+ω̄y, with explicit x, y. |

Scripts:
- `scripts/toycheck.py` (own GF(2^m) code; reads no extracted files) with `scripts/toycheck.log`.
- The auditor's checks are in `audit_RBL_checks/`.
