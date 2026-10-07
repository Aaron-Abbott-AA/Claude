# AUDIT — RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md (independent referee, 7 Oct 2026, 18:29–19:05Z)

Referee: fresh, independent agent (DZ line, cloud container, isolated directory `dz_isolated/referee_RBL`). I have no stake in the note. The owner script was treated as untrusted. I copied it to `checks/owner_copy/` and ran it only with `python3 -I`. All other checks use my own code.

Note audited: `src/note/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md`, sha256 `c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe`.
Owner script: `toycheck.py` (`aeff51cd…a9b`). Owner log: `toycheck.log` (`613fa8c0…dd`).

## Verdict: **PASS-with-fixes**

The note's new mathematics is correct:
- the toy family TX;
- the twisted Schwartz–Zippel lemma TSZ;
- the bivariate rational-branch lift RB (i)–(iii);
- the derivative identity RD(a) and the dimension/defect trade-off RD(b).

One step of Proposition RD is false as stated. RD(c) claims the descent "reaches a bivariate-defect-0 family". That does not follow from the stated inputs, and there is an abstract counterexample (FIX-1).

The status lines also overstate how conditional the result is. "CONDITIONAL only on G2" and "G1 ⇐ G1′ + G2" omit at least three further inputs: the identification of B1, a terminal BWG step valid at positive defect, and G4 (FIX-2, FIX-3).

These are restatements. None destroys a result, but they change the headline claims. **The note needs owner revision before it is sent to Codex.**

## Item table

| # | Item | Label in note | Referee result |
|---|---|---|---|
| 1 | Lemma AR (real type at rational points) | [P] | PASS. The "Consequence" paragraph is interpretive and should be [H] (FIX-8). |
| 2 | TX.1 pointwise identity and C_α(V_α) ⊂ F_Q | [P; C] | PASS. Wording fix: the "every α" claim needs degenerate α excluded, and α ∈ F_Q gives defect 0 (FIX-4). |
| 3 | TX.2 generic relation, real type fails | [P] | PASS. Add the one-line proof that the generic defect is exactly 1 (FIX-4). |
| 4 | TX.3 C(W) ⊄ ηF_Q | [P] | PASS |
| 5 | TX.4 rational, RR violated (rank ρ) | [P] | PASS |
| 6 | TX "Meaning" (G1 not provable from PHFG step-1 hypotheses) | [P] | PASS, relative to the hypotheses listed |
| 7 | [C] toycheck table | [C] | PASS. Reproduced byte for byte with seeds 1, 2, 3. Control wording needs a fix (FIX-9). |
| 8 | Lemma TSZ | [P] | PASS (hand proof, plus [C] exhaustive at q = 16 and sampled at q = 64, 256) |
| 9 | Theorem RB(i) | [P] | PASS |
| 10 | RB(ii) ι-real minimal relation, γ₀ ≠ 0 | [P] | PASS |
| 11 | RB(iii) module over L₂, line at degree a₂ | [P] | PASS. Wording of left/right division (FIX-6). Relation counts confirmed [C]. |
| 12 | RB "Numerical range" arithmetic | [P] | Arithmetic PASS (39,800 cells). Applying it to "every open even cell" is conditional on the identification of B1 (FIX-2). "EXACTLY" should read "contains" (FIX-7). |
| 13 | RD(a) derivative identity | [P] | PASS |
| 14 | RD(b) W₀ ≠ W ⟹ defect drop | [COND] | PASS (given RR), apart from the garbled "x(W)" wording (FIX-5) |
| 15 | RD(c) "reach a bivariate-defect-0 family" | [COND] | **FAIL as stated.** The correct invariant is dim ≥ ρ′−2a₂ throughout the descent (FIX-1). |
| 16 | RD(d) defect 0 ⟹ ηU₀, then η′ = 0 | [COND] | PASS, if defect 0 is ever reached |
| 17 | §5 Status "CONDITIONAL only on G2" | — | **Overclaim** (FIX-2) |
| 18 | §6 "G1 ⇐ G1′ + G2", WG threshold (4/3)2^{ρ/2}−1 | [OPEN; H] | Arithmetic PASS. The implication omits conditions (FIX-3). |
| 19 | §6 "why counting fails", Lang-type route | [H] | Heuristic, labelled correctly. The Kummer equations for the extreme coefficients check out. |
| 20 | Citations [A]: HFD §1, EBR Lemma G, PHFG/G1–G4, WG and RR quotes | [A] | Match the handoff texts. The WG/RR quotes are second-hand readings (FIX-10). |

## Detailed audit

