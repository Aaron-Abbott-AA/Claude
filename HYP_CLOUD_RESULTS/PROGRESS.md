# HYP cloud session — PROGRESS

Session: cloud (claude.ai/code session_018ipZ7GACBWTbpNANdAnLV8), continuing HYP(2) from session_012ij7YN37LGpSS88rmUGQ7E.
Not linked to the user's computer, so no mailbox access. **No A306 packet has been delivered.** The pending ACKs file (primary_sources/new_after_A305/ACKS_PENDING_sha256.txt) was not in the bundle.
Input bundle: HYP_CLOUD_HANDOFF_20261007.zip. All files match MANIFEST_SHA256.txt.
No file whose name contains "DZ" was opened. A DZ-CLOUD-HANDOFF zip was uploaded to this session but was left unopened.

## Log (UTC 2026-10-07)
1. **R18-T v2** (`notes/R18T_TWIST_NOTE_v2.md`) — owner revision applying audit FIX-1..7 (+N1, N3–N8, N10).
2. **Revision check of v2** (`reviews/REVISION_CHECK_HYP_M2_ROUND18T_V2_20261007.md`, fresh referee, own checks in `reviews/revcheck_R18Tv2_checks/`). Verdict: **PASS-with-fixes**.
   - FIX-1..7 are all ADDRESSED.
   - Lemma 2.1A was verified by hand and by exact GF(2) computation (E=4,8,16, Fermat).
   - The (N10) remark is correct.
   - §§3–4 numbers recompute exactly (1764 grid cases).
   - Seven minor items RC-1..7 were raised.
3. **R18-T v2.1** (`notes/R18T_TWIST_NOTE_v2_1.md`) — applies RC-1..7, so it is the final version for PRIMARY.
   - RC-1: self-contained Lemma 2.1A proof.
   - RC-2: N10 uses the alignment coefficients.
   - RC-3: N2 applied; N9 deferred (script comments only).
   - RC-4, RC-5, RC-6, RC-7: wording and citations.
   - No statement, label or number changed relative to v2.
   - **Ready to send to PRIMARY** (in A306, once the R19 audit is in).
4. **R19 audit** (`audits/AUDIT_HYP_M2_ROUND19_20261007.md`, fresh referee; checks in `audits/audit_R19_checks/`). Verdict: **PASS-with-fixes**.
   - No headline claim breaks, and all Cor. 4.2 thresholds stand. Every number was reproduced independently.
   - FIX-1 (Thm 4.1 Step 3, the Z(λ) places) and FIX-2 (Lemma 1.1(i) at singular branches) are substantive. Neither changes a number.
   - FIX-3..8: labels, understatements, wording and citations.
5. **R19 v2** (`notes/R19_CORRESPONDENCE_ROUTE_v2.md`) — applies FIX-1..8 and N1–N8.
6. **Revision check of R19 v2** (`reviews/REVISION_CHECK_HYP_M2_ROUND19_V2_20261007.md`; checks in `reviews/revcheck_R19v2_checks/`). Verdict: **PASS-with-fixes**.
   - FIX-1 and FIX-2 were re-derived.
   - All Cor. 4.2 numbers were recomputed from v2's (4.1) and are unchanged.
   - Eight minor items RC-1..8 were raised.
7. **R19 v2.1** (`notes/R19_CORRESPONDENCE_ROUTE_v2_1.md`) — applies RC-1..8. It is final. No statement, proof step or number changed; RC-5 fills two missing table cells.
8. **A306 draft** (`A306_draft/`) — packet kit for PRIMARY (R18-T v2.1 and R19 v2.1, each with its audit and revision check, plus scripts). **NOT delivered**: the local HYP session must poll, acknowledge, build and place it (see `A306_draft/README.md`).

9. **R20 owner v1** (`notes/HYP_M2_ROUND20_owner_v1.md`, scripts in `notes/R20_owner_scripts/`) — **UNAUDITED owner draft**; the independent audit is IN PROGRESS. Do not send it to PRIMARY before the audit. What it claims, all inside (𝒦):
   - Frobenius reduction on the subline gives no ≈a/E bound. Negative results: Prop 2.2, Prop 2.3, Example 2.4.
   - Prop 3.1: constant T in (𝒦) forces a>=d′, which would close constant-T (R2) at n=256 for every D.
   - Lemma 4.2 / Thm 5.1: a per-point bound with no τ_0 restriction, at n=256.
   - Prop 5.2: uses the N4 inequality.
   - Lower 𝔮-thresholds for non-constant T: r=4 2E/Q (n=256) and nE/(16Q) (n>=512); r=8 2E/Q, 32E/Q, 64E/Q (n=256, 512, 1024); r=16 8E/Q.

