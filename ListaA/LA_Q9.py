precoInicial = int(input("Insira o preço inicial: "))
desconto = int(input("Insira o desconto a ser aplicado: "))

precoFinal = precoInicial - (precoInicial * (desconto/100))

print("O preço final será:", precoFinal)