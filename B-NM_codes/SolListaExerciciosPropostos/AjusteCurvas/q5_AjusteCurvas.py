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
#%% --------------------------------------------------------

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


lista_coeficientes = []
lista_erros = []
lista_r2 = []
for i in range(2,5):
    # Cálculo dos coeficientes do polinômio de grau i
    coef = np.polyfit(x, y, i)
    y_modelo = np.polyval(coef, x)
    erro = erro_absoluto(y, y_modelo)
    r2 = r2_score(y, y_modelo)
    # Armazenamento dos resultados
    lista_coeficientes.append(coef)
    lista_erros.append(erro)
    lista_r2.append(r2)
    # Exibição dos resultados
    print(f"Grau {i}:")
    print(f"Coeficientes: {np.round(coef,4)}")
    print(f"Erro absoluto: {erro:.6f}")
    print(f"R²: {r2:.6f}\n")

# ---------------------------------------------
# Escolha do melhor modelo (maior R²)
# ---------------------------------------------
melhor_grau = np.argmax(lista_r2) + 2  # +2 porque os graus começam em 2
print(f"Modelo mais adequado: grau {melhor_grau}")

# ---------------------------------------------
# Gráfico comparativo
# ---------------------------------------------
x_plot = np.linspace(min(x), max(x))

plt.figure(figsize=(10,6))
plt.plot(x, y, 'o', label='Dados')
for i in range(3):
    coef = lista_coeficientes[i]
    y_plot = np.polyval(coef, x_plot)
    plt.plot(x_plot, y_plot, label=f'Grau {i+2}')

plt.grid(True)
plt.title("Comparação de ajustes polinomiais")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
# %%
