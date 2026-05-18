"""
Ajuste, pelo método dos mínimos quadrados, um modelo linear aos dados apresentados e 
determine o coeficiente de determinação R². 
Analize a qualidade do ajuste obtido.

x=[0,1,2,3,4]
y=[1.1,2,2.9,4.2,4.8]

- Produza um $novoY$ a partir da reta gerada.
- Calcule o erro quadrático total.
- Encontre o valor de y para um delta | delta está contido em x.
- Trace o gráfico com:  x por y , x por novoY. 
"""
#%%
import numpy as np
import random as rd
import matplotlib.pyplot as plt

# --------------------------------------------------------
# Cálculo do modelo
# --------------------------------------------------------
def CalcCoef(x:list, y:list):
    """
    Calcula o ajuste linear e retorna o polinômio.
    """
    p = np.poly1d(np.polyfit(x, y, 1))
    a, b = p.c   # #Exportar os coeficientes para exibição
    print("\nReta ajustada:")
    print(p)
    print(f"\nEquação:")
    print(f"y = {a:.4f}x + {b:.4f}")
    return p
# --------------------------------------------------------
# Produção de novo Y
# --------------------------------------------------------
def NovoY(x_novo, p):
    """
    Avalia p(x)
    """
    return p(x_novo)

# --------------------------------------------------------
# Gerar x dentro do domínio
# --------------------------------------------------------
def NovoX(x:list):
    """
    Gera x aleatório dentro do intervalo
    """
    x = np.array(x)
    rd.seed()
    return rd.uniform(x.min(), x.max())

# --------------------------------------------------------
# Erro quadrático + R²
# --------------------------------------------------------
def CalcErroGlobal(y_real, y_pred):

    sqr = np.sum((y_real - y_pred)**2)
    sqt = np.sum((y_real - np.mean(y_real))**2)
    r2 = 1 - sqr/sqt
    print(f"\nErro quadrático total = {sqr:.6f}")
    print(f"R² = {r2:.6f}")
    return sqr, r2


# -------------------------------------------------------
# Gráfico
# --------------------------------------------------------
def Graf(x, y, y2, p, r2, ponto=None):

    xp = np.linspace(min(x), max(x))
    titulo = f"Reta ajustada com R² = {r2:.4f}"
    plt.figure(figsize=(10,6))
    plt.plot(x, y, 'o', label='Dados')
    plt.plot(x, y2, 's', label='novoY')
    plt.plot(xp, p(xp), '-', label=f'p(x) = {str(p).replace("\n", "")}')
    if ponto is not None:
        xn, yn = ponto
        plt.plot(xn, yn, 'ro', markersize=10, label='Ponto')
    plt.title(titulo)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()


# ============================================================
# Dados
# ============================================================

x = np.array([0,1,2,3,4], dtype=float)
y = np.array([1.1,2.0,2.9,4.2,4.8], dtype=float)

# ============================================================
# Execução
# ============================================================

p = CalcCoef(x, y)

# novoY para todos os pontos
novoY = NovoY(x, p)

# ponto aleatório
delta = NovoX(x)
y_delta = NovoY(delta, p)

print(f"\nDelta = {delta:.4f}")
print(f"f({delta:.4f}) = {y_delta:.4f}")

# erros
erro, r2 = CalcErroGlobal(y, novoY)

# gráfico
Graf(x, y, novoY, p, r2, (delta, y_delta))

"""
COMENTÁRIOS

Graf(x,y,y2,coef,r2,(x_novo,y_novo))
Arranjo ponto=(x_novo,y_novo) visa apenas permitir o uso do método sem passar o par (x,y).
O que pode ser estruturado com:
Chamada: Graf(x,y,y2,coef,r2,x_novo,y_novo)
Definição: 
 def Graf(x:list,y:list,y2,coef,r2,x_novo=None,y_novo=None):
.
.
.
    if  (x_novo and  y_novo) is not None:
    ...

"""

# %%
