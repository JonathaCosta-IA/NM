# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [0,1,2]
# y = [1,3,2]
#
# - Construir spline linear
# - Analisar erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([0,1,2])
y = np.array([1,3,2])

# ---------------------------------------------
# Função spline linear
# ---------------------------------------------
def spline_linear(x, y, xp):
    for i in range(len(x)-1):
        if x[i] <= xp <= x[i+1]:
            return y[i] + (y[i+1]-y[i])*(xp-x[i])/(x[i+1]-x[i])

# ---------------------------------------------
# Avaliação
# ---------------------------------------------
x_plot = np.linspace(0,2,200)
y_plot = [spline_linear(x,y,xi) for xi in x_plot]

# erro (comparando com interpolação quadrática)
y_real = np.polyval(np.polyfit(x,y,2), x_plot)
erro = np.abs(y_real - y_plot)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(f"Erro médio: {np.mean(erro):.6f}")

# ---------------------------------------------
# Gráfico
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_plot, label='Spline linear')
plt.plot(x_plot, y_real, '--', label='Referência')
plt.scatter(x,y)
plt.legend()
plt.grid(True)
plt.show()