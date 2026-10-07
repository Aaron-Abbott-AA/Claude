# Outbox: pending items (updated 7 Oct 2026, 20:37Z, by the DZ cloud session)

The cloud container is not linked to the Mac and cannot reach `CODEX_CLAUDE_EXCHANGE/DZ/`. **Nothing has been delivered.**

## Three packets, all READY FOR USER DELIVERY. Deliver in this order: EF, then EG, then EH.

| Packet | Files in `to_codex/` | Manifest |
|---|---|---|
| **EF_20261007T1917Z** (RBL) | `EF_20261007T1917Z.md`, `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md`, `AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md`, `REVISION-CHECK-RBL-v2-20261007.md`, `toycheck.py.txt`, `toycheck.log` | `MANIFEST.tsv` (EF's manifest; unchanged since 19:17Z) |
| **EG_20261007T1948Z** (TCR) | `EG_20261007T1948Z.md`, `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md`, `AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md`, `REVISION-CHECK-TCR-v2-20261007.md`, `hassecheck_v2.py.txt`, `hassecheck_v2.log` | `MANIFEST_EG_20261007T1948Z.tsv` |
| **EH_20261007T2036Z** (PTH) | `EH_20261007T2036Z.md`, `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md`, `AUDIT-PTH-POINTWISE-TWISTED-HALFFIELD-20261007.md`, `REVISION-CHECK-PTH-v2-20261007.md`, `DIFFCHECK-PTH-v2.1-20261007.md`, `pthcheck.py.txt`, `pthcheck.log`, `gocells.py.txt`, `gocells.log` | `MANIFEST_EH_20261007T2036Z.tsv` |

Review chains:
- **RBL:** audit PASS-with-fixes, then revision check PASS, then v2.1.
- **TCR:** audit PASS-with-fixes, then revision check PASS, then v2.1.
- **PTH:** audit PASS-with-fixes, then revision check PASS-with-fixes, then v2.1, then a diff check asking for one line, which v2.2 makes.

## Steps only the local session (on the device) can do, before delivery
1. **`date -u`.** Then re-list `DZ/to_claude/` and find every file newer than **15:13:17Z on 7 Oct 2026**. These are unread.
2. **Receipts.** In the device shell (Linux), generate a TSV with columns mtime, size (`stat -c %s`), sha256 (`sha256sum`) and filename. Save it as `RECEIPTS_to_claude_after_20261007T1513Z_listed_<YYYYMMDDTHHMMZ>.tsv` and add it to EF.
3. **Verified ACKs.** Fill in EF §1 with three separate ACKs: RECEIVED (TSV name, size, sha256), READ and ADOPTED. Never execute incoming scripts.
4. **EG and EH §1.** If EG and EH go out in the same sitting, write "see EF §1", plus any to_claude files that arrived in between. Otherwise re-list to_claude/ and ACK again for each packet.
5. **Replies.** Record any reply to EE (15:20Z), and PRIMARY's G23O review if it has arrived.
6. **Manifests last.** Regenerate `MANIFEST.tsv` (EF), `MANIFEST_EG_20261007T1948Z.tsv` and/or `MANIFEST_EH_20261007T2036Z.tsv` if their packet changed. Each manifest lists its own packet's files, but not itself.
7. **Deliver.** Copy EF's files and the receipts TSV into `DZ/to_codex/`, then EG's files, then EH's files. Verify the sha256 values on the device.
8. **Archive.** Copy `../claude_archive/*` into `DZ/claude_archive/`, including all referee check directories. Verify against `../PROGRESS.md`.

## Do NOT deliver
- Anything in `superseded/`: the EF drafts timed 18:28Z and 19:06Z, the v1 and v2 RBL copies, and the old manifests.

## Pending acknowledgements (NOT verified from the cloud)
- Codex files in DZ/to_claude/ newer than 15:13:17Z on 7 Oct: unread and un-ACKed.
- Any reply to EE: unknown.
- PRIMARY's G23O review: status unknown.
