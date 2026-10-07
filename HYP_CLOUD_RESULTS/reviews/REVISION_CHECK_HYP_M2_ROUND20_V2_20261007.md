# REVISION CHECK — HYP M>=2, round 20 (owner v2)

7 October 2026. This is an independent revision check of `src/HYP_M2_ROUND20_owner_v2.md` against `src/inputs/R20_v1.md` and the v1 audit `src/inputs/AUDIT_HYP_M2_ROUND20_20261007.md`.

**How the check was run.**
- `src/` was verified against `checks/src_SHA256SUMS.txt` at the start and again at the end: 21/21 files OK.
- Only `src/` was read. Writes went only to `checks/` and to this file.
- No file whose name contains "DZ" was opened.
- The owner scripts were copied to `checks/owner_copy/` and run there with `python3 -I`, one process at a time. The longest run took 37 s.
- The referee scripts `rc_*.py` are new, use exact arithmetic (`Fraction`, `galois`, `sympy`) and were run with `python3 -I`. The longest run took 39 s.

Line numbers (L…) below refer to `HYP_M2_ROUND20_owner_v2.md`.

---

## §0 Verdict

**PASS-with-fixes (minor).**

- **All fixes applied.** Every audit item (FIX-1..8, N1–N8) is addressed. One cosmetic residue of FIX-8a remains (RC-4).
- **Headline claims unchanged.** Prop. 3.1/Cor. 3.2, Lemmas 4.1–4.3, Thm 5.1 (4.1′), Prop. 5.2 and the Cor. 5.3 threshold table have unchanged statements and numbers. The only exceptions are the two edits the audit asked for: the supremum 0.7009 (FIX-8b) and max(2g−2,0) in B_𝔅 (FIX-4).
- **Threshold table recomputed independently.** It was rebuilt from the printed formulas with exact Fractions over 216 rows: 0 mismatches against the printed table, 0 against the R19 Cor. 4.2 pattern, and every closed set is upward closed.
- **The disagreement.** It is decided in the owner's favour on the mathematics. The audit's "genuine (g≠0) clusters" all lie on the collision locus j(u)=E+1, and there is no full fibre at any g≠0 point with j(u)=E. This was checked exhaustively over GF(2^21) and proved by hand.
- **One new overclaim.** The owner's addendum says these clusters are "charged in the count through Σ(j(u)−E)". That is inaccurate and needs a one-sentence fix (RC-1).
- **No other unintended changes.** The diff shows no other unintended edits and no other new overclaims. Labels in §0, the body and §9 agree, apart from a numbering slip in §0 (RC-3).

---

## §1 Fix-by-fix table

