# Harmonic analysis of balanced conjugate copies

The balanced input $`\psi^{\otimes N}\otimes(\psi^*)^{\otimes N}`$ has an orthogonal decomposition into complex-projective harmonics. This account derives the decomposition, its normalization, and the multiplication estimate used in the [converse](converse.md). It also identifies the traceless projector used in the [construction](construction.md).

The operational promises are specified in the [model](model.md), and the purification-source comparison is in [access_comparison.md](access_comparison.md). Connections with earlier work are collected in [RELATED_WORK.md](../references/RELATED_WORK.md).

## 1. Conventions and the polynomial realization

Fix $`d\geq2`$ and $`V=\mathbb C^d`$ with its supplied orthonormal basis. The conjugate Hilbert space is $`\overline V`$. Inner products are conjugate linear in their first argument:

```math
\langle x,y\rangle=x^\dagger y.
```

Let $`\mu`$ be the probability measure induced by Haar measure on the unit sphere of $`V`$. All functions below are invariant under $`\psi\mapsto e^{i\theta}\psi`$, so they may equivalently be regarded as functions on $`\mathbb{CP}^{d-1}`$. For scalar or Hilbert-space-valued functions, use

```math
\langle f,g\rangle_2
=\int\langle f(\psi),g(\psi)\rangle\,d\mu(\psi),
\qquad
\|f\|_2^2=\langle f,f\rangle_2.
```

The balanced tensor space and its coherent input vectors are

```math
\mathcal R_N
=\mathrm{Sym}^N(V)\otimes\mathrm{Sym}^N(\overline V),
\qquad
v_N(\psi)=\psi^{\otimes N}\otimes(\psi^*)^{\otimes N}.
\tag{H1}
```

Here $`\mathcal R_0=\mathbb C`$ and $`v_0=1`$. The unitary-group action is

```math
D_N(U)=U^{\otimes N}\otimes\overline U^{\otimes N}.
```

Introduce independent formal variables $`z=(z_1,\ldots,z_d)`$ and $`w=(w_1,\ldots,w_d)`$. Let $`\mathscr P_{p,q}`$ be the polynomials homogeneous of degree $`p`$ in $`z`$ and degree $`q`$ in $`w`$. On their direct sum, define the Fischer inner product by

```math
\langle z^\alpha w^\beta,z^{\alpha'}w^{\beta'}\rangle_F
=\alpha!\,\beta!\,\delta_{\alpha,\alpha'}\delta_{\beta,\beta'}.
\tag{H2}
```

Thus multiplication by $`z_i`$ is adjoint to $`\partial_{z_i}`$, and multiplication by $`w_i`$ is adjoint to $`\partial_{w_i}`$. A unitary polynomial realization of $`\mathcal R_N`$ is

```math
\mathcal B_N:
|\alpha\rangle\otimes|\overline\beta\rangle
\longmapsto
\frac{w^\alpha z^\beta}{\sqrt{\alpha!\,\beta!}},
\qquad |\alpha|=|\beta|=N,
\tag{H3}
```

where the kets on the left are normalized occupation vectors. The swap of $`z`$ and $`w`$ in this convention makes the coefficient-function map linear in its tensor argument:

```math
(J_Nu)(\psi)
:=\langle v_N(\psi),u\rangle
=N!\,(\mathcal B_Nu)(\psi,\overline\psi).
\tag{H4}
```

Indeed,

```math
v_N(\psi)
=N!\sum_{|\alpha|=|\beta|=N}
\frac{\psi^\alpha\overline\psi^\beta}
{\sqrt{\alpha!\,\beta!}}
|\alpha\rangle\otimes|\overline\beta\rangle.
```

Restriction of a polynomial in $`\mathscr P_{N,N}`$ to $`w=\overline z`$ and $`\|z\|=1`$ is injective. If the restriction vanishes, homogeneity makes it vanish for every $`z\in\mathbb C^d`$. Substituting $`z=x+iy`$ and $`w=x-iy`$ gives a polynomial that vanishes for every real $`x,y`$; all its coefficients therefore vanish. The change of formal variables is invertible, so the original polynomial is zero.

