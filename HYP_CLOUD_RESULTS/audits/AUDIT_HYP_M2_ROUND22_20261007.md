# Audit of HYP M>=2 round 22 (owner v1): vector own-line identity, constant twists outside (𝒦), (R1) at 𝔮>S

7 October 2026. Independent adversarial referee audit of `src/HYP_M2_ROUND22_owner_v1.md` (sha256 `91e5997c…cc70`, matches `checks/src_SHA256SUMS.txt`).

**Rules kept.**
- I read only under `src/` and wrote only under `checks/` and this file.
- I opened no file whose name contains "DZ". The PRIMARY TSY/TSYC copies mention DZ only in their bodies and credit lines.
- I copied the owner scripts to `checks/owner_copy/` and ran them with `python3 -I`, one process at a time. All three outputs are byte-identical.
- My own checks use `galois` and `fractions` and not the owner's `gf2k` helper. They were run with `python3 -I`, one at a time, the longest in 108 s.

---

## §0 Verdict: **PASS-with-fixes**

I found **no mathematical error in any headline result.** I re-derived every main statement by hand. Thm 3.1 I also re-derived by a second, shorter route, which gives a slightly sharper exact form. Every statement was then tested with independent exact computations designed to break it. All six statements the coordinator asked about **survive**:

| item | survives? | how checked |
|---|---|---|
| Prop. 2.3 (★) | **yes**, exactly as printed | hand re-derivation from R16.1 + alignment + FNAL/TSY + R18-T 2.1(i) + TSYC; exact toy with a *fully general* second layer S, mod t^K (`thm31_toy_indep`) |
| Lemma 2.2 (e_u∈{E,E+1}) | **yes**; compatible with R19 Prop. 1.1 (see §2.2) | hand proof checked, plus a second shorter proof (line method); 29 705 points on 2 Fermat + 13 random-centre runs over GF(2^8/10/12), 1 223 full Hensel and line-order computations, all consistent; 463 points with e_u=E+1 (13 of them on random centres) |
| Thm 3.1 (order ≥X−ρ, congruence mod t^X; regularity ord s̃≥e−X) | **yes** | second independent proof (§2.4); toy: 6 constant + 11 non-constant cases; the gap cases e−X−ρ<=ord s̃<e−X are unsolvable *with* alignment and solvable *without* it |
| Cor. 4.1 (constant, not (𝒦): excluded, all D, all n) | **yes** | every step re-derived; exceptional sets and multiplicities re-charged; numbers recomputed (max 0.0460944) |
| Cor. 4.2 ((𝒦): excluded unless F²\|a_P, F²\|a_R) | **yes** | re-derived; max 0.0929718 |
| Thm 5.3 ((R1) and (𝒦_ψ)∖(𝒦) excluded at 𝔮>S) | **yes** | Lemma 5.1(a), Lemma 5.2 and R21 Lemma 3.2/Remark 3.4 re-derived; max 0.1477030 and 0.1043053 |

**The fixes do not change any closure.** The two substantive fixes are both overclaims of what a statement shows:
- **FIX-1:** the "precise negative result (PROVED)" of Remark 4.4 is labelled stronger than its proof supports.
- **FIX-2:** the justification for "F²|a is invisible on C̃" (Prop. 4.3) is wrong as written, although the conclusion survives in its correct direction.

The remaining fixes concern:
- a false remark after Prop. 2.3 (FIX-3);
- a novelty overclaim for Cor. 3.2 (FIX-4);
- a citation of a step inside a CONDITIONAL proposition (FIX-5);
- "≤" bounds printed below their exact values (FIX-6);
- an internal inconsistency in §6 about Prop. 5.5 (FIX-7);
- toy wording and coverage (FIX-8).

---

## §1 Item table

