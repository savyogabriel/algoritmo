# Exercício 28: Horas para semanas, dias e horas
horas = int(input("Horas: "))
semanas = horas // (24 * 7)
horas %= (24 * 7)
dias = horas // 24
horas %= 24
print(f"{semanas} semanas, {dias} dias e {horas}h")