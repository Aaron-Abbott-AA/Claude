# REVISION CHECK — RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md (independent referee, 7 Oct 2026, 19:08–19:14Z)

Referee: fresh, independent agent (DZ line, isolated directory `dz_isolated/referee_RBLv2`). I have no stake in the note. I did not run or read any owner script. Every check below is my own code, run with `python3 -I`.

Files under check (sha256):
- v2 `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md`: `f9a1116197a710dac9c5b5cd69b85a36515460028bfcb8d5d05907d9833622ab`.
- v1 `RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md`: `c5f5b805c19676f7a021d8efabc0df5db8c54fe2ccebae30d7b4ad62c2a34cfe`. This matches the hash cited in the audit.
- Audit `AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md`: `75830869976bb05b946b3f528ecc64df7437dc0b9da260fe6e1467f64730a015`.

## Verdict: **PASS**
- All 11 audit FIX items are ADDRESSED. The substantive ones are FIX-1, FIX-2 and FIX-3.
- The re-derivations confirm the corrected mathematics:
  - the RD(c) nonzero-descendant invariant;
  - the stalling constant family;
  - the exact pointwise defects of TX;
  - the generic defect of TX, which is exactly 1;
  - the range and weight arithmetic;
  - the FIX-6 leading coefficient;
  - the FIX-11 fixed field.
- The headline claims are now correctly conditional:
  - RB is [P];
  - RD is [COND on G2 + G5 + (B1a)–(B1b)];
  - G1 ⇐ G1′ + G2 + G4 + G5 + B1 identification.
- I found no new overclaim and no unintended mathematical change.
- There are 9 new items. All are cosmetic (RC-1…RC-9). None is blocking.
- **Release condition.** RC-1 is a required one-line owner edit before release. The v2 header still says "HOLD: do not send to Codex until [re-checked]", and that line must be updated to cite this check. RC-2…RC-9 are recommended, not required.

## Fix-by-fix table

| FIX | Audit's demand | Status | Location in v2 | Referee re-derivation / remark |
|---|---|---|---|---|
| FIX-1 (subst.) | Replace RD(c)'s "reach a bivariate-defect-0 family" with the nonzero-descendant invariant dim ≥ ρ′−2a₂. Name the terminal condition (G5). Make RD [COND on G2+G5]. | **ADDRESSED** | Title ("descends while staying nonzero"); §5 header; §5(c) "Replaced"; §5(e) G5; §5 proof 3; §5 Status; §8 | See R1 below: the invariant is re-proved and an exhaustive state-space check passes. The stalling constant family is confirmed: defect 1 at every square-root step, k = 0…m, at m = 12 and 16 (C1-D). G5 is a new name with no collision in the handoff (grep: no "G5"). The logic "(c) + G5 ⟹ contradiction; defect 0 ⟹ (d) ⟹ HFA1 (G2)" is sound. |
| FIX-2 (subst.) | Make the arc application of RB conditional on (a) B1 monic and (b) B1's root space being a ρ-dim Frobenius twist of V_α, plus the terminal BWG. Change the Status. | **ADDRESSED** | §4 "Application to the arc [COND on (B1a), (B1b)]"; §5 header; §5 Status; §6 | The audit's (a), (b), (c) are now (B1a), (B1b) and G5. Both B1 items are marked [A]-pending, and the ρ′-subspace caveat is kept. |
| FIX-3 (subst.) | G1 ⇐ G1′ + G2 + G4 + G5 + [A] B1. Title "modulo named inputs". | **ADDRESSED** | Title; §6 heading; §6 bold implication; §6 "G4 is the geometric irreducibility…" | The chain checks: G1′ + WG (needs G4) gives e_w = 1; then RB needs (B1a)–(B1b), RD needs G2, and termination needs G5. G3 is correctly omitted, since it concerns only PHFG's "Moreover" count. WG threshold e < (4/3)2^{ρ/2}−1 re-checked (C2). |
| FIX-4 | Exclude degenerate α; a = 0 on F_Q∖U; a = 1 exactly off F_Q; one-line proof that the generic defect is 1; relabel "always 1" as sampling. | **ADDRESSED** | §2 item 1 "Exact values"; item 2 "generic defect is exactly 1"; table note; "Meaning" bullet | C1-A/B: exhaustive at m = 12, ρ = 5 (all 4096 α) and at m = 12, ρ = 6. All of F_Q checked at m = 16, ρ = 6, plus 300 random α ∉ F_Q. 0 mismatches. The count d₁ = 1, d₂ = ρ−1 is fine (Moore over F_q(X) gives d₁+d₂ = ρ). Small wording issues: RC-2, RC-3. |
| FIX-5 | Fix the garbled "x(W)" independence wording in RD(b). | **ADDRESSED** | §5 proof 2; §7 RD(b) | The argument now reads correctly. If ℓ = c(γ,ιγ), then ℓ ≡ 0 on W, a contradiction. |
| FIX-6 | Division-with-remainder wording, exponent 2^{n−k}. | **ADDRESSED** | §4 proof 4; §7 RB(iii) | The leading coefficient of (cτ^d)∘B is c·lc(B)^{2^d} (C2, 200 random cases over F_256). The phrase "free of rank 2" was dropped (RC-5). |
| FIX-7 | "EXACTLY" → "contains". | **ADDRESSED** | §4 Numerical range bullet 2 | a* ≤ ρ/2−2 holds in all 39,798 band cells with ρ ≥ 6 (C2). |
| FIX-8 | Label §1 Consequence [H]. | **ADDRESSED** | §1 "Consequence [H]" | — |
| FIX-9 | Control row: "generically" ρ/2, sporadic ρ/2−1, "no degree-1 bivariate relation". | **ADDRESSED** | §2 Control bullet | Matches the audit's seed-1 m = 20 finding (defect 3 = ρ/2−1 at ρ = 8). |
| FIX-10 | Mark WG/RR as [A] via summary readings. | **ADDRESSED** | Inputs [A], last bullet | IDEAS §305 does record "summaries READ, no proofs checked" (line 11, RR at line 18). HFD §3 quotes WG "as in HFA1" but does not itself record the summary-only status (RC-7). |
| FIX-11 | Add Y = x+ω̄y. | **ADDRESSED** | §4 Setting | Re-derived: ι(x) = x, ι(y) = y, x+ωy = X and x+ω̄y = Y, for all 240 ω ∈ F_256∖F_16 (C2). |

