# Scientific guide

The task is to prepare the canonical purification of a mixed state whose two nonzero eigenvalues are known. Its unknown eigenvector can occupy an arbitrarily large signal space. Supplying independent conjugate samples removes the need to manufacture the conjugate direction, but leaves a coherence requirement: the known reference branch and the unknown signal-pair branch must be assembled into one pure state.

## Reading route

1. [Model and theorem](model.md) fixes the promised state family, target, squared-fidelity convention, success instrument and hard total-copy budget. It states both the sample-complexity theorem and the matched-purification comparison.
2. [Construction](construction.md) first works with pure signal samples. A collective contraction and a filter on the residual registers produce the target exactly. A fixed-budget extraction step supplies those pure samples from the original mixed sources.
3. [Harmonic analysis](harmonic_analysis.md) develops the common mathematical tool. The balanced input orbit decomposes into projective harmonics. The highest-degree weight and a multiplication coefficient quantify the part of the input that can supply coherent reference-to-signal amplitude.
4. [Converse](converse.md) applies those identities to an arbitrary success Stinespring contraction. The bound controls average unnormalized target fidelity and success together, and therefore covers approximate, adaptive and heralded protocols.
5. [Access comparison](access_comparison.md) derives the two-preparation Bell protocol and explains why the conjugate relation between purifying registers is a real supplied resource. It also identifies the role of the flat spectrum and environmental dimension.

The construction and converse meet at the same total-copy scale. Their combination distinguishes three questions that otherwise look similar: retaining a purification, randomly purifying identical samples, and preparing a prescribed canonical output. The [related-work account](../references/RELATED_WORK.md) compares these operational contracts and identifies the inherited methods.

## Proof and verification

The formulas in the theorem have their proofs in the topic pages above. The [verification code](../verification/README.md) builds the relevant finite matrices from occupation-number actions and checks the complete successful operation. It supplies reproducible checks of normalization and resource interpretation, while the analytical arguments establish the asymptotic and worst-case statements.
