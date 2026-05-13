#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

"""
Considere a função:

f(x) = 1 / (1 + x^2), no intervalo [0,1]

1) Calcule a integral utilizando:
   - Método do trapézio composto
   - Método de Simpson 1/3

2) Utilize n = 2^k, com k = 1, 2, ..., 6

3) Construa um gráfico em escala log-log do erro em função do passo h

4) Estime numericamente a ordem de convergência de cada método
"""

# Função
f = lambda x: 1/(1 + x**2)
a, b = 0, 1
I_exato = np.pi / 4

# Métodos
def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    return h * (0.5*y[0] + np.sum(y[1:-1]) + 0.5*y[-1])

def simpson_1_3(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n deve ser par")
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    S = y[0] + y[-1]
    S += 4 * np.sum(y[1:-1:2])
    S += 2 * np.sum(y[2:-2:2])
    return (h/3) * S

# Refinamento
ks = np.arange(1, 7)
ns = 2**ks

h_vals = []
erro_trap = []
erro_simp = []

for n in ns:
    h = (b - a) / n
    I_trap = trapezio_composto(f, a, b, n)
    I_simp = simpson_1_3(f, a, b, n)

    h_vals.append(h)
    erro_trap.append(abs(I_trap - I_exato))
    erro_simp.append(abs(I_simp - I_exato))

h_vals = np.array(h_vals)
erro_trap = np.array(erro_trap)
erro_simp = np.array(erro_simp)

# --------- GRÁFICO EM ESCALA NATURAL ---------
plt.figure()
plt.plot(h_vals, erro_trap, marker='o', label='Trapézio')
plt.plot(h_vals, erro_simp, marker='s', label='Simpson 1/3')
plt.xlabel('h')
plt.ylabel('Erro absoluto')
plt.title('Escala natural')
plt.legend()
plt.grid()
plt.show()

# --------- GRÁFICO LOG-LOG ---------
plt.figure()
plt.loglog(h_vals, erro_trap, marker='o', label='Trapézio')
plt.loglog(h_vals, erro_simp, marker='s', label='Simpson 1/3')
plt.xlabel('h')
plt.ylabel('Erro absoluto')
plt.title('Escala log-log')
plt.legend()
plt.grid()
plt.show()