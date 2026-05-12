"""
Em um ensaio de tração uniaxial de um aço, foram obtidos os seguintes dados experimentais de tensão ($sigma$) 
em função da deformação ($\varepsilon$):

varepsilon & sigma
0.0000 &   0.0 \\
0.0002 &  42.0 \\
0.0004 &  85.0 \\
0.0006 & 128.0 \\
0.0008 & 170.0 \\
0.0010 & 210.0 \\
0.0012 & 250.0 \\
0.0014 & 295.0 \\
0.0016 & 340.0 \\
0.0018 & 380.0 \\
0.0020 & 420.0 \\
0.0022 & 455.0 \\
0.0024 & 485.0 \\
0.0026 & 510.0 \\
0.0028 & 535.0 \\
0.0030 & 555.0 \\

Utilize a fórmula de diferença centrada para estimar numericamente o módulo de elasticidade tangente
 E_i = sigma / varepsilon nos pontos internos da tabela.
Utilize fórmulas de diferença progressiva e regressiva para estimar $E$ nos pontos extremos.
Com base nos valores obtidos, identifique o intervalo de deformação no qual o material apresenta comportamento aproximadamente linear.
Estime o módulo de elasticidade médio $E$ do material na região elástica e compare com o valor típico para o aço ($E \approx 200$ GPa).
Discuta a influência da discretização dos dados na precisão da estimativa de $E$, 
considerando erros de truncamento e possíveis ruídos experimentais.

"""

import numpy as np
import matplotlib.pyplot as plt

epsilon = np.array([
   0.0000, 0.0002, 0.0004, 0.0006, 0.0008,
   0.0010, 0.0012, 0.0014, 0.0016, 0.0018,
   0.0020, 0.0022, 0.0024, 0.0026, 0.0028,
   0.0030])
sigma = np.array([
  0.0,   42.0,   85.0,  128.0,  170.0,
210.0,  250.0,  295.0,  340.0,  380.0,
420.0,  455.0,  485.0,  510.0,  535.0,
555.0])

E=np.zeros_like(sigma)

# Diferença centrada (região interna)
for i in range(1, len(epsilon)-1):
    E[i] = (sigma[i+1] - sigma[i-1]) / (epsilon[i+1] - epsilon[i-1])

# Bordas (baixa ordem)
E[0]  = (sigma[1] - sigma[0]) / (epsilon[1] - epsilon[0])
E[-1] = (sigma[-1] - sigma[-2]) / (epsilon[-1] - epsilon[-2])


# Vetor para módulo tangente
print("Módulo de elasticidade local (GPa).")
[print(f"{E[i] / 1e3 :.3f}") for i in range(len(E))]

tol = 5*1e3
# Estimativa do módulo na região elástica (primeiros pontos)
for i in range(len(E)):
    if (E[i+1] - E[i]) > tol: 
        break
# Média trecho aproximadamente linear
E_medio = np.mean(E[1:i])*1e-3  
print("\nEstimativa de E (média região elástica) =", E_medio, "GPa")
# Vetor para módulo tangente
print("Módulo de elasticidade local (GPa).")
[print(f"{E[i] / 1e3 :.3f}") for i in range(len(E))]

tol = 5*1e3
# Estimativa do módulo na região elástica (primeiros pontos)
for i in range(len(E)):
    if (E[i+1] - E[i]) > tol: 
        break
# Média trecho aproximadamente linear
E_medio = np.mean(E[1:i])*1e-3  
print("\nEstimativa de E (média região elástica) =", E_medio, "GPa")
# Vetor para módulo tangente
print("Módulo de elasticidade local (GPa).")
[print(f"{E[i] / 1e3 :.3f}") for i in range(len(E))]

tol = 5*1e3
# Estimativa do módulo na região elástica (primeiros pontos)
for i in range(len(E)):
    if (E[i+1] - E[i]) > tol: 
        break
# Média trecho aproximadamente linear
E_medio = np.mean(E[1:i])*1e-3  
print("\nEstimativa de E (média região elástica) =", E_medio, "GPa")

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
'''Alternativa no VS code para: não bloquear o terminal 
e aguardar 'n' s antes de fechar os gráficos
        '''
# plt.show(block=False)   
# plt.pause(5)            
# plt.close('all')        
        
# -------------------------------------

