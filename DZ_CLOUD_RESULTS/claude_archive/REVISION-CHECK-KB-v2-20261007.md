# REVISION CHECK — KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.md (independent referee, cloud session, 7 Oct 2026, 21:12–21:18Z)

Referee: a fresh, isolated subagent for the DZ line (project "Wan's numbers of PPs"). It had no contact with the owner session, with Codex, or with the HYP line. The files read are listed in §6.

**Note checked:** `src/KB-KUMMER-BINOMIAL-GATE-NOTE-20261007-v2.md`, sha256 `4af210536e8b98d17be78024c65ce4ffadd0a1c464490dc0d6634598fe49df59`. The copy in `claude_archive/` is byte-identical (checked with `cmp`).
**Against:** v1, sha256 `d6b60aa1d52119e7b4247072c47bd94f5deab0a7b8639363b9da4575b6f124d7`, which matches the prefix and suffix cited in v2's status block. The archive copy is also byte-identical. The audit of v1 has sha256 `fc0cc9cec7fbe9a725ca50dd9ed3c5ae0b61d15b5abc2d2199b8135838daf168`.

**Labels** follow the handoff: [P] owner proof, [C] computation, [H] heuristic, [A] reading of a source, [COND] conditional, [OPEN] open problem. Anything the referee proves is marked "[P, referee]".

## 0. Verdict: **PASS-with-fixes**

**All 11 audit items are ADDRESSED: FIX-1, FIX-2 and m1–m9.** The optional lemma, KB(vi), was adopted, and it **passes** a full audit (§2).

**One new blocking item: RC-1, a status overclaim.**
- The title and §3 say that **all** B = 1 subcases "go to HFA".
- §3's OPEN list and §2's last bullet then leave the general B = 1 case (gate-failing cells with g < 3ρ/2) out of what is open.
- That case is not covered by HFA. By KB(i) it has a₂ ≥ (3ρ−2g)/4 ≥ 1, so it is not a global (H) family.
- HFD §3's narrow-sub-case route is a sketch, and its WG step needs an orbit e < 2^{ρ/2}. KB(vi) itself proves e ≥ 2^{ρ/2+1} − 1.
- The fix is a wording edit in three or four places. No mathematics changes.

**Four cosmetic items: RC-2 to RC-5.**

**Outbox:** the note needs a **small owner edit** (RC-1, and optionally RC-2 to RC-5) before it can go out. After that edit no re-audit is needed, only a diff check.

## 1. Fix-by-fix table

| Item | Requested | Location in v2 | Finding | Status |
|---|---|---|---|---|
| FIX-1 | Route the B = 1 inner-resonance subcase to HFA, cite the ledger, change "open pending EWF1" to "closed by HFA [A], pending HFA3 scope", rephrase §4(a), record general B = 1 as HFD §3's partial case | l.1 (title); §1 "Subcases with B = 1" l.76–85; §3 l.98–101; §4(a) l.104 | Every requested element is present. The [P, referee] relation w^Q = y·w is re-derived in §2 below. The η(P) ≠ 0 argument and the citations (STATE §3y, IDEAS §321 / EB, STATE §3z) are correct. The status wording is exactly what the audit asked for. **New overreach while implementing it:** see RC-1. | ADDRESSED (RC-1) |
| FIX-2 | Correct "same threshold as WG", record the Kummer–Weil bound, optionally add KB(vi) | §1(vi) l.52 and proof step 5 l.69–74; §2 l.88–90; also §3 l.97 and §4(b) l.108 | The false sentence is gone. The window [3, 2^{ρ/2+1} − 3], the 37/88 count, the survival of e = N′ and the ratio of about 1.5 are all reproduced exactly (`kbv2_weil`). The §2 header "[H; arithmetic P]" is now true. | ADDRESSED |
| m1 | Label "counting alone" as [H] in the title | l.1 | "Counting alone does not exclude the rest [H]". | ADDRESSED |
| m2 | "Nonzero"; A is the minimal-degree solution; only deg A ≤ m/4 − 1 is used | §0 l.21–23 | All three are present. This matches GX v2.1's (GLS₁) wording. | ADDRESSED |
| m3 | One-line proof that χ(G) lies in no proper subfield | §1(i) l.35 | 2^{m/8} − 1 ≤ 2^{ρ/2} − 1 < T, which is correct because m/4 ≤ ρ. Rechecked for all 2450 KB-admitting cells with ρ ≤ 200. | ADDRESSED |
| m4 | Separability and unramifiedness; trivial decomposition group; delete "except possibly zeros of h" | §0 (B1a⁺) l.24; §1(iv) l.50; (v) l.51; proof step 4 l.68 | All present, and the clause is deleted. (B1a⁺) was given "T-degree 2^ρ" to support this; see RC-4. | ADDRESSED |
| m5 | k := η^e ∈ F_q[X] with deg ≤ eu; y = h^{s+1} | §1(ii) l.44; (iii) l.48; proof steps 2–3 l.63, l.67 | Correct. Q − 1 = (s−1)(s+1) because Q = s². χ(g)^e = 1 because χ(G) is cyclic of order e. | ADDRESSED |
| m6 | Standing setting; GO's input step; a₂ ≥ (3ρ−2g)/4 | §0 l.12–15; §1(i) l.36 | Present and correct: ρ − m/4 = (3ρ−2g)/4, and a* ≤ ρ/2 − 2 follows from g ≥ ρ+3. | ADDRESSED |
| m7 | η(P) rather than η(α); Frobenius twist; η(P) ≠ 0 | §1 subcases l.79 | All three are present. | ADDRESSED |
| m8 | "Audited" rather than "reviewed"; inner-resonance citation is IDEAS §321 / EB | §0 l.18; §2 l.92; §1 subcases l.82 | "DZ-internal notes, audited and revision-checked" is accurate. GX v2 was revision-checked (PASS) before the v2.1 RC edits. PTH v2 was revision-checked, and v2.1 was diff-checked before v2.2. | ADDRESSED |
| m9 | Define d | §0 l.29 | d := deg B = deg A. | ADDRESSED |

