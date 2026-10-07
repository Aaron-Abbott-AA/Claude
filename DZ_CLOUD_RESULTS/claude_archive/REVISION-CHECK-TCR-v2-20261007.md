# REVISION CHECK: TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.md (independent referee, cloud session, 7 Oct 2026, 19:39–19:47Z)

Referee: a fresh, isolated subagent for the DZ line ("Wan's numbers of PPs"). I had no contact with the owner session, with Codex, or with the v1 referee. I read nothing outside the DZ scope (see §6).

Notes checked:
- v2 note: sha256 `2eb8e88fa50b2f0c142f8797a5def4a48ddcd8bb5341fa5aabbc7fc4fc2cca38`.
- v1 note: sha256 `bfb63eda267a614a23d6c149a768651ceb8a00081598f26bb6543818bbc07a85`. This matches the hash quoted in v2 and in the audit.
- Audit of v1: `AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md`, sha256 `ac0852eb7dbd26615f2181ac4ef2a8acfaeb838947e6ac6a52ec61c5c5f2273d`.

Labels are as in the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN] open problem.

## 0. Verdict: **PASS** (no blocking issue). The owner should make a small edit before the note goes to the outbox.

- **The fixes.** All 11 FIX items (FIX-1 to FIX-3 and m1–m8) are ADDRESSED. Their locations are in the table in §1.
- **The substantive fixes.**
  - FIX-1 replaces the loose identification (I216) with (I216′). That statement fixes the frame, the scale, the twist and injectivity. Its frame-dependence remark and its counterexample were re-derived independently: analytically, and by [C] check R1.
  - FIX-2 corrects the headline claims. "G5 is removed" now reads "G5 is traded", and Prop 216.3 is now marked as an unaudited earlier owner statement whose proof is not in the handoff.
  - FIX-3 names the stronger twist hypothesis (B1b-fix).
- **The proofs.**
  - The new explicit induction in CD (m5) is correct. It was checked abstractly (R3) and line by line.
  - Lemma HF was re-verified with independent code (R2).
  - The owner's new script reproduces its log byte for byte (R0).
- **New issues.** There are 8 new RC items, none blocking.
  - RC-1 is the most useful one to fix. The pair-uniqueness clause of (I216′) is stated "among the nonfocus μ". Read literally, it is false whenever the comparison direction is itself a nonfocus that lies in the index set. Theorem TC still holds, through the note's own fallback bound "or at worst n" together with v > n. But one line of wording should be corrected before the questions in §6(c) go to Codex, so that Codex is not asked to confirm a hypothesis that cannot hold.
  - RC-7 is administrative and must be done. The "HOLD / not yet re-checked" status line has to be updated.
- **The labels.** TC and RS correctly carry [COND]. Three new derived statements in §0 lack labels (RC-2). I found no new overclaim.

## 1. Fix-by-fix table

