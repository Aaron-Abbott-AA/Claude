# Independent audit: HYP M>=2 round 19 (own-line correspondence route), owner note

7 October 2026. Claude, independent adversarial referee.

**Audited file:** `src/R19_CORRESPONDENCE_ROUTE_owner.md` (SHA-256 d24913db…a2fe3b, recorded in `checks/src_SHA256SUMS.txt`).

**Rules followed.**
- I read only files under `src/`. I wrote only under `checks/` and this file.
- I opened no file whose name contains "DZ" (none present).
- The owner scripts were copied to `checks/owner_copy/` and re-run there with `python3 -I`. All six `.out` files are byte-identical to the shipped ones.
- All other checks are my own scripts in `checks/` (`c0`–`c3`), using exact Fractions and galois 0.4.11 finite fields.

**Scale:** PASS / PASS-with-fixes / FAIL.

---

## 0. Verdict

**PASS-with-fixes.** No headline claim breaks. Every number in Cor. 4.2 is reproduced exactly. The thresholds are unchanged after the fixes. But the PROVED label on Thm 4.1 needs one missing step (FIX-1), and Lemma 1.1(i)/Lemma 1.5 need a corrected proof plus a small extra charge (FIX-2).

**What holds, conditional on the cited inputs:**
- Prop. 1.1, contact exactly E via FNAK.
- Prop. 1.2, the projective polynomial and Lang (for generic u).
- Lemma 1.4: (A) separability over u, (B) inseparability over v.
- Example 1.6 (Fermat σ1).
- Thm 2.1 and Cor. 2.2. I attempted a Frobenius-graph counterexample; it fails, and §3 below explains why.
- Lemma 3.0, Lemma 3.1 normal form, Cor. 3.2, Prop. 3.3 height, Prop. 3.4, Lemma 3.5.
- Inequality (4.1) **as stated**.
- Cor. 4.2: all τ_max values and all 𝔮-thresholds, re-derived independently, including every d' in [2E−2, 2E+4] and Q up to 2^19.

**Substantive fixes:**
- **FIX-1 (Thm 4.1, Step 3).** At a residual place v with p(v)=0, Π_1(u,v)=0 holds for **every** u, so "Π_1=0 ⇒ π=0" fails there. These places are exactly those where C_P and C_R vanish identically at z(v). They are not charged.
  - Repair: in the frame p=λp′, the factor λ is a regular section of degree a·d′−deg𝓟−ρ deg[T]. Hence deg𝓟+#Z(λ) ≤ a·d′.
  - The missing charge d·#Z(λ) is therefore absorbed by the existing p-term 2r(d−1)·a·d′, and (4.1) survives verbatim.
- **FIX-2 (Lemma 1.1(i), Lemma 1.5, Thm 4.1 Step 4).** In characteristic 2, the branch tangent at a singular branch is **not** in general the limit of nearby tangents. Explicit counterexample: (1,t²,t³) (c2(a)).
  - Lemma 1.1(i) is true for branches of multiplicity m(w)<E, by a different argument (given below). It is unproved for m(w)≥E.
  - Lemma 1.5's "multiplicity m(w)" for cuspidal w can then fail for one u per such w.
  - An extra term (d′−E)·⌊(2d′+2g−2)/(E−1)⌋ must be added to (4.1). This is negligible: no threshold changes (c1).

The other fixes are labels, overclaims and wording (FIX-3 to FIX-8).

---

## 1. Parameter constraints used

- q=Eh, E=rQS, T=QS, X=T/2, ρ=Q/2. Here r>=4, Q>=128, S>=64, all dyadic.
- Strip: 256E<=h<4QE, with n=h/E dyadic (so n<=2Q).
- M<16h/625, N=M−1−X<16h/625, M′=(M−1)/2, and a=M′+X−ρ−d′<8h/625−d′+X−ρ.
- d<=E+2, d′>=2E−2. Also d′<=deg C_f=2E+1, and d′−E<=d−1.
- 2g−2<=d(d−3), deg ψ<=(E+1)d, d_def<=q/1000, and the boundary charge is 6d_def+7.
- 128<=𝔮<=E (R18 Thm 4.2(i)–(iii), Cor. 5.5).
- G9: N_good>1551q/4000+1. Like the owner, I use the stricter test bound/q<1551/4000.
- |𝔈∖boundary|<=1.5d²+3.5d+1 (R16.4). This includes {g=0} (<=3d) and {D=0}.

