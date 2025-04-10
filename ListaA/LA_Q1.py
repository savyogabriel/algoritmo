nota_1 = int(input("Insira nota 1: "))
peso_1 = int(input("Insira peso 1: "))

nota_2 = int(input("Insira nota 2: "))
peso_2 = int(input("Insira peso 2: "))

nota_3 = int(input("Insira nota 3: "))
peso_3 = int(input("Insira peso 3: "))

media_ponderada = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / (peso_1 + peso_2 + peso_3)

print("A média ponderada das três notas é:", media_ponderada)