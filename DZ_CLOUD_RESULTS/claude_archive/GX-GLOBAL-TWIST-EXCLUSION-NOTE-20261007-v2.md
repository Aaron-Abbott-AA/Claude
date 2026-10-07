# Even ρ, structured branch: once the Lang twist is global and the gate holds, the rational twisted family A(U′) descends LOSSLESSLY to constants, so, **given GLS₁'s degree bound**, the range restriction a* ≤ (ρ−4)/3 of PTH-GO is unnecessary [v2: FIX-1] [COND on GLS₁, (GT), G4, WG [A], (B1a⁺), (B1b), G2 = {RR_k}, (I216′) incl. (B1b-fix), Prop 216.3 [A]] (owner note **v2**, cloud session, 7 Oct 2026, 20:48Z; v1 20:39Z)

Claude DZ (cloud continuation of session_01JBo5c8BAGb4ugZEpxorNDq; container NOT linked to the Mac).
Labels: [P] owner proof; [C] computation; [H] heuristic; [A] reading of reviewed or earlier sources; [COND] conditional on a named input; [OPEN] open problem.

**AUDIT STATUS (v2).**
- GX v1 (sha256 e4df4fd1…22230d) was independently audited in AUDIT-GX-GLOBAL-TWIST-EXCLUSION-20261007.md. Verdict: **PASS-with-fixes** (2 substantive, 8 minor).
- This **v2** applies FIX-1, FIX-2 and m1–m8. Each change is marked [v2: FIX-n] or [v2: m-n].
- **v2 HOLD:** v2 has not been revision-checked. Do not send to Codex until it has been.

## 0. Inputs
- **PTH v2.2 (EH; audit chain complete).** Used:
  - Lemma MI;
  - Lemma ML;
  - Proposition GO (a)–(d), together with its setting:
    - W is the root space of the WG family B1 (weight u = R/4);
    - the generic relation (C, D) over L = F_q(X) has degree a₂ ≤ a* ≤ ρ/2 − 2;
    - P = C + Dτ^{m/2}, R_P ⊇ W, and G = Gal(L^sep/L).
- **(GLS₁)** (PTH v2.2 §4): C·A = D·A^{(Q)} has a nonzero solution A ∈ L^sep{τ} with deg A ≤ a₂. The line clause is automatic, by ML [v2: m1].
  - Only the bound d := deg A ≤ ρ − a₂ − 3 is used. GLS₀ together with that bound would suffice.
- **(GT)**, **G4**, **WG [A]** (summary reading only), **(B1a⁺)** and **(B1b)**, as in PTH v2.2.
- **G2 = {RR_k}** (TCR v2.1, Lemma HF), here applied to a rational subspace W′ ⊂ W: RR_k says dim W′_k − dim W′_{k+1} ≤ 2.
  - RR_k on W′ follows from RR_k on W^rat, since RR_k passes to subspaces. So GX's G2 input is the same as TCR RS(a)'s [v2: m3].
- **(I216′)** including (B1b-fix), and **Prop 216.3 [A]**: the terminal step of TCR v2.1, Theorem TC, steps 3–4.

## 1. Lemma SQ (rational twisted families are killed by RR unless their twist is a square) [P] [v2: m6; renamed from "Lemma DZ"]
**Setting.**
- A ∈ L{τ} has degree d.
- U′ ⊂ F_Q is an F₂-subspace with dim U′ ≥ d + 3.
- W′ := A(U′) ⊂ F_q[X], and the derivative map w ↦ w′ on W′ has F₂-rank ≤ 2 (RR).

**Statement.**
- (i) A′ := Σ a_i′τ^i is 0. So every coefficient a_i lies in L² = F_q(X²).
- (ii) W′ ⊂ F_q[X²], and √W′ = A_½(√U′), where A_½ := Σ √a_i τ^i ∈ L{τ} has degree d and √U′ ⊂ F_Q has the same dimension.

