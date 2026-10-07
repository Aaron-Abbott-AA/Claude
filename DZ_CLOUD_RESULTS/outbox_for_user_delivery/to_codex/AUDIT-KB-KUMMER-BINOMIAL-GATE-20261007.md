# AUDIT — KB-KUMMER-BINOMIAL-GATE-NOTE-20261007.md (independent referee, cloud session, 7 Oct 2026, 20:59–21:08Z)

Referee: a fresh, isolated, adversarial subagent for the DZ line (project "Wan's numbers of PPs"). It had no contact with the owner session or with Codex, and it read no files outside the DZ scope. The files read are listed in §6.

**Note audited:** `src/KB-KUMMER-BINOMIAL-GATE-NOTE-20261007.md`, sha256 `d6b60aa1d52119e7b4247072c47bd94f5deab0a7b8639363b9da4575b6f124d7`. The copy in `claude_archive/` is byte-identical (checked with `cmp`).

**Owner scripts:** none. The note cites no script, so nothing was rerun from `claude_archive/scripts/`.

**Labels** follow the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN] open problem. Anything the referee proves is marked "[P, referee]".

## 0. Verdict: **PASS-with-fixes**

**The mathematics of Proposition KB (i)–(v) is correct** under its stated inputs:
- GLS₁, (B1a⁺) and (B1b);
- PTH v2.2 MI, ML and GO(a)–(c), together with GO's input step;
- GX v2.1's failure pattern.

Every step was checked by hand:
- **(i), the (GT)-failure chain:** t > ρ/2, then t = dim U′, then t = m/4, then the cell is gate-failing.
- **(ii), the factorisation:** A = B·a₀, B ∈ L{τ}, g(η) = ηχ(g), h ∈ L.
- **(iii), integrality:** Moore left inverse over F_s, then η integral, then h ∈ F_q[X].
- **(iv), values on N.**
- **(v), the Kummer orbit.**

The arithmetic was checked for every even ρ ≤ 200 (`kb_arith`), and the linear algebra was checked in finite-field toys (`kb_ff`). There were 0 violations.

**Two items must change before the note goes to Codex. Neither breaks Proposition KB.**
- **FIX-1 (wrong routing of the deg B = 0 inner-resonance subcase).**
  - At g = 3ρ/2 we have ρ | m/2. So F_{2^ρ} ⊂ F_Q, and W = ηF_{2^ρ} ⊂ ηF_Q with w^Q = y·w for y = η^{Q−1} ∈ L.
  - The "globally binomial (E)" subcase is therefore **also a global half-field (H) family**: there is a degree-0 generic relation, and a(V_α) = 0 at every nonfocus [P, referee].
  - The project ledger records the global (H) branch as closed by IHF/HFA/HFA3, including the c = 1 cells at g = 3ρ/2 [A].
  - So the subcase should be routed through HFA, and the Codex question should be about HFA's scope, not EWF1's. As written, §1, §3 and §4(a) list it as open pending EWF1.
- **FIX-2 (a false "arithmetic P" claim in §2, and a missed strengthening).**
  - "This is the same threshold as WG" is wrong.
  - The Kummer structure that KB itself proves gives a sharper Weil count:
    - the genus is at most (e−1)(eu−1)/2;
    - every α ∈ N is totally split;
    - there are v > q/2 such places.
  - That count **excludes T ≤ e ≤ 2^{ρ/2+1} − 3** [P, referee, mod the same inputs]. The threshold is about 1.5·T, not T.
  - It removes admissible orders e in 37 of the 88 gate-failing cells with ρ ≤ 40, but never all of them. So the [H] conclusion "counting alone does not exclude KB" survives (`kb_weil`).

**Owner revision is required.** It consists of restatements plus one optional added lemma; no proof needs to be rewritten.

**FIX count: 2 substantive, 9 minor.**

## 1. Item table

