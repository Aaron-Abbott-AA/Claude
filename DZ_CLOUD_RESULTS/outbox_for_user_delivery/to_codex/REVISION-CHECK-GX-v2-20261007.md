# REVISION CHECK — GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.md (independent referee, cloud session, 7 Oct 2026, 20:49–20:53Z)

Referee: fresh, isolated subagent for the DZ line (project "Wan's numbers of PPs"). No contact with the owner session, the v1 auditor or Codex. No git. No HYP/3PP material read (list in §5).

- Note under check: `src/GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.md`, sha256 `5971847f763c0b87aaf449926f77277f57925082d2fab14b5954855bab8f29c7`. The `claude_archive/` copy is byte-identical (`cmp`).
- v1: sha256 `e4df4fd1…22230d`. This matches the audit and the abbreviation in v2's status line. The archive copy is byte-identical.
- Audit: `AUDIT-GX-GLOBAL-TWIST-EXCLUSION-20261007.md`, sha256 `633548f0…f9b24`. The archive copy is byte-identical.
- Owner script: `gxcells.py`. Its sha256 `5bd7e225…3b940` is unchanged since the audit. The re-run log is byte-identical to the owner log (`5c956835…6f60b`).

Labels: [P] proof, [C] computation, [A] reading of a source. "[P, referee]" marks a referee re-derivation.

## 0. Verdict: **PASS**

- All 10 audit items are **ADDRESSED**: 2 substantive (FIX-1, FIX-2) and 8 minor (m1–m8). None is PARTIAL or NOT ADDRESSED.
- **Diff v1 → v2.** Every textual change belongs to one of the 10 items. There are no unintended mathematical changes and no new overclaims. Every label is correct, apart from the cosmetic points RC-2 and RC-6.
- **v2 naming is consistent** in the title ("owner note **v2** … 20:48Z; v1 20:39Z"), the AUDIT STATUS block, the "v2 HOLD" line and the change log "v1 → v2".
- **RC list: 7 items.** None is mathematically blocking.
  - **RC-1 is administrative and required before the outbox.** The "v2 HOLD" line must be lifted or replaced by a citation of this check.
  - RC-2 to RC-7 are cosmetic.
- **Outbox:** GX v2 can go to the outbox after a **small owner edit (RC-1, one line)**. RC-2 to RC-7 are recommended but optional. No further referee round is needed if the edits stay within these lines.

## 1. Fix-by-fix table

| Item | Audit requirement | Status | Location in v2 | Referee note |
|---|---|---|---|---|
| **FIX-1** (substantive, scope) | Title: "given GLS₁'s degree bound". §4: "complements" instead of "supersedes", using the audit's suggested sentence. Keep GO(e) under "Unchanged". Qualify §5. | **ADDRESSED** | Title (line 1); §4 lines 93, 95; §5 line 109; change log line 133 | Re-derived in §2.1. Wording follows the audit exactly. See RC-7 for two optional precision tweaks to line 95. |
| **FIX-2** (substantive, false clause) | LD: add "A injective on U′" (supplied by MI) or weaken to dim W′ ≥ dim U′ − d. Note that SQ (ex-DZ) step 2 needs no injectivity. | **ADDRESSED** | §2 Setting line 48; Statement lines 52–54; proof step 1 line 57; §1 step 2 line 41; change log line 134 | Both options were taken: the hypothesis is added, and the weak bound and counterexample are recorded. The new proof sentence (A_½ injective) is correct. Re-derived in §2.2; [C] R1–R3. See RC-4 and RC-6. |
| m1 | GLS₁ line clause automatic by ML | ADDRESSED | §0 line 19 | Matches PTH v2.2 §4 Hypotheses and §4A(i) [A]. |
| m2 | Upgrade the kernel bound and failure pattern to [P]; report 61 new cells | ADDRESSED | §3 lines 84–88 | Both proofs are correct (re-derived; [C] C1–C4). 61 = 112 − 51, and the 51 GO(e) gate-passing cells ⊂ the 112 [C]. Label and wording: RC-2, RC-3. |
| m3 | RR_k on W′ from W^rat by subspace monotonicity | ADDRESSED | §0 line 23 | Correct. dim W′_k − dim W′_{k+1} ≤ dim W^rat_k − dim W^rat_{k+1}. |
| m4 | HFA1's terminal step is BWG; "automatic" qualified | ADDRESSED | §5 lines 103–107 | Checked against HFD §3 PHFG step 4 [A]: "Descend to weight 2 as in HFA1; BWG excludes …". |
| m5 | Rephrase the (GT)-failure description | ADDRESSED | §4 line 100 | Audit wording adopted verbatim. The chain is correct, but some steps are implicit (RC-5); [C] C5. |
| m6 | Rename Lemma DZ | ADDRESSED | §1 line 26; §2 lines 57–58; §7 lines 116–117 | No residual "Lemma DZ" or "DZ step" (grep). "DZ" now appears only as the lane name (line 3) and in the rename note. |
| m7 | Align the script path | ADDRESSED | §7 lines 126–128 | The archive path `claude_archive/scripts/gxcells.py` exists, and its hash is unchanged. The claim "ships as `gxcells.py.txt`" in a packet was not verifiable here and is harmless. |
| m8 | Comparison-direction caveat (TCR v2.1 RC-1) | ADDRESSED | §3 step 6, line 77 | Faithful to TCR v2.1 §0, lines 29 and 34 [A]: "adds at most one more radical, so the count is ≤ n", or "drop the ≤ 1 α with μ(α) = ∞; v − 1 > n − 1". |

