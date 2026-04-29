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


class RegLin():

    def __init__(self,x:list,y:list,graf=0):
            self.x = np.array(x)
            self.y = np.array(y)
            self.coef = np.polyfit(self.x,self.y,1)
            self.y2 = np.polyval(self.coef,self.x)
            self.novo_x = self.NovoX()
            self.novo_y = self.NovoY(self.novo_x)
            self.ExibeCoef()
            self.ErroR2 = self.CalcErroGlobal()
            if graf==1:self.Graf()

    def CalcErroGlobal(self):
        # Soma dos resíduos dos quadrados:o quanto o modelo errou em cada ponto.
        SomaResiduosQuadrados = np.sum((self.y - self.y2)**2)
        # Soma dos quadrados totais: o quanto os dados variam em torno da própria média, sem nenhum modelo.
        SomaDesvQuadrados = np.sum((self.y - np.mean(self.y))**2)
        r2  = 1 - SomaResiduosQuadrados / SomaDesvQuadrados
        print(f"Erro global é {round(r2,2)}")
        return r2

    def NovoX(self):
        x_inter = self.x.min() + rd.random()*10
        if x_inter > self.x.max():   # Garantindo que o novo X não seja maior que o maior valor de x
            self.NovoX()
        else:
            return x_inter

    def NovoY(self,x_novo):
        return np.polyval(self.coef,x_novo)

    def ExibeCoef(self):
        m=np.round(self.coef[0],2)
        b=np.round(self.coef[1],2)
        print(f"A equação descrita pelos coeficientes é:\n y={m}x + {b}")

    def Graf(self):
        m,b = np.round(self.coef[0],2) , np.round(self.coef[1],2)
        plt.figure(figsize=(12,8))
        plt.plot(self.x,self.y,'o',label="Dados")
        plt.plot(self.x,self.y2,"--",label="Ajuste linear")
        plt.plot(self.novo_x,self.novo_y,"*r",label = "Ponto interpolado com p(x)", markersize=12)
        plt.title(f"Função para reta\n y={m}x + {b} com r2={round(self.ErroR2,2)}")
        plt.grid(True)
        plt.legend()
        plt.show()
# # ---------------------------------------------


