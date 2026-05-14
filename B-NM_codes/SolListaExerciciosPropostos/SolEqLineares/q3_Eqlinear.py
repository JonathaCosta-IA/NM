# ============================================================
# ENUNCIADO:
# - Implementar método de Jacobi
# - Critério: ||x(k+1) - x(k)||
# - Determinar número de iterações
# - Comparar com solução exata
# ============================================================

import numpy as np

# -------------------- Dados --------------------
A = np.array([[10., -1., 2., 0.],
              [-1., 11., -1., 3.],
              [2., -1., 10., -1.],
              [0., 3., -1., 8.]])

b = np.array([6., 25., -11., 15.])


# -------------------- Função --------------------
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


# -------------------- Resultados --------------------
x_jacobi, it = jacobi(A, b)
x_exato = np.linalg.solve(A, b)

print("Solução Jacobi:", x_jacobi)
print("Iterações:", it)
print("Solução exata:", x_exato)