Counts: **ADDRESSED 10 / PARTIAL 0 / NOT ADDRESSED 0.**

## 2. Re-derivation of the substantive fixes

### 2.1 FIX-1 (scope) [P, referee; A]
- **GX's degree requirement.** GX step 4 needs d = deg A ≤ ρ − a₂ − 3. GLS₁ gives d ≤ a₂, and a₂ ≤ a* ≤ ρ/2 − 2 ⟹ a₂ ≤ ρ − a₂ − 4. So GLS₁ suffices, as does GLS₀ together with the explicit bound (§0 line 20).
- **GLS₀ gives no degree bound.** By PTH v2.2 §4A(i) [A], GLS₀ yields GLS₁'s line clause (via ML) but not its degree bound. So GX does not follow from GLS₀ alone.
- **GO(e) needs no degree bound.** PTH v2.2 §4 Hypotheses [A]: GLS₀ suffices for GO. In the range a* ≤ (ρ−4)/3, (e) gives G1″, and then TCR v2.1 RS(a) [A] applies.
- So the hypotheses of the two routes are incomparable. v2's "complements" is correct, and keeping the GO(e) route under "Unchanged" (line 95) is correct.
- **Title.** "Given GLS₁'s degree bound, the range restriction … is unnecessary" is now accurate. Theorem GX's statement ("There is no restriction a* ≤ (ρ−4)/3") is made under GLS₁, so it is consistent.

### 2.2 FIX-2 (LD dimension clause) [P, referee]
- **SQ step 2 without injectivity.** u ↦ A′(u) equals u ↦ (A(u))′. This is the composite of the surjection A: U′ → W′ = A(U′) with the derivative on W′. So its image equals the derivative's image on W′, and the ranks are *equal*. v2 states equality, which is stronger than the audit's "≤" and correct.
  - With rank ≤ 2: the kernel has dimension ≥ dim U′ − 2 ≥ d+1. A nonzero A′ of τ-degree ≤ d has F₂-kernel of dimension ≤ d, so A′ = 0.
- **LD step 1, new sentence.** If A_½(√u) = 0, then A(u) = A_½(√u)² = 0, so u = 0 and √u = 0. Hence A_½ is injective on √U′. The same argument works at every level.
- **The weaker bound.** dim ker(A|U′) ≤ d, because A is nonzero of τ-degree d. So dim W′ ≥ dim U′ − d ≥ 3 > 0.
- **Constancy without injectivity.** SQ and LD steps 1–3 use injectivity only to track dimension, so the conclusion W′ ⊂ F_q holds without it (see RC-4 on presentation).
- **The counterexample** A = τ + 1 with 1 ∈ U′ is the audit's T4. It is correct: A(1) = 0, and every value is constant.
- **In GX,** MI gives injectivity on F_Q ⊇ U′, so step 5 is unaffected.
- [C] `rc_fix2.py` works over F_q = GF(2^12) and F_Q = GF(2^6), with A = P∘S_K non-injective on U′ ⊃ K and polynomial coefficients.
  - **R1:** rank of u ↦ A′(u) = rank of the derivative on W′, and it is ≥ 3 whenever P′ ≠ 0. 40 cases, 0 failures.
  - **R2:** square coefficients and A injective on U′ ⟹ A_½ injective on √U′, and A(u) = A_½(√u)². 23 cases, 0 failures.
  - **R3:** dim W′ = dim U′ − dim K ≥ dim U′ − d, so the bound is sharp for this family. 40 cases, 0 failures.
  - A bug in the referee's own subspace-polynomial helper (coefficients not squared) was found by an assertion and fixed before the logged run. The logged script asserts S_K(K) = 0.