---

## 2. Item table

| item | verdict | notes |
|---|---|---|
| Def. 1.0 | PASS-with-wording (FIX-6) | "bijection on points" holds only on normalisations: Γ′ has points of multiplicity >=E−3 at Bs(f) |
| Lemma 1.1(i) | **gap** (FIX-2) | Continuity argument invalid in char 2 at singular branches (c2(a)). True for m(w)<E by the (s−t)^E argument; open for m(w)>=E |
| Lemma 1.1(ii) | PASS | Used only generically (Lemma 1.4) |
| Prop. 1.1 (i),(ii) | PASS (minor wording N1) | FNAK dualises; ε_2 a power of 2; multiplicity of Δ′ is 1 |
| Prop. 1.2 | PASS for u with ℓ_u∩Bs(f)=∅ (N2) | Cofactor derivation correct; Lang correct; cross-ratios checked (c2(b)) |
| Lemma 1.4 (A),(B) | PASS | Both derivation arguments verified line by line |
| Lemma 1.5 | PASS for non-cuspidal w; **gap** for cuspidal w with m(w)>=E (FIX-2) | Count Σ(m−1)<=2d′+2g−2 correct |
| Example 1.6 | PASS | Identity checked by hand; owner script re-run |
| Thm 2.1 | PASS | Counterexample attempt with Frobenius graphs fails (§3.2) |
| Cor. 2.2 (i),(ii) | PASS | Identities B^tΩB=detB·Ω etc. checked exhaustively over GF(4) (c2(c)) |
| Lemma 3.0 | PASS | |
| Lemma 3.1 (+ reduction F∤(C_P,C_R)) | PASS | Reduction keeps ℓ_u∣G, FNAM2; (𝒦) is re-derived for the reduced pencil, not inherited |
| Cor. 3.2 | PASS | Requires 𝒞 normalised via the morphism z, not raw e(U) (FIX-1) |
| Prop. 3.3 | PASS (can be sharpened, N4) | Comparison numbers checked (c3) |
| Prop. 3.4 | PASS (the dichotomy) | "p regular off det T̂=0": p is regular everywhere in the correct frame (FIX-1) |
| Lemma 3.5 | PASS | (ii) checked exhaustively over GF(4)/GF(16) (c2(c)) |
| Thm 4.1 / (4.1) | **PASS-with-fixes** (FIX-1, FIX-2) | Inequality (4.1) holds as stated after FIX-1; FIX-2 adds a negligible term |
| Cor. 4.2 numbers | PASS (understatement, FIX-5) | All values reproduced exactly; d′ scan, Q up to 2^19, asymptotics |
| §5 Props 5.1/5.2 | label overclaim (FIX-4) | "gives no relation" / "cannot improve" are HEURISTIC |
| §0, §5 COMPUTED claims on monodromy | overclaim (FIX-3) | Transitivity shown only for E=8 (and by a combinatorial argument for E=16); not for E=32 |
| §5(b) "inseparable degree >=E over Γ_v" | unproved (FIX-3) | Lemma 1.4(B) gives only "inseparable" |
| Citations/status | FIX-7 | R18-T is now audited; §6.3 cites R18-T Prop. 2.2, whose (H_bs) never holds |

---

## 3. Detailed audit

### 3.1 §1: the correspondence

**Def. 1.0.**
- On the normalisations Γ̃×Γ̃′^{(1/E)}, the map y↦v (the inverse birational map composed with the E-th-power Frobenius twist) is a bijection on places. So (u,y)↦(u,v) is a bijection 𝒵′→𝒵 on points of the normalisations.
- Pointwise, v:=f(y^[E]) is undefined when y^[E] is a base point of f.
- Every proper base point q of f lies on Γ′ with multiplicity >=E−3 (R18-T audit FIX-1). So several places of Γ̃′ lie over q, and on the plane curves themselves the map is not a bijection.
- This is wording only (FIX-6), but it is the one place where the note's language suggests Γ′∩Bs(f)=∅.

