# DIFFCHECK — SH-SUBHALFFIELD-CRITERION-NOTE-20261007 v1 → v2

Referee diff check, by the same isolated referee agent that wrote AUDIT-SH-SUBHALFFIELD-CRITERION-20261007.md. Written 7 Oct 2026, 23:03Z (`date -u` checked).
- Same rules and isolation as the audit. No incoming scripts were executed, no git was used, and no HYP/3PP directories, uploads or other scratchpads were read.

## Verdict: **PASS**

All fixes are correctly applied: FIX-1 (including Claim U, adopted with credit), FIX-2 and m1–m9. Nothing else changed. The packet copy is byte-identical, and every MANIFEST_EM hash is correct.

**EM may flip to READY** once this file is attached and the manifest is regenerated last, as EM's own status block prescribes.

## 1. Files and hashes

| File | sha256 | Note |
|---|---|---|
| v1 `claude_archive/SH-SUBHALFFIELD-CRITERION-NOTE-20261007.md` | 6fe44b3a…2e (full: 6fe44b3aa532917279ff06cf69568075fbb97986e36ca3a7ce13c15972668e2e) | The audited version, unchanged |
| v2 `referee_SH/src/…-v2.md` | 05f8fd30b6d1aff9bdb7cc996c7759d308a4539d66fcf4de371a4ff9ec5b946a | 18129 bytes |
| v2 `claude_archive/…-v2.md` | 05f8fd30b6d1aff9bdb7cc996c7759d308a4539d66fcf4de371a4ff9ec5b946a | Identical |
| v2 `outbox_for_user_delivery/to_codex/…-v2.md` | 05f8fd30b6d1aff9bdb7cc996c7759d308a4539d66fcf4de371a4ff9ec5b946a | **Identical to the archive v2** |

## 2. Diff v1 → v2 (`diff` of the full files; every hunk inspected)

| Item | Where in v2 | Applied correctly? |
|---|---|---|
| Title / status / change log | The title says "Owner note **v2** … 23:01Z; v1 22:40Z". The AUDIT STATUS block names v1's hash, the audit's hash (18f00635…96b68c, which matches), the verdict, and "STATUS: v2 — PENDING DIFF-CHECK". §8 "Change log v1 → v2" is present. | Yes |
| FIX-1 | SH1 now reads "depends only on W and a₂, by SH(c)". The v1 parenthetical is declared false for a₂ > a(W), with the W = λF_Q example [P + C, referee]. The corrected statement holds under a₂ = a(W) and ρ ≥ 2a₂+1. **Claim U** is stated with the hypotheses K a field of characteristic 2, a = a(W) and dim W ≥ 2a+1. Its five-step proof matches the audit's §2.2 verbatim in substance: the top map, the normalised pair, the K-linear count, deg E = deg H₁ + a ≤ 2a, and the contradiction. It is credited [P, referee; adopted]. Sharpness is cited as [C, referee] T3. The owner's added remark (K-linearity; char 2 gives H₁D₁ + H₂D₂ = 0) is correct. The title and §4(a) are updated. | Yes |
| FIX-2 | RK's header now reads "cannot be extended by a **rational (G-fixed)** root". The new paragraph "What RK does not exclude" covers: the M_W / P̃ correspondence; that W″ inherits the unique relation and the GLS₀ failure; R_P for m/2 odd; band existence [OPEN]; and the referee's [C] polynomial-root search. §3 is restricted to "cannot be a G-fixed extension", with the new [OPEN] bullet. Its dimension range 3..(m−15)/3 for ker P̃ is correct: 6 ≤ 3 + dim Z₀ ≤ (m−6)/3, which forces m ≥ 24. §5(c) adds the Codex question. | Yes |
| m1 | The title says GLS₁ (ρ > 3a₂) / twist degree < ρ−2a₂. | Yes |
| m2 | SH2: the e = 0 qualifier is moved and deg A_α ≤ a holds for every e. The ⟺ of the two dim U conditions is spelled out via SH(a) and then SH(b). | Yes |
| m3 | SH3: "with dim U > a₂" is added. | Yes |
| m4 | §3: the monomial bullet is relabelled [A] (RX v2 §3). | Yes |
| m5 | §4(a): "no (C, D)" is removed; a₂ and (N0) are made intrinsic via Claim U. | Yes |
| m6 | §6: the Vandermonde factorisation is labelled [P], with [C] as confirmation. | Yes |
| m7 | RK step 1: "(in fact ≤ 2 …)" is added, with the correct gcd. | Yes |
| m8 | §3 [OPEN] premise is labelled [COND (B1b)] / [A], with a(V_α) ≤ a*. | Yes |
| m9 | The "Consequence" after Claim U says the unique-relation hypothesis of GLO FIX-1 / RX §3 is automatic. | Yes |
| **Other changes** | None. Theorem SH (a)–(c) and its proof, RK steps 1–4 (apart from the m7 parenthesis), §3's [H] items, §4(b), §4(c), §5(a), §5(b) and §7 are byte-unchanged. The only other edit is the §5 heading ("packet EM, PENDING DIFF-CHECK"), which is appropriate. | Confirmed |

**Cited directory.** §8 cites `audit_SH_checks/`. It exists in `claude_archive/`, and `sha256sum -c checks_SHA256SUMS.txt` there gives 14/14 OK. It is byte-identical to the referee's `checks/`.

## 3. Packet EM and MANIFEST_EM_20261007T2301Z.tsv
All recomputed sha256 values and sizes match the manifest:

| File (to_codex/) | Size | sha256 | Manifest |
|---|---|---|---|
| EM_20261007T2301Z.md | 3068 | b19d8981…fc8d | match |
| SH-SUBHALFFIELD-CRITERION-NOTE-20261007-v2.md | 18129 | 05f8fd30…946a | match |
| AUDIT-SH-SUBHALFFIELD-CRITERION-20261007.md | 23224 | 18f00635…b68c | match (identical to the archive audit) |
| slcheck.py.txt | 3783 | bc74772c…4934 | match (identical to `claude_archive/scripts/slcheck.py`) |
| slcheck.log | 1124 | a060fbd3…260a | match (identical to `claude_archive/scripts/slcheck.log`) |

- The manifest mtimes agree with `stat`.
- EM's body (§2(a)–(c), §3(a)–(c)) faithfully summarises v2. It claims nothing beyond v2, and it keeps GLS₀ for arcs OPEN.
- EM currently says "PENDING DIFF-CHECK — NOT READY". **To flip it:** attach this file, update the status block, then regenerate the manifest last. The EM hash will change; this is expected.

## 4. Files read
- v1 and v2 of the SH note.
- EM_20261007T2301Z.md and MANIFEST_EM_20261007T2301Z.tsv.
- The hashes and sizes of the to_codex attachments.
- `claude_archive/audit_SH_checks/checks_SHA256SUMS.txt` (verified).
