"""Finite-matrix sanity checks for exact n-by-one filter; not an asymptotic proof."""
import itertools
import json
import math
import numpy as np


def occupations(total, d):
    if d == 1:
        return [(total,)]
    return [(i,) + tail for i in range(total + 1)
            for tail in occupations(total - i, d - 1)]


def coherent(z, occ):
    n = sum(occ[0])
    return np.array([math.sqrt(math.factorial(n) / math.prod(math.factorial(k) for k in a))
                     * np.prod([z[i] ** a[i] for i in range(len(z))]) for a in occ])


def case(d, n, seed=849120):
    rng = np.random.default_rng(seed + d * 100 + n)
    ins, res = occupations(n, d), occupations(n - 1, d)
    ri = {a: j for j, a in enumerate(res)}
    dimr, dimi = len(res), len(ins) * d
    C = np.zeros((dimr, dimi), complex)
    E = np.zeros((d * d * dimr, dimi), complex)
    for ai, a in enumerate(ins):
        for j in range(d):
            col = ai * d + j
            for i in range(d):
                if a[i]:
                    b = list(a)
                    b[i] -= 1
                    row = ri[tuple(b)]
                    E[(i * d + j) * dimr + row, col] = math.sqrt(a[i] / n)
                    if i == j:
                        C[row, col] = math.sqrt(a[i])
    W = np.vstack((C / math.sqrt(n), E)) / math.sqrt(2)
    q = 2 * n / (d + 2 * n - 1)
    K = math.sqrt(q) * W
    z = rng.normal(size=d) + 1j * rng.normal(size=d)
    z /= np.linalg.norm(z)
    v = np.kron(coherent(z, ins), z.conj())
    t = np.concatenate(([1], np.kron(z, z.conj()))) / math.sqrt(2)
    wanted = math.sqrt(q) * np.kron(t, coherent(z, res))
    errs = {
        "CCdagger": np.linalg.norm(C @ C.conj().T - (d + n - 1) * np.eye(dimr)),
        "E_isometry": np.linalg.norm(E.conj().T @ E - np.eye(dimi)),
        "exact_output": np.linalg.norm(K @ v - wanted),
        "success": abs(np.linalg.norm(K @ v) ** 2 - q),
        "norm": abs(np.linalg.norm(W, 2) ** 2 - (d + 2 * n - 1) / (2 * n)),
        "contractivity_excess": max(0, np.linalg.eigvalsh(K.conj().T @ K).max() - 1),
    }
    assert max(errs.values()) < 1e-11, (d, n, errs)
    return {"d": d, "n": n, "q": q, "max_residual": max(errs.values()), "errors": errs}


def two_by_two(seed=148127):
    """A nontrivial residual-X LP optimum independently checked as an operator."""
    d, n, m = 2, 2, 2
    rng = np.random.default_rng(seed)
    insa, insb = occupations(n, d), occupations(m, d)
    resa, resb = occupations(n - 1, d), occupations(m - 1, d)
    rai = {a: j for j, a in enumerate(resa)}
    rbi = {b: j for j, b in enumerate(resb)}
    dimr, dimi = len(resa) * len(resb), len(insa) * len(insb)
    C = np.zeros((dimr, dimi), complex)
    E = np.zeros((d * d * dimr, dimi), complex)
    for ai, a in enumerate(insa):
        for bi, b in enumerate(insb):
            col = ai * len(insb) + bi
            for j in range(d):
                for k in range(d):
                    if a[j] and b[k]:
                        ar, br = list(a), list(b)
                        ar[j] -= 1
                        br[k] -= 1
                        row = rai[tuple(ar)] * len(resb) + rbi[tuple(br)]
                        x = math.sqrt(a[j] * b[k])
                        E[(j * d + k) * dimr + row, col] = x / math.sqrt(n * m)
                        if j == k:
                            C[row, col] = x
    W = np.vstack((C / math.sqrt(n * m), E)) / math.sqrt(2)
    # Occupation enumeration is ascending, so Ω is still (1,0,0,1).
    omega = np.array([1, 0, 0, 1], complex) / math.sqrt(2)
    P0 = np.outer(omega, omega.conj())
    P1 = np.eye(dimr) - P0
    X = (10 / 13) * P0 + (14 / 13) * P1
    sqrtX = math.sqrt(10 / 13) * P0 + math.sqrt(14 / 13) * P1
    K = np.kron(np.eye(1 + d * d), sqrtX) @ W
    spectrum = np.linalg.eigvalsh(K.conj().T @ K)
    expected_spectrum = np.array([7 / 13] * 5 + [1] * 4)
    q = 12 / 13
    errors = {
        "spectrum": np.linalg.norm(spectrum - expected_spectrum),
        "E_isometry": np.linalg.norm(E.conj().T @ E - np.eye(dimi)),
    }
    for trial in range(5):
        z = rng.normal(size=d) + 1j * rng.normal(size=d)
        z /= np.linalg.norm(z)
        v = np.kron(coherent(z, insa), coherent(z.conj(), insb))
        residual = np.kron(coherent(z, resa), coherent(z.conj(), resb))
        target = np.concatenate(([1], np.kron(z, z.conj()))) / math.sqrt(2)
        wanted = np.kron(target, sqrtX @ residual)
        errors[f"factorization_{trial}"] = np.linalg.norm(K @ v - wanted)
        errors[f"success_{trial}"] = abs(np.linalg.norm(K @ v) ** 2 - q)
    assert max(errors.values()) < 1e-11, errors
    return {
        "d": d, "n": n, "m": m,
        "residual_LP_weights": [5 / 13, 7 / 13],
        "residual_X_eigenvalues": [10 / 13, 14 / 13],
        "q": q,
        "old_top_residual_filter_q": 1 / 2,
        "effect_spectrum": spectrum.tolist(),
        "max_residual": max(errors.values()),
        "errors": errors,
    }


if __name__ == "__main__":
    result = {"scope": "finite matrix checks only", "cases": [case(d, n) for d in (2, 3, 4) for n in (1, 2, 3)],
              "nontrivial_residual_X_case": two_by_two()}
    print(json.dumps(result, indent=2))