### §1 Lemma AR
Specialising a primitive generic relation at α, where it does not vanish, gives a nonzero relation of degree ≤ a on V_α. At a(V_α) = a < ρ/2, HFD §1 makes the relations of degree ≤ a a χ-stable F_q-line, and that line contains a real relation.

Write the specialised relation as λ·(C_r, C̄_r). Then D_α = (λ/λ̄)·C̄_α, so κ_α = λ/λ̄ is well defined.

The proof is correct. The "Consequence" ("NO information beyond…") is a reading of the lemma, not a theorem.

### §2 Proposition TX
- **Composition identity.** (τ+c)∘(τ+d) = τ² + (d²+c)τ + cd. With c = ᾱ(α+ᾱ), d = α, and c′ = α(α+ᾱ), d′ = ᾱ, both sides equal τ² + (α²+αᾱ+ᾱ²)τ + α^{Q+1}(α+ᾱ). Checked by hand and by [C] (T1).
- **Mapping into F_Q.** Since \bar Γ_α = Δ_α, we get C_α(V_α) ⊂ F_Q. [C] T3: 0 failures at m = 12 (all α), 16.
- **Exceptional sets (FIX-4).**
  - V_α is degenerate (dim ρ−1) exactly when α ∈ U∖{0}.
  - For α ∈ F_Q, V_α ⊂ F_Q, so a(V_α) = 0.
  - Referee proof that a(V_α) = 1 exactly for α ∉ F_Q. Suppose (u₁²+αu₁) = r(u₂²+αu₂) with r ∈ F_Q. Then α(u₁+ru₂) = ru₂²+u₁². So either α ∈ F_Q, or u₁ = ru₂, which forces r² = r, i.e. u₁ = u₂.
  - [C] T2 at m = 12, ρ = 6: every α ∉ F_Q has a = 1 (4032 α), and α = 0 has a = 0. At m = 16: 194 α ∈ F_Q∖U have a = 0, and 299 random α ∉ F_Q have a = 1.
  - The owner's "always 1" is a sampling artefact: F_Q has density 1/Q. The statement "≤ 1" is correct.
- **Generic level.**
  - w^Q = u² + X^Q u is exact, because u ∈ F_Q (T4 checks it by direct polynomial powering).
  - C(w) = D(w^Q) holds as polynomials in F_q[X] (T4: 0 failures).
  - The generic defect is exactly 1. A degree-0 generic relation would specialise to a = 0 at almost all α, contradicting the computation above. Hence "the degree-1 relations form a line" holds for ρ ≥ 3. The note should include this line (FIX-4).
  - Real type fails. c₁^Q = X^{q+Q}+X^{2q} ≠ X²+X^{Q+1} = d₁ (T5). κ = 1 is forced by the monic leading terms.
- **TX.3.** Comparing coefficients gives c = (u₁/u₂)⁴ = (u₁/u₂)², so u₁ = u₂. [C] T6: no pair with a constant ratio.
- **TX.4.** w′ = u, rank ρ (T8).
- **Bivariate lift.** The relation Γ = τ + Y(X+Y) has ιΓ = τ + X(X+Y), and Γ(w) = (ιΓ)(ιw). [C] T7: 0 failures.
- **Meaning paragraph.** Valid relative to the stated list of PHFG step-1 hypotheses. The note correctly says TX is not an arc family.

### §3 Lemma TSZ
Every step checks:
1. The change of variables (x,y) ↦ (x+ωy, x+ω̄y) has determinant ω+ω̄ ≠ 0.
2. The total degree of h is ≤ deg_X + deg_Y ≤ 2δ.
3. The F_Q-splitting h = h₁ + ωh₂ is coefficientwise, and h_i is F_Q-valued on F_Q².
4. Schwartz–Zippel over F_Q² gives ≤ 2δQ zeros.

If 2δ ≥ Q the hypothesis is vacuous, so there is no issue there. The bound is not sharp: it can be improved to (deg_X+deg_Y)Q, but that is not needed.

[C] check_tsz:
- m = 4, δ = 1, exhaustive over all 16⁴−1 nonzero f: the maximum is 5 zeros, against a bound of 8.
- Sampled and structured products at m = 6 and m = 8, δ ≤ 3: no violation. The maximum was 33 against a bound of 96.

### §4 Theorem RB
- **Fixed field of ι.** With x = (ω̄X+ωY)/(ω+ω̄) and y = (X+Y)/(ω+ω̄), we have ι(x) = x and ι(y) = y, and [L₂ : F_Q(x,y)] = 2. So F = F_Q(x,y), and Y = x+ω̄y (FIX-11).
- **RB(i).**
  - M(α,ᾱ) is the HFD defect matrix, using w(α)^Q = w^{(Q)}(ᾱ).
  - Each (2a+2)-minor has bidegree ≤ u(2^{a+1}−1).
  - TSZ then gives rank < 2a+2 over L₂, and an L₂-kernel vector is a relation for all w by F₂-additivity.