**Lemma 1.1(i): proof gap (FIX-2).**
- The proof says that the branch tangent is "the limit of the tangents at nearby places". In characteristic 2 this is false for singular branches.
- *Counterexample (c2(a)).* Take the branch z(t)=(1,t²,t³), with generic order sequence (0,1,2).
  - z×z′=(t⁴,t²,0) tends to the line (0,1,0), which meets the branch with multiplicity 2.
  - The true branch tangent is (0,0,1), which meets the branch with multiplicity 3.
- **Correct argument, valid for all places w with m(w)<E.** Let v(s) be the branch of Γ at w and z(t) the branch of Γ′.
  - v(s)^[E]·z(s)=0 identically.
  - v(0)^[E]−v(t)^[E] is divisible by t^E.
  - Hence ℓ_w·z(t)=(v(0)^[E]−v(t)^[E])·z(t)=O(t^E), i.e. I_w(ℓ_w)>=E.
  - If m(w)<E, a line through z(0) with multiplicity >m(w) is the branch tangent. So ℓ_w is the tangent.
- For m(w)>=E the statement is unproved. For smooth branches (m=1), the note's continuity argument is also fine, since z×z′ at t=0 equals z_0×z_1≠0.
- *Effect.* Lemma 1.5 for non-cuspidal w is unaffected. Lemma 1.4 uses only the generic statement (ii). Prop. 1.1 uses only good u.

**Prop. 1.1.**
- (i) FNAK's proof is symmetric in points and lines, so the tangent line is projectively defined over K^{ε_2}.
- ε_2 is a power of 2 (Stöhr–Voloch p-adic criterion).
- If ε_2>=2E, both U_1/U_0 and U_2/U_0 lie in K², so K⊂K². That is impossible.
  - (N1: the note says "x=U_1/U_0∈K², which is false". One coordinate ratio alone may lie in K². Both together cannot.)
- Hence ε_2=E. The Stöhr–Voloch sum is correct: deg R=(1+E)(2g−2)+3d′, and j_i>=ε_i at every place.
- (ii) Δ′→Γ̃_u is purely inseparable of degree E, and the generic local intersection is j(u)=E. So Δ′ has multiplicity 1, and the residual degree over u is d′−E.
- Over y, 𝒵′ has degree d and Δ′ has degree 1 (it is a graph over Γ̃′^{(1/E)}). So the residual degree over y is d−1. Correct.

**Prop. 1.2.**
- The factorisation e∘ν_u=b(t)λ(t), with b cubic and λ linear, needs C_u=f(ℓ_u) to be a smooth conic through Bs(e). That holds iff ℓ_u avoids Bs(f), i.e. for all u outside <=3d points (N2).
- The cofactor argument is correct: H(s_u,t) has t-degree <=1 and is divisible by (t−t_u)^E=t^E−s_u, so it vanishes. The degree count is 3+E+(E+1)=2E+4.
- Lang's theorem gives fixed points g(P¹(F_E)).
- *c2(b).* For E=4 (GF(2^8)) and E=8 (GF(2^12)), random nondegenerate brackets with >=4 rational roots were tested: every 4-point cross-ratio lies in F_E (10/10 samples).
- The owner's degenerate E=32 sample ("contact 0") was traced in `c0`: the sampled point u is a **base point of e lying on Γ** (Bu=(1440,0,0)). It is not a defect of Prop. 1.2, but it illustrates that Bs(e)∩Γ≠∅.

**Lemma 1.4.**
- (A): the subfield L_s=L^{2^i}; the derivation D kills k(u); u·Dy=0; y∦Dy because y_0=1. Since D|_{k(y)}=φ·d/dx_y, the tangent of Γ′^{(1/E)} at the generic y is [f(y^[E])]=v. So u=v, a contradiction. Correct.
- (B) direct: δ kills E-th powers; u^[E] and v^[E] are both orthogonal to e(v) and δe(v); and e(v)×δe(v)≠0 because k(Γ′)⊄K². Correct.

