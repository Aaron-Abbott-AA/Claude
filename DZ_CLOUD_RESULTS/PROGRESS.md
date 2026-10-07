# DZ cloud session — PROGRESS (last updated 7 Oct 2026, 19:19Z)

## Context
- **Input:** DZ-CLOUD-HANDOFF-20261007.zip, unzipped in the isolated scratch area; START-HERE followed.
- **Mailbox:** the container is NOT linked to the Mac and has no mailbox access. Nothing was delivered and nothing was ACKed.
- **Scripts:** no incoming scripts were executed. Our own toycheck.py was run with `python3 -I`, nice 19, one process at a time, a few seconds per run.
- **Deferred computation:** none.
- **The goal is NOT complete.** G1′ and G5 are OPEN, and the linear-gap conjecture is open.

## Work done and verdicts
| Time (UTC) | Item | Status | Verdict |
|---|---|---|---|
| 18:07 | Read the handoff | [A] | n/a |
| 18:24 | toycheck.py at m = 16, 20, 24 | COMPUTED | reproduced exactly by the auditor |
| 18:27 | RBL note v1 | written | **PASS-with-fixes** (independent audit, 18:29–19:05Z; 3 substantive + 8 minor items) |
| 19:06 | RBL note v2 (FIX-1…FIX-11 applied) | written | **PASS** (independent revision check, 19:08–19:14Z; 11/11 addressed; 9 cosmetic RC items) |
| 19:16 | RBL note v2.1 (RC-1…RC-9 applied; no mathematical change) | written | current version |
| — | Lemma AR | PROVED | PASS |
| — | Proposition TX | PROVED + COMPUTED | PASS |
| — | Lemma TSZ | PROVED | PASS |
| — | Theorem RB | PROVED; arc application CONDITIONAL on (B1a)–(B1b) | PASS |
| — | Proposition RD (a) | PROVED | PASS |
| — | Proposition RD (b)–(d) | CONDITIONAL on G2 | PASS |
| — | Proposition RD, termination | CONDITIONAL on G5 | PASS (as restated) |
| — | G1 ⇐ G1′ + G2 + G4 + G5 + B1 identification | CONDITIONAL | PASS (as restated) |
| — | G1′, G5 | OPEN | — |
| — | Lang-equation route | HEURISTIC | — |
| 19:17 | Outbox packet EF_20261007T1917Z | **READY FOR USER DELIVERY** (device-only steps pending) | — |
| 19:18 | HANDBACK and CHECKPOINT-ADDENDUM (19:18Z); zip rebuilt | written | — |

- **CITED inputs:** WG, RR, BWG, HFA1, Lemma G and HFD §1, read only through the handoff's summary notes.

