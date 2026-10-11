# REVISION CHECK of HYP M>=2 round 24, owner v2 (7 October 2026)

This is an independent revision check of `src/HYP_M2_ROUND24_owner_v2.md` (sha256 `2fe03398…e231`). It is checked against `src/inputs/R24_v1.md` (sha256 `111cced0…1edd`, the same file the audit checked) and `src/inputs/AUDIT_HYP_M2_ROUND24_20261007.md`.

**Rules kept.**
- I read only files under `src/`. I wrote only to `checks/` and to this file.
- No file whose name contains "DZ" exists under `src/`, and none was opened.
- One owner script was run, as a copy in `checks/owner_copy/`, with `python3 -I`: `numerics_R24.py`, 0.2 s. Its output is byte-identical to the original.
- My own scripts are exact (sympy over GF(2), Fractions) and were run with `python3 -I`, one at a time. The longest took 10 s.

## §0 Verdict

**PASS-with-fixes (cosmetic only).**

- FIX-1..3 and N1–N11 are all ADDRESSED.
- **FIX-1's new construction (Lemma 2.1, step (o)) is correct: PROVED.** It holds at every z∈Γ' with f(z)≠0, singular points of Γ' included. The only inputs are global ones: FNAL common image, F|a_P (zero top, via R22 Lemma 2.4(iv)), global alignment, and f(z)≠0.
  - I verified it as exact polynomial identities on a toy with a nodal Γ' (§2). The node is the only GF(2)-point of Γ' with f≠0, and the construction works there.
  - Negative controls confirm that both common image and zero top are needed.
  - The fallback (restricting the lemma to z(u)) is not needed. It would in any case suffice, since only z(u) is used downstream.
- **No headline claim or number changed.**
  - No numeric token of v1 is missing from v2.
  - Every headline number has the same number of occurrences as in v1: 0.167242, 91941792089517/549755813888000, 32480243592761/219902325555200, 0.167228, 3780, 280, 150/150, 15/15.
  - The only new numbers are 0.147704 and 0.104306 (N1, from R22/R23), plus 17 820, 119/120 and 13/43 s (bookkeeping).
- **The standing-hypotheses wording and the sharpening are correct.**
  - The wording matches R23 §1 and R22 §1, plus "all original gates".
  - The residual needs Q>=256, and the D-lanes need D>=256 and Q>=512. I recomputed this exactly (§3).
- The three RC items below are cosmetic. None affects a claim or a label of a headline result.

## §1 Fix-by-fix table

| item | requested | v2 location | status |
|---|---|---|---|
| FIX-1 | Lemma 2.1: either restrict to z(u), or construct κ̃ at general z | Lemma 2.1 header and first bullet; proof step (o); (i) "by (o)"; status table | ADDRESSED. The construction is correct (§2). The header omits two inputs it uses (RC-1). |
| FIX-2 | Prop 4.2: formal germs. Withdraw "R22 Remark 4.4 becomes PROVED". State the local fact | §0 item 8; Prop 4.2 title, statement, (B) and end of proof; "truncation realises finite jets"; Cor 4.3 bullets 1, 3, 4; status table | ADDRESSED |
| FIX-3 | Remark 3.5: observation PROVED, "yields nothing" HEURISTIC | Remark 3.5 (two bullets); §0 "What failed"; status table | ADDRESSED. One PROVED sentence now sits inside the HEURISTIC bullet (RC-2). |
| N1 | Thm 3.3, case 𝔮_max>S: cite 5.3(i),(ii) and R23 Cor 4.2(i) | Thm 3.3 statement bullet 1 and proof | ADDRESSED. I checked 0.104306 and Cor 4.2(i) "for every 𝔮_max" against R22 and R23. |
| N2 | Standing-hypotheses qualifier in §0 "Newly closed" and in the title | title; §0 item 5; §0 "Newly closed"; Cor 2.5 status row | ADDRESSED. The list matches R23 §1. §5's header keeps v1's shorter list (RC-3). |
| N3 | "FNAM2" should read "Δ≢0", with "(given (2.1),(2.2))" | §0 item 3; Cor 2.3(i); status table | ADDRESSED. No incorrect use of "FNAM2" remains. |
| N4 | Residual Q>=256; Q>=512 on the D-lanes | §0 COMPUTED Part C; §0 residual; Cor 2.4; §5 | ADDRESSED. Recomputed exactly (§3). The Part C row of the §6 table is not annotated (RC-3). |
| N5 | The toy checks (B) only along ℓ_u | Remark 4.4; §6 table; status table | ADDRESSED |
| N6 | 𝒞_A→C_A^hom; r→r_V in Lemma 3.1 | everywhere (no 𝒞_A remains outside the version history); Lemma 3.1 statement and proof | ADDRESSED |
| N7 | "at most three proper base points" | §5 next step 1 | ADDRESSED |
| N8 | The zero-alignment exclusion needs only (2.2) | "What is new in Cor 2.5"; Cor 2.5 status row | ADDRESSED. Correct: λ_A=0 gives A^tf^[Q]=0 with f^[Q]≢0, so det A≡0. |
| N9 | Record the upgrade of R23 Cor 3.3's n=256 grid result | §0 "Newly closed"; Cor 2.5 status row | ADDRESSED. Checked against R23 Cor 3.3 ("r∈{4,8}, n=256: every dyadic 𝔮>=128 closes", grid). |
| N10 | Part A header and count; det_identity timing | §0 COMPUTED; §6 table rows | ADDRESSED |
| N11 | Lemma 3.1 is classical in substance (associated curves) | after the Lemma 3.1 statement | ADDRESSED |

