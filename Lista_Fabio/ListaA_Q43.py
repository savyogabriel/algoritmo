# Exercício 43: Sistema de equações lineares
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
f = float(input("f: "))
x = (c*e - b*f) / (a*e - b*d)
y = (a*f - c*d) / (a*e - b*d)
print(f"x = {x:.2f}, y = {y:.2f}")