**Lemma 1.5.**
- The non-cuspidal case is correct.
- Cuspidal case: "a non-tangent line has multiplicity exactly m" is true. But ℓ_u (u≠w) can be the true tangent of a cusp w only if ℓ_w is not that tangent. By the argument above this forces m(w)>=E.
- There are at most (2d′+2g−2)/(E−1) such w, and for each at most one u (Frobenius is injective), with excess <=d′−E.
- So Σ_uκ(u)<=d(2d′+2g−2)+(d′−E)⌊(2d′+2g−2)/(E−1)⌋.
- The count Σ(m−1)<=deg(z×dz)=2d′+2g−2 is correct.

**Example 1.6.**
- D_ζ∈(F_E^*)³ gives Φ_ζ(u)∈Γ.
- u^[E]·σ1(v)=v_0v_1v_2(1+ζ^{−1}+(1+ζ)ζ^{−1})=0.
- d′=2(E−1), because Fermat avoids the coordinate points, so d′−E=E−2.
- Each graph has degree 1 over u, so 𝒵′^res is the reduced union of the E−2 graphs. PROVED as claimed.

### 3.2 §2: invariance forces constancy

**Thm 2.1: correct.**
- Every component of 𝒵 dominates both factors. No vertical or horizontal components exist when e is read as the morphism Γ̃→Γ′; with raw e(V), Γ×{v_0} for v_0∈Bs(e)∩Γ would appear.
- k(𝒵_1)=k(Γ_u)k(Γ_v) is separable over k(h), with h=g_0(u)=g_0(v). So it is separable over k(Γ_v), contrary to Lemma 1.4(B).

**Counterexample attempt (Frobenius graphs), as requested.**
- On a component v=Φ(u)=D·u^[E] (Fermat), invariance g=g∘Φ gives g=((g∘D)^{(1/E)})^E∈K^E.
- With g=g_1^E, Frobenius injectivity gives g_1∘Φ=g_1, so g_1∈K^E as well. Iterating, g∈∩_mK^{E^m}=k.
- So purely inseparable composition does not create invariants; it is precisely what kills them.
- The general proof needs only that k(𝒵_1)/k(Γ_v) is inseparable while separating functions pull back separably. No irreducibility or monodromy is involved.
- The attempt also fails for "projective" invariance [T̂](u)=[T̂](v), because it reduces to ratios (Cor. 2.2(i)).

**Cor. 2.2(ii): correct.**
- k(𝒵_1)⊂L′ with L′/k(Γ_u) separable, so ψ(u)∉k(𝒵_1)². The degree of γ over F_0=L^{ρ𝔮} is 2ρ𝔮>=4.
- So M_11=M_22=0 and M_12=M_21, i.e. M=mΩ, and B(u)=(m/det B(v))B(v).
- Both identities, and the implication, were checked exhaustively over GF(4) (c2(c)).

### 3.3 §3: the kernel-aligned case

**Reduction.**
- If F divides every entry of C_P and C_R, (𝒦) holds trivially. The note correctly reruns R18-T's dichotomy on C/F^k: ℓ_u∤F, Δ/F^{2k}≢0, and a decreases.
- R18-T Lemma 3.2 and Prop. 3.3(a) are pencil-independent algebra, so they apply. Fine.

**Lemma 3.1.**
- 𝒞_P=0 implies 𝒞_RB=0, hence 𝒞_R=0. Both are nonzero.
- Rank one, and the rows are multiples of b_1^⊥.
- 𝒞_Pb_2=p_P det B and 𝒞_Rb_1=p_R det B, so p_P=p_R. Correct.

**Cor. 3.2.** 𝒞_c=p⊗(Bc)^⊥ gives c^[T,t]𝒞_cc^[Q]=(c^[T]·p)·det(Bc,c^[Q]). Substituting c^[Q]=κ_uB(u)c gives κ_uΠ_1Ξ. Correct (owner check (3) re-run).

