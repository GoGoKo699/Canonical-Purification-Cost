# Reproducing the finite checks

`verify_construction.py` constructs the successful Kraus operator directly
in normalized occupation-number bases. It checks its normalization, exact action
on complex coherent inputs, and success probability. A separate calculation
checks the matched-purification comparison, including its gauge and spectrum
restrictions.

These are finite numerical checks of the formulas. The analytic proofs establish
the dimension-dependent statements; this program does not implement a scalable
quantum circuit or prove the asymptotic converse.

## Run

From the repository root, with Python 3.12:

```sh
python3 -m pip install -r requirements.txt
OPENBLAS_NUM_THREADS=1 python3 verification/verify_construction.py
```

The default command writes `verification/results/construction.json` and returns
exit code zero only if every reported error is at most `1e-10`. It prints a compact
summary. The JSON contains the random seed, package versions, script SHA-256,
individual errors, and predicted spectral multiplicities. Small numerical
differences across BLAS implementations are expected.

To select individual cases and preserve the stored default result:

```sh
OPENBLAS_NUM_THREADS=1 python3 verification/verify_construction.py \
  --case 2,3 --case 4,2 --seed 2317 --output /tmp/canonical-check.json
```

Repeated `--case d,N` arguments replace the default occupation-basis cases. The
four purifier cases still run. This dense audit rejects input dimension greater
than 2500 to avoid accidental large allocations.

## Exact allocation and mixed-source checks

The [pure exact frontier](../science/exact_frontier.md) is an analytical LP characterization. The evaluator uses exact rational harmonic weights and recurrence coefficients, then calls SciPy's floating-point LP solver. Its numerical optimum is not a symbolic solution of every LP.

From the repository root, run:

    OPENBLAS_NUM_THREADS=1 python3 verification/verify_all_allocation.py --self-test --output verification/results/exact_frontier.json
    OPENBLAS_NUM_THREADS=1 python3 verification/check_pure_filter.py > verification/results/pure_filter.json

The first command checks 112 allocations with $`d=2,3,5,20`$ and budgets through six, 60 exact rational Jacobi recurrence identities, zero-budget boundaries, exchange symmetry and the sharp n-by-one formula. Seven explicit occupation-space success effects verify physical contractivity for the LP's residual operator. An exact rational primal/dual certificate proves the $`d=2,n=m=2`$ optimum $`12/13`$ independently of floating-point LP output.

The mixed checks compare 15 finite one-conjugate hard-cap values against the exact rational binomial sum, check four boundary/exchange cases, and use independently certified pure sector values to obtain

```math
Q_2^*(2,2)=\frac{331}{780}.
```

The exact value follows from occupancy weights multiplying $`q_2^*(1,1)=2/3`$, $`q_2^*(2,1)=q_2^*(1,2)=4/5`$ and $`q_2^*(2,2)=12/13`$. These tests check finite accounting, not a broader product conjecture.

The second command independently builds the full n-by-one success operation at $`d=2,3,4`$ and $`n=1,2,3`$, tests the contraction identity and target factorization on seeded complex inputs, and checks the nontrivial $`d=2,n=m=2`$ residual operator. In that example the success effect has eigenvalues $`7/13`$ five times and $`1`$ four times; its exact target success is $`12/13`$. Reports are stored in [exact_frontier.json](results/exact_frontier.json) and [pure_filter.json](results/pure_filter.json).

Individual allocations can be evaluated without the full suite:

    python3 verification/verify_all_allocation.py --d 3 --n 3 --m 2
    python3 verification/verify_all_allocation.py --mixed --d 2 --n 2 --m 2
    python3 verification/verify_all_allocation.py --mixed --d 10 --n 20 --m 1

The mixed option interprets n and m as separate mixed-source request caps. Its floating-point binomial transform uses the pure LP for every observed signal count; at one conjugate mixed specimen it additionally reports the exact rational formula. It includes zero-signal sectors, every vacuum outcome and failed filters. It does not simulate a stricter simultaneous total cap or replace hard caps by expected waiting costs.

The analytic rigidity, kernel-positivity and occupancy proofs establish the all-dimensional arbitrary-processor theorem. These finite calculations test normalization, coefficients, physical realization and counting. They do not certify gate-efficient implementation, literature priority, a closed elementary optimum, the broad $`nm`$-of-order-$`d`$ conjecture or an approximate-fidelity product law.

