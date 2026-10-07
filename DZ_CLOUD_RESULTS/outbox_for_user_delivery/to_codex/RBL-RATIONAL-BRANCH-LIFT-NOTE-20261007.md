# Even ρ, gap G1: generic real type is FALSE in the abstract setting (toy family TX); the rational branch lifts BIVARIATELY (twisted Schwartz–Zippel) and then descends as in HFA1; G1 reduces to an orbit bound G1′ (owner note, cloud session, 7 Oct 2026, 18:27Z)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac). Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed sources; [COND] conditional on a named input.

**AUDIT STATUS: NOT INDEPENDENTLY AUDITED.** This cloud session had no subagent tool, so only an owner self-check (§7) was done. Per the standing rules, nothing here may be sent to Codex before an independent agent audit.

**Inputs [A]:** HFD §1 (real structure, pair-relation module, Popov degrees), EBR (Lemma G, the generic relation C(w) = D(w^Q) with deg ≤ a*), PHFG sketch (HFD §3) with its steps 2–4 and gaps G1–G4, WG as quoted there ("a component of degree e_w > 1 with all nonfoci totally split needs √q ≤ 3u(e_w+1)"), RR as quoted ("derivative rank ≤ 2 for rational root subspaces").

**Notation.** m even, Q = 2^{m/2}, q = Q², x̄ = x^Q on F_q. N = set of original nonfoci, v = |N| > Q²/2. a(V) = half-field defect. For a polynomial f ∈ F_q[X], f^{(Q)} has its coefficients raised to the Q-th power, so f(α)^Q = f^{(Q)}(ᾱ) for α ∈ F_q.

## 1. Lemma AR (real type at rational points is automatic) [P]
Let a := a_gen be the generic defect (minimal degree of a generic relation C(w) = D(w^Q)), with a < ρ/2. Let α ∈ N with a(V_α) = a, and suppose the primitive generic relation (C, D) does not vanish at α. Then (C_α, D_α) is real type: D_α = κ_α C̄_α.

*Proof.* The specialisation is a nonzero relation of degree ≤ a on V_α. By HFD §1, at a(V_α) = a < ρ/2 the degree-≤a relations form a χ-stable line, and a χ-stable line is spanned by a real relation. ∎

**Consequence.** Pointwise realness carries NO information beyond "generic identity + V_α ⊂ F_q". Any proof of G1 must extract the extra input from the arc (weights, WG, RR, BWG), not from the pointwise real structure itself.

## 2. Proposition TX (a toy family: generic real type fails) [P; C]
Let ρ ≥ 6 be even, ρ ≤ m/2, U ⊂ F_Q a fixed ρ-dimensional F₂-subspace, and A = Z² + XZ. Put
  W := A(U) = {u² + Xu : u ∈ U} ⊂ F_q[X],   V_α = W(α) (α ∈ F_q).

1. **Pointwise defect ≤ 1 at EVERY α ∈ F_q.** Take Γ_α = τ + ᾱ(α+ᾱ) and Δ_α = τ + α(α+ᾱ), where τ is squaring. Then Γ_α(τ+α) = Δ_α(τ+ᾱ): both sides equal τ² + (α²+α^{Q+1}+α^{2Q})τ + α^{Q+1}(α+ᾱ). Since u ∈ F_Q gives v̄ = ū² + ᾱū = (τ+ᾱ)(u), we get Γ_α(v) = Δ_α(v̄) = \overline{Γ_α(v)}. So C_α := Γ_α maps V_α into F_Q.
2. **Generic relation, NOT real type.** Over L = F_q(X), w^Q = u² + X^Q u, and the same identity with ᾱ replaced by X^Q gives the generic relation
   C = Z² + X^Q(X+X^Q)Z,   D = Z² + X(X+X^Q)Z,   C(w) = D(w^Q).
   For ρ ≥ 4 the degree-1 relations form a line (a = 1 < ρ/2). Real type would need D = κC^{(Q)}. That forces κ = 1 and X²+X^{Q+1} = X^{q+Q}+X^{2q} in F_q[X], which is false.
3. **C(W) is not contained in ηF_Q for any η.** C(w) = u⁴ + (X²+X^{Q+1}+X^{2Q})u² + X^{Q+1}(X+X^Q)u. Comparing the X⁰- and X²-coefficients, a constant ratio C(w₁)/C(w₂) forces (u₁/u₂)² = 1, i.e. u₁ = u₂.
4. **The family is rational and violates RR.** All roots are polynomials. w′ = u, so the derivative map W → W′ is injective (rank ρ).

