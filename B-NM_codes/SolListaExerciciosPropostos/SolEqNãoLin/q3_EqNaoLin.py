# ============================================================
# ENUNCIADO:
# f(x) = x^3 - 2x - 5
# - Implementar Newton
# - x0 = 2
# - Critério: erro relativo
# - Analisar convergência
# ============================================================

import numpy as np

def f(x):
    return x**3 - 2*x - 5

def df(x):
    return 3*x**2 - 2


def newton(f, df, x0, tol=1e-6, max_iter=100):
    x = x0

    for k in range(max_iter):
        x_new = x - f(x)/df(x)

        if abs((x_new - x)/x_new) < tol:
            return x_new, k+1

        x = x_new

    return x, max_iter


# -------------------- Resultados --------------------
raiz, it = newton(f, df, 2)

print("Raiz:", raiz)
print("Iterações:", it)