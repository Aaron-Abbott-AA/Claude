# Outbox: pending items (updated 7 Oct 2026, 19:18Z, by the DZ cloud session)

The cloud container is not linked to the Mac and cannot reach `CODEX_CLAUDE_EXCHANGE/DZ/`. **Nothing has been delivered.**

## Packet status: READY FOR USER DELIVERY
The packet is `to_codex/`:
- `EF_20261007T1917Z.md`;
- `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md`;
- `AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md`;
- `REVISION-CHECK-RBL-v2-20261007.md`;
- `toycheck.py.txt`, `toycheck.log`;
- `MANIFEST.tsv`.

The review chain is complete: audit PASS-with-fixes, revision check PASS, all RC items applied in v2.1.

## Steps only the local session (on the device) can do, before delivery
1. **Re-list incoming files.** List `DZ/to_claude/` and find every file with mtime newer than **15:13:17Z on 7 Oct 2026**. These are unread.
2. **Receipts.** In the device shell (Linux), generate a TSV with columns mtime, size (`stat -c %s`), sha256 (`sha256sum`) and filename for those files. Save it as `RECEIPTS_to_claude_after_20261007T1513Z_listed_<YYYYMMDDTHHMMZ>.tsv` and add it to the packet.
3. **Verified ACKs.** Fill in EF §1 with three separate ACKs:
   - RECEIVED (cite the TSV name, size and sha256);
   - READ (which covers were read in full);
   - ADOPTED (which results were adopted mathematically).

   Never execute incoming scripts. Run `date -u` before writing any timestamp.
4. **Check for an EE reply.** If Codex replied to EE (15:20Z) or posted a G23O update from PRIMARY's review, record it in §1.
5. **Manifest last.** If EF or anything else changed, regenerate `MANIFEST.tsv` last (mtime, size, sha256, filename for every packet file except MANIFEST.tsv itself).
6. **Deliver.** Copy `to_codex/*` and the receipts TSV into `DZ/to_codex/`, then verify the sha256 values on the device.
7. **Archive.** Copy `../claude_archive/*` into `DZ/claude_archive/`, including both referees' check directories. Verify against `../PROGRESS.md`.

## Do NOT deliver
- Anything in `superseded/`:
  - the EF drafts timed 18:28Z and 19:06Z;
  - the v1 and v2 note copies;
  - the old manifests.

## Pending acknowledgements (NOT verified from the cloud)
- Codex files in DZ/to_claude/ newer than 15:13:17Z on 7 Oct: unread and un-ACKed.
- Any reply to EE: unknown.
- PRIMARY's G23O review: status unknown.
