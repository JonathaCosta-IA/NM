#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

"""
Para a integral:

∫₀^π sin(x) dx

Implemente e compare os seguintes métodos:
- Método do ponto médio
- Método do trapézio
- Método de Simpson 1/3

Utilize n = 4, 10, 50 subintervalos.
Construa um gráfico do erro absoluto em função de n e discuta os resultados.
"""

# Métodos numéricos
def ponto_medio(f, a, b, n):
    h = (b - a) / n
    x = a + h*(np.arange(n) + 0.5)
    return h * np.sum(f(x))

def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])

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

# Função e valor exato
f = np.sin
a, b = 0, np.pi
I_exato = 2.0

# Valores de n
ns = [4, 10, 50]

# Armazenamento de erros
erro_pm = []
erro_trap = []
erro_simp = []

col1 = 20

for n in ns:
    I_pm = ponto_medio(f, a, b, n)
    I_trap = trapezio_composto(f, a, b, n)
    I_simp = simpson_1_3(f, a, b, n if n % 2 == 0 else n+1)

    e_pm = abs(I_pm - I_exato)
    e_trap = abs(I_trap - I_exato)
    e_simp = abs(I_simp - I_exato)

    erro_pm.append(e_pm)
    erro_trap.append(e_trap)
    erro_simp.append(e_simp)

    print(f"\n--- n = {n} ---")
    print(f"{'Métrica':<{col1}} | {'Valor':>{col1}}")
    print("-" * (col1*2 + 3))
    print(f"{'Ponto médio':<{col1}} | {I_pm:>{col1}.10f}")
    print(f"{'Trapézio':<{col1}} | {I_trap:>{col1}.10f}")
    print(f"{'Simpson 1/3':<{col1}} | {I_simp:>{col1}.10f}")
    print(f"{'Exato':<{col1}} | {I_exato:>{col1}.10f}")
    print(f"{'Erro Ponto Médio':<{col1}} | {e_pm:>{col1}.10e}")
    print(f"{'Erro Trapézio':<{col1}} | {e_trap:>{col1}.10e}")
    print(f"{'Erro Simpson':<{col1}} | {e_simp:>{col1}.10e}")

# Gráfico do erro
plt.figure()
plt.plot(ns, erro_pm, marker='o', label='Ponto Médio')
plt.plot(ns, erro_trap, marker='s', label='Trapézio')
plt.plot(ns, erro_simp, marker='^', label='Simpson 1/3')
plt.xlabel('n')
plt.ylabel('Erro absoluto')
plt.title('Erro absoluto vs n')
plt.legend()
plt.grid()
plt.show()

