import numpy as np
import matplotlib.pyplot as plt

# Deformação (ε) mais densa
epsilon = np.array([
    0.0000, 0.0002, 0.0004, 0.0006, 0.0008,
    0.0010, 0.0012, 0.0014, 0.0016, 0.0018,
    0.0020, 0.0022, 0.0024, 0.0026, 0.0028,
    0.0030
])

# Tensão (σ) em MPa (dados de medição simulados com leve não linearidade)
sigma = np.array([
      0.0,   42.0,   85.0,  128.0,  170.0,
    210.0,  250.0,  295.0,  340.0,  380.0,
    420.0,  455.0,  485.0,  510.0,  535.0,
    555.0
])
# Vetor para módulo tangente
E = np.zeros_like(epsilon) # ou E=np.zeros(len(epsilon))

# Diferença centrada (região interna)
for i in range(1, len(epsilon)-1):
    E[i] = (sigma[i+1] - sigma[i-1]) / (epsilon[i+1] - epsilon[i-1])

# Bordas (baixa ordem)
E[0]  = (sigma[1] - sigma[0]) / (epsilon[1] - epsilon[0])
E[-1] = (sigma[-1] - sigma[-2]) / (epsilon[-1] - epsilon[-2])

print("Módulo de elasticidade local (MPa):")
print(E)

# Estimativa do módulo na região elástica (primeiros pontos)
E_medio = np.mean(E[1:6])*1e-3  # trecho aproximadamente linear
print("\nEstimativa de E (região elástica) =", E_medio, "GPa")

# Gráficos
plt.figure()
plt.plot(epsilon, sigma, 'o-', label="Curva σ-ε")
plt.xlabel("Deformação (ε)")
plt.ylabel("Tensão (MPa)")
plt.grid()
plt.legend()
plt.title("Tensão x deformação da amostra")
plt.savefig("DeformacaoTensao.png")

plt.figure()
plt.plot(epsilon, E, 'o-', label="Módulo tangente (MPa)")
plt.xlabel("Deformação (ε)")
plt.ylabel("E (MPa)")
plt.grid()
plt.legend()
plt.title("Deformação x  Módulo de elasticidade da amostra")
plt.savefig("DeformacaoModuloElasticidade.png")


# plt.show(block=False)   # NÃO bloqueia
# plt.pause(10)           # mantém aberto por 'n' s
# plt.close('all')        # Fecha as figuras