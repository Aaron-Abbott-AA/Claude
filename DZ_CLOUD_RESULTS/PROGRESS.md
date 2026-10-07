# DZ cloud session — PROGRESS (last updated 7 Oct 2026, 19:08Z)

## Context
- **Input:** DZ-CLOUD-HANDOFF-20261007.zip, unzipped in the isolated scratch area; START-HERE followed.
- **Mailbox:** the container is NOT linked to the Mac and has no mailbox access. Nothing was delivered or ACKed.
- **Scripts:** no incoming scripts were executed. Our own `toycheck.py` was run with `python3 -I`, nice 19, one process at a time, a few seconds per run.
- **Deferred computation:** none.
- **The goal is NOT complete.** G1′ and G5 are OPEN, and the linear-gap conjecture is open.

## Work done
| Time (UTC) | Item | Label / status | Audit verdict |
|---|---|---|---|
| 18:07 | Read the handoff | [A] | n/a |
| 18:24 | toycheck.py at m = 16, 20, 24 | COMPUTED | auditor reproduced it exactly |
| 18:27 | RBL note v1 | — | **PASS-with-fixes** (independent referee, 18:29–19:05Z; 3 substantive + 8 minor) |
| 18:27→19:06 | Lemma AR | PROVED | PASS ("Consequence" now [H]) |
| | Proposition TX | PROVED + COMPUTED | PASS (exceptional sets fixed in v2) |
| | Lemma TSZ | PROVED | PASS |
| | Theorem RB (i)–(iii) | PROVED; application to the arc CONDITIONAL on (B1a)–(B1b) | PASS |
| | Proposition RD (a), (b), (d) | CONDITIONAL (G2) | PASS |
| | Proposition RD (c) | CONDITIONAL (G2 + G5 + B1) | v1 FAILED as stated; restated in v2 |
| | G1 ⇐ G1′ + G2 + G4 + G5 + B1 identification | CONDITIONAL | corrected in v2 |
| | G1′ (orbit bound), G5 (terminal step at positive defect) | OPEN | — |
| | Lang-equation route | HEURISTIC | — |
| 19:06 | RBL note v2 (all FIX-1 to FIX-11 applied, each marked) | written | **v2 revision check PENDING** |
| 19:06 | Outbox EF_20261007T1906Z (carries the v2 note and the audit) | **ON HOLD** | — |
| 19:07 | HANDBACK and CHECKPOINT-ADDENDUM (19:07Z) | written | — |

- **CITED inputs:** WG, RR, BWG, HFA1, Lemma G and HFD §1, read only through the handoff's summary notes.

