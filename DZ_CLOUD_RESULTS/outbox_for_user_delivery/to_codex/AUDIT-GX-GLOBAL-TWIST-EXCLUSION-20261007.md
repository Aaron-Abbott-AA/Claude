# AUDIT — GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007.md (independent referee, cloud session, 7 Oct 2026, 20:41–20:47Z)

Referee: fresh, isolated, adversarial subagent for the DZ line (project "Wan's numbers of PPs"). No contact with the owner session or with Codex. No files outside the DZ scope were read (list in §6).
Note audited: `src/GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007.md`, sha256 `e4df4fd1441988e6b1fe17d94f1259ba663a47fa588a219174dbfa2dfd22230d`. The copy in `claude_archive/` is byte-identical (`cmp`).
Owner script: `gxcells.py` (sha256 `5bd7e225…3b940`) and `gxcells.log` (sha256 `5c956835…6f60b`).
Labels follow the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN]. Where the referee proves something, it is marked "[P, referee]".

## 0. Verdict: **PASS-with-fixes**

- **The mathematics is correct.**
  - Lemma DZ is correct and short: (i) and (ii) were checked by hand, and the bound dim U′ ≥ d+3 is sharp (§3, T2).
  - Lemma LD is correct as used in Theorem GX: the induction over Hasse levels, the use of HF, and the terminal step were checked.
  - Theorem GX steps 1–6 follow from PTH v2.2 GO (a)–(d), MI, ML, (B1a⁺) and the TCR v2.1 terminal step, under the named inputs.
  - The coverage arithmetic (200 / 112 / 88) was reproduced exactly by the owner script (byte-identical log) and by independent referee code. The referee also proved the failure pattern for every even ρ (§2, item 15).
- **Two statements must be corrected before the note goes to Codex. Neither breaks Theorem GX.**
  - **FIX-1 (scope).** The note says GX "supersedes" PTH v2.2 GO(e)'s restriction, and the title says the restriction is "unnecessary". The two routes have *incomparable* hypotheses.
    - GX needs GLS₁'s degree bound (deg A ≤ ρ − a₂ − 3).
    - GO(e) needs only GLS₀, but it uses RB/TSZ through TCR RS(a).
    - So GO(e) must stay in the reduction ledger as a separate route.
  - **FIX-2 (false clause in a [P] lemma).** Lemma LD's statement "dim W′ = dim U′" is false without injectivity of A on U′. Counterexample: A = τ + 1 with 1 ∈ U′ (§3, T4). In GX, MI supplies injectivity, so GX is unaffected.
- **Owner revision is required.** It consists of restatements only; no proof needs to be rewritten.

FIX count: **2 substantive, 8 minor.**

## 1. Item table

