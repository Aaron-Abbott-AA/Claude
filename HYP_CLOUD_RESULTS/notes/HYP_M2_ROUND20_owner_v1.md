# HYP M>=2, round 20 (owner v1): the F_E-subline question — Frobenius reduction equals the own-line vanishing order, a line-restriction bound with a controlled exceptional set, constant twists in (𝒦), and an exact re-count of (R2)

7 October 2026. Claude HYP(2) owner research note. This is the R19 §6 follow-up: primary task step 1 ("sharpen Lemma 3.5 on the F_E-subline"); secondary tasks steps 2 and 3.

**Version.** v1 owner draft. Not yet audited.

Inputs (read, not re-proved):
- R19 v2.1 (`R19_CORRESPONDENCE_ROUTE_v2_1.md`), audited and revision-checked. Used: Lemma 1.1(i), Prop. 1.1, Prop. 1.2, Lemma 1.5, Lemma 3.0, Lemma 3.1, Cor. 3.2, Prop. 3.3, Prop. 3.4, Lemma 3.5, Thm 4.1 (all steps), Example 1.6, and the N4 inequality of Thm 4.1 Step 4.
- R18-T v2.1 (`R18T_TWIST_NOTE_v2_1.md`), audited and revision-checked. Used: Lemma 1.2, Prop. 4.1(ii), Prop. 4.2, Example 4.3, §6 residual list.
- R18 v2.1, R17 v2.1, R16 v2.1. Used: R16 §1 (U^[E]=αℓ+βm, deg ψ<=(E+1)d), R14.1 (ψ∉K²), R16 Step 2 (contact).
- PRIMARY FNAK/FNAL/TSY/TSYC/FNAM/FNAN/FNAO/FNAP as reviewed (PASS / PASS-with-fixes). Used: FNAM2 (generic invertibility Δ≢0), FNAM3/TSYC (ℓ_u | G_{c(u)}), FNAP §4 (D∈{1,2} counterexamples). All PRIMARY results are PRIMARY's.

Labels (as in R18-T/R19):
- **PROVED**: complete proof given here, conditional only on the named inputs. (Owner proof; not yet audited.)
- **CONDITIONAL**: proved under a named hypothesis that is not established.
- **COMPUTED**: exact finite-field or exact-rational computation. It proves only where an exact rational bound is evaluated.
- **HEURISTIC / OPEN / CITED**: as stated.

Rules followed: no file whose name contains "DZ" was opened; no PRIMARY/Codex script was executed (only `.md` read); all scripts are mine, run with `python3 -I`, one at a time, each < 1 min. The R19 helpers `env_lib.py`, `numerics_K.py` in `scripts/` were read, not run; `numerics_K.py`'s evaluation is re-implemented in `numerics_R20.py` (mode "R19") and reproduces every R19 Cor. 4.2 threshold.

Notation is R19's: q=Eh, E=rQS=rT, ρ=Q/2, X=T/2, n=h/E; d=deg Γ<=E+2; d'=deg Γ'>=2E−2; a=deg C_•; c(u)=(√β:√α)(u); T=T̂^[𝔮], τ_0=deg 𝓣=deg[T]/𝔮; B=swap·(T^t)^[ρ] with entries b̂^{ρ𝔮}; z:Γ̃→Γ' the normalised e; ℓ_u={Y: u^[E]·Y=0}; 𝒞_c=C_c(z); (𝒦): 𝒞_cBc=0 for all c∈k². Δ(c,Y):=det C_c(Y)=c_1²Δ_0+c_1c_2Δ_1+c_2²Δ_2 (FNAM2: Δ≢0). New:
- V_u(Y):=C_{c(u)}(Y)·c(u)^[Q], a vector of two forms of degree a in Y, and ξ^ω_u:=(ω^tV_u)|_{ℓ_u}, a binary form of degree a on ℓ_u (ω∈k²).
- m:=min(ρ𝔮,E).
- N_Ξ(u):=#{residual places v of ℓ_u : Ξ(u,v)=0}.
- k_P:=number of places of Γ̃ over a point P∈Γ'; mb(u):=Σ_{P∈ℓ_u∩Γ'}(k_P−1).
- 𝔅:={u∈Γ̃ : V_u|_{ℓ_u}≡0} ("own line divides V_u").

---

## 0. Summary

**The question.** Can N_Ξ(u) (the residual zeros of Ξ(u,·)=σ_u^{ρ𝔮}) be bounded by ≈a/E+O(1), or by anything much smaller than R19's τ_0−1, through Frobenius reduction modulo the projective polynomial (αt+β)t^E+γt+δ?

