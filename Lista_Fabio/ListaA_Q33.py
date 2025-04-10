# Exercício 33: Soma do número com seu inverso (3 dígitos)
numero = int(input("Número (3 dígitos): "))
inverso = int(str(numero)[::-1])
soma = numero + inverso
print(f"Soma: {numero} + {inverso} = {soma}")