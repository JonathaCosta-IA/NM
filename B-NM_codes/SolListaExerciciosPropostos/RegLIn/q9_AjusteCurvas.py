# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [1,2,4]
# y = [2,3,7]
#
# - Interpolação de Newton
# - Estimar f(1.5)
# --------------------------------------------------------

import numpy as np

# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([1,2,4], dtype=float)
y = np.array([2,3,7], dtype=float)

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
# Avaliação
# ---------------------------------------------
def newton(x, table, xp):
    n = len(x)
    result = table[0][0]
    prod = 1
    for i in range(1,n):
        prod *= (xp - x[i-1])
        result += table[0][i]*prod
    return result

xp = 1.5
yp = newton(x, table, xp)

# ---------------------------------------------
# Resultado
# ---------------------------------------------
print(f"f(1.5) ≈ {yp:.6f}")