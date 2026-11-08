# Independent samples and matched conjugate purifications

The resource separation concerns a specified coherent quantum output. For the
rank-two family

```math
\mathcal H=\mathbb C|\mathrm{vac}\rangle\oplus\mathbb C^d,
\qquad
\rho_\psi=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|
+|\psi\rangle\langle\psi|}{2},
```

the target is the canonical purification

```math
|T_\psi\rangle
=\frac{|\mathrm{vac},\mathrm{vac}\rangle
+|\psi\rangle|\psi^*\rangle}{\sqrt2}
=\mathrm{vec}(\sqrt{\rho_\psi}).
```

The vacuum vector and the basis defining complex conjugation are known. The
direction $`\psi\in\mathbb C^d`$ is unknown. Throughout,
$`\mathrm{vec}(X)=\sum_{ij}X_{ij}|i\rangle|j\rangle`$, and fidelity with a
pure target means the squared fidelity $`\langle T|\sigma|T\rangle`$.

For every fixed success requirement $`p_{\min}\in(0,1)`$ and fixed conditional fidelity
$`F_0\in(1/2,1]`$, the [rank-two copy theorem](model.md) gives total hard copy complexity
$`\Theta(\sqrt d)`$ from independent samples of $`\rho_\psi`$ and $`\rho_\psi^*`$.
All source calls count, including discarded filtering attempts. The lower bound
permits arbitrary joint processing and arbitrary allocation between the two
streams; it does not assert a separate $`\Omega(\sqrt d)`$ requirement for each
stream. The constructive upper bound prepares the target exactly on success.

A matched purification/conjugate-purification pair supplies a different resource:
one pair with a two-dimensional environment produces the target exactly with
probability $`1/4`$, uniformly over the unknown purification gauge. The following
calculation establishes that comparison and its limits.

## Bell contraction of a matched pair

Let $`|R\rangle\in\mathcal H\otimes\mathbb C^k`$ purify a state $`\rho`$, and write
its coefficient matrix as

```math
|R\rangle=\sum_{i,a}R_{ia}|i\rangle|a\rangle,
\qquad RR^\dagger=\rho.
```

The second supplied state is its exact complex conjugate in the corresponding
bases:

```math
|R^*\rangle=\sum_{j,b}\overline{R_{jb}}|j\rangle|b\rangle.
```

Project the two environment registers onto the normalized Bell state

```math
|\Phi_k\rangle=\frac1{\sqrt k}\sum_{a=1}^k|a,a\rangle.
```

Keeping the system registers, the unnormalized accepted vector is

```math
\begin{aligned}
(I\otimes\langle\Phi_k|)(|R\rangle\otimes|R^*\rangle)
&=\frac1{\sqrt k}\sum_{i,j,a}R_{ia}\overline{R_{ja}}|i,j\rangle\\
&=\frac{\mathrm{vec}(RR^\dagger)}{\sqrt k}\\
&=\frac{\mathrm{vec}(\rho)}{\sqrt k}.
\end{aligned}
```

Here the tensor factors are reordered so the two environment factors are
adjacent. The success probability and normalized accepted state are therefore

```math
p_{\mathrm{Bell}}=\frac{\mathrm{Tr}(\rho^2)}{k},
\qquad
|B_\rho\rangle=
\frac{\mathrm{vec}(\rho)}{\sqrt{\mathrm{Tr}(\rho^2)}}.
```

The probability includes the normalization of the Bell projection. Omitting the
factor $`1/\sqrt k`$ would describe an operator with norm greater than one.

For $`\rho_\psi`$, the nonzero eigenvalues are both $`1/2`$, so
$`\mathrm{Tr}(\rho_\psi^2)=1/2`$ and
$`\mathrm{vec}(\rho_\psi)=|T_\psi\rangle/\sqrt2`$. Consequently,

```math
(I\otimes\langle\Phi_k|)(|R\rangle\otimes|R^*\rangle)
=\frac{|T_\psi\rangle}{\sqrt{2k}},
\qquad p_{\mathrm{Bell}}=\frac1{2k}.
```

| Environment dimension | Exact target probability from one pair |
| --- | ---: |
| $`k=2`$ | $`1/4`$ |
| $`k=4`$ | $`1/8`$ |
| Any fixed $`k\ge2`$ | $`1/(2k)`$ |

