peso = int(input("Insira seu peso: "))
altura = float(input("Insira sua altura: "))

imc = peso / altura ** 2

print(round(imc, 2))