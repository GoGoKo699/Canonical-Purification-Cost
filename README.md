# Canonical purification from conjugate samples

How many physical samples are needed to assemble a specified purification of an unknown mixed state? This project gives matching bounds for a rank-two family whose spectrum is already known. The source supplies both the mixed state and its complex conjugate, so the remaining task is to create the required coherent correlation.

Let $|\mathrm{vac}\rangle$ be a known reference state and let $|\psi\rangle$ be an unknown unit vector in an orthogonal $d$-dimensional signal space. Define

$$
\rho_\psi=\frac{|\mathrm{vac}\rangle\langle\mathrm{vac}|+|\psi\rangle\langle\psi|}{2},
\qquad
|T_\psi\rangle=\frac{|\mathrm{vac},\mathrm{vac}\rangle+|\psi\rangle|\psi^*\rangle}{\sqrt2}.
$$

The target is the canonical purification of $\rho_\psi$ in a fixed supplied basis.

## Principal result

Independent copies of $\rho_\psi$ and $\rho_\psi^*$ require and suffice with **$\Theta(\sqrt d)$ total copies** to prepare the target at fixed nontrivial fidelity and success probability. The lower bound allows arbitrary collective operations, quantum memory, adaptive instruments and approximate outputs. The construction produces the exact target on its successful branch.

| Supplied resource | Supported preparation guarantee |
|---|---|
| Independent mixed samples and their conjugates | Optimal total copy cost $\Theta(\sqrt d)$ at fixed error and success |
| A purification with a two-dimensional environment, together with its exactly matched conjugate | Two source preparations give the exact target with probability $1/4$ |

The first statement uses a hard total-copy budget. More precisely, it holds for every fixed conditional squared fidelity $F_0\in(1/2,1]$ and success probability $p_{\min}\in(0,1)$, or for deterministic preparation with fixed squared fidelity $F_0\in(1/2,1)$. It does not require a separate lower bound on each sample stream. Every source preparation, including those in rejected attempts, is charged.

The comparison shows what is lost when the purifying registers are discarded. Both sample streams already contain the unknown direction and its conjugate. Retaining a matched pair of small purifying registers additionally permits coherent assembly of the two target branches. The cost of recovering that capability from independent marginals grows with the ambient dimension even though the source rank is only two.

## Read the science

Start with the [model and theorem](science/model.md). The [science guide](science/README.md) connects the proof and its interpretation.

| Question | Authoritative account |
|---|---|
| What is supplied, produced and counted? | [Operational model](science/model.md) |
| How does the protocol reach the square-root scale? | [Exact construction and finite copy budget](science/construction.md) |
| Which symmetry identities control the bound? | [Projective harmonics](science/harmonic_analysis.md) |
| Why can arbitrary approximate processors do no better? | [Converse](science/converse.md) |
| What does a matched purification pair provide? | [Access comparison](science/access_comparison.md) |
| How does this relate to existing purification and program results? | [Related work](references/RELATED_WORK.md) |

## Learn the result

The educational anchor is John Watrous's *The Theory of Quantum Information* (2018). The [learning guide](learning/README.md) connects the relevant foundations to this project's mechanism and proof. Its [source bridge](learning/anchor.md) gives focused section pointers, translates notation and fidelity conventions, and explains the additional mathematics developed here. The [30-milestone map](learning/milestones.md) follows the project from its basic objects to the complete resource comparison.

## Reproduce the finite checks

The [verification guide](verification/README.md) specifies the environment, command and expected output. The code independently constructs normalized occupation-basis matrices for the complete successful operation. It checks physical normalization, accepted-state factorization, success probabilities and the matched-purification comparison. These finite checks test implementation and normalization; the dimension-uniform theorem follows from the analytical proofs.

## Scope

The known reference direction, flat rank-two spectrum and fixed conjugation basis are part of the model. The constant-cost comparison supplies an exactly conjugate-correlated pair with a known constant environmental dimension. Arbitrary purifications with unrelated gauges do not provide that resource. The result concerns producing a quantum state; no decision-query separation is claimed.

The upper bound is information theoretic. Efficient gate synthesis of the collective traceless-sector filter, general-rank preparation, vanishing-error optimality and a sharp unbalanced-copy law are outside the established result. [Related work](references/RELATED_WORK.md) credits the existing random-purification, superposition and mixed-tensor methods that inform the proof.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
