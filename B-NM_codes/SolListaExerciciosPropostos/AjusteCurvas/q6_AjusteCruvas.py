# --------------------------------------------------------
# ENUNCIADO
# --------------------------------------------------------
# Sejam os vetores:
# x =[8, 2, 11, 5, 1, 9, 4, 12, 7, 3, 10, 6]
# y = [64, 4, 121, 25, 1, 81, 16, 144, 49, 9, 100, 36]
# - Construir o polinômio interpolador de Lagrange
# - Estimar f(2.5)
# - Analisar erro
# - Apresentar graficamente
# --------------------------------------------------------
#%%
import numpy as np
import matplotlib.pyplot as plt

def lagrange1(x, y, xp):
    '''
    Resultado DIRETO da interpolação de Lagrange, sem exibir o polinômio.
    Método de Lagrange para interpolação polinomial.
    x: vetor de pontos x
    y: vetor de pontos y correspondentes a f(x)
    xp: ponto onde queremos estimar f(xp)
    Retorna a estimativa yp, ou seja, f(xp) usando o polinômio de Lagrange.
   '''   
    n = len(x)
    yp = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if i != j:
                L *= (xp - x[j])/(x[i] - x[j])
        yp += y[i]*L
    return yp

# ---------------------------------------------
# Lagrange com exibição do polinômio p(x)
# -------------------------------------------------
def lagrange2(x, y):
    '''
    Resultado INDIRETO, via p(x)
    Método de Lagrange para interpolação polinomial.
    x: vetor de pontos x
    y: vetor de pontos y correspondentes a f(x)
    Retorna o polinômio de Lagrange p(x) como um objeto np.poly1d, 
    que pode ser avaliado em qualquer ponto.
    '''
    n = len(x)
    p = np.poly1d([0]) 
    # Criando um polinômio inicializado com zero que armazenará o resultado de todos os
    # termos do polinômio de Lagrange
    for i in range(n):
        # Criando o polinômio Li para o termo i-ésimo, que é o produto de
        # (x - x[j])/(x[i] - x[j]) para j != i
        Li = np.poly1d([1.0])
        for j in range(n):
            if i != j:
                # np.poly1d([1, -x[j]]) representa o polinômio (1*x - x[j])
                # O produto Li é atualizado multiplicando-se pelo fator 
                # (x - x[j])/(x[i] - x[j])
                Li *=  np.poly1d([1, - x[j]])  / (x[i] - x[j])
        p += y[i] * Li

    return p

def erro_absoluto(real, aprox):
    return np.abs(real - aprox)
# ---------------------------------------------
# Dados
# ---------------------------------------------
x = np.array([8, 2, 11, 5, 1, 9, 4, 12, 7, 3, 10, 6])
y = np.array([64, 4, 121, 25, 1, 81, 16, 144, 49, 9, 100, 36])

p = lagrange2(x, y)
xp = 2.5
yp = p(xp)

# valor real (considerando f(x) =x²)
real = xp**2
erro = erro_absoluto(real, yp)
# ---------------------------------------------
# Resultados
# ---------------------------------------------
print("\nPolinômio p(x):")
print(p)
print(f"f({xp}) ≈ {yp:.6f}")
print(f"Valor real = {real:.6f}")
print(f"Erro = {erro:.6e}")

# ---------------------------------------------
# Gráfico comparativo
# ---------------------------------------------
x_plot = np.linspace(x.min(), x.max())
y_plot = p(x_plot)

plt.figure()
plt.plot(x, y, 'o', label='Dados')
plt.plot(x_plot, y_plot, label='Lagrange')
plt.plot(x_plot, x_plot**2, '--', label='Real (x²)')
plt.plot(xp, yp, 'ro', label=f'Estimativa em x={xp}',markersize=12)
plt.legend()
plt.title(f'Interpolação de Lagrange - Estimativa em x={xp}')
plt.grid(True)
plt.show()


# %%
