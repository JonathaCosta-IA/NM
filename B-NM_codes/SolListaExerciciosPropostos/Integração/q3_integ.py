"""
Implemente o método de Simpson 1/3, garantindo que o número de subintervalos $n$ seja par.

Utilize o método para calcular:

    \int_{0}^{2} \ln(x+1)\,dx
Compare os resultados com aqueles obtidos pelo método do trapézio composto utilizando o
mesmo número de subintervalos.

"""

import numpy as np

def trapezio_composto(f, a, b, n):
    h = (b - a) / n
    soma = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        soma += f(a + i*h)
    
    return h * soma


def simpson_13(f, a, b, n):
    ''' Método 1/3 de simpson
    '''
    
    if n % 2 != 0:
        raise ValueError("n deve ser par")
    
    h = (b - a) / n
    soma = f(a) + f(b)
    
    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * f(a + i*h)
        else:
            soma += 4 * f(a + i*h)
    
    return h * soma / 3

f = lambda x: np.log(x + 1)

# Valor exato: (x+1)ln(x+1) - x
def integral_exata(x):
    return (x+1)*np.log(x+1) - x

exato = integral_exata(2) - integral_exata(0)

n = 4
simpson = simpson_13(f, 0, 2, n)
trap = trapezio_composto(f, 0, 2, n)

col1 = 10
print(f"{'Métrica':<{col1}} | {'Valor':>{col1}}")
print("-"*(col1 * 3))
print(f"{'Simpson':<{col1}} | {simpson:>{col1}.6f}")
print(f"{'Trapézio':<{col1}} | {trap:>{col1}.6f}")
print(f"{'Exato':<{col1}} | {exato:>{col1}.6f}")



"""
FORMATAÇÃO:
    :>{col1}.6f
    : - definição da formatação
    >{col1} - total de digitos
    .6f - total de casas decimas
    .3e - formato 10³
"""

