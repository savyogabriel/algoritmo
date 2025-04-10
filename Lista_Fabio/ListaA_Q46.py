# Exercício 46: Pagamento em entrada + 2 prestações
valor_mercadoria = float(input("Valor da mercadoria (R$): "))
prestacao = int(valor_mercadoria / 3)
entrada = valor_mercadoria - 2 * prestacao
print(f"Entrada: R${entrada:.2f} | 2x R${prestacao:.2f}")