## §2 The new FIX-1 construction (Lemma 2.1, step (o))

**The claim.** Let z∈Γ' with f(z)≠0, and O=O_{P²,z}. Then there is κ̃_P∈O³ with κ̃_P·f^[ρ]=0 exactly and P^t≡f^[X]⊗κ̃_P mod F.

**Re-derivation.**

1. **Common image is global.** FNAL defines H_P=[f^[X]]_×P^t/F as a *global polynomial division*: "every entry … vanishes on the prime curve Γ', so F divides it". So [f^[X]]_×P^t∈F·M_3(O) at every z, with no restriction to good points.

2. **Parallel columns.** Pick i with f_i(z)≠0, so f_i^X is a unit of O. The components of [w]_×v are the three 2×2 minors w_av_b−w_bv_a.
   - If all of them are ≡0 mod F and w_i is a unit, then v−(v_i/w_i)w≡0 mod F, component by component.
   - This holds over any commutative ring. It needs neither that O/F is a domain nor that Γ' is smooth at z.
   - Hence P^t≡f^[X]⊗κ mod F, with κ=(row i of P^t)/f_i^X∈O³. ✓

3. **κ·f^[ρ]∈FO.** Global alignment gives P^tf^[ρ]=a_Pf^[X]. F|a_P holds globally: R22 Lemma 2.4(iv) derives it from zero top, then uses that F is prime in S. Hence f^[X](κ·f^[ρ])≡0 mod F. Since f_i^X is a unit, κ·f^[ρ]∈FO. ✓

4. **The correction.** e'=e_i/f_i^ρ satisfies e'·f^[ρ]=1. Put κ̃=κ−(κ·f^[ρ])e'. Then κ̃·f^[ρ]=0 identically, and κ̃≡κ mod F because κ·f^[ρ]∈FO. ✓

5. **Compatibility.** κ mod F is unique, because f^[X] is unimodular. So any two syzygy lifts differ by Fη with Fη·f^[ρ]=0, hence η∈Syz_O(f^[ρ]) since F is a nonzerodivisor.
   - This is exactly gauge (ii). Lifts from different charts i, and R22 §1's lift at z(u), are therefore gauge-equivalent.
   - R22 §1's lift λ̃(𝒜̃_11j_1^[ρ]+𝒜̃_12j_2^[ρ]) is an exact syzygy, because J^tf=0. ✓

