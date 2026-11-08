# Exact heralded frontier with unequal pure supplies

[Model](model.md) · [Mixed-source frontier](mixed_frontier.md) · [Balanced construction](construction.md) · [Harmonic analysis](harmonic_analysis.md) · [Verification](../verification/README.md)

The exact target imposes more structure than an approximate fidelity requirement. Every successful amplitude must factor into the same canonical target and an inaccessible residual vector. This factorization determines the full pure-copy frontier, including highly unequal allocations, as an attained finite linear program.

## Task and theorem

Fix $`d\ge2`$, $`V=\mathbb C^d`$ and the known vacuum from the [model](model.md). Supply

```math
v_{n,m}(\psi)=|\psi\rangle^{\otimes n}\otimes|\psi^*\rangle^{\otimes m},
\qquad
|T_\psi\rangle=
\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}.
```

Let $`q_d^*(n,m)`$ be the maximum worst-case success probability of an exact heralded processor:

```math
\Lambda(|v_{n,m}(\psi)\rangle\langle v_{n,m}(\psi)|)
=p_\psi|T_\psi\rangle\langle T_\psi|,
\qquad
\inf_\psi p_\psi=q.
```

Here $`\Lambda`$ is any completely positive trace-nonincreasing map, fixed independently of $`\psi`$. Arbitrary ancillary memory, collective operations, adaptive measurements, multiple accepting outcomes and discarded systems are allowed. The budgets are hard separate caps: a processor may request at most $`n`$ pure ordinary specimens and $`m`$ pure conjugate specimens on every branch. Precollecting both pools and discarding unused registers includes all such request orders.

The exact results are:

```math
q_d^*(n,0)=q_d^*(0,m)=0,
\qquad
q_d^*(n,1)=q_d^*(1,n)=\frac{2n}{d+2n-1}\quad(n\ge1).
```

