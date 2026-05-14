# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [-1,0,1,2,3]
# y = [1,0,1,8,27]
#
# - Implementar:
#   * Regressão polinomial
#   * Lagrange
#   * Newton
#   * Splines
# - Comparar resultados
# - Análise de erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# ---------------------------------------------
# Classe base
# ---------------------------------------------
class Interpolador:
    def __init__(self, x, y):
        self.x = np.array(x)
        self.y = np.array(y)

# ---------------------------------------------
# Lagrange
# ---------------------------------------------
class Lagrange(Interpolador):
    def avaliar(self, xp):
        n = len(self.x)
        yp = 0
        for i in range(n):
            L = 1
            for j in range(n):
                if i != j:
                    L *= (xp - self.x[j])/(self.x[i] - self.x[j])
            yp += self.y[i]*L
        return yp

# ---------------------------------------------
# Regressão polinomial
# ---------------------------------------------
class Regressao(Interpolador):
    def __init__(self, x, y, grau):
        super().__init__(x,y)
        self.coef = np.polyfit(x,y,grau)

    def avaliar(self, xp):
        return np.polyval(self.coef, xp)

# ---------------------------------------------
# Spline cúbico
# ---------------------------------------------
class SplineCubico(Interpolador):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.cs = CubicSpline(x,y, bc_type='natural')

    def avaliar(self, xp):
        return self.cs(xp)

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([-1,0,1,2,3])
y = np.array([1,0,1,8,27])

# ---------------------------------------------
# Modelos
# ---------------------------------------------
lag = Lagrange(x,y)
reg = Regressao(x,y,3)
spl = SplineCubico(x,y)

# ---------------------------------------------
# Avaliação
# ---------------------------------------------
x_plot = np.linspace(-1,3,200)

y_lag = np.array([lag.avaliar(xi) for xi in x_plot])
y_reg = reg.avaliar(x_plot)
y_spl = spl.avaliar(x_plot)

# ---------------------------------------------
# Erro (referência: x^3)
# ---------------------------------------------
y_real = x_plot**3

def erro(y_real, y_modelo):
    return np.mean(np.abs(y_real - y_modelo))

print("Erro Lagrange:", erro(y_real,y_lag))
print("Erro Regressão:", erro(y_real,y_reg))
print("Erro Spline:", erro(y_real,y_spl))

# ---------------------------------------------
# Gráfico comparativo
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_real, label='Real')
plt.plot(x_plot, y_lag, '--', label='Lagrange')
plt.plot(x_plot, y_reg, '--', label='Regressão')
plt.plot(x_plot, y_spl, '--', label='Spline')
plt.scatter(x,y)
plt.legend()
plt.grid(True)
plt.show()