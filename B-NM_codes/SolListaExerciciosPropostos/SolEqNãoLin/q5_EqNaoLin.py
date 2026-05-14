# ============================================================
# ENUNCIADO:
# f(x) = x^3 - 7x + 6
# - Implementar secante
# - x0 = 0, x1 = 1
# - tol = 1e-6
# - Comparar com Newton
# ============================================================

import numpy as np

def f(x):
    return x**3 - 7*x + 6

def df(x):
    return 3*x**2 - 7


def secante(f, x0, x1, tol=1e-6):
    for k in range(100):
        x2 = x1 - f(x1)*(x1 - x0)/(f(x1) - f(x0))
        if abs(x2 - x1) < tol:
            return x2, k+1
        x0, x1 = x1, x2
    return x2, k+1


def newton(f, df, x0):
    x = x0
    for k in range(100):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < 1e-6:
            return x_new, k+1
        x = x_new
    return x, k+1


# -------------------- Resultados --------------------
x_sec, it_sec = secante(f, 0, 1)
x_new, it_new = newton(f, df, 1)

print("Secante:", x_sec, "Iterações:", it_sec)
print("Newton:", x_new, "Iterações:", it_new)