| Item | Audit request | Status | Location in v2 | Referee note |
|---|---|---|---|---|
| FIX-1 | Replace (I216) with a precise statement fixing the frame, scale, twist and an injective α ↦ μ; record the frame counterexample (C3) and the R3AF–AI scaling remark; redirect §6(c) | **ADDRESSED** | §0, lines 21–35; §3 steps 3–4 (lines 97–98); §6(c) (lines 136–141); §7 (lines 146–147) | (I216′) matches the audit's suggested form. The pair-counting derivation in line 30 is correct, but only among the finite nonfoci; see RC-1 and RC-2. The counterexample was re-derived (§2.1). |
| FIX-2 | Correct the title, §3 "What changed" and §5 (G5 traded, not removed); make the status of Prop 216.3 explicit | **ADDRESSED** | Title (line 1); §0 lines 17–20; §3 lines 100–105; §5 lines 126–131 | The title names (I216′) + Prop 216.3, and (B1b-fix) only implicitly, through "including". Acceptable. |
| FIX-3 | Name (B1b-fix) and use the name in TC, RS, §5 and §6(a) | **ADDRESSED** (with cosmetic RC-3) | §0 lines 13–15; TC header line 87 and step 1 (line 95); §3 line 104; §5 line 127; §6(a) line 134 | The §4 (RS) header does not name it, although the change log says §4 does. It is covered only by the "folded into (I216′)" convention, and the text of (I216′) does not mention V_α (RC-3). |
| m1 | Mark G4 as needed only for G1′ ⇒ G1″ | ADDRESSED | §4 header (line 107); §5 line 128 | — |
| m2 | Call the HF consequence a reformulation of G2 | ADDRESSED | §1, lines 61–63 | — |
| m3 | State RR_k directly on W^rat_k | ADDRESSED | §4 step 4, line 121 | The phrase "part of G2 for the rational subspace" is consistent with RR's scope ("rational root subspaces"). |
| m4 | Separate rationality from (B1a) | ADDRESSED | §3 Setting, line 90 | — |
| m5 | Make the CD induction explicit; mark step 3 as redundant | ADDRESSED | §2 line 73, step 2 line 79, step 3 lines 80–81 | Verified (§2.2, R3). Step 3 uses the symbol d₁, which v2 never defines (RC-5). |
| m6 | Log seeds and command lines; force s′ = 0 samples | ADDRESSED | §1 [C], lines 53–59; `hassecheck_v2.py/.log` | Re-run byte-identical (R0); 227 + 173 + 119 = 519 cases with s′ = 0, as stated. |
| m7 | Simplify the RS step-2 justification | ADDRESSED | §4 step 2, line 119 | — |
| m8 | Make injectivity explicit in TC step 3 and §7 | ADDRESSED | Line 97; line 146 | It says "distinct radicals" where it should say "distinct directions" (RC-4). |

**Counts: ADDRESSED 11, PARTIAL 0, NOT ADDRESSED 0.**

## 2. Re-derivation of the substantive fixes

### 2.1 FIX-1: (I216′), pair counting, and frame dependence

**Pair counting ([P] by the referee, modulo the two-level autocorrelation read from STATE §5 [A]).**
- STATE §5 says that each nonfocus projection U_μ has autocorrelation exactly n on Rad_μ∖0.
- So for b ∈ Rad_μ∖0 we have U_μ + b = U_μ. The projection π_μ is injective on R, so the n points of R split into n/2 unordered pairs {P, P′} with π_μ(P − P′) = b.
- Suppose each unordered pair serves at most one μ (pair uniqueness). There are n(n−1)/2 pairs, so #{μ : b ∈ Rad_μ} ≤ (n(n−1)/2)/(n/2) = n − 1.
- Hence line 30 of v2 is correct: given (I216′) and this [A] reading, Prop 216.3 holds in that frame.

**Where pair uniqueness holds.**
- Take π_μ(x, y) = y + μx and a pair difference (Δx, Δy) with Δx ≠ 0. Then Δy + μΔx = b has exactly one solution μ.
- So pair uniqueness among the *finite* nonfoci holds exactly when there are no vertical pairs, that is, exactly when ∞ is a nonfocus.
- **It fails when ∞ itself is counted as a nonfocus μ.** Take π_∞ = x and a pair with Δx = b. That pair serves ∞ and also, generically, one finite μ.
  - In that case the bound becomes n − 1 + 1 = n. The extra 1 comes from ∞, because x is injective on R and so at most n/2 pairs have Δx = b.
  - This is exactly the hedge "or at worst n" in v2. The hedge is correct, but v2 does not justify it, and the hypothesis as literally stated excludes it (RC-1).

**The counterexample, re-derived analytically.**
- Take R = {(a, a²) : a ∈ A₀}, with A₀ ≤ F_q an F₂-subspace of dimension k.
- The secant slopes are a + a′ ∈ A₀∖0, so the n − 1 foci each carry a perfect matching.
- In the original frame, π_μ(R) = {a² + μa}, which is a subspace. b lies in it exactly when μ = (b + a²)/a for some a ∈ A₀∖0, which gives at most n − 1 values of μ.
- In the frame (X, Y) = (t₀x + y, x), with t₀ ∈ A₀∖0 a focus, the focus direction (1, t₀) becomes vertical. Then π_μ = a + μ(a² + t₀a), and at a = t₀ this equals t₀ for every μ. **So b = t₀ lies in every finite nonfocus radical.**

