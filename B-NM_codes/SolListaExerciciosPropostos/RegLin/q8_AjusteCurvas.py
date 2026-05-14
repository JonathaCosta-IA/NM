# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [1,2,3]
# y = [1,8,27]
#
# - Construir tabela
# - Determinar polinômio
# --------------------------------------------------------

import numpy as np

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([1,2,3], dtype=float)
y = np.array([1,8,27], dtype=float)

# ---------------------------------------------
# Diferenças divididas
# ---------------------------------------------
n = len(x)
table = np.zeros((n,n))
table[:,0] = y

for j in range(1,n):
    for i in range(n-j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1])/(x[i+j] - x[i])

# ---------------------------------------------
# Resultados
# ---------------------------------------------
print("Tabela de diferenças:")
print(table)

print("\nCoeficientes do polinômio:")
for i in range(n):
    print(f"a{i} = {table[0][i]:.6f}")