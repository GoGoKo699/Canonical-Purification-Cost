# Exact frontier from mixed sources

[Model](model.md) · [Pure-copy frontier](exact_frontier.md) · [Balanced construction](construction.md) · [Access comparison](access_comparison.md) · [Verification](../verification/README.md)

The known orthogonal vacuum flag makes extraction from these mixed sources lossless. Consequently the exact frontier under separate hard source caps is the binomial average of the exact pure-copy frontier, rather than merely an upper-bound construction with a doubling overhead.

## Separate hard caps

Use the independent sources

```math
\rho_\psi=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+
|\psi\rangle\langle\psi|}{2},
\qquad
\rho_\psi^*=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+
|\psi^*\rangle\langle\psi^*|}{2}
```

and the same prescribed target $`T_\psi`$. Let $`Q_d^*(A,B)`$ be the maximum worst-case probability of exact heralded output when every branch requests at most $`A`$ ordinary mixed specimens and $`B`$ conjugate mixed specimens. All discarded registers, vacuum outcomes, filter failures and unsuccessful repetitions count toward these caps.

These are separate source caps with total maximum $`A+B`$. Adaptive request order and early stopping are permitted. If a stricter additional total cap $`t\lt A+B`$ is imposed, precollecting both pools would violate it; the theorem below is not a characterization of that different request-tree constraint.

## Exact binomial frontier

Let $`q_d^*(k,\ell)`$ be the [pure-copy optimum](exact_frontier.md), including its zero-budget boundary.

**Theorem.** For all $`d\ge2`$ and nonnegative integers $`A,B`$,

```math
\boxed{
Q_d^*(A,B)=
2^{-(A+B)}
\sum_{k=0}^{A}\sum_{\ell=0}^{B}
\binom Ak\binom B\ell\,q_d^*(k,\ell).
}
\tag{M1}
```

Equivalently $`Q_d^*(A,B)=\mathbb E[q_d^*(K,L)]`$, where $`K\sim\mathrm{Bin}(A,1/2)`$ and $`L\sim\mathrm{Bin}(B,1/2)`$ are independent.

### Proof

Precollect $`A+B`$ specimens. Any processor with the separate hard caps can be simulated on this input by selecting its next requested register and discarding unused ones. This includes adaptive order and all coherent processing after each request.

Measure every register with the known projectors

```math
P_0=|\mathrm{vac}\rangle\langle\mathrm{vac}|,
\qquad P_s=I-P_0.
```

When the outcome is forgotten, this measurement leaves the input unchanged. The input is already block diagonal in occupancy patterns; off-diagonal action between distinct blocks cannot affect a processor's output. Every pattern has probability $`2^{-(A+B)}`$, independent of $`\psi`$. Given counts $`(k,\ell)`$, known permutations put the signal registers into $`v_{k,\ell}(\psi)`$; all other registers are known vacua. Pattern positions contain no extra information about $`\psi`$.

For any exact successful processor, its unnormalized output is a sum of positive pattern-conditioned outputs. A positive sum supported on the single ray $`T_\psi`$ forces every summand to have support on that ray. Hence every conditioned map is itself exact, possibly with zero success.

Worst-case versus average success needs care. Twirling an exact pure or mixed processor over $`U(d)`$ preserves exactness and makes success uniform on the orbit, equal to its original Haar average. Thus the optimal Haar-average exact success equals the optimal worst-case success in each count sector. The average contribution from a pattern with counts $`(k,\ell)`$ is at most $`q_d^*(k,\ell)`$. Summing the pattern probabilities proves the upper bound in (M1).

