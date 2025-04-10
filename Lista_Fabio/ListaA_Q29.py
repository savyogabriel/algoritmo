# Exercício 29: Meses para anos e meses
meses = int(input("Meses: "))
anos = meses // 12
meses_restantes = meses % 12
print(f"{meses} meses = {anos} anos e {meses_restantes} meses")