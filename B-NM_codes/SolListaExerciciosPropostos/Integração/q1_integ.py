"""
Implemente um \textit{script} que realize a aproximação da integral definida 
utilizando o método do trapézio simples.

Aplique a função para calcular:

    ∫(x²+1)dx
Determine também o erro absoluto em relação ao valor analítico da integral.

"""


def trapezio_simples(f, a, b):
    '''
    Método do trapézio simples
    '''
    return (b - a) * (f(a) + f(b)) / 2

# Função
fx = lambda x: x**2 + 1

# Cálculo de fx no intervalo [0,2]
aprox = trapezio_simples(fx, 0, 2)

# Valor exato: ∫(x²+1)dx = x³/3 + x
exato = (2**3)/3 + 2
erro = abs(exato - aprox)

col1 = 15
print(f"{'Métrica':<{col1}} | {'Valor':>{col1}}")
print("-"*(col1 * 3))
print(f"{'Aproximação':<{col1}} | {aprox:>{col1}.6f}")
print(f"{'Exato':<{col1}} | {exato:>{col1}.6f}")
print(f"{'Erro':<{col1}} | {erro:>{col1}.6e}")