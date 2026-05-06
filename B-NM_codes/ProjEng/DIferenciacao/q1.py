import numpy as np

def f(x):
    return np.log(x)

x = 1.0
h = 0.1

num = (f(x + h) - f(x)) / h
exact = 1 / x
erro = abs(num - exact)

print("Ex1:")
print("Numérico =", num)
print("Exato    =", exact)
print("Erro     =", erro)