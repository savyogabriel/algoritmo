# Exercício 39: Cálculo de expressão (R + S)
a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
r = (a + b) ** 2
s = (b + c) ** 2 / 2
d = r + s
print(f"D = R + S = {d:.2f}")