| item | owner label | referee finding | referee label |
|---|---|---|---|
| Lemma 2.1 (i)–(iii) | PROVED | correct; (ii) and (iii) verified exactly in the toy (`lem21`, `tsy`) | PROVED |
| Lemma 2.2 | PROVED; COMPUTED | correct. The hypothesis "Γ smooth at u" is not needed for e_u<=E+1 (N1). Holds on random centres too | PROVED; COMPUTED (extended) |
| Prop. 2.3 (★) | PROVED; COMPUTED | correct as printed, for every c∈k². The **remark after it is wrong** (FIX-3) | PROVED (remark: fix) |
| FNAL "forgets the span(f^[X]) component" | (attribution) | accurate. FNAL §4 says verbatim "Taking a determinant forgets a component in span(f^[X])". FNAL1 is det(u^[X],f^[X],P_c^tu^[ρ])=0; (★)'s second scalar is the forgotten one | — |
| Lemma 2.4 | PROVED | correct; (iv) should be proved locally rather than cited (FIX-5) | PROVED |
| Thm 3.1 (i)–(iv) | PROVED; COMPUTED | correct; holds in a sharper **exact** form (N2) | PROVED; COMPUTED (independent) |
| Cor. 3.2 | PROVED | correct; but the first bullet already follows from R16.2 + R19 Lemma 3.5 (FIX-4) | PROVED (novelty claim: fix) |
| Cor. 4.1 | PROVED; COMPUTED | correct; numbers reproduced | PROVED; COMPUTED |
| Cor. 4.2 | PROVED; COMPUTED | correct; numbers reproduced | PROVED; COMPUTED |
| Prop. 4.3 (i)–(iv) | PROVED (necessary) | (i)–(iv) correct. The "invisible on C̃" justification is wrong as written, and "every C̃ is still possible" is an overclaim (FIX-2) | PROVED (i)–(iv); justification: fix |
| Remark 4.4 negative result | PROVED | the decomposition is right (I re-derived the consistency of the J-part). The claim that the remaining condition carries no (C,a)-information is not proved (FIX-1) | PROVED (decomposition) + HEURISTIC (non-determination) |
| Remark 4.5 | PROVED statement | correct (re-derived) | PROVED |
| Remark 4.6 | PROVED/HEURISTIC | correct as labelled | as labelled |
| Lemma 5.1 | PROVED | correct | PROVED |
| Lemma 5.2 | PROVED | correct (Riemann–Hurwitz with wild ramification handled by ord_P(Diff)>=e_P−1) | PROVED |
| Thm 5.3 | PROVED; COMPUTED | correct; two "≤" decimals are below the exact values (FIX-6) | PROVED; COMPUTED |
| Cor. 5.4 | PROVED | correct; thresholds 0.240047q and 0.283445q | PROVED |
| Prop. 5.5 | CONDITIONAL / pencil PROVED | correct; the pencil case is unconditional and also applies in (𝒦), which §6 omits (FIX-7) | as labelled |
| Remark 5.6 | PROVED; HEURISTIC impact | correct | as labelled |
| §6 residual list | — | the (R2) line understates Prop. 5.5 (FIX-7); the rest is consistent | — |
| §7 toys | COMPUTED | reproduced byte-identically; coverage caveats (FIX-8) | COMPUTED |

---

## §2 Detailed audit

### 2.1 Prop. 2.3 (★), and the FNAL attribution

I re-derived (★) line by line. In characteristic 2, gu=f(Y)+tω gives g^ρu^[ρ]=f^[ρ]+t^ρω^[ρ] and g^Xu^[X]=f^[X]+t^Xω^[X].
- Global alignment gives g^ρP_c^tu^[ρ]=a_cf^[X]+t^ρW, with W:=P_c^tω^[ρ].
- Crossing with g^Xu^[X] and using f^[X]×f^[X]=0 gives t^Xa_c(f×ω)^[X]+t^ρf^[X]×W+t^{ρ+X}W×ω^[X].
- R18-T 2.1(i) with exponent 1 and TSYC (J(Y(t))^tω(t)=b for all t) give (f×ω)^[X]=κ_0^XJ^[X]Ωb^[X].
- FNAL+TSY give f^[X]×W=F·J^[X]C_c(J^tω)^[ρ]=F·J^[X]C_cb^[ρ].

So (★) holds exactly as printed, as a polynomial identity in t and for every c. R16.1 makes the left side 0 at c=c(u)=(√β:√α)(u), with the same V=u^[E]×c_0 and D≠0.

**FNAL text.**
- FNAL §2 takes "its determinant with f(Y(t))^[X] and u^[X]", i.e. the scalar det(u^[X],f^[X],P_c^tu^[ρ]).
- FNAL §4 states "Taking a determinant forgets a component in span(f^[X])".
- Since f^[X]=g^Xu^[X]+t^Xω^[X], FNAL1 says only P_c^tu^[ρ]∈span(u^[X],f^[X]), while R16.1 says P_c^tu^[ρ]∈span(u^[X]).

The note's description ("drops a component", "the span(f^[X]) component") is therefore accurate.

**COMPUTED** (`thm31_toy_indep.out`). (★) holds mod t^K in all 34 random aligned samples, for constant and non-constant first layers. It also holds on all 78 sampled FN solutions (13 solvable cases × 6). The toy uses a **general** 3×3 second layer S and recovers C from H=[f^[X]]_×S=J^[X]CJ^[ρ,t] by unit minors; the full factorisation is verified each time.

