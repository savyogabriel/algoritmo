# Exercício 5: Soma dos dígitos (C + D + U)
numero = int(input("Número (3 dígitos): "))
centena = numero // 100
dezena = (numero % 100) // 10
unidade = numero % 10
soma = centena + dezena + unidade
print(f"Soma dos dígitos de {numero}: {soma}")