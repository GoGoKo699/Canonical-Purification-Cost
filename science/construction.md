# Exact heralded construction

[Model](model.md) · [Harmonic analysis](harmonic_analysis.md) · [Converse](converse.md) · [Access comparison](access_comparison.md) · [Related work](../references/RELATED_WORK.md)

The construction prepares the exact target on success. Its central step coherently combines two ways of removing one specimen from each conjugate stream: a contraction that produces a known vacuum pair, and an extraction that retains the unknown signal pair. A projection on the residual systems makes this combined operation a valid success operator with constant probability at $`N`$ proportional to $`\sqrt d`$.

We first give the operation for $`N`$ pure specimens of each type. We then obtain these specimens from a fixed number of mixed-source requests and give explicit repetition bounds. Every rejected specimen and unsuccessful attempt is included in the final hard total budget.

## Symmetric input spaces

Let $`\mathcal V\cong\mathbb C^d`$ be the known signal subspace from the [model](model.md). The second stream transforms under the conjugate representation, denoted $`\overline{\mathcal V}`$. Both physical registers have the supplied computational basis.

For $`N\ge0`$, set

```math
\mathcal R_N
=\mathrm{Sym}^N(\mathcal V)
\otimes\mathrm{Sym}^N(\overline{\mathcal V}),
\qquad
|v_N(\psi)\rangle
=|\psi\rangle^{\otimes N}\otimes|\psi^*\rangle^{\otimes N}.
```

Use $`\mathcal R_0=\mathbb C`$ and $`v_0=1`$. The promised pure input belongs to $`\mathcal R_N`$.

It is convenient to describe these symmetric spaces with normalized occupation states. Let $`a_i`$ and $`b_i`$ be the annihilation operators for coordinate $`i`$ in the first and second symmetric factors. For example,

```math
a_i|n_1,\ldots,n_d\rangle
=\sqrt{n_i}\,|n_1,\ldots,n_i-1,\ldots,n_d\rangle.
```

The two families act on different factors. This is a notation for finite symmetric tensor spaces, rather than an assumption that bosonic hardware is supplied.

## Contraction and extraction

For $`N\ge1`$, define

```math
C_N=\sum_{i=1}^d a_i b_i:
\mathcal R_N\longrightarrow\mathcal R_{N-1}.
```

Each annihilator satisfies

```math
a_i|\psi\rangle^{\otimes N}
=\sqrt N\,\psi_i|\psi\rangle^{\otimes(N-1)},
```

and the corresponding second-stream coefficient is $`\sqrt N\,\overline{\psi_i}`$. Therefore

```math
C_Nv_N(\psi)
=N\sum_{i=1}^d|\psi_i|^2v_{N-1}(\psi)
=Nv_{N-1}(\psi).
```

Define the extraction map

```math
E_N
=\frac1N\sum_{i,j=1}^d
|i,j\rangle\otimes a_i b_j:
\mathcal R_N
\longrightarrow
(\mathcal V\otimes\overline{\mathcal V})\otimes\mathcal R_{N-1}.
```

It removes one factor from each symmetric stream and writes those factors into the output registers. More explicitly,

```math
E_Nv_N(\psi)
=|\psi\rangle|\psi^*\rangle\otimes v_{N-1}(\psi).
```

The map is an isometry on all of $`\mathcal R_N`$, not only on the promised coherent inputs. Indeed,

```math
\begin{aligned}
E_N^\dagger E_N
&=\frac1{N^2}\sum_{i,j}a_i^\dagger a_i\,b_j^\dagger b_j\\
&=\frac1{N^2}
\left(\sum_i a_i^\dagger a_i\right)
\left(\sum_j b_j^\dagger b_j\right)
=I_{\mathcal R_N},
\end{aligned}
```

because the two occupation numbers both equal $`N`$ on $`\mathcal R_N`$.

Embed the extracted signal pair into the output space $`\mathcal H\otimes\mathcal H`$ and define

```math
W_N
=\frac1{\sqrt2}
\left(
|{\rm vac},{\rm vac}\rangle\otimes\frac{C_N}{N}
+E_N
\right).
```