**The remark after Prop. 2.3 is false (FIX-3).**
- Dotting with u^[X] gives nothing: the left side of (★) is ⊥u^[X], and the right side·u^[X] vanishes identically (two equal terms t^{X+ρ}g^{−X}F·b^{[X],t}C_cb^[ρ] cancel).
- Dotting with ω^[X] gives t^ρ·F·b^{[X],t}C_cb^[ρ], not t^{ρ+X}·F·b^{[X],t}C_cb^[ρ].
- COMPUTED: `dot_uX_rhs_zero` is True in every case; `dot_omX_is_t^rho_F_bCb` is True and `…t^(rho+X)…` is False in every case.

The conclusion of the remark (the ω^[X]-component is FNAL2/TSYC; one further scalar is new) is unaffected.

### 2.2 Lemma 2.2, and reconciliation with R19 Prop. 1.1 / R20

**The proof is correct.**
- u^[E]·e(v)=(u+v)^[E]·e(v) on Γ, and (u+v(s))^[E]=Σ_{k>=1}s^{kE}y_k^[E]. Hence u^[E]·e(v(s))=s^E·y_1^[E]·e(v(s))+O(s^{2E}).
- If y_1^[E]·e(u)≠0, then e_u=E.
- Otherwise {y_1^[E]·Y=0} is a line through the smooth point z(u) that differs from the tangent ℓ_u, because y_1∦u in an affine lift. It therefore meets Γ' with multiplicity exactly 1, so e_u=E+1<2E.
- The criterion is independent of the lift: y_1↦ay_1+bu multiplies it by a^E.

**N1: a shorter proof, with fewer hypotheses.**
- With w:=df_z(V), the expansion is f(z+tV)^[E]=g^Eu^[E]+t^Ew^[E]+t^{2E}w_2^[E].
- Hence C_f(z+tV)=t^E(z·w^[E])+t^{E+1}(V·w^[E])+O(t^{2E}), where C_f(Y)=Y·f(Y)^[E]=F·C'.
- If both coefficients vanished, w^[E] would be ⊥z,V, so w∥u, which contradicts projective étaleness of f at z (V∦z).
- So e_u<=ord_tC_f(z+tV)<=E+1, needing only g(u)≠0, V non-radial and étaleness, not smoothness of Γ at u.
- The criterion z·w^[E]=0 coincides with the owner's y_1^[E]·e(u)=0, since w≡ay_1 (mod u) by the order-E osculation of Γ and f(ℓ_u) (R16 Lemma 1.1).

**Reconciliation with R19 Prop. 1.1.** There is no conflict.
- R19 Prop. 1.1 says j(u)>=E at every place, j(u)=E for all but finitely many u, and Σ_u(j(u)−E)<=(E+1)(2g−2)+3d'.
- Lemma 2.2 adds a **pointwise upper bound at good places**: the excess j(u)−E is 0 or 1. The excess 1 occurs exactly on the zero set of the lift-invariant quantity y_1^[E]·e(u), which is finite by R19. That set is charged by R19's sum, which itself is unchanged.
- An excess >=2 can only occur at non-good places: singular branches, ramification of e, g=0, or Bs(e).
- In R19 Prop. 1.2's conic parameter, e_u=E+1 means the residual factor (αt+β)t^E+(γt+δ) has a simple root at t_u, i.e. one residual point collides with u. This is exactly R20's "j(u)=E+1 on the special clusters" (294/294 in the R20 revision check).

**COMPUTED** (`lemma22_contact.out`). Random paired centres e(U)=LU×NU over GF(2^8) (E=8,16,32), GF(2^10) (E=8,16) and GF(2^12) (E=8,16), plus the σ1 control. I enumerated all affine points and kept the 29 705 points that are smooth, have g≠0 and non-radial V. Four criteria were compared:
- (A) branch order by Hensel;
- (B) line order ord_tC_f(z+tV), an exact polynomial;
- (C) the owner's criterion;
- (D) the referee's z·w^[E] criterion.

Results:
- (C) and (D) agree at **all** 29 705 points.
- (A)=(B)∈{E,E+1} and (E+1 ⟺ (C)) at all 1 223 fully computed points. These are all 463 predicted E+1 points plus samples.
- The σ1 control reproduces the owner's 450 E+1 points at E=16 over GF(2^12).
- 13 E+1 points occur on random centres, which the owner's Fermat-only check did not cover.

