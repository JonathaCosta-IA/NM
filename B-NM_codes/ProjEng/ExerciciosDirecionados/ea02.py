#=========================================================================
# Faça um modelo geral para rebecer dois vetores e calcular:
# (a) a função y = mx + b que melhor se ajusta aos dados, utilizando regressão linear
# por mínimos quadrados
# (b) o erro global, utilizando r2.
#=========================================================================

# (JRC) Adicionalmente:
#  A - Encontre o valor para x aleatório contido no domínio do função.
#  B - Trace um gráfico com a função encontrada e encontre
#=========================================================================
import numpy as np
import random as rd
import matplotlib.pyplot as plt

def CalcCoef(x:list,y:list):
    coef = np.polyfit(x,y,1)
    m=np.round(coef[0],2)
    b=np.round(coef[1],2)
    print(f"A equação descrita pelos coeficientes é:\n y={m}x + {b}")
    return coef


def NovoY(x_novo,coef:np.array):
    return np.polyval(coef,x_novo)


def NovoX(x:list):
    x=np.array(x)
    x_inter = x.min() + rd.random()*10
    if x_inter > x.max():   # Garantindo que o novo X não seja maior que o maior valor de x
        NovoX(x)
    else:
        return x_inter

def CalcErroGlobal(y,y2):
    s = np.sum((y - y2)**2)
    print(f"Erro global vale: {np.round(s, 4)}")


def Graf(x:list,y:list,y2,coef):
    m,b = np.round(coef[0],2) , np.round(coef[1],2)
    plt.figure(figsize=(12,8))
    plt.plot(x,y,'o',label="Dados")
    plt.plot(x,y2,"--",label="Ajuste linear")
    plt.title(f"Função para reta\n y={m}x + {b}")
    plt.grid(True)
    plt.legend()
    plt.show()
# # ---------------------------------------------
x=[2,5,6,8,9,13,15]
y=[7,8,10,11,12,14,15]

coef = CalcCoef(x,y)
x_novo = NovoX(x)  # Gerar um x aleatório contido no intervalo
y_novo = NovoY(x_novo,coef)
y2 = NovoY(x,coef)
CalcErroGlobal(y,y2)
Graf(x,y,y2,coef)
# # ---------------------------------------------

