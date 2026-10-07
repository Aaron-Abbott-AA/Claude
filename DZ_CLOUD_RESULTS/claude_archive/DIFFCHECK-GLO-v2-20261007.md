# DIFFCHECK — GLO v2 against v1 and AUDIT-GLO (independent referee, cloud session, 7 Oct 2026, 22:08–22:14Z)

Referee: the same isolated subagent that wrote AUDIT-GLO-GENERIC-LANG-OBSTRUCTION-20261007.md. The same rules and isolation applied, and git was not used.

**Inputs**
- **v1:** `src/GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007.md`, sha256 `3a8a7dbb7d1d1c9cddbe73d41f9204ff09edfe55eaf6ac5e2f7c8bb331136cf2`.
- **v2:** `src/GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md`, sha256 `9b1d48befb6a52b107ed49d177ab9cab293406a1653a8fdd3e9f052ba5faf40f`.
- **Audit:** `AUDIT-GLO-GENERIC-LANG-OBSTRUCTION-20261007.md`, sha256 `43daf52d99a65be34acc3e7f1b50c2002f98d7372424ae42e214da72ef77cb8d`.

## 0. Verdict: **PASS**

- **The fixes.** FIX-1, FIX-2 and m1–m12 are all applied correctly.
- **No other changes.** A line diff shows every removed v1 line and every added v2 line lies inside a block tagged [v2: …], with two exceptions:
  - the status, title and §7 heading updates;
  - the change log itself.
- **No proof was altered**, and no new mathematical claim was introduced beyond the audit's recommendations. One clause, under m2, is new; the referee verified it (§2, c1).
- **v2 is named consistently.** The title says "Owner note **v2** … 22:05Z; v1 21:41Z". The AUDIT STATUS block says v2 and PENDING DIFF-CHECK, and cites v1's sha256 and the audit verdict correctly. §10 is the v1 → v2 change log.
- **Packet EK.** Its GLO v2 copy is byte-identical to the archive v2 (`cmp`, and the sha256 values agree). All 8 rows of `MANIFEST_EK_20261007T2206Z.tsv` verify for size, sha256 and mtime.
- **EK may flip to READY** after these steps:
  1. attach this DIFFCHECK;
  2. update EK's status block;
  3. regenerate MANIFEST_EK last, since EK.md will change;
  4. do the usual device-only steps (re-list to_claude/, receipts and ACKs).
- **Four cosmetic notes (c1–c4) are optional and do not block.**

## 1. Item-by-item

| Item | Audit request | Where in v2 | Applied? |
|---|---|---|---|
| FIX-1 | Restrict NG to W = R_P. State the band's dim W = ρ ≤ (m−6)/3 and real type only at α = 1. Withdraw "necessary". Add [OPEN]. | Title; Scope; §5 "Scope of NG" (two lists: features not modelled, and restricted message [P]/[OPEN] with the referee's [H] count and [P] ηF_{2^ρ} remark); §6(a) ("withdrawn"); §6(f) | **Yes.** The wording matches the audit, the referee attributions are correctly labelled, and §6(c) is retained unchanged. |
| FIX-2 | "Exact" means per fixed n; a semi-decision; AC failure certificate. | Title; new "Scope of 'exact'" block after Theorem OB; §1 Remark (failure certificate) [P, referee; adopted]; §6(a); §6(f) (degree bound [OPEN]) | **Yes.** The example A(τ^{m/2}+1) and the MI remark are correct. |
| m1 | NG: m ≥ 4; "≤ m/2"; G-stable; reason for uniqueness. | §5 NG | **Yes** |
| m2 | Define generic a(W). | §0 "Generic defect" | **Yes**; see c1 |
| m3 | RD: "nonempty". | §3 RD | **Yes** |
| m4 | OB1(c): explicit identity, not a Kummer condition. | §4 | **Yes** |
| m5 | TB: "lies in ker λ". | §2 TB | **Yes.** It is restated as "solutions of degree ≤ n are exactly the truncations … whose top block lies in ker λ", which is correct. |
| m6 | DO: drop deg d₀ > deg c₀. | §5 DO | **Yes.** "θ may have either sign"; "both of the following". |
| m7 | R0 [COND]: plentiful, nonzero, twist-invariance. | §0 R0 | **Yes**, still under the [COND] label. |
| m8 | "No generic analogue" labelled [H]. | §4 after PV | **Yes** |
| m9 | TH: threshold with v′. | §4 TH Consequence | **Yes.** "Yields GLS₁ when (4Q+4)δ < v′", and it "can never apply unless δ < q/(4Q+4)". Both are correct. See c2. |
| m10 | Negative control relabelled ad hoc. | §3 [C], §9 | **Yes** |
| m11 | T3 planted split. | §2 [C] T3, §9 | **Yes.** The figures 29/32 and 30/32 (5 negatives) match the logs, and the referee figures (404 instances, 0 mismatches) match the audit. |
| m12 | ML over L̄; Kummer extension Galois. | §0 R0, §1 GR | **Yes** |
| — | Referee check citations in §2 and §9 | §9 "Referee checks" | **Correct.** The archived `audit_GLO_checks/` matches the audit's `checks_SHA256SUMS.txt` (16/16 OK; the sums file is byte-identical). |