The vacuum and signal output sectors are orthogonal. On a promised input,

```math
W_Nv_N(\psi)
=|T_\psi\rangle\otimes v_{N-1}(\psi).
```

This identity has the desired coherence, but by itself does not establish a physical operation: $`W_N`$ need not be a contraction. Its norm on the entire input space must be controlled.

## A filter on the residual systems

For $`m\ge1`$, let $`P_m`$ be the orthogonal projector onto

```math
\ker C_m\subseteq\mathcal R_m,
```

and set $`P_0=I_{\mathcal R_0}`$. These are known projectors determined by $`d`$ and $`m`$. For $`d\ge2`$ and $`m\ge1`$, the vector $`|1\rangle^{\otimes m}\otimes|2\rangle^{\otimes m}`$ belongs to $`\ker C_m`$, so the residual projector is nonzero. In the harmonic decomposition, $`\ker C_m`$ is the highest, completely traceless component; its description and orbit weight are proved in [harmonic analysis](harmonic_analysis.md).

The following norm identity gives the normalization needed for the success map.

**Residual contraction identity.** For every $`N\ge1`$,

```math
C_NC_N^\dagger P_{N-1}
=(d+2N-2)P_{N-1}.
```

To prove it, use $`C=\sum_i a_i b_i`$ on the direct sum of the occupation sectors. The canonical commutation relations give

```math
[C,C^\dagger]
=\sum_{i=1}^d
\left(a_i^\dagger a_i+b_i^\dagger b_i+I\right).
```

On $`\mathcal R_{N-1}`$ the right side is $`(d+2N-2)I`$. If $`w`$ lies in the range of $`P_{N-1}`$, then $`Cw=0`$, including the scalar sector when $`N=1`$. Hence

```math
CC^\dagger w=[C,C^\dagger]w=(d+2N-2)w.
```

In particular,

```math
\|P_{N-1}C_N\|^2=d+2N-2,
\qquad
C_N^\dagger P_{N-1}C_N
\le(d+2N-2)I_{\mathcal R_N}.
```

This argument uses the kernel property directly and does not require an optimality assertion about the filter.

## Complete positivity and exact output

Set

```math
\alpha_N^2
=\frac{2N^2}{N^2+d+2N-2},
\qquad
K_N
=\alpha_N(I_{\rm out}\otimes P_{N-1})W_N.
```

**Lemma.** The operator $`K_N`$ is a contraction for every integer $`d\ge2`$ and $`N\ge1`$.

The two terms of $`W_N`$ have orthogonal output sectors, so their contributions to $`K_N^\dagger K_N`$ add without cross terms:

```math
K_N^\dagger K_N
=\frac{\alpha_N^2}{2}
\left(
\frac{C_N^\dagger P_{N-1}C_N}{N^2}
+E_N^\dagger(I_{\rm out}\otimes P_{N-1})E_N
\right).
```

The residual contraction identity bounds the first term. Since $`E_N`$ is an isometry and $`P_{N-1}`$ is an orthogonal projector, the second term is at most $`I_{\mathcal R_N}`$. Consequently,

```math
\begin{aligned}
K_N^\dagger K_N
&\le
\frac{\alpha_N^2}{2}
\left(\frac{d+2N-2}{N^2}+1\right)I_{\mathcal R_N}\\
&=I_{\mathcal R_N}.
\end{aligned}
```

Extend $`K_N`$ by zero on the orthogonal complement of $`\mathcal R_N`$ in the full input tensor product. This extension remains a contraction. Thus

```math
\mathcal E_{\rm succ}(X)
=\mathrm{Tr}_{\rm res}(K_NXK_N^\dagger)
```

is a completely positive, trace-nonincreasing success map on all inputs. A failure operation with effect $`I-K_N^\dagger K_N`$ completes a quantum instrument. For example, its positive square root may be used as a failure Kraus operator, with the residual failure system discarded after recording the flag.

The scalar $`\alpha_N^2`$ can exceed one for some choices of $`d,N`$. It is not used as a probability on its own; the complete operator $`K_N`$ is contractive by the displayed inequality.

