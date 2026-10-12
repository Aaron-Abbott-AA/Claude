# FINAL HANDBACK — DZ cloud sessions (7–12 Oct 2026) → the local session "(Active) DZ (2)" (session_01JBo5c8BAGb4ugZEpxorNDq)
Written 12 Oct 2026, 00:07Z. **This is the last DZ step in the cloud.** It supersedes every earlier HANDBACK-*.md; those files are kept unchanged.
The cloud container was **never linked to the Mac** and had **no mailbox access**. Nothing has been delivered to Codex, and **no ACKs have been given**.

## 1. State of every note (all in `DZ_CLOUD_RESULTS/claude_archive/`)
| Note | Current file (sha256 prefix) | Review chain | Content (labels) | Packet |
|---|---|---|---|---|
| **RBL** | RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md (f3a2e176) | audit PASS-with-fixes → revision check PASS | TX, TSZ, RB, RD(a) [P]; RD(b)–(d) [COND G2] | EF — READY |
| **TCR** | TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md (4b2d969b) | audit PASS-with-fixes → revision check PASS | HF [P]; CD, TC, RS [COND] | EG — READY |
| **PTH** | PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md (9ecf61da) | audit → revision check PASS-with-fixes → diff check | LS, MI, PTH, ML [P]; GO [COND GLS₀, (GT), G4, WG, (B1a⁺), (B1b)] | EH — READY |
| **GX** | GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.1.md (2b2a1d69) | audit → revision check PASS | SQ [P]; LD [P mod RR_k]; GX [COND] | EI — READY |
| **KB** | KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.1.md (1cc7fc50) | audit → revision check → diff check PASS | KB (i)–(vi) [P under GLS₁, (B1a⁺), (B1b)]; general B = 1 OPEN | EJ — READY |
| **GLO** | GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md (9b1d48be) | audit PASS-with-fixes → diff check PASS | FS, GR/AC, OB/TB (per degree), RLE, RD/N1, OB1 (Δ·Ω₁), PV, TH, VO/DO, NG (W = R_P) [P] | EK — READY |
| **RX** | RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md (fcecc2c7) | audit PASS-with-fixes → diff check PASS | RW/RW′ (Kummer divisibility), RX: W = F₂[X]_{≤2a} has no twist; real type > 63q/64 (referee proof) [P] | EL — READY |
| **SH** | SH-SUBHALFFIELD-CRITERION-NOTE-20261007-v2.md (05f8fd30) | audit PASS-with-fixes → diff check PASS | SH: GLS₀ ⟺ W ⊇ A(U), dim U > a₂ + deg A [P]; Claim U (referee); RK (a = 1: ker P ∩ L = W) [P] | EM — READY |
| **KP** | KP-RX-ROOTSPACE-GALOIS-NOTE-20261007-v2.md (b8a80414) | audit PASS-with-fixes → **diff check PENDING** | FR, GS [P]; KP: no G-stable band-dimensional subspace of RX's R_P (a = 1, m = 24..44) [P + C]; KL (m = 10, 14, 18) | EN — **PENDING DIFF-CHECK** |

The audits, revision checks and diff checks sit next to each note in `claude_archive/`, with referee checks in `audit_*_checks/` and `revcheck_*_checks/`. Owner scripts are in `claude_archive/scripts/`.

## 2. Packets in `outbox_for_user_delivery/to_codex/` (delivery order EF → EN)
| Packet | Cover (sha256 prefix) | Manifest (prefix) | Status |
|---|---|---|---|
| EF_20261007T1917Z (RBL) | 3fde9902 | MANIFEST.tsv (558079f6) | READY FOR USER DELIVERY |
| EG_20261007T1948Z (TCR) | d1e46b68 | MANIFEST_EG_… (c272ebfd) | READY |
| EH_20261007T2036Z (PTH) | 1865a79c | MANIFEST_EH_… (75e7453e) | READY |
| EI_20261007T2056Z (GX) | 0ac56b0f | MANIFEST_EI_… (1a122b2d) | READY |
| EJ_20261007T2120Z (KB) | b8eda808 | MANIFEST_EJ_… (6596167c) | READY |
| EK_20261007T2206Z (GLO) | 50b89fbf | MANIFEST_EK_… (d46d6611) | READY |
| EL_20261007T2232Z (RX) | 8e0a4d5d | MANIFEST_EL_… (0b4ae6de) | READY |
| EM_20261007T2301Z (SH) | 0278d555 | MANIFEST_EM_… (043ebbb0) | READY |
| **EN_20261012T0006Z (KP)** | aaf7a1f8 | MANIFEST_EN_20261012T0006Z.tsv (f070794b) | **PENDING DIFF-CHECK — do NOT deliver yet** |

- `superseded/` must **never** be delivered.
- Some notes' own status lines still read "PENDING DIFF-CHECK". In each case the hold is discharged by the attached diff check, and the notes were not re-edited, to keep their checked hashes.

## 3. Device steps still pending (local session only)
1. **Diff check of KP v2.**
   - Arrange a referee diff check of KP v2 against v1 and AUDIT-KP.
   - If it passes, add `DIFFCHECK-KP-v2-20261007.md` to to_codex, flip EN's status block to READY, and regenerate MANIFEST_EN last.
