entrada = int(input("Insira os minutos que deseja converter: "))

horas = entrada // 60
minutos = entrada % 60

print(horas, "hora(s) e", minutos, "minuto(s)")