**Normalisation (relevant to FIX-1).**
- 𝒞_•=C_•(z) must use the **morphism** z:Γ̃→Γ′, i.e. sections of z^*O(a), of degree a·d′. This is what Prop. 3.3 uses.
- With the raw polynomial e(U), 𝒞 and hence p vanish at every v∈Bs(e)∩Γ̃. Such points exist: see c0, and the R18-T audit, item g2.

**Prop. 3.3.**
- Row i of [𝒞_P|𝒞_R] equals p_i(T_11^ρ,T_21^ρ,T_12^ρ,T_22^ρ). So ρ·deg[T]<=a·d′. Correct.
- The comparison values are confirmed (c3): a<=1.3999E at h=256E (r=4); the ratio to the a-priori bound is 0.427; and the ratio tends to 1 as n grows (0.714 at n=512, 0.857 at n=1024).

**Prop. 3.4.** The dichotomy is correct. The sentence "Off det T̂=0, p is regular: its poles lie where a column of B has a common zero" is imprecise; see FIX-1. In the correct frame p is regular everywhere.

**Lemma 3.5.**
- (i) Ξ(u,·)=Σw_ic_jb̂_ij^{ρ𝔮}=σ_u^{ρ𝔮}. Correct (owner check (2)).
- (ii) The expansion argument is correct. The implication "det(B_*c,B_kc)≡0 with B_* invertible ⇒ B_k∝B_*" was verified exhaustively over GF(4), with c ranging over P¹(GF(16)): 720 vanishing pairs, 0 violations (c2(c)).
- (iii) σ_u is a nonzero section of degree τ_0 vanishing at u. Correct.
- Note: with p regular everywhere, the set W={det T̂=0} need not be removed in Thm 4.1 at all, because σ_u's zero count already covers W. The 2dτ_0 term is conservative.

### 3.4 §4: Theorem 4.1

**Step 1.**
- c^[T]=(β,α)^[X]. On 𝒵′, p′(v)=(p′^σ(y))^E, and E=2rX. So
      Π_1 = λ(v)·(β̃(u)^X p′_1(v) + α̃(u)^X p′_2(v)) = λ(v)·π(u,y)^X.
- deg π=(d′−E)deg ψ+(d−1)·2r·deg𝓟, using deg 𝓟^σ=deg 𝓟. Correct.

**Step 2.**
- π≡0 on a component gives ψ(u)∈L², contradicting Lemma 1.4(A) and R14.1. Correct.
- (N3: the parenthesis "p′^σ_2≡0 would force p≡0" is wrong as reasoning. If p′_2≡0 then π=β̃(u)p′^σ_1(y)^{2r}≢0 directly. Harmless.)

**Step 3: gap (FIX-1).**
- Write p=λp′ with p′ a section of 𝓟 without common zeros. Let w=(t̂_11,t̂_21,t̂_12,t̂_22)^{ρ𝔮} (no common zeros).
- Then [𝒞_P|𝒞_R]=λ·p′⊗w, so λ is a **regular** section of z^*O(a)⊗𝓟^{−1}⊗𝓣^{−ρ𝔮}.
- At a zero v of λ, i.e. a place where every entry of C_P and C_R vanishes at z(v):
  - Π_1(u,v)=0 and G_{c(u)}(z(v))=0 for **every** u;
  - but π(u,y_v)≠0 for generic u.
- So the step "at every remaining residual place Π_1=0, so π=0" fails at Z(λ), and the proof never removes these places. c2(d) illustrates this on random data (50/50).
- **Repair.**
  - #Z(λ)<=deg λ=a·d′−deg𝓟−ρ·deg[T].
  - Remove Res(u)∩Z(λ) in Step 3. This costs Σ_u<=d·#Z(λ).
  - Since d<=2r(d−1):
        2r(d−1)deg𝓟 + d·#Z(λ) <= 2r(d−1)(a·d′ − ρ·deg[T]) <= 2r(d−1)·a·d′.
  - So (4.1) holds as printed. It even improves by 2r(d−1)ρ·deg[T] (N4).

