# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# Sejam os vetores:
# x = [1, 2, 3]
# y = [1, 4, 9]
#
# - Construir o polinômio interpolador de Lagrange
# - Estimar f(2.5)
# - Analisar erro
# - Apresentar graficamente
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([1, 2, 3])
y = np.array([1, 4, 9])

# ---------------------------------------------
# Lagrange com exibição do polinômio p(x)
# -------------------------------------------------
def lagrange(x, y):
    n = len(x)
    p = np.poly1d([0.0])

    for i in range(n):
        Li = np.poly1d([1.0])

        for j in range(n):
            if i != j:
                Li *= np.poly1d([1.0, -x[j]]) / (x[i] - x[j])

        p += y[i] * Li

    return p

p = lagrange(x, y)

print("\nPolinômio p(x):")
print(p)

#%%
def lagrange2(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*L
    return yp

def erro_absoluto(real, aprox):
    return np.abs(real - aprox)

# ---------------------------------------------
# Estimativa
# ---------------------------------------------
xp = 2.5
yp = lagrange(x, y, xp)

# valor real (sabemos que é x²)
real = xp**2
erro = erro_absoluto(real, yp)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(f"f(2.5) ≈ {yp:.6f}")
print(f"Valor real = {real:.6f}")
print(f"Erro = {erro:.6e}")

# ---------------------------------------------
# Gráfico comparativo
# ---------------------------------------------
x_plot = np.linspace(1, 3)
y_plot = [lagrange(x, y, xi) for xi in x_plot]

plt.figure()
plt.plot(x, y, 'o', label='Dados')
plt.plot(x_plot, y_plot, label='Lagrange')
plt.plot(x_plot, x_plot**2, '--', label='Real (x²)')
plt.legend()
plt.grid(True)
plt.show()