It follows that $`J_N`$ is injective and that

```math
\mathrm{span}\{v_N(\psi):\|\psi\|=1\}=\mathcal R_N.
\tag{H5}
```

This cyclicity property will supply a short proof of irreducibility below. The intertwining convention is

```math
J_ND_N(U)=\mathcal U(U)J_N,
\qquad
(\mathcal U(U)f)(\psi)=f(U^\dagger\psi).
\tag{H6}
```

## 2. Fischer decomposition and the traceless sector

Define multiplication and contraction operators

```math
s(z,w)=\sum_{i=1}^d z_iw_i,
\qquad
\Delta=\sum_{i=1}^d\partial_{z_i}\partial_{w_i},
\qquad
\mathscr H_{p,q}=\ker\Delta\cap\mathscr P_{p,q}.
\tag{H7}
```

On the physical slice $`w=\overline z`$, $`s=\|z\|^2`$. The real Euclidean Laplacian is $`4\Delta`$, so $`\mathscr H_{p,q}`$ is the usual space of bihomogeneous complex harmonics. The Fischer decomposition and its complex-harmonic interpretation are standard; see [De Bie, Sommen, and Wutzig, §2.2, Lemma 3][DSW]. We give the needed proof and normalization here.

Because $`s^\dagger=\Delta`$ in the Fischer inner product, finite-dimensional orthogonal-complement duality gives

```math
\mathscr P_{N,N}
=\mathscr H_{N,N}\mathbin{\oplus_F}s\mathscr P_{N-1,N-1}.
\tag{H8}
```

Multiplication by $`s`$ is injective. Iteration therefore gives the algebraic direct sum

```math
\mathscr P_{N,N}
=\bigoplus_{\ell=0}^N s^{N-\ell}\mathscr H_{\ell,\ell}.
\tag{H9}
```

The summands in (H9) are also orthogonal in the Fischer inner product. To see both this fact and their normalization, introduce the Euler operators $`E_z=\sum_i z_i\partial_{z_i}`$ and $`E_w=\sum_iw_i\partial_{w_i}`$. Direct differentiation gives

```math
[\Delta,s]=d+E_z+E_w.
```

For $`h\in\mathscr H_{\ell,\ell}`$ and $`j\geq1`$, it follows that

```math
\Delta(s^jh)
=j(d+2\ell+j-1)s^{j-1}h,
\qquad
\|s^jh\|_F^2
=j!\,(d+2\ell)_j\,\|h\|_F^2.
\tag{H10}
```

Here $`(a)_j=a(a+1)\cdots(a+j-1)`$. The first identity follows by commuting $`\Delta`$ through the $`j`$ factors of $`s`$; the second follows by applying the first identity $`j`$ times and using adjointness. If $`j>k`$, then moving $`k`$ factors of $`s`$ from one side of an inner product to the other leaves a positive power of $`s`$ paired with a harmonic polynomial, which gives zero. This proves the orthogonality in (H9).

Transfer these spaces back to the tensor realization:

```math
\mathcal V_{N,\ell}
:=\mathcal B_N^{-1}
\bigl(s^{N-\ell}\mathscr H_{\ell,\ell}\bigr),
\qquad
\mathcal R_N=\bigoplus_{\ell=0}^N\mathcal V_{N,\ell}.
\tag{H11}
```

Let $`P_{N,\ell}`$ be the corresponding orthogonal projections. In occupation notation the contraction

```math
C_N=\sum_{i=1}^d a_ib_i:\mathcal R_N\longrightarrow\mathcal R_{N-1}
```

corresponds under $`\mathcal B_N`$ to $`\Delta`$. Therefore the top projector used in the construction is precisely

```math
P_N:=P_{N,N},
\qquad
\mathrm{ran}P_N=\ker C_N.
\tag{H12}
```

In particular, (H10) implies