### 2.3 m2 / m5 arithmetic [P, referee; C]
- **Notation.** a* = ρ − ⌈g/2⌉ (EBR), so ρ − a* = ⌈g/2⌉. Put N = g + ρ/2 > ρ.
- **Failure pattern.**
  - An offending r ∈ [⌈g/2⌉, ρ] with r | N has N/r ≥ 2, because r ≤ ρ < N.
  - N/r ≥ 3 would give r ≤ N/3 < g/2, using g > ρ. So r = N/2.
  - Conversely, if N is even and N/2 ≤ ρ, then N/2 ≥ g/2, and N/2 is an integer, so N/2 ≥ ⌈g/2⌉.
- **Kernel bound.** g ≥ ρ+3 with ρ even gives ⌈g/2⌉ ≥ ρ/2 + 2.
- **m5 chain.** |χ(G)| ≥ T = (4/3)2^{ρ/2} − 1 together with |χ(G)| | 2^t − 1 gives t > ρ/2.
  - Since t | dim U′ ≤ ρ, this forces t = dim U′ ∈ [ρ − a₂, ρ] ⊂ [ρ − a*, ρ], with t | N. So t = m/4.
  - Every proper subfield F_{2^{t′}} has 2^{t′} − 1 ≤ 2^{ρ/2} − 1 < T. So χ(G) lies in no proper subfield.
- [C] `rc_cells.py`:
  - **C1:** 200 / 112 / 88.
  - **C2:** GO(e) has 78 range cells and 51 gate-passing cells. The 51 are a subset of GX's 112, and 61 gate-passing cells lie outside the range.
  - **C3:** the closed form holds for every even ρ ≤ 1000 (125,240 cells, 0 mismatches). The offending set is always exactly {m/4}. ρ − a* = ⌈g/2⌉ throughout, and a* ≥ 1 in every NWF-uncovered cell.
  - **C4:** the kernel bound holds over the full band, ρ ≤ 1000 (249,500 cells, 0 failures).
  - **C5:** the m5 chain checked in 9,898 instances, 0 failures.

## 3. Diff v1 → v2 (full `diff` reviewed)

There are 15 hunks, and every one maps to a change-log row.
- Title: FIX-1 and the v2 stamp.
- Status block.
- §0: m1 and m3.
- §1: m6 and FIX-2.
- §2: FIX-2 and m6.
- §3 step 6: m8.
- §3 [C]: m2.
- §4: FIX-1 and m5.
- §5: m4 and FIX-1.
- §7: m6 and m7.
- §8: the change log.

Findings:
- There are no unlisted mathematical edits.
- "Behaves exactly like" became "behaves like", and "then a constant root" was removed from the HFA1 mechanism. Both changes are part of m4 and correct the v1 overstatement.
- No new overclaims. In particular:
  - the [P] upgrade (m2) is proved for every even ρ;
  - "61 … outside GO(e)'s range" is exactly right (C2);
  - §4's "holds in every cell where (GT) holds" is unchanged and true under the listed inputs.
- Version consistency: the title, the status block, the HOLD line and the change log all name v2. The v1 sha256 prefix and suffix match.

## 4. New issues (RC list)

