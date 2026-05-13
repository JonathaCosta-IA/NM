#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

"""
Implemente o método de Simpson 1/3, garantindo que o número de subintervalos n seja par.
Utilize o método para calcular:

∫₀² ln(x+1) dx

Compare os resultados com aqueles obtidos pelo método do trapézio composto
utilizando o mesmo número de subintervalos.
"""

def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n deve ser par para Simpson 1/3")
    
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    S = y[0] + y[-1]
    S += 4 * np.sum(y[1:-1:2])
    S += 2 * np.sum(y[2:-2:2])
    
    return (h/3) * S


def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    
    return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])


# Função
f = lambda x: np.log(x + 1)

# Intervalo e discretização
a, b = 0, 2
n = 10  # par

# Cálculos
I_simpson = simpson_1_3(f, a, b, n)
I_trap = trapezio_composto(f, a, b, n)

# Valor exato
I_exato = 3*np.log(3) - 2

# Saída padronizada
col1 = 20

print(f"{'Métrica':<{col1}} | {'Valor':>{col1}}")
print("-" * (col1*2 + 3))

print(f"{'Simpson 1/3':<{col1}} | {I_simpson:>{col1}.10f}")
print(f"{'Trapézio':<{col1}} | {I_trap:>{col1}.10f}")
print(f"{'Exato':<{col1}} | {I_exato:>{col1}.10f}")
print(f"{'Erro Simpson':<{col1}} | {abs(I_simpson - I_exato):>{col1}.10e}")
print(f"{'Erro Trapézio':<{col1}} | {abs(I_trap - I_exato):>{col1}.10e}")