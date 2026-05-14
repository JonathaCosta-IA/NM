"""
Ajuste, pelo método dos mínimos quadrados, um modelo linear aos dados apresentados e 
determine o coeficiente de determinação R². 
Analize a qualidade do ajuste obtido.

x=[0,1,2,3,4]
y=[1.1,2,2.9,4.2,4.8]

- Produza um $novoY$ a partir da reta gerada.
- Calcule o erro quadrático total.
- Encontre o valor de y para um delta | delta está contido em x.
- Trace o gráfico com:  x por y , x por novoY. 
"""
# --------------------------------------------------------
# Solução proposta com funções(métodos)
# --------------------------------------------------------

import numpy as np
import random as rd
import matplotlib.pyplot as plt

def CalcCoef(x:list,y:list):
    """
    Método para calcular os coefientes para dois vetores (x,y)
    """
    coef = np.polyfit(x,y,1)
    m=np.round(coef[0],2)
    b=np.round(coef[1],2)
    print(f"A equação descrita pelos coeficientes é:\n y={m}x + {b}")
    return coef


def NovoY(x_novo,coef:np.array):
    """
    Método para gerar um novo Y, recebendo (f(x) e x)
    """
    return np.polyval(coef,x_novo)


def NovoX(x:list):
    """
    Método utilizado para gerar um x randomico dentro do domínio de X
    """
    rd.seed(rd.random())
    x=np.array(x)
    x_inter = x.min() + rd.random()*10
    if x_inter > x.max():   # Garantindo que o novo X não seja maior que o maior valor de x
        return NovoX(x)
    else:
        return x_inter

def CalcErroGlobal(y,y2):
    """
    Método utilizado para calcular o erro relativo r²
    """
    # Soma dos resíduos dos quadrados
    # Isto representa quanto o modelo errou em cada ponto.
    SomaResiduosQuadrados = np.sum((y - y2)**2)

    # Soma dos quadrados totais
    # Isto representa o quanto os dados variam em torno da própria média,
    # sem nenhum modelo, desvio.
    SomaDesvQuadrados = np.sum((y - np.mean(y))**2)
    
    r2  = 1 - SomaResiduosQuadrados / SomaDesvQuadrados
    print(f"Erro global é {round(r2,2)}")

    return r2

def Graf(x:list,y:list,y2,coef,r2,ponto=None):
    m,b = np.round(coef[0],2) , np.round(coef[1],2)
    plt.figure(figsize=(12,8))
    plt.plot(x,y,'o',label="Dados")
    plt.plot(x,y2,"--",label="Ajuste linear")
    if  ponto is not None:
        x_novo,y_novo = ponto
        plt.plot(x_novo,y_novo,"ro",markersize=12,label="Ponto aleatório")
    
    plt.title(f"Função para reta\n y={m}x + {b}\n Erro global r²={round(r2,3)}")
    plt.grid(True)
    plt.legend()
    plt.show()
# # ---------------------------------------------
x=[0,1,2,3,4]
y=[1.1,2,2.9,4.2,4.8]

coef = CalcCoef(x,y)
x_novo = NovoX(x)  # Gerar um x aleatório contido no intervalo
y_novo = NovoY(x_novo,coef)
print(f"\nO valor aleatório de x no domínio X é {round(x_novo,4)}.\nO valor f({round(x_novo,4)}) = {round(y_novo,4)}.")
y2 = NovoY(x,coef)
r2=CalcErroGlobal(y,y2)
Graf(x,y,y2,coef,r2,(x_novo,y_novo))
# # ---------------------------------------------

"""
COMENTÁRIOS

Graf(x,y,y2,coef,r2,(x_novo,y_novo))
Arranjo ponto=(x_novo,y_novo) visa apenas permitir o uso do método sem passar o par (x,y).
O que pode ser estruturado com:
Chamada: Graf(x,y,y2,coef,r2,x_novo,y_novo)
Definição: 
 def Graf(x:list,y:list,y2,coef,r2,x_novo=None,y_novo=None):
.
.
.
    if  (x_novo and  y_novo) is not None:
    ...

"""
