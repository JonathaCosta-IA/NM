# ============================================================
# ENUNCIADO:
# f(x) = cos(x) - x
# - Implementar ponto fixo
# - Escolher g(x)
# - Verificar |g'(x)| < 1
# - Comparar com Newton
# ============================================================

import numpy as np

def g(x):
    return np.cos(x)

def dg(x):
    return -np.sin(x)

def f(x):
    return np.cos(x) - x

def df(x):
    return -np.sin(x) - 1


def ponto_fixo(g, x0, tol=1e-6):
    x = x0
    for k in range(1000):
        x_new = g(x)
        if abs(x_new - x) < tol:
            return x_new, k+1
        x = x_new
    return x, k+1


def newton(f, df, x0):
    x = x0
    for k in range(100):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < 1e-6:
            return x_new, k+1
        x = x_new
    return x, k+1


# -------------------- Resultados --------------------
x_pf, it_pf = ponto_fixo(g, 0.5)
x_new, it_new = newton(f, df, 0.5)

print("Ponto fixo:", x_pf, "Iterações:", it_pf)
print("Newton:", x_new, "Iterações:", it_new)
print("|g'(x)| ≈", abs(dg(x_pf)))