## Construction checks

For

```math
\mathcal R_N=\mathrm{Sym}^N(\mathbb C^d)
\otimes\mathrm{Sym}^N(\overline{\mathbb C^d}),
```

the program builds annihilation matrices with entries $`\sqrt{m_i}`$ and forms
$`C_N=\sum_i a_i\otimes a_i`$. It computes the residual projector as

```math
P_{N-1}=I-C_{N-1}^{\dagger}
(C_{N-1}C_{N-1}^{\dagger})^{-1}C_{N-1},
```

with $`P_0=I`$. This kernel calculation does not use the formula for the highest
harmonic weight. The extraction blocks are $`E_{ij}=a_i\otimes a_j/N`$.

The resulting matrix has one output block for $`|\mathrm{vac},\mathrm{vac}\rangle`$
and $`d^2`$ blocks for signal pairs. The checks are:

- The full spectrum of $`K^{\dagger}K`$ lies in $`[0,1]`$, up to the stated tolerance.
- $`K v_N=\alpha |T_\psi\rangle\otimes P_{N-1}v_{N-1}`$ for a seeded complex unit
  vector $`\psi`$, where
  $`\alpha^2=2N^2/(N^2+d+2N-2)`$.
- The observed success equals $`\alpha^2 p_{N-1}`$, and the directly projected
  weight equals
  $`p_N=\prod_{j=0}^{N-1}(d-1+j)/(d-1+N+j)`$.
- The extraction is an isometry and the computed residual projector is
  idempotent.
- The contraction commutator is
  $`C_NC_N^{\dagger}-C_{N-1}^{\dagger}C_{N-1}=(d+2N-2)I`$.
- The full spectrum of $`C_N^{\dagger}C_N`$ agrees with
  $`(N-\ell)(d+N+\ell-1)`$ with multiplicity
  $`\binom{d+\ell-1}{\ell}^2-\binom{d+\ell-2}{\ell-1}^2`$.
- The nonzero spectrum of $`C_N^{\dagger}P_{N-1}C_N`$ is the single value
  $`d+2N-2`$, with multiplicity equal to the residual traceless dimension.

In the multiplicity formula, a binomial coefficient with lower index $`-1`$ is zero.

The default 14 cases are $`d=2`$, $`N=1,\ldots,5`$; $`d=3`$, $`N=1,\ldots,4`$;
$`d=4`$, $`N=1,2,3`$; and $`(d,N)=(5,2),(6,2)`$. They include $`\alpha^2>1`$, where
normalization must come from the full operator bound and cannot be inferred from
the scalar prefactor alone.

## Matched-purifier checks

Four cases use environment dimension $`k=2`$ or $`4`$ and nonzero eigenvalues
$`(1/2,1/2)`$ or $`(0.8,0.2)`$. Each uses a seeded complex signal state and a complex
random environment isometry. The contraction is formed from the two full
purification state vectors and a normalized Bell bra.

The code verifies the exact output $`\mathrm{vec}(\rho)/\sqrt{k}`$,
success $`\mathrm{Tr}(\rho^2)/k`$, and canonical-output squared fidelity

```math
\frac{\bigl(\sum_i\lambda_i^{3/2}\bigr)^2}{\sum_i\lambda_i^2}.
```

For the flat rank-two spectrum the probability is $`1/4`$ at $`k=2`$ and $`1/8`$ at
$`k=4`$, and the canonical fidelity is one. For $`(0.8,0.2)`$ the fidelity is
$`81/85\simeq0.952941`$, demonstrating the flat-spectrum restriction.

Two controls isolate the gauge requirement. An independent random gauge is
recorded as an example, without drawing a statistical conclusion from one draw.
A deterministic swap of the two environment Schmidt vectors gives zero overlap
with the canonical target while preserving both system marginals. Finally, the
independent Haar average is calculated exactly: the conditioned systems remain
$`\rho\otimes\rho^*`$, with target fidelity $`1/4`$ for the flat rank-two case.

These controls diagnose the direct Bell protocol. The arbitrary-processor lower
bound is a separate analytic result, not an inference from these examples.
