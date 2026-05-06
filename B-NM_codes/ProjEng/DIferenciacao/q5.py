import numpy as np

def f(x):
    return np.sin(x)

x = np.pi / 4
h = 0.01

num = (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
exact = -np.sin(x)

erro = abs(num - exact)

print("\nEx5:")
print("Numérico =", num)
print("Exato    =", exact)
print("Erro     =", erro)