| item | status | location in v2 | comment |
|---|---|---|---|
| FIX-1 (Lemma 2.1(iii) false) | ADDRESSED | L141–143 (statement), L148–150 (proof and counterexample), L52, L115, L381, status L406 | Replaced by the affine statement, which is now PROVED: referee `rc_misc` (d) finds 0/300 affine changes that raise the level. The counterexample t·w^7 → t^7·w is reproduced. Möbius non-invariance is propagated to §0 and §7 step 2. The audit's finer Möbius statement is not adopted. That is acceptable, since (iii) is unused. |
| FIX-2 (Example 2.4 clusters degenerate) | ADDRESSED (+ owner addendum; see §2, RC-1, RC-2) | Prop. 2.3(iv) L168–171; Ex. 2.4 L175–190; §0 L59, L89–92, L13; §8 L393; status L408–409 | U_1=0/g=0 is stated. The formula Ξ=x^14(1+x^49) is included. (iv) is relabelled HEURISTIC. |
| FIX-3a (Prop. 2.3(ii) → HEURISTIC) | ADDRESSED | L58, L158, L160–163, status L408 | "Generic" is made explicit, including in §0 L87 ("Generic forms…"). |
| FIX-3b (§0 "≈a/E: no") | ADDRESSED | L45–47, L95–99, status L422 | The claim is now PROVED only for m=E. Beyond that it is HEURISTIC/OPEN. |
| FIX-3c (Remark 3.3 conclusion) | ADDRESSED | L116, L226, L230, status L420 | |
| FIX-4 (B_𝔅 with max(2g−2,0)) | ADDRESSED | L66, L255, L269–270, L284, status L415; `numerics_R20_v2.py` header | The case analysis was re-checked: N_k≥0 forces 2a−d'≥0, so both cases are <=B_𝔅. No numeric change (2g−2=d(d−3)≥0 in the code). |
| FIX-5 (Prop. 2.2 precision; t=∞) | ADDRESSED | L55, L135, L152 | `rc_misc` (e): the condition s<=a−m−K−1 is exactly the condition under which the reduction beats a−m (0 counterexamples). |
| FIX-6 (Remark 4.4) | ADDRESSED | L273–274 | See RC-6: the hypotheses (good, non-cuspidal) are left implicit. |
| FIX-7 (Cor. 2.5, Z(μ)∪Pole(μ)) | ADDRESSED | L194–202, status L410 | |
| FIX-8a (Q=8192 missing from grid) | ADDRESSED (cosmetic residue RC-4) | L81–82, L329 | Cor. 3.2 L221 and §8 L390 still say "Q∈{128,…,16384}". |
| FIX-8b (supremum 0.7009) | ADDRESSED | L221, status L412 | Recomputed: (2048/625+1/8−2)/2=0.700900. The grid maximum is 0.700669, also with Q=8192. |
| FIX-8c (stale script headers) | ADDRESSED | `*_v2.py`; §8 L390–394 | The v1→v2 diffs of `numerics_R20` and `toy_line_order` change comments only. The outputs reproduce byte-identically (§4). |
| FIX-8d (env_lib description) | ADDRESSED | L28, L395 | Matches the file header and the `from ps import *` line. |
| FIX-8e (`scripts/` vs `owner_scripts/`) | ADDRESSED | L386 | |
| N1 (k infinite ⇒ Δ≡0) | ADDRESSED | L214 | |
| N2 (non-cuspidality only; min(N,j(u))) | ADDRESSED | L240–241 | |
| N3 (Lemma 3.5(ii) set not removed) | ADDRESSED | L292 | |
| N4 (Bs(f)∩Γ' covered by δ_P) | ADDRESSED | L296 | |
| N5 (d'−E<=E+1 vs the d' scan) | ADDRESSED | L136 | |
| N6 (homogeneity in Prop. 6.2) | ADDRESSED | L353 | |
| N7 (Decimal locate + exact verify) | ADDRESSED | L313 | |
| N8 (env_lib/numerics_K not run) | ADDRESSED | L28, L395 | |

---

## §2 Adjudication: are the GF(2^21) clusters at x∈μ_49∖μ_7 "genuine" (audit) or degenerate (owner)?

### Toy data
- Γ: U_0^7+U_1^7+U_2^7=0, with e=σ1.
- Residual points: v_ζ=diag(1,ζ,ζ/(1+ζ))u^[8], for ζ∈F_8∖{0,1}.
- M(U)=[[U_0^7,U_1^7],[U_2^7,U_0^7+U_1^7]], c(u)=(√(U_2^7),√(U_0^7)), and Ξ(u,v)=det(M(v)c,M(u)c).

### (a) The formula, PROVED by the referee
On the chart u=(1,x,y), put b=x^7, so y^7=1+b. Put s=√(1+b), so c=(s,1). Since v_ζ^7=(1,b^8,(1+b)^8), a direct expansion gives

  Ξ(u,v_ζ) = (s+1)^2·(b+b^8) = (1+b+1)(b+b^8) = b^2(1+b^7) = x^14(1+x^49),

independent of ζ. This was confirmed symbolically over F_2 in `rc_fermat` (1).

Equivalently, Ξ≡0 on the fibre exactly when b∈F_8, i.e. M(u)^[8]=M(u). In that case Ξ=det(M(u)c,M(u)c)=0 trivially. The g=0 clusters (x=0) are the case b=0. The x∈μ_49∖μ_7 clusters are the case b∈F_8∖{0,1}.

### (b) The owner's proof that v_ζ=u at ζ=x^{−7} is correct
- For x∈μ_49∖μ_7, ζ:=x^{−7}∈μ_7∖{1}=F_8∖{0,1}.
- Then ζx^8=x.
- Also y^7=1+x^7=(1+ζ)/ζ, so (ζ/(1+ζ))y^8=y.
- Hence v_ζ=u. The other five v_ζ are distinct from u, because their second coordinates differ.
- Γ is smooth and e^*ℓ_u=E·u+Σ_ζv_ζ (degree 14). So ord_u e^*ℓ_u>=E+1.

### (c) Independent exhaustive computation (`rc_fermat.out`)
The computation covers all 2,095,345 affine points of Γ(GF(2^21)) with U_0=1 and U_2≠0, not 42 samples.
- Ξ is ζ-independent at every point and equals x^14(1+x^49) at every point.
- There are exactly 301 full fibres: 7 with g=0 (x=0) and 294 with g≠0, all at x∈μ_49∖μ_7.
- **j(u) computed directly**, as the multiplicity of x_u in P(X)=(1+X^7)(X+x^8)^7+y^56X^7 via Hasse derivatives. On g≠0 points the conic is a graph over x and all 14 intersections are affine.
  - Over all g≠0 points, j(u)∈{8,9}.
  - {g≠0, j(u)>E} = {some v_ζ=u} = {g≠0 full fibres}: all 294 points, each with exactly one colliding ζ, ζ=x^{−7}, and j(u)=E+1 exactly.
- **No full fibre exists at any g≠0 point with j(u)=E.**
- Since the formula is an identity on the curve, the same holds over the algebraic closure.

### (d) Verdict on the disagreement
- **On the mathematics the owner is right.**
  - The audit's statement "genuine full residual clusters (g≠0) exist at x∈μ_49∖μ_7" is literally true as to g≠0. But these are not clusters at generic (j(u)=E) points.
  - They are exactly the collision locus j(u)=E+1, and the vanishing is forced trivially: Ξ(u,u)=0 together with ζ-independence, or equivalently M(u)∈M_2(F_8).
  - The audit's conclusion "the qualitative claim (iv) survives" should therefore be withdrawn. The toy exhibits **no** full fibre at a point with g≠0 and j(u)=E.
- **Labels.**
  - Prop. 2.3(iv) as HEURISTIC is correct, and is now the right label.
  - Example 2.4 as "identities PROVED, counts COMPUTED, relevance HEURISTIC" is correct.
  - The owner's addendum ("PROVED; COMPUTED 42/42") is correct but under-reported: 294/294 hold, and the formula itself is provable (RC-2).
- **One overreach (RC-1).**
  - j(u)>E is **not** among the "good u" exclusions (R19 §3: 𝔈, boundary, {λ'=0}, {det T̂=0}, {g=0}). The Σ(j(u)−E) term in (4.1)/(4.1′) charges only the j(u)−E residual places lost to the collision.
  - At the 294 points, the other d'−j(u)=5 genuine residual places are all Ξ-zeros, and nothing in Thm 5.1 charges them as such. In a genuine (𝒦)-pencil, such points would still have to satisfy Lemma 4.2 or lie in 𝔅.
  - So the sentence "the GF(2^21) clusters are 'collision' points, charged in the count through Σ(j(u)−E)" (L188, echoed at L13) overstates the case.
  - The correct statement is: "they lie on the collision locus {j(u)>E}; this locus is not excluded from the count, but the toy shows no full fibre off it".
  - Relatedly, "N_Ξ(u)∈{0,6}" counts u itself at collision points. There N_Ξ(u)=5=d'−j(u) genuine residual places.

---

## §3 Headline claims and numbers (unchanged)

- **Prop. 3.1 / Cor. 3.2.**
  - The proof is unchanged apart from N1.
  - `rc_misc` (a): the grid maximum of a_max/d' at n=256 is 0.700669 (0.7007), the same with or without Q=8192.
  - The minimum at n=512 is 2.2921 (≈2.3).
  - The supremum is 0.700900.
  - The exact inequality 3.2768E+E/(2r)−Q/2<4E−4 holds on the test set.
- **Lemmas 4.1–4.3, Thm 5.1.**
  - The statements are textually unchanged except N2 (a strengthening remark), FIX-4 (B_𝔅) and N3/N4 (comments).
  - The (4.1′) formula lines are byte-identical between v1 and v2. The B_𝔅 definition line is added.
  - D_1/E=0.600, 0.662, 0.692 (n=256, m=E) and −2.68, −2.62, −2.58 (n=512) reproduce "0.60, 0.66, 0.69 / ≈−2.6".
- **Prop. 5.2.** Margin at r=16, Q=128, n=256, 𝔮=E/16: −0.00386 at τ_0=1 and −0.30862 at τ_hi=85692. This reproduces the printed −0.0039 → −0.31.
- **Cor. 5.3 table.**
  - The table rows are byte-identical in v1 and v2.
  - `rc_thresholds.py` was written from the printed (4.1) [incl. the FIX-2 term], (4.1)+N4 and (4.1′), with the printed normalisation, τ_hi and exclusion rule (bound<1551q/4000; (4.1) restricted to τ_0<=d'−E; all 7 d'; dyadic 128<=𝔮<=E).
  - Grid: r∈{4,8,16}, Q∈{128,…,16384} **incl. 8192**, S∈{64,256}, n∈[256,2Q].
  - Result: **216 rows, 0 mismatches** against the printed R20 table, 0 against the R19 Cor. 4.2 pattern, and 0 non-upward-closed sets.
  - The parenthetical values (E/64 and E/8192 for r=4; E/16 and E/32 for r=16) and "N4 alone: 8E/Q" for r=8 also reproduce.

---

## §4 Owner scripts (copies in `checks/owner_copy/`, run with `python3 -I`)

- **Byte-identical to the delivered outputs (`cmp`):**
  - `numerics_R20.py`, `numerics_R20_v2.py`: both outputs are identical to each other and to the delivered ones.
  - `toy_line_order_v2.py`.
  - `fermat_cluster_v2.py`.
- **Comment-only changes.** The v1→v2 script diffs (`numerics_R20`, `toy_line_order`) change comments and header only.
- **Copied, not run:** `env_lib.py` (needs the missing `ps`), `numerics_K.py`, and `fermat_cluster.py` and `toy_line_order.py` (v1; superseded and audited byte-identically before).

---

## §5 Diff v1 → v2

All 49 diff hunks were inspected. Each one is either a marked "[v2: …]" change, the version and label header, or a direct consequence of a fix. Examples of the last kind are "Generic forms" at L87, the Prop. 2.3 proof sentence at L173, and the Rules paragraph at L28.

- No theorem statement, formula or table number changed except as requested.
- The only new mathematical content is the owner addendum (L13, L91–92, L183–189). Its overreach is RC-1.
- Labels in §0, the body and §9 agree, except the numbering slip in RC-3.

---

## §6 New issues (RC-n)

- **RC-1 (wording / overclaim; L13, L188).**
  - Problem: "charged in the count through Σ(j(u)−E)" is inaccurate. The points with j(u)>E are not excluded as non-good. Σ(j−E) charges only the collided place(s), not the remaining d'−j(u) Ξ-zero residual places.
  - Fix: replace with "they lie on the collision locus {j(u)>E} (not excluded from the count; in a (𝒦)-pencil Lemma 4.2/𝔅 would still apply there); the toy has no full fibre at g≠0, j(u)=E".
  - Also note that N_Ξ(u)=5=d'−j(u) genuine residual places at these points (L178 "∈{0,6}" counts u itself).
- **RC-2 (evidence and label upgrade; L13, L91–92, L182–183).**
  - The 42/42 check covers one y per x. The referee checked all 294 points exhaustively, together with j(u)=E+1 and the converse (no full fibre at g≠0, j(u)=E) over all 2,095,345 points.
  - The formula Ξ=b^2(1+b^7) (b=x^7) has a three-line proof (§2(a)). Include it and label the formula and the "every full fibre degenerate" conclusion PROVED, rather than "referee's symbolic computation; COMPUTED 20/20".
- **RC-3 (label numbering; §0 L56–59).**
  - §0 item 2 numbers the clustering obstruction "(iii) (HEURISTIC)", but in the body it is Prop. 2.3(iv). The body's (iii) is the COMPUTED method bound.
  - The labels themselves agree with the body and §9, but the numbering misattributes them. Renumber §0 to (i), (ii), (iv), or add (iii) COMPUTED.
- **RC-4 (FIX-8a residue; L221, L390).** Cor. 3.2 and the §8 numerics row still say "Q∈{128,…,16384}" for the owner grid, which omits 8192. The numbers are unaffected: the maximum is 0.700669 with Q=8192 too.
- **RC-5 (scope sentence; L13).** "Correction to the audit's wording" is fair. Add that the audit's literal claim (g≠0) is true, and that the dispute is only about j(u)=E vs j(u)>E. See §2(d).
- **RC-6 (minor; Remark 4.4 L274).** The second bullet uses Lemma 4.2's hypotheses (u good, non-cuspidal). State them.

None of RC-1..6 affects any PROVED headline claim or any number.

---

## §7 Files in `checks/`

| file | content |
|---|---|
| `src_SHA256SUMS.txt` | pre-existing checksums of `src/`; verified 21/21 OK at the start and at the end |
| `owner_copy/{numerics_R20,numerics_R20_v2,toy_line_order_v2,fermat_cluster_v2}.py` + `.out` | owner scripts re-run with `python3 -I`; outputs byte-identical to `src/owner_scripts/*.out` |
| `owner_copy/{env_lib,numerics_K,fermat_cluster,toy_line_order}.py` | copied, not run |
| `rc_thresholds.py` / `.out` | independent exact-Fraction recomputation of R19 (4.1), (4.1)+N4 and (4.1′) thresholds: 216 rows, 0 mismatches, upward closed |
| `rc_misc.py` / `.out` | Cor. 3.2 ratios and supremum; D_1/E; Prop. 5.2 margin; Lemma 2.1(iii) affine invariance and counterexample; Prop. 2.2 FIX-5 inequality |
| `rc_fermat.py` / `.out` | Example 2.4 adjudication: symbolic Ξ=b^2(1+b^7) over F_2; exhaustive GF(2^21) scan (2,095,345 points); j(u) via Hasse derivatives; collisions ζ=x^{−7} |
| `checks_SHA256SUMS.txt` | SHA-256 of every file above |
