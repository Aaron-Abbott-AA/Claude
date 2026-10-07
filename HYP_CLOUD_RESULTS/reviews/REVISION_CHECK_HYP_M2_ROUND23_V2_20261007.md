# REVISION CHECK — HYP M>=2, round 23 (owner v2)

This is an independent revision check of `src/HYP_M2_ROUND23_owner_v2.md` against `src/inputs/R23_v1.md` and `src/inputs/AUDIT_HYP_M2_ROUND23_20261007.md` (FIX-1..5, N1–N6). Date: 7 October 2026.

**Scope and rules followed.**
- I read only under `src/`, and I wrote only under `checks/` and to this file.
- No file whose name contains "DZ" was opened; `find` shows that none exists.
- `checks/src_SHA256SUMS.txt` verifies 28/28 files. The owner `SHA256SUMS.txt` verifies 4/4.
- The owner script `numerics_R23_v2.py` was copied to `checks/owner_copy/` and re-run with `python3 -I` (9.8 s). Its output is **byte-identical** to `src/owner_scripts/numerics_R23_v2.out` (SHA256 963abf3c…e1).
- I also checked that Parts A, C and D (lines 1–76) of the v2 output are byte-identical to v1's `numerics_R23.out`, as v2 claims.
- My own scripts are exact (Fraction and integer polynomials with isqrt), written from the R19/R20/R22 texts and not from owner code. They ran with `python3 -I`, one process at a time; the longest run was 33 s.

---

## Verdict

**PASS-with-fixes (minor).**
- All five fixes and all six notes are addressed.
- FIX-1 was recomputed independently, by brute force over every integer τ_0. Every interval quoted in v2 is exactly right.
- FIX-2 is correctly implemented, and its central claim holds in an even stronger form than v2 states: the literal m=E−X already reproduces every closure.
- No closure and no headline number changed. The diff from v1 to v2 contains only the marked revisions.
- The remaining items are minor:
  - RC-1 is the one substantive one. v2 adds a new sentence in §3 whose stated justification is insufficient, although its conclusion is true.
  - RC-2..RC-5 are wording and precision fixes.

---

## Fix-by-fix table

