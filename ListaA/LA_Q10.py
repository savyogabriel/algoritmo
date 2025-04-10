valorInicial = int(input("Insira o valor inicial: "))
taxaJuros = float(input("Insira a taxa de juros: "))
tempo = int(input("Insira o tempo de aplicação: "))

montante = valorInicial + (valorInicial * taxaJuros * tempo)

print("O montante final será", montante, "R$")