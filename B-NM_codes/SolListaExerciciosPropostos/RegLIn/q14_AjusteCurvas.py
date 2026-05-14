# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [0,1,2,3]
# y = [0,1,0,1]
#
# - Construir spline cúbico natural
# - Analisar erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([0,1,2,3])
y = np.array([0,1,0,1])

# ---------------------------------------------
# Spline cúbico natural
# ---------------------------------------------
cs = CubicSpline(x,y, bc_type='natural')

x_plot = np.linspace(0,3,200)
y_plot = cs(x_plot)

# referência (polinômio grau 3)
y_ref = np.polyval(np.polyfit(x,y,3), x_plot)
erro = np.abs(y_ref - y_plot)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print(f"Erro médio: {np.mean(erro):.6f}")

# ---------------------------------------------
# Gráfico
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_plot, label='Spline cúbico')
plt.plot(x_plot, y_ref, '--', label='Polinômio grau 3')
plt.scatter(x,y)
plt.legend()
plt.grid(True)
plt.show()