Independent repetition gives any fixed success probability below one using a
constant number of pairs when $`k`$ is fixed. The displayed Bell protocol has no
dimension-independent probability guarantee when $`k`$ grows without bound.
Compression of an unknown large purification environment is an additional task,
and is not assumed here.

## Gauge independence requires a matched pair

If an environment unitary $`V`$ changes the first purification to
$`(I\otimes V)|R\rangle`$, its coefficient matrix becomes $`RV^T`$. The conjugate
state has coefficient matrix $`R^*V^\dagger`$. Thus the Bell contraction is still

```math
\frac{RV^T V^* R^\dagger}{\sqrt k}
=\frac{\rho}{\sqrt k}.
```

Neither the purification gauge nor a classical description of it is needed.
The protocol also works if a matched pair is drawn from an unknown distribution
of gauges: every component gives the same accepted system vector. What matters
is the conjugate relation between the two supplied gauges.

To see why arbitrary purifications do not give this identity, write an
eigendecomposition $`\rho=B\Lambda B^\dagger`$, with $`B^\dagger B=I_r`$. Two
purification coefficient matrices can have the forms

```math
R=B\sqrt\Lambda A^T,
\qquad
S=B^*\sqrt\Lambda D^T,
\qquad A^\dagger A=D^\dagger D=I_r.
```

They have system marginals $`\rho`$ and $`\rho^*`$, respectively. Bell contraction
gives the matrix

```math
\frac{RS^T}{\sqrt k}
=\frac{B\sqrt\Lambda\,(A^T D)\,\sqrt\Lambda B^\dagger}{\sqrt k}.
```

For the matched case $`D=A^*`$, the middle factor is $`I_r`$. Independent gauges have
no such identity. For a concrete rank-two example, take $`D=A^*X`$, where $`X`$
swaps the two Schmidt labels. With $`\Lambda=I_2/2`$, the accepted vector is
proportional to

```math
|\mathrm{vac}\rangle|\psi^*\rangle
+|\psi\rangle|\mathrm{vac}\rangle,
```

which is orthogonal to $`|T_\psi\rangle`$. Both supplied system marginals are
unchanged.

There is also an exact one-copy calculation for independently Haar-random
gauges. Averaging either purification over its environment gives
$`\rho\otimes I_k/k`$. Two independent averages therefore have no correlations
between their environments and systems. Bell selection succeeds with probability
$`1/k^2`$ and leaves the conditioned systems in $`\rho\otimes\rho^*`$. For the
rank-two family,

```math
\langle T_\psi|\rho_\psi\otimes\rho_\psi^*|T_\psi\rangle=\frac14.
```

These examples establish the failure of the direct Bell contraction for
unmatched gauges. The many-copy lower bound for arbitrary processors comes from
the separate harmonic analysis, not from these examples.

## What ordinary random purification supplies

Tang, Wright, and Zhandry's random purification channel, and Girardi, Mele, and
Lami's formulation, map identical mixed samples to an average of tensor powers
of a purification with a common random environment gauge. In the finite-rank
form, for a fixed reference purification $`|R_\rho\rangle`$,

```math
\mathcal P^{(n)}(\rho^{\otimes n})
=\mathbb E_V\left[
\left((I\otimes V)|R_\rho\rangle\langle R_\rho|
(I\otimes V^\dagger)\right)^{\otimes n}\right].
```

