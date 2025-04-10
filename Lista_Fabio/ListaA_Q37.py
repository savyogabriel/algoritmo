# Exercício 37: Idade (dias) → anos, meses e dias
dias = int(input("Dias: "))
anos = dias // 365
dias %= 365
meses = dias // 30
dias %= 30
print(f"{anos} anos, {meses} meses e {dias} dias")