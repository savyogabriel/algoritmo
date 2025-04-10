numero = int(input("Insira o número de deseja inverter: "))

centena = numero // 100
dezena = (numero % 100) // 10
unidade = (numero % 100) % 10

invertido = (unidade * 100) + (dezena * 10) + centena

print(invertido)