6. **Downstream.**
   - (i)–(iii) use only (o), R18-T Lemma 2.1(ii) (global), J^{[X],t}(z) of rank 2 (its minors are κ_0^{−1}f(z)≠0), unimodularity of f^[X] and f^[ρ], and that F is prime in S.
   - These hold at every z∈Γ' with f(z)≠0.
   - The step "F|a' in S iff in O" holds at every z∈Γ', because O⊂S_{(F)}.
   - Prop 4.2's remark that Lemma 2.1 holds verbatim over Ô is fine at z(u): Γ' is smooth there, so FÔ is prime.

**Verdict on FIX-1: PROVED.** The extended statement is correct. Only z=z(u) is used in §4, so the restricted fallback is not needed. If it were, it would still suffice for everything downstream.

**Exact check (`checks/fix1_construction_toy.py` → `.out`, 10 s).** All checks are polynomial identities over GF(2)[y0,y1,y2]. The setting:
- f is the standard Cremona map and J=[(y0,y1,0),(y0,0,y2)], so κ_0=1. ρ=2, X=4.
- Γ' is F=y0²y2+y0y1²+y0y1y2+y1y2², which:
  - passes through Bs(f);
  - is irreducible over GF(2) and has a GF(2)-rational double point, so it is absolutely irreducible;
  - has a node at (1:1:1), where f≠0. This is the only GF(2)-point of Γ' with f≠0, and it is a point that R22 §1 does not cover.
- P^t=f^[X]⊗κ_0'+F(BJ^{[ρ],t}+f^[X]⊗σ_0). This satisfies common image, global alignment, F|a_P and the R18-T layer identity.

Denominators are powers of f_i, which are coprime to the prime F. So "divisible by F as a polynomial" is equivalent to "in F·O_z for every z∈Γ' with f_i(z)≠0", and each check is uniform over the chart. On all three charts f_i≠0, the following hold:
- (o): κ·f^[ρ]∈FO; κ̃·f^[ρ]=0; P^t−f^[X]⊗κ̃∈F·M_3.
- (i): J^{[X],t}S=ΩC_PJ^{[ρ],t}; the remainder is f^[X]⊗σ; a_P=Fσ·f^[ρ].
- (ii): lifts on different charts differ by Fη with η a syzygy.
- (iii): F²|a_P ⟺ σ·f^[ρ]∈FO, and the second-order lift exists mod F².

Results:
- Mode F²|a: 37/37 checks in each of 2 trials.
- Mode generic (F²∤a): 31/31 in each of 2 trials.
- The exact failing sets are empty.
- **Controls.** Without zero top, (o) fails on every chart. Without common image, (o) fails on every chart, as do the hypotheses themselves. So the checks are not vacuous, and both hypotheses of (o) are needed.

## §3 Standing hypotheses, residual sharpening, headline invariance

**Standing hypotheses.** v2 lists: global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮_max>=128, all original gates. This is R23 §1 (= R22 §1 with 𝔮_max) plus "all original gates", which matches v1's §1 ("including G5 and PRIM"). Correct.

**Sharpening (`checks/sharpening_exact.py` → `.out`, exact).**
- r, Q, S, 𝔮 are powers of 2 (R23 notation). q=Eh, so n=h/E is a power of 2. The strip gives n<4Q, i.e. n<=2Q.
- Cor 2.4 excludes n=256, so n>=512, which forces Q>=256. This is correct.
- D-lanes: D=2^{s mod v} with Q=2^v and S=2^s (PRIMARY FNAP), so D<Q. The residual needs 512<=n<4D, so D>=256 and then Q>=512. This is correct. It also gives S>=D>=256, which v2 does not state (optional).
- Exact recomputation on r∈2^2..2^12, Q∈2^7..2^20, S∈2^6..2^20 (2310 rows), n dyadic up to 2^40, using feasibility "⌈8nE/625⌉−1+Q−QS>=4E−4":
  - The feasible set at n=256 is empty.
  - Ignoring n<4Q, the least feasible n is 512 for every row (this reproduces Part C).
  - Inside the strip, Q=128 has no feasible scale (empty set). The rows that are feasible with Q<256 form the empty set. Every Q>=256 row is feasible at n=512, so the condition Q>=256 is exactly sharp.
  - D-lanes (1936 rows with D>=4): 924 are feasible with n<4D, and the set violating "D>=256, Q>=512, S>=256" is empty.
