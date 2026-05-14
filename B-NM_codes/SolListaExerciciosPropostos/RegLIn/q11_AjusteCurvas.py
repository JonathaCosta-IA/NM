# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [1, 2]
# y = [2, 4]
#
# - Construir spline linear
# - Estimar f(1.5)
# - Analisar erro
# - Representar graficamente
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([1,2])
y = np.array([2,4])

# ---------------------------------------------
# Função spline linear
# ---------------------------------------------
def spline_linear(x, y, xp):
    return y[0] + (y[1]-y[0])*(xp-x[0])/(x[1]-x[0])

# ---------------------------------------------
# Estimativa
# ---------------------------------------------
xp = 1.5
yp = spline_linear(x,y,xp)

# Função real (linear exata)
real = 2*xp
erro = np.abs(real - yp)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(f"f(1.5) ≈ {yp:.6f}")
print(f"Erro = {erro:.6e}")

# ---------------------------------------------
# Gráfico
# ---------------------------------------------
x_plot = np.linspace(1,2,100)
y_plot = [spline_linear(x,y,xi) for xi in x_plot]

plt.figure()
plt.plot(x_plot, y_plot, label='Spline linear')
plt.plot(x_plot, 2*x_plot, '--', label='Função real')
plt.scatter(x,y)
plt.legend()
plt.grid(True)
plt.show()