### 2.3 Lemma 2.4 and the zero-top input

Lemma 2.4(i) is correct. More simply, at a good z, row_k(P^t)/f_k(Y)^X with u_k≠0 is itself a lift of κ^Y in O_{P²,z}, and any two lifts differ by F·(…).

For (iv), F|a_•, the note cites R18-T Prop. 2.2 Step 3. That step sits inside a proposition that is CONDITIONAL on (H_lift), although its own argument is local and unconditional. **FIX-5:** state the two-line local proof instead:
- on Γ' off Bs(f), P^t=f^[X]⊗κ with κ·f^[ρ]=g^{ρ−X}ϰ_P·U^[ρ]=0 (zero top);
- so a_Pf^[X]=0 on Γ', hence F|a_P.

I checked this; the conclusion stands.

### 2.4 Thm 3.1: re-derivation and a second proof

**The owner's proof is correct.**
- Steps 1–3: divide (★) by F≠0 in k((t)), then apply Cramer's rule on a unit 2×2 minor of J^[X](Y(t)), using J(z) of rank 2 since its minors are ∝gu.
- Step 4 is the graph argument at a smooth z, with ℓ_u tangent and contact e_u.

**Second proof (referee).**
- Write P_c^t=f^[X]⊗κ̃_c+F S_c with S_c regular (Lemma 2.4).
- Put σ:=κ̃_c·u^[ρ]. Since J^tu=(t/g)b, σ=(t/g)^ρ s̃_u.
- FN then reads (S_cu^[ρ]+(σ/F)f^[X])×u^[X]=0. So S_cu^[ρ]=θω^[X]+μu^[X], with θ=σt^X/F and μ∈k[[t]].
- Alignment gives S_cf^[ρ]=a'_cf^[X], hence g^ρS_cu^[ρ]=a'_cf^[X]+t^ρS_cω^[ρ].
- Apply J^{[X],t}, which kills f^[X], and use J^{[X],t}S_c=κ_0^{−X}ΩC_cJ^{[ρ],t}. This gives, **exactly** (not only mod t^X):

      C_c(Y(t))b^[ρ] = κ_0^X·( t^{X−ρ}μ̂ + t^X s̃_u/F )·Ωb^[X],   μ̂:=g^{ρ−X}μ ≡ a'_c (mod t^ρ).      (†)

Consequences of (†):
- Regularity of the left side forces ord θ>=ρ, i.e. ord s̃_u>=e_u−X, which is Thm 3.1(i).
- Reduced mod t^X, (†) is Thm 3.1(ii).
- For a constant twist s̃_u≡0, which gives (iv).
- (†) also shows that V_u|_{ℓ_u} is everywhere a scalar multiple of the constant vector Ωb^[X]∝(c^[T])^⊥, consistent with R21 Lemma 3.1 (N2).
- The proof shows where the "+ρ" comes from: FN together with common image alone gives only ord s̃_u>=e_u−X−ρ (the R16.2 level), and the alignment identity supplies the remaining ρ.

**COMPUTED** (`thm31_toy_indep.out`; GF(2^8), general S, F=t^e·unit).

Constant layer, 6 cases (ρ,X)∈{(1,4),(2,4),(2,8),(4,8),(4,16),(8,16)}:
- FN is solvable;
- every sampled solution has ord C_cb^[ρ]=X−ρ **exactly**, so the bound is attained;
- the congruence (ii) holds;
- (†) holds mod t^{K−ρ−2}.

Non-constant layer, 11 cases:
- all 4 "gap" cases e−X−ρ<=ord s̃<e−X are FN-**unsolvable** although the FN equation has no pole;
- the same 4 cases become **solvable when alignment is dropped** (control `main2`);
- all 7 cases with ord s̃>=e−X are solvable, with order exactly min(X−ρ, X+ord s̃−e), and (ii) and (†) hold.

The owner's control (C) contained only one unsolvable case, (ρ,X,e,ν)=(1,4,7,1), which is the trivial pole case ord σ+X<e. So it did not test the non-trivial part of "solvable iff ord s̃>=e−X" (FIX-8).

### 2.5 Cor. 3.2 and Lemma 5.1

Both are correct.
- ν_u∈ρ𝔮·Z_{>=1}∪{∞}, since Ξ(u,·)=σ_u^{ρ𝔮} and Ξ(u,u)=0.
- Thm 3.1(i) gives ν_u>=e_u−X when ν_u<e_u.
- In Lemma 5.1(a), the least multiple of ρ𝔮=2^kX (k>=1) that is >=(2r−1)X is >=2rX=E, also when 2^k>2r. Hence δ_u>=X−1>=X−ρ.