## Files (sha256)
| sha256 | File |
|---|---|
| 2ad21b2d720db8a0f318638baf707bafffde10f735a06a8ec76679b1ee98c676 | DZ-HANDBACK-20261007T1918Z.zip |
| 75830869976bb05b946b3f528ecc64df7437dc0b9da260fe6e1467f64730a015 | claude_archive/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md |
| 72229fabbe07e98fc7a8de2f02becb5f15a60b7376dc52dfd94be64dfcc08be7 | claude_archive/CHECKPOINT-ADDENDUM-20261007T1830Z.md |
| 65c09bc33155cb6d839e0043721adcffd4a23da25f95bdfea0c4ed96f08a5dd2 | claude_archive/CHECKPOINT-ADDENDUM-20261007T1907Z.md |
| 3a082594e6bd36585d00bada48cb73fb85644374aa031e368e7a9edf78e11d3f | claude_archive/CHECKPOINT-ADDENDUM-20261007T1918Z.md |
| bbc7a88dc329c1949446c0a17a3fea5bbfe76852ef4049b53eb92806694e2c81 | claude_archive/HANDBACK-20261007T1830Z.md |
| 7c54d04efc7215af415267d06ed00e79d6c23f81e92ed3833ec4d6cabc893f08 | claude_archive/HANDBACK-20261007T1907Z.md |
| eb65e707eb40b840e9606b5e09297d01fe8f27491d70ddb39bee06752af263e9 | claude_archive/HANDBACK-20261007T1918Z.md |
| f3a2e176f7e3929170b6f1bec0bed5bde5086d77d3a0cf7f75a6f8d6784d9453 | claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md |
| f9a1116197a710dac9c5b5cd69b85a36515460028bfcb8d5d05907d9833622ab | claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md |
| c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe | claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md |
| e0cd99ba293e48ec8fbb68f96bd87afc19af5ab860e83753d1e09c00b14d558a | claude_archive/REVISION-CHECK-RBL-v2-20261007.md |
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
| e0aefe252ebcf2871dedc964b931b27a148ff503e1854db8bf1fd25298317e7f | claude_archive/revcheck_RBLv2_checks/check_arith_v2.log |
| 56636e9f6b858e141b987bdbc570bbea1a0a088391031d9806601a9adf1453bf | claude_archive/revcheck_RBLv2_checks/check_arith_v2.py |
| 5c1e0a61381ccdb98ad9ce017bdbef0edea731bf1e20358cf7658d32aa8ae22b | claude_archive/revcheck_RBLv2_checks/check_tx_v2.py |
| df60a3b63ed139dd4554c9a5e4b297ba881e5b8ccdd264325f751bcf5844257f | claude_archive/revcheck_RBLv2_checks/check_tx_v2_12_5.log |
| a5e37b1e39b73f9ae2415b38f334f887b53449711c0c914417c171fc2a8604d5 | claude_archive/revcheck_RBLv2_checks/check_tx_v2_12_6.log |
| 33c9eb32415c8d0a8aee84a56f360a165c2ad61f5ab73cbfadba4b84b9c2ec08 | claude_archive/revcheck_RBLv2_checks/check_tx_v2_16_6.log |
| 46f17dc0b2076e557c6da01e53ab7e6696958105c5268be384ece2111e99ba70 | claude_archive/revcheck_RBLv2_checks/checks_SHA256SUMS.txt |
| dfd90e8899ff47d567f69b19ad3e16e1dc66d347b4e886792ca462f8cac0919c | claude_archive/revcheck_RBLv2_checks/wdiff_v1_v2.log |
| 47ed7ed1e0480a91e87933828c5e3a5a087be9a5628c8ea7503c0cd185a9ab33 | claude_archive/revcheck_RBLv2_checks/wdiff_v1_v2.py |
| 613fa8c094d5929812880a4da4d838f201cf51386ed2fed8c53715e9a1c145dd | claude_archive/scripts/toycheck.log |
| aeff51cd313c50d1cae1a59a92cd7ece26576756d8b41592751e9354e90a3d9b | claude_archive/scripts/toycheck.py |
| cddd8d9aa76662d4acdd0b18735dcab052b8c65bec94fbf42bac76d2b6c426db | outbox_for_user_delivery/README-PENDING.md |
| e27609fd1e0cc3359822103072c1a0b07225608e170cfa9f518ab4c0cf61f251 | outbox_for_user_delivery/superseded/EF_20261007T1828Z.md |
| cffccf56af82a80e084e36acfcd39958ac6a87fe13de1e853be5ec163575d394 | outbox_for_user_delivery/superseded/EF_20261007T1906Z.md |
| 18d331067cee4b82eb11aeb295778702b2a26f74b0bd33f9e1ecc4898f9fd8f0 | outbox_for_user_delivery/superseded/MANIFEST-20261007T1828Z.tsv |
| 5d158704fb2582b28bee891c219fb3c6fd197668ac21b7179db6aa7319f0f0f9 | outbox_for_user_delivery/superseded/MANIFEST-20261007T1906Z.tsv |
| f9a1116197a710dac9c5b5cd69b85a36515460028bfcb8d5d05907d9833622ab | outbox_for_user_delivery/superseded/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md |
| c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe | outbox_for_user_delivery/superseded/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md |
| 75830869976bb05b946b3f528ecc64df7437dc0b9da260fe6e1467f64730a015 | outbox_for_user_delivery/to_codex/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md |
| 3fde9902162ad0f147b91447e4f12bb935d6dc6dd978bad5eabb19c8839e1628 | outbox_for_user_delivery/to_codex/EF_20261007T1917Z.md |
| 558079f6acd1672385b01b213f28d12a0ae3a805f06b91917cf6e7d26afa26f0 | outbox_for_user_delivery/to_codex/MANIFEST.tsv |
| f3a2e176f7e3929170b6f1bec0bed5bde5086d77d3a0cf7f75a6f8d6784d9453 | outbox_for_user_delivery/to_codex/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md |
| e0cd99ba293e48ec8fbb68f96bd87afc19af5ab860e83753d1e09c00b14d558a | outbox_for_user_delivery/to_codex/REVISION-CHECK-RBL-v2-20261007.md |
| 613fa8c094d5929812880a4da4d838f201cf51386ed2fed8c53715e9a1c145dd | outbox_for_user_delivery/to_codex/toycheck.log |
| aeff51cd313c50d1cae1a59a92cd7ece26576756d8b41592751e9354e90a3d9b | outbox_for_user_delivery/to_codex/toycheck.py.txt |