**[C] R1** (`tcrv2_referee_checks.py frame 5`): q = 64 and 256, n = 4, 8 and 16.
- **Original frame and 3 random frames with a nonfocus vertical (24 frames):**
  - hyperfocused (n − 1 slopes, each a matching);
  - the two-level autocorrelation set equals the translation stabiliser, as asserted;
  - pair uniqueness holds among the finite nonfoci;
  - the maximum number of finite radicals per b is **exactly n − 1**;
  - with π_∞ included, pair uniqueness **fails** in all 24 frames, and the maximum is **exactly n**.
- **Focus-vertical frame (6 cases):** b = t₀ lies in **all** finite nonfocus radicals: 62, 58, 50, 254, 250 and 242 of them, matching audit C3. Pair uniqueness fails.

**TC with RC-1 taken into account.**
- Total nonfoci: q + 1 − (n − 1) = q/2 + d + 2, using STATE §1 ("exactly n − 1 slopes").
- Finite nonfoci: q/2 + d + 1.
- Comparison with n = q/2 − d:
  - If μ is allowed to be ∞ (constant n): margin v − n = 2d + 2 > 0.
  - If μ(α) is restricted to the finite nonfoci (constant n − 1): at most one α is lost, and v − 1 − (n − 1) ≥ 2d + 1 > 0.
- **Either way TC step 4 goes through, so the theorem stands.** The arithmetic was checked with sympy in R4.

**Scaling remark (R3AF–AI).** v2 records it correctly. The scaling ambiguity is why φ must be independent of α. Taking φ = λx^{2^{−s}} as an instance is consistent with this.

### 2.2 CD induction (m5)

- **Invariant.** The invariant H(k) is dim W_k ≥ ρ′ − 2(a₂ − a(k)). Since a₂ ≤ ρ′/2 − 2, it implies a(k) ≤ dim W_k/2 − 2.
- **Base case.** H(0) holds.
- **Preservation.**
  - A lossless step keeps the dimension, and a(k+1) ≤ a(k).
  - A lossy step drops the dimension by at most 2 (RR_k), and a(k+1) ≤ a(k) − 1 (RD(b)).
- **Step 3 is redundant.** At a(k) = 0, a lossy step would force a(k+1) ≤ −1.
- **[C] R3** (`cdind`): every abstract path for ρ′ ≤ 24 and a₂ ≤ ρ′/2 − 2, 2926 reachable states, 0 failures.
- **[A]** The audit's C2-cd check (600 concrete families) is cited accurately.

### 2.3 Lemma HF and the Hasse script (m6)

- **R0.** The owner's `hassecheck_v2.py` was copied to `checks/owner_copy/` and re-run with the logged command lines. The output is **byte-identical** to the owner's log. The script reads no files.
- **R2.** Independent code (galois, GF(2^10), seed 13), not derived from the owner's code:
  - (H1): 0 failures in 500 samples;
  - (H2): 0 failures, with 283 cases where s′ = 0;
  - the rank identity rank(D^{(2^k)}|W_k) = dim W_k − dim W_{k+1}: 0 failures on 100 random F₂-spaces.

### 2.4 Arithmetic (§4 table, §0 margin)

**[C] R4** (`arith`) checked 870 even cells with ρ ≤ 60 and found 0 failures:
- 2a* + 4 = 2ρ − 2⌈g/2⌉ + 4;
- the value is 6 at g = 2ρ − 2, and ρ at g = ρ + 3 and ρ + 4;
- a* ≤ ρ/2 − 2;
- the margins v − n = 2d + 2 (all nonfoci) and 2d + 1 (finite nonfoci);
- the pair-count bound n − 1, or n when π_∞ is included.

## 3. Diff v1 → v2: unintended changes, overclaims and labels

The diff, with the [v2: …] tags stripped, has 238 changed lines. I compared the two versions section by section.

**Intended changes.** Every intended change matches the change log in §8, except that the log lists §4 under FIX-3 (see RC-3).

