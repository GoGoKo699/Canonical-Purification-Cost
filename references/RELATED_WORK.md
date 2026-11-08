# Related work and attribution

[Scientific guide](../science/README.md) · [Model](../science/model.md) · [Structured bibliography](references.bib)

The contribution established here is the sharp total-copy cost for a prescribed canonical purification of a rank-two, flat-spectrum family, with independent conjugate samples already supplied. The fixed-error converse and the exact heralded construction have the same square-root dependence on the signal dimension. The comparison with a matched purification pair uses a known constant environmental dimension. The exact allocation account additionally gives polynomial rigidity, a sharp n-by-one optimum, an attained finite LP for all pure allocations and its lossless binomial mixed-source transform.

This account separates that statement from the broader existence of purification channels, the value of conjugate access, and the general theory of coherent state transformations. Source versions below fix the statements being compared; the distinctions are operational, rather than a claim that the underlying mathematical tools are new.

## Random purification and source access

### Tang–Wright–Zhandry

Ewin Tang, John Wright and Mark Zhandry, [*Conjugate queries can help*, arXiv:2510.07622v2](https://arxiv.org/abs/2510.07622v2), revised 8 May 2026. Theorem 1.5 simulates forward/inverse state-preparation queries using samples and a randomized compatible preparation oracle. Its decision-task consequence and footnote 3 identify a further conjugate-query lifting question, including the obstacle of inconsistent purification choices.

Here, the required output is a specified quantum state. The Bell protocol also assumes a bounded environmental dimension. The present theorem makes no claim to settle that decision-task conjecture or to compare arbitrary black-box oracles without their access promises. The state-pair formulation in [access comparison](../science/access_comparison.md) avoids charging unneeded inverse or controlled queries.

### Girardi–Mele–Lami

Filippo Girardi, Francesco Anna Mele and Ludovico Lami, [*Random purification channel made simple*, arXiv:2511.23451v3](https://arxiv.org/abs/2511.23451v3), revised 22 June 2026. Lemma 1 and the channel construction provide an ensemble of identical, consistently randomized purifications from identical mixed-state samples. Appendix B, Theorem 22, treats a purifying register whose dimension is the promised rank bound.

A common gauge within one identical-copy stream does not supply conjugate-correlated gauges across two separately processed streams. Our matched-source protocol needs precisely that cross-stream relation. Its quantitative reconstruction cost is the subject of the [converse](../science/converse.md). The elementary independent-gauge calculation appears in [access comparison](../science/access_comparison.md).

### Lowe–Tan

Angus Lowe and Xinyu Tan, [*Random dimension reduction and learning symmetric properties of quantum states*, arXiv:2606.23592v2](https://arxiv.org/abs/2606.23592v2), revised 2 October 2026. Theorem 3.4 excludes a proposed exact joint random-purification channel for general pairs. Its contract retains all input data marginals while requiring consistently transformed compressed ancilla marginals; the proof uses no information without disturbance.

The qualitative failure of joint random purification is therefore an antecedent. Our task consumes its source specimens and returns one specified approximate output. Its promised conjugate orbit, error criterion and dimension-dependent copy bound differ from that retained-data no-go theorem.

## Specified purification and universal machines

### Utsumi–Nakata–Wang–Takagi

Takeru Utsumi, Yoshifumi Nakata, Qisheng Wang and Ryuji Takagi, [*Quantum algorithms for Uhlmann transformation*, arXiv:2509.03619v3](https://arxiv.org/abs/2509.03619v3). Section 7.1, Theorem 17, supplies a canonical-purification algorithm from ordinary mixed samples, with explicit dimension, trace-error and minimum-nonzero-eigenvalue dependence. For fixed error and the present flat rank-two spectrum, its bound is linear in ambient dimension up to logarithmic factors.

The square-root upper bound here additionally uses conjugate samples. It should therefore be read as a theorem in a different supplied-resource model, with a matching converse in that model. It is not a same-access improvement of Theorem 17. The distinction between fidelity estimation and transforming prescribed purifications is also relevant to the output contract.

### Liu–Du–Eisert–Cai–Liu

Zhenhuan Liu, Zhenyu Du, Jens Eisert, Zhenyu Cai and Zi-Wen Liu, [*No Universal Purification in Quantum Mechanics*, arXiv:2509.21111v2](https://arxiv.org/abs/2509.21111v2), revised 14 June 2026. Their universal purity and approximate-dilation bounds establish substantial obstructions for arbitrary input families; Theorem 2 gives a dimension-growing pure-dilation lower bound using a classical diagonal family.

The present theorem fixes a rank-two spectrum and supplies both conjugate marginals. Its role is to quantify the remaining coherent assembly cost on this particular orbit. It does not claim the first large sample obstruction to purification in general.

### Del Toro–Bavaresco

Zoe G. del Toro and Jessica Bavaresco, [*Probabilistic and approximate universal quantum purification machines*, arXiv:2604.06325v2](https://arxiv.org/abs/2604.06325v2), revised 7 May 2026. Theorem 1 excludes exact probabilistic purification when a promised family contains a pure state and a nontrivial mixture containing that state. Their approximate problem minimizes over purification gauges, with strategies analyzed under a Haar–Stinespring prior.

Our promised inputs all have rank two, and the output gauge is prescribed. An all-vacuum input component may be rejected by the successful instrument. Those differences prevent the exact positivity argument from applying directly. The many-copy strategy bounds in that work do not establish the conjugate-sample frontier proved here.

## Superposition and covariant transformation

### Fixed-reference superposition

Michał Oszmaniec, Andrzej Grudka, Michał Horodecki and Antoni Wójcik, [*Creation of superposition of unknown quantum states*, arXiv:1505.04955v4](https://arxiv.org/abs/1505.04955v4), Physical Review Letters **116**, 110403 (2016), give a fixed-reference-overlap superposition protocol and its one-copy optimality statement. The signal-pair vector in this project has a known overlap with a normalized maximally entangled vector, so the one-pair construction belongs to that established setting.

Ming-Xing Luo, Hui-Ran Li, Hong Lai and Xiaojun Wang, [*Unified quantum no-go theorems and transforming of quantum states in a restricted set*, arXiv:1701.04166v2](https://arxiv.org/abs/1701.04166v2), Quantum Information Processing **16**, 297 (2017), extend such constructions to multiple inputs. Section IV.B, Theorem 8, uses prescribed overlaps with an entangled reference and projects the residual systems onto that reference.

The [collective construction](../science/construction.md) instead retains an unknown traceless residual state that factors from the accepted target. Its norm and orbit weight give constant success at the square-root copy scale. The [robust converse](../science/converse.md) allows every successful operation, including approximate output and residual states outside this construction.

### The phase-selection obstruction

Zuzana Gavorová, [*Topologically driven no-superposing theorem with a tight error bound*](https://doi.org/10.22331/q-2025-11-20-1916), Quantum **9**, 1916 (2025), establishes a finite-error obstruction to uniformly superposing unknown states on the full pure-state domain. Here the vector formed from a state and its conjugate is invariant under the unknown state's global phase. The promised target is therefore a continuous function of the ray and does not require the forbidden phase choice. The restriction to this orbit is essential.

### Covariant conversion and harmonic analysis

Iman Marvian and Robert W. Spekkens, [*The asymmetry properties of pure quantum states*, arXiv:1105.1816v2](https://arxiv.org/abs/1105.1816v2), Physical Review A **90**, 014102 (2014), give a characteristic-function framework for pure-state transformations under symmetry. That framework is background for orbit-based reasoning. The explicit projective harmonic weights and multiplication estimate used in our approximate arbitrary-processor bound are developed in [harmonic analysis](../science/harmonic_analysis.md).

For exact stochastic conversion, Iman Marvian and Robert W. Spekkens, [*The theory of manipulations of pure state asymmetry: basic tools and equivalence classes of states under symmetric operations*, arXiv:1104.0018v2](https://arxiv.org/abs/1104.0018v2), New Journal of Physics **15**, 033001 (2013), §IX, Theorem 26 and Corollary 27, give the general positive-definite characteristic-function criterion. Kernel domination and covariance in [the exact frontier](../science/exact_frontier.md) are instances of that established machinery. The task-specific contribution is the exact residual polynomial support, its unequal charged Jacobi coefficients and the finite hard-allocation optimization. Neither generic stochastic conversion nor Schur's lemma is claimed as a new framework.

Hendrik De Bie, Frank Sommen and Michael Wutzig, [*Plane wave formulas for spherical, complex and symplectic harmonics*, arXiv:1702.00611v2](https://arxiv.org/abs/1702.00611v2), Section 2.2, provide complex harmonic decomposition and reproducing-kernel formulas. The [NIST Digital Library of Mathematical Functions, Chapter 18](https://dlmf.nist.gov/18), supplies standard Jacobi normalization and polynomial identities. These mathematical ingredients are inherited. The scientific pages derive the normalization needed for this input orbit and show how it enters the physical converse.

## Related repository results

These repositories supply relevant scientific antecedents. Links are pinned to the compared source revisions. Quantum-Program-Composition is a sister project sharing a contraction/normalization mechanism; the model differences prevent a black-box transfer of its theorem.

| Repository | Established task and relevant method | Distinction here |
|---|---|---|
| [Quantum-Coherent-Collisions](https://github.com/GoGoKo699/Quantum-Coherent-Collisions/tree/219f590010247124f48feffaf244a60f306335f4) | Coordinatewise amplitude powers from identical pure samples; occupation filters and torus-character converses | The target here combines a known reference with a phase-invariant matrix vectorization; the proof uses projective harmonics of fundamental and conjugate streams |
| [Quantum-Program-Composition](https://github.com/GoGoKo699/Quantum-Program-Composition/tree/a5a49a020ef9cf29a7beffd0d3129f09d76b712d) | Composition of full unitary Choi programs; collective Bell contractions, Gram normalization and traceless mixed tensors | Rank-one signal specimens have different marginals and orbit weights; the required canonical-output coherence is not a composition Choi state |
| [Entanglement-Purification-Rigidity](https://github.com/GoGoKo699/Entanglement-Purification-Rigidity/tree/e0b2346a7e673249582e563825ce466d989d80c0) | Universal nondegradation constraints for separable branches acting on noisy entangled pairs | The present task allows global operations and prepares an unknown prescribed dilation; it imposes no separability or LOCC restriction |

Coherent pooling, contraction sectors and success-weighted error accounting are shared methods. The canonical contributions are the robust total-copy theorem with its matching instrument and purification-pair comparison, and the exact hard-allocation frontier with its arbitrary-processor proof and fully counted mixed reduction. The [sister boundary](../science/mixed_frontier.md#relation-to-program-composition) distinguishes rank-one signal specimens and inaccessible mixed-source environments from accessible unitary Choi programs and approximate polar output. Replacing $`d^2`$ by $`d`$ in the composition law would be invalid. No fixed-approximate-fidelity product law is inferred, and the broad $`nm`$-of-order-$`d`$ interpretation stays conjectural here.
