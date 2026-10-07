# Revision check of HYP M>=2 round 21 (owner v2) against the audit of v1

7 October 2026. Independent revision check of `src/HYP_M2_ROUND21_owner_v2.md` (sha256 `60a6e253…dfc0`) against `src/inputs/AUDIT_HYP_M2_ROUND21_20261007.md` (FIX-1..6, N1–N12) and `src/inputs/R21_v1.md` (sha256 `1088d185…5de`, the file the audit checked).

Rules kept:
- Only `src/` was read. Only `checks/` and this file were written.
- No file whose name contains "DZ" was opened (none exists under `src/`).
- Owner scripts were run only as copies in `checks/owner_copy/`, with `python3 -I`, one process at a time. The longest run was 6.0 s.
- All 21 `src/` checksums in `checks/src_SHA256SUMS.txt` and all 12 entries of the owner's `SHA256SUMS.txt` verify OK (`checks/src_verify.out`).

---

## Verdict: **PASS-with-fixes** (one wording fix, RC-1; the rest are cosmetic)

- **FIX-1 (the main overclaim) is fully addressed.**
  - Nowhere in v2 (title, version history, summary, "What failed", Prop. 2.3, Cor. 2.4, Remark 2.5, §4, §5, status table) is it claimed that 𝔉_D satisfies FNAL/TSY/TSYC/FNAM in full. Nowhere is it claimed that the families "cannot be excluded" by those inputs.
  - Every surviving mention of FNAL/TSY/TSYC/FNAM is one of three things: a C-level consequence ("the content of FNAL2/TSYC/FNAM3"), the explicit OPEN lifting question, or a HEURISTIC exclusion route.
  - Cor. 2.4 is now consistent with Remark 2.5.
- **FIX-2 is correct.**
  - The monotonicity argument is valid. The term-by-term display equals the raw bound exactly.
  - Each term is non-increasing in r, Q, S and n, verified symbolically.
  - The corner values are reproduced exactly with Fractions: 0.0433718q and 0.0472784q, against 0.38775q.
  - The κ²-type bound (𝔡² in v2) is 0.11023472q < 0.1103q, and it is also monotone.
