"""
A função f(x) = sin(x) é avaliada numericamente. 
Utilize a fórmula de três pontos centrada para aproximar 
f''(pi/4) com h = 0,01. 
Compare com o valor analítico da segunda derivada.
"""

import numpy as np

def f(x):
    # Função de interesse
    return np.sin(x)

x = np.pi / 4 # ponto de análise
h = 0.01 # passo


num = (f(x + h) - 2*f(x) + f(x - h)) / (h**2) # Eq. três pontos
df2fx = -np.sin(x)

erro = abs(num - df2fx)

print(f"Exato    = {df2fx:.9f}")
print(f"Numérico = {num:.9f}")
print(f"Erro     = {erro:.3e}")