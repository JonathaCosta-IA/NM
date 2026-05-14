# ============================================================
# ENUNCIADO:
# - Implementar Gauss com pivoteamento parcial
# - Resolver sistema
# - Comparar com sem pivoteamento
# - Calcular resíduos
# - Discutir estabilidade
# ============================================================

import numpy as np

# -------------------- Dados --------------------
A = np.array([[0., 2., 3.],
              [4., 5., 6.],
              [7., 8., 9.]])

b = np.array([6., 15., 24.])


# -------------------- Funções --------------------
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

    return x


def gauss_pivoteamento(A, b):
    A = A.copy()
    b = b.copy()
    n = len(b)

    for k in range(n-1):
        p = np.argmax(abs(A[k:,k])) + k

        if p != k:
            A[[k,p]] = A[[p,k]]
            b[[k,p]] = b[[p,k]]

        for i in range(k+1, n):
            m = A[i,k] / A[k,k]
            A[i,k:] -= m * A[k,k:]
            b[i] -= m * b[k]

    x = np.zeros(n)
    for i in reversed(range(n)):
        x[i] = (b[i] - np.dot(A[i,i+1:], x[i+1:])) / A[i,i]

    return x


# -------------------- Resultados --------------------
x_piv = gauss_pivoteamento(A, b)
res_piv = np.linalg.norm(A @ x_piv - b)

print("Solução com pivoteamento:", x_piv)
print("Resíduo (pivoteado):", res_piv)

# tentativa sem pivoteamento
try:
    x_np = gauss_sem_pivoteamento(A, b)
    res_np = np.linalg.norm(A @ x_np - b)
    print("Solução sem pivoteamento:", x_np)
    print("Resíduo (sem pivoteamento):", res_np)
except:
    print("Falha sem pivoteamento (pivô nulo).")