**Meaning.** PHFG step 1 claimed "S_j generically dependent ⟹ C(W) ⊂ F_Q (constants) after rescaling". TX satisfies all the hypotheses used at that point:
- a generic family with polynomial roots;
- every α totally split;
- pointwise defect ≤ 1 everywhere;
- generic defect 1 ≤ ρ/2 − 2.

Yet the conclusion fails. **So G1, as formulated (lift the real type generically), is not provable from those hypotheses.** TX is not an arc family; it is excluded by RR (item 4). The correct target must use arc input. See §5.

**[C] toycheck.py** (own code, `python3 -I`):

| m | ρ | α tested | a(V_α) | C_α(v) ∉ F_Q | bivariate rank at independent (X,Y) |
|---|---|---|---|---|---|
| 16 | 6 | 199 | always 1 | 0 | always 3 |
| 20 | 8 | 120 | always 1 | 0 | always 3 |
| 24 | 10 | 60 | always 1 | 0 | always 3 |

- At (16, 6) one more α gave a degenerate V_α and was skipped.
- The last column shows a bivariate degree-1 relation (§4) in every case.
- **Control:** a random rational family of degree ≤ 3 has pointwise defect ρ/2 and bivariate rank 4, i.e. no relation.

## 3. Lemma TSZ (twisted Schwartz–Zippel) [P]
Let f ∈ F_q[X,Y] with deg_X f ≤ δ and deg_Y f ≤ δ. Suppose f(α, ᾱ) = 0 for all α in a set N ⊂ F_q with |N| > 2δQ. Then f = 0.

*Proof.*
1. Fix ω ∈ F_q∖F_Q. Every α ∈ F_q is uniquely x+ωy with x, y ∈ F_Q, and then ᾱ = x+ω̄y.
2. Put h(x,y) := f(x+ωy, x+ω̄y). This is a polynomial of total degree ≤ 2δ.
3. Write h = h₁ + ωh₂ with h₁, h₂ ∈ F_Q[x,y]. At F_Q-points both h_i take F_Q-values, so both vanish on the image N′ ⊂ F_Q² of N, and |N′| = |N|.
4. A nonzero polynomial of total degree ≤ 2δ has at most 2δQ zeros in F_Q² (Schwartz–Zippel). Hence h₁ = h₂ = 0, so h = 0.
5. (x,y) ↦ (x+ωy, x+ω̄y) is an invertible linear change of variables over F_q, because ω ≠ ω̄. Hence f = 0. ∎

## 4. Theorem RB (rational branch: pointwise defect lifts to a bivariate real relation) [P]
**Setting.**
- L₂ := F_q(X,Y), with the order-2 automorphism ι(f)(X,Y) := f^{(Q)}(Y,X). Its fixed field is F := F_Q(x,y), where X = x+ωy.
- W ⊂ F_q[X] is a ρ′-dimensional F₂-space of polynomials of degree ≤ u.
- For α ∈ N, W(α) is ρ′-dimensional and a(W(α)) ≤ a, where a ≤ ρ′/2 − 2.

**Statement.** If 2u(2^{a+1}−1)Q < |N|, then:
- (i) the pair (W, ιW) has a nonzero relation of degree ≤ a over L₂, i.e. Σ_{e≤a} γ_e w^{2^e} + δ_e(ιw)^{2^e} = 0 for all w ∈ W;
- (ii) one such relation of minimal degree a₂ ≤ a can be taken **ι-real** (δ = ιγ), with γ₀ ≠ 0. Equivalently, C := Σγ_eτ^e has C(W) ⊂ F;
- (iii) the relations of degree ≤ a₂ form an L₂-line.

*Proof.*
1. **(i)** Let M(X,Y) = [w_i(X)^{2^e} | w_i^{(Q)}(Y)^{2^e}]_{e≤a} (ρ′ × (2a+2)).
   - Since ιw = w^{(Q)}(Y) and w(α)^Q = w^{(Q)}(ᾱ), M(α,ᾱ) is exactly the defect matrix of W(α).
   - Each (2a+2)-minor has deg_X, deg_Y ≤ u(2^{a+1}−1) and vanishes at every (α,ᾱ), α ∈ N.
   - By TSZ every minor is 0, so rank M < 2a+2 over L₂.