Counts: **ADDRESSED 11 / PARTIAL 0 / NOT ADDRESSED 0.**

## Re-derivations (referee)

**R1. RD(c) invariant [P, referee; C2].**
- Let the starting family have dimension ρ′ and bivariate defect a₂ ≤ ρ′/2−2.
- At each square-root step, either W₀ = W (no dimension loss, defect unchanged), or RR gives dim W₀ ≥ dim W − 2 and RD(b) gives a defect drop of ≥ 1.
- The total number of drops is ≤ a₂. So ρ_i ≥ ρ′−2(a₂−a_i) ≥ ρ′−2a₂ ≥ 4.
- The condition a_i ≤ ρ_i/2−2 is preserved, because a falls by ≥ 1 whenever ρ/2 falls by ≤ 1. This in turn keeps RD(b)'s requirement d₂ ≥ a₂+1 valid at every step.
- C2 enumerates all reachable (dim, defect) states for ρ′ ≤ 80: 405,858 states, 0 failures.

**R2. Stalling family [P, referee; C1-D].**
- W = {u²+βu : u ∈ U}, with β ∉ F_Q, consists of constants. So W₀ = W and √W = Frob^{−1}(W) = {s²+β^{1/2}s : s ∈ U^{1/2}}, which is the same shape. "Its own descendant up to Frobenius twist" is exactly right.
- The defect is 1 for every β ∉ F_Q, by the TX argument with α replaced by β.
- C1-D checks defect 1 and the form of each descendant at every step k = 0…m: m = 12 (ρ = 5, 6) and m = 16 (ρ = 6).

**R3. TX exact defects [P, re-checked; C1-A/B].**
- The proof in v2 §2 item 1 is correct, but needs the extra remark of RC-3.
- Degenerate α: exactly U∖{0}.
- Defect 0: exactly on {0} ∪ (F_Q∖U).
- Defect 1: exactly on α ∉ F_Q.

**R4. TX item 3 [P, referee].**
- C(w) = u⁴ + (X²+X^{Q+1}+X^{2Q})u² + (X^{Q+2}+X^{2Q+1})u, recomputed by hand. D(w^Q) gives the same expression.
- The X⁰- and X²-coefficients are u⁴ and u². So a constant ratio c satisfies c = (u₁/u₂)⁴ = (u₁/u₂)², which forces u₁ = u₂.
- v2's new form and v1's form "(u₁/u₂)² = 1" are both correct.

