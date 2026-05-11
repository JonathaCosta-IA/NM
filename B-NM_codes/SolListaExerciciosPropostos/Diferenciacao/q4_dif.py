"""
A tabela abaixo fornece valores experimentais de uma função:

  x & f(x) \\
1,0 & 2,7183 \\
1,1 & 3,0042 \\
1,2 & 3,3201 \\

Utilize a fórmula de diferença regressiva para estimar $f'(1,2)$.

"""


import numpy as np

x = np.array([1.0, 1.1, 1.2])
f = np.array([2.7183, 3.0042, 3.3201])

h = 0.1

num = (f[2] - f[1]) / h

print("Derivada experimental em x=1.2 =",f[-1])
print("Derivada aproximada em x=1.2 =", num)
print(f"Erro absoluto {abs(num-f[-1]):.3f}")