- **RB(ii).**
  - ι²w = w^{(q)}(X) = w, so S(γ,δ) = (ιδ, ιγ) is an ι-semilinear involution on each space of relations of degree ≤ L.
  - Galois descent for the quadratic extension L₂/F gives a fixed vector, and a fixed vector has δ = ιγ with γ ≠ 0.
  - The γ₀ ≠ 0 argument is right. Entrywise squaring is the Frobenius embedding L₂ → L₂², rank is invariant under field extension, so W² has the same minimal degree.
- **RB(iii).**
  - Relations are a left L₂{τ}-module.
  - The reduction step needs c·lc(B)^{2^{n−k}} = lc(A), which is always solvable. A weak Popov form with pivots in distinct columns therefore exists over the non-perfect L₂.
  - The predictable-degree property holds, because Frobenius-twisting a leading row preserves its pivot position.
  - The quotient has L₂-dimension ρ′, because the functionals w ↦ w^{2^e} span L₂^{ρ′} (Moore). So d₁+d₂ = ρ′, and the count at L = a₂ is 1.
  - [C] check_module (M1): the relation counts n(L) match (L+1−d₁)₊ + (L+1−d₂)₊ for every L, in five families A(U) (ρ = 6, 8; deg A = 1, 2, 3), with d₁ = deg A.
  - The note's wording ("Only right division… a/b^{2^k}… left Euclidean") mixes conventions, and the exponent should be the degree difference (FIX-6).
- **Numerical range.**
  - [C] check_range, exact arithmetic over all even ρ ≤ 400 and g ∈ [ρ+3, 2ρ] (39,800 cells):
    - 2u(2^{a+1}−1)Q < KR²/2 for u = R/4 and every a ≤ ρ/2−2;
    - R2^aQ = 2^{a−ρ/2}Q² ≤ Q²/4;
    - a* = ρ−⌈g/2⌉ = ρ−1−⌊(g−1)/2⌋ ≤ ρ/2−2;
    - the weight-K condition a ≤ g−ρ/2−4 holds for all a ≤ a*.
    - 0 failures.
  - The arithmetic is sound. The claim that "the hypothesis of RB holds in every open even cell" is not [P], however. RB needs W ⊂ F_q[X], and that holds only in the rational branch and only if B1 is monic over F_q[X], so that rational roots are polynomials of degree ≤ u. It also needs W(α) to be a ρ-dimensional Frobenius twist of V_α at every α ∈ N. The note itself lists the second point as audit point (2), "[A] needed from Codex" (FIX-2).
  - If W(α) were only a ρ′-dimensional subspace of V_α, its defect would still be ≤ a(V_α), but RB would need a ≤ ρ′/2−2, which can fail.

### §5 Proposition RD
- **RD(a).** Correct. D_X kills squares and functions of Y.
- **RD(b).** Correct. Write ℓ for (D_Xγ, D_Xιγ). If ℓ were an L₂-multiple of (γ,ιγ), then γ₀w′ = 0 on W, so W₀ = W. Hence W₀ ≠ W gives two independent relations of degree ≤ a₂ on W₀.
  - d₂(W₀) ≥ ρ″/2 ≥ ρ′/2−1 ≥ a₂+1, so the count forces d₁(W₀) ≤ a₂−1.
  - RB(ii) is pure algebra, so it applies to W₀ and to √W₀ without TSZ.
  - [C] (M2): dim W = 10, a₂ = 3, dim W₀ = 8, a₂(W₀) = 1. Consistent.
- **RD(c) is false as stated.**
  - The iteration loses dimension only at defect drops, so the invariant dim ≥ ρ′−2a₂ ≥ 4 is correct. Nothing in RB/RD/RR, however, forces a defect drop ever to occur.
  - Counterexample within RB's and RD's hypotheses: the constant family W = {u²+βu : u ∈ U}, U ⊂ F_Q, β ∉ F_Q.
    - W ⊂ F_q[X] has degree 0 ≤ u, and W(α) is ρ-dimensional with a = 1 ≤ ρ/2−2 at every α.
    - RR holds (rank 0).
    - W₀ = W, and √W is again a constant family with defect 1, forever.
  - [C] (M3): defect 1 at six successive square-root steps, with all derivatives zero.
  - More generally, any family whose polynomial degree reaches 0 before its defect reaches 0 stalls. So the step "we reach a bivariate-defect-0 family" and the hand-off to "exactly HFA1's (H) structure" in (d) are unproved. Termination has to come from arc input: the weight bookkeeping and BWG at the terminal weight must apply to a nonzero family of possibly positive defect, or such families must be excluded otherwise.
  - What RB+RD do establish is the useful part: the descended family stays nonzero, with dim ≥ ρ′−2a₂ ≥ 4.
