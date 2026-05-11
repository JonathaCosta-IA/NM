import numpy as np
import matplotlib.pyplot as plt

def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        soma += f(a + i*h)
    
    return h * soma

def simpson_13(f, a, b, n):
    if n % 2 != 0:
        raise ValueError("n deve ser par")
    
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * f(a + i*h)
        else:
            soma += 4 * f(a + i*h)
    
    return h * soma / 3

def ponto_medio(f, a, b, n):
    h = (b - a) / n
    soma = 0
    
    for i in range(n):
        xi = a + (i + 0.5)*h
        soma += f(xi)
    
    return h * soma

f = np.sin
exato = 2.0  # ∫₀^π sin(x)dx = 2

ns = [4, 10, 50]

erros_mid = []
erros_trap = []
erros_simp = []

print("\nQ4:")

col=10
formate = f"<{10}.6f"

print(f"{'Métrica':<{col+4}} | {'Valor':>{col*2}}\n")

for n in ns:
    mid = ponto_medio(f, 0, np.pi, n)
    trap = trapezio_composto(f, 0, np.pi, n)
    simp = simpson_13(f, 0, np.pi, n if n % 2 == 0 else n+1)
    
    erros_mid.append(abs(exato - mid))
    erros_trap.append(abs(exato - trap))
    erros_simp.append(abs(exato - simp))
    
    print(f"n = {round(n,1):<{10}} | mid={mid:{formate}} | trap={trap:{formate}} | simp={simp:{formate}}")

    

# Gráfico
plt.plot(ns, erros_mid, 'o-', label="Ponto Médio")
plt.plot(ns, erros_trap, 's-', label="Trapézio")
plt.plot(ns, erros_simp, '^-', label="Simpson")
plt.xlabel("n")
plt.ylabel("Erro absoluto")
plt.legend()
plt.grid()
plt.show()