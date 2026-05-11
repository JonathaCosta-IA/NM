#=========================================================================
# Exercício 5.1 / Capítulo 5 Ajuste de Curvas e Interpolação, Gilat.
# Com base no seguinte conjunto de dados:
# x = {2,5,6,8,9,13,15}
# y = {7,8,10,11,12,14,15}
# Use a regressão linear por mínimos quadrados para determinar os 
# coeficientes m e b da função y = mx + b que melhor se ajusta aos dados.
# Determinar o erro global.
#=========================================================================

# (JRC) Adicionalmente:
#  A - Encontre o valor para x = 7.25
#  B - Trace um gráfico com a função encontrada e encontre
#=========================================================================

import numpy as np
import matplotlib.pyplot as plt

x=np.array([2,5,6,8,9,13,15])
y=np.array([7,8,10,11,12,14,15])
coef = np.polyfit(x,y,1)
m=np.round(coef[0],2)
b=np.round(coef[1],2)
print(f"A equação descrita pelos coeficientes é:\n y={m}x + {b}")
# ---------------------------------------------
# novo X
x_novo = 7.25
y_novo = np.round(np.polyval(coef,x_novo),2)
print(f"\nO valor de x = {x_novo} resulta em imagem {y_novo}.")
# ---------------------------------------------
y2 = np.polyval(coef,x)

# ---------------------------------------------
s = np.sum((y - y2)**2) # srq
print(f"Erro global(soma dos resíduos dos quadrados) vale: {np.round(s, 4)}")

# ---------------------------------------------
plt.figure(figsize=(12,8))
plt.plot(x,y,'o',label="Dados")
plt.plot(x,y2,"--",label="Ajuste linear")
plt.title(f"Função para reta\n y={m}x + {b}")
plt.grid(True)
plt.legend()
plt.show()

