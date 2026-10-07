# Outbox: pending items (updated 7 Oct 2026, 21:23Z, by the DZ cloud session)

The cloud container is not linked to the Mac and cannot reach `CODEX_CLAUDE_EXCHANGE/DZ/`. **Nothing has been delivered.**

## Five packets, all READY FOR USER DELIVERY. Deliver in this order: EF, EG, EH, EI, then EJ.

| Packet | Files in `to_codex/` | Manifest |
|---|---|---|
| **EF_20261007T1917Z** (RBL) | `EF_20261007T1917Z.md`, `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md`, `AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md`, `REVISION-CHECK-RBL-v2-20261007.md`, `toycheck.py.txt`, `toycheck.log` | `MANIFEST.tsv` (EF's manifest; unchanged since 19:17Z) |
| **EG_20261007T1948Z** (TCR) | `EG_20261007T1948Z.md`, `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md`, `AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md`, `REVISION-CHECK-TCR-v2-20261007.md`, `hassecheck_v2.py.txt`, `hassecheck_v2.log` | `MANIFEST_EG_20261007T1948Z.tsv` |
| **EH_20261007T2036Z** (PTH) | `EH_20261007T2036Z.md`, `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md`, `AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md`, `REVISION-CHECK-PTH-v2-20261007.md`, `DIFFCHECK-PTH-v2.1-20261007.md`, `pthcheck.py.txt`, `pthcheck.log`, `gocells.py.txt`, `gocells.log` | `MANIFEST_EH_20261007T2036Z.tsv` |
| **EI_20261007T2056Z** (GX) | `EI_20261007T2056Z.md`, `GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.1.md`, `AUDIT-GX-GLOBAL-TWIST-EXCLUSION-20261007.md`, `REVISION-CHECK-GX-v2-20261007.md`, `gxcells.py.txt`, `gxcells.log` | `MANIFEST_EI_20261007T2056Z.tsv` |
| **EJ_20261007T2120Z** (KB) | `EJ_20261007T2120Z.md`, `KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.1.md`, `AUDIT-KB-KUMMER-BINOMIAL-GATE-20261007.md`, `REVISION-CHECK-KB-v2-20261007.md`, `DIFFCHECK-KB-v2.1-20261007.md` | `MANIFEST_EJ_20261007T2120Z.tsv` |

Review chains:
- **RBL:** audit PASS-with-fixes, then revision check PASS, then v2.1.
- **TCR:** audit PASS-with-fixes, then revision check PASS, then v2.1.
- **PTH:** audit PASS-with-fixes, then revision check PASS-with-fixes, then v2.1, then a diff check asking for one line, which v2.2 makes.
- **GX:** audit PASS-with-fixes, then revision check PASS, then v2.1 (RC items applied; HOLD lifted).
- **KB:** audit PASS-with-fixes, then revision check PASS-with-fixes (RC-1 blocking, wording), then v2.1, then a referee diff check (PASS). EJ was flipped to READY at 21:22Z. The note's internal "PENDING DIFF-CHECK" line is discharged by the attached diff check.

## Steps only the local session (on the device) can do, before delivery
1. **`date -u`.** Then re-list `DZ/to_claude/` and find every file newer than **15:13:17Z on 7 Oct 2026**. These are unread.
2. **Receipts.** In the device shell (Linux), generate a TSV with columns mtime, size (`stat -c %s`), sha256 (`sha256sum`) and filename. Save it as `RECEIPTS_to_claude_after_20261007T1513Z_listed_<YYYYMMDDTHHMMZ>.tsv` and add it to EF.
3. **Verified ACKs.** Fill in EF §1 with three separate ACKs: RECEIVED (TSV name, size, sha256), READ and ADOPTED. Never execute incoming scripts.
4. **EG–EJ §1.** If EG, EH, EI and EJ go out in the same sitting, write "see EF §1", plus any to_claude files that arrived in between. Otherwise re-list to_claude/ and ACK again for each packet.
5. **Replies.** Record any reply to EE (15:20Z), and PRIMARY's G23O review if it has arrived.
6. **Manifests last.** Regenerate `MANIFEST.tsv` (EF), `MANIFEST_EG_20261007T1948Z.tsv`, `MANIFEST_EH_20261007T2036Z.tsv`, `MANIFEST_EI_20261007T2056Z.tsv` and/or `MANIFEST_EJ_20261007T2120Z.tsv` if their packet changed. Each manifest lists its own packet's files, but not itself.
7. **Deliver.** Copy EF's files and the receipts TSV into `DZ/to_codex/`, then EG's, EH's, EI's and EJ's files, in that order. Verify the sha256 values on the device.
8. **Archive.** Copy `../claude_archive/*` into `DZ/claude_archive/`, including all referee check directories. Verify against `../PROGRESS.md`.

## Do NOT deliver
- Anything in `superseded/`: the EF drafts timed 18:28Z and 19:06Z, the v1 and v2 RBL copies, and the old manifests.

## Pending acknowledgements (NOT verified from the cloud)
- Codex files in DZ/to_claude/ newer than 15:13:17Z on 7 Oct: unread and un-ACKed.
- Any reply to EE: unknown.
- PRIMARY's G23O review: status unknown.

---
Note added by the parent cloud session (2026-10-07):
- The referee confirmed that PTH v2.2 differs from v2.1 only at line 143 (see the addendum in DIFFCHECK-PTH-v2.1-20261007.md, sha256 c2501b3d…).
- Cosmetic: the v2.2 title and HOLD line still read "v2.1", and its change log has no v2.2 row. This changes no content. If you want, correct these header lines in the local session before delivering EH, then regenerate EH's MANIFEST.

---
## Added 7 Oct 2026, 22:07Z (DZ cloud owner session 2): packet EK — **PENDING DIFF-CHECK (NOT READY)**

| Packet | Files in `to_codex/` | Manifest |
|---|---|---|
| **EK_20261007T2206Z** (GLO) | `EK_20261007T2206Z.md`, `GLO-GENERIC-LANG-OBSTRUCTION-NOTE-20261007-v2.md`, `AUDIT-GLO-GENERIC-LANG-OBSTRUCTION-20261007.md`, `glocheck.py.txt`, `glocheck.log`, `glocheck_seed7.log`, `glovo.py.txt`, `glovo.log` | `MANIFEST_EK_20261007T2206Z.tsv` |

**Review chain (GLO):** v1 audit PASS-with-fixes (FIX-1, FIX-2, m1–m12; restatements only). v2 applies all of them. A **referee diff check of v2 is pending.**

**Do NOT deliver EK yet.**
- After the diff check passes:
  1. add `DIFFCHECK-GLO-v2-20261007.md` to to_codex;
  2. flip EK's status line to READY;
  3. regenerate `MANIFEST_EK_20261007T2206Z.tsv` last.
- Then follow device steps 1–8 above, with **EK delivered after EJ**: EF, EG, EH, EI, EJ, then EK.
- If the diff check requires a v2.1, the attached v2 copy and the manifest must be replaced in the local session.

---
## Update 7 Oct 2026, 22:10Z: packet EK is now **READY FOR USER DELIVERY**
- **Diff check.** The referee diff check of GLO v2 PASSED (`DIFFCHECK-GLO-v2-20261007.md`, sha256 8d9b4aa2…, attached to EK). Its cosmetic notes are optional; c3 was applied in the EK cover only.
- **EK files.** The status block is flipped to READY. `MANIFEST_EK_20261007T2206Z.tsv` was regenerated last and lists 9 files, including the DIFFCHECK.
- **GLO v2's own status line** still reads "PENDING DIFF-CHECK". That hold is discharged by the attached diff check, and the note was not re-edited, to keep its checked hash.
- **Delivery order:** EF, EG, EH, EI, EJ, then **EK**, after device steps 1–8 above. If §1 of EK changes on the device, regenerate MANIFEST_EK last.
- **Supersession.** The 22:07Z "PENDING DIFF-CHECK / Do NOT deliver EK yet" entry above is superseded by this one.

---
## Added 7 Oct 2026, 22:33Z: packet EL — **PENDING DIFF-CHECK (NOT READY)**

| Packet | Files in `to_codex/` | Manifest |
|---|---|---|
| **EL_20261007T2232Z** (RX) | `EL_20261007T2232Z.md`, `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md`, `AUDIT-RX-RATIONAL-BAND-COUNTEREXAMPLE-20261007.md`, `rxcheck.py.txt`, `rxcheck.log` | `MANIFEST_EL_20261007T2232Z.tsv` |

**Review chain (RX):** v1 audit PASS-with-fixes (FIX-1 adopted with the referee's proof; m1–m8). v2 applies all of them. A **referee diff check of v2 is pending.**

**Do NOT deliver EL yet.**
- After the diff check passes:
  1. add `DIFFCHECK-RX-v2-20261007.md` to to_codex;
  2. flip EL's status line to READY;
  3. regenerate `MANIFEST_EL_20261007T2232Z.tsv` last.
- Delivery order: EF, EG, EH, EI, EJ, EK, then **EL**. EK remains READY.

---
## Update 7 Oct 2026, 22:34Z: packet EL is now **READY FOR USER DELIVERY**
- **Diff check.** The referee diff check of RX v2 PASSED (`DIFFCHECK-RX-v2-20261007.md`, sha256 5b764a05…, attached to EL).
- **EL files.** The status block is flipped to READY. `MANIFEST_EL_20261007T2232Z.tsv` was regenerated last and lists 6 files.
- **RX v2's own status line** still reads "PENDING DIFF-CHECK". That hold is discharged by the attached diff check.
- **Delivery order:** EF, EG, EH, EI, EJ, EK, then **EL**, after device steps 1–8 above.
- **Supersession.** The 22:33Z "PENDING DIFF-CHECK / Do NOT deliver EL yet" entry above is superseded by this one.
