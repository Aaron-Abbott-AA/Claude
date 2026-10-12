# DIFFCHECK — KP-RX-ROOTSPACE-GALOIS-NOTE-20261007 v1 → v2

Referee diff check, by the same isolated referee agent that wrote AUDIT-KP-RX-ROOTSPACE-GALOIS-20261007.md. Written 12 Oct 2026, 00:08Z (`date -u` checked).
- Same rules and isolation as the audit. No incoming scripts were executed, no git was used, no process was killed, and no HYP/3PP directories, uploads or other scratchpads were read.

## Verdict: **PASS**

- FIX-1, FIX-2 and m1–m6 are all correctly applied.
- Apart from the marked edits, the AUDIT STATUS block, the change log §10 and one referee-summary bullet in §5, nothing changed.
- The title, the status block and the change log all name v2.
- The packet copy is byte-identical to the archive v2.
- Every MANIFEST_EN hash, size and mtime is correct.

**EN may flip to READY** once this file is attached and the manifest is regenerated last, as EN's own status block prescribes. There is one records point to handle when flipping (§4, R1): the expected file name.

## 1. Files and hashes

| File | sha256 | Note |
|---|---|---|
| v1 `claude_archive/KP-RX-ROOTSPACE-GALOIS-NOTE-20261007.md` | 87430b2398f7858c53fcc92ad5d87b395eeefd382af2c90d0354985a89256ffd | The audited version, unchanged |
| v2 `referee_KP/src/…-v2.md` | b8a804145e3d21cafb3112a8f37d297b26cc3504452fa557718fa9e1073b6634 | 16501 bytes |
| v2 `claude_archive/…-v2.md` | b8a804145e3d21cafb3112a8f37d297b26cc3504452fa557718fa9e1073b6634 | Identical |
| v2 `outbox_for_user_delivery/to_codex/…-v2.md` | b8a804145e3d21cafb3112a8f37d297b26cc3504452fa557718fa9e1073b6634 | **Identical to the archive v2** |
| `claude_archive/AUDIT-KP-RX-ROOTSPACE-GALOIS-20261007.md` | 7639a0ae97b1cac86edbb1c847a295e9412db619d67089927f037168c3b4ee7b | Matches the hash cited in v2's AUDIT STATUS (7639a0ae…b4ee7b) |
| `claude_archive/audit_KP_checks/` | — | `sha256sum -c checks_SHA256SUMS.txt`: 21/21 OK. `diff -r` against the referee's `checks/` shows them identical. |

## 2. Diff v1 → v2 (`diff` of the full files; every hunk inspected)