| # | Item | Claimed label | Referee finding | Status |
|---|---|---|---|---|
| 1 | Title | [COND GLS₁, (B1a⁺), (B1b)] | The structural part is correct. The clause "counting alone does not exclude it" is [H] and should be labelled as such. | m1 |
| 2 | §0 inputs: PTH v2.2 (MI, ML, GO (a)–(c), setting), GX v2.1 failure pattern | [A] | They match PTH v2.2 §2, §4, §4A and GX v2.1 §3. They are called "reviewed", but they are DZ-internal audited notes, not Codex/PRIMARY-reviewed results. | m8 |
| 3 | §0 (GLS₁) paraphrase | — | "Nonzero" is missing. KB must use the **minimal-degree** solution, as GO does: g(A) = Aχ(g) holds only for that one. Only deg A ≤ m/4 − 1 is used, in (iii). | m2 |
| 4 | §0 standing setting | — | Even ρ, ρ+3 ≤ g ≤ 2ρ, a(V_α) ≤ a* at every nonfocus, a* ≥ 1, and GO's input step (EBR Lemma G [A], v > Q²/2) are implicit only. | m6 |
| 5 | KB(i): t > ρ/2 ⟹ t = dim U′ ∈ [ρ−a₂, ρ], t \| m/2 ⟹ t = m/4, cell gate-failing | [P] | Correct. The chain is 2^t − 1 ≥ \|χ(G)\| ≥ T > 2^{ρ/2} − 1, then 0 < ρ − a₂ ≤ dim U′ ≤ ρ < 2t, then [ρ−a₂, ρ] ⊂ [⌈g/2⌉, ρ], then GX's pattern. Checked for all 9898 band cells with ρ ≤ 200 and every a₂ ≤ a*: the candidate set is ∅ or {m/4}, and is never outside a gate-failing cell. | PASS |
| 6 | KB(i): "U′ = λF_s, F₂(χ(G)) = F_s" | [P] | True, but the proof only asserts it. One line is needed: a proper subfield F_{2^r}, r \| m/4, has r ≤ m/8 ≤ ρ/2, so 2^r − 1 < T (checked for ρ ≤ 200). | m3 |
| 7 | KB(i): implicit consequence | — | dim W′ = m/4 ≥ ρ − a₂ forces **a₂ ≥ (3ρ−2g)/4**, which is > 0 whenever g < 3ρ/2. This is useful, and it is not stated. | m6 |
| 8 | KB(ii): b_i := a_i/a₀^{2^i} G-fixed, B ∈ L{τ}, b₀ = 1, deg B = deg A, A(x) = B(a₀x), W′ = B(ηF_s), g(η) = ηχ(g), h ∈ L | [P] | Correct: (Aζ)_i = a_iζ^{2^i}, (L^sep)^G = L, λ ∈ F_Q is G-fixed, and χ(g)^{s−1} = 1. Also η^{Q−1} = y = h^{s+1}. Verified in toys (`kb_ff` F1: 40 trials per seed, 2 seeds). | PASS; m5 |
| 9 | KB(iii): Moore left inverse with F_s entries ⟹ η ∈ F_s·W′; integral, pole order ≤ u; h ∈ F_q[X], deg h ≤ N′u | [P] | Correct. d+1 ≤ a₂+1 ≤ ρ−a₂ ≤ m/4 holds because 2a₂+1 ≤ ρ. The Moore block is invertible, its inverse has F_s entries, and X₀ = η. F_q[X] is integrally closed. The toys confirm it. "d" is undefined in the note. Sharper statement: k := η^e ∈ F_q[X] with deg k ≤ eu. | PASS; m5, m9 |
| 10 | KB(iv): η(P) ∈ F_q for P \| α ∈ N; h(α) ∈ {0} ∪ (F_q^*)^{N′} | [P] | Correct. "Totally split" uses deg_T B1 = 2^ρ (monic, (B1a⁺)) together with ρ-dimensional W(α) ⊂ F_q, so B1(α,·) is separable and the place is unramified. This should be said. (F_q^*)^{s−1} = ker N_{F_q/F_s} was verified exhaustively for m = 8, 16. | PASS; m4 |
| 11 | KB(v): orbit ηχ(G) of size e, T ≤ e \| N′, cyclic Kummer of degree e, totally split at α ∈ N "except possibly zeros of h" | [P] | Correct. η^e ∈ L, and μ_e ⊂ F_s ⊂ L. The exception is **superfluous**: η lies in the splitting field of B1, which is totally split at every α ∈ N. The Frobenius sentence should say that the decomposition group is trivial (unramified, residue degree 1). | PASS; m4 |
| 12 | §1 subcase g = 3ρ/2: W′ = W = B(ηF_{2^ρ}); B = 1 ⟹ globally binomial (E); EWF1 scope pending | [A-pending] | W′ = W is correct (m/4 = ρ). With B = 1 the family is also **global (H)**: ρ \| m/2, w^Q = yw, and a ≡ 0. That is HFA's hypothesis, which is recorded as closed [A]. Routing it through EWF1 alone is incomplete. Also "η(α)" should be η(P): V_α is a Frobenius twist of η(P)F_{2^ρ}, with η(P) ≠ 0. | **FIX-1**; m7 |
| 13 | §2 Weil/Kummer bullet: r ≤ eu, needs r ≳ Q/2, consistent iff e ≳ 2^{ρ/2+1}, N′ ≥ 2^{ρ/2+2} | [H; arithmetic P] | The arithmetic is right: r ≤ eu, Q/(2u) = 2^{ρ/2+1}, N′ ≥ 2^{ρ/2+2}. **"Same threshold as WG" is false**: the Kummer count excludes e ≤ 2^{ρ/2+1} − 3, while WG gives T ≈ (4/3)2^{ρ/2}. The conclusion survives because e = N′ is always admissible and escapes. | **FIX-2** |
| 14 | §2 norm/Schwartz–Zippel: deg h < s/8 needed | [H] | The arithmetic 4·deg h·s³ < s⁴/2 ⟺ deg h < s/8 is correct (`kb_weil`). | OK |
| 15 | §2 parallel with HFA's inner resonance [A, NDX §4(a) correction] | [A] | The parallel is right. The correction is recorded in IDEAS §321 and packet EB, not in NDX itself. | m8 |
| 16 | §3 updated picture | [COND] | The dichotomy (GT) / ¬(GT) is exhaustive and the GX branch is cited correctly. The OPEN list must be updated per FIX-1. | FIX-1 |
| 17 | §4 Codex questions | — | (a) should ask about HFA/HFA3 scope at g = 3ρ/2, where the B = 1 family is global (H), and keep EWF1 only as an alternative. (b) is fine. | FIX-1 |
| 18 | §5 self-check, audit points (1)–(3) | — | (1) holds, since [ρ−a₂, ρ] ⊂ [ρ−a*, ρ]. (2) holds, with the caveat about separability (m4). (3) §2 is [H], with FIX-2. | OK |

