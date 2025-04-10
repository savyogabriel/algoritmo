# Exercício 6: Conversão de km/h para m/s (Vm/s = Vkm/h / 3.6)
velocidade_kmh = float(input("Velocidade em km/h: "))
velocidade_ms = velocidade_kmh / 3.6
print(f"{velocidade_kmh} km/h = {velocidade_ms:.2f} m/s")