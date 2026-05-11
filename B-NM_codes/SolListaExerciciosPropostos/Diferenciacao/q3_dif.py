
""""
Dada a função $f(x) = e^{-x}$, utilize a fórmula de diferença centrada de segunda ordem para estimar $f'(0)$ com $h = 0{,}05$. 
Analise a ordem do erro de truncamento.

"""

import numpy as np

def f(x):
    # Função basilar f(x) = e (-x)
    return np.exp(-x)

# Parâmetros
x0 = 0.0
h = 0.05

# Diferença centrada de segunda ordem
df_num = (f(x0 + h) - f(x0 - h)) / (2 * h)

# Valor exato
df_exact = -np.exp(-x0)

# Erros
erro_abs = abs(df_num - df_exact)
erro_rel = erro_abs / abs(df_exact)

print(f"Valor exato          : {df_exact:.10f}")
print(f"Aproximação numérica : {df_num:.10f}")
print(f"Erro absoluto        : {erro_abs:.6e}")
print(f"Erro relativo        : {erro_rel:.6e}")

