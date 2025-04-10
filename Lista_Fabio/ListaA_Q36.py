# Exercício 36: Idade (anos, meses, dias) → dias
anos = int(input("Anos: "))
meses = int(input("Meses: "))
dias = int(input("Dias: "))
total_dias = anos * 365 + meses * 30 + dias
print(f"Idade em dias: {total_dias}")