**Unintended or undocumented changes (all cosmetic):**
- TC step 1 drops v1's citation "RBL v2.1 §4 (Numerical range)" (RC-6).
- RS step 3 drops v1's "the TSZ condition does not depend on dimension". That sentence is the reason RB's numerical condition carries over to W′ (RC-6).
- RS(b) drops v1's gloss on G1″ ("large-orbit roots span ≤ ρ − 2a* − 4 dimensions mod W^rat"). Harmless.
- §7 drops v1's remark on an α-dependent s(α), where pigeonhole gives only v/m. Harmless now that φ is α-independent.
- New parenthetical in TC step 1: "the defect is invariant under Frobenius twists and scalings". This is correct: C(x/λ) has the same degree, and coefficient-wise Frobenius sends C to C^σ with C^σ(v²) = C(v)².

**Overclaims.**
- No new overclaim was found.
- The title still states the conclusion without the [COND] tag. That was true in v1 as well, and the title now names the conditional inputs explicitly. Acceptable (optional RC-8).
- "G5 is not eliminated but TRADED" is accurate.

**Labels.**
- These are correct: TC [COND on G2, (B1a), (I216′) incl. (B1b-fix), Prop 216.3 [A]]; RS [COND …; G4 for (b) only]; CD [P mod RR_k]; HF [P]; §5 [COND]; G1″ [OPEN].
- These lack labels (RC-2):
  - line 30, "Prop 216.3 holds in that frame by pair counting";
  - line 34, the R3AF–AI scaling remark ([A], IDEAS-RECENT §298 via the audit);
  - line 36, "v − n ≥ 2d + 1" ([A], STATE §1 gives exactly n − 1 foci).

## 4. New issues (RC list)

| RC | Severity | Location | Issue and suggested edit |
|---|---|---|---|
| **RC-1** | minor, non-blocking (recommended before §6(c) goes to Codex) | §0 (I216′) "pair uniqueness", line 27; line 30 | "At most one solution among the nonfocus μ" is false whenever the comparison direction (∞) is a nonfocus and belongs to the index set: π_∞ and one finite μ share pairs (R1, all 24 frames). **Edit:** say "among the nonfocus μ ≠ the comparison direction". Add one sentence: "the comparison projection, if used, adds at most one radical, so the count is ≤ n; alternatively drop the ≤ 1 α with μ(α) = ∞, since v − 1 > n − 1". TC is unaffected. |
| RC-2 | cosmetic (labels) | Lines 30, 34, 36 | Line 30: label it [P mod the two-level autocorrelation, STATE §5 [A]]. Optionally note that, given (I216′) and that [A] reading, the unaudited Prop 216.3 is *derived* in the needed form, which would remove it as a separate input. Line 34: label [A] (R3AF–AI, IDEAS-RECENT §298). Line 36: label [A] (STATE §1: exactly n − 1 foci; finite nonfoci q/2 + d + 1). |
| RC-3 | cosmetic | §0 line 15; §4 header line 107; change log line 158 | (B1b-fix) is "folded into (I216′)", but the text of (I216′) never mentions V_α, and the RS header does not name (B1b-fix). Logically, TC step 1 needs only RBL's weak (B1b), since the defect is twist-invariant, and fixedness enters only through the α-independent φ in step 3. **Edit:** either add the clause "(twist) W(α) = V_α^{2^s}, s fixed" to (I216′), or list (B1b-fix) explicitly in the §4 header and correct the change log. |
| RC-4 | cosmetic | Line 97; line 146 | "v DISTINCT nonfocus radicals" and "distinct α give distinct radicals" should say distinct *directions* μ(α). Pair counting counts μ, and two directions could have equal radical subspaces. |
| RC-5 | cosmetic | §2 step 3, line 80 | d₁ is undefined in v2. It is the audit's symbol for the degree of the D_X-image relation. Say "would force a(k+1) ≤ −1" instead. |
| RC-6 | cosmetic | TC step 1 (line 95); RS step 3 (line 120) | Restore the citation "RBL v2.1 §4 (Numerical range)" and the remark "the TSZ condition 2u(2^{a*+1}−1)Q < v does not depend on ρ′". |
| **RC-7** | administrative, **required before the outbox** | Lines 9 and 133 | The "HOLD … NOT yet been re-checked" status must be updated to cite this revision check (PASS) and its sha256. |
| RC-8 | optional | Title | Append "[COND]", or "(conditional on G2, B1, (I216′), Prop 216.3)". |

