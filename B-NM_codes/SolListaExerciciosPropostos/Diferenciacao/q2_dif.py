"""
Considere a função $f(x) = ln(x)$. 
Utilize a fórmula de diferença progressiva de primeira ordem para aproximar $f'(1)$ com $h = 0{,}1$. 
Compare com o valor exato da derivada e calcule o erro absoluto.
"""


import numpy as np

def f(x):
    # Função f(x)
    return np.log(x)

x = 1.0
h = 0.1

#Aproximação de df/dx para x=1, com h=0.1
dfdx = (f(x + h) - f(x)) / h
exact = 1 / x
#Erro da aproximação
erro = abs(dfdx - exact)

print(f"Numérico = {dfdx:.6f}")
print(f"Exato    = {exact:.6f}")
print(f"Erro     = {erro:.6e}")

'''
Note que:
Valor exato a partir da derivação manual
f(x) = ln x
f'(x) = 1/x
'''