```math
C_NC_N^\dagger
=(d+2N-2)I
\quad\text{on }\ker C_{N-1},
\tag{H13}
```

with the natural interpretation $`\ker C_0=\mathcal R_0`$.

The dimension of the degree-$`\ell`$ harmonic space is

```math
h_\ell
:=\dim\mathscr H_{\ell,\ell}
=\binom{d+\ell-1}{\ell}^{\!2}
-\binom{d+\ell-2}{\ell-1}^{\!2},
\tag{H14}
```

where the second term is zero for $`\ell=0`$. This follows directly from (H8) and
$`\dim\mathscr P_{\ell,\ell}=\binom{d+\ell-1}{\ell}^2`$.

## 3. Irreducibility and multiplicity one

Every summand in (H11) is invariant under $`U(d)`$: the operator $`s`$, the contraction $`\Delta`$, and the Fischer inner product are invariant. The following argument proves that each summand is irreducible and that distinct summands are inequivalent, without requiring a highest-weight classification.

Let

```math
K=U(1)\times U(d-1)\subset U(d)
```

be the stabilizer of the ray of $`e_1`$. The vector $`v_N(e_1)`$ is fixed by $`K`$. In the polynomial realization, the $`K`$-invariant polynomials of bidegree $`(N,N)`$ are exactly the linear combinations of

```math
(z_1w_1)^j
\left(\sum_{i=2}^d z_iw_i\right)^{N-j},
\qquad j=0,\ldots,N.
\tag{H15}
```

To justify this description, first use the independent phase actions on the first coordinate and the remaining coordinates: only equal holomorphic and antiholomorphic degrees can occur in each block. On the remaining coordinates, $`U(d-1)`$ acts transitively on each sphere, so a homogeneous invariant of bidegree $`(r,r)`$ is a constant times the $`r`$th power of their squared norm. This gives (H15), and the listed polynomials are linearly independent. Consequently,

```math
\dim\mathcal R_N^K=N+1.
\tag{H16}
```

Now refine (H11) into an orthogonal decomposition into irreducible $`U(d)`$ representations, which exists because the representation is finite dimensional and unitary. Each irreducible summand has a nonzero projection of $`v_N(e_1)`$: otherwise the entire orbit of that vector would miss the summand, contradicting (H5). That projection is a nonzero $`K`$-fixed vector. There are already $`N+1`$ nonzero summands in (H11); for example, $`z_1^\ell w_d^\ell`$ is a nonzero harmonic polynomial for every $`\ell`$. Equation (H16) leaves room for exactly $`N+1`$ irreducible summands. Hence each $`\mathcal V_{N,\ell}`$ is irreducible and its $`K`$-fixed space is one dimensional.

The summands are pairwise inequivalent. Suppose two were equivalent and let $`T`$ be a nonzero unitary intertwiner between them. Their projected vectors $`P_{N,\ell}v_N(e_1)`$ span their one-dimensional $`K`$-fixed lines, so $`T`$ maps one of these vectors to a nonzero multiple of the other. The same relation then holds for their projections of every orbit vector $`v_N(\psi)`$. The span of the orbit would satisfy this fixed linear relation between the two summands and would be a proper subspace of $`\mathcal R_N`$, again contradicting (H5).

Thus (H11) is a multiplicity-free decomposition into $`N+1`$ pairwise inequivalent irreducible representations.

Define the harmonic function spaces

```math
\mathcal H_\ell
=\{\psi\mapsto h(\psi,\overline\psi):h\in\mathscr H_{\ell,\ell}\},
\qquad
\mathcal L_N=\bigoplus_{\ell=0}^N\mathcal H_\ell.
\tag{H17}
```

Their degree is the balanced degree $`\ell`$; the corresponding real homogeneous polynomial degree is $`2\ell`$. By (H4), restriction maps $`\mathcal V_{N,\ell}`$ onto $`\mathcal H_\ell`$, since $`s=1`$ on the unit sphere. The map is equivariant and injective. The Haar $`L^2`$ inner product is invariant, so inequivalent irreducible spaces are orthogonal in $`L^2`$. Consequently, (H17) is an orthogonal direct sum and $`\mathcal L_N`$ is exactly the restriction of $`\mathscr P_{N,N}`$ to the sphere.

