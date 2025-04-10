# Exercício 3: Minutos → horas e minutos
minutos_totais = int(input("Minutos: "))
horas = minutos_totais // 60
minutos = minutos_totais % 60
print(f"{minutos_totais} minutos = {horas}h {minutos}min")