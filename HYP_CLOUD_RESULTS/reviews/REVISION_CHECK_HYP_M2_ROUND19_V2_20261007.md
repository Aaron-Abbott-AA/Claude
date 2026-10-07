# Revision check: HYP M>=2 round 19 v2 (own-line correspondence route)

7 October 2026. Claude, a fresh and independent referee. This is a revision check of v2 against the v1 audit.

**Checked file:** `src/R19_CORRESPONDENCE_ROUTE_v2.md` (SHA-256 215b9925…5c8cd).

**Against:**
- `src/inputs/R19_v1_owner.md`. Its SHA-256 is d24913db…a2fe3b, which matches the hash recorded in the audit, so this is the audited v1.
- `src/inputs/AUDIT_HYP_M2_ROUND19_20261007.md`, with FIX-1..8 and N1–N8.

**Cited inputs consulted:** `R18T_TWIST_NOTE_v2_1.md` (Lemma 2.1A, Prop. 2.2/(H_lift), Prop. 4.1, Cor. 3.5) and `PRIMARY_FNAK.md`.

**Rules followed:**
- I read only under `src/` and wrote only under `checks/` and to this file.
- I opened no file whose name contains "DZ".
- I ran no `src/` script. All computations use my own scripts, run with `python3 -I` (exact Fractions, sympy over GF(2)).
- Each run took under 2 s.

Line numbers below refer to v2.

---

## 1. Verdict

**PASS-with-fixes.**

- **The two substantive repairs are correct and complete.**
  - FIX-1: the Z(λ) charge is absorbed into the printed term.
  - FIX-2: Lemma 1.1(i) is now proved for m(w)<E and marked OPEN for m(w)>=E, and the cusp-tangent term is added to (4.1).
- **Nothing downstream breaks:**
  - Lemma 1.4 uses Lemma 1.1 only at a generic place, where m=1.
  - Lemma 1.5 and Prop. 1.1 remain valid.
  - Thm 4.1 keeps its PROVED label (conditional on the cited inputs).
- **Numbers.** All Cor. 4.2 numbers I recomputed are reproduced exactly from (4.1) as printed in v2. The FIX-2 term changes no integer τ_max and no threshold.
- **What remains:**
  - One audit fix is PARTIAL: FIX-4, where three flat "no B(u)–B(v) relation" sentences are still unlabelled.
  - There are a few minor consistency and wording items (RC-2..RC-8). One of them (RC-5) predates v2.
  - None of them changes a statement, a proof or a number.

---

## 2. Fix-by-fix table

| item | status | location in v2 | remarks |
|---|---|---|---|
| FIX-1 (Z(λ) at residual places; z-normalisation) | **ADDRESSED** | notation l.27; Prop. 3.4 l.264; Thm 4.1 note l.291, Step 1 l.297–300, Step 3 l.308, Step 4 l.313 | Re-derived in §3.1 below. Small leftovers: RC-2, RC-3, RC-7 |
| FIX-2 (Lemma 1.1(i); Lemma 1.5; (4.1) cusp term) | **ADDRESSED** | §0 l.44; Lemma 1.1 l.93–106; Lemma 1.5 l.159–167; (4.1) l.289; Step 4 l.312; §8 l.424, l.428 | Re-derived in §3.2 below. Wording: RC-8 |
| FIX-3(a) (monodromy: E=8, 16 only) | ADDRESSED | l.66, l.139, l.369, l.429 | Matches the audit's wording |
| FIX-3(b) ("inseparable", not "inseparable degree >=E") | ADDRESSED | l.367 | |
| FIX-4 (labels: Prop. 5.1(i), 5.2 cost, (R1)) | **PARTIAL** | done at l.71 (last two sentences), l.348–349, l.356, l.362, l.434–435 | Still unlabelled at l.71 (first sentence), l.268 and l.380; see RC-1 |
| FIX-5 (Cor. 4.2 statements) | ADDRESSED | l.59, l.61, l.72, l.321, l.333, l.336–337, l.383 | r=16 is 512E/Q; r=8 at n=1024 is 0.0022E; the margin 0.4096<0.42496 is cited. All confirmed (rc1) |
| FIX-6 (Def. 1.0 normalisations; Prop. 1.2 generic u) | ADDRESSED | l.88, l.121 | R18-T v2.1 Lemma 2.1A exists and states mult>=E−3 |
| FIX-7 (R18-T status; (H_bs)→(H_lift)) | ADDRESSED | l.11, l.397, l.438–440 | Consistent with the R18-T v2.1 header and §8 |
| FIX-8 (E=32 degenerate sample; "0/0" test) | ADDRESSED | l.137, l.407, l.413–416 | |
| N1 (both coordinate ratios, K⊂K²) | ADDRESSED | l.115 | |
| N2 (Prop. 1.2 generic u; αδ=βγ not analysed) | ADDRESSED | l.121 | |
| N3 (Step 2 parenthetical) | ADDRESSED | l.302 | Uses the undefined symbol β̃; see RC-4 |
| N4 (optional strengthening) | ADDRESSED (noted, not used) | l.313 | Prop. 3.3 is not sharpened. That is acceptable, since N4 is optional |
| N5 (r=8, n=1024 wording) | ADDRESSED | l.321 | |
| N6 (do not upgrade to "inseparable degree E") | ADDRESSED | l.43 unchanged; l.367 | |
| N7 (3d double count is harmless) | ADDRESSED (no change needed) | — | No text change; none required |
| N8 (script header citations) | ADDRESSED | l.415 | |

