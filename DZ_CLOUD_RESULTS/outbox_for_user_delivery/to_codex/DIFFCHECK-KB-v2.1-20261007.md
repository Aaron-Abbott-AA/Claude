# DIFFCHECK — KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.1.md against v2 (independent referee, cloud session, 7 Oct 2026, 21:20–21:22Z)

Referee: the same isolated subagent that wrote REVISION-CHECK-KB-v2-20261007.md (sha256 `5a61b09e53709ad866aa8ed5b7485eb9d1758780b71e0f2da966c9c15c46944d`). The same rules and isolation applied.

**Notes compared:**
- v2: sha256 `4af210536e8b98d17be78024c65ce4ffadd0a1c464490dc0d6634598fe49df59`.
- v2.1: `src/KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.1.md`, sha256 `1cc7fc50f72689de55cbc915219f7314806e32dec470bc1356fe796034d6b385`, 13815 bytes.

## Verdict: **PASS**
- All five RC items are applied correctly.
- The diff contains no other change.
- Version naming is consistent.
- The outbox copy is byte-identical to the archive copy.
- All four MANIFEST hashes and sizes verify.
- **EJ_20261007T2120Z can be flipped to READY FOR USER DELIVERY.** The packet's own device-only steps still apply.

## 1. Diff v2 → v2.1 (`diff`: 10 hunks, every one accounted for)

| Hunk (v2.1 lines) | Content | RC | Check |
|---|---|---|---|
| l.1, title | "The inner-resonance B = 1 subcase is global half-field and goes to HFA [A]; the general B = 1 case (g < 3ρ/2) is a partial half-field and stays OPEN [v2.1: RC-1]". The version tag reads "owner note v2.1, … 21:19Z; v2 21:10Z; v1 20:59Z". | RC-1 | Correct; this is the requested wording. |
| l.6–11, status block | Header "AUDIT STATUS (v2.1)". Records the full sha256 of the audit, the v2 prefix 4af21053…fe49df59, and the full sha256 and verdict of the revision check. States "applies RC-1 to RC-5" and "PENDING DIFF-CHECK". | RC-5 | Every hash and verdict matches the actual files. |
| l.17, §0 | v := \|N\| > q/2 (GO's input step / EBR Lemma G [A]). | RC-3 | Correct. |
| l.73, (vi) proof | Curve renamed to Y^e = k, with a note explaining why. | RC-2 | Correct; the mathematics is unchanged. |
| l.79, §1 subcase header | "the inner resonance is routed to HFA; the general case is OPEN". | RC-1 | Correct. |
| l.89–91, general B = 1 | "Status: OPEN (§4(a))", with three reasons: a₂ ≥ (3ρ−2g)/4 ≥ 1, so the case is not (H); HFD §3 is a sketch with gap G1, and its narrow repair has a size condition; its WG step needs e_w < 2^{ρ/2}, against e ≥ 2^{ρ/2+1} − 1. | RC-1 | These match the revision check's reasons, and every one is correct. |
| l.98, §2 | "B ≠ 1, or B = 1 off the inner resonance, needs arc-specific input". | RC-1 | Correct. |
| l.104–106, l.109, §3 | B = 1 is split into the inner resonance (HFA [A], pending HFA3's scope) and the general case (OPEN). The general B = 1 case is added to the OPEN list. | RC-1 | Correct. |
| l.127, §5 point (2) | Routing restricted to the inner resonance; the general case is OPEN. | RC-1 | Correct. |
| l.144–153, §6 row and new §7 | The unlogged v2 edits are now logged. A v2 → v2.1 change log covers RC-1 to RC-5, and RC-1 is marked blocking. | RC-4 | The listed locations match the diff. |

- **Nothing else changed.** §0's inputs, Proposition KB (i)–(vi) and its proof apart from the Y rename, the inner-resonance text, §4(a)/(b) and the v1 → v2 change-log rows are all byte-identical to v2.
- **Naming.** The title, the status block ("AUDIT STATUS (v2.1)", "This v2.1 applies…", "v2.1 status"), the §7 header "v2 → v2.1" and the [v2.1: RC-n] markers all agree, and they agree with the file name.

## 2. Outbox and MANIFEST (`outbox_for_user_delivery/to_codex/`)

**`cmp` results.** Every file in each row is byte-identical:

| File | Outbox | Archive | Other copy |
|---|---|---|---|
| KB v2.1 | yes | yes | referee `src/` |
| AUDIT-KB | yes | yes | referee `src/` |
| REVISION-CHECK-KB-v2 | yes | yes | referee's own copy |

**MANIFEST_EJ_20261007T2120Z.tsv** (sha256 `4333d99e8b2ca05498ff00b34fed759540e69ce7079dab39fbd1bb758016fdac`). It has 4 rows, and each row's size, sha256 and mtime match the actual file:

| File | Size | sha256 |
|---|---|---|
| EJ_20261007T2120Z.md | 3081 | `48197426d89d606fee1061549fd3c019ec65b1fd70b121f7344538a1a4ac8189` |
| KB v2.1 | 13815 | `1cc7fc50…d6b385` |
| AUDIT-KB | 21282 | `fc0cc9ce…38daf168` |
| REVISION-CHECK-KB-v2 | 14170 | `5a61b09e…c46944d` |

**EJ content.** §2(a)–(d) and §3(a)/(b) summarise v2.1 faithfully, including the OPEN status of the general B = 1 case. Its status line reads "PENDING DIFF-CHECK", and the coordinator flips it.

## 3. Observations (non-blocking, no edit required)
- **DC-1.** The status line inside v2.1, at l.11 ("PENDING DIFF-CHECK. Do not send…"), will travel to Codex unchanged. This follows the PTH v2.2 precedent, and the EJ packet together with this diff check records the outcome. Editing the note now would change its hash and force the MANIFEST to be regenerated, so leaving it is acceptable.
- **DC-2 (optional).** EJ does not list this DIFFCHECK as an attachment. If it is added, the MANIFEST must be regenerated last.

## 4. Files read
- `referee_KBv2/src/`: the v2.1 note (by diff against v2 and grep) and the v2 note.
- `outbox_for_user_delivery/to_codex/`:
  - the directory listing;
  - `EJ_20261007T2120Z.md`, in full;
  - `MANIFEST_EJ_20261007T2120Z.tsv`, in full;
  - `cmp`, sha256, size and mtime of the 4 EJ files.
- `claude_archive/`: the directory listing, plus `cmp` of the KB v2.1, AUDIT-KB and REVISION-CHECK-KB-v2 copies.
- **Not read:** HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, uploads, other scratchpads. No git. Nothing was modified except this file and its archive copy.
