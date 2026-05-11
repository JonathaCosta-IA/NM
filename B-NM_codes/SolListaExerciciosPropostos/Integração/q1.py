def trapezio_simples(f, a, b):
    return (b - a) * (f(a) + f(b)) / 2

# Função
f = lambda x: x**2 + 1

# Cálculo
aprox = trapezio_simples(f, 0, 2)

# Valor exato: ∫(x²+1)dx = x³/3 + x
exato = (2**3)/3 + 2
erro = abs(exato - aprox)


col1 = 15
col2 = 15

print("\nQ1:")

print(f"{'Métrica':<{col1}} | {'Valor':>{col2}}")
print("-"*(col1 + col2 + 3))

print(f"{'Aproximação':<{col1}} | {aprox:>{col2}.6f}")
print(f"{'Exato':<{col1}} | {exato:>{col2}.6f}")
print(f"{'Erro':<{col1}} | {erro:>{col2}.6e}")