**Step 4: exceptional sets.**
- Charged, each with its source:
  - boundary 6d_def+7;
  - 𝔈, which includes {g=0}, Sing Γ, {D=0}, ramification and infinity;
  - {λ′=0}<=Nd;
  - {det T̂=0}<=2τ_0;
  - the 2deg ψ points of Lemma 3.5(ii);
  - FIX-N1's 3d, a harmless double count since 𝔈 already contains {g=0}.
- Residual places at base points of f are handled by κ(u) (multiple branches are distinct places) and need no g(v)≠0. Places in Bs(e)∩Γ̃ are handled by the z-normalisation. Missing are Z(λ) (FIX-1) and the cusp-tangent excess (FIX-2).
- With both, the corrected inequality is (4.1) + (d′−E)⌊(2d′+2g−2)/(E−1)⌋ on the right.

### 3.5 Cor. 4.2: numerics (c1, exact Fractions, independent code)

**Reproduction.**
- Every owner τ_max/E and every 𝔮-threshold in both owner outputs is reproduced exactly.
- I scanned **every** integer d′∈[2E−2,2E+4] (the owner used only 2E−2, 2E, 2E+4). The minimum is always at d′=2E−2, so the owner's choice is not optimistic.
- Adding the FIX-2 term changes no printed digit and no threshold.
- I also used a per-d′ exact threshold test (a(d′)d′/(ρ𝔮)<=τ_max(d′) for every admissible d′<=2E+1). It gives the same least 𝔮 as the owner's conservative test in every row.

**Grid.** r∈{4,8,16,32}, Q∈{128,…,4096,16384}, S∈{64,256}, dyadic n∈[256,2Q]: 232 rows.

**r=4.**
- 𝔮>=E/4 suffices in all 58 rows, including n=2Q up to Q=16384.
- 𝔮>=nE/(8Q) suffices for every n>=512 (0 failures).
- *Asymptotics (Part C).* At n=2Q and 𝔮=E/4:
  - the (𝒦)-height/E increases to 256/625=0.40960;
  - τ_max/E decreases to 1−0.2048/(1551/4000−0.0316)=0.42496;
  - at Q=2^19 the values are 0.40954 against 0.42503.
- The claim "𝔮>=E/4 throughout the strip" therefore holds with a uniform margin ≈0.015E.

**r=8.**
- n=256 gives nE/(16Q) and n=512 gives nE/(4Q). Both are confirmed up to Q=16384.
- τ_max=0.0022E at n=1024. "Fails at n>=1024" means that no 𝔮<=E suffices; τ_max is not 0 there (N5). From n=2048 on, τ_max=0.

**r=16.** Only n=256 closes:
- Q=512 with 𝔮=E (omitted by the note; 𝔮=E is admissible);
- Q=1024: E/2; Q=2048: E/4; Q=4096: E/8; Q=16384: E/32.

So "only n=256 with Q>=1024 (𝔮>=E/2)" understates (FIX-5).

**r=32.** Never closes.

**Dominant-term remark.** The p-term/q is 0.0875 at r=4, n=256 and tends to 0.0512r as n grows (c3). Correct.

### 3.6 §5 and labels

- Prop. 5.1(i): "it gives no relation between B(u) and B(v)" is not a mathematical statement. Prop. 5.2's "every section … has per-point cost >=…" is explicitly heuristic. Yet §0 (R1) calls it "PROVED as a cost statement". Only 5.1(ii) (the degree count) is PROVED (FIX-4).
- §5(b), "𝒵^res has inseparable degree >=E over Γ_v": Lemma 1.4(B) proves only that it is inseparable.
  - With L=k(𝒵′_1)⊃k(𝒵_1), the inseparable degree is E/[L:k(𝒵_1)] when L/k(y) is separable. [L:k(𝒵_1)] is not controlled.
  - If L/k(y) is inseparable, the same derivation argument shows that y would be the tangent of Γ at u, which is not excluded.
  - Exactly E holds in the Fermat case (FIX-3).