## 2. Detailed audit

**KB(i).**
- GO(c) gives |χ(G)| = orbit size, and |χ(G)| divides 2^t − 1, where F_{2^t} = {z ∈ F_Q : zU′ ⊆ U′} is a field.
- (GT) fails, so 2^t − 1 ≥ T = (4/3)2^{ρ/2} − 1 > 2^{ρ/2} − 1. Hence t > ρ/2.
- U′ is an F_{2^t}-space with 0 < ρ − a₂ ≤ dim U′ = dim W′ ≤ dim W = ρ < 2t. (The lower bound is GO(b), and MI gives dim U′ = dim W′.) So dim U′ = t, and t | m/2.
- Since a₂ ≤ a* = ρ − ⌈g/2⌉, t is a divisor of N = m/2 = g + ρ/2 in [⌈g/2⌉, ρ].
- GX v2.1's pattern (re-proved here: N > ρ, and N/3 < ⌈g/2⌉ because g > ρ) forces t = N/2 = m/4. Then g ≡ ρ/2 (mod 2) because m/4 ∈ ℤ, and g ≤ 3ρ/2 because m/4 ≤ ρ.
- **F₂(χ(G)) = F_s.** If χ(G) ⊂ F_{2^r} with r | m/4 and r < m/4, then r ≤ m/8 ≤ ρ/2, so |χ(G)| ≤ 2^{ρ/2} − 1 < T, a contradiction (m3).
- **Unstated consequence.** m/4 = dim W′ ≥ ρ − a₂, i.e. a₂ ≥ (3ρ−2g)/4. For g < 3ρ/2 this is a positive lower bound on the generic relation degree; for example (10,13) needs a₂ ≥ 1, and (18,21) needs a₂ ≥ 3 (m6).
- **[C, referee] `kb_arith`.** Even ρ ∈ [6, 200], all 9898 band cells, every a₂ ∈ [0, a*]:
  - the candidate t-set is ∅ or {m/4};
  - it is nonempty exactly when m/4 ∈ [ρ−a₂, ρ], always in a gate-failing cell;
  - subfield bound, Moore bound d+1 ≤ m/4, T ≤ N′ and N′ ≥ 2^{ρ/2+2} all hold;
  - 0 violations;
  - for ρ ∈ [10, 40], a* ≥ 1 and non-NWF cells there are 88 gate-failing cells, matching GX v2.1.

