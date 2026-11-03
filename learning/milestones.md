# Thirty milestones for canonical-purification cost

[Learning guide](README.md) · [Educational anchor and bridge](anchor.md) · [Scientific guide](../science/README.md) · [Exact model and theorem](../science/model.md)

The project asks how many independent copies of an unknown mixed state and its complex conjugate are needed to prepare a specified pure correlation. The promised family has a known vacuum direction and one unknown signal direction. Its canonical purification requires coherence between the vacuum pair and the conjugate signal pair. The result identifies the total copy cost of producing that coherence and compares samples with a source that supplies matched conjugate purifications.

This map has exactly thirty understanding targets. The allocation follows the proof rather than the chapter order of the educational source.

| Phase | Milestones | Role in the scientific account |
|---|---|---|
| Background/preliminaries | M01–M13 | Connect states, purifications, physical operations, success criteria, sample resources, symmetry, and averaged amplitudes into a precise preparation problem. M13 integrates this framework. |
| Narrative/innovation | M14–M30 | Develop the collective construction and its physical normalization, the harmonic quantities shared by both proofs, the unrestricted converse, and the access comparison. M30 integrates the result and its limits. |

Thirteen foundational milestones are useful because the argument connects three kinds of reasoning: physical operations on states, hard resource accounting, and orthogonal decompositions of functions of an unknown direction. Seventeen narrative milestones then follow the two proofs and the operational comparison. The construction and converse meet at the same normalized harmonic decomposition: it measures the residual weight retained by the construction and the coherence available to an arbitrary processor. Each phase moves from individual objects and mechanisms to the complete statement it supports.