2. **(ii) A real relation.** ι(w^{(Q)}(Y)) = w^{(q)}(X) = w(X). So (γ,δ) ↦ (ιδ, ιγ) maps relations to relations; it is ι-semilinear and of order 2.
   - A nonzero ι-stable L₂-space contains a nonzero fixed vector (Galois descent for L₂/F).
   - A fixed vector has δ = ιγ, and γ ≠ 0 because otherwise δ = 0 too.
3. **(ii) γ₀ ≠ 0.** If γ₀ = 0 (hence δ₀ = 0), the coefficients (γ_{e+1}, δ_{e+1}) give a relation of degree a₂−1 for W² = {w²}.
   - But M(W²) at degree d is the entrywise square of M(W) at degree d. Entrywise squaring is a field embedding and preserves rank, so W² has the same minimal degree a₂. Contradiction.
4. **(iii) Pair-relation module over L₂.** HFD §1 transfers verbatim. Only right division in L₂{τ} is needed (leading coefficient a/b^{2^k} always exists), so L₂{τ} is left Euclidean.
   - The relation module is free of rank 2 and has a weak Popov basis with pivots in distinct columns. So the predictable-degree property holds, and the degree-≤L relations have dimension (L+1−d₁)₊ + (L+1−d₂)₊.
   - Moore over L₂ gives d₁+d₂ = ρ′.
   - At d₁ = a₂ ≤ ρ′/2−2 this count is 1 for L = a₂. ∎

**Numerical range.** For WG's family B1 of weight u = R/4 (and |N| = v > Q²/2 = KR²/2):
- 2u·2^{a+1}Q = R2^aQ = 2^{a−ρ/2}Q² ≤ Q²/4 < v whenever **a ≤ ρ/2−2**.
- That is EXACTLY the structured range a ≤ a* of EBR, so the hypothesis of RB holds in every open even cell.
- For weight K the condition is K·2^{a+3} < Q, i.e. a ≤ g−ρ/2−4. Given a ≤ a* = ρ−⌈g/2⌉, this holds for every g ≥ ρ+3 (check: at g = ρ+3, a* = ρ/2−2 ≤ ρ/2−1).

## 5. Proposition RD (descent in the rational branch) [COND on G2: RR for the descended square-root families, and HFA1's terminal BWG step]
**Setting.** Keep RB's setting, and suppose RR applies to W and to every square-root descendant (gap G2 of HFD §3, the same input PHFG and HFA1 use). Let D_X = ∂/∂X on L₂, and W₀ := ker(D_X|W) = W ∩ F_q[X²].

**Statement.**
- (a) γ₀w′ = ℓ(w) := Σ_e D_X(γ_e)w^{2^e} + D_X(ιγ_e)(ιw)^{2^e} for all w ∈ W.
- (b) RR gives dim W₀ ≥ ρ′−2. Moreover, either W₀ = W, or W₀ has bivariate defect ≤ a₂−1.
- (c) Iterating (√W₀ ⊂ F_q[X] has degree ≤ u/2 and the same bivariate defect as W₀) and losing ≤ 2 dimensions per defect drop, we reach a bivariate-defect-0 family of dimension ≥ ρ′−2a₂ ≥ 4.
- (d) Bivariate defect 0 means (cw)/(cw₁) ∈ F ∩ F_q(X) = F_Q for all w, so the family is ηU₀ (η ∈ F_q[X], U₀ ⊂ F_Q). This is exactly HFA1's rational (H) structure, and RR then forces η′ = 0 at each further step (rank of u ↦ η′u is dim U₀ ≥ 4). The descent continues as in HFA1 to the BWG contradiction.

*Proof.*
1. **(a)** Apply D_X to the real relation. D_X kills (ιw)^{2^e} and w^{2^e} for e ≥ 1, because these are functions of Y or squares.
2. **(b)** Suppose W₀ ≠ W. Then ℓ is nonzero on X_W := span_{L₂} x(W), while (γ,ιγ) vanishes there. So ℓ and (γ,ιγ) are two independent relations of degree ≤ a₂ on W₀.
   - With ρ″ = dim W₀ ≥ ρ′−2 and d₂ ≥ ρ″/2 ≥ a₂+1, the count (a₂+1−d₁)₊ + (a₂+1−d₂)₊ ≥ 2 forces d₁ ≤ a₂−1.
   - The minimal relation is again ι-real, by RB(ii) applied to W₀.