## Files (sha256)
| sha256 | File |
|---|---|
| f9a1116197a710dac9c5b5cd69b85a36515460028bfcb8d5d05907d9833622ab | claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md |
| c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe | claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md (v1) |
| 75830869976bb05b946b3f528ecc64df7437dc0b9da260fe6e1467f64730a015 | claude_archive/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md (referee; unedited) |
| 7c54d04efc7215af415267d06ed00e79d6c23f81e92ed3833ec4d6cabc893f08 | claude_archive/HANDBACK-20261007T1907Z.md |
| bbc7a88dc329c1949446c0a17a3fea5bbfe76852ef4049b53eb92806694e2c81 | claude_archive/HANDBACK-20261007T1830Z.md (superseded) |
| 65c09bc33155cb6d839e0043721adcffd4a23da25f95bdfea0c4ed96f08a5dd2 | claude_archive/CHECKPOINT-ADDENDUM-20261007T1907Z.md |
| 72229fabbe07e98fc7a8de2f02becb5f15a60b7376dc52dfd94be64dfcc08be7 | claude_archive/CHECKPOINT-ADDENDUM-20261007T1830Z.md |
| aeff51cd313c50d1cae1a59a92cd7ece26576756d8b41592751e9354e90a3d9b | claude_archive/scripts/toycheck.py |
| 613fa8c094d5929812880a4da4d838f201cf51386ed2fed8c53715e9a1c145dd | claude_archive/scripts/toycheck.log |
| 3b830fbb9c63983d02386dabb3eb65a561f6a731e08423139124648f2157a7a0 | claude_archive/audit_RBL_checks/check_module.log |
| c917304b283071fd840ecb2c91a8097d69f6aed47bb40dde6841c5ef194acf7a | claude_archive/audit_RBL_checks/check_module.py |
| 28b999345df75f76fe3d8acbd35fd526e5d277451f01099fb2b76631bab9b397 | claude_archive/audit_RBL_checks/check_range.log |
| 0aaf65be461359f059e28a38783b006c1dcd8e3131aadd75efe79de16c03c1d8 | claude_archive/audit_RBL_checks/check_range.py |
| 93a8f2c1853aa01965b0398aa8ae2b2c11ae844cca41d9514264cd68f44261cb | claude_archive/audit_RBL_checks/check_tsz.log |
| 6213b513b4dedcb3946f4deda52b774349c3f589e1e49903a68ca93347bffe92 | claude_archive/audit_RBL_checks/check_tsz.py |
| b15063ddc820b9bd450b669e70c0f7ba5d9164f2c80ede66b8d2d28124e576ce | claude_archive/audit_RBL_checks/check_tx.py |
| 6b28fac17688329b3332bab48af53a6d7345961d740ee8962f9368d539372d3f | claude_archive/audit_RBL_checks/check_tx_12_6.log |
| 8ad84ff4ccdbe18c4d8c6fa4d00be1e9fb86c2f8c451882c29f557d128418490 | claude_archive/audit_RBL_checks/check_tx_16_6.log |
| eb2060efb2f5b8ab9dd2b9959f19b00e1fd73c94e53cff58e39fb95070a4142f | claude_archive/audit_RBL_checks/check_tx_16_8.log |
| 1ec7d997739514b8d4dca51eea74706da509ac602af21e7b80afbe9768eb728b | claude_archive/audit_RBL_checks/checks_SHA256SUMS.txt |
| 637efd5863f7177b01124bf3d4976c7d370fed6543fd2d228660e04439df3fdb | claude_archive/audit_RBL_checks/owner_copy/rerun_16_6.log |
| cf8fac45fbe82b22d351a58929b9395267d49fc5abd3cd8fa964fdef9f06646b | claude_archive/audit_RBL_checks/owner_copy/rerun_20_8_s1.log |
| 348020bb710cf3923372bd8ea3cb132a527fd670003ffef6358ccd13d36fa8a1 | claude_archive/audit_RBL_checks/owner_copy/rerun_20_8_s2.log |
| f8d0afac7f5e12f56c4c006fa59c75a1faa4a76f475a1659bdf4e6c95f836fbe | claude_archive/audit_RBL_checks/owner_copy/rerun_24_10_s3.log |
| aeff51cd313c50d1cae1a59a92cd7ece26576756d8b41592751e9354e90a3d9b | claude_archive/audit_RBL_checks/owner_copy/toycheck.py |
| 893ea9e4cbcb5395a36de24ba1be782182d6240b374e76986ec625c0e53fd43d | outbox_for_user_delivery/README-PENDING.md |
| cffccf56af82a80e084e36acfcd39958ac6a87fe13de1e853be5ec163575d394 | outbox_for_user_delivery/to_codex/EF_20261007T1906Z.md (ON HOLD) |
| f9a1116197a710dac9c5b5cd69b85a36515460028bfcb8d5d05907d9833622ab | outbox_for_user_delivery/to_codex/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md |
| 75830869976bb05b946b3f528ecc64df7437dc0b9da260fe6e1467f64730a015 | outbox_for_user_delivery/to_codex/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md |
| aeff51cd313c50d1cae1a59a92cd7ece26576756d8b41592751e9354e90a3d9b | outbox_for_user_delivery/to_codex/toycheck.py.txt |
| 613fa8c094d5929812880a4da4d838f201cf51386ed2fed8c53715e9a1c145dd | outbox_for_user_delivery/to_codex/toycheck.log |
| 5d158704fb2582b28bee891c219fb3c6fd197668ac21b7179db6aa7319f0f0f9 | outbox_for_user_delivery/to_codex/MANIFEST.tsv |
| e27609fd1e0cc3359822103072c1a0b07225608e170cfa9f518ab4c0cf61f251 | outbox_for_user_delivery/superseded/EF_20261007T1828Z.md (do not deliver) |
| c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe | outbox_for_user_delivery/superseded/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md (do not deliver) |
| 18d331067cee4b82eb11aeb295778702b2a26f74b0bd33f9e1ecc4898f9fd8f0 | outbox_for_user_delivery/superseded/MANIFEST.tsv (do not deliver) |
| 8a8dabc9728a204da72bbdae7fc13f78f060c7b646eaa6580d01e6585fe64ba1 | DZ-HANDBACK-20261007T1907Z.zip (contains claude_archive/ and outbox_for_user_delivery/) |

## Pending for the user
1. **Not delivered.** Nothing has gone to `CODEX_CLAUDE_EXCHANGE/DZ/`. Copying `claude_archive/*` to DZ/claude_archive/ is safe now.
2. **Hold EF.** Hold `to_codex/*` (EF_20261007T1906Z) until all three are done:
   - (a) a referee confirms the v2 revision;
   - (b) EF §1 is filled from a fresh to_claude/ listing, with a receipt TSV;
   - (c) MANIFEST.tsv is regenerated if anything is edited.
3. **ACKs not verified:**
   - Codex files in to_claude/ newer than 15:13:17Z;
   - any reply to EE;
   - PRIMARY's review of G23O.

## Resume message (paste into the local DZ session)
> The DZ cloud session (7 Oct 2026, 18:07–19:08Z; not linked to the Mac) has finished. Its files are in the GitHub-synced folder `DZ_CLOUD_RESULTS/`, also bundled as `DZ-HANDBACK-20261007T1907Z.zip`.
>
> Read, in order:
> 1. `claude_archive/HANDBACK-20261007T1907Z.md`;
> 2. `claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md`;
> 3. the independent audit `claude_archive/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md` (verdict on v1: PASS-with-fixes; all fixes applied in v2).
>
> Verify the sha256 values against `DZ_CLOUD_RESULTS/PROGRESS.md`, then copy `claude_archive/*` into `CODEX_CLAUDE_EXCHANGE/DZ/claude_archive/`.
>
> Then:
> 1. Have a fresh referee check that v2 applies FIX-1 to FIX-11 correctly.
> 2. Re-list `DZ/to_claude/` (files newer than 15:13:17Z on 7 Oct), read the new Codex covers, generate the receipt TSV on the device, and fill §1 of `outbox_for_user_delivery/to_codex/EF_20261007T1906Z.md`.
> 3. Regenerate `MANIFEST.tsv`, and send EF with the v2 note, the audit and the toycheck attachments to `DZ/to_codex/`. Do NOT send anything from `superseded/`.
> 4. Research: G1′ (orbit bound) and G5 (terminal step at positive defect). Ask Codex for the B1 identification (B1a)–(B1b).
>
> Do not claim G1 or the conjecture is complete.