- Owner `numerics_R24.py` rerun: byte-identical.

**Headline invariance (`checks/numbers_labels_diff.py` → `.out`; `checks/diff_v1_v2.txt`).**
- The v1→v2 diff has 253 lines. Every change is either a [v2]-tagged fix, the version history, or the renaming of 𝒞_A and r.
- The statements of Lemma 3.1, Thm 3.3, Prop 2.2, Cor 2.3, Cor 2.4 and Cor 2.5 are unchanged in content. Their wording changes only by N1–N4, N6 and N8.
- Thm 3.3's 𝔮_max>S bullet now correctly allows "(𝒦) or <=0.104306q" (N1). This makes the case more precise and is not a new claim.
- **Labels.**
  - PROVED rises from 31 to 33 occurrences: the FIX-3 split and "PROVED for formal germs". It is not added to any new claim.
  - HEURISTIC rises from 8 to 15: FIX-2, FIX-3, and the explanatory text.
  - CONDITIONAL, OPEN and CITED are unchanged.
  - The status table changes only in the rows for Lemma 2.1, Prop 2.2, Cor 2.3, Cor 2.5, Remark 3.5, Prop 4.2 and Cor 4.3, all as the fixes require.
- I found no new overclaim. The new sentence "every finite jet is realised by polynomials" (truncation of the formal germ) is correct. "R22 Remark 4.4 stays HEURISTIC" is correct.

## §4 RC issues (all cosmetic; none affects a claim)

- **RC-1 (Lemma 2.1 header citations).** The header lists "FNAL common image, zero top, R18-T Lemma 2.1(ii), FNAM1", but step (o) also uses two further inputs:
  - global alignment (P^tf^[ρ]=a_Pf^[X]);
  - R22 Lemma 2.4(iv), for the *global* divisibility F|a_P. In R22, "zero top" is the first-layer condition κ_P·f^[ρ]=0 on Γ', and F|a_P is derived from it there.

  Both are standing or audited inputs. Suggest adding them to the header.
- **RC-2 (Remark 3.5 labels).** The sentence "If ε_top<N_1, R22 Prop 5.5 already closes it (R23 §3, RC-1)" now sits inside the (HEURISTIC) bullet. It is a PROVED statement (R23 v2.1 RC-1). Suggest moving it to its own bullet, or to the PROVED bullet.
- **RC-3 (two places missed by N2/N4).**
  - The §6 table row for Part C still says "least feasible n=512 for all 280 (r,Q,S)" without the n<4Q caveat that §0 and Cor 2.4 now carry.
  - The §5 header keeps v1's abbreviated hypothesis list "(global alignment, Q>=128, 256E<=h<4QE, 𝔮_max>=128)".

  Suggest one [v2: N4] annotation, and "standing hypotheses of §1" in §5.
- *Optional:* on the D-lanes, D=2^{s mod v}<=S also gives S>=256.

## §5 Files in `checks/` (checksums in `checks/checks_SHA256SUMS.txt`)

| file | content | result |
|---|---|---|
| `diff_v1_v2.txt` | `diff` of v1 against v2 | 253 lines; all changes accounted for |
| `numbers_labels_diff.py` → `.out` | multiset comparison of numeric and label tokens; status-table row diff; [v2] tag census | no v1 number lost; headline counts equal; N1–N11 and FIX-1..3 all tagged |
| `fix1_construction_toy.py` → `.out` (10 s) | Lemma 2.1 (o), (i)–(iii) as exact identities over GF(2)[y0,y1,y2], nodal Γ', all charts, 2 controls | 37/37 and 31/31 in each trial; exact failing sets empty; controls fail as expected |
| `sharpening_exact.py` → `.out` (0.2 s) | Cor 2.4 and N4 sharpening, exact | n=256 infeasible; Q>=256 exactly; D-lanes D>=256, Q>=512 (and S>=256) |
| `owner_copy/numerics_R24.py`, `numerics_R24.rerun.out` | owner script rerun | byte-identical |
| `src_SHA256SUMS.txt` | sha256 of all 33 `src/` files | — |
