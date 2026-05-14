# ============================================================
# ENUNCIADO:
# - Implementar fatoração LU (sem pivoteamento)
# - Resolver sistema usando LU
# - Resolver com numpy.linalg.solve
# - Comparar erro
# ============================================================

import numpy as np

# -------------------- Dados --------------------
A = np.array([[1., 2., 3.],
              [2., 5., 2.],
              [3., 1., 5.]])

b = np.array([14., 18., 20.])


# -------------------- Funções --------------------
def LU(A):
    n = A.shape[0]
    L = np.eye(n)
    U = A.copy()

    for k in range(n-1):
        for i in range(k+1, n):
            L[i,k] = U[i,k] / U[k,k]
            U[i,k:] -= L[i,k] * U[k,k:]

    return L, U


def solve_LU(L, U, b):
    n = len(b)

    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i,:i], y[:i])

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (y[i] - np.dot(U[i,i+1:], x[i+1:])) / U[i,i]

    return x


# -------------------- Resultados --------------------
L, U = LU(A)
x_lu = solve_LU(L, U, b)
x_np = np.linalg.solve(A, b)

erro = np.linalg.norm(x_lu - x_np)

print("x (LU):", x_lu)
print("x (NumPy):", x_np)
print("Erro:", erro)