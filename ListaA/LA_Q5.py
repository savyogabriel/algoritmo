valor = int(input("Insira o valor recebido: "))

notas50 = valor // 50
notas10 = (valor % 50) // 10

print(notas50, "nota(s) de 50 e", notas10, "nota(s) de 10")