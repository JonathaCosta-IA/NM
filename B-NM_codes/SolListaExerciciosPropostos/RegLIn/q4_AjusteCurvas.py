# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# Sejam os vetores:
# x = [-2, -1, 0, 1, 2]
# y = [4.1, 1.0, 0.2, 1.1, 3.9]
#
# - Ajustar um polinômio p(x) de grau 2 aos dados.
# - Calcular o erro absoluto associado ao ajuste.
# - Comparar graficamente y e p(x) em função de x.
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([-2, -1, 0, 1, 2])
y = np.array([4.1, 1.0, 0.2, 1.1, 3.9])

# ---------------------------------------------
# 1) Ajuste polinomial (grau 2)
# ---------------------------------------------
coef = np.polyfit(x, y, 2)   # [a, b, c]
a, b, c = coef

print("Polinômio ajustado:")
print(f"p(x) = {a:.4f}x² + {b:.4f}x + {c:.4f}")

# ---------------------------------------------
# 2) Avaliação do modelo nos pontos originais
# ---------------------------------------------
y_ajust = np.polyval(coef, x)

# ---------------------------------------------
# 3) Erro absoluto total
# ---------------------------------------------
erro_abs_total = np.sum(np.abs(y - y_ajust))

print(f"\nErro absoluto total: {erro_abs_total:.6f}")

# Erro ponto a ponto (diagnóstico)
print("\nErro absoluto por ponto:")
for xi, yi, yi_aj in zip(x, y, y_ajust):
    print(f"x = {xi:>2} | |erro| = {abs(yi - yi_aj):.6f}")

# ---------------------------------------------
# 4) Curva suave para visualização
# ---------------------------------------------
x_plot = np.linspace(min(x), max(x), 200)
y_plot = np.polyval(coef, x_plot)

# ---------------------------------------------
# 5) Gráfico comparativo
# ---------------------------------------------
plt.figure(figsize=(10,6))
plt.plot(x, y, 'o', label='Dados experimentais')
plt.plot(x_plot, y_plot, '-', label='Ajuste quadrático')
plt.grid(True)
plt.legend()
plt.title("Ajuste polinomial de grau 2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()