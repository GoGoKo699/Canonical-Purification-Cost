# A robust converse for arbitrary processors

Preparing the canonical purification of the promised rank-two state with squared fidelity exceeding $1/2$ by a fixed positive amount requires $\Omega(\sqrt d)$ total mixed-state copies at constant success probability. The lower bound allows arbitrary collective operations, coherent memory, ancillary systems, measurements, and adaptive classical control. It follows from an exact finite-copy inequality, proved below for the stronger input that supplies pure copies of both $\psi$ and $\psi^*$.

The input and output promises are given in [model.md](model.md). All harmonic identities used here are proved in [harmonic_analysis.md](harmonic_analysis.md). The matching upper bound is in [construction.md](construction.md), and the constant-size matched-purification resource is treated separately in [access_comparison.md](access_comparison.md). See [RELATED_WORK.md](../references/RELATED_WORK.md) for comparisons with earlier purification and superposition results.

## 1. Target, success probability, and fidelity

Let $V=\mathbb C^d$, $d\geq2$, and let

$$
H=\mathbb C|\mathrm{vac}\rangle\oplus V,
\qquad
\rho_\psi
=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+|\psi\rangle\langle\psi|}{2},
$$

where $\psi$ is an unknown unit vector in $V$. The target is

$$
|T_\psi\rangle
=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle\otimes|\psi^*\rangle}{\sqrt2}.
\tag{C1}
$$

All complex conjugates refer to the supplied basis. The second signal factor may equivalently be identified with the conjugate Hilbert space $\overline V$.

Begin with the balanced pure input

$$
v_N(\psi)=\psi^{\otimes N}\otimes(\psi^*)^{\otimes N}
\in\mathcal R_N
=\operatorname{Sym}^N(V)\otimes\operatorname{Sym}^N(\overline V).
\tag{C2}
$$

Let $\Lambda$ be the successful branch of a processor, a completely positive trace-nonincreasing map to the target output space $O=H\otimes H$. No symmetry is imposed on $\Lambda$. Define the unnormalized accepted output, its probability, and its target overlap by

$$
\sigma_\psi
=\Lambda(|v_N(\psi)\rangle\langle v_N(\psi)|),
\qquad
q(\psi)=\operatorname{Tr}\sigma_\psi,
\qquad
g(\psi)=\langle T_\psi|\sigma_\psi|T_\psi\rangle.
\tag{C3}
$$

For $q(\psi)>0$, the conditional squared fidelity is

$$
F(\psi)=\frac{g(\psi)}{q(\psi)}.
$$

When the target is pure, squared fidelity is exactly this overlap with the normalized output. Haar-average quantities are

$$
p=\int q(\psi)\,d\mu(\psi),
\qquad
f=\int g(\psi)\,d\mu(\psi).
\tag{C4}
$$

For $p>0$, $f/p$ is the conditional fidelity averaged over successful runs. The posterior distribution of $\psi$ in this average is proportional to $q(\psi)d\mu(\psi)$. It is generally different from the unweighted average of $F(\psi)$.

## 2. Finite-copy theorem

Set

$$
p_N
=\frac{\Gamma(d+N-1)^2}
{\Gamma(d-1)\Gamma(d+2N-1)},
\qquad
\delta_N=1-p_N,
\qquad
\lambda_N
=1-\frac{(N+d-1)^2}{(2N+d-1)(2N+d)}.
\tag{C5}
$$

The conventions for $N=0$ are $p_0=1$, $\delta_0=0$, and $\lambda_0=1/d$.

**Theorem 1.** Every successful completely positive trace-nonincreasing processor acting on (C2) satisfies

$$
\boxed{
f\leq
\left(\frac12+\frac{\sqrt{\lambda_N}}2\right)p
+\sqrt{\delta_Np}.
}
\tag{C6}
$$

In particular, if $p>0$ and $f/p\geq F_0$ with

$$
F_0>\frac12+\frac{\sqrt{\lambda_N}}2,
$$

then