- Transitivity of arithmetic monodromy (§0, §5(b)). I checked which orbit partitions are compatible with the cycle types in `corr_random.out` (c2(e)):
  - E=8: the pattern 9 (irreducible) proves it.
  - E=16: the three patterns admit no intransitive orbit partition, so transitivity also follows, by an argument the note does not give.
  - E=32: the orbit partition 30+3 is compatible with all three cycle types, so transitivity is **not** established.
  - Correct the claim to "E=8 (and E=16)" (FIX-3).

---

## 4. Fixes

**FIX-1 (substantive; Thm 4.1 Step 3, Prop. 3.4 last sentence, Step 1 "p′").**
- *Problem.* At residual places v with p(v)=0, i.e. C_P(z(v))=C_R(z(v))=0, Π_1(u,v)=0 for every u, but π(u,y_v)≢0. The implication Π_1=0⇒π=0 needs λ(v)≠0, and these places are not removed.
  - If 𝒞 were normalised with raw e(U), every v∈Bs(e)∩Γ̃ would be such a place.
- *Correction.*
  1. State that 𝒞_• is formed with the morphism z:Γ̃→Γ′, i.e. sections of z^*O(a).
  2. Write p=λp′. Then λ is a regular section of z^*O(a)⊗𝓟^{−1}⊗𝓣^{−ρ𝔮}, so deg𝓟+#Z(λ)<=a·d′−ρ·deg[T].
  3. In Step 3, also remove Res(u)∩Z(λ). In Step 4 add Σ_u|Res(u)∩Z(λ)|<=d·#Z(λ).
  4. Note that 2r(d−1)deg𝓟+d#Z(λ)<=2r(d−1)a·d′, so (4.1) is unchanged.
  5. Replace "Off det T̂=0, p is regular" by "p=λp′ is regular everywhere".

**FIX-2 (substantive; Lemma 1.1(i), Lemma 1.5, Thm 4.1 Step 4).**
- *Problem.* The continuity proof is invalid at singular branches in characteristic 2. Counterexample: (1,t²,t³).
- *Correction.*
  1. Prove Lemma 1.1(i) via I_w(ℓ_w)>=E, from (v(0)^[E]−v(t)^[E])·z(t)=O(t^E), for branches with m(w)<E. Mark m(w)>=E as open.
  2. In Lemma 1.5, add "(cuspidal, and ℓ_u not the branch tangent; the latter can fail only if m(w)>=E, for at most one u per w)".
  3. In (4.1), add (d′−E)⌊(2d′+2g−2)/(E−1)⌋ to the right-hand side. All Cor. 4.2 numbers are unchanged (c1, column "with FIX-2").

**FIX-3 (overclaims, COMPUTED/structure).**
- (a) Replace "so the arithmetic monodromy is transitive" (§0, §5(b)) by "transitive for E=8 (an irreducible specialisation) and E=16 (cycle-type combinatorics); not decided for E=32".
- (b) Replace "𝒵^res has inseparable degree >=E over Γ_v" by "is inseparable over Γ_v (Lemma 1.4(B)); the inseparable degree is E in the Fermat example".

**FIX-4 (labels, §0 (R1), §5, §8).**
- Prop. 5.1(i) and the "no B(u)–B(v) relation" sentence → HEURISTIC.
- Keep Prop. 5.1(ii) as PROVED.
- In §0 (R1), replace "PROVED as a cost statement" by "the degree counts are PROVED; the claim that the route cannot improve the cost is HEURISTIC".

**FIX-5 (Cor. 4.2 statements: understatements and imprecision).**
- r=16: "n=256 only; 𝔮>=512E/Q for Q>=512 (E at Q=512, E/2 at 1024, …, E/32 at 16384)".
- r=8: "τ_max≈0.002E at n=1024 (no 𝔮<=E suffices), 0 for n>=2048", in place of "fails at n>=1024".
- The table rows and the "nE/(8Q) in general" statement were checked only on the owner's grid. They are now verified up to Q=16384, and at n=2Q up to Q=2^19 with the limit 0.4096<0.42496. Cite the margin.