For the promised input, the accepted vector factors exactly:

```math
K_Nv_N(\psi)
=\alpha_N|T_\psi\rangle
\otimes P_{N-1}v_{N-1}(\psi).
```

The target is therefore independent of the discarded residual system. Every accepted output is exactly $`|T_\psi\rangle\langle T_\psi|`$.

## Exact success probability

Write

```math
p_m=\|P_mv_m(\psi)\|^2.
```

The [harmonic analysis](harmonic_analysis.md) proves that this quantity is independent of $`\psi`$ and equals

```math
\begin{aligned}
p_m
&=\frac{\Gamma(d+m-1)^2}
{\Gamma(d-1)\Gamma(d+2m-1)}\\
&=\prod_{j=0}^{m-1}
\frac{d-1+j}{d-1+m+j},
\qquad m\ge0,
\end{aligned}
```

with the empty product $`p_0=1`$. Hence the exact pure-input success probability is

```math
q_N
=\|K_Nv_N(\psi)\|^2
=\frac{2N^2}{N^2+d+2N-2}\,p_{N-1}.
```

All these quantities are positive for the stated $`d,N`$. Their interpretation as probabilities follows from the contraction proof, which applies to the entire input space.

### The case of one specimen from each stream

When $`N=1`$, the residual space is scalar and $`P_0=I`$. Let

```math
|\Omega_d\rangle=\sum_{i=1}^d|i,i\rangle.
```

Then $`C_1=\langle\Omega_d|`$ and $`E_1`$ is the natural identification of the input pair with the signal output sector. The success operator is

```math
K_1
=\frac{
|{\rm vac},{\rm vac}\rangle\langle\Omega_d|+E_1
}{\sqrt{d+1}},
\qquad
q_1=\frac{2}{d+1}.
```

This supplies a well-defined starting case, with no negative tensor powers or residual projection to implement. The collective construction below obtains constant success using $`N`$ of order $`\sqrt d`$. Fixed-overlap superposition constructions are discussed in [related work](../references/RELATED_WORK.md).

## A uniform bound at the square-root scale

Choose

```math
N=\lceil\sqrt d\rceil,
\qquad m=N-1.
```

Since $`d\ge2`$, we have $`N\ge2`$. Also $`m^2\lt d`$, and the quantities are integers, so $`m^2\le d-1`$. The product formula gives

```math
\begin{aligned}
-\log p_m
&=\sum_{j=0}^{m-1}
\log\left(1+\frac{m}{d-1+j}\right)\\
&\le\sum_{j=0}^{m-1}\frac{m}{d-1+j}
\le\frac{m^2}{d-1}
\le1.
\end{aligned}
```

Therefore $`p_{N-1}\ge e^{-1}`$. Moreover, $`d\le N^2`$, and

```math
\alpha_N^2
\ge\frac{N^2}{N^2+N-1}
\ge\frac45.
```

The last inequality is equivalent to $`(N-2)^2\ge0`$. Combining the estimates yields the finite, dimension-independent bound

```math
q_N\ge\frac4{5e}
\qquad\text{for every integer }d\ge2.
```

The exact expression also gives $`q_N\longrightarrow e^{-1}`$ as $`d\to\infty`$ with $`N=\lceil\sqrt d\rceil`$. The uniform bound is sufficient for the hard-budget theorem and is not asserted to be optimal.

## Extracting pure specimens from the mixed sources

Measure each mixed specimen with the known two-outcome projective measurement

```math
\left\{
|{\rm vac}\rangle\langle{\rm vac}|,
\quad
I-|{\rm vac}\rangle\langle{\rm vac}|
\right\}.
```

For $`\rho_\psi`$, the signal outcome occurs with probability $`1/2`$ and leaves the exact pure state $`|\psi\rangle`$. For $`\rho_\psi^*`$, it likewise leaves $`|\psi^*\rangle`$ with probability $`1/2`$. The outcome probability is independent of the unknown direction.

