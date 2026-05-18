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
def lagrange(x, y):
    n = len(x)
    p = np.poly1d([0])
    for i in range(n):
        L = np.poly1d([1])
        for j in range(n):
            if i != j:
                L *= np.poly1d([1, - x[j]]) / (x[i] - x[j])
        p += y[i]*L
    return p

# ---------------------------------------------
# Avaliação
# ---------------------------------------------
x_plot = np.linspace(0,2)
modelo = lagrange(x, y) # Construção do modelo de Lagrange
y_lag = modelo(x_plot)
y_real = np.exp(x_plot)
erro = np.abs(y_real - y_lag)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(modelo)
print(f"Erro médio: {np.mean(erro):.6e}")
print(f"Erro máximo: {np.max(erro):.6e}")
# ---------------------------------------------
# Gráfico
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_real, label='exp(x)')
plt.plot(x_plot, y_lag, '--', label='Modelo de Lagrange')
plt.scatter(x, y)
plt.legend()
plt.title(f"Ajuste de Curvas - Lagrange")
plt.grid(True)
plt.show()