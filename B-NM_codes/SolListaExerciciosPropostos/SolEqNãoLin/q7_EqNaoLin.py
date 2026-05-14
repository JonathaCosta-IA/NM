# ============================================================
# ENUNCIADO:
# Sistema:
# x^2 + y^2 = 4
# x - y = 1
# - Implementar Newton para sistemas
# - Construir Jacobiana
# ============================================================

import numpy as np

def F(X):
    x, y = X
    return np.array([x**2 + y**2 - 4,
                     x - y - 1])

def J(X):
    x, y = X
    return np.array([[2*x, 2*y],
                     [1, -1]])


def newton_sistema(F, J, X0, tol=1e-6):
    X = X0

    for k in range(100):
        delta = np.linalg.solve(J(X), -F(X))
        X_new = X + delta

        if np.linalg.norm(X_new - X) < tol:
            return X_new, k+1

        X = X_new

    return X, k+1


# -------------------- Resultados --------------------
sol, it = newton_sistema(F, J, np.array([1., 1.]))

print("Solução:", sol)
print("Iterações:", it)
print("Validação F(x):", F(sol))