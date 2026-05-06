import numpy as np

def f(x):
    return x**3 - 2*x + 1

x = 2.0
h = 0.1

prog = (f(x + h) - f(x)) / h
reg  = (f(x) - f(x - h)) / h
cent = (f(x + h) - f(x - h)) / (2*h)

exact = 3*x**2 - 2

print("\nEx4:")
print("Progressiva =", prog, "Erro =", abs(prog - exact))
print("Regressiva  =", reg,  "Erro =", abs(reg  - exact))
print("Centrada    =", cent, "Erro =", abs(cent - exact))
print("Exato       =", exact)