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
# Resumo
# A tabela existe para:
# organizar diferenças divididas;
# extrair coeficientes;
# montar o polinômio interpolador de Newton.
# É um processo sistemático para evitar resolver sistema linear.
# ---------------------------------------------
n = len(x)
table = np.zeros((n,n))
table[:,0] = y

for j in range(1,n):
    for i in range(n-j):
        table[i,j] = (table[i+1,j-1] - table[i,j-1])/(x[i+j] - x[i])

# ---------------------------------------------
# Polinômio
# ---------------------------------------------
p = np.poly1d([table[0,0]])
termo = np.poly1d([1])

for i in range(1,n):
    termo *= np.poly1d([1,-x[i-1]])
    p += table[0,i]*termo

# ---------------------------------------------
# Saída
# ---------------------------------------------
print("Tabela:")
print(table)

print("\nPolinômio:")
print(p)