# AUDIT — KP-RX-ROOTSPACE-GALOIS-NOTE-20261007.md (owner note v1)

Independent referee audit by a fresh, isolated referee agent (DZ lane).
- **Timing.** Started 7 Oct 2026, 23:36Z. Interrupted by a usage-limit pause and a container restart. Resumed and finished 12 Oct 2026, 00:03Z (`date -u` checked). The file name keeps the note's date.
- **Note audited:** `KP-RX-ROOTSPACE-GALOIS-NOTE-20261007.md`, sha256 `87430b2398f7858c53fcc92ad5d87b395eeefd382af2c90d0354985a89256ffd`.
  - The working copy (`referee_KP/src/`) and the `claude_archive/` copy are byte-identical.
  - The hash matches HANDBACK-20261007T2330Z.
- **Owner scripts.** All four files match note §9 and the `claude_archive/scripts/` copies:
  - `kpcheck.py` bb1eb2a4…9a60;
  - `kpcheck.log` cb00f4b0…8d96;
  - `kprat.py` bde29362…4e5b;
  - `kprat.log` cc1344df…27ee9.
- **Labels** are as in the handoff: [P] proof; [C] computation; [H] heuristic; [A] reading of a reviewed source; [COND]; [OPEN].
- **Isolation.**
  - No incoming scripts were executed. Owner scripts were re-run only from `checks/owner_copy/`, with `python3 -I`.
  - No git was used. No HYP/3PP directories, uploads or other scratchpads were read.
  - No process was killed.
  - The only file written in `DZ_CLOUD_RESULTS` is the copy of this audit.

## Verdict: **PASS-with-fixes**

**The mathematics of the note is correct.**
- Lemmas FR and GS are correct as [P]. FR has one small presentational gap (m1).
- Theorem KP (i)–(iii) is correct as [P + C], for the stated m.
- Proposition KL is correct as [P + C].

**The computations are VERIFIED** by independent referee code (§5). This code uses its own moduli, its own cofactor/M_W/quotient routines, a Frobenius matrix built by iterating τ, Hessenberg characteristic polynomials, and two factorisation libraries.
- All **356** owner Frobenius samples were recomputed sample by sample. The factor-degree lists agree on 356/356.
- Fresh referee samples (different seeds and moduli) reproduce every intersection of subset-sum sets in the §5 table.
- Lemma FR was checked against **actual roots**: the F₂-kernel of P̃_α in GF(2^{2mL}) and the matrix of Frobenius on it. Of 78 samples, all 78 nullities agreed, and the characteristic polynomials matched in all 39 samples that split.
- KL was re-derived:
  - the Newton polygons allow no finite pole;
  - the degree at ∞ is exactly 12;
  - the F₂-dimension of roots in F_q[X]_{≤16} is 0 for m = 10, 14, 18;
  - the control on P gives 3.
- The owner logs reproduce byte-identically (kprat), or block-identically for the m re-run (kpcheck).

**FIX count: 2 substantive, 6 minor (m1–m6).**
- **FIX-1 (evidence for KP(i) misreported).** The owner's runs contain **no** irreducible characteristic polynomial: 0 of the 36 samples logged for m ≡ 0 (mod 4).
  - The script's message "irreducible Frobenius found … stopping early" fires when the **intersection** of subset-sum sets equals {0, n}, not when one polynomial is irreducible. For m = 24, the two logged samples have factor degrees [5,5] and [2,4,4].
  - The conclusion "G acts irreducibly on R_P/W" is still correct, because the intersection {0, n} already implies it.
  - The literal statement "some degree-2 Frobenius has an irreducible characteristic polynomial" is also **true** for all six m, but only by referee samples (§5, table F3).
- **FIX-2 (§6(a) overclaim, repeated in HANDBACK-2330Z §2 item 4).** "Any band-dimensional non-implication must therefore come from a different (C, D) **and a non-rational W**." The "non-rational W" part does not follow. RK and KP concern only RX's P. A rational (G-fixed) band-dimensional W with a **different** (C, D) is excluded by nothing cited; RX v2 §3 excludes only monomial W. The scope (a = 1, m = 24..44) also needs to be stated.

**Owner revision is needed**, to wording and records only; no proof changes. A referee **diff check suffices**.

## 1. Item table

