"""
Questão proposta
Considere a função $f(x) = x^3$. Calcule numericamente a derivada primeira no ponto $x = 3$
 aplicando as fórmulas de diferenças finitas progressiva, regressiva e central, utilizando:
\begin{itemize}
    \item os pontos x = 2, x = 3 e x = 4.
    \item os pontos x = 2,75, x = 3 e x = 3,25.
\end{itemize} 
Compare os resultados com a derivada exata (analítica) e expresse os erros relativo e absoluto.

"""

import numpy as np

def f(x):
    # Função basica
    return x**3

def derivada_exata(x):
    # Derivada calculada manualmente
    return 3*x**2

def diferenca_progressiva(f, x, h):
    ''' Equação básica da diferença progressiva'''
    return (f(x + h) - f(x)) / h

def diferenca_regressiva(f, x, h):
    # Equação básica da diferença regressiva
    return (f(x) - f(x - h)) / h

def diferenca_central(f, x, h):
    # Equação básica da diferença central
    return (f(x + h) - f(x - h)) / (2*h)

def erros(aprox, exato):
    # Erros no sistema
    erro_abs = abs(aprox - exato)
    erro_rel = erro_abs / abs(exato)
    return erro_abs, erro_rel

def analisar_conjunto(x, h):
    exato = derivada_exata(x) # Retorno em tupla

    prog = diferenca_progressiva(f, x, h)
    reg  = diferenca_regressiva(f, x, h)
    cent = diferenca_central(f, x, h)

    print(f"\n{'-'*10}\n h = {h}\n{'-'*10}")
    print(f"Valor exato: {exato:.6f}")

    for nome, val in [("Progressiva", prog), ("Regressiva", reg), ("Central", cent)]:
        ea, er = erros(val, exato)
        print(f"{nome:<12} {val:<10.6f} | erro abs = {ea:<10.3e} | erro rel = {er:<10.3e}")
# Ponto de interesse
x0 = 3

# Conjunto 1: x = 2, 3, 4  → h = 1
analisar_conjunto(x0, h=1)

# Conjunto 2: x = 2.75, 3, 3.25 → h = 0.25
analisar_conjunto(x0, h=0.25)