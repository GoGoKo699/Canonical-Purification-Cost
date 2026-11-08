# Thirty milestones for canonical-purification cost

[Learning guide](README.md) · [Educational anchor and bridge](anchor.md) · [Scientific guide](../science/README.md) · [Exact model and theorem](../science/model.md)

The project asks how many independent copies of an unknown mixed state and its complex conjugate are needed to prepare a specified pure correlation. The promised family has a known vacuum direction and one unknown signal direction. Its canonical purification requires coherence between the vacuum pair and the conjugate signal pair. The project determines the exact heralded frontier for hard separate source budgets, retains the robust total-copy theorem for approximate output, and compares samples with matched conjugate purifications.

This map has exactly thirty understanding targets. The allocation follows the proof rather than the chapter order of the educational source.

| Phase | Milestones | Role in the scientific account |
|---|---|---|
| Background/preliminaries | M01–M13 | Connect states, purifications, physical operations, success criteria, sample resources, symmetry, and averaged amplitudes into a precise preparation problem. M13 integrates this framework. |
| Narrative/innovation | M14–M30 | Connect exact filters to polynomial rigidity, the all-allocation LP and the mixed-source binomial frontier; then situate them beside the inherited robust total-copy theorem and matched-purification comparison. M30 integrates the result and its limits. |

Thirteen foundational milestones are useful because the argument connects three kinds of reasoning: physical operations on states, hard resource accounting, and orthogonal decompositions of functions of an unknown direction. Seventeen narrative milestones then connect local contraction to unrestricted exact processing, hard mixed-source accounting, and the two existing comparisons. The normalized harmonic decomposition supports both the finite exact frontier and the inherited approximate converse, but those results have different success and budget quantifiers. Each phase moves from individual objects and mechanisms to the complete statement it supports.

