# Revision check: HYP M>=2 round 18-T, owner note v2

7 October 2026. This is an independent revision check of `src/R18T_TWIST_NOTE_v2.md` against `src/inputs/R18T_TWIST_NOTE_v1.md` and the audit `src/inputs/AUDIT_HYP_M2_ROUND18T_20261007.md`.

**Rules followed.**
- I read only files under `src/`.
- I wrote only under `checks/` and to this file.
- I opened no file whose name contains "DZ".
- I ran no script from `src/`. All computation is in my own scripts in `checks/`, run with `python3 -I`.

---

## 1. Verdict

**PASS-with-fixes.**

**FIX-1 is implemented correctly in substance.**
- (H_bs) is no longer used anywhere as if it held. It now appears only in four places:
  - the version history;
  - the "superseded v1 hypothesis" record and Steps 1 and 4 of the proof of Prop. 2.2, which are explicitly kept as a record;
  - the Prop. 2.4 "In particular" paragraph and §5.1, as "(H_bs) never holds";
  - the §8 table.
- Every former PROVED consequence has been relabelled correctly:
  - Prop. 2.2 and Cor. 2.3 → CONDITIONAL on (H_lift);
  - the "In particular" example → CONDITIONAL on (H_lift);
  - Remark 2.5 → split into PROVED / CONDITIONAL / HEURISTIC / OPEN parts;
  - Summary items 2–3, §5 items 1–2 and §8 → relabelled to match.
- (H_lift) is stated as OPEN, and it appears in the §6 residual list and in the §8 OPEN row.
- The title no longer claims "why identities alone cannot force constancy".

**Lemma 2.1A is true. Its written proof has three small gaps** (RC-1), each closable in one line:
- why C_f vanishes on Γ';
- why C_f≢0;
- why F occurs in C_f with multiplicity 1, which is needed for the bound E−3. Membership q∈Γ' does not need it.

**The (N10) remark is correct.** It needs one wording precision about "same alignment" (RC-2).

**§§3–4 are unchanged** except for the three intended edits (FIX-3, FIX-5, N4). Every number reproduces exactly.

**No new mathematical overclaim was found.** The remaining issues are bookkeeping: N2 is not applied although the header claims N1–N10 (RC-3), plus RC-4 to RC-7.

---

## 2. Fix-by-fix table