## Pending for the user
The device-only steps are listed in full in outbox_for_user_delivery/README-PENDING.md. In brief:
1. Re-list DZ/to_claude/ (files newer than 15:13:17Z on 7 Oct).
2. Generate the receipt TSV on the device.
3. Fill in the three ACKs of EF §1 (received / read / adopted).
4. Check for a reply to EE and any update on G23O.
5. Regenerate MANIFEST.tsv last.
6. Deliver to_codex/* and the receipts.
7. Archive claude_archive/* and verify the sha256 values.

Never deliver anything in superseded/.

**Unverified ACKs:**
- unread Codex files after 15:13:17Z;
- any reply to EE;
- PRIMARY's G23O review.

## Resume message (paste into the local DZ session)
> The DZ cloud session (7 Oct 2026, 18:07–19:19Z; not linked to the Mac) has finished. Its files are in the GitHub-synced folder `DZ_CLOUD_RESULTS/`, also bundled as `DZ-HANDBACK-20261007T1918Z.zip`.
>
> Read, in order:
> 1. `claude_archive/HANDBACK-20261007T1918Z.md`;
> 2. `claude_archive/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.1.md` (the current version);
> 3. `claude_archive/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md` (on v1: PASS-with-fixes);
> 4. `claude_archive/REVISION-CHECK-RBL-v2-20261007.md` (on v2: PASS).
>
> Verify the sha256 values against `DZ_CLOUD_RESULTS/PROGRESS.md`, then copy `claude_archive/*` into `CODEX_CLAUDE_EXCHANGE/DZ/claude_archive/`.
>
> Then:
> 1. Run `date -u`. Re-list `DZ/to_claude/` for files newer than 15:13:17Z on 7 Oct, and read the new Codex covers. Never execute incoming scripts.
> 2. Generate the receipt TSV (`stat -c %s`, `sha256sum`) on the device.
> 3. Fill in §1 of `outbox_for_user_delivery/to_codex/EF_20261007T1917Z.md`, ACKing receipt, reading and adoption separately.
> 4. Regenerate `MANIFEST.tsv` last. Copy `to_codex/*` plus the receipts TSV into `DZ/to_codex/`, and verify the sha256 values on the device. Do NOT send anything from `superseded/`.
> 5. Research next: G1′ (the Galois orbit bound for the WG family) and G5 (the terminal step at positive defect). Ask Codex for the B1 identification (B1a)–(B1b).
>
> Do not claim G1 or the conjecture is complete.