**R5. Range arithmetic [C2].**
- Checked over every even ρ ∈ [6, 400] and g ∈ [ρ+3, 2ρ], 39,798 cells. The audit's 39,800 also counts the two ρ = 4 cells.
- Q² = KR².
- 2u(2^{a+1}−1)Q < Q²/2 for all a ≤ ρ/2−2.
- R2^aQ ≤ Q²/4.
- a* = ρ−⌈g/2⌉ = ρ−1−⌊(g−1)/2⌋ ≤ ρ/2−2.
- Weight K: K·2^{a+3} < Q, equivalently a ≤ g−ρ/2−4, for all a ≤ a*.
- WG threshold: Q > 3u(e+1) ⟺ e < (4/3)2^{ρ/2}−1, checked for ρ ≤ 20.
- 0 failures.

## Diff v1 → v2 (unintended changes / overclaims / labels)
I ran a word-level diff of the whole note (`checks/wdiff_v1_v2.log`). Every hunk is one of three kinds:
- (i) a logged FIX;
- (ii) bullet or sentence reformatting with no change of content;
- (iii) one of the following **unlogged but correct** editorial edits:
  - §1 AR proof step 3 (λ/λ̄), taken from the audit;
  - §2 item 3, exponent form (u₁/u₂)⁴ = (u₁/u₂)²;
  - "(the leading coefficients are monic)";
  - RD(c) degree bound changed from "u/2" to "(current degree)/2", which is more accurate;
  - attributions to the auditor's [C] checks;
  - dropped phrases, see RC-5;
  - script paths changed (RC-9).

**No new overclaim.** The three headline places that overclaimed in v1 are now all conditional:
- the title;
- the §5 Status;
- the §6 implication.

The new Status bullet "RB+RD do NOT by themselves remove G1 in the rational branch" is explicit.

**Labels.**
- The project labels [P]/[C]/[H]/[A] are used, plus [COND] (declared) and [OPEN] (undeclared, as in v1; see RC-8).
- New claims are labelled:
  - Numerical range (arithmetic) [P];
  - Application [COND on (B1a), (B1b)];
  - Consequence [H];
  - "single example [H]";
  - B1 items [A]-pending.

## RC list (new issues)
All items are cosmetic; none is blocking.

- **RC-1 (cosmetic; required before release).**
  - The v2 header says "The v2 revision itself has NOT yet been re-checked by a referee. **HOLD**: do not send to Codex until it is."
  - Replace it with a line citing this check, e.g. "v2 re-checked (REVISION-CHECK-RBL-v2-20261007.md, 19:08–19:14Z): PASS; 11/11 FIX addressed."
