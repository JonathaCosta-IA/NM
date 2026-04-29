
# Q5.3
"""
Ano = [1850,1900,1950,1980,2000]
População = [1.3, 1.6, 3, 4.4, 6]

Assuma que o crescimento da população possa ser modelado por uma mx 
função exponencial p = be^(mx), onde x é o ano e p é a população em bilhões.
Linearize essa função (Seção 5.3) e use a regressão linear por mínimos qua-
drados para determinar as constantes b e m para as quais a função fornece o
melhor ajuste para os dados. Use essa equação para estimar a população em
1970.
"""

"""
Linearização de p=be^(mx) 

    Aplicando ln (p) = ln (be^(mx)) =>
              ln p = mx + ln b  =>
                Y  = mx +  B

Fazendo  Y = ln p e B = ln b, tal que Y=mx+B, em que:

m = coeficiente angular (mesmo da exponencial)
b = e^B = coeficiente linear recuperado após a regressão
"""


import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Dados
# -----------------------------------------------------------
x = np.array([1850, 1900, 1950, 1980, 2000])
p = np.array([1.3,  1.6,  3.0,  4.4,  6.0])

# -----------------------------------------------------------
# Linearização de p=be^(mx) 
#        ln(p) = mx + ln(b)  →  Y = mx + B
# -----------------------------------------------------------
Y = np.log(p)                          # variável linearizada
coef = np.polyfit(x, Y, 1)             # regressão linear em [x, ln(p)]
m  = coef[0]
B  = coef[1]
b  = np.exp(B)                         # recupera b = e^B

print(f"Coeficientes encontrados:")
print(f"  m = {m:.6f}")
print(f"  b = {b:.6e}")
print(f"\nModelo: p = {b:.4e} * e^({m:.6f} * x)")

# -----------------------------------------------------------
# Estimativa para 1970
# -----------------------------------------------------------
x_est = 1970
p_est = b * np.exp(m * x_est)
print(f"\nEstimativa para {x_est}: p = {p_est:.3f} bilhões")

# -----------------------------------------------------------
# Erro global (SSR no espaço linearizado)
# -----------------------------------------------------------
Y2  = np.polyval(coef, x)
# Soma dos resíduos dos quadrados:o quanto o modelo errou em cada ponto.
ssr = np.sum((Y - Y2)**2)
# Soma dos quadrados totais: o quanto os dados variam em torno da própria média, sem nenhum modelo.
ss_tot = np.sum((Y - np.mean(Y))**2)
r2  = 1 - ssr / ss_tot
print(f"\nR² (espaço linearizado) = {r2:.6f}")

# -----------------------------------------------------------
# Gráfico
# -----------------------------------------------------------
x_cont = np.linspace(1840, 2010, 500)
p_cont = b * np.exp(m * x_cont)

plt.figure(figsize=(10, 6))
plt.plot(x, p, 'o', markersize=8, label="Dados originais")
plt.plot(x_cont, p_cont, '--', label=f"$p = {b:.3e}\\,e^{{{m:.5f}x}}$")
plt.plot(x_est, p_est, '*r', markersize=12,
         label=f"Estimativa 1970: {p_est:.3f} bi")

plt.xlabel("Ano")
plt.ylabel("População (bilhões)")
plt.title("Ajuste exponencial — Crescimento populacional")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()