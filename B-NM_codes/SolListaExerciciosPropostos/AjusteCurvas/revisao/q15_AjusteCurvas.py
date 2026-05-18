# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# x = [1,2,3,4]
# y = [2,3,5,4]
#
# - Spline cúbico natural
# - Erro
# - Gráfico
# --------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([1,2,3,4])
y = np.array([2,3,5,4])

cs = CubicSpline(x,y, bc_type='natural')

x_plot = np.linspace(1,4,200)
y_plot = cs(x_plot)

plt.figure()
plt.plot(x_plot, y_plot, label='Spline cúbico')
plt.scatter(x,y)
plt.grid(True)
plt.legend()
plt.show()