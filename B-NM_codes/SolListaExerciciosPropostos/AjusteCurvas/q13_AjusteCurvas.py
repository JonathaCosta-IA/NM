# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [1,2,3]
# y = [1,3,2]
#
# - Determinar coeficientes
# - Analisar erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

x = np.array([1,2,3])
y = np.array([1,3,2])

# Ajuste referência
coef_ref = np.polyfit(x,y,2)

# spline simples (mesma ideia anterior)
y_ref = np.polyval(coef_ref, x)

print("Coeficientes referência:", coef_ref)

# Gráfico
x_plot = np.linspace(1,3,200)
plt.figure()
plt.plot(x_plot, np.polyval(coef_ref,x_plot), label='Ajuste quadrático')
plt.scatter(x,y)
plt.grid(True)
plt.legend()
plt.show()