'''
Implemente o método do trapézio composto e utilize-o para aproximar a integral:

    \int_{0}^{1} e^x \, dx

Considere os valores n = 4, 8, 16, 32, 48 subintervalos. 
Apresente os resultados em forma de tabela e analise a convergência do método.

'''


import numpy as np

def trapezio_composto(f, a, b, n):
    ''' 
    Método do trapézio composto
    '''
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        soma += f(a + i*h)
    
    return h * soma

f = lambda x: np.exp(x)
# Primitiva calculada manualmente
exato = np.e - 1
dados = []

# Resultados
# ================================
# Particionamento: 4, 8, 16, 32, 48
for n in [4, 8, 16, 32, 48]:
    aprox = trapezio_composto(f, 0, 1, n)
    erro = abs(exato - aprox)
    dados.append((n, aprox, erro))

# Cabeçalho
print(f"{'n':>5} | {'aprox':>12} | {'erro':>12}")
print("-"*36)
# Linhas
for n, aprox, erro in dados:
    print(f"{n:5d} | {aprox:12.6f} | {erro:12.6e}")