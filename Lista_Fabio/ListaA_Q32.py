# Exercício 32: Diferença entre número e seu inverso (3 dígitos)
numero = int(input("Número (3 dígitos): "))
inverso = int(str(numero)[::-1])
diferenca = numero - inverso
print(f"Diferença: {numero} - {inverso} = {diferenca}")