"""
 --------------------------------------------------------
# ENUNCIADO
Considere os dados da questão anterior.
Calcule o polinômio de interpolação $p(x)$ utilizando Lagrange.
Calcule o polinômio de interpolação $p(x)$ utilizando Newton.   
Calcule o polinômio de interpolação $p(x)$ utilizando regressão linear.
Calcule o polinômio de interpolação $p(x)$ utilizando regressão polinomial com graus(2,3,4).
Compare erro e custo computacional para um ponto de teste t=50.
# --------------------------------------------------------

"""
#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arquivo = "https://raw.githubusercontent.com/JonathaCosta-IA/NM/refs/heads/main/B-NM_codes/SolListaExerciciosPropostos/z_AplicMN_eng/MercadoImobil.csv"
df = pd.read_csv(arquivo)
y= df['x'].values

#------------------------------
#Erros
#------------------------------

def erro_absoluto(real, aprox):
    return np.abs(real - aprox)

#------------------------------
#p(x) via Lagrange
#------------------------------

def lagrange(x, y, xp):
    n = len(x)
    yp = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*L
    return yp