RC count: 8. **Blocking: 0.** Cosmetic or minor: 8. RC-1 is the recommended wording fix. RC-7 is the required administrative edit.

**Outbox recommendation.** TCR v2 can go to the outbox after a small owner edit: RC-7 (required), plus RC-1 (strongly recommended, one or two lines). Neither needs new mathematics. No further referee round is needed if the edits are limited to these lines.

## 5. Referee checks (`checks/`, all run with `python3 -I`, one process at a time, each under 15 s)

| ID | Command | Result |
|---|---|---|
| R0 | `owner_copy/hassecheck_v2.py 8 400 1`, `12 300 2`, `16 200 3` | Output byte-identical to the owner's `hassecheck_v2.log` (`owner_copy/rerun_v2.log`); 0/0 failures; 519 cases with s′ = 0 |
| R1 | `tcrv2_referee_checks.py frame 5` | 30 frames. Nonfocus-vertical frames: pair uniqueness holds among the finite nonfoci; max n − 1 per b (sharp); including π_∞, pair uniqueness fails and max = n. Focus-vertical frames: b = t₀ lies in all finite nonfocus radicals (62/58/50/254/250/242). All assertions passed. |
| R2 | `tcrv2_referee_checks.py hasse 13 500` | (H1) 0, (H2) 0 (283 cases with s′ = 0), rank identity 0 failures / 100 spaces |
| R3 | `tcrv2_referee_checks.py cdind` | 2926 states, 0 invariant failures |
| R4 | `tcrv2_referee_checks.py arith` | 870 cells, 0 failures; margins 2d + 2 / 2d + 1; pair bound n − 1 (+1) |

All outputs are in `checks/run.log`. Contents of `checks/checks_SHA256SUMS.txt`:
```
c70f46589ed72c5b8aa9a79271dcae5c2dc480a8c2f8c8021810af9f18cdc7de  tcrv2_referee_checks.py
3a17d74b0a6678b0a78054d5d16ec1dc3faddaad7006c62436e14977cfce0c87  run.log
afe56bb12cb83f3e6d70bf78969d8d2d2af723c2a24ce5afcbcb275308f9c5d9  owner_copy/hassecheck_v2.py
117c91da14040a82868734517b0155c0865bfe907bbd075a93c3e11fc150ba50  owner_copy/rerun_v2.log
```
Location: `dz_isolated/referee_TCRv2/checks/`. The owner script copy has the same hash as `src/owner_scripts/hassecheck_v2.py`, and the re-run log has the same hash as the owner's log.

## 6. Files read

**DZ handoff and context.**
- `dz_isolated/work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`, read in full. It contains no explicit referee read-restriction; I obeyed its standing rules, including running no Codex scripts and labelling every claim.
- `DZ-CLOUD-HANDOFF/docs/STATE-PROJECT-TRIM.md`: lines 1–20, lines 195–225, and grep hits for "216 | radical | nonfoc | foci".
- Directory names only: `DZ-CLOUD-HANDOFF/` and `docs/`, `notes/`.

**Revision-check sources.**
- `dz_isolated/referee_TCRv2/src/TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007-v2.md` (full)
- `dz_isolated/referee_TCRv2/src/TCR-TERMINAL-CONSTANT-ROOT-NOTE-20261007.md` (full)
- `dz_isolated/referee_TCRv2/src/AUDIT-TCR-TERMINAL-CONSTANT-ROOT-20261007.md` (full)
- `dz_isolated/referee_TCRv2/src/owner_scripts/hassecheck_v2.py` and `hassecheck_v2.log` (full; read before running the copy)

**Output location.** `/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive/`: I only tested that the target file name did not already exist. Nothing was listed or opened there.

**Not read.** No HYP or 3PP directories, no uploads, no other scratchpad directory, no git.