| # | Item | Claimed label | Referee finding | Status |
|---|---|---|---|---|
| 1 | Title: "range restriction a* ≤ (ρ−4)/3 is unnecessary" | [COND …] | True only under GLS₁'s degree bound, which GO(e) does not need. | FIX-1 |
| 2 | §0 inputs: PTH v2.2 MI, ML, GO (a)–(d) and setting | [A] | Matches PTH v2.2 §2, §4, §4A. ML was audited (REVISION-CHECK-PTH-v2, DIFFCHECK v2.1 / v2.2 CONFIRMED). | OK |
| 3 | §0 GLS₁ paraphrase | — | Omits PTH's "line clause". That clause is automatic by ML, so this is harmless. | m1 |
| 4 | §0: "only d ≤ ρ−a₂−3 is used; GLS₀ + that bound suffices" | — | Correct. GX step 4 needs only dim U′ ≥ d+3 together with dim U′ ≥ ρ−a₂. | OK |
| 5 | §0 G2 = {RR_k} on the rational subspace W′ | [COND] | Correct. RR_k is monotone under subspaces (§2, item 11), so G2 on W^rat suffices. That is the same input as TCR RS(a). | m3 |
| 6 | Lemma DZ step 1 (derivative of A(u)) | [P] | Correct: u ∈ F_Q is X-constant; product and quotient rule in L. | PASS |
| 7 | Lemma DZ step 2 (kernel bound) | [P] | Correct. u ↦ A(u)′ factors through the derivative on W′, so its rank is ≤ 2 *without* injectivity of A. A nonzero τ-polynomial of degree ≤ d has F₂-kernel of dimension ≤ d. The bound d+3 is sharp (T2). | PASS |
| 8 | Lemma DZ step 3 (f′ = 0 ⟺ f ∈ F_q(X²) = L²) | [P] | Correct: L = L² ⊕ X·L², and (g + Xh)′ = h. F_q is perfect. | PASS |
| 9 | Lemma DZ (ii) | [P] | Correct. W′ ⊂ F_q[X²] follows directly from w′ = 0 for polynomials, and √w = A_½(√u). deg A_½ = d. Checked numerically (T3). | PASS |
| 10 | Lemma LD statement: "dim W′ = dim U′" | [P mod RR_k] | **False without injectivity of A on U′** (T4). The constancy conclusion is correct. | FIX-2 |
| 11 | Lemma LD proof (losslessness at every level; constants for 2^k > u) | [P mod RR_k] | Correct. The level-k data are A_{2^{−k}} with unchanged degree d and U′^{2^{−k}} with unchanged dimension. RR for W′^{(k)} is RR_k on W′ by HF. For 2^k > u, the space W′ ∩ F_q[X^{2^k}] contains only constants. | PASS |
| 12 | LD "Comparison with CD" | — | Correct. LD uses no bivariate relation, no TSZ and no RS(a) range. | OK |
| 13 | GX step 1 (GO ⟹ \|χ(G)\| = 1) | [COND] | Correct. Orbit size is exactly \|χ(G)\| (GO(c)), and W′ ≠ 0 because dim ≥ ρ−a₂ ≥ 4. (GT) gives < T, and WG+G4 exclude 1 < e < T. This answers owner point (1). | PASS |
| 14 | GX step 2 (χ trivial ⟹ A ∈ L{τ}; dim U′ = dim W′) | [P] | Correct. (L^sep)^G = L, and MI gives injectivity on F_Q. | PASS |
| 15 | GX step 3 ((B1a⁺) ⟹ polynomials of degree ≤ u) | [COND] | Correct. A root in L that is integral over F_q[X] lies in F_q[X], which is integrally closed. Pole order ≤ u at ∞ gives deg ≤ u. This answers owner point (2). | PASS |
| 16 | GX step 4 (dim U′ ≥ ρ − a₂ ≥ d+3) | [P] | Correct. a* ≤ ρ/2−2 holds throughout the band (g ≥ ρ+3), and d ≤ a₂ by GLS₁. | PASS |
| 17 | GX steps 5–6 (LD ⟹ constant root; TCR terminal step) | [COND] | Correct. The citation matches TCR v2.1 TC steps 3–4, including injectivity of α ↦ μ(α) and v > n. | PASS |
| 18 | §3 [C] gxcells: 200 cells, kernel bound in all, 112 pass / 88 fail, failures ⟺ ρ′ = (g+ρ/2)/2 ∈ [ρ−a*, ρ] | [C] | Reproduced exactly (owner copy: log byte-identical; referee code: same numbers). All of it is in fact [P] for every even ρ (§2). | PASS; m2 |
| 19 | §4 "New route … supersedes PTH v2.2 GO(e)'s restriction" | [COND] | Overclaim. The routes are complementary, not nested. | FIX-1 |
| 20 | §4 OPEN: "bad case U′ = λF_{2^{ρ′}}, ρ′ = m/4, χ(G) generating F_{2^{ρ′}}" | [OPEN] | Correct as a necessary description. It should be phrased as "(GT) fails ⟺ \|χ(G)\| ≥ T, which forces …". | m5 |
| 21 | §5 Remarks | [H] | HFA1 ends with BWG at weight 2, not with a constant root. "Automatic" holds only under GLS₁'s degree bound. | m4 |
| 22 | §6 Questions for Codex | — | Fine. (a) asks exactly for GLS₁. | OK |
| 23 | §7 self-check and script path | — | All three audit points are answered above. The path "scripts/gxcells.py" is shipped as `owner_scripts/`. | m7 |
| 24 | Naming: "Lemma DZ" | — | Collides with the lane name "DZ". | m6 |

## 2. Detailed audit

**Lemma DZ.**
- Step 1: for u ∈ U′ ⊂ F_Q, d/dX(a_iu^{2^i}) = a_i′u^{2^i}, valid for a_i ∈ L.
- Step 2: the map u ↦ A′(u) = (A(u))′ is the composite of A: U′ → W′ with the derivative on W′. So its rank is ≤ 2, and its kernel has dimension ≥ dim U′ − 2 ≥ d+1. This needs no injectivity.
  - A nonzero A′ of τ-degree ≤ d is a nonzero polynomial of degree ≤ 2^d, so it has ≤ 2^d roots. Its F₂-kernel therefore has dimension ≤ d, and A′ = 0.