*Proof.*
1. **The derivative.** For u ∈ U′ (a constant): w = Σ a_i u^{2^i}, so w′ = Σ a_i′u^{2^i} = A′(u).
2. **Kernel bound.** The rank is ≤ 2, so A′ vanishes on a subspace of U′ of dimension ≥ dim U′ − 2 ≥ d + 1.
   - A nonzero τ-polynomial of degree ≤ d has an F₂-kernel of dimension ≤ d (it has at most 2^d roots).
   - Hence A′ = 0.
   - Injectivity of A on U′ is not needed here: u ↦ A(u)′ = A′(u) is a map on U′, and its rank is the rank of the derivative on W′ = A(U′), because it factors through W′ [v2: FIX-2].
3. **Squares.** In characteristic 2 with F_q perfect, f′ = 0 ⟺ f ∈ F_q(X²) = L². So a_i = s_i² with s_i := √a_i ∈ L.
4. **(ii).** w = Σ s_i² u^{2^i} = (Σ s_i (√u)^{2^i})² = A_½(√u)², and √u ∈ F_Q. ∎

## 2. Lemma LD (lossless descent to constants) [P mod RR_k on W′]
**Setting.**
- W′ = A(U′) ⊂ F_q[X], with A ∈ L{τ} of degree d.
- U′ ⊂ F_Q with dim U′ ≥ d + 3, and **A injective on U′**. In GX this is supplied by MI (A is injective on F_Q) [v2: FIX-2].
- Every element of W′ has degree ≤ u.
- RR_k holds on W′ for all k with 2^k ≤ u.

**Statement.** W′ ⊂ F_q, i.e. **every element of W′ is a constant**, and dim W′ = dim U′ (by injectivity) [v2: FIX-2].
- Without injectivity one still has dim W′ ≥ dim U′ − d > 0.
- Counterexample to the v1 clause without injectivity: A = τ + 1 with 1 ∈ U′ (referee T4).

*Proof.*
1. Lemma SQ at level 0 gives W′₁ = W′ (no loss) and W′^{(1)} = A_½(√U′), of the same form and the same d. A_½ is injective on √U′ because A is injective on U′: A(u) = A_½(√u)².
2. By Lemma HF (TCR v2.1), RR for W′^{(k)} is RR_k on W′. So Lemma SQ applies at every level, and every level is lossless: W′ = W′_k for all k.
3. For 2^k > u, W′_k consists of 2^k-th powers of polynomials of degree < 1, i.e. of constants. ∎

**Comparison with TCR's Lemma CD.** CD needed the bivariate defect (RB, via TSZ) to bound the lossy levels, and paid ≤ 2 dimensions per defect drop. Here the *twist* structure W′ = A(U′) with a global A makes **every level lossless**. No bivariate relation, no TSZ and no RS(a) range condition are needed.

## 3. Theorem GX (structured branch, global twist) [COND on GLS₁, (GT), G4, WG [A], (B1a⁺), (B1b), G2, (I216′) incl. (B1b-fix), Prop 216.3 [A]]
**Setting.** Even ρ, ρ+3 ≤ g ≤ 2ρ, and a(V_α) ≤ a* at every original nonfocus.

**Statement.** Under the inputs above there is no original arc. **There is no restriction a* ≤ (ρ−4)/3.**

*Proof.*
1. **GO.** GO (a)–(d) of PTH v2.2 (GLS₁ ⟹ GLS₀; (GT); G4; WG) gives:
   - A(F_Q) ⊂ R_P, G-stable, with G acting through χ;
   - W′ := W ∩ A(F_Q), with dim W′ ≥ ρ − a₂ and every orbit in W′∖{0} of size |χ(G)|;
   - by (GT) and WG, |χ(G)| = 1.
