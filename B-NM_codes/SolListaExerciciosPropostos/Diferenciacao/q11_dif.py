'''
 Problema: Análise de dados experimentais de um sistema elétrico
Dados fornecidos:
 - Vetores discretos de tempo t (s), tensão V (V) e corrente I (A)
Solicitado: 
 1) Calcular a potência instantânea: P(t) = V(t) * I(t)
 2) Estimar numericamente a derivada dP/dt usando:
    - Diferença progressiva
    - Diferença regressiva
    - Diferença centrada
 3) Comparar os métodos quanto à precisão e uso nas extremidades
 4) Construir gráficos:
    - V(t), I(t), P(t)
    - Comparação das derivadas dP/dt
 5) Identificar:
    - Maior aumento de potência
    - Maior queda de potência
 6) Interpretar o comportamento dinâmico da carga (transientes)
 7) Discutir a influência do passo de amostragem (Δt)

'''

import numpy as np
import matplotlib.pyplot as plt

class AnaliseEletrica():
    
    def __init__(self,
                 t = np.array([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,
                               5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]),
                 V = np.array([220.000,220.495,220.958,221.363,221.683,221.898,221.995,
                               221.968,221.818,221.556,221.197,220.763,220.282,219.784,
                               219.298,218.856,218.486,218.212,218.045,217.990,218.082]),
                 I = np.array([0.52,0.61,0.68,0.74,0.79,0.76,0.70,0.99,1.49,0.36,
                               0.28,0.19,1.14,1.15,0.18,1.27,0.38,0.47,0.59,0.71,0.78])
                 ):
        self.t = t
        self.U = V
        self.I = I
        self.dP_prog=np.array([])
        self.dP_reg=np.array([])
        self.dP_cent=np.array([])
        
        self.P = self.U * self.I
        
        self.CalcDerivadas()
        self.Graficos()
        
    def CalcDerivadas(self):
        # Passo das
        dt = 0.5
        # Derivadas
        self.dP_prog = (self.P[1:] - self.P[:-1]) / dt
        self.dP_reg  = (self.P[1:] - self.P[:-1]) / dt
        self.dP_cent = (self.P[2:] - self.P[:-2]) / (2*dt)
        
        
        
    def Graficos(self):
        # Gráficos
        series = [self.U, self.I, self.P]
        titulos = ["Tensão", "Corrente", "Potência","Derivadas"]
        cores  = ['r--', 'b', 'g']
        
        for i,(y,cor,titulo) in enumerate(zip(series,
                                              cores,
                                              titulos),start=1):
            plt.subplot(2,2,i)
            plt.plot(self.t, y, cor, label=titulo)
            plt.title(titulo)
            plt.legend()
            plt.grid(True)
        
        plt.subplot(2,2,4)
        plt.plot(self.t[:-1], self.dP_prog, 'r-', label="Progressiva")
        plt.plot(self.t[1:],  self.dP_reg,  'b--', label="Regressiva")
        plt.plot(self.t[1:-1], self.dP_cent,'g-.', label="Centrada")
        plt.title("Derivadas")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()


# ------------------------------------------------------
'''
Importe ou informe um conjunto de dados de mesma dimensão:
t(s), U(V), i (A)
'''

a=AnaliseEletrica()
