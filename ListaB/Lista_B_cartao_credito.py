# Simulador de Cartão de Crédito (# Simulador de Fatura de Cartão de Crédito (Rotativo)
def calcular_fatura_com_juros(valor_fatura, meses_sem_pagar):
    juros_rotativo = 0.12  # 12% ao mês
    multa_atraso = 0.02    # 2%
    juros_mora = 0.01       # 1%
    total_juros = juros_rotativo + multa_atraso + juros_mora
    valor_corrigido = valor_fatura * (1 + total_juros) ** meses_sem_pagar
    return valor_corrigido

def simulador_cartao():
    print("=== SIMULADOR DE FATURA DE CARTÃO ===")
    valor_fatura = float(input("Valor total da fatura (R$): "))
    p1 = float(input("Valor do Plano P1 (R$): "))
    p2 = float(input("Valor do Plano P2 (R$): "))
    meses = int(input("Meses sem pagar: "))

    # Cenário 1: Pagamento parcial P1
    saldo_devedor_p1 = valor_fatura - p1
    fatura_final_p1 = calcular_fatura_com_juros(saldo_devedor_p1, meses)

    # Cenário 2: Pagamento parcial P2
    saldo_devedor_p2 = valor_fatura - p2
    fatura_final_p2 = calcular_fatura_com_juros(saldo_devedor_p2, meses)

    # Resultados
    print("=== RESULTADOS ===")
    print(f"Valor original da fatura: R${valor_fatura:.2f}")
    print(f"Cenário P1 ({p1:.2f}):")
    print(f"Fatura após {meses} meses: R${fatura_final_p1:.2f} (+{(fatura_final_p1/valor_fatura - 1)*100:.2f}%)")
    print(f"Cenário P2 ({p2:.2f}):")
    print(f"Fatura após {meses} meses: R${fatura_final_p2:.2f} (+{(fatura_final_p2/valor_fatura - 1)*100:.2f}%)")

if __name__ == "__main__":
    simulador_cartao()