- **FIX-3 is correct.** The "newly closed" wording now credits R20 v2.1 Cor. 3.2 for (R2) at n=256 for every D. It claims as new only C̃∉𝔉_D in (R2) at n>=512 (a>=d') and in (R3). This matches R20 lines 112/119/241/383 exactly.
- **One residual overclaim is left from v1 (FIX-5, PARTIAL).** §4 "Next steps" item 3 still says "Cor. 3.3 shows that per-point residual bounds are unavailable". v2 itself relabels that statement HEURISTIC (summary item 5, Cor. 3.3, status table).
- **The diff v1→v2 (`checks/diff_v1_v2.txt`, 30 hunks) contains only fix-tagged changes and the κ(u)→𝔡(u) rename.**
  - No proof step, hypothesis or number was changed beyond what the audit asked for.
  - No new overclaim appears apart from minor wording noted below.
  - Labels agree across the summary, the body and the §6 status table. The note has no §8; its status table is §6.

---

## Fix-by-fix table

| item | status | location in v2 | comment |
|---|---|---|---|
| **FIX-1** overclaim in Prop. 2.3 / Cor. 2.4 / summary item 3 | **ADDRESSED** | version history; §0 item 3 (title, closing paragraph, OPEN bullet); "What failed" (a); Prop. 2.3 title; Cor. 2.4 (restated, OPEN bullet, consistency with Rem. 2.5); §4 residual list; §6 rows Prop. 2.3/Cor. 2.4 | The audit's wording is adopted almost verbatim. The phrases "every algebraic identity", "all/every available identit…" and "cannot be excluded" occur 0 times (`R2_text_scan.out`). Lifting to original data (global alignment, G5, FNAL quotient through TSY with C=C̃, the forgotten span(f^[X]) component, R16's vector identity) is labelled OPEN in §0, Cor. 2.4, §4 and §6. The FNAL §4 citation ("FNAL2 is NECESSARY, not sufficient … forgets a component in span(f^[X])") was checked against `PRIMARY_FNAL.md` l.80. |
| **FIX-2** whole-strip monotonicity in Cor. 2.2 | **ADDRESSED** | §0 item 2; Cor. 2.2 proof "[v2: FIX-2] Whole strip"; §6 | The display (16/625)(1+2/E)+(D+2)/n·(1+1/E)(1+2/E)+8(Q+1)/(625rQS)+6/1000+7/q equals (Nd+(D+2)(E+1)d+(Q+1)a+6d_def+7)/q exactly, at 201 points. Each term has a derivative of sign <=0 in r, Q, S and n (sympy). Corner (4,128,64,256): 7451214389181/171798691840000=0.0433718 and 8122364470431/171798691840000=0.0472784, each < 1551/4000 with margin >0.34. The grid maximum equals the corner. 3000 random non-dyadic strip points do not exceed it. The strip bounds r>=4, Q>=128, S>=64 agree with FNAP l.47. |
| **FIX-3** "newly closed" / prior state | **ADDRESSED** | §0 "Newly closed (…) [v2: FIX-3]"; §4 residual list | "Before this note …" is gone. R20 Cor. 3.2 is credited for constant (𝒦) at n=256 for every D. What is new is stated as C̃∉𝔉_D (⟺ P_D≢0) in (R2) at n>=512 (a>=d') and in (R3) for every n. What remains is 𝔉_D∩{F\|h} and 𝔉_D∩{F∤h}. The dependence on (L, B) is stated. All of this is consistent with R20 v2.1 Prop. 3.1/Cor. 3.2 and its OPEN list ("constant T with a>=d' and D∈{1,2}"). |
| **FIX-4** 0.1102q → <0.1103q | **ADDRESSED** | §0 item 4; COMPUTED bullet; Lemma 3.2(iii); Cor. 3.3; Remark 3.5; §5; §6 | Exact max 946909077437/8589934592000=0.11023472 (<=0.110235<0.1103; >0.1102). It is 0.1102324 with d'<=2E+1. The only remaining "0.1102" is inside the v2 history tag. |
| **FIX-5** ⊋→⊇; restrict Cor. 3.3 / summary item 5 | **PARTIAL** | done: §0 item 4 (⊇), item 5; Lemma 3.2(iv); Cor. 3.3 title and consequences; §6. **Not done: §4 Next steps item 3** | **RC-1.** v2 l.260 keeps v1's sentence "Cor. 3.3 shows that per-point residual bounds are unavailable". This contradicts v2's own relabelling of that claim as HEURISTIC. |
| **FIX-6** Prop. 2.3(vi) reason | **ADDRESSED** (wording nit RC-3) | Prop. 2.3(vi) | "[B] is constant (B=λ^ρB_0)" is fixed. The a>=d' ⇒ a−m>=d'−E>=#residual argument is added, consistent with R20 l.108 and Lemma 4.2 (m=min(ρ𝔮,E)<=E). |
| N1 script headers / directory name | ADDRESSED | §5 header and last row; `*_v2.py` | The diffs of the v2 copies are header-only. Re-runs are byte-identical to both v1 and v2 outputs. Cosmetic residue: RC-4. |
| N2 a=0 kernel suffices for every a | ADDRESSED | Prop. 2.1 after "unique"; COMPUTED bullet 1 | — |
| N3 GF(2)-only twist in `family_check` | ADDRESSED | COMPUTED bullet 2; `family_check_v2.py` header; §6 Prop. 2.3 row | — |
| N4 c_1c_2≠0 unnecessary | ADDRESSED | Lemma 3.1 | The η formula with c_1=0 was checked: V_2=0, (c^[T])^⊥=(c_2^T,0). |
| N5 Lemma 3.2 dependencies | ADDRESSED | Lemma 3.2 header; §6 | — |
| N6 κ_u / κ(u) clash | ADDRESSED | v2 history; §0 items 4–5; §3; §4; §5 | No defect-κ remains in v2 (17 v1 lines renamed). The scalar κ_u is kept. Residue: RC-4. |
| N7 D=2 form of W_c | ADDRESSED | Prop. 2.3(vii) | W_c=L^{−t}(h'/F)(Bc)^{⊥[2]} follows from q=h'z^{⊥[2]}. |
| N8 Remark 3.4 order claim | ADDRESSED | Remark 3.4 first bullet; §6 | Labelled HEURISTIC, with β(u)≠0, the common local frame and non-cuspidality recorded. |
| N9 PENDING headers | ADDRESSED | Inputs list | Confirmed: `PRIMARY_FNAO.md` l.3 and `PRIMARY_FNAP.md` l.3 read "independent review PENDING". |
| N10 a=deg_Y h>=d', h≢0 | ADDRESSED | Prop. 2.3(i) | — |
| N11 grid includes S<Q | ADDRESSED (rounding nit RC-2) | Cor. 2.2 proof | — |
| N12 Step 1 needs only D>=3 | ADDRESSED | Prop. 2.1, D>=4 bullet | — |

---

## RC items

- **RC-1 (wording; residual overclaim from v1; must fix).**
  - §4 "Next steps" item 3 (v2 l.260) reads "Cor. 3.3 shows that per-point residual bounds are unavailable".
  - Replace it with: "Cor. 3.3 shows that the R20 order-at-z(u) mechanism gives order 0 off Z(𝔡); that no per-point residual bound exists is HEURISTIC".
  - This completes FIX-5. No other location carries the unrestricted claim. The "What failed" (b) line already uses the restricted form.
- **RC-2 (cosmetic, numeric rounding).**
  - The D=2 true-lane supremum is 0.04723835 (at S=QD=256). To 7 digits that is 0.0472383. The note, following the audit, prints 0.0472384.
  - This is harmless as an upper bound, but it should read "0.0472383" or "<0.0472384".
  - D=1 (0.0433453, at S=Q=128) is correct.
  - These lane values are only cited ("the audit finds"). They are not used in any proof.
- **RC-3 (cosmetic, FIX-6 wording).**
  - Prop. 2.3(vi): "on its own it would push u into 𝔅 via R20 Lemma 4.2" drops the condition.
  - It should read: "if a−m+mb(u) were smaller than N_Ξ(u), Lemma 4.2 would put u in 𝔅".
  - The next bullet supplies the correct conclusion, so nothing is overclaimed.
- **RC-4 (cosmetic, N1/N6 residue).**
  - `numerics_R21_v2.py`/`.out` still name the quantity "kappa^2", whereas §5 says "deg 𝔡²/q".
  - §5 still points to `scripts/SHA256SUMS.txt`, but the delivered file is `owner_scripts/SHA256SUMS.txt`.
- **RC-5 (cosmetic, FIX-4/FIX-2 for Lemma 3.2(iii)).**
  - The whole-strip claim for the 𝔡² bound rests on "the same monotonicity as in Cor. 2.2 (audit)". The terms are in fact different: 2/n(1+1/E)(1+2/E) + (64/625)(1+2/E) + (1+2/E)/(nrS).
  - The referee verified that each of these is non-increasing (`R1_numerics_exact.out`), so the claim is true.
  - One displayed line would make it self-contained.
- **RC-6 (cosmetic, labels).** The task brief refers to a "§8". v2's status table is §6, and v2 has no §8. The §6 labels match the summary and the body item by item (`R2_text_scan.out`, last block):
  - PROVED / COMPUTED for Prop. 2.1 and Prop. 2.3;
  - PROVED (C-level only) plus OPEN for Cor. 2.4;
  - PROVED plus HEURISTIC for Cor. 3.3;
  - PROVED identity, HEURISTIC m=1 and OPEN usefulness for Remark 3.4.

No item from the audit is NOT ADDRESSED. No new overclaim was introduced. The only v1 numbers that changed are the FIX-4 ones. The FIX-2 values (0.0433718, 0.0472784, 0.0433453, 0.0472384) are additions, and the version history's "only number changed" is accurate.

---

## checks/ files

| file | content | result |
|---|---|---|
| `src_SHA256SUMS.txt` | pre-supplied checksums of `src/` | 21/21 OK |
| `src_verify.out` | `sha256sum -c` of the above and of the owner `SHA256SUMS.txt` | 33/33 OK |
| `diff_v1_v2.txt` | `diff R21_v1.md HYP_M2_ROUND21_owner_v2.md` | 30 hunks, all fix-tagged or N6 rename |
| `owner_copy/{classify_PD_v2,family_check_v2,numerics_R21_v2}.py` → `.out`, `run_log.txt` | owner v2 scripts re-run with `python3 -I` | all three byte-identical to the owner's v2 and v1 outputs (20/20 OK; 36/36 plus control; 1260 rows) |
| `R1_numerics_exact.py` → `.out` | exact Fractions plus sympy: corner values, termwise = raw, symbolic monotonicity (with a negative control), grid reproduction, D-lane corners, 𝔡² bound, 3000 random strip points | ALL OK. 0.0433718 / 0.0472784; 𝔡² 0.11023472<0.1103; D=2 lane 0.0472383 (RC-2) |
| `R2_text_scan.py` → `.out` | scan of v1 against v2 for the audit's overclaim phrases, presence of the fix tags, and status-table labels | FIX-1 phrases 0 hits; all 18 tags present; one unrestricted FIX-5 sentence left (RC-1) |
| `checks_SHA256SUMS.txt` | checksums of all of the above | — |
