# Exercício 20: Converter °C para °F (t°F = (9 * t°C + 160) / 5)
celsius = float(input("Temperatura em °C: "))
fahrenheit = (9 * celsius + 160) / 5
print(f"{celsius}°C = {fahrenheit}°F")