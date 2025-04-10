# Exercício 35: Soma dos dígitos (4 dígitos)
numero = input("Número (4 dígitos): ")
soma = sum(int(digito) for digito in numero)
print(f"Soma dos dígitos de {numero}: {soma}")