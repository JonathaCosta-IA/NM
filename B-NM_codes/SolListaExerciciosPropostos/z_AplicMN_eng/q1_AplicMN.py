# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# - Converter os valores para IEEE 754 (float32).
# - Calcular o erro absoluto e relativo médio.
# - Avaliar o impacto no somatório total.
# --------------------------------------------------------

"""
# --- NOTA SOBRE PRECISÃO DE PONTO FLUTUANTE ---
# A precisão (dígitos decimais confiáveis) é calculada por: bits * log10(2)
#
# Float32 (Precisão Simples):
#   - 24 bits efetivos (23 mantissa + 1 implícito)
#   - 24 * 0.301 ≈ 7.22 -> ~7 dígitos confiáveis.
#
# Float64 (Precisão Dupla - Padrão do Python):
#   - 53 bits efetivos (52 mantissa + 1 implícito)
#   - 53 * 0.301 ≈ 15.95 -> ~15 a 16 dígitos confiáveis.
#
# CONCLUSÃO: Float32 ≈ 7 dígitos | Float64 ≈ 16 dígitos.
# Obs: Mais dígitos impressos não garantem maior precisão real.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------
# Dados
# ---------------------------------------------
df = pd.read_csv("dados.csv")
x = pd.to_numeric(df["x"], errors="coerce").to_numpy(dtype=np.float64)

x32 = x.astype(np.float32)              # IEEE 754 (32 bits)
# ---------------------------------------------
# 1) Cálculo dos erros
# ---------------------------------------------
erro_abs = np.abs(x - x32)
erro_rel = np.abs((x - x32) / np.where(x != 0, x, 1))

erro_abs_medio = np.mean(erro_abs)
erro_rel_medio = np.mean(erro_rel)

print("Erro absoluto médio:", erro_abs_medio)
print("Erro relativo médio:", erro_rel_medio)

# ---------------------------------------------
# 2) Impacto no somatório
# ---------------------------------------------
soma64 = np.sum(x)
soma32 = np.sum(x32)

erro_soma_abs = np.abs(soma64 - soma32)
erro_soma_rel = erro_soma_abs / soma64

print("\nSoma (float64):", soma64)
print("Soma (float32):", soma32)

print("\nErro absoluto na soma:", erro_soma_abs)
print("Erro relativo na soma:", erro_soma_rel)

# ---------------------------------------------
# 3) Diagnóstico ponto a ponto
# ---------------------------------------------
col=10
print("\nErro absoluto por ponto (primeiros 10):")
for i in range(10):
    print(f"x[{i}] = {x[i]:<{col}.6f} | |erro| = {erro_abs[i]:<{col}.10f}")

# ---------------------------------------------
# 4) Curva para visualização
# ---------------------------------------------
indices = np.arange(len(x))


# =============================================================================
# 5) Analise do impacto
# =============================================================================
conclusao = '''
****************************************************************
Considerações finais:

No contexto de engenharia,tem-se que:
    -float64 (dupla precisão) é o padrão mais confiável.
    -float32 (simples precisão) introduz erro pequeno.
Contudo, o erro se acumula em operações globais especialmente em 
somatórios longos.

Portanto, em aplicações de engenharia com grande volume de dados, 
float32 só é aceitável quando há restrição de memória/desempenho, 
porém ainda com muita atenção.
O adequado é utilizar float64.
Assim, o engenheiro deve atentar para tipologia dos dados, e 
estruturação na linguam utilizada, bem como para os impactos 
numa aplicação de campo.
****************************************************************
'''
print(conclusao)

# ---------------------------------------------
# 6) Gráfico comparativo
# ---------------------------------------------
plt.figure(figsize=(10,6))
plt.plot(indices, erro_abs, label='Erro absoluto')
plt.grid(True)
plt.legend()
plt.title("Erro absoluto ponto a ponto (float64 vs float32)")
plt.xlabel("Índice do vetor")
plt.ylabel("Erro")
plt.show()

plt.figure(figsize=(10,6))
plt.plot(indices, erro_rel, label='Erro relativo')
plt.grid(True)
plt.legend()
plt.title("Erro relativo ponto a ponto (float64 vs float32)")
plt.xlabel("Índice do vetor")
plt.ylabel("Erro")
plt.show()


