# ============================================================
# ENUNCIADO:
# f(x) = e^{-x} - x
# - Implementar falsa posição
# - Comparar com bisseção
# - Analisar eficiência
# ============================================================

import numpy as np

def f(x):
    return np.exp(-x) - x


def falsa_posicao(f, a, b, tol=1e-6, max_iter=1000):
    for k in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

        if abs(f(c)) < tol:
            return c, k+1

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c, max_iter


def bissecao(f, a, b, tol=1e-6):
    for k in range(1000):
        c = (a+b)/2
        if abs(f(c)) < tol:
            return c, k+1
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c, k+1


# -------------------- Resultados --------------------
r_fp, it_fp = falsa_posicao(f, 0, 1)
r_bi, it_bi = bissecao(f, 0, 1)

print("Falsa posição:", r_fp, "Iterações:", it_fp)
print("Bisseção:", r_bi, "Iterações:", it_bi)