# Exercício 45: Distribuição ótima de notas
valor = int(input("Valor do saque (R$): "))
notas = [50, 10, 5, 1]
quantidades = {}
for nota in notas:
    quantidades[nota] = valor // nota
    valor %= nota
print("Distribuição:")
for nota, qtd in quantidades.items():
    if qtd > 0:
        print(f"{qtd} nota(s) de R${nota}")