| # | Item | Label | Finding | Result |
|---|---|---|---|---|
| 1 | Header, audit status (HOLD, not in outbox), scope, "what is not claimed" | — | Accurate. | PASS |
| 2 | Title / abstract | — | The math is correct, but "For m ≡ 0 (mod 4), G acts irreducibly", "For m ≡ 2 (mod 4), only hyperplanes …" and "lines are excluded **exactly** for m = 10, 14, 18" read as general statements. The evidence covers m = 24..44 (and 10, 14, 18 for lines). | m4 |
| 3 | §0 setting: P = P̃·M_W, n = h−2, R_P/W ≅ ker P̃ via M_W (cites SH audit §2.4) | [P, referee]/[A] | Correct. P̃ ∈ F₂[X]{τ}, because right division by a monic element keeps coefficients in F₂[X]. Leading coefficient d₁; constant c₀/(M_W)₀. Exact division re-verified [C, F1/F6]. | PASS |
| 4 | §0 question, band range 6 ≤ dim ≤ (m−6)/3 | [A] | Matches SH v2 §3/§5(c) and the SH diff check: ker P̃ dims 3..(m−15)/3, which needs m ≥ 24. | PASS |
| 5 | Lemma FR statement and proof | [P] | Correct. Steps 1 and 3 are right. Step 2 identifies M̄ = k̄{τ}/k̄{τ}P̃ with Hom(V, k̄); "τ^N ⊗ 1" must be read on k̄ ⊗_k M (not as left multiplication by τ^N on M̄, which is only 2^N-semilinear over k̄). Validated against actual roots [C, F4]. | PASS; m1 |
| 6 | FR matrix form, ordering Aσ(A)…σ^{N−1}(A) | [P] | Correct. Re-derived: τ(v) = Aσ(v), with A[i][i−1] = 1 and A[i][n−1] = p̃_i/p̃_n (char 2). The doubling F_{a+b} = F_aσ^a(F_b) in `frob_charpoly` is correct. The referee instead iterates τ N times; results identical. | PASS |
| 7 | Lemma GS (good reduction, Frobenius, subset sums; irreducible ⇒ irreducible G-action) | [P]/[A] | Correct. d₁^{−1}P̃ is monic over O_𝔭. The constant c₀/(M_W)₀ is a unit iff c₀(α) ≠ 0 and dim W(α) = 3 (automatic for α ∉ F₄). The separable reduction gives an unramified place and an F₂-linear, Frobenius-equivariant bijection on roots. G here is the **arithmetic** group Gal(L^sep/L), as in SH. | PASS; m2 |
| 8 | §2 Remark (degree-1 places uninformative) | [A]/[P via PTH] | True for α ∉ Z = F_Q. Referee: dim(ker P̃_α ∩ F_q) ≥ n−1 at 210/210 α ∈ F_q∖F_Q, m = 10..26 [C, F5]. Needs the qualifier α ∉ F_Q. | m6 |
| 9 | KP(i) "Some degree-2 Frobenius has an **irreducible** characteristic polynomial" (m = 24..44, m ≡ 0 mod 4) | [P + C] | **The owner's evidence does not show this.** None of the 36 logged samples is irreducible (F2). The script stops on intersection = {0, n}. The statement is true by referee samples (F3). The conclusion (G irreducible on R_P/W) follows from either. | **FIX-1** |
| 10 | KP(i) consequence: S ⊂ W, or S + W = R_P with dim S ≥ m/2 − 2 | [P] | Correct. dim R_P = m/2 + 1 (separable), dim W = 3. | PASS |
| 11 | KP(ii) intersection {0, 1, n−1, n} over 40 samples (m = 26..42, m ≡ 2 mod 4) | [P + C] | Correct. Owner samples recomputed 40/40 for each m. Fresh referee samples (40 per m, other seeds and moduli) give the same intersections [C, F1]. Deduction: dim S ≤ 4 or dim S ≥ n−1. | PASS |
| 12 | KP(iii) arithmetic and band conclusion | [P] | Correct. Excluded: 5..m/2−4. (m−6)/3 ≤ m/2−4 ⟺ m ≥ 12. m/2−3 > (m−6)/3 ⟺ m > 6. "Whether or not containing W" is right: the statement is about all G-stable S. | PASS |
| 13 | Prop KL: lines ⟺ L-rational roots | [P] | Correct. GL₁(F₂) = 1, and (L^sep)^G = L. | PASS |
| 14 | KL: Newton polygons, no finite poles, degree ≤ 12, exact kernel = 0, control = 3 | [P + C] | VERIFIED independently [C, F6]. The finite-place slopes are fractional (max 1/2, 1/8, 1/32 for m = 10, 14, 18), so no integer pole order exists. At ∞ there is one segment of slope 12 (degree exactly 12). Kernel on F_q[X]_{≤16} = 0; control on P = 3. The owner log's "possible poles … 0" lists places with fractional positive slope, which is confusing to read. | PASS; m5 |
| 15 | KL consequence: only hyperplanes are possible; no 4-dimensional W″ ⊃ W | [P + C] | Correct. | PASS |
| 16 | KL [C/OPEN] (lines for m ≥ 26, m/2 odd; hyperplane mechanism) | [OPEN]/[H] | Properly labelled. (Referee, for information: m = 22 gives intersection {0, 1, 8, 9} [C, F1]; it is outside the band and not claimed.) | PASS |
| 17 | §5 computations: sanity checks, 356 samples, "no warnings" | [C] | Confirmed. Referee check (d) is stronger: cp(P) = (T+1)³·cp(P̃) holds **exactly** in every referee sample. The sentence "a run stops early once an irreducible characteristic polynomial appears" and the column "irreducible found: yes" are false descriptions of the runs. | **FIX-1** |
| 18 | §5 table values (n, samples, intersections) | [C] | All correct (F1, F2). | PASS |
| 19 | §6(a) "RX construction exhausted … must therefore come from a different (C, D) **and a non-rational W**" | [P + C] | "Different (C, D)" is correct for a = 1 and m = 24..44: any W with RX's relation lies in R_P. **"Non-rational W" does not follow.** RK and KP say nothing about rational W with another relation, and RX v2 §3 covers only monomial W. a ≥ 2 is untouched. | **FIX-2** |
| 20 | §6(b) [H] pattern "irreducible for m ≡ 0 mod 4" | [H] | It should read "intersection {0, n} (G irreducible on R_P/W)". Individual Frobenius polynomials are mostly reducible. Referee [C]: the pattern also holds at m = 12, 16, 20. | FIX-1 (wording) |
| 21 | §6(c) unchanged status | — | Correct. | PASS |
| 22 | §6(d) method: "… excludes G-stable sub-radicals …, and with them SH-type twisted half-fields of those dimensions" | [P] | The first half is correct. The second half is imprecise: a twisted half-field A(U) is G-stable only in special cases. What is G-stable is A(F_Q) (dim m/2) and W ∩ A(F_Q) = A(U′) of SH(b), for a minimal twist A (g(A) = Aχ(g)). Irreducibility of R_P/W does **not** exclude a G-stable A(F_Q) (dim m/2 ≥ n). | m3 |
| 23 | §7 question to Codex | — | Fine. | PASS |
| 24 | §8 self-check | — | Accurate, except where FIX-1 applies. | PASS |
| 25 | §9 script hashes | [C] | Verified. | PASS |