| item | status | location in v2 | referee check |
|---|---|---|---|
| **FIX-1** (r=16, n=256 failing sets) | **ADDRESSED** | version history; §0 "What remains"; Cor 3.3 (r=16 bullet); §6 next step 2; §7 diagnostics rows | Recomputed independently (`fix1_failing_sets.out`); details below. Every quoted interval matches. "Single value" survives only where v2 itself quotes v1. "Small per-point gain" is withdrawn. 8E/Q is unchanged. |
| **FIX-2** (attribution of Cor 3.3) | **ADDRESSED** | §0 idea and items 5 and "Newly closed"; Remark after Prop 2.1; Prop 3.2 heading and "Weaker form"; Cor 3.3 heading and mode "R22only"; §8 table | Prop 3.2's weaker form is correct. The crediting of Cor 3.3 is correct. Literal m=E−X, N_1=1 reproduces the R23 closures on 198/198 rows and 112/112 B2 cases. See RC-2 and RC-3. |
| **FIX-3** (overclaim "unconditional"; "newly closed") | **ADDRESSED** | §0 item 9 and "Newly closed"; Cor 4.5 statement and Remark; §8 table | "Unconditional" is withdrawn, and the hypothesis ε_top<N_0 is kept. Classical V and dim V=2 are marked "already in R22". The 𝔮_max restriction is called vacuous, which is correct (N_0>=7). The optional observation was implemented in a changed form; see RC-1. |
| **FIX-4** ("none" rows not vacuous) | **ADDRESSED** | §0 COMPUTED; Cor 3.3 self-check; §8 table | Over the 74 "none" rows of the 198-row grid, τ_hi at the least closing 𝔮 lies in {1,2,6,12}. The examples check: 12 at (8,2048,1024,64), 2 at (16,512,256,64), 6 at (8,8192,16384,64). `fix2_fix4_modes.out` |
| **FIX-5** (Cor 5.2 edge-case citation) | **ADDRESSED** | Cor 5.2; §8 table | The new argument is valid. With m=E>a=E−1, the line form ξ^ω_u has degree a but order >=E at z(u), so ξ^ω_u≡0 and u∈𝔅 (R20 Lemma 4.2 proof, Lemma 4.3). m=E−X<a would not suffice. Wording fix: RC-4. |
| **N1** (S>=128 superfluous; any 𝔮>=2) | **ADDRESSED** | §0 item 6; §1 after (1.1); Prop 4.1 (new case S=64); §8 table | The S=64 case is correct. R22 Lemma 5.1(a) with 𝔮_max>S gives min(ν_u,e_u)>=E, so 𝔅_0=∅ and 𝔡=0 at every good point. |
| **N2** (Γ' smooth at z(u)) | **ADDRESSED** | §1, new paragraph | The audit's sentence is reproduced. |
| **N3** (N_1=2rS/𝔮_max) | **ADDRESSED** | §3 "Residual of (R2)" | Correct, including "N_1=1, condition void if 𝔮_max>2rS". |
| **N4** ("Frobenius non-classical") | **ADDRESSED** | §0 "What remains"; Cor 4.5 title and Remark; §6; §8 | No occurrence of "Frobenius non-classical" remains, except in v2's quotation of v1. |
| **N5** (Q=8192, 198 rows) | **ADDRESSED** | §7 Part B row | The owner grid is still described as 162 rows; that is correct for the owner grid. My recount over 198 rows, Q=8192 included, agrees in all five modes. |
| **N6** (audit toys) | **ADDRESSED** | §7 caveat | The toys are cited as the audit's and described as checks of mechanism, not original models. |

---

## FIX-1: independent recomputation

**Setting.**
- r=16, n=256, Q=128, S=64, so E=131072.
- R23 mode: m=E and N_1=⌈E/(ρ𝔮)⌉.
- R20 Cor 5.3 normalisation, with a=8h/625−d'+X−ρ taken as an exact upper bound (not floored).
- A τ_0 is excluded if (4.1)-N4 holds (on the domain τ_0<=d'−E+N_1−1) or (4.1′) holds, each against 1551q/4000.

**Methods used.**
- An exact integer-polynomial interval solver.
- A brute-force scan of **every** integer τ_0∈[1,τ_hi]. At 𝔮=128 that is 5.48M values.
- Direct Fraction evaluation of the printed formulas at every interval end ±1.

All three agree.

| 𝔮 | d' | τ_hi | N4 holds | (4.1′) holds | failing set (referee) | v2 says |
|---|---|---|---|---|---|---|
| 4096 = 4E/Q | 2E−2 | 171385 | [1,5472] | [63626,τ_hi] | **[5473,63625]** (58153 values) | [5473,63625] ✓ |
| 4096 | 2E+4 | 171383 | [1,5500] | [63608,τ_hi] | **[5501,63607]** | [5501,63607] ✓ |
| 1024 | 2E−2 | 685541 | [1,1808] | [254503,τ_hi] | **[1809,254502]** | ✓ |
| 1024 | 2E+4 | 685533 | [1,1817] | [254430,τ_hi] | **[1818,254429]** | ✓ |
| 128 | 2E−2 | 5484333 | [1,1527] (domain ends at 131085) | [2036041,τ_hi] | **[1528,2036040]** | ✓, including "131085 only the end of N4's domain; N4 holds only up to 1527" |
| 128 | 2E+4 | 5484267 | [1,1535] | [2035462,τ_hi] | **[1536,2035461]** | ✓ |
| 8192 = 8E/Q | all 7 values | 85692 | all | – | ∅ (closes) | threshold 8E/Q unchanged ✓ |

**Union over all seven d'.** The failing sets for the five intermediate d' are nested inside the d'=2E−2 set. So the unqualified quotes in §0 and §6 ([5473,63625] and [1528,2036040]) are also correct as unions over d'.

**Places in v2 that cite these numbers** (all consistent with the table):
- the version history ("~58 000");
- §0 "What remains";
- Cor 3.3, the r=16 bullet;
- §6 step 2;
- §7, the diagnostics (v1) and `numerics_R23_v2` rows.

---

## FIX-2: Prop 3.2, Cor 3.3 crediting, and uses of the bootstrap

**The weaker form of Prop 3.2.** In (𝒦), R20 Lemma 4.2's order step gives order >=min(ν_u,e_u) on ℓ_u. With R22 Cor 3.2 (ν_u>=E−X) this gives m>=E−X, and so D_1>=d'−a−X. That is what v2 states, and its conditionality is right: R22 Cor 3.2 replaces Prop 2.1.

**Crediting of Cor 3.3** (`fix2_fix4_modes.out`). I ran five modes on 198 rows (r∈{4,8,16}, all Q from 128 to 16384 including 8192, S∈{64,256}, n<=8192, n<4Q) and on the 112 B2 cases:
- R20: m=min(ρ𝔮,E);
- R23: m=E, N_1=⌈E/(ρ𝔮)⌉;
- R22ceil: m=min(ρ𝔮⌈(E−X)/(ρ𝔮)⌉,E), which is v2's "R22only";
- EXplain: the literal m=E−X, N_1=1;
- EXmax: m=max(min(ρ𝔮,E),E−X).

Results:
- R22ceil, EXplain and EXmax each agree with R23 on **198/198** rows and **112/112** B2 cases.
- R23 differs from R20 exactly on the 32 rows with n=256 and r∈{4,8}; every 𝔮 closes there.
- R20 mode reproduces the R20 v2.1 table: 2E/Q; 32E/Q; nE/(16Q); 64E/Q; 8E/Q; "none".

So "the gain of Cor 3.3 needs only R22 Cor 3.2" is correct, even in its literal E−X form.

**Uses of the bootstrap in v2.** Prop 2.1(ii) is load-bearing in:
- Thm 3.1, via Prop 2.1(iii) and Cor 2.2(i),(ii);
- Cor 5.2, both in its edge case and in Prop 2.3's (𝒦)-order 2E+ρ−X used in its main count.

It also appears in two non-load-bearing places: the m=E statement of Prop 3.2 and mode R23.

There is one further use that FIX-2's lists do not mention: §3 "Residual of (R2)" applies R22 Prop 5.5 "with N_1 in place of N_0 by Prop 2.1" (RC-2).

Cor 2.2(iii) and Remark 5.3 do not use the bootstrap. Prop 4.1, Cor 4.2 and §4 do not use it either.

---

## v1→v2 diff (`checks/diff_v1_v2.txt`, `checks/numbers_v1_v2.out`)

**The diff.** It has 183 lines. Every change carries a "[v2: FIX-n]" or "[v2: Nn]" mark, except the version, status and "audited" wording and the script-runtime line.

**Numbers.**
- The only numeric tokens removed are v1's diagnostic numbers 2036041, 254503 and 63608. The values 131085 and 63626 survive, but in fewer places.
- Every headline number has the same count in v1 and v2: 0.0925781 and its exact fraction, 0.092579, 0.240046, 0.238, 0.119, 0.4766, 443, 1260, 0.08263, 0.104306, 0.147704, 2E/Q, 32E/Q and 64E/Q.

**Closures.** No closure was added or withdrawn. The "Newly closed" list only lost "classical V", which is now marked as already in R22.

**Labels.** Labels agree across §0, the body and the §8 status table, with one exception: the new §3 sentence (RC-1) has no label. No new overclaim was found apart from RC-1.

---

## RC list

**RC-1 (new claim, insufficient justification; conclusion true).**

*Where.* §3 "Residual of (R2)", marked "[v2: FIX-3, audit's optional observation]".

*What v2 says.* "For ε_top<N_1 the weight N_1−ε_top is >=1, so R22 Prop 5.5's count is automatic there as well."

*Why the reason fails.* Weight >=1 alone does not make the count close. With only Σε_i<=2ε_top<=2(N_1−1), the bound fails to close in 1389 of 8820 grid cases (`r2_prop55_weight.out`).

*Why the conclusion holds.* N_1=2rS/𝔮_max is a power of 2, and Lemma 4.3(i),(iv) apply to any V of dim<=4. Together they give Σε_i/(N_1−ε_top)<=6. The maximum is at ε=(0,1,2,3) with N_1=4; for N_1>=8 the ratio is <=10/3. So the bound is <=0.068732q on the whole strip, which equals R22's classical-case number.

*Fix.*
- Replace the reason with this one.
- Label the sentence PROVED (from Lemma 4.3), numbers COMPUTED.
- Note that it differs from the audit's observation, which concerned N_0 and γ.

**RC-2 (FIX-2 lists of bootstrap uses incomplete).** The Remark after Prop 2.1 and the version history say the raise to E is used "by Thm 3.1 and Cor 5.2's edge case". Two more uses should be added:
- §3's "N_1 in place of N_0 by Prop 2.1", for Prop 5.5 in (R2);
- Prop 2.3's (𝒦)-order, which Cor 5.2's main count uses.

**RC-3 (precision; optional).** Prop 3.2's weaker form and §0 say "m>=E−X". The backing mode "R22only" uses R22 Cor 3.2's ceiling form, min(ρ𝔮⌈(E−X)/(ρ𝔮)⌉,E). The statement is nonetheless literally true: m=E−X, N_1=1 gives identical closures (198/198 rows, 112/112 B2 cases; referee). v2 could cite this, or state the ceiling form.

**RC-4 (wording, Cor 5.2 edge case).** "|𝔅|<=B_𝔅=O(E²)≪q" should read: N_good <= |𝔅| + cuspidal places (<=2d'+2g−2) + the standing charges (Nd, {det T̂=0}, 𝔈, boundary) < 1551q/4000. The charge Nd≈0.0256q is not O(E²). The conclusion is unaffected.

**RC-5 (cosmetic).**
- Cor 3.3's "(τ_hi=171385)" holds for d'=2E−2; at d'=2E+4, τ_hi=171383.
- §0's "at 𝔮=128 on [1528,2036040]" is the d'=2E−2 set, which is also the union over d'. Adding "d'=2E−2" or "union over d'" would make this precise.

---

## checks/ files

| file | content |
|---|---|
| `src_SHA256SUMS.txt` | provided; verifies 28/28 |
| `owner_copy/numerics_R23_v2.py`, `owner_copy/numerics_R23_v2.rerun.out` | owner v2 script, re-run; byte-identical to `src/owner_scripts/numerics_R23_v2.out` |
| `rc_bounds.py` | referee's exact implementation of (4.1)-N4 (with N_1) and (4.1′), R20 Cor 5.3 normalisation, in five m-modes; exact interval solver |
| `fix1_failing_sets.py` → `.out` | FIX-1: failing sets for 𝔮∈{128,1024,4096,8192}, all 7 d'; brute-force scan of every τ_0; direct-formula checks at the interval ends |
| `fix2_fix4_modes.py` → `.out` | FIX-2, FIX-4, N5: least closing 𝔮 per row, 198 rows × 5 modes; B2 112 cases; τ_hi in the "none" rows |
| `r2_prop55_weight.py` → `.out` | RC-1: weight and order-sum ratios for N_1=2^j; bound on the whole strip and on an 8820-case grid |
| `numbers_v1_v2.py` → `.out` | numeric-token diff of v1 and v2; headline-number counts |
| `diff_v1_v2.txt` | `diff` of v1 against v2 |
| `checks_SHA256SUMS.txt` | SHA256 of all the above |