For every positive allocation, the [finite LP below](#the-exact-allocation-lp) gives the exact optimum. It has $`\min(n,m)`$ variables and an explicit physical realization for every feasible point. No elementary closed formula for all allocations is asserted. The proposed interpretation that a copy product of order $`d`$ controls a specified constant-success regime remains a separate conjecture; it is not a premise of the LP, a product-only mixed-source theorem, or a law for approximate output.

## The pure n-by-one filter is contractive

Use normalized symmetric occupation spaces

```math
R_{n,m}=\mathrm{Sym}^n(V)\otimes
\mathrm{Sym}^m(\overline V),
\qquad R_{0,0}=\mathbb C.
```

The annihilators $`a_i,b_i`$ have occupation matrix elements $`\sqrt{n_i}`$ in their respective factors. This is finite-dimensional tensor notation, not an assumption of supplied bosonic hardware. For $`n,m\ge1`$, put

```math
C_{n,m}=\sum_i a_i b_i,
\qquad
E_{n,m}=\frac1{\sqrt{nm}}\sum_{i,j}|i,j\rangle\otimes a_i b_j,
```

and define the fixed linear map

```math
W_{n,m}
=\frac1{\sqrt2}
\left(
|\mathrm{vac},\mathrm{vac}\rangle\otimes\frac{C_{n,m}}{\sqrt{nm}}
+E_{n,m}
\right).
```

Number conservation gives $`E_{n,m}^\dagger E_{n,m}=I`$ on all of $`R_{n,m}`$. On the promised inputs,

```math
C_{n,m}v_{n,m}(\psi)=\sqrt{nm}\,v_{n-1,m-1}(\psi),
\qquad
W_{n,m}v_{n,m}(\psi)=T_\psi\otimes v_{n-1,m-1}(\psi).
```

The last identity alone does not make $`W_{n,m}`$ a physical success map. Its norm must be controlled on the entire input space.

For $`m=1`$, the residual $`R_{n-1,0}`$ contains no conjugate particle. The commutator

```math
[C,C^\dagger]=d+N_a+N_b
```

therefore implies

```math
C_{n,1}C_{n,1}^\dagger=(d+n-1)I_{R_{n-1,0}}.
```

The vacuum and signal output sectors are orthogonal, so

```math
W_{n,1}^\dagger W_{n,1}
=\frac12\left(I+\frac{C_{n,1}^\dagger C_{n,1}}n\right),
\qquad
\|W_{n,1}\|^2=\frac{d+2n-1}{2n}.
```

Consequently

```math
K_{n,1}=\sqrt{\frac{2n}{d+2n-1}}\,W_{n,1}
```

is a contraction. Extend it by zero outside $`R_{n,1}`$ and complete it with failure effect $`I-K_{n,1}^\dagger K_{n,1}`$. Its uniform exact success is $`2n/(d+2n-1)`$. At $`n=1`$, this recovers the [one-pair construction](construction.md#the-case-of-one-specimen-from-each-stream) with success $`2/(d+1)`$.

## Rigidity of every exact processor

A success map has a Stinespring contraction

```math
\mathsf V:R_{n,m}\longrightarrow
(\mathcal H\otimes\mathcal H)\otimes\mathcal E,
\qquad \mathsf V^\dagger\mathsf V\le I.
```

This incorporates every success Kraus operator and every inaccessible discarded system. Since the reduced accepted output has rank one, for every unit $`\psi`$

```math
\mathsf Vv_{n,m}(\psi)=T_\psi\otimes e(\psi).
```

The residual $`e(\psi)`$ can be unnormalized or zero. No individual Kraus outcome is required to have positive success on every input.

For one scalar environment coordinate, let $`A(z,w)`$ be the vacuum amplitude and $`B_{ij}(z,w)`$ the signal amplitude. They are polynomials of bidegree $`(n,m)`$ in independent variables $`z,w`$. On unit physical vectors, where $`w=\overline z`$, exactness says

```math
B_{ij}(z,\overline z)=z_i\overline z_j A(z,\overline z).
```

Set $`\eta(z,w)=\sum_i z_iw_i`$. Rescale a nonzero physical vector to unit norm. Homogenizing the preceding equality gives

```math
\eta B_{ij}=z_iw_j A.
```

This first holds for all $`z`$ with $`w=\overline z`$. Substitute $`z=x+iy,w=x-iy`$; the difference is a polynomial vanishing for every real $`x,y`$, hence identically zero. The invertible linear substitution proves the identity for independent formal variables. The unit sphere itself is not assumed Zariski dense in those variables.

For $`d\ge2`$, $`\eta`$ is irreducible: a factorization of this bilinear form would have coefficient matrix of rank one, whereas its matrix has rank $`d`$. It is coprime to each $`z_iw_j`$. Unique factorization thus forces

```math
A=\eta a,\qquad B_{ij}=z_iw_j a,
\qquad a\in\mathcal P_{n-1,m-1}.
```

Here $`\mathcal P_{a,b}`$ denotes bihomogeneous polynomials of bidegree $`(a,b)`$. Amplitudes outside the two target output sectors vanish by the same polynomial argument. If either budget is zero, divisibility would require a negative bidegree, so every accepted amplitude is zero. This proves the zero-budget boundary, including the no-input case.

The coherent orbit spans $`R_{n,m}`$: a linear functional vanishing on that orbit is a polynomial vanishing on all physical vectors, hence has zero coefficients. Therefore the factorization is an operator identity,

```math
\mathsf V=(I_{\rm out}\otimes L)W_{n,m}.
```

The $`\sqrt2`$ factor from the vacuum target amplitude is absorbed into $`L`$. With $`X=L^\dagger L`$, exact physical success maps are precisely the positive residual operators satisfying

```math
X\ge0,\qquad
W_{n,m}^\dagger(I_{\rm out}\otimes X)W_{n,m}\le I.
\tag{E1}
```

Their success is

```math
p_\psi=
\langle v_{n-1,m-1}(\psi)|X|v_{n-1,m-1}(\psi)\rangle.
```

Conversely, every feasible $`X`$ is realized by $`L=\sqrt X`$ followed by a failure completion. The residual operator need not itself obey $`X\le I`$; (E1) is the physical condition.

## Covariance and the sharp n-by-one converse

The map $`W_{n,m}`$ intertwines the input action $`U^{\otimes n}\otimes\overline U^{\otimes m}`$ with the target action and residual action. Haar averaging $`X`$ under the residual representation preserves (E1). It makes the success probability independent of $`\psi`$, equal to the original Haar average and at least the original worst-case guarantee. Thus optimal worst-case and optimal Haar-average exact success coincide.

For $`m=1`$, the residual representation $`\mathrm{Sym}^{n-1}(V)`$ is irreducible. Schur's lemma makes the averaged operator $`X=cI`$. Equation (E1) then requires

```math
c\,\|W_{n,1}\|^2\le1,
\qquad
q\le c\le\frac{2n}{d+2n-1}.
```

The filter above attains the bound. This proves optimality over all exact processors, rather than merely optimizing its scalar normalization.

## Unequal harmonic sectors and orbit weights

By exchanging the two supplied pools, assume $`n\ge m\ge1`$. Set $`r=n-m`$ and $`k=m`$. The Fischer decomposition is

```math
\mathcal P_{n,m}
=\bigoplus_{j=0}^k
\eta^{k-j}\mathcal H_{r+j,j},
\qquad
\mathcal H_{a,b}
=\ker\left(\sum_i\partial_{z_i}\partial_{w_i}\right)
\big|_{\mathcal P_{a,b}}.
```

These are the unequal-degree complex harmonics. Their dimensions are

```math
h_j=
\binom{d+r+j-1}{r+j}\binom{d+j-1}{j}
-\binom{d+r+j-2}{r+j-1}\binom{d+j-2}{j-1},
\tag{E2}
```

with the second term defined as zero at $`j=0`$. Fischer decomposition follows from the contraction/insertion commutator as in the [balanced harmonic account](harmonic_analysis.md).

For completeness, irreducibility and multiplicity one can be checked from the cyclic coherent vector at $`\psi=|1\rangle`$. Its stabilizer $`U(1)\times U(d-1)`$ acts through the character of charge $`r`$. The full character subspace has dimension $`k+1`$: its polynomials are generated by the first-coordinate factors and powers of the perpendicular squared norm. Each nonzero invariant Fischer summand contains a nonzero projection of the cyclic vector onto its character space. Hence each of the $`k+1`$ summands has a one-dimensional character line and is irreducible. Two equivalent summands would identify these lines under an intertwiner; the coherent orbit would then occupy just one fixed multiplicity direction and could not span both. Cyclicity excludes that possibility.

Put $`s=\langle\psi|\phi\rangle`$ and $`t=|s|^2`$. The unit-diagonal positive-definite sector kernels are

```math
Z_j(\psi,\phi)=s^rQ_j(t),
\qquad
Q_j(t)=\frac{P_j^{(d-2,r)}(2t-1)}{P_j^{(d-2,r)}(1)}.
\tag{E3}
```

Here $`P_j^{(\alpha,\beta)}`$ is the Jacobi polynomial. The factor $`s^r`$ retains the input's unequal global-phase charge. Reversing the kernel convention conjugates all kernels without changing the coefficients or optimum. The radial Haar measure and Jacobi norm give

```math
(d-1)\int_0^1t^r(1-t)^{d-2}Q_j(t)Q_\ell(t)\,dt
=\frac{\delta_{j\ell}}{h_j}.
\tag{E4}
```

The input Gram kernel is $`s^rt^k`$. Expand

```math
t^k=\sum_{j=0}^kp_jQ_j(t),
\qquad
p_j=h_j\frac{\Gamma(d)n!m!}{(m-j)!\,\Gamma(d+n+j)}.
\tag{E5}
```

Every $`p_j`$ is positive and $`\sum_jp_j=1`$. To derive the normalization explicitly, shifted Rodrigues gives

```math
Q_j(t)=
\frac{(-1)^j}{j!\binom{j+d-2}{j}}\,
(1-t)^{-(d-2)}t^{-r}
\frac{d^j}{dt^j}
\left[(1-t)^{d-2+j}t^{r+j}\right].
```

Insert this into (E4), integrate by parts $`j`$ times and use the beta integral. The boundary terms vanish, and

```math
\begin{aligned}
\frac{p_j}{h_j}
&=(d-1)\int_0^1t^{k+r}(1-t)^{d-2}Q_j(t)\,dt\\
&=\frac{(d-1)k!}{(k-j)!\,j!\binom{j+d-2}{j}}
\mathrm{B}(k+r+1,d-1+j)\\
&=\frac{\Gamma(d)n!m!}{(m-j)!\,\Gamma(d+n+j)}.
\end{aligned}
```

In particular, the highest traceless input weight is

```math
p_{\rm top}=p_k
=\frac{\Gamma(d+n-1)\Gamma(d+m-1)}
{\Gamma(d-1)\Gamma(d+n+m-1)}
=\prod_{\ell=0}^{m-1}
\frac{d-1+\ell}{d+n-1+\ell}.
\tag{E6}
```

## The exact allocation LP

The normalized Jacobi recurrence is

```math
tQ_j=A_jQ_{j+1}+B_jQ_j+C_jQ_{j-1},
```

where

```math
A_j=
\frac{(j+d-1)(j+d+r-1)}
{(2j+d+r-1)(2j+d+r)},
\qquad
C_j=
\frac{j(j+r)}
{(2j+d+r-2)(2j+d+r-1)}
\quad(j\ge1),
```

and $`C_0=0`$, $`B_j=1-A_j-C_j`$. These coefficients are nonnegative. Defining $`C_0`$ separately includes $`d=2,r=0`$ without a removable $`0/0`$.

Let $`M`$ be the $`(k+1)\times k`$ matrix with nonzero entries

```math
M_{j,j}=\frac{1+B_j}{2},
\qquad
M_{j+1,j}=\frac{A_j}{2},
\qquad
M_{j-1,j}=\frac{C_j}{2}\quad(j\ge1).
\tag{E7}
```

**Theorem.** For $`n\ge m\ge1`$, with $`p`$ from (E5),

```math
\boxed{
q_d^*(n,m)=
\max\left\{
\sum_{j=0}^{k-1}u_j:\ 
u_j\ge0,\ Mu\le p
\right\}.
}
\tag{E8}
```

Together with exchange symmetry and the zero-budget boundary, this characterizes every allocation. The residual $`R_{n-1,m-1}`$ contains exactly the sectors $`j=0,\ldots,k-1`$.

### Necessity for arbitrary processors

Twirl an arbitrary exact success map as above. Its success becomes uniform. Its environment Gram kernel

```math
f(\psi,\phi)=\langle e(\psi)|e(\phi)\rangle
```

is invariant and positive definite. Polynomial rigidity restricts every environment coordinate to the residual polynomial space. Multiplicity one and Schur's lemma therefore force

```math
f(\psi,\phi)=s^r\sum_{j=0}^{k-1}u_jQ_j(t),
\qquad u_j\ge0.
```

Nonnegative coefficients are equivalent to kernel positivity because each $`Z_j`$ is an irreducible reproducing kernel, with mutually orthogonal feature spaces. The input kernel minus the accepted output kernel must be positive definite by contractivity. Since

```math
\langle T_\psi|T_\phi\rangle=\frac{1+t}{2},
```

this condition is positivity of $`s^rt^k-(1+t)f/2`$. Expanding with the recurrence gives exactly $`Mu\le p`$. On the diagonal, success is $`\sum_ju_j`$. The arbitrary inaccessible environment cannot add further sectors, because rigidity already restricts each of its coordinates.

### Sufficiency as a physical instrument

For any feasible $`u`$, realize $`f`$ by finite feature vectors $`e(\psi)`$ using the residual sector spaces scaled by $`\sqrt{u_j}`$. Positivity of the difference kernel says that for every finite set and coefficients $`c_a`$,

```math
\left\|\sum_a c_a T_{\psi_a}\otimes e(\psi_a)\right\|^2
\le
\left\|\sum_a c_a v_{n,m}(\psi_a)\right\|^2.
```

Thus the assignment $`v_{n,m}(\psi)\mapsto T_\psi\otimes e(\psi)`$ respects every linear relation among the input vectors and defines a contraction on their span. That span is $`R_{n,m}`$. Extend the map by zero on the orthogonal complement and complete it with failure effect $`I-\mathsf V^\dagger\mathsf V`$. This is a finite-dimensional success instrument with exact target and uniform success $`\sum_ju_j`$.

Each column of $`M`$ sums to one. Hence feasibility gives $`\sum_ju_j\le\sum_jp_j=1`$, so the feasible set is compact and the maximum is attained. This proof constructs a valid processor; it does not assume efficient synthesis of the optimal residual filter.

## An exact converse and a nontrivial optimum

Rigidity makes the vacuum component $`\mathsf A=(\langle\mathrm{vac},\mathrm{vac}|\otimes I)\mathsf V`$ annihilate the highest input sector. Since $`\mathsf A^\dagger\mathsf A\le I`$ and the weight (E6) is constant on the orbit, every exact processor obeys the pointwise bound

```math
p_\psi=2\|\mathsf A v_{n,m}(\psi)\|^2
\le
\min\left\{1,2(1-p_{\rm top})\right\}
\le
\min\left\{1,\frac{2nm}{d+\max(n,m)-1}\right\}.
\tag{E9}
```

For $`n\ge m`$, the last step uses

```math
1-\prod_{\ell=0}^{m-1}
\left(1-\frac n{d+n-1+\ell}\right)
\le
\sum_{\ell=0}^{m-1}\frac n{d+n-1+\ell}
\le\frac{nm}{d+n-1}.
```

This exact-output converse does not imply an approximate-fidelity product law.

For $`d=2,n=m=2`$, the input weights are $`p=(1/3,1/2,1/6)`$. The LP is

```math
\frac34u_0+\frac1{12}u_1\le\frac13,
\qquad
\frac14u_0+\frac34u_1\le\frac12,
\qquad u_1\le1,
\qquad u_0,u_1\ge0.
```

The feasible vector $`(u_0,u_1)=(5/13,7/13)`$ has success $`12/13`$. The nonnegative dual vector $`(12/13,16/13,0)`$ has the same objective, proving

```math
q_2^*(2,2)=\frac{12}{13}.
```

The residual weights in $`R_{1,1}`$ are $`(1/2,1/2)`$, so a corresponding positive operator in (E1) is

```math
X=\frac{10}{13}P_{\rm scalar}
+\frac{14}{13}P_{\rm traceless}.
```

The success effect has eigenvalues $`7/13`$ with multiplicity five and $`1`$ with multiplicity four. This improves the [balanced top-residual filter](construction.md), whose success is $`1/2`$ in this case. That filter establishes the desired copy scale, but is not generally optimal at a fixed finite allocation.

## Dependencies and boundaries

The [balanced construction](construction.md), its one-pair case and the [robust total-copy converse](converse.md) retain their own statements. The new exact rigidity and LP use the stronger rank-one output promise; they do not replace the approximate-output argument. The exact mixed frontier follows by the [separate occupancy reduction](mixed_frontier.md).

Positive-definite-kernel criteria for covariant stochastic pure-state conversion are established machinery: Marvian and Spekkens, [arXiv:1104.0018v2](https://arxiv.org/abs/1104.0018v2), §IX, Theorem 26 and Corollary 27. The work here identifies this target's residual polynomial support, unequal charged harmonic weights and finite allocation constraints. Jacobi identities and complex harmonic decomposition are credited in [Related work](../references/RELATED_WORK.md).

The sister project [Quantum-Program-Composition](https://github.com/GoGoKo699/Quantum-Program-Composition/tree/a5a49a020ef9cf29a7beffd0d3129f09d76b712d) shares coherent contraction and whole-space normalization. Its unitary Choi theorem and approximate successful polar output have different hypotheses. Neither supplies a premise for (E8) or (E9); see the [operational comparison](mixed_frontier.md#relation-to-program-composition).