| item | status | location in v2 | comment |
|---|---|---|---|
| FIX-1 (H_bs) never holds; (H_lift) | **ADDRESSED** (proof gaps: RC-1) | Lemma 2.1A (l.137–146); Hypothesis (H_lift) (l.148–150); Prop. 2.2 (l.152–178); Cor. 2.3 (l.180–188); Prop. 2.4 "In particular" (l.199–201, 209); Remark 2.5 (l.213–223); §0 items 2–3 (l.43–49) and "What failed" (l.76–77); §5.1–5.2 (l.364–369); §6 (l.387); §8 (l.423–427, 434) | All relabellings follow the audit's proposed text. "Without (H_bs)" has moved forward as "The general case (this is the actual case)". (H_lift)⇒P(q)=R(q)=0 is stated. Steps 5–6 use only (H_lift) (l.178). Minor wording: RC-5. |
| FIX-2 (Γ-local structure is not invariant) | **ADDRESSED** | Remark 2.5 l.213–215; §5.1 l.365 | "and by R16–R18's Γ-local structure" is deleted. The non-invariance of R16.2, Lemma 1.2, FN and FNAN/FNAO is now stated explicitly. FNAN/FNAO/FNAP have been removed from the list of invariant identities. |
| FIX-3 (λ' regular off {g=0} and Bs(e); FIX-N1) | **ADDRESSED** | Lemma 1.1 statement l.96 and proof l.100; Thm 3.4 proof l.309 | Lemma 1.2 and Lemma 3.1 already exclude 𝔈⊇{g=0} and the boundary⊇Bs(e). No number changes. |
| FIX-4 (citations and status) | **ADDRESSED** | Header l.13–17; §1 l.90; §8 l.437–441 | R17 v2.1 and R18 v2.1 are now cited. PRIMARY statuses are taken from the Claude review, consistent with R18 v2.1's header. The "DZ-reviewed per FNAO" phrase and the "pending: R18 v1" line are removed. New in v2: "developed in R19, owner draft" (§8 l.435); see RC-7. |
| FIX-5 (D-windows) | **ADDRESSED** (§7 inconsistency: RC-4) | §0 item 5 l.60; Cor. 3.5 l.319 | D<=n/16 for n=256…8192. "Nonempty low-height closing window (θ_max>0)" and "only deg[T]<=θ_max·rh closed" are both stated. I recomputed this independently (rc2): it holds on 1764 grid cases. |
| FIX-6 (half-section vs counted section) | **ADDRESSED** | §0 "What failed" l.71–74; §5.5 l.375 | Both X·deg[T] (for 𝔊_k) and ≈T·deg[T]=2X·deg[T] (for 𝔊_k²) are stated. This is consistent with (3.0), since Q(Q−1+T−D)/(Q−1)≈T. |
| FIX-7 (§5.3 restricted) | **ADDRESSED** | §5.3 l.371–373 | The claim is now PROVED only for 𝔊_k with k<min(ρ𝔮,E) (Prop. 4.1(iii)); the general claim is labelled HEURISTIC. |
| N1 notation | **ADDRESSED** (warning only, no renaming) | l.19–22 | Acceptable, since the audit only recommended renaming. Two further clashes are unlisted: S (the ring k[Y] vs Q^jD) and g (the cubic g(u) vs the form g in Cor. 2.3/Prop. 2.4 vs g(w) in Lemma 3.2). See RC-6. |
| N2 (Lemma 1.2: c_1=0; s=s_M(u)) | **NOT ADDRESSED** | Lemma 1.2 is unchanged from v1 (l.103–111) | The header (l.8) says N1–N10 are applied "where they affect content". See RC-3. |
| N3 (Step 3 does not need (H_bs)) | **ADDRESSED** | l.172 | The argument is the audit's: F is prime and F∤f_i^X for some i. |
| N4 (edge case a=E−1, d'=2E−2) | **ADDRESSED** | §4 Remarks l.351 | Correct, because D divides both E and ρ𝔮, so a+1<=min(ρ𝔮,E) ⟺ D⌈(a+1)/D⌉<=min(ρ𝔮,E). Prop. 3.3(b) needs D>=4, which is not repeated in the remark (RC-6, optional). |
| N5 (m·d'<Nd; §5 vs §8.1) | **ADDRESSED** | Cor. 2.3 l.182; §0 item 3 l.48–49 | m·d'<=(M−1−4X−2ρ)d<(M−1−X)d=Nd uses d'<=2d. "R18 §5 bound (used in R18 §8.1)" is harmonised, and R18 v2.1 l.277 confirms e_M<=Nd/ρ. |
| N6 (𝔮 range) | **ADDRESSED** | Cor. 2.3 l.184 | 0.0512E at h=256E and 64E/625 as h→4QE. Both recomputed (rc2). |
| N7 ("off the exceptional set") | **ADDRESSED** | §0 item 4 l.52 | |
| N8 ("the method needs D>=4") | **ADDRESSED** | §5.4 l.374 | The wording is slightly awkward but correct. |
| N9 (script cosmetics) | **NOT VERIFIABLE** | — | The scripts are not in `src/`. v2 says nothing about N9; see RC-3. |
| N10 (ker J^[X,t]=S·f^[X]) | **ADDRESSED** (wording: RC-2) | Remark after Prop. 2.4, l.211 | See §3.2. |

---

## 3. Detailed findings on FIX-1

### 3.1 Lemma 2.1A

The statement is: q a proper base point of f ⇒ q∈Γ', and mult_qΓ'>=E−3.

**Is C_f really a form that vanishes on Γ'?** Yes, but v2 asserts this without a reason. The reason is as follows.
- On Γ the own-line incidence u^[E]·e(u)=0 holds; it is used in Lemma 3.1. So C_orig(U):=U^[E]·e(U) vanishes on Γ.
- FNAM gives f(e(U))=g(U)U, hence C_f(e(U))=e(U)·(gU)^[E]=g^E·C_orig(U).
- So C_f vanishes on e(Γ), which is dense in Γ'.
- *COMPUTED (rc1 A):* the identity C_f∘e=g^E·C_orig holds exactly for 9 random quadratic Cremona centres over GF(2), with E=4,8,16.

**Is C_f≢0?** Yes, but v2 does not say why.
- E is a power of 2 and the characteristic is 2. So every monomial of Z_i·f_i^E has exponent vector ≡e_i (mod E), and the three summands have disjoint supports.
- Hence C_f=0 iff f=0.
- Degree 2E+1 was confirmed (rc1 A).

**Does F occur in C_f with multiplicity 1?** Yes, but v2 does not say so.
- F is prime and vanishes where C_f does, so F|C_f.
- If F²|C_f, then 2d'<=2E+1. That contradicts d'>=2E−2 for E>=3.
- So C_f=F·R with deg R=2E+1−d'<=3.

**Do multiplicities add up correctly?** Yes.
- mult_q(C_f)=mult_qF+mult_qR.
- mult_qR<=deg R<=3, for any nonzero form R, and this counts all components of R with their multiplicities.
- mult_qC_f>=E, since each f_i vanishes at q.
- Hence mult_qF>=E−3>0.
- *COMPUTED (rc1 A, B):*
  - mult_qC_f∈{E,E+1} at all 27 base points tested.
  - On the σ model, C_f=Z_0Z_1Z_2·F with deg F=2E−2. There mult_{(1:0:0)}F=E−1 and the cofactor has multiplicity 2.

**Conclusion.** The lemma is PROVED once the three one-line justifications are added (RC-1). The label is acceptable now, because the gaps are routine.

### 3.2 The (N10) remark

The claim is that ker J^[X,t]=S·f^[X].
- J^[X,t] is the 2×3 matrix with rows j_1^[X], j_2^[X]. Its 2×2 minors are the coordinates of j_1^[X]×j_2^[X]=κ_0^{−X}f^[X].
- The ideal (f_i^X) has the same radical as (f_0,f_1,f_2). That ideal has height 2, because f is a Cremona map without common factor. S is CM, so the grade is 2.
- By Buchsbaum–Eisenbud (or Hilbert–Burch), 0→S→S³→S² is exact with the first map given by the minors. So the claim is correct.
- *COMPUTED (rc1 C):* the kernel dimension in each degree δ equals dim S_{δ−2X}, for X=2,4, three random J each, δ<=2X+2. There are 0 mismatches.

**Wording issue (RC-2).** P'^t=P^t+f^[X]⊗η is automatically globally aligned, with a'=a_P+η·f^[ρ]. "Same alignment" therefore gives η·f^[ρ]=0 only when it means **the same coefficients a_P, a_R**, as in Prop. 2.4(i). Zero top alone gives only η·f^[ρ]≡0 (mod F). So the phrase "the syzygy condition on η is exactly the zero-top/alignment requirement" should say "same alignment coefficients a_P, a_R".

### 3.3 Prop. 2.2 / Cor. 2.3 / Prop. 2.4 / Remark 2.5 under (H_lift)

- Steps 5–6 use only (H_lift); this checks.
- The degree count for η in the "In particular" example closes: (m−ρ𝔮)+ρ𝔮+ρ=M'−2X.
- (H_lift)⇒P(q)=R(q)=0 checks: F(q)=0 and f(q)=0.
- The HEURISTIC bullet in Remark 2.5 includes the audit's logical caveat ("would have to prove those identities inconsistent for such data").

Two minor wording points:
- "the two obstructions to a lift" (l.157) should read "the two obstructions to the construction of Steps 1–4". A non-vanishing (a) or (b) does not by itself refute (H_lift). See RC-5.
- Steps 1 and 4 still read "Under (H_bs)…" inside the proof of a proposition that now assumes (H_lift). This is acceptable because l.162 labels them as a record.

---

## 4. Diff of §§3–4 and the numbers

`checks/diff_v1_v2.txt` is the full diff. Restricted to §§3–4, only three hunks differ:
1. the FIX-3 bullet added to the proof of Thm 3.4;
2. the FIX-5 bullet in Cor. 3.5;
3. the N4 remark after Prop. 4.2.

The statements, proofs and formulas (3.0), (3.1), (3.2) are otherwise byte-identical.

**Numbers (rc2, exact Fractions).**
- Corner rest=1490227160815097/10995116277760000, identical to the note.
- θ_max=0.249775.
- D=4 minima per n: 0.2498, 0.2772, 0.2911, 0.2980, 0.3015, 0.3032.
- D-windows are exactly D<=n/16 for n=256…8192.
- min θ_up/θ_max=11.83.
- θ_up(S=64)≈3.28.

All agree with v2.

**Title, header, summary and table.**
- The title is now "…and the decoupling of the two layers", which is not an overclaim.
- The summary, body and §8 labels agree.
- §6 lists (H_lift).

---

## 5. New issues (RC-n)

**RC-1 (Lemma 2.1A proof, l.139–142): complete the proof.** Add three lines:
1. "C_f vanishes on Γ': on Γ, u^[E]·e(u)=0 (own line), and f(e(U))=g(U)U (FNAM), so C_f∘e=g^E·U^[E]·e(U)."
2. "C_f≢0: in characteristic 2 with E a power of 2, the monomials of Z_i f_i^E have exponent ≡e_i mod E, so the three summands cannot cancel."
3. "F|C_f exactly once, since F²|C_f would force 2d'<=2E+1<2(2E−2). So C_f=F·R with deg R<=3, and mult_qR<=deg R."

Also replace "Proof (from the audit)" with a proof that stands on its own.

**RC-2 (Remark after Prop. 2.4, l.211).**
- Replace "the same alignment" with "the same alignment coefficients a_P, a_R".
- Add: "(zero top alone gives only η·f^[ρ]≡0 mod F)".
- Optionally cite Buchsbaum–Eisenbud/Hilbert–Burch for ker J^[X,t]=S·f^[X].

**RC-3 (header l.8, version history).** The claim "applies … N1–N10 where they affect content" is inaccurate. Either:
- apply N2 (Lemma 1.2: the c_1=0 / s=∞ case via the homogenised 𝔉, and the one-line identification s=s_M(u) via injectivity of W at u); or
- state "N2 deferred; N9 concerns the scripts (fixed / not fixed)".

**RC-4 (§7 table, numerics row, l.406).** "D-windows as in Cor. 3.5" now overstates what the owner script shows. Its grid (Q<=1024, S<=4096) reproduces the windows only up to D=64 (n<4096). Change it to: "D-windows up to D=64; the full D<=n/16 statement is from audit r1 (and this revision check, rc2)". Alternatively, extend the owner grid.

**RC-5 (Prop. 2.2 "The general case", l.157–161).**
- Replace "the two obstructions to a lift are" with "the two obstructions to the construction of Steps 1–4 are".
- Add: "their non-vanishing would not by itself refute (H_lift)".

**RC-6 (minor, optional).**
- N1 warning: add the S clash (ring vs Q^jD) and the g clash (cubic g(u) vs the auxiliary forms g).
- N4 remark (l.351): add "(D>=4)", since Prop. 3.3(b) needs it.
- Header l.10, "No change to §§3–4": also mention the N4 change in §4.

**RC-7 (minor, §8 l.435).** "(developed in R19, owner draft)" refers to a document that is not among the inputs and has not been audited. Either cite its filename, or drop the parenthesis. It does not change any label.

---

## 6. Files in checks/

- `checks/diff_v1_v2.txt`: full `diff` of v1 against v2.
- `checks/rc1_algebra.py` → `checks/rc1_algebra.out`: exact GF(2) computations.
  - (A) f∘e=gU; C_f≢0 of degree 2E+1; C_f∘e=g^E·C_orig; f vanishes at the base points; mult_qC_f>=E (E=4,8,16, 9 random centres).
  - (B) the σ model: C_f=Z_0Z_1Z_2·F, mult F=E−1.
  - (C) ker J^[X,t]=S·f^[X] degree-wise (X=2,4).
  - All PASS.
- `checks/rc2_numerics.py` → `checks/rc2_numerics.out`: exact recomputation of the Cor. 3.5 corner, the D=4 minima, the D-windows (1764 cases), θ_up/θ_max, and the N6 constants. All agree.
- `checks/checks_SHA256SUMS.txt`: hashes of the files above.