The sole educational anchor is **[Watrous2018]**, John Watrous, *The Theory of Quantum Information* (2018). Section numbers below refer to that text; the [anchor guide](anchor.md#where-to-enter-the-textbook) supplies the entry points and notation translation. The project derives its Fischer decomposition, normalized projective kernels, and multiplication lemma locally. Their research attribution remains in [harmonic analysis](../science/harmonic_analysis.md#references) and [related work](../references/RELATED_WORK.md); these are scientific source dependencies, rather than additional educational anchors.

Milestone dependencies name earlier milestones. Source pointers distinguish textbook foundations from the authoritative project statement or derivation. The map identifies the conceptual structure of the result; the scientific pages retain the full technical details.

## Phase I: Background/preliminaries

### M01: States, rays, and the supplied basis

**Phase:** Background/preliminaries.

**Central question:** What is unknown about a pure state, and what does a supplied basis make meaningful?

**Understanding target:** A unit vector represents a pure state up to a global phase. The known decomposition into a vacuum direction and a signal space fixes where the unknown vector lives. Componentwise conjugation refers to the supplied basis, while the pair $`\psi\otimes\psi^*`$ is unchanged by the global phase of $`\psi`$. Watrous uses a star for an adjoint; the project uses $`\dagger`$ for adjoints and a star for entrywise conjugation.

**Dependencies and story role:** No earlier milestone is required. This establishes the elementary object on which every source and target depends.

**Conceptual connection:** Phase cancellation makes the prescribed signal-pair vector a well-defined function of an unknown ray. It removes a phase-choice ambiguity without providing its coherent superposition with the vacuum.

**Sources:** [Watrous2018], §§1.1.1 and 2.1.2; [State family and fixed basis](../science/model.md#state-family-and-fixed-basis); [notation translation](anchor.md#translation-into-the-project-model).

### M02: Mixtures and coherent alternatives

**Phase:** Background/preliminaries.

**Central question:** What distinguishes a random mixture of alternatives from their coherent superposition?

**Understanding target:** A density operator describes both pure and mixed states. A probabilistic mixture of orthogonal vacuum and signal states has no off-diagonal coherence between them. The target pure state includes off-diagonal terms between the vacuum pair and the signal pair, even though its single-register reductions are mixed.

**Dependencies and story role:** Uses M01. It identifies the physical feature that the preparation task must create.

**Conceptual connection:** Supplying the two desired marginal states does not already supply the coherence of their specified purification. This distinction gives the copy-cost question its content.

**Sources:** [Watrous2018], §2.1.2; [State family and fixed basis](../science/model.md#state-family-and-fixed-basis); [two-dimensional signal example](anchor.md#a-two-dimensional-signal-example).

### M03: Composite systems and reductions

**Phase:** Background/preliminaries.

**Central question:** How can different joint states have the same observable state on each register?

**Understanding target:** Tensor products describe composite registers, and a partial trace gives the state accessible on a retained register. A joint state contains correlation information beyond its marginals. Independent specimens form a product conditional on the fixed unknown parameter, even when all specimens depend on the same parameter.

**Dependencies and story role:** Uses M01–M02. It extends the local state description to the source streams, target pair, and inaccessible environments.

**Conceptual connection:** The shared parameter $`\psi`$ is distinct from a supplied common environment or a matched purification gauge. This distinction will determine which resources can be simulated by samples.

**Sources:** [Watrous2018], §§1.1.1 and 2.1.3; [State family and fixed basis](../science/model.md#state-family-and-fixed-basis); [access-comparison introduction](../science/access_comparison.md).

### M04: Purifications and a prescribed representative

**Phase:** Background/preliminaries.

**Central question:** What additional choice is made when a purification is required to be canonical?

**Understanding target:** A purification is a pure joint state with a specified reduced density operator. Transforming its environment can leave that reduction unchanged. Fixing a basis defines the canonical vector $`\mathrm{vec}(\sqrt\rho)`$, so preparing this vector imposes a particular correlation structure. Correct marginals alone do not specify it.

**Dependencies and story role:** Uses M01–M03. It turns the distinction between marginal and joint information into an exact output requirement.

**Conceptual connection:** Purification freedom is harmless when any compatible environment is acceptable, but consequential when two outputs must share a prescribed conjugate relation.

**Sources:** [Watrous2018], §§1.1.2–1.1.3 and 2.1.3; [canonical target and its reductions](../science/model.md#state-family-and-fixed-basis); [gauge matching](../science/access_comparison.md#gauge-independence-requires-a-matched-pair).

### M05: Physical operations and operator bounds

**Phase:** Background/preliminaries.

**Central question:** What makes a proposed linear operation a possible quantum operation?

**Understanding target:** Complete positivity expresses compatibility with untouched ancillary systems. A channel preserves trace; an accepted branch may decrease it. For a single successful Kraus operator $`K`$, the condition $`K^\dagger K\leq I`$ bounds the success probability on the entire input space. Correct action on a promised family of vectors does not by itself establish this operator inequality.

**Dependencies and story role:** Uses M02–M03 and the vector language of M01. It establishes the physicality criterion used by both the construction and the converse.

**Conceptual connection:** An attractive target-producing formula becomes a valid protocol only after its full operator norm is controlled.

**Sources:** [Watrous2018], §§1.1.3 and 2.2.2, especially Theorem 2.22; [Complete positivity and exact output](../science/construction.md#complete-positivity-and-exact-output).

### M06: Heralding and unnormalized outputs

**Phase:** Background/preliminaries.

**Central question:** How should the quality and probability of a successful output be kept separate?

**Understanding target:** An instrument records outcomes and their corresponding quantum outputs. A successful branch produces a positive operator $`\tau`$ whose trace is the success probability $`p`$. Its conditional state is $`\tau/p`$ when $`p>0`$. Discarding a failure does not erase the specimens it consumed, and combining accepted outcomes requires retaining their probabilities.

**Dependencies and story role:** Uses M03 and M05. It provides the accounting language for filtering, repetition, and a converse that permits postselection.

**Conceptual connection:** Unnormalized outputs make quantum state transformations and classical outcome probabilities part of the same linear description.

**Sources:** [Watrous2018], §§2.2.2 and 2.3.1–2.3.2; [Fidelity and success conventions](../science/model.md#fidelity-and-success-conventions); [success quantities](../science/converse.md#1-target-success-probability-and-fidelity), (C3)–(C4).

### M07: Fidelity conventions and a meaningful threshold

**Phase:** Background/preliminaries.

**Central question:** What does a fidelity guarantee mean in this project, including after postselection?

**Understanding target:** Watrous Definition 3.11 uses root fidelity. For a normalized output $`\sigma`$ and pure target $`T`$, the project's convention is its square, $`\langle T|\sigma|T\rangle`$. For an accepted output $`\tau`$, the conditional squared fidelity is $`\langle T|\tau|T\rangle/\mathrm{Tr}\tau`$. The known vacuum pair achieves squared fidelity $`1/2`$, so a fixed improvement above this value is the relevant demand.

**Dependencies and story role:** Uses M02, M04, and M06. It fixes the performance criterion before any resource bound is stated.

**Conceptual connection:** A square-root convention or omitted success normalization would change the numerical threshold and the interpretation of the converse.

**Sources:** [Watrous2018], §3.2, Definition 3.11, and §3.2.1; [Fidelity and success conventions](../science/model.md#fidelity-and-success-conventions); [anchor translation](anchor.md#translation-into-the-project-model).

### M08: State access and hard budgets

**Phase:** Background/preliminaries.

**Central question:** Which resources are counted when a processor is given samples?

**Understanding target:** The source supplies independent density operators without their purifying environments or preparation unitaries. Hard separate caps bound requests from each stream on every execution branch; a hard total cap bounds their sum. Both count rejected samples, discarded vacuum outcomes and failed repetitions. Coherent processing of received registers and adaptive classical source choices remain allowed.

**Dependencies and story role:** Uses M03 and M05–M07. It specifies the resource whose cost the theorem measures.

**Conceptual connection:** A bound on expected requests, hard separate caps, and a hard total cap are different assertions. The exact frontier uses separate caps; the robust total-copy theorem uses a total cap. An additional stricter total cap cannot be inserted into the binomial formula without another argument.

**Sources:** [Watrous2018], §§2.1.3 and 2.2.2 for the state/channel distinction; [hard-budget model](../science/model.md); [mixed-source frontier](../science/mixed_frontier.md); [preparation-oracle scope](../science/access_comparison.md#preparation-oracle-interpretation-and-scope).

### M09: Repeated copies and symmetric spaces

**Phase:** Background/preliminaries.

**Central question:** What structure is present in many identical pure specimens before any processing occurs?

**Understanding target:** The vector $`\psi^{\otimes N}`$ belongs to the symmetric subspace because exchanging its factors changes nothing. Unequal conjugate specimens occupy $`\mathcal R_{n,m}=\mathrm{Sym}^n(V)\otimes\mathrm{Sym}^m(\overline V)`$; balanced inputs have $`n=m=N`$. Normalized occupation coordinates describe this subspace and make contraction and extraction operators explicit; they do not assume a physical bosonic implementation.

**Dependencies and story role:** Uses M01, M03, and M08. It identifies the finite input space on which collective operations and the stronger-input converse are analyzed.

**Conceptual connection:** Permutation symmetry of the input reduces its mathematical description while leaving the processor unrestricted.

**Sources:** [Watrous2018], §7.1.1; [Symmetric input spaces](../science/construction.md#symmetric-input-spaces); [polynomial realization](../science/harmonic_analysis.md#1-conventions-and-the-polynomial-realization); [unequal pure-copy spaces](../science/exact_frontier.md).

### M10: Unitary invariance and averaged guarantees

**Phase:** Background/preliminaries.

**Central question:** Why is an average over unknown directions useful for a worst-case preparation problem?

**Understanding target:** Haar probability measure treats every signal direction equally. A guarantee valid for every direction implies the corresponding averaged success and overlap guarantees. If $`q(\psi)`$ is success probability and $`g(\psi)`$ is unnormalized target overlap, then $`(\int g)/(\int q)`$ is the fidelity averaged over successful runs; it generally differs from $`\int(g/q)`$.

**Dependencies and story role:** Uses M01, M06–M08. It supplies a probability framework for an impossibility proof without replacing the stated worst-case task.

**Conceptual connection:** The robust converse uses symmetry to analyze the supplied orbit without restricting processors. For the exact frontier, a later proof shows that averaging feasible maps preserves exactness and converts average success into a uniform optimum.

**Sources:** [Watrous2018], §§1.2.2 and 7.2.1; [Target, success probability, and fidelity](../science/converse.md#1-target-success-probability-and-fidelity), (C3)–(C4).

### M11: Polynomial amplitudes and orthogonal components

**Phase:** Background/preliminaries.

**Central question:** How does a finite copy supply restrict dependence on the unknown direction?

**Understanding target:** Coordinates of an unequal input are bihomogeneous polynomials with $`n`$ factors of $`\psi`$ and $`m`$ factors of $`\overline\psi`$. Fixed linear maps preserve this finite polynomial space. Haar integration defines an $`L^2`$ inner product in which functions can be separated into orthogonal harmonic degrees. A projection in this function space is distinct from a projection on input tensors; their norm conversion must be derived.

**Dependencies and story role:** Uses M09–M10 and the inner products of M01. It introduces the mathematical language of the lower bound before its specialized identities.

**Conceptual connection:** Copy number controls polynomial degree. Orthogonality then limits which output amplitudes can overlap coherently.

**Sources:** [Watrous2018], §§1.1.1, 7.1.1, and 7.2.1 for the underlying spaces and measure; [polynomial realization](../science/harmonic_analysis.md#1-conventions-and-the-polynomial-realization), (H1)–(H7); [tensor/function norm conversion](../science/harmonic_analysis.md#5-orbit-weights-and-haar-moments), (H30)–(H31); [exact rigidity and unequal harmonics](../science/exact_frontier.md).

### M12: One representation of an arbitrary processor

**Phase:** Background/preliminaries.

**Central question:** How can a single mathematical description include memory, measurements, discarded systems, and accepted outcomes?

**Understanding target:** A Stinespring representation stores discarded information in an environment. Combining all accepted Kraus operators gives a contraction into output and environment registers. Measurement records can be retained in orthogonal environment states. Output amplitudes are consequently environment-valued functions of $`\psi`$, and orthogonality and norm bounds apply componentwise.

**Dependencies and story role:** Uses M05–M06 and M09–M11. It joins physical admissibility with the function-space description needed for an unrestricted converse.

**Conceptual connection:** The environment preserves every possible way the processor can leave information behind. A bound proved in this representation can cover coherent and adaptive processing without assuming a particular circuit or measurement strategy.

**Sources:** [Watrous2018], §2.2.2, Theorem 2.22, and §2.3; [Stinespring form](../science/converse.md#3-stinespring-form-of-an-unrestricted-success-branch); [vector-valued amplitudes](../science/harmonic_analysis.md#7-vector-valued-amplitudes-and-arbitrary-linear-processors).

### M13: Synthesis of the preparation problem

**Phase:** Background/preliminaries.

**Central question:** What must be specified to make a purification copy-cost statement meaningful?

**Understanding target:** A complete statement fixes the unknown state family, known basis and subspaces, supplied registers, permitted operations, target representative, exact or approximate success criterion, fidelity convention and hard budget convention. These choices determine which simulations and comparisons are valid. The proof needs both a physically valid finite-budget construction and an impossibility bound for every allowed processor.

**Dependencies and story role:** Integrates M01–M12 and completes the background phase. It connects the local definitions into one operational framework.

**Conceptual connection:** The target's coherence, the source's inaccessible environments, and the hard-budget convention jointly define the scientific problem. None can be inferred from the phrase “purification” alone.

**Sources:** [Watrous2018], §§2.1.3, 2.2.2, and 3.2; [model and theorem domains](../science/model.md); [exact pure frontier](../science/exact_frontier.md); [mixed frontier](../science/mixed_frontier.md); [bridge to the proof](anchor.md#from-textbook-foundations-to-the-proof).

## Phase II: Narrative/innovation

### M14: The one-pair mechanism

**Phase:** Narrative/innovation.

**Central question:** What can one pure specimen from each conjugate stream already accomplish?

**Understanding target:** The signal-pair vector has known contraction against $`\Omega_d=\sum_i|i,i\rangle`$. Coherently combining that contraction with retention of the signal pair produces the vacuum/signal target. Physical normalization gives exact success $`2/(d+1)`$. The accepted residual is scalar, so no unknown branch record remains to destroy the required coherence.

**Dependencies and story role:** Uses M04–M09 and M13. It begins the narrative with one complete finite transformation and the normalization obstacle that collective copies address.

**Conceptual connection:** Exact target production and a low success probability are compatible; success probability must remain part of the operational claim.

**Sources:** [Watrous2018], §§1.1.2, 2.2.2; [one-pair filter](../science/construction.md#the-case-of-one-specimen-from-each-stream); [exact frontier](../science/exact_frontier.md); [fixed-reference attribution](../references/RELATED_WORK.md#fixed-reference-superposition).

### M15: Unequal contraction and a common residual

**Phase:** Narrative/innovation.

**Central question:** How can different copy supplies leave the same residual in both target branches?

**Understanding target:** For pure budgets $`(n,m)`$, the annihilator contraction $`C=\sum_i a_i b_i`$ obeys $`Cv_{n,m}=\sqrt{nm}\,v_{n-1,m-1}`$. The extraction isometry $`E=(nm)^{-1/2}\sum_{ij}|i,j\rangle\otimes a_i b_j`$ retains the unknown signal pair. Their combination $`W=(|\mathrm{vac},\mathrm{vac}\rangle C/\sqrt{nm}+E)/\sqrt2`$ therefore sends a promised input to $`T_\psi\otimes v_{n-1,m-1}`$.

**Dependencies and story role:** Uses M09, M12 and M14. It extends the elementary operation to arbitrary supplies before making an optimality assertion.

**Conceptual connection:** The two output alternatives share one residual vector. Whole-space normalization is still required even though their action on each promised input is correct.

**Sources:** [Watrous2018], §§1.1.2, 2.1.3, 7.1.1; [unequal exact filter](../science/exact_frontier.md); [balanced construction](../science/construction.md#contraction-and-extraction).

### M16: One conjugate copy and entire-space contractivity

**Phase:** Narrative/innovation.

**Central question:** Why is the n-by-one filter physical without a residual projection?

**Understanding target:** At $`m=1`$, the residual is $`\mathrm{Sym}^{n-1}(V)`$. The extraction is an isometry and $`CC^\dagger=(d+n-1)I`$ there, so
```math
W^\dagger W=\frac12(I+C^\dagger C/n),
\qquad
\|W\|^2=\frac{d+2n-1}{2n}.
```
Scaling by the reciprocal norm gives exact uniform success $`2n/(d+2n-1)`$. Extending the filter by zero outside the separately symmetric input space and adding the complementary failure effect defines a physical instrument.

**Dependencies and story role:** Uses M05, M09 and M15. It supplies a sharp achievable edge case through an operator bound on all inputs.

**Conceptual connection:** No residual trace removal is needed after the conjugate pool is exhausted. This proves achievability; excluding other processors needs the next two milestones.

**Sources:** [Watrous2018], §§1.1.3, 2.2.2, Theorem 2.22; [pure n-by-one filter and norm](../science/exact_frontier.md).

### M17: Exactness and polynomial rigidity

**Phase:** Narrative/innovation.

**Central question:** What does a pure exact successful output force on every Kraus amplitude?

**Understanding target:** Every accepting Kraus vector must lie on the same target ray, because positive outputs cannot cancel outside that ray. Let its vacuum and signal amplitudes be $`A(z,w)`$ and $`B_{ij}(z,w)`$, of bidegree $`(n,m)`$, with $`r(z,w)=\sum_i z_iw_i`$. Homogenizing exactness on unit physical vectors gives $`rB_{ij}=z_iw_jA`$. Rescaling first and then substituting $`z=x+iy,w=x-iy`$ makes this an independent-variable polynomial identity. For $`d\ge2`$, irreducibility of $`r`$ forces $`A=ra`$ with bidegree $`(n-1,m-1)`$.

**Dependencies and story role:** Uses M04, M06, M11–M12 and M15. It changes an exact output promise into a restriction on every possible accepted map.

**Conceptual connection:** The unit sphere itself is not Zariski dense in independent variables. Homogenization is the step that makes the rigidity argument valid. A zero budget in either pool would require a negative residual bidegree and therefore gives zero exact success.

**Sources:** [Watrous2018], §2.2.2 for Kraus positivity; [polynomial rigidity and zero boundaries](../science/exact_frontier.md).

### M18: Residual optimization and the n-by-one converse

**Phase:** Narrative/innovation.

**Central question:** How does rigidity turn a chosen filter into an optimality theorem?

**Understanding target:** Stacking every residual functional into $`L`$ gives an arbitrary exact accepting Stinespring map $`(I_{\rm out}\otimes L)W`$. With $`X=L^\dagger L\ge0`$, physicality is exactly $`W^\dagger(I_{\rm out}\otimes X)W\le I`$. Haar averaging preserves this feasible set and makes success uniform. At $`m=1`$, the residual representation is irreducible, so its averaged $`X`$ is scalar. The norm from M16 then proves
```math
q_d^*(n,1)=\frac{2n}{d+2n-1}.
```

**Dependencies and story role:** Uses M10, M12 and M16–M17. It completes the arbitrary-processor n-by-one optimum, including multiple Kraus outcomes and discarded environments.

**Conceptual connection:** Covariance is obtained by a lossless optimization reduction; it is not an assumption restricting the original processor.

**Sources:** [Watrous2018], §§2.2.2, 7.1.1, 7.2.1; [exact arbitrary-processor reduction](../science/exact_frontier.md).

### M19: Charged harmonics and normalized orbit weights

**Phase:** Narrative/innovation.

**Central question:** How are unequal copy supplies resolved into quantitative sectors?

**Understanding target:** Assume $`n\ge m`$, put $`r=n-m`$ and $`k=m`$. The input kernel is $`s^rt^k`$, with $`s=\langle\psi,\phi\rangle`$ and $`t=|s|^2`$. It decomposes into multiplicity-free kernels $`s^rQ_j(t)`$, where the normalized Jacobi polynomial has parameters $`(d-2,r)`$ and $`Q_j(1)=1`$. The positive weights $`p_j`$ sum to one. The residual contains precisely sectors $`j=0,\ldots,k-1`$. Rodrigues' formula and its beta integral fix all factorial and dimension factors.

**Dependencies and story role:** Uses M09–M11, M17–M18. It quantifies the exact residual optimization while retaining the phase charge caused by unequal supplies.

**Conceptual connection:** The unequal orbit has a nonzero phase character even though the target is phase invariant. Keeping that character in the residual avoids importing a balanced or unitary-Choi formula.

**Sources:** [Watrous2018], §§7.1.1, 7.2.1 for symmetry and measure; [unequal harmonics and weights](../science/exact_frontier.md); [balanced harmonic derivation](../science/harmonic_analysis.md).

### M20: Gram domination and the all-allocation LP

**Phase:** Narrative/innovation.

**Central question:** Why do scalar inequalities characterize every exact processor?

**Understanding target:** An invariant residual Gram kernel has nonnegative coefficients $`u_0,\ldots,u_{k-1}`$. Multiplication by the target overlap $`(1+t)/2`$ is represented by a tridiagonal matrix $`M`$ from the normalized Jacobi recurrence. Contractivity requires the input Gram kernel to dominate the successful output kernel, giving $`Mu\le p`$. Conversely this domination makes the prescribed map well-defined on every linear combination of orbit vectors, hence a contraction. Thus
```math
q_d^*(n,m)=\max\left\{\sum_{j=0}^{k-1}u_j:\ u\ge0,\ Mu\le p\right\}.
```

**Dependencies and story role:** Uses M05, M11–M12 and M17–M19. It completes the finite exact frontier with both unrestricted necessity and physical sufficiency.

**Conceptual connection:** A positive kernel test must respect all linear dependencies among unknown-state inputs. Its sufficiency proof supplies this missing physical step rather than only a numerical bound.

**Sources:** [Watrous2018], §§1.1.1–1.1.3, 2.2.2, 7.2.1 for foundational tools; [exact LP theorem and proof](../science/exact_frontier.md); [research attribution](../references/RELATED_WORK.md).

### M21: An optimum beyond the inherited residual filter

**Phase:** Narrative/innovation.

**Central question:** What does a small example reveal about exact filter optimization?

**Understanding target:** For $`d=2,n=m=2`$, the LP gives $`q_2^*(2,2)=12/13`$, whereas the inherited top-residual filter succeeds with probability $`1/2`$. On the residual one-pair space, the optimum has $`X=(10/13)P_{\rm singlet}+(14/13)P_{\rm traceless}`$. Although one coefficient exceeds one, the full success effect has eigenvalues $`7/13`$ and $`1`$, with multiplicities five and four. It is therefore contractive.

**Dependencies and story role:** Uses M05, M16 and M19–M20. It connects the abstract optimization to an explicit physical operator and shows why a particular residual projection need not be optimal.

**Conceptual connection:** The constraint belongs to the entire accepted operation, not to each residual coefficient separately. A numerical LP solution is checked against the physical operator; it does not replace the proof of the frontier.

**Sources:** [Watrous2018], §§1.1.3, 2.2.2; [two-by-two example](../science/exact_frontier.md); [verification guide](../verification/README.md).

### M22: Known occupancy flags and the mixed frontier

**Phase:** Narrative/innovation.

**Central question:** Why is extracting pure signals lossless for these mixed sources?

**Understanding target:** Each source is block diagonal in the known vacuum/signal decomposition. Measuring those flags leaves the input unchanged when the outcomes are forgotten. Under hard separate mixed caps $`(A,B)`$, the signal counts are independent $`K\sim\mathrm{Bin}(A,1/2)`$ and $`L\sim\mathrm{Bin}(B,1/2)`$. Exactness of the total accepted pure state forces every positive occupancy-pattern contribution to be exact. Twirling aligns worst-case and average success, so the optimum is exactly
```math
Q_d^*(A,B)=\mathbb E[q_d^*(K,L)].
```

**Dependencies and story role:** Uses M02–M03, M06, M08, M10 and M20. It transfers the exact pure frontier into the actual mixed resource model with both a converse and an attaining count-dependent protocol.

**Conceptual connection:** Pattern positions are accessible classical records independent of the unknown direction. Inaccessible source environments are not being supplied. An additional total cap below $`A+B`$ defines a different task.

**Sources:** [Watrous2018], §§2.2.2, 2.3, 7.2.1; [lossless extraction and binomial theorem](../science/mixed_frontier.md).

### M23: Strong imbalance, source ceilings and complete charging

**Phase:** Narrative/innovation.

**Central question:** Why does a copy product fail to describe every mixed success constraint?

**Understanding target:** Zero pure success when either signal count is zero implies
```math
Q_d^*(A,B)\le(1-2^{-A})(1-2^{-B}).
```
With one conjugate mixed specimen, the exact frontier is $`\mathbb E[K/(d+2K-1)]`$ and is at most $`1/2`$, regardless of the ordinary supply. A bounded attempt with caps $`(A,B)`$ charges all $`A+B`$ requests, including vacua, surplus and rejected filters. Repeating it at most $`R`$ times charges hard caps $`(RA,RB)`$ and gives success $`1-(1-u)^R`$ if each fresh attempt succeeds with probability $`u`$.

**Dependencies and story role:** Uses M06–M08, M18 and M22. It converts exact extraction into the operational success frontier in the most asymmetric regimes.

**Conceptual connection:** An expected waiting time for signals is not a hard cap. Large ordinary supply cannot remove a nonzero chance that the small conjugate supply contains no signal at all.

**Sources:** [Watrous2018], §§1.2.2, 2.3; [mixed boundaries and fully counted repetition](../science/mixed_frontier.md).

### M24: The inherited balanced square-root construction

**Phase:** Narrative/innovation.

**Central question:** How does the earlier construction establish a total-copy upper bound?

**Understanding target:** For $`N`$ pure copies from each stream, the top residual projector produces exact success
```math
q_N=\frac{2N^2}{N^2+d+2N-2}\,p_{N-1}.
```
At $`N=\lceil\sqrt d\rceil`$, its normalization and residual weight are both bounded away from zero. Extracting from $`2N`$ mixed requests per stream gives success at least $`1/(5e)`$ with hard total cost $`4N`$ per attempt. Bounded repetition attains any fixed success below one; preparing the vacuum pair on total failure yields a deterministic fixed-fidelity output.

**Dependencies and story role:** Uses M14–M15, M19 and M22–M23. It retains the established constructive total-copy theorem alongside the sharper finite allocation frontier.

**Conceptual connection:** The inherited construction proves the square-root upper bound without being the optimal exact filter at every finite allocation. Its exact accepted output and approximate deterministic completion have different guarantees.

**Sources:** [Watrous2018], §§1.1.3, 1.2.2, 2.3; [balanced residual filter](../science/construction.md); [total-copy theorem](../science/model.md#the-total-copy-theorem).

### M25: The inherited robust coherence inequality

**Phase:** Narrative/innovation.

**Central question:** What survives when successful output need only be approximately correct?

**Understanding target:** An arbitrary Stinespring contraction has vacuum and signal amplitudes of bounded harmonic degree. In the balanced input, the lower-degree vacuum weight is at most $`\delta_N=1-p_N`$. Multiplication by the signal-pair vector shifts part of the top degree outside the available range; the retained fraction is $`\lambda_N`$. For Haar-average success $`p`$ and unnormalized target overlap $`f`$,
```math
f\le\left(\frac12+\frac{\sqrt{\lambda_N}}2\right)p+\sqrt{\delta_Np}.
```
This bound permits approximate and mixed accepted outputs.

**Dependencies and story role:** Uses M07, M10–M12, M19 and M24. It preserves the robust converse that exact polynomial rigidity alone cannot supply.

**Conceptual connection:** Exactness enables the finite LP; approximate output requires a different argument controlling available coherence. The two theorems must not be interchanged by setting an informal error parameter to zero.

**Sources:** [Watrous2018], §§1.1.1, 2.2.2, 3.2, 7.2.1; [multiplication leakage](../science/harmonic_analysis.md#6-exact-multiplication-leakage); [finite robust converse](../science/converse.md#2-finite-copy-theorem).

### M26: Adaptive simulation and the matching total-copy law

**Phase:** Narrative/innovation.

**Central question:** How does a pure-input lower bound cover adaptive mixed-source access?

**Understanding target:** A hard total mixed budget $`T`$ can be simulated with the stronger resource of $`T`$ pure specimens from each stream. Each requested pure specimen is randomly replaced by the vacuum with probability $`1/2`$, hiding that decision from the simulated processor. No branch runs out of either supply. Applying M25 with $`N=T`$ shows that fixed fidelity above $`1/2`$ at fixed positive success needs $`T=\Omega(\sqrt d)`$. Together with M24, this gives the inherited $`\Theta(\sqrt d)`$ total-copy theorem.

**Dependencies and story role:** Uses M08, M12 and M24–M25. It joins the constructive and unrestricted sides of the robust theorem while covering adaptive source order.

**Conceptual connection:** Padding grants the simulator more resources. It proves a lower bound on the total budget and does not require an individual square-root lower bound on each stream.

**Sources:** [Watrous2018], §2.2.2 for channel simulation; [adaptive stronger-input reduction](../science/converse.md#6-from-independent-mixed-samples-to-the-stronger-pure-input); [constant-error consequences](../science/converse.md#7-constant-error-consequences-and-the-fidelity-threshold).

### M27: Exact frontiers, approximate theorems and the product conjecture

**Phase:** Narrative/innovation.

**Central question:** Which claims can be concluded from the different converses?

**Understanding target:** The exact LP covers every finite pure allocation; the binomial transform covers the stated separate mixed caps. A useful task-specific exact converse is $`q_d^*(n,m)\le\min\{1,2nm/(d+\max(n,m)-1)\}`$. The robust total-copy theorem covers approximate outputs under a total cap. None of these statements is being relabeled as a fixed-approximate-fidelity product law. The simplified interpretation that $`nm`$ of order $`d`$ captures an allocation threshold remains a conjecture here, with its performance regime to be specified.

**Dependencies and story role:** Uses M20, M22–M23 and M25–M26. It integrates the theorem quantifiers before comparisons with different source resources.

**Conceptual connection:** A complete finite optimization can be established while a simple asymptotic description remains unproved. Strongly unequal mixed budgets also retain occupancy ceilings that a product alone would omit.

**Sources:** [Watrous2018], §§2.2.2, 3.2 for operation and fidelity distinctions; [exact bounds and limits](../science/exact_frontier.md); [mixed frontier limits](../science/mixed_frontier.md); [robust model](../science/model.md).

### M28: Matched conjugate environments and Bell contraction

**Phase:** Narrative/innovation.

**Central question:** What extra correlation permits a constant-cost source comparison?

**Understanding target:** A purification paired with its exactly matched conjugate retains accessible environment registers with correlated gauge choices. Bell contraction on a known two-dimensional environment converts one preparation from each source into the flat rank-two canonical target with probability $`1/4`$, independently of that common unknown gauge. Independently randomized purification gauges do not supply this matching. For a general spectrum the accepted vector is proportional to $`\mathrm{vec}(\rho)`$, rather than generally to $`\mathrm{vec}(\sqrt\rho)`$; larger environment dimension changes the probability.

**Dependencies and story role:** Uses M03–M04, M08 and M26–M27. It preserves the access comparison with its exact spectrum, environment and gauge assumptions.

**Conceptual connection:** The environments are physical supplied resources in this comparator. They cannot be inserted into a samples-only processor because they exist in a mathematical dilation.

**Sources:** [Watrous2018], §§2.1.3, 2.2.2, 3.2; [matched Bell contraction and general-spectrum limits](../science/access_comparison.md).

### M29: Shared contraction methods and the composition boundary

**Phase:** Narrative/innovation.

**Central question:** What can the sister relationship explain without transferring a theorem?

**Understanding target:** Quantum program composition and canonical purification both contract separately symmetric copy pools and require whole-space physical normalization. The unitary-Choi task instead supplies accessible program halves with maximally mixed inner marginals, and its polar-normalized successful output is generally approximate. The rank-one conjugate orbit and exact canonical coherence here require their own rigidity and success accounting. Replacing a dimension factor in the unitary theorem would not prove the present LP or mixed frontier.

**Dependencies and story role:** Uses M05, M08, M15, M20 and M27–M28. It connects the common mechanism to its distinct operational consequences and credits inherited transformation tools.

**Conceptual connection:** The relationship is a shared method with a checked boundary, not a black-box reduction between incompatible promises. Classical decision outputs, gate-efficient synthesis and repeated use also require their own arguments.

**Sources:** [Watrous2018], §§2.2.2, 7.1.1; [scientific relationship and attribution](../references/RELATED_WORK.md); [sister model](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/a5a49a020ef9cf29a7beffd0d3129f09d76b712d/science/model.md).

### M30: Synthesis of exact assembly, hard budgets and access

**Phase:** Narrative/innovation.

**Central question:** What is the complete current account of canonical-purification cost?

**Understanding target:** The coherent contraction/extraction mechanism gives physical exact filters. Exact-output rigidity identifies every allowed residual dependence, and positive Gram domination gives an attained all-allocation LP. Known orthogonal occupancy flags convert it losslessly into the hard mixed-budget frontier, retaining source scarcity and all failed consumption. The inherited robust harmonic converse and balanced construction separately establish the fixed-performance total-copy law. Matched conjugate environments describe a different, explicitly supplied resource; the program-composition comparison explains common machinery and its transfer boundary.

**Dependencies and story role:** Integrates M14–M29 and completes the narrative phase. It joins the exact finite frontier, the robust asymptotic theorem and the access comparisons without changing any promise.

**Conceptual connection:** The scientific contribution measures the coherent assembly still needed after both conjugate marginals are supplied. Its scope is fixed by the source registers, exactness, success and budget quantifiers; the remaining product conjecture and implementation questions stay separate.

**Sources:** [Watrous2018], §§2.1.3, 2.2.2, 3.2, 7.1.1, 7.2.1; [scientific guide](../science/README.md); [exact pure frontier](../science/exact_frontier.md); [mixed frontier](../science/mixed_frontier.md); [total-copy theorem](../science/model.md); [access comparison](../science/access_comparison.md); [verification](../verification/README.md).

[Watrous2018]: https://jhwatrous.github.io/TQI.pdf
