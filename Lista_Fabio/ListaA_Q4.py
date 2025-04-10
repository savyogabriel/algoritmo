# Exercício 4: Conversão de dólar para real
cotacao_dolar = float(input("Cotação do dólar (R$): "))
valor_dolar = float(input("Valor em dólar (US$): "))
valor_real = valor_dolar * cotacao_dolar
print(f"US${valor_dolar} = R${valor_real:.2f}")