| Item | Where in v2 | Applied correctly? |
|---|---|---|
| Title / status / change log | The title says "Owner note **v2**, … 12 Oct 2026, 00:05Z; v1 7 Oct 2026, 23:30Z". The AUDIT STATUS (v2) block names v1's hash, the audit's hash, the verdict and "STATUS: v2 — PENDING DIFF-CHECK". §10 "Change log v1 → v2" is present and lists FIX-1, FIX-2 and m1–m6. | Yes |
| **FIX-1** | **GS:** the "in particular" bullet now uses the intersection {0, n} (irreducible ⇒ a fortiori). **KP(i)** is restated via the intersection {0, n} and GS. A sub-bullet discloses that none of the 36 logged samples is irreducible and that the script message is a mislabel; the script is left unchanged. A second sub-bullet says the literal v1 statement is true by [C, referee F3/F1], giving owner-sequence #8 for m = 24 and referee samples for m = 44, both correct per audit F3/F1. **§5:** the "stops early" sentence is corrected, the table column is renamed "intersection {0, n} reached (early stop)", and the values are unchanged and correct. **§6(b)** is reworded to the intersection patterns, adding that individual polynomials are mostly reducible. | Yes |
| **FIX-2** | **§6(a):** "different (C, D)" becomes "not proportional to RX's", with the scope a = 1, m = 24..44 and the reason (any W with RX's relation lies in R_P). "And a non-rational W" is explicitly withdrawn. Rational W with another (C, D) are marked [OPEN], and a ≥ 2 is noted as untouched. The change log records that the HANDBACK correction is made in the new HANDBACK. HANDBACK-20261012T0007Z-FINAL §4 item 3 indeed lists "rational W with other relations (KP v2 FIX-2)" as Open. | Yes |
| m1 | FR step 2 makes M̄ = k̄ ⊗_k M (λ ⊗ f ↦ λf) explicit, and Φ is stated as k̄-linear. Step 3 says τ^N ⊗ 1 on k̄ ⊗_k M is not left multiplication on M̄, which is 2^N-semilinear. | Yes |
| m2 | GS: a "Which group" bullet says the arithmetic Gal(L^sep/L) is meant, and geometric-only stability is not addressed. | Yes |
| m3 | §6(d): restricted to the G-stable A(F_Q) and A(U′) = W ∩ A(F_Q) of a minimal twist; a general A(U) need not be G-stable; A(F_Q) is not excluded by irreducibility alone. | Yes |
| m4 | Title: the ranges m = 24..44 (m ≡ 0 mod 4) and m = 26..42 (m ≡ 2 mod 4) are added, and "exactly" is replaced by "the m searched". §5 gains the referee-information bullet: m = 12, 16, 20 give {0, n}, and m = 22 gives {0, 1, 8, 9}, which matches audit F1. | Yes |
| m5 | KL proof: the "(π, 0)" output is explained (fractional slopes ≤ 1/2, 1/8, 1/32; slope 12 at ∞), citing [C, referee F6]. | Yes |
| m6 | §2 Remark: the qualifier α ∉ Z = F_Q is added (Z = F_Q for a = 1, per RX v2 (vi)), with [C, referee F5] 210/210 for m = 10..26. | Yes |
| §5 referee summary (new bullet) | "356 owner samples recomputed; FR against actual roots 78/78, 39/39; fresh samples reproduce every intersection." All of these agree with audit §5. | Yes (accurate) |
| **Other changes** | None. FR steps 1 and 4 (the end of step 2), the matrix form, GS's statement and proof, KP(ii)/(iii) and their proof, KL's statement and proof steps 1–3, §5's sanity bullets, §6(c), §7, §8 and §9 are byte-unchanged. The only other new text is the §10 closing line ("No proof was changed. Scripts unchanged. … `audit_KP_checks/`"), which is accurate. | Confirmed |

**Residual uses of "irreducible"** (grep) are all correct: GS line 46 (irreducible-factor degrees), the a-fortiori remark, the FIX-1 disclosure, KL's "irreducible π", and the galois-moduli remarks.

## 3. Packet EN and MANIFEST_EN_20261012T0006Z.tsv
All recomputed sha256 values, sizes and mtimes match the manifest:

| File (to_codex/) | Size | sha256 | Manifest |
|---|---|---|---|
| EN_20261012T0006Z.md | 2826 | aaf7a1f8…4128 | match |
| KP-RX-ROOTSPACE-GALOIS-NOTE-20261007-v2.md | 16501 | b8a80414…6634 | match (identical to the archive v2) |
| AUDIT-KP-RX-ROOTSPACE-GALOIS-20261007.md | 22701 | 7639a0ae…ee7b | match (identical to the archive audit) |
| kpcheck.py.txt | 7345 | bb1eb2a4…9a60 | match (= `claude_archive/scripts/kpcheck.py`) |
| kpcheck.log | 26888 | cb00f4b0…8d96 | match (= archive) |
| kprat.py.txt | 6291 | bde29362…4e5b | match (= archive) |
| kprat.log | 3596 | cc1344df…7ee9 | match (= archive) |

- The MANIFEST_EN file itself has sha256 f070794b8e9b04d34aea8b3f2733e5f055750f415ec560255c52479e70b6c9a6. This matches the prefix f070794b in HANDBACK-20261012T0007Z-FINAL.
- **EN body (§2(a)–(e), §3).** It faithfully summarises v2:
  - (c) states KP with the scope a = 1, m = 24..44;
  - (e) carries FIX-2 (rational W with other relations [OPEN]);
  - the attachment list flags the kpcheck mislabel.
  - It claims nothing beyond v2, and keeps GLS₀, the even band and the conjecture open.
- EN currently reads "PENDING DIFF-CHECK — NOT READY". **To flip it:** attach this file, update the status block, then regenerate the manifest last. EN's hash will change; this is expected.

## 4. Records point (not a fix to v2)
- **R1 (file name).** EN's status block and attachment list, and HANDBACK-20261012T0007Z-FINAL §3 step 1, expect the name `DIFFCHECK-KP-v2-20261007.md`. As instructed by the coordinator, this file is named **`DIFFCHECK-KP-v2-20261012.md`**. When flipping EN, either cite this name in EN's status block and attachment list, or attach a byte-identical copy under the expected name. Either way, list it in the regenerated manifest.

## 5. Files read
- v1 and v2 of the KP note.
- EN_20261012T0006Z.md and MANIFEST_EN_20261012T0006Z.tsv.
- The hashes and sizes of the to_codex attachments.
- `claude_archive/scripts/kp*` (hashes).
- `claude_archive/AUDIT-KP-…` (hash).
- `claude_archive/audit_KP_checks/checks_SHA256SUMS.txt` (verified).
- HANDBACK-20261012T0007Z-FINAL.md (grep for the KP/EN/FIX-2 lines only).
