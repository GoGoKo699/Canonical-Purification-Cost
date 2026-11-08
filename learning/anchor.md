# Watrous to canonical purification

Two sources supply independent samples of an unknown mixed state and its complex conjugate. The task is to assemble a specified pure state whose two marginals are those source states. The distinction between having the right marginals and having the required coherence is the starting point of this guide.

The [model](../science/model.md) gives the source and output promises. The [exact pure frontier](../science/exact_frontier.md) determines optimal heralded success under separate pure-copy caps; the [mixed frontier](../science/mixed_frontier.md) counts the actual mixed samples. The robust total-copy theorem additionally permits approximate output. The [milestone map](milestones.md) connects its prerequisites and proof into a common reading route. This page translates the selected textbook into the project's notation and identifies the additional arguments supplied by the scientific pages.

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

A vector written as $`u`$ in the textbook may be written as a ket $`|\psi\rangle`$ here. The ket records the same finite-dimensional vector; its outer product $`|\psi\rangle\langle\psi|`$ is a pure-state density operator.

There is a consequential notation change in §1.1.2:

| Operation | Watrous notation | Project notation |
| --- | --- | --- |
| Adjoint, or conjugate transpose | $`A^*`$ | $`A^\dagger`$ |
| Entrywise complex conjugation in the fixed basis | $`\overline A`$ | $`A^*`$, also written $`\overline A`$ in representation formulas |
| Identity operator | $`1_{\mathcal X}`$ | $`I`$ with a space label when needed |

In particular, the source labeled $`\rho_\psi^*`$ is the entrywise conjugate state. The operation $`K_N^\dagger K_N`$ in the construction uses the adjoint. Interchanging these meanings would change both the resource model and the normalization calculation.

### The promised state and the specified purification

The signal space has dimension $`d\ge2`$. A known reference vector adds one more dimension:

```math
\mathcal H=\mathrm{span}\{|\mathrm{vac}\rangle\}\oplus\mathcal V,
\qquad \mathcal V\cong\mathbb C^d.
```

Thus $`d`$ is the signal dimension, the full single-system dimension is $`d+1`$, and the mixed state has rank two. For an unknown unit vector $`|\psi\rangle\in\mathcal V`$, the sources and target are

```math
\rho_\psi
=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+|\psi\rangle\langle\psi|}{2},
\qquad
|T_\psi\rangle
=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}.
```

The second source supplies $`\rho_\psi^*`$. Its specimens are independent of those from the first source, conditional on the same unknown $`\psi`$. Both source environments have been discarded.

Section 2.1.3 supplies the language of purification. The extra specification here is that the output must be the displayed vector in the supplied basis. With the convention

```math
\mathrm{vec}(X)=\sum_{i,j}X_{ij}|i,j\rangle,
```

