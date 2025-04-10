# Exercício 30: Minutos para dias, horas e minutos
minutos = int(input("Minutos: "))
dias = minutos // (24 * 60)
minutos %= (24 * 60)
horas = minutos // 60
minutos %= 60
print(f"{dias}d {horas}h {minutos}min")