- **RD(d).** Correct when defect 0 is reached. F ∩ F_q(X) = F_Q, because f(X) = f^{(Q)}(Y) forces f to be constant. Also u ↦ η′u is injective when η′ ≠ 0.

### §6 G1′
- The WG threshold is right: Q ≤ 3u(e+1) with u = R/4 ⟺ e ≥ (4/3)2^{ρ/2}−1 ([C] R3).
- The bold implication "G1 ⇐ G1′ + G2" also needs:
  - (i) the B1 identification (FIX-2);
  - (ii) G4, geometric irreducibility, for WG;
  - (iii) the terminal step of FIX-1.
- The heuristic paragraphs are labelled correctly. For the Lang-type equation, the extreme-coefficient Kummer relations a_a^{(Q−1)2^a} = c_a/d_a and a₀^{Q−1} = c₀/d₀ are correct. The "2a+1 vs 2a+2" real count is plausible but unverified, as the note says.

### Owner script
- Reviewed in full. It is self-contained, reads no files, uses Rabin's irreducibility test, and computes the defect via rank on F^e/χF^e columns.
- Re-run from `checks/owner_copy/` with `python3 -I`. Seeds 1, 2, 3 reproduce the three blocks of `toycheck.log` exactly.
- Seed 1 at m = 20 gives one control α with defect 3 < ρ/2, so "random family has pointwise defect ρ/2" holds only generically (FIX-9).

## FIX list (substantive first)

**FIX-1 (substantive). §5 RD(c)–(d), §5 Status, title.**
- *Problem.* "Iterating … we reach a bivariate-defect-0 family of dimension ≥ ρ′−2a₂" is unproved and false in the abstract setting. The constant family {u²+βu}, β ∉ F_Q, satisfies every hypothesis and never drops defect. (d)'s reduction to HFA1's (H) structure is therefore not established.
- *Correction.* Replace (c) with: "Each step either halves the degree without loss (W₀ = W) or loses ≤ 2 dimensions and drops the defect. Hence every descendant has dim ≥ ρ′−2a₂ ≥ 4, and the inequality a_i ≤ ρ_i/2−2 is preserved. If defect 0 is reached, (d) applies."
- Add a named condition, e.g. **G5**: the terminal step of HFA1 (weight bookkeeping plus BWG) excludes a nonzero rational descended family at the terminal weight irrespective of its defect, or positive-defect terminal families are excluded by other arc input.
- State RD as [COND on G2 + G5].

**FIX-2 (substantive). §4 "Numerical range" last sentence; §5 Status ("CONDITIONAL only on G2").**
- *Problem.* Applying RB to the arc needs, beyond G2:
  - (a) B1 is monic over F_q[X] (rational roots are polynomials of degree ≤ u = R/4);
  - (b) at every original nonfocus α, B1's root space is ρ-dimensional and a Frobenius twist of V_α (so its defect is ≤ a(V_α));
  - (c) HFA1's terminal BWG (FIX-1).
  The note's own audit point (2) concedes (b) is [A]-pending.
- *Correction.* Label the sentence "hence the hypothesis of RB holds in every open even cell" [COND on (a), (b)]. Change the Status to "conditional on G2, G5 and the B1 identification (a)–(b)".

**FIX-3 (substantive). §6 bold implication "G1 ⇐ G1′ + G2" and the title's "G1 reduces to an orbit bound G1′".**
- *Problem.* The implication also uses G4 (geometric irreducibility, for WG), the B1 identification (FIX-2) and G5 (FIX-1).
- *Correction.* "G1 ⇐ G1′ + G2 + G4 + G5 + [A] B1 identification". Adjust the title to "…reduces, modulo named inputs, to an orbit bound G1′".

**FIX-4 (minor). §2 TX item 1, item 2 and the [C] table.**
- "Pointwise defect ≤ 1 at EVERY α ∈ F_q" should exclude the degenerate α ∈ U∖{0}.
- Add: a(V_α) = 0 for α ∈ F_Q∖U, and a(V_α) = 1 exactly for α ∉ F_Q (proof as in this audit). The table's "always 1" reflects sampling.
- Add the one-line proof that the generic defect is exactly 1, which "the degree-1 relations form a line" uses.

