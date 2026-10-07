# DIFFCHECK — RX v2 against v1, and the packet EL contents

Diff check by the referee who audited RX v1 (AUDIT-RX-RATIONAL-BAND-COUNTEREXAMPLE-20261007.md, sha256 7cfed7981b1e70574906fbca7f6b9feb287a96ce2d50dfc9597b8bbebc59b0a8). Written 7 Oct 2026, 22:35Z (`date -u` checked). The same isolation rules apply: only DZ files were read, no git was used, and no owner script was executed.

- **v1:** `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007.md`, sha256 `ff4da8dd5631fc79bcf20e946ef822d3b3fcaaa33181e46538509517942d76c7`.
- **v2:** `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md`, sha256 `fcecc2c7758565594e3d02f4da64f81d2da17a8407069898dd50c10a74610e18`, 17180 bytes.
  - The referee's `src/` copy, the `claude_archive/` copy and the `outbox_for_user_delivery/to_codex/` copy are byte-identical.

## Verdict: **PASS**
- Every FIX and minor item is correctly applied.
- The adopted referee argument is reproduced faithfully and credited.
- Nothing else changed in substance.
- The title, the status line and the change log all name v2.
- The packet EL files match MANIFEST_EL exactly.

**EL may flip to READY** once this file is attached and MANIFEST_EL is regenerated last, as EL's own status note and README-PENDING require.

## 1. Item-by-item check (from `diff v1 v2`)

| Item | Where in v2 | Check | Result |
|---|---|---|---|
| FIX-1 | Title; RX(vi-a)/(vi-b); proof step 7; §2 [C](B); §4(a); §6; §8 | (vi) is replaced by the referee argument: rank of N(α) off Z; F₂-independence of 1, α, …, α^{2a}; the kernel line spanned by (C_α, D_α); σ-stability; Hilbert 90 giving κ = λ^{Q−1} with κ^{Q+1} = 1. The bound \|Z\| ≤ deg M_{2a+2} = (a−1)2^{a+1} + 2 + Q[(2a−1)2^a − a + 1] < 2a·2^a·Q, with \|Z\|/q < a·2^{−2a−4} ≤ 1/64 for m ≥ 6a+9. Formulas re-checked against the audit and the exact E2 degrees (2Q+2, 11Q+10, 38Q+34). The HFD §1 [A] dependence is removed, with the reason. "Almost every" becomes "> 63q/64 points" in the title and §4(a). Credited as "[P, referee; adopted]". [C, referee] numbers are quoted correctly. | OK |
| m1 | RX(iv) | Cites GLO v2 FS(b) for L^sep → L̄. The referee's GF(2^61) Δ·Ω₁ check is quoted correctly and labelled [C, referee]. | OK |
| m2 | §3 | ρ ≥ 2a₂+4 in the band, equal to the G1″ threshold. The intermediate dimensions 2a₂+2 and 2a₂+3 are noted. | OK |
| m3 | §3 | The hypothesis a < m/2 is added. The F_q-scaled monomial extension is credited to the referee. | OK |
| m4 | §3 | Completeness for polynomial roots and no pole at X = 0 are labelled [C, referee K1]. Poles at other finite places are marked untested. K2/K3 are quoted correctly (dimensions 3 and 5 = W; F_q[X]_{≤10} has dimension 3). | OK (remark R1) |
| m5 | §4(c) | "Logically independent" is replaced by the two directions (RX, RW). | OK |
| m6 | §2 [C] | Script cosmetics recorded; script unchanged, so its hash is preserved. | OK |
| m7 | §2 heading; RX(v) | Now "the dimension range 2a₂ < dim W ≤ (m−6)/3 posed by GLO FIX-1". The odd-parity remark is added. | OK |
| m8 | §6 | The (vi) self-check is updated. | OK |
| Status | Header; §5 heading | The audit status block names v1's hash, the audit's hash (7cfed798…59b0a8, correct) and the verdict, and says v2 is PENDING DIFF-CHECK. §5 is retitled "packet EL, PENDING DIFF-CHECK", which is administrative only. | OK |
| Change log | §8 | Present and accurate. It says "No other proof was changed", which the diff confirms: Lemma RW, RW′, RX(i)–(iii), proof steps 1–6 and §4(b) and §4(d) are verbatim from v1. | OK |

- **No unflagged substantive change.** The only unmarked edits are the status block, the §5 heading and the §2 [C](B) cross-reference, all administrative.
- **`audit_RX_checks/` in claude_archive.** This is the coordinator's copy of the referee checks. All 8 files verify against `checks_SHA256SUMS.txt`, which is identical to the referee's (sha256 81ceccebb7bac30d249d4ea749f7e3baad9cd5c56f1b6f72387b5cbb6750bf3e).

**Remark R1 (non-blocking; no edit required).** m4's sentence "any polynomial root of P has degree ≤ 2a" is labelled [C, referee K1]. It was verified only for the tested (a, m): (1,16), (1,18), (1,20), (2,22) and (3,28). It covers every search it is applied to. If the owner revises again for any other reason, add "(in the tested (a, m))".

## 2. Packet EL_20261007T2232Z (outbox_for_user_delivery/to_codex/)
- **RX v2.** The outbox copy is byte-identical to the archive v2 (fcecc2c7…0e18).
- **MANIFEST_EL_20261007T2232Z.tsv.** Every row matches sha256, size and mtime (via `stat`):

| File | Size | sha256 | Match |
|---|---|---|---|
| EL_20261007T2232Z.md | 2969 | 99fa78547d4d9e97e9b97bfc340648be06fd21dec4271cf153909d22f1aa2dc6 | yes |
| RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md | 17180 | fcecc2c7758565594e3d02f4da64f81d2da17a8407069898dd50c10a74610e18 | yes |
| AUDIT-RX-RATIONAL-BAND-COUNTEREXAMPLE-20261007.md | 20407 | 7cfed7981b1e70574906fbca7f6b9feb287a96ce2d50dfc9597b8bbebc59b0a8 | yes (unedited; equals the referee's original) |
| rxcheck.py.txt | 6462 | a53dcda9d24ca7291f5fa2726cf743405ebfc23cca96d3db61177ced88f9f047 | yes (equals archive scripts/rxcheck.py) |
| rxcheck.log | 2350 | 16a5315f2bddfb4891b5e264374473559876a676a57d0a650da3eb45abf2ae53 | yes |

- **The EL cover's mathematical summary is consistent with v2.** It covers RW/RW′, RX, > 63q/64 real type credited to the referee, the odd dimension, ρ ≥ 2a₂+4 and the questions.
- **The EL cover is still marked PENDING DIFF-CHECK.** To flip it:
  1. attach this file;
  2. change the status line to READY;
  3. regenerate MANIFEST_EL last, because EL's hash will change.

## 3. Files read
- `referee_RX/src/RX-…-NOTE-20261007.md` and `-v2.md` (diff).
- `claude_archive/`: the RX v1 and v2 copies and the AUDIT-RX copy (hashes); `audit_RX_checks/` (hash verification).
- `outbox_for_user_delivery/`: `to_codex/EL_20261007T2232Z.md`, `MANIFEST_EL_20261007T2232Z.tsv`, the listed attachments (hashes and stat), and README-PENDING.md (grep for EL).
- Nothing outside DZ was read.