3. **(c)** The inequality a_i ≤ ρ_i/2−2 is preserved: ρ drops by ≤ 2 when a drops by ≥ 1.
4. **(d)** w/w₁ is ι-fixed and lies in F_q(X). ι-fixed means it equals its own (Q)-twist in Y, so it is constant and lies in F_Q. ∎

**Status.** RB + RD remove G1 **in the rational branch** (all roots of the WG family rational). This is CONDITIONAL only on G2, which PHFG already needed. The bivariate real relation replaces the false "C(W) ⊂ F_Q constants".

## 6. What G1 now is: the orbit bound G1′ [OPEN; H]
By TX, generic real type cannot be the target. By RB/RD, the rational branch is handled (mod G2). WG kills components with 1 < e_w < (4/3)2^{ρ/2} − 1 (u = R/4). So:

**G1′ (orbit bound).** In an open even cell with a(V_α) ≤ a* at every nonfocus, every root of the WG family has Galois orbit e_w < (4/3)2^{ρ/2} − 1.

Then WG gives e_w = 1, and RB+RD (mod G2) excludes the family. **G1 ⇐ G1′ + G2.**

**Why counting does not give G1′ [H].**
- **Base-curve counting fails.**
  - The generic relation's coefficients have degree ~K·Q·2^{a+1} (Lemma G). TX shows that degree ~Q is intrinsic (coefficients involve X^Q).
  - So every conjugated identity over the α-line has degree ≥ Q·deg > v.
  - TSZ needs bidegree < Q/4, and only the ROOTS have that (degree u). The coefficients do not.
- **Counting on the cover fails too.** On the Galois closure X_W the minors have low bidegree on X_W × X_W^{(Q)}. But the twisted rational points lie on the Frobenius graph, and counting on a curve of genus ≳ |G|u gives nothing.
- **Twisted half-field families.** For the natural families A(ηU₀) with η Kummer, or C^{−1}(ηU₀), one has e_w ≤ 2^a·e with e | 2^t−1. **No family with generic defect a ≥ 1 and large orbits is known.** Constructing one, or proving G1′ from the arc's B1 structure (STT), is the next step.
- **A possible route.** Lang-type equation C·A = D·A^{(Q)} (deg A ≤ a).
  - Pointwise it has a nonzero F_Q-line of solutions A_α. It comes from a real 2a+1 vs 2a+2 dimension count and is not checked in this note.
  - Its extreme coefficients satisfy Kummer equations a_a^{(Q−1)2^a} = c_a/d_a and a₀^{Q−1} = c₀/d₀.
  - If a generic solution with small orbits exists, then R_P ⊇ A(ηF_Q), and W ∩ A(ηF_Q) has dim ≥ ρ−a with e_w ≤ e·(orbit of A).
  - [H] only.

## 7. Owner self-check (NOT an independent audit)
- **TX identity Γ(τ+α) = Δ(τ+ᾱ):** τ-coefficients α²+α^{Q+1}+α^{2Q} on both sides; constants α^{Q+1}(α+ᾱ) on both sides. Rechecked by hand and confirmed numerically (C2: 0 failures at m = 16, 20, 24).
- **TSZ:** total degree of h is ≤ deg_X + deg_Y. The F_Q-splitting h = h₁ + ωh₂ is valid because the values h_i(x,y) lie in F_Q at F_Q-points.
- **RB(i):** the minors' degrees are deg_X ≤ u·Σ_{e≤a}2^e. The ι-columns have the same Y-degree.
- **RB(iii):** weak Popov over the non-perfect L₂ uses only right division. Windows start at 0, so no φ^{−1} is needed (unlike HFD, which used σ^{−1} on F_Q).
- **RD(b):** the two relations are independent as vectors in L₂^{2a₂+2} because they differ on x(W). D_X(ιγ_e) is well defined, since ιγ_e ∈ L₂.
- **Points to audit.**
  - (1) TSZ constants versus the exact v for each cell.
  - (2) Whether the WG family B1's radical at α has defect ≤ a(V_α). This holds if it is a Frobenius twist of a subspace of V_α. [A] needed from Codex: what B1 is.
  - (3) RD's reliance on RR for subspaces of descendants (G2).
  - (4) In RB(iii), whether "dimension ρ′ at α ∈ N" implies F₂-independence over L₂. It does: an F₂-dependence over L₂ would specialise to one.

Script: `toycheck.py` (own GF(2^m) code; reads no extracted files) with `toycheck.log`.
