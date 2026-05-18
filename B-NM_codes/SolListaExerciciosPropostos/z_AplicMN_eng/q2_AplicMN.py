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
df = df.sort_values("area_m2")
x = df.area_m2.to_numpy(dtype=np.float32)
y = df.valor_mil_rs.to_numpy(dtype=np.float32)

# %%