One complete attempt requests exactly $`2N`$ mixed specimens from each stream, for a total of $`4N`$ requests. In each stream retain the first $`N`$ signal specimens if there are enough; otherwise declare the attempt unsuccessful. Any surplus specimens are discarded. Conditional on obtaining enough signals, rearranging the retained registers using their known positions produces precisely $`v_N(\psi)`$.

For one stream, the number of signal outcomes is $`X\sim\mathrm{Bin}(2N,1/2)`$. Symmetry of this binomial distribution gives

```math
s_N:=\Pr[X\ge N]
=\frac12+\frac12\,\frac{\binom{2N}{N}}{2^{2N}}
\ge\frac12.
```

The source specimens are independent, so both streams supply enough signals with probability $`s_N^2\ge1/4`$. Apply $`K_N`$ only when this extraction succeeds. The complete mixed-input attempt therefore succeeds with the exact probability

```math
u_N=s_N^2q_N.
```

For $`N=\lceil\sqrt d\rceil`$,

```math
u_N\ge\frac1{5e}.
```

Every successful output is exactly $`T_\psi`$. The count $`4N`$ includes all vacuum outcomes, discarded surplus signals, and specimens in a rejected coherent filter.

## Bounded repetition and deterministic output

Run at most $`r\ge1`$ complete attempts on fresh source specimens, stopping when one succeeds. The hard total budget is

```math
t=4Nr.
```

Fresh tensor-product inputs make each new attempt's success probability $`u_N`$, even conditional on failure of earlier attempts. Thus the probability that every attempt fails is

```math
(1-u_N)^r
\le\left(1-\frac1{5e}\right)^r
\le e^{-r/(5e)}.
```

For the heralded task, declare success exactly when an attempt succeeds. The accepted output remains exact, and a success probability at least $`p_{\min}\in(0,1)`$ is ensured by

```math
r=
\left\lceil
5e\log\frac1{1-p_{\min}}
\right\rceil.
```

This supplies the same upper bound for every accepted-fidelity requirement $`F_0\in(1/2,1]`$.

For a deterministic output, keep the successful target if there is one and prepare the known vacuum pair if every attempt fails. If $`S`$ is the overall success probability, the resulting state is

```math
\sigma_\psi
=S|T_\psi\rangle\langle T_\psi|
+(1-S)|{\rm vac},{\rm vac}\rangle
\langle{\rm vac},{\rm vac}|.
```

Its squared fidelity is

```math
\langle T_\psi|\sigma_\psi|T_\psi\rangle
=S+\frac{1-S}{2}
\ge1-\frac12 e^{-r/(5e)}.
```

Therefore any fixed $`F_0\in(1/2,1)`$ is achieved with

```math
r=
\left\lceil
5e\log\frac1{2(1-F_0)}
\right\rceil.
```

For fixed thresholds, $`r`$ is independent of $`d`$, and the hard total budget is $`O(\sqrt d)`$. Early stopping can reduce the number of specimens used on particular branches, but the guarantee already charges the maximum $`4Nr`$, including all unsuccessful attempts.

## Finite-allocation optimality

The residual projection used here is a sufficient filter, not generally the optimal exact filter at a finite allocation. For example, at $`d=2,N=2`$ it succeeds with probability $`1/2`$, whereas the arbitrary-processor exact optimum is $`12/13`$. The [exact unequal-supply frontier](exact_frontier.md) proves that optimum and characterizes every allocation; the [mixed frontier](mixed_frontier.md) averages it over the lossless signal counts. The present construction remains the explicit instrument establishing the balanced square-root upper bound.

## What the construction establishes

The operation depends only on the known basis, the signal dimension, and the chosen number of specimens. It proves exact heralded preparation by a finite-dimensional quantum instrument, followed by explicit extraction and repetition. A gate-efficient circuit for the residual projector is not part of the copy-complexity claim.

The matching [converse](converse.md) allows arbitrary collective processors and arbitrary allocations between the two mixed streams. The [access comparison](access_comparison.md) treats a different resource: an arbitrary constant-environment purification paired with its exactly matched conjugate. The [related-work account](../references/RELATED_WORK.md) identifies the earlier superposition and contraction methods used as background.