Write $`\Pi_\ell`$ and $`\Pi_{\leq N}`$ for the orthogonal projections in function space. These are distinct from the tensor projections $`P_{N,\ell}`$. Complex conjugation preserves each $`\mathcal H_\ell`$: on polynomials it conjugates the coefficients and exchanges $`z,w`$, which preserves bidegree $`(\ell,\ell)`$ and the equation $`\Delta h=0`$.

## 4. Reproducing kernels and the normalized Jacobi polynomial

Choose an $`L^2(\mu)`$-orthonormal basis $`Y_{\ell,1},\ldots,Y_{\ell,h_\ell}`$ of $`\mathcal H_\ell`$. Its projection kernel is

```math
K_\ell(\psi,\phi)
=\sum_{a=1}^{h_\ell}
Y_{\ell,a}(\psi)\overline{Y_{\ell,a}(\phi)},
\qquad
(\Pi_\ell f)(\psi)
=\int K_\ell(\psi,\phi)f(\phi)\,d\mu(\phi).
\tag{H18}
```

The kernel is independent of the chosen basis and invariant under a simultaneous unitary on both arguments. Since the arguments are rays, it depends only on

```math
t=|\langle\psi,\phi\rangle|^2.
```

Fixing $`\phi=e_1`$ and using the invariant-polynomial description in (H15), this dependence is a polynomial of degree at most $`\ell`$. Transitivity and the trace of the projection give

```math
K_\ell(\psi,\psi)=h_\ell.
\tag{H19}
```

For fixed $`\phi`$, the Haar distribution of $`t`$ is

```math
d\nu_d(t)=(d-1)(1-t)^{d-2}\,dt,
\qquad 0\leq t\leq1.
\tag{H20}
```

For example, write a uniform unit vector as $`g/\|g\|`$ for independent standard complex Gaussian coordinates. Then $`|g_1|^2`$ is exponential, the sum of the other $`d-1`$ squared magnitudes is an independent gamma variable of shape $`d-1`$, and their ratio gives (H20).

The polynomial $`K_\ell(t)`$ is orthogonal to every polynomial of degree below $`\ell`$: the latter are in $`\mathcal L_{\ell-1}`$. It is nonzero by (H19), so its degree is exactly $`\ell`$. Jacobi orthogonality therefore identifies it uniquely as

```math
K_\ell(\psi,\phi)=h_\ell Q_\ell(t),
\qquad
Q_\ell(t)
=\frac{P_\ell^{(d-2,0)}(2t-1)}{P_\ell^{(d-2,0)}(1)},
\qquad Q_\ell(1)=1.
\tag{H21}
```

This is the complex-projective addition theorem with probability-normalized Haar measure. The general bihomogeneous kernel is given in [De Bie, Sommen, and Wutzig, §2.2, Theorem 4][DSW]; Jacobi orthogonality and standardization are fixed by [NIST DLMF, Table 18.3.1][DLMF18.3].

The norm of the reproducing kernel gives its exact radial normalization:

```math
\int_0^1 Q_\ell(t)Q_m(t)\,d\nu_d(t)
=\frac{\delta_{\ell m}}{h_\ell}.
\tag{H22}
```

For the diagonal case, use
$`\int|K_\ell(\psi,\phi)|^2d\mu(\psi)=K_\ell(\phi,\phi)=h_\ell`$;
the off-diagonal case follows from orthogonality of harmonic spaces. The polynomials in (H21) have real coefficients, so no conjugate is missing in (H22).

The endpoint value and leading coefficient are

```math
P_\ell^{(d-2,0)}(1)=\binom{\ell+d-2}{\ell},
\qquad
L_\ell:=[t^\ell]Q_\ell(t)
=\frac{\binom{2\ell+d-2}{\ell}}{\binom{\ell+d-2}{\ell}}
=\frac{\Gamma(2\ell+d-1)\Gamma(d-1)}{\Gamma(\ell+d-1)^2}.
\tag{H23}
```