The same $`V`$ is shared within this identical-copy stream. Girardi, Mele, and
Lami's Theorem 22 allows an environment of dimension $`r`$ when
$`\mathrm{rank}\rho\le r`$. These results therefore already provide small
random purification environments. Independently applying the channels to
$`\rho`$ and $`\rho^*`$ does not assert conjugate correlation between the two
gauges. See [Tang–Wright–Zhandry, Lemma 2.11](https://arxiv.org/pdf/2510.07622v2)
and [Girardi–Mele–Lami, Lemma 1 and Theorem 22](https://arxiv.org/html/2511.23451v3).

Lowe and Tan's Theorem 3.4 gives a related obstruction: no exact channel can,
for all pairs with a common low-dimensional support, retain the entire input
data marginal while producing the specified common-gauge compressed ancilla
marginal. Its conditions differ from consuming samples to prepare one canonical
output. It does not provide the present approximate $`\sqrt d`$ copy bound, but
the general warning that joint random purification cannot be assumed is already
present there. See [Lowe–Tan, Section 3.3 and Theorem 3.4](https://arxiv.org/html/2606.23592v2).

## Preparation-oracle interpretation and scope

Suppose a preparation unitary satisfies $`U|0\rangle=|R\rangle`$, where the input
$`|0\rangle`$ is the known real computational basis vector. Access to $`U^*`$ then
gives $`U^*|0\rangle=|R^*\rangle`$. One forward call to each of $`U`$ and $`U^*`$,
followed by the Bell projection, realizes the protocol. It works for every
purification gauge and every extension of that state preparation to a unitary.
Inverse or controlled queries are unnecessary for this construction.

Access to $`U^*`$ is an input resource. It is not inferred from access to an
unknown state, and complex conjugation is not inserted as an operation available
to the mixed-sample processor. The known basis fixes the meaning of $`\rho^*`$,
$`U^*`$, and the canonical output. It does not reveal the unknown eigenvectors.
The output is insensitive to the phase convention for $`\psi`$, since
$`|\psi\rangle|\psi^*\rangle`$ is unchanged by $`\psi\mapsto e^{i\theta}\psi`$.

Tang, Wright, and Zhandry's Theorem 1.5 simulates ordinary forward/inverse
purification-oracle queries by samples, with a distribution over oracle
extensions; its rank-dependent environment condition permits $`k\ge2r`$. Thus
$`k=4`$ is a constant-size choice for this rank-two comparison. Their footnote 3
discusses lifting decision lower bounds from copies of $`\rho\otimes\rho^*`$ to
conjugate/transpose query access and explicitly identifies inconsistent oracle
choices when the simulation is applied twice. See
[Tang–Wright–Zhandry, Theorem 1.5 and footnote 3](https://arxiv.org/pdf/2510.07622v2).

The present task requires returning a quantum register close to
$`|T_\psi\rangle`$. No conversion of this requirement into a classical decision
problem is established here. In particular, the result does not settle the
decision-task conjecture discussed in that footnote. A verification measurement
depending on the unknown $`\psi`$ cannot simply be granted to a decision algorithm
without changing its access model.

The copy theorem counts source specimens and permits unrestricted processing.
The upper-bound channel uses a projector onto a traceless symmetric sector. Its
existence and Kraus normalization do not by themselves give an efficient gate
decomposition. No optimal gate count, circuit depth, or implementation robustness
claim follows from the copy bound. The finite matrix audit in
[verification/README.md](../verification/README.md) checks the mathematical
normalization and state identities.

## General-spectrum identity and limits of the comparison

The Bell identity holds for any density operator, but its normalized output is
$`|B_\rho\rangle\propto\mathrm{vec}(\rho)`$, whereas canonical purification
is $`|C_\rho\rangle=\mathrm{vec}(\sqrt\rho)`$. Their squared fidelity is

```math
|\langle C_\rho|B_\rho\rangle|^2
=\frac{\left(\sum_i\lambda_i^{3/2}\right)^2}{\sum_i\lambda_i^2},
```

where $`\lambda_i`$ are the eigenvalues of $`\rho`$. Equality to one holds exactly
when all nonzero eigenvalues are equal: proportionality of $`\rho`$ and
$`\sqrt\rho`$ requires $`\lambda_i=c\sqrt{\lambda_i}`$ on the support. For example,
the spectrum $`(0.8,0.2)`$ gives $`81/85`$, not exact canonical purification.

For a flat rank-$`r`$ state $`\rho=P/r`$, the same identity does yield canonical
purification with probability $`1/(rk)`$. This is a direct general-rank Bell
calculation. The complete copy-complexity theorem in this project concerns the
rank-two family with a known vacuum and an unknown one-dimensional signal.
No matching copy theorem for arbitrary rank, arbitrary spectrum, or an unknown
general support is asserted by the Bell calculation alone.

## References used for the access-model comparison

1. Ewin Tang, John Wright, and Mark Zhandry, *Conjugate queries can help*,
   [arXiv:2510.07622v2](https://arxiv.org/pdf/2510.07622v2), 8 May 2026.
2. Filippo Girardi, Francesco Anna Mele, and Ludovico Lami, *Random purification
   channel made simple*, [arXiv:2511.23451v3](https://arxiv.org/html/2511.23451v3),
   22 June 2026.
3. Angus Lowe and Xinyu Tan, *Random dimension reduction and learning symmetric
   properties of quantum states*,
   [arXiv:2606.23592v2](https://arxiv.org/html/2606.23592v2), 2 October 2026.
