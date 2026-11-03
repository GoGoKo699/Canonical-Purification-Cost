# Model and total copy complexity

[Construction](construction.md) · [Harmonic analysis](harmonic_analysis.md) · [Converse](converse.md) · [Access comparison](access_comparison.md) · [Related work](../references/RELATED_WORK.md)

The task is to prepare a specified pure correlation from two streams of mixed quantum states. Both a state and its complex conjugate are supplied, so producing the conjugate marginal is already part of the available resource. The remaining task is to create the coherence required by the canonical purification.

## State family and fixed basis

Fix an integer $d\ge 2$ and a known decomposition

$$
\mathcal H=\operatorname{span}\{|{\rm vac}\rangle\}\oplus\mathcal V,
\qquad
\mathcal V\cong\mathbb C^d.
$$

The computational basis is $|{\rm vac}\rangle,|1\rangle,\ldots,|d\rangle$. Complex conjugation, including the notation $|\psi^*\rangle$, always refers to this basis. The vacuum vector and the projector onto $\mathcal V$ are known. The unknown parameter is an arbitrary unit vector $|\psi\rangle\in\mathcal V$.

The two sources prepare independent specimens of

$$
\rho_\psi
=\frac{|{\rm vac}\rangle\langle{\rm vac}|+|\psi\rangle\langle\psi|}{2},
\qquad
\rho_\psi^*
=\frac{|{\rm vac}\rangle\langle{\rm vac}|+|\psi^*\rangle\langle\psi^*|}{2}.
$$

Independence means that, conditional on the fixed unknown $\psi$, any collection of requested specimens is a tensor product of the corresponding source states. The streams share the parameter $\psi$, but their inaccessible source environments are not supplied.

The desired output is