$$
\boxed{
p\leq
\frac{\delta_N}
{\left(F_0-\frac12-\frac{\sqrt{\lambda_N}}2\right)^2}.
}
\tag{C7}
$$

For a trace-preserving processor, $p=1$, and hence its Haar-average squared fidelity obeys

$$
\boxed{
\overline F
\leq\frac12+\frac{\sqrt{\lambda_N}}2+\sqrt{\delta_N}.
}
\tag{C8}
$$

Each right-hand side may of course be capped by the trivial probability or fidelity bound of one. Equation (C6) is useful without an exact-output promise and without a covariance restriction.

## 3. Stinespring form of an unrestricted success branch

Choose Kraus operators $K_a$ for $\Lambda$. Complete positivity gives
$\Lambda(X)=\sum_aK_aXK_a^\dagger$, and trace nonincrease gives
$\sum_aK_a^\dagger K_a\leq I$. Thus the operator

$$
\mathsf V:\mathcal R_N\longrightarrow O\otimes E,
\qquad
\mathsf V=\sum_a K_a\otimes|a\rangle,
$$

satisfies

$$
\mathsf V^\dagger\mathsf V\leq I,
\qquad
\Lambda(X)=\operatorname{Tr}_E[\mathsf V X\mathsf V^\dagger].
\tag{C9}
$$

This is the contraction form of a Stinespring representation. The finite-dimensional Kraus and Stinespring characterizations are stated in [Watrous, §2.2.2, Theorem 2.22][Watrous]. The inequality in (C9) also follows directly from the displayed Kraus construction.

All ancillas and discarded systems can be included in $E$. If a protocol uses intermediate measurements, retain their outcomes in orthogonal environment registers and include the operations controlled by those outcomes. Grouping all accepting outcomes gives exactly one map of the form (C9). Coherent operations and adaptive instruments therefore require no separate restriction or averaging argument.

Decompose the output vector according to its overlap with the two target sectors:

$$
\mathsf Vv_N(\psi)
=|\mathrm{vac},\mathrm{vac}\rangle\otimes a(\psi)
+b(\psi)+r(\psi),
\tag{C10}
$$

where

$$
b(\psi)=\sum_{i,j=1}^d|i,j\rangle\otimes b_{ij}(\psi)
\in(V\otimes\overline V)\otimes E,
$$

and $r(\psi)$ lies in output sectors orthogonal to both $|\mathrm{vac},\mathrm{vac}\rangle$ and $V\otimes\overline V$. These sectors are mutually orthogonal. Put

$$
A=\|a\|_2^2,
\qquad
B=\|b\|_2^2.
$$

Then

$$
A+B\leq p.
\tag{C11}
$$

