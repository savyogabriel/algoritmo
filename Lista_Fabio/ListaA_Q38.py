# Exercício 38: Soma de frações
num1 = int(input("Numerador 1: "))
den1 = int(input("Denominador 1: "))
num2 = int(input("Numerador 2: "))
den2 = int(input("Denominador 2: "))
numerador = num1 * den2 + num2 * den1
denominador = den1 * den2
print(f"Soma: {numerador}/{denominador}")