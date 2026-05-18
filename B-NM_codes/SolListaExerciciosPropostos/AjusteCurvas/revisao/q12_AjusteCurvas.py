# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [0,1,2]
# y = [1,2,0]
#
# - Construir spline quadrática com continuidade da derivada
# - Analisar erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([0,1,2])
y = np.array([1,2,0])

# ---------------------------------------------
# Sistema para spline quadrática
# S1(x) = a1 + b1(x-x0) + c1(x-x0)^2
# S2(x) = a2 + b2(x-x1) + c2(x-x1)^2
# ---------------------------------------------

# Montagem do sistema linear
A = np.array([
    [1,0,0,0,0,0],
    [1,1,1,0,0,0],
    [0,0,0,1,0,0],
    [0,0,0,1,1,1],
    [0,1,2,0,-1,0],
    [0,0,0,0,1,2]
], dtype=float)

b = np.array([1,2,2,0,0,0], dtype=float)

coef = np.linalg.solve(A,b)

# ---------------------------------------------
# Funções spline
# ---------------------------------------------
def S1(xp):
    return coef[0] + coef[1]*xp + coef[2]*xp**2

def S2(xp):
    t = xp-1
    return coef[3] + coef[4]*t + coef[5]*t**2

# ---------------------------------------------
# Avaliação
# ---------------------------------------------
x_plot = np.linspace(0,2,200)
y_plot = []

for xi in x_plot:
    if xi <= 1:
        y_plot.append(S1(xi))
    else:
        y_plot.append(S2(xi))

y_plot = np.array(y_plot)

# referência (polinômio grau 2)
y_ref = np.polyval(np.polyfit(x,y,2), x_plot)
erro = np.abs(y_ref - y_plot)

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print("Coeficientes:", coef)
print(f"Erro médio: {np.mean(erro):.6f}")

# ---------------------------------------------
# Gráfico
# ---------------------------------------------
plt.figure()
plt.plot(x_plot, y_plot, label='Spline quadrática')
plt.plot(x_plot, y_ref, '--', label='Referência')
plt.scatter(x,y)
plt.legend()
plt.grid(True)
plt.show()