# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# Sejam os vetores:
# x = [-1, 0, 1, 2, 3]
# y = [1, 0, 1, 8, 27]
#
# - Ajustar polinômios p(x) de grau 2, 3 e 4.
# - Calcular o erro absoluto para cada modelo.
# - Determinar o coeficiente de determinação R² para cada ajuste.
# - Identificar o modelo mais adequado.
# - Comparar graficamente os ajustes obtidos.
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([-1, 0, 1, 2, 3])
y = np.array([1, 0, 1, 8, 27])

# ---------------------------------------------
# Funções auxiliares
# ---------------------------------------------
def erro_absoluto(y, y_modelo):
    return np.sum(np.abs(y - y_modelo))

def r2_score(y, y_modelo):
    ss_res = np.sum((y - y_modelo)**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - ss_res/ss_tot

# ---------------------------------------------
# Ajuste grau 2
# ---------------------------------------------
coef2 = np.polyfit(x, y, 2)
y2 = np.polyval(coef2, x)
erro2 = erro_absoluto(y, y2)
r2_2 = r2_score(y, y2)

# ---------------------------------------------
# Ajuste grau 3
# ---------------------------------------------
coef3 = np.polyfit(x, y, 3)
y3 = np.polyval(coef3, x)
erro3 = erro_absoluto(y, y3)
r2_3 = r2_score(y, y3)

# ---------------------------------------------
# Ajuste grau 4
# ---------------------------------------------
coef4 = np.polyfit(x, y, 4)
y4 = np.polyval(coef4, x)
erro4 = erro_absoluto(y, y4)
r2_4 = r2_score(y, y4)

# ---------------------------------------------
# Impressão dos resultados
# ---------------------------------------------
print("Grau 2:")
print(f"Coeficientes: {np.round(coef2,4)}")
print(f"Erro absoluto: {erro2:.6f}")
print(f"R²: {r2_2:.6f}\n")

print("Grau 3:")
print(f"Coeficientes: {np.round(coef3,4)}")
print(f"Erro absoluto: {erro3:.6f}")
print(f"R²: {r2_3:.6f}\n")

print("Grau 4:")
print(f"Coeficientes: {np.round(coef4,4)}")
print(f"Erro absoluto: {erro4:.6f}")
print(f"R²: {r2_4:.6f}\n")

# ---------------------------------------------
# Escolha do melhor modelo (maior R²)
# ---------------------------------------------
if r2_3 >= r2_4 and r2_3 >= r2_2:
    melhor_grau = 3
elif r2_4 >= r2_2:
    melhor_grau = 4
else:
    melhor_grau = 2

print(f"Modelo mais adequado: grau {melhor_grau}")

# ---------------------------------------------
# Gráfico comparativo
# ---------------------------------------------
x_plot = np.linspace(min(x), max(x), 200)

y_plot2 = np.polyval(coef2, x_plot)
y_plot3 = np.polyval(coef3, x_plot)
y_plot4 = np.polyval(coef4, x_plot)

plt.figure(figsize=(10,6))
plt.plot(x, y, 'o', label='Dados')
plt.plot(x_plot, y_plot2, label='Grau 2')
plt.plot(x_plot, y_plot3, label='Grau 3')
plt.plot(x_plot, y_plot4, label='Grau 4')

plt.grid(True)
plt.legend()
plt.title("Comparação de ajustes polinomiais")
plt.xlabel("x")
plt.ylabel("y")
plt.show()