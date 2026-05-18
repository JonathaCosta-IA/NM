"""
Com base no seguinte conjunto de dados:
 x = {2,5,6,8,9,13,15}
 y = {7,8,10,11,12,14,15}
 Use a regressão linear por mínimos quadrados para determinar os 
Determine a reta $y = a + bx$ por mínimos quadrados 
 -Produza um $novoY$ a partir da reta gerada.
 -Calcule o erro quadrático total.
 -Trace o gráfico com: x por y , x por novoY 
"""
#=========================================================================
#%%
import numpy as np
import matplotlib.pyplot as plt

x=np.array([2,5,6,8,9,13,15])
y=np.array([7,8,10,11,12,14,15])
coef = np.polyfit(x,y,1)
p = np.poly1d(coef)
print(f"\nPolinômio p(x):{p}")

comentarios = """
----------------------------------------------------------------------------------
Perceba que:
Os comandos polyfit e poly1d são complementares.
 -numpy.polyfit calcula os coeficientes do polinômio de ajuste;
    Manualmente, o coeficiente de x (m) e o coeficiente constante (b) podem ser extraídos dos 
    coeficientes retornados por polyfit,
    m=np.round(coef[0],3)
    b=np.round(coef[1],3)
    print(f"A equação descrita pelos coeficientes é: y={m}x + {b}")

 -numpy.poly1d representa o polinômio a partir dos coeficientes, permitindo avaliar o polinômio 
 em qualquer ponto x. P(x) é a função polinomial que pode ser usada para calcular os valores de y 
 correspondentes a qualquer valor de x, incluindo os dados originais e novos pontos.
 print(f"\nPolinômio p(x):{p}")
 Aqui é possível avaliar o polinômio em qualquer valor de x, por exemplo: p(5)
 ----------------------------------------------------------------------------------
 """
print(comentarios)

# ---------------------------------------------
# novo X
x_novo = 7.25
y_novo = p(x_novo)
print(f"\nO valor de x = {x_novo} resulta em imagem {y_novo}.")
# ---------------------------------------------
NovoY = p(x)
# ---------------------------------------------
s = np.sum((y - NovoY)**2) # srq
print(f"Erro global(soma dos resíduos dos quadrados) vale: {np.round(s, 4)}")
# ---------------------------------------------
plt.figure(figsize=(12,8))
plt.plot(x,y,'o',label="Dados")
plt.plot(x,NovoY,"--",label="Ajuste linear")
plt.title(f"Função para reta p(x) ={str(p).replace('\n', ' ')}") #replace('\n', ' ') remover quebras de linha automátiva
plt.grid(True)
plt.legend()
plt.show()


# %%
