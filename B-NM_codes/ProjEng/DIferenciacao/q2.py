import numpy as np

def f(x):
    return np.exp(-x)

x = 0.0
h = 0.05

num = (f(x + h) - f(x - h)) / (2*h)
exact = -np.exp(-x)
erro = abs(num - exact)

print("\nEx2:")
print("Numérico =", num)
print("Exato    =", exact)
print("Erro     =", erro)