**FIX-5 (minor). §5 RD(b) proof and §7.** "ℓ is nonzero on X_W := span_{L₂} x(W)" and "they differ on x(W)" are garbled. Replace with: "ℓ does not vanish identically on W (else γ₀w′ ≡ 0, i.e. W₀ = W), while (γ,ιγ) does. So ℓ is not an L₂-multiple of (γ,ιγ), and both vanish on W₀."

**FIX-6 (minor). §4 RB(iii) and §7.** "Only right division … a/b^{2^k} … left Euclidean" should read: "division with remainder A = PB + R (B on the right) exists, because the leading coefficient lc(A)/lc(B)^{2^{n−k}} always exists (n−k = degree difference). This gives weak Popov forms for left submodules."

**FIX-7 (minor). §4 Numerical range.** "That is EXACTLY the structured range a ≤ a*" should read "this range contains EBR's structured range, since a* ≤ ρ/2−2".

**FIX-8 (minor). §1 Consequence.** Label it [H]. It is interpretive.

**FIX-9 (minor). §2 control row.** Say "generically pointwise defect ρ/2 (seed 1 at m = 20 shows a sporadic α with ρ/2−1); bivariate rank 4, i.e. no degree-1 bivariate relation". The current text says "no relation".

**FIX-10 (minor). Inputs [A].** The WG and RR statements are quoted from HFD §3 and IDEAS §305, which record that only Codex summaries were read. Mark them as "[A] via HFD/IDEAS summary reading".

**FIX-11 (minor). §4 Setting.** Add "Y = x+ω̄y" next to "X = x+ωy", so that ι(x) = x and ι(y) = y is explicit.

## Minor notes
- Each lemma's TSZ use needs |N| > 2δQ with δ the larger partial degree. A sharper (deg_X+deg_Y)Q also holds; it is not needed.
- RB(ii) and RD(b) use only algebra over L₂, not TSZ, so they apply to all descendants.
- The header "AUDIT STATUS: NOT INDEPENDENTLY AUDITED" should be updated once the fixes are applied.
- [H] in §6: the claim "TX shows degree ~Q is intrinsic" rests on a single example. It is acceptable as [H].

## Files read
I followed the handoff's referee rules. START-HERE contains no restriction on what a referee may read, beyond the project rules (label claims, audit before sending, never execute incoming Codex scripts). No review or adoption files are designated off-limits.

Read in full:
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`
- `work/DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`
- `work/DZ-CLOUD-HANDOFF/notes/EBR-EVEN-BAND-REDUCTION-NOTE-20261007.md`
- `referee_RBL/src/note/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md`
- `referee_RBL/src/note/owner_scripts/toycheck.py`
- `referee_RBL/src/note/owner_scripts/toycheck.log`

Read in part:
- `docs/IDEAS-PROJECT-TRIM.md`, lines 1–60 and 400–432
- `docs/STATE-PROJECT-TRIM.md`, lines 1–80

Grep excerpts only, for WG/RR/HFA/BWG/B1/STT/auditor references:
- `docs/*.md`, `notes/*.md`, `packets/*.md` in the handoff

Not read:
- anything under HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS or uploads, or any other scratchpad;
- any file content in DZ_CLOUD_RESULTS (only its directory names were listed, to locate the output folder).

## checks/ contents
Each script is my own code, run with `python3 -I`. See `checks/checks_SHA256SUMS.txt`.
- `check_tx.py`: TX identities, all exceptional sets, generic identity in F_q[X], real-type failure, bivariate real relation. Logs: `check_tx_12_6.log`, `check_tx_16_6.log`, `check_tx_16_8.log`.
- `check_tsz.py` / `check_tsz.log`: TSZ, exhaustive at q = 16 and sampled at q = 64, 256.
- `check_range.py` / `check_range.log`: numerical range, a* forms and WG threshold (39,800 cells).
- `check_module.py` / `check_module.log`:
  - (M1) relation-module counts over L₂;
  - (M2) RD(b) consistency;
  - (M3) RD(c) constant-family counterexample.
  - A first run was killed by the container restart. A second run hung because of a referee bug: it asked for ρ = 10 > m/2, which makes rand_U loop forever. After the fix it completed.
- `owner_copy/toycheck.py`, an untouched copy, with `rerun_16_6.log`, `rerun_20_8_s1.log`, `rerun_20_8_s2.log` and `rerun_24_10_s3.log`. Seeds 1, 2, 3 reproduce the owner log exactly.
