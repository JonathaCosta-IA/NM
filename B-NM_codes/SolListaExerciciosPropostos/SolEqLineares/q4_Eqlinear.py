# ============================================================
# ENUNCIADO:
# - Implementar Jacobi e Gauss-Seidel
# - Comparar número de iterações
# - Analisar convergência
# - Validar com solução exata
# ============================================================

import numpy as np

# -------------------- Dados --------------------
A = np.array([[4., 1.],
              [2., 3.]])

b = np.array([1., 2.])


# -------------------- Funções --------------------
def jacobi(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)

    for k in range(max_iter):
        x_new = np.zeros(n)

        for i in range(n):
            s = np.dot(A[i,:], x) - A[i,i]*x[i]
            x_new[i] = (b[i] - s) / A[i,i]

        if np.linalg.norm(x_new - x) < tol:
            return x_new, k+1

        x = x_new

    return x, max_iter


def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.zeros(n)

    for k in range(max_iter):
        x_old = x.copy()

        for i in range(n):
            s1 = np.dot(A[i,:i], x[:i])
            s2 = np.dot(A[i,i+1:], x_old[i+1:])
            x[i] = (b[i] - s1 - s2) / A[i,i]

        if np.linalg.norm(x - x_old) < tol:
            return x, k+1

    return x, max_iter


# -------------------- Resultados --------------------
x_j, it_j = jacobi(A, b)
x_gs, it_gs = gauss_seidel(A, b)
x_exato = np.linalg.solve(A, b)

print("Jacobi:", x_j, "Iterações:", it_j)
print("Gauss-Seidel:", x_gs, "Iterações:", it_gs)
print("Exato:", x_exato)