**FIX-4 (novelty overclaim).** "Before this note only σ_u(u)=0 was known" and "This is new information on the twist itself" overstate the novelty.
- R16.2 alone, combined with TSYC's J(Y(t))^tu=(t/g)b transported to Γ by the graph argument, gives ϰ_c(y)·u^[ρ]=unit·t^ρ·c^t𝒜(y)c^[Q]+O(s^{ρE}). Hence ν_u+ρ>=E−X.
- Because ν_u is a multiple of ρ𝔮, this already gives ν_u>=E−X when 𝔮<=S, and ν_u>=E when 𝔮>S.
- So the first bullet of Cor. 3.2, and therefore Prop. 5.5 and Remark 5.6, were derivable from R16.2 + R19 Lemma 3.5.
- What is genuinely new is the extra +ρ, which matters only for the e_u=E+1 refinements (Cor. 3.2 second bullet; Lemma 5.1(b) with e_u=E+1), and above all the C-layer order (Thm 3.1(ii)–(iv)). Thm 5.3 really does need the latter.
- The toy control above confirms the split exactly: without alignment, FN admits ord s̃=e−X−ρ.

### 2.6 Cor. 4.1: attempt to break it

I attacked each ingredient in turn.

1. **Slopes.**
   - Constant 𝒜 means CMIX with constant A (R18-T Lemma 1.1, with the scalar absorbed into λ').
   - The good slopes lie among the <=Q+1 roots of c^tAc^[Q]=0, and c^[Q]∝Bc there (FNAO §2, valid pointwise off {λ'=0}).
   - So 𝒱_c=C_c(Y)c^[Q]∝C_c(Y)Bc is fixed per slope.
2. **Exceptional slopes.**
   - Outside (𝒦), c↦C_c(Y)Bc mod F is a nonzero binary quadratic form with coefficients in the domain S/F. It has at most 2 projective roots, even over Frac(S/F).
   - The good points of one slope lie in a single ψ-fibre (ψ(u)=c_2²/c_1², including 0 and ∞), of size <=(E+1)d.
   - Charge: 2(E+1)d. Correct.
3. **Non-exceptional slopes.**
   - Fix one component G with F∤G. Thm 3.1(iv) gives ord_t G(z+tV)>=X−ρ at each good u of that slope.
   - The graph argument at the smooth z(u) with contact e_u>=E>X−ρ gives order >=X−ρ on Γ'.
   - Distinct good u are distinct places, and e is a local isomorphism.
   - z^*G≢0 has degree a·d', formed with the **morphism** z; base points of e or f on Γ̃ only add zeros and cannot invalidate an upper bound.
   - So #{u: c(u)=c}<=ad'/(X−ρ). This holds even when a<X−ρ (then ℓ_u|G, and the count on Γ' is still valid).
4. **Every good point is accounted for.**
   - A good point has a slope, which is either exceptional (fibre charge) or not (zero of z^*G).
   - The non-good points are {λ'=0} (Nd), 𝔈 (1.5d²+3.5d+1, containing {g=0}, {D=0}, Sing Γ, ramification and infinity), and the boundary (6d_def+7, containing Bs(e)).
   - {det T̂=0} is empty for a constant twist.
   - Nothing is double-credited, and no point is deleted without charge.
5. **Inputs actually used.** R16.1, Lemma 2.4 (common image), alignment and zero top, FNAL/TSY/FNAM1, TSYC/FNAM3, FNAO §2, FNAN §1 and R16.4. P_D≢0, FNAM2, FNAP and G5 are indeed not used, as the note claims.

I could not break Cor. 4.1. Its consequences are also correct: R21 Cor. 2.2 is superseded outside (𝒦), 𝔉_D∩{F∤h} is closed (R21 Prop. 2.3(i)), and the constant D>=4 lanes outside (𝒦) are closed for every n in the strip.

A consistency check is also satisfied. R21 Cor. 3.3's scenario "𝔡(u)≠0 at good u" is now impossible for constant twists, since Thm 3.1(iv) forces 𝔡(u)=0. Through R21 Lemma 3.2(iii) this gives a second, weaker exclusion route (𝔡≢0 ⇒ <=0.148q).

### 2.7 Cor. 4.2, Prop. 4.3, Remarks 4.4–4.6

**Cor. 4.2 is correct.**
- In (𝒦), F|C_cBc, so the left side of (ii) is O(t^{e_u}) with e_u>=E>X. Hence t^{X−ρ}a'_c≡0 (mod t^X), so a'_c=O(t^ρ) on ℓ_u, hence on Γ'.
- a'_c is linear in c, so there is at most one exceptional slope unless F|a'_P and F|a'_R.
- Each other slope has <=deg a'·d'/ρ good points.

Prop. 4.3(i)–(iv) are correct necessary conditions. For (iv): deg a=M'+Q−T<2d' together with F²|a forces a=0.

**FIX-2.** The claim that F²|a "is not visible on C̃" is justified by "P^t↦P^t+f^[X]⊗η with η arbitrary (not a syzygy) leaves C unchanged and changes a by η·f^[ρ]", citing R18-T Prop. 2.4. This is wrong as stated.
- For non-syzygy η this change breaks zero top unless F|η·f^[ρ].
- It changes the first layer, and hence the (constant) twist, unless η|_{Γ'}=0.
- R18-T Prop. 2.4 concerns syzygies only.

The correct modification is the one in Remark 4.6, η=Fξ. It keeps C, the first layer and zero top, and changes a'↦a'+ξ·f^[ρ]. So F²|a can be destroyed without changing C̃, which means F²|a is not implied by C̃.

The converse is not shown: that F²|a can be *achieved* for a given C̃ needs a'∈(F)+I_ρ. So "every C̃ is still possible at the C-level" should read "Thm 3.1/Cor. 4.2 impose no further condition on C̃".

**FIX-1 (Remark 4.4).** I re-derived the decomposition:
- FN at u ⟺ (γ);
- (γ) is solvable for y∈k[[t]]³ iff (α) and (β) hold;
- the J-part of the solution is automatically consistent. Dotting t^X·(γ) with u^[X] gives b^{[X],t}ΩJ^{[X],t}y=κ_0^{−X}b^{[X],t}C_cb^[ρ], and the functional b^{[X],t}Ω has kernel spanned by b^[X].

So FN at u ⟺ (α)∧(β)∧(one scalar condition per order on the f^[X]-component of y_u). That much is PROVED.

The further claim that this component "is not determined by (C,a)", which underlies "(β) is the full (C,a)-content", is asserted, not proved. The freedom available while keeping (C, a, constant first layer) is only P^t↦P^t+F f^[X]⊗ξ with F|ξ·f^[ρ]. This changes y_u by f^[X](ξ·ω^[ρ]), a restricted family. The "precise negative result" should be relabelled HEURISTIC in that part. The sentence "any further exclusion … must use (γ)" is true but tautological, since FN ⟺ (γ).

**Remark 4.5** is correct. From (†) with s̃=0 and F|C_cBc: μ=F²t^{ρ−X}·(…) and y_u=O(t^{e_u−X}).

**Remark 4.6** is correct as labelled.

### 2.8 Lemma 5.2, Thm 5.3, Cor. 5.4

**Lemma 5.2 is correct.**
- R21 Remark 3.4 gives V_u(z(v))=κ_u[β(u)(ψ(v)+ψ(u))k_22(v)+𝒞_c(v)(B(u)+B(v))c] in a frame of 𝓣^{ρ𝔮} that is the ρ𝔮-th power of a frame of 𝓣. So B(v)−B(u)=(B̂(v)−B̂(u))^{[ρ𝔮]} has order >=ρ𝔮.
- The left side has order >=min(ord V_u|_{ℓ_u}, e_u) by the graph argument.
- Summation uses ord_u>=max(0,2−e_ψ(u))>=2−e_ψ(u) and Σ(e_ψ−1)<=deg Diff_ψ=2g−2+2deg ψ. Wild ramification is fine, since ord(Diff)>=e−1, and ψ is separable because ψ∉K².
- k_22 is formed with z, of degree ad'+ρ·deg[T].

**Thm 5.3.**
- (i) At 𝔮>S, every good u has 𝔡(u)=V_u(z(u))/κ_u=0 (Lemma 5.1(a)). R21 Lemma 3.2(iii) then gives (𝒦_ψ) or N_good<=charges+deg 𝔡².
- (ii) m'_u>=min(X−ρ,E,ρ𝔮)>=2, and Lemma 5.2 applies on {β≠0} (charge deg ψ).
- The charges are complete: Nd, 2deg[T]/𝔮, 𝔈, boundary, plus deg ψ in (ii).
- Since 𝔮>=128 (R18 Cor. 5.5), all of (R1) at S=64 is excluded.

Unlike Cor. 3.2, Thm 5.3 genuinely needs the new C-layer order: Lemma 5.1(a) uses Thm 3.1(iii).

**Cor. 5.4.** The thresholds are 1551/4000−0.14770305=0.240047q and 1551/4000−0.10430527=0.283445q.

### 2.9 Prop. 5.5 and Remark 5.6

Correct.
- σ_u∈V=span(t̂_ij) (R19 Lemma 3.5(i)), and ord_uσ_u>=N_0 gives j_{r_V}(u)>=N_0.
- Stöhr–Voloch Thm 1.5 gives v_u(R)>=Σ(j_i−ε_i)>=N_0−ε_{r_V}.
- Maximal 𝔮 makes [V] separable. For dim V=2 this is Riemann–Hurwitz for a separable map of degree τ_0 ramified to order >=N_0 at every good point.

**FIX-7.** The pencil case is unconditional and holds inside (𝒦) as well, since Cor. 3.2 holds for every twist. So:
- every non-constant twist with dim V=2 and 𝔮<(2r−1)S is excluded, in (R1) or (R2);
- with Thm 5.3, (R1) with dim V=2 is closed entirely.

§6 says "(R2) … unchanged … apart from Prop. 5.5 (CONDITIONAL)". That understates the result and is inconsistent with §0 item 8.

### 2.10 Numerics

**Owner.** `numerics_R22.py` reruns byte-identically.

**Referee** (`numerics_indep.py`, an independent implementation from the printed formulas):
- grid r∈{4,…,128}, Q∈{2^7,…,2^14} (including 8192), S∈{2^6,…,2^13}, dyadic n∈[256,2Q];
- two variants: (V1) the owner's normalisation; (V2) exact a=8h/625+X−ρ−d', scanned over every d'∈[2E−2,2E+4].

| count | max/q (V1, corner (4,128,64,256)) | owner's exact fraction reproduced | V2 max | < 1551/4000 |
|---|---|---|---|---|
| Cor. 4.1 | 0.0460943829 | yes | 0.0456252 | yes |
| Cor. 4.2 | 0.0929718271 | yes | 0.0826343 | yes |
| Thm 5.3(i) | **0.1477030473** (max) | yes | 0.1338780 | yes |
| Thm 5.3(ii) | 0.1043052693 | yes | 0.0896422 | yes |
| Prop. 5.5 classical | 0.0687322573 | yes | 0.0687323 | yes |
| Prop. 5.5 pencil | 0.0491941590 | yes | 0.0491942 | yes |

- Term-wise monotonicity under doubling of r, Q, S or n: 146 640 comparisons, 0 violations. So the whole-strip supremum is the corner.
- **FIX-6:** several printed "≤" decimals are *below* the exact maxima: Thm 5.3 "≤0.147703q" (exact 0.14770305) and "≤0.104305q" (0.10430527), and Prop. 5.5 "≤0.049194" (0.04919416) and "≤0.068732" (0.06873226). Round up: 0.147704, 0.104306, 0.049195, 0.068733. No conclusion changes; the smallest margin is 0.2400.

---

## §3 FIX items (substantive first)

- **FIX-1 (Remark 4.4; overclaim of a PROVED negative result).** Split the label:
  - PROVED: FN at u ⟺ (α)∧(β)∧(a scalar condition per t-order on the f^[X]-component of y_u); the J-part consistency is automatic. Include the one-line proof in §2.7.
  - HEURISTIC: that this component carries no (C,a)-information. With (C, a, first layer) fixed, the only freedom is P^t↦P^t+Ff^[X]⊗ξ, which is restricted.
  - Note that "any exclusion must use (γ)" is tautological, since FN ⟺ (γ).
- **FIX-2 (Prop. 4.3, after (iv); wrong justification, overclaim).**
  - Replace "η arbitrary (not a syzygy) … (R18-T Prop. 2.4)" by the Remark 4.6 modification η=Fξ. It keeps C, the first layer and zero top, and changes a'↦a'+ξ·f^[ρ].
  - Conclude only that F²|a is not implied by C̃.
  - Replace "every C̃ is still possible at the C-level" by "Thm 3.1/Cor. 4.2 impose no condition on C̃ beyond those of R21".
- **FIX-3 (remark after Prop. 2.3; false statement).**
  - (★)·u^[X] is identically 0 on both sides and carries no information.
  - (★)·ω^[X] gives t^ρ·F·b^{[X],t}C_cb^[ρ], which is FNAL2/TSYC, not t^{ρ+X}·F·b^{[X],t}C_cb^[ρ].
  - COMPUTED in `thm31_toy_indep.out`.
- **FIX-4 (Cor. 3.2 / §0 item 4 / "R19 had only σ_u(u)=0"; novelty overclaim).**
  - State that the first bullet already follows from R16.2 (ν_u>=E−X−ρ via TSYC transported to Γ) together with ν_u∈ρ𝔮Z.
  - The new content is the +ρ (used only at e_u=E+1) and the C-layer order of Thm 3.1(ii)–(iv), on which Thm 5.3 depends.
- **FIX-5 (Lemma 2.4(iv), Thm 3.1 dependency line).** Do not cite "R18-T Prop. 2.2 Step 3", a step of a CONDITIONAL proposition. Give the local proof: off Bs(f) on Γ', κ·f^[ρ]=g^{ρ−X}ϰ_P·U^[ρ]=0, hence F|a_P.
- **FIX-6 (rounding).** Round up the "≤" decimals of Thm 5.3 and Prop. 5.5 (§2.10). Cor. 4.1's 0.046095 and Cor. 4.2's 0.092972 are fine.
- **FIX-7 (§6 consistency).**
  - Record that the Prop. 5.5 pencil case is unconditional and holds in (𝒦).
  - So non-constant twists with dim V=2 and 𝔮<(2r−1)S are excluded in (R1) and (R2), and (R1) with dim V=2 is closed by Thm 5.3 + Prop. 5.5.
  - Update the (R2) line accordingly.
- **FIX-8 (toy wording and coverage).**
  - The owner's toy S=J^[X]C''J^[ρ,t]+f^[X]⊗ξ with polynomial C'' is not "the most general P". It realises only C=Ω(J^{[X],t}J^[X])C''.
  - Case (A) uses e_F=3<X, which is harmless because F cancels for a constant layer (§2.4).
  - In (C), the only unsolvable control is the trivial pole case. State this, and cite the referee toy for the non-trivial gap cases.

## §4 Minor notes

- **N1.** Lemma 2.2 admits the line-method proof of §2.2, which needs neither smoothness of Γ nor the branch. Its criterion z·w^[E]=0 agrees with y_1^[E]·e(u)=0 at every one of 29 705 points. In the lift "v(s)=u+sy_1+…", say "affine lift", so that y_1∦u is automatic.
- **N2.** Thm 3.1 holds in the exact form (†) (not only mod t^X). This makes "V_u|_{ℓ_u}∥(c^[T])^⊥ with scalar t^{X−ρ}μ̂+t^Xs̃/F" explicit and links it to R21 Lemma 3.1's η_u.
- **N3.** In Thm 3.1(iv), "exact leading term" should be "exact congruence". The term t^{X−ρ}a'_c is leading only when a'_c(z(u))≠0.
- **N4.** The §0 item 3 phrase "with the exact leading term" has the same issue.
- **N5.** Lemma 5.2 could use m'_u>=X−ρ (much larger than 2) at 𝔮>S. It is not needed, but it shows the margin.
- **N6.** The Cor. 5.4 thresholds are 0.240047q and 0.283445q (exact differences), consistent with the printed ≈0.240 and ≈0.283.
- **N7.** Prop. 2.3's dependency list should also name FNAM1 (J and κ_0).
- **N8.** The note's §7 calls the directory `scripts/`; it was delivered as `owner_scripts/`. The checksums match.

## §5 Files in `checks/`

| file | content | result |
|---|---|---|
| `src_SHA256SUMS.txt` | pre-supplied hashes of `src/` | all OK (`sha256sum -c`) |
| `owner_copy/` (+ `rerun/`) | copies of the owner scripts and outputs; reruns with `python3 -I` | numerics, contact_check and toy_vector_FN all **byte-identical**; times 0.15 s, 18.6 s, 2.9 s |
| `numerics_indep.py` → `.out` | independent exact-Fraction recomputation of the six counts; V1/V2; Q up to 16384 (incl. 8192), n up to 2Q; monotonicity; Cor. 5.4 thresholds | §2.10 |
| `lemma22_contact.py` → `.out` | Lemma 2.2 on random paired centres plus σ1 over GF(2^8/10/12); branch vs line order; owner's vs referee's criterion | §2.2: 29 705 points, 1 223 full checks, 0 failures |
| `thm31_toy_indep.py` → `.out` | (★), the remark, Thm 3.1 (i)–(iv), (†), solvability vs prediction, and the no-alignment control; general S over GF(2^8) | §2.1, §2.4: all as predicted; FIX-3 confirmed |
| `checks_SHA256SUMS.txt` | hashes of all files above | — |