2. **χ trivial ⟹ A ∈ L{τ}.** g(A) = Aχ(g) = A for all g ∈ G, so A ∈ L{τ}. U′ := A^{−1}(W′) ∩ F_Q has dim U′ = dim W′, by MI.
3. **W′ is rational and polynomial.** W′ = A(U′) consists of rational roots of B1. By (B1a⁺) they are polynomials of degree ≤ u.
4. **Kernel bound.** dim U′ ≥ ρ − a₂ ≥ d + 3, since d ≤ a₂ and 2a₂ + 3 ≤ ρ − 1 (a₂ ≤ ρ/2 − 2).
5. **Descent.** Lemma LD (with G2) gives W′ ⊂ F_q, nonzero.
6. **Contradiction.** A nonzero constant c ∈ W′ ⊂ W lies in W(α) for every α ∈ N. (As in TCR v2.1 RC-1, the comparison projection adds at most one radical, or the ≤ 1 α with μ(α) = ∞ is dropped; v > n covers both [v2: m8].) By (I216′), φ(c) lies in the radicals of v distinct nonfocus directions μ(α), and v > n. This contradicts Prop 216.3 in the (I216′) frame, as in TCR v2.1 TC steps 3–4. ∎

**[C] gxcells.py (coverage, arithmetic only).** Among even ρ ∈ [10, 40] and cells ρ+3 ≤ g ≤ min(2ρ, ⌈3ρ/2⌉+2) with a* ≥ 1:
- there are **200** cells, and the kernel bound ρ − a* − 2 > a* holds in all of them;
- the **sufficient** gate passes in **112** cells and fails in 88;
- the failures are exactly the cells where ρ′ := (g + ρ/2)/2 is an integer in [ρ−a*, ρ], e.g. (10,13) with ρ′ = 9 and (10,15) with ρ′ = 10.
- In the failing cells (GT) can still hold; it is then a property of the Kummer class y (PTH §4A).
- **Upgraded to [P] for every even ρ** [v2: m2; proofs from the referee's §2]:
  - **Kernel bound.** ρ − a* − 2 > a* ⟺ a* < (ρ−2)/2, which holds because a* ≤ ρ/2 − 2.
  - **Failure pattern.** Write N := m/2 = g + ρ/2. Any offending r ∈ [ρ−a*, ρ] = [⌈g/2⌉, ρ] divides N with quotient ≥ 2, and quotient ≥ 3 is impossible since N/3 < ⌈g/2⌉. So r = N/2 = m/4, and the sufficient gate fails ⟺ N is even and N/2 ≤ ρ ⟺ g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2.
  - The referee checked the closed form numerically up to ρ = 400.
- **Comparison with GO(e) [C, referee].** 61 of the 112 gate-passing cells (ρ ≤ 40) lie outside GO(e)'s range a* ≤ (ρ−4)/3.

## 4. Updated reductions (adds a route) [COND]
- **New route (GX).** G1 ⇐ GLS₁ + (GT) + G4 + WG [A] + (B1a⁺) + (B1b) + G2 + (I216′)[incl. (B1b-fix)] + [A] Prop 216.3.
  - This holds in every cell where (GT) holds, including all 112 sufficient-gate cells (ρ ≤ 40).
  - It **complements** PTH v2.2 GO(e) [v2: FIX-1]. Under GLS₁ (or GLS₀ + deg A ≤ ρ − a₂ − 3) it removes the range a* ≤ (ρ−4)/3 and the RB/TSZ inputs. Under GLS₀ alone, GO(e) remains the only route, in its range.
- **Unchanged.**
  - The GO(e) route (PTH v2.2): under GLS₀ + (GT) + G4 + WG [A] + (B1a⁺) + (B1b), plus TCR's inputs, for a* ≤ (ρ−4)/3 [v2: FIX-1].
  - The TCR route: G1 ⇐ G1″ + G2 + (B1a) + (I216′) + Prop 216.3.
  - The RBL rational-branch route.
- **OPEN.**
  - **GLS₁ / GLS₀**, the generic twist.
  - **(GT) in the 88 sufficient-gate failures** [v2: m5]. (GT) fails ⟺ |χ(G)| ≥ T. By GO(c) this forces t = dim U′ = ρ′ = m/4 > ρ/2, so U′ = λF_{2^{ρ′}}, and χ(G) ⊂ F_{2^{ρ′}}^* lies in no proper subfield.

## 5. Remarks [H]
- **Mechanism.** GX shows that with a global twist the structured branch behaves like HFA1's (H) branch: twist, then RR, then lossless square-root descent.
  - HFA1's own terminal step is BWG after descent to weight 2 (HFD §3, PHFG step 4 [A]).
  - GX ends instead at a constant root, which is killed by Prop 216.3 via (I216′) [v2: m4].
  - In HFA1 the twist is a scalar (A = η, deg 0).
  - Here A has degree ≤ a₂. The only new requirement is the kernel bound dim U′ ≥ deg A + 3, which is automatic *under GLS₁'s degree bound* [v2: m4].
- **The non-rational case** (|χ(G)| ≥ T, possible only in gate-failing cells) needs an argument for Kummer-twisted families A(a₀λF_{2^{ρ′}}).
- **So everything structured now hinges on GLS₁ (or GLS₀ with the degree bound; GO(e) covers GLS₀ alone in its range) and (GT)** [v2: FIX-1]. These are exactly the "global twisted half-field" questions put to Codex in EH §3(a)–(b).

## 6. Questions for Codex (for a later packet, after audit)
- **(a)** GLS₁: in the structured branch, is the pointwise minimal Lang twist A_α (unique up to F_Q^*, PTH ML) the specialisation of a twist over L^sep of degree ≤ a₂?
- **(b)** In the cells where ρ′ = (g+ρ/2)/2 ∈ [ρ−a*, ρ], can B1's Galois group act on W ∩ A(F_Q) through a character generating F_{2^{ρ′}}?

## 7. Owner self-check (NOT an independent audit)
- **SQ step 1.** u ∈ F_Q is constant in X, so (a_iu^{2^i})′ = a_i′u^{2^i}.
- **SQ step 2.** Kernel of a nonzero linearised polynomial of τ-degree ≤ d: at most 2^d roots, so F₂-dimension ≤ d.
- **GX step 2.** χ trivial and g(A) = Aχ(g) give G-invariance of the coefficients, so A ∈ L{τ}, with no separability issue.
- **GX step 4.** d ≤ a₂ ≤ ρ/2 − 2 gives ρ − a₂ − (d+3) ≥ ρ − 2a₂ − 3 ≥ 1.
- **LD.** Each level uses RR_k on W′. That is G2 for the rational subspace W′, as in TCR v2.1 RS step 4.
- **Points to audit.**
  - (1) That GO(d) indeed gives |χ(G)| = 1 under (GT): orbits are exactly |χ(G)|, and WG excludes 1 < e < T.
  - (2) That (B1a⁺) makes the rational roots polynomials.
  - (3) The coverage count.

Script [v2: m7]:
- `scripts/gxcells.py` and `.log` (own code; arithmetic only; run as `nice -n 19 python3 -I`).
- Archive path: `claude_archive/scripts/`. In a packet it ships as `gxcells.py.txt`; for the referee it was `owner_scripts/gxcells.py`.

## 8. Change log v1 → v2 [v2]
| Item | Where | Change |
|---|---|---|
| FIX-1 | Title, §4, §5 | "Supersedes" replaced by "complements GO(e)". The title now says "given GLS₁'s degree bound". The GO(e) route is kept under "Unchanged". |
| FIX-2 | §1 step 2, §2 | LD assumes A injective on U′ (supplied by MI in GX); the weaker bound without it is noted, with the counterexample. SQ needs no injectivity. |
| m1 | §0 | The line clause of GLS₁ is automatic by ML. |
| m2 | §3 | Kernel bound and failure pattern upgraded to [P] for every even ρ; 61 cells are new relative to GO(e). |
| m3 | §0 | RR_k on W′ follows from RR_k on W^rat. |
| m4 | §5 | HFA1's terminal step is BWG; "automatic" is qualified by the degree bound. |
| m5 | §4 | (GT)-failure description rephrased. |
| m6 | §1, everywhere | Lemma DZ renamed Lemma SQ. |
| m7 | §7 | Script paths. |
| m8 | §3 step 6 | Comparison-direction caveat added. |