2. **Verify and copy.** Run `date -u`. Verify the sha256 values against `DZ_CLOUD_RESULTS/PROGRESS.md`, then copy `claude_archive/*` (including all `audit_*`/`revcheck_*` folders) to `CODEX_CLAUDE_EXCHANGE/DZ/claude_archive/`.
3. **New Codex files.** Re-list `DZ/to_claude/` for files newer than **15:13:17Z on 7 Oct 2026**, read the new covers, and generate the receipt TSV on the device (mtime, `stat -c %s`, `sha256sum`, name). **Never execute incoming scripts.**
4. **ACKs.** Fill in §1 of EF … EN with separate ACKs for RECEIVED, READ and ADOPTED. Regenerate each changed manifest last.
5. **Deliver** EF, EG, EH, EI, EJ, EK, EL, EM and then EN to `DZ/to_codex/`, following `outbox_for_user_delivery/README-PENDING.md`. Verify the sha256 values on the device.
6. **Memo §216.** Re-read it for Prop 216.3's frame hypotheses ((I216′), (B1b-fix)).
7. **Earlier replies.** Record any reply to EE and PRIMARY's G23O review.

## 4. Open research targets, in priority order
1. **Codex answers** to the questions in EK §3, EL §3, EM §3 and EN §3.
   - The valuations of B1's (c₀, d₀, c_{a₂}, d_{a₂}): do VO/DO or RW′ trigger?
   - Do STT/MRL give a twisted half-field A(U) ⊂ W with dim U > a₂ + deg A (equivalent to GLS₀ by SH), or the RLE solution B ∈ L{τ}?
   - Is Δ·Ω₁ ≡ 0 in a₂ = 1 cells?
   - An explicit B1 relation for a small band cell, for the KP Frobenius test.
2. **GLS₀/GLS₁ for the arc family** (the central gap) [OPEN].
   - Equivalent (SH) to "generic PTH (ii)": the arc radical W contains a large twisted half-field.
   - GO/GX/KB remain [COND] on it.
3. **The even-band non-implication question** [OPEN]. Is there a G-stable W with 2a₂+4 ≤ dim W ≤ (m−6)/3 and a unique (N0) relation (automatic under a₂ = a(W) by Claim U) but no twist?
   - Closed so far: monomial W (RX §3); RX's own polynomial (RK: no rational extension; KP: no G-stable band-dimensional subspace for a = 1, m = 24..44).
   - **Open:** rational W with other relations (KP v2 FIX-2); non-rational W; a ≥ 2.
4. **The B1 identification and frame** ((B1a⁺), (B1b), (I216′)) and **G2 in Hasse form**: ask Codex.
5. **The gate-failing KB cells:** twisted Kummer–binomials with deg B ≥ 1; general B = 1 with g < 3ρ/2.
6. **G1″ independently of GLS.** This is more important now that GLS₀ is known not to follow abstractly (GLO NG, RX).
7. **General-m versions of KP**, and the line case for m ≡ 2 (mod 4) with m ≥ 26 [OPEN, low priority].
8. **Lower priority (STATE):** ρ = 1 cells, small cells and endpoints.

**The overall linear-gap conjecture is OPEN. Do not claim G1, GLS₀ or the conjecture is complete.**

## 5. Resume message (paste into "(Active) DZ (2)")
> The DZ cloud sessions (7–12 Oct 2026; never Mac-linked; no mailbox) wrote everything to `DZ_CLOUD_RESULTS/`, also bundled as the newest `DZ-HANDBACK-*.zip`.
>
> 1. Read `claude_archive/HANDBACK-20261012T0007Z-FINAL.md` first. Verify the sha256 values against `DZ_CLOUD_RESULTS/PROGRESS.md`, then copy `claude_archive/*` (with all `audit_*`/`revcheck_*` folders) to `CODEX_CLAUDE_EXCHANGE/DZ/claude_archive/`.
> 2. Arrange the referee diff check of `KP-RX-ROOTSPACE-GALOIS-NOTE-20261007-v2.md`. If it passes, attach `DIFFCHECK-KP-v2-20261007.md` to EN, flip EN to READY, and regenerate `MANIFEST_EN_20261012T0006Z.tsv` last.
> 3. Run `date -u`. Re-list `DZ/to_claude/` for files newer than 15:13:17Z on 7 Oct, read the new covers, and generate the receipt TSV on the device. Never execute incoming scripts.
> 4. Fill in §1 (separate RECEIVED, READ and ADOPTED ACKs) of EF, EG, EH, EI, EJ, EK, EL, EM and EN. Regenerate the changed manifests last. Deliver them in that order to `DZ/to_codex/`, per `outbox_for_user_delivery/README-PENDING.md`. Never send anything in `superseded/`. Verify the sha256 values on the device.
> 5. Re-read memo §216 (Prop 216.3 frame). Record the replies to EE and PRIMARY's G23O review.
> 6. Research next, per FINAL HANDBACK §4:
>    - Codex's answers (VO/RW′ on B1; STT/MRL ⇒ a twisted half-field in W);
>    - GLS₀ = generic PTH (ii);
>    - the even-band question for rational W with other relations, non-rational W, and a ≥ 2;
>    - the B1/(I216′)/G2 confirmations;
>    - the KB gate-failing cells;
>    - G1″.
>
> Do not claim G1, GLS₀ or the conjecture is complete.
