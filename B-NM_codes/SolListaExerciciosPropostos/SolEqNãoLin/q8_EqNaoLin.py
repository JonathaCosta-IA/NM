# ============================================================
# ENUNCIADO:
# f(x) = x - tan(x)
# - Implementar bisseção, secante, Newton
# - Comparar iterações
# - Discutir dificuldades numéricas
# ============================================================

import numpy as np

def f(x):
    return x - np.tan(x)

def df(x):
    return 1 - 1/np.cos(x)**2


def bissecao(f, a, b):
    for k in range(1000):
        c = (a+b)/2
        if abs(f(c)) < 1e-6:
            return c, k+1
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return c, k+1


def secante(f, x0, x1):
    for k in range(100):
        x2 = x1 - f(x1)*(x1-x0)/(f(x1)-f(x0))
        if abs(x2-x1) < 1e-6:
            return x2, k+1
        x0, x1 = x1, x2
    return x2, k+1


def newton(f, df, x0):
    x = x0
    for k in range(100):
        x_new = x - f(x)/df(x)
        if abs(x_new-x) < 1e-6:
            return x_new, k+1
        x = x_new
    return x, k+1


# -------------------- Resultados --------------------
x_bi, it_bi = bissecao(f, 4, 4.7)
x_sec, it_sec = secante(f, 4, 4.5)
x_new, it_new = newton(f, df, 4.5)

print("Bisseção:", it_bi)
print("Secante:", it_sec)
print("Newton:", it_new)