**Counts:** 11 ADDRESSED, 0 PARTIAL, 0 NOT ADDRESSED.

## 2. Re-derivation of the substantive fixes and audit of the optional lemma KB(vi)

**FIX-1 (inner resonance g = 3ρ/2, B = 1)** [P, referee, re-derived].
- m = 2g + ρ = 4ρ, so m/4 = ρ, s = 2^ρ and Q = 2^{2ρ} = s².
- With B = 1 we have A = a₀, and W′ = W = ηF_{2^ρ}, of dimension ρ = dim W.
- F_{2^ρ} ⊂ F_Q, so for w = ηt we get w^Q = η^Q t = η^{Q−1}w. Here η^{Q−1} = a₀^{Q−1} = y ∈ L, using λ^{Q−1} = 1. So C = y, D = 1 is a degree-0 generic relation.
- Pointwise, W(α) = η(P)F_{2^ρ} has dimension ρ by (B1b), so η(P) ≠ 0. A Frobenius twist of η(P)F_{2^ρ} lies in η(P)^{2^f}F_Q, so a(V_α) = 0 (C = x/μ has degree 0).
- **Consistency:** KB(i)'s bound gives a₂ ≥ (3ρ − 3ρ)/4 = 0, so nothing conflicts.

**FIX-2 / KB(vi) — full audit of the optional lemma.**

Statement: under KB's inputs plus the count v := |N| > q/2 (GO's input step, EBR Lemma G [A]), e ≥ 2^{ρ/2+1} − 1. Put K := 2^{ρ/2}.

1. **The cover.** L(η) = L(k^{1/e}), with k = η^e ∈ F_q[X] by (iii), deg k ≤ eu, and μ_e ⊂ F_s ⊂ F_q.
   - e | s − 1 is odd, so the cover is tame.
   - Riemann–Hurwitz for a Kummer cover gives 2γ − 2 = −2e + Σ_P (e − gcd(e, v_P(k))). Bounding the sum by the r₀ finite zeros plus ∞, each contributing ≤ e − 1, gives 2γ ≤ (r₀−1)(e−1) ≤ (eu−1)(e−1).
   - The case r₀ = 0 (k constant) would make L(η)/L a constant-field extension, or trivial. Both are excluded: the first by total splitting at a rational place, the second by e ≥ T > 1.
2. **Constant field.** A rational place of L that splits into e rational places forces the full constant field of L(η) to be F_q. The note states this, and it is correct.
3. **Total splitting at every α ∈ N.** η = Σ M⁺_{0j}w_j lies in the splitting field of B1. B1(α, ·) is monic with 2^ρ distinct roots in F_q, by (B1a⁺) and (B1b). So every place above α is unramified with residue degree 1. This holds at zeros of k too, so no exception is needed.
4. **Weil.** e·v ≤ q + 1 + 2γ√q ≤ q + 1 + (eu−1)(e−1)Q, with Q = √q = 2^{g+ρ/2} = 4uK, where u = 2^{g−2}.
5. **The exact window** [P, referee]. Put f(e) := e(q/2 + 1) − q − 1 − (eu−1)(e−1)Q. This is concave in e, and Q² = q = 2uKQ.
   - f(3) = Q(2uK − 6u + 2) + 2 > 0 for K ≥ 4.
   - f(2K−3) = Q[u(4K−12) + 2K − 4] + 2K − 4 > 0.
   - f(2K−1) = Q(2K − 2 − 2u) + 2K − 2 < 0, since u = 2^{g−2} ≥ 2^{ρ+1} > K.
   - Hence the contradiction set among odd e is exactly [3, 2K−3]. Every e ≥ T > 1 in it is impossible, and e ≥ 2K − 1. **PASS.**