Unchanged (verified by diff): FS, GR (apart from the m12 line), the AC statement, the OB statement and proof, the TB formula, the RLE statement and proof, N1, OB1 (a)–(c) proofs, PV, the Hermitian remark, VO, the NG computations, §7(a)–(c), §8 and the §9 table. Section 7's heading now reads "(packet EK, PENDING DIFF-CHECK)", which is a status edit only.

## 2. Cosmetic notes (optional; none blocks)
- **c1 (m2's new clause).** "For W ⊂ F_q this agrees with the pointwise half-field defect of HFD." This is **true**. A one-line reason could be added:
  - [P, referee sketch] The relation space of a finite W ⊂ F_q has an F_q-basis.
  - If (C, D) over F_q is a relation, then so is (D^{(Q)}, C^{(Q)}), because w^{Q²} = w.
  - So (E, E^{(Q)}) with E := ζC + ζ^QD^{(Q)} is a real relation of no larger degree, and E(W) ⊂ F_Q.
  - E is nonzero for some ζ ∈ F_q^*. Otherwise C = D = 0, using ζ = 1 together with any ζ having ζ^{Q−1} ≠ 1.
  - The converse is immediate.
- **c2.** TH's Consequence uses real type at α ∈ N, which comes from HFD §1 [A] and (B1b). It could carry "[COND (B1b), HFD §1 [A]]" rather than sitting under TH's [P] header. The same structure was already in v1, so this is not a regression.
- **c3.** EK §3(a) says "G1 needs G1″ directly", while GLO §7(a) says "G1 needs another route". The note's phrasing is the safer one; consider aligning EK with it.
- **c4.** The [P, referee] ηF_{2^ρ} remark uses a₂ < ρ/2, which always holds in the setting (a₂ ≤ a* < ρ/2). It could be stated.

## 3. Packet EK verification (`/home/user/Claude/DZ_CLOUD_RESULTS/outbox_for_user_delivery/to_codex/`)
- **The GLO v2 copy** (`GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md`) has sha256 `9b1d48be…faf40f`. It is identical to `claude_archive/` and to the referee's `src/` copy (`cmp`: IDENTICAL).
- **The MANIFEST_EK rows.** All 8 match the files on disk for size, sha256 and mtime:
  - EK_20261007T2206Z.md;
  - GLO v2;
  - AUDIT-GLO;
  - glocheck.py.txt;
  - glocheck.log;
  - glocheck_seed7.log;
  - glovo.py.txt;
  - glovo.log.
- **Other attachments.**
  - AUDIT-GLO in to_codex is byte-identical to the archive copy.
  - `glocheck.py.txt` and `glovo.py.txt` are byte-identical to `claude_archive/scripts/glocheck.py` and `glovo.py`.
- **EK.md.** It is still marked "PENDING DIFF-CHECK — NOT READY", which is correct for now. Its §2 summary is consistent with v2: FIX-1 scope, FIX-2 semi-decision, v′ threshold and m ≥ 4.
- **Required when EK flips to READY:**
  - add DIFFCHECK-GLO-v2-20261007.md to the attachments;
  - edit the status block;
  - regenerate MANIFEST_EK last, because EK.md's sha256 will change.

## 4. Files read
- `referee_GLO/src/GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md` (full), and v1 (from the audit).
- `outbox_for_user_delivery/to_codex/EK_20261007T2206Z.md` and `MANIFEST_EK_20261007T2206Z.tsv` (full).
- Hashes and `cmp` only for the other EK attachments, the archive copies, and `claude_archive/audit_GLO_checks/`.
- Nothing outside the DZ scope was read, and nothing in DZ_CLOUD_RESULTS was modified except adding this file to `claude_archive/`.