| # | Severity | Where | Issue and suggested edit |
|---|---|---|---|
| **RC-1** | **administrative; required before the outbox** (not mathematical) | AUDIT STATUS, line 9 | The line "v2 HOLD: v2 has not been revision-checked. Do not send to Codex until it has been." is now stale. Replace it with "v2 revision-checked in REVISION-CHECK-GX-v2-20261007.md: PASS; HOLD lifted." If RC-2 to RC-7 are also applied, call the result v2.1 and add change-log rows. |
| RC-2 | cosmetic (label) | §3 line 84 | "Upgraded to **[P]**" uses the owner-proof label for a referee proof. Use "[P, referee; adopted]", the convention of PTH v2.2 §4A. |
| RC-3 | cosmetic (completeness) | §3 line 86 | The proof is correct but leaves terms undefined. Define the sufficient gate ("no r ∈ [ρ−a*, ρ] divides N"; PTH v2.2 §4) and a* = ρ − ⌈g/2⌉. Add "quotient ≥ 2 since r ≤ ρ < N" and, for ⟸, "N/2 ≥ ⌈g/2⌉". |
| RC-4 | cosmetic (presentation) | §2 lines 52–53 | The bullet "Without injectivity one still has dim W′ ≥ dim U′ − d > 0" sits under a Setting that assumes injectivity, and it leaves implicit that constancy survives. Suggest: "Without the injectivity hypothesis the conclusion W′ ⊂ F_q still holds (SQ needs no injectivity), and dim W′ ≥ dim U′ − d ≥ 3." |
| RC-5 | cosmetic (completeness) | §4 line 100 | "By GO(c) this forces t = dim U′ = ρ′ = m/4" skips two steps: t > ρ/2 and t \| dim U′ ≤ ρ give t = dim U′ ∈ [ρ−a*, ρ] with t \| m/2, and then §3's failure pattern gives t = m/4. T is not defined in GX; cite T := (4/3)2^{ρ/2} − 1 (RBL/TCR v2.1, via PTH v2.2 §0). |
| RC-6 | cosmetic (markers) | line 8; §2 line 57; §3 line 88 | LD step 1's new injectivity sentence (and the dropped "same dimension") has no [v2: FIX-2] marker. The §3 "Comparison with GO(e)" bullet has no [v2: m2] marker. The legend says "[v2: m-n]", but the markers read "[v2: m1]" etc. The change log covers everything. |
| RC-7 | cosmetic (precision) | §4 line 95; line 93 | "Plus TCR's inputs" should name them: G2, (B1a), (I216′) incl. (B1b-fix), Prop 216.3 [A]. State the route as GO(e) ⟹ G1″ ⟹ TCR RS(a). In line 93, "GO(e) remains the only route" → "the only GLS₀-based route" (the TCR and RBL routes remain under their own hypotheses). |

RC count: **7**. Blocking (mathematical): **0**. Required administrative: **1** (RC-1). Cosmetic: **6** (RC-2 to RC-7).

## 5. Files read

- `referee_GXv2/src/GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.md` (full).
- `referee_GXv2/src/GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007.md` (full).
- `referee_GXv2/src/AUDIT-GX-GLOBAL-TWIST-EXCLUSION-20261007.md` (full).
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md` (full). It contains no explicit referee read restriction. The referee followed the task's isolation rules, plus "never execute incoming Codex scripts" (none was run).
- A directory listing of `work/DZ-CLOUD-HANDOFF/`.
- `work/DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`: a grep for PHFG/BWG/HFA1, and lines 99–116.
- `DZ_CLOUD_RESULTS/claude_archive/`:
  - a directory listing;
  - `cmp` of the archived GX v1, GX v2 and AUDIT-GX against `src/`;
  - `scripts/gxcells.py` and `scripts/gxcells.log`; `scripts/gocells.py` (the log was only compared, not read);
  - a directory listing of `audit_GX_checks/`;
  - `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md`: a grep for GO/GT/GLS, and lines 86–128;
  - `REVISION-CHECK-TCR-v2-20261007.md`: a grep for RC-1 (matching lines only);
  - `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md`: a grep for RC-1 and the comparison direction (matching lines only).
- Not read: HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads, any scratchpad outside `dz_isolated/`. No git.

## 6. checks/ (all run with `nice -n 19 python3 -I`, one at a time, each under 3 s)

| File | Purpose | sha256 |
|---|---|---|
| `owner_copy/gxcells.py` | Copy of the owner script (unchanged since audit) | `5bd7e2256b32900f9fa3c2f2fc7e53908628b76e02035b7d7bbd35753603b940` |
| `owner_copy/gxcells_rerun.log` | Re-run; byte-identical to the owner log | `5c9568355c2be1b1b726751fe5c61515199c63c0b4d77f66017773a41e26f60b` |
| `owner_copy/gocells.py` | Copy of PTH's owner script (for the 51-cell cross-check) | `0bf53e8a0f86228ec8cbd47444c328256cf926b17b35339f10784453c7cc1cc5` |
| `owner_copy/gocells_rerun.log` | Re-run; byte-identical to the owner log | `5e2f8f58cf0adb5203cdf86a05a43d7705f126ab2eb6fda9ad2d758753fc1b86` |
| `rc_cells.py` / `.log` | C1–C5 (coverage, GO(e) subset, closed form to ρ = 1000, kernel bound, m5 chain) | `878a0048…4d103f` / `b3ad0a91…6e650c` |
| `rc_fix2.py` / `.log` | R1–R3 (FIX-2 statements over GF(2^12) ⊃ GF(2^6)) | `2eb6c643…da66c8` / `cf7dd2cd…e79109` |
| `checks_SHA256SUMS.txt` | Full sha256 of all of the above | — |