**KB(ii).**
- **Which solution.** GO(a)'s identity g(A) = Aχ(g) holds for the **minimal-degree** solution, which is unique up to F_Q^* by ML. A non-minimal solution of degree ≤ a₂ need not satisfy it. The note must name A as the minimal solution; its degree is ≤ a₂ under GLS₁ (m2).
- **The steps.**
  - Coefficientwise, g(a_i) = a_iχ(g)^{2^i}, so b_i is G-fixed and lies in (L^sep)^G = L.
  - b_d ≠ 0, so deg B = deg A.
  - A(λt) = B(ηt), η = a₀λ, and g(η) = ηχ(g), because λ ∈ F_Q ⊂ L.
  - h = η^{s−1} is fixed, since χ(g) ∈ F_s^*.
  - y = a₀^{Q−1} = η^{Q−1} = h^{s+1}.
- **[C, referee] `kb_ff` F1.** Host F_{2^32} ⊃ F_q = F_{2^16} ⊃ F_Q ⊃ F_s = F_16, with d ∈ {0,…,3}. In 40 trials per seed and 2 seeds:
  - A(λt) = B(ηt) on F_s;
  - the Moore rank is d+1, and its left inverse has F_s entries;
  - X_i = b_iη^{2^i} and X₀ = η;
  - the simulated twist a_i ↦ a_iχ^{2^i} preserves W′ and sends η ↦ ηχ with h fixed;
  - y = h^{s+1};
  - 0 failures.

**KB(iii).**
- **The bound.** d+1 ≤ m/4: d ≤ a₂, 2a₂+1 ≤ ρ−3, and m/4 ≥ ρ − a₂.
- **Recovering η.** The (d+1)×(d+1) Moore block on t₁,…,t_{d+1} is invertible, and its inverse has F_s entries. So η = X₀ is an F_s-combination of w₁,…,w_{d+1} ∈ W′ ⊂ roots of B1.
- **Integrality.** Integrality and the pole bound v_P(·) ≥ −u·e(P|∞) are preserved by F_q-linear combinations. h is integral and lies in L, so h ∈ F_q[X], with deg h = −v_∞(h) ≤ N′u.
- **Sharper statement (m5).** Since η^e is G-fixed, k := η^e ∈ F_q[X] with deg k ≤ eu. §2 uses exactly this sharper bound, but it is never stated.

