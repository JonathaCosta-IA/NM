# ============================================================
# ENUNCIADO:
# Considere o sistema Ax = b.
# - Implementar eliminação de Gauss sem pivoteamento
# - Resolver o sistema
# - Mostrar matriz triangular superior
# - Calcular o resíduo ||Ax - b||
# ============================================================

import numpy as np

# -------------------- Dados --------------------
A = np.array([[2., -1., 1.],
              [3.,  3., 9.],
              [3.,  3., 5.]])

b = np.array([2., -1., 4.])


# -------------------- Função --------------------
def gauss_sem_pivoteamento(A, b):
    A = A.copy()
    b = b.copy()
    n = len(b)

    for k in range(n-1):
        for i in range(k+1, n):
            m = A[i,k] / A[k,k]
            A[i, k:] -= m * A[k, k:]
            b[i] -= m * b[k]

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]

    return A, x


# -------------------- Resultados --------------------
U, x = gauss_sem_pivoteamento(A, b)
residuo = np.linalg.norm(A @ x - b)

print("Matriz U:\n", U)
print("Solução x:", x)
print("\nResíduo:", residuo)