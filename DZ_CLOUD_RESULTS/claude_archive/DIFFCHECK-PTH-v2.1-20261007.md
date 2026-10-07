# DIFFCHECK — PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.1.md (revision referee, cloud session, 7 Oct 2026, 20:33–20:40Z)

This check was done by the same isolated referee as REVISION-CHECK-PTH-v2-20261007.md (sha256 920a94d9d819c1923898b6a2a5a51f2c242d87fd37c8d3905a54d273bddcffcd), under the same rules and isolation.

Note checked: `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.1.md`, sha256 `869cdf73fe9702b0bcf9d2e562b00001799b2a6dcb06ffee01ebb86d0b2133d7`. The copies in `src/` and `claude_archive/` are identical.

Method: a line diff of v2 (sha256 478ffaf9…dfea87) against v2.1. Every hunk was read and checked against the RC list. Residual statements were found with greps for GLS₁, c₀/d₀ and d₀.

## Verdict: **NEEDS EDIT (one line)**
- RC-1 to RC-12 are all correctly applied, including the repair to Lemma ML.
- The diff contains no change outside the RC items, apart from the expected header and status updates.
- **However, one line that was not edited now contradicts the RC-10 edit.** §4A Consequence (i), l.143, still reads "GLS₁ ⟸ GLS₀". (See D-1.)
- After that one-line fix, PTH v2.1 can go to the outbox. No further check is needed beyond confirming that this single line changed.

## RC-by-RC

| RC | Location in v2.1 | Applied correctly? |
|---|---|---|
| RC-1 | l.132 (ML statement), l.139–140 (proof step 4 and the general bottom identity), l.144–148 (Consequence ii), l.151 (Consequence iii), l.172 (§6a) | **Yes.** See the strengthening repair below. |
| RC-2 | l.101 | **Yes.** The equivalence is now stated with the stabiliser bound, and the note says (GT) can hold in gate-failing cells (TX). |
| RC-3 | l.172 | **Yes.** "Equivalently" is replaced by "in particular (necessary conditions)", and (GT) is stated via y. |
| RC-4 | l.154–156 | **Yes.** "Of degree < m/2" is added, with the B(τ^{m/2}+1) reason, and the note says (iv) is unused in GO. |
| RC-5 | l.65–70 | **Yes.** V is specified, the [P]/[C] split is correct, and the λF_Q remark is included. |
| RC-6 | Title | **Yes.** |
| RC-7 | l.107 | **Yes.** |
| RC-8 | l.94 | **Yes.** |
| RC-9 | l.125 | **Yes.** (GT) is now stated to be automatic in the 51 cells and is removed from the input list there. |
| RC-10 | l.99–100 | **Yes, but incomplete.** GLS₁ keeps v1's bound deg A ≤ a₂, and "GLS₁ ⟹ GLS₀; GLS₀ suffices" is correct. §4A (i), l.143, was not updated (D-1). |
| RC-11 | l.162 | **Yes.** |
| RC-12 | l.80, l.89, l.92–94 | **Yes.** The general bound deg < Q²/4 is re-derived below. R_P is now defined in §3, and (B1b)'s [A]-pending status is noted. |

**The repair to the strengthening (RC-1) [P, re-checked].**
- ML now states "a₀ ≠ 0; c₀ = 0 ⟺ d₀ = 0; d₀ ≠ 0 if c₀ ≠ 0". This follows from c₀a₀ = d₀a₀^Q with a₀ ≠ 0. The counterexample C = D = τ, A = 1 is cited.
- The general bottom identity at the least index i with (c_i, d_i) ≠ (0, 0) is correct: both coefficients are nonzero, and (a₀^{Q−1})^{2^i} = c_i/d_i.
- In Consequence (ii), y = a₀^{Q−1} is G-fixed because χ(g)^{Q−1} = 1. y lies in L^sep, so y ∈ L. Indexing by "the least i with c_i ≠ 0" is the same as the least i with (c_i, d_i) ≠ 0, because c_i = 0 ⟺ d_i = 0 at that index.
- Consequence (iii) is correct.
- Optional wording: "which always holds pointwise by HFD §1" (l.132) refers to PTH's real relation, not to an arbitrary C ∈ F_q{τ}. "For PTH's real relation C" would be more precise. This is cosmetic.

**RC-12 bound [P, re-checked].**
- (2^{j+1}−1)(Q+1) < 2^{ρ/2−1}Q for j ≤ ρ/2−2, and Σ_T 2^e < 2^ρ.
- So deg < 2^{2g+ρ−3} + 2^{g+ρ−2} ≤ 2^{2g+ρ−2} = Q²/4, using g ≥ 1.
- Q²/4 < Q²/2 < v.
- This is consistent with the numerical worst ratio of 0.25 relative to Q²/2.

## D-1 (must fix, one line)
- **Where:** §4A Consequences (i), l.143.
- **Current text:** "GLS₁ ⟸ GLS₀. GO uses no degree bound on A."
- **Problem:** GLS₁ now includes deg A ≤ a₂ (l.99), so GLS₀ does not imply it. The line also contradicts l.100 ("GLS₁ ⟹ GLS₀").
- **Suggested text:** "(i) GLS₁ ⟹ GLS₀, and GLS₀ already gives GLS₁'s line clause (by ML), though not its degree bound. GO uses no degree bound on A, so GLS₀ suffices."

## Other changes
The diff has exactly 18 hunks, and every hunk is either an RC item or one of the following expected non-RC changes:
- the title timestamp and version;
- the AUDIT STATUS block (l.6, l.10–14), which records the v2 revision check, its sha256, its verdict, and the hold;
- the new §9 change log, whose 12 rows match the edits.

There are no other textual changes. §§0–2, PTH (i)–(iii), GO (a)–(e) and their proofs, the coverage numbers, §5 apart from the RC-11 label, and §§7–8 are byte-unchanged.

## Files read
- `referee_PTHv2/src/PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.1.md`: the diff against v2, plus lines 141–144, 160–170 and 176–186.
- A sha256 comparison of the `claude_archive/` copy.
- The source directory listing.

Nothing else was read. No HYP or 3PP directories, no uploads, no other scratchpads, and no git were used. No computations were needed.
