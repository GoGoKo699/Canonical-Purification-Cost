# Watrous to canonical purification

Two sources supply independent samples of an unknown mixed state and its complex conjugate. The task is to assemble a specified pure state whose two marginals are those source states. The distinction between having the right marginals and having the required coherence is the starting point of this guide.

The [model and theorem](../science/model.md) give the exact task. The [milestone map](milestones.md) connects its prerequisites and proof into a common reading route. This page translates the selected textbook into the project's notation and identifies the additional arguments supplied by the scientific pages.

## Selected educational anchor

John Watrous, *The Theory of Quantum Information*, Cambridge University Press, **2018**, first published 2018. ISBN **9781107180567**; DOI **10.1017/9781316848142**. The [publisher's front matter][Watrous-frontmatter] fixes this bibliographic identity.

- [Published book and DOI][Watrous-book].
- [Author's book page][Watrous-author], with chapter links and errata.
- [Author-hosted manuscript, standard layout][Watrous], used for the section and theorem pointers below.

The author makes the manuscript available for personal reading and restricts its redistribution. This repository links to that access copy; its own explanations and derivations are in the pages below.

## Where to enter the textbook

Use the sections that supply the concepts needed at each step. The route is organized around the scientific question rather than the order of the entire book.

| Concept needed here | Watrous section | Connection to this project |
| --- | --- | --- |
| Vectors, operators, tensor products, positive operators and norms | §§1.1.1–1.1.3 | Read the state definitions and the operator inequality that makes a success filter physical. |
| Partial trace and purification | §2.1.3 | Distinguish a specified canonical purification from other states with the same marginal. |
| Completely positive maps and their representations | §2.2.2, especially Theorem 2.22 | Express a successful operation by Kraus operators or a Stinespring contraction. |
| Measurement outcomes and their probabilities | §2.3 | Track signal extraction, success flags and failed attempts. |
| Fidelity | §3.2, especially Definition 3.11 | Translate the book's convention into the project's squared target overlap. |
| Symmetric tensor spaces | §7.1.1 | Describe repeated pure specimens and their normalized occupation basis. |
| Unitarily invariant probability | §7.2.1 | Interpret the normalized Haar average in the lower bound. |

These locations are in the [author's standard-layout manuscript][Watrous]. The proof-specific use of each foundation is explained below; the canonical proofs remain in [science/](../science/README.md).

## Translation into the project model

### Vectors, adjoints and conjugates

A vector written as $u$ in the textbook may be written as a ket $|\psi\rangle$ here. The ket records the same finite-dimensional vector; its outer product $|\psi\rangle\langle\psi|$ is a pure-state density operator.

There is a consequential notation change in §1.1.2:

| Operation | Watrous notation | Project notation |
| --- | --- | --- |
| Adjoint, or conjugate transpose | $A^*$ | $A^\dagger$ |
| Entrywise complex conjugation in the fixed basis | $\overline A$ | $A^*$, also written $\overline A$ in representation formulas |
| Identity operator | $1_{\mathcal X}$ | $I$ with a space label when needed |

In particular, the source labeled $\rho_\psi^*$ is the entrywise conjugate state. The operation $K_N^\dagger K_N$ in the construction uses the adjoint. Interchanging these meanings would change both the resource model and the normalization calculation.

### The promised state and the specified purification

The signal space has dimension $d\ge2$. A known reference vector adds one more dimension:

$$
\mathcal H=\operatorname{span}\{|\mathrm{vac}\rangle\}\oplus\mathcal V,
\qquad \mathcal V\cong\mathbb C^d.
$$

Thus $d$ is the signal dimension, the full single-system dimension is $d+1$, and the mixed state has rank two. For an unknown unit vector $|\psi\rangle\in\mathcal V$, the sources and target are

$$
\rho_\psi
=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+|\psi\rangle\langle\psi|}{2},
\qquad
|T_\psi\rangle
=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}.
$$

The second source supplies $\rho_\psi^*$. Its specimens are independent of those from the first source, conditional on the same unknown $\psi$. Both source environments have been discarded.

Section 2.1.3 supplies the language of purification. The extra specification here is that the output must be the displayed vector in the supplied basis. With the convention

$$
\operatorname{vec}(X)=\sum_{i,j}X_{ij}|i,j\rangle,
$$

the target is $\operatorname{vec}(\sqrt{\rho_\psi})$. Its two marginals are $\rho_\psi$ and $\rho_\psi^*$. A different purification can have the same first marginal while failing this output requirement. A common global phase of $\psi$ cancels between $\psi$ and $\psi^*$, so the target depends only on the unknown ray. See [the state family and fixed basis](../science/model.md#state-family-and-fixed-basis).

### Success maps and the copy budget

Theorem 2.22 gives the completely positive map representation used here. In project notation, a success branch has the form

$$
\Lambda(X)=\sum_a K_aXK_a^\dagger,
\qquad
\sum_a K_a^\dagger K_a\le I.
$$

The inequality expresses trace nonincrease: success need not occur on every run. Collecting the outcome label $a$ into an environment gives the contraction form used in [the unrestricted-processor converse](../science/converse.md#3-stinespring-form-of-an-unrestricted-success-branch). Its environment can include discarded registers and measurement records. Consequently, the converse covers collective processing and adaptive instruments.

The resource count is an additional operational assumption, specified in [the model](../science/model.md#allowed-processors-and-the-hard-budget). A hard total budget $t$ bounds the number of mixed specimens requested on **every execution branch**, counting both streams and all failed attempts. The balanced pure input used in the proofs has $N$ copies of each pure signal. That $N$ is a proof parameter; it is not the mixed-source total budget. The reduction uses a stronger pure supply to simulate any mixed-source protocol. It yields a lower bound on the total number of mixed samples, without requiring a separate lower bound for each stream.

### Fidelity conventions

Watrous's Definition 3.11 uses root fidelity:

$$
F_{\mathrm W}(P,Q)=\|\sqrt P\sqrt Q\|_1.
$$

For a normalized state $\sigma$ and this pure target, the project uses

$$
F_\psi(\sigma)
=\langle T_\psi|\sigma|T_\psi\rangle
=F_{\mathrm W}\bigl(\sigma,|T_\psi\rangle\langle T_\psi|\bigr)^2.
$$

If $\tau_\psi$ is an unnormalized accepted output, its success probability is $p_\psi=\operatorname{Tr}\tau_\psi$. The conditional guarantee is

$$
\langle T_\psi|\tau_\psi|T_\psi\rangle\ge F_0p_\psi,
\qquad p_\psi\ge p_{\min}.
$$

Keeping $p_\psi$ in this inequality prevents a rare successful event from being mistaken for a constant-success protocol. The [converse](../science/converse.md#1-target-success-probability-and-fidelity) calls this unnormalized state $\sigma_\psi$ and denotes its probability by $q(\psi)$; its $f/p$ is the success-weighted average conditional fidelity.

The known vacuum-pair output has squared fidelity $1/2$, or root fidelity $1/\sqrt2$, for every $\psi$. The theorem concerns fixed improvements above this baseline: $F_0\in(1/2,1]$ and $p_{\min}\in(0,1)$ for heralded preparation, or $F_0\in(1/2,1)$ for deterministic preparation. The endpoints and hard-budget quantifiers are stated in [the total-copy theorem](../science/model.md#the-total-copy-theorem).

## A two-dimensional signal example

Take $d=2$ and let an unknown phase $\theta$ determine

$$
|\psi_\theta\rangle
=\frac{|1\rangle+e^{i\theta}|2\rangle}{\sqrt2},
\qquad
|\psi_\theta^*\rangle
=\frac{|1\rangle+e^{-i\theta}|2\rangle}{\sqrt2}.
$$

The processor is not given $\theta$. This subfamily provides a small example; the theorem allows every unit vector in the full signal space. Write

$$
|\chi_\theta\rangle
=|\psi_\theta\rangle|\psi_\theta^*\rangle
=\frac{|1,1\rangle+e^{-i\theta}|1,2\rangle
+e^{i\theta}|2,1\rangle+|2,2\rangle}{2}.
$$

The desired vector is $(|\mathrm{vac},\mathrm{vac}\rangle+|\chi_\theta\rangle)/\sqrt2$. Compare it with the incoherent joint state

$$
\omega_\theta
=\frac{|\mathrm{vac},\mathrm{vac}\rangle\langle\mathrm{vac},\mathrm{vac}|}{2}
+\frac{|\chi_\theta\rangle\langle\chi_\theta|}{2}.
$$

All three joint states below have first marginal $\rho_{\psi_\theta}$ and second marginal $\rho_{\psi_\theta}^*$. Their overlaps with the target differ:

| Joint state | Squared target fidelity |
| --- | ---: |
| Independent source pair $\rho_{\psi_\theta}\otimes\rho_{\psi_\theta}^*$ | $1/4$ |
| Incoherent correlated state $\omega_\theta$ | $1/2$ |
| Canonical target state | $1$ |

For the independent pair, the vacuum-pair and signal-pair sectors each have weight $1/4$; each contributes half its weight to the target overlap. For $\omega_\theta$, they instead each have weight $1/2$, but the off-diagonal terms connecting those two sectors are absent. The pure target includes these terms. The marginal calculation therefore cannot certify the requested coherence.

Now change the supplied resource. Let the source retain a two-dimensional environment and supply the matched pair

$$
|R_\theta\rangle
=\frac{|\mathrm{vac}\rangle|0\rangle+|\psi_\theta\rangle|1\rangle}{\sqrt2},
\qquad
|R_\theta^*\rangle
=\frac{|\mathrm{vac}\rangle|0\rangle+|\psi_\theta^*\rangle|1\rangle}{\sqrt2}.
$$

Project their two environment registers onto $|\Phi_2\rangle=(|0,0\rangle+|1,1\rangle)/\sqrt2$. After grouping the environment factors together, the accepted system vector is

$$
(I\otimes\langle\Phi_2|)
(|R_\theta\rangle\otimes|R_\theta^*\rangle)
=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\chi_\theta\rangle}{2\sqrt2}
=\frac{|T_{\psi_\theta}\rangle}{2}.
$$

Its squared norm is $1/4$. One source preparation of each matched purification therefore gives the exact target with that probability. The projection retains both equal environment labels coherently; it does not learn which target branch occurred. The [access comparison](../science/access_comparison.md#bell-contraction-of-a-matched-pair) proves the same identity for any unknown purification gauge when the second purification is its exactly matched conjugate. Independent mixed samples do not include those environment registers.

For comparison, one mixed specimen from each stream yields two pure signals with probability $1/4$ after the known vacuum-versus-signal measurement. Their state is then $\chi_\theta$. The [one-pair success filter](../science/construction.md#the-case-of-one-specimen-from-each-stream) converts this state to the target with probability $2/(d+1)=2/3$, so this particular two-request mixed-sample attempt succeeds with probability $1/6$. Both requests count when it fails. These small-dimensional probabilities illustrate the operations and resource count; the dimension-growing separation follows from the full construction and converse.

## From textbook foundations to the proof

The textbook supplies the language for states, physical maps, error and symmetry. The following steps connect those foundations to the established result.

1. **Specify the transformation and resource.** The [model](../science/model.md) fixes the known vacuum, conjugation basis, flat rank-two spectrum, independent samples, target and hard total budget. These promises determine the task to which the theorem applies.
2. **Resolve the balanced conjugate tensor space.** The [harmonic analysis](../science/harmonic_analysis.md) starts from symmetric tensors and derives the relevant complex-projective decomposition. It computes the highest-sector weight $p_N$ and multiplication coefficient $\lambda_N$, with explicit normalization. Standard Fischer and Jacobi ingredients are attributed there to their research sources. Here $p_N$ is an input-sector weight, distinct from a processor's success probability.
3. **Build a physical coherent filter.** The [construction](../science/construction.md) introduces the contraction $C_N$, extraction map $E_N$ and residual projector $P_{N-1}$. It proves the full success operator satisfies $K_N^\dagger K_N\le I$ before using its action on the promised inputs. Mixed-state extraction and bounded repetition then account for every consumed copy.
4. **Bound every successful processor.** The [converse](../science/converse.md) combines a general Stinespring contraction with the harmonic estimates to control the coherence available at fixed fidelity and success. Haar averaging organizes the proof; the processor is not assumed covariant. The result is robust to approximate outputs and unrestricted joint processing.
5. **Interpret the resource separation.** The [access comparison](../science/access_comparison.md) identifies the extra conjugate correlation supplied by a matched purification pair. The flat spectrum and fixed environment dimension are essential to its exact constant-probability comparison. The result concerns a quantum output and total copy cost; it does not establish an efficient gate decomposition or a classical decision-query separation.

These are locally developed proof steps with their dependencies exposed, rather than an attribution of the square-root copy theorem to the textbook. The [related-work account](../references/RELATED_WORK.md) separates imported mathematical ingredients, earlier preparation results and source-model distinctions. Those primary references support the science; Watrous remains the single educational anchor.

## Reading route

The [30-milestone map](milestones.md) gives the project's connected understanding targets and source pointers. For the direct scientific route, begin with [model.md](../science/model.md), follow either the [construction](../science/construction.md) or [converse](../science/converse.md), and open [harmonic_analysis.md](../science/harmonic_analysis.md) when their shared identities are needed. The [verification guide](../verification/README.md) gives reproducible finite checks and explains their scope alongside the analytical proofs.

[Watrous]: https://jhwatrous.github.io/TQI.pdf
[Watrous-author]: https://jhwatrous.github.io/books-and-courses.html
[Watrous-book]: https://doi.org/10.1017/9781316848142
[Watrous-frontmatter]: https://assets.cambridge.org/97811071/80567/frontmatter/9781107180567_frontmatter.pdf