## 2. Detailed audit

### 2.1 Lemma FR
- Let k = F_{2^N}, M = k{τ}/k{τ}P̃, V = ker P̃ (|V| = 2^n by separability).
- **Linearity of τ^N.** τ^N is k-linear on M, since τ^N c = c^{2^N}τ^N = cτ^N.
- **The isomorphism Φ.** Define Φ: k̄ ⊗_k M → Hom_{F₂}(V, k̄) by λ ⊗ f ↦ (v ↦ λ f(v)).
  - It is k̄-linear.
  - It is well defined, since k{τ}P̃ vanishes on V.
  - It is injective, since an element is a linearised polynomial Σ λ_j τ^j of τ-degree < n, which has < 2^n roots.
  - Both sides have dimension n.
- **Frobenius.** Φ((1 ⊗ τ^N)(λ ⊗ f)) = λ f(·)^{2^N} = λ f(Fr ·), because f has coefficients in k. So τ^N ⊗ 1 = Fr^∗, the transpose of Fr ⊗ 1 on V ⊗ k̄. Hence the characteristic polynomials agree, and they lie in F₂[T].
- **m1 (wording).** The note's M̄ = k̄{τ}/k̄{τ}P̃ is the same space as k̄ ⊗_k M, via λ ⊗ f ↦ λf. But on M̄, left multiplication by τ^N is not k̄-linear. Say "τ^N ⊗ 1 on k̄ ⊗_k M".
- **[C, F4] FR against actual roots** (`kp_ref_roots.py`). In B = GF(2^{2mL}) (sparse modulus, re-verified by Rabin's test), α = Tr_{B/F_{2^N}}(x). Compare:
  - nullity(τ^{NL} − 1) on M;
  - dim_{F₂} ker(P̃_α|_B), from an NL×NL F₂ system.
  - For (m, L) = (10,7), (10,12), (14,12), (14,15), (18,12), (24,10): 78/78 equal.
  - In the 39 samples where P̃_α splits in B, the F₂ characteristic polynomial of x ↦ x^{2^N} on the actual kernel equals the σ-module polynomial (39/39).

### 2.2 Lemma GS
- **Good reduction.** d₁^{−1}P̃ ∈ O_𝔭{τ} is monic. Its constant term c₀/((M_W)₀ d₁) is a unit at 𝔭 iff c₀(α) ≠ 0 (and d₁(α) ≠ 0). This holds because (M_W)₀ = Π_{w∈W∖0} w is nonzero at α iff 1, α, α² are F₂-independent, which is automatic for α ∉ F₄.
- **Frobenius.** The reduction is separable, so 𝔭 is unramified in the splitting field. Reduction modulo a prime above 𝔭 is an injective ring map, hence an F₂-linear bijection on roots that intertwines Fr_𝔓 with the q^r-power.
- **Subset sums.** The restriction of Fr to a G-stable U has a characteristic polynomial dividing the full one. Correct.
- **m2 (scope).** G is the arithmetic group Gal(L^sep/L), L = F_q(X), exactly as in SH v2's question. Subspaces stable only under the geometric subgroup Gal(L^sep/F̄_qL) are not addressed. This is fine for the question as posed, but worth one line.

### 2.3 Theorem KP — FIX-1
- **Every owner sample was recomputed** (`kp_ref_ownerlog_compare.py`, F2): the owner's sampling was replicated (galois modulus, random.Random(m)), with all algebra in referee code. Agreement was 356/356.
- **But for m = 24, 28, 32, 36, 40, 44, none of the logged samples is irreducible.**
  - m = 24: [5,5], [2,4,4].
  - m = 32: [7,7], [2,12].
  - m = 44, sample 9: [2,2,16]. And so on.
- **Why the script stops.** kpcheck.py stops when `poss == {0, h−2}`, i.e. when the running intersection of subset-sum sets is {0, n}. It then prints "irreducible Frobenius found (char poly irreducible …)". That message is a mislabel.
- **Why the conclusion survives.** By GS, the dimension of every G-stable subspace of ker P̃ lies in every subset-sum set, hence in the intersection {0, n}. So G is irreducible on ker P̃ ≅ R_P/W, and KP(i)'s conclusion and (iii) are correct as [P + C].
- **The literal statement (i) is also true** (F3, F1, referee seeds). A genuinely irreducible degree-2 Frobenius was found for every m:
  - m = 24: 2/20 samples;
  - m = 28: the owner's sampling, sample #12, cp = 0x1aeb;
  - m = 32: 1/20;
  - m = 36: 1/20;
  - m = 40: 1/20;
  - m = 44: 2/20.
- **Repair.** Either
  - restate (i) as "the intersection of the subset-sum sets of the sampled degree-2 Frobenius elements is {0, n}; hence (GS) G acts irreducibly on R_P/W"; or
  - keep the literal statement and cite [C, referee] F3/F1.
  - In both cases, correct the §5 sentence "a run stops early once an irreducible characteristic polynomial appears" (it stops once the intersection is {0, n}), relabel the table column, and fix §6(b) and the HANDBACK-2330Z wording.
  - The script may stay unchanged to keep its hash, with its misleading message noted in the text.
- **KP(ii)** was confirmed sample by sample, and by fresh referee samples (40 per m, other seeds and moduli). The intersection is {0, 1, n−1, n} for m = 26, 30, 34, 38, 42, and also for 10, 14, 18.
- **KP(iii)** was re-derived; see the item table.

### 2.4 Proposition KL
- **Newton-polygon argument.** A root t ∈ L has integer valuation equal to minus a slope. The finite-place polygons (at all F₂-irreducible factors of the coefficients; these give the same valuations as their F_q-factors, being separable) have positive slopes only in (0, 1). So there are no poles.
- **At ∞.** There is one segment of slope 12, so deg t = 12.
- **Search.** The search on F_q[X]_{≤12} is complete.
- **Referee re-derivation** (`kp_ref_rat.py`):
  - cofactors by 3×3 expansion;
  - M_W from Π_{w∈W}(x + w);
  - P̃ by solving top-down, with P = P̃∘M_W checked exactly;
  - factorisations re-multiplied;
  - kernel on F_q[X]_{≤16} with its own modulus.
  - **Result:** 0 for m = 10, 14, 18, and 3 for the P control.
- **m5.** The owner's kprat output reports "possible poles (π, max order) … 0". These are the places with fractional positive slopes. A sentence saying so would help readers.

### 2.5 §6 consequences — FIX-2 and m3
- **FIX-2.** For a = 1 and m = 24..44, KP and RK show that no band-dimensional G-stable W has RX's relation. So a band non-implication for a = 1 at these m must use a relation not proportional to RX's (C, D).
  - Nothing in the note, in RK, or in RX v2 §3 shows that such a W must be **non-rational**. RX v2 §3 excludes only monomial or scaled-monomial W, and RK concerns only RX's P.
  - **Repair:** "… must come from a (C, D) not proportional to RX's (for a = 1, m = 24..44). Rational W with another (C, D) are not excluded by RK/KP (RX v2 §3 excludes monomial ones only) [OPEN]."
  - The same correction applies to HANDBACK-20261007T2330Z §2 item 4.
- **m3.** §6(d): replace "and with them SH-type twisted half-fields of those dimensions" by: "and with them the G-stable subspaces A(F_Q) and W ∩ A(F_Q) = A(U′) (SH(b)) attached to a minimal twist A, when their dimensions fall in the excluded range. A general A(U) need not be G-stable. For RX's P with R_P/W irreducible, a G-stable A(F_Q) (dim m/2) is **not** excluded by irreducibility alone."

## 3. FIX entries (substantive first)
- **FIX-1 (substantive; KP(i), §5 text and table column, §6(b); HANDBACK-2330Z wording).**
  - **Problem.** The note's evidence for "some degree-2 Frobenius has an irreducible characteristic polynomial" is misreported. Of the 36 samples logged for m ≡ 0 (mod 4), none is irreducible. The script's "irreducible … found" message is triggered by the intersection of subset-sum sets reaching {0, n}.
  - **What stands.** The conclusion (G irreducible on R_P/W, hence (iii)) is unaffected.
  - **Repair.** Restate (i) via the intersection {0, n}, or cite the referee's genuinely irreducible samples (F3/F1). Correct the §5 "stops early" sentence and the table header. Reword §6(b).
- **FIX-2 (substantive; §6(a), HANDBACK-2330Z §2 item 4).**
  - **Problem.** "Must … come from a different (C, D) and a non-rational W" overclaims.
  - **Repair.** Keep "a different (C, D)" with its scope (a = 1, m = 24..44). Drop "non-rational W", or mark rational W with other (C, D) as [OPEN] (RX v2 §3 excludes monomial W only).

## 4. Minor notes
- **m1 (FR proof, step 2/3).** Make the identification k̄ ⊗_k M ≅ M̄ explicit, and say that τ^N ⊗ 1 (not left multiplication by τ^N on M̄) corresponds to precomposition with Fr.
- **m2 (GS scope).** G is the arithmetic Galois group Gal(L^sep/L). Say that subspaces stable only under the geometric subgroup are not addressed. This matches SH's question.
- **m3 (§6(d)).** Restrict "SH-type twisted half-fields" to the G-stable A(F_Q) and A(U′) = W ∩ A(F_Q) of a minimal twist. Note that irreducibility of R_P/W does not exclude A(F_Q) (§2.5).
- **m4 (title/abstract).**
  - Add "(m = 24..44)" to the m ≡ 0 and m ≡ 2 (mod 4) statements.
  - Replace "lines are excluded exactly for m = 10, 14, 18" by "lines are excluded for m = 10, 14, 18 (the m searched)".
  - Optional [C, referee] additions: m = 12, 16, 20 also give intersection {0, n}, and m = 22 gives {0, 1, 8, 9}.
- **m5 (KL / kprat output).** Explain that the listed "(π, 0)" places are those with fractional positive slopes (max 1/2, 1/8, 1/32), so no integer pole order exists.
- **m6 (§2 Remark).** Add "for α ∉ Z = F_Q" (Z from RX v2 (vi); Z = F_Q for a = 1). Optionally cite [C, referee] F5: dim(ker P̃_α ∩ F_q) ≥ n−1 at 210/210 such α, m = 10..26, with the direct root count equal to the FR nullity.

## 5. Checks (referee code; `referee_KP/checks/`)
All were run with `nice -n 19 python3 -I`, one process at a time, each under 10 minutes. The referee code shares no code with the owner's scripts. It uses `galois` only for factoring over F₂ (cross-checked against sympy), for the sparse big-field moduli (re-verified by Rabin's test), and — in F2/F3 only — to replicate the owner's moduli.

