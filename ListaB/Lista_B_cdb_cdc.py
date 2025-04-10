# Simulador de CDB e CDC (# Simulador de CDB (Investimento) e CDC (Empréstimo)
def calcular_juros_compostos(valor, taxa, tempo, anual=True):
    """Calcula juros compostos (anual ou mensal)"""
    if anual:
        return valor * (1 + taxa/100) ** tempo
    else:
        return valor * (1 + taxa/100) ** tempo

def simulador_cdb():
    print("=== SIMULADOR CDB (Investimento) ===")
    valor_investido = float(input("Valor investido (R$): "))
    taxa_anual = float(input("Taxa de juros anual (%): "))
    ano_vencimento = int(input("Ano de vencimento (ex: 2035): "))
    prazo_anos = ano_vencimento - 2025
    montante = calcular_juros_compostos(valor_investido, taxa_anual, prazo_anos)
    print(f"Valor final após {prazo_anos} anos: R${montante:.2f}")
    return valor_investido, montante

def simulador_cdc():
    print("=== SIMULADOR CDC (Empréstimo) ===")
    valor_emprestimo = float(input("Valor do empréstimo (R$): "))
    taxa_mensal = float(input("Taxa de juros mensal (%): "))
    parcelas = int(input("Número de parcelas (ex: 24, 36, 60): "))
    montante = calcular_juros_compostos(valor_emprestimo, taxa_mensal, parcelas, anual=False)
    valor_parcela = montante / parcelas
    print(f"Total a pagar: R${montante:.2f}")
    print(f"Parcelas: {parcelas}x de R${valor_parcela:.2f}")
    return valor_emprestimo, montante

def resumo_lucro_banco(cdb_investido, cdb_montante, cdc_emprestimo, cdc_montante):
    lucro = cdc_montante - cdb_montante
    print("=== RESUMO DO BANCO ===")
    print(f"Total pago ao investidor (CDB): R${cdb_montante:.2f}")
    print(f"Total recebido do cliente (CDC): R${cdc_montante:.2f}")
    print(f"Lucro do banco: R${lucro:.2f}")

# Execução
if __name__ == "__main__":
    print("===== SIMULADOR FINANCEIRO (CDB + CDC) =====")
    cdb_investido, cdb_montante = simulador_cdb()
    cdc_emprestimo, cdc_montante = simulador_cdc()
    resumo_lucro_banco(cdb_investido, cdb_montante, cdc_emprestimo, cdc_montante)