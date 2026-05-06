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

f = lambda x: 1/(1 + x**2)

# Valor exato: arctan(1) = π/4
exato = np.pi / 4

ns = [2**k for k in range(1, 7)]
h_vals = []
erro_trap = []
erro_simp = []


print("\nQ5:")
for n in ns:
    h = 1/n
    h_vals.append(h)
    
    trap = trapezio_composto(f, 0, 1, n)
    simp = simpson_13(f, 0, 1, n if n % 2 == 0 else n+1)
    
    erro_trap.append(abs(exato - trap))
    erro_simp.append(abs(exato - simp))
    
    print(f"n={n:<5} | erro_trap={erro_trap[-1]:<10.6e} | erro_simp={erro_simp[-1]:<10.6e}")

# Gráfico log-log
plt.loglog(h_vals, erro_trap, 'o-', label="Trapézio")
plt.loglog(h_vals, erro_simp, 's-', label="Simpson")
plt.xlabel("h")
plt.ylabel("Erro")
plt.legend()
plt.grid()
plt.show()

# Estimativa da ordem (inclinação)
ordem_trap = np.polyfit(np.log(h_vals), np.log(erro_trap), 1)[0]
ordem_simp = np.polyfit(np.log(h_vals), np.log(erro_simp), 1)[0]

print("\nOrdem estimada:")
print("Trapézio ~", ordem_trap)
print("Simpson ~", ordem_simp)