- Step 3: L = F_q(X) has basis {1, X} over F_q(X²) = L², because F_q is perfect. (g + Xh)′ = h, so f′ = 0 ⟺ f ∈ L².
- (ii): Σ s_i²u^{2^i} = (Σ s_i u^{2^{i−1}})².
- Sharpness [P, referee; C]: with d = deg A, the bound "dim U′ ≥ d+3" cannot be lowered.
  - Take A = X·S_K + E, with S_K the subspace polynomial of a d-dimensional K ⊂ F_Q and E ∈ F_q{τ} of degree ≤ d.
  - Then A′ = S_K ≠ 0. For U′ ⊃ K the derivative rank is dim U′ − d, which equals 2 at dim U′ = d+2.
  - Confirmed in 360 instances (T2).

**Lemma LD.**
- The induction is: W′_k = W′ and W′^{(k)} = A_{2^{−k}}(U′^{2^{−k}}), with deg A_{2^{−k}} = d and dim U′^{2^{−k}} = dim U′.
  - RR for W′^{(k)} ⟺ RR_k on W′ (TCR v2.1 HF, using W′_k = W′).
  - DZ then gives W′^{(k)} ⊂ F_q[X²], i.e. W′_{k+1} = W′.
- At the first K with 2^K > u, W′ = W′_K ⊂ F_q[X^{2^K}] has all degrees ≤ u < 2^K. So W′ ⊂ F_q.
- Only RR_k with 2^k ≤ u is used, as stated.
- **However, the clause "dim W′ = dim U′" needs A injective on U′.** In LD's setting only W′ = A(U′) is assumed. For A = τ + 1 and 1 ∈ U′, W′ = A(U′) consists of constants of dimension dim U′ − 1 (T4, dim U′ ∈ {4, 5, 6} with d = 1). The hypotheses of LD hold there: all elements are constants, so RR_k holds trivially.
- In general dim W′ ≥ dim U′ − d. In GX, MI supplies injectivity, so GX step 5's "nonzero" is safe either way (dim W′ ≥ 3 > 0) → FIX-2.