| ID | File | Content | Result |
|---|---|---|---|
| F0 | `kpref_lib.py`, `kp_ref_selftest.py/.log` | Library: own Ben-Or moduli, windowed GF(2^N) multiply, Hessenberg characteristic polynomial, top-down quotient, iterated-τ Frobenius matrix. Self-tests: field axioms; char poly vs det(tI−A) at random t; quotient recovery. | ALL OK |
| F1 | `kp_ref_frob.py/.log` | Fresh samples, own moduli. Seeds 9000+m: 40 per m for m ≡ 2 (mod 4); 20 for m = 24..44 with m ≡ 0 (mod 4); 30 for m = 12, 16, 20. Per sample: (a) cofactor relation kills W(α); (b) P = P̃∘M_W exactly; (c) characteristic polynomials of P̃ and P; (d) cp(P) = (T+1)³·cp(P̃) exactly; (e) galois and sympy factorisations agree. | All checks pass. Intersections are {0, n} for m ≡ 0 (mod 4), m = 12..44, and {0, 1, n−1, n} for m ≡ 2 (mod 4), m = 10..42. Irreducible samples: m = 24: 2/20, 32: 1/20, 36: 1/20, 40: 1/20, 44: 2/20, 28: 0/20 (see F3). |
| F2 | `kp_ref_ownerlog_compare.py/.log` | Owner sampling replicated; referee algebra; per-sample comparison with kpcheck.log. | 356/356 factor lists agree. **Genuinely irreducible among the owner's logged samples: 0.** |
| F3 | `kp_ref_ownersamples.py/.log`, `kp_ref_ownersamples_diag.py/.log` | First genuinely irreducible sample within the owner's sampling sequence; per-sample diagnostics for m = 24 and 36. | Irreducible at owner-sequence samples #8 (m = 24), #12 (28), #10 (32), #9 (36), #22 (40); none in the first 40 for m = 44 (F1 has two). The diagnostics confirm that the owner's stopping samples are reducible. |
| F4 | `kp_ref_roots.py/.log` | FR against actual roots in GF(2^{2mL}). | 78/78 nullities equal; 39/39 characteristic polynomials match on split samples. |
| F5 | `kp_ref_deg1.py/.log` | Degree-1 places α ∈ F_q∖F_Q, m = 10..26, 30 each. | dim ≥ n−1 at 210/210; the direct root count equals the FR nullity. |
| F6 | `kp_ref_rat.py/.log` | KL re-derivation: Newton polygons, exact quotient, kernel on F_q[X]_{≤16}, P control. | 0 (m = 10, 14, 18); control 3. No integer positive slope; degree at ∞ exactly 12. |
| O1 | `owner_copy/kprat.py`, `owner_copy/kprat_rerun.log` | Owner script copy re-run. | Byte-identical to kprat.log. |
| O2 | `owner_copy/kpcheck.py`, `owner_copy/kpcheck_rerun_subset.log` | Owner script copy re-run for m = 10, 24, 26, 28, 44. | Each block identical to the corresponding block of kpcheck.log. |
| — | `checks_SHA256SUMS.txt` | sha256 of all of the above. | — |