**KB(iv)/(v).**
- **Why α splits.** (B1b) gives W(α) of dimension ρ inside F_q, and (B1a⁺) makes B1 monic of T-degree 2^ρ. So B1(α,·) has 2^ρ distinct roots in F_q. The splitting field of B1 is therefore unramified at α with residue degree 1, i.e. **totally split**.
- **Values.** η lies in that field and is integral, so η(P) ∈ F_q and h(α) = η(P)^{s−1}.
- **Norm.** (F_q^*)^{s−1} = ker N_{F_q/F_s}, as the subgroup of index s−1 in a cyclic group. `kb_ff` F2 checked this exhaustively for m = 8 and 16.
- **The exception is superfluous.** L(η) ⊂ Split(B1) is totally split at **every** α ∈ N, including zeros of k. At such zeros e | v_α(k). (m4)
- **Kummer structure.** L(η)/L is Galois and cyclic of degree e = |ηχ(G)|, with η^e ∈ L, and μ_e ⊂ F_s ⊂ L.

**§1 subcase g = 3ρ/2 (FIX-1).**
- **W′ = W.** Here m/4 = ρ = dim W.
- **With B = 1 the family is global (H).**
  - W = ηF_{2^ρ}, and ρ | m/2 = 2ρ. So F_{2^ρ} ⊂ F_Q, and for w = ηt, w^Q = η^Qt = y·w with y ∈ L.
  - So the generic radical satisfies HFA's hypothesis "Rem ≡ cX" (a degree-0 generic relation, a₂ = 0).
  - Pointwise, V_α is a Frobenius twist of η(P)F_{2^ρ} ⊂ η(P)F_Q, so a(V_α) = 0 at every nonfocus.
  - η(P) ≠ 0: when B = 1, reduction W → W(α) is injective and w = ηt.
  - [P, referee]; `kb_ff` F3 checked the inclusion numerically at (ρ, g, m) = (6, 9, 24).
- **What the ledger records.**
  - STATE §3y: "IHF/HFA: the global half-field branch is closed".
  - IDEAS §321: the inner-resonance correction e | 2^{gcd(ρ, g+ρ/2)} − 1, followed by "IHF/HFA … closed global (H) in the near-diagonal".
  - STATE §3z (C1): "with HFA3, every c = 1 cell closes", listing (10,15), (14,21) and (24,36). These are all g = 3ρ/2 cells, where C1's (E) alternative is likewise inside (H).
- **So the subcase is closed [A] modulo HFA's stated scope**, independently of EWF1. EWF1 ("globally binomial resonant g ≥ ρ+2", IDEAS §319) remains a second possible route.
- **General B = 1.** In any gate-failing cell, B = 1 gives W′ = ηF_s ⊂ ηF_Q, a partial half-field sub-radical of dimension m/4 ≥ ρ − a₂. That is HFD §3's "narrow partial-half-field sub-case". This is worth recording.

**§2 (FIX-2).**
- **The count.** For the Kummer curve y^e = k:
  - e is odd, so the cover is tame;
  - r₀ ≤ deg k ≤ eu;
  - Riemann–Hurwitz gives 2·genus ≤ (r₀−1)(e−1).
- **Weil.** The v > q/2 places of N are totally split (KB(v)), and this forces the constant field to be F_q. So e·v ≤ q + 1 + (eu−1)(e−1)Q.
- **Contradiction range.** With √q = 4u·2^{ρ/2}, this is contradictory exactly for odd e in [3, 2^{ρ/2+1} − 3]. That was computed exactly in all 88 gate-failing cells with ρ ≤ 40; the ratio of the largest excluded e to T is 1.46–1.50.
- **Comparison with WG.** WG's T = (4/3)2^{ρ/2} − 1 comes from the generic component bound √q ≤ 3u(e+1). The Kummer genus is about half as large, so **the thresholds differ**.
- **Effect.**
  - In 37 of 88 cells some admissible e ≥ T (e | s−1 and e generating F_s) falls in the excluded window.
  - In no cell are all admissible e excluded: e = N′ always escapes.
  - So "counting alone does not exclude KB" stands as [H].
  - But KB(v) can be upgraded to **e ≥ 2^{ρ/2+1} − 1** [P, referee, mod GLS₁, (B1a⁺), (B1b), EBR Lemma G [A]].
- **Other §2 arithmetic.** r ≤ eu, the requirement r ≳ Q/2, N′ ≥ 2^{ρ/2+2}, and the Schwartz–Zippel bound deg h < s/8 are all correct.