---

## 3. Detailed checks of FIX-1 and FIX-2

### 3.1 FIX-1 (PROVED; re-derived)

**Where p lives.**
- Lemma 3.1 says row i of [𝒞_P|𝒞_R] equals p_i·(T_11^ρ,T_21^ρ,T_12^ρ,T_22^ρ), i.e. p_i·w with w=(t̂_ij)^{ρ𝔮}.
- The entries of w are sections of 𝓣^{ρ𝔮} with no common zero.
- At each place some w_j≠0, so p_i=𝒞_{ij}/w_j is regular there.
- Hence p is a regular section of z^*O(a)⊗𝓣^{−ρ𝔮}. That bundle has degree a·d'−ρ𝔮τ_0=a·d'−ρ·deg[T].

**The inequality.**
- Write p=λp', where λ is the common divisor and p' is a section of 𝓟 with no common zeros.
- Then deg𝓟+deg div(λ)=a·d'−ρ·deg[T], so
  - deg𝓟+#Z(λ) <= a·d'−ρ·deg[T]. **Confirmed.**
- Z(λ) is exactly the set of common zeros of all entries of [𝒞_P|𝒞_R], because p' and w have no common zeros. **Confirmed.** A toy check over GF(2)[t] is rc2(e), 38/38.

**The absorption.**
- π has degree <=(d'−E)deg ψ+2r(d−1)deg𝓟.
- The new charge is Σ_u|Res(u)∩Z(λ)|<=d·#Z(λ). Each v lies on Res(u) only for u on the line e(v)^{[1/E]}, which gives <=d values of u.
- Since d<=2r(d−1) for d>=2,
  - 2r(d−1)deg𝓟+d·#Z(λ) <= 2r(d−1)(deg𝓟+#Z(λ)) <= 2r(d−1)(a·d'−ρ deg[T]) <= 2r(d−1)·a·d'.
- **Confirmed.** In the count, the Z(λ) charge sits next to deg π, not inside the bracket multiplied by (d'−E−τ_0+1). So (4.1) is unchanged.

**Step 3.**
- Step 3 now removes Res(u)∩W, then the <=τ_0−1 Ξ-zeros, then Res(u)∩Z(λ) (l.306–308).
- At each remaining place Ξ≠0, so Prop. 3.4 gives Π_1=0. Since λ(v)≠0, it follows that π=0.
- **Z(λ) is removed. Confirmed.**

**The identity Π_1=λ·π^X.**
- c(u)^[T]=(β,α)^[X] and p(v)=λ(v)·p'^σ(y)^[E]. With E=2rX, this gives Π_1=λ(v)(βp'^σ_1{}^{2r}+αp'^σ_2{}^{2r})^X.
- Checked symbolically, rc2(d), 20/20.
- **Consistency:**
  - Step 1 (l.300) and Step 3 (l.308) use λ·π^X, and so does Prop. 3.4 (l.264, "Π_1=0 includes the places with λ(v)=0").
  - §0 l.57 and §4 l.364 still say "Π_1 is an X-th power of a cheap section". This remains literally true, since λ(v)=λ^σ(y)^E on 𝒵' and so Π_1=(λ^σ(y)^{2r}π)^X. But it is not the same formulation as Step 1 (RC-3).

**Prop. 3.4.**
- v1's "Off det T̂=0, p is regular" is gone, replaced by "p=λp' is regular everywhere". **Confirmed.**
- The hypothesis det T̂(v)≠0 is retained. It is harmless but has no stated role any more (RC-7).

### 3.2 FIX-2 (PROVED for m(w)<E; OPEN for m(w)>=E; re-derived)

**The new proof of Lemma 1.1(i).**
- C_orig vanishes on Γ, so v(t)^[E]·z(t)≡0.
- (v(0)−v(t))^[E] is divisible by t^E (Frobenius is additive in characteristic 2).
- Hence w^[E]·z(t)=O(t^E), and so I_w(ℓ_w)>=E for every place.
- A line through z(0) other than the branch tangent meets a branch of multiplicity m with multiplicity exactly m. So m(w)<E forces ℓ_w to be the tangent. **Correct.**
- rc2(b): random branches with z=v^[E]×y, for E=4 and 8. I_w(ℓ_w)>=E in 80/80 cases, and ℓ_w is the tangent in 74/74 cases with m<E.
- The v1 counterexample (1,t²,t³) is reproduced (rc2(a)): the limit line (0,1,0) has multiplicity 2, the true tangent (0,0,1) has multiplicity 3.

**OPEN status for m(w)>=E.**
- This is justified.
- rc2(c) gives a local branch pair with v^[E]·z≡0 (v=(1,t,0), z=(t^E,1,1+t^{E+1})). There m=E, I(ℓ_w)=E, and the true tangent has multiplicity E+1.
- So the incidence argument alone cannot decide this case. Whether such branches occur on an actual Γ' is the open point.
- The bound #{w : m(w)>=E}<=⌊(2d'+2g−2)/(E−1)⌋ follows from Σ_{cusp}(m−1)<=deg(z×dz)=2d'+2g−2, because ord_w(z×dz)>=m−1. **Correct.**

**The cusp-tangent term.**
- For each w with m(w)>=E, at most one good u has ℓ_u equal to the true tangent. Good u are smooth points and u↦u^[E] is injective.
- For that u, I_w(ℓ_u)−1<=d'−j(u)−1<d'−E.
- So Σ_uκ(u)<=d·Σ(m−1)+(d'−E)·#{m>=E}<=d(2d'+2g−2)+(d'−E)⌊(2d'+2g−2)/(E−1)⌋. **Correct.**
- The term is placed outside the (d'−E−τ_0+1)-bracket, as it should be.

**Downstream uses.**
- *Lemma 1.4(A)* uses Lemma 1.1(ii) only at the generic y (m=1). Valid.
- *Lemma 1.5:*
  - Non-cuspidal branches: m=1<E. Valid.
  - Cuspidal branches with m<E: valid.
  - Cuspidal branches with m>=E: covered by the stated exception. Valid.
- *Prop. 1.1(i).*
  - j(u)>=E for all u comes from the "in all cases" clause, which is proved.
  - The Stöhr–Voloch sum survives even when ℓ_u is not the branch tangent, because j(u)<=j_2(u). Valid.
- *Prop. 1.2* uses contact >=E at u. Valid.

**Cor. 4.2 numbers are unchanged (rc1).** These are computed from (4.1) as printed in v2. The normalisation is that of l.318, with 2g−2=d(d−3), integer τ_0<=d'−E, and the full scan d'∈[2E−2,2E+4].
- *τ_max/E, r=4:* 0.71027, 0.56482, 0.49422, 0.45942, 0.44215, 0.43355 for n=256..8192. Printed: 0.71, 0.565, 0.494, 0.459, 0.442, 0.434.
- *τ_max/E, r=8:* 0.47728, 0.15746 and 0.00220, with none from n=2048. Printed: 0.477, 0.157, 0.0022E, 0.
- *τ_max/E, r=16, n=256:* 0.01127. Printed: 0.011.
- *Effect of FIX-2:* the integer τ_max is identical with and without the FIX-2 term in every row. The arg-min is always d'=2E−2.
- *r=4 thresholds:* Q∈{128,…,4096,16384}, S∈{64,256}, every dyadic n∈[256,2Q]: 50 rows.
  - The conservative test and the per-d' test agree.
  - The table cells E/16, E/32, E/128 (n=256), E/4, E/16 (n=512) and E/8, E/32 (n=1024) are reproduced.
  - 𝔮=E/4 suffices in every row.
  - nE/(8Q) holds for every n>=512.
- *r=4 asymptotics* at n=2Q, 𝔮=E/4: at Q=2^19, height/E=0.40954 against τ_max/E=0.42503 (margin 0.0155E). This matches the cited limit 0.4096<0.42496.
- *r=16, n=256:*
  - Q=128 and Q=256: none.
  - Q=512: E. Q=1024: E/2. Q=2048: E/4. Q=4096: E/8. Q=8192: E/16. Q=16384: E/32.
  - All equal 512E/Q, as printed.
  - n=512 never closes.
- *r=8:* E/8, E/16, E/64 (n=256) and E/2, E/8 (n=512), as printed. At n=1024 there is none.

---

## 4. Diff v1→v2 and label audit

- `checks/diff_v1_v2.txt` has 216 lines, all reviewed.
- Every hunk corresponds to a marked FIX/N item or to the version-history and status bookkeeping, with two exceptions:
  - The Thm 2.1 *Remark* (l.191) gains an **unmarked** sentence taken from audit §3.2. Its content is correct (RC-6).
  - The inputs line (l.11) adds "Lemma 2.1A" to the R18-T items used. This is consistent with FIX-6.
- **No statement, proof or number outside the fixes was altered.** (4.1) differs from v1 only by the FIX-2 line.

**No new overclaim.**
- The title adds only "(v2)".
- The PROVED label now reads "v1 independently audited, v2 revision check pending". That is accurate.
- §8:
  - Lemma 1.1 is split into PROVED/OPEN.
  - Lemma 1.5 is PROVED with the exception.
  - Monodromy is COMPUTED for E=8 and 16 only.
  - Prop. 5.1(i) and the 5.2 cost statement are HEURISTIC.
  - Thm 4.1 is "PROVED with the v2 repairs" and "independently reproduced". The last phrase is accurate for the audit's c1 and for this check.
- One mild new assertion appears: "Bs(e)∩Γ̃ … is nonempty" (l.27). It is stated as general fact without support (RC-2).

**Consistency of cross-references.**
- Lemma 2.1A, Prop. 2.2 and (H_lift) exist in R18-T v2.1 with the stated status.
- "audit c0", "c1", "c2(e)" and "§3.2" exist in the audit.
- Lemma 1.5's count is cited correctly from Lemma 1.1.
- Prop. 3.4 forward-references Thm 4.1 Step 1 correctly.
- Summary, body and §8 labels agree, except for the FIX-4 residue (RC-1) and the table legend (RC-5).

---

## 5. New issues (RC-n)

**RC-1 (FIX-4 residue; label).** The flat claim "no B(u)–B(v) relation outside (𝒦)" is still unlabelled in three places:
- §0 (R1), first sentence (l.71);
- §3 "Answer to question (a)" (l.268: "Outside (𝒦): no such relation exists (§5)");
- §6 (R1) (l.380: "The residual route gives nothing (§5)").

The title of Prop. 5.1 still reads "(no B(u)/B(v) relation; …)", and (i) keeps a "Proof … ∎" line.
- *Correction:* append "(HEURISTIC, Prop. 5.1(i))" at l.71, l.268 and l.380.
- In Prop. 5.1, either retitle it or mark the proof of (i) as a "Reason (HEURISTIC)".

**RC-2 (l.27; overstatement).** "Bs(e)∩Γ̃, which is nonempty" is not established in general. The audit shows it only in a random toy (c0).
- *Correction:* "which can be nonempty (e.g. audit c0; always if Γ=C_orig, since C_orig⊃Bs(e))". FIX-1 does not depend on nonemptiness.

**RC-3 (l.57, l.364 vs l.300; formulation).** §0 and the "Why (𝒦) escapes" remark say that Π_1 is an X-th power of a cheap section, while Step 1 has Π_1=λ(v)·π^X.
- *Correction:* add "(Π_1=λ(v)π^X; since λ(v)=λ^σ(y)^E on 𝒵', this is (λ^σ(y)^{2r}π)^X)".
- *Optional:* counting zeros of π̃:=λ^σ(y)^{2r}π instead of π gives the same bound, by the inequality in §3.1. It needs no removal of Z(λ), and it is an equivalent alternative to the v2 repair.

**RC-4 (l.302; notation).** "β̃(u)" is undefined; Step 1 uses β(u). *Correction:* replace β̃ with β.

**RC-5 (Cor. 4.2 table, l.325–335; pre-existing in v1, not a v2 regression).** The legend says "— means n>=4Q", but some "—" cells are inside the strip:
- r=4, n=256, Q=4096: the computed threshold is E/512;
- r=4, n=512, Q=4096: the computed threshold is E/64.

The r=8 rows have three entries for four Q-columns. At Q=4096 the computed thresholds are E/256 (n=256) and E/32 (n=512), consistent with nE/(16Q) and nE/(4Q).
- *Correction:* fill these cells, or say "not tabulated", in place of "—".

**RC-6 (bookkeeping).**
- The Thm 2.1 Remark addition (l.191) lacks a "[v2: …]" marker. *Correction:* add "[v2: audit §3.2]".
- The label list (l.16–19) does not define CONDITIONAL, which l.397 uses. *Correction:* add it.

**RC-7 (Prop. 3.4, l.259; optional).**
- After FIX-1, the hypothesis det T̂(v)≠0 has no stated role, because p and B are regular everywhere.
- *Correction:* drop it, or note "kept for convenience; W is removed in Step 3 anyway". Either way, no number changes.

**RC-8 (Lemma 1.5, l.161/166; wording).**
- "At most one u per such w (Frobenius is injective)" is true for u as points of Γ, and in particular for good u, which are smooth.
- It is not true for places of Γ̃: several places over a singular point share the same ℓ_u.
- *Correction:* say "at most one good u (u↦u^[E] is injective on points)".

---

## 6. Files in `checks/`

- `src_SHA256SUMS.txt`: hashes of the five `src/` files. The v1 hash matches the audit's record.
- `diff_v1_v2.txt`: `diff` of v1 against v2.
- `rc1_numerics.py` → `rc1_numerics.out`: an independent exact-Fraction evaluation of (4.1) as printed in v2, with the Cor. 4.2 normalisation. It covers:
  - τ_max for r=4, 8, 16, with and without the FIX-2 term, over the full d' scan;
  - r=4 thresholds (conservative and per-d') for Q up to 16384 and S∈{64,256};
  - r=16 at n=256 and 512 for Q=128..16384;
  - r=8 rows;
  - r=4 asymptotics up to Q=2^19.
- `rc2_algebra.py` → `rc2_algebra.out`: characteristic-2 local checks.
  - (a) the v1 continuity counterexample;
  - (b) I_w(ℓ_w)>=E, and ℓ_w is the tangent when m<E;
  - (c) a local toy with m=E where ℓ_w is not the tangent, supporting the OPEN label;
  - (d) the identity Π_1=λπ^X;
  - (e) p regular, with Z(λ) equal to the common zeros of [𝒞_P|𝒞_R].
- `checks_SHA256SUMS.txt`: hashes of the files above.