Both follow from the finite Jacobi expansion in [DLMF Eq. 18.5.7][DLMF18.5] and agree with the leading-coefficient convention in Table 18.3.1.

## 5. Orbit weights and Haar moments

The coherent input has kernel

```math
\langle v_N(\psi),v_N(\phi)\rangle
=|\langle\psi,\phi\rangle|^{2N}=t^N.
\tag{H24}
```

For each tensor irrep set

```math
p_{N,\ell}=\|P_{N,\ell}v_N(\psi)\|^2.
```

This number is independent of $`\psi`$ by transitivity and commutation of the projection with $`U(d)`$. The projected kernel belongs to $`\mathcal H_\ell`$ in its first argument and is invariant under the stabilizer of its second argument. Its one-dimensional invariant line and diagonal value therefore give

```math
\langle v_N(\psi),P_{N,\ell}v_N(\phi)\rangle
=p_{N,\ell}Q_\ell(t),
\qquad
t^N=\sum_{\ell=0}^N p_{N,\ell}Q_\ell(t).
\tag{H25}
```

All weights are positive, and their sum is one. Positivity follows because a nonzero invariant summand cannot be orthogonal to the cyclic orbit.

The full finite formula is

```math
p_{N,\ell}
=h_\ell\int_0^1t^NQ_\ell(t)\,d\nu_d(t)
=h_\ell\frac{\Gamma(d)(N!)^2}
{(N-\ell)!\,\Gamma(d+N+\ell)},
\qquad 0\leq\ell\leq N.
\tag{H26}
```

For completeness, the shifted Rodrigues identity is

```math
(1-t)^{d-2}P_\ell^{(d-2,0)}(2t-1)
=\frac{(-1)^\ell}{\ell!}
\frac{d^\ell}{dt^\ell}
\left[t^\ell(1-t)^{d+\ell-2}\right].
```

Insert it in the first integral in (H26), integrate by parts $`\ell`$ times, and use the beta integral. All boundary terms vanish: the polynomial in brackets has zeros of order at least $`\ell`$ at both endpoints. This yields the second expression in (H26). This Rodrigues convention is also specified by [DLMF §18.5(ii)][DLMF18.5].

The highest weight has an even shorter derivation. Comparing leading coefficients in (H25) gives $`p_{N,N}=1/L_N`$. Thus, with the notation used throughout the project,

```math
\boxed{
p_N:=p_{N,N}
=\frac{\Gamma(d+N-1)^2}
{\Gamma(d-1)\Gamma(d+2N-1)}
=\prod_{j=0}^{N-1}\frac{d-1+j}{d-1+N+j}.
}
\tag{H27}
```

The empty product gives $`p_0=1`$. Define $`\delta_N=1-p_N`$. Since
$`1-\prod_j(1-x_j)\leq\sum_jx_j`$ for $`0\leq x_j\leq1`$,

```math
0\leq\delta_N
\leq\sum_{j=0}^{N-1}\frac{N}{d-1+N+j}
\leq\frac{N^2}{d-1+N}.
\tag{H28}
```

In particular, $`N=o(\sqrt d)`$ implies $`\delta_N=o(1)`$. If $`N/\sqrt d\to c\in[0,\infty)`$, taking logarithms in (H27) gives

```math
p_N\longrightarrow e^{-c^2}.
\tag{H29}
```

The exact input Haar moment is

```math
\Omega_N
:=\int |v_N(\psi)\rangle\langle v_N(\psi)|\,d\mu(\psi)
=\sum_{\ell=0}^N\frac{p_{N,\ell}}{h_\ell}P_{N,\ell}.
\tag{H30}
```

Indeed, invariance and multiplicity one make the moment scalar on each irrep, and its trace on that irrep is $`p_{N,\ell}`$. In particular,