6. **[C, referee] `kbv2_weil`.**
   - All 2450 KB-admitting cells with ρ ≤ 200: Q = 4uK, the window endpoints, the escape of 2K−1, the escape of N′, N′ ≥ 2^{ρ/2+2}, the bound on a₂, d + 4 ≤ m/4 and the subfield bound all hold, with 0 violations.
   - GX census, ρ ∈ [10, 40]: exactly **88** gate-failing cells, with the exact window equal to [3, 2K−3] in each.
   - Admissible e (e | s−1, e ≥ T, ord_e 2 = m/4) are excluded in some cell for **37** of the 88 cells. e = N′ is admissible and survives in all 88.
   - (2K−1)/T lies in [1.500, 1.512].
7. **[C, referee] `kbv2_kummer_toy`.** For 102 random curves y^e = k over F_{2^8} and F_{2^12} (e odd, e | q−1), the bound N₁ ≤ q + 1 + (deg k − 1)(e−1)√q held every time, with 0 violations.

**Label check.** "[P, referee; adopted]" is correct. The extra input "EBR Lemma G [A]" (the count v > q/2) is already inside the standing setting, via GO's input step, but v itself is never defined in v2 (RC-3).

## 3. Diff v1 → v2 (`checks/kb_v1_v2.diff`, 184 lines)

**Naming consistency: OK.**
- The file name is `-v2`.
- The title says "owner note v2 … 21:10Z; v1 20:59Z", with markers [v2: m1, FIX-1, FIX-2].
- The status block is headed "AUDIT STATUS (v2)" and carries a "v2 HOLD".
- The change log is headed "v1 → v2".
- The [v2: …] markers sit at every logged location.
- The change-log rows match the actual edits.

**Unintended or unlogged changes, all harmless (RC-4):**
- (B1a⁺) gained "of T-degree 2^ρ". This changes a named input. It is implied by W being the ρ-dimensional root space of a separable monic B1, but it should be logged.
- "P ⊇ W" became "R_P ⊇ W". This is a clarification.
- (B1b)'s "In particular B1 is totally split at α" was moved, as a derived statement, into (iv).
- FIX-2 also edits §3 (l.97) and §4(b) (l.108), which the change log does not list.
- §4(b) is now restricted to deg B ≥ 1.

**Overclaims:** only RC-1. No other [P] clause was strengthened beyond what was proved. The proof of KB(i)–(v) is unchanged in substance from the audited v1.

**Label errors:** none beyond RC-3. The use of [A], [H], [C, referee] and [P, referee; adopted] is consistent.

## 4. New issues (RC list)

**RC-1 (BLOCKING; wording only) — the general B = 1 case is presented as routed to HFA and has dropped off the OPEN list.**

Where:
- the title: "The B = 1 subcases are half-field and go to HFA";
- §3 l.98: "B = 1 subcases: half-field, routed to HFA [A]";
- §3 OPEN, l.100: only "KB with B ≠ 1";
- §2 l.92: "KB with B ≠ 1 needs arc-specific input".

Why the claim fails for g < 3ρ/2:
- W′ = ηF_s is a sub-radical of dimension m/4 < ρ.
- KB(i) forces a₂ ≥ (3ρ−2g)/4 ≥ 1, so this is **not** HFA's global (H) hypothesis (a ≡ 0).
- The HFD §3 route is a sketch ([Prop], with gap G1), its narrow repair needs 2j + 2log₂(j+1) < ρ/2, and its WG step 3 needs e_w < 2^{ρ/2}.
- KB(vi) gives e ≥ 2^{ρ/2+1} − 1, so that WG step fails exactly here, by construction.
- §1 l.85 ("HFD §3's narrow partial-half-field sub-case [A]") and §4(a) (which asks Codex whether HFA covers it) are correct. The title and §3 contradict them.