The checks directory is **not** copied into `DZ_CLOUD_RESULTS`, per this audit's instructions. Only this audit file is written there.

## 6. Files read
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`. It places no restriction on which files a referee may read.
- `referee_KP/src/KP-RX-ROOTSPACE-GALOIS-NOTE-20261007.md`, and `src/owner_scripts/kpcheck.py`, `kpcheck.log`, `kprat.py`, `kprat.log`.
- `claude_archive/` (DZ):
  - `RX-RATIONAL-BAND-COUNTEREXAMPLE-NOTE-20261007-v2.md`;
  - `SH-SUBHALFFIELD-CRITERION-NOTE-20261007-v2.md`;
  - `AUDIT-SH-SUBHALFFIELD-CRITERION-20261007.md`;
  - `DIFFCHECK-SH-v2-20261007.md` (first 60 lines);
  - `TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.1.md` (§3–§6 only, for RS);
  - `HANDBACK-20261007T2303Z.md`, `HANDBACK-20261007T2330Z.md`;
  - a grep of `GLO-…-v2.md` for "rational";
  - the hashes of `claude_archive/scripts/kp*`.
- **Not read:** HFD, EBR, OBC, PTH and the IDEAS/STATE docs. They enter only through [A] citations that this note does not use in its [P] steps.