The sole educational anchor is **[Watrous2018]**, John Watrous, *The Theory of Quantum Information* (2018). Section numbers below refer to that text; the [anchor guide](anchor.md#where-to-enter-the-textbook) supplies the entry points and notation translation. The project derives its Fischer decomposition, normalized projective kernels, and multiplication lemma locally. Their research attribution remains in [harmonic analysis](../science/harmonic_analysis.md#references) and [related work](../references/RELATED_WORK.md); these are scientific source dependencies, rather than additional educational anchors.

Milestone dependencies name earlier milestones. Source pointers distinguish textbook foundations from the authoritative project statement or derivation. The map identifies the conceptual structure of the result; the scientific pages retain the full technical details.

## Phase I: Background/preliminaries

### M01: States, rays, and the supplied basis

**Phase:** Background/preliminaries.

**Central question:** What is unknown about a pure state, and what does a supplied basis make meaningful?

**Understanding target:** A unit vector represents a pure state up to a global phase. The known decomposition into a vacuum direction and a signal space fixes where the unknown vector lives. Componentwise conjugation refers to the supplied basis, while the pair $\psi\otimes\psi^*$ is unchanged by the global phase of $\psi$. Watrous uses a star for an adjoint; the project uses $\dagger$ for adjoints and a star for entrywise conjugation.

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

**Conceptual connection:** The shared parameter $\psi$ is distinct from a supplied common environment or a matched purification gauge. This distinction will determine which resources can be simulated by samples.

**Sources:** [Watrous2018], §§1.1.1 and 2.1.3; [State family and fixed basis](../science/model.md#state-family-and-fixed-basis); [access-comparison introduction](../science/access_comparison.md).

### M04: Purifications and a prescribed representative

**Phase:** Background/preliminaries.

**Central question:** What additional choice is made when a purification is required to be canonical?

**Understanding target:** A purification is a pure joint state with a specified reduced density operator. Transforming its environment can leave that reduction unchanged. Fixing a basis defines the canonical vector $\operatorname{vec}(\sqrt\rho)$, so preparing this vector imposes a particular correlation structure. Correct marginals alone do not specify it.

**Dependencies and story role:** Uses M01–M03. It turns the distinction between marginal and joint information into an exact output requirement.

**Conceptual connection:** Purification freedom is harmless when any compatible environment is acceptable, but consequential when two outputs must share a prescribed conjugate relation.

**Sources:** [Watrous2018], §§1.1.2–1.1.3 and 2.1.3; [canonical target and its reductions](../science/model.md#state-family-and-fixed-basis); [gauge matching](../science/access_comparison.md#gauge-independence-requires-a-matched-pair).

### M05: Physical operations and operator bounds

**Phase:** Background/preliminaries.

**Central question:** What makes a proposed linear operation a possible quantum operation?

**Understanding target:** Complete positivity expresses compatibility with untouched ancillary systems. A channel preserves trace; an accepted branch may decrease it. For a single successful Kraus operator $K$, the condition $K^\dagger K\leq I$ bounds the success probability on the entire input space. Correct action on a promised family of vectors does not by itself establish this operator inequality.

**Dependencies and story role:** Uses M02–M03 and the vector language of M01. It establishes the physicality criterion used by both the construction and the converse.

**Conceptual connection:** An attractive target-producing formula becomes a valid protocol only after its full operator norm is controlled.

**Sources:** [Watrous2018], §§1.1.3 and 2.2.2, especially Theorem 2.22; [Complete positivity and exact output](../science/construction.md#complete-positivity-and-exact-output).

### M06: Heralding and unnormalized outputs

**Phase:** Background/preliminaries.

**Central question:** How should the quality and probability of a successful output be kept separate?

**Understanding target:** An instrument records outcomes and their corresponding quantum outputs. A successful branch produces a positive operator $\tau$ whose trace is the success probability $p$. Its conditional state is $\tau/p$ when $p>0$. Discarding a failure does not erase the specimens it consumed, and combining accepted outcomes requires retaining their probabilities.

**Dependencies and story role:** Uses M03 and M05. It provides the accounting language for filtering, repetition, and a converse that permits postselection.

**Conceptual connection:** Unnormalized outputs make quantum state transformations and classical outcome probabilities part of the same linear description.

**Sources:** [Watrous2018], §§2.2.2 and 2.3.1–2.3.2; [Fidelity and success conventions](../science/model.md#fidelity-and-success-conventions); [success quantities](../science/converse.md#1-target-success-probability-and-fidelity), (C3)–(C4).

### M07: Fidelity conventions and a meaningful threshold

**Phase:** Background/preliminaries.

**Central question:** What does a fidelity guarantee mean in this project, including after postselection?

**Understanding target:** Watrous Definition 3.11 uses root fidelity. For a normalized output $\sigma$ and pure target $T$, the project's convention is its square, $\langle T|\sigma|T\rangle$. For an accepted output $\tau$, the conditional squared fidelity is $\langle T|\tau|T\rangle/\operatorname{Tr}\tau$. The known vacuum pair achieves squared fidelity $1/2$, so a fixed improvement above this value is the relevant demand.

**Dependencies and story role:** Uses M02, M04, and M06. It fixes the performance criterion before any resource bound is stated.

**Conceptual connection:** A square-root convention or omitted success normalization would change the numerical threshold and the interpretation of the converse.

**Sources:** [Watrous2018], §3.2, Definition 3.11, and §3.2.1; [Fidelity and success conventions](../science/model.md#fidelity-and-success-conventions); [anchor translation](anchor.md#translation-into-the-project-model).

### M08: State access and a hard total budget

**Phase:** Background/preliminaries.

**Central question:** Which resources are counted when a processor is given samples?

**Understanding target:** The source supplies independent density operators without their purifying environments or preparation unitaries. A hard total budget bounds requests on every execution branch across both streams. It includes rejected samples, discarded vacuum outcomes, and failed repetitions. Coherent processing of received registers and adaptive classical source choices remain allowed.

**Dependencies and story role:** Uses M03 and M05–M07. It specifies the resource whose cost the theorem measures.

**Conceptual connection:** A bound on expected requests, a bound for each stream separately, and a hard bound on their total are different assertions. The project proves the last of these.

**Sources:** [Watrous2018], §§2.1.3 and 2.2.2 for the state/channel distinction; [Allowed processors and the hard budget](../science/model.md#allowed-processors-and-the-hard-budget); [preparation-oracle scope](../science/access_comparison.md#preparation-oracle-interpretation-and-scope).

### M09: Repeated copies and symmetric spaces

**Phase:** Background/preliminaries.

**Central question:** What structure is present in many identical pure specimens before any processing occurs?

**Understanding target:** The vector $\psi^{\otimes N}$ belongs to the symmetric subspace because exchanging its factors changes nothing. Balanced conjugate specimens occupy $\mathcal R_N=\operatorname{Sym}^N(V)\otimes\operatorname{Sym}^N(\overline V)$. Normalized occupation coordinates describe this subspace and make contraction and extraction operators explicit; they do not assume a physical bosonic implementation.

**Dependencies and story role:** Uses M01, M03, and M08. It identifies the finite input space on which collective operations and the stronger-input converse are analyzed.

**Conceptual connection:** Permutation symmetry of the input reduces its mathematical description while leaving the processor unrestricted.

**Sources:** [Watrous2018], §7.1.1; [Symmetric input spaces](../science/construction.md#symmetric-input-spaces); [polynomial realization](../science/harmonic_analysis.md#1-conventions-and-the-polynomial-realization).

### M10: Unitary invariance and averaged guarantees

**Phase:** Background/preliminaries.

**Central question:** Why is an average over unknown directions useful for a worst-case preparation problem?

**Understanding target:** Haar probability measure treats every signal direction equally. A guarantee valid for every direction implies the corresponding averaged success and overlap guarantees. If $q(\psi)$ is success probability and $g(\psi)$ is unnormalized target overlap, then $(\int g)/(\int q)$ is the fidelity averaged over successful runs; it generally differs from $\int(g/q)$.

**Dependencies and story role:** Uses M01, M06–M08. It supplies a probability framework for an impossibility proof without replacing the stated worst-case task.

**Conceptual connection:** Averaging the input orbit is an analysis tool. It does not assert that an optimal or admissible processor must be covariant.

**Sources:** [Watrous2018], §§1.2.2 and 7.2.1; [Target, success probability, and fidelity](../science/converse.md#1-target-success-probability-and-fidelity), (C3)–(C4).

### M11: Polynomial amplitudes and orthogonal components

**Phase:** Background/preliminaries.

**Central question:** How does a finite copy supply restrict dependence on the unknown direction?

**Understanding target:** Coordinates of the balanced input are polynomials with $N$ factors of $\psi$ and $N$ factors of $\overline\psi$. Fixed linear maps preserve this finite polynomial space. Haar integration defines an $L^2$ inner product in which functions can be separated into orthogonal harmonic degrees. A projection in this function space is distinct from a projection on input tensors; their norm conversion must be derived.

**Dependencies and story role:** Uses M09–M10 and the inner products of M01. It introduces the mathematical language of the lower bound before its specialized identities.

**Conceptual connection:** Copy number controls polynomial degree. Orthogonality then limits which output amplitudes can overlap coherently.

**Sources:** [Watrous2018], §§1.1.1, 7.1.1, and 7.2.1 for the underlying spaces and measure; [polynomial realization](../science/harmonic_analysis.md#1-conventions-and-the-polynomial-realization), (H1)–(H7); [tensor/function norm conversion](../science/harmonic_analysis.md#5-orbit-weights-and-haar-moments), (H30)–(H31).

### M12: One representation of an arbitrary processor

**Phase:** Background/preliminaries.

**Central question:** How can a single mathematical description include memory, measurements, discarded systems, and accepted outcomes?

**Understanding target:** A Stinespring representation stores discarded information in an environment. Combining all accepted Kraus operators gives a contraction into output and environment registers. Measurement records can be retained in orthogonal environment states. Output amplitudes are consequently environment-valued functions of $\psi$, and orthogonality and norm bounds apply componentwise.

**Dependencies and story role:** Uses M05–M06 and M09–M11. It joins physical admissibility with the function-space description needed for an unrestricted converse.

**Conceptual connection:** The environment preserves every possible way the processor can leave information behind. A bound proved in this representation can cover coherent and adaptive processing without assuming a particular circuit or measurement strategy.

**Sources:** [Watrous2018], §2.2.2, Theorem 2.22, and §2.3; [Stinespring form](../science/converse.md#3-stinespring-form-of-an-unrestricted-success-branch); [vector-valued amplitudes](../science/harmonic_analysis.md#7-vector-valued-amplitudes-and-arbitrary-linear-processors).

### M13: Synthesis of the preparation problem

**Phase:** Background/preliminaries.

**Central question:** What must be specified to make a purification copy-cost statement meaningful?

**Understanding target:** A complete statement fixes the unknown state family, known basis and subspaces, supplied registers, permitted operations, target representative, success criterion, fidelity convention, and hard total budget. These choices determine which simulations and comparisons are valid. The proof needs both a physically valid finite-budget construction and an impossibility bound for every allowed processor.

**Dependencies and story role:** Integrates M01–M12 and completes the background phase. It connects the local definitions into one operational framework.

**Conceptual connection:** The target's coherence, the source's inaccessible environments, and the hard-budget convention jointly define the scientific problem. None can be inferred from the phrase “purification” alone.

**Sources:** [Watrous2018], §§2.1.3, 2.2.2, and 3.2; [Model and total copy complexity](../science/model.md); [bridge to the proof](anchor.md#from-textbook-foundations-to-the-proof).

## Phase II: Narrative/innovation

### M14: The one-pair mechanism

**Phase:** Narrative/innovation.

**Central question:** What can one pure specimen from each conjugate stream already accomplish?

**Understanding target:** The signal-pair vector has a known overlap with the unnormalized vector $\Omega_d=\sum_i|i,i\rangle$. A coherent combination of contraction onto this vector and retention of the signal pair produces the desired vacuum/signal superposition. Physical normalization gives exact success probability $q_1=2/(d+1)$, which decreases with dimension.

**Dependencies and story role:** Uses M04–M09 and the framework of M13. It begins the narrative with a complete local mechanism and identifies what collective processing must improve.

**Conceptual connection:** The unknown global phase cancels, allowing a known-reference superposition mechanism. The quantitative obstacle is the normalization needed for a valid operation.

**Sources:** [Watrous2018], §§1.1.2 and 2.2.2; [one specimen from each stream](../science/construction.md#the-case-of-one-specimen-from-each-stream); [worked signal example](anchor.md#a-two-dimensional-signal-example); [fixed-reference attribution](../references/RELATED_WORK.md#fixed-reference-superposition).

### M15: Collective contraction and extraction

**Phase:** Narrative/innovation.

**Central question:** How can two branches of a collective operation leave the same unknown residual state?

**Understanding target:** On balanced pure inputs, the contraction $C_N$ removes a conjugate pair with amplitude $N$, while the isometry $E_N$ extracts a signal pair. Their coherent combination leaves $v_{N-1}(\psi)$ in both branches and places the target in the output. Equal residual vectors prevent the environment from distinguishing the vacuum and signal alternatives.

**Dependencies and story role:** Uses M09, M12, and M14. It extends the one-pair mechanism to many copies while exposing the remaining operator-norm issue.

**Conceptual connection:** Exact output factorization concerns what happens on the promised orbit. It is the mechanism to preserve, while the next step supplies a physical normalization on all inputs.

**Sources:** [Watrous2018], §§1.1.2, 2.1.3, and 7.1.1; [Contraction and extraction](../science/construction.md#contraction-and-extraction).

### M16: Residual filtering and the whole-space Kraus norm

**Phase:** Narrative/innovation.

**Central question:** Why does filtering the residual systems turn the collective formula into a valid accepted operation?

**Understanding target:** The projector $P_{N-1}$ retains the residual sector annihilated by pair contraction. The identity $C_NC_N^\dagger P_{N-1}=(d+2N-2)P_{N-1}$ controls the contraction branch; the extraction branch is bounded by its isometry property. Together they give $K_N^\dagger K_N\leq I$ on the entire symmetric input space, with a zero extension outside it and a complementary failure outcome.

**Dependencies and story role:** Uses M05–M06 and M15. It supplies the construction's physicality proof before computing accepted probability.

**Conceptual connection:** The residual state may remain unknown because it factors from the target. Its retained weight matters for success, while the operator inequality governs admissibility on arbitrary superpositions of inputs.

**Sources:** [Watrous2018], §§1.1.3 and 2.2.2; [A filter on the residual systems](../science/construction.md#a-filter-on-the-residual-systems); [Complete positivity and exact output](../science/construction.md#complete-positivity-and-exact-output).

### M17: Traces, harmonics, and multiplicity one

**Phase:** Narrative/innovation.

**Central question:** What is the residual sector retained by the filter, and how does it organize the whole input space?

**Understanding target:** In polynomial coordinates, pair contraction becomes a Laplacian and insertion of a trace becomes its Fischer adjoint. Their ladder relation decomposes balanced polynomials into traceless harmonic pieces. Under $U(d)$ these pieces are irreducible and occur once each. The top tensor projector $P_N$ selects the contraction kernel, and its function counterpart selects harmonic degree $N$.

**Dependencies and story role:** Uses M09–M11 and M16. It gives the mathematical decomposition that supports both the success calculation and the converse.

**Conceptual connection:** The same trace-removal operation has an operational role as a filter and an analytic role as separation by harmonic degree. The local proof establishes the representation facts rather than assuming them from permutation symmetry alone.

**Sources:** [Watrous2018], §§1.1.1–1.1.2 and 7.1.1 for foundational linear algebra and symmetry; [Fischer decomposition](../science/harmonic_analysis.md#2-fischer-decomposition-and-the-traceless-sector), (H8)–(H14); [irreducibility and multiplicity one](../science/harmonic_analysis.md#3-irreducibility-and-multiplicity-one), (H15)–(H17).

### M18: Normalized kernels and exact orbit weights

**Phase:** Narrative/innovation.

**Central question:** How much of a coherent input lies in each harmonic sector, with all normalization factors fixed?

**Understanding target:** Probability-normalized Haar measure gives the addition kernel $K_\ell=h_\ell Q_\ell$, with $Q_\ell(1)=1$ and squared radial norm $1/h_\ell$. Expanding the input kernel $t^N$ in these polynomials identifies its sector weights. In particular,

$$
p_N=\|P_Nv_N(\psi)\|^2
=\prod_{j=0}^{N-1}\frac{d-1+j}{d-1+N+j}.
$$

The Haar moment also fixes the conversion between tensor norms and function norms.

**Dependencies and story role:** Uses M10–M11 and M17. It converts the decomposition into quantitative probabilities used by both proofs.

**Conceptual connection:** A reproducing kernel simultaneously records harmonic dimension, normalization, and overlap of the input orbit. Keeping these roles separate prevents dimension factors from being lost.

**Sources:** [Watrous2018], §§1.1.1 and 7.2.1 for inner products and invariant measure; [normalized kernels](../science/harmonic_analysis.md#4-reproducing-kernels-and-the-normalized-jacobi-polynomial), (H18)–(H23); [orbit weights](../science/harmonic_analysis.md#5-orbit-weights-and-haar-moments), (H24)–(H31).

### M19: The square-root scale in the construction

**Phase:** Narrative/innovation.

**Central question:** Why does the collective accepted probability become constant with about a square root of the dimension in copies?

**Understanding target:** Exact accepted probability is

$$
q_N=\frac{2N^2}{N^2+d+2N-2}\,p_{N-1}.
$$

The first factor reflects physical normalization; the second is the residual weight. For $N=\lceil\sqrt d\rceil$ both are bounded away from zero, giving $q_N\geq4/(5e)$. The limit $p_N\to e^{-c^2}$ when $N/\sqrt d\to c$ explains the same scale quantitatively.

**Dependencies and story role:** Uses M16–M18. It turns the valid pure-input mechanism into a constant-success collective protocol.

**Conceptual connection:** Increasing the copy number improves the contraction amplitude while retaining enough residual weight. The prefactor can exceed one; the full product $q_N$ is the accepted probability.

**Sources:** [Watrous2018], §§1.1.3 and 1.2.2 for norm and probability foundations; [Exact success probability](../science/construction.md#exact-success-probability); [uniform square-root bound](../science/construction.md#a-uniform-bound-at-the-square-root-scale); [orbit-weight asymptotics](../science/harmonic_analysis.md#5-orbit-weights-and-haar-moments), (H27)–(H29).

### M20: From mixed specimens to a hard-budget upper bound

**Phase:** Narrative/innovation.

**Central question:** How does the pure-input construction yield the claimed cost for the actual mixed sources?

**Understanding target:** A known vacuum/signal measurement extracts a pure signal specimen with probability $1/2$ without learning its direction. Requesting $2N$ mixed specimens from each stream yields enough signals for one attempt with sufficient probability to guarantee overall success at least $1/(5e)$. Bounded repetition uses a hard maximum of $4Nr$ specimens. On total failure, outputting the vacuum pair gives the stated deterministic fidelity.

**Dependencies and story role:** Uses M06–M08 and M19. It completes the upper bound in the original resource model, including failed extractions and attempts.

**Conceptual connection:** A repeat-until-success intuition becomes a hard-budget theorem only after fixing the number of attempts and specifying the final failure behavior.

**Sources:** [Watrous2018], §§1.2.2 and 2.3.1–2.3.2; [Extracting pure specimens](../science/construction.md#extracting-pure-specimens-from-the-mixed-sources); [Bounded repetition and deterministic output](../science/construction.md#bounded-repetition-and-deterministic-output); [explicit theorem constants](../science/model.md#the-total-copy-theorem).

### M21: The normalized multiplication lemma

**Phase:** Narrative/innovation.

**Central question:** What fraction of a highest-degree amplitude can remain available after multiplication by the signal-pair vector?

**Understanding target:** Multiplication by $\chi(\psi)=\psi\otimes\psi^*$ is an $L^2$ isometry but can raise harmonic degree from $N$ to $N+1$. For every degree-$N$ function, the squared norm retained in degrees at most $N$ is exactly the fraction

$$
\lambda_N
=1-\frac{(N+d-1)^2}{(2N+d-1)(2N+d)}.
$$

Irreducibility makes the relevant compressed operator scalar; its trace, the addition kernel, and a ratio of leading coefficients determine that scalar. The identity extends componentwise to environment-valued functions.

**Dependencies and story role:** Uses M11–M12 and M17–M18. It supplies the main quantitative obstruction to coherent output assembly.

**Conceptual connection:** An isometry can preserve total norm while transferring most of it into a degree unavailable to the other output amplitude. The unavailable component, rather than norm loss, drives the converse.

**Sources:** [Watrous2018], §§1.1.1–1.1.3 and 7.2.1 for the underlying norm and averaging tools; [Exact multiplication leakage](../science/harmonic_analysis.md#6-exact-multiplication-leakage), (H32)–(H37); [vector-valued extension](../science/harmonic_analysis.md#7-vector-valued-amplitudes-and-arbitrary-linear-processors), (H38).

### M22: Harmonic bounds for an arbitrary successful processor

**Phase:** Narrative/innovation.

**Central question:** Why do the harmonic identities constrain a processor that has no imposed symmetry?

**Understanding target:** An arbitrary Stinespring contraction produces vacuum, signal, and irrelevant output sectors with environment-valued amplitudes. Every amplitude is a fixed linear image of $v_N(\psi)$ and hence has harmonic degree at most $N$. The lower-degree vacuum amplitude has average squared norm at most $\delta_N=1-p_N$, because applying a contraction cannot enlarge the corresponding input weight. This identification respects complex conjugation in the tensor-to-function map.

**Dependencies and story role:** Uses M12, M17–M18, and M21. It transfers orbit identities into a restriction on every accepted operation.

**Conceptual connection:** The proof uses symmetry to analyze the supplied family, while retaining arbitrary processors, environments, and accepted measurement records.

**Sources:** [Watrous2018], §2.2.2, Theorem 2.22; [arbitrary linear amplitudes](../science/harmonic_analysis.md#7-vector-valued-amplitudes-and-arbitrary-linear-processors), (H39)–(H40); [Stinespring decomposition](../science/converse.md#3-stinespring-form-of-an-unrestricted-success-branch), (C9)–(C11); [available lower-degree amplitude](../science/converse.md#4-the-available-lower-degree-amplitude), (C12)–(C13).

### M23: Coherence and the finite-copy inequality

**Phase:** Narrative/innovation.

**Central question:** How do unavailable harmonic components limit fidelity above the vacuum baseline?

**Understanding target:** The target overlap consists of diagonal contributions bounded by half the success probability, plus coherence between vacuum and signal amplitudes. Cauchy–Schwarz bounds the lower-degree contribution through $\delta_N$ and the highest-degree contribution through $\lambda_N$. For average success $p$ and average unnormalized overlap $f$, this yields

$$
f\leq\left(\frac12+\frac{\sqrt{\lambda_N}}2\right)p
+\sqrt{\delta_Np}.
$$

It applies to approximate and mixed accepted outputs as well as exact ones.

**Dependencies and story role:** Uses M07, M10, and M21–M22. It completes the robust pure-input converse in a finite form before taking an asymptotic limit.

**Conceptual connection:** High conditional fidelity can be traded against acceptance probability, but at fixed positive success neither a small lower-degree weight nor the inaccessible highest-degree component can be ignored.

**Sources:** [Watrous2018], §§1.1.1 and 3.2.1; [Finite-copy theorem](../science/converse.md#2-finite-copy-theorem), (C5)–(C8); [coherence bound](../science/converse.md#5-bounding-the-coherence-required-by-the-target), (C14)–(C17).

### M24: Adaptive samples and the stronger pure-input reduction

**Phase:** Narrative/innovation.

**Central question:** Why does the balanced pure-input bound constrain every strategy with a hard total mixed-copy budget?

**Understanding target:** A known channel can turn one pure signal specimen into the required vacuum/signal mixture. Supplying a simulator with $T$ pure specimens of each conjugate type therefore covers every branch of a protocol requesting at most $T$ mixed specimens in total. Registers can be prepared in advance and selected adaptively; all subsequent coherent processing belongs to one accepted completely positive map. The bound from M23 applies with $N=T$.

**Dependencies and story role:** Uses M08, M12–M13, and M23. It moves the converse from an analytically convenient stronger resource to the original sample model.

**Conceptual connection:** Giving a lower-bound simulator extra specimens strengthens the input resource and preserves the implication. This proves a bound on the total budget, without proving a separate lower bound for each stream.

**Sources:** [Watrous2018], §§2.2.1–2.2.2 and 2.3; [stronger-input simulation](../science/model.md#why-balanced-pure-inputs-suffice-for-the-lower-bound); [adaptive reduction](../science/converse.md#6-from-independent-mixed-samples-to-the-stronger-pure-input), (C18) and Corollary 2.

### M25: The matching total-copy law

**Phase:** Narrative/innovation.

**Central question:** Which guarantees have matching upper and lower copy bounds?

**Understanding target:** For fixed success threshold $p_{\min}\in(0,1)$ and conditional squared-fidelity threshold $F_0\in(1/2,1]$, the finite converse excludes total budgets below a constant multiple of $\sqrt d$. The construction achieves $O(\sqrt d)$ total cost with exact accepted output and any fixed success below one. A failure fallback also gives the matching deterministic law for fixed $1/2<F_0<1$. Thus both stated costs are $\Theta(\sqrt d)$.

**Dependencies and story role:** Combines M19–M20 with M23–M24. It integrates the two proof directions into the main theorem before comparing access models.

**Conceptual connection:** The guarantee is a fixed improvement above a free baseline. The constants may depend on performance thresholds; the statement neither requires each stream separately to be costly nor asserts exact probability-one preparation.

**Sources:** [Watrous2018], §§2.3 and 3.2 for performance foundations; [The total-copy theorem](../science/model.md#the-total-copy-theorem); [Constant-error consequences and the fidelity threshold](../science/converse.md#7-constant-error-consequences-and-the-fidelity-threshold), (C19)–(C21).

### M26: Bell contraction of a matched purification pair

**Phase:** Narrative/innovation.

**Central question:** What changes when the source supplies a purification and its exact complex conjugate?

**Understanding target:** For a purification with a known $k$-dimensional environment and its matched conjugate, projecting the two environments onto the normalized Bell vector leaves $\operatorname{vec}(\rho)/\sqrt k$. The success probability is $\operatorname{Tr}(\rho^2)/k$. For the project's flat rank-two state this is the desired canonical target on success, with probability $1/(2k)$; a two-dimensional environment gives $1/4$.

**Dependencies and story role:** Uses M03–M08, M14, and M25. It introduces the operational comparator after establishing the cost of independent samples.

**Conceptual connection:** Access to matched source environments permits the required correlation to be assembled from a constant number of supplied purification pairs when their environmental dimension is bounded independently of $d$.

**Sources:** [Watrous2018], §§1.1.2, 2.1.3, and 2.3.1; [Bell contraction of a matched pair](../science/access_comparison.md#bell-contraction-of-a-matched-pair).

### M27: Gauge matching and ordinary random purification

**Phase:** Narrative/innovation.

**Central question:** Which relation between purifying environments is essential to the Bell protocol?

**Understanding target:** Applying an unknown unitary gauge to one purification is harmless when the other receives its complex conjugate: the matching transformations cancel in the Bell contraction. Independent gauge choices do not have this cancellation. Ordinary random-purification constructions can supply a consistent gauge within an identical-copy stream; that does not supply the required conjugate correlation between two separately processed streams. Failure of an independently gauged Bell attempt alone is not a general impossibility proof.

**Dependencies and story role:** Uses M04, M08, M24, and M26. It identifies the extra resource that makes the comparison meaningful.

**Conceptual connection:** An unknown but matched reference can be useful without being learned. The quantitative obstruction for independent samples is supplied by the arbitrary-processor converse, not by a single unsuccessful protocol.

**Sources:** [Watrous2018], §§2.1.3 and 7.2.1; [gauge cancellation and counterexamples](../science/access_comparison.md#gauge-independence-requires-a-matched-pair); [ordinary random purification](../science/access_comparison.md#what-ordinary-random-purification-supplies); [related source-access results](../references/RELATED_WORK.md#random-purification-and-source-access).

### M28: Spectrum and environmental-dimension limits

**Phase:** Narrative/innovation.

**Central question:** Which promises make the matched-pair protocol an exact, constant-success comparison?

**Understanding target:** Bell contraction produces a vector proportional to $\operatorname{vec}(\rho)$, whereas canonical purification uses $\operatorname{vec}(\sqrt\rho)$. These normalized vectors agree for a flat nonzero spectrum. Its probability also contains the inverse environmental dimension, so an arbitrarily large unknown environment does not inherit the constant-success guarantee. Compressing that environment would require an additional operation and its own resource analysis.

**Dependencies and story role:** Uses M04, M07, and M26–M27. It fixes the domain of the access comparison before its broader interpretation.

**Conceptual connection:** The spectrum controls the accepted target and the environment size controls success. Neither promise follows merely from saying that a compatible purification is available.

**Sources:** [Watrous2018], §§1.1.3, 2.1.3, and 3.2.1; [Bell success normalization](../science/access_comparison.md#bell-contraction-of-a-matched-pair); [General-spectrum identity and limits](../science/access_comparison.md#general-spectrum-identity-and-limits-of-the-comparison).

### M29: What the access comparison establishes

**Phase:** Narrative/innovation.

**Central question:** How should the copy theorem and its comparator be situated among purification and query results?

**Understanding target:** The separation concerns producing a specified quantum output from independent samples versus a matched conjugate-purification resource. It does not automatically yield a separation for classical decision problems, where verification of an unknown target is a separate issue. A forward preparation operation and its conjugate suffice for the Bell protocol; they are additional access assumptions. The copy theorem gives information-theoretic operations without a gate-efficiency guarantee.

**Dependencies and story role:** Uses M08, M25, and M26–M28. It connects the result to earlier purification, superposition, and source-simulation questions while retaining their different resource and output requirements.

**Conceptual connection:** Comparisons are meaningful only after aligning the supplied resources, required output, error criterion, and computational cost. Matching one of these features does not align all four.

**Sources:** [Watrous2018], §§2.2.2 and 3.1 for operations and classical state-discrimination outputs; [Preparation-oracle interpretation and scope](../science/access_comparison.md#preparation-oracle-interpretation-and-scope); [Related work and attribution](../references/RELATED_WORK.md).

### M30: Synthesis of the mechanism, converse, and resource distinction

**Phase:** Narrative/innovation.

**Central question:** What is the complete explanation of the square-root copy cost and the matched-purification advantage?

**Understanding target:** The collective filter produces the required coherence with a valid whole-space normalization and enough residual harmonic weight at the square-root scale. Below that scale, arbitrary accepted processors have too little lower-degree weight and too little retained highest-degree overlap to exceed the vacuum baseline by a fixed amount at constant success. Balanced pure-input simulation turns this into a hard total-copy bound. Matched conjugate environments provide a different resource whose Bell contraction bypasses that sample requirement under the stated spectrum and dimension promises.

**Dependencies and story role:** Integrates M14–M29, especially the complete theorem in M25 and the access boundaries in M27–M29. It completes the narrative phase and the common map.

**Conceptual connection:** The result quantifies coherent assembly after both conjugate marginal states are already supplied. Its significance lies in the matching constructive and unrestricted lower bounds, together with a precise account of what additional source correlation changes the cost.

**Sources:** [Watrous2018], §§2.1.3, 2.2.2, 3.2, and 7.2.1 as the shared foundations; [main theorem](../science/model.md#the-total-copy-theorem); [construction conclusion](../science/construction.md#what-the-construction-establishes); [converse conclusion](../science/converse.md#7-constant-error-consequences-and-the-fidelity-threshold); [access comparison](../science/access_comparison.md); [scientific attribution](../references/RELATED_WORK.md).

[Watrous2018]: https://jhwatrous.github.io/TQI.pdf
