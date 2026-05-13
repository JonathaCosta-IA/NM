"""
Com base no seguinte conjunto de dados:
 x = {0.1, 0.2, 0.3, 0.4}
 y = {1.2, 2.3, 3.1, 3.9}
 Use a regressão linear por mínimos quadrados para determinar os 
     Produza um $novoY$ a partir da reta gerada.
     Calcule o erro quadrático total.
     Trace o gráfico com: x por y , x por novoY
     Interprete o coeficiente angular b como a rigidez do sistema,
     à luz da relação força--deslocamento. 
"""
#=========================================================================

import numpy as np
import matplotlib.pyplot as plt

x=np.array([0.1, 0.2, 0.3, 0.4])
y=np.array([1.2, 2.3, 3.1, 3.9])
coef = np.polyfit(x,y,1)
m=np.round(coef[0],3)
b=np.round(coef[1],3)
print(f"A equação descrita pelos coeficientes é:\n y={m}x + {b}")
# ---------------------------------------------
# novo X
x_novo = 7.25
y_novo = np.round(np.polyval(coef,x_novo),3)
print(f"\nO valor de x = {x_novo} resulta em imagem {y_novo}.")
# ---------------------------------------------
NovoY = np.polyval(coef,x)

# ---------------------------------------------
s = np.sum((y - NovoY)**2) # srq
print(f"Erro global(soma dos resíduos dos quadrados) vale: {np.round(s, 4)}")


# ---------------------------------------------
plt.figure(figsize=(12,8))
plt.plot(x,y,'o',label="Dados")
plt.plot(x,NovoY,"--",label="Ajuste linear")
plt.title(f"Função para reta\n y={m}x + {b}")
plt.grid(True)
plt.legend()
plt.show()

# Interpretação de mx
#------------------------------------

interpretacao="""
------------------------------------------------------------------------------
É esperado que o aluno reconheça que b = dF /dx, ou seja,a taxa de variação da
força em relação ao deslocamento é o coeficiente angular.
Se comparado com o modelo clássico: F = kx, tem-se que:
    
 b≈k.

Isso implica que quanto maior (b) maior da rigidez do sistema e
quanto menor for b, menor será a rigidez do sistema, portanto, 
mais flexível é o sistema.
------------------------------------------------------------------------------
  """
print(interpretacao)