- **RC-2 (cosmetic).** §2 table note: "The auditor's exhaustive check at m = 12 confirmed the exact values in item 1."
  - At m = 12 with ρ = 6 we have U = F_Q, so F_Q∖U = ∅. The defect-0 case on F_Q∖U was not exercised at m = 12. (The audit's T2 covered it at m = 16.)
  - Suggested wording: "exact values confirmed by the auditor (m = 12, ρ = 6, all α; F_Q∖U at m = 16) and by the revision referee (m = 12, ρ = 5, all α; m = 16, ρ = 6, all α ∈ F_Q)".
- **RC-3 (cosmetic).** §2 item 1 proof, "the latter gives r² = r, so u₁ = u₂": insert "and r ≠ 0 (since v₁ ≠ 0), so r = 1 and u₁ = u₂".
- **RC-4 (cosmetic).** §5 Status bullet 3, "RB+RD reduce the structured branch to the terminal question G5", should read "…reduce the rational branch to G5 (mod G2, (B1a)–(B1b))", as §6 already says.
  - Optionally, make the RD label finer:
    - (a) [P];
    - (b)–(d) [COND G2] in the abstract setting;
    - arc application [COND (B1a)–(B1b)];
    - termination [COND G5].
  - Optionally, note that G5 subsumes the BWG clause of HFD §3's G2 for positive-defect terminal families.
  - The current blanket label is conservative, not an overclaim.
- **RC-5 (cosmetic).** Two v1 justifications were dropped without being logged:
  - §4 RB(iii) no longer says the relation module is "free of rank 2". The count (L+1−d₁)₊+(L+1−d₂)₊ uses this. Reinstate the phrase.
  - §7 audit point (4) lost its one-line reason: "an F₂-dependence over L₂ would specialise to one". Reinstate it.
  - Also add the unlogged editorial edits listed in the Diff section to §8 as "editorial (no change of content)".
- **RC-6 (cosmetic).** §7 point (1), "TSZ constants against the exact v: PASS (auditor, 39,800 cells)": the check used the bound v > Q²/2 = KR²/2, not the exact v. Say "against v > Q²/2".
- **RC-7 (cosmetic).** FIX-10 sentence, "Those documents record that only Codex summaries of WG/RR were read":
  - IDEAS §305 records this explicitly.
  - HFD §3 quotes WG "as in HFA1" without stating the reading status.
  - Suggested wording: "IDEAS §305 records summary-only reading; HFD §3's WG quote rests on the same reading."
- **RC-8 (cosmetic).** The [OPEN] label (§6 heading) is not in the declared label list. Add "[OPEN] open problem" to the labels line, or use [H].
- **RC-9 (cosmetic, packaging).** The note now cites `scripts/toycheck.py`, `scripts/toycheck.log` and `audit_RBL_checks/`. Make sure these paths exist in the outbox packet, or adjust the paths.

## Files read
START-HERE contains no referee read restriction beyond the project rules (label claims, audit before sending, never execute incoming Codex scripts). I followed them.

Read in full:
- `work/DZ-CLOUD-HANDOFF/START-HERE-CLOUD-SESSION.md`
- `referee_RBLv2/src/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007-v2.md`
- `referee_RBLv2/src/RBL-RATIONAL-BRANCH-LIFT-NOTE-20261007.md`
- `referee_RBLv2/src/AUDIT-RBL-RATIONAL-BRANCH-LIFT-20261007.md`

Read in part:
- `work/DZ-CLOUD-HANDOFF/notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`, lines 95–140 (§3 PHFG, gaps G1–G4)
- `work/DZ-CLOUD-HANDOFF/docs/IDEAS-PROJECT-TRIM.md`, lines 1–30 (§305)

Grep excerpts only:
- "G5" over the whole handoff (no hits)
- RR / WG / "summar" in HFD and IDEAS-PROJECT-TRIM

Listings (names only):
- `referee_RBLv2/`
- the `work/DZ-CLOUD-HANDOFF/` tree
- the existence of `/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive`

Not read or listed:
- HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads;
- any other scratchpad directory;
- any file content in DZ_CLOUD_RESULTS;
- any owner or auditor script. No git was used.

## checks/ contents
Each script is my own code, run with `python3 -I` (galois 0.4.11, numpy 2.5.3). Each run took under 25 s.
- `check_tx_v2.py`, which takes the arguments m ρ n_off seed. It checks:
  - (A) every α ∈ F_Q: degenerate exactly on U∖{0}, defect 0 elsewhere;
  - (B) α ∉ F_Q, exhaustive or sampled: defect 1;
  - (C) the TX composition identity;
  - (D) the constant family {u²+βu}: defect and form at every square-root step.

  Logs:
  - `check_tx_v2_12_5.log` (exhaustive, 4096 α);
  - `check_tx_v2_12_6.log` (exhaustive; F_Q∖U = ∅);
  - `check_tx_v2_16_6.log` (F_Q exhaustive, 192 α in F_Q∖U; 300 random α off F_Q).

  0 mismatches in all three.
- `check_arith_v2.py` / `check_arith_v2.log`. It checks:
  - range, a* and weight-K arithmetic (39,798 cells);
  - the WG threshold;
  - the RD(c) state-space invariant (405,858 states);
  - the FIX-6 leading coefficient;
  - FIX-11 (ι fixes x and y; X, Y recovered).

  Failures: none.
- `wdiff_v1_v2.py` / `wdiff_v1_v2.log`: the word-level diff of v1 against v2.

`checks/checks_SHA256SUMS.txt`:
```
5c1e0a61381ccdb98ad9ce017bdbef0edea731bf1e20358cf7658d32aa8ae22b  check_tx_v2.py
df60a3b63ed139dd4554c9a5e4b297ba881e5b8ccdd264325f751bcf5844257f  check_tx_v2_12_5.log
a5e37b1e39b73f9ae2415b38f334f887b53449711c0c914417c171fc2a8604d5  check_tx_v2_12_6.log
33c9eb32415c8d0a8aee84a56f360a165c2ad61f5ab73cbfadba4b84b9c2ec08  check_tx_v2_16_6.log
56636e9f6b858e141b987bdbc570bbea1a0a088391031d9806601a9adf1453bf  check_arith_v2.py
e0aefe252ebcf2871dedc964b931b27a148ff503e1854db8bf1fd25298317e7f  check_arith_v2.log
47ed7ed1e0480a91e87933828c5e3a5a087be9a5628c8ea7503c0cd185a9ab33  wdiff_v1_v2.py
dfd90e8899ff47d567f69b19ad3e16e1dc66d347b4e886792ca462f8cac0919c  wdiff_v1_v2.log
```