```math
\|J_Nu\|_2^2
=\frac{p_{N,\ell}}{h_\ell}\|u\|^2
\quad\text{for }u\in\mathcal V_{N,\ell}.
\tag{H31}
```

The scalar-function and tensor inner products are therefore not implicitly identified: their conversion factor is explicit.

## 6. Exact multiplication leakage

Let $`W=V\otimes\overline V`$ and

```math
\chi(\psi)=\psi\otimes\psi^*,
\qquad
(Mf)(\psi)=\chi(\psi)f(\psi).
\tag{H32}
```

Since $`\|\chi(\psi)\|=1`$, $`M:L^2(\mu)\to L^2(\mu;W)`$ is an isometry. Function-space projections act componentwise on vector-valued functions. Multiplication of a bidegree-$`(N,N)`$ polynomial by $`\psi_i\overline\psi_j`$ has bidegree $`(N+1,N+1)`$, so

```math
M\mathcal H_N\subset W\otimes\mathcal L_{N+1}.
```

**Multiplication lemma.** For every $`f\in\mathcal H_N`$,

```math
\boxed{
\|\Pi_{N+1}Mf\|_2^2=A_N\|f\|_2^2,
\qquad
\|\Pi_{\leq N}Mf\|_2^2=\lambda_N\|f\|_2^2,
}
\tag{H33}
```

where

```math
A_N=\frac{(N+d-1)^2}{(2N+d-1)(2N+d)},
\qquad
\lambda_N=1-A_N.
\tag{H34}
```

**Proof.** Put $`m_{ij}(\psi)=\psi_i\overline\psi_j`$, so $`Mf`$ has components $`m_{ij}f`$. The operator

```math
B_N
=(M|_{\mathcal H_N})^\dagger\Pi_{N+1}(M|_{\mathcal H_N})
=\left.\Pi_N\left(\sum_{i,j}M_{ij}^\dagger\Pi_{N+1}M_{ij}\right)\right|_{\mathcal H_N}
```

is positive and commutes with the $`U(d)`$ action. More explicitly, equip vector-valued functions with

```math
(\mathcal U_W(U)F)(\psi)
=(U\otimes\overline U)F(U^\dagger\psi).
```

Then $`M\mathcal U(U)=\mathcal U_W(U)M`$, and the componentwise harmonic projections commute with $`\mathcal U_W(U)`$. Irreducibility of $`\mathcal H_N`$ implies $`B_N=a_NI`$ for a scalar $`a_N`$: otherwise the eigenspaces of this positive operator would be proper invariant subspaces.

Compute this scalar by tracing in an orthonormal harmonic basis. With $`t=|\langle\psi,\phi\rangle|^2`$,

```math
\begin{aligned}
\mathrm{Tr}_{\mathcal H_N}B_N
&=\sum_{a,i,j}\|\Pi_{N+1}(m_{ij}Y_{N,a})\|_2^2\\
&=\iint
K_{N+1}(\psi,\phi)
K_N(\phi,\psi)
\sum_{i,j}\overline{m_{ij}(\psi)}m_{ij}(\phi)
\,d\mu(\psi)d\mu(\phi)\\
&=h_Nh_{N+1}\int_0^1
tQ_N(t)Q_{N+1}(t)\,d\nu_d(t).
\end{aligned}
\tag{H35}
```

The conjugations in the second line matter: the component sum is

```math
\sum_{i,j}\overline{\psi_i\overline\psi_j}\,
\phi_i\overline\phi_j
=|\langle\psi,\phi\rangle|^2=t.
```

Expand $`tQ_N(t)`$ in the orthogonal basis $`Q_0,\ldots,Q_{N+1}`$. Its coefficient at $`Q_{N+1}`$ is fixed solely by leading coefficients:

```math
[Q_{N+1}](tQ_N)
=\frac{L_N}{L_{N+1}}
=\frac{(N+d-1)^2}{(2N+d-1)(2N+d)}=A_N.
\tag{H36}
```