**Fix.**
- Title: "The inner-resonance B = 1 subcase is global half-field and goes to HFA [A]".
- §3: split it into "inner resonance B = 1: routed to HFA, pending HFA3's scope" and "general B = 1 (g < 3ρ/2): partial half-field, OPEN (question §4(a))".
- OPEN list: add "general B = 1 with g < 3ρ/2".
- §2 l.92: "B ≠ 1, or B = 1 off the inner resonance".

**RC-2 (cosmetic).** The proof of (vi) writes the curve as "y^e = k", but y is already a₀^{Q−1} ∈ L from (ii). Rename it, e.g. Y^e = k.

**RC-3 (cosmetic).** v is used in (vi) ("the v > q/2 places of N") but never defined. Add "v := |N| > q/2 (GO's input step / EBR Lemma G [A])" to §0.

**RC-4 (cosmetic).** Log the unlogged changes in §6:
- (B1a⁺) "T-degree 2^ρ", under m4;
- R_P ⊇ W;
- (B1b)'s splitting sentence moved into (iv);
- FIX-2's edits to §3 and §4(b).

**RC-5 (cosmetic, optional).** Following the PTH/GX precedent, the AUDIT STATUS block could record the audit file's sha256 (`fc0cc9ce…38daf168`, full value above) and, after this check, this revision check's sha256 and verdict.

**RC count:** 1 blocking (RC-1, wording only) and 4 cosmetic (RC-2 to RC-5).

## 5. `checks/` (referee code, `nice -n 19 python3 -I`, galois 0.4.11, sympy 1.14.0, each run under 1 s)
- **`kbv2_weil.py` / `kbv2_weil.log`.** Exact integer arithmetic.
  - The KB(vi) window and the escapes of 2K−1 and N′ for all ρ ≤ 200.
  - The GX census of 88 cells and the 37 cells with an excluded admissible e.
  - The bounds of KB(i)/(iii).
  - 0 violations.
- **`kbv2_kummer_toy.py` / `kbv2_kummer_toy.log`.** A Weil + Riemann–Hurwitz sanity toy for Kummer curves: 102 tests, 0 violations.
- **`kb_v1_v2.diff`.** The v1 → v2 diff.
- **`checks_SHA256SUMS.txt`** (sha256 `4bf7de268ee2d1f8464dd0f2def871d58483fc725ff5fdf1c2e00df295c2204a`):
  - `b52dbf29abca3d5ac587231718c389710b309bb3ef0a6bb1d0f804520941c970  kbv2_weil.py`
  - `1e19d399e0a2a34a6432a70dc1a05e669f36c8c8f4bfdba50a6da71e2002d6b7  kbv2_weil.log`
  - `93ce98ce7dd21ad8afead9e1f840992436f9f418c7ca2d3b35ae0db4f99fed6b  kbv2_kummer_toy.py`
  - `183a3c3208eadfad1309b265482a34883c1daa48b47adf3ae26bb3ffcc34094a  kbv2_kummer_toy.log`
  - `a9512e4bc2cca0d1a363f2148bdf168dc4f3cd6d95ba7bf3ea77f7696e079232  kb_v1_v2.diff`
- The checks live in `referee_KBv2/checks/`. The only file written to DZ_CLOUD_RESULTS is this one.

## 6. Files read
**`referee_KBv2/src/`** (all in full):
- the v2 note;
- the v1 note;
- `AUDIT-KB-KUMMER-BINOMIAL-GATE-20261007.md`.

**Handoff (`work/DZ-CLOUD-HANDOFF/`):**
- `START-HERE-CLOUD-SESSION.md`, in full. It contains no explicit restriction on what a referee may read; its isolation rules were followed.
- `notes/HFD-HALF-FIELD-DEFECT-NOTE-20261007.md`: the heading list, grep hits for "partial", and lines 99–125 (§3 PHFG and its audit gaps).
- The directory listing.

**Archive (`/home/user/Claude/DZ_CLOUD_RESULTS/claude_archive/`):**
- the directory listing;
- a `cmp` of the KB v1 and v2 copies;
- `GX-GLOBAL-TWIST-EXCLUSION-NOTE-20261007-v2.1.md`: status lines from 1–20 (grep) and lines 70–110 (census and failure pattern);
- `PTH-POINTWISE-TWISTED-HALFFIELD-NOTE-20261007-v2.2.md`: status lines from 1–20 (grep);
- verdict lines (grep) of `REVISION-CHECK-GX-v2`, `REVISION-CHECK-PTH-v2` and `DIFFCHECK-PTH-v2.1`.

**Not read:** HYP_CLOUD_RESULTS, 3PP_CLOUD_RESULTS, /root/.claude/uploads, and any scratchpad outside dz_isolated/. Git was not used.