Conversely, read the occupancy pattern and apply an optimal twirled pure-count instrument for the observed counts. The [pure LP](exact_frontier.md#the-exact-allocation-lp) attains each of its finitely many optima. Every success is exactly $`T_\psi`$, and summing their uniform probabilities attains (M1). This proves equality for arbitrary mixed-source processors, not just for protocols that initially choose to extract signals.

The argument also works for known, unequal signal probabilities by replacing the fair binomial weights. Its essential feature is the known orthogonal decomposition; it gives no analogous identity for general unflagged nonorthogonal mixtures.

## Strongly unequal supplies and extraction ceilings

The pure zero-budget boundary gives

```math
Q_d^*(A,0)=Q_d^*(0,B)=0,
\qquad
Q_d^*(A,B)\le(1-2^{-A})(1-2^{-B}).
\tag{M2}
```

In particular, one conjugate mixed specimen imposes success at most $`1/2`$, however large the ordinary supply. Using the sharp pure n-by-one optimum,

```math
\boxed{
Q_d^*(A,1)=
2^{-A}\sum_{k=0}^{A}\binom Ak
\frac{k}{d+2k-1}.
}
\tag{M3}
```

The $`k=0`$ term is zero. For $`A/d\to c>0`$ as $`d\to\infty`$, binomial concentration and bounded convergence imply

```math
Q_d^*(A,1)\longrightarrow\frac{c}{2(1+c)}.
```

For $`A/d\to\infty`$, this optimum tends to $`1/2`$. More generally, for fixed $`B\ge1`$, retain one conjugate signal whenever any occurs and use the sharp pure n-by-one filter on all ordinary signals. This yields

```math
Q_d^*(A,B)\ge
(1-2^{-B})\,
\mathbb E\left[\frac{2K}{d+2K-1}\right].
```

Together with (M2), it proves $`Q_d^*(A,B)\to1-2^{-B}`$ when $`B`$ is fixed and $`A/d\to\infty`$. The rare-stream extraction ceiling survives arbitrarily large supplies of the other source. Therefore a proposed copy-product scale alone cannot specify every fixed-success mixed frontier.

## Fully counted extraction and bounded repetition

For a simple explicit protocol, choose a pure filter with uniform exact success $`q`$ on $`(n,m)`$ signals. Request exactly $`A`$ and $`B`$ mixed specimens. Fail if either observed signal count is insufficient; otherwise retain known $`n,m`$ signal positions and apply the filter. Its exact success is

```math
u=q\,\Pr[K\ge n]\,\Pr[L\ge m].
\tag{M4}
```

| Resource | One attempt | At most $`R`$ independent attempts |
|---|---:|---:|
| Ordinary mixed requests | $`A`$ | $`RA`$ |
| Conjugate mixed requests | $`B`$ | $`RB`$ |
| Total mixed requests | $`A+B`$ | $`R(A+B)`$ |
| Ordinary signals used by filters | At most $`n`$ | At most $`Rn`$ |
| Conjugate signals used by filters | At most $`m`$ | At most $`Rm`$ |
| Exact heralded success | $`u`$ | $`1-(1-u)^R`$ |

The caps include vacua, unused surplus signals, failed extraction, rejected filters and unsuccessful previous attempts. Early stopping reduces consumption on some branches but does not change the hard maxima. For $`A=2n,B=2m`$, each binomial tail is at least $`1/2`$, so $`u\ge q/4`$. The [balanced construction](construction.md#extracting-pure-specimens-from-the-mixed-sources) uses this convenient bound.

A hard budget must stop after a fixed cap. The expected waiting cost $`2n`$ for obtaining $`n`$ signals is not a hard cap if requests continue indefinitely. Exact binomial tails give the finite success loss at any actual cap. Applying the optimal pure-count filter to every observed $`(K,L)`$ uses surplus information and attains (M1), whereas preselecting $`(n,m)`$ gives only the simpler lower bound (M4).

## Relation to program composition

The sister project [Quantum-Program-Composition](https://github.com/GoGoKo699/Quantum-Program-Composition) and this task share coherent contraction on separately symmetric copy pools and a whole-input-space physical normalization check. The [pure canonical filter](exact_frontier.md#the-pure-n-by-one-filter-is-contractive) adds a vacuum branch to an extracted state/conjugate pair, and exactness constrains their relative amplitude.

The supplied objects differ. Full unitary Choi programs have accessible two-register purifications with maximally mixed inner marginals. Here the mixed-source environments are inaccessible, and extracted signals are rank-one state specimens. The composition processor's polar-normalized successful output is generally approximate; polar normalization cannot be assumed to preserve this target's exact vacuum/signal coherence. Its unitary-Choi copy-product theorem is therefore not transferred by replacing $`d^2`$ with $`d`$.

This repository is the authoritative home of the exact canonical rigidity, allocation LP and binomial mixed frontier. The [composition-side boundary account](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/main/science/canonical_purification_boundary.md) explains the shared method with its original Choi result intact. The [related-work account](../references/RELATED_WORK.md) credits the inherited superposition, harmonic and stochastic conversion machinery. The broad $`nm`$-of-order-$`d`$ interpretation remains conjectural here; no new approximate-fidelity product law or gate-efficient optimal implementation is asserted.
