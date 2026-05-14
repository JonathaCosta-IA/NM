# ============================================================
# ENUNCIADO:
# f(x) = x^3 - x - 2
# - Implementar bisseção
# - Encontrar raiz em [1,2], tol = 1e-5
# - Mostrar número de iterações
# - Verificar erro final
# ============================================================

import numpy as np

# -------------------- Função --------------------
def f(x):
    return x**3 - x - 2


# -------------------- Método --------------------
def bissecao(f, a, b, tol=1e-5, max_iter=1000):
    if f(a)*f(b) > 0:
        raise ValueError("Intervalo inválido")

    for k in range(max_iter):
        c = (a + b)/2

        if abs(f(c)) < tol or (b - a)/2 < tol:
            return c, k+1, abs(f(c))

        if f(a)*f(c) < 0:
            b = c
        else:
            a = c

    return c, max_iter, abs(f(c))


# -------------------- Resultados --------------------
raiz, it, erro = bissecao(f, 1, 2)

print("Raiz:", raiz)
print("Iterações:", it)
print("Erro final:", erro)