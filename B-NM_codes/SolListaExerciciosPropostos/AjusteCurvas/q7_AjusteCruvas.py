# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [0,1,2]
# y = [1, e, e²]
#
# - Construir Lagrange
# - Analisar erro
# - Comparar com função real
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([0,1,2])
y = np.exp(x)

# ---------------------------------------------
# Funções auxiliares
# ---------------------------------------------
def lagrange(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*L
    return yp

# ---------------------------------------------
# Avaliação
# ---------------------------------------------
x_plot = np.linspace(0,2,200)
y_lag = np.array([lagrange(x,y,xi) for xi in x_plot])
y_real = np.exp(x_plot)

erro = np.abs(y_real - y_lag)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(f"Erro médio: {np.mean(erro):.6e}")
print(f"Erro máximo: {np.max(erro):.6e}")

# ---------------------------------------------
# Gráfico
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_real, label='exp(x)')
plt.plot(x_plot, y_lag, '--', label='Lagrange')
plt.scatter(x, y)
plt.legend()
plt.grid(True)
plt.show()