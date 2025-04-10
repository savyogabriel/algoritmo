# Exercício 40: Custo do fumante
anos_fumando = int(input("Anos fumando: "))
cigarros_por_dia = int(input("Cigarros por dia: "))
preco_carteira = float(input("Preço da carteira (20 cigarros): "))
total_cigarros = anos_fumando * 365 * cigarros_por_dia
total_carteiras = total_cigarros / 20
gasto_total = total_carteiras * preco_carteira
print(f"Gasto total: R${gasto_total:.2f}")