**FIX-6 (wording on base points, Def. 1.0 and Prop. 1.2).**
- "Bijection 𝒵′→𝒵 on points" → "on points of the normalisations; v=f(y^[E]) is the birational map extended to Γ̃′, undefined pointwise at Γ′∩Bs(f), where Γ′ has multiplicity >=E−3".
- Prop. 1.2: add "for u with ℓ_u∩Bs(f)=∅ (all but <=3d points)".

**FIX-7 (citations).**
- R18-T is now audited (PASS-with-fixes), so update the header line "owner draft under audit".
- §6 item 3 cites "polynomial-origin situations (R18-T Prop. 2.2)". By the R18-T audit FIX-1, (H_bs) never holds; cite (H_lift) (OPEN) instead.

**FIX-8 (owner script note).**
- §7 says "one degenerate sample at E=32". c0 shows that this u is a base point of e on Γ. Say so; it is evidence for Bs(e)∩Γ≠∅, which is relevant to FIX-1.
- `corr_fermat.out` reports "symmetry … 0/0": that test never ran. Delete it or report it as "not exercised".

---

## 5. Minor notes

- **N1.** Prop. 1.1(i): "x=U_1/U_0∈K², which is false". Use both ratios (K⊂K²).
- **N2.** Prop. 1.2: generic-u hypothesis (FIX-6). The degenerate case αδ=βγ is not analysed; it is not used.
- **N3.** Thm 4.1 Step 2: correct the parenthetical reasoning (§3.4).
- **N4 (optional strengthening).** FIX-1's identity gives deg𝓟<=a·d′−ρ deg[T], which strengthens both Prop. 3.3 and the p-term of (4.1) by 2r(d−1)ρ·deg[T]. The owner may use it.
- **N5.** Cor. 4.2 wording for r=8, n=1024 (FIX-5).
- **N6.** §0, item 1: "Every non-diagonal component of 𝒵⊂Γ×Γ is inseparable over Γ_v; in 𝒵′, the v-functions are E-th powers". This is correct. Do not upgrade it to "inseparable degree E" (FIX-3b).
- **N7.** The 3d of FIX-N1 is double-counted inside 𝔈. That is harmless.
- **N8.** The comment headers of the owner scripts say "Theorem 4.4 of NOTE_CORRESPONDENCE_ROUTE.md" and "Prop 4.2" (they should say Thm 4.1 and Prop. 3.3).

---

## 6. Files in `checks/`

- `src_SHA256SUMS.txt`: hashes of `src/` (pre-existing).
- `owner_copy/`: the owner scripts, re-run with `python3 -I`. All six outputs are byte-identical to `src/r19_scripts/*.out`.
- `c0_corr_random_debug.py` → `.out`: the owner's random-centre script with one diagnostic line added. The degenerate E=32 sample is u∈Bs(e)∩Γ.
- `c1_numerics.py` → `.out`: independent exact-Fraction evaluation of (4.1).
  - every d′∈[2E−2,2E+4];
  - the FIX-2 term;
  - per-d′ exact 𝔮-thresholds;
  - the grid r∈{4,8,16,32}, Q<=16384;
  - the r=4 claims (E/4; nE/(8Q));
  - asymptotics at n=2Q up to Q=2^19.
- `c2_algebra.py` → `.out`:
  - (a) the char-2 cusp counterexample to the continuity argument of Lemma 1.1(i);
  - (b) Lang/Möbius check of Prop. 1.2 via cross-ratios;
  - (c) exhaustive GF(4) checks of B^tΩB=det B·Ω, Cor. 2.2(ii) and Lemma 3.5(ii);
  - (d) the FIX-1 phenomenon;
  - (e) orbit-partition test for monodromy transitivity.
- `c3_prop33_comparison.py` → `.out`: Prop. 3.3 comparison numbers and the 0.0512r dominant-term remark.
- `checks_SHA256SUMS.txt`: hashes of all files above.
