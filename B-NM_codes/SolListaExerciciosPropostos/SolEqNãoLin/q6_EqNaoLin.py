# ============================================================
# ENUNCIADO:
# f(x) = ln(x) + x^2 - 3
# - Implementar bisseção e Newton
# - Comparar soluções
# - Analisar convergência
# - Plotar gráfico
# ============================================================

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x) + x**2 - 3

def df(x):
    return 1/x + 2*x


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


def newton(f, df, x0):
    x = x0
    for k in range(100):
        x_new = x - f(x)/df(x)
        if abs(x_new - x) < 1e-6:
            return x_new, k+1
        x = x_new
    return x, k+1


# -------------------- Resultados --------------------
x_bi, it_bi = bissecao(f, 1, 2)
x_new, it_new = newton(f, df, 1.5)

print("Bisseção:", x_bi, it_bi)
print("Newton:", x_new, it_new)

# -------------------- Gráfico --------------------
x = np.linspace(0.1, 2, 100)
y = f(x)

plt.plot(x, y,'r')
plt.axhline(0)
plt.grid()
plt.show()