**Theorem GX.**
- (1) GO(c) gives orbit size exactly |χ(G)| on W′∖{0}. Under (GT), |χ(G)| < T, and WG with G4 forbids 1 < e_w < T, so |χ(G)| = 1.
- (2) g(A) = A·χ(g) = A for all g ∈ G. Since L^sep/L is Galois, the coefficients lie in L.
- (3) W′ ⊂ L is fixed pointwise. (B1a⁺) gives integrality over F_q[X] and the pole bound at ∞, so W′ ⊂ F_q[X]_{≤u}.
- (4) dim W′ ≥ ρ + m/2 − (m/2 + a₂) (GO(b), with dim R_P ≤ deg_τ P ≤ m/2 + a₂). And d ≤ a₂ ≤ a* ≤ ρ/2 − 2, so ρ − a₂ ≥ d + 3.
- (5) LD, where RR_k on W′ follows from G2 on the rational root subspace (item 11 below).
- (6) This is TCR v2.1 TC steps 3–4 verbatim.
- The logical chain closes. [COND] list check: GLS₁, (GT), G4, WG [A], (B1a⁺), (B1b) (for dim W = ρ and GO's input step), G2, (I216′) incl. (B1b-fix), and Prop 216.3 [A]. MI and ML are audited [P], so the list is complete.

**Item 11 (G2 on subspaces) [P, referee].**
- Let W′ ⊂ W^rat. The map W′_k → W^rat_k/W^rat_{k+1} has kernel W′_k ∩ F_q[X^{2^{k+1}}] = W′_{k+1}.
- So dim W′_k − dim W′_{k+1} ≤ dim W^rat_k − dim W^rat_{k+1} ≤ 2.
- Hence GX uses G2 only on W^rat, exactly as TCR RS(a) step 4 does.

**Coverage [P, referee; C].**
- Put N = m/2 = g + ρ/2 > ρ and let r ∈ [⌈g/2⌉, ρ] with r | N, so N/r ≥ 2.
  - If N/r ≥ 3, then r ≤ (g + ρ/2)/3 < g/2, using g > ρ. That is impossible.
  - So r = N/2 = m/4. It lies in range ⟺ N is even and N/2 ≤ ρ ⟺ g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2. (N/2 ≥ ⌈g/2⌉ always holds.)
- The kernel bound ρ − a* ≥ a* + 3 is a* ≤ (ρ−3)/2, which follows from a* ≤ ρ/2 − 2.
- Every NWF-uncovered cell has a* ≥ 1 for ρ ≥ 8.
- The cell count is Σ_{ρ=10,…,40} ρ/2 = 200.
- [C] `gx_cells_ref.py`:
  - 200 / 112 / 88 reproduced;
  - the closed form was checked for even ρ ∈ [10, 400] (0 mismatches; the offending r is always m/4);
  - the kernel bound was checked over 39,788 band cells (0 failures);
  - GO(e): 78 range cells, 51 passing the gate (matches PTH v2.2). **61** gate-passing cells are new relative to GO(e).

**FIX-1 analysis.**
- PTH v2.2 GO(e): G1″ ⇐ **GLS₀** + (GT) + G4 + WG + (B1a⁺) + (B1b), in the range a* ≤ (ρ−4)/3. Then G1 via TCR RS(a), which uses RB (bivariate relation through TSZ, RBL v2.1 §4) and CD.
- GX: G1 ⇐ **GLS₁** (degree bound d ≤ ρ − a₂ − 3) + the same gate inputs + G2 + (B1a⁺) + (I216′) + Prop 216.3, with no RB/TSZ and no range.
- GLS₀ does not imply the degree bound. PTH v2.2 §4A (i), the DIFFCHECK D-1 line, says so explicitly. So in the range a* ≤ (ρ−4)/3 GO(e) is *not* subsumed: it still works when the generic twist exists but has large degree.
- "Supersedes" and "unnecessary" overstate this. Both routes must stay in the ledger.

## 3. Checks run (all `python3 -I`, `nice -n 19`, one process at a time, each < 10 s)

- **owner_copy/gxcells.py → gxcells_rerun.log.** Byte-identical to the owner log (`diff` empty).
- **gx_cells_ref.py → gx_cells_ref.log.** Independent coverage, the closed form to ρ = 400, the kernel bound, and the GO(e) comparison (numbers above).
- **dz_ld_check.py → dz_ld_check.log.** Uses the `galois` library over GF(2^8) (seed 1, 60 samples) and GF(2^12) (seed 2, 120 samples).
  - **T1 (DZ contrapositive, random A ∈ F_q[X]{τ}).** Whenever A′ ≠ 0 and dim U′ ≥ d+3, the derivative rank is ≥ 3: 170 cases with A′ ≠ 0, 0 failures.
  - **T2 (sharpness).** A = X·S_K + E gives rank exactly 3 at dim U′ = d+3 and exactly 2 at d+2: 360 cases, 0 failures.
  - **T3 (DZ (ii)).** Square coefficients give W′ ⊂ F_q[X²] and √w = A_½(√u): 847 elements, 0 failures.
  - **T4 (LD clause).** A = τ + 1 with 1 ∈ U′ gives constants of dimension dim U′ − 1, the FIX-2 counterexample: 6 cases (dim U′ = 3, …, m/2), all as predicted; the 4 with dim U′ ≥ 4 = d+3 satisfy all of LD's hypotheses.
  - **T5 (LD chain).** Coefficients in F_q[X^{2^K}] give a lossless chain, and adding one odd-degree term gives level-0 rank ≥ 3: 724 checks, 0 failures.
- The checksums are in `checks/checks_SHA256SUMS.txt`.

## 4. FIX entries

**FIX-1 (substantive; scope and ledger).**
- **Where:** title; §4 "New route (GX)", bullet 2 ("supersedes"); §5 "So everything structured now hinges on …".
- **Problem:** GX and GO(e) have incomparable hypotheses.
  - GX needs GLS₁'s degree bound (deg A ≤ ρ − a₂ − 3), which GLS₀ does not give.
  - GO(e) needs only GLS₀, but it uses RB/TSZ and the range a* ≤ (ρ−4)/3.
- **Required change:**
  - Replace "supersedes PTH v2.2 GO(e)'s restriction" with: "complements PTH v2.2 GO(e). Under GLS₁ (or GLS₀ + deg A ≤ ρ − a₂ − 3) it removes the range a* ≤ (ρ−4)/3 and the RB/TSZ inputs. Under GLS₀ alone, GO(e) remains the only route, in its range."
  - In the title, write "… is unnecessary **given GLS₁'s degree bound** …".
  - Keep the GO(e) line in §4 under "Unchanged".

**FIX-2 (substantive; false clause in a [P] statement; Theorem GX unaffected).**
- **Where:** Lemma LD, Setting and Statement.
- **Problem:** "dim W′ = dim U′" fails without injectivity of A on U′ (A = τ + 1, 1 ∈ U′; T4).
- **Required change:** do one of the following.
  - Add "A is injective on U′" to LD's Setting, noting that it is supplied in GX by MI.
  - Or replace the clause with "dim W′ ≥ dim U′ − d > 0".

  Also note in DZ step 2 that injectivity is not needed there: u ↦ A(u)′ factors through W′.

## 5. Minor notes

- **m1.** §0: GLS₁ is quoted without PTH's line clause. Add "(the line clause is automatic by ML)".
- **m2.** §3 [C]: two of the coverage claims can be upgraded to [P] for every even ρ, not just ρ ≤ 40 (proofs in §2):
  - the kernel bound (from a* ≤ ρ/2 − 2);
  - "failures ⟺ g ≡ ρ/2 (mod 2) and g ≤ 3ρ/2, with r = m/4 the unique offending divisor".

  It would also be informative to state that 61 of the 112 gate-passing cells are new relative to GO(e).
- **m3.** §0 / LD: say explicitly that RR_k on W′ follows from RR_k on W^rat by subspace monotonicity, so GX's G2 input is the same as TCR RS(a)'s.
- **m4.** §5 [H]:
  - HFA1's terminal step is BWG after descent to weight 2 (HFD §3, PHFG step 4 [A]), not a constant root.
  - "The kernel bound … is automatic" should read "automatic under GLS₁'s degree bound".
- **m5.** §4 OPEN: phrase it as "(GT) fails ⟺ |χ(G)| ≥ T. By GO(c) this forces t = dim U′ = ρ′ = m/4 > ρ/2, so U′ = λF_{2^{ρ′}}, and χ(G) ⊂ F_{2^{ρ′}}^* lies in no proper subfield."
- **m6.** Consider renaming "Lemma DZ", for example to "Lemma SQ", to avoid a clash with the lane name.
- **m7.** §7 says "Script: scripts/gxcells.py". It is shipped as `owner_scripts/gxcells.py`; align the path, as in PTH v2.2 §8.
- **m8.** GX step 6 could repeat TCR v2.1 RC-1's comparison-direction caveat: the count is ≤ n, or the ≤ 1 α with μ(α) = ∞ is dropped. v > n already covers it, so this is cosmetic.

## 6. Files read

- `referee_GX/src/GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007.md` (full), `src/owner_scripts/gxcells.py`, `src/owner_scripts/gxcells.log`.
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md` (full), plus a directory listing of the handoff.
- `work/DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`, lines 90–140 (PHFG, HFA1 mechanism).
- A grep of `docs/*.md` and `notes/*.md` for RR/HFA1/BWG (matching lines only).
- `DZ_CLOUD_RESULTS/claude_archive/`:
  - `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md` (full);
  - `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md` (full);
  - `DIFFCHECK-PTH-v2.1-20261007.md` (full);
  - a grep of `REVISION-CHECK-PTH-v2-20261007.md` for ML/GLS;
  - `AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md`, lines 1–40 (format only);
  - a directory listing, and a `cmp` of the archived GX note.
- RBL v2.1 was not opened: GX does not use RB/TSZ, and its (B1b) is cited through PTH and TCR.
- Not read: HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads, other scratchpads, PROGRESS.md. No git was used.

## 7. checks/

| File | Purpose |
|---|---|
| `owner_copy/gxcells.py` | Copy of the owner script. |
| `owner_copy/gxcells_rerun.log` | Re-run output; identical to the owner log. |
| `gx_cells_ref.py` and `.log` | Independent coverage, the closed form to ρ = 400, and the GO(e) comparison. |
| `dz_ld_check.py` and `.log` | Numerical tests T1–T5 of DZ and LD (GF(2^8), GF(2^12)). |
| `checks_SHA256SUMS.txt` | sha256 of all of the above. |