**Counterexample search.** No counterexample to any [P] clause was found.
- The only clause that is literally overstated is "(except possibly zeros of h)", and it is harmless.
- "That is exactly the family treated by … MH/BC/EWF1" is incomplete (FIX-1), not false.

## 3. FIX items (substantive first)

**FIX-1 (substantive) — reroute the deg B = 0 inner-resonance subcase (§1 subcase, §3 OPEN, §4(a)).**
- **Add [P, referee].** At g = 3ρ/2 with B = 1:
  - W = ηF_{2^ρ} ⊂ ηF_Q, with w^Q = η^{Q−1}w and η^{Q−1} = y ∈ L;
  - this gives a degree-0 generic relation (a₂ = 0), and V_α ⊂ μ_αF_Q at every nonfocus;
  - it is the global (H) family under HFA's hypothesis.
- **Cite [A].** STATE §3y (IHF/HFA closed the global half-field branch), IDEAS §321 (inner-resonance correction, then the (H) closure in the near-diagonal), and STATE §3z (C1 + HFA3 close (10,15), (14,21), (24,36)).
- **Change the status.** "Open pending EWF1" becomes "closed by HFA [A], pending confirmation that HFA3's statement covers g = 3ρ/2". EWF1 can be kept as an alternative.
- **Rephrase Codex question §4(a)** accordingly.
- **Record the general case.** Any B = 1 is the partial-half-field sub-case of HFD §3.

**FIX-2 (substantive) — correct §2's "same threshold as WG" and record the Kummer–Weil bound.**
- Replace the sentence with: "the Kummer cover (genus ≤ (e−1)(eu−1)/2, totally split at v > q/2 places) excludes 3 ≤ e ≤ 2^{ρ/2+1} − 3, which is stronger than WG's T ≈ (4/3)2^{ρ/2}. It removes some admissible e in 37 of the 88 cells with ρ ≤ 40, but e = N′ always survives."
- Optionally add this as KB(vi), "e ≥ 2^{ρ/2+1} − 1" [P, referee], under the same inputs plus EBR Lemma G [A].
- The §2 header "[H; arithmetic P]" stays true only after this correction.

## 4. Minor notes
- **m1.** Title: label "counting alone does not exclude it" as [H].
- **m2.** §0 (GLS₁):
  - write "a nonzero solution";
  - in KB, A must be the **minimal-degree** solution (unique up to F_Q^*, ML), as in GO(a);
  - only deg A ≤ m/4 − 1 is used, in (iii), so GLS₀ plus that bound would suffice.
- **m3.** KB(i): add the one-line proof that χ(G) lies in no proper subfield of F_s (2^{m/8} − 1 ≤ 2^{ρ/2} − 1 < T).
- **m4.** KB(iv)/(v):
  - say that (B1a⁺) monic of T-degree 2^ρ plus (B1b) makes B1(α,·) separable, so the place is unramified;
  - "Frobenius fixes the w_j" should read "the decomposition group at P is trivial";
  - delete "(except possibly zeros of h)", which is superfluous; at such α, e | v_α(η^e).
- **m5.** KB(iii):
  - state k := η^e ∈ F_q[X] with deg k ≤ eu; §2 uses it;
  - KB(ii): note y = η^{Q−1} = h^{s+1}.
- **m6.** State the standing setting: even ρ, ρ+3 ≤ g ≤ 2ρ, a(V_α) ≤ a* at every nonfocus, a* ≥ 1, and GO's input step (EBR Lemma G [A]). Add the forced bound a₂ ≥ (3ρ−2g)/4, which follows from dim W′ = m/4 ≥ ρ − a₂.
- **m7.** §1 subcase:
  - write η(P), not "η(α)";
  - V_α is a Frobenius twist of η(P)F_{2^ρ};
  - note that η(P) ≠ 0 there.
