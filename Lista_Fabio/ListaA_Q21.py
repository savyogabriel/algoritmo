# Exercício 21: Converter °F para °C (t°C = (5 * t°F - 160) / 9)
fahrenheit = float(input("Temperatura em °F: "))
celsius = (5 * fahrenheit - 160) / 9
print(f"{fahrenheit}°F = {celsius:.2f}°C")