$$
|T_\psi\rangle
=\frac{|{\rm vac},{\rm vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}
\in\mathcal H\otimes\mathcal H.
$$

The two terms are orthogonal, so the displayed vector is normalized. It is also independent of the choice of global phase for $\psi$: replacing $\psi$ by $e^{i\theta}\psi$ leaves $\psi\otimes\psi^*$ unchanged.

To connect this expression with canonical purification, define

$$
|\Omega_{\mathcal H}\rangle
=|{\rm vac},{\rm vac}\rangle+\sum_{i=1}^d|i,i\rangle.
$$

Since the two nonzero eigenvalues of $\rho_\psi$ are $1/2$,

$$
(\sqrt{\rho_\psi}\otimes I)|\Omega_{\mathcal H}\rangle
=|T_\psi\rangle.
$$

Consequently,

$$
\operatorname{Tr}_2|T_\psi\rangle\langle T_\psi|=\rho_\psi,
\qquad
\operatorname{Tr}_1|T_\psi\rangle\langle T_\psi|=\rho_\psi^*.
$$

The specified relative coherence is part of the target. Producing an arbitrary state with these two marginals, or an arbitrary purification in a different environment, is a different output requirement. The [access comparison](access_comparison.md) explains why this distinction matters for random purification.

## Allowed processors and the hard budget

A processor may use arbitrary ancillary systems in states independent of $\psi$, unrestricted coherent memory, collective quantum operations, adaptive measurements, and classical processing. It may choose which source to request next using its previous measurement outcomes. Its operations are fixed by the known problem parameters and its observed outcomes; it receives no classical description of $\psi$.

A **hard total budget $t$** means that every execution branch requests at most $t$ source specimens in total, counting both streams. Every request counts, including specimens discarded after a vacuum outcome, specimens used in a rejected filter, and specimens consumed by unsuccessful repetitions. The budget is a bound on every branch, rather than an expectation over outcomes.

The input resource consists of the supplied states. No preparation unitary, source reflection, inverse operation, or matched purification is included in this model. The processor itself is unrestricted, and the lower bound imposes no computational, memory, locality, or measurement-depth restriction.

For fixed numbers $n$ and $m$ of requests, a heralded processor is described by a completely positive, trace-nonincreasing success map applied to

$$
\rho_\psi^{\otimes n}\otimes(\rho_\psi^*)^{\otimes m}.
$$

Adaptive source requests are allowed under the same hard total budget. They are included in the lower-bound reduction below.

## Fidelity and success conventions

For a normalized output state $\sigma$, define its squared fidelity with the pure target by

$$
F_\psi(\sigma)=\langle T_\psi|\sigma|T_\psi\rangle.
$$

This convention has no square root. A successful output may be mixed.

For a heralded processor, let $\tau_\psi$ be its unnormalized output on the success flag and let

$$
p_\psi=\operatorname{Tr}\tau_\psi.
$$

Given constants $F_0\in(1/2,1]$ and $p_{\min}\in(0,1)$, the required worst-case guarantees are

$$
p_\psi\ge p_{\min},
\qquad
\langle T_\psi|\tau_\psi|T_\psi\rangle\ge F_0p_\psi
\quad\text{for every unit }\psi\in\mathcal V.
$$

Equivalently, the normalized state $\tau_\psi/p_\psi$ has squared fidelity at least $F_0$. Writing the requirement in this homogeneous form retains the success probability when different inputs or internal outcomes are averaged.

For a deterministic processor, the normalized output $\sigma_\psi$ must satisfy

$$
F_\psi(\sigma_\psi)\ge F_0
\quad\text{for every unit }\psi\in\mathcal V,
\qquad F_0\in(1/2,1).
$$

The threshold $1/2$ has a direct operational meaning. The known state $|{\rm vac},{\rm vac}\rangle$ achieves squared fidelity exactly $1/2$ for every $\psi$ without consuming any samples. The theorem concerns an improvement above this baseline that remains fixed as $d$ grows.

## The total-copy theorem

Let $T_{\rm her}(d;F_0,p_{\min})$ be the smallest hard total budget of a processor satisfying the heralded guarantee, and let $T_{\rm det}(d;F_0)$ be the corresponding quantity for deterministic preparation.

**Theorem.** For every fixed $F_0\in(1/2,1]$ and $p_{\min}\in(0,1)$,

$$
T_{\rm her}(d;F_0,p_{\min})=\Theta(\sqrt d).
$$

For every fixed $F_0\in(1/2,1)$,

$$
T_{\rm det}(d;F_0)=\Theta(\sqrt d).
$$

The asymptotic constants may depend on the chosen accuracy and success thresholds, but not on $d$. The upper bound prepares the exact target on every accepted outcome. In particular, it includes $F_0=1$ in the heralded statement. Repetition establishes any fixed success probability below one; probability-one exact preparation is not part of this theorem.

Here is an explicit upper bound valid for every integer $d\ge2$. Put $N=\lceil\sqrt d\rceil$. The [construction](construction.md) uses exactly $2N$ mixed specimens from each stream in one attempt, succeeds with probability at least $1/(5e)$, and outputs $T_\psi$ exactly on success. Thus it suffices to choose

$$
r_{\rm her}
=\left\lceil
5e\log\frac{1}{1-p_{\min}}
\right\rceil,
\qquad
T_{\rm her}(d;F_0,p_{\min})\le4\lceil\sqrt d\rceil r_{\rm her}.
$$

For deterministic preparation, output the vacuum pair if every attempt fails. Its fidelity is at least $1-\frac12 e^{-r/(5e)}$, so

$$
r_{\rm det}
=\left\lceil
5e\log\frac{1}{2(1-F_0)}
\right\rceil,
\qquad
T_{\rm det}(d;F_0)\le4\lceil\sqrt d\rceil r_{\rm det}.
$$

All logarithms here are natural. Both repetition counts are positive integers on their stated parameter ranges. These constants are convenient uniform guarantees, rather than optimal constants.

## Why balanced pure inputs suffice for the lower bound

The [converse](converse.md) grants a stronger input resource: $N$ exact copies of $\psi$ and $N$ exact copies of $\psi^*$, with arbitrary joint processing. In the fixed computational basis, write

$$
|v_N(\psi)\rangle
=|\psi\rangle^{\otimes N}\otimes|\psi^*\rangle^{\otimes N}.
$$

One pure specimen can simulate one requested mixed specimen through the known channel

$$
\mathcal D(X)
=\frac12X+\frac12\operatorname{Tr}(X)|{\rm vac}\rangle\langle{\rm vac}|.
$$

It sends $|\psi\rangle\langle\psi|$ to $\rho_\psi$, and similarly for the conjugate stream. The random replacement decision is hidden from the simulated processor.

Suppose the original processor has hard total budget $t$ and chooses its source adaptively. Give its simulator $t$ pure specimens of each type. On each source request, the simulator takes an unused specimen of the requested type and applies $\mathcal D$. Each stream can be requested at most $t$ times, so the simulation covers every execution branch and exactly reproduces the original source statistics. The balanced lower bound can therefore be applied with $N=t$.

This implication concerns the **total** budget. The theorem does not require every successful strategy to use $\Omega(\sqrt d)$ specimens from each stream separately. The explicit upper bound uses a balanced supply, while the lower bound permits any allocation and any adaptive request order within the hard total budget.

## Reading the proof

The [construction](construction.md) first treats pure conjugate specimens, proves that its success operator is a contraction on the entire input space, and then accounts for extraction from the mixed sources and bounded repetition. The [harmonic analysis](harmonic_analysis.md) computes the weight of the traceless sector and a multiplication coefficient on complex projective space. The [converse](converse.md) uses these quantities to bound the success-weighted fidelity of every processor.

The result is an information-theoretic statement about copies. The construction specifies known finite-dimensional quantum operations; no gate-efficiency bound is included. The state family has a known vacuum direction, rank two, and flat nonzero spectrum. Those promises are part of the theorem.

The assumption $d\ge2$ includes the smallest nontrivial signal space. If $d=1$, the signal ray is already known and $\psi\otimes\psi^*=|1,1\rangle$, so the target can be prepared without source specimens. The asymptotic problem begins at $d\ge2$.

The [related-work account](../references/RELATED_WORK.md) distinguishes this preparation theorem from earlier superposition constructions, ordinary random purification, and classical decision problems.