- **m8.** Citations:
  - PTH v2.2 and GX v2.1 are DZ-internal audited notes ("audited"), not "reviewed" in the Codex/PRIMARY sense;
  - the inner-resonance correction is in IDEAS §321 and packet EB (it corrects NDX §4(a)).
- **m9.** KB(iii): define d := deg B = deg A.

## 5. `checks/` (referee code; `nice -n 19 python3 -I`; galois 0.4.11, sympy 1.14.0; each run took under 1 min)
- **`kb_arith.py` / `kb_arith.log`.** KB(i) chain, subfield bound, Moore bound, N′ bound and the forced lower bound on a₂.
  - Even ρ ∈ [6, 200]: 9898 cells, 2450 admitting KB, 0 violations.
  - There are 88 gate-failing cells for ρ ≤ 40.
- **`kb_ff.py` / `kb_ff.log` (seed 20261007) and `kb_ff_seed7.log` (seed 7).** Finite-field toys:
  - F1: (ii)/(iii);
  - F2: power subgroup = norm kernel;
  - F3: inner-resonance (H) inclusion;
  - 0 failures.
  - The logs are identical because the output does not print the seed.
- **`kb_weil.py` / `kb_weil.log`.** Exact Kummer–Weil exclusion window for the 88 cells (ρ ≤ 40), compared with T and 2^{ρ/2+1}. Also lists the admissible orders and the ones that escape, and checks the Schwartz–Zippel arithmetic.
- **`checks_SHA256SUMS.txt`** (sha256 `809fa4472f3043b1d8fa82b576cc9102abbddd3f5605cc957e980d0be85cfd28`):
  - `65b2f61c758952672abb9c83555d841a2a22815c1dfe7156eba2cd8f217eeebb  kb_arith.py`
  - `7fe6115f336bcd41f85b61d89f1d0b547113276fb9ed8bfec31435e9ed3b933e  kb_arith.log`
  - `dbb2a31223dbad40fec7b98acffbb343fabff645cba4ae5db175ab212472ddf2  kb_ff.py`
  - `a879f4e8de5aa14e8d4c609770648be2cf290421fb0bd52fd1d0970695392b6a  kb_ff.log`
  - `a879f4e8de5aa14e8d4c609770648be2cf290421fb0bd52fd1d0970695392b6a  kb_ff_seed7.log`
  - `55b8f4c2e0980be89a376e1068675e8216f93a5a343919ec1545a6bafa972570  kb_weil.py`
  - `fed7414633530c7f7227d16a043dc16aec0610e8018c74318636e72a156749ee  kb_weil.log`
- The checks live in `referee_KB/checks/`. Per the instructions, nothing other than this audit file was written to DZ_CLOUD_RESULTS.

## 6. Files read
- **The note under audit:** `referee_KB/src/KB-KUMMER-BINOMIAL-GATE-NOTE-20261007.md`. The archive copy was compared with `cmp` only.
- **Handoff** (`work/DZ-CLOUD-HANDOFF/`):
  - `START-HERE-CLOUD-SESSION.md`;
  - `notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`, lines 80–140 (§2b end, §3 PHFG and its audit gaps);
  - `notes/NDX-LTPRIME-NEAR-DIAGONAL-NOTE-20261007.md`, lines 85–110 (§4(a));
  - `packets/EB_20261007T1201Z.md`, lines 10–30;
  - `docs/IDEAS-PROJECT-TRIM.md`, lines 265–330 (§319–§322);
  - `docs/STATE-PROJECT-TRIM.md`, lines 30–80 (§4b, §3z, §3y);
  - grep hits for EWF1/HFA/WG in `notes/`, `docs/` and `packets/`.
- **Archive** (`/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive/`):
  - `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md` (full);
  - `GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.1.md` (full);
  - `scripts/gxcells.py` and `.log` (read only, not run);
  - `AUDIT-GX-GLOBAL-TWIST-EXCLUSION-20261007.md`, lines 1–60 (for the format);
  - grep of RBL v2.1 and TCR v2.1 for the WG threshold T.
- **Not read:** HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, uploads, other scratchpads. Git was not used.