Using (H22), equation (H35) becomes $`\mathrm{Tr}B_N=h_NA_N`$. Hence $`a_N=A_N`$. Since $`M`$ is an isometry and its output has no degree above $`N+1`$, the retained fraction is $`1-A_N`$. This proves (H33).

The finite expression

```math
\lambda_N
=\frac{(2N+1)d+3N^2-1}{(d+2N-1)(d+2N)}
\leq
\frac{2N+1}{d-1}+\frac{3N^2}{d(d-1)}
\tag{H37}
```

shows that $`\lambda_N=o(1)`$ when $`N=o(\sqrt d)`$. Two normalization checks are $`A_0=(d-1)/d`$ and $`A_1=1/3`$ when $`d=2`$.

## 7. Vector-valued amplitudes and arbitrary linear processors

The multiplication lemma extends without change to any environment Hilbert space $`E`$:

```math
f\in\mathcal H_N\otimes E
\quad\Longrightarrow\quad
\|\Pi_{\leq N}(M\otimes I_E)f\|_2^2
=\lambda_N\|f\|_2^2.
\tag{H38}
```

Expand $`f`$ in an orthonormal basis of $`E`$ and apply (H33) to each component. For an infinite-dimensional $`E`$, the same conclusion follows by finite-rank approximation or monotone summation of the nonnegative squared norms. Finite-dimensional input and output maps already admit a finite-dimensional Stinespring environment.

A separate fact connects the function decomposition to a general processor. Let $`A:\mathcal R_N\to E`$ be any linear map, with no covariance assumption, and define

```math
a(\psi)=Av_N(\psi),
\qquad
a_\ell(\psi)=AP_{N,\ell}v_N(\psi).
\tag{H39}
```

Then $`a_\ell\in\mathcal H_\ell\otimes E`$. To check the conjugation convention, take $`e\in E`$:

```math
\langle e,a_\ell(\psi)\rangle
=\langle P_{N,\ell}A^\dagger e,v_N(\psi)\rangle
=\overline{J_N(P_{N,\ell}A^\dagger e)(\psi)}.
```

The last function is in $`\mathcal H_\ell`$ because that space is preserved by complex conjugation. Thus $`a=\sum_\ell a_\ell`$ is precisely its orthogonal $`L^2`$ harmonic decomposition.

If $`A^\dagger A\leq I`$, equation (H30) gives the quantitative bound

```math
\begin{aligned}
\|a_{<N}\|_2^2
&=\int\|A(I-P_N)v_N(\psi)\|^2\,d\mu(\psi)\\
&=\mathrm{Tr}\!\left[
A^\dagger A(I-P_N)\Omega_N(I-P_N)
\right]\\
&\leq\mathrm{Tr}[(I-P_N)\Omega_N]
=1-p_N=\delta_N.
\end{aligned}
\tag{H40}
```

This estimate applies to arbitrary environment-valued amplitudes of a processor. It uses contraction of $`A`$, not covariance of $`A`$. Together, (H38) and (H40) are the two harmonic estimates needed for the [constant-error converse](converse.md).

## References

- H. De Bie, F. Sommen, and M. Wutzig, *Plane wave formulas for spherical, complex and symplectic harmonics*, Journal of Approximation Theory **222**, 110–131 (2017), [arXiv:1702.00611v2][DSW]. Section 2.2, especially Lemma 3 and Theorem 4, records the complex Fischer decomposition and reproducing kernel. The normalization and the irreducibility argument used above are derived explicitly here.
- NIST Digital Library of Mathematical Functions, [§18.3, Table 18.3.1][DLMF18.3], for Jacobi orthogonality and leading coefficients; [§18.5(ii) and Eq. 18.5.7][DLMF18.5], for Rodrigues and finite-series conventions. The applications to input weights and multiplication leakage are derived in Sections 5 and 6 above.

[DSW]: https://arxiv.org/pdf/1702.00611v2
[DLMF18.3]: https://dlmf.nist.gov/18.3
[DLMF18.5]: https://dlmf.nist.gov/18.5
