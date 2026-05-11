"""
Considere a função $f(x) = x^3 - 2x + 1$. 
Utilize:
     diferença progressiva,
     diferença regressiva,
     diferença centrada,
para estimar f(2) com h = 0,1. 
Compare os resultados e identifique qual método apresenta menor erro.
"""

import numpy as np

def f(x):
    # Função proposta
    return x**3 - 2*x + 1

x = 2.0
h = 0.1

prog = (f(x + h) - f(x)) / h
reg  = (f(x) - f(x - h)) / h
cent = (f(x + h) - f(x - h)) / (2*h)

dfdx = 3*x**2 - 2

print("Exato       =", dfdx)
print(f"Progressiva = {prog} | Erro = {abs(prog - dfdx):6f}")
print(f"Regressiva  = {reg}  | Erro = {abs(reg  - dfdx):6f}")
print(F"Centrada    = {cent} | Erro = {abs(cent - dfdx):6f}")