## Statuses (R19 v2.1)
- Prop 1.1, Prop 1.2 (F_E-subline), Lemma 1.4, Lemma 1.5 (with the cusp-tangent exception) and Example 1.6: PROVED.
- Lemma 1.1: PROVED for m(w)<E; OPEN for m(w)>=E.
- Thm 2.1, Cor 2.2 (invariance ⇒ T constant): PROVED.
- Lemma 3.0, Lemma 3.1 (𝒦 normal form), Cor 3.2, Prop 3.3 (ρ·deg[T]<=a·d'), Prop 3.4 and Lemma 3.5: PROVED.
- Thm 4.1: PROVED, with the repairs. Cor 4.2: COMPUTED exactly and reproduced independently twice. (𝒦) with non-constant T is closed for r=4 at 𝔮>=E/4, for r=8 at n<=512 with 𝔮>=nE/(16Q) or nE/(4Q), and for r=16 at n=256 with 𝔮>=512E/Q.
- Prop 5.1(ii) and the 5.2 degree counts: PROVED. Prop 5.1(i) and "the route cannot improve (R1)": HEURISTIC.
- Arithmetic monodromy transitive: COMPUTED for E=8 and 16; not decided for E=32.

## Statuses (R18-T v2.1)
- Lemma 1.1, Lemma 1.2, Lemma 2.1 and Lemma 2.1A (Γ'⊃Bs(f)): PROVED.
- Prop 2.4 (i)–(v) (decoupling): PROVED.
- Prop 2.2 and Cor 2.3: CONDITIONAL on (H_lift), which is OPEN.
- Remark 2.5 obstruction: CONDITIONAL/HEURISTIC.
- Def 3.0, Lemma 3.1, Lemma 3.2, Prop 3.3 and Thm 3.4: PROVED.
- Cor 3.5: COMPUTED (exact).
- Props 4.1, 4.2: PROVED. Example 4.3: COMPUTED, and not a model.
- OPEN: constancy of T in 𝔇_16, (R1), (R2), (R3), (R4), (H_lift).
- Carried over: R17 v2.1 and R18 v2.1 were audited, revision-checked and sent as A305.

## Mailbox
Not linked. No A306 has been delivered; the packet kit is in A306_draft/. The pending-ACK file named by the user is not present in the bundle.

## Hashes (sha256)
361c929170381d83a82dd1baa4741a6025b3f9054838e024a641fce1d2ddcbf6  notes/HYP_M2_ROUND20_owner_v1.md
419b99c61b7d1d4333aa3ee64b283ba22dc9e60c7a39f1fa88c5684a93bf201b  notes/R18T_TWIST_NOTE_v2.md
65ba7f0bdffda18145365625e13d138c4e66b70015100fe0dbe0ff33e25b41ed  notes/R18T_TWIST_NOTE_v2_1.md
215b9925a4e042c4b449a587e45e898613349a58d799a87b454991e31555c8cd  notes/R19_CORRESPONDENCE_ROUTE_v2.md
465496ba78a7c5704139fd938ac0f3bc5316b949731e20ac545ed0219a576be1  notes/R19_CORRESPONDENCE_ROUTE_v2_1.md
63ea9f4bb675a8d6c808ad9f7a2700dc6f4aa9dc6db8a1cab05577244e3c4fcf  reviews/REVISION_CHECK_HYP_M2_ROUND18T_V2_20261007.md
1edc8e8d73872b99d845d0514d05f8440325ea59acc74c6875b066147893d909  reviews/REVISION_CHECK_HYP_M2_ROUND19_V2_20261007.md
f3013a20c4df2acc5f8972a29300e26a28832c262bd589814b7c3f515aa3e35c  audits/AUDIT_HYP_M2_ROUND19_20261007.md
bb192fc85e963433ed4a24779770e96b674cf3bb6817b0daf51aa482bcf5d35a  A306_draft/src/M2_ROUND18T_AUDIT_OF_V1.md
65ba7f0bdffda18145365625e13d138c4e66b70015100fe0dbe0ff33e25b41ed  A306_draft/src/M2_ROUND18T_NONCONSTANT_TWIST_REDUCED_COVER_KERNEL_ALIGNED_v2_1.md
63ea9f4bb675a8d6c808ad9f7a2700dc6f4aa9dc6db8a1cab05577244e3c4fcf  A306_draft/src/M2_ROUND18T_REVISION_CHECK_OF_V2.md
f3013a20c4df2acc5f8972a29300e26a28832c262bd589814b7c3f515aa3e35c  A306_draft/src/M2_ROUND19_AUDIT_OF_V1.md
465496ba78a7c5704139fd938ac0f3bc5316b949731e20ac545ed0219a576be1  A306_draft/src/M2_ROUND19_OWN_LINE_CORRESPONDENCE_KERNEL_ALIGNED_COUNT_v2_1.md
1edc8e8d73872b99d845d0514d05f8440325ea59acc74c6875b066147893d909  A306_draft/src/M2_ROUND19_REVISION_CHECK_OF_V2.md
76828abcfd5dce535ce3df3a1f4a37522ed8918a5043c5a9f3b8db82e7e2805a  A306_draft/src/message_template.md
f621ebbda9be9b86507ffe48f4320089129bad2404d722a41457499ee6177789  A306_draft/src/scripts_audit_checks.tar.xz
8db929b026b651161c982efef1c1433afd06ebaf0a3cf2403074056544fc310f  A306_draft/build_A306.py
