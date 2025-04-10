# Exercício 26: Dias para semanas e dias
dias = int(input("Dias: "))
semanas = dias // 7
dias_restantes = dias % 7
print(f"{dias} dias = {semanas} semanas e {dias_restantes} dias")