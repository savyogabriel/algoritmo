# Exercício 41: Custo do carro ao consumidor
custo_fabrica = float(input("Custo de fábrica: "))
percent_distribuidor = 0.28
impostos = 0.45
custo_consumidor = custo_fabrica * (1 + percent_distribuidor + impostos)
print(f"Custo ao consumidor: R${custo_consumidor:.2f}")