The environment-valued amplitudes $a$ and $b_{ij}$ all belong to $\mathcal L_N\otimes E$. They are obtained by applying fixed linear functionals or linear maps to $v_N(\psi)$. The final section of [harmonic_analysis.md](harmonic_analysis.md#7-vector-valued-amplitudes-and-arbitrary-linear-processors) proves this statement, including the complex-conjugation convention, for an arbitrary linear map.

## 4. The available lower-degree amplitude

Let $P_N$ be the top traceless tensor projector, and let

$$
\mathsf A=(\langle\mathrm{vac},\mathrm{vac}|\otimes I_E)\mathsf V.
$$

It is a contraction because it is the composition of a projection with the contraction $\mathsf V$. The harmonic decomposition of $a$ is

$$
a=a_{<N}+a_N,
\qquad
a_{<N}(\psi)=\mathsf A(I-P_N)v_N(\psi),
\qquad
a_N(\psi)=\mathsf A P_Nv_N(\psi).
\tag{C12}
$$

Here $a_N\in\mathcal H_N\otimes E$, $a_{<N}\in\mathcal L_{N-1}\otimes E$, and these functions are $L^2$-orthogonal. For $N=0$, interpret $a_{<0}=0$.

The total lower-degree input weight is exactly $\delta_N$. Applying the contraction $\mathsf A$ cannot increase its average squared norm, so

$$
\begin{aligned}
\|a_{<N}\|_2^2
&=\int\|\mathsf A(I-P_N)v_N(\psi)\|^2\,d\mu(\psi)\\
&\leq\int\|(I-P_N)v_N(\psi)\|^2\,d\mu(\psi)
=\delta_N.
\end{aligned}
\tag{C13}
$$

Orthogonality in (C12) also gives $\|a_N\|_2^2\leq A$. Identifying (C12) as the actual harmonic decomposition is essential: it follows from the explicit tensor-to-function identification, not from assuming that the processor respects the group action.

## 5. Bounding the coherence required by the target

Use the isometry

$$
(Ma)(\psi)=\chi(\psi)\otimes a(\psi),
\qquad
\chi(\psi)=\psi\otimes\psi^*.
\tag{C14}
$$

Its pointwise adjoint on $b$ is

$$
(M^\dagger b)(\psi)
=\sum_{i,j}\overline\psi_i\psi_j\,b_{ij}(\psi).
$$

In particular, $\|M^\dagger b\|_2\leq\|b\|_2$. By (C1) and (C10), the exact unnormalized fidelity is

$$
\begin{aligned}
f
&=\frac12\|a+M^\dagger b\|_2^2\\
&=\frac{A+\|M^\dagger b\|_2^2}{2}
+\operatorname{Re}\langle Ma,b\rangle_2\\
&\leq\frac p2+|\langle Ma,b\rangle_2|.
\end{aligned}
\tag{C15}
$$

Thus any improvement above the $1/2$ overlap of the vacuum output requires coherent overlap between the vacuum and signal amplitudes.

For the lower-degree part, the isometry property and Cauchy–Schwarz give

$$
|\langle Ma_{<N},b\rangle_2|
\leq\sqrt{\delta_N}\sqrt B.
\tag{C16}
$$

For the highest-degree part, $b$ has no harmonic component above degree $N$. Consequently,

$$
\begin{aligned}
|\langle Ma_N,b\rangle_2|
&=|\langle\Pi_{\leq N}Ma_N,b\rangle_2|\\
&\leq\sqrt{\lambda_N}\,\|a_N\|_2\sqrt B\\
&\leq\sqrt{\lambda_N}\sqrt{AB}.
\end{aligned}
\tag{C17}
$$

The second line is the vector-valued multiplication lemma (H38). The degree-$N+1$ component of the product of a highest-degree amplitude with $\chi(\psi)$ is orthogonal to every possible signal amplitude of an $N$-pair processor. The retained fraction is $\lambda_N$, which tends to zero in the regime $N=o(\sqrt d)$.

Combining (C15)–(C17) and using $\sqrt{AB}\leq(A+B)/2\leq p/2$ and $B\leq p$ proves

$$
f\leq\frac p2+\sqrt{\delta_NB}+\sqrt{\lambda_NAB}
\leq\left(\frac12+\frac{\sqrt{\lambda_N}}2\right)p
+\sqrt{\delta_Np}.
$$

This is (C6). Rearranging it under the stated fidelity condition gives (C7); setting $p=1$ gives (C8).

## 6. From independent mixed samples to the stronger pure input

The theorem applies to a protocol with a hard budget of $T$ total copies, where each requested copy is either $\rho_\psi$ or $\rho_\psi^*$. The allocation may depend on earlier outcomes, and all processing of the supplied registers may be coherent.

To simulate such a protocol, give the simulator $T$ pure copies of $\psi$ and $T$ pure copies of $\psi^*$. On each source register apply the known channel

$$
\mathcal D(X)
=\frac12\iota X\iota^\dagger
+\frac12\operatorname{Tr}(X)|\mathrm{vac}\rangle\langle\mathrm{vac}|,
\tag{C18}
$$

where $\iota:V\hookrightarrow H$ is the fixed inclusion. This produces $T$ independent copies of each mixed source. In every branch the original protocol uses at most $T$ copies of either type, so the simulator has enough of both.

All these registers can be supplied before processing begins. Adaptive requests select the next unused register of the appropriate type. Unused registers are discarded at the end. Coherent routing, controlled swaps, memory, and deferred measurements are operations inside the resulting processor and do not change the initial product-state resource. The simulator therefore implements a fixed completely positive trace-nonincreasing map on the balanced pure input $v_T(\psi)$.

This reduction concerns independent state samples. It does not grant access to a state-preparation unitary, its discarded purification register, or an additional coherently controlled preparation interface. Such resources are specified separately in [access_comparison.md](access_comparison.md).

**Corollary 2.** Every protocol using at most $T$ total mixed-source copies obeys (C6)–(C8) with $N=T$. For a fixed nonadaptive allocation of $n$ copies of $\rho_\psi$ and $m$ copies of $\rho_\psi^*$, the stronger balanced input with $N=\max\{n,m\}$ suffices, so that value can be used instead.

The padding argument deliberately gives the lower-bound simulator more copies than the original protocol. A lower bound for this stronger input remains a valid lower bound for the original hard total budget.

## 7. Constant-error consequences and the fidelity threshold

Fix constants $p_{\min}>0$ and $F_0>1/2$. Suppose a protocol has average success at least $p_{\min}$ and success-weighted average conditional squared fidelity at least $F_0$. Worst-case guarantees $q(\psi)\geq p_{\min}$ and $F(\psi)\geq F_0$ for every $\psi$ imply these average guarantees.

For a hard total mixed-copy budget $T$, a useful necessary finite-dimensional condition is

$$
F_0-\frac12
\leq\frac{\sqrt{\lambda_T}}2
+\sqrt{\frac{\delta_T}{p_{\min}}}.
\tag{C19}
$$

The exact constants are specified in (C5). In particular,

$$
\delta_T\leq\frac{T^2}{d-1+T},
\qquad
\lambda_T
=\frac{(2T+1)d+3T^2-1}{(d+2T-1)(d+2T)}.
\tag{C20}
$$

If $T=o(\sqrt d)$, both correction terms in (C19) vanish. More quantitatively, for $T\leq c\sqrt d$, the second term is at most $c/\sqrt{p_{\min}}+o(1)$, while the first term tends to zero. Choosing $c$ below a fixed multiple of $(F_0-1/2)\sqrt{p_{\min}}$ makes (C19) impossible for sufficiently large $d$. Hence

$$
T=\Omega_{p_{\min},F_0}(\sqrt d).
\tag{C21}
$$

The same conclusion holds for an unconditional channel with Haar-average fidelity at least a fixed $F_0>1/2$, by taking $p_{\min}=1$.

The threshold has a direct operational meaning: always outputting $|\mathrm{vac},\mathrm{vac}\rangle$ costs no copies and has squared fidelity exactly $1/2$ with every target. The theorem concerns a fixed positive improvement above this baseline. Its finite-dimensional terms do not exclude improvements that themselves vanish with $d$.

The [exact heralded construction](construction.md) uses $O(\sqrt d)$ copies of each stream with constant success probability; a constant number of independent repetitions gives any prescribed fixed success probability below one. On overall failure one may output the vacuum pair, yielding any prescribed fixed unconditional fidelity below one with the same asymptotic order. Together with (C21), this establishes the matching $\Theta(\sqrt d)$ total-copy law for these constant-performance criteria.

This conclusion is a lower bound on the **total** number of samples. It does not impose an individual $\Omega(\sqrt d)$ lower bound on each stream. Padding to a balanced input proves the total bound; an asymmetric protocol with a much larger allocation to one stream is not ruled out by that statement. All budgets in this account are hard maxima on copies supplied to the protocol.

## Reference

- John Watrous, *The Theory of Quantum Information*, Cambridge University Press (2018), [author manuscript][Watrous], §2.2.2, Theorem 2.22. The proof above uses the finite-dimensional Kraus/Stinespring representation, with the trace-nonincreasing condition giving a contraction. The harmonic estimates are derived in [harmonic_analysis.md](harmonic_analysis.md), and the task-specific literature is discussed in [RELATED_WORK.md](../references/RELATED_WORK.md).

[Watrous]: https://cs.uwaterloo.ca/~watrous/TQI/TQI.pdf
