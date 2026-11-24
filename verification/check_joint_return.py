"""Check exact and approximate joint return in finite occupation bases."""

from math import sqrt

import numpy as np

from check_pure_filter import coherent, occupations


def annihilators(d, occupation_basis, residual_basis):
    """Construct one annihilation matrix for each coordinate."""
    residual_index = {
        occupation: row for row, occupation in enumerate(residual_basis)
    }
    matrices = np.zeros((d, len(residual_basis), len(occupation_basis)))
    for column, occupation in enumerate(occupation_basis):
        for i, count in enumerate(occupation):
            if count:
                residual = list(occupation)
                residual[i] -= 1
                matrices[i, residual_index[tuple(residual)], column] = sqrt(count)
    return matrices


def check(d, n, m, rng):
    ordinary, conjugate = occupations(n, d), occupations(m, d)
    ordinary_return, conjugate_return = occupations(n - 1, d), occupations(m - 1, d)
    left = annihilators(d, ordinary, ordinary_return)
    right = annihilators(d, conjugate, conjugate_return)
    extraction = [np.kron(a, b) for a in left for b in right]
    contraction = sum(extraction[i * d + i] for i in range(d))
    target_map = np.vstack([contraction, *extraction]) / sqrt(2 * n * m)

    gram = target_map.T @ target_map
    identity = np.eye(gram.shape[0])
    np.testing.assert_allclose(
        gram, (identity + contraction.T @ contraction / (n * m)) / 2,
        atol=1e-12,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    largest_supply = max(n, m)
    exact_success = 2 * largest_supply / (d + 2 * largest_supply - 1)
    np.testing.assert_allclose(eigenvalues[-1] * exact_success, 1, atol=1e-12)
    assert eigenvalues[0] >= 0.5 - 1e-12

    inverse_sqrt = (eigenvectors / np.sqrt(eigenvalues)) @ eigenvectors.T
    polar = target_map @ inverse_sqrt
    np.testing.assert_allclose(polar.T @ polar, identity, atol=1e-12)

    psi = rng.normal(size=d) + 1j * rng.normal(size=d)
    psi /= np.linalg.norm(psi)
    sample = np.kron(coherent(psi, ordinary), coherent(psi.conj(), conjugate))
    residual = np.kron(
        coherent(psi, ordinary_return), coherent(psi.conj(), conjugate_return)
    )
    purification = np.r_[1, np.kron(psi, psi.conj())] / sqrt(2)
    expected = np.kron(purification, residual)

    accepted = sqrt(exact_success) * (target_map @ sample)
    np.testing.assert_allclose(accepted, sqrt(exact_success) * expected, atol=1e-12)
    np.testing.assert_allclose(np.linalg.norm(accepted) ** 2, exact_success)

    weights = np.abs(eigenvectors.T @ sample) ** 2
    variance = (d - 1) / (4 * n * m)
    np.testing.assert_allclose(weights @ eigenvalues, 1)
    np.testing.assert_allclose(weights @ eigenvalues**2, 1 + variance)
    fidelity = abs(np.vdot(expected, polar @ sample)) ** 2
    np.testing.assert_allclose(fidelity, (weights @ np.sqrt(eigenvalues)) ** 2)
    assert fidelity >= 1 / (1 + variance) - 1e-12
    print(f"d={d} n={n} m={m}: exact success={exact_success:.9f}, polar fidelity={fidelity:.9f}")


def main():
    rng = np.random.default_rng(78013)
    for d, n, m in [(2, 1, 1), (2, 1, 3), (2, 2, 2), (2, 2, 3),
                    (3, 1, 2), (3, 2, 1), (3, 2, 3)]:
        check(d, n, m, rng)
    print("All seven exact and approximate joint-return cases passed.")


if __name__ == "__main__":
    main()
