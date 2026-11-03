#!/usr/bin/env python3
"""Finite matrix checks for the canonical-purification construction.

The matrices are built in normalized bosonic occupation bases. Projectors are
computed from kernels, independently of the closed-form harmonic weights. This
program checks finite examples; the analytic arguments establish the theorem.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
import hashlib
import json
import math
from pathlib import Path
import platform
import sys

import numpy as np
import scipy
from scipy.linalg import eigvalsh


DEFAULT_CASES = (
    [(2, n) for n in range(1, 6)]
    + [(3, n) for n in range(1, 5)]
    + [(4, n) for n in range(1, 4)]
    + [(5, 2), (6, 2)]
)


@lru_cache(maxsize=None)
def occupations(d: int, n: int) -> tuple[tuple[int, ...], ...]:
    """Occupation tuples in a fixed order; every basis vector has norm one."""
    if d == 1:
        return ((n,),)
    return tuple(
        (j,) + tail for j in range(n + 1) for tail in occupations(d - 1, n - j)
    )


def symmetric_dimension(d: int, n: int) -> int:
    return math.comb(d + n - 1, n) if n >= 0 else 0


def harmonic_dimension(d: int, n: int) -> int:
    return symmetric_dimension(d, n) ** 2 - symmetric_dimension(d, n - 1) ** 2


def annihilators(d: int, n: int) -> list[np.ndarray]:
    """a_i: Sym^n(C^d) -> Sym^(n-1)(C^d), with sqrt(m_i) entries."""
    if n < 1:
        raise ValueError("An annihilation matrix requires n >= 1.")
    source, target = occupations(d, n), occupations(d, n - 1)
    lookup = {occupation: i for i, occupation in enumerate(target)}
    matrices = []
    for i in range(d):
        matrix = np.zeros((len(target), len(source)))
        for j, occupation in enumerate(source):
            if occupation[i]:
                reduced = list(occupation)
                reduced[i] -= 1
                matrix[lookup[tuple(reduced)], j] = math.sqrt(occupation[i])
        matrices.append(matrix)
    return matrices


def contraction(d: int, n: int) -> np.ndarray:
    return sum(np.kron(a, a) for a in annihilators(d, n))


def traceless_projector(d: int, n: int) -> np.ndarray:
    """Orthogonal projector onto ker(C_n), obtained without harmonic formulas."""
    if n == 0:
        return np.eye(1)
    c = contraction(d, n)
    # C_n is onto. Its row Gram matrix is positive definite.
    projector = np.eye(c.shape[1]) - c.T @ np.linalg.solve(c @ c.T, c)
    return (projector + projector.T) / 2


def coherent_vector(psi: np.ndarray, n: int) -> np.ndarray:
    coefficients = []
    for occupation in occupations(len(psi), n):
        multiplicity = math.factorial(n) / math.prod(
            math.factorial(j) for j in occupation
        )
        coefficients.append(
            math.sqrt(multiplicity) * np.prod(psi ** np.asarray(occupation))
        )
    return np.asarray(coefficients, dtype=complex)


def highest_harmonic_weight(d: int, n: int) -> float:
    return math.prod((d - 1 + j) / (d - 1 + n + j) for j in range(n))


def operator_norm(matrix: np.ndarray) -> float:
    return float(np.linalg.norm(matrix, ord=2))


def construction_case(d: int, n: int, seed: int, tolerance: float) -> dict:
    a = annihilators(d, n)
    c = contraction(d, n)
    residual_projector = traceless_projector(d, n - 1)
    extraction_blocks = [np.kron(x, y) / n for x in a for y in a]
    alpha_squared = 2 * n * n / (n * n + d + 2 * n - 2)
    scale = math.sqrt(alpha_squared / 2)
    # Output order: vacuum-vacuum, then (i,j) signal pairs; residual last.
    k = np.vstack(
        [scale * residual_projector @ c / n]
        + [scale * residual_projector @ block for block in extraction_blocks]
    )
    gram = k.T @ k
    gram_spectrum = eigvalsh(gram)
    dimension = gram.shape[0]

    rng = np.random.default_rng(seed + 100 * d + n)
    psi = rng.normal(size=d) + 1j * rng.normal(size=d)
    psi /= np.linalg.norm(psi)
    v = np.kron(coherent_vector(psi, n), coherent_vector(psi.conj(), n))
    residual = np.kron(
        coherent_vector(psi, n - 1), coherent_vector(psi.conj(), n - 1)
    )
    target = np.concatenate(([1], np.kron(psi, psi.conj()))) / math.sqrt(2)
    output = k @ v
    factored = math.sqrt(alpha_squared) * np.kron(
        target, residual_projector @ residual
    )
    success = float(np.vdot(output, output).real)
    success_formula = alpha_squared * highest_harmonic_weight(d, n - 1)
    top_component = traceless_projector(d, n) @ v
    top_weight = float(np.vdot(top_component, top_component).real)

    # C_n^dagger C_n on H_l has eigenvalue (n-l)(d+n+l-1).
    contraction_spectrum = eigvalsh(c.T @ c)
    predicted_groups = [
        {
            "harmonic_degree": ell,
            "eigenvalue": (n - ell) * (d + n + ell - 1),
            "multiplicity": harmonic_dimension(d, ell),
        }
        for ell in range(n, -1, -1)
    ]
    predicted_spectrum = np.concatenate(
        [np.full(group["multiplicity"], group["eigenvalue"]) for group in predicted_groups]
    )
    beta = d + 2 * n - 2
    projected_spectrum = eigvalsh(c.T @ residual_projector @ c)
    projected_rank = harmonic_dimension(d, n - 1)
    projected_prediction = np.concatenate(
        [np.zeros(dimension - projected_rank), np.full(projected_rank, beta)]
    )
    lower_contraction_gram = (
        np.zeros((1, 1))
        if n == 1
        else contraction(d, n - 1).T @ contraction(d, n - 1)
    )
    extraction_gram = sum(block.T @ block for block in extraction_blocks)
    errors = {
        "cp_upper_violation": max(0.0, float(gram_spectrum[-1]) - 1),
        "cp_lower_violation": max(0.0, -float(gram_spectrum[0])),
        "exact_factorization": float(np.linalg.norm(output - factored)),
        "success_probability": abs(success - success_formula),
        "highest_harmonic_weight": abs(top_weight - highest_harmonic_weight(d, n)),
        "extraction_isometry": operator_norm(extraction_gram - np.eye(dimension)),
        "residual_projector_idempotence": operator_norm(
            residual_projector @ residual_projector - residual_projector
        ),
        "contraction_spectrum": float(
            np.max(np.abs(contraction_spectrum - predicted_spectrum))
        ),
        "projected_contraction_spectrum": float(
            np.max(np.abs(projected_spectrum - projected_prediction))
        ),
        "contraction_commutator": operator_norm(
            c @ c.T - lower_contraction_gram - beta * np.eye(c.shape[0])
        ),
    }
    return {
        "d": d,
        "N": n,
        "input_dimension": dimension,
        "alpha_squared": alpha_squared,
        "KdaggerK_min_eigenvalue": float(gram_spectrum[0]),
        "KdaggerK_max_eigenvalue": float(gram_spectrum[-1]),
        "success_observed": success,
        "success_formula": success_formula,
        "highest_harmonic_weight_observed": top_weight,
        "highest_harmonic_weight_formula": highest_harmonic_weight(d, n),
        "contraction_spectrum_prediction": predicted_groups,
        "projected_contraction_nonzero_eigenvalue": beta,
        "projected_contraction_rank": projected_rank,
        "errors": errors,
        "passed": all(error <= tolerance for error in errors.values()),
    }


def random_isometry(rng: np.random.Generator, rows: int, columns: int) -> np.ndarray:
    matrix = rng.normal(size=(rows, columns)) + 1j * rng.normal(size=(rows, columns))
    q, r = np.linalg.qr(matrix)
    diagonal = np.diag(r)
    return q * (diagonal / np.abs(diagonal))


def bell_contract(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    """Contract two purification coefficient matrices with a normalized Bell bra."""
    if first.shape != second.shape:
        raise ValueError("The two system and environment dimensions must agree.")
    system_dimension, environment_dimension = first.shape
    pair = np.kron(first.ravel(), second.ravel()).reshape(
        system_dimension, environment_dimension, system_dimension, environment_dimension
    )
    bell = np.eye(environment_dimension) / math.sqrt(environment_dimension)
    return np.einsum("iajb,ab->ij", pair, bell)


def squared_fidelity_with_vector(matrix: np.ndarray, target: np.ndarray) -> float:
    return float(abs(np.vdot(target, matrix)) ** 2 / np.vdot(matrix, matrix).real)


def purifier_case(environment_dimension: int, eigenvalues: tuple[float, float],
                  seed: int, tolerance: float) -> dict:
    """A complex random gauge, a mismatched gauge, and the independent Haar mean."""
    k = environment_dimension
    eigenvalues_array = np.asarray(eigenvalues)
    system_dimension = 6
    rng = np.random.default_rng(seed + 1000 * k + round(100 * eigenvalues[0]))
    psi = rng.normal(size=system_dimension - 1) + 1j * rng.normal(size=system_dimension - 1)
    psi /= np.linalg.norm(psi)
    basis = np.zeros((system_dimension, 2), dtype=complex)
    basis[0, 0], basis[1:, 1] = 1, psi
    gauge = random_isometry(rng, k, 2)
    independent_gauge = random_isometry(rng, k, 2)
    root_eigenvalues = np.sqrt(eigenvalues_array)
    first = (basis * root_eigenvalues) @ gauge.T
    rho = (basis * eigenvalues_array) @ basis.conj().T
    canonical = (basis * root_eigenvalues) @ basis.conj().T
    purity = float(np.sum(eigenvalues_array ** 2))

    output = bell_contract(first, first.conj())
    success = float(np.vdot(output, output).real)
    canonical_fidelity = squared_fidelity_with_vector(output, canonical)
    fidelity_formula = float(np.sum(eigenvalues_array ** 1.5) ** 2 / purity)

    # Both controls purify rho*, but only first.conj() has the matched gauge.
    independent = (basis.conj() * root_eigenvalues) @ independent_gauge.T
    independent_output = bell_contract(first, independent)
    swapped = (basis.conj() * root_eigenvalues) @ gauge[:, ::-1].conj().T
    swapped_output = bell_contract(first, swapped)
    swapped_fidelity = squared_fidelity_with_vector(swapped_output, canonical)
    swapped_success = float(np.vdot(swapped_output, swapped_output).real)

    # Independent Haar averages are rho x I/k and rho* x I/k at one copy.
    uniform_environment = np.eye(k) / k
    bell = np.eye(k) / math.sqrt(k)
    averaged_output = np.einsum(
        "ij,ab,kl,cd,ac,bd->ikjl",
        rho, uniform_environment, rho.conj(), uniform_environment, bell, bell,
        optimize=True,
    ).reshape(system_dimension ** 2, system_dimension ** 2)
    averaged_success = float(np.trace(averaged_output).real)
    averaged_conditioned = averaged_output / averaged_success
    averaged_fidelity = float(
        np.vdot(canonical.ravel(), averaged_conditioned @ canonical.ravel()).real
    )
    errors = {
        "purification_marginal": operator_norm(first @ first.conj().T - rho),
        "matched_bell_vector": float(np.linalg.norm(output - rho / math.sqrt(k))),
        "matched_success_purity_over_k": abs(success - purity / k),
        "canonical_fidelity_formula": abs(canonical_fidelity - fidelity_formula),
        "independent_gauge_marginal": operator_norm(
            independent @ independent.conj().T - rho.conj()
        ),
        "swapped_gauge_marginal": operator_norm(swapped @ swapped.conj().T - rho.conj()),
        "swapped_gauge_orthogonality": abs(swapped_fidelity),
        "swapped_gauge_success": abs(swapped_success - 2 * math.prod(eigenvalues) / k),
        "independent_haar_success": abs(averaged_success - 1 / k ** 2),
        "independent_haar_conditioned_state": operator_norm(
            averaged_conditioned - np.kron(rho, rho.conj())
        ),
        "independent_haar_canonical_fidelity": abs(
            averaged_fidelity - float(np.sum(eigenvalues_array ** 3))
        ),
    }
    return {
        "system_dimension": system_dimension,
        "environment_dimension": k,
        "nonzero_eigenvalues": list(eigenvalues),
        "flat_spectrum": eigenvalues[0] == eigenvalues[1],
        "purity": purity,
        "matched_success_observed": success,
        "matched_success_formula": purity / k,
        "matched_canonical_fidelity": canonical_fidelity,
        "matched_canonical_fidelity_formula": fidelity_formula,
        "independent_random_gauge_success": float(np.vdot(independent_output, independent_output).real),
        "independent_random_gauge_canonical_fidelity": squared_fidelity_with_vector(
            independent_output, canonical
        ),
        "swapped_gauge_canonical_fidelity": swapped_fidelity,
        "independent_haar_average_success": averaged_success,
        "independent_haar_average_canonical_fidelity": averaged_fidelity,
        "errors": errors,
        "passed": all(error <= tolerance for error in errors.values()),
    }


def parse_case(value: str) -> tuple[int, int]:
    try:
        d, n = map(int, value.split(","))
    except ValueError as error:
        raise argparse.ArgumentTypeError("Use --case d,N with integer d >= 2 and N >= 1.") from error
    if d < 2 or n < 1:
        raise argparse.ArgumentTypeError("Each case needs d >= 2 and N >= 1.")
    return d, n


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", action="append", type=parse_case,
                        help="Replace defaults with this d,N case; may be repeated.")
    parser.add_argument("--seed", type=int, default=2317)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().parent / "results" / "construction.json")
    args = parser.parse_args()
    if args.seed < 0 or not math.isfinite(args.tolerance) or args.tolerance <= 0:
        parser.error("Use a nonnegative seed and a finite positive tolerance.")
    cases = args.case or DEFAULT_CASES
    for d, n in cases:
        if symmetric_dimension(d, n) ** 2 > 2500:
            parser.error("This dense audit is limited to input dimension <= 2500.")

    construction_results = [construction_case(d, n, args.seed, args.tolerance) for d, n in cases]
    purifier_results = [
        purifier_case(k, spectrum, args.seed, args.tolerance)
        for k in (2, 4) for spectrum in ((0.5, 0.5), (0.8, 0.2))
    ]
    all_results = construction_results + purifier_results
    passed = all(result["passed"] for result in all_results)
    summary = {
        "passed": passed,
        "construction_cases": len(construction_results),
        "purifier_cases": len(purifier_results),
        "maximum_absolute_error": max(max(result["errors"].values()) for result in all_results),
        "maximum_KdaggerK_eigenvalue": max(result["KdaggerK_max_eigenvalue"] for result in construction_results),
        "maximum_factorization_error": max(result["errors"]["exact_factorization"] for result in construction_results),
        "maximum_success_probability_error": max(result["errors"]["success_probability"] for result in construction_results),
    }
    payload = {
        "description": __doc__,
        "provenance": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
            "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "seed": args.seed,
            "absolute_tolerance": args.tolerance,
        },
        "summary": summary,
        "construction_cases": construction_results,
        "matched_purifier_cases": purifier_results,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    print(json.dumps({**summary, "results_file": str(args.output)}, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
