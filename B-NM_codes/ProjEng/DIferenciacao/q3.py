import numpy as np

x = np.array([1.0, 1.1, 1.2])
f = np.array([2.7183, 3.0042, 3.3201])

h = 0.1

num = (f[2] - f[1]) / h

print("\nEx3:")
print("Derivada aproximada em x=1.2 =", num)