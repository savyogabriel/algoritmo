# Simulador de Viagem (# Simulador de Viagem com Carro Híbrido (BYD)
def calcular_consumo(distancia, percentual_eletrico, km_l_alcool=10, km_l_gasolina=12):
    distancia_combustao = distancia * (1 - percentual_eletrico/100)
    litros_alcool = distancia_combustao / km_l_alcool
    litros_gasolina = distancia_combustao / km_l_gasolina
    return litros_alcool, litros_gasolina

def simulador_viagem():
    print("=== SIMULADOR DE VIAGEM (BYD) ===")
    distancia = float(input("Distância total da viagem (km): "))
    percentual_eletrico = float(input("Percentual com motor elétrico (%): "))
    preco_alcool = float(input("Preço do álcool (R$/L): "))
    preco_gasolina = float(input("Preço da gasolina (R$/L): "))

    litros_alcool, litros_gasolina = calcular_consumo(distancia, percentual_eletrico)
    custo_alcool = litros_alcool * preco_alcool
    custo_gasolina = litros_gasolina * preco_gasolina

    print("=== TABELA COMPARATIVA ===")
    print(f"Distância com combustão: {distancia * (1 - percentual_eletrico/100):.2f} km")
    print(f"ÁLCOOL: {litros_alcool:.2f}L (R${custo_alcool:.2f})")
    print(f"GASOLINA: {litros_gasolina:.2f}L (R${custo_gasolina:.2f})")

if __name__ == "__main__":
    simulador_viagem()