the target is $`\mathrm{vec}(\sqrt{\rho_\psi})`$. Its two marginals are $`\rho_\psi`$ and $`\rho_\psi^*`$. A different purification can have the same first marginal while failing this output requirement. A common global phase of $`\psi`$ cancels between $`\psi`$ and $`\psi^*`$, so the target depends only on the unknown ray. See [the state family and fixed basis](../science/model.md#state-family-and-fixed-basis).

### Success maps and the copy budget

Theorem 2.22 gives the completely positive map representation used here. In project notation, a success branch has the form

```math
\Lambda(X)=\sum_a K_aXK_a^\dagger,
\qquad
\sum_a K_a^\dagger K_a\le I.
```

The inequality expresses trace nonincrease: success need not occur on every run. Collecting the outcome label $`a`$ into an environment gives the contraction form used in [the unrestricted-processor converse](../science/converse.md#3-stinespring-form-of-an-unrestricted-success-branch). Its environment can include discarded registers and measurement records. Consequently, the converse covers collective processing and adaptive instruments.

The resource count is an additional operational assumption. The exact frontier and the robust total-copy theorem use distinct caps:

| Model | Hard budget on every branch | Performance quantity |
|---|---|---|
| Pure signals | At most $`n`$ specimens of $`\psi`$ and $`m`$ of $`\psi^*`$ | Best worst-case exact heralded success $`q_d^*(n,m)`$ |
| Independent mixed samples | At most $`A`$ requests for $`\rho_\psi`$ and $`B`$ for $`\rho_\psi^*`$ | Best worst-case exact heralded success $`Q_d^*(A,B)`$ |
| Total mixed-copy theorem | At most $`t`$ requests across both streams | Fixed conditional fidelity and success, or fixed deterministic fidelity |

Every request counts, including vacua, surplus and failed attempts. A hard cap is different from the mean time needed to collect enough signals. The mixed binomial theorem assumes the separate caps without an additional stricter total cap below $`A+B`$. Adaptive source order is included by supplying both full capped pools in advance and discarding unused registers.

The inherited total-copy converse instead grants a stronger balanced pure supply with $`N=t`$ specimens per stream to simulate every adaptive request. Its parameter $`N`$ is not a mixed total cost and does not imply a separate square-root lower bound on each stream. See the [exact pure](../science/exact_frontier.md), [exact mixed](../science/mixed_frontier.md) and [robust total-copy](../science/converse.md) accounts.

### Fidelity conventions

Watrous's Definition 3.11 uses root fidelity:

```math
F_{\mathrm W}(P,Q)=\|\sqrt P\sqrt Q\|_1.
```

For a normalized state $`\sigma`$ and this pure target, the project uses

```math
F_\psi(\sigma)
=\langle T_\psi|\sigma|T_\psi\rangle
=F_{\mathrm W}\bigl(\sigma,|T_\psi\rangle\langle T_\psi|\bigr)^2.
```

If $`\tau_\psi`$ is an unnormalized accepted output, its success probability is $`p_\psi=\mathrm{Tr}\tau_\psi`$. The conditional guarantee is

```math
\langle T_\psi|\tau_\psi|T_\psi\rangle\ge F_0p_\psi,
\qquad p_\psi\ge p_{\min}.
```

Keeping $`p_\psi`$ in this inequality prevents a rare successful event from being mistaken for a constant-success protocol. The [converse](../science/converse.md#1-target-success-probability-and-fidelity) calls this unnormalized state $`\sigma_\psi`$ and denotes its probability by $`q(\psi)`$; its $`f/p`$ is the success-weighted average conditional fidelity.

For the exact frontier, the successful normalized output must equal $`|T_\psi\rangle\langle T_\psi|`$ for every $`\psi`$; success probability may vary before the covariance reduction. The exactness condition is stronger than a fixed approximate-fidelity guarantee and enables the polynomial argument below.

The known vacuum-pair output has squared fidelity $`1/2`$, or root fidelity $`1/\sqrt2`$, for every $`\psi`$. The inherited total-copy theorem concerns fixed improvements above this baseline: $`F_0\in(1/2,1]`$ and $`p_{\min}\in(0,1)`$ for heralded preparation, or $`F_0\in(1/2,1)`$ for deterministic preparation. The endpoints and hard-budget quantifiers are stated in [the total-copy theorem](../science/model.md#the-total-copy-theorem).

## A two-dimensional signal example

Take $`d=2`$ and let an unknown phase $`\theta`$ determine

```math
|\psi_\theta\rangle
=\frac{|1\rangle+e^{i\theta}|2\rangle}{\sqrt2},
\qquad
|\psi_\theta^*\rangle
=\frac{|1\rangle+e^{-i\theta}|2\rangle}{\sqrt2}.
```

The processor is not given $`\theta`$. This subfamily provides a small example; the theorem allows every unit vector in the full signal space. Write

```math
|\chi_\theta\rangle
=|\psi_\theta\rangle|\psi_\theta^*\rangle
=\frac{|1,1\rangle+e^{-i\theta}|1,2\rangle
+e^{i\theta}|2,1\rangle+|2,2\rangle}{2}.
```

The desired vector is $`(|\mathrm{vac},\mathrm{vac}\rangle+|\chi_\theta\rangle)/\sqrt2`$. Compare it with the incoherent joint state

```math
\omega_\theta
=\frac{|\mathrm{vac},\mathrm{vac}\rangle\langle\mathrm{vac},\mathrm{vac}|}{2}
+\frac{|\chi_\theta\rangle\langle\chi_\theta|}{2}.
```

All three joint states below have first marginal $`\rho_{\psi_\theta}`$ and second marginal $`\rho_{\psi_\theta}^*`$. Their overlaps with the target differ:

| Joint state | Squared target fidelity |
| --- | ---: |
| Independent source pair $`\rho_{\psi_\theta}\otimes\rho_{\psi_\theta}^*`$ | $`1/4`$ |
| Incoherent correlated state $`\omega_\theta`$ | $`1/2`$ |
| Canonical target state | $`1`$ |

For the independent pair, the vacuum-pair and signal-pair sectors each have weight $`1/4`$; each contributes half its weight to the target overlap. For $`\omega_\theta`$, they instead each have weight $`1/2`$, but the off-diagonal terms connecting those two sectors are absent. The pure target includes these terms. The marginal calculation therefore cannot certify the requested coherence.

Now change the supplied resource. Let the source retain a two-dimensional environment and supply the matched pair

```math
|R_\theta\rangle
=\frac{|\mathrm{vac}\rangle|0\rangle+|\psi_\theta\rangle|1\rangle}{\sqrt2},
\qquad
|R_\theta^*\rangle
=\frac{|\mathrm{vac}\rangle|0\rangle+|\psi_\theta^*\rangle|1\rangle}{\sqrt2}.
```

Project their two environment registers onto $`|\Phi_2\rangle=(|0,0\rangle+|1,1\rangle)/\sqrt2`$. After grouping the environment factors together, the accepted system vector is

```math
(I\otimes\langle\Phi_2|)
(|R_\theta\rangle\otimes|R_\theta^*\rangle)
=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\chi_\theta\rangle}{2\sqrt2}
=\frac{|T_{\psi_\theta}\rangle}{2}.
```

Its squared norm is $`1/4`$. One source preparation of each matched purification therefore gives the exact target with that probability. The projection retains both equal environment labels coherently; it does not learn which target branch occurred. The [access comparison](../science/access_comparison.md#bell-contraction-of-a-matched-pair) proves the same identity for any unknown purification gauge when the second purification is its exactly matched conjugate. Independent mixed samples do not include those environment registers.

For comparison, one mixed specimen from each stream yields two pure signals with probability $`1/4`$ after the known vacuum-versus-signal measurement. Their state is then $`\chi_\theta`$. The [one-pair filter](../science/construction.md#the-case-of-one-specimen-from-each-stream) converts it to the target with probability $`2/(d+1)=2/3`$. The two-request mixed attempt therefore succeeds with probability $`1/6`$. The exact frontier proves this is optimal under these separate hard caps: zero-signal sectors cannot succeed, and the one-pair pure optimum is $`2/3`$. Both requests count on failure.

Increasing a **pure** ordinary supply while retaining one pure conjugate specimen gives a second complete example:

| Signal dimension | Pure budgets $`(n,m)`$ | Optimal exact success |
|---|---|---|
| $`d=2`$ | $`(1,1)`$ | $`2/3`$ |
| $`d=2`$ | $`(2,1)`$ | $`4/5`$ |
| $`d=2`$ | $`(3,1)`$ | $`6/7`$ |
| $`d=2`$ | $`(2,2)`$ | $`12/13`$ |

The first three entries follow from $`q_d^*(n,1)=2n/(d+2n-1)`$. The fourth comes from the full residual optimization; the earlier top-residual projection gives only $`1/2`$ at that same allocation. The [exact proof](../science/exact_frontier.md) explains both the norm calculation and the unrestricted converse.

A single **mixed** conjugate specimen instead contains a usable conjugate signal with probability only $`1/2`$. Thus even an arbitrarily large ordinary mixed supply cannot make $`Q_d^*(A,1)`$ exceed $`1/2`$. The distinction between the pure table and this ceiling is a source-access distinction, not a change in target accuracy. The [mixed frontier](../science/mixed_frontier.md) retains this occupancy probability exactly.

## From textbook foundations to the proof

The textbook supplies the language for states, physical maps, error and symmetry. The scientific pages supply the task-specific transformations and converses.

### Exact heralded success at fixed allocations

1. **Start with a physical filter.** In the [exact pure frontier](../science/exact_frontier.md), contraction and extraction give $`Wv_{n,m}=T_\psi\otimes v_{n-1,m-1}`$. Correct promised action alone does not prove admissibility. At $`m=1`$, $`CC^\dagger=(d+n-1)I`$ and $`E^\dagger E=I`$ give $`\|W\|^2=(d+2n-1)/(2n)`$. Scaling $`W`$ by its reciprocal norm yields the exact n-by-one success in the table.
2. **Use exactness before symmetry.** Positivity forces every accepting Kraus vector onto the target ray. Its vacuum and signal polynomial components obey $`rB_{ij}=z_iw_jA`$, where $`r=\sum_i z_iw_i`$. One must homogenize and rescale the unit-vector equation before treating $`z,w`$ as independent variables. Irreducibility of $`r`$ then forces the residual degree to be $`(n-1,m-1)`$. This also proves zero exact success at a zero pure budget.
3. **Retain every processor through its residual.** An exact accepting Stinespring operator has the form $`(I_{\rm out}\otimes L)W`$. Its positive residual operator $`X=L^\dagger L`$ obeys $`W^\dagger(I_{\rm out}\otimes X)W\le I`$. Haar averaging preserves feasibility and makes success uniform. An irreducible n-by-one residual then proves the sharp upper bound matching step 1.
4. **Resolve unequal supplies quantitatively.** For $`n\ge m`$, the residual has $`m`$ irreducible harmonic sectors with phase charge $`n-m`$. The [pure-frontier page](../science/exact_frontier.md) derives their normalized Jacobi kernels and exact orbit weights, including the Rodrigues beta integral. These are locally supplied mathematical steps, rather than a claim that the textbook states the new allocation theorem.
5. **Turn kernel bounds into an operation.** A positive residual kernel has nonnegative coefficients $`u_j`$. Multiplication by the target overlap $`(1+t)/2`$ gives the matrix $`M`$ of the exact LP. Gram domination is equivalent to $`Mu\le p`$, and its sufficiency proof checks every linear dependence among orbit vectors before defining a physical contraction. This makes the LP an attained frontier, rather than only a converse.
6. **Count the actual mixed source.** The [mixed-frontier proof](../science/mixed_frontier.md) measures known vacuum/signal blocks without disturbance. Positivity forces exactness separately in every pattern, while conditioning on its signal counts attains the pure optimum. Thus
   $`Q_d^*(A,B)=\mathbb E[q_d^*(K,L)]`$, with independent $`K\sim\mathrm{Bin}(A,1/2)`$ and $`L\sim\mathrm{Bin}(B,1/2)`$ counts. This identity includes all requests, zero-signal events and rejected filters. Bounded repetition charges new hard caps instead of an unbounded expected waiting time.

### Robust total-copy cost and the access comparison

The inherited [balanced construction](../science/construction.md) projects an unknown residual onto its top traceless sector, checks the full success norm and obtains constant exact acceptance with $`N`$ of order $`\sqrt d`$. Explicit extraction and repetition give the hard total mixed-copy upper bound.

The inherited [converse](../science/converse.md) permits approximate successful outputs. It combines an arbitrary Stinespring contraction with two balanced harmonic quantities: the lower-degree input weight $`\delta_N`$ and the top-degree multiplication retention $`\lambda_N`$. The [harmonic-analysis page](../science/harmonic_analysis.md) derives their normalization. Stronger balanced pure-input simulation then proves the matching total-copy lower bound for adaptive mixed access. This robust argument has a different purpose and different quantifiers from exact polynomial rigidity.

The [access comparison](../science/access_comparison.md) separately assumes physically supplied matched conjugate purifications. Its flat spectrum, known environment dimension and matched gauge enable exact Bell contraction. These assumptions cannot be supplied by merely writing a Stinespring dilation of an independent mixed-state source.

### The sister relationship and its boundary

[Quantum-Program-Composition](https://github.com/GoGoKo699/Quantum-Program-Composition) also contracts separately symmetric copy pools and checks physical normalization on the whole input space. Its theorem supplies full unitary Choi programs with accessible halves and maximally mixed inner marginals. Its polar-normalized successful state is generally approximate. Those promises do not apply to the rank-one signal orbit and exact canonical coherence here.

The shared method therefore motivates a comparison, not a theorem transfer obtained by replacing a dimension factor. The exact LP and binomial frontier are proved for the canonical model itself. The simplified interpretation that $`nm`$ of order $`d`$ describes a product threshold remains conjectural here; no fixed-approximate-fidelity product law or gate-efficient optimal-filter synthesis is claimed.

The [related-work account](../references/RELATED_WORK.md) credits the inherited coherent constructions and general stochastic kernel-transformation framework. These primary references support the research; Watrous remains the sole educational anchor.

## Reading route

The [30-milestone map](milestones.md) gives the project's connected understanding targets and source pointers. For the exact route, begin with the [model](../science/model.md), then read the [pure frontier](../science/exact_frontier.md) and [mixed frontier](../science/mixed_frontier.md). For the robust total-copy route, follow the [balanced construction](../science/construction.md) and [converse](../science/converse.md), opening [harmonic_analysis.md](../science/harmonic_analysis.md) for their shared identities. The [verification guide](../verification/README.md) gives reproducible finite checks and explains their scope alongside the analytical proofs.

[Watrous]: https://jhwatrous.github.io/TQI.pdf
[Watrous-author]: https://jhwatrous.github.io/books-and-courses.html
[Watrous-book]: https://doi.org/10.1017/9781316848142
[Watrous-frontmatter]: https://assets.cambridge.org/97811071/80567/frontmatter/9781107180567_frontmatter.pdf