**Answer.** "Much smaller than τ_0−1": **yes**, in the only regime where a per-point improvement can matter (a<d', i.e. n=256), and with an exceptional set of size O(E²). "≈a/E": **no**, not by this mechanism. The Frobenius reduction is *equivalent* to the own-line vanishing order at z(u), and that order is capped at E. Details:

**PROVED.**
1. **Reduction lemma (Lemma 2.1, Prop. 2.2).**
   - Reducing ξ=Σ_k ξ_k t^{kE} modulo P_u=A_2(t)t^E+A_1(t) bounds its zeros on the subline by s+⌊a/E⌋, where s=max deg ξ_k.
   - s<=s_0 iff the Hasse derivatives D^{(j)}ξ vanish for s_0<j<E ("E-sparsity").
   - For E<=a<2E and t^E|ξ, the reduction gives exactly deg ξ_1=a−E. This is the same as the vanishing-order bound, so the subline adds **nothing** beyond the order-E zero at z(u).
2. **Obstructions to ≈a/E (Prop. 2.3).**
   - (i) The values of Ξ(u,·) on the ≤E+1 residual points carry no Frobenius information, since every element of k is a ρ𝔮-th power.
   - (ii) The order of ξ^ω_u at z(u) is >=min(ρ𝔮,E), and no more can be forced from Γ' data: the contact is exactly E.
   - (iii) Ξ-zeros can fill entire residual fibres. Any per-point bound therefore needs an exceptional set (Example 2.4).
   - Under the extra hypothesis that T̂ is of plane-polynomial origin (H_po), N_Ξ(u)<=m_T−1+mb(u) (Cor. 2.5, CONDITIONAL).
3. **Constant twists in (𝒦) (Prop. 3.1).**
   - (𝒦) with [T] constant forces a>=d'. The proof is two lines: F divides C_c(Y)Bc, which has degree a, and FNAM2.
   - Since a_max<d' at n=256 for every r>=4, Q, S, **(𝒦) with constant T is impossible at n=256 for every D, including the D∈{1,2} lanes** (Cor. 3.2). In general it is impossible whenever M'<2d'−X+ρ.
4. **Line-restriction bound (Lemma 4.2), replacing Lemma 3.5(iii).**
   - Let u be good, non-cuspidal, and u∉𝔅. Then N_Ξ(u)<=a−m+mb(u), with m=min(ρ𝔮,E), whatever τ_0 is.
5. **The exceptional set (Lemma 4.3).** |𝔅|<=B_𝔅:=2deg ψ+2(2a−d')d'+2g−2=O(E²). The proof uses (𝒦)⇒F|Δ, FNAM2, R14.1 and the contact >=E. No τ_0 hypothesis is needed.
6. **A count without the τ_0 restriction (Thm 5.1, (4.1′)).** It holds when D_1:=d'−E−(a−m)>0. For ρ𝔮>=E (m=E) this means a<d', which holds at n=256 and fails at n>=512.
7. **The N4 re-count of R19 (Prop. 5.2).** R19 Thm 4.1 Step 4 already proves 2r(d−1)deg𝓟+d·#Z(λ)<=2r(d−1)(ad'−ρ·deg[T]) (audit note N4, "not used"). Inserting it into (4.1) is free. It shows that the p-term budget is shared with the twist height, which partly answers step 3 (the "2r loss").

**COMPUTED** (exact Fractions, `numerics_R20.out`; mode "R19" reproduces every R19 Cor. 4.2 entry). (𝒦) with non-constant T is excluded for all dyadic 𝔮 at least:

| r | n | R19 | R20 (Prop. 5.2 ∪ Thm 5.1) |
|---|---|---|---|
| 4 | 256 | 8E/Q | **2E/Q** |
| 4 | 512–8192 | nE/(8Q) | **nE/(16Q)** (so 𝔮>=E/8 throughout the grid) |
| 8 | 256 | 16E/Q | **2E/Q** |
| 8 | 512 | 128E/Q | **32E/Q** |
| 8 | 1024 | none | **64E/Q** (Q>=512) |
| 16 | 256 | 512E/Q (Q>=512) | **8E/Q** (every Q>=128) |

Grid: Q∈{128,…,16384}, S∈{64,256}, every d'∈[2E−2,2E+4]. The self-check finds 0 mismatches.

Also COMPUTED:
- **Fermat toy (E=8, GF(2^12)).**
  - The contact of ℓ_u is exactly E.
  - Forms of degree a with order N along Γ' at u have order exactly min(N,E) on ℓ_u. The cap at E is attained even for N=3E.
  - The method bound a−E is attained, and k=a−E+1 imposed residual zeros force ℓ_u | A (the 𝔅 alternative).
- **Clustering example (Example 2.4).** N_Ξ(u)∈{0,6} on all 4221 points, and =6 at 7 of them.

**What failed.**
- The ≈a/E bound. The Frobenius reduction gives nothing beyond the vanishing order (Prop. 2.2), and E-sparsity is not available: it fails for generic local data (COMPUTED), and polynomial-origin second layers are impossible when a<d' (Prop. 6.2).
- At n>=512 the line bound is vacuous (a−E>d'−E).
- (R1): only the decomposition identity (6.1) and the explicit three-term X-power obstruction. No cheap factor was found (HEURISTIC).

**New territory closed (PROVED, numbers COMPUTED).**
- (R2), constant T: the n=256 strip (every r>=4, Q, S, D). In general this holds whenever a<d'.
- (R2), non-constant T: the 𝔮-ranges of the table above. These are newly closed: r=16 at Q∈{128,256}; r=8 at n=1024; and lower 𝔮 for r=4, 8, 16 at n=256 and for r=4, 8 at n>=512.

**Still OPEN in (R2):**
- non-constant T below these 𝔮;
- r=8 with n>=2048;
- r=16 with n>=512;
- constant T with a>=d' and D∈{1,2}.

**Next step (HEURISTIC, §7).**
- At n=256 the remaining gap 𝔮<2E/Q (8E/Q for r=16) is where the own-line order m=ρ𝔮 is below E. Raising m there, through higher-order vanishing of σ_u at u, would close it.
- At n>=512 (a>d'), reduce V_u modulo F|_{ℓ_u}=t^E·P̃_u(t), which is itself E-sparse. This is the genuine form of the a/E question there.
- The non-constant analogue of Prop. 3.1 through R19's frame only reproduces F|Δ (R18-T Prop. 4.2). Remark 3.3 explains why.

---

## 1. Setting

Standing hypotheses are R19 §3: 𝔇_16 (global alignment, common image, zero top, first scalar order ρ, pure, Q>=128, 256E<=h<4QE, 𝔮>=128), the (𝒦) reduction F∤(C_P,C_R), and "good u" as in R19 §3 (off 𝔈, the boundary, {λ'=0}, {det T̂=0} and {g=0}). At a good u, c(u)^[Q]=κ_uB(u)c(u) with κ_u≠0 (R18-T Lemma 1.2).

**Identity (1.1) (PROVED; it is R19 Lemma 3.1 + Lemma 3.0).** For a good u and every place v,
      V_u(z(v)) = 𝒞_{c(u)}(v)c(u)^[Q] = κ_u·p(v)·Ξ(u,v),   Ξ(u,v)=det(B(v)c(u),B(u)c(u)).
*Proof.* 𝒞_c=p⊗(Bc)^⊥ (R19 Lemma 3.1, via the morphism z). Hence 𝒞_c(v)w=p(v)det(B(v)c,w); take w=c^[Q]=κ_uB(u)c. ∎

So, for every ω, Ξ(u,v)=0 implies ω^tV_u(z(v))=0. The point z(v) lies on ℓ_u when v is residual. The question is how many such zeros the binary form ξ^ω_u can have.

---

## 2. Frobenius reduction on the subline, and why ≈a/E is out of reach

Put the conic/line parameter of R19 Prop. 1.2 so that z(u) is t=0. The residual parameters are then roots of P_u(t)=A_2(t)t^E+A_1(t) with A_1,A_2 linear and coprime (the non-degenerate case αδ≠βγ of Prop. 1.2; with s_u=0, H=s(A_2(t)s+A_1(t)) in Prop. 1.2's proof). If j(u)=E, then A_1(0)≠0: otherwise t=0 would also be a root of the residual factor, and the contact would exceed E. So t=0 is not a residual parameter. (The u with j(u)>E are charged by Σ(j(u)−E) in §5.)

**Lemma 2.1 (reduction modulo the projective polynomial; PROVED).** Let ξ∈k[t] have degree <=a. Write ξ=Σ_{k=0}^{K}ξ_k(t)t^{kE} with deg ξ_k<E and K=⌊a/E⌋, and put s:=max_k deg ξ_k.
- (i) Put R:=Σ_kξ_kA_1^kA_2^{K−k}. If R≢0, then #{roots t_i of P_u with A_2(t_i)≠0 and ξ(t_i)=0}<=deg R<=s+K.
- (ii) (Sparsity criterion.) s<=s_0 iff the Hasse derivatives D^{(j)}ξ vanish identically for all s_0<j<E.
- (iii) E-sparsity of level s is preserved by every projective change of the parameter, up to s↦s+(a mod E).

*Proof.*
- **(i)** At a root with A_2(t_i)≠0, t_i^E=A_1(t_i)/A_2(t_i) (characteristic two). So ξ(t_i)=Σ_kξ_k(t_i)(A_1/A_2)^k(t_i)=R(t_i)/A_2(t_i)^K.
- **(ii)** For 0<i<E, D^{(i)}(t^{kE})=0 (Lucas), so by Leibniz D^{(j)}(ξ_kt^{kE})=D^{(j)}(ξ_k)t^{kE}. Hence D^{(j)}ξ=Σ_kD^{(j)}(ξ_k)t^{kE}, and the decomposition is unique. Since deg ξ_k<E, D^{(j)}ξ_k≡0 for all s_0<j<E iff deg ξ_k<=s_0. (The coefficient of t^j in ξ_k equals D^{(j)}ξ_k(0), and a polynomial of degree <E with D^{(j)}≡0 for all j>s_0 has degree <=s_0.)
- **(iii)** (λt+μ)^{kE}=(λ^Et^E+μ^E)^k. For a Möbius change, clear denominators with (γt+δ)^a=(γt+δ)^{a mod E}((γt+δ)^E)^{K}. ∎

**Proposition 2.2 (on the subline the reduction equals the vanishing order; PROVED).** Let E<=a<2E and suppose t^E|ξ (the case m=E of Lemma 4.1 below). Then the reduction bound of Lemma 2.1(i) equals deg(ξ/t^E)<=a−E. This is exactly the bound obtained from the order-E zero at t=0 alone. More generally, if t^m|ξ with m<=E, the vanishing-order bound a−m is at least as good as Lemma 2.1(i) unless deg ξ_k<=a−m−K for all k.

*Proof.* K=1, ξ_0=0 and ξ_1=ξ/t^E, so R=ξ_1A_1. A root of A_1 that is a root of P_u satisfies A_2(t_i)t_i^E=0, which gives t_i=0, and that is not a residual parameter. So the residual zeros of ξ are those of ξ_1. The general case: a−m vs s+K with s=max deg ξ_k. ∎

So a bound ≈a/E+O(1) through the subline requires s=O(1), i.e. ξ^ω_u is E-sparse along ℓ_u. In the n=256 regime (E<=a<2E) this means ξ^ω_u=t^E·(polynomial of degree O(1)). That is a vanishing of order >=a−O(1) at z(u).

**Proposition 2.3 (obstructions; PROVED, with (ii) COMPUTED for sharpness).**
- (i) **Pointwise vacuity.** For fixed u the residual set has <=d'−E<=E+1 points (R19 Prop. 1.1–1.2). Every function on it is the restriction of a polynomial of degree <=E in t, and every value of Ξ(u,v)=σ_u(v)^{ρ𝔮} is a ρ𝔮-th power in the perfect field k. So no per-point argument can use the Frobenius structure of Ξ through its values. Any gain must come from the form ξ^ω_u: its degree a and its local behaviour at z(u).
- (ii) **The E-cap.** The local information at z(u) yields order >=min(ρ𝔮,E) (Lemma 4.1). It yields no more in general: Lemma 4.1's proof uses Γ' only through its contact with ℓ_u, which is exactly E at generic u (R19 Prop. 1.1). COMPUTED (`toy_line_order.out`, Fermat E=8, 3 points each):
  - forms with order N∈{16,24} along Γ' at u restrict to ℓ_u with order **exactly** 8=E, never more;
  - with N=4 the order is exactly 4.
  So the vanishing-order bound a−m is the best obtainable from this local data. By Prop. 2.2 the subline reduction adds nothing to it.
- (iii) **The method bound is attained.** COMPUTED (same file):
  - a=12, N=8 together with k residual zeros imposed: for k<=4=a−E there are solutions with ξ≢0 and order 8 at z(u);
  - for k=5,6 every solution has ξ≡0, i.e. ℓ_u|A. This is the 𝔅 alternative of Lemma 4.2.
  - Likewise for a=13: k<=5 vs k=6.
- (iv) **Clustering (Example 2.4).** Ξ-zeros can occupy all residual points of ℓ_u simultaneously. So any per-point bound below d'−E must allow an exceptional set of u.

*Proof of (i).* Lagrange interpolation, and perfectness of k. (ii) and (iii) are as computed, with the claims about the proof read off from Lemma 4.1. (iv) is Example 2.4. ∎

**Example 2.4 (Ξ-zeros cluster on residual fibres; PROVED identity, COMPUTED count).**
- **The data.** Fermat σ1 with E=8: Γ: U_0^7+U_1^7+U_2^7=0. The residual points of ℓ_u are v_ζ=diag(1,ζ,ζ/(1+ζ))u^[8], ζ∈F_8∖{0,1} (R19 Ex. 1.6).
- **The twist.** Take M(U)=[[U_0^7,U_1^7],[U_2^7,U_0^7+U_1^7]], whose entries are F_2-forms in U_i^7. Since (ζ_iu_i^8)^7=u_i^{56}, M(v_ζ)=M(u)^[8] for every ζ.
- **Consequence.** Ξ(u,v_ζ)=det(M(u)^[8]c,M(u)c) is independent of ζ, so N_Ξ(u)∈{0,6}={0,d'−E}.
- **Computation (`fermat_cluster.out`).** Over GF(2^12), 4221 affine points: the histogram is {0: 4214, 6: 7}.
- **Scope.** This is a toy: no (𝒦)-pencil and no FN condition is imposed. It shows only that "all-or-nothing" fibres occur for invariant twists.

**Corollary 2.5 (polynomial-origin twist; CONDITIONAL on (H_po), OPEN).** (H_po) says: there are forms B̃_ij(Y) of degree m_T and a rational function μ on Γ' with t̂_ij=μ·B̃_ij(z) on Γ̃.

Under (H_po), σ_u(v)=μ(v)σ̃_u(z(v)) with σ̃_u:=Σŵ_iĉ_jB̃_ij of degree m_T, and σ̃_u(z(u))=0. Hence, off the set of u with σ̃_u|_{ℓ_u}≡0, N_Ξ(u)<=m_T−1+mb(u)+#(Res(u)∩Z(μ)). That is ≈τ_0/d' instead of τ_0−1.
- (H_po) is not implied by (H_lift) (R18-T Prop. 2.2 gives only [T^ρ] by forms, not T̂).
- The exceptional set {σ̃_u|_{ℓ_u}≡0} is not bounded here.

*Proof.* Restrict σ̃_u to ℓ_u: it is a binary form of degree m_T, with one zero at z(u). ∎

---

## 3. Constant twists in (𝒦)

**Proposition 3.1 ((𝒦) with constant twist forces a>=d'; PROVED, conditional on FNAM2).** Assume (𝒦) and that [T] is constant (B=λB_0 with B_0∈GL_2(k), λ a function). Then a>=d'. Equivalently (a=M'+X−ρ−d') M'>=2d'−X+ρ. Since d'>=2E−2, (𝒦) with constant T is impossible whenever M<8E−T+Q−7.

*Proof.*
- **F divides a fixed vector of forms.** (𝒦) says C_c(z(v))B_0c=0 for all c∈k² and all v. So for each c the vector of forms W_c(Y):=C_c(Y)B_0c, of degree a and polynomial in (c,Y), vanishes on Γ'. Since F is irreducible, F divides both entries.
- **It vanishes identically.** If a<d', then W_c(Y)=0 in k[c,Y].
- **Contradiction.** For every c≠0, B_0c≠0 lies in ker C_c(Y), so Δ(c,Y)=det C_c(Y)=0 identically. This contradicts FNAM2. ∎

*Remarks.*
- This is the constant-T analogue of R18-T Prop. 4.2 (F|Δ_i, deg 2a<d'). No count, no D, and no good point is used. Hence it covers the D∈{1,2} lanes, where FNAP §4 shows that the algebraic step of FNAP fails.
- It does not use the reduction F∤(C_P,C_R). If F|(C_P,C_R) with a<d', then C=0, which also contradicts FNAM2.

**Corollary 3.2 (n=256; PROVED, numbers COMPUTED exactly).**
- With the normalisation a<=8h/625−d'+X−ρ, the inequality a_max<d' holds for every d'∈[2E−2,2E+4] at n=256, for all r∈{4,8,16}, Q∈{128,…,16384} and S∈{64,256}. The maximum of a_max/d' is 0.7007 (`numerics_R20.out` (C)).
- By exact algebra the same holds for all r>=4, Q, S: a_max<d' for every d'>=2E−2 ⟸ 8h/625+X−ρ<4E−4. At n=256 this reads 3.2768E+E/(2r)−Q/2<4E−4, which holds since E/(2r)<=E/8 and E>=2^15.
- It fails at n=512 (a_max/d'≈2.3).
- **Hence (R2) with constant T is closed at n=256 for every D.** In particular, the D∈{1,2} constant-twist lanes inside (𝒦) are closed there, which R18-T/R19 had left to FNAP §4.

**Remark 3.3 (why the gain a<d' vs 2a<d' is special to constant T; PROVED).**
- For non-constant T, the natural polynomial replacement for B(z)c is R19's frame (Prop. 3.3): on Γ', (row_iC_c)^⊥=p_i·Bc.
- With it, C_c(Y)(row_iC_c(Y))^⊥ has first entry row_i·row_i^⊥=0 identically, and second entry det(row_j,row_i)=Δ(c,Y).
- So "(𝒦) via the frame" is exactly F|Δ, of degree 2a, which is R18-T Prop. 4.2 (2a<d').
- The window d'/2<=a<d' for non-constant T is therefore not closed by Prop. 3.1-type algebra. It is where Thm 5.1 operates.

---

## 4. The line-restriction bound and its exceptional set

**Lemma 4.1 (order transfer to the own line; PROVED).** Let u be a non-cuspidal place (in R19 Lemma 1.5's sense: z∧dz≠0 at u), let A(Y) be a form, and suppose A(z(y))=O(s^N) along the branch of Γ̃ at u (s a local parameter). Then A|_{ℓ_u}, written in a linear parameter t with t=0 at z(u), vanishes at t=0 to order >=min(N,E) (or A|_{ℓ_u}≡0).

*Proof.*
- **Coordinates.** Choose coordinates with ℓ_u={Y_2=0} and z(u)=(1,0,0). Write z(y(s))=(z_0,z_1,z_2)(s). Then ord_s z_2=j(u)>=E (R19 Lemma 1.1(i): the own line meets every branch with multiplicity >=E).
- **The line parameter.** z_0(0)≠0, and t(s):=z_1/z_0 has ord_st=1, because the place is non-cuspidal and the tangent is ℓ_u.
- **Compare.** A(z_0,z_1,z_2)=A(z_0,z_1,0)+O(z_2)=z_0^{deg A}·A|_{ℓ_u}(t(s))+O(s^E). The left side is O(s^N). So A|_{ℓ_u}(t(s))=O(s^{min(N,E)}), and since ord t(s)=1 this is the claimed t-order. ∎

**Lemma 4.2 (line-restriction bound; replaces R19 Lemma 3.5(iii); PROVED).** Assume R19 §3's standing hypotheses and (𝒦). Let u be good and non-cuspidal, with u∉𝔅. Then
      N_Ξ(u) <= a − m + mb(u),   m=min(ρ𝔮,E).
No hypothesis on τ_0, and no non-constancy of T, is needed.

*Proof.*
- **Choose a row.** Since u∉𝔅, choose ω∈{e_1,e_2} with ξ:=ξ^ω_u≢0, a binary form of degree a.
- **Order at z(u).** By (1.1), ω^tV_u(z(y))=κ_u(ω·p(y))Ξ(u,y), and Ξ(u,y)=σ_u(y)^{ρ𝔮} with σ_u(u)=0 (R19 Lemma 3.5(i)). p is regular (R19 Thm 4.1 Step 1). So the order at y=u is >=ρ𝔮. By Lemma 4.1, ξ vanishes at z(u) to order >=m.
- **Other zeros.** Hence ξ has at most a−m distinct zeros on ℓ_u other than z(u).
- **Each Ξ-zero gives a zero of ξ.** If v is a residual place with Ξ(u,v)=0, then z(v)∈ℓ_u and ξ(z(v))=0 by (1.1).
- **Counting places.** Distinct places with distinct points z(v)≠z(u) give distinct zeros. Places sharing a point P, or lying over z(u) with v≠u, are at most Σ_P(k_P−1)=mb(u) in number beyond the points counted. ∎

**Lemma 4.3 (the exceptional set 𝔅; PROVED, conditional on FNAM2 and R14.1).** Assume (𝒦). Let k>=1 be maximal with F^k | Δ_0,Δ_1,Δ_2 (k>=1 by R18-T Prop. 4.1(ii)), and write Δ=F^kΔ^{(k)}. Put N_k=2a−kd'<=2a−d'. Then
      |𝔅| <= B_𝔅 := 2deg ψ + 2(2a−d')d' + 2g − 2.

*Proof.*
- **Step 1: 𝔅 forces Δ^{(k)} to vanish on the own line.** If u∈𝔅, then C_{c(u)}(Y)c(u)^[Q]=0 for Y∈ℓ_u, with c(u)^[Q]≠0. So Δ(c(u),·) vanishes on ℓ_u. F|_{ℓ_u}≢0, since Γ' is irreducible and is not a line. So Δ^{(k)}(c(u),·) vanishes on ℓ_u.
- **Step 1: order along Γ.** As in Lemma 4.1 (coordinates with ℓ_u={Y_2=0}), Φ_u(y):=Δ^{(k)}(c(u),z(y)) vanishes at y=u to order >=j(u)>=E. Here c(u) is frozen, and this holds at every place u, cuspidal or not.
- **Step 2: Case φ≢0.** Write α̃,β̃ for sections of 𝓐 without common zero (deg𝓐=deg ψ), with c=(√β̃,√α̃). Put
      φ²(u):=β̃²Δ^{(k)}_0(z)²+α̃β̃Δ^{(k)}_1(z)²+α̃²Δ^{(k)}_2(z)²,
  a section of degree 2deg ψ+2N_kd'. It equals Φ_u(u)². If φ²≢0, Step 1 gives 𝔅⊂Z(φ²), so |𝔅|<=2deg ψ+2N_kd'.
- **Step 3: Case φ≡0, the identities.** Put δ_i:=Δ^{(k)}_i(z)/s_0∈K for a fixed section s_0. Then δ_0+√ψδ_1+ψδ_2=0 in K(√ψ). Since √ψ∉K (R14.1), δ_1=0 and δ_0=ψδ_2. Also Δ^{(k)}_2(z)≢0: otherwise all three vanish on Γ', i.e. F^{k+1} divides every Δ_i, contradicting the maximality of k.
- **Step 3: Φ_u explicitly.** β̃(y)Φ_u(y)=Δ^{(k)}_2(z(y))·[β̃(u)α̃(y)+α̃(u)β̃(y)].
  - The bracket is the pull-back by ψ of the linear form vanishing at ψ(u). Its order at y=u is the ramification index e_ψ(u).
  - If β̃(u)≠0, Step 1 gives ord_u(Δ^{(k)}_2∘z)+e_ψ(u)>=E>=2. So u∈Z(Δ^{(k)}_2∘z) or e_ψ(u)>=2.
  - If β̃(u)=0, then α̃(u)≠0 and Φ_u=α̃(u)Δ^{(k)}_2∘z. So u∈Z(Δ^{(k)}_2∘z).
- **Step 3: count.** ψ is separable (ψ∉K²). By Riemann–Hurwitz, the ramified places number <=deg R_ψ=2g−2+2deg ψ. Hence |𝔅|<=N_kd'+2g−2+2deg ψ.
- **Conclusion.** Both cases are <=B_𝔅, using N_k<=2a−d'. ∎

*Remark 4.4.*
- When a<d' (in particular under Thm 5.1's D_1>0), 𝔅 contains R19 Lemma 3.5(ii)'s set: σ_u≡0 makes V_u vanish on Γ', hence F|V_u, hence V_u≡0. So Lemma 4.3 also re-bounds that set without the factor deg ψ.
- In Example 2.4-type clustering, a fibre filled with Ξ-zeros makes ξ vanish at z(u) to order >=m and at d'−E further points. If m+d'−E>a, this forces u∈𝔅. Lemma 4.3 says that in a genuine (𝒦)-pencil such u number O(E²), far below q.

---

## 5. The count without the τ_0 restriction, and the N4 re-count

**Theorem 5.1 ((𝒦), any twist height; PROVED, conditional on the cited inputs).** Assume R19 §3's standing hypotheses, (𝒦) for the reduced pencil, and D_1:=d'−E−(a−m)>0 with m=min(ρ𝔮,E). Then
      N_good·D_1 <= (d'−E)deg ψ + 2r(d−1)(a d' − ρ·deg[T]) + [(E+1)(2g−2)+3d'] + d(2d'+2g−2)
                    + (d'−E)⌊(2d'+2g−2)/(E−1)⌋ + 2dτ_0 + d·(d'−1)(d'−2)/2
                    + D_1·[Nd + 2τ_0 + (1.5d²+3.5d+1) + 3d + 6d_def + 7 + B_𝔅 + (2d'+2g−2)].        (4.1′)

*Proof.* This is R19 Thm 4.1 with Step 3's Ξ-removal replaced.
- **Step 1–2 (unchanged).** π=β(u)p'^σ_1(y)^{2r}+α(u)p'^σ_2(y)^{2r} is a nonzero section on each component of 𝒵'^res. Its degree is <=(d'−E)deg ψ+2r(d−1)deg𝓟.
- **Step 3 (modified).** For a good u, outside the R19 exceptional sets, outside 𝔅 and outside the cuspidal places (<=Σ(m(w)−1)<=2d'+2g−2 of them, R19 Lemma 1.5):
  - the distinct residual places number >=d'−j(u)−κ(u);
  - remove those in W={det T̂=0} (kept as in R19), at most N_Ξ(u)<=a−m+mb(u) Ξ-zeros (Lemma 4.2), and those in Z(λ);
  - at every remaining residual place, Π_1=0 (R19 Prop. 3.4) and λ≠0, so π=0.
- **Step 4: sum over u.**
  - Σ(j−E)<=(E+1)(2g−2)+3d' and Σκ<=d(2d'+2g−2)+(d'−E)⌊…⌋ (R19).
  - Σ|Res∩W|<=2dτ_0.
  - Σ_u mb(u)<=d·Σ_P(k_P−1)<=d·Σ_Pδ_P=d((d'−1)(d'−2)/2−g)<=d(d'−1)(d'−2)/2. A point P lies on ℓ_u for at most d places u, namely those on the line (P^{[1/E]})^⊥; and δ_P>=k_P−1.
  - Σ|Res∩Z(λ)|<=d#Z(λ).
- **The p-term.** R19 Step 1 gives deg𝓟+#Z(λ)<=ad'−ρ deg[T]. With d<=2r(d−1), the π-degree term plus the Z(λ) charge is <=2r(d−1)(ad'−ρ deg[T]). This is R19's N4 form.
- **Assemble.** Compare with deg π and add the exceptional sets. ∎

**Proposition 5.2 (R19 (4.1) with the N4 term; PROVED in R19, evaluated here).** In R19 (4.1), the term 2r(d−1)·ad' may be replaced by 2r(d−1)(ad'−ρ·deg[T]).

*Proof.* R19 Thm 4.1 Step 4, second bullet [v2: N4]. ∎

*Why it matters (the "2r loss", step 3).* The p-section and the twist height share one budget, deg𝓟+#Z(λ)+ρ deg[T]<=ad'. So the factor 2r multiplies only ad'−ρ deg[T]. For large ρ𝔮 the bound *decreases* with τ_0. For example, at r=16, Q=128, n=256, 𝔮=E/16, the margin grows from −0.0039 at τ_0=1 to −0.31 at τ_0=τ_hi (COMPUTED). This removes the 2r loss in the high-height part of the range. It does not remove it at τ_0=O(1).

**Corollary 5.3 (numerics; COMPUTED exactly in `numerics_R20.out`).**
- **Normalisation.** As in R19 Cor. 4.2: d=E+2; every d'∈[2E−2,2E+4]; g<=(d−1)(d−2)/2 in all 2g−2 terms; a<=8h/625−d'+X−ρ; N<16h/625; d_def<=q/1000; deg ψ<=(E+1)d. For Thm 5.1, also d(d'−1)(d'−2)/2 (g>=0) and B_𝔅 with these bounds.
- **The τ_0-range.** τ_0∈[1,τ_hi], with τ_hi=⌊min(ad'/(ρ𝔮),(Nd/ρ+d)/𝔮)⌋ (Prop. 3.3 / R18).
- **Exclusion test.** For given (r,Q,S,n,d',𝔮), the model is excluded for all τ_0 if every τ_0 lies in the exact solution set of (4.1)-N4 (restricted to τ_0<=d'−E) or of (4.1′).
  - Both reduce to polynomial inequalities in τ_0 (quadratic, resp. linear), solved exactly with Fractions.
  - They were cross-checked against direct exact evaluation: 0 mismatches in 2564 (τ_0, case) pairs.
- **Reproduction.** Mode "R19" (no N4, no (4.1′)) reproduces every entry of R19 Cor. 4.2's table, and its r=16 sequence E, E/2, E/4, E/8, E/32 for Q=512…16384.

| r | n | least dyadic 𝔮 from which all larger 𝔮 close: R19 → **R20** | which bound does it |
|---|---|---|---|
| 4 | 256 | 8E/Q → **2E/Q** (E/64 at Q=128, E/8192 at Q=16384) | (4.1′) |
| 4 | 512 | 64E/Q → **32E/Q** | N4 |
| 4 | 1024 / 2048 / 4096 / 8192 | nE/(8Q) → **nE/(16Q)** (so E/8 at n=2Q on the grid) | N4 |
| 8 | 256 | 16E/Q → **2E/Q** | (4.1′) (N4 alone: 8E/Q) |
| 8 | 512 | 128E/Q → **32E/Q** | N4 |
| 8 | 1024 | none → **64E/Q** (Q∈{512,…,16384}) | N4 |
| 8 | >=2048 | none → none | — |
| 16 | 256 | 512E/Q (Q>=512 only) → **8E/Q** (all Q>=128: E/16 at Q=128, E/32 at 256) | N4 |
| 16 | >=512 | none → none | — |

- **Monotonicity.** For each case the closed 𝔮-set is upward closed (`numerics_R20.out`, bit strings).
- **D.** Neither (4.1′) nor (4.1)-N4 uses D. So these ranges include the D∈{1,2} lanes of (𝒦) with non-constant T.
- **Where (4.1′) applies.** D_1>0 holds at n=256 (D_1/E≈0.60, 0.66, 0.69 for r=4, 8, 16 at m=E) and fails at n=512 (D_1/E≈−2.6). So Thm 5.1 is an n=256 tool.
- **Why r=16 gains nothing from (4.1′).** Its p-term dominates at τ_0=1 whatever the denominator.

---

## 6. Secondary tasks: (R1) (step 2) and the polynomial-origin test (step 3)

**(6.1) A decomposition of 𝒞_c relative to Bc (PROVED identity).** For any w with det(B(v)c,w)≠0, in characteristic two,
      𝒞_c(v) = [ k_c(v)⊗w^⊥ + (𝒞_c(v)w)⊗(B(v)c)^⊥ ] / det(B(v)c,w),   k_c:=𝒞_cBc (the (𝒦)-defect).
At a good u and a residual v, the vanishing G_{c(u)}(z(v))=0 becomes
      (c^[T]·k_c(v))·det(B(u)c,w) = (c^[T]·𝒞_c(v)w)·Ξ(u,v),   c=c(u).          (6.2)

*Proof.* For any x, x=[det(x,w)b+det(b,x)w]/det(b,w) with b=B(v)c. Apply 𝒞_c(v), and use c^[Q]=κ_uB(u)c. ∎

(6.2) isolates Ξ (handled per point by §4) from the defect term.

*Why the defect side is not cheap (HEURISTIC; the degree facts are PROVED).*
- On 𝒵', v-functions are E-th powers and E=2rX. So c_l^T·k_{l,ij}(v)=((β,α)_l·k^σ_{l,ij}(y)^{2r})^X.
- The remaining factor c_ic_j∈{β,√(αβ),α} gives c^[T]·k_c(v)=βΠ_{11}^X+√(αβ)Π_{12}^X+αΠ_{22}^X, a **three-term** sum of X-th powers with non-power coefficients.
- Unlike (𝒦)'s Π_1=λπ^X, no single X-th root exists. A three-term Frobenius identity (a Mason–Stothers-type count in characteristic 2) would be needed. This is the precise form of R19 Prop. 5.2's obstruction at residual points.
- **Status of (R1): no progress (OPEN).**

**Proposition 6.2 (no polynomial-origin second layer when a<d'; PROVED, conditional on FNAM2).** Assume (𝒦) and a<d'. Then there are no polynomial vectors p̃(Y), b̃_1(Y), b̃_2(Y) with C_P≡p̃⊗b̃_1^⊥ and C_R≡p̃⊗b̃_2^⊥ mod F. In particular R18-T Example 4.3-type data (which needs a>=d') do not occur at n=256.

*Proof.* C_P−p̃⊗b̃_1^⊥ is a matrix of forms of degree a<d' (homogeneity forces deg p̃+deg b̃=a) divisible by F, so it is 0. Likewise for R. Then C_c=p̃⊗(b̃_1c_1+b̃_2c_2)^⊥ has rank <=1, so Δ≡0, contradicting FNAM2. ∎

*Consequence for step 3.* R19 suggested testing the 2r loss on Example 4.3-type data. At n=256 such data cannot exist. At n>=512 they can, but there the line-restriction route is vacuous. The partial answer to the 2r loss is Prop. 5.2: it is offset by the twist height.

---

## 7. What remains, and next steps

**Residual after this note** (inside 𝔇_16, global alignment, Q>=128, 256E<=h<4QE, 𝔮>=128):
- **(R1).** Unchanged (§6: decomposition (6.1)/(6.2), three-term obstruction).
- **(R2): (𝒦) with 2a>=d'.**
  - Constant T: closed at n=256 for every D (Cor. 3.2), and in general whenever a<d'. Open for a>=d' (n>=512) with D∈{1,2} (FNAP still covers D>=4, n>=4D).
  - Non-constant T: closed in the ranges of Cor. 5.3. Open:
    - 𝔮<2E/Q (r=4, 8 at n=256), 𝔮<8E/Q (r=16, n=256);
    - 𝔮<nE/(16Q) (r=4, n>=512; r=8, n∈{512,1024});
    - r=8 with n>=2048;
    - r=16 with n>=512.
- **(R3), (R4), (H_lift):** as in R18-T/R19.

**Next steps (HEURISTIC).**
1. **n=256, small 𝔮.**
   - Theorem 5.1 needs m=min(ρ𝔮,E)>a−(d'−E)≈0.3–0.4E. Below 𝔮≈2E/Q the order at z(u) is only ρ𝔮.
   - The order of Ξ(u,·) at u is ρ𝔮·ord_uσ_u. If the FN relation c(u)^[Q]∥B(u)c(u), differentiated along Γ (c(u) moves with u), forced ord_uσ_u>=2 at good u, then m would double, and the gap would shrink by a factor 2 per extra order.
   - This needs a Hasse-derivative computation of σ_u at u, using that c(u)^[2] is a separable function.
2. **n>=512 in (𝒦).**
   - There a>d', and Lemma 4.2 is vacuous.
   - Reduce V_u modulo F·(forms of degree a−d') restricted to ℓ_u. The restriction F|_{ℓ_u}=t^E·P̃_u(t) is itself E-sparse (Prop. 1.2: a polynomial in t^E with linear coefficients). So on the subline the question is exactly Lemma 2.1 with K>=2: does the residue of V_u modulo F|_{ℓ_u} have small sparsity level s? This is the right form of the a/E question at n>=512. It is OPEN, and the toy evidence (Prop. 2.3(ii)) says it is not forced by local data alone.
3. **(R1).** A Frobenius three-term (Mason–Stothers / Voloch-type) count for βΠ_11^X+√(αβ)Π_12^X+αΠ_22^X on 𝒵'.

---

## 8. Computations (`scripts/`, all run with `python3 -I`, single process, each < 1 min)

| script → output | content | result |
|---|---|---|
| `numerics_R20.py` → `numerics_R20.out` | exact Fraction evaluation of R19 (4.1) (mode R19), (4.1) with N4 (Prop. 5.2), (4.1′) (Thm 5.1); all d'∈[2E−2,2E+4]; Q∈{128,…,16384}, S∈{64,256}, r∈{4,8,16}, strip n; Prop. 3.1 check a_max<d' | reproduces R19 Cor. 4.2; Cor. 5.3 table; a_max/d'<=0.7007 at n=256 (constant T closed), fails at n=512; self-check 0/2564 mismatches |
| `toy_line_order.py` → `.out` | Fermat σ1, E=8, GF(2^12): contact; order of A|_{ℓ_u} at z(u) for forms with order N along Γ' (N=4,8,16,24); residual zeros imposed (k) | contact exactly 8; order = min(N,8) exactly (cap at E attained for N=16, 24); k<=a−E gives ξ≢0, k>a−E forces ℓ_u|A (a=12, 13), 3/3 trials each |
| `fermat_cluster.py` → `.out` | Example 2.4: invariant twist on Fermat E=8, GF(2^12) | 4221 points; Ξ(u,v_ζ) independent of ζ for all u; N_Ξ histogram {0: 4214, 6: 7} |
| `env_lib.py`, `numerics_K.py` | R19 helpers (copied) | read, not executed |

Checksums: `scripts/SHA256SUMS.txt`.

---

## 9. Status

| item | status |
|---|---|
| (1.1) V_u(z(v))=κ_u p(v)Ξ(u,v) | PROVED (R19 Lemma 3.1 + Lemma 3.0) |
| Lemma 2.1 (reduction mod P_u; Hasse-sparsity criterion; projective invariance) | PROVED |
| Prop. 2.2 (reduction = vanishing order for E<=a<2E) | PROVED |
| Prop. 2.3 (obstructions to ≈a/E: pointwise vacuity, E-cap, clustering) | PROVED (i), (iv); (ii), (iii) sharpness COMPUTED |
| Example 2.4 (all-or-nothing Ξ-fibres, invariant twist) | PROVED identity; COMPUTED |
| Cor. 2.5 (bound m_T−1 under plane-polynomial twist) | CONDITIONAL on (H_po), OPEN; exceptional set not bounded |
| Prop. 3.1 ((𝒦) with constant T ⇒ a>=d') | PROVED (FNAM2) |
| Cor. 3.2 ((R2) constant T closed at n=256, every D) | PROVED; a_max<d' COMPUTED exactly |
| Lemma 4.1 (order transfer to ℓ_u) | PROVED |
| Lemma 4.2 (N_Ξ(u)<=a−m+mb(u) off 𝔅 ∪ cusps) | PROVED |
| Lemma 4.3 (|𝔅|<=2deg ψ+2(2a−d')d'+2g−2) | PROVED (FNAM2, R14.1, R19 Lemma 1.1(i), R18-T Prop. 4.1(ii)) |
| Thm 5.1 ((4.1′), no τ_0 restriction, D_1>0) | PROVED (conditional on R19 Thm 4.1's inputs) |
| Prop. 5.2 ((4.1) with N4 term) | PROVED in R19; evaluated here |
| Cor. 5.3 thresholds | COMPUTED exactly; R19 table reproduced |
| (6.1)/(6.2) decomposition; Prop. 6.2 (no polynomial-origin layer for a<d') | PROVED |
| "no cheap factor in (R1)" | HEURISTIC |
| ≈a/E bound on the subline | not obtainable by Frobenius reduction (Prop. 2.2–2.3); in general OPEN |
| (R1); (R2) below the Cor. 5.3 ranges; r=8 n>=2048; r=16 n>=512; constant T with a>=d', D∈{1,2} | OPEN |

Dependencies: R19 v2.1 and R18-T v2.1 (audited, revision-checked); FNAM2/FNAM3/TSYC (PRIMARY, reviewed); R14.1, R16 §1. This note is an unaudited owner v1; its new PROVED claims (Prop. 3.1, Lemmas 4.1–4.3, Thm 5.1, Prop. 6.2) should be audited before use. No manuscript was edited. The goal (classification of hyperovals) is not claimed complete.
