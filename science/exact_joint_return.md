# Canonical purification with returned pure specimens

[Model](model.md) · [Exact target-only frontier](exact_frontier.md) · [Finite checks](../verification/README.md#joint-return-checks)

Fix $`d\ge2`$ and positive integers $`n,m`$. Supply $`n`$ pure specimens of an unknown unit vector $`|\psi\rangle`$ and $`m`$ pure specimens of its conjugate $`|\psi^*\rangle`$ in the given signal basis. Write

```math
v_{n,m}(\psi)=|\psi\rangle^{\otimes n}|\psi^*\rangle^{\otimes m},
\qquad
T_\psi=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}.
```

The joint target is $`T_\psi\otimes v_{n-1,m-1}(\psi)`$. An accepted outcome of an exact instrument must give this full product, up to the success probability. The processor may use arbitrary collective operations, ancillas, adaptive measurements and known routing of the returned registers. The failure branch has no return requirement.

**Exact-return theorem.** The maximum worst-case acceptance probability is

```math
q_{\mathrm{return}}(d,n,m)=\frac{2M}{d+2M-1},
\qquad M=\max(n,m).
```

**Approximate-return construction.** A deterministic processor attains joint squared fidelity

```math
F_{\mathrm{global}}\ge \frac{nm}{nm+(d-1)/4}
```

uniformly over $`\psi`$. This fidelity tests the purification and all returned specimens together.

At $`d=n=m=2`$, exact return succeeds with probability $`4/5`$. The [target-only optimum](exact_frontier.md) is $`12/13`$ at the same allocation. In general, a fixed exact-return success $`q\in(0,1)`$ requires $`M\ge q(d-1)/[2(1-q)]`$. The smaller pool can contain one specimen, so the minimum total is of order $`d`$ for fixed $`q`$. The existing [target-only construction](construction.md) attains fixed exact success at order $`\sqrt d`$ by filtering the residual. The deterministic polar construction below also permits balanced pure supplies of order $`\sqrt d`$ for any fixed joint squared fidelity below one.

## The common map and the contraction norm

Use the symmetric spaces $`R_{n,m}=\mathrm{Sym}^n(\mathcal V)\otimes\mathrm{Sym}^m(\overline{\mathcal V})`$. As in the [exact frontier](exact_frontier.md#the-pure-n-by-one-filter-is-contractive), $`C=\sum_i a_i b_i`$ contracts the two pools and

```math
E=\frac1{\sqrt{nm}}\sum_{i,j}|i,j\rangle\otimes a_i b_j
```

isometrically extracts one signal specimen from each pool. The annihilators act on orthonormal occupation bases. The map whose action is the joint target is

```math
W=\frac1{\sqrt2}\left(
|\mathrm{vac},\mathrm{vac}\rangle\otimes \frac{C}{\sqrt{nm}}+E
\right),
\qquad
W^\dagger W=\frac12\left(I+\frac{C^\dagger C}{nm}\right).
```

The vacuum and signal sectors are orthogonal, and $`E^\dagger E=I`$ on $`R_{n,m}`$. Acting on the promised input, $`C`$ gives $`\sqrt{nm}\,v_{n-1,m-1}(\psi)`$, while $`E`$ retains both extracted signals. Therefore $`Wv_{n,m}(\psi)=T_\psi\otimes v_{n-1,m-1}(\psi)`$.

To evaluate the norm on the whole input space, let $`\Lambda_{n,m}=\|C^\dagger C\|_{R_{n,m}}`$. The commutator $`[C,C^\dagger]=d+N_a+N_b`$ on the residual sector gives

```math
\Lambda_{n,m}=\Lambda_{n-1,m-1}+d+n+m-2,
\qquad
\Lambda_{n,0}=\Lambda_{0,m}=0.
```

Here $`C^\dagger C`$ on the input and $`CC^\dagger`$ on the residual have the same largest eigenvalue. Summing the recurrence gives $`\Lambda_{n,m}=\min(n,m)(d+M-1)`$. Define $`\lambda=(d+M-1)/M`$. It follows that $`\|W\|^2=(1+\lambda)/2`$.

## Why exact return fixes the entire success map

Refine the success branch into Kraus maps $`K_\alpha`$, applying any known routing first. Positivity and the rank-one joint target imply that each $`K_\alpha v_{n,m}(\psi)`$ is a scalar multiple of the joint target, including the zero vector. This property also holds when the instrument discards records or reports several success outcomes.

For independent formal vectors $`z,w`$, write $`\eta(z,w)=\sum_i z_iw_i`$. The homogeneous joint target is

```math
t(z,w)=\frac{\eta(z,w)|\mathrm{vac},\mathrm{vac}\rangle+\sum_{i,j}z_iw_j|i,j\rangle}{\sqrt2}
\otimes z^{\otimes(n-1)}\otimes w^{\otimes(m-1)}.
```

This vector agrees with the physical joint target at $`w=\overline z`$ and $`\|z\|=1`$. In fixed coordinates put $`f_\alpha(z,w)=K_\alpha(z^{\otimes n}\otimes w^{\otimes m})`$. Both $`f_\alpha`$ and $`t`$ have bidegree $`(n,m)`$. Every cross product $`(f_\alpha)_i t_j-(f_\alpha)_j t_i`$ vanishes on the physical unit sphere. Homogeneity extends the identity to $`w=\overline z`$ at arbitrary norm. Substituting $`z=x+iy`$ and $`w=x-iy`$ gives a polynomial vanishing for every real $`x,y`$. The substitution is invertible over $`\mathbb C`$, so all these are polynomial identities in independent $`z,w`$.

The target coordinates include $`z_1^n w_1^m/\sqrt2`$ and $`z_2^n w_2^m/\sqrt2`$. These use disjoint variables, so all target coordinates have greatest common divisor one. Taking the quotient of one Kraus coordinate by the corresponding nonzero target coordinate gives a common rational factor for every coordinate. In lowest terms its denominator divides every target coordinate, so the factor is a polynomial. Bidegree equality forces it to be a constant $`c_\alpha`$.

The physical orbit spans $`R_{n,m}`$. A linear functional vanishing on that orbit gives a homogeneous polynomial that is identically zero by the same substitution, forcing every symmetric coefficient to vanish. Hence $`K_\alpha=c_\alpha W`$ on the whole symmetric input. The success probability $`q=\sum_\alpha|c_\alpha|^2`$ is uniform and the trace-nonincreasing condition gives

```math
q W^\dagger W\le I,\qquad q\le\frac2{1+\lambda}.
```

The map $`W/\|W\|`$ attains this value. Extending it by zero off the symmetric subspace and completing with the complementary failure effect gives an instrument on the physical input space. When one pool has just one specimen, dropping the return requirement gives the same probability by the exact n-by-one theorem.

## Polar normalization and deterministic joint fidelity

Put $`A=W^\dagger W`$. Since $`A\ge I/2`$, the polar map $`U_{\mathrm{pol}}=WA^{-1/2}`$ is an isometry on $`R_{n,m}`$. Projecting onto that known input subspace and supplying a fixed output on its complement completes it to a channel. For a normalized promised input $`v=v_{n,m}(\psi)`$, the squared overlap with the normalized target $`Wv`$ is

```math
F_{\mathrm{global}}=|\langle Wv,U_{\mathrm{pol}}v\rangle|^2
=\langle v,\sqrt A\,v\rangle^2.
```

Write $`B=C^\dagger C`$ and $`r=v_{n-1,m-1}(\psi)`$. The identity $`Cv=\sqrt{nm}\,r`$ gives the first moment $`\langle B\rangle_v=nm`$. For the second, use $`\langle B^2\rangle_v=nm\langle r,CC^\dagger r\rangle`$. The commutator contributes $`d+n+m-2`$. The residual contraction contributes $`(n-1)(m-1)`$, including zero when either residual pool is empty. Consequently

```math
\langle B^2\rangle_v=nm(nm+d-1),\qquad
\langle A\rangle_v=1,\qquad
\langle A^2\rangle_v=1+\frac{d-1}{4nm}.
```

For the spectral distribution of $`A`$ in $`v`$, Hölder's inequality gives $`1=\mathbb E[A]\le(\mathbb E[\sqrt A])^{2/3}(\mathbb E[A^2])^{1/3}`$. This proves the stated fidelity guarantee. The guarantee applies to any positive pure allocation. The optimal approximate allocation law and exact return of mixed-source registers remain open here.

## Sister results

[Quantum Program Composition](https://github.com/GoGoKo699/Quantum-Program-Composition/blob/main/science/exact_joint_return.md) uses polynomial rigidity on unitary matrix entries to compute its own exact joint-return optimum. Its polar construction motivated the approximate joint-return protocol above. [Quantum Multicopy Teleportation](https://github.com/GoGoKo699/Quantum-Multicopy-Teleportation/blob/main/science/exact-return.md) evaluates the same contraction norm after reducing an ordered port space to symmetric pools. Its exact Bell-return theorem uses an instrument at the sender and port selection at the receiver. With the same $`\lambda`$, composition and teleportation both have optimal exact success $`1/(d\lambda)`$, while purification coherently combines the vacuum contraction with isometric signal extraction and has optimal exact success $`2/(1+\lambda)`$.
